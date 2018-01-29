import requests

PB_URL = 'https://api.pushbullet.com/v2/pushes'


def push_text(access_token, title, body):
    headers = {
        'Content-Type': 'application/json',
        'Access-Token': access_token
    }

    push_data = {
        "title": title,
        "body": body,
        "type": "note"
    }
    requests.post(url=PB_URL, headers=headers, json=push_data)

push_text('o.wb4ohuDmb2mJicXO6byAuYwFnwsC3de5', "bingwen rocks", "lalalalalla")
