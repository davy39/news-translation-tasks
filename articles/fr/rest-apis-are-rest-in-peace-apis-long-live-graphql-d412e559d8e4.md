---
title: Les API REST sont des API REST-in-Peace. Vive GraphQL.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-24T15:57:37.000Z'
originalURL: https://freecodecamp.org/news/rest-apis-are-rest-in-peace-apis-long-live-graphql-d412e559d8e4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2mTYU2RCJHagQrqQokYpww.png
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Les API REST sont des API REST-in-Peace. Vive GraphQL.
seo_desc: 'By Samer Buna


  Update: This article is now part of my “Complete Introduction to GraphQL”.

  Read the updated version of this content and more about GraphQL at jscomplete.com/why-graphql.


  After years of dealing with REST APIs, when I first learned abou...'
---

Par Samer Buna

> **Mise à jour :** Cet article fait maintenant partie de mon Introduction complète à GraphQL.

> Lisez la version mise à jour de ce contenu et plus sur GraphQL sur [**jscomplete.com/why-graphql**](https://jscomplete.com/g/rest-in-peace-apis).

Après des années à travailler avec des API REST, lorsque j'ai découvert GraphQL et les problèmes qu'il tente de résoudre, je n'ai pas pu résister à tweeter le titre exact de cet article.

Bien sûr, à l'époque, ce n'était qu'une tentative de ma part d'être drôle, mais aujourd'hui, je crois que cette prédiction amusante se réalise réellement.

Ne vous méprenez pas, s'il vous plaît. Je ne vais pas accuser GraphQL de tuer REST ou quoi que ce soit de ce genre. REST ne mourra probablement jamais, tout comme XML ne l'a jamais fait. Je pense simplement que GraphQL fera à REST ce que JSON a fait à XML.

Cet article n'est pas réellement à 100 % en faveur de GraphQL. Il y a une section très importante sur le coût de la flexibilité de GraphQL. Avec une grande flexibilité vient un grand coût.

Je suis un grand fan de Always [Start with WHY](https://startwithwhy.com/), alors faisons cela.

### En résumé : Pourquoi GraphQL ?

Les 3 problèmes les plus importants que GraphQL résout magnifiquement sont :

* **Le besoin de faire plusieurs allers-retours pour récupérer les données requises par une vue** : Avec GraphQL, vous pouvez toujours récupérer toutes les données initiales requises par une vue avec un _seul_ aller-retour vers le serveur. Pour faire de même avec une API REST, nous devons introduire des paramètres et des conditions non structurés qui sont difficiles à gérer et à mettre à l'échelle.
* **La dépendance des clients aux serveurs** : Avec GraphQL, le client parle un langage de requête qui : 1) élimine le besoin pour le serveur de coder en dur la forme ou la taille des données, et 2) découple les clients des serveurs. Cela signifie que nous pouvons maintenir et améliorer les clients séparément des serveurs.
* **La mauvaise expérience des développeurs front-end** : Avec GraphQL, les développeurs expriment les besoins en données de leurs interfaces utilisateur en utilisant un langage déclaratif. Ils expriment _ce_ dont ils ont besoin, et non _comment_ le rendre disponible. Il existe une relation étroite entre les données nécessaires à l'UI et la manière dont un développeur peut exprimer une description de ces données en GraphQL.

Cet article expliquera en détail comment GraphQL résout tous ces problèmes.

Avant de commencer, pour ceux d'entre vous qui ne sont pas encore familiarisés avec GraphQL, commençons par des définitions simples.

### Qu'est-ce que GraphQL ?

GraphQL est un _langage_. Si nous enseignons GraphQL à une application logicielle, cette application sera en mesure de communiquer de manière _déclarative_ tout besoin de données à un service de données backend qui parle également GraphQL.

> Tout comme un enfant peut rapidement apprendre une nouvelle langue — tandis qu'un adulte aura plus de mal à l'assimiler — commencer une nouvelle application à partir de zéro en utilisant GraphQL sera beaucoup plus facile que d'introduire GraphQL dans une application mature.

