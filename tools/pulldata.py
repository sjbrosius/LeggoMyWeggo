#!/bin/env python3
import requests
import secrets
import json

headers = {
    'Subscription-Key': secrets.SECRET_SUB_KEY,
    'Content-Type' : "application/json"
}
base = "https://api.wegmans.io/"
outfile = "recipes.json"

def makeQuery(url, headers):
    querystring = {"api-version":"2018-10-18"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()


recipes = makeQuery(base+"meals/recipes/", headers)
recs = []
count = 0
print(len(recipes["recipes"]))
for recipe in recipes["recipes"]:
    count+=1
    print(count, end='\r')
    extension = recipe["_links"][0]["href"].split('?')[0]
    recipeResp = makeQuery(base+extension, headers)
    if len(str(recipeResp)) < 10000:
        recs.append(recipeResp)

print("")

with open(outfile, 'a') as f:
    json.dump(recs, f)
