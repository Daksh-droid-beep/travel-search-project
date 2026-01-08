import requests
import json

# 🔥 STABLE OVERPASS SERVER
OVERPASS_URL = "https://overpass.kumi.systems/api/interpreter"


def build_doc(name, city, state, doc_type, description):
    return {
        "name": name,
        "city": city,
        "state": state,
        "country": "India",
        "type": doc_type,
        "description": description,
        "keywords": list(set(name.lower().split()))
    }


def fetch_from_osm(query):
    r = requests.post(OVERPASS_URL, data=query, timeout=300)
    r.raise_for_status()
    return r.json()


def fetch_cities():
    print("Fetching cities (safe)...")

    query = """
    [out:json][timeout:200];
    node["place"="city"](20.0,70.0,30.0,90.0);
    out;
    """

    try:
        data = fetch_from_osm(query)
    except Exception as e:
        print("Cities failed:", e)
        json.dump([], open("cities_ready.json", "w"), indent=2)
        return

    output = []
    for el in data.get("elements", []):
        tags = el.get("tags", {})
        name = tags.get("name")
        if not name:
            continue

        output.append(
            build_doc(
                name=name,
                city=name,
                state=tags.get("addr:state", ""),
                doc_type="city",
                description=f"{name} is a city in India."
            )
        )

    json.dump(output, open("cities_ready.json", "w", encoding="utf-8"), indent=2)
    print("Cities saved:", len(output))


def fetch_monuments():
    print("Fetching monuments (safe)...")

    query = """
    [out:json][timeout:200];
    node["historic"="monument"](20.0,70.0,30.0,90.0);
    out;
    """

    try:
        data = fetch_from_osm(query)
    except Exception as e:
        print("Monuments failed:", e)
        json.dump([], open("monuments_ready.json", "w"), indent=2)
        return

    output = []
    for el in data.get("elements", []):
        tags = el.get("tags", {})
        name = tags.get("name")
        if not name:
            continue

        output.append(
            build_doc(
                name=name,
                city=tags.get("addr:city", ""),
                state=tags.get("addr:state", ""),
                doc_type="monument",
                description=tags.get(
                    "description",
                    f"{name} is a historical monument in India."
                )
            )
        )

    json.dump(output, open("monuments_ready.json", "w", encoding="utf-8"), indent=2)
    print("Monuments saved:", len(output))


if __name__ == "__main__":
    fetch_cities()
    fetch_monuments()
    print("DONE")
