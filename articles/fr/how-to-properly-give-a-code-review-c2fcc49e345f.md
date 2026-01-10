---
title: Comment faire une revue de code correctement
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2019-02-13T18:12:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-properly-give-a-code-review-c2fcc49e345f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*MQGtEWPkQYWeOatk
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: teamwork
  slug: teamwork
- name: technology
  slug: technology
seo_title: Comment faire une revue de code correctement
seo_desc: You're sitting at your desk, minding your own business, when one of your
  colleagues comes over and asks if you could give them a code review. Not wanting
  to seem rude (and remembering that they have bestowed this favor upon you not so
  long ago), you ...
---

Vous êtes assis à votre bureau, occupé à vos affaires, lorsqu'un de vos collègues vient vous demander si vous pourriez faire une revue de leur code. Ne voulant pas paraître impoli (et vous souvenant qu'ils vous ont rendu ce service il n'y a pas si longtemps), vous acceptez de vous rendre à leur bureau pour examiner ce sur quoi ils ont travaillé.

À ce moment-là, vous n'avez aucune idée de ce sur lequel votre collègue a travaillé. Il pourrait s'agir d'une simple correction de bug, d'une petite fonctionnalité ou d'un refactoring majeur. Quelle que soit l'ampleur de la tâche, vous devez toujours être préparé lorsque vous faites une revue de code. Pour savoir comment, lisez ce qui suit.

#### Les bases : qu'est-ce qu'une revue de code ?

