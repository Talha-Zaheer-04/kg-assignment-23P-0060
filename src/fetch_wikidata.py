import requests
import csv
import os
import time

# Wikidata requires a User-Agent to allow your script to connect
HEADERS = {"User-Agent": "KRR-coursework/1.0 (p230060@pwr.nu.edu.pk)"}

scientists = {
    "Q937": "Albert Einstein",
    "Q7186": "Marie Curie",
    "Q1456": "Pieter Zeeman",
    "Q9299": "Erwin Schrödinger",
    "Q3518": "Albert A. Michelson"
}

properties = {
    "P19": "bornIn",
    "P69": "educatedAt",
    "P166": "receivedAward",
    "P108": "worksAt",
    "P184": "doctoralAdvisor"
}

def fetch_wikidata():
    rows = []
    
    for qid, name in scientists.items():
        print(f"Fetching data for {name}...")
        url = f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json"
        
        # Retry up to 3 times if the network fails
        success = False
        for attempt in range(3):
            try:
                r = requests.get(url, headers=HEADERS, timeout=15)
                if r.status_code == 200:
                    success = True
                    break
                else:
                    print(f"  [Warning] Got status {r.status_code}. Retrying in 3s...")
                    time.sleep(3)
            except Exception as e:
                print(f"  [Error] {e}. Retrying in 3s...")
                time.sleep(3)
                
        if not success:
            print(f"  [FAILED] Could not fetch {name} after 3 tries.")
            continue
            
        data = r.json()
        entity = data['entities'][qid]
        claims = entity.get('claims', {})
        
        for prop_code, pred_name in properties.items():
            if prop_code in claims:
                for claim in claims[prop_code]:
                    mainsnak = claim.get('mainsnak', {})
                    datavalue = mainsnak.get('datavalue', {})
                    
                    if datavalue.get('type') == 'wikibase-entityid':
                        obj_id = datavalue['value']['id']
                        rows.append({"subject": name, "predicate": pred_name, "object": obj_id})
        
        # Wait 2 seconds between different scientists
        time.sleep(2)
    
    os.makedirs("eval", exist_ok=True)
    with open("eval/wikidata_export.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["subject", "predicate", "object"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nSaved eval/wikidata_export.csv with {len(rows)} facts!")

if __name__ == "__main__":
    fetch_wikidata()