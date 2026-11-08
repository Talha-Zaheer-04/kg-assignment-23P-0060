# Knowledge Graph Assignment

## Fuseki Configuration

- Dataset Name: kg-23p-0060
- Dataset Type: Persistent (TDB2)
- Namespace: http://example.org/kg/23p-0060/

## Description

This project extracts a small knowledge graph from five Wikipedia articles and one private document. The pipeline reads the raw text, uses a Python script with spaCy and Regular Expressions to extract triples (subject, predicate, object), and saves them to a CSV file. The triples are then converted to RDF (Turtle) format, loaded into an Apache Jena Fuseki database, and queried using SPARQL. Finally, the extracted data is evaluated against Wikidata to calculate precision and recall.

## How to Run It

1. Install dependencies:
   `pip install spacy rdflib pyshacl requests`
   `python -m spacy download en_core_web_sm`
2. Fetch the Wikipedia articles:
   `python src/fetch_wikipedia.py`
3. Extract the triples:
   `python src/extract.py`
4. Convert the triples to RDF:
   `python src/csv_to_ttl.py`
5. Start Fuseki, create a persistent dataset, and upload `out/kg.ttl`.
6. Run the SPARQL queries from the `queries/` folder.

## Extractor Rules

Here is a brief explanation of how the extractor works:

* **Pronouns (He/She):** Before extraction, the text is split into sentences. A regex replaces "He" or "She" with the last known PERSON entity (using spaCy's Named Entity Recognition) found in the document. The filename is also used as an anchor to prevent co-authors from hijacking the subject.
* **Negation:** Any sentence containing the word "not" or "never" is completely skipped to ensure false facts are not extracted.
* **bornIn:** Uses a regular expression to find the word "born in" and grabs the subsequent location. If the location is a year (e.g., 1960), it is filtered out.
* **educatedAt:** Uses spaCy's dependency parse. It looks for the verb "study" (lemma) and finds the prepositional object attached to the preposition "at" or "in".
* **worksAt:** Uses spaCy's dependency parse. It looks for the verbs "join", "work", or "move" and extracts the direct object or prepositional object (at, to, for), provided the object starts with a capital letter (Proper Noun).
* **receivedAward:** Uses a regular expression to find the phrase "received the [Award Name]".
* **doctoralAdvisor:** Uses a regular expression to find the pattern "[Name]'s doctoral advisor was [Name]".
* **Same Entity Merging:** The extractor identifies the main person from the filename (e.g., "Yasir Siddiqui"). If it finds a partial name like "Dr. Siddiqui" or just "Siddiqui" in the text, it merges it with the full name.
  * **Merge Count:** The extractor successfully merged **2** aliases (e.g., "Dr. Siddiqui" -> "Yasir Siddiqui").

## Folder Structure
* `src/`: Contains the Python scripts (`fetch_wikipedia.py`, `extract.py`, `csv_to_ttl.py`).
* `data/raw/`: Contains the 6 downloaded text files.
* `out/`: Contains `triples.csv` and `kg.ttl`.
* `queries/`: Contains the 6 SPARQL query files (`q1.rq` to `q6.rq`).
* `results/`: Contains the CSV outputs from running the queries.
* `eval/`: Contains the evaluation metrics, Wikidata export, and error analysis.
* `screenshots/`: Contains the screenshots of Fuseki.
* `ontology.ttl`, `shapes.ttl`: The OWL ontology and SHACL validation shapes.
* `step3_note.md`: The note on OWL vs SHACL.
* `predictions.md`, `reflection.md`: The Step 6 files.