import matplotlib.pyplot as plt
import numpy as np
mode_transport=np.array(['Walking','Cycling','Car','Bus','Train'])
freq=np.array([29,15,35,18,3])
plt.title('Anjali E V\n23MCA016',loc='right')
plt.xlabel('Mode of Transport')
plt.ylabel('Frequency')
plt.bar(mode_transport,freq,width=0.1,color='green')
plt.show()