import os
path = os.getcwd()
folders = []
# r=root, d=directories, f = files

outfile = open("Out_Result.csv","w") # to write to output because lazy to read from Command line
outfile.write("sep=|\n")
for r, d, f in os.walk(path):
	for files in f:
		infile = open(files, 'r')
		firstLine = infile.readline()
		print (files+"|"+firstLine)
		outfile.write(files+"|"+firstLine+"no of comma"+"|"+str(firstLine.count(',')) )
