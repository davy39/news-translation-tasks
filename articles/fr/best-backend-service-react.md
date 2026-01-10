---
title: Le meilleur Backend as a Service pour votre application React
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-11-29T22:56:39.000Z'
originalURL: https://freecodecamp.org/news/best-backend-service-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/mugshotbot.com_customize_color-pink-description-Create-a-culture-people-want-to-be-part-of-with-Gifcoins-3A-the-easy-to-use-peer-recognition-platform.-hide_watermark-0-image-2683d973-mode-light-pattern-bank_note-theme-two_up-title-Peer-to-p.png
tags:
- name: backend
  slug: backend
- name: React
  slug: react
seo_title: Le meilleur Backend as a Service pour votre application React
seo_desc: If you're building an app on your own or on a budget, you may want to consider
  using a backend-as-a-service (BaaS). Doing so allows you to focus on the frontend
  of your application, but still have a full-stack app with a database, authentication,
  and...
---

Si vous construisez une application seul ou avec un budget limité, vous pourriez envisager d'utiliser un backend-as-a-service (BaaS). Cela vous permet de vous concentrer sur le frontend de votre application, tout en ayant une application full-stack avec une base de données, une authentification, et plus encore. 

Dans ce guide, nous allons couvrir trois des meilleures options pour vous en tant que développeur React afin de lancer rapidement votre application en utilisant un backend-as-a-service, tout en économisant du temps, des efforts et des coûts. 

## Supabase

Pendant de nombreuses années, Firebase a dominé le domaine du backend-as-a-service. Cependant, au cours des dernières années, Supabase a émergé comme une excellente alternative. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-29-at-1.56.30-PM.png)
_Page d'accueil de Supabase_

Le principal avantage de Supabase est qu'il est **open-source**. En bref, Supabase vous permet de prendre votre code et de le déployer où vous le souhaitez. Vous pouvez construire votre application, la déployer sur les serveurs de Supabase, ou la déployer sur votre propre service d'hébergement plus tard. 

Le grand avantage de cela est qu'il vous aide à éviter le **vendor lock-in**. Le problème du vendor lock-in apparaît si vous vous retrouvez dans une situation où vous souhaitez migrer loin du service que vous utilisez. Par exemple, si les prix du service deviennent trop élevés ou si vous avez des problèmes fondamentaux avec l'utilisation du service. Le problème est que vous êtes "verrouillé" et il peut être très difficile d'aller ailleurs.

Comme vous le verrez avec les deux autres options de cette liste (Firebase et AWS Amplify), elles ont un certain degré de vendor lock-in. En bref, il n'est pas facile de migrer loin d'elles. 

Supabase, en revanche, vous donne la flexibilité d'héberger votre projet où vous le souhaitez sans un processus de migration difficile. 

Supabase vous offre une base de données Postgres et elle est compatible avec presque tous les frameworks React, y compris de nombreuses autres bibliothèques JavaScript non-React. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-29-at-12.44.58-PM.png)
_Bibliothèques JavaScript supportées par Supabase_

Pour commencer à utiliser Supabase avec votre application React, vous installerez le package npm `supabase-js`. 

Pour démarrer votre projet Supabase et créer votre base de données, vous vous connecterez à Supabase.com. Le niveau gratuit vous donnera toutes les fonctionnalités majeures dont vous avez besoin, y compris une base de données gratuite, ainsi qu'une authentification intégrée. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-29-at-12.47.11-PM.png)
_Authentification Supabase_

L'authentification Supabase inclut de nombreux fournisseurs sociaux majeurs comme Google et Facebook. 

Ils offrent également un stockage intégré qui vous permet de stocker tout type de fichier. Cette fonctionnalité serait essentielle si votre application propose des téléchargements de vidéos ou d'images.

Supabase prend également en charge les données en temps réel via WebSockets, une fonctionnalité que Firebase et AWS Amplify offrent également.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/supabase-storage-and-functions.jpg)
_Stockage et fonctions Supabase_

