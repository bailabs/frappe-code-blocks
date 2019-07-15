# Usage:
# ---------------
# if data:
#     _fill_rows_total(data)


def _fill_rows_total(data):
    compute_fields = [
        'material_issue',
        'direct_cost',
        'labour',
        'central_labour',
        'central_expenses',
        'indirect_expenses',
        'overhead_charges'
    ]

    for row in data:
        row['total'] = sum([row.get(field) for field in compute_fields])
