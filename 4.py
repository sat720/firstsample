# for multiple numbers and each number conversion


numo = input("Enter multiple numbers seperated by space where each number is converted: \n")
numo = numo.split(" ")
for i in range(len(numo)):
    numo[i]= int(numo[i])

base = []
for j in range(2,63):
    base.append(j)
hexi = []
for i in range(ord("A"),(ord("Z")+1)):
    hexi.append(chr(i))
for i in range(ord("a"),(ord("z")+1)):
    hexi.append(chr(i))
for num in numo:
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
