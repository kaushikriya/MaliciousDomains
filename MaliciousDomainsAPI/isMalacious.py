import is_malicious
import csv

MispIps= open("MISP.csv",'r')
IBMIps=open("IPv4.csv",'r')

with open('IPv4.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        is_malicious(row[1],'ip')

with open('MISP.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        is_malicious(row,'ip')

