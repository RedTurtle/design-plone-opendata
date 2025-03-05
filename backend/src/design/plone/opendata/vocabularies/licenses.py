from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


# import csv

# https://github.com/italia/daf-ontologie-vocabolari-controllati/blob/master/VocabolariControllati/licences/licences.csv

# LICENSES_CSV = """code_level_1,label_level_1,code_level_2,label_level_2,code_level_3,label_level_3
# A,Licenza Aperta,A.1,Dominio pubblico,A.1.1,Creative Commons CC0 1.0 Universal - Public Domain Dedication (CC0 1.0)
# A,Licenza Aperta,A.1,Dominio pubblico,A.1.2,ODC Public Domain Dedication and License (PDDL)
# A,Licenza Aperta,A.2,Attribuzione,A.2.1,Creative Commons Attribution 4.0 International (CC BY 4.0)
# A,Licenza Aperta,A.2,Attribuzione,A.2.2,Creative Commons Attribution 3.0 Unported (CC BY 3.0)
# A,Licenza Aperta,A.2,Attribuzione,A.2.3,Creative Commons Attribuzione Italia 3.0 (CC BY 3.0 IT)
# A,Licenza Aperta,A.2,Attribuzione,A.2.4,Creative Commons Attribution 2.5 Generic (CC BY 2.5)
# A,Licenza Aperta,A.2,Attribuzione,A.2.5,Creative Commons Attribuzione 2.5 Italia (CC BY 2.5 IT)
# A,Licenza Aperta,A.2,Attribuzione,A.2.6,Creative Commons Attribution 2.0 Generic (CC BY 2.0)
# A,Licenza Aperta,A.2,Attribuzione,A.2.7,Creative Commons Attribuzione 2.0 Italia (CC BY 2.0 IT)
# A,Licenza Aperta,A.2,Attribuzione,A.2.8,Creative Commons Attribution 1.0 Generic (CC BY 1.0)
# A,Licenza Aperta,A.2,Attribuzione,A.2.9,Italian Open Data License 2.0 (IODL 2.0)
# A,Licenza Aperta,A.2,Attribuzione,A.2.10,Open Data Commons Attribution License (ODC_BY)
# A,Licenza Aperta,A.3,Effetto Virale (a.k.a. Condivisione allo stesso modo),A.3.1,Creative Commons Attributon–ShareAlike 4.0 International (CC BY-SA 4.0)
# A,Licenza Aperta,A.3,Effetto Virale (a.k.a. Condivisione allo stesso modo),A.3.2,Creative Commons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)
# A,Licenza Aperta,A.3,Effetto Virale (a.k.a. Condivisione allo stesso modo),A.3.3,Creative Commons Attribuzione - Condividi allo stesso modo 3.0 Italia (CC BY-SA 3.0 IT)
# A,Licenza Aperta,A.3,Effetto Virale (a.k.a. Condivisione allo stesso modo),A.3.4,Creative Commons Attribution-ShareAlike 2.5 Generic (CC BY-SA 2.5)
# A,Licenza Aperta,A.3,Effetto Virale (a.k.a. Condivisione allo stesso modo),A.3.5,Creative Commons Attribuzione - Condividi allo stesso modo 2.5 Italia (CC-BY-SA 2.5 IT)
# A,Licenza Aperta,A.3,Effetto Virale (a.k.a. Condivisione allo stesso modo),A.3.6,Creative Commons Attribution-ShareAlike 2.0 Generic (CC BY-SA 2.0)
# A,Licenza Aperta,A.3,Effetto Virale (a.k.a. Condivisione allo stesso modo),A.3.7,Creative Commons Attribuzione - Condividi allo stesso modo 2.0 Italia (CC BY-SA 2.0 IT)
# A,Licenza Aperta,A.3,Effetto Virale (a.k.a. Condivisione allo stesso modo),A.3.8,Creative Commons Attribution - ShareAlike 1.0 Generic (CC BY-SA 1.0)
# A,Licenza Aperta,A.3,Effetto Virale (a.k.a. Condivisione allo stesso modo),A.3.9,Italian Open Data License 1.0 (IODL 1.0)
# A,Licenza Aperta,A.3,Effetto Virale (a.k.a. Condivisione allo stesso modo),A.3.10,Open Data Commons Open Database License 1.0 (ODbL)
# A,Licenza Aperta,A.3,Effetto Virale (a.k.a. Condivisione allo stesso modo),A.3.11,GNU Free Documentation License 1.3 (GFDL 1.3)
# A,Licenza Aperta,A.4,Effetto Virale / copyleft non compatibile ,A.4.1,Against DRM (2.0)
# B,Licenza Non Aperta,B.1,Solo uso non commerciale,B.1.1,Creative Commons Attribution–NonCommercial 4.0 International (CC BY-NC 4.0)
# B,Licenza Non Aperta,B.1,Solo uso non commerciale,B.1.2,Creative Commons Attribution-NonCommercial 3.0 Unported (CC BY-NC 3.0)
# B,Licenza Non Aperta,B.1,Solo uso non commerciale,B.1.3,Creative Commons Attribuzione - Non Commerciale 3.0 Italia (CC BY-NC 3.0 IT)
# B,Licenza Non Aperta,B.1,Solo uso non commerciale,B.1.4,Creative Commons Attribution-NonCommercial 2.5 Generic (CC BY-NC 2.5)
# B,Licenza Non Aperta,B.1,Solo uso non commerciale,B.1.5,Creative Commons Attribuzione - Non Commerciale 2.5 Italia (CC BY-NC 2.5 IT)
# B,Licenza Non Aperta,B.1,Solo uso non commerciale,B.1.6,Creative Commons Attribution-NonCommercial 2.0 Generic (CC BY-NC 2.0)
# B,Licenza Non Aperta,B.1,Solo uso non commerciale,B.1.7,Creative Commons Attribuzione - Non Commerciale 2.0 Italia (CC BY-NC 2.0 IT)
# B,Licenza Non Aperta,B.1,Solo uso non commerciale,B.1.8,Creative Commons Attribution - NonCommercial 1.0 Generic (CC BY-NC 1.0)
# B,Licenza Non Aperta,B.1,Solo uso non commerciale,B.1.9,Creative Commons Attribution–NonCommercial - ShareAlike 4.0 International (CC BY-NC-SA 4.0)
# B,Licenza Non Aperta,B.1,Solo uso non commerciale,B.1.10,Creative Commons Attribution-NonCommercial - ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)
# B,Licenza Non Aperta,B.1,Solo uso non commerciale,B.1.11,Creative Commons Attribuzione–Non Commerciale - Condivisione allo stesso modo 3.0 Italia (CC BY-NC-SA 3.0 IT)
# B,Licenza Non Aperta,B.1,Solo uso non commerciale,B.1.12,Creative Commons Attribution-NonCommercial-ShareAlike 2.5 Generic (CC BY-NC-SA 2.5)
# B,Licenza Non Aperta,B.1,Solo uso non commerciale,B.1.13,Creative Commons Attribuzione–Non Commerciale - Condivisione allo stesso modo 2.5 Italia (CC BY-NC-SA 2.5 IT)
# B,Licenza Non Aperta,B.1,Solo uso non commerciale,B.1.14,Creative Commons Attribution-NonCommercial-ShareAlike 2.0 Generic (CC BY-NC-SA 2.0)
# B,Licenza Non Aperta,B.1,Solo uso non commerciale,B.1.15,Creative Commons Attribuzione–Non Commerciale - Condivisione allo stesso modo 2.0 Italia (CC BY-NC-SA 2.0 IT)
# B,Licenza Non Aperta,B.1,Solo uso non commerciale,B.1.16,Creative Commons Attribution–NonCommercial - ShareAlike 1.0 Generic (CC-BY-NC-SA 1.0)
# B,Licenza Non Aperta,B.1,Solo uso non commerciale,B.1.17,Dichiarazioni di uso standard beni culturali (BCS)
# B,Licenza Non Aperta,B.2,Non opere derivate,B.2.1,Creative Commons Attribution–NoDerivs 4.0 International (CC BY-ND 4.0)
# B,Licenza Non Aperta,B.2,Non opere derivate,B.2.2,Creative Commons Attribution-NoDerivs 3.0 Unported (CC BY-ND 3.0)
# B,Licenza Non Aperta,B.2,Non opere derivate,B.2.3,Creative Commons Attribuzione–Non opere derivate 3.0 Italia (CC BY-ND 3.0 IT)
# B,Licenza Non Aperta,B.2,Non opere derivate,B.2.4,Creative Commons Attribution-NoDerivs 2.5 Generic (CC BY-ND 2.5)
# B,Licenza Non Aperta,B.2,Non opere derivate,B.2.5,Creative Commons Attribution–Non opere derivate 2.5 Italia (CC BY-ND 2.5 IT)
# B,Licenza Non Aperta,B.2,Non opere derivate,B.2.6,Creative Commons Attribution-NoDerivs 2.0 Generic (CC BY-ND 2.0)
# B,Licenza Non Aperta,B.2,Non opere derivate,B.2.7,Creative Commons Attribution–Non opere derivate 2.0 italia (CC BY-ND 2.0 IT)
# B,Licenza Non Aperta,B.2,Non opere derivate,B.2.8,Creative Commons Attribution–NonDerivs 1.0 Generic (CC BY-ND 1.0)
# B,Licenza Non Aperta,B.2,Non opere derivate,B.2.9,Creative Commons Attribution–NoDerivs-NonCommercial 1.0 Generic (CC BY-ND-NC 1.0)
# C,Licenza sconosciuta,C.1,Licenza sconosciuta,C.1.1,Licenza Sconosciuta"""

