---
title: Comment planifier trois jours à l'avance avec React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-16T16:04:46.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-plan-three-days-ahead-with-react-99ca0f8eb0f6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MEInIgK_vlkZg3b0v-WPHg.jpeg
tags:
- name: beginner
  slug: beginner
- name: code
  slug: code
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Comment planifier trois jours à l'avance avec React
seo_desc: 'By Mohit Jain

  Today we’ll be making a ‘to-do’ website… with some different features.

  You can check the live demo of what we will be making here.

  For the front end, we will be using React.js. React.js is a component based library
  which is used to deve...'
---

Par Mohit Jain

Aujourd'hui, nous allons créer un site web de "to-do"... avec quelques fonctionnalités différentes.

Vous pouvez consulter la démonstration en direct de ce que nous allons créer [ici](https://mohit0101.github.io/next-3-days-plan-browser-homepage/).

Pour le front-end, nous utiliserons React.js. React.js est une bibliothèque basée sur les composants qui est utilisée pour développer des interfaces utilisateur (UI) interactives.

Pour le back-end et le stockage, nous utiliserons le stockage local du navigateur. Cela nous permet de sauvegarder des données afin que, la prochaine fois que nous ouvrirons notre site, nous puissions accéder aux données que nous avons sauvegardées précédemment.

#### Create-React-App

Commençons. Tout d'abord, vous devez configurer Node (un environnement d'exécution JavaScript multiplateforme) et React.

