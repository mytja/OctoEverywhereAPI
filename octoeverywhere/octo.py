import requests
import json

def getSessionCookie(email, password):
    url = 'https://octoeverywhere.com/api/user/login'

    values = {'Email': email, 'Password': password}

    headers = {
        "Content-Type": "application/json"
    }

    session = requests.Session()

    r = session.post(url, data=json.dumps(values), headers=headers)

    if r.status_code == 200:
        return session.cookies.get_dict()
    else:
        raise Exception("Incorrect login info with status code of " + str(r.status_code))


def getUserInfo(cookie):
    cookies = {
        "OctoEverywhereSessionKey": cookie
    }

    url = "https://octoeverywhere.com/api/user/info"

    r = requests.post(url, cookies=cookies)

    return r.json()

def getAllPrinterInfo(cookie):
    user = getUserInfo(cookie)

    cookies = {
        "OctoEverywhereSessionKey": cookie
    }

    url = "https://octoeverywhere.com/api/printer/info"

    printer = []

    for i in user["Result"]["PrinterIds"]:
        data = {
            "Id": str(i)
        }
        r = requests.post(url, cookies=cookies, data=json.dumps(data))
        printer.append(r.json())
    
    return printer

def getPrinterInfo(cookie, printer_id):
    cookies = {
        "OctoEverywhereSessionKey": cookie
    }

    url = "https://octoeverywhere.com/api/printer/info"

    data = {
        "Id": printer_id
    }
    r = requests.post(url, cookies=cookies, data=json.dumps(data))
    return r.json()

def getStats(cookie):
    cookies = {
        "OctoEverywhereSessionKey": cookie
    }

    url = "https://octoeverywhere.com/api/stats/stats"

    r = requests.get(url, cookies=cookies)
    return r.json()

def getMessages(cookie):
    cookies = {
        "OctoEverywhereSessionKey": cookie
    }

    url = "https://octoeverywhere.com/api/user/getmessage"

    r = requests.post(url, cookies=cookies)
    return r.json()

def popupSeen(cookie):
    cookies = {
        "OctoEverywhereSessionKey": cookie
    }

    url = "https://octoeverywhere.com/api/user/reportmessageseen"

    data = {
        "Message": "HasShownFirstTimePortalCredsMessage"
    }
    r = requests.post(url, cookies=cookies, data=json.dumps(data))
    return r.json()
