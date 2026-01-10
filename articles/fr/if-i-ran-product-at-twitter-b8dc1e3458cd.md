---
title: Si je dirigeais le produit chez Twitter
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-01-20T22:36:00.000Z'
originalURL: https://freecodecamp.org/news/if-i-ran-product-at-twitter-b8dc1e3458cd
coverImage: https://s3.amazonaws.com/cdn-media-1.freecodecamp.org/ghost/2019/05/1_69IwUfCLRSi6l966dXRixA.png
tags:
- name: Design
  slug: design
- name: Product Management
  slug: product-management
- name: social media
  slug: social-media
- name: startup
  slug: startup
- name: Twitter
  slug: twitter
seo_title: Si je dirigeais le produit chez Twitter
seo_desc: 'By Austen Allred

  I think about Twitter a lot. Probably more than someone who doesn’t have any monetary
  incentive to do so ever should. I’m not an investor (even in the public market),
  I don’t have a relationship with anyone who works there, and I hav...'
---

Par Austen Allred

Je pense beaucoup à Twitter. Probablement plus que quelqu'un qui n'a aucun intérêt financier à le faire ne devrait jamais le faire. Je ne suis pas un investisseur (même sur le marché public), je n'ai pas de relation avec qui que ce soit qui y travaille, et je n'ai aucun pouvoir pour mettre en œuvre des changements, mais j'aime profondément le produit, sans parler de ce qu'il a fait pour ma vie.

Ce post a commencé par moi tapant quelques idées dans un avion comme une sorte d'expérience de pensée, et s'est terminé par moi réfléchissant au produit comme si c'était le mien.

J'ai abordé cela du point de vue d'un fondateur de startup : Comment une équipe d'ingénierie pourrait-elle obtenir le meilleur retour sur investissement ? Je suis sûr que Twitter est très dispersé, donc partiellement comme un défi et partiellement parce que c'est la façon dont je suis habitué à penser, j'ai essayé de réutiliser autant d'éléments et de modèles de conception existants que possible pour rendre les changements hypothétiques relativement simples.

Mais d'abord, avant de plonger, nous devons comprendre un peu où en est Twitter et pourquoi.

### Les problèmes de Twitter

