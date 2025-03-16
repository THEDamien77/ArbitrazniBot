import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1350910551852580884/A63OR7c24B2Tr4pio5jIJsK5Wm1fKiGTod2Tw6qA4ZbTEQUycaR2K0IfiKUn6h6xVNWo"  

def posli_notifikaci(zprava):
    data = {"content": zprava}
    requests.post(WEBHOOK_URL, json=data)

# Testovací zpráva
posli_notifikaci("🔔 Nová arbitrážní příležitost byla přidána do seznamu!")
