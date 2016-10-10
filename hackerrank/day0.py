X = list(map(int,input().split()))
W = list(map(float,input().split()))
print (round(sum([i[0]*i[1] for i in zip(X,W)])/sum(W),1))



