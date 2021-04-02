# OctoEverywhereAPI
Login into OctoEverywhere and use it in your app, instead of NGROK

# Usage
## Get session cookie:
```py
from octoeverywhere import *

session = getSessionCookie("email@example.com", "password")
```

If we inserted correct login info, we should get something like this:
```json
{'OctoEverywhereSessionKey': 'dnmdmkjasnmkjkj644kJhjjhhHSIJSAjJKHKJAJSJIUEWUEHXSHWETWQZROO94UZZW'}
```

Otherwise, an exception will be thrown:
```
Incorrect login info with status code of 400
```

## Get printer info:
You can get Printer IDs, with `getUserInfo()` function.

```py
from octoeverywhere import *

printer = getPrinterInfo("<your session cookie>", "<your printer ID>")
```

If we inserted correct login info, we should get something like this:
```json
{'Error': '', 'Status': 200, 'Result': {'Id': '<your printer ID>', 'Name': 'example', 'Owners': ['test@example.com'], 'LastConnectionTime': '2021-03-30T15:33:23.4649623Z', 'LastDisconnectTime': '2021-03-30T15:33:13.9014383Z'}}
```

Otherwise, a following JSON will be thrown:
```json
{'Error': 'No printer found', 'Status': 404, 'Result': None}
```

## Get all printers info
```py
from octoeverywhere import *

user = getUserInfo("<your session cookie>")
```

Response (returns a List with JSON):
```json
[{'Error': '', 'Status': 200, 'Result': {'Id': '<your printer ID>', 'Name': 'example', 'Owners': ['test@example.com'], 'LastConnectionTime': '2021-03-30T15:33:23.4649623Z', 'LastDisconnectTime': '2021-03-30T15:33:13.9014383Z'}}]
```

## Get user info
```py
from octoeverywhere import *

user = getUserInfo("<your session cookie>")
```

Response:
```json
{'Error': '', 'Status': 200, 'Result': {'Email': 'test@example.com', 'PrinterIds': ['PVNZ67HA2GPR514Q2O5X9UB5B8HH3PUT0DAMUQY8'], 'IsMfaEnabled': False, 'HasSeenFirstTimePortalCredsMessage': True}}
```

## Get OctoEverywhere Statistics for their website
```py
from octoeverywhere import *

user = getStats("<your session cookie>")
```

Response:
```json
{'Error': '', 'Status': 200, 'Result': {'Stats': {'ConnectedPrinters': 5476, 'WebcamMinutesStreamtedInLast24Hours': 3172}}}
```

## Get Messages
```py
from octoeverywhere import *

user = getMessages("<your session cookie>")
```

Response:
```json
{'Error': '', 'Status': 200, 'Result': {'MessageId': 0, 'HtmlString': None, 'NeedsAck': False, 'OverridePrinterErrors': False}}
```

## Example
Full example is avaiable in `test.py` file
