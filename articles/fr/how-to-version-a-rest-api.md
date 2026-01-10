---
title: Comment versionner une API REST
subtitle: ''
author: Tim Kleier
co_authors: []
series: null
date: '2020-03-03T01:17:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-version-a-rest-api
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/Art-Exhibit-Blog-Banner.png
tags:
- name: api
  slug: api
- name: data contracts
  slug: data-contracts
- name: REST
  slug: rest
- name: REST API
  slug: rest-api
- name: versioning
  slug: versioning
seo_title: Comment versionner une API REST
seo_desc: "If you're not very familiar with APIs, you might be wondering...why all\
  \ the fuss about API versioning? \nIf you've been burned by API changes, you're\
  \ probably the one fussing. If you are a maintainer of an API, you might also be\
  \ fussing about trying t..."
---

Si vous n'êtes pas très familier avec les APIs, vous vous demandez peut-être... pourquoi tout ce remue-ménage autour du versionnage des APIs ?

Si vous avez été brûlé par des changements d'API, vous êtes probablement celui qui s'inquiète. Si vous êtes un mainteneur d'une API, vous pourriez également vous inquiéter en essayant de répondre à des questions difficiles comme celles-ci :

```
# Est-ce la version 2 de seulement les produits ou de l'API entière ?
/v2/products

# Qu'est-ce qui a catalysé le changement entre v1 et v2 ? Comment sont-ils différents ?
/v1/products
/v2/products
```

Ces questions autour du versionnage ne sont pas faciles à répondre. Il n'est pas toujours clair de savoir à quoi `v1` ou `v2` fait référence. Et nous ne devrions pas simplement faire une deuxième version d'un endpoint lorsque la première ne semble plus suffire.

Il y a des raisons claires _pourquoi_ votre API doit avoir un versionnage, et il y a des stratégies claires pour _comment_ naviguer efficacement les changements d'API.

Cependant, j'ai constaté que la plupart des développeurs -- y compris moi-même, jusqu'à ce que j'apprenne certaines leçons à la dure -- ne sont pas conscients de ces raisons et stratégies.