Vous pouvez télécharger et installer Node depuis le [site web de node.js](https://nodejs.org/en/). Après cela, ouvrez le terminal et utilisez la commande `cd` pour accéder au répertoire où vous souhaitez sauvegarder le projet. Ensuite, exécutez ces deux commandes :

```
npm install -g create-react-app
```

```
create-react-app next-3-days-planner
```

`npm install` est une commande pour installer des packages npm, et le drapeau `-g` permet d'installer le package globalement dans notre système.

`create-react-app` va configurer un nouveau répertoire de projet. Il prend également en charge toutes les choses nécessaires à React comme webpack, babel et JSX afin que les débutants n'aient pas à se soucier de la configuration de leur projet initial.

Je nomme ce projet `next-3-day-planner` mais vous pouvez le nommer comme vous le souhaitez.

Ouvrez le répertoire du projet dans votre éditeur de code préféré.

#### Le composant parent

Maintenant, créons notre composant parent. Ouvrez le fichier `App.js` et supprimez tout. Ajoutez ce snippet de code :

Dans les deux premières lignes, nous importons la classe `React`, qui nous aide à créer des composants. Nous importons également `ReactDOM` qui aide à rendre les composants dans le DOM (modèle d'objet de document).

Nous avons également importé le composant `Header`, qui sera utilisé pour afficher la barre d'en-tête du site web.

Le composant `Textbox` contiendra la section d'entrée où l'utilisateur tapera son élément "todo".

Ensuite, nous importons quelques autres composants enfants. Ce sont `DisplayToday`, `DisplayTomorrow`, `DisplayDayAfterTomorrow`. Ces trois composants nous aident à afficher notre liste de tâches.

Si vous voyez une erreur, ne vous inquiétez pas. Nous n'avons pas encore défini ces composants !

Ensuite, nous définissons notre composant `App`, qui est notre composant parent.

Ce composant a un état qui sera utilisé pour stocker des données. La clé `Today` sera utilisée pour stocker la liste des éléments de tâches qui doivent être accomplis aujourd'hui. La même chose s'applique pour les clés `Tomorrow` et `Day_After_Tomorrow`.

`updateEntry()`, `deleteEntry()` sont deux fonctions utilisées pour ajouter des éléments aux listes et pour supprimer un élément des listes. Nous allons les définir maintenant.

#### Mise à jour des entrées de liste

La fonction `updateEntry()` prend deux paramètres.

`term` est le nouvel élément de tâche que nous devons sauvegarder, et `day` est le "jour" dans lequel nous voulons ajouter cet élément de tâche.

Nous avons un bloc if-else, qui vérifie la valeur de `day` et ajoute cet élément de tâche à ce tableau particulier.

Les trois points `...` avant `this.state.Today` nous aident à concaténer le tableau avec de nouvelles valeurs.

#### Suppression des entrées

Codons la fonction de suppression :

La fonction `deleteEntry()` sera déclenchée chaque fois que l'utilisateur clique sur le bouton "supprimer l'élément" sur la page.

La fonction `deleteEntry()` prend deux paramètres.

`index` est l'emplacement d'index de l'élément dans le tableau qui doit être supprimé. Le deuxième paramètre est `day`, qui est le jour à partir duquel nous voulons supprimer l'entrée.

Pour implémenter la logique de suppression d'une entrée du tableau, nous utiliserons la fonction `filter()` de JavaScript.

Cette fonction parcourt chaque élément du tableau et retourne l'élément si la logique que nous définissons correspond à vrai.

Ensuite, nous mettons à jour la valeur de `state` en utilisant la méthode `setState()`, qui ré-affiche le DOM par défaut.

#### Fonction de rendu

Codons la fonction `render` de notre composant `App`.

Ici, nous avons mentionné tous nos composants enfants (_que nous coderons plus tard...) et passé quelques attributs à chaque balise.

Le `Header` reçoit un attribut `nam` qui fait référence à `this.state.username`. C'est le nom d'utilisateur que nous avons défini dans l'état.

`Textbox` reçoit l'attribut `updateEntry` qui fait référence à la fonction `this.updateEntry` que nous avons définie ci-dessus.

N'oubliez pas d'ajouter cette ligne à la fin de `App.js` afin que nous puissions voir notre sortie dans l'écran du navigateur :

```
export default App;
```

### Composants enfants

Créez un nouveau répertoire à l'intérieur de `src` et nommez-le `Components`.

Ensuite, créez trois nouveaux fichiers nommés `Display.js`, `Header.js` et `Textbox.js` à l'intérieur du répertoire `Components`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_fE56JXq7GVv6qgHb_Ko6A.png)

### Composant Header

Commençons par le fichier `src/Components/Header.js` :

Notre en-tête est très simple. Il affiche simplement le nom d'utilisateur que nous avons passé en tant qu'attribut. Il accède à cet attribut en utilisant `this.props.nam`.

Les attributs `className` étranges que vous voyez ne sont rien d'autre que des attributs de classe HTML. `className` est un mot-clé spécifique à JSX pour les classes HTML. Ces classNames nous aideront à concevoir notre site web avec l'aide de CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*j59S60efTIR-6qMss59Obg.png)

### Composant Textbox

Maintenant, codons le composant `Textbox`. Cela affichera le formulaire où les utilisateurs peuvent sélectionner un jour dans le menu déroulant et ajouter un élément à sa liste de tâches pour ce jour, en utilisant le champ de saisie HTML.

Ouvrez `src/Component/Textbox.js` et codez ce qui suit :

La classe de composant `Textbox` a un objet d'état. Le `term` sera utilisé pour stocker l'entrée que l'utilisateur tape, et le `day` est initialisé par défaut à aujourd'hui. Cependant, sa valeur peut changer si l'utilisateur sélectionne un autre jour comme `Tomorrow` ou `Day After Tomorrow`.

La fonction `render` rend un formulaire simple qui a deux fieldsets.

L'un a une balise HTML `<select>` pour que l'utilisateur puisse sélectionner le jour.

Cette balise select a un événement `onChange` associé. Cet événement sera déclenché chaque fois qu'une nouvelle option est sélectionnée. La fonction `handleSelect` sera appelée et mettra à jour la valeur de `day` dans l'état du composant.

Nous avons également une autre balise input où l'utilisateur tapera son "objectif de tâche" qu'il souhaite accomplir. Cela a également un événement `onChange` qui appellera la fonction `handleChange`. Cette fonction mettra à jour la valeur de `term` dans l'état du composant.

La balise de formulaire enveloppante a un événement `onSubmit` qui sera déclenché lorsque le formulaire est soumis, et il appellera la fonction `handleSubmit`.

La fonction `handleSubmit` appelle la fonction `updateEntry` et passe la valeur de `term` et `day`. Maintenant, la fonction `updateEntry` ajoutera le `term` et le `day` dans l'état du composant parent et il sera sauvegardé là.

La fonction `handleSubmit` définit également la valeur de `term` à vide afin que la valeur suivante puisse y être sauvegardée.

Note : ici, nous parlons de deux états. L'un est l'état du composant App que nous considérerons comme notre état principal. Ses données seront sauvegardées en permanence même après avoir fermé le site web et le serveur. L'autre état auquel nous faisons référence est l'état particulier du composant. Celui-ci est utilisé pour stocker des données temporairement. Par exemple, ici, l'état du composant Textbox est un état temporaire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qkkouycB868dZydeRVbIbA.png)

### Composants d'affichage

Codons nos composants d'affichage.

Nous avons divisé la logique d'affichage en trois composants, qui affichent la liste de tâches des objets d'état `Today`, `Tomorrow` et `Day_After_Tomorrow`.

Ouvrez `src/Components/Display.js` et collez le code suivant :

Le fichier Display.js contient trois classes qui ont un code identique.

Prenons `class DisplayToday` pour une explication :

Rappelez-vous que dans la classe de composant `App` à l'intérieur de la fonction `render`, lorsque nous appelons :

```
/* Fichier App.js */
```

```
<DisplayToday items={this.state.Today} deleteItem={this.deleteEntry} />
```

...nous faisons référence à cette classe `DisplayToday` du fichier Display.js.

Nous avons passé deux attributs. `item` pointe vers le tableau `Today` défini dans l'état du fichier `App.js`, et `deleteItem` fait référence à la fonction `deleteEntry` que nous avons écrite dans le fichier `App.js`.

La classe `DisplayToday` à l'intérieur du fichier `Display.js` rend le composant `DisplayToday` et parcourt la liste d'éléments que nous avons passée dans l'attribut.

C'est la ligne qui effectue la tâche de parcourir chaque élément :

```
this.props.items.map((item, index)=> return ( /* item ici */ )) 
```

Ici, `item` est chaque élément d'un tableau et `index` est l'emplacement d'index de cet élément dans le tableau.

Nous avons également une balise `<button>` qui a un écouteur d'événement `onClick` lié à une fonction locale `removeThis`.

Lorsque l'utilisateur clique sur le bouton, l'événement `onClick` est déclenché et la fonction `removeThis` est appelée. Cette fonction reçoit la valeur d'index de l'élément dans le tableau en tant que paramètre et appelle la fonction `deleteEntry`, et passe l'index du tableau et le nom du tableau en tant que paramètres.

```
removeThis(e){        this.props.deleteEntry(e, 'Today');  }
```

Ensuite, la fonction `deleteEntry` supprimera cet emplacement d'index particulier du tableau.

Vous pouvez remonter et jeter un coup d'œil à la fonction `deleteEntry` que nous avons codée dans le fichier App.js.

Le fonctionnement de la classe `DisplayTomorrow` et de la classe `DisplayDayAfterTomorrow` est le même que celui de la classe `DisplayToday`.

Nous avons donc presque terminé, ajoutons maintenant quelques touches finales.

#### Le CSS

Pour le CSS, j'ai décidé d'utiliser un framework CSS au lieu de tout coder.

Après une petite recherche, j'ai trouvé [Hack.css](https://github.com/egoist/hack). J'ai vraiment aimé ses polices monospacées et son thème classique "hacker".

Configurer le CSS avec le projet est une tâche très facile. Il suffit d'exécuter la commande suivante :

```
npm install --save hack
```

Ajoutez cette ligne en haut avec les autres instructions d'importation dans votre fichier App.js :

```
import 'hack';
```

Si vous souhaitez ajouter un style CSS personnalisé, créez un nouveau fichier appelé `src/style.css`.

Écrivez votre CSS dans ce fichier et importez-le dans `App.js` en haut avec les autres instructions d'importation.

#### Stockage

Configurons le stockage.

Nous utiliserons le stockage local du navigateur comme stockage principal de notre site web.

Ce que nous allons faire ensuite est simplement magique.

L'intégration de notre site web avec le stockage du navigateur ne serait pas si facile sans [React Simple Storage](https://github.com/ryanjyost/react-simple-storage).

Il suffit d'exécuter la commande suivante dans le terminal :

```
npm install --save react-simple-storage
```

Ouvrez le fichier App.js et en haut du fichier, ajoutez cette ligne :

```
import SimpleStorage from 'react-simple-storage'
```

Maintenant, dans votre classe de composant App, faites défiler jusqu'à la fonction render et ajoutez cette ligne après la première balise `<div>` :

```
<SimpleStorage parent={this} />
```

Et voilà ! Maintenant, nos données seront sauvegardées dans le navigateur et seront récupérées depuis le navigateur lorsque nous rouvrirons notre site web.

### Le résultat !

Pour voir ce que nous avons accompli, ouvrez votre terminal et tapez :

```
npm start
```

Maintenant, dans le navigateur, accédez à `localhost:3000`.

J'espère que vous avez apprécié cela !

Quelques choses à ajouter comme devoirs...

* Fonctions de validation de code. Actuellement, même une entrée vide est également mise à jour, mais notre application devrait afficher une erreur indiquant que l'utilisateur doit d'abord écrire quelque chose.
* Affichage de la date et de l'heure
* Ajout d'une option pour modifier le nom d'utilisateur

Si vous êtes bloqué quelque part, vous pouvez aller sur ma [page GitHub](https://github.com/mohit23x) où vous trouverez le code complet.

Si vous souhaitez utiliser ce site web quotidiennement pour augmenter votre productivité, vous pouvez définir [cette page](https://mohit0101.github.io/next-3-days-plan-browser-homepage/) comme page d'accueil de votre navigateur (elle a quelques fonctionnalités supplémentaires ajoutées).

...jusqu'à la prochaine fois, bon codage !