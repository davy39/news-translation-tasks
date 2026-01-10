---
title: 'Comment un développeur C++ apprend JavaScript : une histoire frustrante mais
  finalement satisfaisante'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-26T19:41:22.000Z'
originalURL: https://freecodecamp.org/news/tales-of-a-c-developer-learning-javascript-96b0a3324d25
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1sxcjy4QPYQGMyOlkwqHjQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: 'Comment un développeur C++ apprend JavaScript : une histoire frustrante
  mais finalement satisfaisante'
seo_desc: 'By DHARA DOSHI

  This year I started my journey into Web Development. As the umpteenth article on
  the web will profess: JavaScript is the holy grail.

  And so I began my journey into this new stack, new domain, and a whole new level
  of newness.

  So, in th...'
---

Par DHARA DOSHI

Cette année, j'ai commencé mon voyage dans le développement Web. Comme le professe le énième article sur le web : JavaScript est le saint graal.

Et ainsi, j'ai commencé mon voyage dans cette nouvelle pile, ce nouveau domaine, et un tout nouveau niveau de nouveauté.

Donc, au milieu de la journée, au milieu d'une fonctionnalité que je mettais en œuvre, j'étais presque au stade où j'avais envie de m'arracher les cheveux. Ma frustration n'avait pas de limites, et mon syndrome de l'imposteur était à son comble.

Avant de vous en dire plus sur quel problème a failli me rendre folle, laissez-moi donner un peu de contexte sur moi-même.

