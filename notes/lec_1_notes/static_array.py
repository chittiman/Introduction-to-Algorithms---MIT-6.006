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
        
if __name__ == "__main__":
    x = StaticArray(5)
    x[1] = 1
    for i in x:
        print(i)
