import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime
def plot(months,frequency,uid):
    figure=plt.gcf()
    figure.set_size_inches(2.8, 2.2)
    y_pos=np.arange(len(months))
    plt.bar(y_pos,frequency,align='center',alpha=0.2,width=0.2)
    plt.xticks(y_pos,months)
    plt.ylabel('no of classes attended')
    plt.title('attendance report')
    for i in range(len(frequency)):
        plt.text(x=i, y=frequency[i] ,s=frequency[i] , color='blue', fontweight='bold')
    fname='project/images/'+str(uid)+'-'+str(datetime.datetime.date(datetime.datetime.now()))+'.png'
    plt.savefig(fname,dpi=100)
    plt.clf()
    return fname
def call(months,frequency,uid):
    plot(months,frequency,uid)
