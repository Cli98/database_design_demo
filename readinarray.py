import numpy as np
combine=np.load('date13.npy')
counter=0
for i in range(14,31):
    filename='date'+str(i)+'.npy'
    counter+=1
    temp=np.load(filename)
    combine=np.vstack((combine,temp))
test=np.load('date31.npy')
print(combine.shape)    
    
