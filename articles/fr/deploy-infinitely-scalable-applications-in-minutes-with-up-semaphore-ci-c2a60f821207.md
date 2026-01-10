---
title: Comment déployer des applications infiniment évolutives sur AWS en quelques
  minutes avec Up & Semaphore CI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-04T20:29:43.000Z'
originalURL: https://freecodecamp.org/news/deploy-infinitely-scalable-applications-in-minutes-with-up-semaphore-ci-c2a60f821207
coverImage: https://cdn-media-1.freecodecamp.org/images/1*giDY-7KKIxxiVMdXh_fIpg.jpeg
tags:
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment déployer des applications infiniment évolutives sur AWS en quelques
  minutes avec Up & Semaphore CI
seo_desc: 'By TJ Holowaychuk

  Many Apex Up users have been asking about integration with continuous integration
  platforms, this post walks through staging and deploying Up to production using
  Semaphore CI.

  Serverless Up applications typically deploy in a few sec...'
---

Par TJ Holowaychuk

De nombreux utilisateurs d'[Apex Up](https://github.com/apex/up) ont demandé une intégration avec des plateformes d'intégration continue. Cet article explique comment mettre en scène et déployer Up en production en utilisant [Semaphore CI](https://semaphoreci.com/).

Les applications serverless Up se déployent généralement en quelques secondes depuis un ordinateur portable. Cependant, avec une connexion réseau médiocre, vous pourriez envisager d'utiliser un CI, non seulement pour améliorer le flux de travail et les tests, mais aussi pour bénéficier d'une vitesse de téléchargement accrue.

Semaphore est mon CI de choix — il a un design épuré, vous permet de chiffrer facilement les variables d'environnement, de planifier des builds temporisés et ne vous oblige pas à encombrer vos dépôts avec des fichiers de configuration. Cela dit, tant que vous pouvez définir des variables d'environnement, vous pouvez choisir la plateforme CI que vous préférez.

### L'Application

Pour cet exemple, nous allons déployer une application Node.js minimale avec [Koa](http://koajs.com/). Créez un nouveau dépôt dans votre GitHub et ajoutez `app.js` avec le code suivant :

```
const Koa = require('koa')
const app = new Koa
const { PORT = 3000 } = process.env
```

```
app.use(function *() {
  this.body = "Hello\n"
})
```

```
app.listen(PORT)
```

Vous pouvez ajouter les dépendances via npm ou yarn, selon votre préférence. Déployez l'application sur AWS et admirez ce magnifique "Hello" :

```
$ up
$ curl `up url`
Hello
```

Maintenant, configurons le CI.

### Installation

Pour commencer avec Semaphore, vous devez d'abord créer un nouveau projet :

![Image](https://cdn-media-1.freecodecamp.org/images/AAlXwpQb3HFUWlplzxX9nujLZij7j-R19ofd)

Puis trouvez le dépôt que vous avez créé précédemment dans GitHub :

![Image](https://cdn-media-1.freecodecamp.org/images/DTOBiQIoSHp8dH0UBYuSX9nsljsAjFw1Gm0T)

Passons maintenant à la partie intéressante — la configuration du build !

### Configuration des Jobs

L'une des choses que j'apprécie vraiment chez Semaphore, c'est que vous n'avez pas besoin d'utiliser des fichiers de configuration dans votre dépôt. Il suffit de définir les jobs et les commandes nécessaires dans l'interface utilisateur. Si votre cas d'utilisation le permet, vous pouvez même exécuter des jobs en parallèle pour accélérer les choses.

Le job "Installation" installera les packages NPM pour l'application, ajustera le propriétaire de `/usr/local/bin` puisque c'est là que Up sera installé par défaut, puis installera enfin Up lui-même. Up est distribué sous forme de binaires, donc ce processus ne prend que quelques secondes.

```
npm install
sudo chown -R $(whoami) /usr/local/bin
curl -f https://up.apex.sh/install | sh
```

Vous pouvez définir et réorganiser les commandes. Cependant, si vous cliquez sur "Modifier le Job", vous pouvez copier-coller les commandes ci-dessus sous forme de texte. Le deuxième job dans ce cas est utilisé pour déployer en développement (`up`).

![Image](https://cdn-media-1.freecodecamp.org/images/w-gqSlUmkoNDXHmFsqDkrcsUd81ns0hlwi7F)

Dans les scénarios où vous rencontrez des problèmes de permissions lors de l'installation dans /usr/local/bin, ou si vous préférez simplement éviter cela, vous pouvez fournir un chemin d'installation avec `BINDIR` :

```
curl -sf https://up.apex.sh/install | BINDIR=. sh
```

Notez que si vous exécutez Node.js avec Up, vous voudrez spécifier **6.10.3**, car c'est la version "native" de Node.js supportée par [AWS Lambda](https://aws.amazon.com/lambda/).

### Configuration de vos identifiants AWS

Après avoir configuré les jobs, il suffit de sélectionner votre branche et de cliquer sur "Start".

![Image](https://cdn-media-1.freecodecamp.org/images/Ch9LA9g3ZBQCPOLkmCfb4nwF8q5eUaMvDgGd)

La première chose que vous verrez, c'est que `up` échoue ! Cela est dû au fait que nous n'avons pas fourni d'identifiants AWS, donc Up ne sait pas où déployer et n'est pas autorisé à le faire.

![Image](https://cdn-media-1.freecodecamp.org/images/XhKBFTrr-KTwbMxabpG-y0odBYHnoSVpu1JF)

Si vous allez dans l'onglet "Variables d'Environnement" dans la barre latérale, vous pouvez ajouter des variables d'environnement en texte brut ou chiffrées. Vous aurez besoin de deux variables, `AWS_ACCESS_KEY_ID` et `AWS_SECRET_KEY_ID`. La première peut être en texte brut, mais la seconde doit être chiffrée. En cas de doute, chiffrez simplement.

![Image](https://cdn-media-1.freecodecamp.org/images/B56aGYdcVJtL3IFIJW3ibFmdRfX2VoPV7l8b)

Maintenant, lorsque vous effectuez un nouveau build, vous devriez avoir un pipeline CI réussi !

![Image](https://cdn-media-1.freecodecamp.org/images/8oeJIvWWzvjbVS9uhqHTNIQfzOnvaZzWxfAO)

> Vous pouvez en savoir plus sur les options pour les identifiants AWS dans la [documentation Up](http://up.docs.apex.sh/#aws_credentials). Assurez-vous également de ne jamais utiliser vos identifiants root dans des services externes tels que le CI.

### Déploiement en Production avec Up Pro

La [version Pro de Up](https://github.com/apex/up#pro-features) est en accès anticipé — seulement 10 $/mois avec une réduction pour une utilisation illimitée dans votre organisation — offrant des variables d'environnement chiffrées, des alertes et bien plus encore !

Après [vous être abonné à Up Pro](http://up.docs.apex.sh/#guides.subscribing_to_up_pro), vous devrez vous authentifier afin d'installer le binaire Pro. Exécutez la commande suivante pour copier les identifiants dans votre presse-papiers.

```
$ up team ci --copy
```

Ajoutez une nouvelle variable d'environnement chiffrée nommée `UP_CONFIG` :

![Image](https://cdn-media-1.freecodecamp.org/images/MCi78yihSturQkKdPCg1vu5s5kd6efUo3qrg)

Ensuite, vous devrez ajouter `up upgrade` après l'installation de Up. Cela installera la version Pro, car elle détecte `UP_CONFIG`. Notez que le job "Deploy" a été modifié pour déployer en production plutôt qu'en développement. Changer cette commande vous permet de mapper les branches GIT aux différentes étapes, afin que vous puissiez utiliser le CI pour pousser en développement, en staging ou en production.

Notez que vous pouvez mettre à niveau vers une version spécifique de Up via `up upgrade -t 0.5.4` pour "verrouiller" la version.

![Image](https://cdn-media-1.freecodecamp.org/images/w-oaM4NS85gdr2iv8btyob96EJYxrtuHD5Rg)

Essayez de changer la chaîne "Hello\n" dans app.js en "Hello from Semaphore CI\n" et poussez le commit sur GitHub.

```
app.use(function *() {
  this.body = "Hello from Semaphore CI\n"
})
```

En une minute ou moins, vous devriez voir le beau vert feuillu du succès ! Il n'y a pas de build distant côté AWS, une fois que c'est vert, votre application est en ligne et sert des requêtes, en moins d'une minute.

![Image](https://cdn-media-1.freecodecamp.org/images/-uMNtZ7IC5fxZst3PNXqbGjG5rfERr3ZpGG8)

Si le déploiement d'applications, d'API et de sites sur votre propre compte AWS en une seule commande vous semble utile, jetez un coup d'œil à [Apex Up](https://github.com/apex/up) — et découvrez [Semaphore CI](https://semaphoreci.com/) pour créer des workflows d'intégration continue à l'échelle de l'organisation.

**ÉDIT** : Notez qu'avec les versions récentes de Up, vous pouvez également mettre à niveau le binaire en place, afin d'éviter les problèmes de permissions ou les changements dans `/usr/local/bin`, et optionnellement passer une version spécifique pour "verrouiller" la version d'**Up Pro** via `-t x.x.x`

```
curl -f https://up.apex.sh/install | BINDIR=. sh
./up upgrade -t 0.5.8
./up production
```

J'ai contacté Semaphore CI et ils ont offert de fournir une réduction de 30 % pour les trois premiers mois aux utilisateurs de Up, en utilisant le coupon "**SEMAPHORE330**". Notez qu'il est valable jusqu'au 31 décembre.