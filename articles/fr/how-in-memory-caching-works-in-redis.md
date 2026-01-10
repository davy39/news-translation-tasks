---
title: Comment le cache en mémoire fonctionne dans Redis
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-07-16T16:19:35.000Z'
originalURL: https://freecodecamp.org/news/how-in-memory-caching-works-in-redis
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1752680755362/97cde2e5-3bb3-4b5d-b073-dcbf03c7f871.png
tags:
- name: Redis
  slug: redis
- name: caching
  slug: caching
- name: development
  slug: development
- name: memory
  slug: memory
seo_title: Comment le cache en mémoire fonctionne dans Redis
seo_desc: 'When you’re building a web app or API that needs to respond quickly, caching
  is often the secret sauce.

  Without it, your server can waste time fetching the same data over and over again
  – from a database, a third-party API, or a slow storage system.

  ...'
---

Lorsque vous construisez une application web ou une API qui doit répondre rapidement, le cache est souvent la solution secrète.

Sans lui, votre serveur peut perdre du temps à récupérer les mêmes données encore et encore - à partir d'une base de données, d'une API tierce ou d'un système de stockage lent.

Mais lorsque vous stockez ces données en mémoire, les mêmes informations peuvent être servies en quelques millisecondes. C'est là que Redis intervient.

Redis est un outil rapide et flexible qui stocke vos données en RAM et vous permet de les récupérer instantanément. Que vous construisiez un tableau de bord, automatisiez des publications sur les réseaux sociaux ou gériez des sessions utilisateur, Redis peut rendre votre système plus rapide, plus efficace et plus facile à mettre à l'échelle.

Dans cet article, vous apprendrez comment fonctionne le cache en mémoire et pourquoi Redis est un choix de prédilection pour de nombreux développeurs.

## **Table des matières**

