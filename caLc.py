import json
import time
import os

def allPathsSourceTarget(graph):
    def dfs(node, path):
        if node == target:
            targets.append(path)
            return

        for neighbor in graph[node]:
            dfs(neighbor, path + [neighbor])

    target = len(graph) - 1
    targets = []
    dfs(0, [0])

    return targets

def graphLoader():
    graphs = list(filter(lambda x: x!=None,map(lambda x: x if "graph" in x else None, os.listdir(os.path.dirname(__file__)))))
    for graph in graphs:
        #print(os.path.join(os.path.dirname(__file__),graph));continue
        with open(os.path.join(os.path.dirname(__file__),graph), 'r') as f:
            yield json.load(f)
graphs = list(graphLoader())

sT = time.time()
res = allPathsSourceTarget(graphs[0])
timePassed = time.time()-sT
lenList = len(res)
print(lenList)
print(timePassed)

with open('output.json', 'w') as f:
    json.dump(res, f, indent = 2)
    f.close()

