import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

with open("settings.txt", "r") as settings:
    freq, tick = map(float, settings.read().split("\n"))

with open("data.txt", "r") as data:
    y = data.read()
    y = list(map(float, y.split("\n")))
vol = np.array(y)
tim = np.arange(0, len(y) / freq, 1 / freq)
fig, ax = plt.subplots()
ax.plot(tim, vol, color = "red", label = "V(t)", linewidth = "1", linestyle = '-', marker ='.', markevery = 5)
ax.set_title("Зарядка и разрядка конденсатора в RC-цепи", loc = "center")
ax.set_xlabel("Время, с")
ax.set_ylabel("Напряжение, В")
ax.set_xticks(np.arange(0, tim[-1] + 1, 1))
ax.set_yticks(np.arange(0, vol.max(), 0.5))
ax.margins(0, tick * 5)
ax.set_ylim(bottom = 0)
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.grid('on', which = 'major', linewidth = 0.8, color = 'darkgray', linestyle = '-')
ax.grid('on', which = 'minor', linewidth = 0.4, color = 'lightgray', linestyle = '--')
ax.legend()
timzar = vol.argmax() / freq
timrazr = tim[-1] - timzar
s1 = 'Время зарядки = ' + str(round(int(timzar*100))/100) + ' с'
s2 = 'Время разрядки = ' + str(round(int(timrazr*100))/100) + ' с'
ax.annotate(s1, xy=(5.2, 2.7))
ax.annotate(s2, xy=(5.2, 2.2))
plt.show()
plt.savefig("plot.svg")