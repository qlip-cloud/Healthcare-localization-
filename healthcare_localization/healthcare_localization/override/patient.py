import frappe
from erpnext.healthcare.doctype.patient.patient import Patient

class HealthcarePatient(Patient):
    def add_as_website_user(self):
        # Se omite la creación de usuario si registran correo electrónico

        return