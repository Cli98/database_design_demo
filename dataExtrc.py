import pandas as pd
import pickle
import math
from time_trans import *
class dataExtrc(object):
    def __init__(self):
        self.real_power_matrix=[]
        self.reactive_power_matrix=[]
        self.total_power=[]
        self.time_matrix=[]

    def result(self,cursor):
        #n=0
        for entry in cursor:
            data = [pickle.loads(entry['rawData'])][0]
            self.real_power_matrix.append(sum(data[2]))
            self.reactive_power_matrix.append(sum(data[3]))
            self.total_power.append(math.sqrt(sum(data[2])**2+sum(data[3])**2))
            #self.time_matrix.append(timestamp_datetime(data[-1]))
            self.time_matrix.append(data[-1])
            #n+=1
            #if n>10000:
             #   break

        dict={"real_power":self.real_power_matrix,"reactive_power":self.reactive_power_matrix,'total_power':self.total_power}
        result=pd.DataFrame(dict,index=self.time_matrix)
        return result

    def linear_approximation(self,startDate,control_const=100):
        estimate_const=0.3
        #60047 for a day/1786652 for whole database
        max_Reach=control_const**2
        default_Date="2016-01-13 07:00:00"
        default_Date=datetime_timestamp(default_Date)
        skip_entry=int((startDate-default_Date)*estimate_const)
        if skip_entry>max_Reach:
            skip_entry=max_Reach
        if skip_entry<0:
            skip_entry=0
        return  skip_entry
