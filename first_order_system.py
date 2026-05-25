import numpy as np
import matplotlib.pyplot as plt
import control as ct


t=np.linspace(0, 10, 1000)

K=1
T=[0.5,1,2,3,4]
color=['r','g','b','m','c']
for T,color in zip(T,color):
    num=[K]
    den=[T,1]
    sys=ct.TransferFunction(num,den)
    t_out,y_out=ct.step_response(sys,t)#transfer function step response
    plt.plot(t_out,y_out,color,label='T={}'.format(T))

plt.xlabel('Time')
plt.ylabel('Response')
plt.title('Step Response of First-Order Systems')
plt.legend()
plt.grid(True)
plt.show()
print("It's over")