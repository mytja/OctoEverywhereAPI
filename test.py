from octoeverywhere import *

login = getSessionCookie("example@example.com", "password")
print(login["OctoEverywhereSessionKey"])

user = getUserInfo(login["OctoEverywhereSessionKey"])
print(user)

printer = getPrinterInfo(login["OctoEverywhereSessionKey"], "your printer key")
print(printer)

allprinter = getAllPrinterInfo(login["OctoEverywhereSessionKey"])
print(allprinter)

stats = getStats(login["OctoEverywhereSessionKey"])
print(stats)

messages = getMessages(login["OctoEverywhereSessionKey"])
print(messages)

popup = popupSeen(login["OctoEverywhereSessionKey"])
print(popup)