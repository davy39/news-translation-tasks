---
title: Création de commandes Slack serverless en quelques minutes avec Go & Up
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-11T00:39:48.000Z'
originalURL: https://freecodecamp.org/news/creating-serverless-slack-commands-in-minutes-with-up-f04ce0cfd52c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uFEp4Ubz5TOzlfo0-FE5Qw.png
tags:
- name: golang
  slug: golang
- name: Productivity
  slug: productivity
- name: serverless
  slug: serverless
- name: slack
  slug: slack
- name: Web Development
  slug: web-development
seo_title: Création de commandes Slack serverless en quelques minutes avec Go & Up
seo_desc: 'By TJ Holowaychuk

  This post walks through the creation of a serverless Slack command written in Golang,
  and deployed to AWS Lambda in seconds with Up.

  You’ll be creating a /time <url> command used to check how long a website takes
  to respond. Up uses...'
---

Par TJ Holowaychuk

Cet article explique la création d'une commande Slack serverless écrite en Golang, et déployée sur AWS Lambda en quelques secondes avec [Up](https://github.com/apex/up).

Vous allez créer une commande `/time <url>` utilisée pour vérifier le temps de réponse d'un site web. Up utilise votre propre compte AWS. Vous pouvez héberger un grand nombre d'applications personnalisées gratuitement tout en utilisant le niveau gratuit d'AWS (1 million de requêtes/m).

Consultez également les [instructions d'installation](https://up.docs.apex.sh/) si vous êtes nouveau sur Up.

### Enregistrement de la commande Slack

La première étape consiste à créer une application Slack, ce qui vous permet d'enregistrer des commandes, entre autres.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dE4mvNpvma_IM0UHxlC4qQ.png)

Une fois créée, cliquez sur « Slash commands » dans le menu de gauche et enregistrez la commande `/time`. Vous devrez garder cette page ouverte pendant un moment car nous avons besoin d'une **URL de requête** pour que Slack sache où envoyer les requêtes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9Ot1sxpiFdpxDYe4xZMOGg.png)

#### Création de la commande Slack

Dans le répertoire de votre projet, créez un fichier nommé `up.json`. Assurez-vous de remplacer `PROFILE` par le nom de votre profil AWS ([en savoir plus](https://apex.github.io/up/#aws_credentials)).

```
{  "name": "slack-cmd-test",  "profile": "PROFILE"}
```

Maintenant, nous avons besoin d'un petit serveur HTTP pour traiter la requête POST de la commande Slack. Créez un fichier `main.go` avec le serveur net/http suivant.

Déployez-le avec `up`.

> **NOTE** : Le premier déploiement peut prendre environ 60 secondes pour configurer les ressources.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QuKc-ue1qJuwg9xt-NOlqQ.png)

Maintenant, vous devez récupérer l'URL et la coller dans la page de la commande Slack pour que Slack sache où envoyer les requêtes. Copiez l'URL de la commande dans le presse-papiers en utilisant :

```
$ up url -cCopied to the clipboard!
```

Collez-la dans le champ **Request URL**, puis vous êtes prêt à effectuer un test :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ht5Cs6Wcfqezwk0ChfC84g.png)

Avec un peu de chance, vous verrez une réponse Hello World !

![Image](https://cdn-media-1.freecodecamp.org/images/1*fFywF9gQ3XNKRe-QYxRHLw.png)

#### Exécution de la requête

Slack envoie une requête POST avec des entrées de formulaire, également connue sous le nom de `application/x-www-form-urlencoded` (un type mime mal nommé, devenu quasi standard).

Pour accéder aux valeurs du formulaire, analysez le formulaire avec la méthode ParseForm(). Dans ce cas, tout ce dont nous avons besoin est le champ « text » de r.Form, le formulaire analysé.

Maintenant que la partie requête est complète, importez le package `time` et enveloppez la requête avec `time.Now()` et `time.Since()` pour enregistrer la durée de la requête.

Déployez à nouveau avec `up` et immédiatement après le déploiement, vous êtes prêt à tester la version réelle :

![Image](https://cdn-media-1.freecodecamp.org/images/1*WTFhC_dOxL3iqNTsQf6x3w.png)

Deux fichiers et quelques commandes plus tard, vous avez terminé ! Répétez pour autant de commandes Slack que nécessaire.

### Test local

L'un des points forts d'Up est le déploiement de serveurs HTTP traditionnels « vanilla ». Cela signifie qu'il n'y a rien de nouveau à apprendre lors des tests sur votre machine, développez l'application comme vous le feriez toujours.

Voici un exemple de cette application testée via `curl` :

```
$ PORT=3000 go run main.go$ curl -d 'text=https://apex.sh' http://localhost:3000/
```

```
https://apex.sh took 19.33542m
```

J'espère que cela a été utile ! Consultez la [documentation](https://apex.github.io/up/) pour plus d'aide, et suivez-moi sur [Twitter](https://twitter.com/tjholowaychuk) pour les mises à jour et divers rants logiciels.