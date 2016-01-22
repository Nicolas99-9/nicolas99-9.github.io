import numpy as np
from pprint import pprint
import codecs
import matplotlib.pyplot as plt 
from sklearn import linear_model

dico1 = {'jan' : 1, 'feb' : 2 , 'mar' : 3 , 'apr' : 4 , 'may' : 5 , 'jun' : 6 , 'jul' : 7 , 'aug' : 8 , 'sep' : 9 , 'aug' : 10 , 'oct' : 11 , 'nov' : 11 , 'dec' : 12}


dico2 = {'mon' : 1 , 'tue' : 2 , 'wed' : 3 , 'thu' : 4 ,'fri' : 5 , 'sat' : 6 , 'sun' : 7 }
def get_value(s):
    return dico1[s]
def get_value2(s):
    return dico2[s]

def read_filess(file_name):
    dico = {}
    test = {}
    test_value = {}
    count = 0
    resulat = {}
    with codecs.open(file_name,"r",encoding="utf-8")as my_file:
        for line in my_file:
            line = line.strip()
            code = line.split(",")
            if(count!=0):
		if(count<400):
		        tab = []
		        for s in range(len(code)-2):
			    if(s == 2):
				tab.append(get_value(code[s]))
		            elif (s==3):
				tab.append(get_value2(code[s]))
			    else:
				tab.append(float(code[s]))
		        dico[count] = tab
		        resulat[count]  = float(code[len(code)-1])
		else:
		        tab = []
		        for s in range(len(code)-2):
			    if(s == 2):
				tab.append(get_value(code[s]))
		            elif (s==3):
				tab.append(get_value2(code[s]))
			    else:
				tab.append(float(code[s]))
		        test[count] = tab
		        test_value[count]  = float(code[len(code)-1])			
            count+=1
    pprint(dico)
    return  (dico,resulat,test,test_value)



def regression_linaire2(dicon,value):
    tmp = []
    for s in dicon:
        tmp.append(int(dicon[s][9]))
    x = sorted(tmp)
    x = tmp
    print(x)
    tmp2 = []
    for s in value:
        tmp2.append(int(value[s]))
    y = np.array(tmp2)
    vp = np.polyfit(x,y,1)
    inter_poly = np.poly1d(vp)
    xp = np.linspace(0,6)
    plt.plot(x,y,"r+",xp,inter_poly(xp),"--")
    plt.savefig("test.png")
    plt.show()

    print(inter_poly(25))
    

    
'''
def regression_linaire(dicon,value):
    tmp = []
    for s in dicon:
        count = 0
        tmp3 = []
        for tt in dicon[s]:
            if(not (count == 2 or count ==3)): 
                tmp3.append(float(tt))
            count +=1
        tmp.append(tmp3)
    x = np.array(tmp)
    #x = tmp
    tmp2=[]
    for s in value:
            tmp2.append(int(value[s]))
    y = np.array(tmp2)
    for X in x:
        print("len y :",len(y),"len x ",len(X))
    fit = np.array([np.polyfit(X,y,len(x[0])) for X in x])
    vp = np.polynomial.polynomial.polyfit(x,y,len(x[0]))
    inter_poly = np.poly1d(vp)
    xp = np.linspace(0,800)
    plt.plot(x,y,"r+",xp,inter_poly(xp),"--")
    plt.savefig("test.png")
    plt.show()
    
       X = np.arange(3)
    Y = np.random.rand(10000, 3)

    fit = np.array([np.polyfit(X, y, 2) for y in Y])
fits = np.polynomial.polynomial.polyfit(X, Y.T, 2)

assert np.allclose(fit.T[::-1], fits)
    '''
    
def question1(model):
    e1 = raw_input("x-axis spatial coordinate within the Montesinho park map: 1 to 9 ")
    e2 = raw_input(" y-axis spatial coordinate within the Montesinho park map: 2 to 9 ")
    e3 = raw_input("month ? (1...12)")
    e4 = raw_input("days (1...7)")
    e5 = raw_input("FFMC (18.7 to 96.20)")
    e6 = raw_input("DMC  ( 1.1 to 291.3 )")
    e7 = raw_input("DC (7.9 to 860.6 )")
    #e8 = raw_input("ISI (0.0 to 56.10 )")
    e9 = raw_input("Temperature (2.2 to 33.30 )")
    e10 = raw_input("Humidity (15.0 to 100 )")
    e11 = raw_input("Wind (0.40 to 9.40 )")
    e12 = raw_input("Rain mm (0.0 to 6.4 )")
    print([e1,e2,e3,e4,e5,e6,e7,e9,e10,e11,e12])
    print("area estimate of the fire (in ha)  : " ,  model.predict([float(e1),float(e2),float(e3),float(e4),float(e5),float(e6),float(e7),float(e9),float(e10),float(e11),float(e12)])) 




def regression_linaire(dicon,value,test,test_value):
    clf = linear_model.LinearRegression()
    clf.fit(dicon.values(),value.values())
    print("coefficient : " ,clf.coef_)
    print("score de la regression lineaire simple : ", clf.score(test.values(),test_value.values()))
    question1(clf)

(dico,value,test,test_value)  = read_filess("forestfires.csv")
pprint(dico)
regression_linaire(dico,value,test,test_value)
