---
title: Comment obtenir les informations de localisation d'une adresse IP en utilisant
  Python
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2022-03-03T17:55:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-location-information-of-ip-address-using-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/location-ip.png
tags:
- name: api
  slug: api
- name: Python
  slug: python
seo_title: Comment obtenir les informations de localisation d'une adresse IP en utilisant
  Python
seo_desc: 'Sometimes you''ll need to know the location of an IP address, whether it''s
  your own or that of a site you''re using.

  One use-case for this is when you want to send login information to users for your
  website.

  In this article, we''re going to see how you...'
---

Parfois, vous aurez besoin de connaître la localisation d'une adresse IP, qu'il s'agisse de la vôtre ou de celle d'un site que vous utilisez.

Un cas d'utilisation pour cela est lorsque vous souhaitez envoyer des informations de connexion aux utilisateurs de votre site web.

Dans cet article, nous allons voir comment trouver la localisation d'une adresse IP en utilisant Python.

# **Préparez vos outils**

Pour accomplir cet objectif, nous allons utiliser deux APIs mentionnées ci-dessous :

1. [**ipify**](https://www.ipify.org/) : Cette API nous aidera à connaître l'adresse IP d'où provient la requête.

2. [**ipapi**](https://ipapi.co/) : Cette API nous aidera à récupérer les informations de localisation pour une adresse IP particulière.

Pour interagir avec ces APIs, nous allons utiliser la bibliothèque `**requests**` en Python. Si vous êtes nouveau dans le domaine des APIs, assurez-vous de consulter [ce tutoriel](https://ireadblog.com/posts/77/python-api-tutorial-how-to-interact-with-web-services) pour en apprendre davantage.

Vous pouvez installer cette bibliothèque en utilisant la commande `pip` comme ceci :

```bash
$ pip install requests
```

Une fois la bibliothèque installée, nous sommes prêts à commencer !

# **Obtenir les informations de localisation**

Comme nous l'avons discuté, nous allons d'abord récupérer notre adresse IP à partir de la première API. Ensuite, nous utiliserons cette adresse IP pour récupérer les informations de localisation pour cette adresse IP particulière. Nous aurons donc deux fonctions :

```py
import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data


print(get_location())
```

Dans le code ci-dessus, nous avons deux fonctions – `**get_ip()**` et `**get_location()**`. Discutons de chacune d'elles séparément.

### Fonction `get_ip()`

Selon la [documentation de l'API](https://www.ipify.org/) d'ipify, nous devons faire une requête **GET** sur [`https://api.ipify.org?format=json`](https://api.ipify.org/?format=json) pour obtenir une réponse JSON qui ressemble à ceci :

```json
{
  "ip": "117.214.109.137"
}
```

Nous stockons cette réponse dans une variable `response` qui n'est rien d'autre qu'une sorte de [dictionnaire Python](https://ireadblog.com/posts/84/everything-you-need-to-know-about-python-dictionaries) avec une paire clé-valeur. Nous avons donc retourné la valeur de la clé `**ip**` comme `**response["ip"]**`.

### Fonction `get_location()`

Selon la [documentation de l'API](https://ipapi.co/api/#introduction) d'ipapi, nous devons faire une requête **GET** sur [`https://ipapi.co/{ip}/{format}/`](https://ipapi.co/%7Bip%7D/%7Bformat%7D/) pour obtenir les informations de localisation pour une adresse IP particulière. `{ip}` est remplacé par l'adresse IP et `{format}` peut être remplacé par l'un de ces formats – `json`, `jsonp`, `xml`, `csv`, `yaml`.

Cette fonction appelle interne la fonction `**get_ip()**` pour obtenir l'adresse IP, puis fait une requête **GET** sur l'URL avec l'adresse IP. Cette API retourne une réponse JSON qui ressemble à ceci :

```json
{
    "ip": "117.214.109.137",
    "version": "IPv4",
    "city": "Gaya",
    "region": "Bihar",
    "region_code": "BR",
    "country": "IN",
    "country_name": "India",
    "country_code": "IN",
    "country_code_iso3": "IND",
    "country_capital": "New Delhi",
    "country_tld": ".in",
    "continent_code": "AS",
    "in_eu": false,
    "postal": "823002",
    "latitude": 24.7935,
    "longitude": 85.012,
    "timezone": "Asia/Kolkata",
    "utc_offset": "+0530",
    "country_calling_code": "+91",
    "currency": "INR",
    "currency_name": "Rupee",
    "languages": "en-IN,hi,bn,te,mr,ta,ur,gu,kn,ml,or,pa,as,bh,sat,ks,ne,sd,kok,doi,mni,sit,sa,fr,lus,inc",
    "country_area": 3287590,
    "country_population": 1352617328,
    "asn": "AS9829",
    "org": "National Internet Backbone"
}
```

Nous obtenons une multitude de données dans la réponse. Vous pouvez utiliser ce qui vous convient. Pour ce tutoriel, nous allons simplement utiliser `**city**`, `**region**` et `country`. C'est pourquoi nous avons créé un dictionnaire appelé `location_data` et stocké toutes les données à l'intérieur, puis retourné le même.

Enfin, nous appelons la fonction `**get_location()**` et affichons le résultat. Notre sortie ressemblera à ceci :

```json
{
  "ip": "117.214.109.137", 
  "city": "Gaya", 
  "region": "Bihar", 
  "country": "India"
}
```

# **Conclusion**

Dans cet article, nous avons appris comment interagir avec des services web pour obtenir des informations de localisation pour une adresse IP particulière.

Merci d'avoir lu ! Pour plus d'articles comme celui-ci, consultez mon blog, [iRead](https://ireadblog.com).