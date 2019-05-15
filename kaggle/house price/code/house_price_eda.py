#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import warnings
warnings.filterwarnings('ignore')


# In[3]:


#读取数据
df_train = pd.read_csv("../input/train.csv")
df_train.head()


# In[4]:


df_train.shape


# In[5]:


df_train_x = df_train.iloc[:,0:-1]
df_train_x.shape


# In[6]:


df_train_x.head()


# In[7]:


df_test_x = pd.read_csv("../input/test.csv")
df_test_x.head()


# In[8]:


df_test_x.shape


# In[9]:


#合并测试集与训练集
df_train_and_test_x = pd.concat([df_train_x,df_test_x],ignore_index=True,axis = 0)
df_train_and_test_x.shape


# 

# In[10]:


df_train_and_test_x.head()


# In[11]:


df_train_and_test_x.tail()


# In[12]:


df_train_and_test_x.info()


# In[13]:


#计算每列的缺失率
df_train_and_test_x_missing_rate = df_train_and_test_x.isna().sum() / df_train_and_test_x.shape[0]
print(df_train_and_test_x_missing_rate)


# In[14]:


#删除缺失值大于0.5的
drop_miss_names = df_train_and_test_x_missing_rate[df_train_and_test_x_missing_rate > 0.5].index
print(drop_miss_names)
df_train_and_test_x.drop(drop_miss_names,axis = 1,inplace=True)


# In[15]:


df_train_and_test_x.shape


# In[16]:


#填充缺失值
df_train_and_test_x_columns = df_train_and_test_x.columns
df_train_and_test_x_dtypes = df_train_and_test_x.dtypes
from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values = np.nan,strategy='most_frequent')
df_train_and_test_x = pd.DataFrame(imp.fit_transform(df_train_and_test_x),columns = df_train_and_test_x_columns)
#设置df类型
for i in range(len(df_train_and_test_x_dtypes.values)):
    df_train_and_test_x[df_train_and_test_x_columns[i]] = df_train_and_test_x[df_train_and_test_x_columns[i]].astype(df_train_and_test_x_dtypes.values[i])
df_train_and_test_x.dtypes


# In[17]:


df_train_and_test_x.isna().sum() / df_train_and_test_x.shape[0]


# In[18]:


#将中文类别标签化
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
for column_name in df_train_and_test_x_columns:
    if df_train_and_test_x[column_name].dtypes == "object":
        print(column_name)
        encoder = LabelEncoder()  
        trans = encoder.fit_transform(df_train_and_test_x[column_name].values)  
        trans = np.array([trans]).T
        enc = OneHotEncoder()
        hot=enc.fit_transform(trans)
        hot=hot.toarray()
        df_hot = pd.DataFrame(hot,columns = [column_name+str(i) for i in range(hot.shape[1])])
        df_train_and_test_x = pd.concat([df_train_and_test_x,df_hot],axis=1)
        df_train_and_test_x = df_train_and_test_x.drop([column_name],axis=1)
df_train_and_test_x.head()


# In[19]:


#删除ID列
df_train_and_test_x.drop(['Id'],inplace = True,axis = 1)


# In[20]:


df_train_and_test_x.head()


# In[21]:


#数据降维
from sklearn.decomposition import PCA
pca = PCA(n_components = 200)
train_test_x = pca.fit(df_train_and_test_x).transform(df_train_and_test_x)


# In[22]:


train_test_x.shape


# In[23]:


type(train_test_x)


# In[31]:


train_x = train_test_x[0:1460,:]
test_x = train_test_x[1460:,:]


# In[32]:


train_x.shape


# In[33]:


test_x.shape


# In[34]:


train_y = df_train.iloc[:,-1:].values


# In[35]:


train_y.shape


# In[40]:


#模型训练
import xgboost as xgb

model  = xgb.XGBRegressor(max_depth = 5,learning_rate=0.1,n_estimators = 500,silent=False,reg_alpha=1,reg_lambda=0.6)
model.fit(train_x,train_y)
print("complish....")


# In[42]:


test_y = model.predict(test_x)


# In[43]:


print(test_y)


# In[44]:


test_y_arr = [[i] for i in test_y]


# In[45]:


print(test_y_arr)


# In[46]:


df_submission = pd.DataFrame()
df_SalePrice = pd.DataFrame(data = test_y_arr,columns = ['SalePrice'])


# In[47]:


id_arr = [[i] for i in range(1461,2920)]
df_id = pd.DataFrame(data = id_arr,columns = ['Id'])


# In[48]:


df_submission = pd.concat([df_id,df_SalePrice],axis = 1)
df_submission


# In[50]:


df_submission = df_submission.reindex([i for i in range(1,1459)])
df_submission


# In[52]:


df_submission.to_csv("sample_submission2.csv")


# In[ ]:


#读取数据
df_train = pd.read_csv("../input/train.csv")
df_test = pd.read_csv("../input/test.csv")
print("read data complish....")


# In[ ]:


df_train.head()


# In[ ]:


df_train.info()


# In[ ]:


df_test.head()


# In[ ]:


df_test.info()


# In[ ]:


#计算每列的缺失率
df_train_missing_rate = df_train.isna().sum() / df_train.shape[0]
print(df_train_missing_rate)


# In[ ]:


type(df_train_missing_rate)


# In[ ]:


have_miss_names = df_train_missing_rate[df_train_missing_rate > 0].index
print(have_miss_names)


