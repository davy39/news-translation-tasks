---
title: Quels langages ont obtenu le plus d'étoiles GitHub en 2016 ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-16T17:29:09.000Z'
originalURL: https://freecodecamp.org/news/data-visualization-what-languages-got-the-most-github-stars-in-2016-a4e3908a9532
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-hRBr9wXEoFe_3TuTpuDVA.jpeg
tags:
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: JavaScript
  slug: javascript
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Quels langages ont obtenu le plus d'étoiles GitHub en 2016 ?
seo_desc: 'By Jose Aguinaga

  A few weeks ago I decided to build an application to find which programming languages
  I star the most in GitHub.

  Why? Because lately I had been starring projects about Machine Learning, Data Science,
  and Artificial Intelligence. I wa...'
---

Par Jose Aguinaga

Il y a quelques semaines, j'ai décidé de créer une application pour découvrir quels langages de programmation j'ai le plus étoilés sur GitHub.

Pourquoi ? Parce que dernièrement, j'avais étoilé des projets sur **l'apprentissage automatique, la science des données** et **l'intelligence artificielle**. Je voulais voir si mon intérêt accru se refléterait d'une manière ou d'une autre dans la chronologie de mes projets étoilés. Et quelle meilleure façon de le découvrir qu'en utilisant un peu de science des données ?

L'expérience consistait à obtenir les informations de GitHub, à les nettoyer et à les afficher dans une visualisation. Pour l'essayer vous-même, rendez-vous sur la page web suivante.

