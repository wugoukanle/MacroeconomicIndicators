# -*- coding: utf-8 -*-
"""
@Project Name  macro_economic
@File Name:    ppi
@Software:     PyCharm
@Time:         2018/6/9 15:44
@Author:       taosheng
@contact:      langangpaibian@sina.com
@version:      1.0
@Description:　
"""
import datetime
import numpy as np
import pandas as pd
import tushare as ts

import matplotlib.pyplot as plt
from matplotlib.dates import YEARLY, DateFormatter, rrulewrapper, DateFormatter, drange
from matplotlib.dates import RRuleLocator, YearLocator, MonthLocator, WeekdayLocator, DayLocator

np.set_printoptions(threshold=2000, linewidth=1000)  # default 1000 default 75
pd.set_option('display.width', 1000)  # default is 80

if __name__ == "__main__":
    ppi = ts.get_ppi()
    """
    month :统计月份
    ppiip :工业品出厂价格指数
    ppi :生产资料价格指数
    qm:采掘工业价格指数
    rmi:原材料工业价格指数
    pi:加工工业价格指数
    cg:生活资料价格指数
    food:食品类价格指数
    clothing:衣着类价格指数
    roeu:一般日用品价格指数
    dcg:耐用消费品价格指数
    """
    print(ppi)
    print(ppi.shape)
    # ppi["month"] = ppi["month"].apply(lambda s: datetime.datetime.strptime(str(s), '%Y.%d'))
    ppi["month"] = pd.to_datetime(ppi["month"])
    ppi = ppi.set_index("month")
    ppi = ppi.replace("--", np.nan)
    ppi = ppi.astype(np.float64)
    ppi = ppi.iloc[::-1, :]
    print(ppi)
    print(ppi.shape)

    # # ax = ppi.plot(grid=True, title="ppi")
    # ax = ppi["ppi"].plot(grid=True, title="ppi")


    fig, ax = plt.subplots()
    ax.plot_date(ppi.index, ppi["ppi"], marker="*", linewidth=1, linestyle="-", color="blue")
    plt.title("ppi", fontproperties='SimHei', fontsize=12)

    # 设置主刻度标签的位置,有标签文本的格式
    ax.xaxis.set_major_locator(YearLocator(base=1, month=1, day=1, tz=None))  # tick every year on Feb 1st
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))  # 设置x轴标签文本的格式
    # 设置次刻度标签的位置,没有标签文本格式
    ax.xaxis.set_minor_locator(YearLocator())  # 将x轴次刻度标签设置为年

    ax.grid(True)
    fig.autofmt_xdate()
    plt.show()

