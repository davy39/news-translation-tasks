---
title: Qu'est-ce que l'Abstraction en Programmation ? Un Guide pour Débutants
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2024-03-19T22:29:31.000Z'
originalURL: https://freecodecamp.org/news/what-is-abstraction-in-coding
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/EmbraceAbstractions-.png
tags:
- name: abstraction
  slug: abstraction
- name: beginners guide
  slug: beginners-guide
seo_title: Qu'est-ce que l'Abstraction en Programmation ? Un Guide pour Débutants
seo_desc: 'I''ve met and talked to multiple new coders recently, and I see a common
  mistake they all seem to make.

  They don''t embrace and understand abstractions in their code, or in their learning.

  But what are abstractions? And why are they important?

  Let''s di...'
---

J'ai récemment rencontré et parlé à plusieurs nouveaux codeurs, et je vois une erreur commune qu'ils semblent tous faire.

Ils ne comprennent pas et n'embrassent pas les **abstractions** dans leur code, ou dans leur apprentissage.

Mais qu'est-ce que les **abstractions** ? Et pourquoi sont-elles importantes ?

Plongeons-nous dans le sujet !

## Qu'est-ce qu'une Abstraction ?

En programmation, les développeurs utilisent souvent des **abstractions** pour simplifier un système. Les **abstractions** sont un moyen de cacher les détails compliqués à l'utilisateur final, et d'essayer de simplifier la tâche que vous essayez d'accomplir.

Mais les abstractions peuvent être utilisées dans plus que juste le code, alors commençons par un exemple.

### Abstractions de la machine à café

Imaginez si vous créiez une machine pour faire du café pour vos utilisateurs. Il pourrait y avoir deux approches :

#### **Comment la Créer avec Abstraction**

* Avoir un bouton qui dit "Faire du café"

#### **Comment la Créer sans Abstraction**

* Avoir un bouton qui dit "Faire bouillir l'eau"
* Avoir un bouton qui dit "Ajouter l'eau froide à la bouilloire"
* Avoir un bouton qui dit "Ajouter 1 cuillère de café moulu à une tasse propre"
* Avoir un bouton qui dit "Nettoyer les tasses sales"
* Et tous les autres boutons

Pouvez-vous voir comment, lorsque nous utilisons l'abstraction, nous n'attendons pas de l'utilisateur qu'il sache comment la machine fait le café ? Mais dans la machine sans abstraction, l'utilisateur doit savoir dans quel ordre appuyer sur chaque bouton, ce qui force l'utilisateur à comprendre comment le café est fait.

## Pourquoi Vous Devriez Abstraire Vos Détails

Lorsque nous utilisons bien les abstractions, nous rendons notre système/base de code/tâche et ainsi de suite beaucoup plus facile à comprendre et à utiliser. En cachant les détails compliqués à l'intérieur d'un module, d'une classe, d'un prototype ou d'une fonction, nous pouvons créer un moyen super simple de faire des choses compliquées.

Par exemple, disons que nous avons un code complexe qui finit par faire beaucoup de mathématiques complexes et difficiles à comprendre. Nous pouvons envelopper toute cette logique dans une fonction et fournir une interface très facile où vous passez simplement votre nombre et la fonction fera le travail.

Les développeurs dans tous les langages et à travers tous les écosystèmes utilisent des abstractions. L'équipe NodeJS ne vous force pas à comprendre comment modifier les 0 et les 1 sur un disque dur pour sauvegarder du texte dans un fichier – vous pouvez simplement appeler la fonction `writeFile`.

Lorsque nous utilisons l'abstraction, nous ne forçons essentiellement pas la personne qui utilise notre code à se soucier des détails d'implémentation. Ils peuvent simplement appeler la fonction et obtenir leur réponse – ils n'ont pas à se soucier de ce que la fonction fait "sous le capot".

_C'est_ la force d'abstraire les détails dans votre code.

Je travaillais autrefois dans une entreprise avec une base de code de 4 millions de lignes. Pouvez-vous imaginer un développeur senior s'attendre à ce que je comprenne chaque fonction ? Chaque module ? Chaque classe ? Je n'aurais JAMAIS fusionné un seul changement dans cette base de code si je l'avais fait !

Vous pouvez créer une base de code réutilisable, simple à comprendre et facilement modifiable en **abstrayant** certains détails dans les modules corrects/en séparant votre code.

## Un Exemple d'Abstraction

Essayons d'illustrer cela avec un exemple de code.

Imaginez que vous travaillez sur une application bancaire, et que vous tombez sans cesse sur cette même soustraction étrange, encore et encore, à différents endroits dans le code.

`const res = bankAccountBalance - 1200`

`const res = bankAccountBalance – 1500`

`const res = bankAccountBalance - 1400`

Pourquoi soustrayons-nous des nombres aléatoires du solde bancaire de tout le monde une fois par an ?! C'est si peu clair, il n'y a aucun commentaire expliquant cela ?! Que se passe-t-il ? Est-ce une erreur ?

