---
title: Les bases de React.js – Le DOM, les composants et les vues déclaratives expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-29T09:12:00.000Z'
originalURL: https://freecodecamp.org/news/reactjs-basics-dom-components-declarative-views
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/photo-1619410283995-43d9134e7656.jpeg
tags:
- name: components
  slug: components
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
- name: Web Development
  slug: web-development
seo_title: Les bases de React.js – Le DOM, les composants et les vues déclaratives
  expliqués
seo_desc: "By Adwaith KS\nReact.js is an open source JavaScript library for creating\
  \ user interfaces. It was created by Facebook back in 2013. \nDemand for React developers\
  \ is skyrocketing, which means that having knowledge of this library is definitely\
  \ going to ..."
---

Par Adwaith KS

React.js est une bibliothèque JavaScript open source permettant de créer des interfaces utilisateur. Elle a été créée par Facebook en 2013.

La demande de développeurs React explose, ce qui signifie qu'avoir des connaissances sur cette bibliothèque en vaudra certainement la peine ! Parmi les sites web populaires construits avec ReactJS, on trouve Dropbox, Netflix et Instacart – et la liste est longue.

Maintenant, la question habituelle que tout le monde se pose est : avons-nous vraiment besoin d'une bibliothèque JavaScript juste pour créer des interfaces utilisateur ? Nous pouvons faire la même chose en utilisant uniquement du HTML et du CSS, n'est-ce pas ?

Alors, qu'est-ce qui rend React si populaire par rapport à l'utilisation de HTML, CSS et JavaScript natifs (vanilla) ? Pour cela, examinons d'abord les deux caractéristiques principales de React :

1. Les vues déclaratives
2. L'approche basée sur les composants

Bien sûr, React ne se résume pas à cela, mais nous nous concentrerons sur ces deux fonctionnalités ici. Avant d'aller plus loin et d'en apprendre davantage sur ces fonctionnalités, nous devons bien comprendre le DOM du navigateur.

## Qu'est-ce que le DOM ?

Le DOM (Document Object Model) représente la page web sous la forme d'une structure en arbre. Chaque morceau de HTML que nous écrivons est ajouté en tant que nœud à cet arbre.

Avec JavaScript, nous pouvons accéder à n'importe lequel de ces nœuds (éléments HTML) et mettre à jour leurs styles, leurs attributs, et ainsi de plus. Cela signifie que le DOM permet à JavaScript d'accéder à la page web et de la modifier facilement.

Maintenant, tout arbre doit avoir un nœud racine, n'est-ce pas ? Ici, le nœud racine est **document.** Vous vous demandez d'où vient ce nœud **document** ? Eh bien, il fait partie du navigateur. Toute balise HTML que vous écrivez sera un enfant direct ou indirect du nœud racine document.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-26-at-12.42.38-AM.png)
_Arbre DOM avec document comme nœud racine_

L'image ci-dessous montre la structure en arbre conceptuelle équivalente du DOM :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Untitled-Diagram.drawio.svg)
_Arbre DOM du navigateur_

Maintenant, j'espère que vous avez une compréhension claire du DOM du navigateur. Plongeons donc dans les deux fonctionnalités principales de ReactJS dont nous allons discuter aujourd'hui, à savoir son approche basée sur les composants et ses vues déclaratives.

## Approche basée sur les composants

Dans React, tout est un composant. Une page web est une collection de composants.

Considérez un composant comme une fonction classique dans n'importe quel langage de programmation. Quels sont les principaux avantages des fonctions ? La réutilisabilité, l'abstraction et l'évitement du code redondant, n'est-ce pas ?

C'est la même chose avec les composants dans React. Ne soyez pas dérouté par le code dans les images ci-dessous, car nous utilisons un mélange de HTML et de JavaScript. Accrochez-vous, nous y reviendrons dans une seconde.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-26-at-1.00.37-AM.png)
_Code pour le composant nommé Card_

