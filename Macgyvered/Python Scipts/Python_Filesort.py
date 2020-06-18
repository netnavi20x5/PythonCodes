import json
import os  
#os.system(cmd) 

docu_list = open('doc.json') 
sort_file=json.load(docu_list)
for category in sort_file:
  print ("mkdir " +category)
  os.system("mkdir " +category)
  for filetype in sort_file[category]:
    print("move *."+filetype+" "+category)
    os.system("move *."+filetype+" "+category)