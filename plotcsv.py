import csv
import matplotlib.pyplot as plt
import datetime

data = {}
with open("my_test.csv","r") as csvfile :
	reader = csv.reader(csvfile);
	for row in reader :
		if row[0][0] == '#' :
			continue
		ts = row[0].replace(" PST","-08:00").replace(" PDT","-07:00")
		dt = datetime.datetime.fromisoformat(ts)
		if dt in data.keys() :
			raise Exception("date/time '%s' duplicated" % row[0])
		data[dt] = float(row[1])

plt.figure(1)
plt.plot(data.keys(),data.values())
plt.savefig("my_test.png")