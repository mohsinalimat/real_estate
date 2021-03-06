// Copyright (c) 2016, Aerele Technologies Private Limited and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["collection report"] = {
	"filters": [
		{
			fieldname: "from_date",
			label: __("From Date"),
			fieldtype: "Date"
		},
		{
			fieldname:"to_date",
			label: __("To Date"),
			fieldtype: "Date",
			default: frappe.datetime.now_date(true)
		},
		{
			fieldname:"user",
			label: __("User"),
			fieldtype: "Link",
			options: "User",
		},
		{
			fieldname:"site_name",
			label: __("Site_name"),
			fieldtype: "Link",
			options : "Site Booking"
		}


	]
};
