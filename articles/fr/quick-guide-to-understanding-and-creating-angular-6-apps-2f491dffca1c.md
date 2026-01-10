---
title: Un guide rapide pour vous aider à comprendre et créer des applications Angular
  6
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-10T16:14:17.000Z'
originalURL: https://freecodecamp.org/news/quick-guide-to-understanding-and-creating-angular-6-apps-2f491dffca1c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*NJiF_4tVYO3O5EhM
tags:
- name: Angular
  slug: angular
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Un guide rapide pour vous aider à comprendre et créer des applications
  Angular 6
seo_desc: 'By Aditya Sridhar

  This post is divided into two parts:

  The first part demonstrates how to create a simple Angular 6 App using Angular CLI
  and explains the project structure.

  The second part explains existing code that I have posted in GitHub. This co...'
---

Par Aditya Sridhar

Cet article est divisé en deux parties :

La première partie démontre comment créer une application Angular 6 simple en utilisant Angular CLI et explique la structure du projet.

La deuxième partie explique le code existant que j'ai publié sur GitHub. Ce code démontre l'utilisation des composants, des services, du client HTTP et de la communication entre les composants.

### Partie 1

#### Installer Node.js si ce n'est pas déjà fait

Vous avez besoin de Node.js, car les bibliothèques requises pour Angular sont téléchargées à l'aide du gestionnaire de paquets node (npm). Référez-vous à [https://nodejs.org/en/](https://nodejs.org/en/) pour installer Node.js.

#### Installer Angular CLI

Angular CLI est une interface en ligne de commande pour Angular, et est très utile pour créer rapidement un modèle de projet Angular 6. Installez le paquet npm Angular CLI globalement en utilisant la commande suivante :

```bash
npm install -g @angular/cli
```

#### Créer le Projet

Angular CLI aide à créer un projet très facilement. Pour créer le projet, utilisez la commande suivante.

```bash
ng new simple-angular6-app
```

**simple-angular6-app** est le nom du projet. Vous remarquerez maintenant qu'un dossier nommé **simple-angular6-app** est créé. Ce dossier est le projet qui a été créé. Pour tester si tout a été correctement configuré, allez dans le dossier du projet et exécutez l'application en utilisant les commandes suivantes :

```bash
cd simple-angular6-app
npm start
```

Allez dans votre navigateur et accédez à l'URL suivante : **localhost:4200**. Vous devriez pouvoir voir que votre application est en cours d'exécution.

L'application devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/HBxcPkVdbdA0Bt0XLfs7cnnpuyyOU4DUIG0Z)

#### Structure de Dossier de Base Expliquée

Lorsque vous créez le projet, vous remarquerez qu'il crée un ensemble de fichiers. Voici quelques-uns des fichiers et dossiers importants dont vous devez être conscient :

