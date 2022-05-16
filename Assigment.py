class Dataset:
    out = []
class Ui:
    def data_in(self):
        for i in range(1, 11):
            distance = float(input("Enter distance:"))
            time = float(input("Enter time taken:"))
            Dataset.out.append([distance, time])
class Me:
    def measure(self):
        var = Dataset.out
        for i in var:
            res = i[0]/i[1]
            i.append(res)
class ShowResults:
    def display(self):
        for i in Dataset.out:
            print(i)

o1 = Ui()
o1.data_in()
o2 = Me()
o2.measure()
o3 = ShowResults()
o3.display()

import csv
row = ['distance', 'time', 'speed']
res = Dataset.out
fo = open("GRL_file.csv", "w")
fo1 = csv.writer(fo)
fo1.writerow(row)
fo1.writerows(res)
fo.close()