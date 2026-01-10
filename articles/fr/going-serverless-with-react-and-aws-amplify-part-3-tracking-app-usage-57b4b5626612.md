---
title: 'Passer au serverless avec React et AWS Amplify Partie 3 : Suivi de l''utilisation
  de l''application'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-01T16:23:02.000Z'
originalURL: https://freecodecamp.org/news/going-serverless-with-react-and-aws-amplify-part-3-tracking-app-usage-57b4b5626612
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JVJUmyxHqvzblJFMRXRp4g.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Passer au serverless avec React et AWS Amplify Partie 3 : Suivi de l''utilisation
  de l''application'
seo_desc: 'By Peter Mbanugo

  Serverless is a cloud-computing execution model in which the cloud provider is responsible
  for executing a piece of code by dynamically allocating resources to run the code
  when needed. With it, we can get reduced operation cost and ...'
---

Par Peter Mbanugo

Le serverless est un modèle d'exécution de cloud computing dans lequel le fournisseur de cloud est responsable de l'exécution d'un morceau de code en allouant dynamiquement des ressources pour exécuter le code lorsque cela est nécessaire. Avec cela, nous pouvons obtenir une réduction des coûts d'exploitation et du temps de développement. Il nous permet de nous concentrer sur notre code pour fournir une valeur commerciale aux utilisateurs sans nous soucier de la construction et de la maintenance des serveurs.

Il faut quelques étapes pour configurer et intégrer ces services avec notre code, et AWS Amplify a été construit pour faciliter la création d'applications serverless sur AWS. Il fournit des outils pour créer et configurer des services avec quelques commandes, et des composants de bibliothèque pour interagir facilement avec ces services à partir de notre code.

Cet article fait partie d'une série où je vous montre comment construire des applications serverless dans React et AWS Amplify. Dans le [premier article](https://medium.freecodecamp.org/going-serverless-with-react-and-aws-amplify-development-environment-set-up-9b15c3363bd), nous avons configuré notre environnement de développement, un projet Amplify et un projet React. Dans le [deuxième article](https://medium.freecodecamp.org/going-serverless-with-react-and-aws-amplify-part-2-creating-and-using-serverless-services-d401ba346eeb), nous avons créé des services backend s'exécutant sur différents services AWS et construit une application React pour effectuer des opérations CRUD, interagissant ainsi avec les services backend que nous avons créés.

Dans cet article, nous allons ajouter des analyses et le suivi de l'utilisation à l'application que nous avons construite dans les articles précédents.

### Configuration du Backend Analytics

Dans de nombreuses applications, il est nécessaire de capturer les données d'utilisation de l'application afin que l'entreprise puisse obtenir des informations sur la manière dont les clients interagissent avec l'application. Nous allons utiliser Amazon Pinpoint pour suivre les métriques d'utilisation de notre application React. Amazon Pinpoint dispose des types d'événements suivants :

1. Événements de monétisation. Ce type d'événement est utilisé pour signaler les revenus générés par votre application et le nombre d'articles achetés par les utilisateurs.
2. Événements de session. Ils suivent l'utilisation et indiquent quand et à quelle fréquence les utilisateurs ouvrent et ferment votre application.
3. Événements d'authentification. Cela montre à quelle fréquence les utilisateurs s'authentifient avec votre application. Les connexions, les inscriptions et les échecs d'authentification sont suivis dans cette catégorie.
4. Événements personnalisés. Ce type d'événements représente des événements non standard que vous définissez en attribuant un type d'événement personnalisé. Vous pouvez ajouter des attributs et des métriques personnalisés à un événement personnalisé.

Pour ajouter Pinpoint à notre projet, ouvrez la commande à la racine de votre projet React et suivez les instructions ci-dessous.

1. Exécutez la commande `amplify add analytics`.
2. Vous serez invité à entrer un nom de ressource pour ce service. Entrez `todosPinpoint` et appuyez sur la touche Entrée.
3. Vous devriez obtenir une invite vous demandant si vous souhaitez permettre aux utilisateurs non authentifiés d'envoyer des événements analytiques. Entrez `n` et appuyez sur Entrée.

