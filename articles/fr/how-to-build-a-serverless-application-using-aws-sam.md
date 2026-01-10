---
title: Comment créer une application serverless en utilisant AWS SAM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-19T21:34:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-serverless-application-using-aws-sam
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/aws-sam.png
tags:
- name: AWS
  slug: aws
- name: Java
  slug: java
- name: serverless
  slug: serverless
seo_title: Comment créer une application serverless en utilisant AWS SAM
seo_desc: 'By Siben Nayak

  In my previous article, I talked about how AWS Chalice helps you quickly build a
  Python-based serverless application and deploy it on AWS within a few minutes.

  While it was a quick and fun prototype, Python may not be the language of c...'
---

Par Siben Nayak

Dans mon [article précédent](https://www.freecodecamp.org/news/how-to-build-a-serverless-application-using-aws-chalice/), j'ai parlé de la manière dont AWS Chalice vous aide à créer rapidement une application serverless basée sur Python et à la déployer sur AWS en quelques minutes.

Bien que ce soit un prototype rapide et amusant, Python peut ne pas être le langage de choix pour beaucoup lorsqu'il s'agit d'exécuter des applications de production à grande échelle.

De nombreuses organisations utilisent Java comme langage de développement principal, et beaucoup de développeurs se tournent également vers de nouveaux langages comme Go.

Dans cet article, je vais vous guider à travers les étapes nécessaires pour créer et déployer la même application serverless qui obtient les dernières nouvelles de Google News. Mais cette fois, nous utiliserons le modèle d'application serverless AWS (SAM) et Java pour notre développement.

Comme Chalice, l'interface de ligne de commande AWS SAM offre un ensemble riche d'outils qui permettent aux développeurs de créer rapidement des applications serverless.

## Prérequis

Ce tutoriel nécessite un compte AWS. Si vous n'en avez pas déjà un, allez-y et [créez-en un](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/). Notre application va utiliser uniquement les ressources de la couche gratuite, donc le coût ne devrait pas être un problème.

Vous devez également configurer la sécurité et créer des utilisateurs et des rôles pour votre accès.

## Comment configurer les identifiants AWS

SAM utilise l'interface de ligne de commande AWS (CLI) en arrière-plan pour déployer le projet. Si vous n'avez pas utilisé la CLI d'AWS auparavant pour travailler avec les ressources AWS, vous pouvez l'installer en suivant les directives [ici](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).

Une fois installé, vous devez [configurer](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) votre CLI AWS pour utiliser les identifiants de votre compte AWS.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-49.png)

## Comment installer SAM

Ensuite, vous devez installer SAM. Nous utiliserons Java dans ce tutoriel, mais vous pouvez utiliser n'importe quel runtime de langage supporté par AWS Lambda.

### Vérifier l'installation de Java

```
$ java --version

openjdk 11.0.8 2020-07-14
OpenJDK Runtime Environment AdoptOpenJDK (build 11.0.8+10)
OpenJDK 64-Bit Server VM AdoptOpenJDK (build 11.0.8+10, mixed mode)
```

### Installer SAM CLI

Selon votre système d'exploitation, les instructions d'installation pour le SAM CLI varieront. Cet article couvre les instructions pour l'installer sur MacOS.

L'approche recommandée pour installer le SAM CLI sur macOS est d'utiliser le gestionnaire de paquets Homebrew.

Vérifiez que vous avez Homebrew installé, comme ceci :

```
$ brew --version

Homebrew/homebrew-core (git revision fe68a; last commit 2020-10-15)
Homebrew/homebrew-cask (git revision 4a2c25; last commit 2020-10-15)
```

Si ce n'est pas le cas, vous pouvez installer Homebrew en utilisant la commande suivante :

```
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

Ensuite, installez SAM en utilisant la commande suivante :

```
brew tap aws/tap
brew install aws-sam-cli
```

### Vérifier l'installation de SAM

```
$ sam --version

