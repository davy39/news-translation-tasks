---
title: Comment mettre en cache des requêtes de base de données coûteuses à l'aide
  du cache serverless Momento
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-22T20:45:05.000Z'
originalURL: https://freecodecamp.org/news/serverless-caching-for-your-web-applications
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/pexels-tiger-lily-4483610.jpg
tags:
- name: caching
  slug: caching
- name: database
  slug: database
- name: serverless
  slug: serverless
seo_title: Comment mettre en cache des requêtes de base de données coûteuses à l'aide
  du cache serverless Momento
seo_desc: 'By Andrew Brown

  When to Use a Cache

  When you are building a web-application, you''ll need to fetch data from a database.
  As your traffic and the size of your database grows, you will find that querying
  your database gets slower and slower.

  In order to...'
---

Par Andrew Brown

## Quand utiliser un cache

Lorsque vous construisez une application web, vous devrez récupérer des données depuis une base de données. À mesure que votre trafic et la taille de votre base de données augmentent, vous constaterez que les requêtes vers votre base de données deviennent de plus en plus lentes.

Afin de retourner rapidement les requêtes aux utilisateurs, un cache peut être une solution économique et facile plutôt que de devoir mettre à niveau votre base de données.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Screen-Shot-2022-12-22-at-10.37.53-AM.png)
_Diagramme montrant comment fonctionne un cache_

Un cache est une base de données en mémoire qui peut stocker des données simples sous forme de structure de données clé-valeur.

Des solutions de cache open-source populaires qui existent déjà sont Memcache et Redis.

## Qu'est-ce que Momento ?

Momento Serverless Cache est un Caching-as-a-Service (CaaS) que vous pouvez intégrer comme solution de cache. Il réduira les requêtes coûteuses ou inutiles contre votre base de données principale.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Screen-Shot-2022-12-22-at-12.54.33-PM.png)

Momento dispose d'un SDK pour les huit langages de programmation les plus populaires. Voici un exemple d'utilisation du SDK Ruby pour faire un simple get et set d'un élément de cache :

```ruby
require 'momento'

client = Momento::SimpleCacheClient.new(
  auth_token: ENV['MOMENTO_AUTH_TOKEN'],
  default_ttl: ENV['MOMENTO_TTL']
)

response = client.set ENV['MOMENTO_CACHE_NAME'], "Hello", "World"
response = client.get ENV['MOMENTO_CACHE_NAME'], key
if response.hit?
  puts "Cache returned: #{response.value_string}"
elsif response.miss?
  puts "The item wasn't found in the cache."
end

```

Juste une petite note : l'entreprise s'appelle Momento et le produit de cache s'appelle Momento Serverless Cache, mais nous dirons simplement "Momento" pour désigner le produit afin de garder cela simple.

## Pourquoi utiliser Momento ?

Momento est un cache serverless, et par conséquent présente les avantages suivants :

* La création d'un nouveau cache est presque instantanée
* Vous payez en fonction de l'utilisation (0,15 $/Go par coût de transfert)
* Il dispose d'un niveau gratuit très généreux (les 50 premiers Go par mois sont gratuits)
* Aucune carte de crédit requise pour commencer à utiliser le cache
* Il se met simplement à l'échelle, aucune configuration ou réglage de serveur requis
* Il fonctionne simplement depuis n'importe où

Momento est idéal pour les développeurs qui ont simplement besoin d'une solution de cache simple et qui souhaitent se concentrer sur leur code au lieu de devoir gérer l'infrastructure de cache.

## Pourquoi ne pas utiliser un service open source géré ?

Il existe déjà des services cloud open source gérés.

Par exemple :

* AWS dispose d'ElasticCache qui vous permet d'exécuter Memcached ou Redis
* Amazon MemoryDB pour Redis
* Azure dispose d'un Azure Cache pour Redis
* Redis dispose de sa propre offre Redis Cloud

Ces services cloud existants peuvent simplifier certains aspects de l'hébergement et de la mise à l'échelle d'une couche de cache pour vos applications web. Mais il y a certaines choses à considérer :

* vous devez choisir la bonne taille de calcul
* il y a des étapes d'intégration d'application supplémentaires
* cela prend du temps (jusqu'à une heure) pour provisionner un cache
* il y a des limitations sur l'endroit où un cache doit résider dans votre réseau

La base de données en mémoire open-source Redis, par exemple, dispose d'une variété de structures de données complexes et d'opérations de données. Elle pourrait être adaptée à des cas d'utilisation plus avancés, où elle dépasse le cadre d'un cache et peut agir (et est commercialisée comme) une base de données principale.

Il n'y a pas de mauvaise réponse lors du choix d'un cache. Ce que vous avez, ce sont des compromis et vous devez choisir la meilleure solution pour votre cas d'utilisation.

## Comment installer le CLI Momento

Momento (au moment de la rédaction de cet article) est un service uniquement API.

Ainsi, pour utiliser Momento, vous devez créer un compte en utilisant leur outil CLI.

**Instructions d'installation pour Windows :**

```bash
brew tap momentohq/tap
brew install momento-cli
```

**Instructions d'installation pour Linux :**

```bash
wget https://github.com/momentohq/momento-cli/releases/download/v0.22.8/momento-cli-0.22.8.linux_x86_64.tar.gz
tar -xvf momento-cli-0.22.8.linux_x86_64.tar.gz --strip-components 3
sudo mv momento /usr/local/bin
rm momento-cli-0.22.8.linux_x86_64.tar.gz
```

Une fois installé, testez que le CLI fonctionne avec la commande suivante :

```bash
momento --version
> momento 0.22.6
```

## Comment créer un compte Momento

Pour créer un compte, entrez la commande suivante :

```bash
momento account signup aws \
--email YOUR_EMAIL \
--region us-east-1

> Signing up for Momento...
> Success! Your access token will be emailed to you shortly.
```

N'oubliez pas de remplacer `YOUR_EMAIL` par votre propre adresse e-mail (par exemple, andrew@example.com).

Momento **va envoyer un jeton d'accès par e-mail** et ce jeton d'accès est la manière dont Momento identifiera et autorisera nos futurs appels API pour utiliser le cache.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Screen-Shot-2022-12-21-at-9.55.07-PM.png)
_Exemple d'e-mail avec le jeton fourni_

