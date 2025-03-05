from design.plone.opendata import _
from plone.restapi.controlpanels import RegistryConfigletPanel
from plone.schema.email import Email

# from zope import schema
from zope.component import adapter
from zope.interface import Interface


class IControlPanel(Interface):
    org_email = Email(
        title=_("Email Organizzazione"),
        required=True,
    )


@adapter(Interface, Interface)
class ControlPanel(RegistryConfigletPanel):
    schema = IControlPanel
    # schema_prefix = "ploneconf"
    configlet_id = "opendata-controlpanel"
    configlet_category_id = "Products"
    title = "Opendata Settings"
    group = "Products"
