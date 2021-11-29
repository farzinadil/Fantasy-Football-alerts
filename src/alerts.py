import requests
import os
import json
import time
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

bearer_token = os.getenv("BEARER_TOKEN")

# Twitter filtered stream auth


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r

# Twitter filtered stream rules


def set_rules():
    # You can adjust the rules if needed
    sample_rules = [
        # 44196397 is the twitter id of the Adam Shefter
        # 36089053 is the twitter id of the Tom Pelissero
        {"value": "from:1358539990670536705"}
    ]
    payload = {"add": sample_rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(
                response.status_code, response.text)
        )

# Twitter filtered stream


def get_stream(set):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", auth=bearer_oauth, stream=True,
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            tweet = json_response["data"]
            tweet_content = tweet['text']
            print(tweet_content)
            with open("public/players.json") as players:
                players = json.load(players)
                for player in players["players"]:
                    if player in tweet_content:
                        sms(tweet_content)
                        break


# send sms with twilio client
def sms(message):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    phone_number = os.getenv("PHONE_NUMBER")
    twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
    client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=phone_number
    )


def main():
    set = set_rules()
    while True:
        try:
            get_stream(set)
        except:
            print("something went wrong")
            time.sleep(60)


if __name__ == "__main__":
    main()
