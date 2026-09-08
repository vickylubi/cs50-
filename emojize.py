import emoji 

def main():
    sentence = input("Input: ")
    print(emoji.emojize(sentence, language='alias'))

main()
