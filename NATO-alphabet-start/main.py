import pandas

df=pandas.read_csv("nato_phonetic_alphabet.csv")

# print(df)




#TODO 1. Create a dictionary in this format:
nato_dict={phonetic.letter:phonetic.code for (word, phonetic) in df.iterrows()}

print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name=input("Enter A Name").upper()
letters=[nato_dict[letter] for letter in name]
print(letters)

