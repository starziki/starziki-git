#Visual studio Code에 최적화되어 있습니다.
#%% [markdown]
# ## 파이썬에서 텍스트 파일과 엑셀 파일 읽기
# # 텍스트 읽기
#%%
import pandas as pd
import numpy as np
CCTV_Seoul = pd.read_csv('~/CCTV_in_Seoul.csv', encoding='utf-8')
CCTV_Seoul.head()

#%%
CCTV_Seoul.columns

#%%
CCTV_Seoul.columns[0]
#%%
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0]:'구별'}, inplace=True)
CCTV_Seoul.head()

#%% [markdown]
# # 엑셀 읽기
#%%
pop_Seoul = pd.read_excel("~/population_in_Seoul.xls", encoding='utf-8')
pop_Seoul.head()
#%% [markdown]
# 세번째 줄부터 읽고 B, D, G, J, N 만 읽음<br>
# FutureWarning: the 'parse_cols' keyword is deprecated, use 'usecols' instead<br>
# parse_cols => usecols
#%%
pop_Seoul = pd.read_excel("~/population_in_Seoul.xls",
    header = 2,
    usecols = 'B, D, G, J, N',
    encoding='utf-8')
pop_Seoul.head()
#%%
pop_Seoul.rename(columns={
    pop_Seoul.columns[0] : '구별',
    pop_Seoul.columns[1] : '인구수',
    pop_Seoul.columns[2] : '한국인',
    pop_Seoul.columns[3] : '외국인',
    pop_Seoul.columns[4] : '고령자',
}, inplace=True)
pop_Seoul.head()

#%%
s = pd.Series([1, 3, 5, np.nan, 6, 8])
s

#%%
dates = pd.date_range('20130101', periods=6)
dates
#%% [markdown]
# 6행 4열의 랜덤한 값을 만들고, 칼럼에는 columns=A,B,C,D를 지정하고 <br>
# index명령으로는 dates를 지정함

#%%
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A','B','C','D'])
df
#%%
df.head(3)

#%%
df.index
#%%
df.columns
#%%
df.values

#%% [markdown]
# 해당 Dataframe의 개요를 봄
#%%
df.info()

#%% [markdown]
# describe()명령을 사용하여 통계적 개요를 확인할 수 있습니다.<br>
# 개수, 평균, 최솟값, 최댓값, 각 1/4지점, 표준편차까지 한번에 알아 볼 수 있음.
#%%
df.describe()

#%% [markdown]
# sort_values은 by로 지정된 열을 기준으로 정렬함, <br>
# ascending은 True일 때 오름차순, False일 때 내림차순임.
#%%
df.sort_values(by='B', ascending=False)

#%%
df['A']

#%% [markdown]
#  행 중간부터 보고 싶을 땐, df[1:3] <br>
# 2013-01-03~2013-01-04보고 싶을 땐  df['20130102':'20130104']
#%%
df[1:3]

#%%
df['20130102':'20130104']

#%% [markdown]
# loc 값을 통해 접근

#%% 
df.loc[dates[0]]

#%% 
df.loc[:,['A','B']]

#%%
df.loc['20130102':'20130104',['A','B']]

#%%
df.loc['20130102',['A','B']]

5
#%%
df.loc[dates[0],'A']

#%% [markdown]
# iloc 행과열의 번호로 접근함.
#%%
df.iloc[3]

#%%
df.iloc[3:5,0:2]

#%%
df.iloc[1:5,:]

#%%
df.iloc[:,1:3]

#%%
df

#%% [markdown]
# 특정조건을 만족하는 데이터만 얻을 수 있음<br>
# 칼럼을 지정할 때 df.A을 함.<br>
# df.a칼럼 조건에 맞는 행만 표시됨.
#%%
df[df.A > 0]

#%% [markdown]
# 데이터전체(df와 같이) 조건을 걸면<br>
# 조건에 맞지 않는 건 NaN으로 표시됨
#%% 
df[ df > 0]

#%% [markdown]
# df2['E']=[~]가 작동하지 않음.<br>
# Pandas0.16.0+는 assign으로 해야함.
# df2 = df2.['E']='one', 'two', ' three', 'four', 'five','Six'] <=안됨.

#%%
df2 = df.copy()
df2=df2.assign(E=['one', 'two', ' three', 'four', 'five','Six'])
df2


#%% [markdown]
#isin으로 쓸것 그리고 있는지 없는지를 확인함.
#df2[df2['E']>]

#%%
df2['E'].isin(['two', 'four'])

#%%
df2[df2['E'].isin(['two', 'four'])]

#%%
df.apply(np.cumsum) 

#%% [markdown]
# 누적합=numpy의 cunsum
#%%
df.apply(np.cumsum) 

