"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #12 - One Up! (addone.py)


Author: Paul Thai

Difficulty Level: 6/10

Background: Do you know how to add? Good! I have just the question for you! 
Most people know how to add by one, but can you add by one in this problem???

Prompt: Given an array, add one to the ones column!

Constraints: You cannot map/join the list into a single number, add one, and then turn it back into a list. 
That's cheating (because I have done it before...) so you must modify the list itself. Be careful of place values! 

Test Cases:
a = [1, 2, 3]; output = [1, 2, 4]
a = [9]; output = [1,0]
a = [1, 4, 5, 9]; output = [1]
"""

class Solution:
    def addOne(self,ary):
        # type ary: list
        # return type: list

        # TODO: Write code below to return a list "ary" with the solution to the prompt
        add = True
        
        for i in range(len(ary)-1, -1, -1):
            print(i)
            if (add):
                ary[i] = ary[i] + 1
                if (ary[i] < 10):
                    add = False
                
                elif (ary[i] > 9 and i == 0):
                    ary[i] = 0
                    print("hi")
                    ary.insert(0, 1)
                
                else:
                    ary[i] = 0
        
            
        return ary

def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = int(array[x])

    tc1 = Solution()
    ans = tc1.addOne(array)
    print(ans)

if __name__ == "__main__":
    main()