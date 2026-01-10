---
title: 'CSS en JavaScript : L''avenir du style basé sur les composants'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-25T14:05:07.000Z'
originalURL: https://freecodecamp.org/news/css-in-javascript-the-future-of-component-based-styling-70b161a79a32
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yVKDbwtvfoakj3RZ9g8ARQ.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: 'CSS en JavaScript : L''avenir du style basé sur les composants'
seo_desc: 'By Jonathan Z White

  By adopting inline styles, we can get all of the programmatic affordances of JavaScript.
  This gives us the benefits of something like a CSS pre-processor (variables, mixins,
  and functions). It also solves a lot of the problems tha...'
---

Par Jonathan Z White

En adoptant les styles en ligne, nous pouvons bénéficier de toutes les possibilités programmatiques de JavaScript. Cela nous offre les avantages d'un pré-processeur CSS (variables, mixins et fonctions). Cela résout également de nombreux problèmes que CSS rencontre, tels que l'espace de noms global et les conflits de style.

Pour une analyse approfondie des problèmes que CSS en JavaScript résout, consultez la célèbre présentation : [React CSS in JS](https://speakerdeck.com/vjeux/react-css-in-js). Pour une étude de cas sur les améliorations de performance que vous obtenez avec Aphrodite, vous pouvez lire [Inline CSS at Khan Academy: Aphrodite](http://engineering.khanacademy.org/posts/aphrodite-inline-css.htm). Si vous souhaitez en savoir plus sur les meilleures pratiques de CSS en JavaScript, consultez le [guide de style d'Airbnb](https://github.com/airbnb/javascript/tree/master/css-in-javascript).

En outre, nous utiliserons des styles JavaScript en ligne pour construire des composants afin d'aborder certains des fondamentaux de la conception que j'ai couverts dans l'un de mes articles précédents : [Avant de maîtriser la conception, vous devez d'abord maîtriser les fondamentaux](https://medium.freecodecamp.com/before-you-can-master-design-you-must-first-master-the-fundamentals-1981a2af1fda).

### Un exemple motivant

Commençons par un exemple simple : créer et styliser un bouton.

Normalement, le composant et ses styles associés iraient dans le même fichier : `Button` et `ButtonStyles`. Cela est dû au fait qu'ils relèvent de la même préoccupation : la vue. Cependant, pour cet exemple, j'ai divisé le code en plusieurs gists pour le rendre plus digeste.

Voici le composant bouton :

Ce n'est rien d'inattendu — juste un composant React sans état. L'endroit où Aphrodite entre en jeu est dans la propriété `className`. La fonction `css` prend un objet `styles` et le convertit en CSS. L'objet `styles` est créé avec la fonction `StyleSheet.create({ ... })` d'Aphrodite. Vous pouvez voir la sortie de `StyleSheet.create({ ... })` avec ce [bac à sable Aphrodite](https://output.jsbin.com/qoseye?).

**Voici la feuille de style du bouton :**

L'un des avantages d'Aphrodite est que la migration est simple et la courbe d'apprentissage est faible. Les propriétés comme `border-radius` deviennent `borderRadius` et les valeurs deviennent des chaînes. Les pseudo-sélecteurs, les requêtes média et les définitions de police fonctionnent tous. De plus, les préfixes de fournisseurs sont ajoutés automatiquement.

**Voici le résultat :**

![Image](https://cdn-media-1.freecodecamp.org/images/1*x1ccRv9UGvcxBvz4TvC4Qg.png)
_[L'un des avantages d'Aphrodite est que la migration est simple et la courbe d'apprentissage est faible.](https://twitter.com/JonathanZWhite" rel="noopener" target="_blank" title=")_

Avec cet exemple en tête, **examinons comment nous pouvons utiliser Aphrodite pour construire un système de design visuel de base**, en nous concentrant sur les fondamentaux de design suivants : la typographie et l'espacement.

### Fondamental n°1 — Typographie

Commençons par la typographie, une base fondamentale pour le design. **La première étape consiste à définir des constantes de typographie**. Et contrairement à Sass ou Less, les constantes pour Aphrodite peuvent aller dans un fichier JavaScript ou JSON.

#### Définir les constantes de typographie

Lors de la création de constantes, **utilisez des noms sémantiques pour vos variables**. Par exemple, au lieu de nommer l'une de vos tailles de police `h2`, utilisez un nom comme `displayLarge` qui décrit son _rôle_. De même, pour les poids de police, au lieu de nommer l'un de vos poids `600`, donnez-lui un nom comme `semibold` pour décrire son _effet_.

Il est important d'obtenir les bonnes valeurs pour les variables comme les tailles de police et les hauteurs de ligne. Cela est dû au fait qu'elles affectent directement le rythme vertical dans un design. Le rythme vertical est un concept qui vous aide à obtenir un espacement cohérent entre les éléments.

Pour en savoir plus sur le rythme vertical, vous pouvez lire cet article : [Pourquoi le rythme vertical est-il une pratique typographique importante ?](https://zellwk.com/blog/why-vertical-rhythms/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ehj9XMvQ9wJNhxWNqwXfKw.png)
_[Utilisez une calculatrice pour déterminer les hauteurs de ligne](https://drewish.com/tools/vertical-rhythm/" rel="noopener" target="_blank" title=")_

Il y a une science derrière le choix des valeurs pour vos hauteurs de ligne et tailles de police. Nous pouvons utiliser des ratios mathématiques pour générer un ensemble de tailles candidates potentielles. Il y a quelques semaines, j'ai écrit un article détaillant la méthodologie : [La typographie peut faire ou défaire votre design : un processus pour choisir la typographie](https://medium.freecodecamp.com/typography-can-make-your-design-or-break-it-7be710aadcfe). Pour déterminer les tailles de police, vous utilisez [Modular Scale](http://www.modularscale.com/). Pour déterminer les hauteurs de ligne, vous pouvez utiliser cette [calculatrice de rythme vertical](https://drewish.com/tools/vertical-rhythm/).

#### Définir un composant d'en-tête

Après avoir défini nos constantes de typographie, l'étape suivante consiste à créer un composant pour consommer les valeurs. **Le but du composant est de garantir la cohérence dans la conception et la mise en œuvre des en-têtes dans la base de code.**

Le composant `Heading` est une fonction sans état qui prend une balise comme propriété et retourne la balise avec son style associé. Cela est possible car nous avons défini les mappages de balises précédemment dans le fichier des constantes.

En bas du fichier du composant, nous définissons notre objet `styles`. C'est là que nous utilisons les constantes de typographie.

Et voici comment le composant `Heading` serait utilisé :

Avec cette approche, **nous réduisons la variabilité inattendue dans notre système de typographie**. Nous évitons l'écueil de centaines de tailles de police différentes en supprimant le besoin de styles globaux et en standardisant les en-têtes dans la base de code. De plus, cette approche que nous avons prise pour construire le composant `Heading` peut être appliquée à la construction d'un composant `Text` pour le corps du texte.

### Fondamental n°2 — Espacement

**L'espacement contrôle à la fois le rythme vertical et horizontal dans le design**. Cela rend l'espacement crucial pour établir un système de design visuel. Tout comme dans la section typographie, la première étape pour aborder l'espacement est de définir des constantes d'espacement.

#### Définir les constantes d'espacement

Lors de la définition des constantes d'espacement pour les marges entre les éléments, nous pouvons adopter une approche mathématique. En utilisant une constante `spacingFactor`, nous pouvons générer un ensemble de distances basées sur un facteur commun. **Cette approche garantit que nous avons un espacement logique et cohérent entre les éléments.**

L'exemple ci-dessus utilise une échelle linéaire, de un à treize. Cependant, expérimentez avec différentes échelles et ratios. Les designs nécessitent différentes échelles en fonction de leur objectif, de leur public et des appareils qu'ils ciblent. Par exemple, **voici les six premières distances calculées en utilisant le nombre d'or** avec un `spacingFactor` de huit.

```
Nombre d'or (1:1.618)
```

```
8.0 x (1.618 ^ 0) = 8.0008.0 x (1.618 ^ 1) = 12.948.0 x (1.618 ^ 2) = 20.948.0 x (1.618 ^ 3) = 33.898.0 x (1.618 ^ 4) = 54.828.0 x (1.618 ^ 5) = 88.71
```

Voici à quoi ressemblerait l'échelle d'espacement dans le code. J'ai ajouté une fonction d'assistance pour gérer le calcul et arrondir la sortie à sa valeur de pixel la plus proche.

Après avoir défini nos constantes d'espacement, nous pouvons les utiliser pour ajouter des marges aux éléments de notre design. **Une approche que nous pouvons prendre est d'importer les constantes d'espacement et de les consommer dans les composants.**

Par exemple, ajoutons un `marginBottom` au composant `Button`.

Cela fonctionne dans la plupart des scénarios. Cependant, que se passe-t-il si nous voulons changer la propriété `marginBottom` du bouton en fonction de l'endroit où le bouton est placé ?

Une façon d'obtenir des marges variables est de remplacer le style de marge à partir du composant parent consommateur. Une approche alternative est de **créer un composant `Spacing` pour contrôler les marges verticales sur les éléments.**

En utilisant cette approche, nous pouvons retirer la responsabilité de définir les marges du composant enfant et la placer dans le composant parent. **De cette façon, le composant enfant devient agnostique en matière de mise en page, ne nécessitant aucune connaissance de l'endroit où se placer par rapport aux autres éléments.**

Cela fonctionne car des composants comme les boutons, les entrées et les cartes peuvent nécessiter des marges variables. Par exemple, un bouton dans un formulaire peut nécessiter des marges plus grandes qu'un bouton dans une barre de navigation. La mise en garde est que si un composant a toujours des marges cohérentes, il serait alors plus logique de gérer les marges à l'intérieur du composant.

Vous avez peut-être également remarqué que les exemples n'utilisent que `marginBottom`. Cela est dû au fait que **définir toutes vos marges verticales dans une seule direction vous permet d'éviter les marges qui s'effondrent et de garder une trace du rythme vertical de votre design**. Vous pouvez en lire plus à ce sujet dans l'article de Harry Robert, [Déclarations de marge à sens unique](https://csswizardry.com/2012/06/single-direction-margin-declarations/).

En dernier lieu, vous pouvez également utiliser les constantes d'espacement que vous avez définies comme rembourrage.

En utilisant les mêmes constantes d'espacement pour les marges et le rembourrage, vous pouvez obtenir une plus grande cohérence visuelle dans votre design.

Voici à quoi pourrait ressembler le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/1*oDkbVmgCJ4ss5fuRNvzoUg.png)
_[En utilisant des constantes d'espacement pour vos marges et rembourrages, vous pouvez obtenir une plus grande cohérence visuelle.](https://twitter.com/JonathanZWhite" rel="noopener" target="_blank" title=")_

Maintenant que vous avez une compréhension du CSS en JavaScript, allez et expérimentez. Essayez d'incorporer des styles JavaScript en ligne dans votre prochain projet. Je pense que **vous apprécierez pouvoir travailler dans un seul contexte pour gérer toutes vos préoccupations de style et de vue.**

Sur le sujet du CSS et du JavaScript, quels sont les nouveaux développements qui vous enthousiasment ? Personnellement, je suis enthousiaste à propos de async/await. Laissez-moi un mot ou envoyez-moi un [tweet](https://twitter.com/jonathanzwhite) sur Twitter.

Vous pouvez me suivre sur [Twitter](https://twitter.com/JonathanZWhite), où je publie des divagations sans sens sur le design, le développement front-end et la réalité virtuelle.