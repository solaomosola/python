#magic = [5,10,6,3,8,1]
#dist =  [5,1,3,8,4,3]

magic=[8,4,1,9]
dist = [10,9,3,5]

def optimizeIt(start,magic,dist,path):
    
    ret_val=None
    path_len = len(path)
    for i in range(path_len):
        if ret_val == None: 
            ret_val = magic[start] 
        if i<path_len-1:
            ret_val = ret_val - dist[path[i]] + magic[path[i+1]]
        else:
            ret_val = ret_val - dist[path[i]]
        #print(i,path_len,path,start,ret_val)
    return ret_val
 
ret_index = -1    
ret_val = None
for start in range(len(magic)):
    path = []
    #Get the order for the magic and distance
    for i in range(len(magic)):
        path.append((start + i) % len(magic))
    #print(path)

    #Check if its okay
    if (ret_val is None):
        ret_val = optimizeIt(start,magic,dist,path)
        if ret_val>=0:
            ret_index = start
    current = optimizeIt(start,magic,dist,path)
    if (ret_val> current and current>=0):
        ret_val = current
        ret_index = start
    
print(ret_index)
