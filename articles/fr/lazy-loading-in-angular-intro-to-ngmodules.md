---
title: Le Lazy Loading dans Angular – Un guide pour débutants sur les NgModules
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-27T18:17:43.000Z'
originalURL: https://freecodecamp.org/news/lazy-loading-in-angular-intro-to-ngmodules
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/cat-1.jpg
tags:
- name: Angular
  slug: angular
seo_title: Le Lazy Loading dans Angular – Un guide pour débutants sur les NgModules
seo_desc: "By Arjav Dave\nWhat is Lazy Loading?\nLazy loading is the process of loading\
  \ components, modules, or other assets of a website as they're required. \nSince\
  \ Angular creates a SPA (Single Page Application), all of its components are loaded\
  \ at once. This m..."
---

Par Arjav Dave

## Qu'est-ce que le Lazy Loading ?

Le lazy loading est le processus de chargement des composants, modules ou autres ressources d'un site web au fur et à mesure qu'ils sont nécessaires.

Comme Angular crée une [SPA (Single Page Application)](https://en.wikipedia.org/wiki/Single-page_application#:~:text=From%20Wikipedia%2C%20the%20free%20encyclopedia,browser%20loading%20entire%20new%20pages.), tous ses composants sont chargés en même temps. Cela signifie qu'un grand nombre de bibliothèques ou de modules inutiles pourraient également être chargés.

Pour une petite application, cela ne poserait pas de problème. Mais à mesure que l'application grandit, le temps de chargement augmentera si tout est chargé en même temps. Le lazy loading permet à Angular de charger les composants et les modules au moment où ils sont nécessaires.

Tout d'abord, pour comprendre comment le lazy loading fonctionne dans Angular, nous devons comprendre les blocs de construction de base du framework : les NgModules.

## Que sont les NgModules ?

Les bibliothèques Angular comme RouterModule, BrowserModule et FormsModule sont des NgModules. [Angular Material](https://material.angular.io/), qui est un outil tiers, est également un type de NgModule.

Les NgModules consistent en des fichiers et du code liés à un domaine spécifique ou possédant un ensemble de fonctionnalités similaires.

Un fichier NgModule typique déclare des composants, des directives, des pipes et des services. Il peut également importer d'autres modules nécessaires au module actuel.

L'un des avantages importants des NgModules est qu'ils peuvent être chargés en lazy loading. Voyons comment nous pouvons configurer le lazy loading.

Vous pouvez [consulter ci-dessous](#heading-module-racine) pour voir à quoi ressemble un fichier NgModule de base.

## Comment créer des NgModules

Dans ce tutoriel, nous allons créer deux modules, _Module A_ et _Module B_, qui seront chargés en lazy loading. Sur l'écran principal, nous aurons deux boutons pour charger chaque module de manière paresseuse.

### Créer le projet

Créez un nouveau projet Angular appelé _lazy-load-demo_ en exécutant la commande ci-dessous :

```
ng new lazy-load-demo --routing --style css
code lazy-load-demo
```

Ici, nous créons un nouveau projet avec le routage. Deuxièmement, nous mentionnons le format de la feuille de style en CSS. La deuxième commande ouvre votre projet dans VS Code.

<h3 id="module-racine">Module racine</h3>

Par défaut, un module racine ou module d'application est créé sous _/src/app_. Voici le fichier NgModule qui est créé.

```
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

Tout d'abord, nous importons tous les modules et composants requis.

Ensuite, le décorateur **`@NgModule`** indique que la classe AppModule est un type de NgModule. Le décorateur accepte _declarations, imports, providers,_ et _bootstrap._ Voici les descriptions pour chacun d'eux :

* **declarations** : Les composants de ce module.
* **imports** : Les modules requis par le module actuel.
* **providers** : Les fournisseurs de services, le cas échéant.
* **bootstrap** : Le composant _racine_ qu'Angular crée et insère dans la page web hôte `index.html`.

### Écran principal

L'écran principal aura deux boutons, **Load Module A** & **Load Module B.** Comme leur nom l'indique, cliquer sur ces boutons chargera chaque module en lazy loading.

Pour cela, remplacez votre fichier _app.component.html_ par le contenu ci-dessous.

```
<button style="padding: 20px; color: white; background-color: green;" routerLink="a">Load Module A</button>
<button style="padding: 20px; color: white; background-color: blue;" routerLink="b">Load Module B</button>
<router-outlet></router-outlet>
```

Définissons les modules pour les routes _a_ & _b_.

### Modules chargés en Lazy Loading

Afin de créer des modules chargés en lazy loading, exécutez les commandes ci-dessous :

```
ng generate module modulea --route a --module app.module
ng generate module moduleb --route b --module app.module
```

Les commandes généreront deux dossiers appelés **modulea** et **moduleb**. Chaque dossier contiendra ses propres fichiers _module.ts_, _routing.ts_ et _component_.

Si vous vérifiez votre fichier _app-routing.module.ts_, vous verrez le code ci-dessous pour les routes :

```
const routes: Routes = [
  { path: 'a', loadChildren: () => import('./modulea/modulea.module').then(m => m.ModuleaModule) },
  { path: 'b', loadChildren: () => import('./moduleb/moduleb.module').then(m => m.ModulebModule) }
];
```

Cela implique que lorsque la route _a_ ou _b_ est visitée, leurs modules respectifs sont chargés en lazy loading.

En lançant le projet avec **ng serve**, vous verrez l'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-25-at-11.18.55-PM.png)
_Page d'accueil_

Lorsque vous cliquez sur le bouton _Load Module A_, vous serez dirigé vers la page _a_. Voici à quoi devrait ressembler votre écran :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-25-at-11.18.14-PM.png)
_Module A chargé en lazy loading_

Vous devriez voir un écran similaire indiquant **moduleb works!** lorsque vous cliquez sur _Load Module B._

## Comment vérifier que le Lazy Loading a fonctionné

Afin de vérifier que les fichiers ont été chargés, ouvrez les outils de développement en appuyant sur F12. Ensuite, consultez l'onglet _Network_ (Réseau) comme vous pouvez le voir dans la capture d'écran ci-dessous. Lorsque vous actualisez la page, elle affichera quelques fichiers qui ont été demandés.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Network-Tab-1.jpg)
_Onglet Network_

Allez-y et effacez votre liste de requêtes en appuyant sur le bouton d'effacement comme indiqué dans l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-25-at-11.42.21-PM.png)

Lorsque vous cliquez sur _Load Module A_, vous verrez une requête pour _modulea-modulea-module.js_ comme dans la capture d'écran ci-dessous. Cela vérifie que le _Module A_ a été chargé en lazy loading.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-25-at-11.46.50-PM.png)
_Module A chargé_

De même, lorsque vous cliquez sur _Load Module B_, le fichier _moduleb-moduleb-module.js_ est chargé. Cela vérifie que le Module B a été chargé en lazy loading.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-25-at-11.47.10-PM.png)
_Module B chargé_

Maintenant, lorsque vous essayez de cliquer sur les boutons, il ne chargera plus ces fichiers _js_.

## Cas d'utilisation des NgModules

Comme nous l'avons vu, il est très facile de créer des modules en lazy loading. Il existe de nombreux cas d'utilisation où ils sont utiles, tels que :

* Créer un module séparé pour les écrans avant connexion vs après connexion.
* Pour un site de commerce électronique, les écrans destinés aux vendeurs vs ceux destinés aux clients peuvent appartenir à des modules séparés. Vous pouvez également créer un module séparé pour le paiement.
* Un CommonModule séparé contenant des composants, des directives ou des pipes partagés est généralement créé. Des directives comme le bouton _Copy Code_, des composants comme _up vote/down vote_ sont généralement inclus dans un module commun.

## Conclusion

Pour les sites web plus petits, le fait que tous les modules soient chargés en même temps n'a peut-être pas beaucoup d'importance. Mais, à mesure que le site grandit, il est utile d'avoir des modules séparés qui sont chargés au besoin.

Grâce au lazy loading, le temps de chargement des sites web peut être considérablement réduit. C'est particulièrement utile lorsque vous essayez d'obtenir un meilleur classement pour le SEO. Même si ce n'est pas le cas, des temps de chargement plus courts signifient une meilleure expérience utilisateur.

Êtes-vous intéressé par d'autres tutoriels ? Consultez ces ressources :

* [Apprendre le TDD avec les tests d'intégration dans .NET](https://arjavdave.com/2021/04/14/learn-test-driven-development-with-integration-tests-in-net-5-0/)
* [Comment authentifier et autoriser correctement les API dans .NET](https://arjavdave.com/2021/03/31/net-5-setup-authentication-and-authorisation/)
* [Azure Functions & wkhtmltopdf : Convertir du HTML en PDF](https://arjavdave.com/2021/03/22/azure-functions-wkhtmltopdf/)