import spacy

nlp = spacy.load('en_core_web_md')

with open ("../demo_data/poodle.txt", "r") as f:
    text = f.read()

doc = nlp(text)

sentence1 = list(doc.sents)[1]

doc1 = nlp("High level written and verbal communication skills and ability to work with all levels of an organisation")
doc2 = nlp("consultancy: Providing advice and recommendations, based on expertise and experience, to address client needs.")
doc3 = nlp("data engineering: Designing, building, operationalising, securing and monitoring data pipelines and data stores.")
doc4 = nlp("governance: Defining and operating a framework for making decisions, managing stakeholder relationships, and identifying legitimate authority.")
doc5 = nlp("buisness administration: Managing and performing administrative services and tasks to enable individuals, teams and organisations to succeed in their objectives.")

print (doc1, "<->", doc2, doc1.similarity(doc2))
print (doc1, "<->", doc3, doc1.similarity(doc3))
print (doc1, "<->", doc4, doc1.similarity(doc4))
print (doc1, "<->", doc5, doc1.similarity(doc5))


# # import numpy as np
# # your_word = "varieties"

# # ms = nlp.vocab.vectors.most_similar(
# #     np.asarray([nlp.vocab.vectors[nlp.vocab.strings[your_word]]]), n=10)
# # words = [nlp.vocab.strings[w] for w in ms[0][0]]
# # distances = ms[2]
