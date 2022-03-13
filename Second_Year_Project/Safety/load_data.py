from csv import writer
import os

def load_data():
    with open('Safety/static/DATA/data.txt' , 'r') as f:
        x = f.readline()
        f.close()

    with open("Safety/static/EXCEL/Intrue_Detection.csv" , 'a') as f:
        object_write = writer(f)
        object_write.writerow(list(x.split(',')))
        f.close()

    os.remove('Safety/static/DATA/data.txt')
