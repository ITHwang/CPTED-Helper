#!/usr/bin/env python
# coding: utf-8

# # 도로명

# In[499]:


#!/usr/bin/env python3
import pandas as pd
import numpy as np

data_df=pd.read_excel("C:\\Users\\intae\\Desktop\\공모전\\도로명정보조회.xls",sheetname='도로명정보조회' )
data_df.head(5)


# In[500]:


# 칼럼명 제대로
data_df.columns = [''] * len(data_df.columns)
data_df.columns=['시군구','도로명번호','도로명','로마자표기','읍면동일련번호','시도명','시군구명','읍면동구분','읍면동코드','읍면동명']
data_df=data_df.drop(0, inplace=False)

# 추출
data_df= data_df[data_df['읍면동일련번호']=='00']
data_df=data_df['도로명']
data_df=data_df.reset_index()
data_df=data_df.drop(['index'],axis=1,inplace=False)
data_df.head()


# In[501]:


data_df.info()


# # 안전비상벨

# In[502]:


data1_df=pd.read_csv("C:\\Users\\intae\\Desktop\\공모전\\안전비상벨위치.csv",encoding='euc-kr')
data1_df.head(5)


# In[503]:


# 도로명주소 추출 후 칼럼 추출
data1_df = data1_df[['소재지도로명주소']]
data1_df[['소재지도로명주소','dd']]=data1_df['소재지도로명주소'].str.split(' ', n=1, expand=True)
data1_df=data1_df.drop(['dd'],axis=1,inplace=False)

# 지번주소 인덱스 삭제
for name in data1_df['소재지도로명주소']:
    if name=='서울특별시':
        data1_df=data1_df.drop(data1_df[data1_df['소재지도로명주소']==name].index,inplace=False,axis=0)

# 오기된 도로명주소 행 삭제
for address in data1_df['소재지도로명주소']:
    if address not in list(data_df['도로명'].values):
        data1_df = data1_df.drop(data1_df[data1_df['소재지도로명주소']==address].index, inplace=False, axis=0)
        
data1_df


# In[504]:


# 개수 세기
addresses_count={}
for address in list(data1_df['소재지도로명주소']):
    try:
        addresses_count[address]+=1
    except:
        addresses_count[address]=1
print(addresses_count)


# In[505]:


data2_df=pd.DataFrame.from_records([addresses_count])
data2_df=data2_df.transpose().reset_index()
data2_df.rename(columns={'index': '도로명', 0: '안전비상벨 개수'}, inplace=True)
data2_df


# In[506]:


data_df=pd.merge(data_df,data2_df,on='도로명',how='left')


# In[507]:


data_df['안전비상벨 개수'] = data_df['안전비상벨 개수'].fillna(0).astype('int')
data_df


# # CCTV

# In[508]:


data1_df=pd.read_csv("C:\\Users\\intae\\Desktop\\공모전\\CCTV.csv",encoding='euc-kr')
data1_df.head(5)


# In[509]:


# 도로명주소 추출 후 칼럼 추출
data1_df = data1_df[['소재지도로명주소','카메라대수']]
data1_df[['소재지도로명주소','dd']]=data1_df['소재지도로명주소'].str.split(' ', n=1, expand=True)
data1_df=data1_df.drop(['dd'],axis=1,inplace=False)

# 오기된 도로명주소 행 삭제
for address in data1_df['소재지도로명주소']:
    if address not in list(data_df['도로명'].values):
        data1_df = data1_df.drop(data1_df[data1_df['소재지도로명주소']==address].index, inplace=False, axis=0)

data1_df=data1_df.reset_index()
data1_df=data1_df.drop(['index'],axis=1,inplace=False)
data1_df


# In[510]:


addresses=[]
add=[]
for index, address in enumerate(list(data1_df['소재지도로명주소'])):
    address=(address+str(' '))* data1_df.ix[index, ['카메라대수']]
    addresses.extend(address)
for element in addresses:
    dd=str(element).split(sep=' ')
    add.extend(dd)
add
   


# In[511]:


# 고유값 추출
addresses_count={}
for address in add:
    try:
        addresses_count[address]+=1
    except:
        addresses_count[address]=1
