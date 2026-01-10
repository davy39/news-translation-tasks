---
title: Comment configurer une application Ember.js de base
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-09T13:06:53.000Z'
originalURL: https://freecodecamp.org/news/setting-up-a-basic-ember-js-app-c9323760c675
coverImage: https://cdn-media-1.freecodecamp.org/images/1*--wRIhx_atl50C4NlkMY5Q.jpeg
tags:
- name: coding
  slug: coding
- name: ember
  slug: ember
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Comment configurer une application Ember.js de base
seo_desc: 'By Tracy Lee | ladyleet

  So, you want to test out Ember, eh? This article will walk through building a basic
  app.

  Here’s what we’ll do:


  Set up ember-cli

  Create a new application

  Use materalize-css for styling

  Create components

  Cover basic use of Embe...'
---

Par Tracy Lee | ladyleet

Alors, vous voulez tester Ember, hein ? Cet article vous guidera à travers la création d'une application de base.

Voici ce que nous allons faire :

1. Configurer ember-cli
2. Créer une nouvelle application
3. Utiliser materialize-css pour le style
4. Créer des composants
5. Couvrir l'utilisation de base du routeur d'Ember
6. Explorer l'aide "each" pour itérer sur les données

D'abord, vous devriez installer ember-cli. Presque toutes les applications sont construites avec ember-cli. Il est très rare que vous en trouviez une qui ne l'est pas.

Et voici un avantage majeur d'Ember et de la communauté Ember — ils s'appuient sur la convention plutôt que sur la configuration plus lourdement qu'Angular et React. Ils utilisent cela comme l'une de leurs forces, ce qui en fait un framework populaire pour les entreprises qui veulent construire des applications à grande échelle.

Être conventionnel permet à Ember de développer des normes communautaires telles que l'histoire de ember-cli-deploy, une forte histoire autour d'Ember Data, et les nombreuses contributions que la communauté est en mesure de faire grâce à l'écosystème des addons ember. (consultez [emberaddons.com](http://emberaddons.com))

Sur le site Ember.js, vous trouverez des instructions d'installation simples, et même un petit guide de démarrage rapide que vous pouvez suivre !

Allez-y et installez ember-cli pour commencer :

```
$ npm install -g ember-cli
```