Cet article cherche à mettre en lumière ces raisons de versionnage et stratégies pour l'accomplir. Nous allons supposer un contexte d'API [REST](https://restfulapi.net/), car c'est un standard pour de nombreuses APIs, et nous allons nous concentrer sur l'aspect _versionnage_.

## Qu'est-ce que le Versionnage ?

Nous devrions commencer par nous mettre d'accord sur ce que signifie le terme "versionnage d'API". Voici notre définition de travail :

> Le versionnage d'API est la pratique de gestion transparente des changements apportés à votre API.

Le versionnage est une communication efficace autour des changements apportés à votre API, afin que les consommateurs sachent à quoi s'attendre. Vous livrez des données au public d'une certaine manière et vous devez communiquer lorsque vous changez la façon dont ces données sont livrées.

En résumé, cela revient à gérer les contrats de données et les changements de rupture. Le premier est le bloc de construction principal de votre API et le second révèle pourquoi le versionnage est nécessaire.

### Contrats de Données

Une API est une **Interface** de Programmation d'Application, et une interface est une frontière _partagée_ pour échanger des informations. Le contrat de données est le cœur de cette interface.

> Un contrat de données est un accord sur la forme et le contenu général des données de requête et/ou de réponse.

Pour illustrer un contrat de données, voici un corps de réponse JSON de base :

```json
{
  "data": [
    {
      "id": 1,
      "name": "Product 1"
    },
    {
      "id": 2,
      "name": "Product 2"
    }
  ]
}
```

C'est un objet avec une propriété `data` qui est un tableau (liste) de produits, chacun avec une propriété `id` et `name`. Mais la propriété `data` aurait tout aussi bien pu s'appeler `body`, et la propriété `id` sur chaque produit aurait pu être un GUID au lieu d'un entier. Si un seul produit était retourné, `data` pourrait être un objet au lieu d'un tableau.

Ces changements apparemment subtils auraient conduit à un accord différent, un contrat différent, concernant la "forme" des données. La forme des données pourrait s'appliquer aux noms de propriétés, aux types de données, ou même au format attendu (JSON vs. XML).

## Pourquoi le Versionnage est-il Nécessaire ?

Avec les APIs, quelque chose d'aussi simple que changer un nom de propriété de `productId` à `productID` peut casser des choses pour les consommateurs. Cette même chose est arrivée à notre équipe la semaine dernière.

Heureusement, nous avions des tests pour attraper les changements dans le contrat de l'API. Cependant, nous n'aurions pas dû avoir besoin de ces tests, car les mainteneurs de l'API auraient dû savoir que ce serait un changement de rupture.

### Changements de Rupture

C'était un changement de rupture dans le contrat de données convenu car leur changement nous a forcés à changer notre application également.

> _Qu'est-ce qui constitue un "changement de rupture" dans un endpoint d'API ?_ Tout changement dans votre contrat d'API qui force le consommateur à faire également un changement.

Les changements de rupture entrent principalement dans les catégories suivantes :

1. Changer le format de requête/réponse (par exemple, de XML à JSON)
2. Changer un nom de propriété (par exemple, de `name` à `productName`) ou un type de données sur une propriété (par exemple, d'un entier à un float)
3. Ajouter un champ requis sur la requête (par exemple, un nouvel en-tête requis ou une propriété dans un corps de requête)
4. Supprimer une propriété sur la réponse (par exemple, supprimer `description` d'un produit)

### Gestion des Changements d'API

Il n'est jamais sage ou gentil de forcer les consommateurs d'une API à faire un changement. Si vous devez faire un changement de rupture, c'est pour cela que le versionnage existe, et nous allons couvrir les moyens les plus efficaces de versionner votre application et vos endpoints.

Mais d'abord, discutons brièvement de la manière d'éviter les changements de rupture en premier lieu. Nous pourrions appeler cela la gestion des changements d'API.

La gestion efficace des changements dans le contexte d'une API est résumée par les principes suivants :

* Continuer à supporter les propriétés/endpoints existants
* Ajouter de nouvelles propriétés/endpoints plutôt que de changer ceux existants
* Obsolescence réfléchie des propriétés/endpoints obsolètes

Voici un exemple qui démontre ces trois principes dans le contexte de la réponse pour la demande de données utilisateur :

```json
{
  "data": {
    "id": 1,
    "name": "Carlos Ray Norris",     // propriété originale
    "firstName": "Carlos",           // nouvelle propriété
    "lastName": "Norris",            // nouvelle propriété
    "alias": "Chuck",                // propriété obsolète
    "aliases": ["Chuck", "Walker"]   // nouvelle propriété
  },
  "meta": {
    "fieldNotes": [
      {
        "field": "alias",
        "note": "Obsolescence prévue pour [date future]. Veuillez utiliser aliases."
      }
    ]
  }
}
```

Dans cet exemple, `name` était une propriété originale. Les champs `firstName` et `lastName` sont mis en œuvre pour fournir une option plus granulaire, au cas où le consommateur souhaiterait afficher "M. Norris" avec une interpolation de chaîne sans avoir à analyser le champ `name`. Cependant, la propriété `name` sera supportée de manière continue.

`alias`, en revanche, va être déprécié au profit du tableau `aliases` -- parce que Chuck a tant d'alias -- et il y a une note dans la réponse pour indiquer le délai d'obsolescence.

## Comment Versionner une API ?

Ces principes vous mèneront loin dans la navigation des changements de votre API sans avoir besoin de lancer une nouvelle version. Cependant, parfois c'est inévitable, et si vous avez besoin d'un tout nouveau contrat de données, vous aurez besoin d'une nouvelle version de votre endpoint. Vous devrez donc communiquer cela au public d'une manière ou d'une autre.

À titre de remarque, notez que nous ne parlons pas de la version de la base de code sous-jacente. Donc, si vous utilisez le [versionnage sémantique](https://semver.org/) pour votre application qui supporte également une API publique, vous voudrez probablement séparer ces systèmes de versionnage.

Comment créer une nouvelle version de votre API ? Quelles sont les différentes méthodes pour le faire ? Vous devrez déterminer quel _type_ de stratégie de versionnage vous souhaitez adopter en général, et ensuite, au fur et à mesure que vous développez et maintenez votre API, vous devrez déterminer la _portée_ de chaque changement de version.

### Portée

Commençons par la portée. Comme nous l'avons exploré ci-dessus, parfois les contrats de données seront compromis par un changement de rupture, et cela signifie que nous devrons fournir une nouvelle version du contrat de données. Cela pourrait signifier une nouvelle version d'un endpoint, ou cela pourrait signifier un changement à un niveau plus global de l'application.

Nous pouvons penser aux niveaux de changement de portée dans une analogie d'arbre :

* **Feuille** - Un changement à un endpoint isolé sans relation avec d'autres endpoints
* **Branche** - Un changement à un groupe d'endpoints ou à une ressource accessible via plusieurs endpoints
* **Tronc** - Un changement au niveau de l'application, justifiant un changement de version sur la plupart ou tous les endpoints
* **Racine** - Un changement affectant l'accès à toutes les ressources de l'API de toutes les versions

Comme vous pouvez le voir, en passant de la feuille à la racine, les changements deviennent progressivement plus impactants et globaux en portée.

La portée _feuille_ peut souvent être gérée par une gestion efficace des changements d'API. Si ce n'est pas le cas, créez simplement un nouvel endpoint avec le nouveau contrat de données de la ressource.

Une _branche_ est un peu plus délicate, selon le nombre d'endpoints affectés par le changement de contrat de données sur la ressource en question. Si les changements sont relativement confinés à un groupe clair d'endpoints liés, vous pourriez potentiellement naviguer cela en introduisant un nouveau nom pour la ressource et en mettant à jour votre documentation en conséquence.

```
# variants, qui a un changement de rupture, est accessible sur plusieurs routes
/variants
/products/:id/variants

# nous introduisons product-variants à la place
/product-variants
/products/:id/product-variants
```

Un _tronç_ fait référence aux changements au niveau de l'application qui sont souvent le résultat d'un changement dans l'une des catégories suivantes :

* Format (par exemple, de [XML](https://www.w3schools.com/xml/xml_whatis.asp) à [JSON](https://www.w3schools.com/js/js_json_intro.asp))
* Spécification (par exemple, d'une spécification interne à [JSON API](https://www.freecodecamp.org/news/p/ccead735-3d4a-4304-b4e2-57b78ce59156/jsonapi.org) ou [Open API](https://www.openapis.org/))
* En-têtes requis (par exemple, pour l'authentification/autorisation)

Cela nécessitera un changement dans la version globale de votre API, vous devez donc planifier soigneusement et exécuter la transition correctement.

Un changement _racine_ vous forcera à aller un pas plus loin pour vous assurer que tous les consommateurs de toutes les versions de votre API sont conscients du changement.

## Types de Versionnage d'API

Alors que nous nous tournons vers différents types de versionnage d'API, nous voudrons utiliser ces informations sur les différentes portées des changements d'API pour évaluer les types. Chaque approche a ses propres forces et faiblesses pour traiter les changements en fonction de leur portée.

Il existe plusieurs méthodes pour gérer la version de votre API. Le versionnage par chemin URI est le plus courant.

### Chemin URI

```
http://www.example.com/api/v1/products
http://api.example.com/v1/products
```

Cette stratégie consiste à mettre le numéro de version dans le chemin de l'URI, et est souvent faite avec le préfixe "v". Plus souvent qu'autrement, les concepteurs d'API l'utilisent pour faire référence à leur version d'application (c'est-à-dire "tronç") plutôt qu'à la version de l'endpoint (c'est-à-dire "feuille" ou "branche"), mais ce n'est pas toujours une supposition sûre.

Le versionnage par chemin URI implique des versions orchestrées de l'application qui nécessiteront l'une des deux approches suivantes : maintenir une version tout en développant une nouvelle ou forcer les consommateurs à attendre de nouvelles ressources jusqu'à ce que la nouvelle version soit publiée. Cela signifie également que vous devrez reporter les endpoints non modifiés d'une version à l'autre. Cependant, pour les APIs avec une volatilité relativement faible, c'est encore une option décente.

Vous ne voudriez probablement pas relier votre numéro de version à celui de l'endpoint ou de la ressource, car cela pourrait facilement aboutir à quelque chose comme un `v4` de `products` mais un `v1` de `variants`, ce qui serait plutôt confus.

### Paramètres de Requête

```
http://www.example.com/api/products?version=1
```

Ce type de versionnage ajoute un paramètre de requête à la demande qui indique la version. Très flexible en termes de demande de la version de la ressource que vous souhaitez au niveau "feuille", mais il ne tient pas compte de la version globale de l'API et se prête aux mêmes problèmes de désynchronisation mentionnés dans le commentaire ci-dessus sur le versionnage au niveau de l'endpoint du chemin URI.

### En-tête

```
Accept: version=1.0
```

L'approche par en-tête est celle qui fournit plus de granularité dans la fourniture de la version demandée de toute ressource donnée.

Cependant, elle est enterrée dans l'objet de requête et n'est pas aussi transparente que l'option de chemin URI. Il est également toujours difficile de dire si `1.0` fait référence à la version de l'endpoint ou de l'API elle-même.

### Intégration des Types

Chacune de ces approches semble avoir la faiblesse de favoriser une portée "feuille" ou "tronç", mais ne supporte pas les deux.

Si vous devez maintenir la version globale de l'API et également fournir un support pour plusieurs versions de ressources, envisagez un mélange des types Chemin URI et Paramètres de Requête, ou une approche d'En-tête plus avancée.

```
# Combinaison de chemin URI et de paramètres de requête
http://api.example.com/v1/products?version=1
http://api.example.com/v1/products?version=2

# En-têtes étendus, pour http://api.example.com/products
Accept: api-version=1; resource-version=1
Accept: api-version=1; resource-version=2
```

## Conclusion

Nous avons couvert beaucoup de terrain ici, alors faisons un récapitulatif :

* Le versionnage d'API est la pratique de gestion transparente des changements apportés à votre API.
* La gestion d'une API se résume à définir et faire évoluer les contrats de données et à traiter les changements de rupture.
* La manière la plus efficace de faire évoluer votre API sans changements de rupture est de suivre les principes de gestion efficace des changements d'API.
* Pour la plupart des APIs, le versionnage dans le chemin URI est la solution la plus simple.
* Pour les APIs plus complexes ou volatiles, vous pouvez gérer différentes portées de changements en employant une intégration des approches de chemin URI et de paramètres de requête.

Bien que ces principes devraient fournir une direction claire sur la manière de gérer efficacement les changements de vos APIs, faire évoluer une API est potentiellement plus un art qu'une science. Cela nécessite de la réflexion et de la prévoyance pour créer et maintenir une API fiable.