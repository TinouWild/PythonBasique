import json
from collections import OrderedDict

product_name = "Kitounette-32-Update"
id_kit = "5e61095cfe011f0634cc1829"
url_publish = "http://upd.sauvegarades.org/v4-custom/"
json_path = "package.json"
with open(json_path, 'r') as f:
    data = json.load(f, object_pairs_hook=OrderedDict)

data['name'] = product_name
data['build']['productName'] = product_name
data['author'] = product_name
data['build']['publish']['url'] = "https://upd.sauvegardes.org/v4-" + id_kit + "-" + product_name + "/stable "

with open('test.json', 'w') as f:
    json.dump(data, f, indent=2)

