import datetime

def csvtopng(csvname,pngname=None,col=1,start=None,stop=None) :
	import csv
	import matplotlib.pyplot as plt

	data = {}
	name = None
	if type(start) == str :
		start = datetime.datetime.strptime(start,"%Y-%m-%d %H:%M:%S %Z")
	if type(stop) == str :
		stop = datetime.datetime.strptime(stop,"%Y-%m-%d %H:%M:%S %Z")
	with open("my_test.csv","r") as csvfile :
		reader = csv.reader(csvfile);
		for row in reader :
			if row[0][0] == '#' :
				if len(row) > col :
					name = row[col]
				continue
			dt = datetime.datetime.strptime(row[0][0:19],"%Y-%m-%d %H:%M:%S")
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
	csvtopng("my_test.csv",start="2019-01-01 00:00:00 PST",stop="2019-01-02 00:00:00 PST")