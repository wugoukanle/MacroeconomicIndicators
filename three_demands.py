# -*- coding: utf-8 -*-
"""
@Project Name  macro_economic
@File Name:    three_demands
@Software:     PyCharm
@Time:         2018/6/6 23:52
@Author:       taosheng
@contact:      langangpaibian@sina.com
@version:      1.0
@Description:　
"""


import numpy as np
import pandas as pd
import tushare as ts

import matplotlib.pyplot as plt

np.set_printoptions(threshold=2000, linewidth=1000)  # default 1000 default 75
pd.set_option('display.width', 1000)  # default is 80


if __name__ == "__main__":
    td = ts.get_gdp_for()

    """
    year :统计年度
    end_for :最终消费支出贡献率(%)
    for_rate :最终消费支出拉动(百分点)
    asset_for :资本形成总额贡献率(%)
    asset_rate:资本形成总额拉动(百分点)
    goods_for :货物和服务净出口贡献率(%)
    goods_rate :货物和服务净出口拉动(百分点)
    """

    td = td.set_index("year")
    td = td.iloc[::-1, :]
    print(td)

    td_pull = td[["for_rate", "asset_rate", "goods_rate"]]
    td_pull.plot(grid=True, title="pull of three demands")

    td_contrib = td[["end_for", "asset_for", "goods_for"]]
    td_contrib.plot(grid=True, title="contribution of three demands")

    plt.show()