![Image](https://cdn-media-1.freecodecamp.org/images/QCKxsBY5IL8paEUjhTclr8RAp-SEAoQXSzJF)

La commande que nous avons exécutée a créé la ressource d'analyse et mis à jour la ressource d'authentification localement. Nous devons les provisionner dans le cloud. Exécutez la commande `amplify push` pour créer le service dans le cloud. Une fois terminé, il récupère les informations de service et met à jour **src/aws-exports.js**. Si vous l'ouvrez, vous trouverez les propriétés `aws_mobile_analytics_app_id` et `aws_mobile_analytics_app_region`. Ces informations seront utilisées pour configurer la bibliothèque Amplify.

### Ajout d'Analytics à l'Application

Avec le service Pinpoint créé dans le cloud, nous devons maintenant ajouter du code pour envoyer des données d'utilisation. Dans **src/App.js**, la ligne 7, qui lit `Amplify.configure(aws_exports);` configurera la bibliothèque avec les données de **aws-export.js**. Puisque **aws-export.js** contient `aws_mobile_analytics_app_id`, il configurera également les analyses ainsi que d'autres services dont les informations s'y trouvent.

Par défaut, la bibliothèque Amplify suivra les événements de session utilisateur et d'authentification. Pas besoin d'ajouter du code supplémentaire. Si vous démarrez l'application, connectez-vous ou inscrivez des utilisateurs, vous obtiendrez ces données d'événements envoyées au cloud.

Nous pouvons également enregistrer des événements personnalisés. Enregistrons un événement personnalisé lorsque qu'un élément est supprimé. Ouvrez **src/App.js** et mettez à jour la ligne 4 pour importer le module Analytics :

```
import Amplify, { API, Analytics } from "aws-amplify";
```

Mettez à jour la fonction `delete()` pour inclure l'instruction de code suivante :

```
Analytics.record({ name: "delete", attributes: { id } });
```

Cela enverra un événement `delete` chaque fois que cette fonction est appelée. Cela pourrait être utilisé pour suivre la fréquence à laquelle les éléments sont supprimés. Nous pourrions également suivre les éléments les plus consultés en enregistrant un événement chaque fois que nous allons à la vue Détails. Ajoutez le code suivant à la fonction `loadDetailsPage()` :

```
Analytics.record({  name: "detailsView",  attributes: { title: response.title }});
```

Ouvrez l'application dans un navigateur et sélectionnez différents éléments pour passer par la vue détails des différents éléments que vous avez. Maintenant, connectez-vous à la console de gestion AWS et allez au tableau de bord Pinpoint pour voir le rapport d'analyse de l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/EdT-hx2IXyB-09GcKQ4hd8Ed3kqhWlV9WI-5)

### C'est tout

Vous pouvez intégrer Amazon Pinpoint dans vos applications web pour capturer les données d'utilisation afin de vous fournir des informations sur la manière dont les clients interagissent avec vos applications. Une entreprise peut utiliser ces données pour analyser le comportement des clients, y compris leur engagement, leurs données démographiques et leur activité d'achat.

Je vous ai montré comment créer un service Pinpoint en utilisant l'interface de ligne de commande Amplify, puis l'intégrer dans l'application React pour envoyer des événements personnalisés au service Pinpoint. Il y a plus que nous pouvons faire avec le module d'analyse dans la bibliothèque JavaScript Amplify, comme l'enregistrement automatique des vues de page et des événements. Consultez la [documentation](https://aws-amplify.github.io/docs/js/analytics) pour plus d'informations sur l'API Analytics.

### Lectures Complémentaires

1. [Partie 1 : Configuration de l'environnement de développement](https://medium.freecodecamp.org/going-serverless-with-react-and-aws-amplify-development-environment-set-up-9b15c3363bd)
2. [Partie 2 : Création et utilisation de services serverless](https://medium.freecodecamp.org/going-serverless-with-react-and-aws-amplify-part-2-creating-and-using-serverless-services-d401ba346eeb)

> _Également publié sur mon [blog](https://www.pmbanugo.me/)_