import json 

# Opening JSON file 
f = open('response.json','rb') 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
  
# Iterating through the json 
# list 
#for i in data['responses']: 
#    print(i) 
	
for key, value in data.items():
    for value in key:
       print(value)
	
# Closing file 
f.close() 	
