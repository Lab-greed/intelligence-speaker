

import requests
import json


def tuling(text='你好'):
    tuling_url ='http://openapi.tuling123.com/openapi/api/v2'
    dat={
            "reqType":0,
            "perception": {
                "inputText": {
                    "text": text
                },
                "inputImage": {
                    "url": "imageUrl"
                },
                "selfInfo": {
                    "location": {
                        "city": "忻州",
                        "province": "山西",
                        "street": "七一路"
                    }
                }
            },
            "userInfo": {
                "apiKey": "120143f60e9c4136a07634e704ff825c",
                "userId": "JOJO"
            }
        }
    dat = json.dumps(dat)
    r=requests.post(tuling_url,data=dat)
    print(r.text)
