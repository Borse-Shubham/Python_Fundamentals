import sys 

def main():
    print("Demonstration of command line arguments")

    value1 = int(sys.argv[1])
    value2 = int(sys.argv[2])    
    Ans = value1 + value2

    print("Addition is : ",Ans)
if __name__=="__main__":
    main()