![Image](https://cdn-media-1.freecodecamp.org/images/uqa1TXkxiRmvCzpk7hKIiniHqBLG6iIlOidM)

### Créer une nouvelle application

C'est aussi simple que 1-2-3 ! Il suffit de faire _ember new <nom-du-projet>_ et une application sera générée pour vous.

```
ember new yolobrolo
```

Vous verrez ember-cli créer assez de fichiers.

Principalement, vous devriez noter qu'Ember a créé :

* application.hbs (handlebars, qui est votre fichier html)
* app.js
* router.js
* package.json
* bower.json
* tests

![Image](https://cdn-media-1.freecodecamp.org/images/u8W1gwGP09Zm9SswoeMYnPcym2cZePWx39XO)

Wahoo ! Maintenant, si vous ouvrez votre IDE, vous devriez voir la structure d'une application Ember.

![Image](https://cdn-media-1.freecodecamp.org/images/rSeUbwBASJqaUUNzMoTrTs28kxJhjAZk9tG7)

### Installer Materialize-CSS

Au cas où vous vous poseriez la question, j'adore le design matériel et materialize-css.

Donc, si vous voulez utiliser les styles que j'utilise habituellement, allez-y et exécutez la commande suivante.

```
npm install materialize-css
```

Ensuite, ajoutez ces lignes à votre fichier index.html

```
<!-- Compiled and minified CSS -->  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.7/css/materialize.min.css">
```

```
<!--Import Google Icon Font-->      <link href="http://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
```

```
<!-- Compiled and minified JavaScript -->  <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.7/js/materialize.min.js"></script>
```

Une fois terminé, arrêtez votre serveur et redémarrez-le. Votre police devrait changer pour Roboto :

![Image](https://cdn-media-1.freecodecamp.org/images/QKBS1fALwjuOdlEBzEprrNZ0Hpea5l9fzMUL)
_Avant d'installer materialize-css_

![Image](https://cdn-media-1.freecodecamp.org/images/ZeV8v2aKw-6kJDbt0f4rqBcOp8MI-HfdsrCt)
_Après avoir installé materialize-css_

### Créer des composants

Ember, comme la plupart des frameworks JavaScript de nos jours, adore les composants. Alors créons le composant dont nous avons besoin : une barre de navigation que nous pouvons connecter au routeur ! Nous utilisons la barre de navigation que materialize-css nous donne.

Tout ce que vous avez à faire pour créer un composant est ceci :

```
ember g component <nom-du-composant>
```

Assurez-vous que le nom de votre composant contient un tiret dans le nom car c'est la convention.

Voici les fichiers que ember-cli génère pour moi. Il crée :

* nom-du-composant.hbs
* nom-du-composant.js
* ajoute des tests d'intégration

![Image](https://cdn-media-1.freecodecamp.org/images/tVx23HTngPpZy6FbsA5sVClrDttak5F0hCDl)

Voici à quoi ressemble ma belle barre de navigation.

![Image](https://cdn-media-1.freecodecamp.org/images/ucWBKTzvkOz9s0-EDNfg4yKLYCa5gfyZej9a)

Voici le code par défaut si vous le souhaitez :

```
<nav>    <div class="nav-wrapper">      <a href="#" class="brand-logo center">Logo</a>      <ul id="nav-mobile" class="left hide-on-med-and-down">        <li><a href="#">Vidéos</a></li>        <li><a href="#">À propos</a></li>      </ul>    </div>  </nav>
```

À chaque fois que vous avez besoin de réutiliser un morceau de code encore et encore, il est toujours préférable d'en faire un composant. :)

### Utiliser le routeur d'Ember

Je pense que je prends le routeur d'Ember pour acquis après avoir tant joué avec Angular 2.

En fait, je pense que je prends les routeurs pour acquis en général, mais voici mon ami [Jay Phelps](http://twitter.com/_jayphelps) qui nous explique pourquoi nous devrions nous en soucier.

![Image](https://cdn-media-1.freecodecamp.org/images/Fehcpksz1hYRDLluNfc9KIiEkYV6AZRxe6Co)

Voici un aperçu de base du fonctionnement du routeur d'Ember.

Tout d'abord, vous devriez noter qu'il y a un fichier router.js dans lequel toutes vos routes sont définies. De plus, dans votre fichier application.hbs, il y a {{outlet}} qui sort ce que vous spécifiez au routeur.

Dans mon application, je veux créer 2 routes simples — une page à propos et une page vidéos.

Pour créer une nouvelle route, vous exécutez cette commande dans ember-cli.

```
ember g route <nom-de-la-route>
```

Ember générera alors :

* votre-route.js
* votre-route.hbs
* met à jour le fichier router.js
* crée un test unitaire.

Vous pouvez voir toute la magie depuis la ligne de commande :

![Image](https://cdn-media-1.freecodecamp.org/images/9znjBZrRbIzyM904Ipvuz-n4No7cVK5Vzx7M)

J'adore la façon dont le fichier router.js est automatiquement mis à jour pour moi. Vous pouvez même créer des routes imbriquées depuis la ligne de commande. Les guides Ember.js sont assez géniaux et voici un [lien](https://guides.emberjs.com/v2.7.0/routing/) vers tout ce que le routeur peut faire.

Une chose que j'ai faite dans la capture d'écran ci-dessous était de définir ma route par défaut. Je l'ai fait en spécifiant simplement le chemin de la route comme /. Tout le reste a été pré-généré pour moi avec le CLI.

```
this.route('videos', { path:'/' });
```

![Image](https://cdn-media-1.freecodecamp.org/images/Hunm2wpFTJLIrxai0zNs5fDobyVih1T3qnN-)

### Configurer la sortie du routeur d'Ember

Explorons le fichier application.hbs. C'est là que le routeur sortira.

Vraiment, une des seules choses que j'ajoute dans mon fichier application.hbs est une barre de navigation et un pied de page. Je crée des routes pour tout le reste.

Actuellement, mon fichier application.hbs ressemble à ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/tpeGX5M4bI9DMzh1CoIbMZgC6HB371LwsB3r)

Maintenant, en allant dans mon composant nav-bar, je vais faire fonctionner les routes pour la route de la page à propos et la route des vidéos.

Ember utilise l'aide {{link-to}} pour les transitions entre les routes.

Voici à quoi ressemble la syntaxe :

```
{{#link-to 'videos'}}Vidéos{{/link-to}}
```

L'aide {{link-to}} remplace une balise <a> et est la façon dont nous faisons la transition entre les routes dans Ember. Tout ce que vous avez à faire est de spécifier la route dans les parenthèses comme montré ci-dessus. Dans Angular 2, l'équivalent est le routerLink.

Voici une capture d'écran de toute ma barre de navigation.

![Image](https://cdn-media-1.freecodecamp.org/images/2tLmQelJpI7fPu4zx7kVk1h1c3hbxNFTFmkG)

Maintenant, vous savez comment utiliser la fonctionnalité de base du routeur !

### Itérer sur les données en utilisant l'aide Each

J'ai une route vidéo, et j'aimerais afficher un ensemble de vidéos YouTube sur la page. Je vais créer un simple composant video-card que je vais itérer et afficher sur la page vidéo.

Voici à quoi ressemble une carte vidéo :

![Image](https://cdn-media-1.freecodecamp.org/images/2zrsP51jykbjvWpM8p5MORF7zHch9vKUab8E)

Une partie de la beauté d'Ember est toutes les aides qui vous permettent de faire des choses cool dans votre application.

L'aide {{each}} d'Ember est équivalente à la directive ng-repeat dans Angular 1 et à la directive *ngFor dans Angular 2.

La documentation complète d'Ember sur l'aide each et les aides en général est [ici](https://guides.emberjs.com/v2.6.0/templates/displaying-a-list-of-items/).

Voici à quoi ressemble le code pour une vidéo YouTube affichée :

```
<div class="row"> <div class="col s12 m6 l4"> <div class="card-panel center-align"> <div class="purple-text"> <p>Titre</p> </div> <div class="video-container"> <iframe width="853" height="480" src="https://www.youtube.com/embed/peNV2yJRMLo?rel=0" frameborder="0" allowfullscreen></iframe> </div> <div class="purple-text"> Avec Taras Mankovski </div> </div> </div></div>
```

Après l'avoir disposé, je réalise que je veux itérer sur 3 morceaux de données — le titre, le lien de la vidéo YouTube, et la personne présentée dans la vidéo.

Donc, je dois définir mes données dans un tableau dans mon fichier component.js comme suit :

```
model: [{ title: "Ember DND Helper", people: "Taras Mankovski", videoLink: "peNV2yJRMLo?rel=0" },{ title: "Dependency Injection in Angular 2", people: "Patrick J. Stapleton", videoLink: "46WovCX8i-I?rel=0" },{ title: "Angular CLI", people: "Mike Brocchi", videoLink: "BmZLpNRNnZo" },{ title: "Angular Material 2 Spelunking & Issue Submission", people: "Ben Lesh", videoLink: "3gNsyL7wpXU" }]);
```

![Image](https://cdn-media-1.freecodecamp.org/images/7cZ-psmEqKoJFd8Bhwa5GJQ3JvgkoIoDChyk)

Ensuite, je peux enfin utiliser l'aide {{each}} pour itérer sur mes données.

Encadrez le contenu avec l'aide {{each}} comme ci-dessous, en définissant le modèle et votre variable locale :

```
{{#each model as |video|}} CONTENU {{/each}}
```

Ensuite, prenez les morceaux de contenu que vous souhaitez être dynamiques et remplacez-les par des handlebars et localVariable.x, comme ceci :

```
{{video.title}}
```

```
src="https://www.youtube.com/embed/{{video.videoLink}}"
```

```
{{video.people}}
```

Voici à quoi ressemble le code une fois tout dit et fait :

```
<div class="row"> {{#each model as |video|}} <div class="col s12 m6 l4"> <div class="card-panel center-align"> <div class="purple-text"> <p>{{video.title}}</p> </div> <div class="video-container"> <iframe width="853" height="480" src="https://www.youtube.com/embed/{{video.videoLink}}" frameborder="0" allowfullscreen></iframe> </div> <div class="purple-text"> Avec {{video.people}} </div> </div> </div> {{/each}}</div>
```

![Image](https://cdn-media-1.freecodecamp.org/images/T2HQ0WWJGoeyNxuq3Mpxd1B5kvl6mYb2fLQl)

Voici le résultat final de l'utilisation de l'aide {{each}}.

![Image](https://cdn-media-1.freecodecamp.org/images/rVFQkwb9b69ARcyfSUzwkGDpYFg02inh5kgA)

### **Déployer sur Heroku**

Il était une fois un homme nommé tonycoco. Et tonycoco a rendu le déploiement des applications ember sur Heroku super facile. Voici son [dépôt github](https://github.com/tonycoco/heroku-buildpack-ember-cli) si vous voulez jeter un coup d'œil.

Tout d'abord, vous devriez avoir le Heroku Toolbelt installé et lié à votre compte Heroku.

Ensuite, tout ce que vous avez à faire pour déployer sur Heroku est de valider vos modifications sur master et de pousser.

```
$ heroku create --buildpack https://github.com/tonycoco/heroku-buildpack-ember-cli.git
```

```
$ git push heroku master
```

Attendez qu'il termine complètement le déploiement.

Allez dans votre [tableau de bord des applications Heroku](https://dashboard.heroku.com/apps). Mettez à jour l'application avec le nom que vous voulez (pour correspondre à votre application).

Maintenant, changez le nom de la télécommande Heroku pour correspondre au nouveau nom de l'application dans votre fichier .git/config.

Ensuite, _git push heroku master_ à nouveau et vous devriez être prêt !

Dans ce cas, cette application a été déployée : [http://yolobrolo-ember-1.herokuapp.com/](http://yolobrolo-ember-1.herokuapp.com/)

Yolo ! Amusez-vous bien. J'espère que vous essayerez Ember et que vous l'apprécierez.

### **Regardez-moi construire cela étape par étape**

Oh aussi, à des fins de visualisation, vous pouvez me regarder construire cela [sur YouTube à yolobrolo](https://www.youtube.com/watch?v=-Ury2S9Y-4Q).