Pour enseigner à un service de données à parler GraphQL, nous devons implémenter une couche _runtime_ et l'exposer aux clients qui souhaitent communiquer avec le service. Considérez cette couche côté serveur comme un simple traducteur du langage GraphQL, ou un agent parlant GraphQL qui représente le service de données. GraphQL n'est pas un moteur de stockage, donc il ne peut pas être une solution à lui seul. C'est pourquoi nous ne pouvons pas avoir un serveur qui parle uniquement GraphQL et nous devons implémenter une couche runtime de traduction à la place.

Cette couche, qui peut être écrite dans n'importe quel langage, définit un schéma générique basé sur un graphe pour publier les _capacités_ du service de données qu'elle représente. Les applications clientes qui parlent GraphQL peuvent interroger ce schéma dans ses capacités. Cette approche découple les clients des serveurs et permet aux deux de évoluer et de s'adapter indépendamment.

Une requête GraphQL peut être soit une **query** (opération de lecture), soit une **mutation** (opération d'écriture). Dans les deux cas, la requête est une simple chaîne de caractères qu'un service GraphQL peut interpréter, exécuter et résoudre avec des données dans un format spécifié. Le format de réponse populaire qui est généralement utilisé pour les applications mobiles et web est _JSON_.

### Qu'est-ce que GraphQL ? (Version Explique-moi comme si j'avais 5 ans)

GraphQL est tout au sujet de la communication de données. Vous avez un client et un serveur et les deux doivent communiquer entre eux. Le client doit indiquer au serveur les données dont il a besoin, et le serveur doit répondre à ce besoin de données du client avec des données réelles. GraphQL s'interpose au milieu de cette communication.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fSaxvhFkiXvr8FoFZZjF0g.png)
_Capture d'écran tirée de mon cours Pluralsight — Building Scalable APIs with GraphQL_

Pourquoi le client ne peut-il pas communiquer directement avec le serveur, demandez-vous ? Il le peut certainement.

Il y a plusieurs raisons d'envisager une couche GraphQL entre les clients et les serveurs. L'une de ces raisons, et peut-être la plus populaire, est l'_efficacité_. Le client doit généralement demander au serveur plusieurs ressources, et le serveur comprend généralement comment répondre avec une seule ressource. Ainsi, le client finit par effectuer plusieurs allers-retours vers le serveur pour collecter toutes les données dont il a besoin.

Avec GraphQL, nous pouvons essentiellement déplacer cette complexité de requêtes multiples vers le côté serveur et laisser la couche GraphQL s'en occuper. Le client pose une seule question à la couche GraphQL et obtient une seule réponse qui contient exactement ce dont le client a besoin.

Il y a beaucoup plus d'avantages à utiliser une couche GraphQL. Par exemple, un autre grand avantage est la communication avec plusieurs services. Lorsque vous avez plusieurs clients demandant des données à plusieurs services, une couche GraphQL au milieu peut simplifier et standardiser cette communication. Bien que ce ne soit pas vraiment un point contre les API REST — car il est facile d'accomplir la même chose là-bas — un runtime GraphQL offre une manière structurée et standardisée de le faire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2mTYU2RCJHagQrqQokYpww.png)
_Capture d'écran tirée de mon cours Pluralsight — Building Scalable APIs with GraphQL_

Au lieu qu'un client aille directement aux deux services de données différents (dans la diapositive ci-dessus), nous pouvons avoir ce client communiquer avec la couche GraphQL. Ensuite, la couche GraphQL effectuera la communication avec les deux services de données différents. C'est ainsi que GraphQL isole d'abord les clients du besoin de communiquer dans plusieurs langues et traduit également une seule requête en plusieurs requêtes à plusieurs services utilisant différentes langues.

> Imaginez que vous avez trois personnes qui parlent trois langues différentes et ont différents types de connaissances. Ensuite, imaginez que vous avez une question qui ne peut être répondue qu'en combinant les connaissances des trois personnes ensemble. Si vous avez un traducteur qui parle les trois langues, la tâche de rassembler une réponse à votre question devient facile. C'est exactement ce qu'un runtime GraphQL fait.

