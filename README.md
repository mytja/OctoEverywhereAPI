# OctoEverywhereAPI
Login into OctoEverywhere and use it in your app, instead of NGROK

# We keep the docs of old version [here](https://github.com/mytja/OctoEverywhereAPI/tree/main/legacy/docs.md)

# Usage
## Import
```py
from octoeverywhere import OctoEverywhere

octo = OctoEverywhere("email@example.com", "password")
```

## Get current session cookie:
```py
session = octo.currentCookie
```

## Get new session cookie:
```py
session = octo.getSessionCookie("email@example.com", "password")
```

If we inserted correct login info, we should get something like this:
```py
'dnmdmkjasnmkjkj644kJhjjhhHSIJSAjJKHKJAJSJIUEWUEHXSHWETWQZROO94UZZW'
```

Otherwise, an exception will be thrown:
```
Incorrect login info with status code of 400
```

## Get printer info:
You can get Printer IDs, with `getUserInfo()` function.

```py
printer = octo.getPrinterInfo("<your printer ID>")
```

If we inserted correct login info, we should get something like this:
```py
{'Error': '', 'Status': 200, 'Result': {'Id': '<your printer ID>', 'Name': 'example', 'Owners': ['test@example.com'], 'LastConnectionTime': '2021-03-30T15:33:23.4649623Z', 'LastDisconnectTime': '2021-03-30T15:33:13.9014383Z'}}
```

Otherwise, a following JSON will be thrown:
```py
{'Error': 'No printer found', 'Status': 404, 'Result': None}
```

## Get all printers info
```py
user = octo.getUserInfo()
```

Response (returns a List with JSON):
```py
[{'Error': '', 'Status': 200, 'Result': {'Id': '<your printer ID>', 'Name': 'example', 'Owners': ['test@example.com'], 'LastConnectionTime': '2021-03-30T15:33:23.4649623Z', 'LastDisconnectTime': '2021-03-30T15:33:13.9014383Z'}}]
```

## Get user info
```py
user = octo.getUserInfo("<your session cookie>")
```

Response:
```py
{'Error': '', 'Status': 200, 'Result': {'Email': 'test@example.com', 'PrinterIds': ['PVNZ67HA2GPR514Q2O5X9UB5B8HH3PUT0DAMUQY8'], 'IsMfaEnabled': False, 'HasSeenFirstTimePortalCredsMessage': True}}
```

## Get OctoEverywhere Statistics for their website
```py
user = octo.getStats("<your session cookie>")
```

Response:
```py
{'Error': '', 'Status': 200, 'Result': {'Stats': {'ConnectedPrinters': 5476, 'WebcamMinutesStreamtedInLast24Hours': 3172}}}
```

## Get Messages
```py
user = octo.getMessages("<your session cookie>")
```

Response:
```py
{'Error': '', 'Status': 200, 'Result': {'MessageId': 0, 'HtmlString': None, 'NeedsAck': False, 'OverridePrinterErrors': False}}
```

## Example
Full example is avaiable in `test2.py` file

# [To Do](https://github.com/mytja/OctoEverywhereAPI/projects/1)
