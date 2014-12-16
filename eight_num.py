from node import node
import UserString as us
from functions import expand
end_state=us.MutableString('1238 4765')
open_list=[]
closed_list=[]
count_id=0
#init_state=us.MutableString('1284 3765')
init_state=us.MutableString('2841 3765')
s=node(node_id=count_id,node_state=init_state,father_id=-1,deep=0)
count_id+=1
open_list.append(s)
findn=None
total_states=[]
while(len(open_list)>0):
    bestf=9999999999999
    index=-1
    for n in open_list:
        if n.w+n.deep<bestf:
           index=open_list.index(n)
           bestf=n.w+n.deep
    n=open_list[index]
    open_list.remove(n)
    closed_list.append(n)
    total_states.append(n)
    print len(total_states)
    if n.w==0:
        print "find"
        findn=n
        break

    expand(n,open_list,closed_list)

states=[]
node=findn
while(True):
    states.append(node.node_state)
    if node.current_father<0:
        break
    else:
        for n in closed_list:
            if n.node_id==node.current_father:
                node=n

for state in states[::-1]:
    print state[0:3]
    print state[3:6]
    print state[6:9]
    print ""
    
