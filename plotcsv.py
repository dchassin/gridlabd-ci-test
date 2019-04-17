import datetime

def csvtopng(csvname,pngname=None,col=1,start=None,stop=None) :
	import csv
	import matplotlib.pyplot as plt

	data = {}
	name = None
	with open("my_test.csv","r") as csvfile :
		reader = csv.reader(csvfile);
		for row in reader :
			if row[0][0] == '#' :
				if len(row) > col :
					name = row[col]
				continue
			ts = row[0].replace(" PST","-08:00").replace(" PDT","-07:00")
			dt = datetime.datetime.fromisoformat(ts)
			if dt in data.keys() :
				raise Exception("date/time '%s' duplicated" % row[0])
			if ( start == None or dt >= start ) and ( stop == None or dt <= stop ) :
				data[dt] = float(row[col].split(" ")[0])

	plt.figure(1)
	plt.plot(data.keys(),data.values())
	if name != None :
		plt.ylabel(name.split("[")[0].replace("_"," ").title())
	plt.xlabel("Date/Time")
	plt.grid()
	plt.savefig("my_test.png")

if __name__ == '__main__':
	start = datetime.datetime(2019,1,1,0,0,0,tzinfo=datetime.timezone(datetime.timedelta(hours=-8),"PST"))
	stop = datetime.datetime(2019,1,2,0,0,0,tzinfo=datetime.timezone(datetime.timedelta(hours=-8),"PST"))
	csvtopng("my_test.csv",start=start,stop=stop)