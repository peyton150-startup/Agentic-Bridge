# api_tool.py — Day 1B, Patch 5: one read-only tool that reaches an external service.
# Same tool contract as lookup_word, plus: part of the work happens on a machine
# we do not own, over a network that can fail.

import json
import urllib.error
import urllib.request

POSTCODE_URL = "https://api.zippopotam.us/us/{code}"


def is_valid_postcode(code):
    """The check at the door: exactly 5 digits. No request is built if this fails."""
    return isinstance(code, str) and code.isdigit() and len(code) == 5


def lookup_postcode(code, timeout=5):
    """GET one US postal code. Read-only. Returns one result per failure kind."""
    if not is_valid_postcode(code):
        return {"error": "invalid_input", "status": None, "reason": "exactly 5 digits required"}

    try:
        with urllib.request.urlopen(POSTCODE_URL.format(code=code), timeout=timeout) as response:
            status = response.status
            raw = response.read()
    except urllib.error.HTTPError as exc:        # they answered, with a non-success status
        return {"error": "http", "status": exc.code, "reason": "service refused the request"}
    except Exception as exc:                     # timeout, DNS, refused connection: nothing usable came back
        return {"error": "network", "status": None, "reason": type(exc).__name__}

    if status != 200:                            # success is 200 and nothing else
        return {"error": "http", "status": status, "reason": "not a success status"}

    try:
        body = json.loads(raw)
    except ValueError:
        return {"error": "shape", "status": status, "reason": "body was not JSON"}

    places = body.get("places")                  # a 200 does not promise the fields we need
    if not isinstance(places, list) or not places:
        return {"error": "shape", "status": status, "reason": "no places in body"}

    place = places[0]
    if "place name" not in place or "state" not in place:
        return {"error": "shape", "status": status, "reason": "place is missing required fields"}

    # Bounded result: three fields, not the whole body.
    return {"found": True, "code": code, "place": place["place name"], "state": place["state"]}


print("valid   :", lookup_postcode("15213"))
print("bad input:", lookup_postcode("abc"))
print("404     :", lookup_postcode("99999"))
print("timeout :", lookup_postcode("15213", timeout=0.001))