print(addresses_count)


# In[512]:


data2_df=pd.DataFrame.from_records([addresses_count])
data2_df=data2_df.transpose().reset_index()
data2_df.rename(columns={'index': '도로명', 0: 'CCTV 카메라 개수'}, inplace=True)
data2_df=data2_df.drop(0, inplace=False)
data2_df


# In[513]:


data_df=pd.merge(data_df,data2_df,on='도로명',how='left')
data_df


# In[514]:


data_df['CCTV 카메라 개수'] = data_df['CCTV 카메라 개수'].fillna(0).astype('int')
data_df


# # 담배소매인 지정 업소

# In[515]:


data1_df=pd.read_csv("C:\\Users\\intae\\Desktop\\공모전\\담배소매인지정.csv",encoding='euc-kr')
data1_df.head(5)


# In[516]:


# 도로명주소 추출 후 칼럼 추출
data1_df = data1_df[['업소도로명주소']]
data1_df[['a','b','업소도로명','c']]=data1_df['업소도로명주소'].str.split(' ', n=3, expand=True)
data1_df=data1_df.drop(['a','b','c','업소도로명주소'],axis=1,inplace=False)

# 오기된 도로명주소 행 삭제
for address in data1_df['업소도로명']:
    if address not in list(data_df['도로명'].values):
        data1_df = data1_df.drop(data1_df[data1_df['업소도로명']==address].index, inplace=False, axis=0)

# Null 값 제거
data1_df=data1_df.reset_index()
data1_df=data1_df.drop(['index'],axis=1,inplace=False)

data1_df['업소도로명'] = data1_df['업소도로명'].fillna(0)
data1_df=data1_df.drop(data1_df[data1_df['업소도로명']==0].index,axis=0,inplace=False)

data1_df


# In[517]:


# 개수 세기
addresses_count={}
for address in list(data1_df['업소도로명']):
    try:
        addresses_count[address]+=1
    except:
        addresses_count[address]=1
print(addresses_count)


# In[518]:


data2_df=pd.DataFrame.from_records([addresses_count])
data2_df=data2_df.transpose().reset_index()
data2_df.rename(columns={'index': '도로명', 0: '담배소매인 지정 업소 개수'}, inplace=True)
data2_df


# In[519]:


data_df=pd.merge(data_df,data2_df,on='도로명',how='left')
data_df['담배소매인 지정 업소 개수'] = data_df['담배소매인 지정 업소 개수'].fillna(0).astype('int')
data_df


# # 음식점

# In[520]:


data1_df=pd.read_csv("C:\\Users\\intae\\Desktop\\공모전\\음식점.csv",encoding='euc-kr')
data1_df.head(5)


# In[521]:


# 도로명주소 추출 후 칼럼 추출
data1_df = data1_df[['업종명','인허가일자','소재지(도로명)','업태명']]
data1_df[['a','b','도로명','c']]=data1_df['소재지(도로명)'].str.split(' ', n=3, expand=True)
data1_df=data1_df.drop(['a','b','c','소재지(도로명)'],axis=1,inplace=False)
data1_df=data1_df[['도로명','업종명','인허가일자']]

# Null 값인 행 삭제
data1_df['도로명'] = data1_df['도로명'].fillna(0)
data1_df=data1_df.drop(data1_df[data1_df['도로명']==0].index,axis=0,inplace=False)

# 오기된 도로명주소 행 삭제
for address in data1_df['도로명']:
    if address not in list(data_df['도로명'].values):
        data1_df = data1_df.drop(data1_df[data1_df['도로명']==address].index, inplace=False, axis=0)
        
data1_df=data1_df.reset_index()
data1_df=data1_df.drop(['index'],axis=1,inplace=False)

data1_df


# In[522]:


# 개수 세기
addresses_count={}
for address in list(data1_df['도로명']):
    try:
        addresses_count[address]+=1
    except:
        addresses_count[address]=1
print(addresses_count)


# In[523]:


data2_df=pd.DataFrame.from_records([addresses_count])
data2_df=data2_df.transpose().reset_index()
data2_df.rename(columns={'index': '도로명', 0: '음식점 개수'}, inplace=True)

