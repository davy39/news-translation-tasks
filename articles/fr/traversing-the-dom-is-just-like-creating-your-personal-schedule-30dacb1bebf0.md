---
title: Parcourir le DOM, c'est comme créer votre emploi du temps personnel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-06T17:07:50.000Z'
originalURL: https://freecodecamp.org/news/traversing-the-dom-is-just-like-creating-your-personal-schedule-30dacb1bebf0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TgKhyx4XQbcqJUMHubyQVg.jpeg
tags:
- name: coding
  slug: coding
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Parcourir le DOM, c'est comme créer votre emploi du temps personnel
seo_desc: 'By Kevin Kononenko

  If you use a calendar to plan your day, then you can understand the basics of the
  DOM.

  Think back to the first time you learned HTML.

  Someone (or some software) had to explain how the different elements worked together
  so that you ...'
---

Par Kevin Kononenko

#### Si vous utilisez un calendrier pour planifier votre journée, alors vous pouvez comprendre les bases du DOM.

Retournez à la première fois où vous avez appris le HTML.

Quelqu'un (ou un logiciel) a dû vous expliquer comment les différents éléments fonctionnaient ensemble afin que vous puissiez construire votre première page web.

Ils l'ont probablement décrit comme « des boîtes dans des boîtes... dans des boîtes... dans des boîtes... »

