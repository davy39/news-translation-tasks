---
title: 'Comment aborder votre entretien de développeur Web Q&A : à quoi sert un doctype
  ?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-17T22:42:47.000Z'
originalURL: https://freecodecamp.org/news/web-developer-interview-q-a-what-does-a-doctype-do-146dd757d7d1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*T2mgRWcGugiSXs_kRsRQVg.jpeg
tags:
- name: interview
  slug: interview
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Comment aborder votre entretien de développeur Web Q&A : à quoi sert un
  doctype ?'
seo_desc: 'By Zuzana K

  One part of the interview process for a web developer position probably involves
  answering some questions. Yes, we are not only expected to do the web stuff, but
  we are also expected to know the web stuff.

  I am very capable of writing an ...'
---

Par Zuzana K

Une partie du processus d'entretien pour un poste de développeur web implique probablement de répondre à certaines questions. Oui, non seulement nous devons faire du web, mais nous devons aussi connaître le web.

Je suis tout à fait capable d'écrire un document HTML, d'utiliser des balises sémantiques et de suivre les meilleures normes web, mais il y a des choses que je n'ai jamais pensé à apprendre.

J'ai récemment reçu une liste de questions d'entretien pour développeurs web, et lorsque j'ai jeté un premier coup d'œil à la liste, mon cœur a presque arrêté de battre.

* À quoi sert un doctype ?
* Y a-t-il des problèmes à servir des pages en tant qu'application/xhtml+xml ?
* Quelle est la différence entre la détection de fonctionnalités, l'inférence de fonctionnalités et l'utilisation de la chaîne UA ?

Eh bien, en toute honnêteté, je n'aurais pas pu répondre à la plupart des questions.

Je suppose que c'est là qu'un diplôme en informatique pourrait être utile.

Mais, en tant que développeur autodidacte, je me suis concentré sur le faire plutôt que sur le savoir. Puisque je cherche moi-même un emploi, cependant, j'ai pensé qu'il pourrait être judicieux de me préparer pour un entretien de développeur web et de répondre à certaines de ces questions.

Donc, dans les prochains posts (je ne sais pas combien), je vais prendre une question d'un entretien de développeur web (qui a été très gracieusement fournie par [Rose](http://www.verifyrecruitment.com/blog/index.php/tag/askrose/) de l'agence de recrutement Verify à Dublin, en Irlande), et y répondre du mieux que je peux.

Je vais aborder certaines questions sur HTML, CSS et JavaScript.

Les réponses ne seront pas exhaustives, mais elles nous donneront, à vous et à moi, un bon point de départ si nous voulons creuser un peu plus.

### Question : À quoi sert un <doctype> ?

Doctype est l'abréviation de « document type ». Évidemment, non ? Je veux dire, qui aurait pensé ?

Mais sérieusement, pourquoi devons-nous spécifier le doctype lorsque nous enregistrons le document en tant que fichier HTML, ce qui, sûrement, signifie qu'il s'agit d'un document HTML ? Le problème, c'est que vous avez aussi besoin d'un <!doctype html> pour une page 'php' qui inclut du balisage HTML.

C'est là que cela devient confus. Alors, décomposons un peu.

La déclaration de doctype indique au navigateur quel type de document attendre : HTML5, HTML4.0x, XHTML1.0 (Strict, Transitional ou Frameset), XHTML1.1, [et autres](https://www.w3.org/QA/2002/04/valid-dtd-list.html).

Mais pourquoi est-ce requis ?

Pour des raisons de compatibilité.

Dans les premiers jours d'Internet, deux navigateurs principaux étaient en compétition l'un contre l'autre. Netscape Navigator et Internet Explorer. Ils continuaient à sortir de nouvelles fonctionnalités qui étaient souvent incompatibles avec les autres fonctionnalités existantes ou d'autres navigateurs.

C'était une période difficile pour les développeurs (prenons tous une minute pour compter nos bénédictions).

Alors, le fondateur du World Wide Web, Sir Tim Berners-Lee, a fondé le [World Wide Web Consortium](https://www.w3.org/) (W3C) pour standardiser les protocoles et les technologies utilisés pour construire le web et pour faciliter la vie des développeurs et des utilisateurs.

Les nouveaux protocoles étaient excellents pour les nouveaux navigateurs et les nouvelles implémentations, mais ils auraient complètement cassé les sites existants.

Entrez les Définitions de Type de Document (DTD).

Les DTD indiquent à l'analyseur comment traduire le code en ce que vous voyez à l'écran afin que l'apparence soit uniforme dans différents navigateurs.

Pour rendre un document HTML4.01, utilisez ce code tout en haut de votre document :

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"> 
```

Pour rendre un document HTML5, incluez ce code à la place :

```
<!doctype html>
```

HTML5 est, admettons-le, beaucoup plus facile à déclarer.

L'utilisation de la déclaration de doctype est une exigence imposée par le W3C ; sans elle, les [validateurs HTML](https://validator.w3.org/) ne fonctionneront pas (parce qu'ils ne sauront pas quelle norme utiliser pour vérifier votre code) et le navigateur pourrait rendre le document en mode quirks.

Quoi ? Un mode quirks ?

Si vous ne déclarez pas le doctype, les navigateurs peuvent interpréter le document comme autre chose que du HTML et passer en mode quirks, qui est, en gros, un mode pour les documents sans déclaration de doctype.

Il peut y avoir beaucoup de quirks dans le mode quirks ; cela peut vraiment perturber l'apparence de votre document à l'écran !

Le mode quirks, le mode presque standard et le mode standard complet sont des choses que je vais examiner la prochaine fois.

Pour l'instant, prenez soin de votre doctype et à bientôt !

*Si vous avez apprécié cet article et l'avez trouvé bénéfique, envisagez de me laisser un commentaire ou quelques applaudissements. Merci !*