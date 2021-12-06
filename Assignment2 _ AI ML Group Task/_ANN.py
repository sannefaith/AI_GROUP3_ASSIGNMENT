import numpy as np
from keras.losses import mse

class _ANN:
    def ann(self,batch_size,y_norm,act_output,weight_2,epochs):
        
        for epoch in range(epochs):
            wik=weight_2[0]
            wjk=weight_2[1]
            print(str(epoch+1),"epoch has started...")
            # %%

            
            pred_output=act_output@weight_2
            pred_output=np.reshape(pred_output,(1,-1))
            pred_output

            # %% [markdown]
            # Mean Squared Error

            # %%
            y_true=y_norm[0][0:batch_size]
            y_pred=pred_output
            y_true

            # %%
            #y_true
            y_true

            # %% [markdown]
            # Node K output

            # %%
            yhat=mse(y_true,y_pred).numpy()
            print("Yhat:",yhat)
            s=(y_true-y_pred)
            x=s*s
            x.mean()

            # %% [markdown]
            # Compute error at k

            # %%
            target=0.909
            derivative=yhat*(1-yhat)
            k=(target-yhat)*derivative
            k

            # %%
            target=0.909

            yderivative=y_true[0]*(1-y_true[0])
            #j=(target-y_pred[0])*derivative
            j=k*wjk*yderivative
            j

            # %%
            iderivative=y_true[1]*(1-y_true[1])
            #j=(target-y_pred[0])*derivative
            i=k*wik*iderivative
            i

            # %%
            #new weight at j
            n=0.3
            jwc=wjk+(n*k*yhat)
            print("New Weight At J: "+str(jwc))



            # %%
            #new weight at i
            iwc=wik+(n*k*yhat)
            print("New Weight At I: "+str(iwc))

            # %%
            #new output at K
            weight_2=[iwc,jwc]
            print("Weight2",weight_2)