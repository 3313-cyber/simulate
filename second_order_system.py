import numpy as np
import control as ct
import matplotlib.pyplot as plt


i=input("请输入要仿真的二阶系统数目")
i=int(i)

zeta=[]
wn=[]
color=[]

for i in range(i):
    #zeta:系统阻尼比
    #zeta=0,系统处于临界状态，系统无振荡；0<zeta<1,系统处于欠阻尼状态，系统有振荡；zeta=1,系统处于临界阻尼状态，系统无振荡；zeta>1,系统处于过阻尼状态，系统无振荡。
    zeta.append(float(input(f"请输入{i+1}系统的阻尼比")))
    #wn:系统自然频率
    wn.append(float(input(f"请输入{i+1}系统的自然频率")))
    #参数：'r'：红色，'g'：绿色，'b'：蓝色，'m'：品红色，'c'：青色
    color.append(input(f"请输入{i+1}系统绘制时域曲线的颜色"))

print("完成输入")
t=np.linspace(0, 10, 1000)
1
for z,w,color in zip(zeta,wn,color):
    den=[1,2*z*w,w**2]
    num=[1]
    sys=ct.TransferFunction(num,den)
    #这里采用了单位阶越信号作为输
    t_out,y_out=ct.step_response(sys,t)
    info=ct.step_info(sys)
    plt.plot(t_out,y_out,color,label='zeta={:.2f},wn={:.2f},tr={:.2f},ts={:.2f}'.format(z,w,info['RiseTime'],info['SettlingTime']))

plt.xlabel('Time')
plt.ylabel('Response')
plt.title('Step Response of Second-Order Systems')
plt.legend()
plt.grid(True)
plt.show()
print("It's over")