# In[ ]:


#删除缺失值大于0.5的
drop_miss_names = df_train_missing_rate[df_train_missing_rate > 0.5].index
print(drop_miss_names)
df_train.drop(drop_miss_names,axis = 1,inplace=True)
df_test.drop(drop_miss_names,axis = 1, inplace=True)


# In[ ]:


if 'Alley' not in df_test.columns:
    print("drop sucess")


# In[ ]:


df_train_columns = df_train.columns
df_test_columns = df_test.columns
df_train_dtypes = df_train.dtypes
df_test_dtypes = df_test.dtypes


# In[ ]:


#填充缺失值
from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values = np.nan,strategy='most_frequent')
df_train = pd.DataFrame(imp.fit_transform(df_train),columns = df_train_columns)
for i in range(len(df_train_dtypes.values)):
    df_train[df_train_columns[i]] = df_train[df_train_columns[i]].astype(df_train_dtypes.values[i])
df_train.dtypes


# In[ ]:


df_test = pd.DataFrame(imp.fit_transform(df_test),columns = df_test_columns)
for i in range(len(df_test_dtypes.values)):
    df_test[df_test_columns[i]] = df_test[df_test_columns[i]].astype(df_test_dtypes.values[i])
df_test.dtypes


# In[ ]:


df_test.isna().sum() / df_test.shape[0]


# In[ ]:


df_test.head()


# In[ ]:


from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import warnings
warnings.filterwarnings('ignore')
df_train.columns
for column_name in df_train_columns:
    if df_train[column_name].dtypes == "object":
        print(column_name)
        encoder = LabelEncoder()  
        trans = encoder.fit_transform(df_train[column_name].values)  
        trans = np.array([trans]).T
        enc = OneHotEncoder()
        hot=enc.fit_transform(trans)
        hot=hot.toarray()
        df_hot = pd.DataFrame(hot,columns = [column_name+str(i) for i in range(hot.shape[1])])
        df_train = pd.concat([df_train,df_hot],axis=1)
        df_train = df_train.drop([column_name],axis=1)


# In[ ]:


df_train.head()


# In[ ]:


for column_name in df_test_columns:
    if df_test[column_name].dtypes == "object":
        print(column_name)
        encoder = LabelEncoder()  
        trans = encoder.fit_transform(df_test[column_name].values)  
        trans = np.array([trans]).T
        enc = OneHotEncoder()
        hot=enc.fit_transform(trans)
        hot=hot.toarray()
        df_hot = pd.DataFrame(hot,columns = [column_name+str(i) for i in range(hot.shape[1])])
        df_test = pd.concat([df_test,df_hot],axis=1)
        df_test = df_test.drop([column_name],axis=1)


# In[ ]:


df_test.head()


# In[ ]:


#删除ID列
df_train.drop(['Id'],inplace = True,axis = 1)
df_test.drop(['Id'],inplace = True,axis = 1)


# In[ ]:


df_train.head()


# In[ ]:


df_train_y = df_train['SalePrice']
df_train_x = df_train.drop(['SalePrice'],axis = 1)
df_train_x.shape


# In[ ]:


df_train_y.shape


# In[ ]:


df_test_x = df_test.copy()


# In[ ]:


df_test_x.head()


# In[ ]:


df_test_x.shape


# In[ ]:


df_train_x.shape


# In[ ]:


#数据降维
from sklearn.decomposition import PCA
pca = PCA(n_components = 200)
train_x = pca.fit(df_train_x).transform(df_train_x)
test_x = pca.fit(df_train_x).transform(df_test_x)


# In[ ]:



import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

def analysis_column(df_train):
    df_row_nums,df_column_nums = df_train.shape
    current_index = 1
    for column_name in df_train.columns:
        print(column_name)
        plt.subplot(df_column_nums,1,current_index)
        miss_rate = df_train[column_name].isna().sum(axis = 0)/df_row_nums
    #    print("缺失率:{0}".format(miss_rate))
        if df_train[column_name].dtypes == "int":
            if current_index == 1:
                print(df_train[column_name])
                plt.scatter(range(df_row_nums),df_train[column_name])
            current_index = current_index + 1
        '''
        elif df_train[column_name].dtypes == "object":
            print("每个值得数量")
            value_counts = df_train[column_name].value_counts()
            print(value_counts)
        '''
#分析每列数据的基本属性
analysis_column(df_train)
plt.show()


# In[ ]:


def deal_data(df_train):
    df_row_nums,df_column_nums = df_train.shape
    for column_name in df_train.columns:
        miss_rate = df_train[column_name].isna().sum(axis = 0)/df_row_nums
        if df_train[column_name].dtypes == "object" and miss_rate == 0:
            
    


# In[ ]:


train_column_num = df_train.shape[1]
df_train_x = df_train.iloc[:,0:train_column_num-1]
df_train_y = df_train.iloc[:,train_column_num-1:train_column_num]
print("complish")


# In[ ]:


df_train_x.head()


# In[ ]:


df_train_y.head()


# In[ ]:


df_train_x.fillna(0)
df_train_y.fillna(0)
from sklearn.svm import SVR
l_svr = SVR(kernel='linear')
l_svr.fit(df_train_x,df_train_y)
l_svr.score(df_train_x,df_train_y)


# In[ ]:


#查看基本信息
df_train.info()


# In[ ]:


#查看每个字段的缺失率
df_train.isna().sum()/df_train.shape[0]

