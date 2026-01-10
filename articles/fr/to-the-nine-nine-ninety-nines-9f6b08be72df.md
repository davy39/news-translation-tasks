---
title: À la neuf-neuf-neuf-neuf
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2016-01-28T15:58:41.000Z'
originalURL: https://freecodecamp.org/news/to-the-nine-nine-ninety-nines-9f6b08be72df
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3TUkJkWK5YyV4OTFKzomKA.jpeg
tags:
- name: Design
  slug: design
- name: education
  slug: education
- name: General Programming
  slug: programming
- name: social media
  slug: social-media
- name: technology
  slug: technology
seo_title: À la neuf-neuf-neuf-neuf
seo_desc: 'Yesterday GitHub — the center of the open source universe — went down for
  three hours.

  If you’re new to software development, it may seem strange that a website going
  down for three hours would warrant an article.

  This outage is newsworthy for two re...'
---

Hier, GitHub — le centre de l'univers open source — est tombé en panne pendant trois heures.

Si vous êtes nouveau dans le développement logiciel, il peut sembler étrange qu'un site web en panne pendant trois heures mérite un article.

Cette panne est nouvelle pour deux raisons. Premièrement, parce que ces types de pannes sont rares. La dernière panne majeure de GitHub remonte à 2010, lorsque son PDG a accidentellement [détruit sa base de données de production](https://github.com/blog/744-today-s-outage).

![Image](https://cdn-media-1.freecodecamp.org/images/1*pr5ewaaz05HleGNvDntxQQ.png)
_La dernière fois que la page 500 de GitHub a été largement vue remonte à 2010._

Deuxièmement, GitHub est maintenant le [87e site le plus fréquenté sur Internet](http://www.alexa.com/siteinfo/github.com), [valant 2 milliards de dollars](http://www.wsj.com/articles/github-raises-250-million-at-2-billion-valuation-1438206722), et dispose d'une [équipe de près de 500 personnes](https://github.com/about/team) — dont la plupart sont des ingénieurs.

Un site web construit pour les développeurs, par des développeurs, avec une forte culture d'ingénierie, qui tombe en panne en plein milieu d'une journée de travail — c'est un rappel frappant de la difficulté réelle du développement web.

En attendant le rapport post-mortem de GitHub sur la panne (mise à jour : [c'était une panne de courant](https://github.com/blog/2101-update-on-1-28-service-outage)), explorons le concept de « disponibilité » et parlons de son importance.

#### Haute disponibilité — temps de fonctionnement, temps d'arrêt et beaucoup de neuf

Tout d'abord, couvrons quelques termes que vous entendrez les développeurs utiliser.

Le **temps de fonctionnement** est lorsque un service est disponible et répond aux demandes. Vous lisez cet article sur Medium, donc cela signifie que Medium est en ligne. Maintenant est le temps de fonctionnement de Medium.

Le pire ennemi du temps de fonctionnement est le **temps d'arrêt** — lorsque un service ne répond pas aux demandes.

Sauf si un service était prévu pour tomber en panne lors d'une **panne planifiée** (maintenance) — ou s'il y a un problème de connectivité réseau — le temps d'arrêt signifie généralement que les serveurs ont planté. Quelque part, un développeur essaie frénétiquement de remettre ces serveurs en ligne, afin de sauver ses perspectives de carrière chez son employeur actuel.

La **disponibilité** est le rapport entre le temps de fonctionnement et le temps d'arrêt. Elle est exprimée en « **neuf** ». Vous entendrez quelqu'un dire « Nous avons un temps de fonctionnement de cinq neuf ». Cela signifie que le service est disponible 99,999 % du temps (temps de fonctionnement), et seulement en panne 0,001 % du temps (temps d'arrêt).

Alors, à quoi ressemblent ces chiffres pour des humains comme vous et moi ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*0WSusWv4X_ASlkgLkIFP1w.jpeg)

La norme d'or de la **haute disponibilité** est généralement considérée comme cinq neuf.

Comme vous pouvez le voir, tomber en panne pendant plus d'une heure au total la même année vous fait descendre à « trois neuf ». Désolé GitHub, je suppose que vous allez être coincé ici dans le club des « trois neuf » avec Free Code Camp cette année.

Free Code Camp n'a pas réellement été en panne pendant plus de quelques secondes jusqu'à présent en 2016, mais nous prévoyons de tomber en panne pendant quelques minutes à la fois tout au long de l'année (pannes planifiées) — généralement tard dans la nuit dans l'hémisphère occidental. Et cela s'additionnera probablement à plus d'une heure au total.

Pour nous, trois neuf est bien. Parce que atteindre une haute disponibilité est difficile et coûte généralement beaucoup d'argent.

#### Pourquoi la haute disponibilité est-elle si importante ?

La haute disponibilité est coûteuse à atteindre. Ajouter un neuf supplémentaire à votre disponibilité peut impliquer des millions de dollars en temps de développement et en infrastructure redondante. Alors pourquoi s'embêter ?

Si vous avez vu le film sombre de 2010 « The Social Network », vous vous souvenez peut-être de la scène où le personnage de Mark Zuckerberg [parle de l'importance de la disponibilité](https://www.youtube.com/watch?v=36zhwwm3Lg0). « Nous ne plantons jamais. Si les serveurs sont en panne même pour une journée, notre réputation est irréversiblement détruite. »

![Image](https://cdn-media-1.freecodecamp.org/images/1*4qmA-RUMbZ20L4AAG3FxvA.gif)

Avez-vous vu cette citation et pensé : « en panne même pour une journée — mince, cela vous fait déjà descendre à deux neuf ! » Si oui, merci d'avoir pris le temps de lire mon graphique.

Que cette citation soit une hyperbole — Twitter avait l'habitude de planter tout le temps et cela n'a pas « irréversiblement détruit » sa réputation — tomber en panne vous fait paraître marginalement moins professionnel, au moins aux yeux des autres développeurs. Donc, moins vous tombez en panne, mieux c'est.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fjIjeUvlPu1g-QQD79E0gA.png)
_La fameuse « fail whale » de Twitter. Pour les lecteurs curieux, voici [une conférence d'une heure](https://vimeo.com/53693402" rel="noopener" target="_blank" title=") sur la façon dont ils ont finalement résolu leurs problèmes de temps de fonctionnement en se restructurant._

Une autre raison pour laquelle la haute disponibilité est importante est que le temps d'arrêt peut littéralement coûter à certaines entreprises des millions de dollars en revenus perdus.

Amazon a réalisé un chiffre d'affaires de 81 milliards de dollars en 2014. Il y a 525 600 minutes dans une année. Donc **Amazon vend pour 156 110 $ de marchandises chaque minute**.

La différence entre « quatre neuf de disponibilité » et « cinq neuf de disponibilité » est d'environ 47 minutes par an, ce qui pour Amazon représente plus de 7 millions de dollars de revenus.

#### Comment puis-je maximiser le temps de fonctionnement sans me ruiner ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*7MNVHQPs3Vwm0lzzH6kdEQ.jpeg)
_Il y a des actes de Dieu, et puis il y a des actes humains._

Voici quelques moyens rapides et peu coûteux pour maximiser le temps de fonctionnement de votre site web en évitant les erreurs évitables :

* Écrivez des tests automatisés, et si possible, utilisez un outil d'intégration continue pour détecter les tests défaillants avant de déployer un nouveau code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tiANe5kbadVnyo0RM3pBfA.jpeg)
_Nous utilisons Travis CI intégré à GitHub pour nous assurer que tous nos tests passent avant d'accepter les pull requests._

* Créez un environnement de test local aussi proche que possible de votre site web de production (une façon de faire cela est d'[utiliser Docker](https://www.joyent.com/blog/spin-up-a-docker-dev-test-environment-in-60-minutes-or-less)).
* Créez un environnement de staging qui imite votre environnement de production, et faites en sorte que les membres de votre équipe testent les corrections et les fonctionnalités là-bas.
* Assurez-vous que vos environnements de test et de staging ne peuvent pas accéder à vos données de production (c'est ce qui a causé la grande panne de GitHub en 2010).
* Ne poussez pas de code en production tard dans la nuit. La plupart des temps d'arrêt non planifiés de Free Code Camp ont été causés par un mauvais jugement (généralement le mien) après des nuits blanches. Croyez-moi — aucune fonctionnalité ne vaut la peine de faire planter la production. En cas de doute, dormez là-dessus !

J'espère que cet article vous inspire à poursuivre le nombre de neuf qui vous convient.

Oh, et ne soyez pas trop dur avec vous-même si vous faites occasionnellement quelque chose de stupide et faites planter votre site web. Si cela peut arriver aux excellents ingénieurs de GitHub, cela peut arriver à n'importe qui.

**Je n'écris que sur la programmation et la technologie. Si vous [me suivez sur Twitter](https://twitter.com/ossia), je ne perdrai pas votre temps. ?**