* [Qu'est-ce que le cache en mémoire ?](#heading-qu-est-ce-que-le-cache-en-mémoire)
    
* [Qu'est-ce que Redis ?](#heading-qu-est-ce-que-redis)
    
* [Comment travailler avec Redis](#heading-comment-travailler-avec-redis)
    
    * [Installation de Redis](#heading-installation-de-redis)
        
    * [Types de données Redis](#heading-types-de-données-redis)
        
    * [Redis avec Python](#heading-redis-avec-python)
        
* [Cas d'utilisation réels](#heading-cas-d-utilisation-réels)
    
* [Conclusion](#heading-conclusion)
    

## **Qu'est-ce que le cache en mémoire ?**

Le cache en mémoire est une méthode de stockage des données dans la RAM du système au lieu de les récupérer à partir d'une base de données ou d'une source externe chaque fois qu'elles sont nécessaires.

![Diagramme montrant comment fonctionne le cache](https://cdn.hashnode.com/res/hashnode/image/upload/v1752582672642/78e262d7-76a3-4bf3-886c-32a190d190b7.webp align="center")

Puisque la RAM est incroyablement rapide par rapport au stockage sur disque, vous pouvez accéder aux données mises en cache presque instantanément. Cette approche est parfaite pour les informations qui ne changent pas très souvent, comme les réponses d'API, les profils utilisateur ou les pages HTML rendues.

Plutôt que d'exécuter répétitivement les mêmes requêtes ou appels d'API, votre application vérifie d'abord le cache. Si les données s'y trouvent, elles sont utilisées immédiatement. Si ce n'est pas le cas, vous les récupérez à partir de la source, les sauvegardez dans le cache, puis les retournez.

Cette technique réduit la charge sur votre backend, améliore le temps de réponse et peut considérablement améliorer les performances de votre application sous un trafic intense.

## **Qu'est-ce que Redis ?**

![Redis](https://cdn.hashnode.com/res/hashnode/image/upload/v1752582701613/951f7322-0c49-4437-b97b-6502bd93483a.webp align="center")

[Redis](https://redis.io/) est un magasin de données en mémoire open-source que les développeurs utilisent pour mettre en cache et gérer des données en temps réel.

Contrairement aux bases de données traditionnelles, Redis stocke tout en mémoire, ce qui rend la récupération des données incroyablement rapide. Mais Redis n'est pas qu'un simple magasin clé-valeur. Il offre une large gamme de types de données, des chaînes et listes aux ensembles, hachages et ensembles triés.

Redis est également capable de gérer des tâches plus avancées comme la messagerie pub/sub, les flux et les requêtes géospatiales. Malgré sa puissance, Redis est léger et facile à prendre en main.

Vous pouvez l'exécuter sur votre machine locale, le déployer sur un serveur ou même utiliser des services Redis gérés proposés par des fournisseurs de cloud. Il est utilisé par de grandes entreprises et dans tous types d'applications, du cache et du stockage de sessions à l'analyse en temps réel et aux files d'attente de tâches.

## **Comment travailler avec Redis**

### Installation de Redis

Mettre Redis en place et le faire fonctionner est surprenamment simple. Vous pouvez trouver les instructions d'installation en fonction de votre système d'exploitation [dans la documentation](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/).

Pour vous assurer que Redis fonctionne, exécutez :

```plaintext
redis-cli ping
# Doit répondre avec "PONG"
```

### Types de données Redis

Redis vous offre plusieurs types intégrés qui vous permettent de stocker et de gérer des données de manière flexible.

**Chaînes** : Paires clé → valeur simples.

```plaintext
SET username "Emily"
GET username
```

**Listes** : Collections ordonnées, idéales pour les files d'attente et les chronologies.

```plaintext
LPUSH tasks "task1"
RPUSH tasks "task2"
LRANGE tasks 0 -1
```

**Hachages** : Comme les objets JSON, parfaits pour les profils utilisateur.

```plaintext
HSET user:1 name "Alice"
HSET user:1 email "alice@example.com"
HGETALL user:1
```

**Ensembles** : Collections non ordonnées, idéales pour les tags ou les éléments uniques.

```plaintext
SADD tags "python"
SADD tags "redis"
SMEMBERS tags
```

**Ensembles triés** : Ensembles avec scores - utiles pour les tableaux de classement.

```plaintext
ZADD leaderboard 100 "Bob"
ZADD leaderboard 200 "Carol"
ZRANGE leaderboard 0 -1 WITHSCORES
```

Redis prend également en charge les Bitmaps, les hyperloglogs, les flux, les index géospatiaux, et continue d'étendre son support pour les [structures de données](https://redis.io/technology/data-structures/).

### Redis avec Python

Si vous travaillez en Python, utiliser Redis est tout aussi facile. Après avoir installé la bibliothèque Python `redis` avec `pip install redis`, vous pouvez vous connecter à votre serveur Redis et commencer à définir et obtenir des clés immédiatement.

Voici un exemple simple de [code Python](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/) pour travailler avec Redis :

```plaintext
import redis

# Connectez-vous au serveur Redis local sur le port par défaut 6379 et utilisez la base de données 0
r = redis.Redis(host='localhost', port=6379, db=0)

# --- Exemple de chaîne de base ---

# Définissez une clé appelée 'welcome' avec une valeur de chaîne
r.set('welcome', 'Hello, Redis!')

# Obtenez la valeur de la clé 'welcome'
# La sortie sera une chaîne d'octets : b'Hello, Redis!'
print(r.get('welcome'))


# --- Exemple de hachage (comme un dict Python) ---

# Créez un hachage Redis sous la clé 'user:1'
# Ce hachage stocke les champs 'name' et 'email' pour un utilisateur
r.hset('user:1', mapping={
    'name': 'Alice',
    'email': 'alice@example.com'
})

# Obtenez tous les champs et valeurs dans le hachage sous forme de dictionnaire de chaînes d'octets
# Sortie : {b'name': b'Alice', b'email': b'alice@example.com'}
print(r.hgetall('user:1'))


# --- Exemple de liste (agit comme une file d'attente ou une pile) ---

# Ajoutez 'Task A' à gauche de la liste 'tasks'
r.lpush('tasks', 'Task A')

# Ajoutez 'Task B' à gauche de la liste 'tasks' (il devient le premier élément)
r.lpush('tasks', 'Task B')

# Récupérez tous les éléments de la liste 'tasks' (de l'index 0 à -1, ce qui signifie la liste complète)
# Sortie : [b'Task B', b'Task A']
print(r.lrange('tasks', 0, -1))
```

Vous pourriez stocker les données de session d'un utilisateur, mettre en file d'attente des tâches en arrière-plan, ou même mettre en cache des pages HTML rendues. Les commandes Redis sont rapides et atomiques, ce qui signifie que vous n'avez pas à vous soucier des collisions de données ou de l'incohérence dans les environnements à fort trafic.

L'une des fonctionnalités les plus utiles de Redis est l'expiration des clés. Vous pouvez dire à Redis de supprimer automatiquement une clé après une certaine période, ce qui est particulièrement pratique pour les données de session ou les caches temporaires.

Vous pouvez définir un temps de vie (TTL) sur les clés, afin que Redis les supprime automatiquement

```plaintext
SET session:1234 "some data" EX 3600  # Expire dans 1 heure
```

Redis prend également en charge la persistance, donc même s'il s'agit d'un magasin en mémoire, vos données peuvent survivre à un redémarrage.

Redis n'est pas limité aux petites applications. Il s'adapte facilement grâce à la réplication, au clustering et à [Sentinel](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/).

La réplication vous permet de créer des copies en lecture seule de vos données, ce qui aide à distribuer la charge. Le clustering divise vos données en morceaux et les répartit sur plusieurs serveurs. Et Sentinel gère le basculement automatique pour garder votre système en fonctionnement même si un serveur tombe en panne.

## **Cas d'utilisation réels**

L'une des utilisations les plus courantes de Redis est la mise en cache des réponses d'API.

Supposons que vous avez une application qui affiche des données météorologiques. Plutôt que d'appeler l'[API météorologique](https://openweathermap.org/api) chaque fois qu'un utilisateur charge la page, vous pouvez mettre en cache la réponse pour chaque ville dans Redis pendant 5 ou 10 minutes. De cette façon, vous ne récupérez de nouvelles données que de temps en temps, et votre application devient beaucoup plus rapide et moins chère à exécuter.

Un autre cas d'utilisation puissant est la [gestion des sessions](https://gtcsys.com/faq/what-are-the-best-practices-for-caching-and-session-management-in-web-application-development-2/). Dans les applications web, chaque utilisateur connecté a une session qui suit qui il est et ce qu'il fait. Redis est un excellent endroit pour stocker ces données de session car il est rapide et temporaire.

Vous pouvez stocker l'ID de session comme une clé, avec les informations de l'utilisateur dans un hachage. Ajoutez un temps d'expiration, et vous avez un délai d'expiration de session automatique intégré. Puisque Redis est si rapide et supporte un accès hautement concurrent, il est parfaitement adapté aux applications avec des milliers d'utilisateurs se connectant en même temps.

## **Conclusion**

Le cache en mémoire est l'une des méthodes les plus simples et les plus efficaces pour accélérer votre application, et Redis le rend incroyablement facile à mettre en œuvre. Ce n'est pas seulement un cache, c'est une boîte à outils pour construire des systèmes rapides, scalables et en temps réel. Vous pouvez commencer modestement en mettant en cache quelques pages ou réponses d'API, et à mesure que vos besoins grandissent, Redis grandit avec vous.

Si vous commencez tout juste, essayez d'exécuter Redis localement et expérimentez avec différents types de données. Stockez quelques chaînes, construisez une simple file d'attente de tâches avec des listes, ou suivez les scores des utilisateurs avec un ensemble trié. Plus vous explorerez, plus vous verrez comment Redis peut aider votre application à fonctionner plus rapidement, plus intelligemment et plus efficacement.

Vous avez aimé cet article ? [Connectez-vous avec moi sur LinkedIn](https://www.linkedin.com/in/manishmshiva). À bientôt avec un autre sujet.