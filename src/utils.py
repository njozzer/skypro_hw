import json

def json_read_from_file(filename: str) -> list[dict]:
    if filename is None:
        return []
    
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ ==  "__main__":
    print(json_read_from_file("./data/operations.json"))