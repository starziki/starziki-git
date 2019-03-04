import sqlite3
import cherrypy
import time
import threading
import smtplib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class HelloWorld(object):
    @cherrypy.expose
    def index(self,email=None):
        try:
            conn = sqlite3.connect("sqllite_test.db")
            with conn:
                cursor = conn.cursor()    
                cursor.execute("select * from email_book")
                
                cursor = conn.cursor()    
                cursor.execute("insert into email_book (email,date) values (?, ?)", [email,time.time () ])
                conn.commit()
                return email+" 등록 OK"
        except Exception:
            if email == None:
                return "등록 불가"
            else :
                return email + " 등록 불가"

def collectnews():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument( 'window-size=1920x1920')
    options.add_argument("--disable-gpu")
    #chromedriver를 미리 받아놓고 headless(창 없이 뛰운다) 실행한다.
    driver = webdriver.Chrome("./autoproject/chromedriver", options=options) 
    
    driver.implicitly_wait(3) #브라우저의 정상적인 기동을 위해 3초를 기다린다.
    driver.get("""https://search.naver.com/search.naver?where=news&query=김정은&sm=tab_srt&sort=1&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so%3Add%2Cp%3Aall%2Ca%3Aall&mynews=0&refresh_start=0&related=0""")

    titles = [i.text for i in driver.find_elements_by_xpath("//div[@class='news mynews section _prs_nws']//dt//a")]
    hrefs = [i.get_attribute('href') for i in driver.find_elements_by_xpath("//div[@class='news mynews section _prs_nws']//dt//a")]
    authors = [i.text for i in driver.find_elements_by_xpath("//div[@class='news mynews section _prs_nws']//dl//span[@class='_sp_each_source']")]

    return [titles, hrefs, authors]
    #driver.find_element_by_xpath("//input[@type='text']").send_keys(Keys.RETURN)
    #driver.find_element_by_xpath("//a[@class='q qs' and .='뉴스']").click()
    #return str.join('\n',[i.text for i in driver.find_elements_by_xpath("//h3[@class='r dO0Ag']/a[@class='l lLrAF']")])

def makearray():
    conn = sqlite3.connect("sqllite_test.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("select email from email_book")
        rows = cursor.fetchall()
        temp = []
        for i in range(len(rows)):
            temp.append(''.join(rows[i]))
    return temp

def sendemail():
    msgfmt = """\
From: {} 
To: {}
Subject: {}
{}""" 
    content = ""
    fromaddr = 'starziki@gmail.com'
    toaddr = str.join(',', makearray())
    subject = 'mailing test'
    contents = collectnews()
    
    for i in range(0, 10):
        title = contents[0][i]
        href = contents[1][i]
        author = contents[2][i]
        content += title + " : " + href + "\n" + author + "\n"
    
    msg = msgfmt.format(fromaddr, toaddr, subject, content)
    print(msg)
    msg=msg.encode('utf8')
    username = 'starziki'
    password = 'gsatedxwwkhvystg'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddr, msg)
    server.quit()
    threading.Timer(5,sendemail).start()

if __name__ == "__main__":
    conn = sqlite3.connect("sqllite_test.db")
    with conn:
        cursor = conn.cursor()    
        cursor.execute("create table if not exists email_book(email TEXT primary key, date TEXT)")
        conn.commit()
        
    hello = HelloWorld()
    sendemail()
    cherrypy.quickstart(hello)
