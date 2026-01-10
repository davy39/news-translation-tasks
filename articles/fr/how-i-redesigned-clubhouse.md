---
title: Comment j'ai repensé Clubhouse, l'application la plus en vogue de la Silicon
  Valley
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-02T22:03:37.000Z'
originalURL: https://freecodecamp.org/news/how-i-redesigned-clubhouse
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/clubhouse-product-image-work.jpg
tags:
- name: Design
  slug: design
- name: designer
  slug: designer
- name: software design
  slug: software-design
- name: ux design
  slug: ux-design
seo_title: Comment j'ai repensé Clubhouse, l'application la plus en vogue de la Silicon
  Valley
seo_desc: "By Amy Lima\nI wanted to test my limits as a young designer by improving\
  \ the user experience of Clubhouse, the hottest new audio conversation app on the\
  \ social media scene. \nAfter speaking with both power users and novices on the\
  \ app, I uncovered some..."
---

Par Amy Lima

Je voulais tester mes limites en tant que jeune designer en améliorant l'expérience utilisateur de Clubhouse, la nouvelle application de conversation audio la plus en vogue sur la scène des médias sociaux. 

Après avoir parlé avec des utilisateurs expérimentés et des novices sur l'application, j'ai identifié certains points de friction spécifiques concernant la navigation et la découvrabilité dans l'application. Ces points sont devenus les principaux défis de conception qui ont guidé mon travail tout au long de ce projet.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/onboarding-mockups.jpg)
_Maquettes d'onboarding_

**Avertissement** : Je ne travaille pas pour Clubhouse, et les opinions exprimées dans cette étude de cas sont strictement les miennes. 

En tant que designer en herbe, je reconnais que ma vision pour ce projet peut être trop ambitieuse et parfois dépendante d'hypothèses sur les objectifs commerciaux et les données utilisateurs. 

Dans un monde parfait, je travaillerais aux côtés de l'équipe de Clubhouse avec un accès direct à ces ressources pour guider mon travail. En attendant, cette étude de cas est destinée à être une expérience d'apprentissage exploratoire sur un produit que j'admire profondément.

## Le Brief

Il est difficile de sous-estimer l'excitation autour de **Clubhouse**, l'application de chat audio où les membres peuvent se déplacer dans des salles virtuelles pour discuter de sujets allant de la culture à la politique. 

L'application a levé ses premiers [$100 millions](https://www.forbes.com/sites/alexkonrad/2020/05/15/andreessen-horowitz-wins-vc-sweepstakes-to-back-clubhouse-voice-app/?sh=57e5f3bd6f2a) avec seulement 1 500 utilisateurs un mois après sa sortie bêta. Et au moment de la rédaction de cet article, l'application la plus en vogue de la Silicon Valley vient d'être valorisée à [$1 milliard](https://fortune.com/2021/01/25/clubhouse-reaches-a-1-billion-after-taking-off-some-nine-months-ago/) de dollars, seulement 9 mois après son décollage et avant même son lancement public.

Au-delà de son succès auprès des investisseurs, Clubhouse a rassemblé une base d'utilisateurs incroyablement fidèle, dont la créativité a donné lieu à une salle continue de 24 heures dédiée à l'onboarding des nouveaux utilisateurs, ainsi qu'à une production en direct de [The Lion King.](https://www.complex.com/pop-culture/2020/12/clubhouse-users-organize-live-production-the-lion-king)

En tant qu'utilisateur bêta précoce sur la plateforme sur invitation uniquement, j'ai eu la perspective unique de suivre les mises à jour du produit (et son succès exponentiel) en temps réel. Et j'ai cherché à me challenger avec mon projet le plus ambitieux à ce jour : repenser l'application la plus excitante de la Silicon Valley de ces derniers temps. *Pas de pression.*

Les objectifs généraux de ce projet étaient :

* **Améliorer la découvrabilité au sein de Clubhouse**, permettant aux utilisateurs de trouver plus facilement de nouvelles salles, personnes et clubs avec lesquels interagir
* **Créer une expérience Hallway plus fluide**, où les utilisateurs peuvent filtrer et trouver les salles les plus pertinentes pour eux

## Défis UX : Simplifier une hiérarchie d'informations complexe

