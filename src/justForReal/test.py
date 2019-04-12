# lis = "水星、金星、地球、火星、木星、土星、天王星、海王星"
# lis = lis.split("、")
# for i in lis:
#     print("太阳 行星 "+ i)

lis = [0]*5
lis[1]=1
print(lis)
for index,num in enumerate(lis[1:]):
    print(index)
    index = index+1

    print(index)