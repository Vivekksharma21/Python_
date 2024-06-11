try:
    fileptr=open("vivek.txt","r")
    #fileptr.write("Sample text ")
    f=fileptr.read()
    print(f)
except IOError:
    print("THe file error ")
else:
    print("LEt us read ")
finally:
    fileptr.close()
    print("File closed")