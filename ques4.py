import os #to use the function of operating system
import csv #to read csv file

for file_ in os.listdir("raw"): #to create a list of file in raw folder
    with open('raw/'+ file_, 'rb') as csvfile: 
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            print row #to print all the rows in the raw folder
            if os.path.isfile("processed/" + row[0] +"-processed.csv"): #to append if file already exist in processed folder 
                with open("processed/" + row[0] +"-processed.csv", 'a') as csvfile1:
                    spamwriter = csv.writer(csvfile1, delimiter=',')
                    spamwriter.writerow(row)
            else:
                with open("processed/" + row[0] +"-processed.csv", 'wb') as csvfile1: #to create  if file doesn't already exist in processed folder
                    spamwriter = csv.writer(csvfile1, delimiter=',') 
                    spamwriter.writerow(row)
