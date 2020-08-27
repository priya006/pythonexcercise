import math

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for x in raw_data:
    if not math.isnan(x):
        print(math.isnan(x))
        filtered_data.append(x)
        print(filtered_data)

#enumerate gives the index  and corresponding value in the list
    for i, v in enumerate(['tic', 'tac']):
        print(i, v)
