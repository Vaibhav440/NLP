import spacy 
from collections import Counter
nlp=spacy.load("en_core_web_sm")
text=("Your smile makes me smile"
    "Your laugh makes me laugh"
    "Your eyes are enchanting"
    "You make my thoughts seem daft."
    "Since the day I first laid eyes on you,"
    "My feelings grew and grew."
    "In that first conversation my knees clicked and clacked,"
    "And those butterflies flipped and flapped."
    "And as I spill these simple rhymes"
    "My mind goes over time and time,"
    "I have a crush, a little teenage crush"
    "I don't know what to do, about this lovely little crush")
doc=nlp(text)

#Tokenization

for token in doc:
  print(token,token.idx)


print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
# Stop Word Removal

print([token for token in doc if not token.is_stop])


print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

# Word Frequency

word=[
    token.text
    for token in doc
    if not token.is_stop and not token.is_punct
]

print(Counter(word).most_common(5))


print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

#Lemmatization

for token in doc:
  if str(token)!=str(token.lemma_):
    print(f"{str(token)}:{str(token.lemma_)}")

print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")


#Part_of_speech


for token in doc:
    print(
        f"""
        TOKEN:{str(token)}
        =====
        TAG: {str(token.tag_):10} POS: {token.pos_}
        EXPLANATION: {spacy.explain(token.tag_)}"""
    )

