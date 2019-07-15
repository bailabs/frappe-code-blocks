# Usage
# ------------------
# if data:
#     _fill_Totals(data)


def _fill_totals(data):
	total_row = {
		'normal_hours': 0,
		'normal_cost': 0.00,
		'ot1_hours': 0,
		'ot1': 0.00,
		'ot2_hours': 0,
		'ot2': 0.00,
		'absent_hours': 0,
		'absent': 0.00,
		'total': 0.00
	}

	for row in data:
		for key, value in total_row.items():
			total_row[key] = value + row[key]

	data.append(total_row)