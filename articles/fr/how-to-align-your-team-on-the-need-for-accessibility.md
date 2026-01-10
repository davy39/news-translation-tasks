---
title: Comment faire adhérer votre équipe à l'accessibilité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-13T21:40:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-align-your-team-on-the-need-for-accessibility
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/keyboard-1.jpg
tags:
- name: a11y
  slug: a11y
- name: Accessibility
  slug: accessibility
- name: presentation
  slug: presentation
- name: progressive web app
  slug: progressive-web-app
- name: teamwork
  slug: teamwork
seo_title: Comment faire adhérer votre équipe à l'accessibilité
seo_desc: 'By James Y Rauhut

  We all learn about web accessibility at different points in our career. That means
  a lot of time you are not on the same page as your teammates. I had the privilege
  a couple of months ago to speak at Pingboard about accessibility. O...'
---

Par James Y Rauhut

Nous apprenons tous l'accessibilité web à différents moments de notre carrière. Cela signifie que vous n'êtes souvent pas sur la même longueur d'onde que vos coéquipiers. J'ai eu le privilège, il y a quelques mois, de parler de l'accessibilité chez [Pingboard](http://pingboard.com/). Notre objectif était d'amener toute l'équipe au même niveau de connaissances de base. Si nous avons tous une compréhension de base de qui est affecté par l'accessibilité web et de la manière dont cela les affecte, nous pouvons offrir de meilleures expériences.

