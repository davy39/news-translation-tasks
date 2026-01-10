---
title: Comment j'ai aidé mon partenaire à apprendre à coder
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-22T01:35:08.000Z'
originalURL: https://freecodecamp.org/news/how-i-helped-my-partner-learn-to-code-6e1d1953812f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Pk2JHq0PUJJMRKWbtEvbDQ.jpeg
tags:
- name: careers
  slug: careers
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment j'ai aidé mon partenaire à apprendre à coder
seo_desc: 'By Carl Tashian

  When my partner Siobhán decided she wanted to make a career change into data science
  last spring, I knew it would be a chance for me to see first-hand how someone learns
  to code today.

  I’ve been programming since I was a kid, and in m...'
---

Par Carl Tashian

Lorsque mon partenaire [Siobhán](https://www.freecodecamp.org/news/how-i-helped-my-partner-learn-to-code-6e1d1953812f/undefined) a décidé qu'elle voulait faire un changement de carrière dans la science des données au printemps dernier, j'ai su que ce serait l'occasion pour moi de voir de première main comment quelqu'un apprend à coder aujourd'hui.

Je programme [depuis que je suis enfant](https://medium.freecodecamp.com/how-i-learned-to-program-f196a5a8bfd3#.su3vk8dpf), et dans mon rôle de développeur et de gestionnaire d'ingénierie, j'ai toujours travaillé avec des personnes qui codent depuis au moins un an. Mais commencer depuis le début ? Où est le début, d'ailleurs ?

Pour Siobhán, le point de départ était le [Nanodiplôme d'analyste de données](https://www.udacity.com/course/data-analyst-nanodegree--nd002) chez Udacity, qu'elle a commencé l'été dernier et terminé en février. Ce programme exige que vous ayez suivi un cours d'introduction en informatique, mais lorsqu'elle l'a commencé l'été dernier, elle n'avait jamais fait de programmation auparavant. Ainsi, au début, mon rôle en tant que son coach était de fournir du matériel provenant d'autres sources (comme l'excellent [cours CS50](https://cs50.harvard.edu/) de Harvard) pour compléter ce qu'elle apprenait d'Udacity.

Elle avait beaucoup de questions, allant des aspects pratiques de l'utilisation de l'éditeur de texte et de la ligne de commande, à des questions conceptuelles qui défiaient son modèle de fonctionnement des ordinateurs. Une bonne question qu'elle a posée tôt était : « Pourquoi dois-je utiliser Chrome pour accéder à Jupyter, alors qu'il est déjà sur mon ordinateur ? Chrome n'est-il pas seulement pour se connecter à des sites web ? » Ce qui a conduit à une excellente discussion sur l'architecture client/serveur, TCP/IP, HTTP et le réseau de bouclage localhost.

Siobhán travaille super dur, se levant à 6h la plupart des jours et étudiant jusqu'à tard. L'un des grands défis est de l'aider à rester dans la zone de flux sans être submergée par la quantité de matériel qu'elle apprend. Voici comment nous avons abordé cela :

![Image](https://cdn-media-1.freecodecamp.org/images/ziqTqESg5FSjepmcKtwqd34hZ4fXwhfAZkRj)

Être submergé de temps en temps semble être la seule façon de nous assurer qu'elle maximise le flux. Mais évidemment, nous ne voulons pas rester là longtemps. Cet état d'anxiété, lorsque vous avez quelque chose de beaucoup trop difficile entre les mains, est très inconfortable et peut épuiser votre confiance et votre enthousiasme globaux. Ainsi, chaque fois que nous atteignons ce point, nous faisons un pas en arrière et réévaluons.

À un moment donné l'automne dernier, elle a fait une liste de ce qui était couvert par le programme Udacity, et cela ressemblait à quelque chose comme :

* Python / Jupyter
* R / R Studio
* vim
* git / GitHub
* la ligne de commande
* statistiques
* apprentissage automatique
* matplotlib / pandas / NumPy / SciPi
* JavaScript / D3
* principes de base de l'informatique et algorithmes
* nettoyage de données / JSON / XML / etc.
* SQL / PostgreSQL
* NoSQL / MongoDB

Le programme d'Udacity était un excellent cours d'enquête sur tous ces mondes, mais il couvrait beaucoup de matériel et il y avait un changement de contexte vertigineux chaque fois que Siobhán terminait un projet. Par exemple, après quelques semaines d'apprentissage de JavaScript et D3 et de construction d'une visualisation, elle devait passer au monde très différent de R et RStudio, laissant JavaScript et toute sa syntaxe complètement derrière elle.

Dans le programme Udacity, elle a construit une douzaine de projets de classe et a appris énormément. Mais lorsqu'elle a terminé le programme en février, sa confiance a chuté. Il y avait des moments où elle sentait qu'elle n'avait rien appris parce qu'elle avait eu une expérience si fugace avec chaque langage ou ensemble d'outils.

Elle a donc décidé de faire quelques semaines de pratique simple. L'objectif de la période de pratique est de s'habituer à livrer des projets complets en utilisant uniquement Python, SQL et des bibliothèques d'analyse de données, tout en continuant à construire des connaissances de base en informatique et en statistiques. Avec chaque semaine de cela, sa confiance s'est considérablement améliorée. Elle a vu tout ce qu'elle sait déjà, et elle est capable de se concentrer sur les domaines où elle veut combler sa compréhension et sa fluidité. En revenant à son bureau chaque jour pour travailler sur Python à temps plein, elle devient rapidement une pro.

Nous terminons la période de pratique à la mi-avril, juste au moment où sa recherche d'emploi s'intensifie. Voici quelques choses que j'ai apprises jusqu'à présent en tant que son coach :

#### Exprimer un algorithme comme une idée

Un algorithme peut être le plus facilement exprimé comme une idée. Si vous avez du mal à résoudre un défi de codage, parlez-en d'abord dans votre langue maternelle, pas en pseudocode. Il y a généralement plusieurs façons de pseudocoder une solution (itérative, récursive, OO, fonctionnelle, procédurale), mais il y a beaucoup moins d'approches de base pour développer une solution.

Imaginons que vous essayez de trouver la plus longue sous-chaîne palindromique d'une chaîne donnée. Par exemple, si la chaîne est `aabbdcaacd`, la plus longue sous-chaîne palindromique est `dcaacd`.

Voici comment nous pourrions aborder le problème, en anglais :

* Essayons de trouver des palindromes ! Parce qu'ils sont symétriques, nous pouvons commencer par chercher les centres, ou « graines » de palindromes dans une chaîne.
* Lorsque nous trouvons une graine, nous pouvons essayer de l'étendre vers l'extérieur jusqu'à ce que les côtés gauche et droit ne soient plus égaux.
* Un peu de manipulation révélera qu'il y a des graines de deux et trois caractères. Par exemple, `aa` et `aba` sont des graines.
* Les palindromes peuvent se chevaucher. Si la chaîne est `rrgrrgra`, nous ne voulons pas ignorer `rgrrgr` simplement parce que nous avons trouvé le chevauchement `rrgrr` au début de notre recherche.

Une fois que vous avez énoncé l'idée en langage clair sur ce que vous allez faire, passer au pseudocode (et à la solution) devient beaucoup plus facile. Ce processus vous donne également un meilleur langage que vous pouvez utiliser lorsque vous commencez à nommer les choses dans votre programme.

#### Apprendre à regarder le code

Apprendre à coder n'est pas seulement écrire du code, c'est aussi apprendre à scanner un programme pour sa structure globale, sa fonctionnalité et pour les drapeaux rouges. Ce n'est pas tant de la lecture, comme nous le faisons en anglais. C'est regarder.

Au début, vous essayez simplement de pouvoir comprendre toute la syntaxe tout en construisant un modèle du programme dans votre tête. Une fois que la syntaxe devient plus facile à regarder, vous commencerez à remarquer les erreurs de syntaxe plus tôt. Finalement, quelque chose aura simplement l'air « bizarre » dans le code lorsque vous le regarderez. Les parenthèses ou les guillemets manquants se démarqueront visuellement. (La façon dont votre éditeur de texte traite la coloration syntaxique devient significative à ce stade.)

![Image](https://cdn-media-1.freecodecamp.org/images/Iyfj-KTmoXPmcm-R5-cUldUYBrpW0OyWgTIu)
_[Conférence RailsConf 2014](undefined" rel="noopener" target="_blank" title="">Sandi Metz</a>squint test, couvert dans sa <a href="http://confreaks.tv/videos/railsconf2014-all-the-little-things" rel="noopener" target="_blank" title=")_

La gourou de la conception orientée objet Sandi Metz parle du « squint test » qu'elle utilise parfois pour regarder le code : plissez les yeux en regardant le code, en observant la forme de l'indentation et la couleur. Si la forme ressemble à un ensemble d'escaliers en zigzag ou si les couleurs sont un patchwork, cela pourrait être un bon candidat pour un refactoring.

#### Commencez par maîtriser le programme de 50 lignes...

Je pense qu'il y a un plateau initial que vous devriez atteindre lorsque vous apprenez à coder : le programme procédural de 50 lignes. Pendant cette période, lorsque vous apprenez les blocs de construction des types de données, des boucles et des conditionnelles, il est logique de garder vos programmes courts.

Si vous devenez un maître de ces petits programmes, vous aurez une excellente fondation sur laquelle construire. La solution à tout défi de codage sur [Leetcode](https://leetcode.com/) ou Cracking the Coding Interview peut être écrite comme un petit programme, donc ce sont de grandes pratiques.

Et dans un petit programme de 20 à 50 lignes, il peut être totalement acceptable d'utiliser plusieurs variables globales ou de ne pas écrire de tests. Mais finalement, vous voudrez atteindre le deuxième plateau...

#### ...puis apprenez à garder les programmes plus grands simples

Une fois que vous avez maîtrisé la programmation procédurale simple, vous pouvez théoriquement écrire n'importe quel programme. Vous pouvez même commencer à croire que la programmation est facile.

Mais à mesure que vos programmes grandissent, les normes augmentent. Vous devrez développer plus de façons de gérer la complexité, et il y a une deuxième colline raide à gravir. Vous voulez garder vos programmes simples, alors vous apprenez les subtilités de l'abstraction et de l'encapsulation qui gardent le code simple. Vous apprenez à penser plus sérieusement aux tests et à la façon dont vous nommez les choses.

Vous saurez que vous êtes en route vers le deuxième plateau lorsque votre arrogance initiale d'avoir atteint le premier plateau sera remplacée par la prise de conscience humble que, bien que la programmation soit simple, elle n'est pas toujours facile.

> « La simplicité est une condition préalable à la fiabilité. » — Edsger W. Dijkstra

#### Prenez l'habitude d'écrire des tests

Écrire de bons tests est une compétence en soi, mais il est facile de commencer. Le développement piloté par les tests vous aidera à construire la discipline des bons tests, car il encourage une couverture de test très élevée. Et c'est addictif.

Une approche consiste à commencer à écrire des tests et du code pour couvrir les cas de base évidents, puis à essayer de casser le programme en fournissant des cas limites. Pour atteindre un cas limite, changez l'un des paramètres de votre programme ou fonction en une valeur extrême. Parfois, une « valeur extrême » est simplement une valeur de limite comme `0` ou `1` ou une chaîne vide. Testez autour de cette valeur pour être sûr que votre programme fait la bonne chose dans chaque cas.

Parfois, la réponse avec des entrées extrêmes à une fonction est de lever une exception, et souvent cela n'implique pas d'écrire des lignes de code supplémentaires.

#### Prenez des notes pendant que vous travaillez

Chaque développeur devrait avoir un petit bloc-notes à côté de lui (physiquement ou virtuellement) pour les notes et les questions. Lorsque vous travaillez, beaucoup de choses peuvent survenir que vous ne voulez peut-être pas traiter tout de suite. Voici quelques notes d'hier :

* Le code Python est toujours brouillé lorsque je le colle dans vim ! Beurk.
* Pourquoi écrivons-nous toujours `if __name__ == '__main__':` ? Que signifie cela ?
* Pourquoi ma suite `unittest` doit-elle toujours être définie comme une classe ?

En cas de doute, notez-le simplement et voyez si c'est quelque chose que vous voulez suivre plus tard.

La chose la plus importante que Siobhán fait en ce moment est de coder tous les jours. Nous avons encore quelques semaines avant qu'elle ne soit en mode recherche d'emploi à temps plein, mais la pratique sera une chose continue. Chaque jour, elle renforce des concepts et construit sa compréhension. C'est gratifiant à regarder, et cela m'a aidé à raviver mon excitation pour le plaisir que peut être la programmation.

#### Si vous êtes arrivé jusqu'ici, vous devriez [rejoindre ma liste de diffusion](http://tashian.com/superstack) et je vous enverrai des emails comme si c'était 1995 (max 2 par mois)