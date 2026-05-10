class Solution:

    def calPoints(self, operations: List[str]) -> int:

        n = len(operations)
        myArr = []
        sum = 0


        
        for i in range(n):

            if operations[i] not in ["+", "C", "D"]:
                myArr.append(int(operations[i]))
            elif operations[i] == "+":
                 myArr.append(myArr[-1] + myArr[-2])
            elif operations[i] == "C":
                del myArr[-1]
            elif operations[i] == "D":
                myArr.append(myArr[-1]*2)

        for i in range(len(myArr)):
            print(myArr[i])
            sum += myArr[i]
        
        return sum


    