#%% [markdown]
# 람다를 씀
#%% 
df.apply(lambda x: x.max()-x.min())

#%%
CCTV_Seoul.head()

#%% [makrdown]
# CCTV의 전체 개수인 소계로 오름차순으로 정렬
#%%
CCTV_Seoul.sort_values(by='소계',ascending=True).head()

#%% [makrdown]
# CCTV의 전체 개수인 소계로 내림차순으로 정렬

#%%
CCTV_Seoul.sort_values(by='소계',ascending=False).head()

#%%
CCTV_Seoul=CCTV_Seoul.assign( 최근증가율 = ( CCTV_Seoul['2016년'] + CCTV_Seoul['2015년'] + CCTV_Seoul['2014년'] ) / CCTV_Seoul['2013년도 이전'] * 100)

#%%
CCTV_Seoul.sort_values(by='최근증가율', ascending=False).head(5)

#%%

#%%
pop_Seoul.head()
#%%
pop_Seoul.drop([0], inplace=True)
pop_Seoul.head()



#%%
pop_Seoul['구별'].unique()
#%%
pop_Seoul[pop_Seoul['구별'].isnull()]
#%%
pop_Seoul.drop([26], inplace=True)
pop_Seoul.head()

#%%
# 참 되는 게 있고 안 되는게 있다니...
# 서울인구는 XlS의 확장자에서 바로 읽어서 그런 듯....
#%%
pop_Seoul['외국인비율']=pop_Seoul['외국인']/pop_Seoul['인구수']*100
pop_Seoul['고령자비율']=pop_Seoul['고령자']/pop_Seoul['인구수']*100
pop_Seoul.head()

#%%
pop_Seoul.sort_values(by='인구수', ascending=False).head(5)

#%%
pop_Seoul.sort_values(by='외국인', ascending=False).head(5)
#%%
pop_Seoul.sort_values(by='외국인비율', ascending=False).head(5)
#%%
pop_Seoul.sort_values(by='고령자', ascending=False).head(5)
#%%
pop_Seoul.sort_values(by='고령자비율', ascending=False).head(5)

#%%
data_result = pd.merge(CCTV_Seoul,pop_Seoul,on='구별')
data_result.head()

#%%
del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']
data_result.head()

#%%
import matplotlib.pyplot as plt
%matplotlib inline
#%%
plt.figure
plt.plot([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0])
plt.show()
#%%
t = np.arange(0,12,0.01)
y= np.sin(t)
#%%
plt.figure(figsize=(10,6))
plt.plot(t,y)
plt.show()

#%%
plt.figure(figsize=(10,6))
plt.plot(t,y)
plt.grid()
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.show()

#%%
plt.figure(figsize=(10,6))
plt.plot(t, np.sin(t),lw=3, label='sin')
plt.plot(t, np.cos(t),'r', label='cos')
plt.plot(t,y)
plt.legend()
plt.grid()
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')    
plt.show()

#%%
t = [0, 1, 2, 3, 4, 5, 6]
y = [1, 4, 5, 8, 9, 5, 3]
plt.figure(figsize=(10,6))
plt.plot(t,y,color='green')
plt.show()

#%% [markdown]
# https://matplotlib.org/api/markers_api.html

#%% 
t = [0, 1, 2, 3, 4, 5, 6]
y = [1, 4, 5, 8, 9, 5, 3]
plt.figure(figsize=(10,6))
plt.plot(t,y,color='green',linestyle='dashed', marker='D', markerfacecolor='blue', markersize=13)
plt.show()

#%%
plt.figure(figsize=(10,6)) 
t = [0,1,2,3,4,5,6,7,8,9]
y = [9,8,7,9,8,3,1,4,3,4]
plt.scatter(t,y)
plt.show()

#%%
plt.figure(figsize=(10,6)) 
plt.scatter(t,y,marker='>')
plt.show()

#%%
colormap = t
plt.figure(figsize=(10,6))
plt.scatter(t, y, s= 50, c = colormap,marker=">")
plt.colorbar()
plt.show()

#%% [markdown]
# matplotlib가 기본으로 가진 폰트가 한글 지원하지 않는 관계로 matplotlib의 폰트를 변경함

#%%
import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus']=False

if platform.system()=='Darwin':
    rc('font', family='AppleGothic')
elif platform.system()=='Windows':
    path = 'c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font',family=font_name)
    print(font_name)
else:
    print("Unsupported System0")

#%%
data_result['소계'].plot(kind='barh',grid=True,figsize=(10,10),xlabel='CCTV 개수')
data_result['소계'].plot.xlabel='CCTV 개수'
plt.show()

#%%
plt.figure(figsize=(10,10))
plt.plot
