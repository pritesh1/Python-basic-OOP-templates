#import function
#print function.square(4,1)

def list(*arg): 
    print arg 

list(1,2)

GRAPH = {1 : [2,3], 2:[4,5], 3:[6], 4:None, 5:[7,8], 6:None, 7:None, 8:None}
print GRAPH[4]
#print k
queue = [0]
queue= queue+ [11]
z= queue.pop(0)
z1= queue.pop(0)


def list(*arg,**kwarg):
    print arg
    print kwarg
    
list(z,z1,2,3,4,x=4,y=5,w=99)
print 1


