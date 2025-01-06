import random
import string

def generate_FirstHalfPass(length):
    while True:
        if length <= 10:
            upper_Alpha = random.choice(string.ascii_uppercase)
            middle_pass = ''
            for _ in range(length-3):
                middle_pass += random.choice(string.ascii_letters)
            
            first_Half = upper_Alpha+middle_pass

            print(first_Half)
            return first_Half
        else:
            print("Maximum length of password is 10")
            break

def generate_SecondHalfPass(isDigit,isSpecial):

    if isDigit:
        digit_pass = str(random.randint(1,10))
    else:
        digit_pass = random.choice(string.ascii_letters)

    if isSpecial:
        special_pass = random.choice(string.punctuation)
    else:
        special_pass = random.choice(string.ascii_letters)

    second_Half = digit_pass+special_pass
    print(second_Half)
    return(second_Half)
    
def getDecision(decision):
    while True:
        if decision=='Y'or decision=='y':
            IsDecision = True
        elif decision == 'N'or decision =='n':
            IsDecision = False
        else:
            print("invalid option,choose properly!")
            break
        return IsDecision

if __name__=='__main__':
    
    length = int(input("Enter the length of the password:"))
    digit = input("Do you need Digit:Y/N")     
    isDigit = getDecision(digit.strip())
    special = input("Do you need to add any special Character:Y/N")
    isSpecial = getDecision(special.strip())

    first = generate_FirstHalfPass(length)
    second = generate_SecondHalfPass(isDigit,isSpecial)
    password = first+second
    print(password)



