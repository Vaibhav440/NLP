import spacy
nlp = spacy.load("en_core_web_sm")
about_text = (
    "Gus Proto is a Python developer currently"
    " working for a London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
)
about_doc = nlp(about_text)
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )
    
/*






TOKEN: Gus
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singularTOKEN: Gus
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: Proto
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: is
=====
TAG: VBZ        POS: AUX
EXPLANATION: verb, 3rd person singular present

TOKEN: a
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: Python
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: developer
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: currently
=====
TAG: RB         POS: ADV
EXPLANATION: adverb

TOKEN: working
=====
TAG: VBG        POS: VERB
EXPLANATION: verb, gerund or present participle

TOKEN: for
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: a
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: London
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: -
=====
TAG: HYPH       POS: PUNCT
EXPLANATION: punctuation mark, hyphen

TOKEN: based
=====
TAG: VBN        POS: VERB
EXPLANATION: verb, past participle

TOKEN: Fintech
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: company
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer

TOKEN: He
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: is
=====
TAG: VBZ        POS: AUX
EXPLANATION: verb, 3rd person singular present

TOKEN: interested
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: in
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: learning
=====
TAG: VBG        POS: VERB
EXPLANATION: verb, gerund or present participle

TOKEN: Natural
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: Language
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: Processing
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer
exam@exam-M52AD-M12AD-A-F-K31AD:~$ 


TOKEN: Proto
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: is
=====
TAG: VBZ        POS: AUX
EXPLANATION: verb, 3rd person singular present

TOKEN: a
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: Python
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: developer
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: currently
=====
TAG: RB         POS: ADV
EXPLANATION: adverb

TOKEN: working
=====
TAG: VBG        POS: VERB
EXPLANATION: verb, gerund or present participle

TOKEN: for
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: a
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: London
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: -
=====
TAG: HYPH       POS: PUNCT
EXPLANATION: punctuation mark, hyphen

TOKEN: based
=====
TAG: VBN        POS: VERB
EXPLANATION: verb, past participle

TOKEN: Fintech
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: company
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer

TOKEN: He
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: is
=====
TAG: VBZ        POS: AUX
EXPLANATION: verb, 3rd person singular present

TOKEN: interested
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: in
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: learning
=====
TAG: VBG        POS: VERB
EXPLANATION: verb, gerund or present participle

TOKEN: Natural
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: Language
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: Processing
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer
exam@exam-M52AD-M12AD-A-F-K31AD:~$ 












*/
