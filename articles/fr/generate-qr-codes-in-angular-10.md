---
title: Comment générer des codes QR dans Angular 10
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-10T17:56:29.000Z'
originalURL: https://freecodecamp.org/news/generate-qr-codes-in-angular-10
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9955740569d1a4ca1f23.jpg
tags:
- name: Angular
  slug: angular
- name: qr code
  slug: qr-code
seo_title: Comment générer des codes QR dans Angular 10
seo_desc: 'By Ahmed Bouchefra

  In this tutorial, we''ll learn how to generate QR codes in Angular 10 by building
  a simple example application.

  But first of all, what''s a QR code and what does it do?

  According to Wikipedia:


  A QR code (abbreviated from Quick Respo...'
---

Par Ahmed Bouchefra

Dans ce tutoriel, nous allons apprendre comment générer des codes QR dans Angular 10 en construisant une simple application d'exemple.

Mais tout d'abord, qu'est-ce qu'un code QR et à quoi sert-il ?

Selon [Wikipedia](https://en.wikipedia.org/wiki/QR_code) :

> Un code QR (abréviation de Quick Response code) est un type de code-barres matriciel (ou code-barres à deux dimensions) conçu pour la première fois en 1994 pour l'industrie automobile au Japon.   
>   
> Un code-barres est une étiquette optique lisible par machine qui contient des informations sur l'élément auquel il est attaché.   
>   
> En pratique, les codes QR contiennent souvent des données pour un localisateur, un identifiant ou un traceur qui pointe vers un site web ou une application.   
>   
> Un code QR utilise quatre modes d'encodage standardisés (numérique, alphanumérique, octet/binaire et kanji) pour stocker des données de manière efficace.

Donc, c'est simplement une manière compacte et efficace de stocker des données.

Maintenant, voyons comment générer des codes QR dans vos applications Angular 10 en créant un exemple.

## Prérequis

Avant de commencer, vous avez besoin de quelques prérequis :

* Connaissance de base de TypeScript. En particulier, la familiarité avec les concepts de programmation orientée objet tels que les classes et les décorateurs TypeScript.
* Une machine de développement locale avec **Node 10+**, ainsi que **NPM 6+** installés.

Node est requis par l'Angular CLI comme la plupart des outils front-end de nos jours. Vous pouvez simplement aller sur la page de téléchargements du [site officiel](https://nodejs.org/downloads) et télécharger les binaires pour votre système d'exploitation. 

Vous pouvez également vous référer aux instructions spécifiques de votre système pour savoir comment installer Node en utilisant un gestionnaire de paquets. La méthode recommandée est cependant d'utiliser [NVM](https://github.com/nvm-sh/nvm) — Node Version Manager — un script bash conforme à POSIX pour gérer plusieurs versions actives de Node.js.

**Note** : Vous ne voulez pas installer un environnement local pour le développement Angular mais vous voulez toujours essayer le code de ce tutoriel ? Vous pouvez utiliser [Stackblitz](https://stackblitz.com/), un IDE en ligne pour le développement front-end qui vous permet de créer un projet Angular compatible avec l'Angular CLI.

## Étape 1 — Installation d'Angular CLI 10

Dans cette étape, nous allons [installer le dernier Angular CLI 10](https://www.ahmedbouchefra.com/install-angular-cli/) (au moment de la rédaction de ce tutoriel).

[Angular CLI](https://cli.angular.io/) est l'outil officiel pour initialiser et travailler avec des projets Angular. Pour l'installer, ouvrez une nouvelle interface de ligne de commande et exécutez la commande suivante :

```bash
$ npm install -g @angular/cli

```

Au moment de la rédaction, **angular/cli v10** sera installé sur votre système.

## **Étape 2 — Création d'une nouvelle application Angular 10**

Créons maintenant notre projet. Retournez à votre interface de ligne de commande et exécutez les commandes suivantes :

```bash
$ cd ~
$ ng new angular10qrcode
```

Le CLI vous posera quelques questions :

* **Souhaitez-vous ajouter le routage Angular ?** Tapez **y** pour Oui, et 
* **Quel format de feuille de style souhaitez-vous utiliser ?** Choisissez **CSS**.

Ensuite, naviguez jusqu'au dossier de votre projet et exécutez le serveur de développement local en utilisant les commandes suivantes :

```bash
$ cd angular10qrcode
$ ng serve    
```

Ouvrez votre navigateur web et accédez à l'adresse `http://localhost:4200/` pour voir votre application en cours d'exécution.

Ensuite, ouvrez un nouveau terminal et assurez-vous de naviguer jusqu'au dossier de votre projet et exécutez la commande suivante pour installer la bibliothèque [`ngx-qrcode`](https://github.com/techiediaries/ngx-qrcode) depuis npm en utilisant la commande suivante :

```bash
$ npm install @techiediaries/ngx-qrcode
```

Ensuite, ouvrez le fichier `src/app/app.module.ts` et importez `NgxQRCodeModule` depuis `@techiediaries/ngx-qrcode` dans votre module comme suit :

```ts
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { NgxQRCodeModule } from '@techiediaries/ngx-qrcode';
import { FormsModule } from '@angular/forms';


import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    NgxQRCodeModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

Une fois la bibliothèque importée, vous pouvez utiliser le composant `ngx-qrcode` dans votre application Angular.

> Veuillez noter que nous avons également importé le `FormsModule`.

Ensuite, ouvrez le fichier `src/app/app.component.ts` et mettez-le à jour comme suit :

```ts
import { Component } from '@angular/core';
import { NgxQrcodeElementTypes, NgxQrcodeErrorCorrectionLevels } from '@techiediaries/ngx-qrcode';

@Component({
  selector: 'my-app',
  templateUrl: './app.component.html',
  styleUrls: [ './app.component.css' ]
})
export class AppComponent  {
  elementType = NgxQrcodeElementTypes.URL;
  correctionLevel = NgxQrcodeErrorCorrectionLevels.HIGH;
  value = 'https://www.techiediaries.com/';
}
```

Ensuite, ouvrez le fichier `src/app/app.component.html` et ajoutez le code suivant :

```html
<ngx-qrcode
  [elementType]="elementType"
  [errorCorrectionLevel]="correctionLevel"
  [value]="value"
  cssClass="bshadow"></ngx-qrcode>
```

Nous utilisons diverses propriétés pour configurer notre code QR telles que :

* le type, 
* le niveau de correction d'erreur,
* la valeur,
* la classe CSS.

Vous pouvez trouver plus d'informations sur ces propriétés et les autres propriétés supportées dans la documentation officielle de [`ngx-qrcode`](https://www.techiediaries.com/ngx-qrcode/).

Ensuite, ajoutez une zone de texte pour entrer la valeur que vous souhaitez encoder :

```html
<textarea [(ngModel)] = "value"></textarea>
```

Enfin, ouvrez le fichier `src/styles.css` et ajoutez les styles suivants :

```css
.bshadow {

  display: flex;
  align-items: center;
  justify-content: center;
  filter: drop-shadow(5px 5px 5px #222222);
  opacity: .5;

}

textarea {
    margin-top: 15px; 
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 250px;
    opacity: .5;
}
```

Voici une capture d'écran de notre application :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-from-2020-08-06-20-26-36.png)

C'est tout, nous avons terminé notre projet d'exemple Angular 10 qui démontre comment générer des codes QR. 

Vous pouvez nous rendre visite sur **`Techiediaries`** pour des tutoriels sur Angular et les pratiques modernes de développement web.

Vous pouvez consulter l'application que nous avons construite dans cet article en direct sur Stackblitz :

%[https://stackblitz.com/edit/angular-ngx-qrcode-example?file=src%2Fapp%2Fapp.component.ts]