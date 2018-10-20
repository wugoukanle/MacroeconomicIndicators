# -*- coding: utf-8 -*-
"""
@Project Name  macro_economic
@File Name:    loan_rate
@Software:     PyCharm
@Time:         2018/6/6 22:46
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


def plot_curve(dates, y, title=None):
    """
    绘制曲线
    :param dates:
    :param y:
    :return:
    """
    fig, ax = plt.subplots()
    # ax.plot(y, 'o-')
    # ax.plot(range(len(y)), y, 'o-')
    ax.plot_date(dates, y, marker="*", linewidth=1, linestyle="-", color="blue")

    plt.title(title, fontproperties='SimHei', fontsize=12)
    plt.xlabel("time")
    plt.ylabel("rate")

    ### 设置X轴 ###
    ## 设置x轴范围
    # datemin = datetime.date(dates.min().year - 5, 1, 1)
    # datemax = datetime.date(dates.max().year + 5, 1, 1)
    # ax.set_xlim(datemin, datemax)

    ## 设置x轴tick和ticklabel
    # plt.xticks(np.arange(0, 50, 10), ('Tom', 'Dick', 'Harry', 'Sally', 'Sue'), rotation=90)
    # ax.set_xticks([])
    # ax.set_xticks(list(y.index))
    # ax.set_xticklabels(dates)
    # ax.set_xticklabels(["start","medium","end"])
    # ax.xaxis.set_major_formatter(NullFormatter())       # 设置x轴标签文本的格式
    # ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))  # 设置x轴时间标签显示格式

    # 设置主刻度标签的位置,有标签文本的格式
    ax.xaxis.set_major_locator(YearLocator(base=1, month=1, day=1, tz=None))  # tick every year on Feb 1st
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))  # 设置x轴标签文本的格式

    # rule = rrulewrapper(YEARLY, byeaster=1, interval=5)             # tick every 5th easter
    # ax.xaxis.set_major_locator(RRuleLocator(rule))
    # ax.xaxis.set_major_formatter(DateFormatter('%m/%d/%y'))         # 设置x轴标签文本的格式

    # 设置次刻度标签的位置,没有标签文本格式
    ax.xaxis.set_minor_locator(YearLocator())  # 将x轴次刻度标签设置为年

    ### 设置Y轴 ###
    ax.yaxis.set_major_locator(MultipleLocator(1))  # 将y轴主刻度标签设置为2的倍数
    ax.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))  # 设置y轴标签文本的格式
    ax.yaxis.set_minor_locator(MultipleLocator(0.25))  # 将此y轴次刻度标签设置为0.1的倍数

    # 打开网格
    # ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
    # ax.yaxis.grid(True, which='major')  # y坐标轴的网格使用次刻度
    ax.grid(True)
    fig.autofmt_xdate()
    plt.show()

if __name__ == "__main__":
    loan_rate = ts.get_loan_rate()

    """
    date :执行日期
    loan_type :存款种类
    rate:利率（%）
    """

    # print(loan_rate)

    ## 分组 ##
    gb = loan_rate.groupby(['loan_type'])

    for name, group in gb:
        print(name)
        print(group)

    # print(gb.groups.keys())

    name = r'个人住房公积金贷款(五年以上)'
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

    dates = data["date"].apply(lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'))
    y = data["rate"].astype(np.float64)
    # y = list(y)

    plot_curve(dates, y, title=name)
