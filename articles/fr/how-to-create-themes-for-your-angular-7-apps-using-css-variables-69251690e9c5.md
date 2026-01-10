---
title: Comment créer des thèmes pour vos applications Angular 7 en utilisant les variables
  CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-04T17:22:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-themes-for-your-angular-7-apps-using-css-variables-69251690e9c5
coverImage: https://cdn-media-1.freecodecamp.org/images/0*_r2HnHAK7lak_Fee
tags:
- name: Angular
  slug: angular
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment créer des thèmes pour vos applications Angular 7 en utilisant les
  variables CSS
seo_desc: 'By Stephen McLean

  In this post, we will build a super simple cryptocurrency listing app using Angular
  7 and CSS variables.

  Table of Contents


  Design

  Project Setup

  Code

  Conclusion, Repo, and Further Reading



  What we’re aiming for

  Design

  Feel free to ...'
---

Par Stephen McLean

Dans cet article, nous allons créer une application super simple de liste de cryptomonnaies en utilisant Angular 7 et les variables CSS.

### Table des matières

* [Conception](#conception)
* [Installation du projet](#installationduprojet)
* [Code](#code)
* [Conclusion, Dépôt et Lectures complémentaires](#conclusiondepotetlecturescomplementaires)

![Image](https://cdn-media-1.freecodecamp.org/images/1*0qQjQUQCwg_mhbeMtwXg3Q.gif)
_Ce que nous visons_

### Conception

N'hésitez pas à [passer cette section](#installationduprojet) si vous êtes seulement ici pour le code.

J'ai conçu cette application simple en utilisant [Figma](https://www.figma.com/).

#### Schéma de couleurs

Notre schéma de couleurs est composé des couleurs _premier plan_, _arrière-plan_, _primaire_ et _erreur_. Chaque groupe de couleurs a plusieurs variantes plus claires et plus foncées de la couleur de base.

Pour nos thèmes clair/sombre, les couleurs de premier plan et d'arrière-plan seront simplement échangées.

%[https://www.figma.com/proto/03NzSIaXxIYwk8DdLe5d5Jhr/project-crypto?node-id=1%3A4&scaling=min-zoom&redirected=1]

#### Composants

Ensuite, nous créons les composants. Comme notre application est assez petite, nous n'avons que quelques composants.

Le composant _nav_, qui permettra à notre utilisateur de basculer le thème.

%[https://www.figma.com/proto/03NzSIaXxIYwk8DdLe5d5Jhr/project-crypto?node-id=1%3A2&scaling=min-zoom&redirected=1]

Le composant _tile_ qui affichera les informations sur les pièces.

%[https://www.figma.com/proto/03NzSIaXxIYwk8DdLe5d5Jhr/project-crypto?node-id=2%3A60&scaling=min-zoom&redirected=1]

En mettant tout cela ensemble, nous obtenons nos designs cibles.

%[https://www.figma.com/proto/03NzSIaXxIYwk8DdLe5d5Jhr/project-crypto?node-id=1%3A3&scaling=min-zoom&redirected=1]

%[https://www.figma.com/proto/03NzSIaXxIYwk8DdLe5d5Jhr/project-crypto?node-id=2%3A53&scaling=min-zoom&redirected=1]

#### Installation du projet

Nous allons échafauder notre application en utilisant l'Angular CLI. Tout d'abord, nous devons l'installer.

```
npm install -g @angular/cli
```

Ensuite, créons notre application.

```
ng new project-crypto
```

Et enfin, générons un module pour contenir notre logique de thème.

```
cd project-crypto 
```

```
ng generate module theme 
```

### Code

Très bien, il est temps pour le bon stuff.

#### Définir les variables CSS

Commençons par définir nos variables CSS initiales. Nous pouvons les définir initialement pour refléter notre thème clair. Comme nous voulons que notre thème soit global, je l'ai défini en utilisant le sélecteur `:root`, qui correspondra à l'élément `html`. Vous pourriez utiliser le `body` ou un autre élément de haut niveau ici si vous le souhaitez.

```js
@import url("https://fonts.googleapis.com/css?family=PT+Sans:400,700");
@import url("https://fonts.googleapis.com/css?family=Inconsolata:400,700");

:root {
  /* Couleurs */
  --foreground-default: #08090a;
  --foreground-secondary: #41474d;
  --foreground-tertiary: #797c80;
  --foreground-quaternary: #f4faff;
  --foreground-light: #41474d;

  --background-default: #f4faff;
  --background-secondary: #a3b9cc;
  --background-tertiary: #5c7d99;
  --background-light: #ffffff;

  --primary-default: #5dfdcb;
  --primary-dark: #24b286;
  --primary-light: #b2ffe7;

  --error-default: #ef3e36;
  --error-dark: #800600;
  --error-light: #ffcecc;

  /* Ombres */
  --background-tertiary-shadow: 0 1px 3px 0 rgba(92, 125, 153, 0.5);
}

body {
  background: var(--background-default);
}

html,
body {
  margin: 0;
  padding: 0;
  font-family: "PT Sans", sans-serif;
}
```

#### Définir les thèmes

Ensuite, définissons nos thèmes en TypeScript. Ceux-ci seront utilisés plus tard pour basculer le thème par un service Angular.

Sous notre module `theme` nouvellement créé, créez un nouveau fichier : `theme.ts`

```js
export interface Theme {
  name: string;
  properties: any;
}

export const light: Theme = {
  name: "light",
  properties: {
    "--foreground-default": "#08090A",
    "--foreground-secondary": "#41474D",
    "--foreground-tertiary": "#797C80",
    "--foreground-quaternary": "#F4FAFF",
    "--foreground-light": "#41474D",

    "--background-default": "#F4FAFF",
    "--background-secondary": "#A3B9CC",
    "--background-tertiary": "#5C7D99",
    "--background-light": "#FFFFFF",

    "--primary-default": "#5DFDCB",
    "--primary-dark": "#24B286",
    "--primary-light": "#B2FFE7",

    "--error-default": "#EF3E36",
    "--error-dark": "#800600",
    "--error-light": "#FFCECC",

    "--background-tertiary-shadow": "0 1px 3px 0 rgba(92, 125, 153, 0.5)"
  }
};

export const dark: Theme = {
  name: "dark",
  properties: {
    "--foreground-default": "#5C7D99",
    "--foreground-secondary": "#A3B9CC",
    "--foreground-tertiary": "#F4FAFF",
    "--foreground-quaternary": "#E5E5E5",
    "--foreground-light": "#FFFFFF",

    "--background-default": "#797C80",
    "--background-secondary": "#41474D",
    "--background-tertiary": "#08090A",
    "--background-light": "#41474D",

    "--primary-default": "#5DFDCB",
    "--primary-dark": "#24B286",
    "--primary-light": "#B2FFE7",

    "--error-default": "#EF3E36",
    "--error-dark": "#800600",
    "--error-light": "#FFCECC",

    "--background-tertiary-shadow": "0 1px 3px 0 rgba(8, 9, 10, 0.5)"
  }
};
```

Nous pouvons ajouter autant de thèmes que nous le souhaitons ici. Pour l'instant, contentons-nous des thèmes clair et sombre.

#### Créer le service de thème

Notre service sera responsable de : **suivre le thème actif**, et **mettre à jour les variables CSS** en fonction du thème actif.

Nous pouvons utiliser le CLI pour générer notre nouveau service. Sous `/src/app/theme` exécutez

```
ng generate service theme
```

```
import { Injectable } from "@angular/core";
import { Theme, light, dark } from "./theme";

@Injectable({
  providedIn: "root"
})
export class ThemeService {
  private active: Theme = light;
  private availableThemes: Theme[] = [light, dark];

  getAvailableThemes(): Theme[] {
    return this.availableThemes;
  }

  getActiveTheme(): Theme {
    return this.active;
  }

  isDarkTheme(): boolean {
    return this.active.name === dark.name;
  }

  setDarkTheme(): void {
    this.setActiveTheme(dark);
  }

  setLightTheme(): void {
    this.setActiveTheme(light);
  }

  setActiveTheme(theme: Theme): void {
    this.active = theme;

    Object.keys(this.active.properties).forEach(property => {
      document.documentElement.style.setProperty(
        property,
        this.active.properties[property]
      );
    });
  }
}
```

Quelques points à noter ici :

1. Nous importons nos définitions de thème que nous venons de créer, à la ligne 2.
2. Les lignes 34–39 mettent à jour nos variables CSS définies dans le thème. C'est essentiellement là que la magie opère.
3. Comme, dans cette application d'exemple, nous n'avons que deux thèmes, j'ai ajouté quelques fonctions de commodité pour définir le thème en clair et sombre directement. Vous pouvez utiliser les fonctions `getAvailableThemes` et `setActiveTheme` pour changer le thème dynamiquement en fonction de l'entrée utilisateur.

#### Composants

Le travail difficile est terminé. Maintenant, nous devons simplement assembler nos blocs de construction. Eh bien, en fait, nous devons d'abord créer les blocs de construction 😉. Créons les composants.

Nous commencerons par le composant **nav**. Encore une fois, nous pouvons utiliser l'Angular CLI pour nous donner un bon départ.

```
ng generate component nav
```

```js
import { Component, OnInit } from "@angular/core";
import {
  faLightbulb as faSolidLightbulb,
  faDollarSign,
  IconDefinition
} from "@fortawesome/free-solid-svg-icons";
import { faLightbulb as faRegularLightbulb } from "@fortawesome/free-regular-svg-icons";
import { ThemeService } from "src/app/theme/theme.service";

@Component({
  selector: "app-nav",
  templateUrl: "./nav.component.html",
  styleUrls: ["./nav.component.css"]
})
export class NavComponent implements OnInit {
  faLightbulb: IconDefinition;
  faDollarSign = faDollarSign;

  constructor(
    private themeService: ThemeService
  ) {}

  ngOnInit() {
    this.setLightbulb();
  }

  setLightbulb() {
    if (this.themeService.isDarkTheme()) {
      this.faLightbulb = faRegularLightbulb;
    } else {
      this.faLightbulb = faSolidLightbulb;
    }
  }

  toggleTheme() {
    if (this.themeService.isDarkTheme()) {
      this.themeService.setLightTheme();
    } else {
      this.themeService.setDarkTheme();
    }

    this.setLightbulb();
  }
}
```

**Note :** J'ai utilisé Font Awesome pour les icônes de la barre de navigation. Si vous souhaitez faire de même, vous devrez [installer Font Awesome pour Angular](https://fontawesome.com/how-to-use/on-the-web/using-with/angular).

La logique de notre composant de navigation est assez simple. Nous définissons notre icône en fonction du thème à l'initialisation (ligne 22). Ensuite, nous configurons un gestionnaire d'événements pour basculer le thème. Vous pouvez voir son utilisation dans le HTML ci-dessous.

```js
<nav>
  <fa-icon [icon]="faDollarSign"></fa-icon>
  <h5 class="title secondary-font">ProjectCrypto</h5>
  <fa-icon [icon]="faLightbulb" (click)="toggleTheme()"></fa-icon>
</nav>
```

```css
nav {
  height: 4rem;
  display: flex;
  align-items: center;
  padding-left: 1rem;
  padding-right: 1rem;
  background-color: var(--background-tertiary);
  color: var(--foreground-quaternary);
  font-size: 1rem;
}

nav .title {
  margin-left: auto;
  margin-right: auto;
}
```

Notes sur le CSS du composant de navigation :

1. Les lignes 7 et 8 sont les importantes ici. Ce sont les deux lignes qui utilisent nos variables CSS précédemment définies, et rendent ce composant thématisable.

Ensuite, le composant **tile**.

```
<div class="container">
  <h5 class="name">{{ name }}</h5>
  <h5 class="price">
    <fa-icon [icon]="currencyIcon"></fa-icon>
    {{ price | number }}
  </h5>
  <fa-icon
    [icon]="faHeart"
    (click)="onToggleFavourite()"
    class="favouriteIcon icon"
    [ngClass]="{ isFavourite: isFavourite }"
  ></fa-icon>
</div>
```

```css
.container {
  display: grid;
  grid-template-columns: 0.5fr 1fr 0.5fr;
  align-items: center;
  border-radius: 0.5rem;
  background: var(--background-light);
  color: var(--foreground-tertiary);
  padding-left: 0.5rem;
  padding-right: 0.5rem;
  margin-bottom: 1rem;
  min-height: 8rem;
  box-shadow: var(--background-tertiary-shadow);
}

.container .name {
  justify-self: start;
}

.container .price {
  justify-self: center;
}

.container .icon {
  justify-self: end;
}

.favouriteIcon {
  font-size: 1.5rem;
}

.isFavourite {
  color: var(--primary-default);
}
```

Notes :

1. Le TypeScript de notre composant tile n'a aucune logique de thème, donc je l'ai omis ici.
2. Les lignes 6, 7, 12 et 32 sont ce qui permet à notre composant tile d'être thématisable.

### Conclusion, Dépôt et Lectures complémentaires

Et voilà ! Vous avez maintenant les composants et le thème créés. Vous pouvez ajouter les composants à votre composant d'application de base pour tout assembler avec quelques données de test.

Vous pouvez trouver le dépôt [ici](https://github.com/stephan-mclean/project-crypto).

Apprenez-en plus sur les variables CSS [ici](https://medium.freecodecamp.org/everything-you-need-to-know-about-css-variables-c74d922ea855).

Merci d'avoir lu !