### Pourquoi ai-je dû taper "aws" lors de la création d'un compte ?

Remarquez que nous avons spécifié **aws** et la région AWS **us-east-1** lors de la création.

Lorsque vous créez un compte, vous devez indiquer quel fournisseur de services cloud (CSP) hébergera le cache.

Vous pourriez penser, dois-je avoir et connecter mon propre compte AWS ?

La réponse est non. Le cache est configuré dans le compte AWS de Momento.

La raison pour laquelle Momento vous permet de choisir le CSP est que certaines entreprises ont des politiques de données concernant la partie du monde et le CSP où leurs données doivent résider.

## Comment configurer le CLI pour utiliser le jeton d'accès

Nous devons configurer le CLI pour utiliser le jeton d'accès qui a été envoyé par e-mail.

Tapez la commande `momento configure` pour lancer l'assistant de configuration :

```bash
momento configure
Token: XXXXXXXXXXXXXXXXX
Default Cache [default-cache]: 
Default Ttl Seconds [600]: 
default-cache successfully created as the default with default TTL of 600s
```

* **Token** : Entrez le jeton en le copiant et en le collant depuis l'e-mail précédent
* **Default Cache** : Appuyez sur Entrée
* **Default TTL** : Appuyez sur Entrée

La commande `momento configure` générera deux fichiers de configuration TOML :

1. `~/.momento/credentials` – stocke la configuration sensible, par exemple : jeton d'accès

```toml
[default]
token=XXXXXXXX
```

2. `~/.momento/config` – stocke la configuration commune, par exemple : ttl par défaut

```toml
[default]
cache=default-cache
ttl=600
```

## Comment définir et obtenir des données de cache

Pour définir des données de cache, c'est simple. Vous avez les sous-commandes `cache set` et `cache get` :

```bash
momento cache set --key "andrew" --value "brown" 
momento cache get --key "andrew"
> brown
```

## Comment créer un nouveau cache

Nous pouvons créer un autre cache instantanément avec la commande `cache create`. Et nous fournirons le drapeau `--name` aux commandes `cache get` et `cache set` :

```bash
momento cache create --name freecodecamp
momento cache set --name freecodecamp --key "Quincy" --value "Larson" 
momento cache get --name freecodecamp --key "Quincy" 
> Larson
```

## Comment intégrer Momento directement dans le code de votre application web

Pour utiliser Momento dans le code backend d'une application web, nous devons utiliser l'un des SDK fournis.

Écrivons un exemple d'utilisation de Momento dans une application web Flask (Python) en utilisant le SDK Python de Momento.

Voici à quoi ressemble notre application Flask sans utiliser de cache :

```python
import os
import psycopg2
from flask import Flask, render_template
import json

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn

@app.route('/')

def index():
    json_data = get_free_courses()

    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )
    return response

def get_free_courses():
  json_data = None
  conn = get_db_connection()
  cur = conn.cursor()

  cur.execute('SELECT * FROM free_courses;')
  free_courses = cur.fetchall()

  json_data = json.dumps(free_courses)

  cur.close()
  conn.close()
  return json_data
```

Voici à quoi ressemblerait notre application en implémentant Momento :

```python
import os
import psycopg2
from flask import Flask, render_template
import json
from momento import simple_cache_client as scc

_MOMENTO_AUTH_TOKEN  = os.getenv('MOMENTO_AUTH_TOKEN')
_MOMENTO_TTL_SECONDS = os.getenv('MOMENTO_TTL_SECONDS')
_MOMENTO_CACHE_NAME  = os.getenv('_MOMENTO_CACHE_NAME')

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn

@app.route('/')
def index():
  with scc.SimpleCacheClient(_MOMENTO_AUTH_TOKEN, _MOMENTO_TTL_SECONDS) as cache_client:
    key = 'get_free_courses'
    get_resp = cache_client.get(_CACHE_NAME, 'get_free_courses')
    if get_resp.status() == 'hit':
      json_data = get_resp.value()
    elif get_resp.status() == 'miss':
      json_data = get_free_courses()
      cache_client.set(_CACHE_NAME, 'get_free_courses', json_data)

    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )
    return response

def get_free_courses():
  json_data = None
  conn = get_db_connection()
  cur = conn.cursor()

  cur.execute('SELECT * FROM free_courses;')
  free_courses = cur.fetchall()

  json_data = json.dumps(free_courses)

  cur.close()
  conn.close()
  return json_data
```

## Résumé

Si vous souhaitez essayer Momento, visitez leur documentation sur le site web pour plus d'informations.

%[https://docs.momentohq.com/]