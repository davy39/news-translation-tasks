---
title: Comment utiliser les badges GitHub pour ne plus se sentir comme un débutant
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-30T14:30:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-badges-to-stop-feeling-like-a-noob-d4e6600d37d2
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cab8d740569d1a4ca9262.jpg
tags:
- name: Shields
  slug: shields
- name: 100DaysOfCode
  slug: 100daysofcode
- name: badge
  slug: badge
- name: GitHub
  slug: github
- name: Imposter syndrome
  slug: imposter-syndrome
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment utiliser les badges GitHub pour ne plus se sentir comme un débutant
seo_desc: 'By Cam Barts

  Impostor Syndrome is real, and it plagues new developers. We get all the way through
  a tutorial, bootcamp, or even a degree, yet we still shy away from sharing our code.
  We fear negative feedback on our code’s quality. No one suffers mor...'
---

Par Cam Barts

Le syndrome de l'imposteur est réel et il tourmente les nouveaux développeurs. Nous suivons des tutoriels, des bootcamps, voire même un diplôme, mais nous hésitons toujours à partager notre code. Nous craignons les retours négatifs sur la qualité de notre code. Personne ne souffre plus de cela que les développeurs autodidactes. Parce que nous n'avons aucune expérience ou formation "réelle" ou "officielle", nous considérons notre code comme étant de mauvaise qualité.

J'étais dans cette situation il y a quelques mois. Je travaillais sur [Test-Driven Development With Python de Harry Percival](http://www.obeythetestinggoat.com/). Même si je suivais bien le tutoriel, j'étais gêné à l'idée de partager mon code. Même si mon application fonctionnait comme prévu, je ne voulais pas partager mes progrès. Je ne voulais pas que quelqu'un me signale une erreur évidente à laquelle j'étais aveugle. Je voulais que les autres apprécient mon produit, mais je ne voulais pas qu'ils voient à quel point j'étais un mauvais développeur.

