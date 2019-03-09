from sklearn import tree
import graphviz

x = [[0,0],[1,1]]
y = [0,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)
dot_data = tree.export_graphviz(clf,out_file = None)
gra = graphviz.Source(dot_data)
gra.render("test")
print(gra)
print(clf.predict([[2,2]]))