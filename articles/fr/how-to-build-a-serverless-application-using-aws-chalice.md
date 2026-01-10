---
title: Comment créer une application serverless avec AWS Chalice
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-14T21:50:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-serverless-application-using-aws-chalice
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/cloud-computing--1--1.png
tags:
- name: AWS
  slug: aws
- name: Python
  slug: python
- name: serverless
  slug: serverless
seo_title: Comment créer une application serverless avec AWS Chalice
seo_desc: "By Siben Nayak\nI recently came across AWS Chalice and was fascinated by\
  \ the simplicity and usability it offers. \nAWS Chalice is a serverless framework\
  \ that allows you to build serverless applications using Python, and deploy them\
  \ on AWS using Amazon ..."
---

Par Siben Nayak

J'ai récemment découvert AWS Chalice et j'ai été fasciné par la simplicité et la facilité d'utilisation qu'il offre. 

AWS Chalice est un framework serverless qui permet de créer des applications serverless en utilisant Python, et de les déployer sur AWS en utilisant Amazon API Gateway et AWS Lambda.

J'ai décidé de m'amuser avec et j'ai effectivement pu créer et déployer une API REST d'exemple sur AWS en quelques minutes. 

Dans cet article, je vais vous guider à travers les étapes nécessaires pour construire et déployer une application serverless qui récupère les dernières nouvelles de Google News en utilisant Chalice.

## Prérequis

Ce tutoriel nécessite un compte AWS. Si vous n'en avez pas déjà un, allez-y et [créez-en un](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/). Notre application va utiliser uniquement les ressources de la couche gratuite, donc le coût ne devrait pas être un problème. 

Vous devez également configurer la sécurité et créer des utilisateurs et des rôles pour votre accès.

## Comment configurer les identifiants AWS

Chalice utilise l'interface de ligne de commande AWS (CLI) en arrière-plan pour déployer le projet. Si vous n'avez pas utilisé la CLI d'AWS auparavant pour travailler avec les ressources AWS, vous pouvez l'installer en suivant les directives [ici](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).

Une fois installé, vous devez [configurer](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) votre CLI AWS pour utiliser les identifiants de votre compte AWS. 

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-31.png)

## Comment installer Chalice

Ensuite, vous devez installer Chalice. Nous allons utiliser Python 3 dans ce tutoriel, mais vous pouvez utiliser n'importe quelle version de Python supportée par AWS Lambda.

### Vérifier l'installation de Python

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-32.png)

### Installer Chalice

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-33.png)

### Vérifier l'installation de Chalice

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-34.png)

## Comment créer un projet

Ensuite, exécutez la commande `chalice new-project` pour créer un nouveau projet.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-35.png)

Cela créera un dossier `daily-news` dans votre répertoire actuel. Vous pouvez voir que Chalice a créé plusieurs fichiers dans ce dossier. Nous allons travailler uniquement avec les fichiers `app.py` et `requirements.txt` dans cet article.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-37.png)

Examinons le contenu du fichier `app.py` :

<script src="https://gist.github.com/theawesomenayak/20986881b7ca3c6e9b48a1ec7ce66d2c.js"></script>

La commande `new-project` a créé une application d'exemple `daily-news`. Elle définit une seule vue `/`, qui retourne le corps JSON `{"hello": "world"}` lorsqu'elle est appelée. Vous pouvez maintenant modifier ce modèle et ajouter plus de code pour lire les nouvelles de Google.

Nous allons utiliser le flux RSS de Google pour obtenir nos nouvelles. Comme les flux RSS consistent en des données au format XML, nous aurons besoin d'une bibliothèque Python appelée Beautiful Soup pour analyser les données XML. 

Vous pouvez installer Beautiful Soup et sa bibliothèque d'analyse XML en utilisant `pip`, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-36.png)

Ensuite, ajoutez les imports suivants à `app.py`. Cela ajoute essentiellement des imports de `urllib` pour faire des appels HTTP et de `bs4` pour analyser le XML.

<script src="https://gist.github.com/theawesomenayak/1370454bb17aa7c052af901f73010813.js"></script>

Ensuite, vous devez ajouter une méthode pour récupérer le flux RSS de Google. Nous allons utiliser `urllib` pour faire un appel HTTP à l'endpoint RSS de Google et obtenir la réponse. Vous pouvez ensuite analyser la réponse pour extraire le titre de la nouvelle et la date de publication, et créer une liste d'éléments de nouvelles. 

Pour ce faire, ajoutez le code suivant à votre `app.py` :

<script src="https://gist.github.com/theawesomenayak/a9a5c9c3b812c3a7f96651dd67b240c8.js"></script>

Mettez à jour la méthode index dans `app.py` pour invoquer cette méthode et retourner la liste des éléments de nouvelles comme résultat.

<script src="https://gist.github.com/theawesomenayak/195fff0f32991521ef0c7e34a23a4b47.js"></script>

Notez que vous avez installé quelques dépendances pour faire fonctionner le code. Ces dépendances ont été installées localement et ne seront pas disponibles pour le conteneur AWS Lambda à l'exécution. 

Pour les rendre disponibles pour AWS Lambda, vous devrez les empaqueter avec votre code. 

Pour cela, ajoutez ce qui suit au fichier `requirements.txt`. Chalice empaquette ces dépendances dans le cadre de votre code lors de la construction et les télécharge dans le cadre de la fonction Lambda.

<script src="https://gist.github.com/theawesomenayak/570c0eca944ef5eb23c5b4d40b7a80ca.js"></script>

## Comment déployer le projet

Déployons cette application. Depuis le dossier `daily-news`, exécutez la commande `chalice deploy`.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-38.png)

Cela déploie votre API sur Amazon API Gateway et crée une nouvelle fonction sur AWS Lambda.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2020-10-11-at-12.51.29-PM.png)
_API daily-news_

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2020-10-11-at-12.59.13-PM.png)
_Fonction Lambda daily-news-dev_

Essayons maintenant d'accéder à l'API. Vous pouvez utiliser `curl` pour invoquer l'URL de l'API Gateway que vous avez reçue lors de `chalice deploy`. La réponse de l'appel API retournera une liste d'éléments de nouvelles comme montré ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-41.png)

## Comment nettoyer les ressources

Vous pouvez également utiliser la commande `chalice delete` pour supprimer toutes les ressources créées lorsque vous avez exécuté la commande `chalice deploy`.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-42.png)

## Conclusion

Félicitations ! Vous venez de déployer une application serverless sur AWS en utilisant Chalice. Ce n'était pas trop difficile, n'est-ce pas ?

Vous pouvez maintenant apporter des modifications à votre fichier `app.py` et relancer `chalice deploy` pour redéployer vos changements.

Vous pouvez également utiliser Chalice pour intégrer votre application serverless avec Amazon S3, Amazon SNS, Amazon SQS et d'autres services AWS. Consultez les [tutoriels](https://aws.github.io/chalice/tutorials/index.html) et continuez à explorer. Le code source complet de ce tutoriel peut être trouvé [ici](https://github.com/theawesomenayak/daily-news).

Merci de m'avoir suivi jusqu'ici. J'espère que vous avez aimé l'article. Vous pouvez me contacter sur [LinkedIn](https://www.linkedin.com/in/theawesomenayak/) où je discute régulièrement de technologie et de vie. Consultez également certains de mes autres articles sur [Medium](https://medium.com/@theawesomenayak). Bonne lecture ?