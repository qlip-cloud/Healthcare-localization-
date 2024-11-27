from frappe import _, throw

def tax_id_company_exception():

	throw(_("Tax ID in Company not found"))

def country_third_party_exception():

	throw(_("Country in third party not found"))

def iso_numeric_code_country_exception():

	throw(_("ISO numeric code in Country not found"))

def tax_id_customer_exception():

	throw(_("Tax ID in Customer not found"))

def hco_code_gender_exception():

	throw(_("Code in Gender not found"))

def patient_sales_invoice_exception():

	throw(_("Patient in Sales Invoice not found"))

def patient_empty_field_exception(field_param):

	throw("{} {}".format(_(field_param), _("in Patient not found")))
