#姓名：杨普伦
#学号：20161152092
print("利用绘图工具展示决策树结构")
#-*- coding: utf-8 -*-
# {{{
from io import StringIO
import pandas
import pydotplus
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
def createDataSet():
    """
    创建数据集

    :return: 数据集与特征集
    """
    dataSet = [['hot', 'sunny', 'high', 'false', 'no'],
               ['hot', 'sunny', 'high', 'true', 'no'],
               ['hot', 'overcast', 'high', 'false', 'yes'],
               ['cool', 'rain', 'normal', 'false', 'yes'],
               ['cool', 'overcast', 'normal', 'true', 'yes'],
               ['mild', 'sunny', 'high', 'false', 'no'],
               ['cool', 'sunny', 'normal', 'false', 'yes'],
               ['mild', 'rain', 'normal', 'false', 'yes'],
               ['mild', 'sunny', 'normal', 'true', 'yes'],
               ['mild', 'overcast', 'high', 'true', 'yes'],
               ['hot', 'overcast', 'normal', 'false', 'yes'],
               ['mild', 'sunny', 'high', 'true', 'no'],
               ['cool', 'sunny', 'normal', 'true', 'no'],
               ['mild', 'sunny', 'high', 'false', 'yes']]
    labels = ['climate', 'weather', 'temple', 'cold']
    return dataSet, labels
if __name__ == '__main__':
    dataSet, labels = createDataSet()
    yDataList = []  # 提取每组数据的类别，保存在列表里
    for each in dataSet:
        yDataList.append(each[-1])
    dataDict = {}
    for each_label in labels:
        tempList = list()
        for each in dataSet:
            tempList.append(each[labels.index(each_label)])
        dataDict[each_label] = tempList
    dataPD = pandas.DataFrame(dataDict)

    leDict = dict()
    for col in dataPD.columns:
        leDict[col] = LabelEncoder()
        dataPD[col] = leDict[col].fit_transform(dataPD[col])
    dt = DecisionTreeClassifier()
    dt.fit(dataPD.values.tolist(), yDataList)

    dot_data = StringIO()
    tree.export_graphviz(dt, out_file=dot_data,  # 绘制决策树
                         feature_names=dataPD.keys(),
                         class_names=dt.classes_,
                         filled=True, rounded=True,
                         special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.progs = {'dot': u"C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe"}
    graph.write_pdf("tree.pdf")

    xTest = [['hot', 'overcast', 'high', 'false'], ['mild', 'sunny', 'high', 'true']]
    testDict = {}
    for each_label in labels:
        tempList = list()
        for each in xTest:
            tempList.append(each[labels.index(each_label)])
        testDict[each_label] = tempList
    testPD = pandas.DataFrame(testDict)  # 生成pandas.DataFrame
    for col in testPD.columns:  # 为每一列序列化
        testPD[col] = leDict[col].transform(testPD[col])

    result = dt.predict(testPD.values.tolist())
    print(result)

dot_data = StringIO()
tree.export_graphviz(dt, out_file=dot_data,  # 绘制决策树
		     feature_names=dataPD.keys(),
		     class_names=dt.classes_,
		     filled=True, rounded=True,
		     special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("tree.pdf")















