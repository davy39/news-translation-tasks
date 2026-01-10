---
title: 'Comment j''ai construit mon projet solo : Un moteur d''échecs pour un moteur
  de développement de jeux populaire'
subtitle: ''
author: Lynn Zheng
co_authors: []
series: null
date: '2020-09-08T23:23:46.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-my-one-person-open-source-project
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98ca740569d1a4ca1c15.jpg
tags:
- name: open source
  slug: open-source
- name: projects
  slug: projects
- name: side project
  slug: side-project
seo_title: 'Comment j''ai construit mon projet solo : Un moteur d''échecs pour un
  moteur de développement de jeux populaire'
seo_desc: 'I recently finished one of my summer projects: a chess GUI engine built
  using the Ren’Py Visual Novel Game Development Engine and the python-chess library.

  This engine will be integrated into a kinetic novel game, The Wind at Dawn, at that
  game’s com...'
---

J'ai récemment terminé l'un de mes projets d'été : [un moteur d'interface graphique pour les échecs](https://github.com/RuolinZheng08/renpy-chess) construit en utilisant le [Ren'Py Visual Novel Game Development Engine](http://renpy.org/) et la bibliothèque [python-chess](https://github.com/niklasf/python-chess).

Ce moteur sera intégré dans un jeu de roman cinétique, [*The Wind at Dawn*](https://madeleine-chai.itch.io/the-wind-at-dawn), à la fin de ce jeu.

Dans cet article, je souhaite partager quelques apprentissages clés, techniques et non techniques, que j'ai recueillis en menant ce projet solo du début à la fin en un mois.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/foolsmate.gif align="left")

\_[Mon Projet de Moteur d'Échecs sur GitHub\](https://github.com/RuolinZheng08/renpy-chess" data-href="https://github.com/RuolinZheng08/renpy-chess" class="markup--anchor markup--figure-anchor" rel="noopener" target="*blank)*

## Apprécier la valeur de la réécriture de l'ancien code

Pour les projets d'informatique à l'école, je n'ai rarement l'opportunité ou le besoin de revisiter mon code.

Cependant, ce n'est pas le cas lorsque je travaille sur mes projets passion : j'aime saisir chaque opportunité pour améliorer leur utilité et leur réutilisabilité dans l'espoir que mon code sera utile à d'autres développeurs.

Ce moteur d'échecs est basé sur [un moteur d'échecs que j'ai créé en Ren'Py et en Python vanilla](https://github.com/RuolinZheng08/renpy-chess-engine) tout en apprenant Python pendant ma première pause estivale à l'université.

Ce vieux moteur d'échecs est, à son tour, basé sur un projet de mon cours d'introduction à l'informatique à l'université (un jeu d'échecs avec interface graphique écrit en Racket, un langage de programmation fonctionnelle). Cela signifie que j'ai réécrit mon code deux fois pour produire ce moteur d'échecs final.

Pour ma première réécriture, j'ai simplement « traduit » la logique des échecs (pour déterminer si un mouvement est légal, les conditions de fin de jeu, etc.) de Racket à Python. J'ai également expérimenté la programmation orientée objet, écrit une IA d'échecs minimax en suivant des tutoriels en ligne, et implémenté l'interface graphique en Ren'Py.

Puisque je ne connaissais que les bases des échecs et que j'ai écrit ma logique d'échecs selon les spécifications de notation de mon projet scolaire, mon premier moteur d'échecs ne supportait pas les mouvements spéciaux comme l'en passant, le roque ou la promotion.

Pour résoudre ce problème dans ma deuxième réécriture, j'ai recherché des bibliothèques Python open-source et j'ai trouvé [python-chess](https://github.com/niklasf/python-chess), une bibliothèque avec un support complet pour les mouvements d'échecs et les conditions de fin de jeu comme la revendication d'un match nul lorsque la répétition triple se produit.

En plus de cela, elle a également intégré [Stockfish](https://stockfishchess.org/), une IA d'échecs, et cette intégration permettra à mon moteur d'échecs de configurer la force de l'IA d'échecs.

Ces deux fonctionnalités ont ajouté une grande valeur à ma version 2.0 du moteur d'échecs et m'ont permis de me concentrer sur les aspects plus importants de ma réécriture, que je vais décrire ci-dessous.

## Lire la documentation et garder la compatibilité à l'esprit

Il est devenu une habitude pour moi de parcourir la documentation des bibliothèques dont j'ai besoin pour mon projet avant de me lancer dans la conception et le code. Cela m'aide à évaluer tout problème de dépendance et de compatibilité qui pourrait survenir.

[Ce problème GitHub de Ren'Py](https://github.com/renpy/renpy/issues/2003) indique que Ren'Py utilise Python 2 et n'a pas encore été porté vers Python 3. J'ai donc reconnu que j'avais besoin d'une version de python-chess qui supporte Python 2, [car la dernière version ne supporte que Python 3.7+](https://python-chess.readthedocs.io/en/latest/#features).

Heureusement, [la version 0.23.10](https://python-chess.readthedocs.io/en/v0.23.10/index.html#features) supporte à la fois Python 2.7 et Python 3.4+. J'ai finalement opté pour la version 0.23.11 car c'est la dernière version qui supporte encore Python 2.7.

Ayant résolu les problèmes de dépendance et de compatibilité, j'étais prêt à passer à la conception et au codage.

## Suivre les meilleures pratiques de l'ingénierie logicielle

Note : Beaucoup de termes mentionnés dans cette section proviennent de [Agile/Scrum](https://en.wikipedia.org/wiki/Scrum_%28software_development%29).

### Recueillir les exigences des fonctionnalités pour la conception du projet

Bien qu'il soit tentant de se lancer directement dans le codage, je ne peux pas assez insister sur l'importance de la conception.

Pensez à la conception comme une feuille de route de haut niveau qui délimite clairement le point de départ, les étapes et les points de fin du projet. Cela permet aux développeurs de s'y référer lorsqu'ils sont plongés dans les détails complexes de l'implémentation.

Cela est particulièrement important pour les projets extracurriculaires car ils n'ont généralement pas de spécifications détaillées et hautement techniques, contrairement à la plupart des projets scolaires.

Pour mon moteur d'échecs, j'ai identifié les réécritures/fonctionnalités supplémentaires suivantes :

* Intégrer la logique des échecs de python-chess

* Dans mon code d'interface graphique Ren'Py, remplacer la logique des échecs et l'IA d'échecs que j'ai écrite par la logique des échecs et les API Stockfish de python-chess

* Supporter divers modes de jeu : Joueur contre Joueur, Joueur contre Ordinateur (où le Joueur peut choisir de jouer en noir ou en blanc), force ajustable de l'IA d'échecs via les paramètres de configuration de Stockfish

* Développer une interface graphique Ren'Py pour la promotion du pion

* Développer une interface graphique Ren'Py pour revendiquer un match nul en cas de répétition triple ou de la règle des cinquante coups

### Développer un prototype de preuve de concept

Un prototype de preuve de concept (POC) m'aide à évaluer le temps et l'effort nécessaires pour implémenter les fonctionnalités requises.

Pour le POC de mon moteur d'échecs, j'ai intégré python-chess avec mon code d'interface graphique Ren'Py original. J'ai veillé à ce que son ensemble de fonctionnalités soit minimal mais facilement extensible :

* J'ai intégré python-chess avec mon code d'interface graphique Ren'Py original et j'ai pu déplacer les pièces

* J'ai seulement implémenté Joueur contre Joueur afin de reporter l'intégration de Stockfish pour l'IA d'échecs

* J'ai seulement autorisé les mouvements sans promotion afin de reporter le développement de l'interface graphique pour la promotion du pion

### Identifier la définition de prêt et la définition de terminé du projet

La définition de prêt (DoR) de mon projet découle naturellement de mon investigation initiale sur la compatibilité des versions de la bibliothèque et de mon POC.

En parallèle, la définition de terminé (DoD) de mon projet découle des exigences de fonctionnalités que j'ai identifiées lors de ma phase de conception.

### Livrer un produit minimum viable, ou mieux encore, un produit minimum aimable

![Image](https://www.freecodecamp.org/news/content/images/2020/09/promotion.gif align="left")

*Interface utilisateur de promotion*

Lorsque j'étais en phase de conception pour recueillir les exigences, je savais qu'il y avait beaucoup d'objectifs étendus pour mon projet — peut-être même plus que je ne pourrais jamais accomplir.

Il était donc important pour moi d'implémenter l'ensemble de base des fonctionnalités requises, de livrer un produit minimum viable (MVP), et de recueillir des commentaires pour itérer dessus.

Mieux encore, j'aimerais livrer un produit minimum aimable (MLP) lors de ma première itération. La minuscule différence est que, tandis qu'un MVP ne nécessite rien de plus que des fonctionnalités opérationnelles, un MLP a une expérience utilisateur aimable par conception.

Par exemple, pour implémenter les mouvements de promotion de pion, pour un MVP, je pourrais demander aux utilisateurs d'appuyer sur différentes touches pour sélectionner le type de pièce auquel ils veulent promouvoir (comme B pour fou et K pour chevalier).

Pour un MLP, je devrais implémenter une interface utilisateur avec des boutons en forme de type de pièce qui changent de couleur lorsqu'ils sont survolés ou sélectionnés.

## Être son propre chef de projet

Si vous trouvez que le suivi de la liste des fonctionnalités (plus la liste toujours croissante des bugs et des correctifs) est accablant, vous n'êtes pas seul. Il est temps d'être votre propre chef de projet.

J'ai trouvé que [Trello](https://trello.com/) est un outil incroyable à la fois pour les projets solo et les projets d'équipe.

Voici comment j'organise généralement mon tableau Trello pour un projet de codage :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/board.png align="left")

*Le tableau Trello pour mon projet de moteur d'échecs*

Avoir quatre listes : **Backlog** (pour les fonctionnalités à trier), **TODO**, **Doing**, et **Done**.

Avoir des étiquettes codées par couleur :

* **Prêt pour QA** : une étiquette rouge pour attirer l'attention de mes coéquipiers

* **Impact** : faible (jaune) vs. élevé (orange), déterminé par la quantité d'impact qu'une fonctionnalité ou une correction de bug générera. Par exemple, un panneau d'interface utilisateur légèrement désaligné a un impact faible où un bug provoquant un crash de manière déterministe a un impact élevé.

* **Une estimation du temps qu'il faudra pour implémenter** : trivial (< 1 heure, bleu sarcelle), moyen (1-2 heures, bleu clair), et difficile (2-4 heures, bleu foncé).
  Ma autre règle de base est, si j'estime qu'une carte prendra plus de 4 heures à implémenter, je devrais probablement la décomposer en plusieurs cartes plus fines.

* La couleur sert de grande indication visuelle : je m'attaque toujours aux cartes avec des étiquettes orange et bleu sarcelle (impact élevé et faible engagement de temps) avant de m'attaquer à celles avec des étiquettes jaune et difficile (impact faible mais engagement de temps élevé).

## Écrire de la documentation et réfléchir à son apprentissage

Ayant poussé chaque carte Trello de TODO à Doing à Done et corrigé chaque bug désagréable, est-il enfin temps d'appeler un projet terminé ? Oui et non.

Pour maximiser mon apprentissage à partir d'un projet, je trouve qu'il est extrêmement utile de réfléchir à mes conclusions, techniques ou compétences douces :

1. Écrire un README clair et concis dans le dépôt du projet GitHub. Cela aide les autres développeurs à comprendre et à s'intéresser au projet.

2. Écrire un article de blog (comme celui que j'écris maintenant) sur les aspects de plus haut niveau, par exemple, l'aperçu de l'architecture, la conception des fonctionnalités, les défis et les solutions, et ainsi de suite.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/README-1.png align="left")

*Ma section README sur l'intégration de mon moteur d'échecs dans d'autres projets de jeux*

![Image](https://www.freecodecamp.org/news/content/images/2020/09/-readme1-1.png align="left")

*Ma section README comparant les deux versions de mon moteur d'échecs*

### Crédits et liens

Un grand merci à Tim Min pour m'avoir incité à travailler sur ce projet, pour ses contributions (nouvelles idées de fonctionnalités + QA) sur le tableau Trello, et pour m'avoir tenu responsable. Tim est l'auteur du jeu de roman cinétique, [*The Wind at Dawn*](https://madeleine-chai.itch.io/the-wind-at-dawn).

* [Mon dépôt GitHub du moteur d'échecs](https://github.com/RuolinZheng08/renpy-chess)

* [Le tableau Trello public pour ce projet de moteur d'échecs](https://trello.com/b/ip9YLSPa/renpy-chess)

* [Ren'Py : un moteur de développement de jeux de roman visuel](https://www.renpy.org/)

* [python-chess : une bibliothèque pure Python pour les échecs](https://python-chess.readthedocs.io/en/latest/)

Restez en contact ! Connectez-vous avec moi sur [LinkedIn](https://www.linkedin.com/in/ruolin-zheng/), [GitHub](https://github.com/RuolinZheng08), [Medium](https://medium.com/@ruolinzheng), ou consultez [mon site web personnel](https://ruolinzheng08.github.io/).