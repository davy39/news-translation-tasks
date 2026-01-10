---
title: Comment enseigner la programmation aux adolescents
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-08T14:24:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-teach-programming-to-teenagers-2ecd43846f0d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FNZLxkvfXe2PAIlT8pbf3w.jpeg
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: teaching
  slug: teaching
- name: 'tech '
  slug: tech
seo_title: Comment enseigner la programmation aux adolescents
seo_desc: 'By Sean Choi

  In the past, many enthusiastic parents have approached me and asked me how I learned
  to code in the beginning — mainly with the interest in finding ways to help their
  children how to code. And every time, I didn’t have a clear answer for...'
---

Par Sean Choi

Dans le passé, de nombreux parents enthousiastes sont venus me voir et m'ont demandé comment j'avais appris à coder au début — principalement dans l'intérêt de trouver des moyens d'aider leurs enfants à apprendre à coder. Et à chaque fois, je n'avais pas de réponse claire pour eux, car j'ai appris à coder à un âge beaucoup plus avancé que la plupart des enfants de ces parents. Dans l'intérêt d'aider ces parents, j'ai également essayé de trouver des ressources conçues pour aider les enfants à apprendre à coder.

J'ai découvert qu'il existe de nombreuses ressources pour aider les élèves de la maternelle à la 6e année à apprendre à coder. Certains exemples incluent [Scratch](https://scratch.mit.edu/about) et l'Heure de Code sur [Code.org](https://code.org/) qui sont assez utiles pour quelqu'un de nouveau pour se familiariser avec la programmation.

À travers ces plateformes, les étudiants écrivent des programmes simples qui font bouger des créatures graphiques ou construisent des jeux simples et apprennent les outils de base de la programmation — tels que les boucles et les conditionnelles — tout en développant des compétences utiles en résolution de problèmes. La principale force de ces plateformes est le retour visuel de la plateforme, ce qui aide vraiment les étudiants à rester constamment engagés avec le programme et les exercices.

Cependant, enseigner la programmation aux adolescents après la 6e année est une toute autre histoire. [Cet article](https://www.geekwire.com/2018/new-research-finds-95-teens-access-smartphone-45-online-almost-constantly/) montre que plus de 95 % des adolescents aujourd'hui ont accès à des smartphones. Ainsi, le retour visuel de Scratch ou Code.org ne les impressionne plus. En fait, j'ai découvert que les adolescents les trouvent assez banals et enfantins.

Au lieu de cela, les adolescents veulent construire ou faire quelque chose de _RÉEL_ qu'ils peuvent montrer. Comme construire et lancer une vraie application iPhone ou leur propre site web ou pirater un système. Mais comment pouvez-vous amener quelqu'un qui vient de terminer une série d'exercices Scratch à construire une application iPhone, tout en les gardant constamment engagés pour la terminer ?

Je voulais donc partager mes expériences dans l'enseignement de la programmation à 4 adolescents sur une période de deux ans. Les étudiants avaient des niveaux de compétences en programmation, des personnalités et des attentes différents. Par conséquent, pour garder tout le monde engagé, j'ai dû passer par divers essais pour trouver les matériaux d'enseignement qui fonctionnaient pour tout le monde.

Le but principal de cet article est de partager ce que j'ai appris et les essais qui ont été réussis, dans l'espoir d'aider d'autres adolescents à aimer la programmation.

# Les adolescents ont des attentes élevées

J'ai appris que les adolescents absorbent les nouvelles technologies comme des éponges sèches. Alors que les adultes peuvent être tout à fait à l'aise avec le fait d'être un peu dépassés techniquement, les adolescents parient leur vie sur le fait d'être cool et de suivre la dernière tendance. J'ai constaté que les adolescents tendent à utiliser les applications les plus cool et les plus récentes même avant qu'elles ne fassent les gros titres de TechCrunch ou de CNBC.

En fait, ce sont mes étudiants qui m'ont présenté une série de [jeux .io](https://www.crazygames.com/c/io) et [HQ Trivia](https://en.wikipedia.org/wiki/HQ_Trivia). Il est donc important que ce qu'ils apprennent soit _COOL_, et quelque chose qu'ils peuvent partager avec leurs amis.

La première chose qu'ils ont demandée lorsque j'ai commencé le cours de programmation était « Peut-on pirater des trucs ? Comme des sites web et des applications iPhone ? ».

Je leur ai donc dit que nous devrions d'abord apprendre le HTML et le CSS pour apprendre à pirater un site web et je leur ai montré ceci :

```
<!DOCTYPE HTML>
<html>  
<head><title>Bonjour le monde !</title></head>  
<body><h1>Bonjour le monde !</h1></body>
</html>
```

J'ai expliqué ce que signifiaient chacune de ces balises et comment elles apparaîtraient sur une page. J'ai chargé une page avec ce `hello.html` et toutes leurs attentes de voir une page web cool se sont envolées. Ils étaient immédiatement ennuyés.

Cependant, j'ai continué le cours pour leur enseigner plus de HTML, CSS et JavaScript de base. J'ai pensé qu'en leur enseignant plus de HTML, CSS et JavaScript et en apprenant les techniques pour construire quelques exemples de sites web, ils se sentiraient plus engagés. Cependant, je me trompais.

Même après une série de constructions de sites web simples et leur déploiement sur [Firebase](https://firebase.google.com/), ils continuaient à dire qu'ils voulaient faire quelque chose de plus _RÉEL_ et quelque chose qu'ils pourraient montrer à leurs amis.

# Leur apprendre à faire quelque chose de RÉEL

J'ai réalisé qu'il existe de nombreuses façons de faire quelque chose de réel, et qu'il ne s'agissait pas du tout de créer des logiciels avec une interface graphique mignonne ou de leur enseigner de nouvelles structures de données, ou de prendre du matériel de Harvard CS50 et de le leur montrer.

J'ai décidé qu'il serait préférable d'utiliser du matériel et de faire en sorte que les étudiants ressentent physiquement ce qu'ils avaient codé. Mes deux choix étaient [Raspberry Pi](https://amzn.to/2PLBxk1) et [Arduino](https://amzn.to/2CK7eEc).

Raspberry Pi est un mini-ordinateur qui exécute sa propre version de Linux et est capable d'exécuter la plupart des langages de programmation. Vous pouvez acheter divers périphériques qui peuvent être contrôlés via votre propre logiciel personnalisé.

Arduino est plus impliqué. C'est une plateforme matérielle open-source, et de nombreuses entreprises construisent divers kits, tels que [Voiture Autonome Intelligente](https://amzn.to/2PJHWfu) et [Robot Quadrupède](https://amzn.to/2RQTaNu).

![Image](https://www.freecodecamp.org/news/content/images/2020/07/smart-car.jpeg)
_Voiture intelligente que nous avons construite en utilisant Arduino_

En utilisant Raspberry Pi, nous avons construit une [station météo](https://amzn.to/2pTtXoN) qui détecte la température et la pression de l'air de la zone environnante et les envoie à une base de données cloud. Ensuite, les étudiants ont pu consulter les données météo via un outil de graphique en ligne. Nous avons également programmé des fonctions utilitaires simples, telles que le changement d'unités de température et la recherche de la température minimale/maximale/moyenne, à publier dans la base de données. Ces exercices ont aidé les étudiants à apprendre des structures de données et des algorithmes simples, tels que les tableaux, les dictionnaires et le tri.

Après cela, nous sommes passés à la construction de la voiture autonome basée sur Arduino. Chaque étudiant avait un code exemple qui faisait bouger les voitures et détecter les obstacles. Ensuite, nous avons construit un labyrinthe et avons donné un prix à l'étudiant qui a fait sortir la voiture du labyrinthe en premier.

Les étudiants ont naturellement discuté entre eux de la logique qui aiderait la voiture à sortir du labyrinthe le plus efficacement. Et ils ont trouvé cela assez cool que leur algorithme soit immédiatement appris et exécuté par la voiture qu'ils avaient construite. Plus important encore, les étudiants ont vraiment apprécié, car c'était réel et tangible.

Nous avons également fait quelques exercices pour apprendre les bases du piratage ! Similaire à [LeetCode](https://leetcode.com/), qui vise à aider les participants à apprendre à résoudre des problèmes d'entretien, il existe de nombreux outils conçus pour aider les étudiants à apprendre les bases du piratage. Par exemple, [HackThis](https://www.hackthis.co.uk/) est un site web sympa qui vous donne une série de défis que vous pouvez consulter et résoudre sur votre navigateur. Il vous demande d'utiliser de nombreux outils de navigateur existants, tels que les outils de développement Chrome, pour trouver des déficiences que vous pouvez exploiter pour accéder au système.

Les étudiants ont vraiment aimé cet exercice, car résoudre ces exercices leur donnait l'impression d'être des espions dans Mission Impossible. Après avoir terminé le défi, ils sont allés sur de vrais sites web (je me suis assuré qu'ils ne faisaient rien d'illégal...) et ont essayé de trouver des failles qu'ils pourraient utiliser.

Une fois qu'ils seront plus préparés et qu'ils auront appris les concepts de base de Linux, je prévois de leur enseigner des concepts de piratage plus avancés avec [Kali](https://www.kali.org/) Linux, ce que je pense sera encore plus excitant.

# La compétition comme outil d'apprentissage

![Image](https://www.freecodecamp.org/news/content/images/2020/07/clash-of-code.png)
_Clash of Code pour commencer la journée_

Enfin, la dernière chose que j'ai apprise est que les adolescents sont assez compétitifs. Ils aiment les exercices qui leur donnent un retour immédiat, comme leur donner un score, un badge, ou les placer sur un vrai tableau de scores.

La meilleure plateforme que j'ai trouvée et qui a motivé les étudiants était [CodingGame](https://www.codingame.com/start). Ils résolvaient chaque exercice de programmation et montaient de niveau dans le processus. Les exercices ont également quelques composants visuels sympas, permettant aux étudiants d'être assez engagés dans les exercices.

Nous commencions également la journée en faisant une session de [Clash of Code](https://www.codingame.com/multiplayer/clashofcode), qui est un défi de programmation en direct de 5 minutes entre d'autres utilisateurs en ligne, et les étudiants gagnait parfois contre d'autres joueurs qui avaient des niveaux plus élevés qu'eux ! Cela les motivait vraiment pour commencer une autre journée d'apprentissage de la programmation.

# Réflexions finales

Enseigner la programmation est amusant et éducatif. Non seulement vous apprenez à enseigner à une autre personne, mais cela vous donne également l'occasion de vous mettre à la place des étudiants. Vous apprenez à comprendre comment les autres pensent à un problème et réalisez qu'il existe de nombreuses façons différentes de percevoir le même problème. Vous apprenez également à décrire les problèmes de manière à ce que les étudiants aiment y réfléchir. De plus, personnellement, je pense que l'enseignement vous aide à devenir une personne plus compréhensive et patiente.

J'espère que vous pourrez également me faire savoir comment vous avez aidé les autres à rejoindre le monde de la programmation. Pour ceux d'entre vous qui commencent le voyage d'aider les autres à apprendre à programmer, j'espère vraiment que cet article a donné quelques points à retenir pour votre propre programme.

Merci d'avoir lu !