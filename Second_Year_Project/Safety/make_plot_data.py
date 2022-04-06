import pandas as pd
import matplotlib.pyplot as plt

def make_plot():
    test = {}
    df = pd.read_csv('Safety/static/EXCEL/Intrue_Detection.csv')
    date = df['date'][len(df['Students Detection'])-1:len(df['Students Detection'])-6:-1],df['Students Detection'][len(df['Students Detection'])-1:len(df['Students Detection'])-6:-1].values
    students = df['Students Detection'][len(df['Students Detection'])-1:len(df['Students Detection'])-6:-1].values
    intrusion = df['Intrusion Detection'][len(df['Students Detection'])-1:len(df['Students Detection'])-6:-1].values
    test['date'] = list(date[0].values)
    test['students'] = list(students)
    test['intrusion'] = list(intrusion)
    return test

def make_pie():
    test = {}
    df = pd.read_csv('Safety/static/EXCEL/Intrue_Detection.csv')
    test['students'] = df['Students Detection'][len(df['Students Detection'])-1]
    test['intrusion']= df['Intrusion Detection'][len(df['Students Detection'])-1]
    return test

def make_data():
    data = {}
    df = pd.read_csv('Safety/static/EXCEL/Intrue_Detection.csv')
    data['students'] = df['Students Detection'][len(df['Students Detection'])-1]
    data['intrusion']= df['Intrusion Detection'][len(df['Students Detection'])-1]
    data['total']    = data['students'] + data['intrusion']
    data['avreage']  = format((data['intrusion'] / data['total'])*100,".2f")
    return data