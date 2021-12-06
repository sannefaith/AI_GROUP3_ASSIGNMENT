import pandas as pd 
import numpy as np
from numpy import array
from sklearn.preprocessing import Normalizer
from keras.activations import sigmoid
from keras.losses import mse
from numpy.random import uniform

batch_size=2

data={'Day 1':[30,40,50,20,15,60],'Day 2':[40,50,20,15,60,70],
      'Day 3':[50,20,15,60,70,50],'Target':[20,15,60,70,50,40]}

dataset=pd.DataFrame(data)

dataset

X=dataset.drop('Target',axis=1)
y=dataset['Target']

X

X_norm = Normalizer(norm='max').fit_transform(X)

X_norm

array(y)

np.reshape(array(y),(1,-1))

y_norm=Normalizer(norm='max').fit_transform(np.reshape(array(y),(1,-1)))

y_norm

"""weight_1=array([[.2,.1],[.3,.1],[.2,.1]])
weight_2=array([[.5],[.1]])"""

weight_1=uniform(-1,1,(3,2)) #shape 3 by 2
weight_2=uniform(-1,1,(2,1))

weight_1

X_norm[0:batch_size]

output_1=X_norm[0:batch_size]@weight_1
output_1

from keras.activations import sigmoid
act_output=sigmoid(output_1).numpy()
act_output

pred_output=act_output@weight_2
pred_output=np.reshape(pred_output,(1,-1))

y_true=y_norm[0][0:batch_size]
y_pred=pred_output

y_true

mse(y_true,y_pred).numpy()
