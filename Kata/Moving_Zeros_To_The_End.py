def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)
    #m = []
    #zero = 0
    #for i in array:
    #    if i == 0 and type(i) is not bool:
    #        zero +=1
    #    else:
    #        m.append(i)
    #for i in range(zero):
    #    m.append(0)
    #return m


print(move_zeros([0.0,"a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))
