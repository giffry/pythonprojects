#coding standards
#.................

#1 snake case
#2 camelcase
#3 pascal

results=[
    {"district":"tvm","win":98,"A+":45000},
    {"district":"ktm","win":95,"A+":44000},
    {"district":"apy","win":97,"A+":47000},
    {"district":"idk","win":90,"A+":38000},
    {"district":"ekm","win":99,"A+":56000},
    {"district":"pta","win":99,"A+":58000},
    {"district":"tsr","win":98,"A+":57000},
    {"district":"kzd","win":99,"A+":58000},
    {"district":"pkd","win":95,"A+":50000},
    {"district":"mpm","win":90,"A+":4500},
]

# tvm_win=[i["win"] for i in results if i["district"]=="tvm"]
# print(tvm_win)

# results.sort(key=lambda i:i["win"],reverse=True)
# print(results)
#
# print(max(results,key=lambda i:i["win"]))
# print(min(results,key=lambda i:i["win"]))
# print(max(results,key=lambda i:i["A+"]))
# print(min(results,key=lambda i:i["A+"]))

aplus=sum([i["A+"]for i in results])
print(aplus)
