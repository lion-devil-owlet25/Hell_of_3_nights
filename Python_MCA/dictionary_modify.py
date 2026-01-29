d=[{"ID":1,"NAME":"DOY","ROLL":1,"ENGLISH":50,"MATHS":60,"Status":0},{"ID":2,"NAME":"HANRY","ROLL":2,"ENGLISH":75,"MATHS":78,"Status":0},{"ID":3,"NAME":"KIRA","ROLL":3,"ENGLISH":85,"MATHS":96,"Status":0},{"ID":4,"NAME":"LEORIA","ROLL":4,"ENGLISH":68,"MATHS":69,"Status":0},{"ID":5,"NAME":"PRIOA","ROLL":5,"ENGLISH":96,"MATHS":75,"Status":0}]
avg=0
for i in d:
	avg=(int(i["MATHS"])+int(i["ENGLISH"]))/2
	i["AVERAGE"]=avg
	if (avg>60):
		i["Status"]="PASS"
	else:
		i["Status"]="FAIL"
print(d)