Les ordinateurs ne sont pas assez intelligents pour répondre à n'importe quelle question (du moins pas encore), donc ils doivent suivre un algorithme quelque part. C'est pourquoi nous devons définir un schéma sur le runtime GraphQL et ce schéma est utilisé par les clients.

Le schéma est essentiellement un document de capacités qui contient une liste de toutes les questions que le client peut poser à la couche GraphQL. Il y a une certaine flexibilité dans la manière d'utiliser le schéma car nous parlons d'un graphe de nœuds ici. Le schéma représente principalement les limites de ce qui peut être répondu par la couche GraphQL.

Toujours pas clair ? Appelons GraphQL ce qu'il est vraiment et simplement : _Un remplacement pour les API REST_. Alors laissez-moi répondre à la question que vous vous posez probablement maintenant.

### Qu'est-ce qui ne va pas avec les API REST ?

Le plus gros problème avec les API REST est la nature des multiples endpoints. Ceux-ci nécessitent que les clients effectuent plusieurs allers-retours pour obtenir leurs données.

Les API REST sont généralement une collection d'endpoints, où chaque endpoint représente une ressource. Ainsi, lorsqu'un client a besoin de données provenant de plusieurs ressources, il doit effectuer plusieurs allers-retours vers une API REST pour rassembler les données dont il a besoin.

Dans une API REST, il n'y a pas de langage de requête client. Les clients n'ont pas le contrôle sur les données que le serveur retournera. Il n'y a pas de langage à travers lequel ils peuvent le faire. Plus précisément, le langage disponible pour les clients est très limité.

Par exemple, les endpoints de l'API REST _READ_ sont soit :

* GET `/ResourceName` - pour obtenir une liste de tous les enregistrements de cette ressource, ou
* GET `/ResourceName/ResourceID` - pour obtenir l'enregistrement unique identifié par cet ID.

Un client ne peut pas, par exemple, spécifier quels _champs_ sélectionner pour un enregistrement dans cette ressource. Cette information est dans le service de l'API REST lui-même et le service de l'API REST retournera toujours tous les champs, indépendamment de ceux dont le client a réellement besoin. Le terme de GraphQL pour ce problème est la _sur-récupération_ d'informations qui ne sont pas nécessaires. C'est une perte de ressources réseau et mémoire pour le client et le serveur.

Un autre gros problème avec les API REST est la gestion des versions. Si vous devez supporter plusieurs versions, cela signifie généralement de nouveaux endpoints. Cela conduit à plus de problèmes lors de l'utilisation et de la maintenance de ces endpoints et cela peut être la cause de la duplication de code sur le serveur.

Les problèmes d'API REST mentionnés ci-dessus sont ceux spécifiques à ce que GraphQL tente de résoudre. Ils ne sont certainement pas tous les problèmes des API REST, et je ne veux pas entrer dans ce qu'est et n'est pas une API REST. Je parle principalement des API populaires basées sur des endpoints HTTP de ressources. Chacune de ces API finit par devenir un mélange qui a des endpoints REST réguliers + des endpoints ad-hoc personnalisés conçus pour des raisons de performance. C'est là que GraphQL offre une alternative bien meilleure.

### Comment GraphQL fait-il sa magie ?

Il y a beaucoup de concepts et de décisions de conception derrière GraphQL, mais probablement les plus importants sont :

* Un schéma GraphQL est un schéma fortement typé. Pour créer un schéma GraphQL, nous définissons des _champs_ qui ont des _types_. Ces types peuvent être primitifs ou personnalisés et tout le reste dans le schéma nécessite un type. Ce système de types riche permet des fonctionnalités riches comme avoir une API introspective et être capable de construire des outils puissants pour les clients et les serveurs.
* GraphQL parle des données comme un graphe, et les données sont naturellement un graphe. Si vous devez représenter des données, la bonne structure est un graphe. Le runtime GraphQL nous permet de représenter nos données avec une API de graphe qui correspond à la forme naturelle de graphe de ces données.
* GraphQL a une nature déclarative pour exprimer les besoins en données. GraphQL fournit aux clients un langage déclaratif pour qu'ils expriment leurs besoins en données. Cette nature déclarative crée un modèle mental autour de l'utilisation du langage GraphQL qui est proche de la manière dont nous pensons aux besoins en données en anglais et cela rend le travail avec une API GraphQL beaucoup plus facile que les alternatives.

