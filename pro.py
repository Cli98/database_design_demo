from dataBase import *
from dataExtrc import *
import matplotlib.pyplot as plt
import numpy as np
user=dataBase()
user.welcome()
user.preDB()
dataext=dataExtrc()
result=user.openDB(dataext)


