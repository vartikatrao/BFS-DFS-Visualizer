import networkx as nx
import matplotlib.pyplot as plt
import time

# BFS traversal with delay and order tracking
def BFS(G, source, pos, visited, queue):
    plt.pause(1)
    queue.append(source)
    visited[source] = "grey"  # mark source node as visited
    nx.draw_networkx_nodes(G, pos, nodelist=[source], node_color='grey', node_size=500)
    order = [source]  # to track the order of visited nodes
    while queue:
        curr_node = queue.pop(0)
        plt.pause(1)  # add a delay of 1 second
        print("Visited node:", curr_node)
        for i in G[curr_node]:
            if visited[i] == "white":
                queue.append(i)
                visited[i] = "grey"  # mark node as visited but not finished
                order.append(i)
                nx.draw_networkx_edges(G, pos, edgelist=[(curr_node, i)],
                                       width=2.5, alpha=0.6, edge_color='r')
                nx.draw_networkx_nodes(G, pos, nodelist=[i], node_color='grey', node_size=500)
                plt.draw()
        plt.pause(1)
        visited[curr_node] = "black"  # mark node as finished
        nx.draw_networkx_nodes(G, pos, nodelist=[curr_node], node_color='black', node_size=500)
        plt.draw()
    return order

def BFS_helper(G, source, pos):
    visited = ["white"] * (len(G.nodes()))
    plt.pause(1)
    bfs = []
    for i in range(len(G.nodes())):
        if visited[i] == "white":
            queue = []
            bfs.append(BFS(G, i, pos, visited, queue))
    print("BFS traversal order:", bfs)
    


def CreateGraph():
    G = nx.DiGraph()
    try:
        n = input('Enter number of nodes: ')
        n = n.strip()
        if n.isdigit():
            n = int(n)
            if n <= 0:
                print('Invalid Input')
                exit()

            Matrix = []
            for i in range(n):
                list1 = []
                for j in range(n):
                    print(f'Is there an edge from node {i} to node {j}?')
                    e = int(input('Enter 1 if yes, 0 if no: '))
                    if e != 0 and e != 1:
                        print('Wrong input')
                        exit()
                    list1.append(e)
                Matrix.append(list1)
            source = int(input('Enter source vertex from where BFS has to start: '))
            if source >= n or source<0:
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


def DrawGraph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='white')  # set node_color parameter to 'white'
    return pos


# main function
if __name__ == "__main__":
    G, source = CreateGraph()
    pos = DrawGraph(G)
    BFS_helper(G, source, pos)
