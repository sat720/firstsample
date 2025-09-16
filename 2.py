# for multiple numbers addition and then conversion


num = input("Enter numbers seperated by space for addition to get final only one number: \n")
num = num.split(" ")
pro = 0
base = []
for j in range(2,63):
    base.append(j)
hexi = []
for i in range(ord("A"),(ord("Z")+1)):
    hexi.append(chr(i))
for i in range(ord("a"),(ord("z")+1)):
    hexi.append(chr(i))
for i in num:
    pro+= int(i)
num = pro
print("\nThe coversions of ",num,"are: \n")

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
        # For hexadecimal
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
