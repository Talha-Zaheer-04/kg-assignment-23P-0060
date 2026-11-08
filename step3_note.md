SHACL Report Analysis:
I tested my shape against a test graph where a person had two birthplaces. SHACL correctly flagged this as a violation, proving that the sh:maxCount 1 constraint works. In a real scenario, if this violation appears in my actual data, it means my extractor made a mistake (e.g., extracting both a city and a country as birthplaces) and the data needs cleaning.

OWL Reasoner vs SHACL:

    What OWL can do that SHACL cannot: An OWL reasoner can infer new facts based on logic. For example, since I defined bornIn as a FunctionalProperty, if a person is listed as born in Sukkur, the reasoner automatically infers that any other birthplace listed for them must be the same place (they are equivalent). SHACL cannot infer; it only validates.

    What SHACL can do that OWL cannot: SHACL can validate "closed" rules and data types. For example, SHACL can enforce that a person's name must be a string (text) and not a number, or that a person has at most one birthplace and throw an error if they have two. An OWL reasoner will just accept the data and try to make logical sense of it, rather than throwing an error.