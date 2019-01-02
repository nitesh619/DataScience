import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

data = go.Data([
    go.Mesh3d(
        x = [0, 0, 1, 1, 0, 0, 1, 1],
        y = [0, 1, 1, 0, 0, 1, 1, 0],
        z = [0, 0, 0, 0, 1, 1, 1, 1],
        colorbar = go.ColorBar(
            title='z'
        ),
        colorscale = [['0', 'rgb(255, 0, 255)'], ['0.5', 'rgb(0, 255, 0)'], ['1', 'rgb(0, 0, 255)']],
        intensity = [0, 0.142857142857143, 0.285714285714286, 0.428571428571429, 0.571428571428571, 0.714285714285714, 0.857142857142857, 1],
        i = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
        j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
        k = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
        name='y',
        showscale=True
    )
])
layout = go.Layout(
    xaxis=go.XAxis(
        title='x'
    ),
    yaxis=go.YAxis(
        title='y'
    )
)
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='3d-mesh-cube-python')
py.show()