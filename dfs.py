import networkx as nx
import matplotlib.pyplot as plt
import time

def DFShelper(G, v, visited, colors, sl, pos):
    visited[v] = True
    colors[v] = 'gray'
    sl.append(v)
    nx.draw(G, pos, with_labels=True, node_color=[colors[node] for node in G.nodes()])
    plt.pause(1)
    print("Visited Node:", v)
    for i in G[v]:
        if visited[i] == False:
            DFShelper(G, i, visited, colors, sl, pos)
    colors[v] = 'black'
    nx.draw(G, pos, with_labels=True, node_color=[colors[node] for node in G.nodes()])
    plt.pause(1)
    return sl

def DFS(G, source):
    #initialising visited for all nodes as false and color of all nodes as white
    visited = [False] * (len(G.nodes()))
    colors = ['white'] * (len(G.nodes()))
    sl = []    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='white')
    dfs = [] #2 dimensional array to store different components of a graph
    dfs.append(DFShelper(G, source, visited, colors, sl, pos))
    for i in range(len(G.nodes())):
        if visited[i] == False:
            sl = []
            dfs.append(DFShelper(G, i, visited, colors, sl, pos))
    print("DFS traversal order:", dfs)
    return dfs


def CreateGraph():
    G = nx.DiGraph()
    try:
            n = input('Enter number of nodes')
            n=n.strip()
            if n.isdigit():
                    n=int(n)
                    if (n<=0):
                        print('Invalid Input')
                        exit()
            
                    Matrix = []
                    list1=[]
                    for i in range(n):
                        for j in range(n):
                                print('Is there an edge between node', i ,'and node', j,'?')
                                e=int(input('Enter 1 if yes 0 if no'))
                                if (e!=0 and e!=1):
                                        print('Wrong input')
                                        exit()
                                list1+=[e]
                        Matrix.append(list1)
                    source = int(input('Enter source vertex from where DFS has to start:'))
                    if (source>=n):
                        print('Invalid input')
                        exit()
                    for i in range(n):
                        for j in range(n):
                            if Matrix[i][j] == 1:
                                G.add_edge(i, j)
            else:
                     print('Wrong input')
                     exit()
    except ValueError:
            print('Invalid input')
            exit()
             
    return G, source

if __name__ == "__main__":
    G, source = CreateGraph()
    dfs = DFS(G, source)
