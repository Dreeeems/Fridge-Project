import requests
from deep_translator import GoogleTranslator

def get_image_url(item):

  query = GoogleTranslator(source='auto', target='en').translate(item)
  apiKey = "o46LtQkQP1Nwucqdqdel-jED6rUNX7mHv5eGfpl0w24"
  url = f'https://api.unsplash.com/photos/random?query={query}&client_id={apiKey}'
  response = requests.get(url)
  if response.status_code == 200:
      data = response.json()
      image_url = data['urls']['regular'] 
      return image_url
  else:
    print(f"Error: {response.status_code}")
    return 