---
title: Comment thématiser dynamiquement votre application Ionic et rendre vos utilisateurs
  heureux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-10T16:35:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-dynamically-theme-your-ionic-application-and-make-your-users-happy-ffa17e15dbf7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FPTVBGFH--t0AHelBsBX2g.png
tags:
- name: Ionic Framework
  slug: ionic
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
- name: UX
  slug: ux
seo_title: Comment thématiser dynamiquement votre application Ionic et rendre vos
  utilisateurs heureux
seo_desc: 'By Ryan Gordon

  Designing a sleek color scheme for your mobile application can be time consuming.
  Why not let the user choose their own favourite theme?

  This is one of my favorite features in apps. It provides a great experience for
  users who don’t wa...'
---

Par Ryan Gordon

Concevoir une palette de couleurs élégante pour votre application mobile peut prendre du temps. Pourquoi ne pas laisser l'utilisateur choisir son propre thème préféré ?

C'est l'une de mes fonctionnalités préférées dans les applications. Cela offre une excellente expérience pour les utilisateurs qui ne veulent pas être liés à un seul schéma de couleurs d'accentuation primaire ou qui souhaitent personnaliser le thème pour qu'il corresponde à leur propre style.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mCKTtAbjsDbmijNnIQPI6Q.jpeg)
_Un excellent exemple de thèmes dynamiques dans l'application ToDoist_

Dans cet article Medium, nous allons travailler sur un projet qui comportera plusieurs thèmes que l'utilisateur pourra sélectionner à l'exécution, comme ci-dessus. Lorsqu'un thème est sélectionné par l'utilisateur, idéalement ce changement devrait se produire en temps réel plutôt que de nécessiter que l'utilisateur rouvre l'application.

### Installation et prise en main

Ionic, si vous ne l'avez pas utilisé auparavant, est un framework d'application mobile qui vous permet d'écrire des applications mobiles en HTML, CSS et Typescript. Avec une base de code partagée, vous pouvez développer une application pour iOS ou Android ou la déployer en tant qu'application web.

Pour installer Ionic, ouvrez un terminal et entrez :

`npm install -g ionic@latest`

