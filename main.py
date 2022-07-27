from cProfile import label
import constants_data
import time
import boruvka
import kruskal
import prim
import generate_input
import random
import plotly.express as px
import plotly.graph_objects as go
from collections import defaultdict

inputpath = constants_data.input_loc_path
outputpath = constants_data.output_loc_path
#location path of input and output files

kruskal_time=[]
boruvka_time=[]
prim_time=[]
nodes=[]

def generate_mst_will_all_methods(n):
     
    generate_input.generate_a_random_graph(n)
    #calling generate_a_random_graph() function from generate_input file
    
    #running boruvka's algorithm
    start=time.perf_counter()
    boruvka.generate_mst(n)
    end=time.perf_counter()
    boruvka_time.append(end-start)    
    
    #running kruskal's algorithm
    start=time.perf_counter()
    kruskal.generate_mst(n)
    end=time.perf_counter()
    kruskal_time.append(end-start)
    
    #running prim's algorithm
    start=time.perf_counter()
    prim.generate_mst(n)
    end=time.perf_counter()
    prim_time.append(end-start)


def check_with_increasing_nodes():
    global nodes
    print("Enter nodes : ",end=" ");
    nodes=list(map(int,input().split()))
    for node in nodes:
        print(f"Nodes : {str(node)}\t", end="")
        generate_mst_will_all_methods(node)
        
        
            
def update_storage(): #whenever you call a node, it will take the average with the previous time
    myvalues=defaultdict(list)
    with open(constants_data.storage_loc,"r") as file:
        lines=file.readlines()
        for currentLine in lines:
            n,q,tk,tb,tp=map(float,currentLine.split(" ")) #node,prev_tries,avg_time_kruskal,avg_time_boruvka,avg_time_prim
            myvalues[n]=[q,tk,tb,tp]
    for i in range(len(nodes)):
        if nodes[i] not in myvalues:
            myvalues[nodes[i]]=[1,kruskal_time[i],boruvka_time[i],prim_time[i]]
        else:
            q,tk,tb,tp=myvalues[nodes[i]]
            print(nodes[i],q,tk,tb,tp)
            tk=(tk*q+kruskal_time[i])/(q+1)
            tb=(tb*q+boruvka_time[i])/(q+1)
            tp=(tp*q+prim_time[i])/(q+1)
            myvalues[nodes[i]]=[q+1,tk,tb,tp]
    file.close()
    strr="" #"node, total_tries, avg_time_kruskal, avg_time_boruvka, avg_time_prim"
    for value in sorted(myvalues):
        strr+=str(int(value))+" "+str(int(myvalues[value][0]))+" "+str(myvalues[value][1])+" "
        strr+=str(myvalues[value][2])+" "+str(myvalues[value][3])+"\n"
    with open(constants_data.storage_loc,"w") as file:
        file.write(strr)
        file.close()
    #print(strr)
    
        
check_with_increasing_nodes()
print("Kruskal times- ",end=" "); 
print(kruskal_time)
print("Boruvka times- ",end=" "); 
print(boruvka_time)
print("Prim times- ",end=" "); 
print(prim_time)
 
update_storage()
    
fig=go.Figure()
fig.update_layout(title=dict(text="Kruskal vs Boruvka vs Prim", font_size=30))
fig.update_layout(xaxis_title="Nodes",  xaxis_title_font_size=18, yaxis_title="Time",  yaxis_title_font_size=18)
fig.add_trace(go.Scatter(name="Kruskal", x=nodes, y=kruskal_time, mode='lines+markers'))
fig.add_trace(go.Scatter(name="Boruvka", x=nodes, y=boruvka_time, mode='lines+markers'))
fig.add_trace(go.Scatter(name="Prim", x=nodes, y=prim_time, mode='lines+markers'))
fig.show()
