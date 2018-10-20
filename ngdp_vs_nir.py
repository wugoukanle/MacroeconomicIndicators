# -*- coding: utf-8 -*-
"""
@Project Name  drawing
@File Name:    ngdp_vs_nir
@Software:     PyCharm Community Edition
@Time:         2018/6/26 20:16
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
from matplotlib.ticker import MultipleLocator, NullFormatter, FormatStrFormatter
from matplotlib.dates import YEARLY, DateFormatter, rrulewrapper, DateFormatter, drange
from matplotlib.dates import RRuleLocator, YearLocator, MonthLocator, WeekdayLocator, DayLocator

np.set_printoptions(threshold=2000, linewidth=1000)  # default 1000 default 75
pd.set_option('display.width', 1000)  # default is 80

if __name__ == "__main__":
    ####################################################################################################################
    ## GDP
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
    gq = ts.get_gdp_quarter()
    gq["quarter"] = gq["quarter"].apply(lambda s: datetime.datetime.strptime(str(s), '%Y.%m'))
    # gq["quarter"] = pd.to_datetime(gdp_q["quarter"])
    # gq = gq.set_index("quarter")
    gq = gq.replace("--", np.nan)
    gq["gdp_yoy"] = gq["gdp_yoy"].astype(np.float64)
    # gq = gq.iloc[::-1, :]
    print(gq)

    x1 = gq["quarter"]
    y1 = gq["gdp_yoy"]

    ####################################################################################################################
    ## 利率
    """
    date :变动日期
    deposit_type :存款种类
    rate:利率（%）
    """
    # dr = ts.get_deposit_rate()
    # print(dr)

    """
    date :执行日期
    loan_type :贷款种类
    rate:利率（%）
    """
    lr = ts.get_loan_rate()
    # print(lr)

    ## 分组 ##
    gb = lr.groupby(['loan_type'])
    print(gb.groups.keys())

    name = r'中长期贷款(三至五年)'
    data = gb.get_group(name)
    print(data)
    # print(data.shape)
    # print(type(data))
    # print(type(data["rate"]))
    # print(data["rate"].dtype)
    # data = data.reindex(data.index[::-1])

    ## 缺失值处理 ##
    data = data.replace("--", np.nan)
    print(data)

    x2 = data["date"].apply(lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'))
    y2 = data["rate"].astype(np.float64)

    # 对齐最小时间
    datatime_min = None
    if x1.iloc[-1] < x2.iloc[-1]:
        datatime_min = x2.iloc[-1]
    else:
        datatime_min = x1.iloc[-1]

    x1 = x1.loc[x1 >= datatime_min]
    y1 = y1.reindex(x1.index)
    y1 = y1.loc[x1 >= datatime_min]

    x2 = x2.loc[x2 >= datatime_min]
    y2 = y2.reindex(x2.index)
    y2 = y2.loc[x2 >= datatime_min]

    ####################################################################################################################
    ## 绘图
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    lns1 = ax1.plot(x1, y1, '-', label='normal gdp growth')

    ax2 = ax1.twinx()
    lns2 = ax2.plot(x2, y2, '-r', label='normal interest rate')

    # added these three lines
    lns = lns1 + lns2
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc=0)

    ax1.grid()
    ax1.set_title("normal gdp growth vs normal interest rate")
    ax1.set_xlabel("time")

    ax1.set_ylabel(r"nominal GDP growth")
    ax2.set_ylabel(r"nominal interest rate")

    # ax1.set_ylim(0, 15)
    # ax2.set_ylim(0, 15)

    plt.show()