J'ai à peine commencé à effleurer la surface de JavaScript, et j'ai suivi quelques leçons de FreeCodeCamp (et j'ai admiré ce que [Quincy Larson](https://www.freecodecamp.org/news/tales-of-a-c-developer-learning-javascript-96b0a3324d25/undefined) a accompli). Depuis que j'ai commencé mon voyage en tant que diplômée en informatique il y a plus de 10 ans, je n'avais jamais vu le codage enseigné de manière aussi structurée.

J'ai commencé le développement JavaScript en février 2018 (après avoir suivi un cours avec edX sur JavaScript & JQuery, appelé [Programming for the Web with JavaScript](https://courses.edx.org/courses/course-v1:PennX+SD4x+2T2017/courseware/05f321f8b38c400b96330598e23d639c/66cdc9f1359c44e698177abcd5ab480e/?activate_block_id=block-v1:PennX+SD4x+2T2017+type@sequential+block@66cdc9f1359c44e698177abcd5ab480e)). Cela signifie que je m'y consacre depuis cinq mois maintenant. Je suis étrangement indignée de m'être retrouvée bloquée sur ce problème maintenant plutôt que quelques mois plus tôt, mais un développeur n'a guère le choix avec ce genre de choses. Il faut simplement avaler son ego, à chaque fois. Et apprendre !

Vous vous demandez quel problème spécifique de JavaScript m'a fait poser toutes les questions existentielles de ma vie ?

### Une histoire illustrée de M. Lundi, le bouton.

C'est l'histoire d'un bouton :

![Image](https://cdn-media-1.freecodecamp.org/images/1*OZlc_3RUxnM-3KG0BnNIHA.png)
_Faites la connaissance de M. Lundi (un bouton)_

La personnalité de M. Lundi peut être définie comme :

```
<button type="button" class="btn btn-sm btn-success" id="<mon-week-day">MON</button>
```

Mais M. Lundi n'est pas aussi original que nous le souhaiterions. Il était basé sur un modèle, et la source de sa vraie personnalité était quelque chose comme ceci :

```
<button type="button" class="btn btn-sm btn-success" id="<%=day%>-week-day">day.substr(0, 3).toUpperCase()</button>
```

```
where day is the days of the week: monday, tuesday, wednesday etc.
```

Avis de non-responsabilité : Le code est <%= day %&g[t;](http://ejs.co/) est EJS.

Je voulais donner à la personnalité de M. Lundi une touche de gris dans certaines situations.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JylMwILuBZEokQBARkq_Ow.png)
_N'est-il pas magnifique ? :P_

Mais M. Lundi ne savait tout simplement pas s'amuser. Soupir ! Il ne voulait pas devenir gris !

### Comment j'ai finalement fait ressortir le meilleur de M. Lundi

Je lui ai dit de faire ceci, alors laissez-moi vous préparer pour ajouter de la classe à votre persona.

```
$('#'+day+'week-day').addClass('unselected')
```

Il n'a pas bougé. J'ai changé addClass en toggleClass et rien ne s'est passé. Je pense qu'il n'était pas enthousiaste à l'idée d'être "unselected", bien que je lui aie expliqué pourquoi c'était essentiel.

Ensuite, j'ai sorti les gros canons, la console. Et j'ai essayé de le changer là. La console a jeté un doute sur la capacité de M. Lundi à changer.

Elle disait qu'elle avait changé la couleur, mais je voyais toujours un M. Lundi très vert. Alors, qu'est-ce qui se passait ici ? [Mon esprit Sherlock](https://medium.freecodecamp.org/why-i-feel-like-i-am-sherlock-at-my-software-job-4a303ebdaf63) est venu à mon secours et voilà, j'ai réalisé la plus grande erreur jamais connue de l'humanité dans l'histoire de la programmation (ou du moins dans mon esprit, cela semblait être la plus grande erreur jamais commise).

Il y avait un autre élément avec le même id que M. Lundi. C'est pourquoi il ne bougeait pas et tous les changements étaient probablement ciblés sur l'autre gars. Un cas aigu de crise d'identité, je dois dire !

Comment cela s'est-il produit ? Eh bien, avez-vous déjà entendu la phrase "Trop de cuisiniers gâtent la sauce" ? C'est ce qui s'est passé : deux ou trois personnes avaient travaillé sur le même fichier auparavant, et d'une manière ou d'une autre, ce nouvel id correspondait à l'un des id qu'ils avaient utilisés auparavant pour un élément. Ouf, ce fut une leçon si importante pour moi.

**Tous les éléments doivent avoir des id uniques.**

En tout cas, j'ai changé l'id de M. Lundi et j'ai réessayé.

```
<button type="button" class="btn btn-sm btn-success" id="<monday-hours-day">MON</button>
```

```
$('#'+day+'hours-day').addClass('unselected')
```

Et pourtant, M. Lundi ne voulait pas devenir gris.

### Corriger la plus grande erreur jamais commise

Après quelques heures de recherche sur Google, me demandant si c'était vraiment ce que je voulais faire pour le reste de ma vie (les yeux presque sortis de leurs orbites en essayant de trouver des moyens de rendre M. Lundi gris), j'ai compris quel était le problème.

Et je sais que vous mourez d'envie de le découvrir. Je promets que lorsque vous le saurez, vous me détesterez pour avoir fait l'erreur la plus stupide de l'histoire de l'humanité.

Le problème était que j'avais oublié un '-' (tiret) dans l'id avant hours, lors de l'ajout de la classe unselected.

```
$('#'+day+'hours-day').addClass('unselected')//est clairement faux.
```

```
$('#'+day+'-hours-day').addClass('unselected') //est le code parfait
```

M. Lundi est enfin devenu gris ! Cela m'a apporté un tel bonheur immense que j'ai dormi comme un chiot ce jour-là ! Oui, exactement comme celui sur cette photo.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ok7ZH_FQDizV5A8-QeyY8w.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/JCXANpeR2XI?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Adam Grabek</a> sur <a href="https://unsplash.com/search/photos/happy-sleeping?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

**Pour lire plus d'histoires sur mes escapades dans le monde du code, veuillez me motiver en cliquant sur l'icône "Applaudissements" plusieurs fois — idéalement 50, mais si vous êtes aussi paresseux que moi, j'accepterai 20 (Rien de moins que cela, s'il vous plaît ;) ).**

_Publié à l'origine sur [www.heisenbugtech.com](http://www.heisenbugtech.com/2018/06/26/tales-of-a-c-developer-learning-javascript/)_