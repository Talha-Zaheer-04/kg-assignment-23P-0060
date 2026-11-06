# Predictions

## 1. Expected Number of Triples

I expect the five Wikipedia articles to generate approximately 100–150 triples, depending on how many entities, relationships, and facts the extraction process identifies.

The private document may contribute another 10–15 triples.

The total expected output is therefore approximately 110–165 triples.

## 2. Expected Lowest Precision

I expect the lowest precision to occur in relationships involving education and academic affiliations.

This is because different expressions can describe similar relationships, such as:
- Studied at an institution.
- Graduated from an institution.
- Worked at an institution.
- Received an award from an institution.
The extraction system might incorrectly classify these relationships or associate an entity with the wrong institution.

## 3. Expected Private Document Difficulty

I expect the private document to be more challenging than the Wikipedia articles because it contains several extraction challenges:
1. Aliases: Yasir Siddiqui is also referred to as Dr. Siddiqui.
2. Coreference: The pronouns "he" and "she" refer to previously mentioned people.
3. Multiple relationships: Yasir studied at two institutions, received an award, and worked at another institution.
4. Negative information: The document explicitly states that he never studied at Alderwick University.
5. Indirect relationships: Bushra Awan is Yasir's doctoral advisor, and she later moved to another institution.
The system must correctly identify entities and relationships while avoiding incorrect triples from negative statements and resolving references accurately.
