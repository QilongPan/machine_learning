import pandas as pd 
class Data(object):

    def __init__(self):
        pass

    def data1(self):
        #根据天气判断是否会去打球
        #columns:outlook temperature humidity    windy
        X = [
            ['sunny','hot', 'high','FALSE'],
            ['sunny', 'hot','high','TRUE'],
            ['overcast','hot','high','FALSE'],
            ['rainy','mild',    'high',    'FALSE'],
            ['rainy',   'cool' ,   'normal',  'FALSE'],
            ['rainy',   'cool'  ,  'normal' , 'TRUE' ],
            ['overcast',    'cool' ,   'normal','TRUE'],
            ['sunny',   'mild','high', 'FALSE'],
            ['sunny',   'cool','normal','FALSE'],
            ['rainy',   'mild','normal','FALSE'],
            ['sunny',   'mild','normal','TRUE'],
            ['overcast',    'mild',    'high',    'TRUE'],
            ['overcast','hot', 'normal',  'FALSE'],
            ['rainy','mild','high','TRUE']
            ]
        #0表示不去，1表示去
        #label play
        Y = [0,0,1,1,1,0,1,0,1,1,1,1,1,0]
        return X,Y

def test_data1():
    data = Data()
    X,Y = data.data1()
    df = pd.DataFrame(X,columns = ['outlook','temperature','humidity','windy'])
    print(df)

if __name__ == "__main__":
    test_data1()



