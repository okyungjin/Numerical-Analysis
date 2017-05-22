import numpy as np
import matplotlib.pyplot as plt

Fs = 150.0  # sampling rate
Ts = 1.0/Fs # sampling interval or sampling time
# 0.006666666666666667

t = np.arange(0,1,Ts) # time vector
# 0에서 1초 사이에 0.006 초 간격의 (Ts개) 시간을 만들어라
# np.size(t)=150

ff = 5   # frequency of the signal
y = np.sin(2*np.pi*ff*t)
# sin(2*np.pi)를 1 초 (t) 안에 5개 (ff)의 2*pi 주기의 sin 파를 만들어라. 
# 그런데, 1초 안에는 150개의 점을 찍어라.
# np.size(y)=150

#  compare sine and cosine
y1= np.cos(2*np.pi*ff*t)

########### draw sin and cosine
plt.figure(1)
plt.subplot(2,1,1)
plt.plot(t,y, 'b.')
# np.size(t) = 150
# np.size(y) = 150
plt.xlabel('Time')
plt.ylabel('sin(t)')
plt.grid()
plt.subplot(2,1,2)
plt.plot(t,y1,'r*')
plt.xlabel('Time')
plt.ylabel('cos(t)')
plt.grid()

#### Reduce Sampling Rate

fs = 20.0  # sampling rate
ts = 1.0/fs # sampling interval or sampling time
# 0.05  <-- 0.006666666666666667

t1 = np.arange(0,1,ts) # time vector
# 0에서 1초 사이에 0.05 초 간격의 (ts개) 시간을 만들어라
# np.size(t1)=20

ff1 = 5   # frequency of the signal
yy = np.sin(2*np.pi*ff1*t1)
# sin(2*np.pi)를 1 초 (t) 안에 5개 (ff1)의 2*pi 주기의 sin 파를 만들어라.
# 그런데, 1초 안에는 20개의 점을 찍어라.
# np.size(yy)=20

#  compare sine and cosine
yy1= np.cos(2*np.pi*ff1*t1)

########### draw sin and cosine
plt.figure(2)
plt.subplot(2,1,1)
plt.plot(t1,yy, 'b.')
# np.size(t1) = 20
# np.size(yy) = 20
plt.xlabel('Time')
plt.ylabel('sin(t)')
plt.grid()
plt.subplot(2,1,2)
plt.plot(t1,yy1,'r*')
plt.xlabel('Time')
plt.ylabel('cos(t)')
plt.grid()



