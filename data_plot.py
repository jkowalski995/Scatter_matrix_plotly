import plotly.express as px
import plotly.offline as pxo
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# PLOT COLORSCALE Flow.Bytes.s
# plot rows 1-29 cols 1-58
def plot3(df):
    lst = list(df.columns.values)
    a = 0
    c = 1
    for i in range(1, 13):
        fig = make_subplots(rows=29, cols=6, subplot_titles=(lst[a:(a+6)]))
        a = a + 5
        f = 1
        for x in range(c, (c+6)):
            e = 1
            for y in range(1, 30):
                if x > 58:
                    break
                else:
                    fig.add_trace(
                        go.Scatter(x=df[lst[x - 1]], y=df[lst[y - 1]], name=lst[y - 1], mode='markers',
                                   marker=dict(color=df['Flow.Bytes.s'], showscale=True)),
                        row=e, col=f
                    )
                print("e:", e)
                e = e + 1
            print("f:", f)
            f = f + 1
        fig.update_layout(height=8000, width=1800, showlegend=False)
        fig.write_html("plots/Flow_Bytes_S/file" + str(i) + ".html")
        fig.write_image("plots/Flow_Bytes_S/fig" + str(i) + ".png")
        c = c + 5


# plot rows 30-58 cols 1-58
def plot4(df):
    lst = list(df.columns.values)
    a = 0
    c = 1
    for i in range(1, 13):
        fig = make_subplots(rows=29, cols=6, subplot_titles=(lst[a:(a+6)]))
        a = a + 5
        f = 1
        for x in range(c, (c+6)):
            e = 1
            for y in range(30, 58):
                if x > 58:
                    break
                else:
                    fig.add_trace(
                        go.Scatter(x=df[lst[x - 1]], y=df[lst[y - 1]], name=lst[y - 1], mode='markers',
                                   marker=dict(color=df['Flow.Bytes.s'], showscale=True)),
                        row=e, col=f
                    )
                print("e:", e)
                e = e + 1
            print("f:", f)
            f = f + 1
        fig.update_layout(height=8000, width=1800, showlegend=False)
        fig.write_html("plots/Flow_Bytes_S/file" + str(i+12) + ".html")
        fig.write_image("plots/Flow_Bytes_S/fig" + str(i+12) + ".png")
        c = c + 5
