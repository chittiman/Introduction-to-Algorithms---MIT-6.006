class StaticArray():
    def __init__(self,n):
        self.data = [None]*n

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self,i):
        if i < len(self):
            return self.data[i]
        else:
            raise Exception('Index is out of range')
        
    def __setitem__(self,i,x):
        if i < len(self):
            self.data[i] = x
        else:
            raise Exception('Index is out of range')
        
    def __repr__(self) -> str:
        return str(self.data)
    
    def __iter__(self):
        return (i for i in self.data)
        #Alt - yield from self.data
    
    @classmethod
    def build(cls,sequence):
        seq_len = len(sequence)
        arr = cls(seq_len)
        for i,item in enumerate(sequence):
            arr[i] = item
        return arr
    
# Usage:
#new_instance = StaticArray.build("value1", "value2")


        
if __name__ == "__main__":
    x = StaticArray.build([1,2,3])
    print(type(x))
