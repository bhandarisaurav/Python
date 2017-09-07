import csv

dict = {'Python': '.pys', 'C++': '.cpp', 'Java': '.java'}
w = csv.writer(open("output.csv", "w"))
for key, val in dict.items():
    w.writerow([key, val])