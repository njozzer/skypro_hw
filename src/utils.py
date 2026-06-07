import json


def json_read_from_file(filename: str) -> list[dict]:
    if filename is None:
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("Error: The file does not exist.")
        return []
    except json.JSONDecodeError:
        print("Error: The file contains invalid JSON syntax.")
        return []



if __name__ == "__main__":
    print(json_read_from_file("./data/test.json"))
