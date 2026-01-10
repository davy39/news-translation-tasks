---
title: API publiques que les développeurs peuvent utiliser dans leurs projets
subtitle: ''
author: Ijeoma Igboagu
co_authors: []
series: null
date: '2023-03-02T00:28:23.000Z'
originalURL: https://freecodecamp.org/news/public-apis-for-developers
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/api-cover.jpg
tags:
- name: api
  slug: api
- name: Web Development
  slug: web-development
seo_title: API publiques que les développeurs peuvent utiliser dans leurs projets
seo_desc: "A public API, also known as an external API, is a type of application programming\
  \ interface that allows developers to access specific features and data of a software\
  \ application or service. \nIt is \"public\" in the sense that it is made available\
  \ to th..."
---

Une API publique, également connue sous le nom d'API externe, est un type d'interface de programmation d'applications qui permet aux développeurs d'accéder à des fonctionnalités et des données spécifiques d'une application logicielle ou d'un service. 

Elle est "publique" dans le sens où elle est mise à la disposition des développeurs tiers et n'est pas limitée à un usage interne par l'organisation qui a créé l'API. 

Les API publiques sont mises à la disposition de toute personne qui souhaite les utiliser et ne nécessitent généralement aucune autorisation spéciale ou authentification pour y accéder. Les développeurs peuvent utiliser les API publiques pour créer de nouvelles applications, améliorer celles existantes ou intégrer différents systèmes logiciels.

Dans cet article, nous allons discuter des types d'API publiques, de leurs avantages pour les développeurs, et des API publiques que vous pouvez utiliser dans vos projets.

## Types d'API publiques

Il existe différents types d'API que les développeurs peuvent utiliser pour accéder aux données et aux fonctionnalités fournies par les services en ligne. C'est comme emprunter l'outil de quelqu'un pour vous aider à faire votre travail plus facilement.

Voici les principaux types :

### API Representational State Transfer (REST)

Ce sont des API très populaires et faciles à utiliser qui utilisent des requêtes _HTTP_ pour obtenir ou modifier des données. Un exemple est l'API Twitter et certaines de celles mentionnées dans cet article.

### API Simple Object Access Protocol (SOAP)

Ces API sont plus complexes mais ont des superpouvoirs pour la sécurité et les fonctionnalités avancées. Ces API basées sur le web utilisent le format de données XML pour échanger des données entre les applications. Un exemple populaire est l'API Amazon Web Services (AWS).

### GraphQL

Cette API peut être plus efficace et vous faire gagner du temps en vous donnant uniquement les données dont vous avez besoin. Vous pouvez utiliser l'API GraphQL pour demander uniquement les noms et les descriptions des dépôts d'un utilisateur, plutôt que d'obtenir toutes les données du dépôt en une seule fois. 

Cela facilite le travail avec de grandes quantités de données et peut aider à améliorer les performances de l'application. Un exemple est l'API GraphQL de GitHub.

### Webhooks

Ce sont comme une ligne directe qui vous informe lorsque des choses importantes se produisent. Un exemple serait les notifications en temps réel sur les mises à jour des réseaux sociaux. Vous pouvez également utiliser les webhooks pour notifier une application lorsqu'un utilisateur effectue un achat.

### Websockets

Cette API permet une communication bidirectionnelle entre un client et un serveur en temps réel. Elles sont couramment utilisées pour les applications qui nécessitent des mises à jour en temps réel. Un exemple courant serait les applications de chat ou les jeux en ligne.

## Avantages des API publiques pour les développeurs

J'ai déjà fait allusion à certains des avantages de travailler avec des API publiques. Mais maintenant, laissez-moi expliquer pourquoi elles sont si utiles un peu plus en détail.

### Accès à des fonctionnalités existantes

Les API publiques fournissent aux développeurs un accès à des fonctionnalités et des données existantes qu'ils peuvent utiliser pour créer de nouvelles applications. Cela peut faire gagner du temps et des ressources aux développeurs - ils n'ont pas besoin de tout construire à partir de zéro.

