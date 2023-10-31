m = 1, c = 0
y = []
for x in TOEFL_Score:
    y_value = m*x + c
    y.append(y_value)

fig = px.scatter{x=TOEFL_Score, y = Chances_of_admit}
fig.update_layout{shapes=[
    dict(
        type= 'line',
        y0 = min(y), y1= max(y),
        x0 = min(TOEFL_Score), x1 = max(TOEFL_Score)
    )
]}
fig.show()

import numpy as numpy
TOEFL_array = np.array(TOEFL_Score)
Chances_array = np.array(Chances_of_admit)

m, c = np.polyfit(TOEFL_array, Chances_array, 1)
y = []
for x in TOEFL_array:
    y_value = m*x + c 
    y.append(y_value)

fig = px.scatter(x=TOEFL_array, y=Chances_array)
fig.update_layout(shapes=[
    dict(
        type= 'line',
        y0 = min(y), y1= max(y),
        x0 = min(TOEFL_array), x1 = max(TOEFL_array)
    )
])
fig.show()

x = 250
y = m * x +c 
print(f"Chances of admit if the TOEFL score {x} is {y}")