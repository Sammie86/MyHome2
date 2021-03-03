# Please read string from user
s = input()
# Initializing reverse String to ""
reverseString = ""
# Looping through each character of the input
for i in range(len(s)):
    # Check s[i] is not a space
    if(s[i]!=' '):
        # prepending s[i] to reverseString
        reverseString = s[i] + reverseString
# Check s and reverseString are same
if (s==reverseString):
    # Print message
    print(s,"is a palindrome")
else:
    # Print message if both strings are not equal
    print(s,"is not a palindrome")