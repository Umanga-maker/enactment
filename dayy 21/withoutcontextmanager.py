try:    
    file = open("example.txt", "w")
    file.write("This is an example.")
finally:
    file.close()   # type: ignore
    print("File closed successfully!!") 