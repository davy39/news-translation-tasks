---
title: La Souffrance de l'Attente — Naviguer à travers les 7 Niveaux de l'Enfer des
  Indicateurs de Progression
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-26T23:37:38.000Z'
originalURL: https://freecodecamp.org/news/the-pain-of-waiting-navigating-the-7-levels-of-progress-indicator-hell-decd3e019495
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5klWhpvdsBoo163ZB3VKpA.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: user experience
  slug: user-experience
- name: UX
  slug: ux
seo_title: La Souffrance de l'Attente — Naviguer à travers les 7 Niveaux de l'Enfer
  des Indicateurs de Progression
seo_desc: 'By Mike Zetlow

  How much hell are you willing to put your users through?

  Of course the answer you’d like to give is “None!” But if you’re developing web
  applications, you’re going to make your users wait for results at some point.


  “ While speedy resp...'
---

Par Mike Zetlow

Combien d'enfer êtes-vous prêt à infliger à vos utilisateurs ?

Bien sûr, la réponse que vous aimeriez donner est « Aucun ! ». Mais si vous développez des applications web, vous allez devoir faire attendre vos utilisateurs pour obtenir des résultats à un moment donné.

> « Bien que des temps de réponse rapides soient idéaux, il arrive simplement que même une mise à niveau du serveur ne vous permette pas de respecter les directives de vitesse du système. Dans ces cas, vous devez simplement rassurer l'utilisateur que l'ordinateur n'est pas parti déjeuner mais travaille fidèlement sur sa demande. » — [Les indicateurs de progression rendent un système lent moins insupportable](https://www.nngroup.com/articles/progress-indicators/)

Attendre est un point de douleur. Personne n'aime attendre avant de monter dans des montagnes russes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*q5f96SlK_akITn_cXLDODg.jpeg)
_Ça a vraiment l'air amusant._

Si l'attente est inévitable, nous devrions faire tout notre possible pour réduire cette douleur pour le bien de nos utilisateurs. Disney a expérimenté des « [files d'attente interactives](https://www.youtube.com/watch?v=zuJlaVqe69I) » pour ses attractions. Bien que ce soit à peu près aussi amusant que cela en a l'air, au moins c'est quelque chose.

En développement web, nous faisons quelque chose d'à peu près aussi amusant : des indicateurs de progression. (Aussi appelés : barres de progression, throbbers, barres de chargement, cercles de chargement, icônes de chargement, roues tournantes ou curseurs d'attente.)

Voici les 7 Niveaux de l'Enfer des Indicateurs de Progression, du moins douloureux au plus douloureux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nzvPNWlJloWU0LmbfXGGLg.png)

### Le Premier Niveau de l'Enfer des Indicateurs de Progression

#### Affichage de Progression Précis

Il s'agit d'un indicateur de progression qui affiche l'état précis de votre application. Il est difficile à réaliser correctement et nécessite beaucoup de code supplémentaire (en plus de faire ce que l'utilisateur a demandé à l'application de faire). C'est génial pour les utilisateurs — mais cela appartient toujours à l'Enfer car attendre est un point de douleur, peu importe la précision du temps d'attente.

L'Affichage de Progression Précis est difficile à réaliser. Les développeurs luttent avec ce problème depuis des [décennies](https://developers.slashdot.org/story/13/02/13/0026234/ask-slashdot-why-is-it-so-hard-to-make-an-accurate-progress-bar). Si vous êtes la personne UX qui le propose, votre équipe pourrait demander si vous pouvez obtenir un effet similaire sans autant d'efforts de développement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qh5F7pw_HG1WaNkc4XpPeQ.png)

### Le Deuxième Niveau de l'Enfer des Indicateurs de Progression

#### Affichage de Progression Semi-Précis

De nombreuses applications peuvent approximer le temps d'attente pour les utilisateurs. L'indicateur de progression peut aborder différentes étapes d'une requête et informer les utilisateurs. Ce n'est pas idéal car le temps passé à chaque étape peut varier considérablement, conduisant à une barre de progression « saccadée ».