Le dernier concept est pourquoi je crois personnellement que GraphQL est un changement de jeu.

Ce sont tous des concepts de haut niveau. Entrons dans quelques détails supplémentaires.

Pour résoudre le problème des multiples allers-retours, GraphQL fait du serveur répondant un seul endpoint. Basiquement, GraphQL prend l'idée de l'endpoint personnalisé à l'extrême et fait simplement du serveur entier un seul endpoint personnalisé qui peut répondre à toutes les questions de données.

L'autre grand concept qui accompagne ce concept de single endpoint est le langage de requête client riche qui est nécessaire pour travailler avec cet endpoint personnalisé unique. Sans un langage de requête client, un single endpoint est inutile. Il a besoin d'un langage pour traiter une requête personnalisée et répondre avec des données pour cette requête personnalisée.

Avoir un langage de requête client signifie que les clients seront en contrôle. Ils peuvent demander exactement ce dont ils ont besoin et le serveur répondra avec exactement ce qu'ils demandent. Cela résout le problème de sur-récupération.

En ce qui concerne la gestion des versions, GraphQL a une approche intéressante à ce sujet. La gestion des versions peut être évitée complètement. Basiquement, nous pouvons simplement ajouter de nouveaux _champs_ sans supprimer les anciens, car nous avons un graphe et nous pouvons faire croître le graphe de manière flexible en ajoutant plus de nœuds. Ainsi, nous pouvons laisser les chemins sur le graphe pour les anciennes API et introduire de nouveaux sans les étiqueter comme de nouvelles versions. L'API grandit simplement.

Cela est particulièrement important pour les clients mobiles car nous ne pouvons pas contrôler la version de l'API qu'ils utilisent. Une fois installée, une application mobile peut continuer à utiliser cette même ancienne version de l'API pendant des années. Sur le web, il est facile de contrôler la version de l'API car nous poussons simplement du nouveau code. Pour les applications mobiles, c'est beaucoup plus difficile à faire.

_Pas encore totalement convaincu ?_ Et si nous faisions une comparaison un à un entre GraphQL et REST avec un exemple concret ?

### API RESTful vs API GraphQL — Exemple

Imaginons que nous sommes les développeurs responsables de la construction d'une nouvelle interface utilisateur pour représenter les films et les personnages de Star Wars.

La première UI que nous devons construire est simple : une vue pour afficher des informations sur une seule personne de Star Wars. Par exemple, Dark Vador, et tous les films dans lesquels cette personne est apparue. Cette vue doit afficher le nom de la personne, l'année de naissance, le nom de la planète, et les titres de tous les films dans lesquels ils sont apparus.

Aussi simple que cela puisse paraître, nous traitons en réalité avec 3 ressources différentes ici : Personne, Planète et Film. La relation entre ces ressources est simple et tout le monde peut deviner la forme des données ici. Un objet personne appartient à un objet planète et aura un ou plusieurs objets films.

Les données JSON pour cette UI pourraient être quelque chose comme :

```javascript
{
   "data":{
      "person":{
         "name":"Darth Vader",
         "birthYear":"41.9BBY",
         "planet":{
            "name":"Tatooine"
         },
         "films":[
            {
               "title":"A New Hope"
            },
            {
               "title":"The Empire Strikes Back"
            },
            {
               "title":"Return of the Jedi"
            },
            {
               "title":"Revenge of the Sith"
            }
         ]
      }
   }
}
```

En supposant qu'un service de données nous ait donné cette structure exacte pour les données, voici une façon possible de représenter sa vue avec React.js :

```
// Le composant conteneur :
<PersonProfile person={data.person} ></PersonProfile>
```

```
// Le composant PersonProfile :
Nom : {person.name}
Année de naissance : {person.birthYear}
Planète : {person.planet.name}
Films : {person.films.map(film => film.title)}
```

C'est un exemple simple, et bien que notre expérience avec Star Wars nous ait peut-être aidés ici un peu, la relation entre l'UI et les données est très claire. L'UI a utilisé toutes les clés de l'objet de données JSON que nous avons imaginé.

