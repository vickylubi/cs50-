#Ask for input 
def main():
    text = input("Input ")
    output = remove_vowels(text)
    print(f"Output: {output}")
    
#Check each letter if it is a vowel (A, E, I, O, and U)
def remove_vowels(letters):
    vowels = "aeiou"
    result = ""
    for letter in letters:
        if letter.lower() not in vowels:
            result += letter
    return (result)
    
#Return the word without vowels 
main()