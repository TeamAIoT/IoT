import requests
from bs4 import BeautifulSoup

def get_tem():
  #현재 온도 반환 함수 
  
  #네이버 날씨 페이지 가져오기
  res=requests.get("https://search.naver.com/search.naver?query=날씨")

  #print(res.content)

  #html 파싱 
  soup=BeautifulSoup(res.content,'html.parser')

  #온도 정보가 있는 태그 까지 접근하기 
  data1 = soup.find('div', {'class':'temperature_text'})
  data2 = data1.find('strong')

  data=data2.get_text() #태그 안의 내용들 문자열로 가져오기

  #인덱싱 활용하여 문자열들 중 현재 온도만 형변환하여 tem에 저장
  tem=int(data[5:len(data)-1]) #현재 온도 

  return tem

def get_rain_per():
  #강수 확률 반환 함수 
  
  #네이버 날씨 페이지 가져오기
  res=requests.get("https://search.naver.com/search.naver?query=날씨")

  #print(res.content)

  #html 파싱 
  soup=BeautifulSoup(res.content,'html.parser')

  data1 = soup.find('dl', {'class':'summary_list'})
  data2=data1.find('dd',{'class':'desc'})

  
  data=data2.get_text()

  per=int(data[:len(data)-1])

  return per


