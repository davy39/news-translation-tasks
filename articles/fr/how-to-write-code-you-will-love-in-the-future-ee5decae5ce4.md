---
title: Comment écrire du code que vous aimerez dans le futur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-13T17:48:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-code-you-will-love-in-the-future-ee5decae5ce4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cW0Pr7SZuyuQT2IDoayrrw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
seo_title: Comment écrire du code que vous aimerez dans le futur
seo_desc: 'By Lusan Das

  Uncle Ben once told Peter Parker, “With great power comes great responsibility”.
  This quote applies to fellow programmers who are involved in building projects.
  Being in the industry for over 5 years has made me reflect on my experiences...'
---

Par Lusan Das

L'oncle Ben a un jour dit à Peter Parker, *"Un grand pouvoir implique de grandes responsabilités"*. Cette citation s'applique aux programmeurs qui participent à la construction de projets. Après plus de 5 ans dans l'industrie, j'ai eu l'occasion de réfléchir à mes expériences et il est temps pour moi de redonner à la communauté.

### Le Début

J'ai commencé ma carrière dans une multinationale, mais j'ai rapidement réalisé que je voulais travailler sur des rôles plus stimulants avec de plus grandes responsabilités. Ainsi, après un an, j'ai rejoint une startup.

C'était une équipe de développement de seulement cinq membres. Cela a changé ma vision du développement. J'ai eu la chance de trouver un excellent mentor et des coéquipiers formidables qui m'ont aidé à grandir. Mais nous étions une entreprise en pleine croissance. Pour garantir les livraisons à temps, nous compromettions souvent la qualité de notre code. Nous pensions souvent que nous le corrigerions à la fin. Ainsi, en construisant le navire, nous avons laissé des failles. Cela a conduit à une dette technique, ce qui n'était pas une mauvaise chose.

### Ne jamais compromettre la qualité du code

Après un certain temps, nous avons progressivement réalisé que nous ne pourrions plus évoluer. Nous avons donc décidé de réécrire toute la base de code, ce qui a pris plus de temps. Mais cela a finalement conduit à une base de code de qualité, évolutive et agréable à travailler. Je me souviens encore que nous avions un dossier "**shame folder**" au cas où un développeur déciderait d'écrire du code qu'il savait créerait du travail supplémentaire plus tard.

De cette manière, nous nous sommes rendus responsables du maintien de la qualité. Mais la leçon que j'ai apprise est la suivante :

> *Même si cela prend un peu plus de temps à terminer, nous devrions prendre ce temps et écrire du code de qualité pour l'avenir. Grâce à cet effort supplémentaire, nous avons économisé beaucoup de temps et d'argent.*

Nous avons résolu le problème architectural, mais ensuite est venue la partie amusante : **les performances**. Lorsque nous avons construit notre projet, nous avons utilisé beaucoup de bibliothèques pour un développement rapide. Nous avions l'impression que notre projet avait pris du poids. Il avait besoin de beaucoup d'exercices. Pour perdre ces kilos en trop, nous avons fait quelques analyses et réalisé que nous avions beaucoup de bibliothèques inutiles. Nous aurions pu construire ces bibliothèques nous-mêmes. Nous avons donc supprimé ces bibliothèques et construit les nôtres. Super !! Notre page était plus rapide grâce à une taille de bundle plus petite.

Mais la soif de performance n'était pas encore assouvie. Lorsque vous avez construit un projet à partir de zéro, ce sentiment d'être un spartiate vous consume lentement. L'histoire ne peut pas être terminée. Nous pouvions être plus rapides. Puis nous avons réalisé que nous utilisions encore des bibliothèques. Et si nous n'en utilisions aucune ? L'enthousiasme d'écrire notre propre code nous a consumés, alors nous l'avons fait. Nous avons construit un projet avec presque aucune bibliothèque.

### Toujours documenter et écrire des commentaires de code

Puis est venu un rebondissement dans notre histoire : la startup a finalement été acquise. J'ai été transféré dans une nouvelle équipe. Les nouveaux membres étaient plus familiers avec les bibliothèques existantes sur le marché. Soudain, notre base de code leur était étrangère. Nous avions effectivement écrit nos bibliothèques, mais nous n'avions pas eu assez de temps pour les documenter. Cela a créé un énorme fossé. J'ai appris l'importante leçon de la documentation et des commentaires de code.

> *J'ai réalisé que le code n'est pas seulement pour soi-même. En tant qu'auteur, c'est votre devoir d'écrire pour les masses.*

Donc, la morale est qu'il n'est pas faux d'écrire vos propres bibliothèques. Mais si vous le faites, alors la documentation et les commentaires de code sont une nécessité. N'importe qui devrait pouvoir comprendre facilement votre bibliothèque simplement en lisant votre documentation. Je ne peux pas insister assez, n'écrivez pas pour vous-même ! En tant que relecteur et mainteneur de code, c'est votre responsabilité de vous en assurer.

### Ne réinventez pas la roue, sauf si vous vous assurez qu'elle est maintenable

