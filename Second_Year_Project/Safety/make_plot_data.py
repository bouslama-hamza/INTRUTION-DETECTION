import pandas as pd
import matplotlib.pyplot as plt

def make_plot():
    df = pd.read_csv('Safety/static/EXCEL/Intrue_Detection.csv')
    plt.figure(figsize=(9,5), dpi= 80 , frameon = False)
    plt.style.use('seaborn-darkgrid')
    plt.fill_between(df['date'][len(df['Students Detection'])-1:len(df['Students Detection'])-6:-1], df['Students Detection'][len(df['Students Detection'])-1:len(df['Students Detection'])-6:-1], color="skyblue", alpha=0.3)
    plt.fill_between(df['date'][len(df['Students Detection'])-1:len(df['Students Detection'])-6:-1], df['Intrusion Detection'][len(df['Students Detection'])-1:len(df['Students Detection'])-6:-1], color="lightcoral", alpha=0.3)
    plt.plot(df['date'][len(df['Students Detection'])-1:len(df['Students Detection'])-6:-1], df['Students Detection'][len(df['Students Detection'])-1:len(df['Students Detection'])-6:-1], marker ='o',color="skyblue" , label ='Student Detected')
    plt.plot(df['date'][len(df['Students Detection'])-1:len(df['Students Detection'])-6:-1], df['Intrusion Detection'][len(df['Students Detection'])-1:len(df['Students Detection'])-6:-1],marker ='o', color="lightcoral" , label = 'Intrusion Detected')
    plt.gca().get_yaxis().set_visible(False)
    plt.savefig("Safety/static/EXCEL/plot.png" , transparent=True)

def make_pie():
    df = pd.read_csv('Safety/static/EXCEL/Intrue_Detection.csv')
    labels  = ['Students' ,'Intrusion']
    test = [df['Students Detection'][len(df['Students Detection'])-1] , df['Intrusion Detection'][len(df['Students Detection'])-1]]
    plt.figure(figsize=(4.5,5), dpi= 80 , frameon = False)
    plt.pie(test ,  labels = labels , colors= ['skyblue' , 'lightcoral'])
    plt.savefig("Safety/static/EXCEL/pie.png" , transparent=True)

def make_data():
    data = {}
    df = pd.read_csv('Safety/static/EXCEL/Intrue_Detection.csv')
    data['students'] = df['Students Detection'][len(df['Students Detection'])-1]
    data['intrusion']= df['Intrusion Detection'][len(df['Students Detection'])-1]
    data['total']    = data['students'] + data['intrusion']
    data['avreage']  = format((data['students'] / data['total'])*100,".2f")
    return data