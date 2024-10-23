import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}

word = None
while word != "":
    word = input("Enter a word: ").upper()
    if word != "":
        word_nato = [nato_dict[letter] for letter in word]
        print(word_nato)
        print("")
