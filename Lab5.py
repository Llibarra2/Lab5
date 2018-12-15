'''
Lester Ibarra
80578839
Diego Aguirre
'''

import time

#min heap class
class Heap:
    #class constructor to build an array
    def __init__(self):
        self.heapArr = []

    #method used to insert items in to the array
    def insert(self, key):
        self.heapArr.append(key)
        index = len(self.heapArr) - 1

        while index > 0:

            parentIndex = (index - 1) //2
            if (self.heapArr[index]>= self.heapArr[parentIndex]):
                return
            else:
                self.swap(parentIndex, index)
            index = parentIndex

        #method to extract the minimum value in the array
    def extract_min(self):
        if self.is_empty():
            return None

        #assign the value of the root to min
        #the root is now swapped and heapified
        #lastly the array is shortened by one
        min = self.heapArr[0]
        end = len(self.heapArr)-1
        self.swap(0, end)
        self.heapArr = self.heapArr[:end]
        self.heapify(0)
    #method used to balance the min heap and sustain the min heap properties
    def heapify(self, i):
        n = len(self.heapArr)
        parent = i
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2

        #if statement to check if child is larger than the parent
        if leftChild < n and self.heapArr[i] > self.heapArr[leftChild]:
            parent = leftChild

        #if statement to check if child is larger than the parent
        if rightChild < n and self.heapArr[parent] > self.heapArr[rightChild]:
            parent = rightChild

        #parent is swapped if a larger value is found
        if parent != i:
            self.swap(i, parent)
            self.heapify(parent)

    #sort method to organize numbers in descending order
    def heapSort(self):
        size = len(self.heapArr)
        #temp array to hold the root item every time is is removed
        temp = []

        #for loop to traverse the array and pop the root into the temp array
        for i in range(size):
            temp.append(self.heapArr[0])
            self.swap(0, len(self.heapArr) - 1)
            self.heapArr = self.heapArr[:len(self.heapArr) - 1]
            self.heapify(0)

        #overwritting the heap array with the temp array
        self.heapArr = temp

    #method created to check if the heap array is empty
    def is_empty(self):
        return len(self.heapArr) == 0


        #return the value of the smallest integer in the array
        return min

    #helper method used to print a heap array
    def print(self):
        print(self.heapArr)

        print("Length of the array: %d" % len(self.heapArr))

    #helper method to swap array values
    def swap(self, parent, child):
        self.heapArr[parent], self.heapArr[child] = self.heapArr[child], self.heapArr[parent]

#method used to read a txt file and insert it into a heap array
def read(heap):
    try:
        file = input("Enter file name:")
        #method used to read the txt file
        read = open(file, "r").read().split(",")
        for i in read:
            #the value is hard coded into an integer
            entry = int(i)
            if entry >= 0:
                heap.insert(entry)
        return True
    except FileNotFoundError:
        #error for invalid input
        print("File not found. Please try again\n")
        return False
start = time.time()
def menu():
    menu = ['a', 'b', 'c', 'd', 'e', 'f']
    user = input("\nChoose one of the following options: \n\nA) Show the Min Heap\nB) Insert int value \nC) Extract Minimum Number\nD) Check If Heap Is Empty\nE) Sort the List\n F)Exit\n")
    if user in menu:#checks if users input is in the array: menu
        return user, True
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
        if user == 'a':
            print("\nMin Heap List: \n")
            heap.print()
        #require user to input any number in to created heap
        elif user == 'b':
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
        elif user == 'c':
            minNumber = heap.extract_min()
            print("The minimum extracted is: %d\n" % minNumber)
            print("The new list is: ")
            heap.print()

        elif user == 'd': #call method to check in heap is empty
            answer = heap.is_empty()
            print(answer)

        elif user == 'e': #sorts heap with minHeap
            heap.heapSort()
            heap.print()

        elif user == 'f': #Stops program
            cont = False
            end = time.time()
            print(end - start)


main()
#end of program