Maintenant, imaginez si cette fonctionnalité était plus claire et faisait cela :

```javascript
const minusFeesInUSDollars = (bankAccountBalance ) => {
	// Nos frais annuels pour ce compte sont de 1200 (USD)
    const YEARLY_FEES = 1200;
    return bankAccountBalance - YEARLY_FEES;
}
const minusFeesInGBPounds = (bankAccountBalance ) => {
	// Nos frais annuels pour ce compte sont de 1500 (GBP)
    const YEARLY_FEES = 1500;
    return bankAccountBalance - YEARLY_FEES;
}
const minusFeesInEuros = (bankAccountBalance ) => {
	// Nos frais annuels pour ce compte sont de 1400 (EUR)
    const YEARLY_FEES = 1400;
    return bankAccountBalance - YEARLY_FEES;
}
```

L'exemple n'est pas parfait, car nous pourrions supprimer certaines duplications dans ces fonctions – mais nous avons abstrait la logique en "quelque chose", dans ce cas, une fonction.

## Pourquoi Devrais-je Embrasser les Abstractions ?

J'ai expliqué les **abstractions** jusqu'à présent dans le contexte du code, mais cela peut également s'appliquer à votre parcours d'apprentissage.

Si vous ne pouvez pas embrasser les **abstractions** (au moins lorsque vous commencez), vous ne pourrez jamais comprendre et exceller en tant que développeur.

Pourquoi est-ce le cas ?

Eh bien, parce qu'il y a toujours une **abstraction** en dessous de vous, que vous serez tenté de essayer de comprendre. Cela finira par vous frustrer, vous submerger et **tuer votre apprentissage.**

Voici un exemple.

1. Vous commencez à apprendre React.

_Cela se passe bien ! Je commence à apprendre mes premiers morceaux de code et à rendre quelques choses à l'écran de mon ordinateur. Cela se passe bien. 😊_
2. Vous apprenez que React est une bibliothèque de JavaScript.

_D'accord, c'est cool ! Je devrais apprendre un peu de JavaScript avant de commencer avec React. Je vais arrêter d'apprendre React, et apprendre vanilla JavaScript d'abord._
3. Vous apprenez que JavaScript est un langage de programmation composé de nombreux éléments différents.

_D'accord, cela devient plus complexe maintenant. Il y a des moteurs JavaScript, des API tierces, différents environnements d'exécution. Cela devient confus._
4. Vous essayez de comprendre comment un moteur interprète le code JavaScript.

_D'accord ! Donc votre code JavaScript est exécuté par un logiciel codé en C++. Qu'est-ce que C++ ?_
5. Vous commencez à apprendre C++.

_Ce parcours d'apprentissage ne se passe plus très bien. Cela commence à devenir très confus et beaucoup plus long._
6. Vous apprenez que C++ est simplement une extension de C.

_Qu'est-ce que C ?!_

...et ainsi de suite.

Si vous continuez à creuser de plus en plus profondément, dans chaque petit détail, vous êtes beaucoup plus susceptible d'abandonner votre parcours d'apprentissage, et ce sera seulement parce que vous vous sentez submergé.

Et si par quelque miracle vous n'avez pas abandonné, vous allez passer beaucoup, beaucoup plus de temps à essayer d'apprendre quelques compétences de base dont vous pourriez avoir besoin pour un emploi.

## Comment Embrasser les Abstractions ?

Lorsque vous apprenez, vous allez devoir vous habituer à ne pas comprendre pleinement certaines choses dans votre parcours d'apprentissage.

Vous pouvez simplement "abstraire" cette connaissance, et vous en tenir aux choses qui sont pertinentes pour ce que vous faites actuellement.

Ne poursuivez pas chaque petit détail que vous rencontrez si vous êtes nouveau dans votre parcours d'apprentissage. La vérité est que même les experts ne savent pas tout ! Ils connaissent normalement beaucoup de choses dans un domaine étroit.

## Un Jour Vous Pouvez Creuser dans les Abstractions

Je ne veux pas que cet article donne l'impression que je dis que vous ne devriez jamais plonger sous les abstractions que vous utilisez tous les jours. Mais ce que je dis, c'est que cela ne vous aidera pas à plonger dans les abstractions **avant** d'avoir passé un temps décent à coder d'abord.

Vous devriez essayer d'apprendre les choses au fur et à mesure que vous en avez besoin si vous êtes au début de votre parcours pour devenir développeur.

Après tout, apprendre à coder est déjà assez difficile, sans s'engager à apprendre tout l'écosystème avant même de comprendre les bases.

Une fois que vous commencez à vous sentir à l'aise dans votre parcours d'apprentissage et que vous souhaitez améliorer vos compétences, [alors apprenez comment fonctionnent vos abstractions](https://www.hanselman.com/blog/please-learn-to-think-about-abstractions).

## Conclusion

J'espère que cela a été utile et encourageant si vous vous sentez submergé par tout ce que vous apprenez actuellement.

Je tweete mes articles [ici](https://twitter.com/kealanparr) si vous souhaitez en lire plus.