L'une des principales considérations que j'ai dû prendre en compte était la hiérarchie des principaux composants avec lesquels les utilisateurs peuvent interagir dans l'application :

* **Personnes** (autres utilisateurs de l'application)
* **Salles** (un lieu de rencontre virtuel pour les conversations audio), et
* **Clubs** (groupes basés sur des centres d'intérêt sous lesquels des salles peuvent être hébergées).

Au-delà de cela, **j'ai dû considérer comment chacun de ces composants était connecté**, à la fois sur le plan interpersonnel et dans le temps. 

Actuellement, le Hallway (écran d'accueil) d'un utilisateur de Clubhouse montre les salles _en direct_ connectées aux personnes et aux clubs qu'il suit (que j'appellerai tout au long de cette étude de cas "in-network"). Cela rend difficile pour les utilisateurs de suivre facilement les salles à venir dans leur réseau, ainsi que de rejoindre de nouvelles salles hors réseau.

**Cela est devenu une dichotomie majeure tout au long de mon travail** : je devais trouver un équilibre entre rendre chacune de ces parties individuelles de Clubhouse facilement découvrables tout en maintenant - et en simplifiant - le réseau qui les relie.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/ch-task-flow.jpg)
_Flux de tâches de découverte_

![Image](https://www.freecodecamp.org/news/content/images/2021/02/ch-sketch.jpg)
_Carte mentale de la relation entre les composants de Clubhouse_

## Recherche + Planification : Le rêve d'un chercheur UX

Un autre aspect unique de ce projet était **l'accès direct des utilisateurs bêta aux fondateurs de Clubhouse**, Paul Davison et Rohan Seth. Chaque dimanche, le duo anime le Clubhouse Townhall, un forum ouvert où ils partagent les dernières mises à jour du produit de la semaine, leur feuille de route à venir, leurs objectifs commerciaux et leurs principales priorités, ainsi qu'un espace pour les questions et réponses soumises par les utilisateurs.

Et grâce à la base d'utilisateurs enthousiastes de Clubhouse, les Townhalls officiels sont régulièrement suivis par des salles de récapitulatif du Townhall (mention spéciale au Community Club), où les utilisateurs expérimentés approfondissent les mises à jour de la semaine et les fonctionnalités qu'ils attendent avec le plus d'impatience.

Entre les Townhalls de Clubhouse, les salles de récapitulatif et les salles d'onboarding des nouveaux membres, à la fois officielles et communautaires (y compris les FAQ, les Q&A et les discussions), **j'ai passé en moyenne 5 heures par semaine pendant 6 semaines à recueillir autant d'informations et d'objectifs commerciaux que possible** depuis mon point de vue limité.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clubhouse-research-screenshots.jpg)
_Une compilation de certaines des salles qui sont devenues une partie régulière de ma recherche UX_

À partir de ces discussions, les objectifs généraux de l'équipe de Clubhouse sont :

* **Rendre Clubhouse accessible à tous** : Paul a toujours fait clair que la priorité absolue de l'équipe était de développer Clubhouse aussi rapidement que possible sans sacrifier la qualité
* **Mettre les créateurs en premier** : un autre point que Paul n'a jamais sous-estimé était la priorisation par l'équipe des créateurs de la plateforme, en construisant des outils qui permettraient la monétisation des créateurs
* **Améliorer la découvrabilité et le contenu suggéré** : au moment de ce projet, Clubhouse développait activement son répertoire de sujets et ses algorithmes qui rendraient la recherche de salles pertinentes progressivement plus facile

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clubhouse-sketches.jpg)
_Croquis préliminaires de la manière dont différents écrans pourraient se comporter_

## Entretiens avec les utilisateurs, des utilisateurs expérimentés aux novices

J'ai parlé avec des utilisateurs de Clubhouse — à la fois des utilisateurs expérimentés et des membres plus occasionnels de la communauté — pour découvrir les points de friction qu'ils rencontraient actuellement avec l'expérience de découverte de l'application. Ces entretiens m'ont donné les informations suivantes :

