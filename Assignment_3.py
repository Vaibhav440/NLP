import spacy
raw_text='Apple Inc. is planning to open a new store in San Francisco next month.'
NER=spacy.load("en_core_web_sm",disable=["tok2vec","tagger","parser","attribute_ruler","lemmatizer"])
text=NER(raw_text)
for w in text.ents:
  print(w.text,w.label_)

"""
Apple Inc. ORG
San Francisco GPE
next month DATE
"""