def dosum():
    i=1;j=0
    for i in range(1,101):
        j+=i
        ++i
    return j

if __name__ == "__main__":
    
    print ("the result is %d" %dosum())
