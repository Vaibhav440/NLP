#Bag of words-1
import gensim
from gensim import corpora

#Take the input
text1 = ["""I want to go to school . I am going to school now ."""]

tokens1 = [[item for item in line.split()] for line in text1]
g_dict1 = corpora.Dictionary(tokens1)

#Count number of tokens
print("The dictionary has: " +str(len(g_dict1)) + " tokens\n")
print(g_dict1.token2id)

#Bag of words
g_bow =[g_dict1.doc2bow(token, allow_update = True) for token in tokens1]
print("Bag of Words : ", g_bow)


#TFIDF-2
import pprint
import numpy as np
from gensim import corpora,models
from gensim.utils import simple_preprocess
text = ["The food is excellent but the service can be better",
        "The food is always delicious and loved the service",
        "The food was mediocre and the service was terrible"]

g_dict = corpora.Dictionary([simple_preprocess(line) for line in text])
g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in text]

print("Dictionary : ")
for item in g_bow:
    print([[g_dict[id], freq] for id, freq in item])

g_tfidf = models.TfidfModel(g_bow, smartirs='ntc')
print(" ")
print("TF-IDF Vector:")
for item in g_tfidf[g_bow]:
    print([[g_dict[id], np.around(freq, decimals=2)] for id, freq in item])



#Word2vec
from gensim.models.word2vec import Word2Vec
from multiprocessing import cpu_count

data = [
    "Open Visual Studio Code.",
    "Import the NLTK library",
    "Apart from individual data packages",
    "word2vec is a popular word",
]

# Tokenize the text data (split sentences into words)
tokenized_data = [sentence.split() for sentence in data]

# Create a Word2Vec model
w2v_model = Word2Vec(tokenized_data, min_count=0, workers=cpu_count())

# Find the most similar words to 'word'
similar_words = w2v_model.wv.most_similar('word')

for word, score in similar_words:
    print(f"{word}:{score}")