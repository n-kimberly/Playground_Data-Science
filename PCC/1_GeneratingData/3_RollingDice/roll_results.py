import pygal
import matplotlib.pyplot as plt
from die import Die

die1 = Die()
die2 = Die()

res_lst = []
for num_roll in range(10000):
    result = die1.roll() + die2.roll()
    res_lst.append(result)

# print(res_lst)

res_freq = {}
for result in res_lst:
    res_freq[result] = res_freq.get(result, 0) + 1

# print(res_freq)

res_hist_x = sorted(list(key for key in res_freq))
res_hist_y = list(res_freq[key_sorted] for key_sorted in res_hist_x)
# print(res_hist_x)
# print(res_hist_y)

res_hist = pygal.Bar()
res_hist.title = "Results of rolling two D6 10,000 times"
res_hist.x_labels = res_hist_x
res_hist.x_title = "Roll Result"
res_hist.y_title = "Frequency of Result"

res_hist.add('D6 + D6', res_hist_y)
res_hist.render_to_file('die6_visual.svg')
