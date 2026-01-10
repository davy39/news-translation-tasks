---
title: Mes amis détestent SoundCloud iOS alors je l'ai redessiné pour eux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-22T02:35:54.000Z'
originalURL: https://freecodecamp.org/news/my-friends-hate-soundcloud-ios-so-i-redesigned-it-for-them-d3038cdd020b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pGIr42haQHsmxo9BXZl3JA.png
tags:
- name: Design
  slug: design
- name: music
  slug: music
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: Mes amis détestent SoundCloud iOS alors je l'ai redessiné pour eux
seo_desc: 'By kelleytmnguyen

  What started out as a casual conversation with my friends turned into a serious
  exploration. This was partially because I love SoundCloud, and partially because
  I needed to challenge myself in order to move forward in my career.

  I s...'
---

Par kelleytmnguyen

Ce qui a commencé comme une conversation décontractée avec mes amis s'est transformé en une exploration sérieuse. Cela était partiellement dû à mon amour pour SoundCloud, et partiellement parce que j'avais besoin de me challenger afin d'avancer dans ma carrière.

J'ai commencé à utiliser SoundCloud de manière obsessionnelle en 2013, et depuis, j'ai commencé à utiliser d'autres applications de streaming. SoundCloud est incroyable. Chaque fois que je parcours sa communauté, je peux m'attendre à découvrir tant de nouveaux talents.

J'ai donc entrepris de redessiner l'application iOS de SoundCloud à partir de zéro, de la manière dont mes amis et moi aimerions qu'elle soit.

### Partie I — Partir de zéro

#### Itération I

Au cours des six derniers mois, je n'ai pas pu lutter contre le sentiment que SoundCloud avait changé depuis qu'ils ont lancé leur plateforme mobile. Et pas en bien. Lorsque je demandais à mes amis ce qu'ils en pensaient, ils s'énervaient. Nous débattions de ce que nous aimions encore et de ce qui n'allait pas ; j'avais des conversations approfondies avec mes chauffeurs Lyft ; je glissais discrètement des questions sur SoundCloud dans des discussions aléatoires.

Et voilà, _j'ai découvert que la plupart d'entre nous évitaient de l'utiliser._

Alors, je suis devenu de plus en plus curieux… ?

