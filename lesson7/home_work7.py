while True:
    def palindrome():
        a = input("Enter your number: ")
        if a == a[:: -1]:
            return True
        else:
            return False
    print(palindrome())