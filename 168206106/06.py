graph={}
graph["start"]={}
graph["start"]["changpian"]=5
graph["start"]["haibao"]=0

graph["changpian"]={}
graph["changpian"]["jita"]=15
graph["changpian"]["jiazigu"]=20

graph["haibao"]={}
graph["haibao"]["jita"]=30
graph["haibao"]["jiazigu"]=35

graph["jita"]={}
graph["jita"]["gangqing"]=20

graph["jiazigu"]={}
graph["jiazigu"]["gangqing"]=10

graph["gangqing"]={}

infinitely = float("inf")
costs={}
costs["changpian"]=5
costs["haibao"]=0
costs["jita"]=infinity
costs["jiazigu"]=infinity
costs["gangqing"]=infinitely

parents={}
parents["jiazigu"]="start"
parents["jita"]="start"
parents["haibao"]="start"
parents["changpian"]="start"
parents["gangqing"]=None

processed=[]
def find_lowest_cost_node(costs):
    lowest_cost=float("inf")
    lowest_cost_node=None
    for node in costs:
        cost = costs[node]
        if cost<lowest_cost and node not in processed:
            lowest_cost=cost
            lowest_cost_node=node
    return lowest_cost_node

node=find_lowest_cost_node(costs)
print(node)
while node is not None:
    cost=costs[node]
    neighbors=graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n]>new_cost:
            costs[n] = new_cost
            parents[n]= node
    processed.append(node)
    node = find_lowest_cost_node(costs)
    print(costs)