### Intégration et expérience utilisateur améliorées

Les API publiques accélèrent le processus de développement des applications web et permettent également l'intégration entre différents systèmes.

Vous pouvez utiliser des API publiques pour créer des intégrations entre différentes applications et services. Cela peut améliorer l'expérience utilisateur en facilitant l'utilisation de différents produits ensemble de manière transparente.

### Efficacité améliorée

Les API publiques peuvent aider les développeurs à créer des applications plus efficacement en leur permettant de se concentrer sur les fonctionnalités spécifiques qu'ils souhaitent construire, plutôt que de devoir s'inquiéter de la technologie sous-jacente.

### Fonctionnalités accrues

En utilisant des API publiques, les développeurs peuvent ajouter de nouvelles fonctionnalités à leurs applications sans avoir à les construire eux-mêmes. Cela peut leur permettre de créer des applications plus complexes et innovantes.

## Défis liés à l'utilisation des API publiques

Malgré leur utilité, l'utilisation des API publiques présente certains défis. Voici quelques points à garder à l'esprit :

1. **Problèmes de confidentialité et de sécurité des données :** Les API publiques peuvent exposer des données sensibles et nécessiter des mesures d'authentification pour garantir que les données ne sont pas accessibles par des parties non autorisées.
2. **Documentation :** Certaines API publiques peuvent avoir une documentation incomplète ou mal rédigée, ce qui peut rendre difficile pour les développeurs de comprendre comment utiliser l'API.
3. **Compatibilité :** Certaines API publiques peuvent ne pas être compatibles avec le langage de programmation ou le framework qu'un développeur utilise, ce qui peut rendre difficile l'intégration de l'API avec leur application.
4. **Limites de taux :** De nombreuses API publiques ont des limites de taux, qui restreignent le nombre de requêtes qu'un développeur peut faire dans une période donnée. Si la limite de taux est dépassée, l'API peut retourner des erreurs ou cesser de fonctionner complètement.

## Comment choisir une API publique pour votre projet

Lorsque vous êtes prêt à choisir une API publique avec laquelle travailler, il y a certaines choses à garder à l'esprit. Ces conseils vous aideront à choisir celle qui convient à vos besoins et à éviter certains des défis que nous venons de discuter.

### Disponibilité et fiabilité

Pour vous assurer de choisir la meilleure API pour votre projet, assurez-vous de vérifier sa disponibilité et sa fiabilité. 

Recherchez des API qui offrent des garanties de haute disponibilité et qui ont un historique prouvé de disponibilité fiable. Tenez également compte du fait que l'API a des restrictions d'utilisation ou s'il y a des coûts associés.

### Documentation et support

Choisissez des API qui disposent d'une documentation et d'un support appropriés. Cela vous aidera à comprendre comment les utiliser et à résoudre les problèmes techniques. Recherchez une documentation claire et détaillée qui peut répondre rapidement à vos préoccupations ou questions.

### Sécurité et confidentialité

Prenez en compte la sécurité et la confidentialité de votre projet et de vos données, ce qui pourrait être crucial. Recherchez des API avec des mesures de sécurité solides, comme le chiffrement et l'authentification, et qui ont des politiques de confidentialité transparentes garantissant la protection des données des utilisateurs. Choisissez des API en fonction de la sensibilité de votre projet et de vos données.

### Exigences du projet

Lors de la sélection d'une API, réfléchissez à ce que vous souhaitez accomplir avec votre projet et aux fonctionnalités dont vous avez besoin de la part de l'API. Par exemple, si vous avez l'intention d'intégrer les réseaux sociaux, utilisez une API de réseau social comme Twitter ou Facebook.

### Avis et retours

Consultez les retours et les avis d'autres développeurs qui ont utilisé l'API que vous envisagez. Les avis peuvent fournir des informations sur les forces et les limitations de l'API, ainsi que sur les problèmes potentiels auxquels d'autres développeurs ont été confrontés.

## API publiques courantes utilisées par les développeurs

