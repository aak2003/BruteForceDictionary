import itertools

small_alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

capital_alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

slash = chr(92)

symbols = ['<','>',',','.','"',"'",':',';','[',']','{','}','!','@','#','$','%','^','&','*','(',')','+','=','_','-','/','|','~','`','?', slash]

# Total number of characters: 94
# Password length range: 8-63(in a for loop its till 64)

main = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '<', '>', ',', '.', '"', "'", ':', ';', '[', ']', '{', '}', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '=', '_', '-', '/', '|', '~', '`', '?', slash]

# The main list consists of all the 94 characters.

def create():
    with open('passlist.txt','w') as f:
        #for j in range(8,64):
        t=list(itertools.permutations(main,8))
        for i in range(0,len(t)):
            k = ''.join(t[i])
            f.write(k)
            f.write("\n")
    f.close()

def number_of_passwds():
    with open('passlist.txt','r') as f:
        data = f.read()
        print(len(data))

def start():
    while 1:
        com = input("Enter 1 to create a password file\n 2 to check the number of passwords: ")
        while 1:
            if com=="1":
                create()
                break
            elif com=="2":
                number_of_passwds()
                break
            else:
                print("Please enter a valid option!")
                break
start()