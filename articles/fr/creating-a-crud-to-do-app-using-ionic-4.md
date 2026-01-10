---
title: Comment créer une application de liste de tâches CRUD avec Ionic 3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-24T08:47:12.000Z'
originalURL: https://freecodecamp.org/news/creating-a-crud-to-do-app-using-ionic-4
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca144740569d1a4ca4d9e.jpg
tags:
- name: Firebase
  slug: firebase
- name: Ionic Framework
  slug: ionic
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
- name: TypeScript
  slug: typescript
seo_title: Comment créer une application de liste de tâches CRUD avec Ionic 3
seo_desc: 'By Sameeha Rahman

  Hey all! This is a post on an up and coming tech topic — Ionic! By the end of this
  post you would learn how to create a simple CRUD (Create, Read, Update and Delete)
  to-do list app, which is also connected to Firebase.

  Hybrid Mobile...'
---

Par Sameeha Rahman

Salut à tous ! Voici un article sur un sujet technologique en plein essor — Ionic ! À la fin de cet article, vous aurez appris à créer une application simple de liste de tâches CRUD (Créer, Lire, Mettre à jour et Supprimer), également connectée à Firebase.

# Applications mobiles hybrides — Qu'est-ce que c'est ?

En termes simples, ce sont des applications mobiles créées avec des langages plus faciles à apprendre : HTML, CSS et JavaScript. La beauté du développement d'une application mobile hybride réside dans le fait qu'elles peuvent être compilées pour fonctionner sur n'importe quelle plateforme. Si vous êtes paresseux, comme moi, vous trouverez plus facile d'utiliser un seul code pour construire plusieurs applications, plutôt que de développer des applications séparées pour chaque plateforme.

Ionic est l'un des frameworks populaires pour créer votre propre application mobile hybride. Il peut être construit en tant qu'application Android, iOS, Windows Phone, Progressive Web ou Desktop. Et tester l'application est tellement plus facile puisqu'elle peut être rechargée en direct directement dans votre navigateur.

## Étape 1 — Installation

Tout d'abord, inscrivez-vous pour un compte Ionic Pro, [ici](https://ionicframework.com/pro?source=post_page---------------------------). Cela rendra la construction et le déploiement de l'application plus faciles. Vous devrez peut-être vous connecter à un moment donné pendant le processus de création du projet.

Pour commencer à coder votre première application Ionic, il y a plusieurs choses dont vous avez besoin ;

1. Node.js — C'est assez facile. Rendez-vous simplement sur le site de Node.js [website](https://nodejs.org/en/?source=post_page---------------------------) et téléchargez l'installateur idéal pour vous. Nous avons besoin du Node Package Manager, nommé npm, pour installer toutes les dépendances des nombreux modules que vous souhaitez utiliser dans votre application. Si vous développez sur un Mac et avez Homebrew installé, tapez simplement la commande `brew install npm` dans la console.
2. TypeScript — TypeScript, un sur-ensemble de JavaScript, est utilisé au lieu de JS pour la majorité du code. Après avoir installé Node.js, dans la console, tapez `npm install -g typescript`.
3. Cordova — Cordova est un framework qui construit le code HTML, CSS et JS/TS en une application. Pour installer, tapez `npm install -g cordova`
4. Et enfin, Ionic — Tapez `npm install -g ionic`.

Bonus — Vous pouvez télécharger les trois en une seule fois avec cette commande aussi ! `npm install -g typescript cordova ionic`.

Maintenant que vous avez configuré l'environnement, commençons cette fête !! ??

### Créer votre première application

Depuis la console, déplacez-vous dans le dossier dans lequel vous souhaitez stocker l'application. Ma préférence personnelle est d'avoir un dossier dédié pour tous mes projets Ionic dans mes Documents.

Ensuite, tapez `ionic start`. La console vous demande alors un nom pour le projet, comme ceci, `Nom du projet : Tasks`.

Elle vous demande ensuite de spécifier le type d'application.

```
? Modèle de démarrage : (Utilisez les touches fléchées)
  tabs     | Un projet de démarrage avec une interface à onglets simple
> blank    | Un projet de démarrage vide
  sidemenu | Un projet de démarrage avec un menu latéral avec navigation dans la zone de contenu
  super    | Un projet de démarrage complet avec des pages pré-construites, des fournisseurs et les meilleures pratiques pour le développement Ionic.
  tutorial | Un projet basé sur un tutoriel qui suit la documentation Ionic
  aws      | AWS Mobile Hub Starter
```

Pour l'instant, faisons-en un projet vide, une liste de tâches avec toutes les fonctions CRUD sur une seule page. Il vous demandera ensuite la permission d'ajouter les plateformes Android et iOS.

```
? Intégrer votre nouvelle application avec Cordova pour cibler les plateformes natives iOS et Android ? (y/N) y
```

Il procédera au téléchargement de dépendances supplémentaires qui vous permettront de recharger l'application en direct dans les émulateurs et les appareils. Une fois les SDK natifs téléchargés, vous êtes invité à ajouter le SDK Ionic Pro, si vous le souhaitez.

```
? Installer le SDK Ionic Pro gratuit et connecter votre application ? y
```

Si vous choisissez oui, la console vous demandera alors votre email et mot de passe Ionic Pro, configurés au début de cet article.

```
? Email : 
? Mot de passe :
```

Par la suite, vous avez la possibilité de lier cette application à une application existante, ou d'en créer une nouvelle entièrement.

```
? Que souhaitez-vous faire ? (Utilisez les touches fléchées)
  Lier une application existante sur Ionic Pro
> Créer une nouvelle application sur Ionic Pro
```

La console vous demande ensuite votre hébergeur git préféré, pour stocker votre dépôt. Je préfère GitHub, car c'est quelque chose que je connais mieux.

```
? Quel hébergeur git souhaitez-vous utiliser ? (Utilisez les touches fléchées)
> GitHub
  Ionic Pro
```

Selon votre choix ci-dessus, si vous avez choisi GitHub comme moi, vous devrez peut-être ouvrir votre navigateur pour donner vos identifiants et vous connecter. Une fois terminé, retournez à la console. Vous devez ensuite lier cette application au dépôt ou en créer un nouveau. Si vous n'avez pas de dépôt, retournez à GitHub et créez-en un maintenant. Une fois le nouveau dépôt créé, retournez à la console et tapez `y`.

```
? Le dépôt existe-t-il sur GitHub ? y
```

Par la suite, choisissez le bon dépôt dans la liste affichée sur la console. Je n'utiliserai que la branche master pour l'instant et opterai pour la première option.

```
? Que souhaitez-vous faire ? (Utilisez les touches fléchées)
> Lier uniquement à la branche master
  Lier à des branches spécifiques
```

Et enfin, nous avons terminé la création de l'application !! ??

Mais, si vous avez choisi Ionic Pro comme hébergeur git, choisissez l'option pour générer une paire de clés SSH.

```
? Comment souhaitez-vous vous connecter à Ionic Pro ? (Utilisez les touches fléchées)
> Configurer automatiquement une nouvelle paire de clés SSH pour Ionic Pro
  Utiliser une paire de clés SSH existante
  Ignorer pour l'instant
  Ignorer définitivement cette invite
```

Et nous avons terminé ici aussi ! Maintenant, jetons un coup d'œil à l'application.

Il existe deux commandes différentes pour afficher l'application dans le navigateur.

1. `ionic serve`
2. `ionic serve -l`

`ionic serve` affiche l'application dans la vue d'une application web.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/ionic-serve.png)
_Vue de l'application web_

`ionic serve -l` affiche l'application sur les nombreuses plateformes de dispositifs mobiles. Vous devrez le télécharger depuis la console, lorsque vous y êtes invité, pour obtenir cette vue.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/ionic-serve-l.png)
_Vue des plateformes mobiles_

Et c'est tout pour aujourd'hui ! Nous avons créé et lié avec succès une application Ionic 4 à un hôte de contrôle de version. 

### La structure du projet

