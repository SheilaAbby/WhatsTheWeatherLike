import requests
import secrets

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city = input('Enter your City: ')
requests_url = f'{BASE_URL}?appid={secrets.API_KEY}&q={city}'
response = requests.get(requests_url)

# check the api endpoint status

if response.status_code == 200:
    data = response.json()
    # incase you need to save the data somewhere
    # with open('data.json', 'w') as data_file:
    #     json.dump(data, data_file)
    weather_condition = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)
    print(f'Weather : ',weather_condition)
    print(f'Temp is: ', f'{temperature} Degrees Celcius')
else:
    print(f'{response.status_code} Error occurred')
