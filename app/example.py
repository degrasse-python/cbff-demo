from re import A



import pandas as pd
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.express as px
import plotly.graph_objects as go

path = "./data.csv"
# dataframe from data
df = pd.read_csv(path, encoding="ascii", encoding_errors="replace")
# json
# df['InvoiceDate'] = df['InvoiceDate'].dt.strftime('%m-%d%Y')
df.InvoiceDate = pd.to_datetime(df.InvoiceDate)
df['InvoiceDate'] = df['InvoiceDate'].dt.date
g = df.groupby('InvoiceDate')
y_data = g.UnitPrice.agg(sum).array
x_data = g.InvoiceDate.unique().array
new_x = []
for i in x_data:
    new_x.append(i[0])
fig = px.line(df, x=new_x, y=y_data, opacity=0.8, title="Unsorted Input") 

fig = px.line(x=df['InvoiceDate'], y=df['UnitPrice'])


g.index.tolist()

plot_div = plot([Scatter(x=x_data, y=y_data,
                    mode='lines', name='test',
                    opacity=0.8, marker_color='green')],
                    output_type='div', include_plotlyjs=False,
                    show_link=False, link_text="",
                    )

plot_div = plot([fig],
                    output_type='div', include_plotlyjs=False,
                    show_link=False, link_text="",
                    )

plot_div = plot([Scatter(x=df['InvoiceDate'], y=df['UnitPrice'])],
                    output_type='div', include_plotlyjs=False,
                    show_link=False, link_text="",                        
                        )

# import plotly.express as px
# fig = px.line(df, x="x", y="y", title="Unsorted Input") 
# fig.show()