# -*- coding: utf-8 -*-
"""
@Project Name  macro_economic
@File Name:    money_supply
@Software:     PyCharm
@Time:         2018/6/9 14:19
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

np.set_printoptions(threshold=2000, linewidth=1000)  # default 1000 default 75
pd.set_option('display.width', 1000)  # default is 80

if __name__ == "__main__":
    ms = ts.get_money_supply()
    """
    货币供应量
    month :统计时间
    m2 :货币和准货币（广义货币M2）(亿元)
    m2_yoy:货币和准货币（广义货币M2）同比增长(%)
    m1:货币(狭义货币M1)(亿元)
    m1_yoy:货币(狭义货币M1)同比增长(%)
    m0:流通中现金(M0)(亿元)
    m0_yoy:流通中现金(M0)同比增长(%)
    cd:活期存款(亿元)
    cd_yoy:活期存款同比增长(%)
    qm:准货币(亿元)
    qm_yoy:准货币同比增长(%)
    ftd:定期存款(亿元)
    ftd_yoy:定期存款同比增长(%)
    sd:储蓄存款(亿元)
    sd_yoy:储蓄存款同比增长(%)
    rests:其他存款(亿元)
    rests_yoy:其他存款同比增长(%)
    """
    # print(ms)
    # ms["month"] = ms["month"].apply(lambda s: datetime.datetime.strptime(s, '%Y.%m'))
    ms["month"] = pd.to_datetime(ms["month"])
    ms = ms.set_index("month")
    ms = ms.replace("--", np.nan)
    ms = ms.astype(np.float64)
    ms = ms.iloc[::-1, :]
    print(ms)

    # ax = ms.plot(grid=True, title="money supply")
    ax = ms[["m2","m1","m0","cd","qm","ftd","sd","rests"]].plot(grid=True, title="money supply")
    # ax = ms[["m2_yoy","m1_yoy","m0_yoy","cd_yoy","qm_yoy","ftd_yoy","sd_yoy","rests_yoy"]].plot(grid=True, title="money supply")

    ax.grid(True)

    # plt.show()
    ####################################################################################################################
    msb = ts.get_money_supply_bal()

    """
    货币供应量(年底余额)
    year :统计年度
    m2 :货币和准货币(亿元)
    m1:货币(亿元)
    m0:流通中现金(亿元)
    cd:活期存款(亿元)
    qm:准货币(亿元)
    ftd:定期存款(亿元)
    sd:储蓄存款(亿元)
    rests:其他存款(亿元)
    """
    # print(msb)
    msb["year"] = pd.to_datetime(msb["year"])
    msb = msb.set_index("year")
    msb = msb.replace("--", np.nan)
    msb = msb.astype(np.float64)
    msb = msb.iloc[::-1, :]
    print(msb)

    msb.plot(grid=True, title="money supply balance")
    ax.grid(True)
    plt.show()
