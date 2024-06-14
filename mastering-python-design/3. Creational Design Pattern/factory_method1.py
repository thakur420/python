import json
from pathlib import Path
import xml.etree.ElementTree as ET

class JSONDataExtractor:
    def __init__(self,filepath:Path) -> None:
        self.data = {}
        with open(filepath) as f:
            self.data = json.load(f)
    @property
    def parsed_data(self):
        return self.data
    
class XMLDataExtractor:
    def __init__(self,filepath:Path) -> None:
        self.tree = ET.parse(filepath)
    
    @property
    def parsed_data(self):
        return self.tree

def extract_factory(filepath: Path):
    ext = filepath.name.split(".")[-1]
    if ext == "json":
        return JSONDataExtractor(filepath)
    elif ext == "xml":
        return XMLDataExtractor(filepath)
    else:
        raise ValueError("Cannot extract data")

if __name__ == "__main__":
    json_path = Path(__file__).parent / Path("movies.json")
    json_extractor = extract_factory(json_path)
    data = json_extractor.parsed_data
    for movie in data:
        print(f"- {movie['title']}")
        director = movie["director"]
        if director:
            print(f"  Director: {director}")
        genre = movie["genre"]
        if genre:
            print(f"   Genre: {genre}")

    xml_path = Path(__file__).parent / Path("person.xml")
    xml_extractor = extract_factory(xml_path)
    data = xml_extractor.parsed_data
    items = data.findall("person")
    print("\nXML DATA ..........\n")
    for item in items:
        first = item.find("firstName").text
        last = item.find("lastName").text
        age = item.find("age").text
        print(f"- {first} {last}")
        print(f"   Age: {age}")
        for pn in item.find("phoneNumbers"):
                pn_type = pn.attrib["type"]
                pn_val = pn.text
                phone = f"{pn_type}: {pn_val}"
                print(f"  {phone}")