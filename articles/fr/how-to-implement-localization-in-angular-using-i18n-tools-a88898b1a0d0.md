---
title: Comment implémenter la localisation dans Angular en utilisant les outils i18n
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-08T17:39:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-localization-in-angular-using-i18n-tools-a88898b1a0d0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ov4vHlZxjYYJ_QigtwzXdQ.jpeg
tags:
- name: Angular
  slug: angular
- name: i18n
  slug: i18n
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment implémenter la localisation dans Angular en utilisant les outils
  i18n
seo_desc: 'By Ankit Sharma

  Introduction

  In this article, we will learn how to make our Angular app available in different
  languages using i18n and localization. We will create an Angular application and
  configure it to serve the content in three different langu...'
---

Par Ankit Sharma

### Introduction

Dans cet article, nous allons apprendre comment rendre notre application Angular disponible dans différentes langues en utilisant i18n et la localisation. Nous allons créer une application Angular et la configurer pour servir le contenu dans trois langues différentes. Nous allons également déployer notre application sur Google Firebase et voir comment la localisation fonctionne en temps réel.

Nous allons utiliser Angular 7 et VS Code pour développer notre application. Voici un aperçu de la sortie de l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/0e2O3oZyXvSnQWEfH-a3dDFoLaHZFrV5-Vtw)

### Code source

