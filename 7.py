# for multiple sets seperated by space where each set is either number itself 
# or it is string which is evaluated to get a number and then that number conversion

# this is after changing


numo = input("Enter sets seperated by space where each set is number or string evaluated to number : \n")
numo = numo.split(" ")

base = []
for j in range(2,63):
    base.append(j)
hexi = []
for i in range(ord("A"),(ord("Z")+1)):
    hexi.append(chr(i))
for i in range(ord("a"),(ord("z")+1)):
    hexi.append(chr(i))
for nim in numo:
    
    num = eval(nim)
    print("\nThe conversions of ",num,": ")
    for b in base:
        copy1 = num
        copy2 = copy1
        if b < 10:
            # For binary and octal
            numr = ""
            while copy1 > 0:
                rem = copy1 % b
                numr = numr + str(rem)
                copy1 //= b
            result = ""
            while len(numr)%4 != 0:
                numr +=  "0"
                            
            for i in range(0, len(numr), 4):
                result += numr[i:i+4] + " "
            result = result[::-1]
            numr = result
            if copy2 == 0:
                numr = "0000"
            print("base",b,"  :",numr)
        else:
            # For more than 10
            numr = ""
            while copy1 > 0:
                rem = copy1 % b
                if rem >= 10:
                    numr += hexi[rem - 10]
                else:
                    numr += str(rem)
                copy1 //= b
            result = ""
            while len(numr)%4 != 0:
                numr +=  "0"
            for i in range(0, len(numr), 4):
                result += numr[i:i+4] + " "
            result = result[::-1]
           
            numr = result  # reverse once at the end
            if copy2 == 0:
                numr = "0000"
            print("base",b," :",numr)