Voyons maintenant comment nous pouvons demander ces données en utilisant une API RESTful.

Nous avons besoin des informations d'une seule personne, et en supposant que nous connaissons l'ID de cette personne, une API RESTful est censée exposer ces informations comme suit :

```
GET - /people/{id}
```

Cette requête nous donnera le nom, l'année de naissance et d'autres informations sur la personne. Une bonne API RESTful nous donnera également l'ID de la planète de cette personne et un tableau d'IDs pour tous les films dans lesquels cette personne est apparue.

La réponse JSON à cette requête pourrait être quelque chose comme :

```
{  "name": "Darth Vader",  "birthYear": "41.9BBY",  "planetId": 1  "filmIds": [1, 2, 3, 6],  *** autres informations dont nous n'avons pas besoin ***}
```

Ensuite, pour lire le nom de la planète, nous demandons :

```
GET - /planets/1
```

Et pour lire les titres des films, nous demandons :

```
GET - /films/1GET - /films/2GET - /films/3GET - /films/6
```

Une fois que nous avons les 6 réponses du serveur, nous pouvons les combiner pour satisfaire les besoins en données de notre vue.

Outre le fait que nous avons dû faire 6 allers-retours pour satisfaire un besoin de données simple pour une UI simple, notre approche ici était impérative. Nous avons donné des instructions sur _comment_ récupérer les données et _comment_ les traiter pour les rendre prêtes pour la vue.

