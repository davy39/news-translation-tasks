---
title: Que signifie API ? Une définition de l'acronyme de programmation en anglais
  simple.
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-11-14T18:03:00.000Z'
originalURL: https://freecodecamp.org/news/what-does-api-stand-for-a-definition-of-the-coding-acronym-in-plain-english
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/api-image.jpeg
tags:
- name: api
  slug: api
seo_title: Que signifie API ? Une définition de l'acronyme de programmation en anglais
  simple.
seo_desc: 'Nope, API doesn''t stand for Apple Pie Inside. API stands for Application
  Programming Interface. APIs allow two applications to interface (or interact) with
  each other.

  An API a set of programming instructions and functions used to access a website
  or...'
---

Non, API ne signifie pas Apple Pie Inside. API signifie Application Programming Interface. Les APIs permettent à deux applications d'interagir (ou d'interagir) entre elles.

Une API est un ensemble d'instructions de programmation et de fonctions utilisées pour accéder à un site web ou à une application logicielle basée sur le web. Une API permet à d'autres développeurs d'utiliser les données et les fonctionnalités de votre application. Elle permet à votre produit d'interagir avec d'autres produits.

Les APIs ont été utilisées pour la première fois dans le développement de logiciels et de matériel dans les années 1980. Mais maintenant, lorsque les gens parlent d'APIs, ils font généralement référence aux APIs web, ou plus spécifiquement aux APIs RESTful. Il est devenu une pratique courante d'utiliser des APIs RESTful lors du développement d'applications basées sur le web.

Une API web est essentiellement un programme avec lequel vous interagissez uniquement via des URLs. Normalement, lorsque vous envoyez une requête à une URL avec votre navigateur, un serveur envoie une réponse qui s'affiche pour que vous la consultiez. Les choses sont différentes lorsque vous envoyez une requête à une URL d'une API. Le serveur envoie quelque chose qui est destiné à être utile uniquement pour un ordinateur. Une API retourne des données qui peuvent être utilisées dans un site web ou un programme différent.

## À quoi servent les APIs ?

Les APIs ne sont pas destinées à être utilisées par un utilisateur final. Elles sont utilisées pour que les logiciels interagissent avec d'autres logiciels. Par exemple, un site web peut faire un appel à l'API Open Weather pour obtenir des informations météorologiques à afficher sur le site web.

Les APIs sont également parfois utilisées en interne au sein d'une seule entreprise. Elles peuvent être utilisées pour créer des sites web et des systèmes internes qui interagissent facilement entre eux.

## **Comment fonctionne une API ?**