Par exemple, l'appel pourrait prendre 20 % du temps, la requête 70 % du temps, le tri 2 % du temps, et le retour 8 % du temps. L'utilisateur passe la plupart de son temps à regarder une barre qui est remplie à 20 %, puis soudainement elle avance un peu et c'est terminé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qdvpTCRuyvZce81cKv2NtQ.png)
_Crédit : [https://xkcd.com/612/](https://xkcd.com/612/" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/1*sSQO33S-CfvxNPYoVX6Y6Q.png)

### Le Troisième Niveau de l'Enfer des Indicateurs de Progression

#### Throbber avec des Trucs de Perception

Un [throbber](https://en.wikipedia.org/wiki/Throbber) est un simple indicateur de chargement ou de rotation qui s'anime indéfiniment. À ce niveau, nous ajoutons des trucs de perception qui donnent à l'utilisateur l'impression que le chargement se fait plus rapidement qu'il ne l'est en réalité.

> « Il est soutenu que le temps subjectif n'est pas seulement le plus facilement manipulable, mais aussi le plus important. Après tout, notre perception est notre réalité. Nous n'avons pas besoin de rendre les ordinateurs plus rapides pour qu'ils semblent plus rapides. » - [Chris Harrison](http://www.chrisharrison.net/index.php/Research/ProgressBars2)

Vous pouvez utiliser des trucs de perception sur les Affichages de Progression Précis et Semi-Précis également. Mais ils sont surtout nécessaires au Troisième Niveau de l'Enfer des Indicateurs de Progression et en dessous, où la progression n'est pas mesurée et l'attente peut être la plus frustrante.

Voici trois de mes préférés :

#### Truc de Perception #1 : Augmentation Visuelle

Toutes les conceptions de barres de progression ne se valent pas. Certaines semblent se remplir plus rapidement que d'autres. [Chris Harrison](http://www.chrisharrison.net/index.php/Research/ProgressBars2) a étudié cela, opposant diverses conceptions les unes aux autres :

Les designers UX doivent équilibrer ce truc de perception avec le design de l'application / de la marque.

#### Truc de Perception #2 : Mises à Jour de Statut Textuelles

Fournissez un texte à l'utilisateur (vrai ou faux) sur l'état de l'application.

> « De nombreuses fois, si les utilisateurs sont informés, ils peuvent être plus patients. Il peut être utile d'ajouter une clarté supplémentaire en incluant un texte qui indique à l'utilisateur ce qui se passe ou explique pourquoi l'utilisateur attend. » — [Smashing Magazine](https://www.smashingmagazine.com/2016/12/best-practices-for-animated-progress-indicators/)

Adobe fait du bon travail à ce sujet. Regardez « Lecture des pinceaux… » ci-dessous. (Adobe fait défiler des dizaines de ces statuts en fonction du temps que cela prend pour charger sur la machine de l'utilisateur.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*qxpCiaoDXGmhj2zVtvceDQ.png)

#### Truc de Perception #3 : Humour

Des études ont montré l'efficacité de l'humour pour atténuer l'anxiété. Des entreprises avisées, comme Southwest Airlines, utilisent souvent l'[humour](https://www.youtube.com/watch?v=07LFBydGjaM) pendant les moments d'anxiété potentielle :

Attendre une réponse d'une application augmente définitivement les niveaux d'anxiété des utilisateurs, et l'humour peut être un excellent outil pour atténuer cela. (Cela fonctionne mieux dans les applications grand public, car cela peut ne pas être acceptable dans certaines applications d'entreprise.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*CKvZYp5NB9jdIq_p2tuaVg.png)

### Le Quatrième Niveau de l'Enfer des Indicateurs de Progression

#### La Barre de Progression Sans Fin

Pour les utilisateurs, il semble qu'une barre de progression avance assez rapidement, puis elle ralentit de plus en plus, jusqu'à ce qu'enfin ils ne puissent plus dire si elle avance du tout.

C'est un truc assez méchant à faire subir aux utilisateurs, bien que les développeurs aient pu avoir de bonnes intentions. Les développeurs ont codé un indicateur de progression qui est essentiellement un throbber mais qui ressemble à une barre qui se remplit. Elle ralentit à mesure que la requête prend plus de temps, rampant le long de l'asymptote à un rythme infiniment petit non nul jusqu'à ce que la requête soit complète (si la requête se complète !), et à ce moment-là, le compteur monte brusquement à plein.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WGbU97z9GLS7h_D0Zac61A.png)

Pour les développeurs, cela ressemble à une solution fonctionnelle qui est mathématiquement élégante. Malheureusement, les utilisateurs la détestent.

> « Les changements de vitesse seront remarqués et auront un impact sur la satisfaction de l'utilisateur : si la progression avance rapidement pour ensuite s'arrêter sur le dernier pourcentage restant, l'utilisateur deviendra frustré et les avantages de montrer la progression seront annulés. » — [Les indicateurs de progression rendent un système lent moins insupportable](https://www.nngroup.com/articles/progress-indicators/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Yc24yknEsxUil2RTxb1-BA.png)

### Le Cinquième Niveau de l'Enfer des Indicateurs de Progression

#### Throbber

Vous voyez cela partout dans les applications logicielles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*k6UgQB2PF3WLdkWPo7VXGA.gif)

![Image](https://cdn-media-1.freecodecamp.org/images/1*BJ7hHX9V4Ql2E6BxolFPbA.gif)

Ce ne sont que des animations en boucle. Les throbbers indiquent aux utilisateurs que l'application travaille sur une requête, mais s'ils doivent attendre trop longtemps, ils l'abandonneront. Les throbbers sont mieux utilisés avec des requêtes courtes. S'ils sont utilisés avec des trucs de perception, ils peuvent monter de deux niveaux dans l'Enfer des Indicateurs de Progression. Sinon, ils restent ici.

> « Montrer une animation graphique en boucle offre un retour que le système fonctionne, mais cela ne donne aucune information sur la durée pendant laquelle l'utilisateur devra attendre… Et si un spinner tourne indéfiniment, les utilisateurs ne peuvent pas être sûrs si le système fonctionne toujours ou s'il s'est arrêté, ils peuvent donc décider d'abandonner complètement la tâche. » — [Les indicateurs de progression rendent un système lent moins insupportable](https://www.nngroup.com/articles/progress-indicators/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*VANUtVFRIsT9-psIeuwZzg.png)

### Le Sixième Niveau de l'Enfer des Indicateurs de Progression

#### Texte Statique

Ou :

![Image](https://cdn-media-1.freecodecamp.org/images/1*bPkBdXQYkCcl-pmbsITuMQ.jpeg)

Vous voyez généralement cela sur les sites web gouvernementaux ou les applications où les consommateurs ont peu de choix sur le marché. (Mon portail d'assurance maladie m'a récemment sorti celui-ci.)

Intellectuellement, il y a peu de différence entre cela et une animation en boucle infinie. Mais le texte statique semble juste si **_figé_**.

Les utilisateurs sont plus susceptibles de penser que votre application est bloquée ou cassée avec ce type d'indicateur de progression.

Le [Groupe Nielsen Norman](https://www.nngroup.com/articles/progress-indicators/) le dit mieux : « Indicateurs de progression statiques : ne les utilisez pas. »

![Image](https://cdn-media-1.freecodecamp.org/images/1*TJ_yLCo5-m9axRYtrL5-kg.png)

### Le Septième Niveau de l'Enfer des Indicateurs de Progression

#### Rien

Aucun indicateur de progression.

Juste l'enveloppe vide de l'interface gelée de votre application travaillant dur en arrière-plan tandis que l'utilisateur reste là, perplexe, frustré, priant pour que la fin arrive.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5klWhpvdsBoo163ZB3VKpA.jpeg)

### Étude de Cas : Indicateur de Progression de Connections

Avec [Connections](https://chsiconnections.com/), une application de gestion d'assurance basée sur le web, nous avons parfois laissé les utilisateurs au Septième Niveau de l'Enfer des Indicateurs de Progression. Mon objectif était de nous faire atteindre au moins le Troisième Niveau.

Nous avons implémenté une barre de progression inspirée de YouTube dans notre en-tête pour afficher la progression de la requête de la base de données de l'utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*w0w6CucmVdVpCH4_9z_6mw.gif)

C'est essentiellement un throbber, mais nous avons utilisé quelques trucs de perception pour atténuer l'anxiété de l'attente pour nos utilisateurs :

1. **Augmentation visuelle qui correspond à notre design de marque** — Le rayage se produit de droite à gauche pendant l'attente, puis la barre se remplit rapidement de gauche à droite une fois chargée. Les animations se produisent également à un rythme plus rapide que les valeurs par défaut des frameworks (Bootstrap, je te regarde) pour [qu'elles semblent plus rapides](https://codepen.io/149203/pen/bWzwrb).
2. **Mises à jour de statut textuelles** — Nous affichons une vingtaine de statuts textuels (« Connexion à la base de données », « Acquisition de la connexion », etc.). Ils sont affichés à des intervalles aléatoires de 2 à 4 secondes pour sembler réels.
3. **Humour** — Si la requête prend plus de 12 secondes (douloureux, mais parfois nécessaire), nos mises à jour de statut textuelles deviennent plus drôles et plus étranges. Nous espérons que les requêtes ne prendront jamais autant de temps, mais si c'est le cas, nous essayons de réduire l'anxiété avec de l'humour.

### Attendre est une Souffrance

C'est un point de douleur de toute application logicielle. Espérons que j'ai montré que votre application peut s'élever des profondeurs avec un peu de travail UX et de design. Ne laissez pas vos utilisateurs croupir dans les abîmes de l'Enfer des Indicateurs de Progression. Le niveau le plus élevé d'un Affichage de Progression Précis peut ne pas être réalisable dans votre application, mais avec un peu de créativité, vous pouvez vous élever et maintenir la douleur de l'attente à un niveau bas.