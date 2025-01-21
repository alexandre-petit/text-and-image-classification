import pandas as pd
import requests

columns = [
    "foodId",
    "label",
    "category",
    "foodContentsLabel",
    "image"
]

image_folder = "test_folder"

products = requests.get("https://world.openfoodfacts.org/api/v0/products.json?search=chicken")

print(products.status_code)

#df = pd.DataFrame(columns=columns)



#df.to_csv("new_data.csv", index=False)