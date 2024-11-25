frappe.ui.form.on("Patient", "onload", function(frm) {
    frm.set_query("sex", function() {
        return {
            filters:{
                'hco_code': ['!=', '']
            }
        }
    });
});