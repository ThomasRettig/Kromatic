# Ensure your pyOpenSSL pip package is up to date
# Example posting a image URL:

import requests
r = requests.post(
    "https://api.deepai.org/api/colorizer",
    data={
        'image': 'https://images.pexels.com/photos/57905/pexels-photo-57905.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
    },
    headers={'api-key': 'cd9c1094-c81b-470a-819b-84c2cc01e9fb'}
)
print(r.json())


