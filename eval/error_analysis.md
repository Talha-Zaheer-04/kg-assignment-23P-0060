# Error Analysis

## Top 5 False Positives (Sorted Alphabetically by Subject, Predicate, Object)
1. **Albert A. Michelson, worksAt, Newcomb (E4: Direction or Role)**
   *Why it happened:* The sentence was "joining Newcomb in Washington DC". Newcomb is a person, not a place. The code grabbed the wrong object because it only looked for the word "joining".
   *How to fix it:* Add a rule to check if the object is a known Person entity (using spaCy NER), and if so, do not extract it as a workplace.

2. **Albert Einstein, worksAt, Italy (E4: Direction or Role)**
   *Why it happened:* The sentence was "The Einstein family moved to Italy". The code thought Einstein moved there for work, not his family.
   *How to fix it:* Add a rule to skip sentences that start with "The [Name] family" or contain "family moved".

3. **Albert Einstein, worksAt, US (E4: Direction or Role)**
   *Why it happened:* The sentence was "After moving to the US, Einstein described...". It caught the prepositional phrase instead of a real workplace.
   *How to fix it:* Ensure the verb is an active workplace verb (like "works at"), not just "moving".

4. **Marie Curie, educatedAt, Paris Marie (E1: Wrong Span)**
   *Why it happened:* The extractor used a regex that grabbed the word "Marie" immediately after "Paris" because it didn't know where the place name ended.
   *How to fix it:* Update the regex to stop at punctuation or prepositions, or use the dependency parse to grab the noun phrase exactly.

5. **Marie Curie, worksAt, LibriVox domain (E7: Other)**
   *Why it happened:* The extractor read the "External links" section at the bottom of the Wikipedia page, which contains links like "Works by Marie Curie at LibriVox".
   *How to fix it:* Skip all text after the "== External links ==" heading.

## Top 5 False Negatives
1. **Albert Einstein, receivedAward, Nobel Prize (E2: Pronoun)**
   *Why it happened:* The sentence was "he received the Nobel Prize". The pronoun "he" was not correctly linked to Einstein because the NER got confused by co-authors like Paul Dirac.
   *How to fix it:* Improve the coreference resolution (linking pronouns to the main subject of the document).

2. **Erwin Schrödinger, bornIn, Vienna (E6: Source Gap)**
   *Why it happened:* The Wikipedia text did not explicitly say "born in Vienna" in a simple sentence. The extractor missed the passive voice construction.
   *How to fix it:* Use a more complex NLP parser to understand phrases like "Vienna was the birthplace of...".

3. **Marie Curie, educatedAt, University of Paris (E1: Wrong Span)**
   *Why it happened:* The extractor got "University of Paris Marie" instead of "University of Paris", so it didn't match Wikidata.
   *How to fix it:* Same as above; fix the regex or dependency extraction to stop at the correct noun phrase.

4. **Albert Einstein, worksAt, University of Zurich (E6: Source Gap)**
   *Why it happened:* The text said "He was a professor at Zurich", which didn't match our exact "works at" or "joined" keywords.
   *How to fix it:* Add "professor at" and "lecturer at" to the worksAt rules.

5. **Pieter Zeeman, doctoralAdvisor, Heike Kamerlingh Onnes (E6: Source Gap)**
   *Why it happened:* The word "advisor" was not used. The text likely said "studied under" or "supervised by".
   *How to fix it:* Expand the doctoralAdvisor regex to include "studied under" or "supervised by".