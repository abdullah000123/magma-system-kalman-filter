import numpy as np
import matplotlib.pyplot as plt  
import os

class kalaman:
    def __init__():
        
        X = [0,0]              # Initial state=estimate
        P = np.eye(2)               # Initial estimate error
        Q = np.eye(2)*100      # Process variance
        R = np.eye(2)*1            # Measurement variance 
        K = np.eye(2)*0     

    def estimation(z):
                # PREDICTION STEP
        x_predict = X
        p_predict = P+Q   
                # Update step    
        K = np.dot(p_predict , np.linalg.inv(p_predict +R))
        X = x_predict + np.dot(K , (z -x_predict))       #State update
        P = np.dot((1 - K) , p_predict)                # \Covariance update
           
        return X,x_predict         
# Plotting the results
plt.plot(data, label='data', marker='o')
plt.plot(X, label='Filtered Estimates', marker='x')
plt.legend()
plt.xlabel("X - AXIS")
plt.ylabel("Y - AXIS")
plt.title("2D Kalman FilterMeasurements")
plt.show()
