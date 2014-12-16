import UserString as us
from node import node
def swap(i,state,index,newstates):
    ifnewstate=False
    string=us.MutableString(str(state))
    if i==0:#up
        if index/3!=0:
            string[index]=state[index-3]
            string[index-3]=" "
            ifnewstate=True
    elif i==1:#down
        if index/3!=2:
            ifnewstate=True
            string[index]=state[index+3]
            string[index+3]=" "
    elif i==2:#left
        if index%3!=0:
            string[index]=state[index-1]
            string[index-1]=" "
            ifnewstate=True
    elif i==3:#right
        if index%3!=2:
            string[index]=state[index+1]
            string[index+1]=" "
            ifnewstate=True
    if ifnewstate:
        newstates.append(string)


def get_new_states(state):
    newstates=[]
    index=state.index(" ")
    for i in range(0,4):
        swap(i,state,index,newstates)
    return newstates
def expand_node(n,state,open_list,closed_list):
    flag=0
    index=-1
    for o in open_list:
        if o.node_state==state:
            index=open_list.index(o)
            flag=1
            break
    for c in closed_list:
        if c.node_state==state:
            flag=2
            break
    if flag==0:
        id=len(open_list)+len(closed_list)
        newn=node(node_id=id,node_state=state,father_id=n.node_id,deep=n.deep+1)
        open_list.append(newn)
    elif flag==1:
        open_list[index].fathers.append(n.node_id)
        if n.deep+1<open_list[index].deep:
            open_list[index].current_father=n.node_id
            open_list[index].deep=n.deep+1
            


def expand(n,open_list,closed_list):
    newstates=get_new_states(n.node_state)
    for state in newstates:
        expand_node(n,state,open_list,closed_list)

