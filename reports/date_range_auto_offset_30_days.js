frappe.query_reports["Timesheet Summary"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_days(frappe.datetime.get_today(), -30)
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"on_change": function(query_report) {
				const to_date = query_report.get_filter_value("to_date");
				const from_date = frappe.datetime.add_days(to_date, -30);
				query_report.set_filter_value("from_date", from_date);
			}
		}
	]
}