1. **package.json** : Ce fichier contient la liste des dépendances node nécessaires.
2. **src/styles.css** : Ce fichier contient le CSS global disponible dans toute l'application.
3. **src/main.ts** : Ce fichier est le fichier principal qui démarre l'application Angular (AppModule est initialisé ici comme on peut le voir dans le code). Ici, l'extension .ts signifie TypeScript.
4. **src/index.html** : Ce fichier est le premier fichier qui s'exécute avec main.ts lorsque la page se charge.
5. **src/app/app.module.ts** : Ce fichier est l'endroit où tous les composants, fournisseurs et modules sont définis. Sans les définir ici, ils ne peuvent pas être utilisés ailleurs dans le code.
6. **src/app/app.component.html** : Ce composant est le composant principal d'une application Angular, et tous les autres composants sont généralement présents dans ce composant. **src/app/app.component.ts** est la logique de ce composant, et **src/app/app.component.css** est le CSS de ce composant. Ce composant lui-même ne fait aucune logique importante, mais agit comme un conteneur pour d'autres composants.
7. **dist** : Ce dossier contient les fichiers compilés. TypeScript est essentiellement converti en JavaScript et les fichiers résultants sont stockés ici après le bundling et la minification. (Ce dossier n'apparaît que si l'application est compilée. Un simple "npm start" ne créera pas ce dossier.) Puisque les navigateurs web ne comprennent que JavaScript (au moins pour l'instant), il est donc nécessaire de convertir TypeScript en JavaScript avant de déployer le code. Pour voir ce dossier, vous pouvez taper la commande suivante :

```bash
npm run build
```

Il y a plusieurs autres fichiers, mais connaître ces fichiers de base est un bon début.

#### TypeScript

Angular 6 utilise TypeScript pour implémenter la logique. Ceux d'entre vous qui ont travaillé avec Java trouveront TypeScript très facile. TypeScript est un langage construit sur JavaScript mais qui est sécurisé en termes de types, et TypeScript se compile en JavaScript.

#### Création de Composants et Services

1. **Composant** : Un composant dans Angular effectue une fonction spécifique. Une application Angular est construite en utilisant divers composants. Angular CLI peut être utilisé pour créer des composants facilement. La syntaxe est **ng generate component [nom]**. Utilisez la commande suivante pour créer un composant appelé "customers".

```bash
ng generate component customers
```

2. La commande ci-dessus crée un dossier appelé **customers** à l'intérieur de **src/app**. Le composant créé contient :

* un fichier **customers.component.html** pour décider du modèle (comment l'interface utilisateur du composant doit apparaître)
* un fichier **customers.component.ts** qui contient la logique
* un fichier **customers.component.css** qui contient le contenu CSS
* et un fichier **customers.component.spec.ts** qui est utilisé pour les tests unitaires (les spécifications ne seront pas expliquées dans cet article).

3. **Service** : Un service fournit essentiellement des fonctionnalités qui peuvent être utilisées par n'importe quel composant. Le service peut être partagé entre tous les composants, ou il peut être restreint à un composant particulier (toute logique réutilisable peut être mise dans un service). Angular CLI peut également être utilisé pour créer des services. La syntaxe est **ng generate service [nom]**. Utilisez la commande suivante pour créer un service appelé "data" :

```bash
ng generate service data
```

4. Le service est créé à l'intérieur de **src/app**. Le service créé contient un fichier **data.service.ts** qui contient la logique et un fichier **data.service.spec.ts** pour les tests unitaires.

### **Félicitations** ?

Vous avez créé avec succès votre première application Angular 6 et avez également appris à créer des composants et des services. Maintenant, vous avez également appris la structure de dossier de base d'un projet Angular 6. La partie suivante expliquera le code GitHub existant pour démontrer comment utiliser les composants, les services, le client HTTP et la communication entre les composants.

### Partie 2

#### Code

[Ce code](https://github.com/aditya-sridhar/simple-angular6-app) est expliqué ici, alors clonez le dépôt sur votre machine locale. Le dépôt contient des instructions sur la façon de le cloner et de le configurer.

#### URL de l'Application

Pour voir à quoi ressemble l'application finale, vous pouvez cliquer sur [cette URL](https://aditya-sridhar.github.io/simple-angular6-app/). Cela vous donnera une bonne idée de ce que l'application essaie de faire.

L'application ressemblerait à ceci sur un écran mobile :

![Image](https://cdn-media-1.freecodecamp.org/images/r31wXEDd34foI8fcVwbjw7xv16jQ6RcfVUlM)

#### Que Fait Cette Application ?

Le but de l'application est d'afficher une liste de clients sous forme de cartes. Lorsque les données du client sont cliquées, l'application bascule vers une nouvelle page qui affiche ensuite les détails du client sélectionné.

#### Structure de l'Application Expliquée

**Les Composants Créés sont :**

1. **CustomersComponent** : Cela correspond au dossier **src/app/customers**. Ce composant est utilisé pour afficher la liste des clients. Le fichier **customers.component.ts** contient une fonction appelée **ngOnInit()**. Cette fonction est appelée chaque fois que le composant est chargé. Cette fonction peut donc être utilisée pour charger les données du composant. Ces données sont chargées en appelant la fonction **getCustomerList()**. **getCustomerList()** appelle à son tour le service de données pour obtenir les données nécessaires.
2. **CustomerdetailsComponent** : Cela correspond au dossier **src/app/customerdetails**. Ce composant affiche les détails d'un client sélectionné. Le fichier **customerdetails.component.ts** contient la fonction **ngOnInit()** qui peut être utilisée pour charger les données. Pour charger les données, la fonction **getCustomerDetails()** est appelée. Cette fonction fait un appel au service de données pour obtenir les données nécessaires. Mais ici, vous remarquerez également l'utilisation de **routeParams.id** qui est envoyé au service. **routeParams** est utilisé pour obtenir les paramètres de l'URL de l'application, et le paramètre **id** est utilisé pour déterminer pour quel client les détails doivent être chargés. Cela deviendra plus clair lorsque j'aborderai la partie routage.
3. **DisplayComponent** : Cela correspond au dossier **src/app/display**. Ce composant affiche le nom du client cliqué dans le **CustomersComponent**. (Le but de ce composant est de démontrer la communication entre composants parent et enfant.) C'est un composant enfant de **CustomersComponent**. Dans **customers.component.html**, vous remarquerez que **<app-display [customer] = selectedCustomer> </app-display>**. Cela fait de DisplayComponent un composant enfant de **CustomersComponent**. Les données sont passées de **CustomerComponent** à **DisplayComponent** en utilisant l'attribut **[customer]**.

#### **Les Données d'Exemple**

Les données d'exemple sont présentes dans le dossier **src/assets/samplejson**.

**Les services créés sont :**

1. **DataService** : Cela correspond à **src/app/data.service.ts**. Tout le JSON utilisé dans l'application est stocké dans le dossier **src/assets/samplejson**. DataService aide à obtenir le JSON du dossier **src/assets/samplejson** en utilisant une requête HTTP. Dans les applications réelles, le service aide à obtenir les données d'une API Rest ou de toute autre API en faisant une requête HTTP. Ce service est utilisé à la fois par le **CustomersComponent** et le **CustomerdetailsComponent**.

**Les classes de modèle utilisées sont :**

1. **Customer** : Cela correspond à **src/app/customer.ts**. Il s'agit de la classe de modèle utilisée pour le **CustomersComponent** pour définir la structure de chaque client dans la liste.
2. **CustomerDetails** : Cela correspond à **src/app/customerdetails.ts**. Il s'agit de la classe de modèle utilisée pour **CustomerdetailsComponent** pour définir la structure contenant tous les détails du client.

#### **Module de Routage**

Le module de routage est défini dans **src/app/app-routing.module.ts**. Ce module est ensuite appliqué à l'application en ajoutant `<router-outlet></router-outlet>` dans app.component.html.

Il y a 2 routes présentes dans l'application :

1. **/customers** : Cette URL affiche la liste des clients et pointe vers **CustomersComponent**.
2. **/customerdetails/:id** : Cette URL affiche les détails de chaque client et pointe vers **CustomerdetailsComponent**. L'**id** présent dans cette URL est le routeParam. Cet **id** est à son tour utilisé par le **CustomerdetailsComponent** pour savoir les détails de quel client afficher. Par exemple, **/customerdetails/1** affichera les détails du premier client, **/customerdetails/3** affichera les détails du 3ème client, et ainsi de suite.

### **Félicitations encore** ?

Maintenant, vous savez comment utiliser les composants et les services. Vous savez également comment faire des appels HTTP, comment utiliser le routage et comment passer des routeParams.

Les concepts de base ont été couverts dans cet article, et j'espère qu'il a été utile.

### Références :

1. Pour en savoir plus sur Angular, vous pouvez consulter la documentation [https://angular.io/guide/quickstart](https://angular.io/guide/quickstart). La documentation est très utile pour comprendre les concepts avancés d'Angular.

#### À propos de l'auteur

J'aime la technologie et je suis les avancées technologiques. J'aime aussi aider les autres avec les connaissances que j'ai dans le domaine de la technologie.

N'hésitez pas à me contacter sur mon compte LinkedIn [https://www.linkedin.com/in/aditya1811/](https://www.linkedin.com/in/aditya1811/)

Vous pouvez également me suivre sur Twitter [https://twitter.com/adityasridhar18](https://twitter.com/adityasridhar18)

Mon site web : [https://adityasridhar.com/](https://adityasridhar.com/)

#### Autres articles connexes de moi

[Un guide rapide pour vous aider à comprendre et créer des applications ReactJS](https://medium.freecodecamp.org/quick-guide-to-understanding-and-creating-reactjs-apps-8457ee8f7123)

[Une introduction rapide à Vue.js](https://medium.freecodecamp.org/a-quick-introduction-to-vue-js-72937ee8880d)