---
title: Comment ajouter Bootstrap à une application Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-06T10:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-bootstrap-css-framework-to-an-angular-application
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/angular-bootstrap-cover-hashnode.png
tags:
- name: Angular
  slug: angular
- name: Bootstrap
  slug: bootstrap
- name: CSS
  slug: css
seo_title: Comment ajouter Bootstrap à une application Angular
seo_desc: 'By Rodrigo Kamada

  In this article, we''ll build a web application using the latest version of Angular.
  Then we''ll add the Bootstrap CSS framework which provides rich and responsive interface
  components.

  Let''s get started.

  Prerequisites

  Before you star...'
---

Par Rodrigo Kamada

Dans cet article, nous allons créer une application web en utilisant la dernière version d'Angular. Ensuite, nous ajouterons le framework CSS Bootstrap qui fournit des composants d'interface riches et réactifs.

Commençons.

## Prérequis

Avant de commencer, vous devez installer et configurer les outils ci-dessous pour créer l'application Angular.

* [Git](https://git-scm.com/): Git est un système de contrôle de version distribué et nous l'utiliserons pour synchroniser le dépôt. 
* [Node.js et npm](https://nodejs.org/): Node.js est un logiciel d'exécution de code JavaScript basé sur le moteur V8 de Google. npm est un gestionnaire de paquets pour Node.js (Node Package Manager). Nous utiliserons ces outils pour construire et exécuter l'application Angular et installer les bibliothèques.
* [Angular CLI](https://angular.io/cli): Angular CLI est un outil utilitaire en ligne de commande pour Angular et nous l'utiliserons pour créer la structure de base de l'application Angular.
* Un IDE (comme [Visual Studio Code](https://code.visualstudio.com/) ou [WebStorm](https://www.jetbrains.com/webstorm/)): un environnement de développement intégré est un outil avec une interface graphique qui vous aide à développer des applications. Nous en utiliserons un pour développer notre application Angular.

## Comment créer l'application Angular

[Angular](https://angular.io/) est une plateforme de développement pour construire des applications web, mobiles et de bureau en utilisant HTML, CSS et TypeScript (JavaScript). Actuellement, Angular est à la version 13 et Google est le principal mainteneur du projet.

[Bootstrap](https://getbootstrap.com/) est un framework CSS open source qui possède de nombreux composants pour construire des interfaces web réactives.

Créons l'application avec la structure de base Angular en utilisant `@angular/cli` avec le fichier de route et le format de style SCSS.

```powershell
ng new angular-bootstrap
? Would you like to add Angular routing? Yes
? Which stylesheet format would you like to use? SCSS   [ https://sass-lang.com/documentation/syntax#scss                ]
CREATE angular-bootstrap/README.md (1062 bytes)
CREATE angular-bootstrap/.editorconfig (274 bytes)
CREATE angular-bootstrap/.gitignore (604 bytes)
CREATE angular-bootstrap/angular.json (3273 bytes)
CREATE angular-bootstrap/package.json (1079 bytes)
CREATE angular-bootstrap/tsconfig.json (783 bytes)
CREATE angular-bootstrap/.browserslistrc (703 bytes)
CREATE angular-bootstrap/karma.conf.js (1434 bytes)
CREATE angular-bootstrap/tsconfig.app.json (287 bytes)
CREATE angular-bootstrap/tsconfig.spec.json (333 bytes)
CREATE angular-bootstrap/src/favicon.ico (948 bytes)
CREATE angular-bootstrap/src/index.html (302 bytes)
CREATE angular-bootstrap/src/main.ts (372 bytes)
CREATE angular-bootstrap/src/polyfills.ts (2820 bytes)
CREATE angular-bootstrap/src/styles.scss (80 bytes)
CREATE angular-bootstrap/src/test.ts (743 bytes)
CREATE angular-bootstrap/src/assets/.gitkeep (0 bytes)
CREATE angular-bootstrap/src/environments/environment.prod.ts (51 bytes)
CREATE angular-bootstrap/src/environments/environment.ts (658 bytes)
CREATE angular-bootstrap/src/app/app-routing.module.ts (245 bytes)
CREATE angular-bootstrap/src/app/app.module.ts (393 bytes)
CREATE angular-bootstrap/src/app/app.component.scss (0 bytes)
CREATE angular-bootstrap/src/app/app.component.html (23809 bytes)
CREATE angular-bootstrap/src/app/app.component.spec.ts (1090 bytes)
CREATE angular-bootstrap/src/app/app.component.ts (222 bytes)
✔ Packages installed successfully.
    Successfully initialized git.
```

Maintenant, nous devons installer les bibliothèques `bootstrap` et `bootstrap-icons` qui contiennent les fichiers avec les styles et le code JavaScript de Bootstrap comme ceci :

```powershell
npm install bootstrap bootstrap-icons
```

Après l'installation, nous allons configurer les bibliothèques `bootstrap` et `bootstrap-icons`. Modifiez le fichier `angular.json` et ajoutez les fichiers `bootstrap.scss`, `bootstrap-icons.css` et `bootstrap.bundle.min.js` comme suit :

```json
"styles": [
  "node_modules/bootstrap/scss/bootstrap.scss",
  "node_modules/bootstrap-icons/font/bootstrap-icons.css",
  "src/styles.scss"
],
"scripts": [
  "node_modules/bootstrap/dist/js/bootstrap.bundle.min.js"
]
```

Maintenant, nous allons installer la bibliothèque `@ng-bootstrap/ng-bootstrap` qui contient le support natif pour Angular :

```powershell
npm install @ng-bootstrap/ng-bootstrap@next
```

Après l'installation, nous allons importer le module `NgbModule`. Modifiez le fichier `app.module.ts` et ajoutez les lignes comme suit :

```typescript
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

imports: [
  BrowserModule,
  NgbModule,
  AppRoutingModule,
],
```

Maintenant, nous allons supprimer le contenu de la classe `AppComponent` du fichier `src/app/app.component.ts`. Importez le service `NgbModal` et créez la méthode `open` pour ouvrir une modale comme suit.

```typescript
import { Component } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {

  constructor(private modalService: NgbModal) {
  }

  public open(modal: any): void {
    this.modalService.open(modal);
  }

}
```

Ensuite, nous allons supprimer le contenu du fichier `src/app/app.component.html`. Ajoutez quelques composants en HTML pour visualiser et tester les composants comme suit.

```html
<nav class="navbar navbar-expand-sm navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">
      <h1>Angular Bootstrap</h1>
    </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Accueil</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Lien</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Menu déroulant
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Une autre action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Autre chose ici</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Désactivé</a>
        </li>
      </ul>
      <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Rechercher" aria-label="Rechercher">
        <button class="btn btn-outline-success" type="submit">Rechercher</button>
      </form>
    </div>
  </div>
</nav>
<div class="container-fluid py-3">
  <div class="row my-3">
    <div class="col">
      <label for="exampleFormControlInput1" class="form-label">Adresse email</label>
      <input type="email" class="form-control form-control-sm" id="exampleFormControlInput1" placeholder="nom@example.com">
    </div>
  </div>
  <div class="row my-3">
    <div class="col">
      <label for="exampleFormControlTextarea1" class="form-label">Exemple de zone de texte</label>
      <textarea class="form-control form-control-sm" id="exampleFormControlTextarea1" rows="3"></textarea>
    </div>
  </div>
  <div class="row my-3">
    <div class="col">
      <div class="form-check form-switch">
        <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault">
        <label class="form-check-label" for="flexSwitchCheckDefault">Case à cocher par défaut</label>
      </div>
    </div>
  </div>
  <div class="row my-3">
    <div class="col">
      <button class="btn btn-sm btn-outline-primary" (click)="open(demoModal)">Lancer la modale de démonstration</button>
    </div>
  </div>
</div>

<ng-template #demoModal let-modal>
  <div class="modal-header">
    <h4 class="modal-title" id="modal-basic-title">Mise à jour du profil</h4>
    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" (click)="modal.dismiss('Cross click')"></button>
  </div>
  <div class="modal-body">
    <form>
      <div class="form-group">
        <label for="dateOfBirth">Date de naissance</label>
        <div class="input-group">
          <input id="dateOfBirth" name="dateOfBirth" class="form-control" placeholder="aaaa-mm-jj" ngbDatepicker #dp="ngbDatepicker">
          <button type="button" class="btn btn-outline-secondary bi bi-calendar" (click)="dp.toggle()"></button>
        </div>
      </div>
    </form>
  </div>
  <div class="modal-footer">
    <button type="button" class="btn btn-outline-dark" (click)="modal.close('Save click')">Enregistrer</button>
  </div>
</ng-template>
```

Enfin, nous allons exécuter l'application avec la commande suivante :

```powershell
npm start

> angular-bootstrap@1.0.0 start
> ng serve

✔ Browser application bundle generation complete.

Initial Chunk Files | Names         |      Size
vendor.js           | vendor        |   3.38 MB
styles.css          | styles        | 255.86 kB
polyfills.js        | polyfills     | 128.56 kB
scripts.js          | scripts       |  76.94 kB
main.js             | main          |  22.81 kB
runtime.js          | runtime       |   6.59 kB

                    | Initial Total |   3.86 MB

Build at: 2021-06-27T21:28:22.756Z - Hash: 122b9fa4d57b962e7bcc - Time: 21933ms

** Angular Live Development Server is listening on localhost:4200, open your browser on http://localhost:4200/ **


✔ Compiled successfully.
```

Prêt ! Nous allons accéder à l'URL `http://localhost:4200/` et vérifier si l'application fonctionne. Vous pouvez voir l'application en fonctionnement sur [GitHub Pages](https://rodrigokamada.github.io/angular-bootstrap/) et [Stackblitz](https://stackblitz.com/edit/angular13-bootstrap).

![Image](https://www.freecodecamp.org/news/content/images/2022/04/angular-bootstrap.png)

Le dépôt de l'application est disponible à l'adresse [https://github.com/rodrigokamada/angular-bootstrap](https://github.com/rodrigokamada/angular-bootstrap).

## **Conclusion**

Récapitulons ce que nous avons couvert dans cet article :

* Nous avons créé une application Angular.
* Nous avons ajouté certains composants du framework CSS Bootstrap.

Vous pouvez utiliser cet article pour créer des applications riches et réactives qui offrent une meilleure expérience utilisateur et une plus grande convivialité.

Merci d'avoir lu et j'espère que vous avez apprécié l'article !

Ce tutoriel a été publié sur mon [blog](https://rodrigo.kamada.com.br/share/blog/adicionando-o-framework-de-css-bootstrap-em-uma-aplicacao-angular) en portugais.

Pour rester informé chaque fois que je publie de nouveaux articles, suivez-moi sur [Twitter](https://twitter.com/rodrigokamada).