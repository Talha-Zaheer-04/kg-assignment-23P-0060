import requests, pathlib

HEADERS = {"User-Agent": "KRR-coursework/1.0 (p230060@pwr.nu.edu.pk)"}

def fetch(title):
    r = requests.get(
    "https://en.wikipedia.org/w/api.php",
    params={"action": "query", "prop": "extracts", "explaintext": 1,
    "redirects": 1, "titles": title, "format": "json"},
    headers=HEADERS, timeout=30)
    page = next(iter(r.json()["query"]["pages"].values()))
    return page["extract"]

articles = ['Marie Curie', 'Albert A. Michelson', 'Albert Einstein', 'Pieter Zeeman', 'Erwin Schrödinger']

for article in articles:
    pathlib.Path("data/raw").mkdir(parents=True, exist_ok=True)
    text = fetch(f"{article}")
    pathlib.Path(f"data/raw/{article}.txt").write_text(text, encoding="utf-8")