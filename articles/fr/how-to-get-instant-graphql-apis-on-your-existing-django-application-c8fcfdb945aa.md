---
title: Comment obtenir des API GraphQL instantanées sur votre application Django existante
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-04T19:48:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-instant-graphql-apis-on-your-existing-django-application-c8fcfdb945aa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BRtPUVYOTcVmiL0GlytYAQ.png
tags:
- name: authentication
  slug: authentication
- name: Django
  slug: django
- name: GraphQL
  slug: graphql
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment obtenir des API GraphQL instantanées sur votre application Django
  existante
seo_desc: 'By Karthik Venkateswaran

  TL;DR

  Here are the topics we’ll cover in this article if you want to jump around:

  Why GraphQL?

  GraphQL is a data query language developed by Facebook. It is not tied to any specific
  database. It provides a way for the client ...'
---

Par Karthik Venkateswaran

### TL;DR

Voici les sujets que nous aborderons dans cet article si vous souhaitez sauter d'un point à l'autre :

#### [**Pourquoi GraphQL ?**](https://medium.com/@vasanthivenkateswaran/c8fcfdb945aa#dcf2)

[GraphQL](https://graphql.org/) est un langage de requête de données développé par Facebook. Il n'est pas lié à une base de données spécifique. Il fournit un moyen pour le client d'interroger différentes bases de données simultanément en demandant ce dont il a besoin. Il retourne la réponse dans le format demandé par le client.

#### [**Créer un serveur GraphQL**](#8c56)

Quelles sont les différentes approches disponibles pour créer un serveur GraphQL ? Nous apprendrons comment le moteur Hasura GraphQL fournit le moyen le plus simple d'obtenir une API GraphQL sur votre base de données existante.

#### [**Installation du moteur GraphQL**](#8668)

Nous passerons par l'installation du moteur Hasura GraphQL. Ensuite, nous exposerons des tables via une API GraphQL.

#### [**Sécuriser le serveur GraphQL**](#9050)

#### [**Gérer la migration**](#50e3)

Alors, commençons !

### Pourquoi GraphQL ?

Dans une application Django typique, toute nouvelle exigence de fonctionnalité ou modification de schéma nécessitera d'ajouter ou de modifier une vue existante. Cela peut avoir un impact énorme sur la productivité des développeurs. Cela nécessitera des mises à jour de code à tous les endroits où une API particulière est consommée.

C'est là que [GraphQL](https://graphql.org/) devient utile. [GraphQL](https://graphql.org/) est un langage de requête pour les API. Il abstrait plusieurs sources de données. Cela permet aux développeurs d'applications de demander des données dans le format dont ils ont besoin. Cela se fait sans nécessiter de modifications de l'API backend. Au lieu d'appeler des endpoints individuels pour obtenir des données, nous appelons un seul endpoint. Nous obtenons toutes les informations que nous voulons, structurées exactement comme nous le souhaitons.

Cela peut donc vous faire vous demander : comment obtenir une API GraphQL sur mon application Django existante ?

### Créer un serveur GraphQL

Pour créer un serveur GraphQL, tout ce que vous avez à faire est de définir un **schéma**. Un schéma est un répertoire des types de données dans votre application. Les **fonctions de résolution** indiquent au serveur où et comment récupérer les données pour chaque type de données.

Les approches actuelles impliquent de l'écrire à partir de zéro (schéma, fonctions de résolution) avec l'aide d'outils comme [django-graphene](http://docs.graphene-python.org/projects/django/en/latest/).

Dans cet article, j'utiliserai le [moteur Hasura GraphQL](https://hasura.io) pour obtenir une API GraphQL sur mon application [Django](https://github.com/karthikvt26/django-blog-app/tree/4e92155f0af0f17545a9a77dac7d744b0cc51e31) existante, exécutée localement. Nous aboutirons à une solution comme illustré dans le diagramme ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rDlZ3Ejok1L-IvmpyUTu4w.png)
_Architecture avant et après l'intégration avec le moteur Hasura GraphQL_

Le [moteur Hasura GraphQL](https://hasura.io/) (HGE) vous offre une API GraphQL instantanée en temps réel sur votre base de données Postgres existante. HGE fonctionne directement avec votre système existant :

* [**Base de données Postgres**](#f087) **—** Se connecte à votre base de données existante et fournit une API GraphQL à votre base de données.
* [**Système d'authentification**](#9050) **—** Se connecte à votre système d'authentification existant pour sécuriser l'API GraphQL.
* [**Système de migration**](#50e3) **—** Le moteur Hasura GraphQL n'interfère pas avec le système de migration existant de Django. Le schéma peut être géré séparément via **models.py** et **django migrate** tant qu'il ne modifie pas le schéma suivi par le moteur GraphQL. Plus d'informations sur la manière dont le moteur Hasura GraphQL gère l'état de votre schéma peuvent être trouvées [ici](https://docs.hasura.io/1.0/graphql/manual/engine-internals/index.html).

De plus, il est livré avec une console pratique (similaire à l'admin Django) qui peut être utilisée pour déboguer les API GraphQL.

### Installation

Le moteur Hasura GraphQL peut être installé sur Heroku en utilisant le bouton ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*dcgu-klnpwTWilYiGMdM6Q.jpeg)
_Cliquez sur ce bouton pour déployer le moteur GraphQL sur Heroku_

ou sur toute machine capable d'exécuter Docker. Consultez la section [getting-started](https://docs.hasura.io/1.0/graphql/manual/getting-started/index.html) pour plus d'informations.

#### [Installation avec Docker](https://docs.hasura.io/1.0/graphql/manual/deployment/docker/index.html) et connexion à Postgres existant

Avant d'installer le moteur Hasura GraphQL, j'ai besoin d'obtenir la chaîne de connexion Postgres pour que le moteur Hasura GraphQL se connecte à la base de données. Je peux obtenir la chaîne de connexion Postgres à partir du fichier `[settings.py](https://github.com/karthikvt26/django-blog-app/blob/4e92155f0af0f17545a9a77dac7d744b0cc51e31/blog/settings.py)` de mon application.

```py
DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'SECUREPASSWORD',
        'HOST': '172.17.0.1',
        'PORT': '5432',
    }   
}
```

L'URL de connexion à la base de données sera :

```
postgres://postgres:SECUREPASSWORD@172.17.0.1:5432/postgres
```

Une fois le moteur Hasura GraphQL démarré, la visite de [http://localhost:8080](http://localhost:8080/) ouvre la console Hasura comme ci-dessous. La section **Données** affiche une liste des tables non suivies présentes dans la base de données, regroupées par schéma. Si vous vous demandez ce que sont les tables non suivies, consultez la [documentation](https://docs.hasura.io/1.0/graphql/manual/schema/using-existing-database.html) pour plus d'informations.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dJlxjx1PHK5flNXiKVy5sg.jpeg)
_Console du moteur Hasura GraphQL_

![Image](https://cdn-media-1.freecodecamp.org/images/1*S7hBC1Hefyr1ho3RcneXmw.jpeg)
_Console Hasura | Explorateur de données_

La capture d'écran ci-dessus liste les tables créées par l'application Django comme défini dans ce fichier [**models.py**](https://github.com/karthikvt26/django-blog-app/blob/4e92155f0af0f17545a9a77dac7d744b0cc51e31/medium/models.py) sous les tables non suivies. En cliquant sur le bouton d'ajout, elles apparaissent dans la liste des tables suivies à gauche. Cela les expose pour être interrogées via les API GraphQL :

![Image](https://cdn-media-1.freecodecamp.org/images/1*DU43Tx-lE4AK6CtFlVWRdw.jpeg)

Pour tester si tout fonctionne, essayons de récupérer tous les `authors` disponibles dans la table :

```
query {
  medium_author {
    id
    name
    interests
  }
}
```

La réponse du moteur GraphQL est :

```
{
  "data": {
    "medium_author": [
      {
        "name": "Karthik",
        "id": 2,
        "interests": "Cricket, Music, Code"
      },
      {
        "name": "Second Author",
        "id": 4,
        "interests": "Hockey"
      }
    ]
  }
}
```

#### Relation d'objet et de tableau

Le moteur GraphQL analyse votre schéma et suggère des relations basées sur les clés étrangères définies entre les tables.

![Image](https://cdn-media-1.freecodecamp.org/images/1*b0o9K84Qsfy2khrriNKJxg.jpeg)
_Relations de clés étrangères suggérées_

Le moteur GraphQL suggère automatiquement deux relations pour chaque clé étrangère qu'il rencontre.

* **Relation d'objet** : relation 1:1. Par exemple, un article n'aura qu'un seul auteur.
* **Relation de tableau** : relation 1:plusieurs. Par exemple, un auteur peut écrire plusieurs articles.

Dans le [schéma de blog](https://github.com/karthikvt26/django-blog-app/blob/master/medium/models.py), `mediumArticlesByauthorId` est une « relation de tableau ». Elle est basée sur la clé étrangère `medium_article :: author_id ->` id dans `medium_article`. `mediumAuthorByAuthorId` est une « relation d'objet » basée sur la même clé étrangère.

Lorsque nous suivons ces relations, le schéma GraphQL dérivé contient les noms des relations. Les tables et les relations peuvent être interrogées dans une seule requête :

![Image](https://cdn-media-1.freecodecamp.org/images/1*tSg46B7TF20ceET3rYLboQ.jpeg)
_Requête GraphQL avec relation de tableau_

![Image](https://cdn-media-1.freecodecamp.org/images/1*zeALwfd78Oqp2glGKG8oqw.jpeg)
_Requête GraphQL avec relation d'objet_

### Authentification

Par défaut, le moteur GraphQL est installé en mode développement. Toutes les tables/vues suivies par le moteur GraphQL peuvent être consultées/mises à jour sans aucune vérification. Cela est dangereux et n'est pas recommandé pour un environnement de production.

Hasura vous permet de définir des contrôles d'accès granulaires pour chaque champ de votre schéma GraphQL, essentiellement chaque table ou vue de votre schéma Postgres. Ces règles de contrôle d'accès peuvent utiliser des variables dynamiques qui accompagnent chaque requête. Consultez la [documentation](https://docs.hasura.io/1.0/graphql/manual/auth/index.html) pour plus d'informations.

Le moteur GraphQL peut être sécurisé contre l'accès direct en configurant une URL de webhook. Cela sera appelé par le moteur GraphQL pour valider chaque requête, sauf si la requête contient une `access-key` valide.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pX9ydrpIK9angEvmCHkKrA.png)
_Architecture de la manière dont la requête/réponse se produit_

Avant de sécuriser l'endpoint GraphQL avec `access-key` et `auth-hook` (URL de webhook), ajoutons une simple règle de contrôle d'accès en utilisant la console Hasura pour restreindre l'`author` à ne récupérer que ses données et faire une requête en utilisant l'explorateur GraphQL.

Voici à quoi ressemble la règle de contrôle d'accès pour la table `medium_author` pour le rôle = `user`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sjF-pudjQP96I8X8IMOebQ.jpeg)
_Ajouter un contrôle d'accès à la table author_

J'ai seulement créé la permission `select`, mais vous pouvez configurer pour les quatre types d'opérations (select, insert, update, delete). Consultez la [documentation](https://docs.hasura.io/1.0/graphql/manual/auth/basics.html) pour plus d'informations.

Faisons une requête à partir de la table `medium_author` et voyons quelle est la réponse :

![Image](https://cdn-media-1.freecodecamp.org/images/1*yaSciD7j9zo12Ph1JbBYqQ.jpeg)

Ici, veuillez noter que `x-hasura-user-id` est défini sur « 2 » et `x-hasura-role` est défini sur « user ». Ce sont les données `auth` qui seront transmises par `auth-hook` en [mode production](https://docs.hasura.io/1.0/graphql/manual/deployment/docker/securing-graphql-endpoint.html) (moteur GraphQL démarré avec `access-key` et `auth-hook`).

#### Sécuriser l'API GraphQL

Sécurisons le moteur GraphQL avec `access-key`. Configurons `auth-hook` avec le gestionnaire d'authentification, dans ce cas, l'application Django. Le [webhook](https://github.com/karthikvt26/django-blog-app/blob/e8c966b4d9b87e3a5b6a39f3b7c6e9e02fef034d/medium/views.py#L44) configuré sera invoqué par le moteur GraphQL. Le webhook retournera les `x-hasura-role` et `x-hasura-user-id` appropriés.

```yml
version: '3.6'
services:
  postgres:
    image: postgres
    environment:
    - "POSTGRES_PASSWORD:mysecretpassword"
    ports:
    - "5432:5432"
    restart: always
    volumes:
    - db_data:/var/lib/postgresql/data
  graphql-engine:
    image: hasura/graphql-engine:v1.0.0-alpha13
    ports:
    - "8080:8080"
    depends_on:
    - "postgres"
    restart: always
    environment:
      HASURA_GRAPHQL_DATABASE_URL: postgres://postgres:mysecretpassword@postgres:5432/postgres
    command:
      - graphql-engine
      - serve
      - --access-key=mysecretkey
      - --auth-hook=http://192.168.2.58:9090/validate_request
      - --enable-console
volumes:
  db_data:
```

Essayons de faire la requête à nouveau et voyons quelle est la réponse :

![Image](https://cdn-media-1.freecodecamp.org/images/1*afYqLtDIyrJyR7RU7iG6_w.jpeg)

Le [webhook](https://github.com/karthikvt26/django-blog-app/blob/e8c966b4d9b87e3a5b6a39f3b7c6e9e02fef034d/medium/views.py#L44) configuré rejette la requête car elle n'est pas authentifiée. Essayons de nous connecter en tant qu'utilisateur et de faire la requête avec le jeton d'authentification de l'utilisateur. Le système d'authentification Django résout les `cookies`. Il ajoute les informations de l'utilisateur au contexte de la requête, qui peuvent ensuite être utilisées par le gestionnaire de requêtes.

Pour les besoins de ce blog, j'ai écrit un simple middleware d'authentification. Il analysera `Authorization: Bearer <token>` et le résoudra en un utilisateur Django. L'utilisateur sera ajouté au contexte de la [requête](https://github.com/karthikvt26/django-blog-app/blob/e8c966b4d9b87e3a5b6a39f3b7c6e9e02fef034d/medium/authentication.py#L20). Voici un extrait de code du même.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YTesXQ80z4olokviXp-uTA.jpeg)
_Connexion avec un utilisateur ayant l'id = 2_

![Image](https://cdn-media-1.freecodecamp.org/images/1*I2DOakdiY0X-3bm7UGk9ZQ.jpeg)
_Requête avec l'utilisateur connecté_

L'utilisateur est authentifié par le webhook. Le webhook retourne le `x-hasura-user-id` et le `x-hasura-role` correspondants. Le moteur GraphQL répond avec les résultats appropriés comme configuré dans les règles d'accès.

### Système de migration

Le moteur Hasura GraphQL est livré avec des outils de migration puissants inspirés de Rails pour vous aider à suivre les modifications que vous apportez à votre schéma. Lorsque vous utilisez la console Hasura, l'interface de ligne de commande Hasura générera des fichiers de migration pour vous. Vous pouvez les mettre sous contrôle de version et même les modifier.

Par défaut, la console Hasura est servie par le moteur GraphQL. Elle peut être utilisée pour tester rapidement les fonctionnalités fournies par le moteur GraphQL. Cependant, si vous construisez une application complexe ou ajoutez Hasura à une application ou une base de données existante, vous devrez stocker les migrations pour garantir que votre itération et votre CI/CD se déroulent sans encombre.

#### Installation

Installez `hasura` en exécutant la commande suivante sur votre terminal si vous utilisez une machine Mac/Linux. Sinon, consultez notre [documentation](https://docs.hasura.io/1.0/graphql/manual/hasura-cli/install-hasura-cli.html) pour installer hasura sur différents environnements.

```
curl -L https://cli.hasura.io/install.sh | bash
```

L'exécution de la commande suivante initialisera un répertoire avec des fichiers de configuration hasura configurés pour utiliser votre moteur GraphQL.

```bash
$ hasura init --directory blog-hasura-app --endpoint http://localhost:8080 --access-key=mysecretkey
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*kMA2X_j9L9alBH7w8MnjNw.png)
_hasura init_

Remplacez la valeur de `endpoint` et `access-key` par les valeurs appropriées.

#### Désactiver la migration

Puisque Django gère les migrations par défaut, la migration Hasura peut être désactivée en tapant `hasura console` sur votre terminal. Pour ouvrir la console Hasura, accédez à **Données -> Migratio**ns (dans la barre de navigation de gauche) et désactivez **Autoriser les changements de schéma postgres**.

Nous pouvons toujours stocker les métadonnées Hasura juste pour nous assurer que l'application est toujours dans un état récupérable :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Wo4dKt2qPkKkPnoIbPDShg.jpeg)
_Avant de désactiver la migration_

![Image](https://cdn-media-1.freecodecamp.org/images/1*5ttl3UM-iQKdHCxUt5KUdw.jpeg)
_Après avoir désactivé la migration_

#### Exportation des métadonnées

Exportez les métadonnées Hasura et stockez-les dans le dossier des migrations. Cela garantira que votre système est toujours récupérable à partir de tout état indésirable.

```bash
hasura metadata export
```

La commande ci-dessus exportera le fichier `metadata.yaml` et le stockera dans le dossier `migrations`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*32kfQrUSc6qQBljLhTgFYQ.jpeg)

Veuillez vous assurer que les tables/vues sont créées/modifiées uniquement via le fichier **models.py** de Django pour éviter les incohérences.

Si vous souhaitez utiliser le système de migration Hasura à la place, consultez la [documentation](https://docs.hasura.io/1.0/graphql/manual/migrations/existing-project.html) pour plus d'informations.

[**_Hasura_**](https://goo.gl/fR68ep) _vous offre des API GraphQL instantanées en temps réel sur n'importe quelle base de données Postgres sans avoir à écrire de code backend._

_Pour ceux d'entre vous qui sont nouveaux dans le moteur Hasura GraphQL, [**ci**](https://docs.hasura.io/1.0/graphql/manual/index.html) est un bon endroit pour commencer._