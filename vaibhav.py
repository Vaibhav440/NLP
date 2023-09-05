import spacy
nlp = spacy.load("en_core_web_sm")
conference_help_text = (
    "sachin is good boy"
    " sachin loves srirampur"
    " tushar is very gental boy"
    " piyush is from nashik."
)
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")
        
        
/*

                  is : be
               loves : love
                  is : be
                  is : be

*/