SAM CLI, version 1.6.2
```

## Comment créer un projet

Ensuite, exécutez la commande `sam init` pour créer un nouveau projet.

```
sam init -r java11 -d maven --app-template hello-world -n daily-news-java
```

Par défaut, SAM crée un projet Python. Puisque nous voulons créer un projet Java, nous devrons passer quelques paramètres supplémentaires.

**Paramètres :**

* `-r java11` : utiliser le runtime Java 11
* `-d maven` : utiliser Maven comme gestionnaire de dépendances
* `--app-template hello-world` : utiliser le modèle de démarrage rapide HelloWorld
* `-n daily-news-java` : le nom de notre projet

Cela créera un dossier `daily-news-java` dans votre répertoire actuel. Vous pouvez voir que SAM a créé plusieurs fichiers dans ce dossier.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/sam-ls-la.png)

Examinons le fichier `App.java`.

<script src="https://gist.github.com/theawesomenayak/29b3a5283293880b6910a10854a94cd1.js"></script>

La commande `sam init` a créé une simple fonction Lambda qui retourne le corps JSON `{"message": "hello world"}` et l'adresse IP de la machine lorsqu'elle est appelée. Nous pouvons maintenant modifier ce modèle et ajouter plus de code pour lire les nouvelles de Google.

Examinons maintenant le fichier `template.yml`.

<script src="https://gist.github.com/theawesomenayak/dbbde0bbddb166950735cd5782943373.js"></script>

Celui-ci contient le modèle CloudFormation qui crée notre Amazon API Gateway et les ressources AWS Lambda.

La configuration Lambda spécifie que nous avons une lambda `HelloWorldFunction` qui s'exécute sur `Java 11` et `512 Mo` de mémoire.

La configuration de l'API Gateway définit une seule méthode `GET` avec un chemin `/hello` que nous utiliserons pour invoquer l'API.

Nous utiliserons les bibliothèques internes HTTP et d'analyse XML de Java, donc nous n'avons pas besoin d'ajouter de dépendances à notre fichier `pom.xml`.

Notez que le fichier `pom.xml` par défaut fourni dans le code boilerplate vient avec le source du compilateur défini sur `1.8`. Nous devrons le mettre à jour à `11` afin de pouvoir utiliser la nouvelle bibliothèque HTTP qui fait partie de Java 11.

<script src="https://gist.github.com/theawesomenayak/c5ab30dc3ada4654d9a7da45eb07c53a.js"></script>

Puisque Java est orienté objet, créons également une classe `NewsItem` qui contient le titre et la date de publication d'un article de presse.

<script src="https://gist.github.com/theawesomenayak/8b7e73c5a0c3dc6787cb1ec4505f84cf.js"></script>

Notez que nous avons remplacé la méthode `toString`. Cela crée une représentation JSON de l'objet et évite d'utiliser des bibliothèques d'analyse JSON.

Ensuite, vous devez ajouter une méthode pour récupérer le flux RSS de Google, l'analyser pour extraire le titre des nouvelles et la date de publication, et créer une liste d'articles de presse. Pour ce faire, ajoutez le code suivant à votre `App.java` :

<script src="https://gist.github.com/theawesomenayak/ad384538704b43013ce2acaa74716dcf.js"></script>

Maintenant, mettons à jour la méthode `handleRequest` dans `App.java` pour invoquer cette méthode et retourner la liste des articles de presse comme résultat.

<script src="https://gist.github.com/theawesomenayak/0c069910f066e7544d6e2c8419edcf5f.js"></script>

N'oubliez pas de mettre à jour les tests unitaires également. Ils ont été écrits pour tester la présence de "hello world" dans la réponse et commenceront à échouer après notre modification.

<script src="https://gist.github.com/theawesomenayak/d2a0dd78b9edf309cada547627e927b6.js"></script>

## Comment démarrer la construction

Depuis le dossier `daily-news-java`, exécutez la commande `sam build`.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/sam-build.png)

Cela compile votre code source et construit toutes les dépendances que vous avez dans l'application. Il déplace ensuite tous les fichiers dans le dossier `.aws-sam/build` afin qu'ils soient prêts à être emballés et déployés. Il met également à jour le fichier `template.yml` en conséquence.

## Comment tester votre application localement

Voici la belle partie à propos de SAM. Vous pouvez déployer et tester votre application localement ! Cela est vraiment utile pendant la phase de développement lorsque vous voulez tester votre code sans avoir à le déployer sur AWS.

L'interface de ligne de commande SAM fournit la commande `sam local` pour exécuter votre application localement. Cela utilise en interne Docker pour simuler l'environnement d'exécution de Lambda. Si vous n'avez pas Docker installé, vous pouvez l'obtenir [ici](https://docs.docker.com/get-docker/).

Nous pouvons tester localement notre application de deux manières :

* Héberger l'API localement
* Invoquer directement la fonction Lambda

Examinons ces deux options.

### Hébergement local

Utilisez la commande suivante pour démarrer l'API localement :

```
sam local start-api
```

Cela crée en interne un serveur local et expose un point de terminaison local qui réplique votre API REST.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/sam-local.png)

Une fois le conteneur Docker chargé, vous pouvez accéder à l'API sur `localhost`, comme ceci :

```
curl http://127.0.0.1:3000/hello
```

### Invocation directe

Utilisez la commande suivante pour invoquer la fonction Lambda :

```
sam local invoke "HelloWorldFunction" -e events/event.json
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/sam-invoke.png)

