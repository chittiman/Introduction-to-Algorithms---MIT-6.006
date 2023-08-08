from static_array import StaticArray
class DynamicArray(StaticArray):
    def __init__(self, n):
        super().__init__(n)

    def insert_at(self,i,x):
        if i <= len(self):
            old_data = self.data
            old_len = len(self)
            new_len = old_len + 1
            self.data = [None]*new_len
            for j in range(0,i):
                self[j] = old_data[j]
            self[i] = x
            for j in range(i+1, new_len):
                self[j] = old_data[j-1]
        else:
            raise Exception('Index is out of range')

    def delete_at(self,i):
        if 0<=i< len(self):
            old_len = len(self)
            new_len = old_len - 1
            del_item = self[i]
            for j in range(i,new_len):
                self[j] = self[j+1]
            self.data = self.data[:new_len]
            return del_item
        else:
            raise Exception('Index is out of range')

    def insert_first(self,x):
        self.insert_at(0,x)

    def delete_first(self):
        return self.delete_at(0)
    
    def insert_last(self,x):
        self.insert_at(len(self),x)
    
    def delete_last(self):
        return self.delete_at(len(self)-1)
if __name__ == "__main__":
    x = DynamicArray.build([1,2,3])
    x.insert_at(1,5)
    print(x)
    x.delete_at(2)
    print(x)
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         print("Generic animal sound")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         # Calling the parent class constructor using super()
#         super().__init__(name)
#         self.breed = breed

#     def make_sound(self):
#         print("Woof! Woof!")

# # Creating an instance of Dog
# dog_instance = Dog("Buddy", "Labrador")

# # Accessing attributes of the Dog instance
# print(dog_instance.name)   # Output: Buddy
# print(dog_instance.breed)  # Output: Labrador

# # Calling methods of the Dog instance
# dog_instance.make_sound()  # Output: Woof! Woof!
