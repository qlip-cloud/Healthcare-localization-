import frappe
import json

from healthcare_localization.healthcare_localization.exception import sales_invoices_exception

from electronic_invoicing_colombia.electronic_invoicing_colombia.service.setup.sales_invoices.get_setup  \
    import get_is_not_electronic_invoice_resolution


def handle(sales_invoice):

    transaction_node = {}

    user_list = []

    # ------------------------------- ELIMINAR AL TERMINAR --------------------------------

    transaction_node = get_transaction_info(sales_invoice)

    users_json = get_users_info(sales_invoice.customer, sales_invoice.patient, 1)

    user_list.append(users_json)

    transaction_node["Usuarios"] = user_list

    # ---------------------------------------------------------------------------------

    # TODO: IDENTAR A MEDIDA QUE SE PROGRAME LUEGO DESCOMENTAR PARA PROBAR EL PROCESO
    # if not get_is_not_electronic_invoice_resolution(sales_invoice):

        # # Transacción

        # transaction_node = get_transaction_info(sales_invoice)

    #     # Usuarios
    #     get_users_info(sales_invoice.customer, sales_invoice.patient, 1)

    #     # servicio

    #     __assert_has_service_info(sales_invoice)

    #     # consultas

    #     __assert_has_medical_consultation_info(sales_invoice)

    #     # procedimientos
        
    #     __assert_has_medical_procedure_info(sales_invoice)

    #     # No aplica: urgencias

    #     # hospitalizacion

    #     __assert_has_hospitalization_info(sales_invoice)

    #     # No palica: recienNacidos

    #     # medicamentos

    #     __assert_has_medicines_info(sales_invoice)

    #     # otrosServicios

    #     __assert_has_other_services_info(sales_invoice)

    print("transaction_node", transaction_node)
    print("res json -->>", json.dumps(transaction_node))

    return json.dumps(transaction_node)


def get_transaction_info(sales_invoice):
    """
    numDocumentoIdObligado
    numFactura
    TipoNota
    numNota
    """

    res = {}

    tax_id_company = frappe.db.get_value("Company", sales_invoice.company , "tax_id")

    if not tax_id_company:
        sales_invoices_exception.tax_id_company_exception()

    res["numDocumentoIdObligado"] = tax_id_company

    res["numFactura"] = sales_invoice.name

    if  sales_invoice.is_return or sales_invoice.is_debit_note:

        # TODO: Cómo determinar lo siguiente:
        # Cuando el ajuste en los RIPS esté relacionado con el valor monetario de un
        # dato en RIPS se debe utilizar nota crédito o nota débito según corresponda.
        # Por su parte, en aquellos casos cuando el ajuste no esté relacionado con el
        # valor monetario, se debe - utilizar la nota ajuste RIPS.
        # NA nota ajuste RIPS.
        # NC nota crédito
        # ND nota débito

        res["tipoNota"] = "ND" if sales_invoice.is_debit_note else "NC"
        res["numNota"] = sales_invoice.return_against

    else:
        res["tipoNota"] = None
        res["numNota"] = None


    return res


def get_users_info(si_customer, si_patient, idx):
    """
    tipoDocumentoIdentificacion
    numDocumentoIdentificacion
    tipoUsuario
    fechaNacimiento
    codSexo
    codPaisResidencia
    codMunicipioResidencia
    codZonaTerritorialResidencia
    incapacidad
    consecutivo
    codPaisOrigen
    """
    # TODO: Determinar cuando es más de un usuario que se debe reportar
    # Confirmar si los datos vienen del campo patient asociado a la factura

    # Se incluye validaciones menos en: codMunicipioResidencia y codZonaTerritorialResidencia

    tax_id_customer = frappe.db.get_value("Customer", si_customer, "tax_id")
    if not tax_id_customer:
        sales_invoices_exception.tax_id_customer_exception()

    if not si_patient:
        sales_invoices_exception.patient_sales_invoice_exception()

    patient_doc = frappe.get_doc("Patient", si_patient)
    patient_validation(patient_doc)

    hco_code = frappe.db.get_value("Gender", patient_doc.sex, "hco_code")
    if not hco_code:
        sales_invoices_exception.hco_code_gender_exception()

    iso_residence_country = frappe.db.get_value("Country", patient_doc.hco_residence_country, "hco_iso_numeric_code")
    if not iso_residence_country:
        sales_invoices_exception.hco_iso_residence_country_exception()

    iso_birth_country = frappe.db.get_value("Country", patient_doc.hco_birth_country, "hco_iso_numeric_code")
    if not iso_birth_country:
        sales_invoices_exception.hco_iso_birth_country_exception()

    res = {}    

    res["tipoDocumentoIdentificacion"] = patient_doc.hco_health_document_type
    res["numDocumentoIdentificacion"] = patient_doc.eico_nvben_ndoc
    res["tipoUsuario"] = patient_doc.hco_user_type
    res["fechaNacimiento"] = "{}".format(patient_doc.dob)
    res["codSexo"] = hco_code
    res["codPaisResidencia"] = iso_residence_country
    res["codMunicipioResidencia"] = patient_doc.hco_residence_municipality or None
    res["codZonaTerritorialResidencia"] = patient_doc.hco_territorial_zone or None
    res["incapacidad"] = "patient-encounter --> hco_inability"
    res["consecutivo"] = idx
    res["codPaisOrigen"] = iso_birth_country

    return res


def patient_validation(patient_doc):

    if not patient_doc.hco_residence_country:
        sales_invoices_exception.patient_empty_field_exception("Residence Country")

    if not patient_doc.hco_birth_country:
        sales_invoices_exception.patient_empty_field_exception("Birth Country")

    if not patient_doc.hco_health_document_type:
        sales_invoices_exception.patient_empty_field_exception("Health Document Type")

    if not patient_doc.eico_nvben_ndoc:
        sales_invoices_exception.patient_empty_field_exception("Document number")

    if not patient_doc.hco_user_type:
        sales_invoices_exception.patient_empty_field_exception("User Type")

    if not patient_doc.dob:
        sales_invoices_exception.patient_empty_field_exception("dob")

    if not patient_doc.sex:
        sales_invoices_exception.patient_empty_field_exception("sex")

@frappe.whitelist()
def get_data_third_party(customer):

    third_party_country = ""

    if customer:

        customer_tax_id = frappe.db.get_value("Customer", customer, "tax_id")

        if customer_tax_id:

            search ={
                "tax_id": customer_tax_id
            }

            third_party_country = frappe.db.get_value('qp_CO_ThirdParty', search, "country")

    return {"third_party_country": third_party_country}
