import spacy

nlp = spacy.load('en_core_web_md')

with open ("../demo_data/poodle.txt", "r") as f:
    text = f.read()

doc = nlp(text)

sentence1 = list(doc.sents)[1]

doc1 = nlp("I like salty fries and hamburgers.")
doc2 = nlp("Fast food tastes very good.")
doc3 = nlp("The Empire State Building is in New York")
doc4 = nlp("I enjoy fruits and vegetables.")
doc5 = nlp("I hate fruits and vegetables.")

print (doc4, "<->", doc5, doc4.similarity(doc5))


# import numpy as np
# your_word = "varieties"

# ms = nlp.vocab.vectors.most_similar(
#     np.asarray([nlp.vocab.vectors[nlp.vocab.strings[your_word]]]), n=10)
# words = [nlp.vocab.strings[w] for w in ms[0][0]]
# distances = ms[2]
