import spacy
nlp = spacy.load("en_core_web_sm")
about_text = (
     "sanket is good boy"
    " sachin loves akole"
    " piyush is very smart boy "
    " Natural Language Processing."
)
about_doc = nlp(about_text)

for token in about_doc:
     print (token, token.idx)