Supabase offre des fonctions edge, qui vous permettent d'écrire du code personnalisé qui interagit avec votre base de données. Ces fonctions edge peuvent être utiles si vous souhaitez écrire une logique personnalisée que les packages npm de Supabase ne supportent pas ou si vous souhaitez faire quelque chose sur le serveur, comme envoyer un email. 

Un domaine où Supabase a un avantage sur Firebase est leur fonctionnalité de **recherche en texte intégral**. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-29-at-12.51.11-PM.png)
_Recherche en texte intégral de Supabase_

Si vous souhaitez fournir une fonctionnalité de recherche à votre application basée sur ce qui est stocké dans votre base de données, c'est quelque chose que la base de données Cloud Firestore de Firebase ne fournit tout simplement pas.

Le plan gratuit de Supabase peut vous mener loin, mais si vous souhaitez des sauvegardes de base de données, ainsi que la possibilité de stocker des données supplémentaires, une base de données ou un stockage au-delà des limites gratuites, vous devrez passer à leur plan Pro (qui est de 25 $ par mois par projet). Contrairement à Firebase et AWS, il y a un grand saut dans les prix si vous voulez quelque chose de plus que ce que la limite gratuite offre. 

Cela dit, le niveau pro de Supabase est très généreux. Lorsque vous êtes prêt à lancer votre application dans le monde, il fournira pratiquement tout ce dont vous avez besoin pour un backend pour seulement 25 $ par mois.

## Firebase

Firebase ne peut pas être battu en termes de longévité et de ce qu'il offre. 

Firebase existe depuis 10 ans et offre le plus de produits parmi toutes les solutions de backend. 

C'est un service tout-en-un très sophistiqué, avec son propre stockage de base de données NoSQL, une authentification avec tous les types de fournisseurs sociaux imaginables, ainsi que certaines fonctionnalités que Supabase n'a pas, telles que l'analyse des plantages, des insights de performance, des tests A/B, des notifications push et bien plus encore. 

Si vous voulez vraiment l'option la plus complète, vous devriez sérieusement considérer Firebase. 

![Image](https://www.freecodecamp.org/news/content/images/2024/08/firebase-homepage.jpg)
_Page d'accueil et services de Firebase_

Firebase est tout aussi facile à configurer. Vous pouvez créer un compte et de nombreux projets gratuits sur le site de Firebase. 

Pour créer une base de données ou un stockage dédié, il suffit de cliquer sur un bouton. Firebase est tout aussi inégalé pour fournir un tableau de bord très pratique pour interagir avec tous vos produits individuels, tels que votre base de données. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-29-at-12.59.44-PM.png)
_Firebase Cloud Firestore_

Tous ces avantages de Firebase peuvent être un inconvénient potentiel. Firebase offre tellement qu'il peut être un peu accablant de déterminer ce que vous devriez utiliser et ce que vous ne devriez pas utiliser pour démarrer.

Ma recommandation pour votre application React est d'utiliser d'abord la base de données Cloud FireStore, l'authentification et le stockage, et d'ajouter le service de fonctions Firebase si vous devez fournir une logique personnalisée sur votre serveur. Ce n'est qu'alors que vous devrez examiner leurs autres options. 

Contrairement à Supabase, mais similaire à AWS Amplify, Firebase inclut un hébergement intégré. Il n'est pas nécessaire de chercher ailleurs pour un service d'hébergement ou une autre solution personnalisée.

Le vrai inconvénient de Firebase, comme je l'ai mentionné précédemment, est leur vendor lock-in. Une fois que vous avez construit votre application avec Firebase, il peut être assez difficile de migrer vers une autre plateforme. Cela dit, de nombreuses entreprises ont construit leur moyen de subsistance entier sur Firebase.

