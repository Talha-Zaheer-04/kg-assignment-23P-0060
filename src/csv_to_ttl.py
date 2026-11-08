import csv
import rdflib
from rdflib.namespace import RDF
from urllib.parse import quote

# Create a new graph
g = rdflib.Graph()

# Define our namespaces
EX = rdflib.Namespace("http://example.org/kg#")
g.bind("ex", EX)

# Read your CSV
with open("out/triples.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # 1. Clean the subject and object names (no spaces, safe for URIs)
        subj_uri = EX[quote(row['subject'].replace(" ", "_"))]
        obj_uri = EX[quote(row['object'].replace(" ", "_"))]
        pred = EX[row['predicate']]
        
        # 2. Add the triple to the graph
        g.add((subj_uri, pred, obj_uri))
        
        # 3. Add the type (Person) to the subject so our queries work
        g.add((subj_uri, RDF.type, EX.Person))
        
        # 4. Add the type of the object based on the predicate
        if row['predicate'] == 'bornIn':
            g.add((obj_uri, RDF.type, EX.Place))
        elif row['predicate'] in ['educatedAt', 'worksAt']:
            g.add((obj_uri, RDF.type, EX.Organization))
        elif row['predicate'] == 'receivedAward':
            g.add((obj_uri, RDF.type, EX.Award))
        elif row['predicate'] == 'doctoralAdvisor':
            g.add((obj_uri, RDF.type, EX.Person))

# Save the graph to a file
g.serialize(destination="out/kg.ttl", format="turtle")
print("Saved out/kg.ttl successfully!")