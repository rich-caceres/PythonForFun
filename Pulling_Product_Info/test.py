import requests


data = requests.get('https://www.wernerco.com/us/products/specialty-products/pump-jacks/PJSeries/PJ-100')

print(data.text)