Avec le temps, j'ai réalisé qu'il n'y avait aucun intérêt à réinventer toute la roue. À moins que nous ayons beaucoup de temps pour développer et documenter la même chose afin qu'elle puisse être comprise par tous. S'il existe une bibliothèque qui résout votre problème, alors c'est une excellente idée de contribuer à ce projet spécifique ! Il y a un piège, et je voudrais citer [Phil Walton](https://medium.com/u/af9c5528a8ab) dans son [blog](https://philipwalton.com/articles/how-to-become-a-great-front-end-engineer/) :

> **Réinventer la roue est mauvais pour les affaires, mais c'est génial pour l'apprentissage.** Vous pourriez être tenté de prendre ce widget de typeahead ou cette bibliothèque de délégation d'événements depuis npm, mais imaginez combien vous apprendriez en essayant de construire ces choses vous-même.

Donc, faites votre choix avec sagesse ^_-

### Toujours tester votre base de code

Je ne peux pas insister assez sur l'importance de cela. Grâce à des bibliothèques comme [Jest](https://github.com/facebook/jest) et [React testing library](https://github.com/kentcdodds/react-testing-library), et bien d'autres, tester du code n'a jamais été aussi facile. Souvent, lorsque la base de code devient volumineuse, même un seul changement de ligne peut faire planter l'application. Si nos tests sont automatisés, nous pouvons être confiants quant aux changements que nous apportons.

### Continuez à apprendre

Je voulais que mon développement frontend soit rapide et performant. J'ai finalement décidé d'apprendre React, principalement à cause de mon parcours. Je l'ai trouvé peu contraignant, et l'écrire était très proche de l'écriture de JavaScript pur. Cela a changé ma vie pour le mieux.

Des bibliothèques comme React, Vue, Angular et diverses autres (surtout Redux) ne vous disent pas seulement comment construire une UI rapide. Elles ouvrent également des portes vers d'autres concepts comme la programmation fonctionnelle, l'immuabilité, et bien d'autres, qui vous aident réellement à devenir meilleur dans votre métier. Apprendre React et Redux a amélioré ce que je savais déjà.

### Conclusion

Alors que je gagnais en expérience, j'ai finalement rejoint une autre startup, où j'ai été chargé de construire des produits à partir de zéro et de poser les fondations. Mais cette fois, j'étais armé de toutes mes expériences et de mes erreurs. Je suis heureux de dire que je suis fier de ce que j'ai construit jusqu'à présent et je suis sûr que j'ai encore un long chemin à parcourir. La quête de la perfection est un chemin sans fin, mais nous pouvons toujours nous efforcer de marcher sur le bon chemin.

Toutes les expériences que j'ai mentionnées ne sont pas destinées à être la parole d'évangile. Elles sont très spécifiques à mon parcours dans l'industrie. Mais j'espère que cela vous aidera à devenir un meilleur développeur, et je suis toujours reconnaissant envers la communauté, qui m'a aidé à grandir.

_Suivez-moi sur [twitter](https://twitter.com/daslusan)_ pour obtenir plus de mises à jour concernant les nouveaux articles et pour rester informé des dernières évolutions frontend. De plus, partagez cet article sur twitter pour aider les autres à le connaître. Partager, c'est prendre soin ^_^.

### Quelques ressources utiles

1. [https://philipwalton.com/articles/how-to-become-a-great-front-end-engineer/](https://philipwalton.com/articles/how-to-become-a-great-front-end-engineer/)
2. [https://jestjs.io/](https://jestjs.io/)
3. [https://blog.kentcdodds.com/introducing-the-react-testing-library-e3a274307e65](https://blog.kentcdodds.com/introducing-the-react-testing-library-e3a274307e65)
4. [https://en.wikipedia.org/wiki/Technical_debt](https://en.wikipedia.org/wiki/Technical_debt)
5. [https://en.wikipedia.org/wiki/Software_entropy](https://en.wikipedia.org/wiki/Software_entropy)

### Mes articles précédents

1. [https://medium.freecodecamp.org/the-best-way-to-architect-your-redux-app-ad9bd16c8e2d](https://medium.freecodecamp.org/the-best-way-to-architect-your-redux-app-ad9bd16c8e2d)
2. [https://medium.freecodecamp.org/how-to-use-redux-persist-when-migrating-your-states-a5dee16b5ead](https://medium.freecodecamp.org/how-to-use-redux-persist-when-migrating-your-states-a5dee16b5ead)
3. [https://codeburst.io/redux-observable-to-the-rescue-b27f07406cf2](https://codeburst.io/redux-observable-to-the-rescue-b27f07406cf2)
4. [https://codeburst.io/building-webapp-for-the-future-68d69054cbbd](https://codeburst.io/building-webapp-for-the-future-68d69054cbbd)
5. [https://codeburst.io/cors-story-of-requesting-twice-85219da7172d](https://codeburst.io/cors-story-of-requesting-twice-85219da7172d)
6. [https://blog.usejournal.com/what-i-learnt-from-reactfoo-2018-e4e1a4c6a705](https://blog.usejournal.com/what-i-learnt-from-reactfoo-2018-e4e1a4c6a705)