L'image ci-dessus représente un composant appelé **Card** (puisque le nom de la fonction est Card). Comme mentionné précédemment, les fonctions ou composants peuvent être réutilisés autant de fois que vous le souhaitez. C'est exactement ce que nous faisons dans l'image ci-dessous. Nous réutilisons le composant **Card** (**`<Card />`**) quatre fois. Gardez à l'esprit que l'écriture de **`<Card />`** est équivalente à **`<Card></Card>`**. (Privilégiez la première notation, car elle est plus courante).

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-26-at-1.00.57-AM.png)
_Composant Card réutilisé plusieurs fois_

Bravo si vous y avez pensé ! Les quatre composants `<Card />` sont écrits à l'intérieur d'un autre composant appelé **Home** (puisque le nom de la fonction est Home, `<Home />`). Bravo encore si vous l'aviez deviné !

Bien sûr, vous pouvez réutiliser le composant `<Home />`, qui est lui-même une collection de plusieurs composants `<Card />`. C'est-à-dire que nous pouvons imbriquer n'importe quel nombre de composants à l'intérieur d'autres composants.

Vient maintenant une grande question : si les composants sont imbriqués comme nous l'avons mentionné, quel est le composant de niveau supérieur ? C'est le composant **`<App />`** (fourni par React). Tout composant personnalisé que vous écrivez sera un enfant direct ou indirect du composant **App** dans React.

À haut niveau, toute la structure des composants ressemble à un arbre avec le nœud racine **App**.

Gardez également à l'esprit que les noms des composants prennent une majuscule à la première lettre. Cette convention est utilisée pour distinguer un composant React d'une balise HTML classique.

Que se passe-t-il si vous ne mettez pas de majuscule à la première lettre d'un nom de composant ? Il y aura une ambiguïté pour savoir s'il s'agit d'une balise HTML ou d'un composant React.

Dans l'image ci-dessous, la **Navbar, Carousal, Services**, etc., sont tous des composants. L'ensemble des composants forme la page d'accueil ou le composant Home d'un site web. Propre, n'est-ce pas ?

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-19-at-1.00.33-PM-1.png)
_Page d'accueil composée des composants Navbar, Carousal, Services etc._

Les composants sont disposés dans l'ordre dans lequel ils doivent apparaître dans la page. Ici, la Navbar arrive en premier, en haut, puis le Carousal arrive sous la Navbar, et ainsi de suite.

Si vous observez attentivement les images ci-dessus, nous utilisons un mélange de JavaScript et de HTML. C'est ce qu'on appelle le **JSX (JavaScript XML)**. C'est simplement une façon agréable d'écrire du React.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-26-at-1.05.45-AM.png)
_Bizarre, n'est-ce pas ? C'est le JSX_

Dans l'image ci-dessus, nous assignons du HTML à une variable nommée **element**, tout comme nous assignons des valeurs à des variables en JavaScript. Bien sûr, vous pouvez maintenant réutiliser cette variable (element) n'importe où dans votre code comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-26-at-1.11.55-AM.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-26-at-1.16.52-AM.png)
_Sortie du code ci-dessus_

Et voilà l'essentiel pour les composants dans React. Passons maintenant à la fonctionnalité suivante.

## Vues déclaratives dans React

Dans React, nous n'interagissons pas réellement avec le DOM du navigateur. Oui, vous avez bien entendu ! Nous interagissons avec le DOM virtuel, qui est une copie exacte du DOM du navigateur, mais en mémoire.

Oui ! Nous avons affaire à un nouveau DOM, autre que celui du navigateur. Cela signifie que tout composant React que nous écrivons est inséré comme enfant dans le DOM virtuel.

Vous devez vous demander pourquoi nous avons besoin de ce DOM virtuel alors que nous avons déjà le DOM du navigateur ? Le DOM virtuel est la raison pour laquelle React effectue les rendus si rapidement et efficacement.

Lorsque nous mettons à jour le DOM du navigateur (sans utiliser React), cela prend un temps considérable pour disposer les éléments et redessiner l'écran afin que l'utilisateur voie les changements. Cela implique qu'une grande partie de l'arbre DOM soit redessinée.

Mais, en utilisant React, les mises à jour se produisent d'abord dans le DOM virtuel. Ensuite, le DOM du navigateur et le DOM virtuel sont comparés (processus de "diffing") pour voir s'il y a des mises à jour effectuées dans le DOM virtuel qui doivent être répercutées ou mises à jour dans le DOM du navigateur.

