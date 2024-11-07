import numpy as np
import matplotlib.pyplot as plt  
import os

# Initialize parameters
X = 0              # Initial state=estimate
P = 1             # Initial estimate error
Q = 12         # Process variance
R = 0.01              # Measurement variance 
K = 0                # Initial Kalman=Gain
data=[0.0, 0.642, 0.985, 0.866, 0.342, -0.342, -0.866, -0.985, -0.642, -0.0, 0.642, 0.985, 0.866, 0.342, -0.342, -0.866, -0.985, -0.642, -0.0]



filtered_values = []  
for z in data:
        # PREDICTION STEP
    x_predict = X
    p_predict = P+Q
    
        # Update step
    
    K = p_predict / (p_predict +R)
    X = x_predict + K * (z -x_predict)       #State update
    P = (1 - K) * p_predict                # \Covariance update
   
    filtered_values.append(X)
          
# Plotting the results
plt.plot(data, label='data', marker='o')
plt.plot(filtered_values, label='Filtered Estimates', marker='x')
plt.legend()
plt.xlabel("Time Step")
plt.ylabel("Value")
plt.title("1D Kalman FilterMeasurements")
plt.show()
