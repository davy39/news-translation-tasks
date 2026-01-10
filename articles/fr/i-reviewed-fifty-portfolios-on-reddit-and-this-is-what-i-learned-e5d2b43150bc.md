---
title: Ce que j'ai appris en examinant 50 portfolios sur Reddit en 3 jours fous.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-07T01:47:35.000Z'
originalURL: https://freecodecamp.org/news/i-reviewed-fifty-portfolios-on-reddit-and-this-is-what-i-learned-e5d2b43150bc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kWDEvEcGmI9gjsKInrbQrg.png
tags:
- name: Design
  slug: design
- name: reddit
  slug: reddit
- name: technology
  slug: technology
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Ce que j'ai appris en examinant 50 portfolios sur Reddit en 3 jours fous.
seo_desc: 'By James Y Rauhut

  I’ve always enjoyed critiquing applicants’ portfolios at the design studio where
  I work. And I also often ask for feedback on my own designs on Reddit’s webdev subreddit.

  So one day, I thought it’d be fun to unofficially review the ...'
---

Par James Y Rauhut

J'ai toujours aimé critiquer les portfolios des candidats dans le studio de design où je travaille. Et je demande souvent des retours sur mes propres designs sur le subreddit webdev de Reddit.

Alors un jour, j'ai pensé que ce serait amusant de revoir officiellement les portfolios de quiconque demandant une critique. Je ne savais pas dans quoi je m'embarquais.

J'ai commencé en [offrant mes services gratuitement](https://www.reddit.com/r/webdev/comments/508dys/want_your_portfolio_reviewed/) aux 120 000 personnes qui lisent le subreddit.

Les choses ont commencé tranquillement. Je jouais une partie de Rocket League, puis il y avait un ou deux portfolios à examiner. Ensuite, je suis allé dormir.

Quand je me suis réveillé, j'avais vingt demandes. Et celles-ci ont continué à affluer pendant trois jours consécutifs.

En fin de compte, j'ai pu reconnaître certains schémas communs et des points forts/faibles à travers tous les portfolios. Mettons en lumière ceux-ci.

Notez que cet article parle spécifiquement des développeurs front-end qui souhaitent rejoindre un studio de design. Si vous avez un objectif ou un public différent pour votre travail, cet article peut ne pas être applicable.

### Quelles étaient les pires choses que j'ai vues ?

