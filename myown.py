def add(var1, var2):
    print("Adding ", var1, " And ",var2)
    return var1+var2

def sub(var1, var2):
    print("Substracting ", var1, " And ",var2)
    return var1-var2

# Defining main function
def main():
    print("hey there")
    print(sub(1,2))


# Using the special variable 
# __name__
if __name__=="__main__":
    main()