> Note : vous devez avoir [Node JS et npm](https://nodejs.org/en/download/) installés. Si vous obtenez une erreur avec le code « EACCES », vous aurez peut-être besoin de sudo ou de privilèges d'administrateur.

Pour ce tutoriel, le modèle sidemenu offre un bon point de départ. Pour générer un projet avec ce modèle, entrez cette commande dans le terminal :

`ionic start <nom de votre application> sidemenu`

![Image](https://cdn-media-1.freecodecamp.org/images/1*mLFWCTj1IhdMdMiXSI7OVg.png)
_Exemple de sortie du terminal à partir de la CLI_

Après la génération du projet, changez de répertoire avec :

`cd <nom de votre application>`

Vous avez maintenant un projet Ionic avec un sidemenu et deux pages prêtes à l'emploi ! Pour voir votre création, entrez `ionic serve` dans votre terminal.

#### Configuration des deux premiers thèmes : Todoist Red vs Noir

Pour configurer les deux premiers thèmes, nous devons suivre plusieurs étapes. Presque toutes ces étapes doivent être suivies dans l'ordre pour que les thèmes fonctionnent.

Tout d'abord, nous devons désigner un fichier SCSS qui sera utilisé lorsque le thème est appliqué. Dans le répertoire `src/theme` de votre projet, vous trouverez un fichier `variables.scss`. Les fichiers de thème respectifs sont également situés ici. Créez un nouveau fichier appelé :

```
red.theme.scss
```

Ce fichier sera utilisé pour appliquer le premier thème. À partir de ce fichier, n'importe quel style Ionic par défaut peut être remplacé. Il existe deux options pour appliquer les thèmes :

Option 1 : Styliser uniquement la barre de navigation et certains éléments

Option 2 : Appliquer le thème à tout le contenu de l'arrière-plan

Voici un exemple des deux options appliquées. Le code a un point de contrôle à mi-chemin. Si vous ne souhaitez pas styliser toute l'application, commentez le reste du code en dessous :

C'est le premier fichier SCSS créé ! Le suivant sera pour le mode sombre. Créez un autre nouveau fichier appelé :

```
noir.theme.scss
```

Ce fichier sera utilisé pour appliquer le second thème. Nous n'aurons pas besoin de changer beaucoup de choses pour que le second thème fonctionne, autre que changer les valeurs hexadécimales pour une couleur comme `#333333`.

Il est important de noter, cependant, que **nous devrons renommer** **la classe SCSS de `theme-red` en quelque chose d'unique** pour ce thème. J'appellerai le mien `theme-noir`.

L'étape suivante consiste à importer les fichiers SCSS dans l'application elle-même. Cela est important, sinon le thème ne sera pas chargé dans l'application. Rendez-vous dans le fichier `app.scss` situé à `src/app/app.scss` où vous pouvez importer le thème comme suit :

```
@import '../theme/red.theme';@import '../theme/noir.theme';
```

Maintenant que nous avons créé et importé les fichiers de thème dans le projet, le côté SCSS est pris en charge ! Passons maintenant au Typescript et au HTML.

### Changer le thème de manière programmatique

Changer le thème lui-même ne nécessitera que trois étapes supplémentaires pour une configuration simple :

* un wrapper autour de l'application
* une fonction pour changer le thème à l'exécution
* quelque chose pour maintenir l'état du thème actuel

#### La classe AppState

La classe AppState sera un composant Angular injectable qui contient le thème actuel et qui peut également être utilisé pour mettre à jour le thème.

Il n'y a pas grand-chose à son fonctionnement, autre que le fait qu'elle possède une variable d'état interne. Lorsqu'une opération Get est appelée, un clone de l'état est retourné. Lorsqu'un Set se produit, une propriété de l'état est mise à jour avec une nouvelle valeur, dans ce cas le thème.

L'AppState contiendra le thème actuel et permettra sa modification, mais il devra être importé dans le composant avec lequel vous souhaitez l'utiliser.

Lorsque qu'une application Ionic est configurée pour la première fois en utilisant la CLI, vous trouverez le code suivant dans le fichier `app.component.ts` :

```
// utilisé pour un exemple de ngFor et de navigation
```

```
this.pages = [
```

```
{ title: 'Thème Rouge par Défaut', component: HomePage },
```

```
{ title: 'Liste', component: ListPage }
```

```
];
```

Le tableau qui est affiché est utilisé pour fournir du contenu pour le sidemenu. Ce sidemenu servira de sélecteur de thème dans ce projet plutôt que de menu de navigation.

Modifiez les valeurs dans **this.pages** pour refléter les noms des thèmes que vous souhaitez que l'utilisateur voie (comme le fichier de thème qui sera appliqué, et d'autres actifs comme les fichiers d'images).

Dans cet exemple, le « fichier de thème » va être le nom de la classe CSS que nous voulons utiliser. Nous avons déjà importé les fichiers SCSS au moment où l'application est en cours d'exécution. Donc, plutôt que d'accéder au fichier lui-même, nous accédons à la classe racine dans ce fichier. Dans le cas du thème rouge, la classe `theme-noir` sera appliquée.

#### Affichage des thèmes disponibles et application du wrapper

La dernière étape que nous devons suivre sera d'ajouter un div wrapper. Ce sera l'élément de niveau supérieur dans le fichier `app.html`. Ce wrapper aura le thème choisi appliqué, permettant aux éléments enfants de recevoir également des mises à jour de style. Un exemple de cela dans `app.html` ressemblerait à ceci :

```
<!-- Wrapper sur l'application qui utilisera la thématique -->
```

```
<div class="{{global.state['theme']}}">
```

```
    // ici vous aurez le reste de app.html 
```

```
</div>
```

En termes d'affichage, si vous avez suivi les instructions ci-dessus et renommé le tableau `this.pages` en `this.themes` pour qu'il contienne vos thèmes disponibles, alors vous n'avez pas besoin de changer autre chose pour l'affichage !

Le sidemenu était à l'origine utilisé pour naviguer vers les pages disponibles dans l'application, mais maintenant c'est un excellent sélecteur de thème. Les noms de chaque thème disponible sont affichés en utilisant NgFor et une liaison de données avec le tableau `this.themes`. Le résultat sera une liste très simple qui aura le nom du thème pour chaque entrée. Lorsqu'une entrée est cliquée, ce thème sera appliqué.

Sur le [dépôt Github](https://github.com/Ryan-Gordon/ionic-dynamic-themes), vous pouvez trouver un meilleur exemple avec un indicateur de couleur à côté de chaque entrée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*X-QxmagEFaYE8JMn5w9RHA.png)

### Récapitulatif

Il est temps de faire un rapide récapitulatif de ce que nous avons fait ici. Jusqu'à présent, nous avons mis en œuvre les modifications suivantes pour que la thématique fonctionne :

* Créé des fichiers SCSS de thème pour chaque thème souhaité
* Importé les fichiers de thème créés dans le fichier Sass principal situé à `src/app/app.scss`
* Configuré une classe AppState pour maintenir le thème actuellement appliqué
* Configuré une fonction changeTheme très petite qui définira un nouveau thème dans AppState
* Ajouté un élément wrapper sur le `app.html` qui aura le thème appliqué

Pour créer plus de thèmes à partir de là, copiez l'un des fichiers de thème que vous avez déjà créés, renommez-le et changez les valeurs de couleur hexadécimales dans ce nouveau fichier. Vous pouvez en faire autant que vous le souhaitez ! Assurez-vous simplement d'importer également ce nouveau fichier de thème dans `app.scss` comme vous l'avez fait avec les premiers, sinon cela ne fonctionnera pas.

Avec ces cinq étapes, vous pouvez avoir une thématique dynamique dans n'importe quelle application Ionic. La beauté de la solution est qu'elle fonctionne bien sur toutes les plateformes puisqu'elle n'utilise aucun plugin natif — tout est en HTML, CSS et TS.

En bonus, sur le [dépôt GitHub](https://github.com/Ryan-Gordon/ionic-dynamic-themes), j'ai implémenté deux autres façons de présenter les thèmes disponibles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FPTVBGFH--t0AHelBsBX2g.png)
_Option 2 à gauche et une option modèle à droite_

### Conclusion :

La thématique dynamique nous évite de nous soucier de savoir si notre schéma de couleurs choisi conviendra à tous les publics. Au lieu de faire de nombreuses maquettes avec différents schémas pour évaluer, nous pouvons simplement implémenter tous les schémas de couleurs et laisser l'utilisateur choisir celui qu'il préfère à l'exécution.

Un avantage caché de cela est que nous pouvons collecter des analyses de nos utilisateurs sur le thème qui leur convient le mieux. Dans la fonction `changeTheme` discutée, un webhook ou un événement pourrait être envoyé spécifiant le choix de l'utilisateur. Grâce à cela, les développeurs pourraient recueillir des retours réels des utilisateurs sur les thèmes qui « fonctionnent » et ceux qui ne fonctionnent pas.

Tout le code source de ce tutoriel peut être trouvé dans ce [dépôt Github](https://github.com/Ryan-Gordon/ionic-dynamic-themes).

![Image](https://cdn-media-1.freecodecamp.org/images/1*LGQFvGWTml9dQTsUJO-s8g.png)
_Un dernier regard_

Veuillez envisager de laisser une étoile sur le dépôt. J'accueille favorablement toutes les additions.