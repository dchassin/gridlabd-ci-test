import csv
import matplotlib.pyplot as plt
import datetime

start = datetime.datetime(2019,1,1,0,0,0,tzinfo=datetime.timezone(datetime.timedelta(hours=-8),"PST"))
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
		if dt >= start :
			data[dt] = float(row[1])

plt.figure(1)
plt.plot(data.keys(),data.values())
plt.savefig("my_test.png")
