# -*- coding: utf-8 -*-
"""
@Project Name  macro_economic
@File Name:    three_industries
@Software:     PyCharm
@Time:         2018/6/7 0:17
@Author:       taosheng
@contact:      langangpaibian@sina.com
@version:      1.0
@Description:　
"""
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
    ti_pull = ts.get_gdp_pull()
    """
    year :统计年度
    gdp_yoy :国内生产总值同比增长(%)
    pi :第一产业拉动率(%)
    si :第二产业拉动率(%)
    industry:其中工业拉动(%)
    ti :第三产业拉动率(%)
    """

    ti_pull = ti_pull.set_index("year")
    ti_pull = ti_pull.iloc[::-1, :]
    print(ti_pull)

    ti_pull.plot(grid=True, title="pull of three industries")


    ####################################################################################################################
    ti_contrib = ts.get_gdp_contrib()
    """
    year :统计年度
    gdp_yoy :国内生产总值
    pi :第一产业献率(%)
    si :第二产业献率(%)
    industry:其中工业献率(%)
    ti :第三产业献率(%)
    """
    ti_contrib = ti_contrib.set_index("year")
    ti_contrib = ti_contrib.iloc[::-1, :]
    print(ti_contrib)

    ti_contrib.plot(grid=True, title="contribution of three industries")

    plt.show()
