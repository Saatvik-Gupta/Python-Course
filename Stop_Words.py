import nltk #pip install nltk -->Natural Language Tool Kit
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
nltk.download("punkt_tab")

with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()

words = word_tokenize(text)

stop_words = set(stopwords.words("english"))

filtered_words = [
    word for word in words
    if word.lower() not in stop_words
]

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(" ".join(filtered_words))

print("Original text:")
print(text)

print("\nText after removing stop words:")
print(" ".join(filtered_words))

print("\nResult saved in output.txt")