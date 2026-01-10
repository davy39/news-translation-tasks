---
title: "Présentation de CSSBattle\n\x14\n le premier jeu de code-golf CSS"
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-17T15:52:06.000Z'
originalURL: https://freecodecamp.org/news/introducing-cssbattle-the-first-css-code-golfing-game-88b7518df618
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yDgSJrVPPH70Jdh6KUyokA.png
tags:
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: Games
  slug: games
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: "Présentation de CSSBattle\n\x14\n le premier jeu de code-golf CSS"
seo_desc: 'By kushagra gour

  If you are learning Web development or are already a professional Web developer,
  there is a very high chance you have written CSS at least once in your life. It
  is a very basic building block of any webpage. Amidst all the discussion...'
---

Par kushagra gour

Si vous apprenez le développement Web ou si vous êtes déjà un développeur Web professionnel, il y a de fortes chances que vous ayez écrit du CSS au moins une fois dans votre vie. C'est un bloc de construction très basique de toute page Web. Au milieu de toutes les discussions et de l'amour et de la haine pour CSS, nous vous présentons à tous  [CSSBattle](https://cssbattle.dev) ?

CSSBattle est la première plateforme de [code-golfing](https://en.wikipedia.org/wiki/Code_golf) pour les amateurs de CSS que mon ami [Kushagra Agarwal](https://twitter.com/kushsolitary) et moi avons créée. Le but de ce jeu est simple  vous avez une image cible que vous devez répliquer avec le code CSS (et légèrement HTML si vous le souhaitez) le plus petit possible. Plus la correspondance visuelle est grande et moins il y a de bytes, plus votre score est élevé. Et c'est ainsi que vous grimpez dans les classements de CSSBattle. Voici un exemple d'écran cible :

![Image](https://cdn-media-1.freecodecamp.org/images/1*4Qin5gKKQlk7vJPRi5rKMg.png)
_Cible #9 écran de jeu_

### Quelques statistiques amusantes

Au moment d'écrire cet article, cela fait 10 jours que nous avons lancé CSSBattle. Et voici quelques statistiques amusantes que nous avons recueillies :

* 13000+ joueurs dans le monde
* Plus de 100K soumissions de code
* Nombre minimum de bytes utilisés sur une cible : [seulement 54 bytes](https://cssbattle.dev/play/1)! ?
* Un forum communautaire [lovely](https://spectrum.chat/css-battle) de 140+ joueurs et 40+ conversations

### Développement du produit

Nous avons décidé de construire et de lancer CSSBattle en un mois, pour éviter de nous retrouver dans une boucle infinie d'ajout et de polissage de fonctionnalités. Nous avons dressé une liste des éléments absolument nécessaires pour le lancement et nous nous sommes concentrés dessus.

Pendant le développement, nous avons eu des tonnes de nouvelles idées à implémenter sur le site, que nous avons continué à noter. Je suis fier que nous ayons pu résister à l'envie de travailler sur ces idées excitantes et de finalement lancer en un mois !

#### Stack Technique

Notre stack technique est assez standard pour les produits d'aujourd'hui. Nous avons [React](https://reactjs.org/) (en utilisant create-react-app comme starter) sur le frontend qui est déployé sur [Zeit Now](https://zeit.co/now). Pour le backend, nous utilisons [Firebase](https://firebase.google.com/). Puisque nous avons tous les deux principalement une expérience en frontend/design, Firebase s'est avéré être une option amazing pour implémenter facilement tout ce que nous avions en tête tout en obtenant une scalabilité et une sécurité de classe mondiale sans gérer de serveur !

#### L'algorithme de notation

L'une des choses les plus intéressantes concernant le développement de CSSBattle était la conception de l'algorithme de notation. Nous avons littéralement passé des jours à discuter et à essayer diverses formules. Nous voulions qu'une correspondance visuelle plus grande entraîne toujours un score plus élevé. Et bien sûr, pour le même pourcentage de correspondance, le score devrait augmenter avec la diminution des bytes de code. De plus, nous voulions une progression de score plus rapide vers des bytes plus bas une fois que vous êtes à 100 % de correspondance, pour le rendre plus gratifiant pour les joueurs qui suent sang et eau avec chaque byte supprimé.

En fin de compte, nous sommes satisfaits de ce que nous avons conçu. Peut-être écrirons-nous un article séparé sur l'algorithme de notation :)

### Le Lancement

Nous avions initialement prévu le lancement pour le 5 avril, mais nous avons dû le lancer un jour plus tôt. Nous avions invité de nombreux développeurs CSS éminents à essayer CSSBattle avant de le rendre public. Et "heureusement" [Jonathan Snook](https://twitter.com/snookca) [a tweeté à notre sujet](https://twitter.com/snookca/status/1113480096713793542?s=20) un jour avant que nous prévoyions de lancer, envoyant un énorme flux de développeurs vers le jeu ! Et ainsi nous avons décidé d'avancer notre lancement :)

Nous avons commencé par l'annonce sur [ProductHunt](https://www.producthunt.com/posts/cssbattle) où CSSBattle était le produit #1 du jour. Immédiatement après, il y a eu un [rush sur Reddit](https://www.reddit.com/r/web_design/comments/b9e23w/we_just_launched_cssbattlethe_first_ever_css/). Et puis, le tweet massif et vraiment encourageant de Lea Verou :

Depuis lors, cela a été une folie pour nous deux de voir la communauté grandir, jouer, apprendre et concourir ! Chaque jour, nous voyons des joueurs repousser les limites de la créativité et de l'imagination avec CSS !

### Venez nous rejoindre

Nous avons une [communauté très agréable](https://spectrum.chat/css-battle) de développeurs super créatifs et humbles sur Spectrum où vous pouvez traîner et apprendre quelques astuces CSS.

Alors, qu'attendez-vous ? Si vous avez déjà écrit du CSS, jouez maintenant  [https://cssbattle.dev](https://cssbattle.dev)  
(Nous avons également vu des gens vouloir apprendre le CSS juste pour jouer à ce jeu !)

### 

 Avertissement équitable

CSSBattle est très amusant et [addictif](https://twitter.com/LeaVerou/status/1114422182246064128). Nous avons vu des gens [perdre leur sommeil](https://twitter.com/LeaVerou/status/1114735776766595073), [faire des rêves étranges](https://twitter.com/alexzaworski/status/1114742512067862529), [être en retard pour rencontrer des amis](https://twitter.com/LeaVerou/status/1114953009061072896), [maudire](https://twitter.com/kevinnewcombe/status/1113808767907295233?s=20), [sauter des délais de projet](https://twitter.com/trangcongthanh/status/1114164655448924160?s=20) et [que sais-je](https://twitter.com/hashtag/CSSBattleChallenge). Entrez à vos propres risques ! ?

De plus, nous estimons que c'est notre responsabilité de souligner que, outre les approches créatives, CSSBattle vous oblige à exploiter la manière dont CSS (et HTML) est analysé par les navigateurs. Il est important de comprendre que le CSS que vous écrivez ici n'est pas la manière dont vous écririez dans un projet réel. Les astuces et conseils que vous apprenez en jouant ici vous feront certainement mieux comprendre CSS, mais soyez toujours vigilant et curieux de savoir ce qui est une astuce et ce qui ne l'est pas.

Amusez-vous bien avec CSS !