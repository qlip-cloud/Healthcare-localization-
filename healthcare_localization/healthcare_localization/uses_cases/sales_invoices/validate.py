from var_dump import var_dump 
import frappe
from frappe import _
from electronic_invoicing_colombia.electronic_invoicing_colombia.service.setup.sales_invoices.get_setup import get_is_not_electronic_invoice_resolution
# from electronic_invoicing_colombia.electronic_invoicing_colombia.utils.constant import DOCMEN, DOCMENLOCALHOST, SALES_INV_DT, PURCHASE_INV_DT, REJECTED
# from electronic_invoicing_colombia.electronic_invoicing_colombia.service.setup.sales_invoices.get_setup import handle as get_setup_by_sales_invoice, get_is_not_electronic_invoice_resolution
# from electronic_invoicing_colombia.electronic_invoicing_colombia.service.documenteme.send_option import handle as send_validate_documenteme
# from electronic_invoicing_colombia.electronic_invoicing_colombia.service.pdf.setup import handle as send_pdf_documenteme
# from electronic_invoicing_colombia.electronic_invoicing_colombia.uses_cases.sales_invoices.validation import handle as document_validation

@frappe.whitelist()
def validate_rips(si_doc):

    sales_invoices = frappe.get_doc("Sales Invoice", si_doc)

    # Si es factura electrónica y ya está validada y está activa factura rips y no está la factura validada por el ministerio aún
    if not get_is_not_electronic_invoice_resolution(sales_invoices) and sales_invoice.docstatus == 1 and sales_invoices.hco_rips and not sales_invoices.hco_validated:

        frappe.msgprint(msg=_("Inicia el proceso..."), title=_("Validar RIPS"), indicator="green")

        # # Se traslada validaciones al submit
        # document_validation(sales_invoices)

        # enviroment, invoice_resolution, thrid_party, print_format, company, return_sales_invoice, list_detail_tax, details, discounts = get_setup_by_sales_invoice(sales_invoices)

        # json_data, transform_format =  __prepare_json_transaction(enviroment, sales_invoices, invoice_resolution, print_format, 
        # thrid_party, company, return_sales_invoice, list_detail_tax, details, discounts)
                
        # var_dump(json_data)

        # transaction, transaction_special = send_validate_documenteme(json_data, enviroment, sales_invoices, transform_format.name, transform_format.send_pdf, company)
        # #refactoriza
        
        # __finish_transaction(transaction, sales_invoices, print_format, transform_format, enviroment, transaction_special=transaction_special)
    else:
        frappe.msgprint(msg=_("No se envía la petición..."), title=_("Validar RIPS"), indicator="orange")

# def __finish_transaction(transaction, sales_invoices, print_format, transform_format, enviroment, is_new = False, transaction_special = None):

#     try:

#         __verify_is_success(transaction, sales_invoices)

#         __insert_transactions(transform_format, transaction, transaction_special)

#         # Garantizar hacer commit de todo el proceso si el resultado es exitoso
#         frappe.db.commit()

#         __asign_transsaction_sales_invoice(transaction, sales_invoices)

#         # TODO: Coordinar para hacer pruebas controladas del consumo del servicio
#         # TODO: evaluar proceso tomando en cuenta el caso de hacer commit de las transacciones al final.
#         # FV DS - send_pdf_documenteme
#         send_pdf_to_documenteme = transaction.send_pdf if transaction_special else transform_format.send_pdf
#         if sales_invoices.doctype == SALES_INV_DT and send_pdf_to_documenteme:
#             send_pdf_documenteme(print_format, sales_invoices, transform_format, transaction, enviroment)

#     except eico_DocumentemeError as error_SendDocumenteme:

#         frappe.db.rollback()

#         __insert_transactions(transform_format, transaction, transaction_special)

#         frappe.db.commit()

#         if transaction.response == REJECTED:

#             dian_mess = _("The DIAN is currently experiencing connection issues, please wait a few minutes and try again.")

#             frappe.throw(dian_mess)

#         else:

#             frappe.throw(error_SendDocumenteme.message)

#     except Exception as ex:

#         frappe.throw(ex.args)

# def __prepare_json_transaction(enviroment, sales_invoices, invoice_resolution, print_format, thrid_party, company,
#                             return_sales_invoice = None, list_detail_tax = None, details= None, discounts = None):

#     transform_format = frappe.new_doc('qp_EICO_TransformFormat')

#     transform_format.init(sales_invoices, thrid_party, invoice_resolution, company, return_sales_invoice, list_detail_tax, details, discounts, print_format)

#     # Se hace el insert al final del proceso

#     return transform_format.get_json(enviroment.operator_code), transform_format

# def __verify_is_success(transaction, sales_invoices):

#     if not transaction.is_success():

#         raise eico_DocumentemeError(message=transaction.description)

# def __asign_transsaction_sales_invoice(transaction, sales_invoices):

#     sales_old = frappe.get_doc(sales_invoices.doctype, sales_invoices.name)

#     sales_invoices.eico_transaction = sales_old.eico_transaction

#     if sales_invoices.doctype == SALES_INV_DT:

#         sales_invoices.eico_transaction_pdf = sales_old.eico_transaction_pdf

#         sales_invoices.eico_transaction_acuse = sales_old.eico_transaction_acuse

#     # FV DS - eico_cude / eico_cufe
#     if sales_invoices.doctype == PURCHASE_INV_DT:
#         sales_invoices.eico_cude =  transaction.response_cufe
#     else:
#         sales_invoices.eico_cufe =  transaction.response_cufe

#     sales_invoices.eico_qr = transaction.response_qrcode

# def __insert_transactions(transform_format, transaction, transaction_special):

#     transform_format.insert(ignore_permissions=True)

#     transaction.json_request = transform_format.get("name")

#     transaction.insert(ignore_permissions=True)

#     if transaction_special:

#         transaction_special.insert(ignore_permissions=True)


# class eico_DocumentemeError(Exception):

#     def __init__(self, message="Documenteme Error"):
#         self.message = message
#         super().__init__(self.message)
