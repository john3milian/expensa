# -*- coding: utf-8 -*-
"""
Expense report
Created on Tue Jul 20 16:07:20 2021

@author: HP
"""

from flask import Flask,render_template,request,redirect,url_for
import pandas as pd
import datetime

  
def graph_1_value_counts():
    table = pd.read_csv('expense.txt')
    y_data = table.payment_mode.value_counts(normalize=False)
    labels = y_data.index.tolist()
    count = len(labels)
    file_text_dp = open('graph_datapoints.txt', 'a')
    file_text_dp.seek(0)                        # <- This is the missing piece
    file_text_dp.truncate()
    i=0
    while i < (count - 1):
        file_text_dp.write('{} {}\n'.format(str(labels[i]), str(y_data[i])))
        #file_text_dp.write('{ label: '+'"'+ str(labels[i])+'"'+',  y: '+str(y_data[i])+' },\n')
        i += 1
    file_text_dp.write('{} {}'.format(str(labels[count - 1]), str(y_data[count - 1])))
    file_text_dp.close()
    
def satisfaction_value_counts():
    table = pd.read_csv('expense.txt')
    y_data = table.satisfaction.value_counts(normalize=True)
    labels = y_data.index.tolist()
    count = len(labels)
    file_text_dp = open('satisfaction_graph_datapoints.txt', 'a')
    file_text_dp.seek(0)                        # <- This is the missing piece
    file_text_dp.truncate()
    i=0
    while i < (count - 1):
        file_text_dp.write('{} {}\n'.format(str(labels[i]), str(y_data[i])))
        #file_text_dp.write('{ label: '+'"'+ str(labels[i])+'"'+',  y: '+str(y_data[i])+' },\n')
        i += 1
    file_text_dp.write('{} {}'.format(str(labels[count - 1]), str(y_data[count - 1])))
    file_text_dp.close()
    
def price_line_graph():
    table = pd.read_csv('expense.txt')
    sum_per_day = table.groupby(['date']).sum()
    y_data = sum_per_day.price.tolist() #Change
    labels = sum_per_day.index.tolist()
    count = len(labels)
    file_text_dp = open('price_line_graph_datapoints.txt', 'a')  #Change
    file_text_dp.seek(0)                        # <- This is the missing piece
    file_text_dp.truncate()
    i=0
    while i < (count - 1):
        file_text_dp.write('{} {}\n'.format(str(labels[i]), str(y_data[i])))
        #file_text_dp.write('{ label: '+'"'+ str(labels[i])+'"'+',  y: '+str(y_data[i])+' },\n')
        i += 1
    file_text_dp.write('{} {}'.format(str(labels[count - 1]), str(y_data[count - 1])))
    file_text_dp.close()

def frequency_line_graph():
    table = pd.read_csv('expense.txt')
    frequency = table.date.value_counts()
    labels = frequency.index.tolist()
    y_data = frequency.tolist()
    count = len(labels)
    file_text_dp = open('frequency_line_graph_datapoints.txt', 'a')  #Change
    file_text_dp.seek(0)                        # <- This is the missing piece
    file_text_dp.truncate()
    i=0
    while i < (count - 1):
        file_text_dp.write('{} {}\n'.format(str(labels[i]), str(y_data[i])))
        #file_text_dp.write('{ label: '+'"'+ str(labels[i])+'"'+',  y: '+str(y_data[i])+' },\n')
        i += 1
    file_text_dp.write('{} {}'.format(str(labels[count - 1]), str(y_data[count - 1])))
    file_text_dp.close()



app = Flask(__name__)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/refresh')
def refresh():

    return redirect(url_for('submit'))

@app.route('/purchase', methods = ['POST','GET'])
def submit():
    if request.method == 'POST':
        item_type_ = request.form.get('itm')
        price_ = request.form.get('pric')
        payment_ = request.form.get('paymant')
        quantity_ = request.form.get('quantiti')
        happy_ = request.form.get('happi')
        if item_type_ or price_ or payment_ or quantity_ or happy_ != "":
            file_text = open('expense.txt', 'a')    
            date = datetime.datetime.now().date()
            time = datetime.datetime.now().time()
            file_text.write("\n{},{},{},{},{},{},{}".format(item_type_,price_,quantity_,payment_,happy_,date,time))
            file_text.close()
            #file_text_dps = open('E:/Spyder projects/Expense/graph_datapoints.txt', 'r')
            #file_text_dps.write("")
            graph_1_value_counts()
            satisfaction_value_counts()
            price_line_graph()
            frequency_line_graph()
            
            
            
            return redirect(url_for('refresh'))
        
        
    return render_template('home.html')


@app.route('/textfile')
def fileread():
    file_open = open('graph_datapoints.txt','r')
    return file_open.read()

@app.route('/linefile')
def linefileread():
    file_open = open('price_line_graph_datapoints.txt','r')
    return file_open.read()

@app.route('/linefile2')
def frequencyfileread():
    file_open = open('frequency_line_graph_datapoints.txt','r')
    return file_open.read()

@app.route('/graph_datapoints')
def graphdp():
    #file_open = open('canvas_graph_test.txt','r')
    #file_open = open('graph_datapoints.txt','r')
    file_open = open('satisfaction_graph_datapoints.txt','r')
    return file_open.read()

@app.route('/canvas')
def canvas():
    return render_template('canvas_test.html')


if __name__ == '__main__':
    app.run(debug = True)
    
