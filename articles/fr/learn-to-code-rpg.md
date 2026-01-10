---
title: Apprendre à Coder RPG – Un Jeu Vidéo Visual Novel Où Vous Apprenez les Concepts
  de l'Informatique
subtitle: ''
author: Lynn Zheng
co_authors: []
series: null
date: '2021-12-22T17:23:00.000Z'
originalURL: https://freecodecamp.org/news/learn-to-code-rpg
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/Splash-Art.png
tags:
- name: freeCodeCamp.org
  slug: freecodecamp
- name: Game Development
  slug: game-development
- name: GameDev
  slug: gamedev
- name: Python
  slug: python
seo_title: Apprendre à Coder RPG – Un Jeu Vidéo Visual Novel Où Vous Apprenez les
  Concepts de l'Informatique
seo_desc: 'Hi, everybody – Lynn here. It''s my great pleasure to announce the launch
  of Learn to Code RPG, a project we''ve been developing in secret for the past eight
  months.

  Learn to Code RPG is an interactive visual novel game where you will teach yourself
  to...'
---

Bonjour à tous – Lynn ici. C'est avec un grand plaisir que je vous annonce le lancement de **Learn to Code RPG**, un projet que nous avons développé en secret pendant les huit derniers mois.

**Learn to Code RPG** est un jeu interactif de type visual novel où vous apprendrez à coder, à vous faire des amis dans l'industrie technologique et à poursuivre votre rêve de devenir développeur. 🎯

Le jeu propose :

* Des heures de gameplay 🎮

* Des arts et musiques originaux 🎨

* 600+ questions de quiz sur l'informatique 📚

* 50+ Easter Eggs à découvrir 🚀

* 6 fins différentes 👀

* Des personnages sympathiques et un chat adorable 🐱

* Des minijeux ! 🎮

C'est une première version et nous espérons ajouter plus de contenu à l'avenir. Les futures versions auront plus de **personnages, scénarios, quêtes secondaires, arts, musiques**, et oui, **minijeux**. (Un mode vitesse et survie pour les quiz d'informatique, ça vous dit ?) Nous prévoyons également de le localiser dans différentes langues. 🌍 Le ciel est la limite ici. ✉️

## Vous pouvez le télécharger et y jouer gratuitement sur [itch.io](https://freecodecamp.itch.io/learn-to-code-rpg).

Si vous souhaitez en savoir plus sur le jeu lui-même, mon processus de développement, et ainsi de suite, continuez votre lecture. C'est un devlog très visuel (notre jeu est un Visual Novel pour une raison) et je suis sûr que vous allez l'apprécier.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/img_1-1.png align="left")

*Learn to Code RPG – Un jeu où vous incarnez un personnage apprenant à coder*

## Où Tout a Commencé

Commençons par un peu de contexte sur moi.

J'ai toujours aimé les jeux vidéo riches en histoire depuis que je suis petite. 🧒

Mon intérêt pour le développement de jeux m'a inspiré à étudier l'informatique à l'université. En juin 2021, j'ai obtenu un diplôme de Bachelor et de Master en informatique de l'Université de Chicago.

En juillet 2021, alors que je planifiais mon déménagement à San Francisco pour commencer ma carrière de développeur logiciel, Quincy m'a contactée avec cette idée de jeu.

> Un jeu où vous apprenez à coder, à vous faire des amis, à explorer la culture tech et à finalement percer dans l'industrie technologique. 🎯

Bien que je m'amuse avec des moteurs de développement de jeux comme Unity et Ren'Py et que j'ai créé de petits projets passionnants de mon côté, ce serait la première fois que je construis un jeu de A à Z, en équipe (principalement) solo. Autrement dit, j'étais un peu submergée par cette opportunité de réaliser mon rêve de développement de jeux. 🤯

Eh bien, vous connaissez le dicton : Si on vous offre une place dans une fusée 🚀, ne demandez pas quel siège !

Alors j'ai dit oui et je me suis lancée.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-18-at-12.56.15.png align="left")

*Qui suis-je pour refuser une offre de CupcakeCPU ? 🧁*

