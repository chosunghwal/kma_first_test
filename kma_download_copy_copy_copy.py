# 03.1. Import Module
# https://signing.tistory.com/m/15
from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests
import json
import pandas as pd
from bs4 import BeautifulSoup

import flask
from flask import Flask, request, render_template,url_for, redirect
#import sklearn.external.joblib as extjoblib
import joblib
#from sklearn.externals import joblib
import numpy as np
from scipy import misc

# 1.1 Importing necessary libraries
import smtplib, os, pickle  # smtplib: 메일 전송을 위한 패키지
from email import encoders  # 파일전송을 할 때 이미지나 문서 동영상 등의 파일을 문자열로 변환할 때 사용할 패키지
from email.mime.text import MIMEText   # 본문내용을 전송할 때 사용되는 모듈
from email.mime.multipart import MIMEMultipart   # 메시지를 보낼 때 메시지에 대한 모듈
from email.mime.base import MIMEBase     # 파일을 전송할 때 사용되는 모듈

import csv
import datetime
#import os
import xlrd

app = Flask(__name__)

'''
# 03.2 URL 설정
#   url for request
#http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList
#?serviceKey=인증키&numOfRows=10&pageNo=1
#&dataCd=ASOS&dateCd=DAY&startDt=20100101&endDt=20100102&stnIds=108
#*******************************************************

@app.route('/')
def hello():
    return redirect(url_for('weather')) # face로 리다이렉트
    # return "hello world"

def call_weather_api_ready():
    api_key = open("./weather_api").readlines()[0].strip()
    url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
    params = '?' + urlencode({
        quote_plus("dataType"): "json",
        quote_plus("dataCd"): "ASOS",
        quote_plus("dateCd"): "DAY",
        quote_plus("startDt"): "20200212",
        #quote_plus("startHh"): "00",
        quote_plus("endDt"): "20200512",
        #quote_plus("endHh") : "23",
        quote_plus("stnIds"): "108",
        quote_plus("numOfRows"): "500",
        quote_plus("pageNo"): "1",
        quote_plus("serviceKey"): api_key
        #quote_plus("serviceKey"): "Zdo9nWPw9u%2FiUQLFUevtj5NjPbNDyl15b32b%2BRx9ZHvICrARG%2B9wBQPXgmSVU30Bo9KESuzvm8UVR%2Fssntf8Mg%3D%3D"
    })
    return url,params
'''

#*******************************************************


