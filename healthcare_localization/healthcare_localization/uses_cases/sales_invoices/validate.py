from var_dump import var_dump 
import frappe
from frappe import _
from electronic_invoicing_colombia.electronic_invoicing_colombia.service.setup.sales_invoices.get_setup import get_is_not_electronic_invoice_resolution

@frappe.whitelist()
def validate_rips(si_doc):
    # TODO: Programar lógica
    sales_invoices = frappe.get_doc("Sales Invoice", si_doc)

    # Si es factura electrónica y ya está validada y está activa factura rips y no está la factura validada por el ministerio aún
    if not get_is_not_electronic_invoice_resolution(sales_invoices) and sales_invoice.docstatus == 1 and sales_invoices.hco_rips and not sales_invoices.hco_validated:

        frappe.msgprint(msg=_("POR PROGRAMAR: Inicia el proceso de validar en el ministerio..."), title=_("Validar RIPS"), indicator="green")

    else:
        frappe.msgprint(msg=_("No se envía la petición..."), title=_("Validar RIPS"), indicator="orange")
