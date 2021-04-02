import random
import numpy as np

label=[]
for i in range(15):
    feature = random.randint(6, 20)
    print(feature,end=' ')
    label.append( 3*feature + 4)

print(f"\nlabel= {label}")

#other method
#------------------
feature = np.arange(6, 21)
print(f"\n{feature}")
label = (feature * 3) + 4
print(label)