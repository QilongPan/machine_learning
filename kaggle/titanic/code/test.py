import pandas as pd 
import numpy as np 
from pandas import Series,DataFrame 
from sklearn.linear_model import LinearRegression 
#训练集交叉验证，得到平均值
from sklearn.model_selection import KFold
import numpy as np

data_train = pd.read_csv("E:/machine_learning/kaggle/titanic/data/train.csv")
data_test = pd.read_csv("E:/machine_learning/kaggle/titanic/data/test.csv")
#Age列中的缺失值用Age中位数进行填充
data_train["Age"] = data_train['Age'].fillna(data_train['Age'].median()) 
#Sex性别列处理：male用0，female用1
data_train.loc[data_train["Sex"] == "male","Sex"] = 0
data_train.loc[data_train["Sex"] == "female","Sex"] = 1
#缺失值用最多的S进行填充
data_train["Embarked"] = data_train["Embarked"].fillna('S') 
#地点用0,1,2
data_train.loc[data_train["Embarked"] == "S","Embarked"] = 0    
data_train.loc[data_train["Embarked"] == "C","Embarked"] = 1
data_train.loc[data_train["Embarked"] == "Q","Embarked"] = 2

#新增：对测试集数据进行预处理，并进行结果预测
#Age列中的缺失值用Age均值进行填充
data_test["Age"] = data_test["Age"].fillna(data_test["Age"].median())
#Fare列中的缺失值用Fare最大值进行填充
data_test["Fare"] = data_test["Fare"].fillna(data_test["Fare"].max()) 
 
#Sex性别列处理：male用0，female用1
data_test.loc[data_test["Sex"] == "male","Sex"] = 0
data_test.loc[data_test["Sex"] == "female","Sex"] = 1
#缺失值用最多的S进行填充
data_test["Embarked"] = data_test["Embarked"].fillna('S') 
#地点用0,1,2
data_test.loc[data_test["Embarked"] == "S","Embarked"] = 0    
data_test.loc[data_test["Embarked"] == "C","Embarked"] = 1
data_test.loc[data_test["Embarked"] == "Q","Embarked"] = 2
#选取简单的可用输入特征
predictors = ["Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]    
'''
#初始化现行回归算法
alg = LinearRegression()
#样本平均分成3份，3折交叉验证
#kf = KFold(data_train.shape[0],n_folds=3,random_state=1)   
kf = KFold(n_splits=3,shuffle=False,random_state=1) 
 
predictions = []
for train,test in kf.split(data_train):
	#The predictors we're using to train the algorithm.  Note how we only take then rows in the train folds.
	train_predictors = (data_train[predictors].iloc[train,:])
	#The target we're using to train the algorithm.
	train_target = data_train["Survived"].iloc[train]
	#Training the algorithm using the predictors and target.
	alg.fit(train_predictors,train_target)
	#We can now make predictions on the test fold
	test_predictions = alg.predict(data_train[predictors].iloc[test,:])
	predictions.append(test_predictions)
#The predictions are in three aeparate numpy arrays.	Concatenate them into one.
#We concatenate them on axis 0,as they only have one axis.
predictions = np.concatenate(predictions,axis=0)
 
#Map predictions to outcomes(only possible outcomes are 1 and 0)
predictions[predictions>.5] = 1
predictions[predictions<=.5] = 0
accuracy = sum(predictions == data_train["Survived"]) / len(predictions)
print ("准确率为: ", accuracy)
'''
'''
from sklearn import model_selection
#逻辑回归
from sklearn.linear_model import LogisticRegression   
 
#初始化逻辑回归算法
LogRegAlg=LogisticRegression(random_state=1)
re = LogRegAlg.fit(data_train[predictors],data_train["Survived"])
 
#使用sklearn库里面的交叉验证函数获取预测准确率分数
scores = model_selection.cross_val_score(LogRegAlg,data_train[predictors],data_train["Survived"],cv=3)
 
#使用交叉验证分数的平均值作为最终的准确率
print("准确率为: ",scores.mean())

test_features = ["Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"] 
#构造测试集的Survived列，
data_test["Survived"] = -1
 
test_predictors = data_test[test_features]
data_test["Survived"] = LogRegAlg.predict(test_predictors)

'''
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
 
predictors=["Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]
 
'''
#10棵决策树，停止的条件：样本个数为2，叶子节点个数为1
alg=RandomForestClassifier(random_state=1,n_estimators=10,min_samples_split=2,min_samples_leaf=1) 
 
#Compute the accuracy score for all the cross validation folds.  (much simpler than what we did before!)
#kf=cross_validation.KFold(data_train.shape[0],n_folds=3,random_state=1)
kf=model_selection.KFold(n_splits=3,shuffle=False, random_state=1)
 
 
scores=model_selection.cross_val_score(alg,data_train[predictors],data_train["Survived"],cv=kf)
print(scores)
#Take the mean of the scores (because we have one for each fold)
print(scores.mean())

'''
#30棵决策树，停止的条件：样本个数为2，叶子节点个数为1
alg=RandomForestClassifier(random_state=1,n_estimators=100,min_samples_split=2,min_samples_leaf=1) 
train_predictors = (data_train[predictors])
	#The target we're using to train the algorithm.
train_target = data_train["Survived"]
	#Training the algorithm using the predictors and target.
alg.fit(train_predictors,train_target)
predictions = []
test_predictions = alg.predict(data_test[predictors])
predictions.append(test_predictions)
predictions = np.array(predictions).reshape(418,1)
data1 = DataFrame(predictions)
data1.index = range(892,892+len(data1))
data1.to_csv('E:/machine_learning/kaggle/titanic/data/predictions.csv')
print(data1)
