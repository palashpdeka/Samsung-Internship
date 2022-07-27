import random
import constants_data

def random_graph(n):
    #n=random.randint(100,100000) #nodes
    max_edges=100000
    m=random.randint(n-1,min(n*(n-1)/2,max_edges)) #edges
    a=[]; b=[]
    print("edges : ", str(m))
    for x in range(n-1):
        a.append(x+2)
    b.append(1)
    strr="";
    while len(a)>0: #to ensure that each node is connected to at least one edge
        node1=random.choice(a)
        node2=random.choice(b)
        a.remove(node1)
        b.append(node1)
        wt=random.randint(1,1000) #generating random weight
        strr+=str(node1)+" "+str(node2)+" "+str(wt)+"\n"
        m-=1;
    while m>0:
        node1=random.randint(1,n)
        node2=random.randint(1,n)
        while node1==node2: node2=random.randint(1,n)
        wt=random.randint(1,1000)
        strr+=str(node1)+" "+str(node2)+" "+str(wt)+"\n"
        m-=1;
    return strr


#location path of output file (i.e input.txt)

def generate_a_random_graph(n):        
    filename = str(n)+"_"
    for i in range(0,10) :
        filename += str(random.randint(0,10))
    constants_data.input_loc_path = constants_data.input_loc_temp + filename + '''_input.txt'''
    constants_data.output_loc_path = constants_data.output_loc_temp + filename + '''_output.txt'''
    with open (constants_data.output_loc_path,"w") as file:
        file.write("")
        file.close()
    with open(constants_data.input_loc_path,"w") as file:
        file.write("")
        file.write(random_graph(n))
        file.close()

