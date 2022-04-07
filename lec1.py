import requests
request = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
import pandas as pd
import json
data = pd.DataFrame(json.loads(request.text)["Valute"])
print(data["USD"]["Value"] / data["USD"]["Nominal"])