# 값이 1인 데이터가 너무 많아서 업종명이랑 인허가일자도 제거..


# In[524]:


data_df=pd.merge(data_df,data2_df,on='도로명',how='left')
data_df['음식점 개수'] = data_df['음식점 개수'].fillna(0).astype('int')
data_df


# In[525]:


# Null 값이랑 오기된 주소 행 삭제하고 인덱스 갱신해주고 개수 세주고 피처 만들어주는 함수
def preprocessing(data1_df):
    data1_df['도로명'] = data1_df['도로명'].fillna(0)
    data1_df=data1_df.drop(data1_df[data1_df['도로명']==0].index,axis=0,inplace=False)
    
    for address in data1_df['도로명']:
        if address not in list(data_df['도로명'].values):
            data1_df = data1_df.drop(data1_df[data1_df['도로명']==address].index, inplace=False, axis=0)
        
    data1_df=data1_df.reset_index()
    data1_df=data1_df.drop(['index'],axis=1,inplace=False)
    print(data1_df)
    
    addresses_count={}
    for address in list(data1_df['도로명']):
        try:
            addresses_count[address]+=1
        except:
            addresses_count[address]=1
    print(addresses_count)
    
    data2_df=pd.DataFrame.from_records([addresses_count])
    data2_df=data2_df.transpose().reset_index()
    data2_df.rename(columns={'index': '도로명', 0: '피처'}, inplace=True)
    
    return data2_df


# # 보안등

# In[526]:


data1_df=pd.read_csv("C:\\Users\\intae\\Desktop\\공모전\\보안등.csv",encoding='euc-kr')
data1_df.head(5)


# In[527]:


data1_df = data1_df[['소재지도로명주소']]
data1_df[['a','b','도로명','c']]=data1_df['소재지도로명주소'].str.split(' ', n=3, expand=True)
data1_df=data1_df.drop(['a','b','c','소재지도로명주소'],axis=1,inplace=False)


# In[528]:


data1_df=data1_df[['도로명']]
data2_df= preprocessing(data1_df)


# In[529]:


data2_df.rename(columns={'피처': '보안등 개수'}, inplace=True)
data2_df


# In[530]:


data_df=pd.merge(data_df,data2_df,on='도로명',how='left')
data_df['보안등 개수']= data_df['보안등 개수'].fillna(0).astype('int')
data_df


# # 아파트

# In[531]:


data1_df=pd.read_csv("C:\\Users\\intae\\Desktop\\공모전\\아파트.csv",encoding='euc-kr')
data1_df.head(5)


# In[532]:


data1_df = data1_df[['도로명주소','총호수']]
data1_df[['도로명','a']]=data1_df['도로명주소'].str.split(' ', n=1, expand=True)
data1_df=data1_df.drop(['도로명주소','a'],axis=1,inplace=False)
data1_df=data1_df[['도로명','총호수']]
data1_df


# In[533]:


for address in data1_df['도로명']:
    if address not in list(data_df['도로명'].values):
        data1_df = data1_df.drop(data1_df[data1_df['도로명']==address].index, inplace=False, axis=0)
        
data1_df=data1_df.reset_index()
data1_df=data1_df.drop(['index'],axis=1,inplace=False)

address_without=[]
for address in data1_df['총호수']:
    without=address.replace(',','')
    address_without.append(without)
    
data1_df['총_호수'] = address_without
data1_df= data1_df.drop('총호수',axis=1,inplace=False)
data1_df


# In[534]:


addresses=[]
add=[]
for index, address in enumerate(list(data1_df['도로명'])):
    address=(address+str(' '))* int(data1_df.ix[index, 1])
    addresses.append(address)
for element in addresses:
    dd=str(element).split(sep=' ')
    add.extend(dd)
add


# In[535]:


addresses_count={}
for address in add:
    try:
        addresses_count[address]+=1
    except:
        addresses_count[address]=1
        
print(addresses_count)


# In[536]:


data2_df=pd.DataFrame.from_records([addresses_count])
data2_df=data2_df.transpose().reset_index()
data2_df.rename(columns={'index': '도로명', 0: '아파트 세대 수'}, inplace=True)
data2_df=data2_df.drop(0, inplace=False)
data2_df


# In[537]:


data_df=pd.merge(data_df,data2_df,on='도로명',how='left')
data_df['아파트 세대 수']= data_df['아파트 세대 수'].fillna(0).astype('int')
data_df


# # 과속방지턱

# In[538]:


data1_df=pd.read_csv("C:\\Users\\intae\\Desktop\\공모전\\과속방지턱.csv",encoding='cp949')
data1_df.head(5)


# In[539]:


data1_df = data1_df[['위치']]
data1_df[['도로명','a']]=data1_df['위치'].str.split(' ', n=1, expand=True)
data1_df=data1_df.drop(['위치','a'],axis=1,inplace=False)
data1_df


# In[540]:


data2_df= preprocessing(data1_df)
data2_df.rename(columns={'피처': '과속방지턱 개수'}, inplace=True)
data2_df


# In[541]:


data_df=pd.merge(data_df,data2_df,on='도로명',how='left')
data_df['과속방지턱 개수']= data_df['과속방지턱 개수'].fillna(0).astype('int')
data_df


# # 금연구역

# In[542]:


data1_df=pd.read_csv("C:\\Users\\intae\\Desktop\\공모전\\금연구역.csv",encoding='cp949')
data1_df.head(5)


# In[543]:


data1_df = data1_df[['소재지도로명주소']]
data1_df[['a','b','도로명','c']]=data1_df['소재지도로명주소'].str.split(' ', n=3, expand=True)
data1_df=data1_df.drop(['소재지도로명주소','a','b','c'],axis=1,inplace=False)
data1_df


# In[544]:


data2_df= preprocessing(data1_df)
data2_df.rename(columns={'피처': '금연구역 개수'}, inplace=True)
data2_df


# In[545]:


data_df=pd.merge(data_df,data2_df,on='도로명',how='left')
data_df['금연구역 개수']= data_df['금연구역 개수'].fillna(0).astype('int')
data_df


# # 문화유통업소

# In[546]:


data1_df=pd.read_csv("C:\\Users\\intae\\Desktop\\공모전\\문화유통업소.csv",encoding='cp949')
data1_df.head(5)


# In[547]:


data1_df = data1_df[['영업소소재지(도로명)']]
data1_df[['a','b','도로명','c']]=data1_df['영업소소재지(도로명)'].str.split(' ', n=3, expand=True)
data1_df=data1_df.drop(['영업소소재지(도로명)','a','b','c'],axis=1,inplace=False)
data1_df


# In[548]:


data2_df= preprocessing(data1_df)
data2_df.rename(columns={'피처': '문화유통업소 개수'}, inplace=True)
data2_df


# In[549]:


data_df=pd.merge(data_df,data2_df,on='도로명',how='left')
data_df['문화유통업소 개수']= data_df['문화유통업소 개수'].fillna(0).astype('int')
data_df


# # 임대주택

# In[550]:


data1_df=pd.read_csv("C:\\Users\\intae\\Desktop\\공모전\\임대주택.csv",encoding='cp949')
data1_df


# In[551]:


data1_df = data1_df[['임대물건지 주소']]
data1_df['임대물건지 주소'] = data1_df['임대물건지 주소'].str.lstrip()
data1_df


# In[552]:


data1_df[['a','도로명','b']]=data1_df['임대물건지 주소'].str.split(' ', n=2, expand=True)
data1_df=data1_df.drop(['임대물건지 주소','a','b'],axis=1,inplace=False)
data1_df


# In[553]:


data2_df= preprocessing(data1_df)
data2_df.rename(columns={'피처': '임대주택 개수'}, inplace=True)
data2_df


# In[554]:


data_df=pd.merge(data_df,data2_df,on='도로명',how='left')
data_df['임대주택 개수']= data_df['임대주택 개수'].fillna(0).astype('int')
data_df


# In[557]:


data_df.to_csv("C:\\Users\\intae\\Desktop\\공모전\\동작구.csv",header=True,index=False)