## De Zéro à Héros : Comment Construire un Jeu en Quatre Mois

### L'Histoire

L'idée de l'histoire était assez claire dès le début : Le héros/héroïne prend la décision d'apprendre à coder, surmonte les obstacles tout au long du voyage, rencontre des alliés et des mentors, et finit par obtenir le grand prix – un emploi de développeur brillant.

J'ai commencé avec le cadre d'écriture classique de [Le Voyage du Héros](https://en.wikipedia.org/wiki/Hero%27s_journey), ou le monomythe en 17 étapes.

(Depuis que j'ai commencé à travailler sur ce jeu, je regrette souvent de ne pas avoir suivi au moins un cours d'écriture créative à l'université. 😅)

Voici un aperçu de mon plan pour la première et la troisième étape des 17 étapes, directement depuis mon Google Doc :

<table><tbody><tr><td colspan="1" rowspan="1"><p>1. L'Appel à l'Aventure</p></td><td colspan="1" rowspan="1"><p>la première étape du voyage du héros présente souvent au public l'existence actuelle (et parfois plutôt mundane) du protagoniste.</p></td><td colspan="1" rowspan="1"><p><strong>Personnage Principal (abréviation PP) </strong>obtient son diplôme et retourne vivre chez ses parents. Elle n'est pas vraiment sûre de ce que sa carrière va ressembler, alors elle passe ses journées à travailler des petits boulots et à parcourir les offres d'emploi. Elle a postulé à quelques emplois dans la vente et le conseil, mais ils l'ont rejetée.</p></td></tr></tbody></table>

<table><tbody><tr><td colspan="1" rowspan="1"><p>3. L'Aide Surnaturelle</p></td><td colspan="1" rowspan="1"><p>à cette étape du voyage, le protagoniste cherche une figure sage et gagne peut-être un objet spécial ou une compétence dans le processus.</p></td><td colspan="1" rowspan="1"><p><strong>Annika, </strong>la meilleure amie de PP à l'université, appelle PP un jour. Annika est excitée car elle vient d'obtenir un poste de développeur web junior, après avoir passé 6 mois à rafraîchir ses compétences en informatique (en auditant quelques cours d'informatique à l'université). Annika demande comment va PP ; est ravie que PP envisage également d'apprendre à coder ; et encourage PP qu'elle peut le faire si elle a la bonne méthode d'étude et les bonnes ressources.<br>Annika présente à PP la ressource qu'elle utilise.</p></td></tr></tbody></table>

### Les Personnages

En incluant le personnage principal que le joueur contrôle, nous avons quatre personnages majeurs dans le jeu :

* Le personnage principal, **Lydia**, une récente diplômée de l'université. (Dans les futures versions du jeu, nous pourrons peut-être présenter quelques personnages principaux différents parmi lesquels le joueur pourra choisir.)

* **Annika**, la meilleure amie du personnage principal à l'université

* **Marco**, qui devient le mentor du personnage principal

* **Layla**, la collègue d'intégration du personnage principal à son premier emploi de développeur

J'ai commencé à concevoir les personnages en collectant des images sur Pinterest. Ensuite, Quincy et moi avons commissionné un artiste en ligne pour créer les sprites des personnages et l'image de splash.

Dans les images ci-dessous, vous pouvez voir les inspirations de personnages de Pinterest (le copyright appartient à leurs artistes originaux) et le design final côte à côte.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Untitled265_20211217211947.PNG align="left")

*Art d'inspiration pour Lydia + carte de personnage finale*

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Untitled265_20211217212148.PNG align="left")

*Art d'inspiration pour Annika + carte de personnage finale*

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Untitled265_20211217211928.PNG align="left")

*Art d'inspiration pour Layla + carte de personnage finale*

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Untitled265_20211217211832.PNG align="left")

*Art d'inspiration pour Marco + carte de personnage finale*

Maintenant que nous avons la distribution principale, que pouvons-nous ajouter pour donner plus de profondeur au personnage de **Lydia**, afin qu'elle ne reste pas seule dans sa chambre toute la journée à coder ? Peut-être pourrait-elle avoir un chat dans sa chambre ? 🐱

