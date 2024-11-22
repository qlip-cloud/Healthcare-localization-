from . import __version__ as app_version

app_name = "healthcare_localization"
app_title = "Healthcare Localization"
app_publisher = "Aryrosa Fuentes"
app_description = "Doctypes and customizations for Healthcare Localization"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "aryrosa.fuentes@MENTUM.group"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/healthcare_localization/css/healthcare_localization.css"
# app_include_js = "/assets/healthcare_localization/js/healthcare_localization.js"

# include js, css files in header of web template
# web_include_css = "/assets/healthcare_localization/css/healthcare_localization.css"
# web_include_js = "/assets/healthcare_localization/js/healthcare_localization.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "healthcare_localization/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

doctype_js = {
    "Sales Invoice" : "public/js/sales_invoice.js",
	"Company" : "public/js/company.js",
	"Patient" : "public/js/patient.js"
}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "healthcare_localization.install.before_install"
# after_install = "healthcare_localization.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "healthcare_localization.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {

    "Gender": {
        "validate": ["healthcare_localization.healthcare_localization.uses_cases.gender.validation.handle"]
    }
}


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"healthcare_localization.tasks.all"
# 	],
# 	"daily": [
# 		"healthcare_localization.tasks.daily"
# 	],
# 	"hourly": [
# 		"healthcare_localization.tasks.hourly"
# 	],
# 	"weekly": [
# 		"healthcare_localization.tasks.weekly"
# 	]
# 	"monthly": [
# 		"healthcare_localization.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "healthcare_localization.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "healthcare_localization.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "healthcare_localization.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"healthcare_localization.auth.validate"
# ]

fixtures = [
    {"doctype": "qp_HCO_Operator"},
	{"doctype": "Gender", "filters": [
        [
            "name", "in", [
                "Hombre",
                "Mujer",
				"Indeterminado o Intersexual"
            ]
        ]
    ]}
]

