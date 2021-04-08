from octoeverywhere import OctoEverywhere

octo = OctoEverywhere("example@example.com", "password")

login = octo.getSessionCookie("example@example.com", "password")
print(login)

user = octo.getUserInfo()
print(user)

printer = octo.getPrinterInfo("your printer key")
print(printer)

allprinter = octo.getAllPrinterInfo()
print(allprinter)

stats = octo.getStats()
print(stats)

messages = octo.getMessages()
print(messages)

popup = octo.popupSeen()
print(popup)

valid = octo.isCookieValid()
print(valid)