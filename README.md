# Multiplying-Large-Dimension-Matrices-using-Map-Combine-Reduce
Multiplying large dimension matrices using map combine reduce framework
### The Matrix operation expression is:
	- (D-B-C+A) × E
	- Each with dimension(50 x 50)
	- In above Expression  first we need to add D,A and subtract B and C from that then multuply with E

# In mapper:
	- For every element in Matrices A and D I have generated
		- (A i j value) ==> (i k A j value) 	[where k is from 1-50]
		- (D i j value) ==> (i k A j value)		[where k is from 1-50]
		- I have replaced D with A
	- For every element in Matrices B and C I have generated
		- (B i j value) ==> (i k A j (-1*value))		[where k is from 1-50]
		- (C i j value) ==> (i k A j (-1*value))		[where k is from 1-50]
		- I have replaced B and C with A
		- From given expression it is clear that we need to subtract B and C for this I have multiplied with -1
	- For every element in Matrix E I have generated
		- (E i j value) ==> (k j E i value )	[where k is from 1-50]
# In combiner:
	- For Every element belongs to E no need to modify anything
		- (k j E i value) == > (k j E i value)
	- For elememts belongs to A
		- (i k A j value) sum till same j  then print (i k A j sum(value till j same))
		- (i k A j value) == > (i k A j sum(value till j same))

# In reducer:
	- Sum of value of rows of A whose having same (i k A j)
	- For matrix A those having same (i,k) store these into a vector length of 50
	- For Matrix E also store in vector of size 50
	- Now perfor dot product
	- print (i k result)
	- repeat for every (i,k)
	
# Execution
	- ( python mapper.py file1.txt | sort | python combiner.py; python mapper.py file2.txt | sort | python combiner.py; python mapper.py file3.txt | sort | python combiner.py;) | sort | python reducer.py > result.tx
	or
	- make (just type 'make' in terminal where project files are present)
