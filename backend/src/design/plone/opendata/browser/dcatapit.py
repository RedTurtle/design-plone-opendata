from datetime import datetime
from design.plone.opendata import logger
from design.plone.opendata.controlpanel.opendata import IControlPanel
from plone import api
from plone.namedfile.browser import Download
from Products.Five import BrowserView
from rdflib import BNode
from rdflib import Graph
from rdflib import Literal
from rdflib import Namespace
from rdflib import URIRef
from zope.component import getUtility
from zope.interface import implementer
from zope.interface import Interface
from zope.publisher.interfaces import IPublishTraverse
from zope.publisher.interfaces import NotFound
from zope.schema.interfaces import IVocabularyFactory

import io


# Namespace RDF
FOAF = Namespace("http://xmlns.com/foaf/0.1/")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
LOCN = Namespace("http://www.w3.org/ns/locn#")
HYDRA = Namespace("http://www.w3.org/ns/hydra/core#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
DCAT = Namespace("http://www.w3.org/ns/dcat#")
DCT = Namespace("http://purl.org/dc/terms/")
DCATAPIT = Namespace("http://dati.gov.it/onto/dcatapit#")
VCARD = Namespace("http://www.w3.org/2006/vcard/ns#")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")


class IRDFView(Interface):
    """marker interface"""


@implementer(IRDFView)
class RDFView(BrowserView):
    """"""

    def __call__(self):
        return

    def absolute_url(self):
        """
        Needed for plone.namedfile >= 6.4.0 with canonical header
        """
        return f"{self.context.absolute_url()}/{self.__name__}"


# https://github.com/ckan/ckanext-dcat/blob/master/ckanext/dcat/processors.py

# TODO: spostare sul controlpanel ?
FORMAT = {
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "Excel XLSX",
    "application/vnd.oasis.opendocument.text": "ODT",
    "text/csv": "CSV",
}


# definire un behavior per i file dataset che implementa questo metodo
def format_from_mime_type(mime_type):
    return FORMAT.get(mime_type, "UNKNOWN")


@implementer(IPublishTraverse)
class RDFDownload(Download):
    # def __init__(self, context, request):
    format = None
    mime_type = None

    def publishTraverse(self, request, name):
        super().publishTraverse(request=request, name=name)
        if name == "rdf.xml":
            self.format = "pretty-xml"
            self.mime_type = "application/rdf+xml"
        else:
            logger.errror("RDF format %s not implemented", name)
            raise NotFound(self, name, self.request)
        return self

    # def _getFile(self):
    def __call__(self):
        portal = api.portal.get()
        lang = portal.Language()
        theme_vocabulary = getUtility(
            IVocabularyFactory, "design.plone.opendata.themes"
        )(portal)
        g = Graph()
        # g = ConjunctiveGraph()
        g.bind("foaf", FOAF)
        g.bind("owl", OWL)
        g.bind("skos", SKOS)
        g.bind("locn", LOCN)
        g.bind("hydra", HYDRA)
        g.bind("rdf", RDF)
        g.bind("dcat", DCAT)
        g.bind("dct", DCT)
        g.bind("dcatapit", DCATAPIT)
        g.bind("vcard", VCARD)
        g.bind("xsd", XSD)
        # records = sheet.get_all_records()
        catalog = api.portal.get_tool("portal_catalog")
        brains = catalog(portal_type="OpendataDataset")

        # <vcard:Organization rdf:nodeID="Nefb041d7de8243f9a2d8cf8e9c5eadd8">
        #     <vcard:hasEmail rdf:resource="mailto:redazioneopendatacopertino@gmail.com"/>
        #     <vcard:fn>Redazione OD</vcard:fn>
        # </vcard:Organization>

        # Creazione nodo Organization
        org_node = BNode()  # Nodo anonimo
        # g.add((org_node, RDF.type, VCARD.Organization))
        g.add((org_node, RDF.type, DCATAPIT.Organization))

        org_email = api.portal.get_registry_record(
            interface=IControlPanel, name="org_email", default=None
        )
        if org_email:
            g.add((org_node, VCARD.hasEmail, URIRef(org_email)))
        org_title = api.portal.get_registry_record(
            interface=IControlPanel, name="org_title", default=None
        )
        if org_title:
            g.add((org_node, VCARD.fn, Literal(org_title)))

        catalog_node = BNode()
        g.add((catalog_node, RDF.type, DCATAPIT.Catalog))

        catalog_title = api.portal.get_registry_record(
            interface=IControlPanel, name="catalog_title", default=None
        )
        if catalog_title:
            g.add((catalog_node, DCT.title, Literal(catalog_title)))
        catalog_description = api.portal.get_registry_record(
            interface=IControlPanel, name="catalog_description", default=None
        )
        if catalog_description:
            catalog_description = catalog_description.replace("\n", " ")
            g.add((catalog_node, DCT.description, Literal(catalog_description)))
        catalog_homepage = api.portal.get_registry_record(
            interface=IControlPanel, name="catalog_homepage", default=None
        )
        if catalog_homepage:
            g.add((catalog_node, FOAF.homepage, Literal(catalog_homepage)))
        if lang == "it":
            g.add(
                (
                    catalog_node,
                    DCT.language,
                    URIRef(
                        "http://publications.europa.eu/resource/authority/language/ITA"
                    ),
                )
            )
        elif lang == "en":
            g.add(
                (
                    catalog_node,
                    DCT.language,
                    URIRef(
                        "http://publications.europa.eu/resource/authority/language/ENG"
                    ),
                )
            )
        catalog_issued = api.portal.get_registry_record(
            interface=IControlPanel, name="catalog_issued", default=None
        )
        if catalog_issued:
            g.add(
                (
                    catalog_node,
                    DCT.issued,
                    Literal(catalog_issued.isoformat(), datatype=XSD.date),
                )
            )

        theme_taxonomy_uri = URIRef(
            "http://publications.europa.eu/resource/authority/data-theme"
        )
        g.add((catalog_node, DCAT.themeTaxonomy, theme_taxonomy_uri))
        g.add((theme_taxonomy_uri, RDF.type, SKOS.ConceptScheme))
        g.add((theme_taxonomy_uri, DCT.title, Literal("Vocabulary Theme")))

        # TODO: modified del catalogo andrebbe calcolato alla modifica dei metadati nel controlpanel, dell'oggetto o dei dataset ?
        #       temporaneamente mettiamo now()
        g.add(
            (
                catalog_node,
                DCT.modified,
                Literal(datetime.now().isoformat(), datatype=XSD.dateTime),
            )
        )

        publisher_node = BNode()
        g.add((catalog_node, DCT.publisher, publisher_node))
        g.add((publisher_node, RDF.type, DCATAPIT.Agent))
        g.add(
            (
                publisher_node,
                DCT.identifier,
                Literal(f"{portal.absolute_url()}#publisher"),
            )
        )
        publisher_title = api.portal.get_registry_record(
            interface=IControlPanel, name="publisher_title", default=None
        )
        if publisher_title:
            g.add(
                (
                    publisher_node,
                    FOAF.name,
                    Literal(publisher_title),
                )
            )

        for brain in brains:
            obj = brain.getObject()
            lang = obj.Language()
            # dataset_uri = URIRef(f"{catalog_uri}/dataset/{record['ID']}")
            dataset_uri = URIRef(obj.absolute_url())
            g.add((catalog_node, DCAT.dataset, dataset_uri))
            g.add((dataset_uri, RDF.type, DCATAPIT.Dataset))
            g.add((dataset_uri, DCT.identifier, Literal(brain.getURL())))

            # XXX: verificare il formato iso delle date usato da CKAN
            g.add(
                (
                    dataset_uri,
                    DCT.modified,
                    Literal(
                        brain.modified.asdatetime().isoformat(), datatype=XSD.dateTime
                    ),
                )
            )
            g.add((dataset_uri, DCT.accrualPeriodicity, Literal(obj.frequency)))

            g.add((dataset_uri, DCT.title, Literal(obj.Title(), lang=lang)))
            # g.add((dataset_uri, DCT.issued, Literal(record['PubDate'], datatype=XSD.dateTime)))
            g.add((dataset_uri, DCT.description, Literal(obj.Description(), lang=lang)))
            for theme in obj.themes:
                theme_uri = URIRef(theme)
                g.add((dataset_uri, DCAT.theme, theme_uri))
                # TODO: potrebbero anche essere aggiunti tutti all'inizio
                # g.add((catalog_node, SKOS.Concept, theme_uri))
                g.add((theme_uri, RDF.type, SKOS.Concept))
                term = theme_vocabulary.getTerm(theme)
                # TODO: valutare le traduzioni
                g.add((theme_uri, SKOS.prefLabel, Literal(term.title, lang=lang)))
            if obj.rightsHolder:
                holder_obj = obj.rightsHolder[0].to_object
                if holder_obj:
                    # agent_node = BNode()
                    holder_uri = URIRef(holder_obj.absolute_url())
                    g.add((dataset_uri, DCT.rightsHolder, holder_uri))
                    g.add((holder_uri, RDF.type, DCATAPIT.Agent))
                    g.add(
                        (holder_uri, FOAF.name, Literal(holder_obj.Title(), lang=lang))
                    )
                    g.add(
                        (holder_uri, DCT.identifier, Literal(holder_obj.absolute_url()))
                    )

            # XXX: in questi casi prendiamo dati generali, valutare se metterli anche specifici
            g.add((dataset_uri, DCAT.contactPoint, org_node))
            g.add((dataset_uri, DCT.publisher, publisher_node))

            # location_node = BNode()
            # g.add((dataset_uri, DCT.spatial, location_node))
            # g.add((location_node, RDF.type, DCT.Location))
            # g.add((location_node, DCATAPIT.geographicalIdentifier, URIRef("https://www.geonames.org/6538969")))

            # g.add((dataset_uri, DCT.accrualPeriodicity, URIRef("http://publications.europa.eu/resource/authority/frequency/CONT")))
            # g.add((dataset_uri, DCT.language, URIRef("http://publications.europa.eu/resource/authority/language/ITA")))
            # g.add((dataset_uri, DCT.modified, Literal(record['ModifiedDate'], datatype=XSD.dateTime)))
            # g.add((dataset_uri, DCAT.landingPage, URIRef(f"{catalog_uri}/dataset/{record['ID']}")))

            for file_brain in catalog(path=brain.getPath(), portal_type="File"):
                distribution_uri = URIRef(file_brain.getURL())

                g.add((dataset_uri, DCAT.distribution, distribution_uri))
                g.add((distribution_uri, RDF.type, DCATAPIT.Distribution))
                g.add((distribution_uri, DCT.identifier, Literal(file_brain.getURL())))
                g.add((distribution_uri, DCT.description, Literal(file_brain.Title)))
                g.add(
                    (
                        distribution_uri,
                        DCAT.accessURL,
                        # TODO: qui andrebbe messo il filename, anzichè "file", serve la getObject per recuperarlo ?
                        URIRef(f"{file_brain.getURL()}/@@download/file"),
                    )
                )
                g.add(
                    (
                        distribution_uri,
                        DCT.term("format"),
                        Literal(format_from_mime_type(file_brain.mime_type)),
                    )
                )
                # XXX: per semplicità la licenza è definita nel dataset e non nei singoli file
                # TODO: le licenze potrebbero essere definite una volta sola, poi referenziate qui
                if obj.license == "https://creativecommons.org/licenses/by/4.0/":
                    license_document_uri = URIRef(obj.license)
                    g.add(
                        (
                            license_document_uri,
                            RDF.type,
                            URIRef("http://dati.gov.it/onto/dcatapit#LicenseDocument"),
                        )
                    )
                    g.add(
                        (
                            license_document_uri,
                            DCT.type,
                            URIRef("http://purl.org/adms/licencetype/Attribution"),
                        )
                    )
                    g.add(
                        (
                            license_document_uri,
                            FOAF.name,
                            Literal(
                                "Creative Commons Attribuzione 4.0 Internazionale (CC BY 4.0)",
                                lang="it",
                            ),
                        )
                    )
                    g.add((license_document_uri, OWL.versionInfo, Literal("4.0")))
                elif (
                    obj.license
                    == "https://www.dati.gov.it/content/italian-open-data-license-v20"
                ):
                    license_document_uri = URIRef(obj.license)
                    g.add(
                        (
                            license_document_uri,
                            RDF.type,
                            URIRef("http://purl.org/dc/terms/LicenseDocument"),
                        )
                    )
                    g.add(
                        (
                            license_document_uri,
                            DCT.type,
                            URIRef("http://purl.org/adms/licencetype/Attribution"),
                        )
                    )
                    g.add(
                        (
                            license_document_uri,
                            FOAF.name,
                            Literal(
                                "Italian Open  Data License 2.0 (IODL 2.0)", lang="it"
                            ),
                        )
                    )
                    g.add((license_document_uri, OWL.versionInfo, Literal("4.0")))
                else:
                    license_document_uri = None
                if license_document_uri:
                    license_node = license_document_uri
                    g.add((distribution_uri, DCT.license, license_node))
                    g.add(
                        (license_node, DCATAPIT.LicenseDocument, license_document_uri)
                    )

                # XXX: per semplicità usiamo il rghtsHolder del dataset
                g.add((distribution_uri, DCAT.contactPoint, holder_uri))

            # for keyword in record['Keywords'].split(","):
            #     g.add((dataset_uri, DCAT.keyword, Literal(keyword.strip())))

        #     dataset_uri = URIRef(obj.absolute_url())
        #     g.add((dataset_uri, DCT.title, Literal(obj.Title())))
        #     g.add((dataset_uri, DCT.issued, Literal(record['PubDate'])))
        #     g.add((dataset_uri, DCAT.theme, Literal(record['Theme'])))

        # Salva l'RDF in un file
        out = io.BytesIO()
        g.serialize(destination=out, format=self.format)
        data = out.getvalue()
        self.request.response.setHeader("Content-Length", len(data))
        self.request.RESPONSE.setHeader("Content-Type", self.mime_type)
        # self.request.response.setHeader(
        #         "Content-Disposition",
        #         "attachment; filename=users.xlsx",
        # )
        return data