* **Garder cela léger** : la plupart des utilisateurs préféraient que la découverte de salles soit une expérience spontanée, ne voulant pas nécessairement planifier les salles à venir dans leurs calendriers personnels
* **Hallway encombré** : la plupart des utilisateurs étaient confus quant à la manière dont le hallway était actuellement organisé, et qui des personnes qu'ils suivaient étaient présentes dans une salle donnée
* **Hallway comme source de découverte** : malgré l'expérience encombrée du hallway, la plupart des utilisateurs comptaient encore sur le hallway pour trouver de nouvelles salles, malgré l'existence d'un onglet "Explore" (mais pas encore robuste)
* **Les amis d'abord** : lors de la décision de rejoindre une salle dans le hallway, les utilisateurs voulaient unanimement voir quels de leurs amis étaient dans une salle donnée

![Image](https://www.freecodecamp.org/news/content/images/2021/02/affinity-map--1-.jpg)
_Carte d'affinité de mes entretiens avec les utilisateurs (réalisée avec Evolve)_

Alors, comment pourrions-nous faire du Hallway un lieu clair et concis pour une interaction spontanée, tout en facilitant une découverte légère hors réseau ?

## Solution UX : Rationaliser le pipeline de découverte vers le Hallway

J'ai développé une interface utilisateur simple mais puissante qui facilite la navigation dans votre hallway et vos salles. Elle permet également d'intégrer facilement les salles trouvées via la page de découverte dans votre hallway.

Pour que cette solution semble cohérente et non cloisonnée, **j'ai dû mettre en œuvre une refonte presque complète de Clubhouse**, divisée en 5 expériences principales.

_Interagissez avec le prototype final_ [_ici_](https://www.figma.com/proto/zZ7KUnIt9Hrw27IKiXJfEo/CH-wireframes?node-id=263%3A257&scaling=scale-down)_._

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clubhouse-wireframes.jpg)
_Maquettes préliminaires_

## Expérience 1 : Le Hallway

![Image](https://www.freecodecamp.org/news/content/images/2021/02/ch-hallway-before-after.jpg)
_Le Hallway de Clubhouse actuellement (à gauche), et réoptimisé pour plus de fonctionnalités et d'accès aux contrôles (à droite)_

Les utilisateurs voulaient que leur expérience de hallway soit plus intentionnelle et sous leur contrôle. Pour y parvenir, j'ai établi une hiérarchie de premier niveau :

* **en cours vs. à venir**, pour permettre aux utilisateurs non seulement de voir les salles actives, mais aussi d'avoir un aperçu rapide des salles programmées dans leur réseau
* **filtres par sujets d'intérêt**, sélectionnés par l'utilisateur lors de l'onboarding, et
* **trier les salles dans votre hallway** par personnes vs clubs que vous suivez

Une décision supplémentaire en matière d'interface utilisateur a été de ne présenter que les personnes que vous suivez dans les salles de votre hallway. Cela permettrait de résoudre le problème actuel d'ambiguïté entourant les noms que les utilisateurs voient actuellement dans les cartes de salle de leur hallway.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/hallway-recording-1-.gif)
_Navigation dans le Hallway repensé_

## Expérience 2 : Aperçu de la salle

![Image](https://www.freecodecamp.org/news/content/images/2021/02/room-preview-recording-2-.gif)
_Aperçu de la salle en action, où les utilisateurs peuvent voir une liste complète des amis présents dans une salle donnée_

Actuellement dans Clubhouse, cliquer sur une salle dans un hallway vous fait immédiatement entrer dans la conversation de cette salle.

Étant donné que l'identification des amis dans une salle donnée était un facteur de décision important pour les utilisateurs rejoignant une salle, je voulais concevoir un moyen pour les utilisateurs de voir qui ils connaissent à l'intérieur avant de s'engager à rejoindre.

## Expérience 3 : Découverte

![Image](https://www.freecodecamp.org/news/content/images/2021/02/ch-explore-page-before-and-after--1-.jpg)
_L'onglet Explorer de Clubhouse actuellement (à gauche), et repensé comme une expérience de découverte immersive (à droite)_

**Actuellement, la découverte dans Clubhouse est compartimentée** : les utilisateurs vont dans l'onglet Explorer pour découvrir des personnes et des clubs par catégories et mots-clés, et ils vont dans l'onglet calendrier pour découvrir les salles actives et à venir sur tout Clubhouse.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/ch-save-room-page-after.jpg)
_Apporter une salle à votre hallway via l'onglet Calendrier de Clubhouse actuellement (à gauche), et repensé comme une simple fonction de feuille de fond (à droite)_

**La plupart des participants n'utilisaient pas réellement ces onglets pour atteindre leur objectif principal de découverte**. Au lieu de cela, ils adoptaient des solutions de contournement telles que la découverte de clubs via les profils utilisateurs, la découverte de personnes via les salles, et la découverte de salles principalement via leur hallway, limitant ainsi la portée du contenu auquel ils étaient exposés.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/discovery-filter-recording-1-.gif)
_Une expérience de découverte immersive avec des options de filtre et de tri riches_

Bien que j'ai conçu des solutions d'interface utilisateur pour rendre ces solutions de contournement plus fluides, je voulais que la page de découverte soit la destination de référence pour répondre à tous ces cas d'utilisation, permettant aux utilisateurs de rechercher des personnes, des clubs et des salles par le répertoire de sujets en croissance de Clubhouse, en plus des mots-clés.

J'ai également intégré une fonctionnalité de tri supplémentaire pour faciliter davantage la découverte.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/discovery-recording-1-.gif)
_Envoyer une salle hors réseau à votre Hallway_

Les utilisateurs voulaient également une solution simple et légère pour découvrir et accéder aux salles hors réseau.

La possibilité d'envoyer une salle du flux de découverte à votre hallway sans avoir à suivre les modérateurs de cette salle, le club correspondant, ou à la planifier dans votre calendrier personnel était le plus grand défi de ce projet, impliquant de nombreuses itérations pour sembler intuitif.

## Expérience 4 : Utilisateurs actifs

![Image](https://www.freecodecamp.org/news/content/images/2021/02/ch-active-users-before-after.jpg)
_Le flyout "Disponible pour discuter" de Clubhouse actuellement (à gauche), et repensé comme un onglet "En ligne maintenant" (à droite)_

Un cousin proche du hallway, votre écran d'utilisateurs actifs est l'endroit où se trouvent toutes vos personnes et clubs Clubhouse actuellement en ligne. **83 % des utilisateurs interrogés ont mentionné scanner cet écran pour identifier rapidement les salles dans lesquelles se trouvaient leurs amis.**

J'ai ajouté une barre de recherche très demandée pour faciliter davantage la recherche d'amis, ainsi qu'un menu déroulant de tri pour atteindre une distinction encore plus importante : qui participe activement à une salle vs. qui écoute simplement.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/active-users-recording-1-.gif)
_Découverte des utilisateurs actifs par différentes options de tri_

## Expérience 5 : Profils d'utilisateurs et de clubs

![Image](https://www.freecodecamp.org/news/content/images/2021/02/club-prof-before-after.jpg)
_Profils d'utilisateurs de Clubhouse actuellement (à gauche), et après consolidation des clubs en une seule métrique (à droite)_

**87 % des utilisateurs découvrent des clubs appropriés à suivre via les profils d'utilisateurs directement.** Il existe une hiérarchie supplémentaire au sein des clubs : les followers (qui reçoivent des notifications et voient les salles marquées par le club dans leur hallway), et les membres (qui, en plus de ce qui précède, peuvent également créer des salles marquées par le club eux-mêmes).

Dans la conception actuelle de Clubhouse, **les clubs qu'un utilisateur suit vs. les clubs dont un utilisateur est membre sont à des endroits disparates** : dans la liste des abonnements de l'utilisateur et en bas de leur profil utilisateur, respectivement. Cela était confus pour les utilisateurs souhaitant scanner tous les clubs associés à une personne particulière.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/user-club-profile-recording-1-.gif)
_Navigation dans les profils d'utilisateurs et de clubs_

En faisant des clubs associés à un utilisateur une métrique consolidée, les utilisateurs visitant ce profil **peuvent plus facilement voir à quels clubs cette personne appartient**, et les suivre immédiatement sans visiter un nouvel écran.

Au niveau du club, **pouvoir accéder aux métadonnées** telles que les salles précédemment organisées, les salles à venir et les administrateurs du club peut aider un utilisateur à obtenir un aperçu plus efficace du club.

## UI & Branding : Un cas pour l'UI sombre

En rassemblant toutes les pièces de cette expérience, il est devenu clair que l'ajout de trop d'éléments visuels perturberait la hiérarchie visuelle nécessaire pour naviguer dans l'application avec facilité.

De plus, l'expérience utilisateur typique sur Clubhouse est déjà si immersive et émotive, s'étendant souvent sur toutes les heures de la nuit — je voulais tirer parti de ce cas d'utilisation et implémenter une UI élégante qui met en valeur les quelques types de contenu de Clubhouse de manière harmonieuse.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/CH-style-tile.jpg)
_Un extrait du guide de style qui a guidé mon travail_

## Tests d'utilisabilité : À quel point la recherche et la découvrabilité sont-elles efficaces dans l'application ?

Après avoir mené mes tests d'utilisabilité, j'ai créé une carte d'affinité avec des insights, des comportements et des découvertes lors des tests. 

La plupart des utilisateurs ont navigué dans l'application avec peu ou pas d'erreurs, mais pour de nombreux participants, il y avait un point de friction principal qui perturbait un pilier clé de cette refonte :

**Il était toujours peu clair comment accéder à une salle que vous avez enregistrée depuis la page Découverte vers votre Hallway.**

## Insights des tests d'utilisabilité & Changements de priorité

Initialement, j'ai conçu pour que les salles à venir hors réseau trouvées dans l'onglet découvrir apparaissent dans le hallway en les marquants d'une étoile par l'utilisateur. Celles-ci apparaîtraient ensuite dans votre hallway de manière algorithmique, découvrables via le menu déroulant "trier par". Il y avait quelques problèmes avec cela :

* **La conception originale traitait essentiellement ces salles comme des éléments enregistrés**, ce qui priorisait involontairement (et incorrectement) ces salles par rapport aux autres salles trouvées dans votre hallway
* **Ce traitement pourrait avoir des implications plus grandes de décourager la création spontanée de salles**, ou de prioriser injustement les salles hors réseau en général
* Au-delà de cela, **intégrer un élément enregistré dans un menu déroulant de tri n'était pas intuitif** ou un endroit attendu pour trouver ce type de contenu

![Image](https://www.freecodecamp.org/news/content/images/2021/02/set-notifications-flow-recording-2-.gif)
_Configuration des notifications au niveau de la salle, du club et de l'utilisateur_

## Conclusion : Leçons apprises et où aller à partir de là

En commençant ce projet, je savais que ce serait un défi ambitieux pour une jeune designer. Ce que je ne savais pas, c'était à quel point ce défi serait complexe et global.

J'ai appris que **travailler sur un produit très médiatisé et très apprécié** s'accompagne de beaucoup de pression externe et d'émotions internes pour **bien faire (en apparence) pour tout le monde**. 

Il y a les utilisateurs expérimentés avec un attachement féroce aux structures existantes, et les nouveaux utilisateurs qui ne peuvent pas pleinement expérimenter la nuance d'une application audio en tant que prototype statique.

Ensuite, il y a la petite mais puissante équipe de Clubhouse, qui itère activement leur produit sur une base hebdomadaire, lançant potentiellement des solutions imaginatives pour les mêmes défis sur lesquels je travaille. Et même d'autres que je n'ai pas encore imaginés.

Face à un flux constant de conversations publiques sur un produit excitant qui semblait presque éthéré, je dois humblement admettre qu'il y a eu des moments où cette pression a eu raison de moi et où je me suis sentie comme une imposteur totale qui avait mordu plus que ce qu'elle ne pouvait mâcher.

Les plus grandes leçons que ce projet m'a enseignées étaient l'équilibre délicat entre la persévérance face à des défis complexes, la grâce face à l'échec perçu, et savoir quand être d'accord avec "assez bien" (pour cette itération, bien sûr).

En fin de compte, je suis extrêmement fière de ce que j'ai pu accomplir avec ce projet à ce stade de mon parcours de design. Et je me suis souvent rappelé mon mantra préféré qui m'a conduit au design de produits en premier lieu :

> _"Tout ce que je voulais, c'était un travail comme un livre si bon que je le terminerais pour le reste de ma vie."_

Le design de produits est ce travail pour moi, et je suis fière de dire que bien que ce projet (et tous mes autres) ne sera jamais entièrement terminé, j'ai insufflé autant de vie que possible — j'espère que vous l'avez apprécié !