---
title: Comment intégrer Chart.js dans Angular en utilisant des données d'une API REST
subtitle: ''
author: deji adesoga
co_authors: []
series: null
date: '2023-03-30T15:54:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-chart-js-in-angular-using-data-from-a-rest-api
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Copy-of-Copy-of-Orange-and-White-Vibrant-Food-YouTube-Thumbnail--1-.png
tags:
- name: Angular
  slug: angular
- name: chartjs
  slug: chartjs
- name: REST API
  slug: rest-api
seo_title: Comment intégrer Chart.js dans Angular en utilisant des données d'une API
  REST
seo_desc: 'Charts are a great way of visually displaying large sets of data in formats
  that are easy to understand and analyze. They are a great way of showing the relationship
  that exists between two or more data sets.

  Different types of charts exist, some of ...'
---

Les graphiques sont un excellent moyen de présenter visuellement de grands ensembles de données dans des formats faciles à comprendre et à analyser. Ils sont un excellent moyen de montrer la relation qui existe entre deux ensembles de données ou plus.

Différents types de graphiques existent, dont certains incluent les graphiques en barres, les graphiques en lignes, les graphiques circulaires, les graphiques radar, etc.

Dans cet article, vous utiliserez un framework frontend appelé Angular ainsi qu'une bibliothèque JavaScript appelée [Chart.js](https://www.chartjs.org/) pour afficher des données d'une plateforme de cryptomonnaies appelée [Coinranking](https://coinranking.com/). Vous utiliserez également l'API Coinranking pour visualiser une liste de cryptomonnaies ainsi que leurs prix.

## Prérequis

Pour suivre ce tutoriel, assurez-vous d'être familier avec les bases des technologies listées ci-dessous :

* HTML

* JavaScript

* TypeScript

* npm

## Table des matières

* [Comment installer et créer l'application Angular](#heading-comment-installer-et-creer-lapplication-angular)

* [Comment intégrer Chart.js dans Angular](#heading-comment-integrer-chartjs-dans-angular)

* [Comment intégrer l'API REST](#heading-comment-integrer-lapi-rest)

* [Comment afficher les données dans le graphique](#heading-comment-afficher-les-donnees-dans-le-graphique)

* [Conclusion](#heading-conclusion)

Vous pouvez également regarder la version vidéo de cet article ci-dessous, ou sur ma [chaîne YouTube](https://www.youtube.com/thecodeangle) :

%[https://www.youtube.com/watch?v=WCI4yvrzFwc&t=1s]

## Comment installer et créer l'application Angular

Tout d'abord, vous devez installer et configurer Angular en suivant les étapes suivantes :

### Étape 1 : Installer NPM (Node Package Manager)

Pour installer npm, vous devez télécharger Node.js. Cela peut être fait via le site [website](https://nodejs.org/en/download/).

Node.js est un environnement serveur open-source multiplateforme qui peut fonctionner sur Windows, Linux, Unix, macOS, et plus encore. Il nous permet d'utiliser npm pour installer des bibliothèques comme Chart.js dans notre application Angular.

### Étape 2 : Installer l'Angular CLI (Command Line Interface)

Une fois Node.js installé, vous pouvez maintenant télécharger Angular sur votre machine avec le terminal/la ligne de commande en utilisant la commande suivante :

```javascript
npm install -g @angular/cli
```

Pour confirmer qu'Angular a été installé, vous pouvez voir la version en exécutant la commande `ng v`, ce qui nous donnera le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/capture2.png align="left")

*Version de l'Angular CLI*

### Étape 3 : Créer un nouveau projet Angular

Maintenant qu'Angular est installé, vous pouvez créer un nouveau projet en exécutant les commandes suivantes dans le terminal :

```javascript
ng new ng-chart --routing=false --style=css
cd ng-chart
code .
```

Avec les commandes ci-dessus, nous avons créé un nouveau projet Angular en utilisant la commande `ng new`, désactivé le routage et défini le format de style à CSS.

Ensuite, naviguez dans le répertoire du projet en utilisant la commande `cd`, et ouvrez le projet dans Visual Studio Code.

Vous n'avez pas besoin de générer un nouveau composant pour ce projet. Vous utiliserez les deux fichiers par défaut créés par l'Angular CLI — `app.component.ts` et `app.component.html` — pour rendre le graphique. Ces fichiers se trouvent dans le répertoire `app` de votre projet.

Le fichier `app.component.html` contient un code de base dont vous devez vous débarrasser. La bibliothèque Chart.js peut maintenant être intégrée dans votre application.

## Comment intégrer Chart.js dans Angular

Pour ajouter la bibliothèque chart.js à l'application Angular, vous devez exécuter la commande suivante dans votre terminal :

```javascript
npm i chart.js
```

Pour confirmer que chart.js a été installé, vous pouvez vérifier le fichier `package.json` dans votre projet. Vous devriez voir la version de chart.js dans l'objet `dependencies` comme montré dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/capture4.png align="left")

*Version de Chart.js*

Vous pouvez maintenant importer la bibliothèque chart.js dans votre projet dans le fichier `app.component.ts` comme on peut le voir ci-dessous :

```javascript
import Chart from 'chart.js/auto';
```

Ensuite, créez une variable appelée `chart` et définissez-la sur un tableau vide :

```javascript
chart: any = []
```

Accédez à la page de démarrage de la documentation de chart.js [documentation](https://www.chartjs.org/docs/latest/getting-started/) et récupérez le code de base avec des données statiques, puis collez-le dans le hook de cycle de vie `ngOnInit` :

**Note** : Le hook de cycle de vie `ngOnInit` dans Angular est déclenché une fois après qu'un composant est initialisé. C'est-à-dire qu'il est appelé uniquement lorsque la première détection de changement se produit dans un composant Angular.

```javascript
export class AppComponent {
  title = 'ng-chart';
  chart: any = [];
 
  constructor() {}

  ngOnInit() {
    this.chart = new Chart('canvas', {
      type: 'bar',
      data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [
          {
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });
  }
}
```

Dans le code ci-dessus, dans l'objet data, il y a une clé `labels` qui contient un tableau avec différentes valeurs. En dessous, vous avez le tableau `datasets` qui contient un objet.

Dans l'objet, il y a un tableau appelé `data` avec des valeurs de différents nombres. Ces valeurs représentent les données qui seront affichées sur le graphique dans le navigateur.

Avant que le graphique ne s'affiche dans le navigateur, vous devrez également récupérer la balise html `<canvas></canvas>` et la coller dans le fichier `app.component.html` comme on peut le voir ci-dessous :

```javascript
<div>
  <canvas id="canvas">{{chart}}</canvas>
</div>
```

**Note** : Dans le fichier `app.component.html`, la balise `<canvas>` a un `id` appelé `canvas`. Celui-ci doit avoir le même nom que la valeur à l'intérieur des parenthèses avant l'objet `new Chart` dans le fichier `app.component.ts`. Si les noms ne sont pas les mêmes, le graphique ne s'affichera pas.

Vous pouvez maintenant compiler et servir le projet en exécutant la commande `ng serve --open` dans le terminal. Vous devriez obtenir les résultats suivants :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/capture6.png align="left")

*Affichage des graphiques avec des données statiques*

## Comment intégrer l'API REST

Pour intégrer l'API REST, rendez-vous sur le site web de Coinranking en utilisant ce [lien](https://developers.coinranking.com/api). Vous devriez voir une page comme celle-ci :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/capture8.png align="left")

*Site web de Coinranking*

Commencez par cliquer sur le bouton "Get API Key". Vous serez dirigé vers une page où vous pourrez créer un compte et avoir accès à une clé **API**.

Copiez la clé API et ouvrez le fichier `environment.ts` dans votre projet Angular. Dans l'objet, créez une variable appelée `API_KEY` et collez la clé API générée par CoinRanking comme on peut le voir ci-dessous :

```javascript
export const environment = {
  production: false,
  API_KEY: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
};
```

Ensuite, vous devez copier l'API pour obtenir toutes les cryptomonnaies de la documentation de CoinRanking [documentation](https://developers.coinranking.com/api/documentation/coins).

![Image](https://www.freecodecamp.org/news/content/images/2023/03/capture9.png align="left")

*Documentation de l'API Coinranking*

Pour utiliser le lien API copié ci-dessus, vous devez créer un service Angular en exécutant la commande suivante :

```javascript
ng g service services/chart
```

Avec le fichier `chart.service.ts` créé, vous pouvez maintenant coller le code qui nous aide à consommer l'API REST comme on peut le voir ci-dessous :

Pour résumer le code ci-dessus, voici ce que nous avons fait :

* Nous avons importé le `HttpClient`, `HttpHeaders` à la **ligne 2**, ainsi que le fichier `environment` à la **ligne 3**.

* Entre la **ligne 5** et la **ligne 11**, nous avons créé une variable appelée `httpOptions`. La variable `httpOptions` contient un objet qui contient la configuration `HttpHeaders` importée ci-dessus. Ici, nous avons défini le **content-type**, passé la variable `API_KEY` du fichier `environment` aux en-têtes, puis défini `Access-Control-Allow-Origin` sur un wildcard. Cela signifie que le navigateur doit permettre le code de requête de l'origine.

* À la **ligne 17**, nous avons créé une variable privée appelée `baseUrl` pour contenir l'**API REST**, tandis qu'à la **ligne 28**, nous avons créé une variable appelée `proxyUrl` pour contenir le lien **CORS Anywhere**. Le lien **CORS Anywhere** est un proxy NodeJS qui ajoute des en-têtes CORS à la requête proxy et aide à prévenir les erreurs CORS dans le processus.

* À la **ligne 20**, nous avons injecté le `HttpClient` dans le constructeur ce qui le rend accessible dans le Service.

* Enfin, nous avons créé une fonction appelée `cryptoData()` à la **ligne 22**. Dans cette fonction se trouve une variable appelée `url`. Nous avons utilisé la variable `url` pour ajouter les variables `proxyUrl` et `baseUrl` pour construire notre API. De plus, dans l'instruction `return`, nous avons utilisé la méthode http `get()` pour récupérer les données de l'API REST.

Pour faire fonctionner le `HttpClient`, vous devez importer et injecter le `HttpClientModule` dans le fichier `app.module.ts` comme on peut le voir ci-dessous :

```javascript
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';

@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule, HttpClientModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
```

Comme on peut le voir ci-dessus, le `HttpClientModule` a été importé et injecté dans le tableau `imports`.

## Comment afficher les données dans le graphique

Pour afficher les données sur le graphique, vous devez vous rendre dans le fichier `app.component.ts` et y intégrer votre fichier de service Chart comme on peut le voir ci-dessous :

* Comme on peut le voir ci-dessus, nous commençons par importer le Chart Service et l'injecter dans notre composant aux **ligne 3** et **ligne 17** respectivement.

* Nous avons créé trois variables appelées `result`, `coinPrice`, et `coinName`. Ces variables seront utilisées plus tard dans le projet pour contenir des données.

* Dans le hook de cycle de vie `ngOnInit()`, nous avons appelé la fonction `cryptoData()` à la **ligne 20**, qui retourne un observable auquel on s'abonne. Cela nous permet de retourner une réponse des données dans le processus.

* À la **ligne 21**, nous avons appelé la variable `result` en utilisant le mot-clé `this` et l'avons définie pour contenir les données.

* Ensuite, aux **ligne 22** et **ligne 23**, nous avons appelé les variables **coinPrice** et **coinName**, mappé à travers les données, et attaché le prix de la cryptomonnaie et le nom de la cryptomonnaie à celles-ci respectivement.

* Pour voir les résultats des données dans le navigateur, nous avons utilisé la fonction `console.log()` pour afficher les données, comme on peut le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/capture10-1.png align="left")

*Données de l'API CoinRanking affichées sur la console.*

La dernière chose à faire est de tracer les données vues dans l'image ci-dessus dans le graphique.

* Comme on peut le voir ci-dessus, nous avons d'abord remplacé les données statiques dans les labels à la **ligne 12** par le nom de la cryptomonnaie obtenu de l'API CoinRanking.

* Ensuite, nous avons remplacé les données statiques à la **ligne 15** par le prix obtenu de l'API CoinRanking.

Maintenant, compilez le projet en exécutant la commande `ng serve --open` et voyez les résultats dans le navigateur comme on peut le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/capture11.png align="left")

*Résultats finaux du graphique*

**Note** : Il est possible que vous rencontriez une erreur qui dit **(Échec du chargement de la ressource : le serveur a répondu avec un statut de 403 (Interdit))** après avoir compilé le projet.

Ce que vous devez faire, c'est cliquer sur le lien CORS Anywhere dans la console qui s'ouvrira dans un nouvel onglet, avec un bouton qui dit **Demander un accès temporaire au serveur de démonstration.** Cliquez sur le bouton, puis actualisez la page. Les données devraient maintenant se refléter sur le graphique.

## Conclusion

Dans ce tutoriel, vous avez appris comment installer et intégrer la bibliothèque Chart.js et une API REST dans une application Angular. Si vous voulez accéder à la base de code, vous pouvez cloner le dépôt [ici](https://github.com/desoga10/ng-chart) sur GitHub.

Si vous avez aimé cet article, vous pouvez montrer votre soutien en vous abonnant à ma [chaîne YouTube](https://www.youtube.com/TheCodeAngle) où je crée des tutoriels géniaux sur les technologies de développement web comme JavaScript, React, Angular, Node.js, et plus encore.