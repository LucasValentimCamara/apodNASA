import requests
from datetime import date
from IPython.display import Image #colab python

apiKey = 'DEMO_KEY'
data = date.today()

def APOD():
  URL_APOD = "https://api.nasa.gov/planetary/apod"
  params = {
      'api_key':apiKey,
      'date':data,
      'hd':'True'
  }
  response = requests.get(URL_APOD,params=params).json()

  print('Título: ',response['title'])
  print('Copyright: ',response['copyright'])
  print('Data: ',response['date'])
  print('Explicação: ',response['explanation'])
  print('Link: ',response['hdurl'])
  display(Image(response['hdurl'])) 3colab python

APOD()