Et voici **Mint**, le chat de Lydia. (Art par moi-même en tant qu'artiste de fortune pour que notre artiste puisse se concentrer sur les personnages. L'art numérique 🎨 est mon deuxième plus grand hobby après le développement de jeux.)

![Image](https://www.freecodecamp.org/news/content/images/2021/12/mint.gif align="left")

*Mint dit bonjour !*

### Les Graphismes

Avec les graphismes des personnages terminés, vous pourriez penser que cela conclut la majeure partie des graphismes. Mais pas si vite ! Un visual novel est, comme son nom l'indique, visuel, et a donc besoin de beaucoup plus de graphismes pour raconter une histoire captivante.

Par exemple, dans cette image ci-dessous, en plus des sprites de personnages, il y a l'image de fond et quelques composants GUI comme la boîte de texte.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-18-at-12.40.00.png align="left")

*Composants graphiques de base : GUI, sprites de personnages, fond*

Pour créer les images de fond, j'ai appliqué des filtres d'effets spéciaux aux images de stock pour ajouter une texture de type aquarelle. Ainsi, la palette de couleurs de nos personnages se fond parfaitement dans celle du fond.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Untitled266_20211217213638.PNG align="left")

*En haut : image de stock. En bas : avec filtres*

Pour illustrer le passage du temps en une seule journée, j'ai changé l'éclairage des images de fond en appliquant une manipulation de couleur de manière programmatique. (Consultez [notre dépôt GitHub](https://github.com/freeCodeCamp/LearnToCodeRPG) si vous êtes intéressé par les détails de l'implémentation !)

![Image](https://www.freecodecamp.org/news/content/images/2021/12/color.png align="left")

*Quatre modes d'éclairage*

Pour un coup de pouce motivationnel, chaque fois que j'ai envie de procrastiner, je change de vitesse créative et gribouille des objets divers qui apparaissent tout au long du jeu. 🤣

Et c'est ainsi que nous avons obtenu des cookies, des toasts, des pizzas, du poulet frit, et plus encore dans le jeu !

![Image](https://www.freecodecamp.org/news/content/images/2021/12/ezgif.com-gif-maker-7-.gif align="left")

*Délicieux !*

### Le Code

J'ai utilisé le moteur de jeu avec lequel je suis le plus familière, [le Ren'Py Visual Novel Engine](https://www.renpy.org/). J'ai réutilisé beaucoup de code de mes anciens projets passionnants – par exemple, [des sprites de personnages clignotants](https://gist.github.com/RuolinZheng08/b845f416ebda5b02ebc6b62379105564) et [un minijeu de rythme](https://github.com/RuolinZheng08/renpy-rhythm).

![Image](https://www.freecodecamp.org/news/content/images/2021/12/blink2.gif align="left")

*Personnages clignotants 😉*

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-17-at-19.33.39-1.png align="left")

*Minijeu de rythme. Pouvez-vous obtenir un score parfait ?*

J'ai également incorporé du code open-source de Ren'Py comme [le code pour les balises de texte cinétique](https://wattson.itch.io/kinetic-text-tags) et [le code pour le texte d'icône de plume](https://tacoen.itch.io/feather-icon).

![Image](https://www.freecodecamp.org/news/content/images/2021/12/awesome.gif align="left")

*Balise de texte cinétique, qui peut être désactivée pour l'accessibilité*

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-17-at-22.05.37.png align="left")

*Les icônes de plume sont géniales pour créer une GUI nette et simpliste*

Je vais m'abstenir de plonger dans la base de code ici (parce que je ne saurai pas quand m'arrêter alors 😅). Sachez simplement qu'il y a beaucoup de code, à la fois pour la logique et la GUI. Voir le rapport Ren'Py Lint ci-dessous.

Ouf... Pouvons-nous maintenant passer à quelque chose de plus visuel ?

```pgsql
Ren'Py 7.4.8.1895 lint report, generated at: Fri Dec 17 22:11:43 2021
Statistics:
The game contains 1,335 dialogue blocks, containing 15,390 words and 85,105 characters, for an average of 11.5 words and 64 characters per block.
The game contains 40 menus, 20 images, and 49 screens.
```

### Le Suivi de Progression

Même un projet solo a besoin d'un chef de projet, alors pourquoi ne pas être mon propre chef de projet ?

J'ai utilisé Trello pour suivre mon processus et collaborer avec les autres. J'ai même codé par couleurs les étiquettes pour différentes catégories de tâches, comme *codage, UI/UX, écriture*, et ainsi de suite comme montré dans l'image ci-dessous sur la première carte dans la colonne **Backlog**.

Et wow, n'est-ce pas une longue liste de tâches accomplies ? 😮

![Image](https://www.freecodecamp.org/news/content/images/2021/12/trello.gif align="left")

*Mon tableau Trello*

Tout dans les colonnes **TODO** et **Doing** est déplacé vers **Done**, et cela nous amène à...

## Mon Bilan

Hourra ! Après huit mois (quatre mois d'ébullition de l'idée, plus quatre mois de codage, d'écriture et de création artistique intensifs), nous vous présentons **Learn to Code RPG. 🤩**

En quatre mois dans le jeu, **Lydia** est passée d'*une ingénieure en herbe* à *une ingénieure avec un emploi de développeur*. 🎯

En quatre mois dans le monde réel, je suis passée d'*une développeuse de jeux en herbe* à *une développeuse de jeux qui a réellement construit un jeu*. 🎮

Naturellement, voici la question à un million de dollars : Quel est mon bilan de tout ce processus ?

Eh bien, comme tout processus créatif, le développement de jeux n'est pas facile. J'ai une équipe incroyable qui me soutient : notre artiste Noa qui a créé les arts des personnages, Quincy qui a créé les pistes de musique originales, et les relecteurs et testeurs de freeCodeCamp.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-17-at-22.26.07.png align="left")

*Mes contributions GitHub distinguent les jours où je code des jours où je brainstorm ou j'écris ou je dessine 🦊*

J'ai grandi à la fois en termes de compétences techniques (en trouvant des moyens créatifs de construire des choses dans Ren'Py), de compétences non techniques (en agissant comme mon propre chef de projet), et plus encore (en gérant les attentes, en surmontant le syndrome de l'imposteur et en cherchant un équilibre entre vie professionnelle et vie privée).

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-18-at-12.33.25.png align="left")

*Savez-vous ce qu'est le syndrome de l'imposteur ? 👩‍💻 Vous pariez que je le sais !*

Ce n'était pas une promenade de santé, mais le résultat en vaut chaque seconde de travail acharné. Plus important encore, j'ai hâte que vous jouiez au jeu et que vous me donniez votre avis afin que je puisse améliorer le jeu dans les futures versions.

J'espère que vous prendrez autant de plaisir à jouer à **Learn to Code RPG** que j'en ai eu à le créer ! 🤝

## Liens vers Learn to Code RPG

Vous pouvez trouver le jeu sur itch.io ici :

%[https://freecodecamp.itch.io/learn-to-code-rpg]

[Et voici le dépôt GitHub avec tout le code](https://github.com/freeCodeCamp/LearnToCodeRPG).

Vous pouvez également regarder la bande-annonce du jeu sur YouTube et la partager avec vos amis :

%[https://www.youtube.com/watch?v=vLK4fOeiIEk]

Vous voulez voir à quoi ressemble le jeu ? Regardez le [Let's Play avec Ania et Lynn](https://www.youtube.com/watch?v=b_IDdQzPRR4).

%[https://www.youtube.com/watch?v=b_IDdQzPRR4]

Et [voici le kit de presse officiel du jeu](https://www.freecodecamp.org/news/learn-to-code-rpg-press-kit/).

Si vous êtes intéressé par la création d'un jeu Visual Novel vous-même, consultez cet article de moi :

%[https://www.freecodecamp.org/news/use-python-to-create-a-visual-novel/]