S'il y en a, alors seulement les mises à jour sont effectuées dans le DOM du navigateur pour correspondre au DOM virtuel. Et ces mises à jour ne sont effectuées qu'aux endroits où elles sont nécessaires. Cela signifie que l'intégralité du DOM du navigateur n'est pas mise à jour comme mentionné précédemment. Cela améliore la vitesse et l'efficacité.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/ezgif.com-video-to-gif.gif)
_Seule une partie du DOM est mise à jour, au lieu de l'ensemble_

## Avantages de React

Maintenant que vous connaissez les principales fonctionnalités de React, comprenons les avantages de son utilisation.

1. **Maintenabilité du code,** parce que nous pouvons désormais réutiliser les composants et diviser une logique complexe en parties plus petites.
2. **Rapide et performant,** parce que seule une partie du DOM du navigateur est mise à jour au lieu de l'ensemble.
3. **Flux de données unidirectionnel,** ce qui signifie que le flux de données n'est possible que du composant parent vers les composants enfants. C'est-à-dire que les composants sont imbriqués, le composant le plus élevé étant App. Cela garde tout modulaire.
4. **Facile à apprendre et à utiliser,** le temps de développement est réduit et la courbe d'apprentissage est courte.

Supposons que vous vouliez construire une application web complexe. Vous voulez qu'elle soit rapide et performante, et vous n'avez pas beaucoup de temps pour la développer. Dans ce cas, React devrait être en haut de votre liste !

Maintenant, vous comprenez avec un peu de chance pourquoi React est si populaire même si nous pouvons construire un site web avec seulement du HTML, du CSS et du JavaScript.

Voyons maintenant comment installer React sur votre machine et créer un tout nouveau projet.

## Comment démarrer un nouveau projet React

### Étape 1 – Installer Node

Avant même de penser à React, vous devez avoir installé Node correctement. C'est parce qu'en installant Node, vous obtenez également npm, qui est un gestionnaire de paquets pour JavaScript. Considérez-le comme une application que vous pouvez utiliser pour télécharger des bibliothèques supplémentaires dont vous pourriez avoir besoin dans votre projet.

Téléchargez-le et installez-le à partir d'ici : [**https://nodejs.org/en/download/**](https://nodejs.org/en/download/) (Téléchargez la version LTS).

Après l'installation, ouvrez votre terminal (Mac ou Linux) ou l'invite de commande (Windows) et tapez **`npm -v`** ; cela devrait afficher quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-19-at-12.24.17-PM-2.png)

### Étape 2 – Créer votre application React

Maintenant, il est temps d'installer un outil qui facilite la création d'un projet React. Félicitations ! Vous avez peut-être deviné que je parle de **create-react-app**.

Tapez la commande `npm install create-react-app` et attendez quelques secondes.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-19-at-12.29.08-PM-1.png)

### Étape 3 – Configurer votre application web React

Commençons maintenant à configurer notre toute première application web React. Appelons-la **myreactapp**.

Pour démarrer un nouveau projet React, tapez la commande suivante : `npx create-react-app myreactapp`.

La syntaxe générale est `npx create-react-app <nom_application>` (et notez que c'est npx et non npm, ne vous trompez pas :) ).

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-19-at-12.35.41-PM-2.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-19-at-12.35.52-PM-2.png)
_Suite de l'image précédente_

### Étape 4 – Ouvrir votre nouvelle application React

Il est maintenant temps de voir notre application React en action. Pour cela, déplacez-vous dans le projet créé (**myreactapp** tel que nous l'avons créé à l'étape précédente) en utilisant la commande `cd myreactapp` et tapez ce qui suit : `npm start`.

Cette commande ouvre alors un navigateur avec notre application React nouvellement créée :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-19-at-12.42.06-PM-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-19-at-12.41.28-PM-2.png)

Et voilà ! Vous avez installé React avec succès sur votre machine et avez démarré un tout nouveau projet. Vous êtes maintenant prêt à aborder des concepts plus importants dans React ! Joyeux hacking ❤️