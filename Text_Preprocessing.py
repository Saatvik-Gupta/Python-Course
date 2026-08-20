# Text_Preprocessing- Program for removing Punctuations from a given string of sentence

sentence=input("Enter the String:")

result=" "
for ch in sentence:
    if(ch.isalnum() or ch==" "):
        result+=ch

print(f"String {sentence} without Punctuations is:{result}\n")

# To sort the sentence in ascending order

words=sentence.split() # created a list or a collection of strings

words.sort(key=str.lower)  # key=str.lower makes all words in lowecase and than compare ascii
# otherwise A-Z: 65-90 and a-z:97-122 Upeercase comes first than lower if not key=str.lower/upper

print(f"Sorted Words in {sentence} are : {words}")