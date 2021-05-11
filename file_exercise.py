import json

def main():
  try:
    with open("cities.json") as cities_file:
      cities_data = json.load(cities_file)
      print("Largest cities in the us by population:")
      for i, el in enumerate(cities_data):
        print(f"  {i+1}: {el['name']} - {el['pop']}")
  except json.decoder.JSONDecodeError as error:
    print("There was an error decoding that json file:")
    print(f"\t {error}")

if __name__ == "__main__":
  main()
