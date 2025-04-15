list1 = ['Masale Dose','Idly','Set Dose','Rava dose','Upma','Khali Dose','Pongal']

dose_list = []
for item in list1:
	if 'dose' in item.lower():
		dose_list.append(item)

print(dose_list)
# ['Masale Dose', 'Set Dose', 'Rava Dose', 'Khali Dose']