[**Quels langages ont obtenu le plus d'étoiles GitHub en 2016 ?**](https://starred.jjperezaguinaga.com/)  
[_Un streamgraph des langages étoilés sur GitHub en 2016._starred.jjperezaguinaga.com](https://starred.jjperezaguinaga.com/)

Après l'avoir essayé vous-même, donnez-moi un moment pour expliquer comment cela fonctionne et vous montrer quelques exemples intéressants.

### Récupération et analyse des données

Pour le meilleur ou pour le pire, GitHub ne fournit pas de moyen facile de consommer ces informations. Vous devez parcourir tous vos projets étoilés sur [github.com](https://github.com/jjperezaguinaga?tab=stars), puis cliquer sur de nombreuses pages pour les trouver tous. Selon le nombre de dépôts que vous avez étoilés, cela pourrait vous prendre quelques minutes avant de pouvoir voir tous les projets sur une période spécifique.

La bonne nouvelle est que GitHub dispose d'une [API d'activité d'étoilage](https://developer.github.com/v3/activity/starring/), que j'ai ensuite utilisée pour écrire un utilitaire JavaScript afin de récupérer tous mes projets étoilés de l'année. GitHub vous permet de passer un drapeau pour voir la date à laquelle vous avez étoilé un projet pour la première fois, ce qui m'a permis d'obtenir uniquement les projets que j'ai étoilés en 2016.

Avec les données récupérées, j'ai procédé à leur filtrage en fonction du langage que GitHub leur a attribué. [Ramda](http://ramdajs.com/) s'est avéré particulièrement utile pour mapper et réduire ces données.

Ensuite, pour visualiser ces informations, j'ai décidé d'afficher la fréquence de chaque langage de programmation de dépôt à travers un graphique connu sous le nom de [_streamgraph_](https://en.wikipedia.org/wiki/Streamgraph). En agrégeant chaque instance de langage par mois, je pouvais voir l'augmentation et la diminution de l'intérêt au fil du temps.

![Image](https://cdn-media-1.freecodecamp.org/images/mSp-YanfncIQV-QgEP9ERSpsGLFvqYSOwYt7)
_Un streamgraph de mes projets étoilés en 2016 agrégés par langage et distribués par mois. GitHub est parfois incapable de décider d'un langage spécifique pour un projet et donne **null** à la place._

Comme nous pouvons le voir sur le graphique, j'ai étoilé **142 projets** en 2016. Il y avait plus de 15 langages parmi mes dépôts étoilés, mais je n'affiche que les 7 premiers, car la fréquence par langage diminue après ce nombre. Le langage le plus populaire est JavaScript, ce qui ne me surprend pas, car je travaille comme ingénieur Front-End au quotidien.

Les deuxième et troisième langages de programmation sont **Python** et **Go**, qui sont probablement liés aux projets sur l'intelligence artificielle / l'apprentissage profond dont j'ai parlé plus tôt. Python avait du sens, car il a récemment été considéré comme [le langage le plus populaire pour le Machine Learning](https://www.ibm.com/developerworks/community/blogs/jfp/entry/What_Language_Is_Best_For_Machine_Learning_And_Data_Science?lang=en).

### Tout le monde obtient un graphique.

Dans le cadre du développement de l'outil, j'ai testé l'application avec d'autres développeurs. Cela a produit une série de graphiques intéressants.

Voici une liste de quelques développeurs célèbres, regroupés par les langages qu'ils ont le plus étoilés.

#### Développeurs Javascript

![Image](https://cdn-media-1.freecodecamp.org/images/UQpYL0aoitvNqxcOkbjSQYDYCrPOmN3dDnI-)
_[Addy Osmani](undefined" rel="noopener" target="_blank" title=") — Ingénieur de la plateforme Web chez Google_

![Image](https://cdn-media-1.freecodecamp.org/images/EMz3T7QrysKajc5DJYiTTivCKLMH5BwZRaKg)
_[Paul Irish](undefined" rel="noopener" target="_blank" title=") — Ingénieur des outils de développement Chrome_

![Image](https://cdn-media-1.freecodecamp.org/images/ExICtXhMOdoOXMOlgplXX1J7MMHDT-E29Shl)
_[Eric Elliott](undefined" rel="noopener" target="_blank" title=") — Développeur Javascript_

![Image](https://cdn-media-1.freecodecamp.org/images/AcsyJGT2XWqFiw4HrPeMotvyqLVvispuBOk4)
_[Sindre Sorhus](undefined" rel="noopener" target="_blank" title=") — Licorne déguisée_

![Image](https://cdn-media-1.freecodecamp.org/images/5YQ-WFc89RtC9AjveOxw2XZKWvGf2sl720Bn)
_[John Resig](undefined" rel="noopener" target="_blank" title=") — Ingénieur principal à Khan Academy et créateur de jQuery_

![Image](https://cdn-media-1.freecodecamp.org/images/m3DS7IOoKkFf3ckfgcrRq88lgkte4YoZidb5)
_[Dan Abramov](undefined" rel="noopener" target="_blank" title=") — Ingénieur chez Facebook, co-auteur de Redux, Create React App et React.js_

![Image](https://cdn-media-1.freecodecamp.org/images/NpZZHANKaTtHuGq9OZBTbhUHzBfQ7Bs9dtAo)
_[Ben Alpert](https://github.com/spicyj" rel="noopener" target="_blank" title=") — Ingénieur chez Facebook, contributeur React.js_

#### Développeurs Golang

![Image](https://cdn-media-1.freecodecamp.org/images/MN3igg-z5QlxNlD16JwA3kD8DMt4vyryiqVW)
_[TJ Holowaychuk](undefined" rel="noopener" target="_blank" title=") — Fondateur de Apex.sh, développeur Javascript et Golang_

![Image](https://cdn-media-1.freecodecamp.org/images/THcSt1hkg-pWGXz22Dv3XQFCfRsb8JBHvGB6)
_[Jessie Frazzelle](https://twitter.com/jessfraz" rel="noopener" target="_blank" title=") — Tout sur les conteneurs_

![Image](https://cdn-media-1.freecodecamp.org/images/letMN4s0Z7H9JX05FhRsYXF9hVb-P8wbUTwH)
_[Josh Baker](undefined" rel="noopener" target="_blank" title=") — Prépare un goulash mortel_

![Image](https://cdn-media-1.freecodecamp.org/images/d-T1bJOrS2IQnk0J4dSRciE5Sk8LfwcWqmWo)
_[aarti](https://github.com/aarti" rel="noopener" target="_blank" title=") — Contributeur d'Exercism.io_

#### Développeurs Python

![Image](https://cdn-media-1.freecodecamp.org/images/L-zwvoLMN-Z75MRsA2Fu8dqIbLw98BrEfo28)
_[Thaddee Tyl](undefined" rel="noopener" target="_blank" title=") — Il a vu du code_

![Image](https://cdn-media-1.freecodecamp.org/images/9eOLVdUA4zl0mCL-qHKrqhVe-FaQuQjEb5q7)
_[John Washam](undefined" rel="noopener" target="_blank" title=") — Futur ingénieur chez Google_

![Image](https://cdn-media-1.freecodecamp.org/images/Qu8zbkRm3pamo4rMY4kGcGl9uOIritD84rjm)
_[Geimfari](undefined" rel="noopener" target="_blank" title=") — Pythonista, Erlanger, Cosmonaute_

![Image](https://cdn-media-1.freecodecamp.org/images/o6x0Hp927aOLyKNvmRamf4nLHfu4FeUORk2V)
_[Nam Vu](undefined" rel="noopener" target="_blank" title=") — Futur ingénieur en Machine Learning_

#### Swift, R

![Image](https://cdn-media-1.freecodecamp.org/images/ofo9qk48jvS8fkLlzcLzy57qXvdzNbBqXKj4)
_[Luke Zhao](https://github.com/lkzhao" rel="noopener" target="_blank" title=") — Développeur iOS_

![Image](https://cdn-media-1.freecodecamp.org/images/8enRlEKgyO6Wostjo3R71sqVSnz05jIvCabg)
_[Jennifer Bryan](https://github.com/jennybc" rel="noopener" target="_blank" title=") — Professeure à l'UBC_

### Le truc avec les données

J'ai beaucoup apprécié cette expérience et j'ai appris deux leçons importantes :

* **Les données peuvent être belles**. Tout n'a pas besoin d'avoir un sens profond pour être intéressant. Par exemple, la couverture de cet article est le produit de la superposition d'une série de _streamgraphs_ à partir de divers ensembles de données. J'ai tellement aimé que je l'ai même [copyrightée](https://blockai.com/c/e1jLAq).
* **Nos données nous identifient**. Étant donné suffisamment de projets étoilés, les chances d'avoir deux individus avec exactement les mêmes dépôts étoilés au même moment sont négligeables*. Ainsi, si nous analysons les motifs d'étoilage d'un développeur, nous pourrions l'identifier en voyant ses données. C'est un exemple d'[Analytique Comportementale](http://dl.acm.org/citation.cfm?id=2971707&dl=ACM&coll=DL&CFID=716696458&CFTOKEN=32651178), utilisée par le passé pour [identifier les utilisateurs par l'utilisation d'applications mobiles](http://dl.acm.org/citation.cfm?id=2971707&dl=ACM&coll=DL&CFID=716696458&CFTOKEN=32651178).

À la fin de cette expérience, je m'intéressais davantage à l'exploration des usages de la Visualisation de Données et du Machine Learning qu'auparavant**. Je continuerai à approfondir mes connaissances dans ce domaine pour créer plus d'expériences comme celle-ci à l'avenir.

### Veuillez essayer cela chez vous

Si vous êtes curieux à propos du code, vous pouvez le voir sur GitHub.

[**jjperezaguinaga/github-patterns**](https://github.com/jjperezaguinaga/github-patterns)  
[_github-patterns - ? Quels langages ont obtenu le plus d'étoiles GitHub en 2016 ?g_ithub.com](https://github.com/jjperezaguinaga/github-patterns)

Gardez à l'esprit que le code est très sale, donc des erreurs peuvent survenir (par exemple, l'erreur de dépassement de la limite de taux de GitHub n'est pas capturée), donc ne le prenez pas comme référence pour des projets de production réels. N'hésitez pas à [changer, étendre ou forker le code](https://github.com/jjperezaguinaga/github-patterns) comme vous le souhaitez.

_*Non négligeable, mais très improbable. Une personne devrait étoiler le même projet à la même seconde pour partager le même motif. Il y a 31557600 secondes dans une année astronomique et environ [20M](https://octoverse.github.com/) de dépôts sur GitHub à la fin de 2016, et environ 5,8M d'utilisateurs actifs sur GitHub. Dites-moi quelles sont les chances que deux personnes avec 10 projets étoilés aient le même motif._

_**Udacity a publié ce week-end [un nouveau nanodiplôme sur les fondements du Deep Learning](https://www.udacity.com/course/deep-learning-nanodegree-foundation--nd101). Je me suis inscrit et publierai un aperçu après l'avoir terminé._