Vous vous trouvez probablement dans la même situation au sein de votre entreprise, avec l'opportunité de présenter l'accessibilité. Je souhaite donc faire deux choses pour vous aider : je vais [vous donner ma présentation](https://drive.google.com/file/d/1W62aya8uk0LgMPyMUBSIAJVOQBewmiKd/view?usp=sharing) comme point de départ et vous guider à travers les points que j'aime aborder.

> Vous vous trouvez probablement dans la même situation au sein de votre entreprise, avec l'opportunité de présenter l'accessibilité. 20	8 Je vais [vous donner ma présentation](https://drive.google.com/file/d/1W62aya8uk0LgMPyMUBSIAJVOQBewmiKd/view?usp=sharing) comme point de départ et vous guider à travers les points que j'aime aborder.

# **Rappeler à l'équipe que vous parlez de vraies personnes.**

Lorsque nous lisons la documentation sur l'accessibilité, il est facile d'oublier l'élément humain. Cela se comprend car vous lisez des documents techniques destinés à influencer le code. Il est bon de commencer par cette définition partagée :

**_Une personne handicapée :_** _Une personne qui a une déficience physique ou mentale qui limite substantiellement une ou plusieurs activités majeures de la vie._

Nous utilisons cette définition pour établir un dialogue bienveillant. Les personnes ne veulent pas être appelées « handicapées ». Elles veulent qu'on les appelle par leur nom. Nous devons également clarifier à quel point la gamme des handicaps peut être large. Essayez d'élargir les hypothèses dès le début avec ces points :

* Certains handicaps sont présents dès la naissance, d'autres apparaissent plus tard.
* Certains handicaps sont permanents, d'autres sont temporaires.
* Certains handicaps affectent toujours, d'autres vont et viennent.
* Certains handicaps sont visibles, d'autres sont invisibles.

# **Passer en revue certaines catégories de handicaps avec des expériences émotionnelles et des conseils rapides.**

Maintenant que nous avons établi que nous parlons de personnes, il est temps de parler de leurs expériences. J'aime mélanger cette section avec des conseils rapides pour les catégories de handicaps courantes. Rappeler à votre audience qu'il existe bien plus de handicaps que ceux que vous couvrez. Ils sont difficiles à catégoriser, c'est pourquoi la documentation technique se concentre sur les solutions.

Une chose que vous remarquerez à propos de la présentation est qu'il y a beaucoup de vidéos et d'audios. Je trouve plus efficace de laisser ceux qui ont des handicaps parler davantage que moi de ce sujet. Le multimédia dans la présentation permet à ces personnes de ne même pas avoir à être présentes.

### Visuel

%[https://www.youtube.com/watch?v=UzffnbBex6c]

J'aime partager cette vidéo de Tommy Edison utilisant un lecteur d'écran car il garde les choses légères, mais il passe également par le processus complet d'envoi d'un email. Après la vidéo, vous pouvez souligner que les utilisateurs de Mac peuvent essayer leur lecteur d'écran avec `CMD + F5` à tout moment.

Conseils rapides :

* Les personnes atteintes de dyslexie préfèrent remplacer les paramètres de police.
* Les personnes malvoyantes doivent pouvoir zoomer correctement.
* Les personnes daltoniennes ont besoin d'un rapport de contraste des couleurs global de 4,5:1. Le texte de 19 px ou plus peut avoir un rapport de 3:1.
* Les personnes daltoniennes ont besoin d'étiquettes et de motifs pour les différenciations.

### Auditif et Épilepsie

Les handicaps auditifs sont plus faciles à aborder avec les équipes de produits numériques. Rappelez à votre équipe que tout l'audio doit être associé à des indices visuels et à des sous-titres. Encouragez l'équipe à effectuer des audits de contenu pour vérifier que toutes les vidéos ont des sous-titres.

Les effets stroboscopiques, les scintillements et les flashs peuvent déclencher des crises d'épilepsie. D'autres déclencheurs incluent les animations de plus de 250 ms, le parallaxe et les images se déplaçant sous le texte.

### Moteur

%[https://youtu.be/yx7hdQqf8lE?t=253]

Il y a deux démonstrations que j'aime montrer à mes coéquipiers en ce qui concerne les handicaps moteurs. La première est cachée dans une vidéo plus longue. Un homme nommé Gordin Richins montre à quoi ressemble l'utilisation d'un bâton buccal. C'est une vieille vidéo, mais j'essaie de souligner que les nouvelles technologies peuvent être plus coûteuses.

La deuxième vidéo est une vidéo chaleureuse d'un produit de suivi oculaire. Ceux-ci sont géniaux car ils peuvent fournir des capacités de souris à ceux qui ont des handicaps moteurs. Cependant, nous devrions toujours rendre toutes les expériences accessibles par clavier pour être sûrs.

%[https://www.youtube.com/watch?v=FEQv7buTNxw]

### Cognitif

Les handicaps cognitifs peuvent être difficiles à transmettre. Pour cette dernière catégorie, je me suis en tenu à des conseils rapides pour garder la présentation alternative entre faits et émotion. Voici les conseils rapides que je partage :

* Pour la mémoire, gardez les processus courts et rappelez aux utilisateurs le contexte autant que possible.
* Pour la résolution de problèmes, les messages d'erreur doivent être aussi explicatifs que possible.
* Pour l'attention, utilisez des indices visuels pour mettre en évidence les points ou sections de contenu les plus importants.
* Pour la lecture, la compréhension linguistique et verbale, fournissez des médias supplémentaires qui aident les processus.

# **Souligner à quel point les handicaps sont en réalité courants.**

Saviez-vous qu'une personne sur cinq aux États-Unis a au moins un handicap ? ([source](https://www.census.gov/newsroom/releases/archives/miscellaneous/cb12-134.html)) Cela peut ne pas sembler être le cas sur le lieu de travail, mais nous devrions nous demander pourquoi. C'est le moment de la présentation où les gens devraient comprendre les handicaps invisibles. Les handicaps invisibles peuvent être cachés à l'œil nu. Voici une excellente interview où Carly Medosch parle de travailler avec un handicap invisible :

[**NPR : Les personnes atteintes de "handicaps invisibles" se battent pour la compréhension**](https://www.npr.org/2015/03/08/391517412/people-with-invisible-disabilities-fight-for-understanding)

Cette histoire est une excellente transition vers une grande question : Que pouvons-nous faire, en tant qu'équipes de logiciels d'entreprise, pour aider les personnes handicapées ?

Eh bien, 79 % des personnes en âge de travailler aux États-Unis ont un emploi. Seules 41 % des personnes en âge de travailler aux États-Unis qui ont des handicaps ont un emploi. ([source](https://www.census.gov/newsroom/releases/archives/miscellaneous/cb12-134.html)) Si plus d'emplois étaient accessibles, cet écart se réduirait. Cela signifie que nous, en tant qu'équipes de logiciels d'entreprise, pouvons faire de notre mission de réduire cet écart !

# **Terminer avec le risque juridique pour ceux qui ont besoin de motivation extrinsèque.**

Cela peut ne pas sembler génial, mais certaines personnes peuvent encore avoir besoin de plus de raisons pour lesquelles l'équipe devrait travailler vers des expériences accessibles. C'est pourquoi j'aime terminer la présentation sur les implications juridiques de l'accessibilité.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-13-at-3.45.32-PM.png)
_Plaintes ADA Titre 3 devant les tribunaux fédéraux : 2722 en 2013, 4436 en 2014, 4789 en 2015, 6601 en 2016, 7663 en 2017, 10163 en 2018. https://www.adatitleiii.com/2019/01/number-of-ada-title-iii-lawsuits-filed-in-2018-tops-10000/_

En 1990, la loi sur les Américains handicapés a été signée. Cela offre à ceux qui ont des handicaps la même protection que celle donnée dans la loi sur les droits civiques de 1964. La section 508 stipule que les expériences numériques dans les départements et agences gouvernementaux ont des exigences d'accessibilité.

Les poursuites judiciaires continuent de croître, affirmant que l'ADA couvre également les expériences numériques de toute entreprise. Plus de 10 000 poursuites ont été déposées en 2018 seulement. En fait, l'une de ces [affaires se dirige vers la Cour suprême](https://www.cnbc.com/2019/07/25/dominos-asks-supreme-court-to-say-disability-protections-dont-apply-online.html).

# Faites partie du bon combat.

Envisagez-vous de présenter à votre équipe l'accessibilité web ? Vous devriez vraiment. Vous n'avez pas besoin d'être un expert et ce n'est pas grave si tout le monde ne vous écoute pas. Chaque effort pour rendre le web plus accueillant en vaut la peine.

J'espère que ces ressources vous ont aidé à façonner une future présentation. N'hésitez pas à tout prendre de moi (mais gardez les citations).

Si vous appréciez cela, envisagez de voter pour mon idée de conférence SXSW. Je veux enseigner aux chefs de produit, aux designers et à tout le monde d'autre sur les applications web progressives. Le truc cool avec les PWAs, c'est que beaucoup de critères d'accessibilité sont intégrés ! Si vous voulez en savoir plus, regardez la vidéo ci-dessous.

[Veuillez prendre une minute pour voter pour ma conférence et la partager avec d'autres.](https://panelpicker.sxsw.com/vote/95517)

%[https://www.youtube.com/watch?v=aRwfB7Iiaqo]

Avez-vous d'autres bonnes ressources pour les présentations sur l'accessibilité ? N'hésitez pas à les partager dans les commentaires ou à me les tweeter à [@seejamescode](http://twitter.com/seejamescode). Je retweeterai les meilleures !