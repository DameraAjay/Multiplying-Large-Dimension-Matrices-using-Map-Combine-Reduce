import sys

current_row = None;
current_mat = None;
current_col = None;
current_val = 0;
current_k = None;

a_row = list()
e_col = list()
# a_row[:50] = [0]*50
# e_col[:50] = [0]*50
for line in sys.stdin:
	line = line.strip()
	row,k,mat,col,val= line.split(' ')

	if mat == 'E':
		if len(e_col) == 0:
			a_row.append(current_val)
			current_row = None;
			current_mat = None;
			current_col = None;
			current_val = 0;
			current_k = None
		e_col.append(float(val))
		if len(e_col) == 50:
			value = 0
			for i in range(0,50):
				value += float(a_row[i]) * float(e_col[i])
			print(row,",",k,",",value)
			a_row[:50] = [0]*50
			e_col[:50] = [0]*50
			a_row.clear()
			e_col.clear()
	elif mat == 'A':
		if row == current_row and k == current_k and col == current_col:
			current_val = current_val + float(val)
		else:
			if current_row != None:
				a_row.append(current_val)
			current_val = float(val)
			current_mat = 'A'
			current_row = row
			current_col = col
			current_k = k

