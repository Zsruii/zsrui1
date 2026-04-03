import numpy as np
import matplotlib.pyplot as plt

# 解决中文乱码问题（Windows系统通用）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示异常

# ===================== 连续信号：余弦信号 =====================
t = np.linspace(0, 4 * np.pi, 1000)
y_continuous = np.cos(t)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(t, y_continuous, 'b-', linewidth=2)
plt.title('连续信号：余弦信号 cos(t)')
plt.xlabel('时间 t')
plt.ylabel('信号值')
plt.grid(True)

# ===================== 离散信号：单位阶跃信号 =====================
n = np.arange(-5, 10)
y_discrete = np.where(n >= 0, 1, 0)

plt.subplot(1, 2, 2)
plt.stem(n, y_discrete, 'r-', markerfmt='ro', basefmt='k-')
plt.title('离散信号：单位阶跃信号 u[n]')
plt.xlabel('离散时间 n')
plt.ylabel('信号值')
plt.grid(True)

plt.tight_layout()
plt.show()