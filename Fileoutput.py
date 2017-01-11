from dataBase import *
from dataExtrc import *
import matplotlib.pyplot as plt
import numpy as np
user=dataBase()
user.welcome()
user.preDB()
dataext=dataExtrc()
result=user.openDB(dataext)
result=np.array(result['total_power'])
#print(len(result))
#if len(result)<3378:
#    result=np.array(result)
#    result=np.hstack((result,np.array(2000)))
np.save('date1',result)


