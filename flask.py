

requirements = [4,6,6,7]
orders = requirements
markings = ["3 5 7", "6 8 9", "3 5 6"]
flasks = markings
#lt = flasks[0].replace(" ",",")


def filterFlasks(orders,flasks):
    rem_flasks=[]

    for flask in flasks:
        add = True
        biggest_flask = int(max(flask.split(" ")))
        
        for order in orders:
            if order>biggest_flask:
                add = False
        if (add):
            rem_flasks.append(flask)    

    return rem_flasks



def getLossOfOrder(orders,flasks):
    flasks = flasks.split(" ")
    
    loss = 0
    for order in orders:
        for flask in flasks:
            flask = int(flask)
            if (flask < order): continue
            loss += flask - order
            #print(flask,order,loss)
            break

    return loss

#print(getLossOfOrder(orders,right_Flasks[0]))

#a = ["4 5 6"]
#b = [["2 3 4"], ["4 5 6"]]
#print(a in b)
right_Flasks = filterFlasks(orders,flasks)

index,correct_Index = -1,-1
loss = None

for flask in flasks:
    
    index +=1
    
    if flask in right_Flasks:
        newLoss = getLossOfOrder(orders,flask)
        print(newLoss)
        if loss is None:
            loss = newLoss
            correct_Index = index
        else:
            if newLoss<loss:
                loss = newLoss
                correct_Index = index
print(correct_Index)