Après avoir fait une pause dans [mon propre projet](https://github.com/cam-barts/ObeyTheTestingGoat), j'ai commencé à regarder d'autres projets sur GitHub. J'en ai trouvé quelques-uns qui avaient une petite image sur leurs pages README.

![Image](https://cdn-media-1.freecodecamp.org/images/pPzFRYVv5jJvht3U-2f8KgGIEoF0yqdxNrAD)

À l'époque, étant un débutant, je pensais que c'était simplement une image que Linus Torvalds vous remettait sur une clé USB lorsque vous sortiez de l'école des "Vrais Développeurs". Il ne m'est jamais venu à l'esprit de cliquer dessus. Je pensais que c'était une image statique hébergée quelque part dans le dépôt. Plus tard, je suis tombé sur un projet qui affichait que la construction avait échoué.

![Image](https://cdn-media-1.freecodecamp.org/images/LSWK5plwMRtm14FC4QTmVhBKRF4wxeCj591G)

Pourquoi quelqu'un prendrait-il le temps d'ajouter une image qui dit que leur construction ne passe pas ? Pourquoi faire l'effort d'enlever l'autre image pour mettre celle-ci ? Une image qui dit que votre projet est cassé et l'afficher pour que le monde entier la voie ? Par pure curiosité, j'ai ouvert le format brut du README. J'ai vu ce code :

```
[![Build Status](https://travis-ci.com/username/projectname.svg?branch=master)](https://travis-ci.com/username/projectname)
```

J'étais suffisamment familiarisé avec le markdown pour reconnaître qu'il s'agissait d'un lien cliquable. J'ai donc cliqué sur le bouton et il m'a emmené à Travis-CI. Tout à coup, cela a eu du sens pour moi. Ce bouton n'était pas mis à jour par le développeur du projet, Travis-CI le mettait à jour. **C'est un bouton dynamique.**

### Mon Premier Badge

Ainsi, une fois que j'ai découvert le badge de construction de Travis-CI, j'ai dû l'avoir pour mon projet. Après tout, mon projet entier était consacré à l'écriture et à l'utilisation de tests. Alors pourquoi ne pas avoir quelque chose qui les exécute automatiquement ?

J'ai donc [configuré](https://docs.travis-ci.com/user/getting-started) Travis-CI pour exécuter mes tests unitaires lorsque je poussais des changements vers GitHub. Tout en haut de la page où Travis-CI les exécute, se trouve le badge. J'ai cliqué dessus et obtenu le markdown. Je l'ai ajouté à mon README. J'ai navigué vers la page du projet sur GitHub et VOILÀ ! Mon premier badge était là. J'étais accro !

### La Chasse

![Image](https://cdn-media-1.freecodecamp.org/images/mJJxEV72ft2VNl-DYegNLQ5IyvfxICsSxYtg)

J'ai apprécié que le badge soit un signe clair de l'état actuel de mon projet. Je voulais en savoir plus, alors je suis parti à la chasse aux autres badges. Un autre badge courant que j'ai trouvé était la couverture de code. Le rapport de couverture pouvait être envoyé par Travis-CI à un outil appelé [CodeCov.](http://codecov.io/) Vous pouviez obtenir un badge indiquant la couverture de vos tests, ce qui correspond à la qualité des tests de votre application.

![Image](https://cdn-media-1.freecodecamp.org/images/nXweRmbRr3BHhKQA0ChyI2WHrmiky-FBFDA-)

J'ai également trouvé des badges de licence, et il était logique d'avoir un badge de licence si j'avais une licence. J'ai donc [choisi une licence](https://choosealicense.com/) et je l'ai ajoutée au dépôt. Obtenir le badge pour cela a nécessité une rapide recherche Google, et j'ai trouvé [ce gist](https://gist.github.com/lukas-h/2a5d00690736b4c3a7ba) avec tous les badges de licence courants.

![Image](https://cdn-media-1.freecodecamp.org/images/HoisHZJSio0u2t9dCdOkD8LP6AnWJCpr0JRk)

Venant d'un milieu militaire avec une formation en sécurité, je sais que la plupart des vulnérabilités proviennent de logiciels obsolètes. En tant que nouveau développeur, je sais que cela s'applique également aux logiciels dont dépend votre logiciel. J'ai entendu parler de PyUp grâce au podcast _Talk Python to Me_ de [Michael Kennedy](https://medium.com/u/8f2ec0cf186b). Lorsque j'ai navigué vers [le site](http://pyup.io/), j'ai vu les mots que j'avais commencé à aimer voir, "Gratuit pour l'Open Source". Étant à la chasse aux nouveaux badges, j'ai eu de la chance. En effet, ils fournissent un badge, alors bien sûr, je l'ai ajouté au README.

![Image](https://cdn-media-1.freecodecamp.org/images/9AZzZesmquR0zMx0JtUNAH80jdZ6QeSaiKLQ)

Enfin, j'ai découvert que vous pouviez avoir un badge pour le style. J'avais déjà joué avec [Black](https://github.com/ambv/black) auparavant, et j'ai trouvé un exemple de badge de style et j'ai su que je devais l'avoir. Pour l'amour de mon intégrité, je voulais m'assurer que mon code était toujours conforme au style de Black. J'ai découvert [pre-commit](https://pre-commit.com/), que je pouvais utiliser pour formater mon code avant même de le commiter. Après avoir plongé dans le terrier de pre-commit (qui exécute également mon code contre [bandit](https://github.com/PyCQA/bandit) pour la sécurité et trie mes imports et mes dépendances), je me suis senti confiant pour ajouter le badge Black à mon README.

### Le Résultat Final

Le premier résultat de la chasse aux badges est que **mon projet est de meilleure qualité**. J'ai ajouté une licence à mon projet, j'ai veillé à ce que mes dépendances restent à jour et j'ai maintenu le style de mon projet conforme parce que je voulais les badges.

Plus notablement, **j'ai plus confiance en mon projet**. Je peux en parler en sachant qu'il n'y a pas de failles béantes. Je sais que je suis beaucoup moins susceptible de recevoir des retours sur mon irresponsabilité en matière de sécurité ou mon manque de conformité de style.

Pour faire simple, je me sens mieux à propos de mon code parce que j'ai ces badges GitHub.