À vrai dire, la communauté [r/webdev](https://www.reddit.com/r/webdev) s'en est mieux sortie que l'ensemble des candidats de mon studio. Je pense que cela témoigne de la dévotion des membres de la communauté à leur métier.

Cela ne signifie pas que le portfolio de tout le monde était parfait, cependant. Il y avait des erreurs communes qui étaient absolument à éviter.

#### N'oubliez jamais l'accessibilité au clavier et le contraste.

L'accessibilité était la plus grande erreur commise lors de la révision. Une des premières choses que je fais physiquement avec un portfolio est d'essayer de le naviguer sans utiliser ma souris. Si ce n'est pas possible, je sais que le candidat n'a pas l'accessibilité en tête.

Le contraste des couleurs pour le texte est également un facteur important. J'adorais mettre du texte blanc sur des fonds jaunes. Je pensais être branché !

Mais j'ai rapidement appris dans l'industrie que les utilisateurs ayant une basse vision ont du mal à lire le texte avec de mauvais choix de couleurs. Si vos yeux ne sont pas entraînés à repérer les faibles contrastes, référez-vous au Centre pour les Personnes Handicapées [Color Contrast Checker](http://webaim.org/resources/contrastchecker/).

> Conseil #1 : Certains membres de votre public cible auront des handicaps. Avant d'écrire un quelconque style, assurez-vous que votre HTML est accessible.

#### Arrêtez d'essayer d'évaluer vos propres compétences.

![Image](https://cdn-media-1.freecodecamp.org/images/zvv6TNrph-YbTgNE-50jL7W4QmFMD4Kjdwmy)

Une tendance qui a plagié les sites de portfolios pendant des années a été les barres de progression des compétences. Vous dites que vous êtes compétent à 85 % en Angular ? Qu'est-ce que cela signifie ? Comment cela se compare-t-il à votre compétence à 80 % en Node ? La plupart des réviseurs ne comprendront que trois niveaux de compétence :

* Vous ne connaissez pas du tout la compétence
* Vous êtes encore en train d'apprendre la compétence
* Vous vous sentez confiant dans la compétence

Ne vous inquiétez pas du premier point. Dites-moi simplement ce que vous apprenez et ce en quoi vous vous sentez confiant. Tout cela sera prouvé dans vos projets, de toute façon.

#### Passez au mobile ou rentrez chez vous.

Voulez-vous savoir ce que beaucoup de réviseurs aiment faire avec votre portfolio ? Nous adorons ouvrir votre site web et ajuster immédiatement la largeur de la fenêtre du navigateur d'avant en arrière. Cela nous indique si vous prenez en considération la multitude de dispositifs sur lesquels votre site pourrait être consulté.

Voulez-vous aller au-delà de ce seuil minimum ? Alors écrivez votre CSS en [mobile-first](https://www.sitepoint.com/introduction-mobile-first-media-queries/). Écrire un style mobile-first nous indique que vous aimez écrire la plus petite quantité de code nécessaire. Lorsque vous vous arrêtez simplement à avoir des media queries avec une propriété `max-width`, cela nous indique que les dispositifs mobiles étaient une réflexion après coup dans votre design.

### Que devaient prouver les gens ?

Les projets réels sont la véritable substance d'un site de portfolio. Ils me prouvent que vous avez l'expérience de travail pertinente.

Un CV ou une liste d'emplois précédents est une belle chronologie. Mais en tant que créateur, votre création est la validation ultime.

Voici des parties des sections de projets des gens qui ont facilité ma vie en tant que réviseur.

#### Montrez-moi le code et le site en direct.

Vous avez une description de projet, un compte rendu de processus et parlez de la technologie utilisée. C'est bien, mais où est le code ?

Il est courant que les embauches de l'industrie se retrouvent impliquées dans des projets de travail privés. Mais sans aucune opportunité d'inspecter votre code, vous rendez le travail du réviseur plus difficile. Nous aurons du mal à savoir s'il vaut la peine de passer à l'étape suivante dans un processus de recrutement.

Si le code est propriétaire, où est le site en direct ? Si je peux voir votre code, pourquoi n'auriez-vous pas une version en direct en cours d'exécution ?

> Conseil #2 : Travaillez sur des projets personnels et secondaires liés à la même technologie que vous utilisez au travail. Non seulement cela vous aide à vous former pour votre rôle actuel, mais cela permet également à un réviseur de portfolio de savoir où se situent vos compétences.

#### Dites-moi à quoi vous avez réellement contribué.

![Image](https://cdn-media-1.freecodecamp.org/images/n3vM1vvvu1goDjC3qzJr7VQ8qNtYdPyq2GFU)

Les projets de groupe sont excellents pour montrer à quel point vous collaborez bien. La plupart des projets nécessiteront des compétences de travail d'équipe.

Avec les portfolios, cependant, vous devez être clair sur le travail que vous avez vous-même contribué. Les dépôts Github peuvent fournir un historique clair pour que je puisse examiner votre travail et comprendre cette dynamique de groupe.

L'honnêteté dans vos comptes rendus de projet est toujours appréciée. N'exagérez pas votre rôle au sein d'un projet, car les personnes examinant votre portfolio plongeront dans l'historique Git d'un projet pour vérifier par elles-mêmes.

#### Prouvez que vous n'avez pas besoin de Bootstrap ou de jQuery.

Il est compréhensible si vous avez commencé à apprendre le CSS avec Bootstrap ou le JavaScript avec jQuery. Le problème survient lorsque **tous** vos projets contiennent Bootstrap et jQuery.

Même si Bootstrap est pratique, j'ai besoin de savoir que vous avez une compréhension claire du CSS. J'ai également besoin de savoir si vous avez une base solide en JavaScript pur. Cela garantit que je pourrai vous intégrer à un projet utilisant n'importe quelle combinaison d'outils front-end déjà utilisés.

En fait, nous n'autorisons pas du tout Bootstrap ou jQuery pendant notre processus d'entretien. Vous serez donc mieux préparé pour les futurs entretiens et défis si vous avez les compétences appropriées en CSS et JavaScript.

### Qu'est-ce qui s'est le plus démarqué ?

Nous avons donc passé en revue les éléments dont votre portfolio a besoin et les façons dont les portfolios peuvent mal tourner. Qu'en est-il des éléments qui excitent un réviseur à propos d'un candidat ?

Les conseils suivants peuvent sembler moins concrets que mes suggestions précédentes, mais prenez-les à cœur.

#### Éloignez-vous de la norme.

Presque tout le monde avait le flux standard Intro > Compétences > Projets > Contact sur leur site. Presque tout le monde avait le menu hamburger exactement identique pour la navigation.

Voulez-vous attirer l'attention de vos réviseurs ? Soyez expérimental et apportez de petites modifications qui ne nuisent pas au design.

L'une des plus légères différenciations avait placé leur navigation sur le côté droit au lieu du côté gauche. Je savais qu'il était temps de me concentrer davantage car la navigation n'était pas sur le côté gauche ou en haut standard du layout. Simple, mais efficace.

#### Parlez en direction de votre emploi de rêve.

![Image](https://cdn-media-1.freecodecamp.org/images/xVl6WsFLvxGO3W-9AlK3oo99CSfOIOtUQ1Fx)

Avez-vous vu ce poste que vous voulez absolument ? Construisez votre portfolio autour des exigences et responsabilités de ce travail.

Il est difficile pour moi de comprendre pourquoi vous voulez un emploi dans notre studio lorsque votre portfolio est rempli de thèmes WordPress. Il est également difficile de vous considérer comme un bon candidat pour le rôle si votre principal focus semble être une industrie complètement différente.

Nous aimons les généralistes, mais c'est un grand plus de montrer que votre spécialité est également ce que le rôle prescrit.

> Conseil #3 : Beaucoup de portfolios sont utilisés à la fois pour les candidatures à un emploi et les clients freelance. Ne faites pas cela. La meilleure pratique est qu'un professionnel conçoive des portfolios séparés pour chacun de ces publics.

#### Chaque petit détail compte.

Voici le point le plus difficile pour beaucoup de gens : vous ne pouvez pas contrôler ce que votre réviseur voit sur votre portfolio.

Nous scannons constamment le site web au lieu de le lire de haut en bas. Assurez-vous donc que votre style de mise en page est parfait, que chaque phrase est relue et qu'il n'y a pas de liens brisés.

Il n'y a aucun moyen de savoir quelle partie de votre site le réviseur prendra réellement le temps de regarder.

### Vous pouvez le faire.

J'étais fier de tous les excellents portfolios pour lesquels j'ai pu fournir des retours, et des discussions qui ont suivi.

La partie la plus encourageante était lorsque les développeurs front-end n'étaient pas encore à la hauteur pour notre rôle, et j'ai pu leur donner des retours. Ces professionnels aspirants ont pris la critique au sérieux et positivement.

C'est exactement le genre d'attitude que je recherche plus tard dans le processus lorsque j'interviewe des candidats.

Mon espoir est que ces personnes s'amélioreront, et que j'aurai l'occasion de revoir leur travail à l'avenir.

P.S. Je suis _toujours_ en train de répondre aux demandes tardives de révisions de portfolios. De plus, tous les portfolios de mon image d'ouverture ont demandé la révision publiquement, et ont obtenu des scores élevés !

_Pour plus d'informations : N'hésitez pas à me contacter via les commentaires, [email](mailto:james@seejamescode.com), ou [@seejamescode](https://twitter.com/seejamescode). Je travaille à ATX pour IBM Design et j'adore toujours discuter avec la communauté du design web. N'oubliez pas de partager votre propre portfolio ou votre portfolio préféré dans les commentaires !_