![Image](https://cdn-media-1.freecodecamp.org/images/9BQ24j7g766fg6HShFYdr-zgjqdwiLy3uemj)
_Fry de Futurama_

Qu'est-ce qui rendait les autres applications de streaming mobile plus fortes ou plus faibles que SoundCloud ? Quels étaient les détails de notre mécontentement ? Qu'est-ce qui devait changer ? Pour obtenir des informations, j'ai élargi mon expérience de streaming et j'ai commencé à utiliser Spotify et Apple Music, en comparant et contrastant leurs forces, faiblesses et modèles. Quels éléments et termes étaient universels sur ces plateformes de streaming ?

![Image](https://cdn-media-1.freecodecamp.org/images/n9P-Tv9rdUfHrAjOaAUwtsx2-oYUyt9dgmzZ)

![Image](https://cdn-media-1.freecodecamp.org/images/f7IS7IxlKgsLZEiizsphiaVUHx3Nbf5whKBX)

![Image](https://cdn-media-1.freecodecamp.org/images/3WkO4I0VMNKo66NLaHE7XKUSiuN2yJLEMoa2)

Après avoir mentalement compilé une liste de suggestions et d'améliorations pour SoundCloud (à partir de conversations informelles, etc.), j'ai réalisé l'inévitable.

> _Si je voulais redessiner SoundCloud, je devais partir de zéro._

Je devais commencer à partir de zéro.

#### Situation

En 2016, le marché mondial de la musique enregistrée a augmenté de 5,9 % grâce au streaming ([IFPI Facts and Stats 2016](http://www.ifpi.org/facts-and-stats.php)). 59 % des revenus numériques cette même année provenaient du streaming seul. En tant que l'une des plateformes de streaming les plus populaires, SoundCloud met fortement l'accent sur leur communauté, enregistrant 847 millions de connexions électroniques établies en 2015. Elle possède l'une des plus grandes communautés numériques de musique électronique, estimée à plus de 10 millions.

![Image](https://cdn-media-1.freecodecamp.org/images/ky8PKlQIeHaKsmvDL4C4q-sPilwzMBUq-Gk4)
_[https://soundcloud.com/for/electronic](https://soundcloud.com/for/electronic" rel="noopener" target="_blank" title=")_

#### **Hypothèses**

SoundCloud est devenu un concurrent du streaming musical en 2016 après le lancement de leur service d'abonnement SoundCloud Go. La presse a exprimé des critiques moins que satisfaites lors de sa sortie ; SoundCloud a ensuite répondu en lançant un nouveau niveau appelé SoundCloud Go+ en 2017. Alors que la [plateforme lutte pour gagner des utilisateurs face à Spotify Premium](https://about.crunchbase.com/news/streaming-wars-continue-soundcloud-balance/?utm_source=cb_daily&utm_medium=email&utm_campaign=20170518&utm_content=intro&utm_term=content&send_email=kelleytmnguyen@gmail.com), j'ai commencé à formuler des hypothèses.

> 1. Le streaming et la découverte de musique sont des activités très sociales  
>  2. Créer des playlists est crucial pour l'expérience d'écoute  
>  3. Découvrir de la nouvelle musique doit être pratique

#### Recherche de marché I

À l'échelle mondiale, les plus grandes parts de musique électronique sont détenues en Europe et en Asie, et les flux les plus élevés de musique électronique sont en Amérique, en Grande-Bretagne, au Danemark et au Mexique. ([IMS Summit Business Report 2017](http://www.internationalmusicsummit.com/wp-content/uploads/2017/05/IMS-Business-Report-2017-vFinal2.pdf))

![Image](https://cdn-media-1.freecodecamp.org/images/vRNW1hs96uWqCDp2Waq8KpfhDNY4pAsCyPJw)
_[Qui est l'auditeur de musique électronique ?](http://www.nielsen.com/us/en/insights/news/2014/who-is-the-electronic-music-listener.html" rel="noopener" target="_blank" title=") (Nielsen)_

> « Les milléniaux sont 40 % plus susceptibles d'assister à un événement en club aux États-Unis, et totalisent 2 milliards à l'échelle mondiale » — International Music Summit Business Report 2017

#### **Recherche I**

_Parties prenantes_

J'ai divisé les parties prenantes en deux catégories : les amateurs et les professionnels. Pour répondre à un besoin que tout le monde partageait, j'ai examiné leur rôle global.

> Chaque partie prenante était finalement un auditeur.

En effet, j'ai axé mes questions autour des habitudes des auditeurs et des streamers. Pour cette série, j'ai recueilli des réponses de 23 participants âgés de 18 à 28 ans. 82 % étaient des hommes et 80 % étaient à l'université.

![Image](https://cdn-media-1.freecodecamp.org/images/blasAotnuWo8cXB2ngt8vbmVooOYMghId1Ia)
_Parties prenantes_

J'ai découvert que mes participants étaient plus susceptibles de voir à plusieurs reprises des pistes republiées dans leur fil d'actualité par le même groupe d'artistes. Ils se retrouvaient dans une boucle de rétroaction, où les mêmes pistes circulaient parmi les mêmes utilisateurs. Les utilisateurs étaient moins susceptibles de trouver de la nouvelle musique et étaient influencés par des fonctionnalités telles que le nombre de "j'aime" et de "reposts". Certains d'entre eux ont déclaré qu'ils feraient défiler 3 ou 5 pistes sur leur fil d'actualité, perdraient intérêt et passeraient à autre chose.

**De nouvelles questions ont commencé à se former.** À quel point la connexion d'un utilisateur à la communauté musicale en ligne est-elle importante ? À quelle fréquence les auditeurs écoutent-ils la musique de leurs amis ? Comment sont-ils influencés par les pistes republiées et le nombre de "j'aime" ?

_Entretiens_

J'ai mené 5 entretiens, chacun durant environ 30 minutes. J'ai posé plus de 20 questions, visant à découvrir ce que chaque individu croyait être les forces et les faiblesses de SoundCloud iOS. Mes entretiens ont révélé un manque de confiance dans les recommandations de SoundCloud en tant que plateforme de découverte. SoundCloud n'était pas considéré comme aussi poli que Spotify et Apple Music. **Plutôt, il était vu comme un portfolio pour les artistes en développement au lieu d'une discographie professionnelle.** Tous mes résultats sont compilés [ici](https://docs.google.com/document/d/1Knf2hzWY4bebUQhTu35HNFuVnH2RcPb9meRNNi_m4uM/edit#heading=h.f0z79jq5lysy).

![Image](https://cdn-media-1.freecodecamp.org/images/NYz7nLd-sXsAAOwYinjstlO3lAwsGVmN0Zhu)

À partir des données que j'ai recueillies, j'ai pu brosser un meilleur tableau. J'ai illustré le type de comportements pour lesquels je concevrais avec [des personas et des scénarios](https://files.persona.co/44294/sc-pov-personas.pdf). Le premier scénario est une histoire sur une amie dont l'expérience d'écoute l'a incitée à partager une piste avec une amie. Le second raconte l'histoire d'un jeune adulte actif qui souhaite avoir une nouvelle expérience d'écoute en conduisant au travail dans les embouteillages.

![Image](https://cdn-media-1.freecodecamp.org/images/jvIjVk-VUthDKGpJTe6KY5qV0TLPIadO-uv1)
_Persona Principal_

![Image](https://cdn-media-1.freecodecamp.org/images/ojrCJXO9ACc18f8n-3wkARphJgzOue6xg-5w)

![Image](https://cdn-media-1.freecodecamp.org/images/-9OSPqjvcHnlQqV128rJerN-ay6g0-UotAt5)

**100 % des participants à l'enquête et aux entretiens écoutaient des variations de musique électronique.** Cela incluait une large gamme de sous-genres, y compris le trap, l'electronica et la pop. 60 % des personnes interrogées ont déclaré qu'elles écoutaient des podcasts, des sets ou des mixes, qui pouvaient durer entre 30 minutes et 3 heures. Leurs commentaires ont soutenu ma compréhension de SoundCloud comme une plateforme pour la musique électronique, qu'elle soit sous forme de production de rap ou de sous-genres.

#### Pour revisiter mes hypothèses :

> 1. Mes entretiens ont finalement montré que le streaming et la découverte de musique ne sont pas des activités fortement sociales, mais des explorations personnelles. Le goût individuel est extrêmement unique.

> 2. Tout le monde ne crée pas de playlists car cela demande beaucoup plus d'efforts que ce que l'utilisateur moyen peut se permettre.

> 3. La solution ? Donner aux auditeurs la musique qu'ils ne savaient pas qu'ils voulaient. Ou en d'autres termes, les humains sont paresseux, alors nous devons faire tout le travail.

Plus important encore, la communauté et le dépôt de musique électronique de SoundCloud doivent être à la surface. Cela signifierait **curater le contenu** (sets enregistrés, influenceurs, mixes en direct), et **organiser les bibliothèques** de musique afin d'**engager les habitudes** de la communauté de musique électronique. Pour répondre aux besoins de mes sujets, j'ai fait les propositions suivantes :

#### Propositions

> 1. Une nouvelle page dédiée aux Événements et Mixes

> 2. Organiser et catégoriser la collection de musique sauvegardée

> 3. Une nouvelle page dédiée aux Curateurs

> 4. Un module séparé pour les pistes republiées populaires

> 5. Se concentrer uniquement sur la communauté de musique électronique et de danse

### Prototypage

#### Flux utilisateur

Après avoir étudié les applications de streaming musical courantes et digéré les chemins mobiles de SoundCloud, j'ai visualisé grossièrement ses fonctionnalités les plus importantes. Ces fonctionnalités ont guidé les [flux utilisateur et chemins](https://files.persona.co/44294/sc-infoarch-sitemaps.pdf) que je croyais que les utilisateurs suivraient le plus probablement lors de l'utilisation de SoundCloud.

#### Fidélité basse

En prenant les informations organisées à travers les sitemaps et les flux utilisateur, j'ai créé des wireframes de basse fidélité pour le Profil ou l'Accueil, la Bibliothèque et la Découverte en utilisant des prototypes papier. Je suis passé à des [wireframes numériques](https://files.persona.co/44294/_Flows-ilovepdf-compressed.pdf) par la suite et j'ai dessiné des [cartes de wireframes](https://files.persona.co/44294/sc_Wireframe_Flows.pdf) de base pour regrouper les écrans ensemble.

![Image](https://cdn-media-1.freecodecamp.org/images/7cqLGhC8DxKxJiJoeTYt7HKkMAHcBjeBENqA)

![Image](https://cdn-media-1.freecodecamp.org/images/-BH85pzoax9EpfIZs0atxK6DJehO0mcxypPS)

#### Fidélité moyenne

À partir de la basse fidélité, j'ai pris note de la signification et du but de chaque élément et page. Encore une fois, les éléments suivants sont organisés par les principales branches de l'application : Profil ou Accueil, Découverte et Bibliothèque.

![Image](https://cdn-media-1.freecodecamp.org/images/CkuW3ywdUc-0ahlBrU2A5RsQFpAP6ABM2GGT)

![Image](https://cdn-media-1.freecodecamp.org/images/JakjIw0q1to54VNpYsR-TjoQvAunxQ6GdJIU)

![Image](https://cdn-media-1.freecodecamp.org/images/dDdJlqNz23U2smXf95FoP8-Fn0PcJQ2IfPWi)

**Événements & Mixes**

![Image](https://cdn-media-1.freecodecamp.org/images/tUnDd7ZG-bMwEsMMqbyMKz5sKOuUP5C8gYyN)

_Découvrir > Mixes_ >

1. En vedette — collaborateurs, artistes suggérés, etc.

2. Événements — festivals, performances

3. Localisation — grandes villes et scènes

4. Podcasts — résidents, mixes quotidiens

**Curateurs**

_Découvrir > Mixes_ >

1. Maisons de disques — distributeurs professionnels

2. Auto-produits — chaînes YouTube

3. Collectifs musicaux — groupes, collaborateurs

Presse — magazines et RP présentant de la musique

![Image](https://cdn-media-1.freecodecamp.org/images/5ejrGDxnv5h54tacFw-PutIOWyCA8CydOTa9)

![Image](https://cdn-media-1.freecodecamp.org/images/9Fk7N2h1gu2TAq7Pua0uR3K7orP-HcgQU6GM)

![Image](https://cdn-media-1.freecodecamp.org/images/iy7eMfhZ6vzFEv7QuyEdyfd4lQFxdAxO97Wb)

#### Haute fidélité

[Prototype en ligne](https://xd.adobe.com/view/145e74af-77aa-42c7-8951-5d683f98d40a/)

Faites-moi savoir vos pensées sur la façon dont l'infrastructure fonctionne pour vous, ce qui pourrait être mieux dans l'interface, et votre expérience globale.

**La partie I** était ma première tentative sur Adobe XD, et je suis impressionné par la facilité d'utilisation de la fonctionnalité de prototypage. La partie I couvre également les premières découvertes de recherche et la première maquettes interactives. Pour **la partie II**, je me concentrerai sur la conception visuelle et les micro-interactions en utilisant Sketch et Principle, en lissant les bords du premier modèle pour une meilleure deuxième itération.

### Partie II — Faire un pas en arrière

#### Itération II

**Merci d'avoir lu jusqu'ici !** Les derniers morceaux de ce projet m'ont rendu plus enthousiaste à propos de la conception d'interaction dans son ensemble. J'ai trouvé ces gifs pour vous montrer comment je me sens à propos des progrès ?

![Image](https://cdn-media-1.freecodecamp.org/images/561gyDyTr0gLeUdjk2pkxQW7d2zoYVFXpE8S)

![Image](https://cdn-media-1.freecodecamp.org/images/hnm75Ubkf4hcyQId3H9f4Oq4uFwuS10sOIY7)
_G : Sailor Moon, D : Finn de Adventure Time_

Avant de passer à la deuxième moitié de ce projet, j'ai examiné comment SoundCloud a changé au cours des derniers mois. J'ai revu les données que j'avais recueillies quelques mois plus tôt et j'ai parcouru l'activité actuelle de SoundCloud [ici](https://soundcloud.com/charts/top). Des artistes comme _Lil Uzi Vert_, _Post Malone_ et _Travis Scott_ ont été en tête des classements de SoundCloud, rendant le hip-hop aussi populaire que (sinon plus que) l'électronique. Après avoir basé ce projet sur des sujets qui écoutaient principalement de la musique électronique, j'ai pensé que je devais pivoter dans une toute nouvelle direction.

> J'ai fait un pas en arrière.

Si la base de SoundCloud avait changé, je savais que j'avais besoin de plus de preuves. Je m'étais concentré sur un petit échantillon dans mon propre réseau et j'avais besoin de m'étendre. Pourquoi ne pas recueillir plus de données sur le streaming musical ?

#### Recherche de marché II

Compilé à travers une série d'articles, de communiqués de presse et de recherches de [NYTimes](https://www.nytimes.com/2015/02/26/arts/music/flume-rises-in-the-edm-world.html), [Forbes](https://www.forbes.com/sites/bobbyowsinski/2016/06/16/twitter-invests-soundcloud-but-why/#e1f34c72051e), [WMagazine](https://www.wmagazine.com/story/soundcloud-rappers-lil-uzi-vert-lil-yachty), et plus encore, j'ai réalisé que la tendance pour le hip-hop à travers SoundCloud est apparue au cours des deux dernières années. Les trois premiers artistes sur SoundCloud en 2015 étaient **Drake**, **Major Lazer** et **G-Eazy** ([Forbes 2015](https://www.forbes.com/sites/hughmcintyre/2015/08/23/soundclouds-ten-most-played-artists-this-year-tell-a-lot-about-its-users/2/#7b1192be3990)). En 2016, l'album le plus populaire était _Coloring Book_ de **Chance the Rapper**, la piste la plus favorite _Panda_ de **Desiigner**, et le plus suivi : **Lil Uzi Vert**.

![Image](https://cdn-media-1.freecodecamp.org/images/nRvZ-zluuzHuDwjG1Sq0vfdLu6xVeo1iSmHE)
_[Aperçu de SoundCloud 2016](https://blog.soundcloud.com/2017/01/19/throwbackto2016/" rel="noopener" target="_blank" title=")_

#### Recherche II

J'ai fait une autre enquête plus concise et axée sur les données quantitatives. Composée de quatre questions à choix multiples, j'ai recueilli des réponses de 167 participants.

![Image](https://cdn-media-1.freecodecamp.org/images/OmAGdb8RZCYXzzbU3mpNM2lVlGpR4i14dgZQ)
_Q1 : Quel est votre âge ?_

![Image](https://cdn-media-1.freecodecamp.org/images/tHys7jUHi4BBnA76ViKd3SeIiE2Lx7XBmspW)
_Q2 : Quel(s) genre(s) écoutez-vous le plus ?_

![Image](https://cdn-media-1.freecodecamp.org/images/cPRMUHsYigkBxzVLXOR7uPaOIiMaZvef8J38)
_Q3 : Quelle(s) application(s) de streaming utilisez-vous sur votre téléphone ?_

![Image](https://cdn-media-1.freecodecamp.org/images/xsVvvSS9Iugb7AcCUnIo9lzQGwjMv9dKjy7K)
_Q4 : À quoi utilisez-vous votre/vos application(s) de streaming ?_

Voici les résultats : **La musique électronique et le hip-hop** sont ex æquo pour le genre le plus écouté. La plupart des streamers de musique avaient entre 16 et 27 ans, avec une moyenne d'environ **21 ans**. **Spotify mène** contre SoundCloud en tant que plateforme de streaming mobile préférée. **Le streaming** était considéré comme l'activité la plus importante, puis la découverte, puis la création de playlists.

#### Pour revisiter mes propositions :

> 1. Organiser et catégoriser la collection de musique sauvegardée

> 2. Un module séparé pour les pistes republiées populaires

> 3. Se concentrer sur la communauté de musique électronique, de danse et de hip-hop

> 4. Structurer les pages de Découverte pour s'adapter aux genres et à la communauté

La plupart des résultats de la deuxième série reflétaient les données que j'avais recueillies quelques mois plus tôt, mais j'ai appris quelque chose de nouveau :

> **L'un des points forts de SoundCloud en tant que plateforme est sa polyvalence et sa capacité à évoluer avec son public.**

Pour s'adapter à sa communauté, la conception doit être impartiale, favoriser tous les genres de musique et s'appuyer sur les caractéristiques de la marque actuelle de SoundCloud : sobre et neutre.

### Icônes

J'ai essayé de créer des icônes pour avoir une idée de la perfection des pixels. Bien que ce soit ma première fois et qu'il y ait beaucoup de place pour l'amélioration, j'ai pu voir comment mon attention aux détails pouvait être poussée.

![Image](https://cdn-media-1.freecodecamp.org/images/5-oAzMkMCpDE0DGNDTPxQfC5UIocKygeWUX5)

![Image](https://cdn-media-1.freecodecamp.org/images/EisEtfNUaqTym322sERowBgOA6A3ZQTCOu0v)

### Conception visuelle et micro-interactions

#### **Accueil**

Pour SoundCloud iOS, le but de l'Accueil (et son seul but) est de montrer l'activité des personnes que vous suivez. Tous les posts sont déversés dans le fil d'actualité dans l'ordre chronologique. Les éléments les plus saillants du fil sont l'artwork de chaque post et le nombre de "j'aime" et de "reposts".

![Image](https://cdn-media-1.freecodecamp.org/images/yyy1QXgnv9ESjQKVe3JEDhRMFqGJz2TBdgud)
_SoundCloud vs Itération 2 : Accueil_

**Populaire dans votre fil** permet aux auditeurs de voir l'activité des utilisateurs qu'ils suivent. La première piste de ce module montre que 35 personnes que Mary suit ont aimé un post de Paramore. Le module compile l'activité en une seule notification et tient compte des doublons. Si les personnes que Mary suit reflètent des facettes de ses propres goûts musicaux, Mary pourrait aimer la piste aussi.

![Image](https://cdn-media-1.freecodecamp.org/images/aA-hilb9MiElkzGppTE5MPUPtIgTjdm0KfiL)

![Image](https://cdn-media-1.freecodecamp.org/images/UMxPI--66qWeuaLf5kaqW6pm2nd5yV0EG1cn)
_Itération 2 : Populaire dans votre fil_

Disons qu'un post a moins de 10 "j'aime" et une couverture d'album peu attrayante. L'écouteriez-vous ? _Si nous sommes honnêtes, vous êtes moins susceptible de jouer un post qui semble moins professionnel et les chiffres jouent toujours un rôle dans l'influence de vos attentes._

J'ai supprimé les comptes de "j'aime" et de "reposts" pour réduire le jugement et les préjugés. Les icônes du côté droit catégorisent les posts en types : stations, mixes, playlist, albums ou pistes. Pour se concentrer sur l'écoute plutôt que sur l'apparence, **Votre fil** met l'accent sur le titre, l'artiste et le type.

![Image](https://cdn-media-1.freecodecamp.org/images/UQlhqJ8o9TnCQbFiOrq8OHLB3xSOtWNwG0UP)
_Itération 2 : Votre fil_

#### Recherche

![Image](https://cdn-media-1.freecodecamp.org/images/LXv2RnP8zCMYBHfLsgNdN-4sAKiR4vqg0EYh)
_Itération 1 : recherche et description de l'album_

Sur SoundCloud iOS, appuyer sur l'onglet Recherche vous amène à leur version de Découverte. Appuyer sur la barre de recherche en haut de la page la change en Recherche. **J'ai séparé Recherche et Découverte en 2 onglets distincts pour la navigation.** Si l'auditeur souhaite uniquement rechercher, il appuierait sur le bouton Recherche. Voici un exemple de ma première itération.

**Recherche** contient les recherches récentes et les résultats sont divisés en aperçus de chaque classification, c'est-à-dire pistes, albums, personnes.

J'ai supprimé la barre de filtre qui défilait horizontalement, utilisant uniquement un défilement vertical unique pour éliminer le temps qu'il faudrait pour monter, descendre et aller sur les côtés. La refonte de **Recherche** optimise les résultats en trouvant l'élément le plus pertinent comme Résultat principal et en donnant des extraits des types de résultats disponibles.

![Image](https://cdn-media-1.freecodecamp.org/images/BAJ8aBO5ihE7c61sXTAjxjDXLmX5-D-T-3iH)
_SoundCloud 5.7.1 vs Itération 2 : Recherche_

Pour appliquer des genres aux pistes, SoundCloud permet aux utilisateurs d'étiqueter leurs téléchargements en utilisant des hashtags. J'ai pensé que les hashtags pourraient utiliser un peu plus de vie pour attirer l'attention sur eux.

![Image](https://cdn-media-1.freecodecamp.org/images/6gmfL65V4xNsoUyztfrtTmkb6ZazJCdOdugG)
_Itération 2 : description de l'album et hashtags_

#### Découverte

La page Découverte de la première itération se concentrait davantage sur la décomposition de SoundCloud par types tels que pistes, playlists et albums. Ce que j'ai remarqué, c'est que la navigation à travers ces éléments est devenue répétitive (pistes, playlists et albums auraient tous des modules pour les tendances, les nouveautés et les suggestions). Il n'y avait pas de thème derrière chaque élément de menu.

![Image](https://cdn-media-1.freecodecamp.org/images/yrhzoSRFsUTAm4WdZ-5LzzpnOOXwUyn1ZNG9)
_Itération 1 vs Itération 2 : page d'accueil de Découverte_

Pour rendre les éléments de menu moins arbitraires, j'ai révisé le sitemap de **Découverte** pour correspondre à la démographie d'âge de SoundCloud des participants assidus aux festivals. J'ai également essayé de maintenir un niveau de flexibilité pour les modules présentés sur chaque page. En raison des différents objectifs du projet, j'ai omis les classements lors de la réflexion sur les fonctionnalités de Découverte et j'ai mis l'accent sur **Votre Cloud, Autour du Monde, Lecture Étendue** et **Curaté**.

![Image](https://cdn-media-1.freecodecamp.org/images/14Pkfn94iCIW8JcvAsBU3pT3HCc6YFJy6OgS)
_Sitemap révisé de Découverte_

![Image](https://cdn-media-1.freecodecamp.org/images/aaODZWvC4TK8Tk1-FgL6ccOY5eksp6nCMpOy)
_SoundCloud vs Itération 2 : page d'accueil de Découverte_

_Découvrir > En vedette_  
La dernière addition de SoundCloud à Découverte [est The Upload](https://techcrunch.com/2017/05/03/soundclouds-the-upload-uses-machine-learning-to-help-you-find-new-tracks/). En tant qu'aperçu des artistes ou playlists à la mode curatés par SoundCloud, j'ai créé **une fenêtre En vedette** qui permet aux utilisateurs de parcourir de la nouvelle musique et de nouveaux talents.

![Image](https://cdn-media-1.freecodecamp.org/images/JcXxfQzrg16xtJBxHX6q-0eQ-lyJvBVIfBAF)
_Itération 2 : défilement en vedette pour Découverte_

_Découvrir > Votre Cloud_  
Vos abonnements et abonnés constituent **Votre Cloud**, où réside votre goût musical. Votre Cloud est composé de vos pairs immédiats ainsi que de contenu suggéré que vous pourriez aimer. Avec toutes ces informations tournant autour du (Sou_nd)Cl_oud (ha, vous voyez), cette fonctionnalité capture les éléments pertinents pour renforcer et élargir votre expérience d'écoute.

![Image](https://cdn-media-1.freecodecamp.org/images/KeXd3jPGNAND1SZNhn-E5XrhZZnJ1C5pqjQS)
_De gauche à droite : Votre Cloud, Autour du Monde, Tendances & Nouveautés, Lecture Étendue et Curaté_

_Découvrir > Autour du Monde_  
En tant que plateforme mondiale pour les artistes indépendants dans tant de parties différentes du monde, SoundCloud est devenu une voix pour les grandes villes et scènes. **Autour du Monde** couvre les événements à grande échelle, les sets en direct et les mouvements. Cette page est destinée à porter l'activité mondiale à la surface de SoundCloud.

![Image](https://cdn-media-1.freecodecamp.org/images/RIsaqRK917HcHXs0t5IA7gWqE3FtjbYCqdRI)
_Artwork pour 'Événements en direct' et 'Villes'_

![Image](https://cdn-media-1.freecodecamp.org/images/8TjLy0tFqOqjgU4pmLGAClwIJhL8rQ8SceqA)

_Découvrir > Tendances & Nouveautés_  
Cela existe déjà sur SoundCloud Desktop (mais pas sur mobile) sous Classements. Tendances & Nouveautés identifie les sorties virales et notables des artistes montants, ce qui est parfait pour les artistes et rappeurs de hip-hop à la mode.

_Découvrir > Lecture Étendue_  
La musique électronique est connue pour les sets et les performances plus longues. **Lecture Étendue** compile les téléchargements classés comme mixes ou stations afin que les utilisateurs puissent écouter de la musique pendant des heures.

_Découvrir > Curaté_  
Puisque les humains sont par nature paresseux, **Curaté** est la manière de SoundCloud de redonner à l'auditeur avec des playlists sélectionnées à la main. Ces playlists peuvent aller des sous-genres aux mouvements dans la scène musicale.

![Image](https://cdn-media-1.freecodecamp.org/images/Zoei7OuoPsOw82V7UyYE6dPxyz4lScaGhCFP)
_Artwork pour 'Playlists SoundCloud' et 'Événements à venir'_

#### Lecture en cours

J'ai conservé l'onglet de navigation et la forme d'onde de SoundCloud pour Lecture en cours, mais j'ai rendu les contrôles comme pause, suivant et répétition plus évidents pour l'utilisateur. Je me suis moins concentré sur l'artwork pour faire ressortir le sentiment d'un lecteur multimédia. J'ai également placé l'option de repostage des pistes dans l'écran **Lecture en cours** pour encourager les auditeurs à jouer les pistes avant de les reposter sur leur profil.

![Image](https://cdn-media-1.freecodecamp.org/images/xCx4LxpwCy6eFRAraFG8xIrhSfORfa3Ti4HA)
_Itération 2 : description de la piste et plus_

#### Bibliothèque

Si SoundCloud était plus adapté aux collectionneurs et DJ de vinyles, je pourrais voir comment Collection serait un excellent nom pour la bibliothèque de musique. Mais comme SoundCloud couvre un groupe si vaste d'auditeurs, je voulais utiliser **Bibliothèque** car c'est un titre plus courant.

![Image](https://cdn-media-1.freecodecamp.org/images/klmAmcra8oyZGjAsScdSlTQxb3y3fSzTL1f1)
_SoundCloud vs Itération 2 : Bibliothèque_

J'ai ajouté une fonctionnalité qui pourrait filtrer les pistes non seulement par quand elles ont été aimées, mais par artiste, genre ou titre. Voici un exemple de comment je pensais que cela pourrait ressembler.

![Image](https://cdn-media-1.freecodecamp.org/images/WLLRMJJYRffOnKWuyoXZUFKch12OSsgflLis)
_Itération 2 : filtrer la bibliothèque par artiste_

Sur SoundCloud, aimer quelque chose augmentera le compte de "j'aime" et l'ajoutera à la Bibliothèque, mais il n'y a pas de retour pour montrer que "ajouté à la Bibliothèque" a été effectué. Similaire à la façon dont Apple Music ou Spotify notifie l'utilisateur lorsqu'une piste est ajoutée à la bibliothèque, j'ai illustré l'action pour SoundCloud.

![Image](https://cdn-media-1.freecodecamp.org/images/BH66xhRTOEwLtQXfRWKyNQhluUpHhGWqHyuG)
_Itération 2 : ajouter et supprimer de la bibliothèque_

#### Profil

Enfin, le profil ! Certaines des suggestions que mes interviewés ont demandées étaient de montrer et d'accéder à la description, aux liens et au compte d'abonnés/abonnements. J'ai reproduit la manière dont les posts sont listés sur Découverte sur ce profil d'artiste.

![Image](https://cdn-media-1.freecodecamp.org/images/etwy0QmonIeN30zsSvjFoqGi-XeStaJc39Uu)
_Itération 2 : profil d'artiste et plus d'options_

Tout ce qui est lié à la description vient du haut vers le bas. Pour plus d'options comme suivre, reposter ou accéder aux pistes d'un artiste, le menu vient du bas vers le haut.

![Image](https://cdn-media-1.freecodecamp.org/images/VHH-bvKEeCIBTMdVG-h6JTrVUpV8hOplOApX)
_Itération 2 : description de l'artiste_

### Réflexion sur ce qui a été fait

Ce qui a commencé comme une conversation décontractée avec mes amis s'est transformé en une enquête approfondie sur nos habitudes en tant qu'êtres humains et nos besoins en tant qu'auditeurs. Au cours des 4 derniers mois, j'ai exploré chaque facette de la conception de l'expérience utilisateur et j'ai découvert que ma fascination pour l'interaction homme-machine provenait de ma compassion pour les gens.

J'ai entrepris ce projet comme un défi pour moi-même, pour voir ce que je pouvais vraiment faire. Pas de doutes, pas de retours en arrière. J'ai affronté les jugements, les attentes et ma plus grande barrière : moi-même. Tout au long de cette entreprise, j'ai exercé mes forces et j'ai construit sur mes faiblesses. Certaines choses puissantes que j'ai apprises étaient de savoir comment gérer le changement, à quel point l'itération est cruciale et être minutieux. Plus important encore, _il y a beaucoup plus à apprendre_ en matière de conception et de recherche.

Alors, où aller ? Je ne peux pas vous le dire, car je n'ai pas de réponse solide (certains d'entre nous ne l'ont pas et c'est parfaitement correct). Mais je peux vous dire ceci : je me dirige vers une vie d'apprentissage ; devenir designer de produits ; et viser la lune et au-delà !

N'hésitez pas à me rendre visite sur mon [site web](http://www.kelley-nguyen.me) si vous souhaitez en savoir plus.  
Merci d'avoir regardé !! ?