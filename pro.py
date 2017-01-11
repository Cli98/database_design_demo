from dataBase import *
from dataExtrc import *
import matplotlib.pyplot as plt
import numpy as np
user=dataBase()
user.welcome()
user.preDB()
dataext=dataExtrc()
result=user.openDB(dataext)

#plt.plot(result['total_power'])
#plt.show()
y_list=list(result['total_power'])
time_std=list(result.index)

x=np.matrix(time_std).T
y=np.matrix(result['total_power']).T

mean=np.mean(x)
std=np.std(x)

for i in range(len(list(result.index))):
    time_std[i]=(time_std[i]-mean)/std

x=np.matrix(time_std).T
length=len(y)

plt.plot(x,y,'r+')
#plt.show()

pre=np.ones((length,1))
pre=np.matrix(pre)
x=np.hstack((pre,x))

#linear regression implementation
theta=np.zeros(2)
iteration=1500
alpha=0.2


def cost_Function(X,y,theta):
    theta=np.matrix(theta)
    length=len(y)
    H=X*theta.T
    J=sum((H-y).T*(H-y))/2/length
    return float(J)
res=cost_Function(x,y,theta)

def gradient_Descent(X,y,theta,iteration,alpha):
    length=len(y)
    his=[]
    theta1=list(theta)
    for i in range(iteration):
        theta2=np.matrix(theta1)
        #print(theta2)
        H=X*theta2.T
       
        a=sum(np.array((H-y))*np.array((X[: ,0])))*alpha/length
        b=sum(np.array((H-y))*np.array((X[: ,1])))*alpha/length
        #print(a,b)
        theta1[0]=float(theta1[0]-a)
        theta1[1]=float(theta1[1]-b)
        
        #theta=np.array(theta1)
        #print(theta1)
        #his.append(float(cost_Function(X,y,np.array(theta1))))
        #print(his[i])
    return theta1
theta=gradient_Descent(x,y,theta,iteration,alpha)

#visualization
theta=np.matrix(theta)
plt.plot(x[: ,1],x*theta.T,'b')
plt.xlabel("time in percentage")
plt.ylabel("total power")
plt.title("linear regression results")
plt.show()

#predict modular
counter=0
range_s=(max(y_list)-min(y_list))/100
for i in range(len(time_std)):
    predict=sum(sum(np.array([1, time_std[i]]) *np.array(theta)));
    if abs(predict-y_list[i])<range_s:
        counter=counter+1
print('if we allowed a error rate of 1%')
print('the successful rate is: '+str(counter*100.0/len(time_std))+"%")

