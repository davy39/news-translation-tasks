---
title: Comment personnaliser vos composants React tiers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-27T22:17:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-customize-your-third-party-react-components-e0afd88532c9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZDmijVpPHQCICQZhkJuYVA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment personnaliser vos composants React tiers
seo_desc: 'By Jacob Goh

  Component libraries make our lives easier.

  But as developers, you might often find yourselves in situations where third party
  components don’t provide the functionality or customization capability the project
  needs.

  We are left with 2 ch...'
---

Par Jacob Goh

Les bibliothèques de composants facilitent notre vie.

Mais en tant que développeurs, vous pouvez souvent vous retrouver dans des situations où les composants tiers ne fournissent pas la fonctionnalité ou la capacité de personnalisation dont le projet a besoin.

Nous avons deux choix :

1. Écrire le composant à partir de zéro vous-même
2. Personnaliser les composants tiers

Ce qu'il faut choisir dépend du composant et de la situation dans laquelle vous vous trouvez.

Apparemment, certains composants ne sont pas personnalisables, et certaines exigences de fonctionnalités ne sont pas réalisables. Mais la plupart du temps, la personnalisation des composants tiers est l'option la moins chronophage. Voici comment faire.

#### Avant de commencer

Par exemple, nous allons personnaliser le composant [react-bootstrap-typeahead](https://github.com/ericgio/react-bootstrap-typeahead).

Voici le point de départ si vous souhaitez suivre [https://stackblitz.com/edit/react-hznpca](https://stackblitz.com/edit/react-hznpca)

### 1. Écrire par-dessus le CSS

Cela est assez simple.

Il suffit de trouver quelles sont les classes CSS du composant et de les écrire par-dessus avec un nouveau CSS.

#### Exemple

**Objectif :** Ajouter une icône de liste déroulante à la boîte d'entrée, de sorte qu'elle ressemble à une liste déroulante.

Ajoutez simplement Font Awesome à `index.html`

![Image](https://cdn-media-1.freecodecamp.org/images/16kdVdCg3-4np2wM-rXMDRtIMfa8wyvLHeXN)

et ajoutez ce CSS à `style.css`

![Image](https://cdn-media-1.freecodecamp.org/images/J2-bO98h0LjAkEi03fSc3XzclXUYsJxLwksf)

Démonstration : [https://stackblitz.com/edit/react-wdjptx](https://stackblitz.com/edit/react-wdjptx)

### 2. Composant Wrapper

C'est ici que vous pouvez modifier le comportement par défaut du composant tiers.

Commencez par créer un composant wrapper `CustomizedTypeahead` et remplacez `Typeahead` par celui-ci.

![Image](https://cdn-media-1.freecodecamp.org/images/aaTRPNobErGVL8nvpXSEDxVABlny2wIfbehb)

[https://stackblitz.com/edit/react-rwyjmm](https://stackblitz.com/edit/react-rwyjmm)

Ce composant wrapper n'a aucun effet pour l'instant. Il transmet simplement les `props` au composant Typeahead.

Nous allons personnaliser le comportement du composant en apportant des modifications aux `props`.

#### Exemple : Définir les Props par défaut

**Objectif :** Ajouter des props par défaut

Commençons par la personnalisation la plus simple.

Supposons que nous voulons que tous les `CustomizedTypeahead` aient les props `clearButton` activées par défaut.

Nous pouvons le faire en :

![Image](https://cdn-media-1.freecodecamp.org/images/6gWDhcY-8D4AYgNm9wXwUE770HsYWOiZVyde)

Cela équivaut à :

![Image](https://cdn-media-1.freecodecamp.org/images/QL0N1mtMWXF2BshnSkjGVWe1WJuibMD7EH21)

Nous créons `injectedProps` et mettrons toutes les modifications des `props` à l'intérieur pour rendre le code gérable.

Démonstration : [https://stackblitz.com/edit/react-tk9pau](https://stackblitz.com/edit/react-tk9pau)

#### Exemple : Modifier les Props

**Objectif :** Trier toutes les options par ordre alphabétique

Nous recevons `options`, qui est un tableau d'objets, et `labelKey`, qui nous indique que l'étiquette de l'option doit être `optionObject[labelKey]`. Notre objectif est de trier `optionObject[labelKey]` par ordre alphabétique.

Nous pouvons le faire en utilisant [Array.prototype.sort()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort) pour trier le tableau `options`.

![Image](https://cdn-media-1.freecodecamp.org/images/cAvVBz5nKj0935ITrCMikT0b8CiQiM6DuRyK)

De cette manière, les `options` dans `injectedProps` écraseront les `options` originales dans `props`. C'est ainsi que nous pouvons trier toutes les options par ordre alphabétique par défaut.

Démonstration : [https://stackblitz.com/edit/react-cqv5vz](https://stackblitz.com/edit/react-cqv5vz)

#### Exemple : Intercepter les Écouteurs d'Événements

**Objectif :** Lorsque l'utilisateur sélectionne une option, si l'utilisateur a sélectionné à la fois « California » et « Texas » ensemble, alerter l'utilisateur et effacer la sélection (pour aucune raison particulière autre que pour cette démonstration).

C'est la partie amusante où vous pouvez faire beaucoup de personnalisation.

En gros, voici comment cela fonctionnera :

![Image](https://cdn-media-1.freecodecamp.org/images/T0EgNbA3k5yTxoQ2vDAILqd7aCWUWhsCLn6p)

Remarquez le `if(onChange) onChange(selectedOptions);`. Cela garantit que l'écouteur d'événement onChange original continue de s'exécuter après que nous l'avons intercepté.

![Image](https://cdn-media-1.freecodecamp.org/images/1LsWw93w0xBEd0IKACjquNsAUX8EF7KRDtRB)

Voici ce que nous avons fait dans le code ci-dessus :

1. Nous créons une fonction `onChange` qui a la même structure que la fonction `onChange` par défaut. C'est une fonction qui reçoit un tableau d'options sélectionnées.
2. Nous parcourons les options sélectionnées et vérifions si elles sont valides.
3. Si elles ne sont pas valides, nous affichons une alerte et effaçons l'entrée
4. Nous exécutons l'écouteur d'événement `onChange` original

Démonstration : [https://stackblitz.com/edit/react-ravwmw](https://stackblitz.com/edit/react-ravwmw)

### 3. Modifier le code source

_Attention : Ne pas en abuser ! C'est votre dernier recours. Vous ne devriez le faire que s'il n'y a pas d'autre choix._

Si aucune des méthodes ci-dessus ne fonctionne pour vous, les choix qui s'offrent à vous sont maintenant limités à :

* Trouver une autre bibliothèque de composants
* Écrire votre propre composant à partir de zéro
* **Modifier le code source du composant**

Il n'est en fait pas rare que vous deviez modifier le code source d'un package pour répondre aux besoins d'un projet. Surtout si vous avez trouvé un bug dans un package et que vous devez le corriger de toute urgence.

Mais il y a quelques inconvénients :

* Certains packages utilisent des langages différents comme CoffeeScript ou TypeScript. Si vous ne connaissez pas le langage, vous ne savez pas comment l'éditer.
* Cela peut prendre du temps d'étudier le code source et de déterminer où exactement placer votre modification.
* Vous pouvez involontairement casser une partie du package.
* Lorsque le package est mis à jour, vous devrez appliquer la mise à jour manuellement.

Si vous décidez d'aller de l'avant et d'apporter quelques modifications au code source, voici comment faire.

#### 1. Forker le Dépôt Github

Dans notre cas d'exemple, allez sur [https://github.com/ericgio/react-bootstrap-typeahead](https://github.com/ericgio/react-bootstrap-typeahead) et forkez le dépôt sur votre propre compte GitHub.

#### 2. Cloner le dépôt sur votre machine

#### 3. Apporter la modification

#### 4. Pousser le dépôt sur votre compte GitHub

#### 5. Installer votre dépôt en tant que dépendance

Après avoir forké le dépôt, l'URL de votre dépôt GitHub devrait être `https://github.com/<votre nom d'utilisateur GitHub>/react-bootstrap-typeahead`.

Vous pouvez installer ce dépôt git en tant que dépendance en exécutant cette commande :

```
npm i https://github.com/<votre nom d'utilisateur GitHub>/react-bootstrap-typeahead
```

Après l'installation, vous devriez voir ceci dans package.json :

```
"dependencies": {     "react-bootstrap-typeahead": "git+https://github.com/<votre nom d'utilisateur github>/react-bootstrap-typeahead.git" }
```

### Conclusion

Nous avons parlé de trois façons de personnaliser vos composants React tiers.

1. Écrire par-dessus le CSS
2. Utiliser un Composant Wrapper
3. Modifier le code source

Espérons que cela facilite votre vie en tant que développeur React.

En attendant, prenons tous un moment pour être reconnaissants envers tous les créateurs/contributeurs open source. Sans ces packages open source, nous ne pourrions pas avancer aussi vite que nous le faisons aujourd'hui.

**Quelle est votre expérience avec les bibliothèques de composants tiers ? Quelles autres méthodes utiliseriez-vous pour les personnaliser ? Laissez un commentaire !**

_Publié à l'origine sur [dev.to](https://dev.to/jacobgoh101/3-ways-you-could-customize-3rd-party-react-component-3dpl)._