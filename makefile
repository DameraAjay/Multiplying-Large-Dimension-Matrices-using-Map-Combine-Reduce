tar:
	( python mapper.py file1.txt | sort | python combiner.py; python mapper.py file2.txt | sort | python combiner.py; python mapper.py file3.txt | sort | python combiner.py;) | sort | python reducer.py > result.txt

clean:
	rm result.txt
