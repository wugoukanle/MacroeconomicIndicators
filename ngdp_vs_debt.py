# -*- coding: utf-8 -*-
"""
@Project Name  drawing
@File Name:    ngdp_vs_debt
@Software:     PyCharm Community Edition
@Time:         2018/6/26 19:57
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
    ## debt
    qs = pd.read_excel("totcredit.xlsx", sheetname="Quarterly Series", header=3)
    print(qs.shape)
    # print(qs)
    # print(qs.columns.values)
    # print(qs.index.values)

    """
    Q:CN:C:A:M:770:A        -->     Non financial sector
    Q:CN:G:A:N:770:A        -->     General government
    Q:CN:H:A:M:770:A        -->     Households and NPISHs
    Q:CN:N:A:M:770:A        -->     Non-financial corporations
    Q:CN:P:A:M:770:A        -->     Private non-financial sector
    """
    x2 = qs["Period"]

    # y2 = qs["Q:CN:C:A:M:770:A"]; debt_name = "Non financial sector"
    # y2 = qs["Q:CN:G:A:N:770:A"]; debt_name = "General government"
    # y2 = qs["Q:CN:H:A:M:770:A"]; debt_name = "Households and NPISHs"
    y2 = qs["Q:CN:N:A:M:770:A"]; debt_name = "Non-financial corporations"
    # y2 = qs["Q:CN:P:A:M:770:A"]; debt_name = "Private non-financial sector"

    # 去掉NaN值
    y2.index = x2
    y2 = y2.dropna()
    x2 = y2.index.to_series()

    # 对齐最小时间
    datatime_min = None
    if x1.min() < x2.min():
        datatime_min = x2.min()
    else:
        datatime_min = x1.min()

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
    lns2 = ax2.plot(x2, y2, '-r', label=debt_name)

    # added these three lines
    lns = lns1 + lns2
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc=0)

    ax1.grid()
    ax1.set_title("normal gdp growth vs " + debt_name)
    ax1.set_xlabel("time")

    ax1.set_ylabel(r"nominal GDP growth")
    ax2.set_ylabel(debt_name)

    # ax1.set_ylim(0, 15)
    # ax2.set_ylim(0, 15)

    plt.show()
