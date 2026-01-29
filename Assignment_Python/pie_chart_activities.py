import matplotlib.pyplot as p
act=['Sleeping', 'Eating', 'Working', 'Playing']
h=[8, 2, 10, 4]
p.pie(h, labels=act, autopct='%1.1f%%')
p.title("Daily Activities")
p.show()