Si vous cherchez des idées d'API publiques utiles que vous pouvez utiliser, vous avez de la chance. J'ai compilé une liste ici pour vous aider à commencer, contenant certaines des API publiques les plus populaires qui peuvent ajouter beaucoup à vos projets.

### API [JSONPlaceholder](https://jsonplaceholder.typicode.com/)

Il s'agit d'un site web qui aide les développeurs à tester leurs programmes avant d'utiliser un vrai. Il vous permet de créer, modifier et supprimer des données fictives en utilisant des requêtes HTTP. 

Ces données fictives peuvent être ajustées pour répondre à vos besoins et se présentent sous différentes formes comme JSON, CSV et YAML. Ce site vous aide à vous assurer que votre code fonctionne correctement et à créer des démonstrations pour que les autres puissent voir.

### API météo

Les API météo, telles que [**OpenWeatherMap**](https://openweathermap.org/) et [**Weather Underground**](https://www.wunderground.com/), vous permettent d'incorporer des données météo en temps réel, historiques et prévisionnelles dans vos applications. 

Ces API offrent un large éventail d'informations météo, y compris la température actuelle, la vitesse et la direction du vent, l'humidité, la pression atmosphérique et les précipitations. 

Le seul obstacle est que les utilisateurs doivent obtenir une clé. Mais elles fournissent un accès gratuit ou abordable à leurs données pour un usage non commercial et des projets à petite échelle.

### API d'actualités

Les API d'actualités comme l'[**API du New York Times**](https://developer.nytimes.com/apis) fournissent aux développeurs un accès aux articles de presse et au contenu multimédia. Vous pouvez les utiliser pour récupérer des articles, des images, des vidéos et d'autres types de médias et sont couramment utilisées pour construire des agrégateurs de nouvelles et des moteurs de recherche. 

L'API du New York Times est fréquemment utilisée pour créer des flux de nouvelles personnalisés et des applications qui analysent le contenu des nouvelles pour détecter des tendances.

### API de livres

Celles-ci fournissent un accès aux données et aux informations sur les livres telles que leurs titres, auteurs, genres, ISBN, dates de publication, images de couverture et descriptions. Des exemples sont l'[**API Google Books**](https://developers.google.com/books) et l'[**API Open Library**](https://openlibrary.org/developers/api)**.**

### API de films

Une API de films fournit un accès à une base de données d'informations sur les films, y compris des détails sur les titres de films, les dates de sortie, les genres, les notes, les membres de la distribution, et plus encore. Elle prend également en charge la recherche et le filtrage de films en fonction de divers critères. 

Des exemples sont l'[**API The Movie Database (TMDb)**](https://developers.themoviedb.org/3/getting-started/introduction)**,** l'[**API IMDb**](https://developer.imdb.com/)**,** et l'[**API Rotten Tomatoes**](https://rapidapi.com/collection/rotten-tomatoes-api)**.**

### API de repas et boissons

Cette API fournit un accès à des informations sur la nourriture et les boissons. [**TheMealDB API**](https://www.themealdb.com/api.php) et [**Spoonacular API**](https://spoonacular.com/food-api) sont des exemples d'API qui offrent un accès à des données liées à la nourriture et aux boissons, y compris des détails sur leurs noms, ingrédients, informations nutritionnelles, recettes et images. [**Cocktail DB API**](https://www.thecocktaildb.com/api.php) est une API spécialisée dans les boissons et les cocktails.

### API YouTube

Cette API aide les développeurs à faire beaucoup de choses, comme trouver des vidéos, obtenir des informations à leur sujet, gérer des comptes utilisateurs, ajouter ou modifier des vidéos, obtenir des commentaires et des analyses, et plus encore. 

Cette API est généralement utilisée dans des applications qui montrent des vidéos ou travaillent avec YouTube. Un exemple d'API YouTube est l'[**API YouTube Data**](https://developers.google.com/youtube/v3).

### API Google Search

L'API Google Search est un outil qui vous permet d'accéder et d'intégrer les résultats du moteur de recherche de Google dans vos applications. Elle fournit une gamme de fonctionnalités telles que la recherche de pages web, d'images, de vidéos, d'articles de presse, et plus encore. 

Avec cette API, vous pouvez créer des expériences de recherche personnalisées pour vos utilisateurs, ainsi qu'extraire et analyser les données de recherche. Mais il est important de noter qu'à partir de septembre 2021, Google a obsolète l'API Google Search et l'a remplacée par l'[**API Custom Search JSON**](https://developers.google.com/custom-search/v1/introduction).

### API eCommerce

Ces API aident les développeurs à intégrer des plateformes eCommerce dans leurs applications. Elles vous permettent de gérer des catalogues de produits, de traiter des commandes et des paiements, et de créer des boutiques en ligne et des applications d'achat. 

Des exemples populaires d'API eCommerce incluent [**Shopify API**](https://shopify.dev/docs/api), [**WooCommerce API**](https://woocommerce.com/document/woocommerce-rest-api/), et [**Magento API**](https://www.cloudways.com/blog/magento-2-rest-api/#:~:text=The%20Magento%20API%20allows%20the,responses%20for%20creating%20the%20integration.).

### API de chiens

Cette API est pour les amateurs de chiens et vous donne accès à une base de données d'informations et de médias liés aux chiens. 

Elle inclut des fonctionnalités telles que la récupération d'informations sur les races de chiens, des images, des images de chiens aléatoires, et plus encore. 

Vous pouvez utiliser cette API pour créer diverses applications liées aux chiens telles que l'identification des races de chiens, des galeries d'images de chiens et des applications d'entraînement pour chiens. Des exemples incluent [**Dog API**](https://thedogapi.com/) et [**Dog CEO API**](https://dog.ceo/dog-api/).

### [The Cat API](https://thecatapi.com/)

Il s'agit d'une API basée sur le web qui fournit aux développeurs un accès à une grande collection d'images et d'informations sur les chats, y compris la race, le tempérament, et plus encore. 

L'API est gratuite à utiliser pour des fins non commerciales, avec certaines limitations sur le nombre de requêtes qui peuvent être faites par jour. 

### API de dictionnaire 

Cette API vous permet d'accéder aux données de dictionnaire et de les intégrer dans vos applications. Elle fournit des fonctionnalités telles que les définitions de mots, les synonymes, les antonymes, les traductions, et plus encore. 

Avec cette API, vous pouvez créer des applications liées à la langue telles que des jeux de mots, des applications d'apprentissage de langues et des outils de traduction. 

Des exemples d'API de dictionnaire incluent [**Merriam-Webster Dictionary API**](https://dictionaryapi.com/) et [**Oxford Dictionary API**](https://developer.oxforddictionaries.com/). Ces API fournissent aux développeurs une vaste collection de données liées aux mots que vous pouvez utiliser pour créer diverses applications liées à la langue.

### API de sports

Les API de sports vous donnent accès à de nombreuses informations sur les sports comme les statistiques des joueurs et des équipes, les calendriers et les résultats des matchs. 

Avec ces API, vous pouvez créer des applications qui montrent aux utilisateurs des mises à jour en direct sur les matchs, les scores et d'autres nouvelles sportives. Certains exemples d'API de sports sont [**Sportradar API,**](https://developer.sportradar.com/docs/read/Home) [**Api-Sport**](https://api-sports.io/)**s,** et l'[**API NFL**](https://developer.nfl.com/get-started/overview).

### API de citations

Les API de citations vous donnent accès à une collection de citations célèbres, de proverbes et de phrases de divers auteurs, célébrités et figures historiques. 

Ces API vous permettent de récupérer des citations et de les afficher dans vos applications ou sites web, et elles incluent souvent des fonctionnalités pour rechercher et filtrer des citations en fonction de différents critères, tels que l'auteur, la catégorie ou le mot-clé. Des exemples d'API de citations incluent [**Quotes Free API**](https://zenquotes.io/)**.**

### API de blagues

Il s'agit d'un type d'API publique qui vous donne accès à divers types de blagues, y compris des jeux de mots, des blagues en une ligne, et plus encore. 

Ces API sont souvent utilisées pour créer des applications qui peuvent générer des blagues aléatoires ou afficher des blagues en fonction de catégories ou de thèmes spécifiques. Elles peuvent également être utilisées pour ajouter de l'humour à des applications existantes ou pour créer des applications autonomes liées aux blagues. Des exemples d'API de blagues incluent [**JokeAPI**](https://sv443.net/jokeapi/v2/) et [**DadJokes**](https://dadjokes.io/).

### [National Park Service (NPS) API](https://www.nps.gov/subjects/developer/api-documentation.htm)

Il s'agit d'une API publique gratuite qui permet aux développeurs d'obtenir de nombreuses informations sur les parcs nationaux aux États-Unis. Cela inclut des détails sur l'emplacement des parcs, ce qu'ils contiennent et les événements qui s'y déroulent. L'API contient également des données sur les animaux, les plantes et autres éléments naturels trouvés dans les parcs. 

Tout le monde peut utiliser l'API s'il s'inscrit pour obtenir une clé gratuite, et cela ne coûte pas d'argent. Mais il y a des limites sur la quantité de données que vous pouvez demander chaque jour pour vous assurer qu'elle fonctionne bien pour tout le monde.

### [Giphy SDK API](https://developers.giphy.com/docs/sdk)

L'API Giphy SDK (kit de développement logiciel) fournit un accès à une vaste bibliothèque de GIF et d'autocollants, ainsi que des outils pour rechercher, filtrer et organiser le contenu. Elle vous permet d'ajouter des GIF animés et d'autres types de contenu court à vos applications, sites web et autres produits numériques.

### [Rest Countries API](https://restcountries.com/)

Cette API fournit des informations sur les pays et territoires du monde entier, y compris leurs noms, capitales, devises, langues, et plus encore.

### API de galerie

Cette API vous donne accès à des collections d'images ou d'autres médias et les affiche. Voici quelques exemples : [**Unsplash API**](https://unsplash.com/developers)**,** [**Flickr API**](https://www.flickr.com/services/api/)**,** [**Getty Images API**](https://developers.gettyimages.com/)**,** et [**Pexels API**](https://www.pexels.com/api/)**.**

### [Health API (specifically Covid-19 API)](https://covid19api.com/)

Il s'agit d'une API gratuite pour les développeurs, et vous pouvez l'utiliser pour créer des applications, services et visualisations liés au COVID-19. 

Les développeurs peuvent utiliser ces API pour obtenir les dernières données sur les cas de COVID-19, les décès et les rétablissements, et utiliser ces données pour informer leurs applications et services.

## Conclusion

Les API publiques fournissent aux développeurs un accès à des fonctionnalités, des données et des services préconstruits, leur permettant d'intégrer ces capacités dans leurs applications sans avoir à les construire à partir de zéro. 

Cela peut vous faire gagner du temps et des ressources, vous permettant de vous concentrer sur la construction de fonctionnalités et de fonctionnalités uniques qui distinguent vos applications.

Dans cet article, nous avons couvert certaines API publiques, mais il en existe beaucoup d'autres, couvrant un large éventail de fonctionnalités et de types de données. Vous devez soigneusement considérer les exigences de votre projet et choisir les API qui répondent le mieux à vos besoins.

**Vous pouvez lire davantage sur les API publiques dans ce guide sur** [**35+ API publiques gratuites pour améliorer la productivité**](https://blog.idrisolubisi.com/35-free-public-apis-to-improve-productivity).

Si vous avez aimé cet article, envisagez de le partager pour aider d'autres développeurs.

Vous pourriez également visiter [**mon blog**](https://ijaycent.hashnode.dev/) pour lire d'autres articles de moi, et vous pouvez me suivre sur [**Twitter**](https://twitter.com/ijaydimples) et [**LinkedIn**](https://www.linkedin.com/in/ijeoma-igboagu/).

Merci d'avoir lu 💖