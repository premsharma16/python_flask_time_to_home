from app import app
from flask import render_template
import numpy as np
import matplotlib.pyplot as plt 
''' This is for calling google API and fetching duration to work '''
import googlemaps
import datetime
import re
import matplotlib.pyplot as plt
from pandas import Series
import pandas as pd

gmaps=googlemaps.Client(retry_timeout=10,queries_per_second=1,key='AIzaSyATnjodbtNL-CUZhl2oWcJhSR1_2-KzvSA')

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',title='Home',time_to_home=final_time)

@app.route('/chart')
def chart():
	nw = datetime.datetime.now()
	nw1 = nw.strftime('%Y,%m,%d,%H,%M')
	direc_result = gmaps.directions('SU Block Market, SU Block, Pitampura, Delhi','Bulding no 14,Cybercity, Gurgaon',mode='driving',departure_time=nw)
	final_time=re.sub('mins','',direc_result[0]['legs'][0]['duration_in_traffic']['text'])
	with open("time.csv","a") as fo:
		fo.write(nw1+","+final_time+"\n")
	dic = pd.read_csv('time.csv',delimiter=",")
	return render_template('chart.html',dict=dic)