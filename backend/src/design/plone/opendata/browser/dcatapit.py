from datetime import datetime
from plone import api
from plone.namedfile.browser import Download
from Products.Five import BrowserView

# from rdflib import ConjunctiveGraph
from rdflib import BNode
from rdflib import Graph
from rdflib import Literal
from rdflib import Namespace
from rdflib import URIRef
from zope.interface import implementer
from zope.interface import Interface
from zope.publisher.interfaces import IPublishTraverse

import io


# from zope.publisher.interfaces import NotFound


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

    # def _getFile(self):
    def __call__(self):
        portal = api.portal.get()
        lang = portal.Language()

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
        g.add((org_node, RDF.type, VCARD.Organization))

        # TODO: mettere nel controlpanel degli opendata
        g.add((org_node, VCARD.hasEmail, URIRef("mailto:test@example.org")))
        g.add((org_node, VCARD.fn, Literal(f"Redazione OpenData {portal.Title()}")))

        catalog_uri = URIRef(portal.absolute_url())
        g.add((catalog_uri, RDF.type, DCATAPIT.Catalog))

        # TODO: mettere nel controlpanel degli opendata
        g.add(
            (catalog_uri, DCT.title, Literal(f"Opendata {portal.Title()}", lang=lang))
        )
        g.add(
            (
                catalog_uri,
                DCT.description,
                Literal(f"Opendata {portal.Title()}", lang=lang),
            )
        )

        # modified del catalogo andrebbe calcolato alla modifica dei metadati nel controlpanel, dell'oggetto o dei dataset ?
        # temporaneamente mettiamo now()
        g.add(
            (
                catalog_uri,
                DCT.modified,
                Literal(datetime.now().isoformat(), datatype=XSD.dateTime),
            )
        )

        # TODO: mettere nel controlpanel degli opendata
        publisher_uri = URIRef(f"{portal.absolute_url()}#opendata")
        g.add((catalog_uri, DCT.publisher, publisher_uri))
        g.add((publisher_uri, RDF.type, DCATAPIT.Agent))
        g.add(
            (
                publisher_uri,
                FOAF.name,
                Literal(f"Redazione OpendData {portal.Title()}", lang=lang),
            )
        )
        g.add(
            (
                publisher_uri,
                DCT.identifier,
                Literal(f"{portal.absolute_url()}#opendata"),
            )
        )

        for brain in brains:
            obj = brain.getObject()
            lang = obj.Language()
            # dataset_uri = URIRef(f"{catalog_uri}/dataset/{record['ID']}")
            dataset_uri = URIRef(obj.absolute_url())
            g.add((catalog_uri, DCAT.dataset, dataset_uri))
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
                g.add((dataset_uri, DCAT.theme, URIRef(theme)))

            if obj.rightsHolder:
                holder = obj.rightsHolder[0].to_object
                if holder:
                    # agent_node = BNode()
                    holder_uri = URIRef(holder.absolute_url())
                    g.add((dataset_uri, DCT.rightsHolder, holder_uri))
                    g.add((holder_uri, RDF.type, DCATAPIT.Agent))
                    g.add((holder_uri, FOAF.name, Literal(holder.Title(), lang=lang)))
                    g.add((holder_uri, DCT.identifier, Literal(holder.absolute_url())))

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
                # TODO: qui andrebbe messo il filename, anzichè "file", serve la getObject per recuperarlo ?
                g.add(
                    (
                        distribution_uri,
                        DCAT.accessURL,
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
                g.add((distribution_uri, DCT.license, Literal(obj.license)))

            # for keyword in record['Keywords'].split(","):
            #     g.add((dataset_uri, DCAT.keyword, Literal(keyword.strip())))

        #     dataset_uri = URIRef(obj.absolute_url())
        #     g.add((dataset_uri, DCT.title, Literal(obj.Title())))
        #     g.add((dataset_uri, DCT.issued, Literal(record['PubDate'])))
        #     g.add((dataset_uri, DCAT.theme, Literal(record['Theme'])))

        # Salva l'RDF in un file
        out = io.BytesIO()
        g.serialize(destination=out, format="pretty-xml")
        data = out.getvalue()
        self.request.response.setHeader("Content-Length", len(data))
        self.request.RESPONSE.setHeader("Content-Type", "application/rdf+xml")
        # self.request.response.setHeader(
        #         "Content-Disposition",
        #         "attachment; filename=users.xlsx",
        # )
        return data
