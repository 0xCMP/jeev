import requests


def export(module):
    @module.hear('cat ?fact')
    def cat_fact(message):
        response = requests.get('http://catfacts-api.appspot.com/api/facts?number=1')
        if response.status_code == requests.codes.ok:
            json = response.json()
            if json['success'] == "true":
                message.reply_to_user(json['facts'][0])