d=[{"ID":1,"NAME":"DOY","ROLL":1,"ENGLISH":50,"MATHS":60},{"ID":2,"NAME":"HANRY","ROLL":2,"ENGLISH":75,"MATHS":78},{"ID":3,"NAME":"KIRA","ROLL":3,"ENGLISH":85,"MATHS":96},{"ID":4,"NAME":"LEORIA","ROLL":4,"ENGLISH":68,"MATHS":69},{"ID":5,"NAME":"PRIOA","ROLL":5,"ENGLISH":96,"MATHS":75}]
print(d)
for i in d:
	if int(i["MATHS"])>80:
		print("Name:-",i["NAME"])
		print("Roll:-",i["ROLL"])
