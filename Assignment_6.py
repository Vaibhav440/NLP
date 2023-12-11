import spacy
from spacy import displacy
nlp=spacy.load("en_core_web_sm")
text="I ma vaibhav who loves Ishwar itesms"
doc=nlp(text)
for token in doc:
  print(
      
      f"""
      TOKEN:{token.text}

      ===
      {token.tag_=}
      {token.head.text=}
      {token.dep_=}"""
  )

  displacy.serve(doc,style="dep")