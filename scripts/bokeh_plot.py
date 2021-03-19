import sys
import os.path as osp
from random import random
from bokeh.plotting import figure, curdoc
from bokeh.models import Button, CustomJS, Select, Panel, Tabs
from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.io import show
import pandas as pd
import importlib

sys.path.append('../src/hw4/')
sys.path.append('../data/')
script_dir = osp.dirname(__file__)

import process

def main():

    # LOAD YOUR DATA
    df = pd.read_csv('../data/test2.csv')

    # PRE-PROCESS THE DATA
    df = process.main(df)
    print(df)

    rowList = []
    for index, rows in df.iterrows():
        my_list = [rows.Zipcode]
        rowList.append(my_list)

    print (rowList)

    # GENERATE THE TWO DROPDOWN ZIPCODE MENUS
    zip1 = Select(title="Choose the first Zipcode:", options=rowList)
    zip1.js_on_change("value", CustomJS(code="""
        console.log('select: value=' + this.value, this.toString())
    """))

    zip2 = Select(title="Choose the second Zipcode:",options=rowList)
    zip2.js_on_change("value", CustomJS(code="""
        console.log('select: value=' + this.value, this.toString())
    """))

    # GENERATE YOUR PLOTS
#    p1.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=3, color="red", legend_label = "Zipcode 1", alpha=0.5)

#    p2.line([1, 2, 3, 4, 5], [9, 10, 11, 12, 13], line_width=3, color="navy", legend_label = "Zipcode 2",  alpha=0.5)

#    p3.line([1, 2, 3, 4, 5], [2, 4, 6, 8, 10], line_width=3, color="navy", legend_label = "Zipcode 3",  alpha=0.5)

#    p = figure(plot_width = 600, plot_height = 600)
#    p.multi_line(p1, p2)

    # FORMAT/CREATE THE DOCUMENT
#    curdoc().add_root(column(zip1, zip2, p))


main()
