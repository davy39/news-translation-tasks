---
title: Comment rendre votre site web propre et maintenable avec GraphQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-19T17:56:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-website-clean-and-maintainable-with-graphql-13fe06098656
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sTrMpQxK_1XEV7hORzgE_A@2x.png
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: Microservices
  slug: microservices
- name: Node.js
  slug: nodejs
- name: Web Development
  slug: web-development
seo_title: Comment rendre votre site web propre et maintenable avec GraphQL
seo_desc: 'By Ondrej Polesny

  REST API services, SQL databases, markdown files, text files, SOAP services… can
  you think of yet another way to store and exchange data and content? Production
  websites usually work with several different services and ways to store...'
---

Par Ondrej Polesny

Les services d'API REST, les bases de données SQL, les fichiers markdown, les fichiers texte, les services SOAP… pouvez-vous penser à une autre façon de stocker et d'échanger des données et du contenu ? Les sites web de production utilisent généralement plusieurs services et méthodes différents pour stocker des données, alors comment pouvez-vous garder l'implémentation propre et maintenable ?

Chaque site web Node.js, qu'il s'agisse d'une application monopage ou d'un site régulier, doit se connecter à un service ou système tiers. Au minimum, il doit obtenir du contenu à partir de fichiers markdown ou d'un CMS headless. Mais le besoin d'autres services se fait rapidement sentir. D'abord, il y a un formulaire de contact — vous devez stocker ses soumissions. Ensuite, il y a une recherche en texte intégral — vous devez trouver un service qui vous permet de créer des index et de rechercher à travers eux. Et la liste continue en fonction de la taille de votre projet.

