from clickhouse_driver import Client
import matplotlib.pyplot as plt
import matplotlib.animation as animation
client = Client('localhost')
plt.style.use('dark_background')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
xs = ['DDoS','SQL injection','Sniffing','maodzedun','XSS']
ys = [0,0,0,0,0]
def animate(i):
    ys[0] = client.execute("SELECT COUNT('datetime')  from atacks.atk a WHERE atk_type =='DDoS'")[0][0]
    ys[1] = client.execute("SELECT COUNT('datetime')  from atacks.atk a WHERE atk_type =='SQL injection'")[0][0]
    ys[2] = client.execute("SELECT COUNT('datetime')  from atacks.atk a WHERE atk_type =='Sniffing'")[0][0]
    ys[3] = client.execute("SELECT COUNT('datetime')  from atacks.atk a WHERE atk_type =='maodzedun'")[0][0]
    ys[4] = client.execute("SELECT COUNT('datetime')  from atacks.atk a WHERE atk_type =='XSS'")[0][0]
    ax1.clear()
    ax1.bar(xs, ys)
    plt.xlabel('Вид')
    plt.ylabel('Общее количество атак за все время')
    plt.title('Столбчатая диаграмма\n')
ani = animation.FuncAnimation(fig, animate, interval=200)
plt.show()


# import random
# from collections import deque
#
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
#
# npoints = 100
# x = deque([0], maxlen=npoints)
# y = deque([0], maxlen=100)
# fig, ax = plt.subplots()
# [line] = ax.plot(x, y)
#
#
# def update(dy):
#     x.append(x[-1] + 1)  # update data
#     y.append(y[-1] + dy)
#
#
#     line.set_xdata(x)  # update plot data
#     line.set_ydata(y)
#
#     ax.relim()  # update axes limits
#     ax.autoscale_view(True, True, True)
#     return line, ax
#
#
# def data_gen():
#     while True:
#         yield 1 if random.random() < 0.5 else -1
#
#
# ani = animation.FuncAnimation(fig, update, data_gen,interval= 10)
# plt.show()

