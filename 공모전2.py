#!/usr/bin/env python
# coding: utf-8

# In[21]:


#!/usr/bin/env python3
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
pd.set_option('display.max_rows', 700)
data_df=pd.read_csv("C:\\Users\\intae\\Desktop\\동작구 빅데이터 공모전\\dataset\\동작구.csv",encoding='euc-kr')


# In[22]:


data_df


# In[23]:


data1_df=np.zeros((6,11))
data1_df=pd.DataFrame(data1_df,columns=[data_df.columns])
data1_df= data1_df.drop('도로명',axis=1, inplace=False)
data1_df['지표']=np.zeros((6,))
data1_df.columns=['지표','안전비상벨 개수','CCTV 카메라 개수','담배소매인 지정 업소 개수','음식점 개수',
                 '보안등 개수','아파트 세대 수','과속방지턱 개수','금연구역 개수','문화유통업소 개수','임대주택 개수']
eva=['최솟값','최댓값','평균','중앙값','분산','표준편차']
for i in range(6):
    data1_df.loc[i,'지표']=eva[i]

data1_df


# In[24]:


for col in range(1,11):
    data1_df.iloc[0,col] = data_df[[data_df.columns[col]]].min().values
    
for col in range(1,11):
    data1_df.iloc[1,col]=data_df[[data_df.columns[col]]].max().values

for col in range(1,11):
    data1_df.iloc[2,col] = np.round(data_df[[data_df.columns[col]]].mean().values,3)
    
for col in range(1,11):
    data1_df.iloc[3,col] = data_df[[data_df.columns[col]]].median().values

for col in range(1,11):
    data1_df.iloc[4,col] = np.round(data_df[[data_df.columns[col]]].var().values,3)
    
for col in range(1,11):
    data1_df.iloc[5,col] = np.round(data_df[[data_df.columns[col]]].std().values,3)


# In[25]:


data1_df


# In[26]:


pd.options.display.float_format = '{:,.2f}'.format
data1_df


# In[27]:


data_df['안전비상벨 개수'].hist(grid=False)
plt.title('Emergency bell')
plt.show()


# In[28]:


data_df['CCTV 카메라 개수'].hist(grid=False)
plt.title('CCTV')
plt.show()


# In[29]:


data_df['담배소매인 지정 업소 개수'].hist(grid=False)
plt.title('The cigarettes retailer')
plt.show()


# In[30]:


data_df['음식점 개수'].hist(grid=False)
plt.title('Restorant')
plt.show()


# In[31]:


data_df['보안등 개수'].hist(grid=False)
plt.title('Security lights')
plt.show()


# In[32]:


data_df['아파트 세대 수'].hist(grid=False)
plt.title('Apartment')
plt.show()


# In[33]:


data_df['과속방지턱 개수'].hist(grid=False)
plt.title('Speed dump')
plt.show()


# In[34]:


data_df['금연구역 개수'].hist(grid=False)
plt.title('No smoking area')
plt.show()


# In[35]:


data_df['문화유통업소 개수'].hist(grid=False)
plt.title('Cultural distribution center')
plt.show()


# In[36]:


data_df['임대주택 개수'].hist(grid=False)
plt.title('Rental house')
plt.show()


# In[37]:


data_df


# In[38]:


data_df.columns=['도로명','Emergency bell','CCTV','The cigarettes retailer','Restorant','Security lights',
                'Apartment','Speed dump','No smoking area','Cultural distribution center','Rental house']
corr=data_df.corr()
plt.figure(figsize=(10,10))
plt.title('Correlation by each feature')
sns.heatmap(corr,annot=True,fmt='.1g')


# In[92]:


data2_df=np.zeros((1,10))
data2_df=pd.DataFrame(data2_df,columns=['안전비상벨 개수','CCTV 카메라 개수','담배소매인 지정 업소 개수','음식점 개수',
                 '보안등 개수','아파트 세대 수','과속방지턱 개수','금연구역 개수','문화유통업소 개수','임대주택 개수'])
data2_df


# In[93]:



for col_num in range(1,11):
    nums=[]
    for num in data_df.iloc[:,col_num]:
        
        if num==0:
            nums.append(num)
    data2_df.iloc[0,col_num-1] = len(nums)        
    
data2_df= data2_df.astype(int)
data2_df


# In[96]:


for col_num in range(0,10):
    data2_df.iloc[0,col_num]=str(np.round((data2_df.iloc[0,col_num] / 685)*100,2)) +str('%')
    
data2_df


# In[ ]:




