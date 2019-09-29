import json

import requests

import funcutils


TON_TO_KG_RATE = 1000
PREMIUM_MIN_PRICE = 5
PREMIUM_SUFIX = " (Premium)"
BESTPOTATO_URL = "https://raw.githubusercontent.com/jurekkow/functional-potatoes/master/bestpotato.json"


def drop_unneeded_fields(potato):
    return {"kind": potato["kind"], "price": potato["price"]}


def extract_kind_name(potato):
    potato_kind = json.loads(potato["kind"])
    try:
        kind_name = potato_kind["name"]
    except KeyError:
        kind_name = potato_kind["info"]["name"]
    return {**potato, "kind": kind_name}


def convert_to_price_per_kg(potato):
    price_per_kg = potato["price"] / TON_TO_KG_RATE
    return {**potato, "price": price_per_kg}


def format_kind_name(potato):
    formatted_kind = potato["kind"].title()
    if potato["price"] < PREMIUM_MIN_PRICE:
        return {**potato, "kind": formatted_kind}
    return {**potato, "kind": formatted_kind + PREMIUM_SUFIX}


def map_field_name(potato):
    return {"name": potato["kind"], "priceKg": potato["price"]}


def parse_potato(potato):
    parsers = [
        drop_unneeded_fields,
        extract_kind_name,
        convert_to_price_per_kg,
        format_kind_name,
        map_field_name,
    ]
    return funcutils.pipe(parsers, potato)


def get_bestpotato_potatoes():
    response = requests.get(BESTPOTATO_URL)
    return response.json()["potatoes"]


def get_parsed_potatoes():
    bestpotato_potatoes = get_bestpotato_potatoes()
    return [parse_potato(potato) for potato in bestpotato_potatoes]