Le coût de l'utilisation de Firebase est un peu plus difficile à calculer. Heureusement, Firebase fournit une calculatrice pratique qui vous donnera une bien meilleure idée, basée sur l'utilisation des ressources de votre application. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-29-at-1.03.29-PM.png)
_Calculatrice de plan de Firebase_

Leur plan est généreux pour l'utilisateur gratuit et vous pouvez commencer à utiliser pratiquement tous les services gratuitement. Vous n'aurez à commencer à payer que lorsque vous dépasserez ces limites.

Firebase est le plus proche d'un service tout-en-un pour servir de backend à votre application. Si vous êtes déterminé à construire votre application rapidement, avec le moins de temps possible passé à choisir et à gérer des services, vous ne pouvez pas vous tromper avec Firebase.

## AWS Amplify

Le dernier concurrent est AWS Amplify, qui est souvent négligé, mais ne devrait pas l'être. 

AWS est notoirement difficile à naviguer à certains moments, mais AWS Amplify a été conçu comme une exception à cette règle. AWS Amplify ne fournit pas seulement une base de données impressionnante, un stockage, ainsi qu'une expérience en temps réel pour les développeurs JavaScript, mais il est livré avec une bibliothèque de composants, Amplify UI. 

![Image](https://www.freecodecamp.org/news/content/images/2024/08/aws-amplify.jpg)
_AWS Amplify et Amplify UI_

Par exemple, au lieu de devoir créer votre propre composant d'authentification, Amplify UI vous en fournit un prêt à l'emploi. 

En bref, AWS Amplify vous donne pratiquement tous les outils de Firebase, ainsi que des composants premium pré-faits qui sont déjà intégrés avec votre backend AWS. 

Un avantage supplémentaire de l'utilisation d'AWS Amplify par rapport à Firebase et Supabase est qu'il est probablement celui qui sera le moins coûteux globalement. 

Les prix d'AWS sont parmi les plus bas en matière d'entreprises d'infrastructure. Dans de nombreux cas, AWS vous offrira des crédits de démarrage si vous utilisez AWS pour la première fois. Si c'est le cas, le coût de votre application pourrait être presque nul. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-29-at-1.11.01-PM.png)
_Tarification d'Amplify_

Le grand inconvénient de l'utilisation d'AWS Amplify est qu'il repose sur GraphQL. Si vous n'êtes pas familier avec GraphQL, cela pourrait être un point bloquant pour vous. Il dispose d'une alternative REST API. L'option REST, cependant, n'est pas aussi riche en fonctionnalités et ne fournit pas les mêmes bonus, tels que les données en temps réel avec des abonnements.

Un autre inconvénient de l'utilisation d'AWS Amplify est que vous pouvez écrire des résolveurs personnalisés pour interagir avec votre base de données et d'autres services AWS, mais ils ne sont pas écrits en JavaScript. Au lieu de cela, la console Amplify utilise ce que l'on appelle le "Apache Velocity Template Language" ou VTL. Soyez conscient que l'écriture de code serveur personnalisé pourrait être assez difficile si vous devez écrire une logique métier personnalisée.

AWS Amplify offre une énorme gamme de services intégrés et vous permet de tirer parti de nombreux produits AWS, tels que DynamoDB, S3 et ElasticSearch. Il a été construit pour répondre à tous les besoins imaginables des développeurs que vous pourriez avoir. Il va même jusqu'à vous permettre de faire des choses comme la transcription audio-texte et les intégrations de réalité étendue (XR). 

Amplify vaut définitivement le coup d'œil si vous cherchez à trouver le service le plus rentable qui ne sacrifie aucune des fonctionnalités de Firebase. Amplify est également un bon choix si vous êtes à l'aise avec GraphQL et connaissez bien l'écosystème AWS.

## Merci d'avoir lu !

Espérons que vous êtes maintenant bien équipé pour choisir le meilleur outil de backend as a service pour votre projet React.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre tout seul.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*