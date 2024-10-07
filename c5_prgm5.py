import nltk
from nltk import ngrams
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Sample text
text1 = "The data given satisfies the requirement for model generation. This is used in Data Science Lab."

print("Sentence tokenization:")
print(sent_tokenize(text1))

print("\nWord tokenization:")
print(word_tokenize(text1))

# Tokenize words and remove stop words
text = word_tokenize(text1)
stop_words = set(stopwords.words('english'))
text2 = [word for word in text if word.lower() not in stop_words]

print("\nRemoving stop words:")
print(text2)

print("\nN-grams (3-grams):")
unigrams = ngrams(text2, 3)
for grams in unigrams:
    print(grams)
