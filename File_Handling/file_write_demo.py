try:
    f=open("../data/demo.txt","w")
    f.write("1\n")
    f.write("2")
except Exception as e:
    print(e)
finally:
    f.close()