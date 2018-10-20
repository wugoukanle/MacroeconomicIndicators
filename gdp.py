# -*- coding: utf-8 -*-
"""
@Project Name  macro_economic
@File Name:    gdp
@Software:     PyCharm
@Time:         2018/6/9 15:23
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
    # gdp_y = ts.get_gdp_year()
    # """
    # year :统计年度
    # gdp :国内生产总值(亿元)
    # pc_gdp :人均国内生产总值(元)
    # gnp :国民生产总值(亿元)
    # pi :第一产业(亿元)
    # si :第二产业(亿元)
    # industry :工业(亿元)
    # cons_industry :建筑业(亿元)
    # ti :第三产业(亿元)
    # trans_industry :交通运输仓储邮电通信业(亿元)
    # lbdy :批发零售贸易及餐饮业(亿元)
    # """
    # print(gdp_y)
    # gdp_y["year"] = gdp_y["year"].apply(lambda s: datetime.datetime.strptime(str(s), '%Y'))
    # gdp_y = gdp_y.set_index("year")
    # gdp_y = gdp_y.replace("--", np.nan)
    # gdp_y = gdp_y.astype(np.float64)
    # gdp_y = gdp_y.iloc[::-1, :]
    # print(gdp_y)
    #
    # ax = gdp_y.plot(grid=True, title="gdp year")
    #
    # ax.grid(True)
    #
    # plt.show()
    ####################################################################################################################
    gdp_q = ts.get_gdp_quarter()

    """
    quarter :季度
    gdp :国内生产总值(亿元)
    gdp_yoy :国内生产总值同比增长(%)
    pi :第一产业增加值(亿元)
    pi_yoy:第一产业增加值同比增长(%)
    si :第二产业增加值(亿元)
    si_yoy :第二产业增加值同比增长(%)
    ti :第三产业增加值(亿元)
    ti_yoy :第三产业增加值同比增长(%)
    """
    print(gdp_q)
    gdp_q["quarter"] = gdp_q["quarter"].apply(lambda s: datetime.datetime.strptime(str(s), '%Y.%m'))
    # gdp_q["quarter"] = pd.to_datetime(gdp_q["quarter"])
    gdp_q = gdp_q.set_index("quarter")
    gdp_q = gdp_q.replace("--", np.nan)
    gdp_q = gdp_q.astype(np.float64)
    gdp_q = gdp_q.iloc[::-1, :]
    print(gdp_q)

    # gdp_q = gdp_q[-60:]
    # gdp_q.plot(grid=True, title="gdp quarter")
    # gdp_q[["gdp","pi","si","ti"]].plot(grid=True, title="gdp quarter")
    # gdp_q[["gdp_yoy","pi_yoy","si_yoy","ti_yoy"]].plot(grid=True, title="gdp quarter")
    # plt.show()

    fig, ax = plt.subplots()
    ax.plot_date(gdp_q.index, gdp_q["gdp_yoy"], marker="*", linewidth=1, linestyle="-", color="blue")
    plt.title("gdp_yoy", fontproperties='SimHei', fontsize=12)

    # 设置主刻度标签的位置,有标签文本的格式
    ax.xaxis.set_major_locator(YearLocator(base=1, month=1, day=1, tz=None))  # tick every year on Feb 1st
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))  # 设置x轴标签文本的格式
    # 设置次刻度标签的位置,没有标签文本格式
    ax.xaxis.set_minor_locator(YearLocator())  # 将x轴次刻度标签设置为年

    ax.grid(True)
    fig.autofmt_xdate()
    plt.show()
