def isPalindrome(str):
    if(len(str) == 0 or len(str) == 1):
        return True;
    if(str[0] == str[-1]):
        return isPalindrome(str[1:-1]);
    else:
        return False;


str = input("Enter a string: ");
print("The length of the string is:", len(str));

if(isPalindrome(str)):
    print("The string is a palindrome");
else:
    print("The string is not a palindrome");
