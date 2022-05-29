import csv
import sys

#next months inflation and petrol prediction

file1 = open("data_1.csv", "r")
file2 = open("data_2.csv", "r")

a = file1.readlines()
b = file2.readlines()

c = []

#afisarea celor 2 liste combinate

with open("output-py.csv", "w") as f:
    
    sys.stdout = f #schimbam output ul pentru fisierul creat
    for i in range(122):

        a[i]=a[i][:-1]
        b[i]=b[i][:-1]
        c=a[i].split(',')
        c.append(str(b[i]))

        print(c[0], end = ','), print(c[1], end = "," ), print(c[2], end = "\n") 