![Image](https://www.freecodecamp.org/news/content/images/2019/07/project-structure-ionic.png)
_Répertoire des dossiers_

1. app.module.ts — Le point d'entrée de l'application. Tous les composants, pages, modules et fournisseurs doivent être ajoutés à ce fichier, car il suit et contrôle les nombreuses ressources utilisées par l'application.
2. app.components.ts — La première page chargée lorsque l'application commence à s'exécuter, avec tout le code que vous souhaitez exécuter en premier. Les pages que vous souhaitez que l'utilisateur voie en premier, comme l'écran de connexion, sont placées dans ce composant.
3. app.html — Le modèle de l'application, où les autres pages d'interface utilisateur seront montées.
4. app.scss — La page qui contient toutes les variables et styles Sass à utiliser globalement dans l'application.

Passons maintenant au composant principal que nous allons modifier pour cette application, home.

Comme vu ci-dessus, le composant home a trois pages ;

1. home.html — La vue/UI de la page est codée ici, en utilisant HTML.
2. home.scss — Tout style spécifique à la page doit être ajouté ici, ainsi que les variables Sass à utiliser dans la page.
3. home.ts — La logique opérationnelle, dans notre cas, l'ajout de nouvelles tâches à la liste, est codée en TypeScript ici.

## Étape 2 - Implémentation des opérations CRUD

![Image](https://www.freecodecamp.org/news/content/images/2019/07/wireframeionic.png)
_Maquettes de l'application_

Ce que j'espère implémenter comme vu ci-dessus, est un design très simple ; une entrée de texte pour taper les tâches, un bouton pour l'ajouter à la liste, une vue de liste pour voir les éléments et enfin un bouton de suppression pour retirer les éléments de la liste. Je pourrais changer le design plus tard.

Allez-y et ouvrez votre éditeur. Faisons un rapide tour de toutes les pages et composants trouvés dans le répertoire actuel.

### Création de l'interface utilisateur pour C et R

Pour commencer, abordons d'abord l'interface utilisateur. Lorsque vous ouvrez home.html, voici le code actuel de la page.

```js
<ion-header>
	<ion-navbar>
		<ion-title>Ionic Blank</ion-title>
	</ion-navbar>
</ion-header>
<ion-content padding>
	The world is your oyster.
	<p>If you get lost, the
		<a href="http://ionicframework.com/docs/v2">docs</a>
	will be your guide.
	</p>
</ion-content>
```

Vous pouvez ensuite supprimer tout ce qui se trouve dans les balises `<ion-content>`. C'est le corps de la page et les éléments à l'intérieur de ces balises seront visibles.

Ajoutez maintenant une balise d'entrée dans le corps, afin que nous puissions entrer la tâche, suivie d'un bouton, pour appeler une méthode afin d'ajouter la tâche à la liste.

```js
<ion-content padding>
	<input type="text" placeholder="Enter task">
	<button>Add Task</button>
</ion-content>
```

![Image](https://www.freecodecamp.org/news/content/images/2019/07/boring-basic--3-.png)
_Basique et ennuyeux_

Pas très joli, n'est-ce pas ? Ajoutons un peu de style maintenant !

Ionic a une balise d'entrée spéciale `<ion-input>`, qui vient avec un peu de style codé à l'intérieur, alors allez-y et remplacez le vieux `<input>` ennuyeux par `<ion-input>` !

Ionic vient également avec certaines classes spéciales qui ont du style, comme la classe `ion-button`. Je veux également que le bouton soit à la fin de l'entrée, et non juste en dessous. Les changements finaux ressemblent à ceci ;

```js
<ion-content padding>
	<ion-item>
		<ion-input type="text" placeholder="Enter task" [(ngModel)]="taskName"/>
		<div class="item-note" item-end>
			<button ion-button>Add Task</button>
		</div>
	</ion-item>
</ion-content>
```

![Image](https://www.freecodecamp.org/news/content/images/2019/07/seamless-sleek--2-.png)
_Intégré et élégant_

Beaucoup mieux, n'est-ce pas ? Et tout cela sans écrire de CSS ! Jetons un autre coup d'œil au code ci-dessus.

La balise `<ion-item>` est normalement utilisée avec l'élément `<ion-list>`. Mais, en l'utilisant ici, avec l'entrée à l'intérieur de cet élément, cela lui donne un style supplémentaire lors de la mise au point ou de l'utilisation. L'utilisation de la classe `item-note` pour un élément div permet au bouton d'être aligné avec la balise d'entrée. En faisant cela, on obtient un design plus intégré et élégant, par rapport au premier. Puisque Angular est également intégré à Ionic, nous pouvons utiliser ngModel pour lier facilement les valeurs dans les vues à celles dans les fichiers TypeScript.

Ionic vient également avec un pack intégré d'icônes, Ionicons. C'est très simple à utiliser, et un exemple rapide serait de substituer le texte Add task par `<ion-icon name="add"></ion-icon>`. Trouvez plus d'informations sur Ionicons, [ici](https://ionicons.com/?source=post_page---------------------------).

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Capture.PNG)
_Balise d'entrée finale_

Le résultat final ! Je suis assez satisfait de son apparence maintenant, mais n'hésitez pas à jouer davantage avec les couleurs et le style.

### Implémentation des fonctionnalités de création et de lecture

Maintenant que l'interface utilisateur est terminée, passons à la fonctionnalité. Il est temps de regarder home.ts. Vous commencez avec un code qui ressemble à ceci ;

```js
import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';

@Component({
    selector: 'page-home',
    templateUrl: 'home.html'
})

export class HomePage {
    constructor(public navCtrl: NavController) {  }
}
```

Jetons un rapide coup d'œil à ce que nous avons ici. Vous importez tous les composants ou modules externes dont vous pourriez avoir besoin pour utiliser cette page tout en haut. Les quelques lignes suivantes décrivent le modèle auquel appartiennent les nombreuses fonctions que vous pouvez écrire et manipuler. Et enfin, toute la logique que vous pouvez coder. Tout code que vous souhaitez exécuter avant de visualiser ou d'interagir avec la page doit être écrit dans le constructeur.

Puisque nous allons ajouter de nouvelles tâches à faire chaque fois, nous avons besoin d'un endroit pour les stocker. La manière la plus simple de faire cela est d'initialiser un tableau. Si vous avez déjà de l'expérience avec JavaScript, coder avec TypeScript sera un jeu d'enfant ! 

Appelons notre liste taskList, mais comme nous avons besoin que la liste soit accessible depuis plus d'une méthode du code, nous devons l'initialiser en dehors du constructeur `taskList = [];`. Maintenant, pour écrire le code qui gère le clic sur le bouton Add Task, appelons-le `addTask`. Tout ce que nous devons faire est de capturer le texte dans l'entrée et de le pousser dans le tableau. Puisque nous avons utilisé `ngModel` pour la balise d'entrée, nous pouvons facilement obtenir la valeur à l'intérieur en utilisant `this.taskName`. Et ajouter des valeurs à un tableau est aussi simple que `taskList.push(task)`. Nous devons également nous assurer qu'aucune chaîne vide n'est ajoutée à la liste, alors enveloppez l'instruction ci-dessus dans une condition if, vérifiant si le taskName existe vraiment. Le code final de home.ts ;

```js
import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';

@Component({
    selector: 'page-home',
    templateUrl: 'home.html'
})

export class HomePage {
    taskList = [];

    constructor(public navCtrl: NavController) {}

    addTask() {
        if (this.taskName.length > 0) {
            let task = this.taskName;
            this.taskList.push(task);
            this.taskName = "";
        }
    }
}
```

> Note : Utiliser le mot-clé `let` en TypeScript est équivalent à utiliser `var`, pour la déclaration de variable.

Maintenant, nous pouvons commencer à ajouter de nouvelles tâches !

Mais comment savons-nous que quelque chose est ajouté ???

Facile, ?Squeezy ! C'est pour cela que le R de CRUD est là !

### Exécuter le code et jeter un coup d'œil

Il est temps de C(réer) un moyen pour nous de R(ead) ce que nous tapons ! (Vous voyez ce que j'ai fait là ?) ?

Retournons à home.html. Jusqu'à présent, nous avons mis une balise d'entrée et un bouton pour ajouter des tâches ; maintenant, mettons une liste pour la visualiser. Nous devons maintenant lier la méthode `addTask()` au bouton dans la propriété `(click)`, afin qu'un élément de liste soit ajouté au tableau à chaque clic.

`<ion-list>` est un élément spécial Ionic pour les vues de liste. La balise `<ion-item>` est utilisée à l'intérieur pour générer chaque élément de la liste. `*ngFor` est une méthode facile pour afficher tous les éléments d'une liste, en définissant une vue standard pour chaque élément de la liste.

Le code final de home.html ;

```js
<ion-header>
	<ion-navbar>
		<ion-title>To-do List</ion-title>
	</ion-navbar>
</ion-header>
<ion-content padding>
	<ion-item>
		<ion-input type="text" [(ngModel)]="taskName" placeholder="Enter task"/>
		<div class="item-note" item-end>
			<button ion-button (click)="addTask()"><ion-icon name="add"></ion-icon></button>
		</div>
	</ion-item>
	<div padding>
		<ion-list>
			<ion-item *ngFor="let todo of taskList">
				{{todo}}
			</ion-item>
		</ion-list>
	</div>
</ion-content>
```

La variable `todo` est un stockage temporaire pour l'élément à l'index actuel de la boucle for (ngFor) dans la liste `taskList`, comme déclaré dans le fichier home.ts.

Prêt à voir notre application jusqu'à présent ?

![Image](https://www.freecodecamp.org/news/content/images/2019/07/part2.gif)

Nous l'avons fait !! Ça marche !! ????

Mais ce n'était que Créer et Lire. Il faudra encore implémenter Mettre à jour et Supprimer.

Nous commencerons d'abord par changer l'interface utilisateur pour qu'elle puisse inclure les fonctionnalités de mise à jour et de suppression. Ensuite, nous passerons au code TypeScript, pour montrer sa fonctionnalité.

### Changer cette apparence pour inclure les gestionnaires pour U et D

Oups ! J'ai oublié quelque chose ! Je n'ai pas changé le nom de l'application sur la page d'accueil... ???

Allez-y et appelez-la comme vous le souhaitez (je serai basique avec 'To-do List').

La première étape, à faire dans le fichier home.html, est d'ajouter le bouton de suppression à gauche de chaque élément de la liste. C'est facile ! Réutilisez le même code que j'ai utilisé pour inclure le bouton `addTask` à côté de l'entrée dans le `<ion-item>`, en imbriquant ce bouton dans la div avec la classe item-note, mais changez ce + en une ?f5d1 (nous ne voulons pas être confus maintenant, n'est-ce pas ?). Puisque c'est un bouton, donnez au gestionnaire d'événements le nom `deleteTask()`. Le bouton aura également une autre classe de style `clear`, qui lui donne un fond transparent. Puisque ce bouton sera dans le `<ion-item>` qui est dans le `<ion-list>`, il sera généré pour tous les éléments de la liste.

Nous devons ajouter un autre bouton à la liste pour éditer chaque tâche. Heureusement, plus de copie de code ! Copiez toute la balise du bouton, mais remplacez l'icône ?f5d1 par un 70fe0f et le gestionnaire de clic par `updateTask()`.

Le code pour chaque balise `<ion-item>` ressemble maintenant à ceci

```
<ion-item *ngFor="let todo of taskList; let i = index">
	{{todo}}
	<div class="item-note" item-end>
		<button ion-button clear (click)="updateTask(i)">
			<ion-icon name="create"></ion-icon>
		</button>
		<button ion-button clear (click)="deleteTask(i)">
			<ion-icon name="trash"></ion-icon>
		</button>
	</div>
</ion-item>
```

L'instruction `let i = index` prend l'index de l'élément spécifique dans la liste, afin que nous puissions le transmettre à la méthode, de sorte que seul l'élément à supprimer serait affecté.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Capture3-und.PNG)

Plutôt soigné, n'est-ce pas ??

J'aime beaucoup et cela a l'air bien mieux que le wireframe que j'ai conçu à l'origine.

### Implémentation des fonctionnalités de mise à jour et de suppression

Maintenant, ajoutons des fonctionnalités à nos ?f5d1 et 70fe0f.

Nous devons créer une nouvelle méthode dans home.ts appelée `deleteTask()`, comme spécifié dans home.html ci-dessus. Nous passons l'index du tableau depuis la boucle `ngFor`, afin de connaître la position exacte de la tâche à supprimer. Allez dans home.html et passez le paramètre `i`, qui est l'index de l'élément dans le tableau, dans la méthode `deleteTask`, comme ceci `deleteTask(i)`. Comme vous avez passé l'index à home.ts, vous devez simplement utiliser la méthode `splice()` sur le tableau pour supprimer la tâche souhaitée, en passant l'index de l'élément à supprimer comme paramètre, comme ceci `this.taskList.splice(index, 1);`.

Le code pour la méthode `deleteTask` est ;

```js
deleteTask(index){
    this.taskList.splice(index, 1);
}
```

Court et doux ! ? C'est tout le code dont nous avons besoin pour supprimer des tâches !

Maintenant, pour la mise à jour, cela nécessitera un peu plus de frappe (soyez patient avec moi) !

Mon plan est d'ouvrir une alerte demandant à l'utilisateur de saisir le texte de mise à jour de la tâche. Pour cela, nous devons importer le `AlertController`, un module trouvé dans `ionic-angular`. Vous l'importez en utilisant cette ligne de code.

```js
import { NavController, AlertController } from 'ionic-angular';
```

Vous devez ensuite l'initialiser dans le constructeur, comme ceci ;

```js
constructor(public navCtrl: NavController, public alertCtrl: AlertController)
```

Vous devrez ensuite créer une alerte dans la méthode `updateTask` pour capturer le nouveau nom de la tâche. Pour ce faire, vous devrez passer les éléments suivants dans la méthode create du AlertController ;

1. title — Le titre du message.
2. message — Un message plus long (si nécessaire).
3. inputs — Champ d'entrée avec leur nom et placeholder (le cas échéant).
4. buttons — Boutons ainsi que leur rôle ou gestionnaire (le cas échéant).

L'alerte peut être affichée par la suite avec la simple commande `alert.present()`. J'aurai deux boutons, l'un est un bouton d'annulation, le second est pour éditer et le code du gestionnaire remplacera simplement la tâche saisie par la valeur précédente dans le tableau. Le code pour la méthode `updateTask()` ;

```js
updateTask(index) {
    let alert = this.alertCtrl.create({
        title: 'Update Task?',
        message: 'Type in your new task to update.',
        inputs: [{ name: 'editTask', placeholder: 'Task' }],
        buttons: [{ text: 'Cancel', role: 'cancel' },
                  { text: 'Update', handler: data => {
                      this.taskList[index] = data.editTask; }
                  }
                 ]
    });
    alert.present();
}
```

Tout devrait fonctionner parfaitement maintenant !

Vous voulez voir l'application CRUD finale ?

![Image](https://www.freecodecamp.org/news/content/images/2019/07/part3-und.gif)

Et voilà ! ??

Une liste de tâches CRUD entièrement opérationnelle, avec un codage minimal ! C'est à quel point Ionic peut être facile.

Je pense toujours que nous pouvons la rendre un peu plus conviviale. Faites défiler vers le bas pour plus de fonctionnalités supplémentaires.

### Bonus !! — Auto-focus

![Image](https://www.freecodecamp.org/news/content/images/2019/07/part3-no-autofocus.gif)
_Entrée sans autofocus_

Savez-vous ce que je trouve ennuyeux ? Je dois cliquer sur l'entrée chaque fois que je veux ajouter une nouvelle tâche, même au début. Pourquoi ne pas auto-focaliser l'entrée après avoir cliqué sur le bouton ?

C'est exactement ce que nous allons faire !

L'auto-focus sur Ionic n'est pas aussi facile que dans les interactions HTML/JavaScript classiques. Vous devez importer un composant supplémentaire appelé `ViewChild`. Vous pouvez ensuite connecter facilement l'entrée de la vue (home.html) au contrôleur (home.ts), et la manipuler également. Vous l'importez, comme ceci ;

```js
import { Component, ViewChild } from '@angular/core';
```

Vous pouvez ensuite connecter la balise d'entrée au composant, en dehors du constructeur, en utilisant cette ligne de code,

```js
@ViewChild('taskInput') input;
```

`taskInput` est l'id de la balise d'entrée sur la page home.html. Allez-y et ajoutez `#taskInput` à la balise d'entrée. La balise d'entrée peut maintenant être gérée directement depuis le fichier TypeScript.

Ionic vient avec quelques méthodes qui peuvent être invoquées sur certains événements de l'application, comme lorsque la page se charge dans la vue, se décharge, etc. Ce sont ce qu'on appelle les événements de cycle de vie, et vous pouvez en trouver plus [ici](https://ionicframework.com/docs/api/navigation/NavController/?source=post_page---------------------------). Nous pouvons faire en sorte que l'application se focalise automatiquement sur l'entrée depuis `ionViewDidLoad()`, en définissant un délai. Le code serait ;

```js
ionViewDidLoad(){
    setTimeout(() => {
        this.input.setFocus();
    },350);
}
```

Pour que l'auto-focus fonctionne après avoir ajouté la ligne `this.input.setFocus();` comme dernière instruction dans le gestionnaire `addTask()`. Allons-y pour voir les changements que nous avons apportés !

![Image](https://www.freecodecamp.org/news/content/images/2019/07/part3-autofocus-1.gif)
_Entrée avec autofocus_

Maintenant, c'est ce qu'on appelle intégré... ?

## Étape 3 - Intégration de l'authentification Firebase

Firebase a tout, de l'autorisation à une base de données en passant par le stockage de fichiers, l'une des nombreuses raisons pour lesquelles c'est un bon choix à ajouter aux applications mobiles. Dans cet article, nous allons explorer Firebase, créer un projet et faire un composant de gestion pour Firebase dans l'application.

### Configuration de la console Firebase

Mais d'abord, vous devez créer un projet sur la console Firebase. Tout ce dont vous avez besoin est un compte Google pour accéder à Firebase. Alors rendez-vous [ici](https://console.firebase.google.com/?source=post_page---------------------------) pour commencer. Ajoutez un nouveau projet et donnez-lui un nom (j'ai simplement appelé le mien 'Tasks'), acceptez tout ce qu'ils demandent et cliquez sur Créer un projet.

Maintenant, configurons le projet pour répondre à nos besoins.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Capture2.PNG)

Toutes les zones de Firebase auxquelles nous accéderons se trouvent sous Développer.

Notamment ;

1. Authentification
2. Et Base de données.

Jetons un coup d'œil à l'authentification.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/capture1.PNG)

Comme vous pouvez le voir, toutes les méthodes d'authentification ont été désactivées. Pour l'instant, activez le type le plus basique, Email/Mot de passe, afin que nous puissions commencer à l'utiliser pour enregistrer un compte.

Sous les modèles, les nombreux modèles d'e-mails pour la vérification de l'adresse e-mail à l'oubli du mot de passe peuvent être trouvés. Si vous le souhaitez, vous pouvez changer quelques détails, comme le nom du projet à afficher et le nom de l'expéditeur.

Maintenant, passons à la section Base de données. Firebase propose deux types de bases de données ;

1. Realtime Database — une base de données NoSQL, qui ressemble à un grand objet JSON.
2. Cloud Firestore — Une collection de documents, qui sont essentiellement des objets JSON.

Firestore est la meilleure option car il a une meilleure structure par rapport à la base de données Realtime normale. Dans la base de données Realtime, n'importe qui peut écrire des données n'importe où, s'ils ont la référence à la base de données, affectant grandement toutes les données stockées. Et pour cette raison, j'ai choisi Firestore et créé la base de données en mode test, afin que nous puissions évaluer la base de données.

Firestore en mode test permet à quiconque de lire et d'écrire dedans, alors faisons en sorte que seuls les utilisateurs qui se sont inscrits à l'application aient accès à la base de données. Pour ce faire, remplacez `allow read, write: if false;` par `allow read, write:if request.auth.uid!=null;`. Seuls les utilisateurs enregistrés ont un uid unique, avec lequel les distinguer. Le plus souvent, l'uid est utilisé comme identifiant de l'objet utilisateur. Je vais implémenter la même chose pour ce projet.

Une fois les règles modifiées, nous devons créer une collection, afin que tous nos documents utilisateurs puissent y être mis. Puisque nous ne pouvons pas avoir une collection sans au moins un document, créez un faux utilisateur. Vous pouvez le supprimer du tableau de bord plus tard.

Maintenant que nous avons configuré le tableau de bord Firebase, passons à l'intégration de Firebase dans l'application.

### Lier Firebase à l'application

Il existe un module spécial `AngularFire` que vous pouvez télécharger en utilisant npm pour incorporer Firebase dans l'application Ionic. Pour télécharger, tapez `npm install firebase angularfire2 --save`.

Pour utiliser ce module, vous devez l'importer dans la page app.module.ts, comme ceci

```js
import { AngularFireModule } from 'angularfire2';
import { AngularFireAuthModule } from 'angularfire2/auth';
import { AngularFirestoreModule } from 'angularfire2/firestore';
```

Nous devons également ajouter les données de configuration nécessaires pour que l'application accède et utilise la base de données correcte. Cela peut être trouvé dans la section Aperçu du projet, 'Ajouter Firebase à votre application web'. Vous devez appeler l'objet JSON firebaseConfig et l'initialiser après les imports.

```js
export const firebaseConfig = {
    apiKey: "#######################################",
    authDomain: "###########.firebaseapp.com",
    databaseURL: "https://###########.firebaseio.com",
    projectId: "###########",
    storageBucket: "###########.appspot.com",
    messagingSenderId: "############"
};
```

Une dernière étape ! Vous devez inclure les modules importés ci-dessus, dans le tableau d'importation de `@NgModule` qui contient tous les composants utilisés dans l'application, en initialisant également le module AngularFireModule avec l'objet de configuration ci-dessus.

```js
@NgModule({
    ...
    imports: [
        ...
        AngularFireModule.initializeApp(firebaseConfig), 
        AngularFireAuthModule, 
        AngularFirestoreModule
    ]
})
```

AngularFireAuthModule vient avec de nombreuses méthodes relatives à l'autorisation, comme l'inscription, la connexion, le mot de passe oublié, etc. Toutes les méthodes que nous utiliserons se trouveront dans la propriété auth de AngularFireAuth. Les méthodes utilisées sont ;

1. `signInWithEmailAndPassword()` — Connexion
2. `createUserWithEmailAndPassword()` — Inscription
3. `sendPasswordResetEmail()` — Réinitialiser le mot de passe
4. `signOut()` — Déconnexion

### Implémentation de toute la logique d'authentification

Nous devons ajouter un écouteur, pour vérifier si l'utilisateur s'est connecté ou non, et pour afficher la réponse correcte pour l'un ou l'autre. Nous devons ajouter l'écouteur dans le fichier app.component.ts, car c'est la première page de l'application qui est chargée.

```js
const authObserver = afAuth.authState.subscribe(user => {
    if (user) {
        this.rootPage = HomePage;
        authObserver.unsubscribe();
    } else {
        this.rootPage = LoginPage;
        authObserver.unsubscribe();
    }
});
```

Importez les autres modules nécessaires, comme HomePage, LoginPage et AngularFireAuth.

Commençons par coder la page d'inscription en premier.

Tout d'abord, pour ajouter une nouvelle page à l'application. Il y a deux façons de faire cela ;

1. Créez un nouveau dossier dans le dossier des pages à l'intérieur de src et créez des fichiers .scss, .ts et .html séparés.
2. Ou, soyez paresseux (comme moi ?) et tapez simplement `ionic g page <nom de la page>` dans la console. Les trois fichiers seront générés automatiquement !

Puisque nous devons effectuer de nombreuses validations sur les données saisies dans les pages de connexion, d'inscription et de mot de passe oublié, nous devons utiliser un groupe de formulaires pour suivre tous les champs du formulaire et ajouter toute validation à chaque champ, comme vérifier si l'e-mail ressemble à un e-mail réel, les longueurs de mot de passe, etc. Nous concevrons d'abord la vue de la page. Dans register.html, la balise de formulaire ressemble à ceci ;

```js
<form [formGroup]="signupForm" (submit)="signupUser()" novalidate>
```

`novalidate` est utilisé car la validation réelle est ajoutée dans le fichier .ts au groupe de formulaires `signupForm`.

Ensuite, copiez la balise item exacte que nous avons utilisée pour ajouter les noms de tâches dans la page d'accueil (mais retirez ce bouton, l'id et `[(ngModule)]` cette fois-ci !). Ajoutez une balise pour le nom complet des utilisateurs, l'e-mail, le mot de passe et la confirmation du mot de passe. Le type de balise d'entrée pour les deux derniers est le mot de passe et l'e-mail pour la balise e-mail. Vous devrez également ajouter un `formControlName` à chaque balise d'entrée. Ajoutez également un bouton de type submit, pour soumettre le formulaire. Le corps de votre page d'inscription doit maintenant ressembler à ceci ;

```js
<form [formGroup]="signupForm" (submit)="signupUser()" novalidate>
  <ion-item>
    <ion-input formControlName="firstName" type="text" placeholder="First Name"></ion-input>
  </ion-item>
  <ion-item>
    <ion-input formControlName="lastName" type="text" placeholder="Last Name"></ion-input>
  </ion-item>  
  <ion-item>
    <ion-input formControlName="email" type="email" placeholder="Email"></ion-input>
  </ion-item>
  <ion-item>
    <ion-input formControlName="password" type="password" placeholder="Password"></ion-input>
  </ion-item>
  <ion-item>
    <ion-input formControlName="retype" type="password" placeholder="Confirm Password"></ion-input>
  </ion-item>
  <ion-grid>
    <ion-row>
      <ion-col style="text-align: center">
        <button ion-button center-all type="submit" [disabled]="!signupForm.valid">Create an Account</button>
      </ion-col>
    </ion-row>
  </ion-grid>
<form>
```

Le bouton Register est désactivé jusqu'à ce que tous les champs du formulaire soient valides. Ajoutons maintenant des validateurs à chaque entrée, dans la page register.ts. Nous devrons importer les modules suivants en haut de la page,

```js
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
```

initialisez le groupe de formulaires en dehors du constructeur, afin qu'il puisse être accessible depuis n'importe où dans le composant ; `public signupForm: FormGroup` et initialisez le constructeur de formulaires à l'intérieur des paramètres passés au constructeur, comme ceci ;

```js
constructor(public navCtrl: NavController, public navParams: NavParams, public formBuilder: FormBuilder){}
```

Les validateurs seront ajoutés au formulaire dans le constructeur comme ceci ;

```js
this.signupForm = formBuilder.group({
  email: ['', Validators.compose([Validators.required])],
  password: ['', Validators.compose([Validators.minLength(6), Validators.required])],
  retype: ['', Validators.compose([Validators.minLength(6), Validators.required])],
  firstName: ['', Validators.compose([Validators.maxLength(30), Validators.pattern('[a-zA-Z ]*'), Validators.required])],
  lastName: ['', Validators.compose([Validators.maxLength(30), Validators.pattern('[a-zA-Z ]*'), Validators.required])]
});
```

`Validators.compose` crée une vérification de validation pour la valeur, selon les validations passées dans ses paramètres. La plupart de ces validateurs sont explicites. Le validateur de motif vérifie si la valeur correspond à une regex spécifique. Mais une question reste, comment valider si un email ressemble à un email ? Apparemment, nous devons en créer un...

Mais ne vous inquiétez pas ! C'est assez simple et la seule logique est de voir si cela correspond à une certaine regex.

Nous devons créer un nouveau dossier 'validators' dans le dossier src et un fichier 'email.ts' à l'intérieur. Nous allons déclarer une méthode statique pour vérifier l'email. Lors de la validation de l'email, nous envoyons le `formControl` au validateur, donc dans ce cas, nous devons importer `FormControl`. Une fois que l'email est testé contre la regex, nous devons retourner une valeur pour indiquer si l'email est valide ou non. Le code final pour le validateur d'email est ;

```js
import { FormControl } from '@angular/forms';

export class EmailValidator {  
  static isValid(control: FormControl) {
    const re = /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/.test(control.value);
    if (re) {
      return null;
    }
    return {
      "invalidEmail": true
    };
  }
}
```

Maintenant, importez le `EmailValidator` dans le fichier register.ts et ajoutez-le au tableau dans la méthode `Validators.compose` pour l'entrée d'email.

```js
this.signupForm = formBuilder.group({
    email: ['', Validators.compose([Validators.required, EmailValidator.isValid])],
    ...
});
```

C'est tout pour la partie validation.

Une autre fonctionnalité que vous pouvez ajouter est d'afficher un message d'erreur juste en dessous de l'entrée, ou même faire en sorte que la balise d'entrée devienne rouge si la validation retourne false. Le code pour le message d'erreur ;

```js
<ion-item class="error-message" *ngIf="!signupForm.controls.email.valid  && signupForm.controls.email.dirty">
    <p>Please enter a valid email.</p>
</ion-item>
```

`*ngIf` vous permet d'afficher l'erreur uniquement si la validation est false. Les erreurs doivent être placées juste en dessous de chaque balise, en modifiant le message et le nom de l'entrée (dans l'exemple ci-dessus 'email') en conséquence.

Le code pour une entrée rouge en cas d'erreur de validation ;

```js
[class.invalid]="!signupForm.controls.email.valid && signupForm.controls.email.dirty"
```

Ajoutez ceci à l'intérieur de chaque entrée, en changeant à nouveau le nom des entrées en conséquence.

Maintenant, pour gérer le clic sur le bouton !

Créez la méthode `signupUser()`. Nous utiliserons la méthode `createUserWithEmailAndPassword()` du module AngularFireAuth. Cela retourne une promesse, que nous devons capturer et selon le résultat, gérer soit la connexion de l'utilisateur, soit afficher un message d'erreur. Pour le rendre plus convivial, affichez également un carrousel de chargement à l'utilisateur pendant que l'inscription a lieu.

Comme le bouton n'est activé que lorsque le formulaire entier est valide, nous n'avons pas besoin de revérifier ce fait. Nous vérifierons d'abord si le mot de passe et le mot de passe retapé sont identiques, et si c'est le cas, nous créerons le nouvel utilisateur et ajouterons ses informations à Firestore. Si les deux sont différents, nous afficherons un message d'erreur dans l'alerte, indiquant qu'ils sont différents.

```js
signupUser() {
  if (this.signupForm.value.password == this.signupForm.value.retype) {
    this.afAuth.auth.createUserWithEmailAndPassword(this.signupForm.value.email, this.signupForm.value.password)
      .then(() => {
        let userId = this.afAuth.auth.currentUser.uid;
        let userDoc = this.firestore.doc<any>('users/' + userId);
        userDoc.set({
          firstName: this.signupForm.value.firstName,
          lastName: this.signupForm.value.lastName,
          email: this.signupForm.value.email
        });
        this.navCtrl.setRoot(HomePage);
      }, (error) => {
        this.loading.dismiss().then(() => {
          let alert = this.alertCtrl.create({
            message: error.message,
            buttons: [{ text: "Ok", role: 'cancel' }]
          });
          alert.present();
        });
      });

    this.loading = this.loadingCtrl.create({
      dismissOnPageChange: true,
      content: "Signing up.."
    });
    this.loading.present();
  } else {
    let alert = this.alertCtrl.create({
      message: "The passwords do not match.",
      buttons: [{ text: "Ok", role: 'cancel' }]
    });
    alert.present();
  }
}
```

Vous devrez également importer les modules supplémentaires `AlertController`, `Loading`, `LoadingController`, `AngularFirestore` et `HomePage`.

`loading` doit être déclaré en dehors du constructeur, afin qu'il puisse être accessible par toutes les méthodes. `AlertController`, `LoadingController` et `AngularFirestore` doivent être initialisés dans les paramètres du constructeur.

Et (enfin) la page d'inscription est terminée !

![Image](https://www.freecodecamp.org/news/content/images/2019/07/tenor.gif)

Ouf ! ?? C'est le plus long article que j'ai jamais écrit. Et il y en a encore plus à venir...

Mais ne vous inquiétez pas ! Le reste n'est que du copier + coller.

La page suivante à aborder est la page de connexion. Copiez l'intégralité du formulaire de la page d'inscription dans login.html, car il est temps d'apporter quelques modifications pour qu'il convienne à la connexion. Supprimez les champs de prénom, de nom et de confirmation du mot de passe ainsi que les messages d'erreur. Dans la balise de formulaire, changez toutes les instances de `signupForm` en `loginForm`.

Changez le texte des boutons de soumission en 'Login' et la méthode `onSubmit` en `loginUser()`. Ajoutez également deux boutons, en dehors du formulaire, pour naviguer vers les pages d'inscription et de réinitialisation du mot de passe. Le corps final de `login.html` ;

```js
<form [formGroup]="loginForm" (submit)="loginUser()" novalidate>
  <ion-item>
    <ion-input formControlName="email" type="email" placeholder="Email" [class.invalid]="!loginForm.controls.email.valid && loginForm.controls.email.dirty"></ion-input>
  </ion-item>
  <ion-item class="error-message" *ngIf="!loginForm.controls.email.valid  && loginForm.controls.email.dirty">
    <p>Please enter a valid email.</p>
  </ion-item>
  <ion-item>
    <ion-input formControlName="password" type="password" placeholder="Password" [class.invalid]="!loginForm.controls.password.valid && loginForm.controls.password.dirty"></ion-input>
  </ion-item>
  <ion-item class="error-message" *ngIf="!loginForm.controls.password.valid  && loginForm.controls.password.dirty">
    <p>Your password must be more than 6 characters long</p>
  </ion-item>
  <ion-grid>
    <ion-row>
      <ion-col style="text-align: center">
        <button ion-button center-all type="submit" [disabled]="!loginForm.valid">Login</button>
      </ion-col>
    </ion-row>
  </ion-grid>
</form>
<button ion-button block clear color="danger" (click)="resetPwd()">
  I forgot my password
</button>
<button ion-button block clear (click)="createAccount()">
  Create a new account
</button>
```

Et voilà ! L'interface utilisateur est terminée.

Le `loginForm` a les mêmes validateurs pour les champs d'email et de mot de passe. Donc, procédez à la copie du même `formBuilder`, en omettant les champs de prénom, de nom et de confirmation du mot de passe.

```js
this.loginForm = formBuilder.group({
    email: ['', Validators.compose([Validators.required, EmailValidator.isValid])],
    password: ['', Validators.compose([Validators.minLength(6), Validators.required])]
});
```

La méthode `loginUser()` a un code similaire à celui de la méthode `signupUser`. Donc, copiez-le également dans le fichier login.ts. Le changement à apporter est de supprimer la comparaison des mots de passe et l'accès à la base de données.

```js
loginUser() {
 this.afAuth.auth.signInWithEmailAndPassword(this.loginForm.value.email, this.loginForm.value.password).then(() => {
   this.navCtrl.setRoot(HomePage);
 }, (error) => {
   this.loading.dismiss().then(() => {
     let alert = this.alertCtrl.create({
       message: error.message,
       buttons: [{ text: "Ok", role: 'cancel' }]
     });
     alert.present();
   });
 });
 this.loading = this.loadingCtrl.create({
   dismissOnPageChange: true,
   content: "Logging in.."
 });
 this.loading.present();
}
```

Vous devrez importer les mêmes modules supplémentaires dans le fichier login.ts, à l'exception de AngularFirestore, car vous n'accéderez pas à la base de données maintenant.

Maintenant, pour gérer les boutons de réinitialisation du mot de passe et de la page d'inscription ;

```js
resetPwd() {
    this.navCtrl.push(ResetPasswordPage);
}

createAccount() {
    this.navCtrl.push(RegisterPage);
}
```

Les pages fonctionnent comme une pile ; vous poussez la page suivante au sommet de la pile et vous retirez également du sommet.

Soyez patient avec moi, il nous reste une page à faire. Hourra ! Encore plus de copier + coller !

Pour la réinitialisation du mot de passe, nous n'avons besoin que du champ email, mais nous avons toujours besoin d'un formulaire pour valider l'email saisi. Comme pour la page de connexion, copiez l'intégralité du formulaire de connexion.html, supprimez tous les champs sauf la balise d'entrée d'email et le message d'erreur, changez toutes les instances de `loginForm` en resetPwdForm. Vous obtenez ;

```js
<form [formGroup]="resetPwdForm" (submit)="resetUserPwd()" novalidate>
  <ion-item>
    <ion-input formControlName="email" type="email" placeholder="Email" [class.invalid]="!resetPwdForm.controls.email.valid && resetPwdForm.controls.email.dirty"></ion-input>
  </ion-item>
  <ion-item class="error-message" *ngIf="!resetPwdForm.controls.email.valid  && resetPwdForm.controls.email.dirty">
    <p>Please enter a valid email.</p>
  </ion-item>
  <ion-grid>
    <ion-row>
      <ion-col style="text-align: center">
        <button ion-button center-all type="submit" color="danger" [disabled]="!resetPwdForm.valid">Reset Password</button>
      </ion-col>
    </ion-row>
  </ion-grid>
</form>
```

La même chose doit être faite pour le fichier reset-password.ts. Le constructeur de formulaire ressemble à ceci ;

```js
this.resetPwdForm = formBuilder.group({
    email: ['', Validators.compose([Validators.required, EmailValidator.isValid])]
});
```

tandis que la méthode `resetUserPwd()` ressemble à ceci ;

```js
resetUserPwd() {
 this.afAuth.auth.sendPasswordResetEmail(this.resetPwdForm.value.email).then((user) => {
   let alert = this.alertCtrl.create({
     message: "We just sent a link to reset your password to your email.",
     buttons: [{ text: "Ok", role: 'cancel',
       handler: () => {
         this.navCtrl.pop();
       }}]
   });
   alert.present();
 }, (error) => {
   let errorAlert = this.alertCtrl.create({
     message: error.message,
     buttons: [{ text: "Ok", role: 'cancel' }]
   });
   errorAlert.present();
 });
}
```

Le code du gestionnaire ci-dessus supprime la page de réinitialisation du mot de passe pour afficher la page de connexion une fois la demande de lien envoyée.

Une dernière partie (je suis vraiment désolé ! Je suis fatigué aussi)…??

Le bouton de déconnexion, le code le plus facile et le plus petit !

Vous devez placer un bouton à la fin de l'en-tête de la page d'accueil comme indiqué ci-dessous ;

```js
<ion-header>
	<ion-navbar>
		<ion-title>To-do List</ion-title>
		<ion-buttons end>
			<button ion-button (click)="logout()">Logout</button>
		</ion-buttons>
	</ion-navbar>
</ion-header>
```

Le code pour gérer la déconnexion dans home.ts ;

```js
logout() {
    return this.afAuth.auth.signOut().then(authData => {
        this.app.getRootNav().setRoot(LoginPage);
    });
}
```

Le code après le 'then' ramène l'utilisateur à la page de connexion.

Et c'est tout ! Enfin ! ??

Pour permettre à l'application d'utiliser ces pages, vous devez les inclure dans la page app.module.ts, dans les tableaux declarations et `entryComponents`, comme ceci ;

```js
@NgModule({
    ...
    declarations: [
        ...
        LoginPage, 
        RegisterPage, 
        ResetPasswordPage
    ],
    ...
    entryComponents: [
        ...
        LoginPage, 
        RegisterPage, 
        ResetPasswordPage
    ]
})
```

Jetons un coup d'œil à tout ce que nous avons accompli jusqu'à présent.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/final-auth.gif)
_Application avec authentification_

Et voilà ! ?? Ce n'est pas très joli, mais c'est définitivement fonctionnel.

Comme vous pouvez le voir, lorsqu'un champ particulier de validation retourne false, l'entrée devient rouge et le message d'erreur s'affiche également. Les boutons restent désactivés jusqu'à ce que tous les champs du formulaire soient valides !

Ci-dessous, l'objet utilisateur a également été stocké dans Firestore, avec l'uid de l'utilisateur actuel comme clé du document. Tout fonctionne !

![Image](https://www.freecodecamp.org/news/content/images/2019/07/capture4.PNG)
_Document Firestore_

Maintenant que l'authentification et, par extension, les objets utilisateur ont été implémentés, nous passons maintenant à la synchronisation des opérations CRUD avec Firebase Cloud Firestore.

## Étape 4 - Synchronisation des actions CRUD avec Cloud Firestore

Le codage sera assez simple, car nous avons déjà intégré AngularFire dans notre application. Les principaux changements seront apportés uniquement à la logique backend dans le fichier home.ts, et un simple ajout à home.html pour gérer les listes que nous obtenons de Firestore.

### Le C dans CRUD vers Firestore

Nous commencerons d'abord par ajouter des fonctionnalités à la méthode `addTask()`. Mais d'abord, nous devons importer AngularFirestore dans home.ts et l'initialiser dans le constructeur, comme ceci ;

```js
constructor(...public firestore: AngularFirestore) {}
```

Comme mentionné dans l'article précédent, Firestore n'est pas comme son prédécesseur, ce n'est pas une grande structure JSON. Au lieu de cela, il fonctionne avec ce qu'on appelle des documents. Chaque document est un objet JSON unique qui ne contient qu'un seul type de données, par exemple, l'objet utilisateur ne contiendra que des données utilisateur, telles que leur nom, date de naissance et autres informations personnelles, mais pas d'autres données.

De nombreux documents du même type constituent une collection. Et parfois, un objet peut avoir une collection de différents objets à l'intérieur, et c'est ce que nous faisons aujourd'hui ; créer une collection d'objets de tâches pour chaque utilisateur.

Si vous vous en souvenez, dans l'article précédent, nous avons pris l'uid de l'utilisateur, un identifiant unique que Firebase attribue à tous ses utilisateurs qui s'inscrivent comme identifiant de l'objet JSON de l'utilisateur. Nous en aurons également grandement besoin aujourd'hui, donc la première chose à faire est de capturer l'uid à partir de AngularFireAuth. Comme de nombreuses méthodes utiliseront cette valeur, il sera préférable de déclarer cette variable en dehors du constructeur, puis de l'initialiser à l'intérieur de `ionViewDidLoad`.

Nous le mettons dans `ionViewdidLoad()`, car parfois les détails de l'utilisateur à partir de AngularFireAuth ne sont pas prêts par le constructeur. Et puisque nous n'accéderons qu'à cette collection à l'intérieur de l'objet utilisateur, allez-y et récupérez-la également, de manière similaire à la page d'inscription. Tout cela est ajouté dans l'appel pour obtenir l'userId.

```js
this.afAuth.authState.subscribe(user => {
    if (user) {
        this.userId = user.uid;
        this.fireStoreTaskList = this.firestore.doc<any>('users/' + this.userId).collection('tasks').valueChanges();
        this.fireStoreList = this.firestore.doc<any>('users/' + this.userId).collection('tasks');
    }
});
```

La raison pour laquelle nous avons deux listes est que `fireStoreTaskList` contient la liste que nous visualisons, tandis que `fireStoreList` est la référence à la collection où nous ajoutons directement les nouvelles tâches. La méthode `valueChanges()` retourne une liste Observable, que nous pouvons afficher dans la vue.

Nous pouvons maintenant utiliser cette référence n'importe où dans la page. L'utiliser pour ajouter une tâche dans la méthode `addTask` est très simple. Il est nécessaire d'avoir un identifiant spécifique pour chaque tâche, car nous en aurons besoin lorsque nous tenterons de mettre à jour le taskName, donc nous devons générer l'identifiant et utiliser la méthode `set()` de la collection firestore, pour créer un nouvel objet de tâche, à l'intérieur de la condition if, en remplaçant le code précédent qui pousse le nom de la tâche dans `taskList`.

```js
let id = this.firestore.createId();
this.fireStoreList.doc(id).set({
    id: id,
    taskName: task
});
```

### Le R dans CRUD dans l'application

Maintenant, pour configurer l'affichage de la liste firestore. La partie principale, obtenir la collection, a été faite ci-dessus. Les changements doivent donc être apportés à home.html pour afficher `fireStoreTaskList`.

Le premier changement doit être apporté dans `*ngFor`, le nom de la liste. Puisque la liste sera une réponse asynchrone de firebase, elle est asynchrone. Le `*ngFor` normal provoquera des erreurs. Nous devons également ajouter un pipe async, comme ceci ;

```js
<ion-item *ngFor="let todo of fireStoreTaskList | async">
```

Nous n'avons plus besoin de suivre l'index, car nous utiliserons l'ID de la tâche pour soit supprimer, soit mettre à jour sa valeur. Et le deuxième changement est la valeur que nous allons afficher, puisque todo sera maintenant un objet, nous devons afficher todo.taskName, car c'est ainsi que nous avons nommé la variable de tâche dans l'objet de tâche.

```js
{{todo.taskName}}
```

Et c'est tout ! Regardons maintenant à la fois l'application et Firestore, pour voir si elle est enregistrée.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/part3-autofocus-2.gif)
_Créer et lire des tâches_

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Capture5.PNG)
_Tâche nouvellement créée_

Elle est enregistrée !

Il n'y a pas grand-chose à faire pour le C et le R dans CRUD. Maintenant, passons à la mise à jour puis à la suppression.

### Le U dans CRUD vers Firestore

Heureusement, AngularFirestore a sa propre fonction de mise à jour, qui, étant donné l'ID du document ainsi que les valeurs à mettre à jour, peut être fait en une seule ligne. Mais d'abord, un petit changement dans le fichier home.html, pour permettre cela. Comme dit précédemment, vous n'avez pas besoin de l'index de la tâche dans la liste pour mettre à jour ou supprimer, mais plutôt de l'ID du document, que nous avons simplement stocké dans la variable id d'un objet de tâche.

Notre première tâche est d'envoyer l'id des tâches à la méthode depuis le bouton, comme ceci ;

```js
<button ion-button clear (click)="updateTask(todo.id)">
```

Passez à home.ts et remplacez le code dans le gestionnaire de l'alerte par ;

```js
this.fireStoreList.doc(index).update({ taskName: data.editTask });
```

Nous créons d'abord une référence à l'objet spécifique que l'utilisateur souhaite mettre à jour en utilisant la méthode `doc()`, puis envoyons les données pertinentes que nous souhaitons mettre à jour dans la méthode `update()`.

Maintenant, voyons cette fonctionnalité en action !

![Image](https://www.freecodecamp.org/news/content/images/2019/07/part5-updateTask.gif)
_Mettre à jour le nom de la tâche_

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Capture6.PNG)
_Nom de la tâche mis à jour_

Celui-ci fonctionne aussi !

Passons maintenant au dernier changement, la suppression.

### Le D dans CRUD vers Firestore

La suppression est aussi facile (ou plus facile, vraiment) que la mise à jour.

Vous devrez à nouveau passer l'ID des tâches au bouton de suppression ;

```js
<button ion-button clear (click)="deleteTask(todo.id)">
```

Encore une fois, comme pour la mise à jour, AngularFirestore a une fonction `delete()`, qui est exécutée sur la référence du document à supprimer, comme ceci ;

```js
this.fireStoreList.doc(index).delete();
```

Et maintenant, regardons la dernière fonctionnalité...

![Image](https://www.freecodecamp.org/news/content/images/2019/07/part5-deleteTask.gif)
_Supprimer la tâche_

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Capture7.PNG)
_Tâche supprimée dans Firestore_

Celui-ci est fonctionnel aussi !

Comme vous pouvez le voir, la tâche 'Fold Clothes' avec un ID de 'NSskIVHEg4gKsT3U0xAV' n'est plus là, car elle a été supprimée avec succès.

Et voilà ! Firebase intégré à toutes les opérations CRUD.

## Étape 5 - Contenu bonus : stylisation

Voici une courte liste de contrôle des choses de base qui n'ont pas été couvertes dans les articles précédents ;

1. Styles personnalisés ?
2. Images ?f4f7
3. Polices personnalisées ?

### Embellir l'interface utilisateur

En parcourant mon application, j'ai pu voir quelques choses que je voulais changer.

Vous vous souvenez de ces petits messages sous les champs de saisie dans les pages de connexion, d'inscription et de réinitialisation du mot de passe ?

![Image](https://www.freecodecamp.org/news/content/images/2019/07/part6-error-with-underline.png)
_Message d'erreur avec soulignement_

Je viens de réaliser que, puisque ce sont essentiellement des `<ion-item>`, ils ont une ligne en bas. Pas très joli.

Heureusement, c'est une correction simple ! Il y a une propriété globale appelée `no-lines`, que vous devez ajouter à la balise `<ion-item>` comme ceci ;

```js
<ion-item ... no-lines>
```

Alors, allez-y et ajoutez ceci à toutes les balises `<ion-item>` des messages d'erreur.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/part6-error-without-underline.png)
_Message d'erreur sans soulignement_

Votre message d'erreur ressemble maintenant à ceci.

Passons maintenant aux couleurs !

Si vous avez fouiné dans la structure du projet, vous auriez vu un dossier appelé theme. Le fichier variables.scss à l'intérieur contient une variable de couleur avec 5 couleurs définies. Gardez les couleurs light et dark telles qu'elles sont, ainsi que danger, car nous l'utilisons pour le bouton et la page de réinitialisation du mot de passe. Je vais seulement changer les couleurs primaire et secondaire. J'utilise généralement [coolors.co](https://coolors.co/1d1e18-6b8f71-aad2ba-d9fff5-b9f5d8?source=post_page---------------------------) pour trouver des couleurs complémentaires pour tous les projets que j'ai jamais faits.

> _Avertissement : N'ajoutez pas plus de ces 5 couleurs à l'objet, car cela entraîne la création de plusieurs copies de composants pour chacune de ces couleurs. Cela ajoutera éventuellement un volume indésirable au projet, car tous les composants avec toutes les couleurs ne sont pas utilisés. Si vous devez utiliser plus de couleurs, ajoutez une nouvelle variable pour contenir uniquement cette valeur littérale de couleur._

Les couleurs que je vais utiliser sont ;

```scss
$colors: (
	primary:    #32B596,
	secondary:  #fff350,
	danger:     #f53d3d,
	light:      #f4f4f4,
	dark:       #222
);
```

Le premier endroit pour ajouter un peu de couleur est la barre de navigation supérieure.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/part6-plain-navbar.png)
_Ennuyeux...

Cela avait l'air si fade, n'est-ce pas ??

![Image](https://www.freecodecamp.org/news/content/images/2019/07/part6-colored-navbar.png)
_Ooh la la !_

Plus maintenant.??

Tout ce que vous avez à faire est d'ajouter la couleur primaire à la balise ion-navbar, comme ceci ;

```js
<ion-navbar color='primary'>
```

Vous pouvez ajouter la propriété de couleur de manière similaire à d'autres composants. Par exemple, donnez à l'icône de suppression la couleur stockée dans danger, ou aux boutons d'ajout et de déconnexion la couleur dans secondaire ;

![Image](https://www.freecodecamp.org/news/content/images/2019/07/part6-colorful-app.png)
_Ajout de couleurs partout !_

Je déteste toujours l'apparence du bouton de déconnexion... Pour en faire un vrai bouton, ajoutez simplement la propriété solid à la balise, comme ceci ;

```js
<button ion-button solid color='secondary' (click)="logout()">Logout</button>
```

![Image](https://www.freecodecamp.org/news/content/images/2019/07/part6-colorful-app-logout-btn.png)
_Les boutons doivent ressembler à des boutons !_

Un autre design d'interface utilisateur cool que j'ai vu précédemment avait des icônes avant chaque balise d'entrée sur les pages de connexion, d'inscription et de réinitialisation du mot de passe, alors j'ai décidé d'essayer aussi ! C'est un code assez simple, que vous devez ajouter à l'intérieur de la balise `<ion-item>` mais avant la balise `<ion-input>`, comme ceci ;

```js
<ion-item>
	<div class="item-note" item-start>
		<ion-icon name="at" color='primary'></ion-icon>
	</div>
	<ion-input formControlName="email" ...></ion-input>
</ion-item>
```

Il n'y a pas d'icône qui crie mot de passe, alors j'ai décidé d'utiliser ? comme dans le design d'interface utilisateur que j'ai regardé ; et ? pour les noms des utilisateurs

![Image](https://www.freecodecamp.org/news/content/images/2019/07/part6-input-icons.png)
_Icônes d'entrée de la page d'inscription_

### Ajout d'images

Une image vaut mille mots... Mais nous n'avons pas besoin de telles images... ? Peu importe !

Ajouter des images n'est pas nécessairement difficile, mais le chemin peut parfois être un peu déroutant. Vous pourriez penser qu'il faut ajouter le chemin réel de la page au dossier d'images, qui est `../../assets/imgs/imagename.png`. Le chemin que vous devez vraiment ajouter est le chemin du fichier app.html à l'image dans le dossier d'images, et ce chemin ressemble à `assets/imgs/imagename.png`.

Toutes les images que vous souhaitez utiliser doivent être ajoutées au dossier `src/assets/imgs`. Vous pouvez ensuite utiliser l'image comme si c'était du HTML ;

```js
<img src="assets/imgs/imagename.png"/>
```

Je veux ajouter une image, un peu comme un logo, aux pages de connexion, d'inscription et de réinitialisation du mot de passe.

Pour que l'image ne dépasse pas la page, nous devons également coder un peu de style, et comme cette image sera sur plus d'une page, nous devons écrire le style dans la page app.scss comme ceci ;

```css
.imageTop {
    height: 200px;
    padding: 20px;
    margin: auto;
    display: block;
}
```

Tout ce que vous devez faire maintenant est simplement ajouter la classe à la balise `img`, `class='imageTop'`.

Une autre image (ou deux) que vous pourriez vouloir changer, est la page de démarrage et l'icône de l'application. Vous devrez d'abord ajouter soit (ou les deux) les plateformes Android et iOS, pour utiliser cette fonctionnalité. La commande pour ajouter une plateforme est

```
ionic cordova platform add android
```

Ou `ios`, si c'est votre tasse de 615.

Ionic peut facilement générer des pages de démarrage et des icônes de différentes tailles selon les différents téléphones lorsque vous exécutez la commande `ionic cordova resources` dans le terminal. Vous aurez besoin d'internet pour cela, car ionic télécharge les deux images à analyser pour générer les autres pages de démarrage et icônes.

Avant cela, vous devez ajouter les deux images, nommées `splash.png` et `icon.png`, au dossier resources. Les tailles des deux images doivent être respectivement de 2732*2732 et 1024*1024, pour que les nombreuses pages de démarrage et icônes d'application soient générées.

C'est tout pour les images !

### La typographie, c'est génial !

Tout d'abord, trouvez une police qui vous parle. Les dernières tendances se tournent vers les polices sans empattement qui sont assez faciles à lire. Aussi jolies que soient de nombreuses polices manuscrites fluides, elles ne sont qu'un échec en attente de se produire, comme celle-ci...

![Image](https://www.freecodecamp.org/news/content/images/2019/07/part-6-cows.png)
_J'aime aussi les ? !_

Ou celle-ci,

![Image](https://www.freecodecamp.org/news/content/images/2019/07/part6-adolf.png)
_L'espoir n'a jamais semblé si sombre !_

???

Blagues à part, j'ai choisi la police 'Alegreya Sans' pour cette application. Elle peut être trouvée, [ici](https://www.fontsquirrel.com/fonts/alegreya-sans?source=post_page---------------------------).

Décompressez toutes les polices dans le dossier `assets/fonts`.

Tout ce que vous avez à faire maintenant est d'ajouter le code ci-dessous au fichier variables.scss trouvé dans le dossier `src/theme`.

```scss
@font-face {
	font-family: 'Alegreya Sans Regular';
	src: url("../assets/fonts/AlegreyaSans-Regular.otf");
}
$font-family-base: 'Alegreya Sans Regular';
$font-family-ios-base: 'Alegreya Sans Regular';
$font-family-md-base: 'Alegreya Sans Regular';
$font-family-wp-base: 'Alegreya Sans Regular';
```

Le `@font-face` importe votre police et lui donne un nom, afin qu'elle puisse être utilisée dans toute l'application.

La variable `$font-family-base` attribue la police par défaut.

L'application ressemble maintenant à ceci ;

![Image](https://www.freecodecamp.org/news/content/images/2019/07/final-final-app-full.gif)
_Personne n'a besoin de voir ce mot de passe !_

Comme vous ne pouvez voir la page de démarrage et l'icône que sur un appareil réel, j'ai apporté mon téléphone fidèle dans le mélange (Malheureusement, ce n'est pas un Apple pour s'adapter au reste des gifs/images).

Et c'est tout pour cette série !!!!! ??

Trouvez le dépôt pour cet article, [ici](https://github.com/samsam-026/Tasks/commit/f54bf2d7e534d31a9ae4962a173053a0044e235e?source=post_page---------------------------).

J'espère que vous avez tous passé un bon moment et appris beaucoup de choses lors de ce voyage avec moi !

Merci pour la lecture, et à bientôt ! ??