from frappe.utils.data import date_diff


def get_day_diff(filters):
    return date_diff(
        filters.get('to_date'),
        filters.get('from_date')
    )
