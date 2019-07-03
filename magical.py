magic = [4, 5, 3, 4, 6, 1, 4, 7] 
dist =  [5, 2, 3, 4, 2, 5, 4, 7]

#magic=[2,4,5,2]
#dist = [4,3,1,3]

def fixInput(*arg):
    pass

def optimizeIt(start,magic,dist,path):
   
    if (magic[start]<dist[start]):
        return -1
    
    ret_val=None
    path_len = len(path)
    for i in range(path_len):
        if ret_val == None: 
            ret_val = magic[path[i]] 
        if i<path_len-1:
            ret_val = ret_val - dist[path[i]] + magic[path[i+1]]
        else:
            ret_val = ret_val - dist[path[i]]
      
    return ret_val

ret_index = -1    
ret_val = None
for start in range(len(magic)):
   
    path = []
    #Get the order for the magic and distance
    for i in range(len(magic)):
        path.append((start + i) % len(magic))
  

    if (ret_val is None):
        ret_val = optimizeIt(start,magic,dist,path)
       
        if ret_val>=0:
            ret_index = start
    else: 
        current = optimizeIt(start, magic,dist,path)
        
        if (current>=0):
            if ret_val<0:
                ret_val, ret_index = current, start
                break

       
    
print(ret_index)
