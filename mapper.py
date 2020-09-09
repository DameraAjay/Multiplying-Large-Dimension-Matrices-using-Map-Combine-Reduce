import sys

if __name__ == '__main__':
	filename = sys.argv[1]
	file = open(filename,'r')
	data = file.readlines()
	for i in data:
		mat,row,col,val = i.split(',')
		if val[len(val)-1] == '\n': 
			val = val[:len(val)-1]
		if mat == 'A' or mat == 'D':
			for i in range(1,51):
				print("%02d %02d %s %02d %.15f"%(int(row),i,'A',int(col),float(val)))
		elif mat == 'B' or mat == 'C':
			for i in range(1,51):
				print("%02d %02d %s %02d %.15f"%(int(row),i,'A',int(col),-1*float(val)))
		elif mat == 'E':
			for i in range(1,51):
				print("%02d %02d %s %02d %.15f"%((i,int(col),'E',int(row),float(val))))
