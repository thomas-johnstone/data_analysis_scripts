from bokeh.plotting import show, figure
from random import random
from bokeh.models import ColumnDataSource, CustomJS, Select, CheckboxButtonGroup, Legend
from bokeh.layouts import column
import numpy as np
import pandas as pd



p.line(x = 'x', y = 'y', color = 'red', legend_label = 'Zipcode:' + str(zip1), source = source1, visible = False)
q.line(x = 'x', y = 'y', color = 'red', legend_label = 'Zipcode:' + str(zip2), source = source2, visible = False)