# 메인 페이지 라우팅
@app.route("/")
@app.route("/index")
def index():
    if request.method == 'GET':
        return render_template('weather_copy.html')
    #return flask.render_template('weather_copy.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'GET':
        return render_template('weather_copy.html')
    else:
        stations = [105,108,159,192]
        #stations = [105,108,159]
        #jason_list = list()
        data_other = pd.DataFrame() 
        for station in stations:
                data_other1 = pd.DataFrame() 
                print('stationstationstation:::',station)
                #data_other = pd.DataFrame() 
                startDt = request.form['startdate']
                endDt = request.form['enddate']
                api_key = open("./weather_api").readlines()[0].strip()
                url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
                params = '?' + urlencode({
                quote_plus("dataType"): "json",
                quote_plus("dataCd"): "ASOS",
                quote_plus("dateCd"): "DAY",
                #quote_plus("startDt"): "20200212",
                quote_plus("startDt"): startDt,
                #quote_plus("startHh"): "00",
                #quote_plus("endDt"): "20200512",
                quote_plus("endDt"): endDt,
                #quote_plus("endHh") : "23",
                #quote_plus("stnIds"): "108",
                quote_plus("stnIds"): station,
                quote_plus("numOfRows"): "500",
                quote_plus("pageNo"): "1",
                quote_plus("serviceKey"): api_key
                #quote_plus("serviceKey"): "Zdo9nWPw9u%2FiUQLFUevtj5NjPbNDyl15b32b%2BRx9ZHvICrARG%2B9wBQPXgmSVU30Bo9KESuzvm8UVR%2Fssntf8Mg%3D%3D"
                })
                req = urllib.request.Request(url + unquote(params))
                response_body = urlopen(req, timeout=60).read() # get bytes data
                data = json.loads(response_body)# convert bytes data to json data
                print('json.loadsson.loadsson.loadsson.loadsson.loadsson.loadsson.loads',data)
                result = requests.get(url + unquote(params))
                print('resultresultresultresultresultresult',result)
                if result.status_code == 500:
                    print("response.status_code == 500")
                if result.status_code == 200:
                    print('response.status_code:::::::::::::',result.status_code)
                    js = json.loads(result.content)
                    data_other1 = pd.DataFrame(js['response']['body']['items']['item'])
                    print('data_otherdata_otherdata_otherdata_otherdata_otherdata_other',data_other)
                    print('resultresultresultresultresultresultresultresultresultresult',result)
                    li = ['stnId','tm','avgTa','minTa','maxTa','sumRn','maxWs','avgWs','ddMes','sumRn']
                    data_other1.loc[:,li]
                    data_other = data_other.append(data_other1,ignore_index=True)

        #path = 'D:\\vip\\pythonProject\\flask1\\kma_csv_file'
        path = './kma_csv_file'
        #D:\vip\pythonProject\flask1\kma_csv_file
        '''
        from datetime import datetime

        now = datetime.now() # current date and time

        year = now.strftime("%Y")
        print("year:", year)

        month = now.strftime("%m")
        print("month:", month)

        day = now.strftime("%d")
        print("day:", day)

        time = now.strftime("%H:%M:%S")
        print("time:", time)

        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        print("date and time:",date_time)	
        '''
        '''
        import datetime

        format = "%a %b %d %H:%M:%S %Y"

        today = datetime.datetime.today()
        print 'ISO     :', today

        s = today.strftime(format)
        print 'strftime:', s

        d = datetime.datetime.strptime(s, format)
        print 'strptime:', d.strftime(format)
        '''
        file_name = "TODAYS_SHEET" + datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S') + ".csv" 
        #with open('20201115weather.csv','a') as f:
        #with open(file_name, 'w') as file_:
        print(file_name)
        global os
        with open(os.path.join(path, file_name), 'w') as file_:
                #data_other[li].to_csv(f,header = True)
                data_other[li].to_csv(file_,header = True)
                dlist = data_other.to_dict('list')

        # ---------------------------------------------------------------------------------------------------
        # Attach FILE
        #path = '20201115weather.csv'
        #path = 'D:\\vip\\pythonProject\\flask1\\csv_file'
        #file_name = "TODAYS SHEET " + datetime.datetime.today().strftime('%Y-%m-%d') + ".csv"    
        #with open(os.path.join(path, file_name), 'a') as file_:               
                #file_.write('a,a,a,a,a,a')
        #        data_other[li].to_csv(file_,header = False)
        '''
                writer = csv.writer(file_)

                workbook = xlrd.open_workbook('herp.xlsx')
                worksheet = workbook.sheet_by_name('A Snazzy Title')

                num_rows = worksheet.nrows - 1
                curr_row = -1

                while curr_row < num_rows:
                    curr_row += 1
                    row = [cell.value for cell in worksheet.row(curr_row)]
                    writer.writerow(row) '''
        # -----------------------------------------------------------------------------------------------------
        
        #메일을 보낼 주소들을 미리 저장해준다.
        #테스트를 위해 여러가지 주소로 보내고 싶은데, 계정을 여러 개 갖고 있지 않으므로,
        #내 이메일 주소인 hyeshinoh@gmail.com에서 hyeshinoh 뒤에 ‘+’와 아무 글자를 넣어주면 마치 여러 개의 이메일 주소인 것처럼 사용할 수 있다. 
        # 이렇게 쓰면 메일은 모두 hwalsung777@gmail.com로 전송된다.

        toAddr = ["sunghwal7@naver.com", "hwalsung777@gmail.com", "hwalsung77@hanmail.net"]

        #1.2 Setting login information: email & password
        #password는 직접 노출하면 유출의 위험이 있으므로 아래와 같이 pickle 파일로 저장해서 이용하는 것이 좋다.

        #pw = "jdqpndkvjepwjlgl"    
        #pickle.dump(pw, open("pw.pickle", 'wb'))


        email = "hwalsung777@gmail.com"
        pw = pickle.load(open('pw.pickle', 'rb'))

        print(pw)
        #2. Send text
        #2.1 Access smtp server
        #smtp object를 생성한다.
        smtp = smtplib.SMTP('smtp.gmail.com', 587)   # 587: 서버의 포트번호

        smtp.ehlo()
        smtp.starttls()   # tls방식으로 접속, 그 포트번호가 587
        #mtp.login('hwalsung777@gsmail.com', pickle.load( open('./pw.pickle', 'rb') ))
        #smtp.login('hwalsung777@gmail.com', pw)
        smtp.login('hwalsung777@gmail.com', pickle.load( open('./pw.pickle', 'rb') ))

        #2.2 Make message
        #msg object를 생성하고 제목을 넣어준다.

        msg = MIMEMultipart()    #msg obj.
        msg['Subject'] = 'hyeshin의 SMTP Send Text 테스트'

        #msg object에 본문(text msg)을 추가해준다.

        # text msg
        part = MIMEText('공공데이터 자동 수집 체계 진행중인 기상청 데이터 자동 발송 시험입니다 written by 조성활.')
        msg.attach(part)   #msg에 part obj.를 추가해줌
        msg


        #part_html = MIMEText('<br><a href="https://github.com/hyeshinoh/">hyeshin github</a>', 'html')
        #msg.attach(part_html)

        msg  #msg 상태: 제목, 본문(text), html 코드
        #2.3 email 전송하기
        
        #파일을 첨부해보자. 단, javascript file은 보안 상 이유로 보낼 수 없게 되어 있음
        #3. Send File
        #이제 파일을 첨부해서 이메일을 보내보자
        #파일을 첨부해보자. 단, javascript file은 보안 상 이유로 보낼 수 없게 되어 있음

        # ctype = 'application/octet-stream'
        # maintype, subtype = ctype.split('/', 1)
        #--------------------------------
        import os
        #files_Path = "Output/" # 파일들이 들어있는 폴더
        #files_Path = 'D:\\vip\\pythonProject\\flask1\\kma_csv_file\\'
        #files_Path = '.\\kma_csv_file\\'
        files_Path  = './kma_csv_file/'
        file_name_and_time_lst = []
        print(os.listdir(f"{files_Path}"))
        # 해당 경로에 있는 파일들의 생성시간을 함께 리스트로 넣어줌. 

        for f_name in os.listdir(f"{files_Path}"):
            written_time = os.path.getctime(f"{files_Path}{f_name}")
            file_name_and_time_lst.append((f_name, written_time))
        # 생성시간 역순으로 정렬하고, 
        sorted_file_lst = sorted(file_name_and_time_lst, key=lambda x: x[1], reverse=True)
        # 가장 앞에 이는 놈을 넣어준다.
        print('sorted_file_lst:::',sorted_file_lst)
        recent_file = sorted_file_lst[0]
        print('recent_file',recent_file)
        recent_file_name = recent_file[0] 
        print('recent_file_name:::',recent_file_name)
        #--------------------------------

        with open(os.path.join(path, recent_file_name), 'rb') as f:
        #with open(file_name, 'rb') as f:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(f.read())    #payload: osi 7-layers
            encoders.encode_base64(part)  #base64 encoding: 영상, 이미지 파일을 문자열 형태로 변환
            part.add_header('Content-Disposition', 'attachment', filename=file_name)
            msg.attach(part)
            msg  # 제목, 본문, 파일

        for addr in toAddr:
            msg["To"] = addr
            smtp.sendmail("hwalsung777@gmail.com", addr, msg.as_string())
                #msg는 object이기 때문에 전송을 위해 .as_string()으로 문자열로 바꿔야함(parsing)
            print(addr)

        list1 = dlist.get('stnId')
        print('listlistlistlistlist::',list1)
        list2 = dlist.get('tm')
        print('list2list2list2list2list2::',list2)
        list3 = dlist.get('avgTa')
        list4 = dlist.get('minTa')
        list5 = dlist.get('avgWs')
        list6 = dlist.get('sumRn')
        return render_template('weather_copy.html', d1=list1, d2=list2,d3=list3,d4=list4,d5=list5,d6=list6)                    
           # return render_template('weather_copy.html', data=data_other)**************************************************
           #     
if __name__ == '__main__':  
    #url,params = call_weather_api_ready() 
    #call_weather_api(url,params)
    #weather()
# Flask 서비스 스타트
    app.run(host='0.0.0.0', port=8000, debug=True)