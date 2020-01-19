import requests
import json


def get_data(text):
    data={
        "appid":"",
        "userid":"",       
        "spoken":text
        }
    return data


def get_answer(text):
    data=get_data(text)
    url="https://api.ownthink.com/bot"
    response = requests.post(url=url,data=data)
    response.encoding ='utf-8'
    result = response.json()
   # print(result)
    answer=result['data']['info']['text']
    return answer


def speak (text):
    get_data(text)
    return get_answer(text)

    