from selenium import webdriver #selenium을 이용해 크롬에서 파싱홤.
import xlsxwriter 

if(__name__=="__main__"):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1920')
    options.add_argument("--disable-gpu")
    #chromedriver를 미리 받아놓고 headless(창 없이 뛰운다) 실행한다.
    driver = webdriver.Chrome("./chromedriver", options=options) 
    
    driver.implicitly_wait(3) #브라우저의 정상적인 기동을 위해 3초를 기다린다.
    driver.get("http://www.11st.co.kr/html/main.html")
    
    driver.find_element_by_css_selector('input.header_inp_txt').click()
    driver.find_element_by_css_selector('input.header_inp_txt').send_keys("곤약")
    driver.find_element_by_css_selector('button.btn_search#gnbTxtAd').click()
    
    workbook = xlsxwriter.Workbook('11번가.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0

    for n in range(5):
        worksheet.write(row,col,driver.find_elements_by_css_selector("div.plus_prd > div > ul.tt_listbox > li.ad_sec > div > div.list_info > p.info_tit > a")[n].text)
        worksheet.write(row,col+1,driver.find_elements_by_css_selector("div.plus_prd > div > ul.tt_listbox > li.ad_sec > div > div.list_price > div.price_box > span > strong")[n].text)
        row+=1
    workbook.close()
    driver.close()