Vous pouvez essayer cela vous-même si vous voulez voir ce que je veux dire. Les données de Star Wars ont une API RESTful actuellement hébergée sur [http://swapi.co/](http://swapi.co/). Allez-y et essayez de construire notre objet de données de personne là-bas. Les clés peuvent être un peu différentes, mais les endpoints de l'API seront les mêmes. Vous devrez faire exactement 6 appels API. De plus, vous devrez sur-récupérer des informations dont la vue n'a pas besoin.

Bien sûr, ce n'est qu'une implémentation d'une API RESTful pour ces données. Il pourrait y avoir de meilleures implémentations qui rendront cette vue plus facile à implémenter. Par exemple, si le serveur API implémentait des ressources imbriquées et comprenait la relation entre une personne et un film, nous pourrions lire les données des films avec :

```
GET - /people/{id}/films
```

Cependant, un serveur d'API RESTful pur ne l'implémenterait probablement pas, et nous devrions demander à nos ingénieurs backend de créer cet endpoint personnalisé pour nous. C'est la réalité de la mise à l'échelle d'une API RESTful — nous ajoutons simplement des endpoints personnalisés pour satisfaire efficacement les besoins croissants des clients. La gestion d'endpoints personnalisés comme ceux-ci est difficile.

Examinons maintenant l'approche GraphQL. GraphQL sur le serveur adopte l'idée des endpoints personnalisés et la pousse à l'extrême. Le serveur ne sera qu'un seul endpoint et le canal n'a pas d'importance. Si nous faisons cela via HTTP, la méthode HTTP n'a certainement pas d'importance non plus. Supposons que nous avons un seul endpoint GraphQL exposé via HTTP sur `/graphql`.

Puisque nous voulons demander les données dont nous avons besoin en un seul aller-retour, nous aurons besoin d'un moyen d'exprimer nos besoins complets en données pour le serveur. Nous faisons cela avec une requête GraphQL :

```
GET ou POST - /graphql?query={...}
```

Une requête GraphQL est juste une chaîne de caractères, mais elle devra inclure toutes les parties des données dont nous avons besoin. C'est là que la puissance déclarative entre en jeu.

En anglais, voici comment nous déclarons notre besoin en données : _nous avons besoin du nom d'une personne, de son année de naissance, du nom de sa planète et des titres de tous ses films_. En GraphQL, cela se traduit par :

```
{  person(ID: ...) {    name,    birthYear,    planet {      name    },    films {      title    }  }}
```

Relisez les besoins exprimés en anglais une fois de plus et comparez-les à la requête GraphQL. C'est aussi proche que possible. Maintenant, comparez cette requête GraphQL avec les données JSON originales que nous avons commençées. La requête GraphQL est la structure exacte des données JSON, sauf sans toutes les parties valeurs. Si nous pensons à cela en termes de relation question-réponse, la question est l'énoncé de la réponse sans la partie réponse.

Si l'énoncé de la réponse est :

> _La planète la plus proche du Soleil est Mercure._

Une bonne représentation de la question est le même énoncé sans la partie réponse :

> _(Quelle est) la planète la plus proche du Soleil ?_

La même relation s'applique à une requête GraphQL. Prenez une réponse JSON, retirez toutes les parties réponse (qui sont les valeurs), et vous obtenez une requête GraphQL très adaptée pour représenter une question sur cette réponse JSON.

Maintenant, comparez la requête GraphQL avec l'UI React déclarative que nous avons définie pour les données. Tout dans la requête GraphQL est utilisé dans l'UI, et tout ce qui est utilisé dans l'UI apparaît dans la requête GraphQL.

C'est le grand modèle mental de GraphQL. L'UI connaît les données exactes dont elle a besoin et extraire cette exigence est assez facile. Élaborer une requête GraphQL est simplement la tâche d'extraire ce qui est utilisé comme variables directement depuis l'UI.

Si nous inversons ce modèle, il conservera toujours sa puissance. Si nous avons une requête GraphQL, nous savons exactement comment utiliser sa réponse dans l'UI car la requête aura la même structure que la réponse. Nous n'avons pas besoin d'inspecter la réponse pour savoir comment l'utiliser et nous n'avons besoin d'aucune documentation sur l'API. Tout est intégré.

Les données de Star Wars ont une API GraphQL hébergée sur [https://github.com/graphql/swapi-graphql](https://github.com/graphql/swapi-graphql). Allez-y et essayez de construire notre objet de données de personne là-bas. Il y a quelques différences mineures que nous expliquerons plus tard, mais voici la requête officielle que vous pouvez utiliser contre cette API pour lire notre besoin de données pour la vue (avec Dark Vador comme exemple) :

```
{  person(personID: 4) {    name,    birthYear,    homeworld {      name    },    filmConnection {      films {        title      }    }  }}
```

Cette requête nous donne une structure de réponse très proche de ce que notre vue a utilisé, et rappelez-vous, nous obtenons toutes ces données en un seul aller-retour.

### Le coût de la flexibilité de GraphQL

Les solutions parfaites sont des contes de fées. Avec la flexibilité que GraphQL introduit, une porte s'ouvre sur certains problèmes et préoccupations clairs.

Une menace importante que GraphQL rend plus facile est les attaques par épuisement des ressources (également connues sous le nom d'attaques par déni de service). Un serveur GraphQL peut être attaqué avec des requêtes excessivement complexes qui consommeront toutes les ressources du serveur. Il est très simple de demander des relations imbriquées profondes (utilisateur -> amis -> amis ...), ou d'utiliser des alias de champs pour demander le même champ plusieurs fois. Les attaques par épuisement des ressources ne sont pas spécifiques à GraphQL, mais lorsque nous travaillons avec GraphQL, nous devons être particulièrement prudents à leur sujet.

Il existe certaines mesures d'atténuation que nous pouvons prendre ici. Nous pouvons effectuer une analyse des coûts sur la requête à l'avance et imposer une sorte de limites sur la quantité de données que l'on peut consommer. Nous pouvons également implémenter un délai d'attente pour tuer les requêtes qui prennent trop de temps à résoudre. De plus, puisque GraphQL est simplement une couche de résolution, nous pouvons gérer l'application des limites de débit à un niveau inférieur sous GraphQL.

Si l'endpoint de l'API GraphQL que nous essayons de protéger n'est pas public et est destiné à une consommation interne de nos propres clients (web ou mobile), nous pouvons utiliser une approche de liste blanche et pré-approuver les requêtes que le serveur peut exécuter. Les clients peuvent simplement demander aux serveurs d'exécuter des requêtes pré-approuvées en utilisant un identifiant unique de requête. Facebook semble utiliser cette approche.

L'authentification et l'autorisation sont d'autres préoccupations auxquelles nous devons penser lorsque nous travaillons avec GraphQL. Doit-on les gérer avant, après ou pendant un processus de résolution GraphQL ?

Pour répondre à cette question, pensez à GraphQL comme un DSL (langage spécifique de domaine) au-dessus de votre propre logique de récupération de données backend. Ce n'est qu'une couche que nous pourrions mettre entre les clients et notre service de données réel (ou plusieurs services).

Pensez à l'authentification et à l'autorisation comme une autre couche. GraphQL n'aidera pas à l'implémentation réelle de la logique d'authentification ou d'autorisation. Ce n'est pas fait pour cela. Mais si nous voulons mettre ces couches derrière GraphQL, nous pouvons utiliser GraphQL pour communiquer les jetons d'accès entre les clients et la logique d'application. Cela est très similaire à la manière dont nous faisons l'authentification et l'autorisation avec les API RESTful.

Une autre tâche que GraphQL rend un peu plus difficile est la mise en cache des données client. Les API RESTful sont plus faciles à mettre en cache en raison de leur nature de dictionnaire. Cet emplacement donne ces données. Nous pouvons utiliser l'emplacement lui-même comme clé de cache.

Avec GraphQL, nous pouvons adopter une approche de base similaire et utiliser le texte de la requête comme clé pour mettre en cache sa réponse. Mais cette approche est limitée, pas très efficace et peut causer des problèmes de cohérence des données. Les résultats de plusieurs requêtes GraphQL peuvent facilement se chevaucher, et cette approche de mise en cache de base ne tiendrait pas compte du chevauchement.

Il existe cependant une solution brillante à ce problème. Une requête de graphe signifie un _cache de graphe_. Si nous normalisons une réponse de requête GraphQL en une collection plate d'enregistrements, en donnant à chaque enregistrement un identifiant unique global, nous pouvons mettre en cache ces enregistrements au lieu de mettre en cache les réponses complètes.

Ce n'est pas un processus simple cependant. Il y aura des enregistrements référençant d'autres enregistrements et nous gérerons un graphe cyclique. Le peuplement et la lecture du cache nécessiteront un parcours de requête. Nous devons coder une couche pour gérer la logique du cache. Mais cette méthode sera globalement beaucoup plus efficace que la mise en cache basée sur les réponses. [Relay.js](https://facebook.github.io/relay/) est un framework qui adopte cette stratégie de mise en cache et la gère automatiquement en interne.

Possiblement le problème le plus important auquel nous devrions être attentifs avec GraphQL est le problème communément appelé les requêtes SQL N+1. Les champs de requête GraphQL sont conçus pour être des fonctions autonomes et la résolution de ces champs avec des données provenant d'une base de données peut entraîner une nouvelle requête de base de données par champ résolu.

Pour une logique d'endpoint d'API RESTful simple, il est facile d'analyser, de détecter et de résoudre les problèmes N+1 en améliorant les requêtes SQL construites. Pour les champs résolus dynamiquement par GraphQL, ce n'est pas si simple. Heureusement, Facebook est un pionnier dans une solution possible à ce problème : [DataLoader](https://github.com/facebook/dataloader).

Comme son nom l'indique, DataLoader est un utilitaire que l'on peut utiliser pour lire des données à partir de bases de données et les rendre disponibles pour les fonctions de résolution GraphQL. Nous pouvons utiliser DataLoader au lieu de lire les données directement à partir des bases de données avec des requêtes SQL, et DataLoader agira comme notre agent pour réduire les requêtes SQL réelles que nous envoyons à la base de données.

DataLoader utilise une combinaison de traitement par lots et de mise en cache pour y parvenir. Si la même requête client a entraîné le besoin de demander à la base de données plusieurs choses, DataLoader peut être utilisé pour consolider ces questions et charger par lots leurs réponses à partir de la base de données. DataLoader mettra également en cache les réponses et les rendra disponibles pour les questions ultérieures sur les mêmes ressources.

Merci d'avoir lu.

Apprendre React ou Node ? Consultez mes livres :

* [Learn React.js by Building Games](http://amzn.to/2peYJZj)
* [Node.js Beyond the Basics](http://amzn.to/2FYfYru)