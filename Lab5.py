'''
Lester Ibarra
80578839
Diego Aguirre
'''

#min heap class
class Heap:
    def __init__(self):#class constructor to build an array
        self.heap_array = []



    def insert(self, key): #insert values into heap array
        self.heap_array.append(key)
        for i in range(1, len(self.heap_array)):

            parentIndex = (i - 1) //2
            if (self.heap_array[i]>= self.heap_array[parentIndex]):
                return
            else:
                self.swap(parentIndex, i)
            i = parentIndex



    def heapify(self, i):#switches values of parent and child if child is smaller than parent
        n = len(self.heap_array)
        parent = i
        leftChild = (2*i)+1
        rightChild = (2*i)+2
        
        if leftChild < n and self.heap_array[i] > self.heap_array[leftChild]:
            parent = leftChild#the parent will equal to the left child if smmaller

        if rightChild < n and self.heap_array[parent] > self.heap_array[rightChild]:
            parent = rightChild#the parent will equal to the right child if smaller

        if parent != i:
            self.swap(i, parent)#swaps parent with smallest child, if child is smaller
            self.heapify(parent)
        #method uses if statments since both children could be smaller than the parent
        #but you want the smallest child 


    def heapSort(self):#Sorts in decending order
        size = len(self.heap_array)
        #temp array to hold the root item every time is is removed
        temp = []

        #for loop to traverse the array and pop the root into the temp array
        for i in range(size):
            temp.append(self.heap_array[0])
            self.swap(0, len(self.heap_array) - 1)
            self.heap_array = self.heap_array[:len(self.heap_array) - 1]
            self.heapify(0)

        #overwritting the heap array with the temp array
        self.heap_array = temp



    def is_empty(self):#checks if heap array is empty
        return len(self.heap_array) == 0



    def extract_min(self):#extracts the minimum value in the array
        if self.is_empty():
            return None



        #assign the value of the root to min
        #the root is now swapped and heapified
        #lastly the array is shortened by one
        min = self.heap_array[0]
        end = len(self.heap_array)-1
        self.swap(0, end)
        self.heap_array = self.heap_array[:end]
        self.heapify(0)

        #return the value of the smallest integer in the array
        return min

    #helper method used to print a heap array
    def print(self):
        print(self.heap_array)

        print("Length of the array: %d" % len(self.heap_array))

    #helper method to swap array values
    def swap(self, parent, child):
        self.heap_array[parent], self.heap_array[child] = self.heap_array[child], self.heapArr[parent]



def read(heap):#Reads txt file to input into heap
    try:
        file = input("Enter file name:")
        #method used to read the txt file
        read = open(file, "r").read().split(",")
        for i in read:
            entry = int(i)
            if entry >= 0:
                heap.insert(entry)
        return True
    except FileNotFoundError:
        print("File not found.\n")
        return False
    
    
    
def menu():
    menu = ["a", "b", "c", "d", "e", "f"]

    user = input("\nChoose an option\n\nA) Display Min Heap of Inserted txt File\nB) Insert Number\nC) Extract Minimum Number\nD) Check If Heap Is Empty\nE) Sort the List\n Exit\n")
    if user.lower() in menu:#checks in lower case to avoid  any case sensitivity
        return user.lower(), True
    else:
        print("Invalid option")
        return user, False
    
    
    
def main():
    heap = Heap()
    status = False

    while status is False:
        status = read(heap)
    #variable used to keep the program running
    cont = True
    while cont is True:
        status = False
        while status is False:
            user, status = menu()

        #call method to print min heap array
        if user == "a":
            print("\nMin Heap List: \n")
            heap.print()
        #require user to input any number in to created heap
        elif user == "b":
            status = False
            while status is False:
                user = input("Please enter a digit you wish to insert: ")
                try:
                    number = int(user)
                    heap.insert(number)
                    print("The new heap is: ")
                    heap.print()
                    print("\n")
                    status = True
                except ValueError:
                   print("Make sure to insert an integer")

        #print the minimum number and print the new list
        elif user == "c":
            minNumber = heap.extract_min()
            print("The minimum extracted is: %d\n" % minNumber)
            print("The new list is: ")
            heap.print()

        elif user == "d": #call method to check in heap is empty
            answer = heap.is_empty()
            print(answer)

        elif user == "e":#sorts heap with minHeap
            heap.heapSort()
            heap.print()

        elif user == "f":#Stops program
            cont = False


main()
#end of program