Ce n'est un secret pour personne que Twitter a rencontré quelques obstacles sur la route. La croissance des utilisateurs a ralenti, le prix de l'action est [plus bas que jamais](http://techcrunch.com/2016/01/19/the-fail-whale-returns-twitter-went-down-across-many-regions-today/), Wall Street a perdu patience avec Jack en tant que PDG environ 12 heures après qu'il ait commencé, et de temps en temps j'entends parler de talents qui abandonnent le navire—pas un endroit idéal pour une entreprise publique.

Mais cela dit, je suis toujours optimiste pour Twitter. Même si les capital-risqueurs [spéculent](https://twitter.com/sama/status/688800885783199744) sur le fait que Twitter pourrait être remplacé dans trois ans, je crois qu'il s'agit d'un produit trop bon avec un réseau trop fort pour simplement disparaître. Je suis d'avis que tous ces problèmes peuvent et seront résolus.

En bref, je suis optimiste pour Twitter.

### Dissection des Tweets

Avant de plonger trop profondément dans les changements que je ferais chez Twitter, il est utile de développer une compréhension de ce que je considère comme les éléments fondamentaux d'un tweet et du fil d'actualité Twitter. Lorsque nous le faisons, voir où d'autres fonctionnalités et corrections devraient s'intégrer devient beaucoup plus facile.

Un tweet peut être divisé en quatre éléments de base :

1. Le texte du tweet. Les 140 caractères. (rouge).
2. D'où vient le tweet. Était-ce un retweet ? Vient-il de moments ? (vert).
3. Les pièces jointes. Cela inclut les photos, les vidéos, les vines, periscope, les liens, et maintenant même d'autres tweets. (bleu).
4. Les métadonnées. Qui a tweeté, l'horodatage. (noir).

![Image](https://cdn-media-1.freecodecamp.org/images/1*dYwdn3UVFCjGy0472853hw.png)

### 140 caractères (Remplacer la capture d'écran)

En raison des contraintes SMS mentionnées par Jack dans le tweet ci-dessus, l'une des grandes fonctionnalités accidentelles de Twitter est sa brièveté forcée. Je suis sûr que vous le savez, mais juste pour rappeler, chaque tweet doit être inférieur (ou égal) à 140 caractères.

Beaucoup de gens pensent que c'est génial parce que cela limite l'espace vertical que les tweets prennent dans votre fil d'actualité. Bien que ce soit vrai, les aspects positifs d'un nombre limité de caractères sont beaucoup plus profonds que les tweets ne prenant pas beaucoup de place. (Si l'espace à l'écran était le seul problème, il y aurait une solution facile—ne montrer que les 140 premiers caractères et avoir un bouton "show more" ou quelque chose d'équivalent.) Mais ce n'est pas le point.

L'aspect important des 140 caractères est la charge cognitive nécessaire pour remplir 140 caractères. Jack a un jour décrit cela en utilisant cette métaphore : Imaginez-vous devant une fresque qui sera votre toile ; quelque chose de 20 pieds de large par 8 pieds de haut. Vous êtes obligé de penser et de planifier et de savoir exactement ce que vous devriez faire avec chaque pouce d'espace blanc.

Maintenant, comparez cela à un Post-it. Avec un Post-it, vous notez simplement quelque chose et passez à autre chose.

Twitter, en ce moment, est l'équivalent d'un Post-it. C'est fantastique pour de nombreux cas d'utilisation, et cela a généré une quantité absurdement élevée de contenu provenant d'une grande variété de sources.

Mais certaines pensées ne rentrent tout simplement pas sur des Post-its. Les utilisateurs ont utilisé des captures d'écran, des tweetstorms, et même des sites externes comme twitlonger pour contourner la contrainte des 140 caractères. C'est évidemment quelque chose que Twitter devrait supporter nativement—pourquoi envoyer tout le monde ailleurs et abandonner ces clics et ces vues ?

Si rien d'autre, il semble un peu ridicule que la meilleure façon pour l'ancien PDG de Twitter de communiquer soit de prendre des captures d'écran de son application Notes iOS.

Donc, le défi est de résoudre le besoin de tweets plus longs sans éliminer les avantages des contraintes. Comment empêcher les utilisateurs de sauter à travers des cerceaux ou d'utiliser des solutions de contournement pour faire faire au produit ce qu'ils veulent ?

Maintenant que nous comprenons l'anatomie d'un tweet, c'est vraiment assez simple.

#### Le Post

Il existe plusieurs types de pièces jointes supportées nativement dans Twitter. Certaines que vous ajoutez depuis l'application (photos, vidéos et sondages), certaines sont analysées à partir du corps du tweet (liens et liens vers des tweets), et certaines proviennent d'applications externes (Vine et Periscope).

Les pièces jointes que l'on peut tweeter depuis l'application sont disponibles en bas de chaque écran "composer un Tweet".

Tout ce que Twitter doit faire pour surmonter le dilemme des 140 caractères est d'ajouter une toile plus grande comme nouveau type de pièce jointe. Je l'appellerais, simplement, le "post".

Vous pourriez le disposer ainsi (pardonnez-moi, je ne suis pas designer).

Placez un bouton à droite du bouton de sondage, et vous obtenez :

![Image](https://cdn-media-1.freecodecamp.org/images/1*AD8CxaxNo5iaPeetIeH4yg.png)

Appuyez sur ce bouton, et vous passez à :

![Image](https://cdn-media-1.freecodecamp.org/images/1*hBmCNkABUajOIv0uBcatkQ.png)
_Oui, c'est un plagiat de Medium_

C'est comme joindre une photo, sauf qu'au lieu de sélectionner une photo à joindre, vous ajoutez du texte à un post. Aussi simple qu'une capture d'écran, mais avec beaucoup plus d'utilité.

L'éditeur de texte lui-même n'a pas besoin d'être aussi sophistiqué que représenté ci-dessus ; il pourrait littéralement être du texte brut et les gens l'utiliseraient comme des fous.

La façon dont vous affichez cela dans une timeline a également déjà été résolue : c'est juste une autre forme de pièce jointe, de la même manière qu'une photo ou un tweet cité :

![Image](https://cdn-media-1.freecodecamp.org/images/1*RxLZbV1yYMof11qbiJVfWA.png)

Vous pourriez commencer avec une expérience d'édition et de lecture très simple, et finir avec quelque chose de similaire à Medium, mais construit nativement dans Twitter lui-même.

C'est là que les choses deviennent vraiment intéressantes. Au lieu d'être une plateforme de microblogging, Twitter pourrait en fait devenir... une plateforme de blogging.

#### Le Tweetstorm

Mais un post est quelque peu différent d'un tweetstorm. Un post est un long bloc de texte, alors qu'un tweetstorm est une collection de tweets en tant qu'unités individuelles ; chacun peut être retweeté, répondu et interagi dans son propre contexte. Je ne pense pas que vous voulez (ou devriez) perdre les tweetstorms en raison de l'existence d'un post. Donc, je considère les tweetstorms séparément, encore une fois comme un type de pièce jointe.

![Image](https://cdn-media-1.freecodecamp.org/images/1*phOyf1goql-u4g5vF7XbJQ.png)
_Ajouter un bouton de tweetstorm est simple_

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ld_jWeFOE0CWpfOF6IqPVg.png)
_De même pour la mise en œuvre de la fonctionnalité de composition de tweetstorm_

Vous pourriez même utiliser quelque chose de très similaire à l'écran de création de sondage, sauf qu'au lieu d'ajouter beaucoup d'options de sondage, vous ajoutez des tweets supplémentaires. (Vous utiliseriez probablement plusieurs zones de texte au lieu de champs de texte, bien sûr, mais le principe reste le même.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*gIzGwHt7k-kE6h5BhbK_Kg.png)

Et comment afficher un tweetstorm ? Afficher le premier tweet normalement, et le reste en tant que pièce jointe : "_n_ tweets supplémentaires." Appuyer dessus l'ouvrirait dans une timeline séparée qui permettrait effectivement de lire les tweets dans l'ordre approprié.

### Corriger les abonnements

Au cœur des problèmes de Twitter à Wall Street se trouve le ralentissement de la croissance. En passant quelques minutes avec des personnes qui n'utilisent pas Twitter (ou qui se sont inscrites et n'ont pas trouvé assez de valeur pour continuer), la raison est évidente.

En termes simples, Twitter augmente en valeur avec la qualité de votre fil d'actualité. Cela signifie que les personnes qui consacrent plus de temps et d'efforts à Twitter en tirent plus.

Mais constituer votre fil d'actualité est _très_ difficile, surtout pour les nouveaux utilisateurs qui n'ont rien sur quoi s'appuyer et qui n'ont jamais intentionnellement créé un fil similaire auparavant.

Pour mieux expliquer ce que cela signifie, j'aimerais prendre la liberté de regarder Twitter du point de vue de ma grand-mère.

#### Ma grand-mère

Ma grand-mère, en dehors de l'utilisation occasionnelle de mots de passe comme "p@ssw0rd", est technologiquement compétente. Elle travaillait pour Novell, elle blogue et envoie des e-mails, et connaît certainement son chemin autour d'un ordinateur.

Est-ce que ma grand-mère utilise Facebook ? Bien sûr. Utilise-t-elle Twitter ? Non.

Il est facile de dire que ce n'est "pas notre marché cible", mais à un certain point, pour justifier la capitalisation boursière de x0 milliards de dollars, Twitter doit commencer à attirer la "majorité tardive" des utilisateurs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9_eTA52XG4hx3WSFQUp0uQ.jpeg)

Ma grand-mère est une adopteuse tardive prototype. Elle a commencé à utiliser Facebook sur recommandation de l'un de ses petits-enfants il y a quelques années, acceptant sa demande d'ami comme première. Immédiatement, le reste de la famille a vu qu'elle avait rejoint, et nous avons tous commencé à l'ajouter comme amie. Elle, bien sûr, a accepté les demandes.

Avant qu'elle ne s'en rende compte, et sans faire grand-chose, elle avait recréé une grande partie de son graphe social de la vie réelle sur Facebook. Maintenant, chaque fois qu'elle se connecte à Facebook, elle voit des photos, des vidéos et des publications de sa famille. Importamment, _elle n'a même pas eu à y penser pour que cela arrive_.

Je ne suis pas sûr qu'il y ait une expérience plus addictive quelque part sur Internet.

Facebook a deux avantages majeurs sur un réseau comme Twitter :

1. Les connexions de Facebook sont bidirectionnelles (parfois je l'appelle "paresseuses" ; si je vous ajoute et que vous acceptez, vous m'avez ajouté à votre graphe social sans le savoir. Sur Twitter, chaque utilisateur doit créer son propre graphe manuellement au lieu de simplement réagir aux autres.
2. Facebook recrée un graphe social _existant_, transposant simplement "les personnes que je connais dans la vie" en "les personnes que je connais sur Facebook". La chose géniale (et difficile) à propos de l'utilisation de Twitter est que vous créez un graphe _qui n'existait pas auparavant_ à partir de zéro. Surtout pour les non-adopteurs précoces, c'est un ordre très difficile.

Le graphe unidirectionnel est à la fois ma chose préférée à propos de Twitter et la chose qui fait que la croissance de Twitter est lente. Comme on dit, Facebook est les personnes que vous connaissez, Twitter est les personnes que vous aimeriez connaître.

Le problème de Twitter est que parfois les gens ne savent pas qui ils aimerait connaître. Facebook gagne parce que tout le monde sait qui ils connaissent.

La plupart des utilisateurs de Twitter que je connais passent un temps excessif à élaguer et à découvrir qui suivre—ajoutant et supprimant constamment de leur fil d'actualité. J'irais jusqu'à dire que la valeur que l'on reçoit de l'utilisation de Twitter est directement corrélée à la quantité de temps qu'il ou elle passe à ajuster les personnes qu'il ou elle suit.

#### L'importance du graphe

Le graphe social initial est une métrique si fondamentale pour Facebook que l'équipe de croissance (maintenant légendaire) s'est concentrée _uniquement_ sur l'obtention de sept connexions pour chaque nouveau membre. Ils ont découvert que c'était le point auquel les gens resteraient. Ils savaient que vous seriez accro à ce moment-là.

Mon intuition est qu'un nombre similaire est vrai pour Twitter—à un certain niveau, créer suffisamment de graphe social de qualité rend Twitter addictif.

Le problème auquel Twitter est confronté est que créer ce graphe à partir de rien sur Twitter est d'un ordre de grandeur plus difficile que de recréer un graphe (peut-être même accidentellement) sur Facebook.

Cela est vrai pour les utilisateurs existants et les nouveaux utilisateurs, mais nous nous concentrerons d'abord sur les nouveaux utilisateurs.

#### Intégration : Démarrage du graphe

Twitter semble bien conscient de ce que les informaticiens appellent le problème du [démarrage à froid](https://en.wikipedia.org/wiki/Cold_start) : En bref, ils ne savent rien d'un nouvel utilisateur, et il est difficile de faire des prédictions (sans parler de construire un graphe social) lorsque vous ne savez rien. Ils ont essayé plusieurs façons de le résoudre pour les utilisateurs nouvellement inscrits, de l'actuel "sondage" à la précédente "page d'accueil déconnectée", mais celles-ci manquent clairement la cible.

Après avoir parcouru le processus d'intégration plusieurs fois, je crois honnêtement qu'il serait préférable qu'il n'existe pas du tout dans son état actuel. Il est suffisamment cassé pour que je ne puisse pas imaginer qu'il ne ruine pas l'expérience de quiconque s'inscrit pour la première fois.

Je suis passé par le processus d'intégration et j'ai créé un nouveau compte trois fois de plus ce matin (s'intégrer plusieurs fois sur diverses plateformes est un hobby étrange pour moi). Je l'ai fait une fois en essayant de correspondre exactement à ce que je dirais personnellement, une fois en utilisant uniquement les contacts de mon compte Gmail, et une dernière fois en utilisant uniquement mes contacts mobiles.

Cela est spécifique à moi, donc il peut être difficile de déterminer s'il y a de la valeur, mais je pense que les problèmes seront évidents.

Pour le premier tour, j'ai dit que j'aimais la tech/science dans le sondage de Twitter, et je n'ai donné aucun autre contexte ou contact. Voici qui Twitter a recommandé que je suive :

![Image](https://cdn-media-1.freecodecamp.org/images/1*_R_fxZhOZVwuVmCAoqvFMQ.png)

Inside Science & Tech, un compte dont je n'ai jamais entendu parler, mais il semble scientifique et tech, donc je suppose que cela a du sens. Ensuite TechCrunch, un compte que je ne suis pas actuellement parce que je ne suis pas un grand fan de l'écriture, mais bon, j'ai dit tech, voici TechCrunch.

Il comprenait également plusieurs dirigeants de l'Église LDS. Je ne sais pas d'où cela vient, mais je suis dans l'Utah, donc cela pourrait être quelque chose de basé sur la localisation. Peu importe. J'ai simplement suivi tout le monde que Twitter a recommandé.

À ma surprise, lorsque j'ai regardé le fil d'actualité que cette intégration a peuplé, il était à 99% CNN, ESPN et Utah Jazz. Apparemment, plus bas dans la liste se trouvaient des comptes très non-techniques auxquels je n'ai pas prêté attention (je suppose que beaucoup d'utilisateurs ne le feraient pas non plus), et ces énormes comptes, tweettant constamment et complètement sans rapport, dominaient complètement mon fil d'actualité.

Si j'avais été un utilisateur pour la première fois, je serais parti et ne serais jamais revenu. Mais peut-être que c'était un coup de chance.

J'ai ensuite essayé avec un nouveau compte, en important uniquement ma liste de contacts Gmail. Voici qui Twitter a recommandé que je suive en fonction de mes e-mails :

![Image](https://cdn-media-1.freecodecamp.org/images/1*CNFhWxOuo5_26V6na0mnhw.png)

Peut-être que j'ai un e-mail de la Mormon Newsroom quelque part, mais ils ne sont certainement pas l'un de mes "contacts". Je ne sais pas comment Drake est arrivé là, ou la Maison Blanche, mais cela est à nouveau clairement cassé. Mon fil d'actualité était un fouillis de marques, dont la plupart essayaient de promouvoir du contenu.

Mais peut-être que c'est parce que je suis sur desktop et que personne n'utilise plus desktop ; essayons sur mobile. Cette fois, je vais utiliser uniquement ma liste de contacts mobiles.

À ma surprise, Twitter a à nouveau injecté un grand nombre d'autres comptes pour moi. De Barack Obama et Bill Clinton à des sites d'actualités et toutes sortes de célébrités aléatoires, entrecoupés des personnes que je connais et qui m'intéressent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kL08qv_C7voZP2grGB1cZw.png)

Lorsque je suis arrivé à mon écran d'accueil, les tweets provenaient de (dans cet ordre) :

Time, MarketWatch, Entrepreneur, Time, ESPN, CNN, The Economist, Forbes, Wall Street Journal.

J'ai dû faire défiler _57_ tweets avant de voir quelque chose de quelqu'un que je connaissais.

#### Je ne suis pas venu ici pour suivre des marques

Peut-être que c'est juste moi, mais je parierais que la première étape pour résoudre le problème du graphe social est d'arrêter de fétichiser les comptes populaires et de marque—surtout ceux qui tweetent sept fois par heure. Il semble que Twitter pousse ceux-ci à travers le board. Peut-être que je suis un utilisateur atypique, mais à mon avis, ce sont certains des pires comptes à suivre : Ils tweetent principalement des communiqués de presse et des liens vers des articles.

#### Comment je trouve des gens à suivre

1. J'aime trouver des gens qui tweetent les mêmes liens que moi. Cela signifie qu'en général, ils sont intéressés par les mêmes sujets ou lisent les mêmes choses. Cela devient presque un Nuzzel inversé.
2. Parfois, je passe en revue les tweets que j'ai retweetés et je suis tout le monde qui les a également retweetés.
3. Occasionnellement, j'utilise un outil comme [Electoralhq](https://www.electoralhq.com/) pour créer une liste de toutes les personnes qu'une autre personne suit, recréant essentiellement le fil d'actualité de cette personne. Je peux ensuite utiliser le fil d'actualité de cette personne de temps en temps pour trouver de nouvelles personnes. (Cela était en fait une fonctionnalité de Twitter.)
4. J'adore créer des listes de personnes qui sont suivies par les personnes que je suis, mais qui ne sont pas suivies par moi. J'ai trouvé certains de mes comptes préférés de cette manière.

Comme vous pouvez le voir, ce ne sont pas des choses que la plupart des utilisateurs feraient, mais elles ont tellement augmenté la valeur de Twitter pour moi que je pense que ce serait génial de voir ces outils se généraliser. (J'ai en fait joué avec l'idée de construire certains d'entre eux dans le passé, mais la limitation des appels API l'a rendu impossible.)

Cela est relativement trivial, mais étant donné que la construction d'un graphe social est l'aspect le plus important de Twitter, il serait agréable d'avoir quelques outils supplémentaires pour pouvoir trouver des gens.

### Suivre plus que des gens

Une façon potentiellement encore plus évidente de résoudre le problème du graphe social est de me laisser suivre plus que des gens.

Et si vous pouviez suivre des _événements_ ?

Et si vous pouviez suivre des _sujets_ ?

C'est clairement ce que Twitter a essayé de résoudre avec Moments, mais Moments ne résout pas le problème.

#### Corriger Moments

Le problème avec Moments n'est pas le design ou la position du bouton ou la disposition ; tout cela a été très bien exécuté (chapeau bas à l'équipe Moments pour cela).

Le problème avec Moments est _le contenu_. Moments a essentiellement recréé une portion de la page d'accueil de Yahoo à l'intérieur de Twitter.

Moi, et la plupart des gens que je connais qui utilisent Twitter, allons sur Twitter pour trouver les choses qui _ne sont pas_ sur la page d'accueil de Yahoo.

Ce n'est pas nécessairement la faute de l'équipe éditoriale de Moments non plus ; le problème est que l'équipe éditoriale est chargée d'une mission impossible : Trouver du contenu que tous les utilisateurs de Twitter voudront cliquer. Croyez-moi, cela n'arrivera jamais.

Le problème que Moments s'est fixé de résoudre est que _la curation est difficile_. Un événement se produit, et bien sûr, vous pourriez suivre le hashtag, mais il y a beaucoup trop de firehose à boire. Je serais prêt à parier que le processus de réflexion était quelque chose comme ceci :

> "Il est vraiment difficile pour les gens de curater leurs fils d'actualité suffisamment pour rendre Twitter précieux pendant les grands événements comme [Ferguson]. Comment pouvons-nous résoudre cela ?"

> "Eh bien, engageons simplement des gens pour trouver les meilleures choses et le faire pour eux."

En liant cela à quelques remue-méninges sur la façon d'obtenir ces tweets dans un fil d'actualité, Twitter Moments est né. Je pense qu'ils étaient sur la bonne voie.

Mais je pense aussi que Twitter a manqué une _énorme_ opportunité, spécifiquement parce que cela ne se met pas très bien à l'échelle.

Il peut y avoir des gens qui sont intéressés par les sujets ci-dessus, mais je ne sais pas qui ils sont. Et je parie que Twitter admettrait qu'ils ne le savent pas non plus.

L'opportunité manquée, à mon avis, est qu'il _y a_ des gens qui sont prêts à curater pour les autres sur Twitter, même sur une base tweet par tweet.

Peut-être que ce n'est que 1%. Peut-être que ce n'est que 10%. Mais pourquoi rester là et curater des tweets sur 10 sujets lorsque vous pourriez l'ouvrir et permettre à _tout le monde_ de curater des tweets sur _n'importe quel_ sujet ?

Faire cela l'ouvrirait à tout le monde, et laisserait chaque événement jamais couvert par quelqu'un. Cela pourrait toujours être intégrable et partageable ; vous pourriez même "suivre" un moment et laisser ces liens peupler votre timeline, mais ce serait sur _chaque_ sujet.

#### Ouvrir Moments

Pour comprendre comment Moments fonctionne, décomposons-le à nouveau en morceaux anatomiques.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rPEzeNgGWbGlgGXIEdCX9Q.png)

C'est en fait remarquablement simple. Je n'ai jamais vu le backend de Moments, mais j'imagine qu'il s'agit de quatre champs "titre" puis d'une série de champs pour déposer des liens vers des tweets.

Je sais pour un fait que vous pouvez obtenir des gens ordinaires pour remplir ces champs, car nous avons utilisé presque exactement les mêmes champs chez Grasswire depuis près de deux ans (sauf que nous avons "tag" au lieu de "topic", et "links" au lieu de "tweets").

Alors pourquoi ne pas l'ouvrir ? Exposez le backend, permettez-moi de créer des moments qui vivront sur twitter.com/austenallred/moments, et affichez-les de la même manière. Le travail difficile est fait.

Ensuite, la question se pose de "Moments Discovery".

Une analyse assez rudimentaire de mes tweets par Klout (je sais, je sais) révèle les sujets qui m'intéressent :

![Image](https://cdn-media-1.freecodecamp.org/images/1*_mhBuiBTloSuokQ_NJQ6kA.png)

C'est assez précis ; avec quelques exceptions, j'adorerais voir des Moments sur n'importe lequel de ces sujets. Twitter a toutes ces données ; il sait de quoi je tweete, il faudrait un peu de finesse mais il n'y a aucune raison pour que Twitter ne puisse pas me montrer des Moments sur ces choses. Faire cela rendrait Moments incroyablement précieux pour moi.

Si Moments avait du contenu sur ces choses, je vérifierais probablement l'onglet Moments plusieurs fois par jour. Les gens les créeraient et les intégreraient, les entreprises de presse créeraient des histoires de cette manière ; vous auriez presque un Storify plus facile à utiliser intégré directement dans le produit, mais surtout, il serait _scalable_ et _personnalisé_.

Mais que se passe-t-il si ce que je veux suivre n'est pas un _événement_ ?

#### Collections

Moments est orienté vers les événements avec un temps de début et de fin particulier. Mais qu'en est-il des sujets ?

Les Collections Twitter existent techniquement, mais elles le font dans un format tel que je ne savais même pas qu'elles étaient une chose jusqu'il y a quelques jours. Collections est une très, très bonne idée. Mais il y a un couple de problèmes :

1. Je dois utiliser un outil spécial appelé "curator" pour les créer.
2. Voir une collection est difficile, car elle est quelque peu cachée.

Ces deux problèmes ont des solutions assez évidentes.

Créer une collection devrait être aussi simple que créer une liste, sauf que cette fois, au lieu de rassembler des _personnes_, nous rassemblons des _tweets individuels_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gmgJyuBUcmXCuTNWo7wE5Q.png)

Assez simple : ajoutez un autre élément de liste au menu déroulant de la photo de profil, et tout a une place.

Ce n'est pas difficile de comprendre comment on devrait pouvoir ajouter un tweet à une collection, non plus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pU3THrOdgzCV2AX85mPKAQ.png)

Ces petits détails sont importants, car ainsi il n'y a pas besoin de construire un produit séparé avec une fonctionnalité de recherche, de découverte, une nouvelle façon d'afficher les timelines, etc. Si c'est bien fait, ce serait en fait plus simple de construire de nouvelles fonctionnalités dans le produit existant. Quelques changements d'API, quelques changements d'UI, et vous êtes prêt à partir. (Bien sûr, venant d'un milieu de startup, je suis sûr que je sous-estime la difficulté de cela, mais théoriquement, cela ne devrait pas être complexe.)

Mais ce qui rend les collections _vraiment_ intéressantes pour moi, c'est comment vous pourriez les suivre.

Ce n'est un secret pour personne que la grande majorité de l'utilisation de Twitter se fait dans le fil d'actualité d'un utilisateur. La raison pour laquelle les listes n'ont pas décollé est que les gens utilisent simplement leur fil d'actualité. Si j'étais la personne toute-puissante sur le produit chez Twitter, je permettrais aux gens de suivre une collection, injectant par la suite tous les tweets qui y sont ajoutés dans mon fil d'actualité. (Vérifier les collisions et les doublons serait plus difficile, mais nous allons ignorer cela pour l'instant).

À quoi cela ressemblerait-il lorsqu'il est injecté dans mon fil ? De la même manière que n'importe quel autre tweet, sauf qu'en revenant à notre dissection des tweets, nous aurions maintenant "de @user/nom-de-la-collection" en vert au lieu de "retweeté par [nom complet]". (Je le déposerai à nouveau ci-dessous pour faciliter les choses.) Ajoutez une sorte d'icône Collections, et vous venez de rendre possible le suivi d'un sujet (ou événement) curaté par un autre utilisateur de manière continue.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dYwdn3UVFCjGy0472853hw.png)

Implémenté de cette manière, je peux laisser quelqu'un d'autre faire la curation pour moi sur une base tweet par tweet. Il n'y a vraiment aucun moyen sur Twitter en ce moment de suivre une _chose_. Vous pouvez suivre des _personnes_ qui sont susceptibles de tweeter sur une _chose_, mais elles peuvent tweeter sur ce qu'elles veulent, et vous êtes coincé avec cela.

À un certain niveau, suivre des sujets serait en fait beaucoup plus facile que de suivre des personnes. Les curateurs seraient récompensés en sachant que leur goût est apprécié par _n_ personnes, et les nouveaux utilisateurs pourraient sauter directement dans ce qui les intéresse de manière thématique au lieu d'avoir à trier les personnes qui les intéressent.

Une fois que cela devient plus établi, vous pouvez créer des "collections de groupe" où un utilisateur peut inviter d'autres personnes à ajouter à une collection avec lui ou elle. Mais c'est le mode expert, et nous sommes encore en mode amateur.

### Le Firehose

Probablement la meilleure façon de décrire ce que je ferais si j'étais responsable du produit chez Twitter est de résoudre le problème du "firehose". Le problème de Twitter est qu'il y a _trop de bonnes choses_. C'est un rêve fou pour la grande majorité des startups et des produits, mais ce n'est pas le monde dans lequel vit Twitter.

Le plus gros problème de Twitter dans l'ensemble est la découverte, en raison des graphes sociaux créés manuellement, et je pense que cela contribuerait à résoudre ce problème.

Encore une fois, ce ne sont que des pensées aléatoires, principalement écrites lors d'un long vol en avion, et je n'ai ni information privilégiée ni pouvoir pour mettre en œuvre l'un de ces changements, donc lorsque tout était dit et fait, ce n'était qu'un long remue-méninges pour un produit que j'aime.

Pour résumer :

* Ajouter un nouveau type de pièce jointe qui est un post texte
* Intégration native des tweetstorms
* Enlever les scories de l'intégration des nouveaux utilisateurs
* Ouvrir les moments
* Créer des "collections" suivables

À Twitter en 2016.