
class DynamicArraySeq:
    def __init__(self,ratio = 2):
        self.size = 0
        self.ratio = ratio
        self._compute_bounds()
        self.data = self._allocate_space()
        self.set_space()

    def _allocate_space(self):
        size = max(self.size,1)*self.upper_bound
        return [None]*size
        
    def _compute_bounds(self):
        self.lower_bound = 1 / (self.ratio*self.ratio)
        self.upper_bound = self.ratio

    def __len__(self):
        return self.size
    
    def __iter__(self):
        for i in range(self.size):
            yield self.data[i]

    def __repr__(self):
        return str(list(self))
    
    def set_space(self):
        self.space = len(self.data)

    def insert_last(self,x):
        pres_len = len(self)
        if pres_len < self.space:
            self.data[pres_len] = x
            self.size +=1
        else:
            new_data = self._allocate_space()
            for i in range(pres_len):
                new_data[i] = self.data[i]
            new_data[pres_len] = x
            self.data = new_data
            self.set_space()
            self.size +=1
    
    def build(self,sequence):
        for item in sequence:
            self.insert_last(item)

    def insert_at(self,i,x):
        pres_len = len(self)
        if i == pres_len:
            self.insert_last(x)
            return None
        if pres_len < self.space:
            for j in reversed(range(i,pres_len)):
                self.data[j+1] = self.data[j]
            self.data[i] = x
            self.size += 1 
        else:
            new_data = self._allocate_space()
            for j in range(i):
                new_data[j] = self.data[j]
            new_data[i] = x
            for j in range(i,pres_len):
                new_data[j+1] = self.data[j]
            self.data = new_data
            self.set_space()
            self.size += 1
    
    def insert_first(self,x):
        self.insert_at(0,x)

    # def delete_last(self):
    #     pres_len = len(self)
    #     new_len = pres_len -1
    #     del_item = self.data[new_len]
    #     self.data[new_len] = None
    #     self.size -= 1
    #     if len(self)/self.space < self.lower_bound:
    #         new_data = self._allocate_space()
    #         for i in range(new_len):
    #             new_data[i] = self.data[i]
    #         self.data = new_data
    #         self.set_space()
    #     return del_item

    def delete_at(self,i):
        pres_len = len(self)
        if 0 <= i < pres_len:
            new_len = pres_len -1
            del_item = self.data[i]
            for j in range(i,new_len):
                self.data[j]= self.data[j+1]
            self.data[new_len] = None
            self.size -= 1
            if len(self)/self.space < self.lower_bound:
                new_data = self._allocate_space()
                for i in range(new_len):
                    new_data[i] = self.data[i]
                self.data = new_data
                self.set_space()
            return del_item
        else:
            raise Exception('Index is out of range')
        
    def delete_last(self):
        return self.delete_at(len(self)-1)

    
    def delete_first(self):
        return self.delete_at(0)
    
if __name__ == '__main__':
    dynamic_array = DynamicArraySeq()
    dynamic_array.size = 3
    dynamic_array.data = [1, 2, 3,None]
    dynamic_array.space = 4
    dynamic_array.insert_last(4)
    assert len(dynamic_array) == 4
    assert list(dynamic_array) == [1, 2, 3, 4]