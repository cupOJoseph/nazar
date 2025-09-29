#loop through all the jsons in the jsons folder and add the ipfs hash to the json

import os
import json

ipfs_link = "ipfs://bafybeicf6cxs2dyyywd6ntcjfap7nhe5qvs5yswti5lcqlqwtfcuw7y364/"

# get all the jsons in the jsons folder
jsons = [f for f in os.listdir("jsons") if f.endswith(".json")]

i = 0 # count the number of jsons processed

# loop through all the jsons and add the ipfs hash to the json
for json_file in jsons:
    if i % 100 == 0:
        print(f"Processing json {i+1} of {len(jsons)}")
    i += 1
    with open(f"jsons/{json_file}", "r") as f:
        json_data = json.load(f)
    link = ipfs_link + json_data["name"].replace(" ", "").replace("M", "m") + ".png" 
    #remove spaces from name

    json_data["image"] = link
    with open(f"jsons/{json_file}", "w") as f:
        json.dump(json_data, f)

print("IPFS hashes added to all jsons")