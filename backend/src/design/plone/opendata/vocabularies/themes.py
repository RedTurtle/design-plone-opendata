from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


# Vocabolario TEMI
# 1. Agricoltura, pesca, silvicoltura e prodotti alimentari
# In questo tema rientra tutto ciò che riguarda il settore agricoltura, pesca, politiche forestali e alimentari. URI da
# utilizzare : http://publications.europa.eu/resource/authority/data-theme/AGRI
# 2. Economia e Finanze
# In questo tema rientra tutto ciò che riguarda la tassazione, l’industria, il manifatturiero, il bilancio dello stato, la crescita
# economica, il commercio. URI da utilizzare: http://publications.europa.eu/resource/authority/data-theme/ECON
# 3. Istruzione, cultura e sport
# In questo tema rientra tutto ciò che riguarda la cultura, il turismo, l’istruzione e le attività sportive, eventi culturali e
# locali. URI da utilizzare: http://publications.europa.eu/resource/authority/data-theme/EDUC
# 4. Energia
# In questo tema rientra tutto ciò che concerne il settore dell’energia e dell’estrazione mineraria. URI da utilizzare:
# http://publications.europa.eu/resource/authority/data-theme/ENER
# 5. Ambiente
# In questo tema rientra tutto ciò che riguarda l’ambiente (rifiuti, consumo del suolo, oceani, ecc.) e il clima/meteo.
# URI da utilizzare: http://publications.europa.eu/resource/authority/data-theme/ENVI
# 6. Governo e settore pubblico
# In questo tema rientra tutto ciò che riguarda le politiche di governo, gli affari istituzionali, la trasparenza del settore
# pubblico (dati relativi ad amministrazione trasparente). URI da utilizzare: http://publications.europa.eu/resource/
# authority/data-theme/GOVE
# 7. Salute
# In questo tema rientra tutto ciò che concerne le attività sulla salute e tutto ciò che riguarda gli animali. URI da
# utilizzare: http://publications.europa.eu/resource/authority/data-theme/HEAL
# Capitolo 1.Agenzia per l'Italia Digitaledatipubblici - linee guida cataloghi dati, Release 1.0
# 8. Tematiche internazionali
# In questo tema rientra tutto ciò che concerne le relazioni internazionali, la cooperazione internazionale, i diritti uma
# nitari, le organizzazioni internazionali e gli affari esteri. URI da utilizzare: http://publications.europa.eu/resource/
# authority/data-theme/INTR
# 9. Giustizia, sistema giuridico e sicurezza pubblica
# In questo tema rientra tutto ciò che riguarda le frodi, i crimini, la giustizia, le norme. Rientra anche tutto ciò che
# riguarda la difesa e gli aspetti legati alle attività del ministero dell’interno. URI da utilizzare: http://publications.
# europa.eu/resource/authority/data-theme/JUST
# 10. Regioni e città
# In questo tema rientra tutto ciò che riguarda le strade urbane e i numeri civici. Il tema ha una forte sovrapposizione
# con ambiente perché potrebbe anche contenere tutto ciò che concerne la geografia del territorio (e.g., montagne, laghi,
# fiumi, ecc.). URI da utilizzare: http://publications.europa.eu/resource/authority/data-theme/REGI
# 11. Popolazione e società
# In questo tema rientra tutto ciò che concerne lo sviluppo della società, le condizioni della società, la cittadinanza, la
# demografia, il welfare. URI da utilizzare: http://publications.europa.eu/resource/authority/data-theme/SOCI
# 12. Scienza e tecnologia
# In questo tema rientra tutto ciò che riguarda la ricerca, l’innovazione, la tecnologia, la banda larga e ultralarga, la psi
# cologia, le scienze umane, lo spazio. URI da utilizzare: http://publications.europa.eu/resource/authority/data-theme/
# TECH
# 13. Trasporti
# In questo tema rientra tutto ciò che riguarda i trasporti e le relative infrastrutture, la mobilità. URI da utilizzare:
# http://publications.europa.eu/resource/authority/data-theme/TRAN


@provider(IVocabularyFactory)
class DataThemesVocabulary:
    def __call__(self, context):
        terms = [
            SimpleTerm(
                value="http://publications.europa.eu/resource/authority/data-theme/AGRI",
                title="Agricoltura, pesca, silvicoltura e prodotti alimentari",
            ),
            SimpleTerm(
                value="http://publications.europa.eu/resource/authority/data-theme/ECON",
                title="Economia e Finanze",
            ),
            SimpleTerm(
                value="http://publications.europa.eu/resource/authority/data-theme/EDUC",
                title="Istruzione, cultura e sport",
            ),
            SimpleTerm(
                value="http://publications.europa.eu/resource/authority/data-theme/ENER",
                title="Energia",
            ),
            SimpleTerm(
                value="http://publications.europa.eu/resource/authority/data-theme/ENVI",
                title="Ambiente",
            ),
            SimpleTerm(
                value="http://publications.europa.eu/resource/authority/data-theme/GOVE",
                title="Governo e settore pubblico",
            ),
            SimpleTerm(
                value="http://publications.europa.eu/resource/authority/data-theme/HEAL",
                title="Salute",
            ),
            SimpleTerm(
                value="http://publications.europa.eu/resource/authority/data-theme/INTR",
                title="Tematiche internazionali",
            ),
            SimpleTerm(
                value="http://publications.europa.eu/resource/authority/data-theme/JUST",
                title="Giustizia, sistema giuridico e sicurezza pubblica",
            ),
            SimpleTerm(
                value="http://publications.europa.eu/resource/authority/data-theme/REGI",
                title="Regioni e città",
            ),
            SimpleTerm(
                value="http://publications.europa.eu/resource/authority/data-theme/SOCI",
                title="Popolazione e società",
            ),
            SimpleTerm(
                value="http://publications.europa.eu/resource/authority/data-theme/TECH",
                title="Scienza e tecnologia",
            ),
            SimpleTerm(
                value="http://publications.europa.eu/resource/authority/data-theme/TRAN",
                title="Trasporti",
            ),
        ]
        return SimpleVocabulary(terms)
