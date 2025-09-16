# sa = [1,2,3,4]
# ssum = sum(sa)
# k = len(sa) - 1
# temp = sa[k]

# for i in range(len(sa)):
#     temp = sa[k]
#     ssum -= temp
#     sa[k] = ssum
#     k = k-1
# print(sa)
def calculator():
    print("Expression Calculator")
    print("Type 'exit' to quit.")

    while True:
        expr = input("Enter expression: ")

        if expr.lower() == "exit":
            break

        try:
            result = eval(expr)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

# Run calculator
calculator()
