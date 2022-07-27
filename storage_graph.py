import constants_data
import plotly.express as px
import plotly.graph_objects as go
from collections import defaultdict

myvalues=defaultdict(list)
with open(constants_data.storage_loc,"r") as file:
     lines=file.readlines()
     for currentLine in lines:
         n,q,tk,tb,tp=map(float,currentLine.split(" ")) #node,prev_tries,avg_time_kruskal,avg_time_boruvka,avg_time_prim
         myvalues[n]=[q,tk,tb,tp]
     file.close()
    
kruskal_time=[]
boruvka_time=[]
prim_time=[]
nodes=[]


for node in myvalues:
    nodes.append(int(node))
    kruskal_time.append(myvalues[int(node)][1])
    boruvka_time.append(myvalues[int(node)][2])
    prim_time.append(myvalues[int(node)][3])
    
fig=go.Figure()
fig.update_layout(title=dict(text="Kruskal vs Boruvka vs Prim avg time graph", font_size=30))
fig.update_layout(xaxis_title="Nodes",  xaxis_title_font_size=18, yaxis_title="Time",  yaxis_title_font_size=18)
fig.add_trace(go.Scatter(name="Kruskal", x=nodes, y=kruskal_time, mode='lines+markers'))
fig.add_trace(go.Scatter(name="Boruvka", x=nodes, y=boruvka_time, mode='lines+markers'))
fig.add_trace(go.Scatter(name="Prim", x=nodes, y=prim_time, mode='lines+markers'))
fig.show()