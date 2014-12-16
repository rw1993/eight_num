import UserString
end_state=UserString.MutableString("1238 4765")
class node:
    def __init__(self,node_id,node_state,father_id,deep):
        self.node_id=node_id
        self.node_state=node_state
        self.w=self.count_w()
        self.current_father=father_id
        self.deep=deep
        self.fathers=[]
        self.fathers.append(father_id)
    def count_w(self):
        global end_state
        count=0
        for i in range(0,9):
            if end_state[i]!=self.node_state[i] and self.node_state[i]!=" ":
                count+=1
        return count