![Image](https://miro.medium.com/max/60/1*zvX9FdKVxyLZxutsbo7Igw.png?q=20 align="left")

Quel est le problème avec cela ? Eh bien, rien au début. Lorsque vous êtes motivé à terminer un projet, vous créez un composant pour chacune de ces fonctionnalités. La communication est encapsulée dans les composants respectifs, et après quelques tests rapides, vous êtes heureux que tout fonctionne. Le client est heureux que le projet ait été livré avant la date limite, et en tant qu'effet secondaire, vous êtes également devenu un expert d'une API Content as a Service, des services de soumission de formulaires et de la reconstruction automatique des index de recherche.

Vous avez mis le site web en ligne si rapidement que vous avez été promu ! Et la connaissance du projet et de ses détails avec vous.

En quelques semaines, vos collègues sont chargés d'apporter quelques modifications au projet. Le client souhaite utiliser un autre fournisseur de recherche car l'original est trop cher. Les développeurs travaillent également sur un autre projet qui nécessite un formulaire de contact, ils ont donc pensé à utiliser le même composant, mais à stocker les soumissions dans un service différent. Ils viennent donc vous demander des détails sur votre implémentation.

![Image](https://miro.medium.com/max/60/1*Ek4R9z9_Rp9DP0mVcPhDcw.jpeg?q=20 align="left")

[*Source de l'image*](https://www.reddit.com/r/ProgrammerHumor/comments/8pdebc/only_god_and_i_knew/)

Lorsque vous finissez par abandonner la recherche dans votre mémoire, ils devront faire la même recherche que vous avez faite initialement pour comprendre l'implémentation. L'interface utilisateur est si étroitement couplée avec la fonctionnalité que lorsqu'ils veulent réutiliser les composants, ils finiront probablement par les implémenter à nouveau à partir de zéro (et peut-être copier-coller des morceaux de l'ancien code).

![Image](https://miro.medium.com/max/60/1*n1ukAvnQbjcoCCQTRsfa7w.png?q=20 align="left")

*Infrastructure découplée montrant la communication GraphQL et les résolveurs GraphQL spécifiques*

# Le bon niveau d'abstraction

Alors, comment pouvons-nous éviter ces problèmes pour garder notre code maintenable et propre ? Jetez un coup d'œil au graphique ci-dessus où j'ai divisé la communication avec les services tiers et l'interface utilisateur. Les spécificités de chaque API de service externe sont implémentées dans le middleware sur le back-end du site web. Les composants sur le front-end utilisent tous une seule façon de récupérer et de soumettre des données — GraphQL.

# GraphQL

Alors, qu'est-ce que GraphQL et pourquoi l'utiliser pour communiquer entre le front-end et le back-end ? GraphQL est un langage de requête, un protocole, qui a été fondé exactement à cette fin — pour découpler les données dont le front-end du site web a besoin des requêtes nécessaires pour les récupérer. Il est similaire à une API REST du point de vue de la fonctionnalité car il vous permet d'interroger des données. Pour plus d'informations, consultez la [page d'accueil de GraphQL](http://bit.ly/2TGSV85).

La principale différence réside dans la manière dont vous demandez les données. Supposons qu'un nouveau développeur sur le projet soit chargé de créer une page de blog. La page doit afficher des articles de blog qui sont stockés dans un CMS headless. J'utilise [Kentico Cloud](http://bit.ly/2QzUALM), qui est une plateforme Content as a Service (CaaS) vous permettant de stocker divers types de contenu dans des structures hiérarchiques claires et d'obtenir le contenu via une API REST. Par conséquent, la requête `GET` pour les données utilisant une API REST pourrait ressembler à ceci : https://deliver.kenticocloud.com/{projectID}/items?system.type=blog\_post

Un exemple de réponse serait :

```json
{
  "items": [
    {
      "system": {
        "id": "0282e86e-8c72-47f3-9d3d-2acf93a8986b",
        ...
        "last_modified": "2018-09-18T10:38:19.8406343Z"
      },
      "elements": {
        "title": {
          "type": "text",
          "name": "Title",
          "value": "Hello from new Developer Evangelist"
        },
        "content": {
          ...
        }
        ...
      }
    }
  ]
}
```

La réponse contient les données de tous les articles de blog sous forme JSON. Comme la page n'affiche qu'une liste d'articles de blog, beaucoup de données retournées (à partir du champ `content`) sont redondantes car nous n'avons pas besoin de les afficher. Pour économiser de la bande passante (que vous payez généralement), le développeur devrait utiliser un filtre `columns` supplémentaire : https://deliver.kenticocloud.com/{projectID}/items?system.type=blog\_post&elements=title,image,teaser

Ils doivent connaître les spécificités de l'API et ont probablement sa référence ouverte dans une autre fenêtre de navigateur tout en construisant la requête.

Obtenir les mêmes données avec GraphQL est beaucoup plus facile. Son schéma décrit nativement ce que le front-end est capable de rendre. Le développeur doit spécifier quelles données récupérer en notation graphique :

```graphql
query BlogPosts {
  getBlogPosts {
    elements {
      title
      image
      teaser
    }
  }
}
```

*(Trouvez plus d'exemples de requêtes GraphQL dans cet article* [*Pourquoi GraphQL ?*](http://bit.ly/2WVm1mr) *par Shankar Raju.)*

Maintenant, lorsque vous décidez de passer du stockage de contenu d'un CMS headless à des fichiers markdown ou à une base de données SQL, l'implémentation de la page de blog ne changera pas. La requête GraphQL aura toujours la même apparence.

Comment est-ce possible ? Regardons sous le capot un instant. La séparation de l'implémentation du front-end des services externes est réalisée en utilisant les parties suivantes :

* Schéma GraphQL

* Résolveurs GraphQL

* Serveur Apollo

![Image](https://miro.medium.com/max/60/1*WSbvAW_j4esd86H3z2zpdw.png?q=20 align="left")

# Schéma GraphQL

Le schéma GraphQL est très similaire aux diagrammes de classes. Il spécifie les modèles de données, comme `BlogPost` ou `FormSubmission`, et les requêtes GraphQL.

![Image](https://miro.medium.com/max/60/1*AKWViU8GCa0RIebR5nWUgA.png?q=20 align="left")

Ci-dessus, vous pouvez voir un exemple de schéma de modèles de données d'un site web simple. Notez qu'il y a des types non définis comme `SystemInfo` ou `AssetElement`. Je les ai omis dans le graphique car ils seront générés plus tard par le générateur de types du CMS headless automatiquement.

![Image](https://miro.medium.com/max/60/1*Sy_9h3871bq5A2vH5x_WOg.png?q=20 align="left")

Les requêtes et les mutations (appels qui peuvent modifier et stocker des données) décrivent ensuite comment les données dans ces modèles sont récupérées et manipulées, comme obtenir des données pour `BlogPost` ou soumettre un `FormSubmission`. C'est comme un diagramme de classes pour la couche de données intermédiaire du site web.

![Image](https://miro.medium.com/max/60/1*YLBKXWHdzSygxsCqNjjn-Q.png?q=20 align="left")

# Résolveurs

Les résolveurs sont les implémentations réelles des requêtes définies ci-dessus, comme le résolveur MySQL, le résolveur Kentico Cloud, et autres. Ils sont assignés à des requêtes spécifiques du schéma et sont responsables de leur traitement. Ainsi, lorsqu'un composant front-end souhaite récupérer des articles de blog en utilisant la requête GraphQL `getBlogPosts`, le serveur sélectionne et invoque le résolveur enregistré pour cette requête (résolveur Kentico Cloud). Le résolveur utilise l'API REST du CMS headless pour récupérer le contenu en JSON et le fournit sous forme de tableau d'objets au composant.

![Image](https://miro.medium.com/max/60/1*8AyVZndOfiIajt63M0bjuw.png?q=20 align="left")

Dans ce cas simple, les résolveurs sont appariés aux requêtes et mutations 1:1, mais un résolveur peut être inscrit à autant d'entre eux qu'il peut gérer. Le résolveur MySQL n'a actuellement rien à faire, mais pourrait s'avérer utile plus tard lorsque la fonctionnalité du site web grandira et que nous déciderons de stocker certaines entrées utilisateur sensibles localement en utilisant une base de données.

# Apollo les connecte tous

La dernière pièce du puzzle est le serveur Apollo. C'est le lien qui connecte toutes ces parties. Apollo est une bibliothèque, un framework, qui connecte le schéma GraphQL à un serveur HTTP dans Node.js. J'utilise personnellement Express comme serveur HTTP, mais vous pouvez également [aimer Connect, Restify ou Lambda](http://bit.ly/2IeLR1w).

Apollo a deux parties — serveur et client. Le serveur fonctionne comme un hôte pour le schéma GraphQL et gère les requêtes GraphQL. Ainsi, chaque fois que le front-end invoque une requête GraphQL, le serveur Apollo recherche le bon résolveur, attend qu'il traite les données et transmet sa réponse. Le serveur Apollo est souvent utilisé comme un simple convertisseur de n'importe quelle interface de service vers GraphQL lorsque vous devez vous intégrer à un système qui ne supporte pas nativement GraphQL.

Le client Apollo est un module qui s'intègre au front-end d'un site web et permet l'exécution de requêtes GraphQL.

# Modèle de base pour accélérer les choses

Dans cet article, j'ai expliqué comment séparer les préoccupations, isoler les connecteurs de services tiers et permettre un développement rapide des composants front-end en utilisant GraphQL sans connaître les spécificités de tous les services utilisés.

Mon [prochain article](http://bit.ly/2IsgznK) avec une [démo en direct](http://bit.ly/2GGHIB5) approfondit l'utilisation d'Apollo avec le schéma GraphQL, montre comment définir le schéma et implémenter les résolveurs. Il présente également [un modèle de base](http://bit.ly/2TGTmPW) qui a tous ces outils configurés et prêts pour votre développement.