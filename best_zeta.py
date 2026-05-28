#本代码目的在于计算欠阻尼二阶系统单位脉冲相应下的最佳zeta值，以便在后续的计算中使用
import numpy as np
import matplotlib.pyplot as plt
import control as ct

zeta=np.linspace(0.35,1,10000)#阻尼比从0到1，分成10000份
wn=1#自然频率为1

zeta_list=[]
ts_list=[]

for z in zeta:
    den=[1,2*z*wn,wn**2]
    num=[wn**2]
    sys=ct.TransferFunction(num,den)
    #这里是按照%5误差带进行计算
    #按照%2误差带，最终算出的最佳阻尼比是0.78左右
    info = ct.step_info(sys,SettlingTimeThreshold=0.05)
    print(f"zeta={z}时，调节时间为{info['SettlingTime']}")
    zeta_list.append(z)
    ts_list.append(info['SettlingTime'])

min_ts=min(ts_list)
best_index = np.argmin(ts_list)
best_zeta=zeta_list[best_index]
print("当zeta取{}时有最小调节时间{}".format(best_zeta,min_ts))
plt.plot(zeta_list,ts_list,'r',label='T={}'.format(wn))

plt.xlabel('zeta')
plt.ylabel('SettlingTime')
plt.title('zeta-ts')

plt.legend()
plt.grid(True)
plt.show()