"""
Your 0
smile 5
makes 11
me 17
smileYour 20
laugh 30
makes 36
me 42
laughYour 45
eyes 55
are 60
enchantingYou 64
make 78
my 83
thoughts 86
seem 95
daft 100
. 104
Since 105
the 111
day 115
I 119
first 121
laid 127
eyes 132
on 137
you 140
, 143
My 144
feelings 147
grew 156
and 161
grew 165
. 169
In 170
that 173
first 178
conversation 184
my 197
knees 200
clicked 206
and 214
clacked 218
, 225
And 226
those 230
butterflies 236
flipped 248
and 256
flapped 260
. 267
And 268
as 272
I 275
spill 277
these 283
simple 289
rhymesMy 296
mind 305
goes 310
over 315
time 320
and 325
time 329
, 333
I 334
have 336
a 341
crush 343
, 348
a 350
little 352
teenage 359
crushI 367
do 374
n't 376
know 380
what 385
to 390
do 393
, 395
about 397
this 403
lovely 408
little 415
crush 422
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
[smile, makes, smileYour, laugh, makes, laughYour, eyes, enchantingYou, thoughts, daft, ., day, laid, eyes, ,, feelings, grew, grew, ., conversation, knees, clicked, clacked, ,, butterflies, flipped, flapped, ., spill, simple, rhymesMy, mind, goes, time, time, ,, crush, ,, little, teenage, crushI, know, ,, lovely, little, crush]
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
[('makes', 2), ('eyes', 2), ('grew', 2), ('time', 2), ('crush', 2)]
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Your:your
makes:make
me:I
smileYour:smileyour
makes:make
me:I
laughYour:laughyour
eyes:eye
are:be
enchantingYou:enchantingyou
thoughts:thought
Since:since
laid:lay
eyes:eye
My:my
feelings:feeling
grew:grow
grew:grow
In:in
knees:knee
clicked:click
clacked:clack
And:and
butterflies:butterfly
flipped:flip
flapped:flap
And:and
rhymesMy:rhymesmy
goes:go
crushI:crushi
n't:not

###############           Part_of_speech Tagging       ###############


        TOKEN:Your
        =====
        TAG: PRP$       POS: PRON
        EXPLANATION: pronoun, possessive

        TOKEN:smile
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:makes
        =====
        TAG: VBZ        POS: VERB
        EXPLANATION: verb, 3rd person singular present

        TOKEN:me
        =====
        TAG: PRP        POS: PRON
        EXPLANATION: pronoun, personal

        TOKEN:smileYour
        =====
        TAG: PRP$       POS: PRON
        EXPLANATION: pronoun, possessive

        TOKEN:laugh
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:makes
        =====
        TAG: VBZ        POS: VERB
        EXPLANATION: verb, 3rd person singular present

        TOKEN:me
        =====
        TAG: PRP        POS: PRON
        EXPLANATION: pronoun, personal

        TOKEN:laughYour
        =====
        TAG: PRP$       POS: PRON
        EXPLANATION: pronoun, possessive

        TOKEN:eyes
        =====
        TAG: NNS        POS: NOUN
        EXPLANATION: noun, plural

        TOKEN:are
        =====
        TAG: VBP        POS: AUX
        EXPLANATION: verb, non-3rd person singular present

        TOKEN:enchantingYou
        =====
        TAG: PRP        POS: PRON
        EXPLANATION: pronoun, personal

        TOKEN:make
        =====
        TAG: VB         POS: VERB
        EXPLANATION: verb, base form

        TOKEN:my
        =====
        TAG: PRP$       POS: PRON
        EXPLANATION: pronoun, possessive

        TOKEN:thoughts
        =====
        TAG: NNS        POS: NOUN
        EXPLANATION: noun, plural

        TOKEN:seem
        =====
        TAG: VB         POS: VERB
        EXPLANATION: verb, base form

        TOKEN:daft
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:.
        =====
        TAG: .          POS: PUNCT
        EXPLANATION: punctuation mark, sentence closer

        TOKEN:Since
        =====
        TAG: IN         POS: SCONJ
        EXPLANATION: conjunction, subordinating or preposition

        TOKEN:the
        =====
        TAG: DT         POS: DET
        EXPLANATION: determiner

        TOKEN:day
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:I
        =====
        TAG: PRP        POS: PRON
        EXPLANATION: pronoun, personal

        TOKEN:first
        =====
        TAG: RB         POS: ADV
        EXPLANATION: adverb

        TOKEN:laid
        =====
        TAG: VBD        POS: VERB
        EXPLANATION: verb, past tense

        TOKEN:eyes
        =====
        TAG: NNS        POS: NOUN
        EXPLANATION: noun, plural

        TOKEN:on
        =====
        TAG: IN         POS: ADP
        EXPLANATION: conjunction, subordinating or preposition

        TOKEN:you
        =====
        TAG: PRP        POS: PRON
        EXPLANATION: pronoun, personal

        TOKEN:,
        =====
        TAG: ,          POS: PUNCT
        EXPLANATION: punctuation mark, comma

        TOKEN:My
        =====
        TAG: PRP$       POS: PRON
        EXPLANATION: pronoun, possessive

        TOKEN:feelings
        =====
        TAG: NNS        POS: NOUN
        EXPLANATION: noun, plural

        TOKEN:grew
        =====
        TAG: VBD        POS: VERB
        EXPLANATION: verb, past tense

        TOKEN:and
        =====
        TAG: CC         POS: CCONJ
        EXPLANATION: conjunction, coordinating

        TOKEN:grew
        =====
        TAG: VBD        POS: VERB
        EXPLANATION: verb, past tense

        TOKEN:.
        =====
        TAG: .          POS: PUNCT
        EXPLANATION: punctuation mark, sentence closer

        TOKEN:In
        =====
        TAG: IN         POS: ADP
        EXPLANATION: conjunction, subordinating or preposition

        TOKEN:that
        =====
        TAG: DT         POS: DET
        EXPLANATION: determiner

        TOKEN:first
        =====
        TAG: JJ         POS: ADJ
        EXPLANATION: adjective (English), other noun-modifier (Chinese)

        TOKEN:conversation
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:my
        =====
        TAG: PRP$       POS: PRON
        EXPLANATION: pronoun, possessive

        TOKEN:knees
        =====
        TAG: NNS        POS: NOUN
        EXPLANATION: noun, plural

        TOKEN:clicked
        =====
        TAG: VBD        POS: VERB
        EXPLANATION: verb, past tense

        TOKEN:and
        =====
        TAG: CC         POS: CCONJ
        EXPLANATION: conjunction, coordinating

        TOKEN:clacked
        =====
        TAG: VBN        POS: VERB
        EXPLANATION: verb, past participle

        TOKEN:,
        =====
        TAG: ,          POS: PUNCT
        EXPLANATION: punctuation mark, comma

        TOKEN:And
        =====
        TAG: CC         POS: CCONJ
        EXPLANATION: conjunction, coordinating

        TOKEN:those
        =====
        TAG: DT         POS: DET
        EXPLANATION: determiner

        TOKEN:butterflies
        =====
        TAG: NNS        POS: NOUN
        EXPLANATION: noun, plural

        TOKEN:flipped
        =====
        TAG: VBD        POS: VERB
        EXPLANATION: verb, past tense

        TOKEN:and
        =====
        TAG: CC         POS: CCONJ
        EXPLANATION: conjunction, coordinating

        TOKEN:flapped
        =====
        TAG: VBD        POS: VERB
        EXPLANATION: verb, past tense

        TOKEN:.
        =====
        TAG: .          POS: PUNCT
        EXPLANATION: punctuation mark, sentence closer

        TOKEN:And
        =====
        TAG: CC         POS: CCONJ
        EXPLANATION: conjunction, coordinating

        TOKEN:as
        =====
        TAG: IN         POS: SCONJ
        EXPLANATION: conjunction, subordinating or preposition

        TOKEN:I
        =====
        TAG: PRP        POS: PRON
        EXPLANATION: pronoun, personal

        TOKEN:spill
        =====
        TAG: VBP        POS: VERB
        EXPLANATION: verb, non-3rd person singular present

        TOKEN:these
        =====
        TAG: DT         POS: DET
        EXPLANATION: determiner

        TOKEN:simple
        =====
        TAG: JJ         POS: ADJ
        EXPLANATION: adjective (English), other noun-modifier (Chinese)

        TOKEN:rhymesMy
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:mind
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:goes
        =====
        TAG: VBZ        POS: VERB
        EXPLANATION: verb, 3rd person singular present

        TOKEN:over
        =====
        TAG: IN         POS: ADP
        EXPLANATION: conjunction, subordinating or preposition

        TOKEN:time
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:and
        =====
        TAG: CC         POS: CCONJ
        EXPLANATION: conjunction, coordinating

        TOKEN:time
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:,
        =====
        TAG: ,          POS: PUNCT
        EXPLANATION: punctuation mark, comma

        TOKEN:I
        =====
        TAG: PRP        POS: PRON
        EXPLANATION: pronoun, personal

        TOKEN:have
        =====
        TAG: VBP        POS: VERB
        EXPLANATION: verb, non-3rd person singular present

        TOKEN:a
        =====
        TAG: DT         POS: DET
        EXPLANATION: determiner

        TOKEN:crush
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:,
        =====
        TAG: ,          POS: PUNCT
        EXPLANATION: punctuation mark, comma

        TOKEN:a
        =====
        TAG: DT         POS: DET
        EXPLANATION: determiner

        TOKEN:little
        =====
        TAG: JJ         POS: ADJ
        EXPLANATION: adjective (English), other noun-modifier (Chinese)

        TOKEN:teenage
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:crushI
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:do
        =====
        TAG: VBP        POS: AUX
        EXPLANATION: verb, non-3rd person singular present

        TOKEN:n't
        =====
        TAG: RB         POS: PART
        EXPLANATION: adverb

        TOKEN:know
        =====
        TAG: VB         POS: VERB
        EXPLANATION: verb, base form

        TOKEN:what
        =====
        TAG: WP         POS: PRON
        EXPLANATION: wh-pronoun, personal

        TOKEN:to
        =====
        TAG: TO         POS: PART
        EXPLANATION: infinitival "to"

        TOKEN:do
        =====
        TAG: VB         POS: VERB
        EXPLANATION: verb, base form

        TOKEN:,
        =====
        TAG: ,          POS: PUNCT
        EXPLANATION: punctuation mark, comma

        TOKEN:about
        =====
        TAG: IN         POS: ADP
        EXPLANATION: conjunction, subordinating or preposition

        TOKEN:this
        =====
        TAG: DT         POS: DET
        EXPLANATION: determiner

        TOKEN:lovely
        =====
        TAG: JJ         POS: ADJ
        EXPLANATION: adjective (English), other noun-modifier (Chinese)

        TOKEN:little
        =====
        TAG: JJ         POS: ADJ
        EXPLANATION: adjective (English), other noun-modifier (Chinese)

        TOKEN:crush
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

    """