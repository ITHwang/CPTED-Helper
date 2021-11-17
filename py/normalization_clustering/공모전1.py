#!/usr/bin/env python
# coding: utf-8

# In[172]:


#!/usr/bin/env python3
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
pd.set_option('display.max_rows', 700)
data_df=pd.read_csv("C:\\Users\\intae\\Desktop\\공모전\\동작구.csv",encoding='euc-kr')
data_df.head(5)


# In[173]:


corr=data_df.corr()
plt.figure(figsize=(10,10))
sns.heatmap(corr,annot=True,fmt='.1g')


# In[174]:


from sklearn.decomposition import TruncatedSVD, PCA
from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()
tsvd=TruncatedSVD(n_components=2)

data_df=data_df.drop(['도로명'], axis=1,inplace=False)
data_df_scaled=np.log1p(data_df)
data_df_scaled_standard=StandardScaler().fit_transform(data_df_scaled)
from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=3,init='k-means++',max_iter=300,random_state=0).fit(data_df_scaled_standard)
print(kmeans.labels_)


# In[175]:


data_df=pd.DataFrame(data=data_df_scaled_standard,columns=['안전비상벨','cctv','담배소매인','음식점','보안등','아파트 세대','과속방지턱',                                                          '금연구역','문화유통업','임대주택'])


# In[176]:


data_df['clusters']=kmeans.labels_


# In[177]:


from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca_transformed=pca.fit_transform(data_df)

data_df['pca_x'] = pca_transformed[:,0]
data_df['pca_y'] = pca_transformed[:,1]
data_df.head(3)


# In[178]:


# cluster 값이 0, 1, 2 인 경우마다 별도의 Index로 추출
marker0_ind = data_df[data_df['clusters']==0].index
marker1_ind = data_df[data_df['clusters']==1].index
marker2_ind = data_df[data_df['clusters']==2].index

# cluster값 0, 1, 2에 해당하는 Index로 각 cluster 레벨의 pca_x, pca_y 값 추출. o, s, ^ 로 marker 표시
plt.scatter(x=data_df.loc[marker0_ind,'pca_x'], y=data_df.loc[marker0_ind,'pca_y'], marker='o') 
plt.scatter(x=data_df.loc[marker1_ind,'pca_x'], y=data_df.loc[marker1_ind,'pca_y'], marker='s')
plt.scatter(x=data_df.loc[marker2_ind,'pca_x'], y=data_df.loc[marker2_ind,'pca_y'], marker='^')

plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.show()


# In[179]:


data1_df=pd.read_csv("C:\\Users\\intae\\Desktop\\공모전\\동작구.csv",encoding='euc-kr')
data1_df=data1_df[['도로명']]
data_df=pd.concat([data1_df,data_df],axis=1)
data_df


# In[180]:


clusters_df=pd.DataFrame(columns=['cluster 개수','안전비상벨 개수','CCTV 카메라 개수','문화유통업소 개수','보안등 개수','과속방지턱 개수',                  '음식점 개수','담배소매인 지정 업소 개수','금연구역 개수','임대주택 개수','아파트 세대 수'])
for i in list(range(3)):
    index=data_df[data_df['clusters']==i].index
    data1_df=pd.read_csv("C:\\Users\\intae\\Desktop\\공모전\\동작구.csv",encoding='euc-kr')
    data1_df=data1_df[['안전비상벨 개수','CCTV 카메라 개수','문화유통업소 개수','보안등 개수','과속방지턱 개수',                  '음식점 개수','담배소매인 지정 업소 개수','금연구역 개수','임대주택 개수','아파트 세대 수']]
    data1_df=data1_df.loc[index]
    summm=data_df[data_df['clusters']==i]['도로명'].count()
    print(summm)
    clusters_df.loc[i,'cluster 개수']=summm
    for column in data1_df.columns:
        summ =data1_df[column].sum().sum()
        print('cluster {0}에서 칼럼 {1}의 count'.format(i,column))
        print(summ)
        clusters_df.loc[i,column] =summ

clusters_df


# In[181]:


clusters_mean_df=pd.DataFrame(columns=[])
for ind in list(range(3)):
    for col in np.arange(start=1,stop=11):
        a=np.round((clusters_df.iloc[ind,col]/clusters_df.iloc[ind,0]),3)
        clusters_mean_df.loc[ind,col-1]=a

clusters_mean_df.columns = ['평균 안전비상벨 개수','평균 CCTV 카메라 개수','평균 문화유통업소 개수','평균 보안등 개수',                           '평균 과속방지턱 개수','평균 음식점 개수','평균 담배소매인 지정 업소 개수','평균 금연구역 개수',                           '평균 임대주택 개수','평균 아파트 세대 수']
clusters_mean_df


# In[182]:


# 각 피처별 0번 지역 대비 1번 지역 비율

clusters_mean_sel_df=clusters_mean_df[['평균 안전비상벨 개수','평균 CCTV 카메라 개수','평균 보안등 개수',                                          '평균 임대주택 개수','평균 아파트 세대 수']]
summs=[]
for ind in list(range(3)):
    summ=clusters_mean_sel_df.iloc[ind,3]+clusters_mean_sel_df.iloc[ind,4]
    summs.append(summ)
clusters_mean_sel_df['추정 가구 수']=summs
clusters_mean_sel_df


# In[183]:


clusters_mean_sel_df=clusters_mean_sel_df.drop(2,inplace=False)
clusters_mean_sel_df=clusters_mean_sel_df.drop(['평균 임대주택 개수','평균 아파트 세대 수'],inplace=False,axis=1)
clusters_mean_sel_df


# In[184]:


pers=[]
for iter_ in list(range(4)):
    per=str(np.round((clusters_mean_sel_df.iloc[1,iter_]/clusters_mean_sel_df.iloc[0,iter_])*100,3))+str('%')
    pers.append(per)
clusters_mean_sel_df.loc[2]=pers
clusters_mean_sel_df


# In[185]:


index=data_df[data_df['clusters']==1].index
data1_df=pd.read_csv("C:\\Users\\intae\\Desktop\\공모전\\동작구.csv",encoding='euc-kr')
data2_df=data1_df.loc[index]
data2_df.columns = ['도로명','안전비상벨 개수','CCTV 카메라 개수','문화유통업소 개수','보안등 개수',                           '과속방지턱 개수','음식점 개수','담배소매인 지정 업소 개수','금연구역 개수',                           '임대주택 개수','아파트 세대 수']
data2_df


# In[186]:


# 대로 행 삭제하고 reindex
data2_df=data2_df.drop(3,inplace=False)
data2_df=data2_df.reset_index().drop(['index'],axis=1,inplace=False)
data2_df


# In[187]:


# 임대주택, 아파트 세대 거르기
index_sort_popul=data2_df[data2_df['임대주택 개수']+data2_df['아파트 세대 수']>30].index
data2_df=data2_df.loc[index_sort_popul]
data2_df=data2_df.reset_index().drop(['index'],axis=1,inplace=False)
data2_df


# In[188]:


#안전 비상벨, CCTV 카메라 개수, 보안등 개수 null
index_sort_null=data2_df[data2_df['안전비상벨 개수']+data2_df['CCTV 카메라 개수']+data2_df['보안등 개수']==0].index
data2_df=data2_df.loc[index_sort_null]
data2_df.sort_values(by='아파트 세대 수',ascending=False)

data2_df=data2_df.reset_index().drop(['index'],axis=1,inplace=False)
data2_df

