fo = open("./example.txt", "wb") 
print("file contents:", fo)
print("Closed or not:", fo.closed) 
print("Opening mode: ", fo.mode) 
fo.close() 
print("Closed or not: ", fo.closed) 
print("Opening mode: ", fo.mode)