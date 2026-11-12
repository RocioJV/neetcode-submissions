class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = "" #empty string for the letters 
        for i in s: #i iterates through our string s
            # this function allows us to use .isalpha method 
            if i.isalnum(): #returns True if all the characters are alphabet letters
                letters += i.lower() #this adds the letter to our empty sting
        if letters == letters[::-1]:
            return True
        else:
            return False

            
                
