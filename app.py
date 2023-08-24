import requests
import json
from load import headers, payload
from pprint import pprint


def write_to_file(eventid, data):
    with open(f"Outputs/{eventid}.json", "w") as f:
        json.dump(data, f, indent=4)

def get_request(eventid):
    url = f"https://offeradapter.ticketmaster.com/api/ismds/event/{eventid}/quickpicks?show=places+maxQuantity+sections&mode=primary:ppsectionrow+resale:ga_areas+platinum:all&qty=2&q=not(%27accessible%27)&includeStandard=true&includeResale=true&includePlatinumInventoryType=false&ticketTypes=000000000001%2C299000000007%2C06000002000B%2C06800003000B%2C07000004000B%2C07800005000B&embed=area&embed=offer&embed=description&apikey=b462oi7fic6pehcdkzony5bxhe&apisecret=pquzpfrfz7zd2ylvtz3w5dtyse&resaleChannelId=internal.ecommerce.consumer.desktop.web.browser.ticketmaster.us&limit=40&offset=0&sort=listprice"



    response = requests.request("GET", url, headers=headers, data=payload)


    data = response.json()
    write_to_file(eventid=eventid, data=data)
    return data


if __name__ == "__main__":
    event_ids = open("input.txt", "r").read().splitlines()
    for event_id in event_ids:
        try:
            get_request(eventid=event_id)
        except Exception as e:
            open(f"logs/{event_id}.txt", "w").write(str(e))
    print("Process completed!")