Obtenez le code source de cette application depuis [GitHub](https://github.com/AnkitSharma-007/angular-i18n-localization).

### Qu'est-ce que i18n ?

`I18n`, également connu sous le nom d'internationalisation, est le processus qui permet à notre application de supporter diverses langues afin d'atteindre un public mondial.

### Qu'est-ce que la localisation ?

La localisation est le processus de traduction de l'application dans une langue particulière. Nous devons appliquer l'internationalisation à l'application et ensuite nous pouvons la localiser. La localisation nous permet de servir notre application dans différentes langues.

### Création d'une application Angular 7

La première étape consiste à créer une application Angular 7. Si vous êtes nouveau dans Angular, je vous suggère de lire mon article [Getting Started With Angular 7.0](https://ankitsharmablogs.com/getting-started-with-angular-7-0/) pour apprendre comment configurer l'environnement de développement Angular sur votre machine.

Exécutez la commande suivante pour créer l'application.

```
ng new i18nDemo
```

Ouvrez l'application i18nDemo en utilisant VS Code.

### Configuration du composant de l'application

Ouvrez le fichier `app.component.html`. Remplacez le texte existant par le code suivant.

```
<h1 i18n>  Démonstration de localisation dans Angular en utilisant i18n</h1><h3 i18n="@@myName">  Bonjour, je m'appelle Ankit</h3><p>Ce texte restera le même dans toutes les langues</p><hr />
```

Vous pouvez observer que nous avons marqué les balises `<h1>` et `<h3>` avec l'attribut i18n. C'est une façon de dire à Angular de considérer ce texte comme un contenu traduisible. Nous explorerons l'attribut i18n en détail dans la section suivante.

### Création d'un fichier source de traduction

Exécutez la commande suivante dans le CLI pour créer un fichier source de traduction.

```
ng xi18n --output-path translate
```

Il créera un dossier appelé translate et un fichier `messages.xlf` à l'intérieur. Ouvrez le fichier et vous pouvez observer le code XML suivant à l'intérieur.

```
<?xml version="1.0" encoding="UTF-8" ?><xliff version="1.2" xmlns="urn:oasis:names:tc:xliff:document:1.2">  <file source-language="en" datatype="plaintext" original="ng2.template">    <body>      <trans-unit id="3f2feb6d5fb690628177afa3ade2519db69ba838" datatype="html">        <source>Localization Demo in Angular using i18n</source>        <context-group purpose="location">          <context context-type="sourcefile">app/app.component.html</context>          <context context-type="linenumber">1</context>        </context-group>      </trans-unit>      <trans-unit id="myName" datatype="html">        <source>Hello, My name is Ankit</source>        <context-group purpose="location">          <context context-type="sourcefile">app/app.component.html</context>          <context context-type="linenumber">5</context>        </context-group>      </trans-unit>    </body>  </file></xliff>
```

Ce fichier contient une liste de balises `<trans-unit>`. Ces balises contiendront tout le contenu qui a été marqué pour la traduction en utilisant l'attribut i18n. Vous pouvez également observer que chaque balise `<trans-unit>` a une propriété id associée. Cet identifiant unique sera généré par défaut pour chaque balise marquée avec l'attribut i18n. Nous pouvons également personnaliser l'identifiant en fournissant un nom préfixé avec @@ comme nous l'avons fait avec la balise `<h3>` dans la section précédente. Par conséquent, l'identifiant pour la balise `<h3>` est « myName » comme nous l'avons défini.

Il n'y a pas d'entrée pour la balise `<p>` dans le fichier de traduction car nous ne l'avons pas marquée avec l'attribut i18n. L'outil de traduction Angular ne la prendra pas en compte pour les traductions.

Si vous modifiez le texte de toute balise dans votre fichier HTML, vous devez régénérer le fichier de traduction. La régénération du fichier remplacera l'identifiant par défaut des balises `<trans-unit>`. Par conséquent, il est conseillé de fournir des identifiants personnalisés à chaque balise traduisible pour maintenir la cohérence.

Ainsi, nous avons implémenté avec succès i18n dans notre application. Dans la section suivante, nous allons l'étendre pour la rendre disponible dans différentes langues.

### Traduction du contenu

Nous allons traduire notre application dans deux nouvelles langues en plus de l'anglais, qui sont l'espagnol et l'hindi. Faites trois copies du fichier messages.xlf et renommez-les en `messages.en.xlf`, `messages.es.xlf` et `messages.hi.xlf`. Ces noms de fichiers peuvent être personnalisés selon votre choix, mais l'extension doit être `.xlf`.

Ouvrez messages.es.xlf et mettez-y le contenu suivant.

```
<?xml version="1.0" encoding="UTF-8" ?><xliff version="1.2" xmlns="urn:oasis:names:tc:xliff:document:1.2">  <file source-language="en" datatype="plaintext" original="ng2.template">    <body>      <trans-unit id="3f2feb6d5fb690628177afa3ade2519db69ba838" datatype="html">        <source>Localization Demo in Angular using i18n</source>        <target>Demostración de localización en Angular usando i18n</target>        <context-group purpose="location">          <context context-type="sourcefile">app/app.component.html</context>          <context context-type="linenumber">1</context>        </context-group>      </trans-unit>      <trans-unit id="myName" datatype="html">        <source>Hello, My name is Ankit</source>        <target>Hola, mi nombre es Ankit</target>        <context-group purpose="location">          <context context-type="sourcefile">app/app.component.html</context>          <context context-type="linenumber">5</context>        </context-group>      </trans-unit>    </body>  </file></xliff>
```

C'est le même contenu que le fichier messages.xlf original, mais nous avons ajouté une balise `<target>` correspondant à chaque balise `<source>`. La balise `<target>` contient le texte traduit pour le contenu à l'intérieur de la balise `<source>`. Ici, j'utilise Google Translate pour la traduction, mais dans les applications en temps réel, un expert linguistique traduira les contenus du fichier messages.xlf.

De même, ouvrez messages.hi.xlf et mettez-y le contenu suivant.

```
<?xml version="1.0" encoding="UTF-8" ?><xliff version="1.2" xmlns="urn:oasis:names:tc:xliff:document:1.2">  <file source-language="en" datatype="plaintext" original="ng2.template">    <body>      <trans-unit id="3f2feb6d5fb690628177afa3ade2519db69ba838" datatype="html">        <source>Localization Demo in Angular using i18n</source>        <target>I18n का उपयोग करके Angular में स्थानीयकरण डेमो</target>        <context-group purpose="location">          <context context-type="sourcefile">app/app.component.html</context>          <context context-type="linenumber">1</context>        </context-group>      </trans-unit>      <trans-unit id="myName" datatype="html">        <source>Hello, My name is Ankit</source>        <target>हेलो, मेरा नाम अंकित है</target>        <context-group purpose="location">          <context context-type="sourcefile">app/app.component.html</context>          <context context-type="linenumber">5</context>        </context-group>      </trans-unit>    </body>  </file></xliff>
```

Enfin, nous allons créer le fichier de traduction en anglais. Ouvrez messages.en.xlf et mettez-y le contenu suivant.

```
<?xml version="1.0" encoding="UTF-8" ?><xliff version="1.2" xmlns="urn:oasis:names:tc:xliff:document:1.2">  <file source-language="en" datatype="plaintext" original="ng2.template">    <body>      <trans-unit id="3f2feb6d5fb690628177afa3ade2519db69ba838" datatype="html">        <source>Localization Demo in Angular using i18n</source>        <target>Localization Demo in Angular using i18n</target>        <context-group purpose="location">          <context context-type="sourcefile">app/app.component.html</context>          <context context-type="linenumber">1</context>        </context-group>      </trans-unit>      <trans-unit id="myName" datatype="html">        <source>Hello, My name is Ankit</source>        <target>Hello, My name is Ankit</target>        <context-group purpose="location">          <context context-type="sourcefile">app/app.component.html</context>          <context context-type="linenumber">5</context>        </context-group>      </trans-unit>    </body>  </file></xliff>
```

### Configurer l'application pour servir plusieurs langues

Ouvrez le fichier `angular.json` et ajoutez la configuration suivante.

```
"build": {  ...  "configurations": {    ...    "es": {      "aot": true,      "i18nFile": "src/translate/messages.es.xlf",      "i18nFormat": "xlf",      "i18nLocale": "es",      "i18nMissingTranslation": "error"    }  }},"serve": {  ...  "configurations": {    ...    "es": {      "browserTarget": "i18nDemo:build:es"    }  }}
```

Ici, nous avons ajouté la configuration pour la langue espagnole. Nous avons fourni le chemin et le format du fichier i18n et défini la locale sur « es ». Lorsque nous exécutons l'application, le contenu de l'application sera servi à partir du chemin du fichier i18n fourni.

De même, vous pouvez ajouter la configuration pour d'autres langues.

### Démonstration d'exécution

Une fois que vous avez ajouté la configuration pour toutes les langues dans le fichier angular.json, exécutez la commande suivante pour démarrer le serveur.

```
ng serve --configuration=es
```

Cela lancera l'application en configuration « es » et notre application affichera les traductions en espagnol.

Voir l'écran de sortie comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/MhSiyU2dmWORN8ApRVKLaQ0eXuxmeNIWGtzg)

Les configurations que nous avons définies ne permettront à l'application de fonctionner que sur la machine locale. Nous ne pouvons pas changer la configuration une fois l'application lancée.

Une application de production aura besoin que l'application serve différentes langues simplement en changeant l'URL. Par exemple, `mywebsite.com/es` fournira la version espagnole du site, et `mywebsite.com/en` fournira la version anglaise. Dans ce cas, l'application sera servie à partir de différents répertoires virtuels pour différentes langues. Nous explorerons comment faire cela dans la section suivante.

### Modifier le composant de l'application pour la production

Ouvrez `app.component.ts` et mettez-y le code suivant.

```
import { Component, LOCALE_ID, Inject } from '@angular/core';@Component({  selector: 'app-root',  templateUrl: './app.component.html',  styleUrls: ['./app.component.css']})export class AppComponent {  title = 'i18nDemo';  languageList = [    { code: 'en', label: 'English' },    { code: 'hi', label: 'हिंदी' },    { code: 'es', label: 'Español' }  ];  constructor(@Inject(LOCALE_ID) protected localeId: string) { }}
```

Ici, nous avons défini une liste de langues et leurs codes de locale. Ces codes de locale sont des codes standard. Vous pouvez facilement obtenir une liste de langues et les codes de locale correspondants par une simple recherche Google.

Ajoutez le code suivant dans le fichier `app.component.html`.

```
<ng-container *ngFor="let language of languageList"> <a href="/{{language.code}}/"> <button class="button">{{language.label}}</button> </a></ng-container>
```

Ici, nous avons défini trois boutons pour trois langues. À chaque clic sur un bouton, l'identifiant de la locale changera et l'identifiant de la locale sera ajouté à l'URL également. Cela nous permettra de servir l'application à partir d'un répertoire différent.

Mettez le code suivant dans le fichier `app.component.css` pour appliquer des styles à ces boutons.

```
.button {  background-color: darkslateblue;  border-radius: 5px;  color: white;  padding: 5px;  width: 10%;  margin: 5px;  text-decoration: none;  cursor: pointer;}
```

### Script pour compiler l'application pour la production

Nous devons avoir trois emplacements de service différents pour trois langues différentes. Pour construire le package de l'application pour une langue pour la production, nous utiliserons la commande suivante :

```
ng build --prod --i18n-locale es --i18n-format xlf --i18n-file src/translate/messages.es.xlf --output-path=dist/es --baseHref /es/
```

Comprenons cette commande. Nous avons fourni l'identifiant de la locale pour le package, qui est « es » pour l'espagnol. Nous fournissons également le chemin du fichier i18n et le format. La propriété output-path est nécessaire pour fournir l'emplacement du package de l'application. La propriété baseHref spécifie l'URL de base à partir de laquelle ce package sera servi.

Nous devons exécuter cette commande pour chaque langue que nous fournirons en changeant les valeurs du chemin du fichier i18n et de l'attribut `baseHref`. Cependant, cela sera une tâche fastidieuse si nous avons beaucoup de langues. Par conséquent, nous allons écrire un script pour générer un package pour toutes les langues. Ouvrez le fichier `package.json` et ajoutez les scripts suivants dans la section « scripts ».

```
"build-locale:en": "ng build --prod --i18n-locale en --i18n-format xlf --i18n-file src/translate/messages.en.xlf --output-path=dist/en --baseHref /en/","build-locale:es": "ng build --prod --i18n-locale es --i18n-format xlf --i18n-file src/translate/messages.es.xlf --output-path=dist/es --baseHref /es/","build-locale:hi": " ng build --prod --i18n-locale hi --i18n-format xlf --i18n-file src/translate/messages.hi.xlf --output-path=dist/hi --baseHref /hi/","build-locale": "npm run build-locale:en && npm run build-locale:es && npm run build-locale:hi"
```

Ici, nous avons créé trois scripts pour les trois langues que nous utilisons. Le script « build-locale » les exécutera tous à la fois. Tous ces scripts sont des paires clé-valeur. Les noms de clés que nous utilisons ici sont personnalisables et vous pouvez utiliser n'importe quel nom de votre choix. Pour créer le package de l'application pour toutes les langues, exécutez la commande suivante :

```
npm run build-locale
```

Après une exécution réussie, il créera un dossier « dist » dans le dossier racine de l'application. Le dossier dist contient trois sous-dossiers pour servir notre application dans trois langues différentes. Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/P1mWtTZoaGhfnY9SiqfQbgWiuIVszUDlhvpo)

### Déploiement de l'application sur Firebase

Nous allons déployer cette application sur Firebase pour voir le changement de langue en temps réel. Consultez mon article [Hosting A Blazor Application on Firebase](https://ankitsharmablogs.com/hosting-a-blazor-application-on-firebase/) et suivez les étapes mentionnées pour déployer cette application Angular sur Firebase.

Une fois l'application déployée, vous obtiendrez l'URL d'hébergement. Ouvrez l'URL et ajoutez l'attribut baseHref comme nous l'avons défini précédemment, à l'URL. Ainsi, l'URL sera `yoursite.com/es/` pour la langue espagnole et ainsi de suite.

L'application que nous avons construite ici est hébergée à l'adresse [https://i18ndemo-415ef.firebaseapp.com/en/](https://i18ndemo-415ef.firebaseapp.com/en/). Si vous ouvrez cette URL, vous verrez la sortie comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/x2T6UIVUkrAKqr7yqXy7ZL6dSqwyZ592UKt0)

Cliquez sur les liens fournis. L'URL changera et l'application se rechargera dans la nouvelle langue.

### Conclusion

Dans cet article, nous avons appris comment internationaliser notre application Angular en utilisant les outils i18n. Nous avons également appliqué la localisation à notre application Angular. La localisation nous permet de servir notre application dans différentes langues, ce qui aide à étendre la portée à un public mondial. Nous avons également appris comment la localisation fonctionne dans un environnement de production en déployant notre application sur Firebase.

Obtenez le code source depuis [GitHub](https://github.com/AnkitSharma-007/angular-i18n-localization) et jouez avec pour une meilleure compréhension.

Vous préparez des entretiens ?! Lisez mon article sur [C# Coding Questions For Technical Interviews](https://ankitsharmablogs.com/csharp-coding-questions-for-technical-interviews/)

### Voir aussi

* [Comprendre Blazor côté serveur](https://ankitsharmablogs.com/understanding-server-side-blazor/)
* [Comprendre les animations Angular 6](https://ankitsharmablogs.com/understanding-angular-6-animations/)
* [ASP.NET Core — Utilisation de Highcharts avec Angular 5](https://ankitsharmablogs.com/asp-net-core-using-highcharts-with-angular-5/)
* [ASP.NET Core — CRUD utilisant Angular 5 et Entity Framework Core](https://ankitsharmablogs.com/asp-net-core-crud-using-angular-5-and-entity-framework-core/)
* [Opérations CRUD avec ASP.NET Core en utilisant Angular 5 et ADO.NET](https://ankitsharmablogs.com/crud-operations-asp-net-core-using-angular-5-ado-net/)

Publié à l'origine sur [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)