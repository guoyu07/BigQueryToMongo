import sys
from pymongo import MongoClient

# Args and init
if (len(sys.argv) < 3):
	print "Usage: insert.py <input> <collection>"
	sys.exit()

inp_path = sys.argv[1]
coll_name = sys.argv[2]
f_in = open(sys.argv[1], "r")
coll = MongoClient().local[coll_name]
print "Importing into 'local.%s' ... " % coll_name

# Read headers on first line
fline = f_in.readline()
fline = fline.rstrip()
headers = fline.split(',')

# Read values and insert
for line in f_in:
	obj = dict()
	line = line.rstrip()
	vs = line.split(',')
	for (i, v) in enumerate(vs):
		obj[headers[i]] = v
	coll.insert(obj)

f_in.close()
print "Import successful!"