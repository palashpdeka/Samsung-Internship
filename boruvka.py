#boruvka's algorithm

import constants_data
from collections import defaultdict
import D_S_U
            
def min_weighted_edge(edges):
    m_w_e=() #min_weighted_edge
    min_wt=1000000 #minimum weight
    for i in range(len(edges)):
        if edges[i][2]<min_wt:
            min_wt=edges[i][2]
            m_w_e=edges[i]
    return m_w_e
        
def convert_to_mst(n, gr, outputPath):
    mst_edges=set()
    dsu=D_S_U.DSU(n)
    grh=gr #making a copy of graph
    for node in grh:
        x=[min(node,grh[node][0][1]),max(node,grh[node][0][1]),grh[node][0][0]]
        dsu.merge(node,grh[node][0][1])
        del grh[node][0]
        mst_edges.add(tuple(x))
    while(True):
        temp_gr=defaultdict(list) #temporary graph
        for x in range(1,n+1):
            temp_gr[dsu.parent(x)].append(x)
        if(len(temp_gr)==1):
            break
        for group in temp_gr:
            temp_edges=[] #temporarily storing all possible edges, and finds the min weighted one
            for node in temp_gr[group]:
                if len(grh[node])==0:
                    continue
                node1=min(node,grh[node][0][1])
                node2=max(node,grh[node][0][1])
                if dsu.parent(node1)!=dsu.parent(node2):
                    x=[node1,node2,grh[node][0][0]]
                    temp_edges.append(tuple(x))
            edge=min_weighted_edge(list(set(temp_edges)))
            if(len(edge)!=0):
                dsu.merge(edge[0],edge[1])
                mst_edges.add(edge)
                del grh[edge[0]][0]
                del grh[edge[1]][0]
            
    #print(mst_edges) #mst output of edges in the format [node1,node2,weight]
    #del dsu
    saveOutput(outputPath, mst_edges)
    

#method to take input from a file
def getInput(inputPath):
    mygraph = defaultdict(list)
    #global n; n=1
    file = open(inputPath, "r")
    with open(inputPath,"r") as file:
        lines = file.readlines()
        for currentLine in lines:
            x,y,w=map(int,currentLine.split(" ")) #input in the format [node1,node2,weight]
            mygraph[x].append([w,y])
            mygraph[y].append([w,x])
            #n=max(n,max(x,y))
        for node in mygraph:
            mygraph[node].sort()
    file.close()
    return mygraph

#method to save output to a file
def saveOutput(outputPath, mst_edges):
    output_str = ".\n\n\nOutput generated using Boruvka---\n\n"
    for edges in mst_edges:
        output_str += str(edges) + "\n"
    output_str = output_str.strip()
    with open(outputPath, "a") as file:
        file.write(output_str)
        file.close()

def generate_mst(n):
    inputpath = constants_data.input_loc_path
    outputpath = constants_data.output_loc_path
    gr=defaultdict(list)
    gr=getInput(inputpath)
    convert_to_mst(n, gr, outputpath)
    #print("Boruvka output generated on output.txt")
    
#generate_mst()