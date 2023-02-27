try:
    read_file=open("../data/demo.txt","r")
    data=read_file.read()
    print(data)
except Exception as e:
    print(e)
finally:
    read_file.close()