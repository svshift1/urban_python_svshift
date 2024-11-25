"""   requirements.txt
matplotlib >= 3.6.0
scipy >= 1.8
"""
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation

# для notebooks:  ipympl

# это как раз то, что я преподаю в университете )
# у меня специализация по мат.моделированию.
# в повседневности ориентируюсь на дистрибутив Anaconda

# рекомендую запускать не в блокноте (Jupiter,Kolab), а в обычной командной строке
# результат запуска в IPython может зависеть от настроек,


# желательно раскомментировать : иначе в зависимости от среды (Spyder, PyCharm pro)
# окно с графиком появится не отдельно а во вкладке "plots". должны стоять соотв. пакеты
# matplotlib.use('qtagg')


# в коллабе-юпитере:
# %matplotlib widget

# правая часть уравнения колебаний "честного" а не математического маятника
# x'' + 2*gamma*x' + w0*sin(x) = 0 приведенная к ODE через подстановку x' = v
# где x -- это угол в радианах. функция в векторизованном виде для быстроты рассчетов
def F0(t, z, w, gamma):
    x = z[0, :]
    v = z[1, :]
    # dz[0] -- x'
    # dz[1] -- v' или x"
    dz = np.vstack((v, -2 * gamma * v - w * np.sin(x)))
    return np.array(dz)


# параметры задачи
w0 = 1 * 2 * np.pi  # собственная циклическая частота колебаний - 1 колебание в 2 секунды для ~математического маятник
gamma = 0.0  # коэффициент затуханий
T_max = 30  # к-во секунд

# x0 = -0.1 * np.pi # при этих параметрах получается синусоида
x0 = -0.99 * np.pi # при этих параметрах получается далеко не синусоида )
v0 = 0  # помним, что обычно   v_max = x_max*w0
# если v0 > np.pi*w0  -- маятник будет делать солнышко, и график x(t) поедет ХЗ куда

# решение
dt = 0.1  # шаг по времени, сек
# max_step -- максимально допустимый шаг по времени. меньше 20 кадров в сек не имеет смысла делать для анимации
res = solve_ivp(F0, [0, T_max], [x0, v0], args=(w0, gamma), vectorized=True, max_step=dt)

if not res['success']:
    print(res['message'])
    sys.exit(-1)

A = 1  # длина маятника, для анимации
t = res['t']
x = res['y'][0, :]
v = res['y'][1, :]

fig, ax = plt.subplots(2, 2, width_ratios=[1, 3], height_ratios=[1, 1])

plt.axes(ax[0, 1])
plt.plot(t, x, '-b', label='угол')
px, = plt.plot(t[0], x[0], 'or')
plt.xlabel('t')
plt.ylabel('X')
plt.legend()

plt.axes(ax[1, 1])
plt.plot(t, v, '-b', label='уг. скорость')
pv, = plt.plot(t[0], v[0], 'or')
plt.xlabel('t')
plt.ylabel('Y')
plt.legend()

plt.axes(ax[1, 0])
plt.plot(x, v, '-b', label='фазовая\nдиаграмма')
pf, = plt.plot(x[0], v[0], 'or')
plt.xlabel('X')
plt.ylabel('V')
plt.legend()

#ax[0,0] -- тут анимация
plt.axes(ax[0, 0])
pm1, = plt.plot([0, A * np.sin(x0)], [0, -A * np.cos(x0)], '-b', lw=2)
pm2, = plt.plot(A * np.sin(x0), -A * np.cos(x0), 'o-b', ms=5, lw=2)
plt.axis('square')
plt.xlim([-1.2 * A, 1.2 * A])
plt.ylim([-1.2 * A, 1.2 * A])


#funcan = FuncAnimation(fig, ax[0,0], )


def animate(n, x, v, t, px, pv, pf, pm1, pm2) -> tuple:
    px.set_data([t[n]], [x[n]])
    pv.set_data([t[n]], [v[n]])
    pf.set_data([x[n]], [v[n]])
    pm1.set_data([0, A * np.sin(x[n])], [0, -A * np.cos(x[n])])
    pm2.set_data([A * np.sin(x[n])], [-A * np.cos(x[n])])
    return px, pv, pf, pm1, pm2

# тормозит ужасно. vispy имеет похожий интерфейс и умеет в OpenGL
an = matplotlib.animation.FuncAnimation(fig, animate, fargs=(x, v, t, px, pv, pf, pm1, pm2), frames=int(T_max / dt),
                                       interval=dt*1000, repeat=True, repeat_delay=5)

# в теории это даже как-то с Django можно поженить, но я не пробовал
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
plt.show()
