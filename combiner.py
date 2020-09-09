import sys

current_row = None;
current_mat = None;
current_col = None;
current_val = 0;
current_k = None;

for line in sys.stdin:
	line = line.strip()
	row,k,mat,col,val= line.split(' ')
	if mat == 'E':
		if current_row != None:
			print("%02d %02d %s %02d %.15f"%(int(current_row),int(current_k),current_mat,int(current_col),float(current_val)))
		print("%02d %02d %s %02d %.15f"%(int(row),int(k),mat,int(col),float(val)))
		current_row = None;
		current_mat = None;
		current_col = None;
		current_val = 0;
		current_k = None;
	elif current_k == k and current_row == row and current_mat == mat and current_col == col:
		current_val = float(current_val) + float(val)
	else:
		if current_row != None:
			print("%02d %02d %s %02d %.15f"%(int(current_row),int(current_k),current_mat,int(current_col),float(current_val)))
		current_val = val
		current_col = col
		current_mat = mat
		current_k = k
		current_row = row
if current_mat != 'E' and current_row != None:
	print("%02d %02d %s %02d %.15f"%(int(current_row),int(current_k),current_mat,int(current_col),float(current_val)))