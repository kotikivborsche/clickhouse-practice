from clickhouse_driver import Client
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
client = Client('localhost')
plt.style.use('dark_background')
npoints = 10
x = deque([0], maxlen=npoints)
y0 = deque([0], maxlen=npoints)
y1 = deque([0], maxlen=npoints)
y2 = deque([0], maxlen=npoints)
y3 = deque([0], maxlen=npoints)
y4 = deque([0], maxlen=npoints)
fig, ax = plt.subplots()
[line0] = ax.plot(x, y0, label='DDoS')
[line1] = ax.plot(x, y1, label='SQL injection')
[line2] = ax.plot(x, y2, label='Sniffing')
[line3] = ax.plot(x, y3, label='maodzedun')
[line4] = ax.plot(x, y4, label='XSS')
def animate(dy):
    x.append(x[-1] + 1)
    y0.append(client.execute("SELECT count(`datetime`) from atacks.atk a WHERE atk_type == 'DDoS' AND (DATE_SUB(SECOND ,-17990, NOW('Asia/Yekaterinburg')) < toTimeZone(`datetime`,'Asia/Yekaterinburg')) ")[0][0])
    y1.append(client.execute("SELECT count(`datetime`) from atacks.atk a WHERE atk_type == 'SQL injection' AND (DATE_SUB(SECOND ,-17990, NOW('Asia/Yekaterinburg')) < toTimeZone(`datetime`,'Asia/Yekaterinburg')) ")[0][0])
    y2.append(client.execute("SELECT count(`datetime`) from atacks.atk a WHERE atk_type == 'Sniffing' AND (DATE_SUB(SECOND ,-17990, NOW('Asia/Yekaterinburg')) < toTimeZone(`datetime`,'Asia/Yekaterinburg')) ")[0][0])
    y3.append(client.execute("SELECT count(`datetime`) from atacks.atk a WHERE atk_type == 'maodzedun' AND (DATE_SUB(SECOND ,-17990, NOW('Asia/Yekaterinburg')) < toTimeZone(`datetime`,'Asia/Yekaterinburg')) ")[0][0])
    y4.append(client.execute("SELECT count(`datetime`) from atacks.atk a WHERE atk_type == 'XSS' AND (DATE_SUB(SECOND ,-17990, NOW('Asia/Yekaterinburg')) < toTimeZone(`datetime`,'Asia/Yekaterinburg')) ")[0][0])
    line0.set_xdata(x)
    line1.set_xdata(x)
    line2.set_xdata(x)
    line3.set_xdata(x)
    line4.set_xdata(x)
    line0.set_ydata(y0)
    line1.set_ydata(y1)
    line2.set_ydata(y2)
    line3.set_ydata(y3)
    line4.set_ydata(y4)
    ax.legend(loc = 'upper left')
    ax.relim()
    ax.autoscale_view(True, True, True)
    plt.xlabel('Время, с')
    plt.ylabel('Количетво атак за последние 10 секунд')
    plt.title('Live wormlike diagramm\n')
    return line0,line1,line2,line3,line4, ax
ani = animation.FuncAnimation(fig, animate,interval= 1000)
plt.show()