# XXX: dda tutte le licenze possibili al momento prendiamo solo le più utilizzate
LICENSES_DICT = {
    "https://creativecommons.org/licenses/by/4.0/": "Creative Commons Attribution 4.0 International (CC BY 4.0)",
    "https://www.dati.gov.it/content/italian-open-data-license-v20": "Italian Open  Data License 2.0 (IODL 2.0)",
    # "A.3.9": "Italian Open Data License 1.0 (IODL 1.0)",
    # "B.1.1": "Creative Commons Attribution–NonCommercial 4.0 International (CC BY-NC 4.0)",
    # "B.2.1": "Creative Commons Attribution–NoDerivs 4.0 International (CC BY-ND 4.0)",
    # "C.1.1": "Licenza Sconosciuta",
}

# <dct:license>
#   <dct:LicenseDocument rdf:about="https://www.dati.gov.it/content/italian-open-data-license-v20">
#     <owl:versionInfo>2.0</owl:versionInfo>
#     <foaf:name xml:lang="en">Italian Open Data License 2.0 (IODL 2.0)</foaf:name>
#     <foaf:name xml:lang="de">Italienische Open Data Lizenz 2.0 (IODL 2.0)</foaf:name>
#     <rdf:type rdf:resource="http://dati.gov.it/onto/dcatapit#LicenseDocument"/>
#     <dct:type rdf:resource="http://purl.org/adms/licencetype/Attribution"/>
#     <foaf:name xml:lang="it">Italian Open Data License 2.0 (IODL 2.0)</foaf:name>
#     <foaf:name xml:lang="fr">Italian Open Data License 2.0 (IODL 2.0)</foaf:name>
#   </dct:LicenseDocument>
# </dct:license>


@provider(IVocabularyFactory)
class LicensesVocabulary:
    def __call__(self, context):

        terms = [
            SimpleTerm(value=key, title=label) for (key, label) in LICENSES_DICT.items()
        ]
        return SimpleVocabulary(terms)