Une API donne généralement accès à une grande quantité de données organisées. Le gardien de ces données donne à un développeur la permission (sous la forme d'une _clé API_) de demander des informations à un serveur. Si la requête est réussie, le serveur répond avec un message, généralement au format JSON ou XML.

Habituellement, il y aura une documentation pour une API que vous souhaitez utiliser appelée spécification API. Cela explique les contrôles et comment utiliser l'API.

Voici un exemple de la spécification API pour l'API OpenWeather qui permet d'obtenir la météo actuelle à un emplacement spécifique : [https://openweathermap.org/current](https://openweathermap.org/current)

Les spécifications API contiennent une liste d'URLs que vous pouvez utiliser pour récupérer des données. L'utilisation de l'une des URLs est appelée une _requête API_ ou un _appel API_. Souvent, la spécification montrera les _paramètres_ et la _réponse_ pour chaque URL qui fait partie de l'API.

### Paramètres

Les paramètres sont ce que vous ajoutez à la fin d'une URL pour spécifier quelles informations vous voulez que l'API retourne. Les paramètres sont essentiellement des variables que vous passez à l'API.

L'URL pour obtenir des informations météorologiques de l'API OpenWeather est :
`api.openweathermap.org/data/2.5/weather`.

Cependant, vous devez ajouter une ville en tant que paramètre pour spécifier quel emplacement retourner les données météorologiques. Voici l'URL avec le paramètre de ville :
[`api.openweathermap.org/data/2.5/weather?q=London`](http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22)

Parfois, les paramètres sont requis pour obtenir une réponse. Parfois, les paramètres sont facultatifs. Dans l'API OpenWeather, il est requis de fournir un emplacement, mais il existe d'autres moyens de spécifier l'emplacement en plus du nom de la ville. Toutes les méthodes sont données dans la spécification API.

Les paramètres peuvent également spécifier des choses comme :

* Comment les résultats doivent-ils être triés ?
* Combien de résultats doivent être retournés ?
* Quel format les résultats doivent-ils avoir ?
* Quelle plage de dates voulez-vous pour les résultats ?

### La Réponse

Lorsque vous envoyez une requête à une API, vous recevrez une réponse. Vous recevrez soit les données que vous avez demandées, soit une raison pour laquelle la requête a échoué.

Ci-dessous, un exemple de la réponse que vous obtenez lorsque vous envoyez la requête suivante : [`api.openweathermap.org/data/2.5/weather?q=London`](http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22). Il s'agit d'une réponse JSON.

```javascript
{
    "coord": {
        "lon": -0.13,
        "lat": 51.51
    },
    "weather": [
        {
            "id": 300,
            "main": "Drizzle",
            "description": "light intensity drizzle",
            "icon": "09d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 280.32,
        "pressure": 1012,
        "humidity": 81,
        "temp_min": 279.15,
        "temp_max": 281.15
    },
    "visibility": 10000,
    "wind": {
        "speed": 4.1,
        "deg": 80
    },
    "clouds": {
    	"all": 90
    },
    "dt": 1485789600,
    "sys": {
        "type": 1,
        "id": 5091,
        "message": 0.0103,
        "country": "GB",
        "sunrise": 1485762037,
        "sunset": 1485794875
    },
    "id": 2643743,
    "name": "London",
    "cod": 200
    }
```

Une réponse API peut ne pas être formatée comme cet exemple. Tout le texte est souvent sur une seule ligne. Comme il est principalement destiné à être lu par un ordinateur et non par une personne, le formatage n'a pas d'importance.

### **Clés API**

Si vous essayez l'URL ci-dessus vous-même, vous n'obtiendrez pas la réponse ci-dessus. Cela ressemblera probablement à :

```javascript
{
    "cod": 401,
    "message": "Invalid API key. Please see http://openweathermap.org/faq#error401 for more info."
}
```

La plupart des APIs nécessitent une sorte d'authentification avant de retourner des données. Cela se présente généralement sous la forme d'une _clé API_. Ces clés sont un peu comme un mot de passe. Ce sont une longue chaîne de lettres et de chiffres que vous devez envoyer avec votre requête API afin que le serveur sache que vous êtes autorisé à accéder aux informations.

Pour l'API OpenWeather, et avec de nombreuses autres APIs, vous pouvez obtenir une clé API gratuitement après avoir créé un compte. De nombreuses entreprises utilisent des clés API sur des APIs gratuites pour s'assurer que les gens ne font pas trop de requêtes en une journée. Cela pourrait vraiment ralentir un serveur si une seule personne faisait des milliers de requêtes chaque minute.

Certaines APIs sont publiques sans clé API. Ci-dessous, une API qui vous permet de trouver des mots qui riment. Cliquez sur le lien, puis essayez de changer le dernier mot dans l'URL pour rechercher différents mots qui riment.

[https://api.datamuse.com/words?rel_rhy=camp](https://api.datamuse.com/words?rel_rhy=camp)

## Vous voulez en savoir plus ?

Si vous voulez en savoir plus sur l'utilisation des APIs, consultez la vidéo ci-dessous sur la chaîne YouTube freeCodeCamp.org.

%[https://www.youtube.com/watch?v=BYsTrGH6B2s]