# -*- coding: utf-8 -*-
"""
@Project Name  macro_economic
@File Name:    cpi
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
    cpi = ts.get_cpi()
    """
    month :统计月份
    cpi :价格指数
    """
    print(cpi)
    # cpi["month"] = cpi["month"].apply(lambda s: datetime.datetime.strptime(str(s), '%Y.%d'))
    cpi["month"] = pd.to_datetime(cpi["month"])
    cpi = cpi.set_index("month")
    cpi = cpi.replace("--", np.nan)
    cpi = cpi.astype(np.float64)
    cpi = cpi.iloc[::-1, :]
    print(cpi)

    # ax = cpi.plot(grid=True, title="cpi")


    fig, ax = plt.subplots()
    ax.plot_date(cpi.index, cpi, marker="*", linewidth=1, linestyle="-", color="blue")
    plt.title("cpi", fontproperties='SimHei', fontsize=12)

    # 设置主刻度标签的位置,有标签文本的格式
    ax.xaxis.set_major_locator(YearLocator(base=1, month=1, day=1, tz=None))  # tick every year on Feb 1st
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))  # 设置x轴标签文本的格式
    # 设置次刻度标签的位置,没有标签文本格式
    ax.xaxis.set_minor_locator(YearLocator())  # 将x轴次刻度标签设置为年

    ax.grid(True)
    fig.autofmt_xdate()
    plt.show()