class block():
    def __init__(self,data,bno,prev_block):
        self.data = data
        self.bno = bno
        self.prev_block = prev_block
        return

    def disp_block(self):
        print()
        print('Block Number : {}'.format(self.bno))
        print('Block data : {}'.format(self.data))
        print('Previous Block: {}'.format(self.prev_block))
        return


block0 = block('This is the Genesis block', 0, None)
ll = [block0]

for i in range(1,11):
    ll.append(block('This is block {0}'.format(i),i,i-1))


for block in ll:
    block.disp_block()
    

    
    
    