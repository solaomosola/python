#gridOfNodes = [[0,1,0,0,1,1,1,1], [0,1,0,0,1,1,1,1],[0,0,0,0,0,0,0,0],[0,1,0,0,1,1,1,1]]
gridOfNodes = [[1,0,1,1],[0,1,1,0],[0,0,0,0],[1,0,0,0]]
count = 0
row_index = 0
gridOfNodes_len = len(gridOfNodes)
newgridOfNodes = []

while row_index < gridOfNodes_len:
    if 1 in gridOfNodes[row_index]:
        newgridOfNodes.append(gridOfNodes[row_index])
    row_index+=1

gridOfNodes_len = len(newgridOfNodes)
row_index = 0
while row_index<gridOfNodes_len-1:
    for a in newgridOfNodes[row_index]:
        for b in newgridOfNodes[row_index+1]:
            count+= (a*b)
    row_index+=1

print(count)
#for a in gridOfNodes:
#    print(1 in a)
