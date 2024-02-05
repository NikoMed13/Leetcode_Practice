def Palindrome_number(number):
    number_string = str(number)
    if number_string == number_string[::-1]:
        return True
    else:
        return False

def main():
    print(Palindrome_number(121))
    print(Palindrome_number(-121))
    print(Palindrome_number(10))
if __name__ == "__main__":
    main()
    
    