Selon [Wikipedia](https://en.wikipedia.org/wiki/Code_review), une revue de code est :

> Une activité d'assurance qualité logicielle dans laquelle une ou plusieurs personnes vérifient un programme principalement en visualisant et en lisant des parties de son code source, et elles le font après l'implémentation ou comme une interruption de l'implémentation. Au moins l'une des personnes ne doit pas être l'auteur du code.

Et en termes simples, cela signifie que pour améliorer la qualité du produit de votre entreprise, il est nécessaire que différentes personnes évaluent le code.

Jusqu'à présent, je suppose que je n'ai rien ajouté de nouveau à votre perception d'une revue de code. Mais en toute honnêteté, il reste encore beaucoup d'ambiguïtés :

* Comment doit commencer une revue de code ?
* Comment savoir si une revue de code est bonne ou mauvaise ?
* Combien de temps doit durer une revue de code ?

Ce ne sont que quelques exemples de questions que je suis sûr que vous vous posez. Bien qu'il n'y ait pas de réponse simple pour chacune d'elles, il existe des directives que vous pouvez suivre pour vous aider.

![Image](https://cdn-media-1.freecodecamp.org/images/nCL-jGPPlOdY1JaYcT4PXYDTN56J1mPHEDN5)
_Photo par [Unsplash](https://unsplash.com/@heftiba?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Toa Heftiba</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### La préparation est essentielle

Avant de commencer la revue de code proprement dite, posez-vous ces deux questions :

1. Êtes-vous au courant de ce sur quoi votre collègue a travaillé ?
2. Êtes-vous familier avec la partie du code sur laquelle ils ont travaillé ?

Si vous avez répondu non à l'une de ces questions, alors vous devez faire quelques recherches. Cela vous permettra de venir à la revue de code aussi préparé que possible.

Une façon de combler cette lacune est de regarder le ticket/la tâche associée à la fonctionnalité. Vous devriez y trouver suffisamment d'informations pour connaître l'ampleur et la raison derrière la tâche du développeur. De plus, si c'est courant dans votre lieu de travail, vous pouvez consulter les commentaires dans le ticket. Vous voulez voir s'il y a eu des changements dans le ticket qui ne correspondent pas à l'intention originale. Et si tout le reste échoue, avant de commencer la revue de code, demandez à votre collègue d'expliquer ce sur quoi ils ont travaillé et pourquoi.

Ce que je fais toujours, même si je suis bien au courant de ce qu'est la tâche, c'est de demander au développeur d'expliquer l'ampleur de la tâche en ses propres mots. Ainsi, je peux minimiser le risque de ne pas être au courant de quelque chose dans la tâche. Lorsque le développeur doit réitérer ce qu'il a fait, il peut mieux s'expliquer à lui-même ce qu'il a fait.

![Image](https://cdn-media-1.freecodecamp.org/images/Z52U2ZJOF56lA-XRETqnNYA3MwSU4LgKSQV3)
_Photo par [Unsplash](https://unsplash.com/@roller1?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">kyle smith</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### Écoutez, puis posez des questions

Chaque conversation est une voie à double sens : tandis qu'une partie parle, l'autre écoute. La même logique s'applique à une revue de code. Essayez de ne pas interrompre l'autre développeur afin de ne pas perturber le flux qu'il a préparé dans son esprit. Prenez des notes mentales ou écrivez les choses qui vous semblent importantes afin de vous rappeler ce que vous devez demander lorsque ce sera votre tour.

Une revue de code peut devenir longue et fastidieuse, et il est important de rester concentré et de poser des questions cruciales. Si quelque chose ne vous semble pas clair, demandez au développeur de l'expliquer. Il n'y a aucune honte à ne pas être parfaitement connaisseur de chaque section de votre base de code.

En posant des questions, non seulement **vous** vous familiarisez davantage avec le code, mais le développeur vit également l'expérience de devoir expliquer à quelqu'un d'autre ce qu'il a fait. En faisant cela, plus souvent qu'autrement, le développeur pourrait identifier un scénario auquel il n'avait pas pensé. Ou vous pourriez voir un certain flux qui pourrait causer un bug.

Je sais que certains d'entre vous pourraient dire, **"mais comment puis-je poser des questions si j'ai moins/plus d'expérience que l'autre développeur ? Ne serait-ce pas impoli ?"**

La réponse est **NON**.

Lorsque personne ne pose de questions, personne n'apprend. Le but d'une revue de code n'est pas seulement d'apposer un tampon d'approbation sur ce que l'autre développeur a fait. Vous êtes là pour passer en revue la logique du code, mais vous êtes également en partie responsable de la structure globale du code.

![Image](https://cdn-media-1.freecodecamp.org/images/ayTOonqiasKzPynMEhepqu4Xx0wxSkuEanTI)
_Photo par [Unsplash](https://unsplash.com/@h4x0r3?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Thao Le Hoang</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### Soyez empathique mais honnête

Les développeurs sont fiers de leur travail. Comme la plupart des êtres humains, ils n'aiment pas entendre quelqu'un d'autre leur dire ce qu'ils font de travers. Cela dit, il est important de faire entendre votre voix en tant que relecteur.

De la même manière que chaque personne aura une saveur de glace différente, chaque développeur a une opinion différente sur la manière dont le code doit être écrit et maintenu. Néanmoins, il existe certaines vérités communes auxquelles chaque développeur doit adhérer. Alors, pour garder les choses calmes, assurez-vous de formuler vos déclarations de manière constructive. Ainsi, personne ne devrait être offensé.

Bien sûr, vous aurez des désaccords. Dans certaines situations, il sera important de souligner les inconvénients du code qui doit être réécrit. Si vous atteignez une impasse, essayez d'en discuter avec un autre développeur ou un chef d'équipe. N'oubliez jamais que de l'autre côté, il y a un autre développeur avec son propre point de vue.

#### Bonnes pratiques à garder à l'esprit

Bien que les sujets discutés ci-dessus forment le trépied d'une revue de code (si vous voulez), il y a aussi d'autres choses auxquelles prêter attention :

* Si pertinent, demandez si des tests unitaires ont été ajoutés et, si oui, passez-les en revue
* La [documentation](https://medium.freecodecamp.org/why-documentation-matters-and-why-you-should-include-it-in-your-code-41ef62dd5c2f) fait partie de la revue de code (et s'il n'y en a pas, discutez de l'ajout de celle-ci)
* Avant que la revue de code ne commence, demandez au développeur combien de temps il pense que cela devrait prendre (cela vous aidera à planifier votre journée en conséquence)
* S'il y a beaucoup de changements suite à la revue de code, assurez-vous d'en planifier une autre afin que la prochaine itération ne passe pas inaperçue
* Soyez courtois et essayez de faire des compliments à l'autre développeur sur ce qu'il a fait

Aucune revue de code ne se ressemble, et comme pour la plupart des activités, la pratique rend parfait. Faites confiance à vos instincts et faites confiance à vos collègues. Tout le reste suivra.