![Image](https://cdn-media-1.freecodecamp.org/images/0*B9TUpKE_9uecisNp.)

Et ce niveau de compréhension de base fonctionne assez bien pour commencer ! Mais une fois que vous êtes à l'aise avec le CSS et que vous passez au JavaScript... eh bien, les boîtes dans des boîtes ne suffisent plus.

### JavaScript vous oblige à comprendre le DOM plus profondément

Dès que vous passez à JavaScript et jQuery, vous devez comprendre le Document Object Model (**DOM**). Le DOM est une Interface de Programmation d'Application (API) qui vous permet d'utiliser JavaScript pour apporter des modifications à votre HTML.

C'est la clé pour construire des sites web dynamiques et lier JavaScript et HTML sur le front-end.

Habituellement, le DOM est appelé l'**arbre DOM**. Cela fonctionne assez bien pour expliquer l'idée de base puisque les gens comprennent l'idée de branches d'arbre et d'une hiérarchie infinie de ces branches.

![Image](https://cdn-media-1.freecodecamp.org/images/0*zIrPwyoexWquu-u_.)

Mais l'analogie est encore _si basique_ que vous aurez du mal à comprendre les différentes relations entre les éléments dans le DOM.

Je voulais trouver un moyen d'expliquer les deux concepts clés du DOM :

1. **Contenu** : Les éléments parents contiennent des éléments enfants. Et ces enfants contiennent leurs propres éléments enfants.
2. **Ordre** : Les éléments du DOM ont un ordre défini que vous pouvez manipuler.

J'ai trouvé que le concept d'un **calendrier personnel** fait beaucoup mieux pour montrer les relations complexes entre les éléments dans le DOM. Voici une explication visuelle de la façon d'utiliser un calendrier pour comprendre le DOM.

Pour comprendre ce tutoriel, vous devez simplement comprendre les classes et comment configurer un document HTML.

![Image](https://cdn-media-1.freecodecamp.org/images/0*4QRtYzeFLIZUSklE.)

### Les bases du parcours du DOM

Voici un diagramme rapide des trois premiers mois de 2018.

![Image](https://cdn-media-1.freecodecamp.org/images/0*dYh65M146nRUJ0AE.)

Dans ce cas, l'**année** contient trois **mois**, chacun contenant 4 **semaines**.

Voici le même concept en HTML :

Chaque mois est un `div` qui non seulement a la classe `month`, mais aussi une classe avec un `name` spécifique du mois. Cela est dû au fait qu'il existe un nombre presque infini d'années, donc il y a de nombreux cas pour chaque classe. La même structure est utilisée sur le `div` avec la classe `year` à la ligne 1.

De plus, les semaines n'ont pas d'identifiant particulier au-delà de la classe `week`. Vous verrez pourquoi dans un instant.

En plus d'utiliser des classes et des IDs pour accéder aux éléments via le DOM, nous pouvons également **utiliser les relations entre les éléments**. Il y en a trois que vous devez connaître pour l'instant — enfant, parent et frère.

### Éléments enfants

**Élement enfant** : Un élément qui est contenu dans un autre élément

Exemple — Le `div` **january** est un **enfant** de l'année **2018**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*QMyRD4mD2LIZJh_z.)

### Éléments parents

**Élement parent** : Un élément qui contient d'autres éléments.

Exemple : L'année **2018** est un parent. Mais **January** est aussi un parent car il contient 4 **semaines** !

![Image](https://cdn-media-1.freecodecamp.org/images/0*z_H3YpYWrdd0L_7k.)

### Éléments frères

**Élement frère** : un élément qui a le même parent direct que d'autres éléments.

Exemple : Les **4 semaines** dans **January** sont des frères les unes des autres.

![Image](https://cdn-media-1.freecodecamp.org/images/0*87blfhCQdMA4MV9c.)

Alors, quelle est la différence entre le DOM et le HTML réel, pourriez-vous demander ?

Eh bien, pensez à la façon dont vous utilisez un calendrier personnel. Ce n'est qu'un enregistrement des choses que vous faites pendant vos journées. Ce n'est pas l'activité réelle ! En d'autres termes, c'est un modèle des choses qui se passent pendant la journée.

Le HTML est le contenu réel de votre journée. Les éléments HTML composent la page web, tandis que le DOM est une interface accessible pour diriger les changements.

Voici quelques exemples qui montreront ces concepts en action.

### Exemple #1 : Jouer au football une fois par semaine

D'accord, nous allons montrer comment vous représenteriez certaines habitudes du monde réel dans le DOM. Voici le scénario : Vous voulez jouer au football une fois par semaine pour le mois de janvier.

En termes de HTML, cela signifie que nous devons obtenir chacune des 4 semaines de janvier et changer leur contenu en : « Jouer au football ».

Cela peut sembler une question rhétorique stupide, mais savez-vous ce que ces 4 divs avec la classe `week` ont en commun ?

_La réponse :_ Ils sont tous des **enfants** de la div avec la classe `january` !

Donc, nous pouvons utiliser l'instruction suivante en JavaScript pour obtenir la div avec la classe `january` :

```
document.getElementsByClassName('january');
```

Ensuite, nous avons besoin de tous les enfants de cette div. Nous pouvons mettre à jour l'instruction précédente avec la propriété `_childNodes_` :

```
document.getElementsByClassName('january').childNodes;
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*0C--ByYtO0jfkacv.)

Enfin, nous devons utiliser la propriété `_nodeValue_` pour changer le texte de chaque élément. Et nous devons utiliser une boucle for pour accéder à l'élément dans childNodes, puisque cela retourne un tableau d'éléments. Donc, nous devons parcourir cette liste.

```
let weeks = document.getElementsByClassName('january').childNodes;
```

```
for(let i = 0; i< weeks.length; i++){    weeks[i].nodeValue = "Jouer au football";}
```

Voici le résultat final en HTML :

Nous avons fait deux choses ici :

1. **Parcouru le DOM** — cela signifie que nous avons utilisé une série de sélecteurs pour obtenir les éléments dont nous avons besoin : les 4 divs `week`
2. **Manipulé le DOM** — nous avons effectivement changé le contenu textuel dans les éléments HTML !

### Exemple #2 : Payer votre facture de carte de crédit

Voici le deuxième scénario : Vous devez effectuer un paiement de facture de carte de crédit pendant la première semaine de chaque mois (il y a trois mois au total dans ce cas).

En termes de HTML, cela signifie que nous devons obtenir le **premier élément enfant** de chaque div avec la classe **month**. Vous devez ensuite changer la valeur en **Facture payée**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Irk4Q9j8D6Pmg-Ph.)

Commençons de la même manière que la dernière fois. Nous devons récupérer chaque div avec la classe `month`.

```
document.getElementsByClassName('month');
```

Ensuite, JavaScript a en fait une propriété `firstChild`. Nous pouvons donc récupérer le premier enfant de chaque div avec la classe `month`.

```
document.getElementsByClassName('month').firstChild;
```

Voici à quoi cela ressemble :

![Image](https://cdn-media-1.freecodecamp.org/images/0*BtGZmD-__wPE2sbP.)

Maintenant, comme la dernière fois, nous devons changer la valeur de toutes ces divs `week` en une seule fois pour une valeur de `Facture payée`.

```
document.getElementsByClassName('month').firstChild.nodeValue = "Facture payée";
```

Avoir l'instruction JavaScript sur deux lignes n'a pas d'importance, d'ailleurs, tant qu'il n'y a qu'un seul point-virgule.

HTML final :

Voyez comment nous pouvons mettre à jour des éléments à grande échelle simplement en fonction d'un nom de classe ? Plutôt puissant.

### Exemple #3 : Partir en vacances pendant une semaine

Voici le scénario. Supposons que ce soit votre calendrier de travail, et vous voulez indiquer que vous prendrez la deuxième semaine de février pour partir en vacances avec votre famille.

En termes de HTML, cela signifie que vous devez sélectionner le **deuxième** enfant du div **february** et changer la valeur en **Vacances**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*K_dBM7ch2mgAZ90a.)

La dernière fois, nous avons utilisé la propriété `firstChild` de JavaScript. Mais il n'y a pas de propriété second child ! Au lieu de cela, nous allons utiliser la propriété `childNodes`, comme dans le premier exemple.

`childNodes` retourne un _tableau_ de tous les enfants de l'élément parent. Si vous n'êtes pas déjà familier avec les tableaux, [consultez mon guide ici](https://medium.freecodecamp.org/javascript-arrays-and-objects-are-just-like-books-and-newspapers-6e1cbd8a1746). La bonne nouvelle est que vous pouvez sélectionner des éléments spécifiques en utilisant des crochets `[ ]`, comme pour tout autre tableau.

Puisque les tableaux sont indexés à partir de 0, nous devons sélectionner l'élément avec un index de 1, qui est le deuxième élément.

```
document.getElementsByClassName('february').childNodes[1];
```

Et ensuite, nous devons simplement changer la valeur.

```
document.getElementsByClassName('february') .childNodes[1].nodeValue= 'Vacances';
```

Et le HTML final.

`childNodes` applique simplement la structure de tableau, que vous connaissez probablement déjà, sur le DOM afin que vous puissiez manipuler le HTML.

### Appel à l'action

Avez-vous aimé cela ? Si vous voulez être informé lorsque je publierai de futurs tutoriels utilisant des analogies, inscrivez-vous [ici](https://www.codeanalogies.com/).