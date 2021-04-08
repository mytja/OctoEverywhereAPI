import requests
import json

from .legacy import *

class OctoEverywhere:
    currentCookie = ""
    email = ""
    password = ""

    def __init__(self, email, password):
        session = getSessionCookie(email, password)
        self.email = email
        self.password = password
        self.currentCookie = session

    def getSessionCookie(self, email, password):
        self.currentCookie = getSessionCookie(email, password)["OctoEverywhereSessionKey"]
        return self.currentCookie

    def isCookieValid(self):
        ok = getUserInfo(self.currentCookie)
        if ok["Status"] != 200:
            self.currentCookie = getSessionCookie(self.email, self.password)
            return False
        else:
            return True

    def getUserInfo(self):
        return getUserInfo(self.currentCookie)

    def getAllPrinterInfo(self):
        return getAllPrinterInfo(self.currentCookie)

    def getPrinterInfo(self, printer_id):
        return getPrinterInfo(self.currentCookie, printer_id)

    def getStats(self):
        return getStats(self.currentCookie)

    def getMessages(self):
        return getMessages(self.currentCookie)

    def popupSeen(self):
        return popupSeen(self.currentCookie)
