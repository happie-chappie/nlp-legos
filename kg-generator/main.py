import spacy
from spacy.pipeline import EntityRuler

nlp = spacy.load("en_core_web_sm")
ruler = EntityRuler(nlp)
patterns = [{"label": "ORGA", "pattern": "Apple"}]
ruler.add_patterns(patterns)
nlp.add_pipe(ruler)

doc = nlp("Apple is a company in the U.S.")

for ent in doc.ents:
    print(ent.text, ent.label_)
