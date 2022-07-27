#kruskal's algorithm

import constants_data
from collections import defaultdict
from queue import PriorityQueue
import D_S_U

pq=PriorityQueue()


def convert_to_mst(n, gr, outputPath):
    mst_edges=set()
    dsu=D_S_U.DSU(n)
    while not pq.empty():
        edge=pq.get()
        if dsu.parent(edge[1])!=dsu.parent(edge[2]):
            dsu.merge(edge[1],edge[2])
            edge_=(edge[1],edge[2],edge[0]) #because first value was stored as weight
            mst_edges.add(edge_)
    #print(mst_edges) #mst output of edges in the format [node1,node2,weight]
   # del dsu
    saveOutput(outputPath, mst_edges)

    
#method to take input from a file
def getInput(inputPath):
    mygraph=defaultdict(list)
    #global n; n=1
    file = open(inputPath, "r")
    with open(inputPath,"r") as file:
        lines = file.readlines()
        for currentLine in lines:
            x,y,w=map(int,currentLine.split(" ")) #input in the format [node1,node2,weight]
            mygraph[x].append([w,y])
            mygraph[y].append([w,x])
            #n=max(n,max(x,y))
            pq.put((w,x,y))
    file.close()
    return mygraph
    
#method to save output to a file
def saveOutput(outputPath, mst_edges):
    output_str = ".\n\n\nOutput generated using Kruskal---\n\n"
    for edges in mst_edges:
        output_str += str(edges) + "\n"
    output_str+="\n"+"\n"+"\n"
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
    #print("Kruskal output generated on output.txt")
#generate_mst()