Cela invoque directement la fonction Lambda (comme nous appellerions la méthode `main`) et passe le fichier `event.json` comme charge utile.

## Comment déployer le projet

Déployons l'application. Depuis le dossier `daily-news-java`, exécutez la commande `sam deploy --guided`. Suivez les invites et fournissez les entrées requises (ou appuyez simplement sur Entrée pour accepter les valeurs par défaut).

![Image](https://www.freecodecamp.org/news/content/images/2020/10/sam-deploy.png)

Cela déploie notre application sur AWS en utilisant Amazon API Gateway et AWS Lambda. Il prend les artefacts de déploiement que nous avons construits avec la commande `sam build`, les emballe et les télécharge dans un bucket Amazon S3 créé par l'interface de ligne de commande AWS SAM, et déploie l'application en utilisant AWS CloudFormation.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/sam-cfn.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2020-10-19-at-1.03.01-AM.png)
_API daily-news dans API Gateway_

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2020-10-19-at-1.02.48-AM.png)
_Fonction Lambda daily-news_

Nous pouvons maintenant essayer d'accéder à l'API en utilisant l'URL du point de terminaison fournie ci-dessus.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/sam-curl.png)

## Comment nettoyer les ressources

Nous pouvons utiliser la commande `aws cloudformation delete-stack` pour supprimer la pile AWS CloudFormation ainsi que toutes les ressources qu'elle a créées lorsque nous avons exécuté la commande `sam deploy`.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/sam-delete.png)

## Conclusion

Félicitations ! Vous venez de déployer une application serverless sur AWS en utilisant AWS SAM. Cela a impliqué un peu plus de travail que [précédemment](https://www.freecodecamp.org/news/how-to-build-a-serverless-application-using-aws-chalice/), mais ce n'était pas trop difficile non plus.

Vous pouvez maintenant apporter des modifications à votre fichier `App.java` et réexécuter `sam deploy` pour redéployer vos changements.

Le code source complet de ce tutoriel peut être trouvé [ici](https://github.com/theawesomenayak/daily-news-java).

Merci de m'avoir suivi jusqu'ici. J'espère que vous avez aimé l'article. Vous pouvez me contacter sur [LinkedIn](https://www.linkedin.com/in/theawesomenayak/) où je discute régulièrement de technologie et de vie. Jetez également un coup d'œil à certains de mes autres articles sur [Medium](https://medium.com/@theawesomenayak).

Bonne lecture 📖