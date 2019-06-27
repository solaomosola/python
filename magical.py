magic = [4,2,4,5,2]
dist = [4,4,3,1,3]






def optimizeIt(start,magic,dist,path):
    ret_val=None
    path_len = len(path)
    for i in range(path_len):
        if ret_val == None: 
            ret_val = magic[start] 
        if i<path_len-1:
            ret_val = ret_val - dist[i] + magic[i+1]
        else:
            ret_val = ret_val - dist[i]
        #print(ret_val)
    return ret_val
 
ret_val = -1    

for start in range(len(magic)):
    path = []
    #Get the order for the magic and distance
    for i in range(len(magic)):
        path.append((start + i) % len(magic))
    print(path)

    #Check if its okay
    if (optimizeIt(0,magic,dist,path))== magic[start]:
        ret_val = start
        break
print(ret_val)
