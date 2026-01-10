---
title: Comment j'ai construit un classement des meilleures histoires Medium de tous
  les temps. Et comment il a failli mourir.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-10T11:21:01.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-top-medium-stories-e07a32cf5255
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BUxJuact-veqvL9lvnHlxw.png
tags:
- name: Life lessons
  slug: life-lessons
- name: medium
  slug: medium
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: writing
  slug: writing
seo_title: Comment j'ai construit un classement des meilleures histoires Medium de
  tous les temps. Et comment il a failli mourir.
seo_desc: 'By Michael Deng

  Last year I built Top Medium Stories — a website that showcases the Medium’s top
  stories of all time. This is the tale of how a lone developer scraped thousands
  of stories and hitting seemingly fatal roadblocks.

  Spoiler alert: Life fi...'
---

Par Michael Deng

L'année dernière, j'ai construit Top Medium Stories — un site web qui présente les meilleures histoires de Medium de tous les temps. Voici l'histoire de comment un développeur solitaire a scrapé des milliers d'histoires et a rencontré des obstacles apparemment fatals.

_Alerte spoiler : La vie trouve toujours un chemin. Vous pouvez consulter le classement — mis à jour quotidiennement — sur [TopMediumStories.com](https://topmediumstories.com/)._

### Pourquoi ai-je fait cela ?

En tant que lecteur de longue date sur Medium, j'ai toujours été curieux de savoir quelles étaient les histoires les plus populaires. Bien que le fil personnalisé et les pages thématiques mettent en avant de nombreuses excellentes histoires, beaucoup passent entre les mailles du filet.

Désireux de déterrer les pépites enfouies dans les annales de Medium, je me suis fixé un nouvel objectif début 2017 : je voulais trouver les histoires les plus populaires de tous les temps sur Medium et les partager avec le reste du monde.

Mon objectif a abouti à la publication de ma liste des [Meilleures histoires Medium par année](https://medium.com/startup-grind/most-recommended-medium-stories-by-year-2db66605d5be).

J'ai compilé les histoires manuellement, ce qui était une tâche ardue. Sur une période d'une semaine, j'ai visité chaque page des meilleures histoires depuis le 10 septembre 2014 (date de lancement de la fonctionnalité des meilleures histoires). Pour trouver des histoires encore plus anciennes, j'ai fouillé dans les archives des publications en utilisant la Wayback Machine pour récupérer d'anciennes copies des pages Medium.

J'ai construit un immense tableau de toutes les histoires que j'ai trouvées. C'était un travail fastidieux, mais j'étais fier du résultat.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ctml_IoHbj0xWy78KyJhuw.png)
_Une petite section du tableau colossal ?_

Mais mon sentiment de fierté fut de courte durée, car la liste est rapidement devenue obsolète. Je voulais la maintenir à jour, mais le faire manuellement était impossible.

Puis, une idée m'est venue. J'avais déjà déterminé les étapes manuelles pour collecter les données la première fois. Il n'y avait aucune raison pour que je ne puisse pas automatiser ces étapes avec du code. Ainsi, j'ai décidé de transformer la liste en un site web dynamique.

### Automatisation de la collecte de données

Pour automatiser les étapes manuelles décrites ci-dessus, j'ai écrit un scraper web en utilisant Python [Scrapy](https://scrapy.org/).

Le scraper parcourt chaque page des meilleures histoires depuis le 10 septembre 2014 et ajoute chaque histoire qu'il trouve dans un dictionnaire Python. Le dictionnaire est ensuite trié par le nombre de claps que chaque histoire a reçus et écrit dans un fichier JSON. (Les claps sont l'équivalent des "likes" ou des "upvotes" sur Medium, et les lecteurs peuvent donner jusqu'à 50 claps à une histoire.)

Voici un extrait du fichier JSON :

```json
[  "We fired our top talent. Best decision we ever made.",   {    "recommends": 79000.0,     "pub_url": "https://medium.freecodecamp.org",     "author": "Jonathan Sol\u00f3rzano-Hamilton",     "image": "https://cdn-media-1.freecodecamp.org/images/1*4hU3Xn7wunA81I3v17JIrg.jpeg",     "year": "2017",     "story_url": "https://medium.freecodecamp.org/we-fired-our-top-talent-best-decision-we-ever-made-4c0a99728fde",     "pub": "freeCodeCamp",     "author_url": "https://medium.freecodecamp.org/@peachpie"  }],...
```

Avant de construire le scraper, j'ai vérifié le fichier [robots.txt](https://medium.com/robots.txt) de Medium pour m'assurer que je ne violais aucune politique. J'ai également réglé la vitesse de scraping très lentement (2 secondes entre chaque requête), afin que le scraper ne surcharge pas les serveurs de Medium.

#### Conversion des données en HTML

L'étape suivante était de transformer le fichier JSON en HTML pour afficher les histoires sur une page web.

J'ai installé [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) pour cela. D'abord, j'ai construit un modèle HTML avec des tableaux et des lignes vides. Ensuite, j'ai écrit un script qui utilise BeautifulSoup pour remplir le modèle à partir du fichier JSON.

Avec un fichier HTML de base contenant toutes les histoires que je voulais afficher, il était temps de créer le site web réel.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3XTqVVycq5riBcjR3h5ZgA.jpeg)

### Construction d'un site web génial

Lors de la planification du site web, j'avais trois objectifs en tête :

#### 1. Design minimal et élégant

Le langage de design est centré autour de beaucoup d'espace blanc et de texte à haut contraste. Ainsi, le point focal est sur les histoires qu'il essaie de mettre en avant, et non sur l'esthétique du site web lui-même.

J'ai également ajouté un mode "Compact", qui masque les images des histoires sur le site web. Cela permet aux lecteurs de parcourir la liste avec facilité.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EqIyKAmHT-FrzN4qm7b9mQ.png)
_Mode "Compact"_

#### 2. Rapide

La première version du site web était assez lente. Cela était dû au fait qu'elle essayait de charger des centaines d'images de présentation en même temps.

Pour résoudre ce problème, j'ai utilisé le "lazy loading". Lorsque vous arrivez sur le site web, seules les 50 premières histoires sous "All" sont chargées. Si vous voulez voir plus d'histoires, vous devez cliquer sur "Load more". Ce modèle de design réduit considérablement le temps de chargement initial.

De plus, pour rendre la navigation plus réactive, j'ai conçu ce site web comme une application web monopage. Lorsque vous cliquez sur un bouton, vous ne naviguez pas vers une autre page HTML. Au lieu de cela, jQuery change la vue instantanément.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nU4Novi6IXdTY7CqBZPzgA.gif)
_Navigation réactive et lazy loading en action_

#### 3. Léger

Pour garder le site web léger, j'ai choisi de ne pas utiliser la plupart des bibliothèques frontend populaires. Je n'ai pas utilisé Bootstrap, et j'ai limité l'utilisation de JavaScript/jQuery au minimum.

Un coup d'œil au dépôt du projet révèle une configuration très minimale. Quelques fichiers HTML, un fichier CSS, quelques scripts et une poignée de fichiers de données.

En conséquence, le site web n'a pas beaucoup de parties mobiles et de dépendances. Il est très simple à maintenir et à déboguer.

### **Test et lancement**

J'ai partagé le prototype avec quelques amis et leur ai demandé de le critiquer. En utilisant leurs retours, j'ai itéré sur le design deux fois. Ensuite, je l'ai lancé sur Product Hunt.

Je pouvais à peine dormir cette nuit-là. Je me souviens encore avoir constamment actualisé la page pour vérifier les nouveaux commentaires jusqu'à ce que je m'effondre d'épuisement.

Le lendemain matin, je me suis précipité hors du lit et j'ai ouvert mon ordinateur. Je n'en croyais pas mes yeux ! Top Medium Stories était en tête de la page d'accueil de Product Hunt. À la fin de la journée, il avait été élu le #2 produit du jour.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4XuWJfp8NxmYqJjul8qVRg.png)
_[Page Product Hunt pour Top Medium Stories](https://www.producthunt.com/posts/top-medium-stories" rel="noopener" target="_blank" title=")_

### La mort soudaine de Medium Top Stories

Le lancement sur Product Hunt a dépassé mes attentes les plus folles, et j'ai été sur un petit nuage pendant longtemps. Mais je savais que je n'avais pas terminé tant que je n'avais pas partagé mon projet sur Medium. J'ai commencé ce post il y a six mois et je l'ai enfin terminé il y a quelques semaines. J'étais au-delà de l'excitation à l'idée de le publier.

Avant de soumettre, j'ai décidé d'exécuter le script de collecte de données une dernière fois pour mettre à jour le site web.

Le script a échoué de manière catastrophique.

"Pas de gros problème. Soit Medium a une panne, soit mon internet ne fonctionne pas," ai-je pensé. Mais je me trompais complètement. Lorsque j'ai réalisé ce qui s'était réellement passé, je me suis affalé dans ma chaise et j'ai passé mes doigts sur mon visage par frustration.

Je vous jure, deux jours auparavant, Medium avait supprimé la page des meilleures histoires de leur site web. Ils avaient sabordé la page même dont mon scraper dépendait pour fonctionner !

J'ai immédiatement envoyé un email à Medium, leur demandant de considérer la réintégration de la page des meilleures histoires. Je n'ai pas obtenu la réponse que j'espérais.

![Image](https://cdn-media-1.freecodecamp.org/images/1*h6hNC0_A-gXqzce1xzDliA.png)

Mais je ne leur en ai pas voulu. Mon site web n'était pas officiellement soutenu — ils n'étaient pas obligés de faire quoi que ce soit. Même s'ils n'avaient pas fait ce changement particulier, tôt ou tard une de leurs mises à jour aurait cassé mon site web. C'était inévitable.

Je me sentais désespéré. Puisque le site web ne pouvait plus être mis à jour, il n'était plus qu'une liste statique qui serait bientôt obsolète. Dans mon esprit, Top Medium Stories était mort-né.

### Les germes d'une nouvelle vie

Pendant un moment, j'ai travaillé sur d'autres projets et je n'ai pas regardé Top Medium Stories du tout. Mais je ne pouvais pas m'empêcher de penser à l'histoire inachevée du site web. Je voulais publier un post-mortem — même si cela n'avait pas une fin heureuse. Cela semblait être une bonne façon de clore le projet.

J'ai conclu l'article avec :

> "Donc, j'espère que vous avez apprécié lire à propos de Top Medium Stories. Ce fut une expérience incroyable et je suis fier de ce que j'ai fait — je suis désolé que cela ait dû se terminer ainsi. Il y aura toujours des choses que vous ne pouvez pas prédire ou contrôler, et elles peuvent effacer votre travail en un clin d'œil. C'est la vie."

Alors que je fixais mon brouillon terminé, j'ai réalisé quelque chose. **Je déteste les fins tristes.**

Soudain, mes yeux se sont posés sur ce même blob JSON dont j'ai parlé plus tôt.

```json
[  "We fired our top talent. Best decision we ever made.",   {    "recommends": 79000.0,     "pub_url": "https://medium.freecodecamp.org",     "author": "Jonathan Sol\u00f3rzano-Hamilton",     "image": "https://cdn-media-1.freecodecamp.org/images/1*4hU3Xn7wunA81I3v17JIrg.jpeg",     "year": "2017",     "story_url": "https://medium.freecodecamp.org/we-fired-our-top-talent-best-decision-we-ever-made-4c0a99728fde",     "pub": "freeCodeCamp",     "author_url": "https://medium.freecodecamp.org/@peachpie"  }],...
```

Et j'ai eu une révélation. Je n'avais pas besoin de la page des meilleures histoires pour mettre à jour le site web. Au lieu de cela, je pouvais visiter chaque URL dans le fichier JSON et récupérer les données directement depuis la page web de l'histoire.

Pour récupérer de nouvelles histoires, je pouvais scraper la nouvelle page Popular on Medium, qui me donnerait les meilleures histoires publiées récemment.

Après avoir refactorisé mon code, j'ai réalisé quelque chose : il est possible que chaque nouvelle histoire populaire ne finisse pas par être mise en avant sur la page Popular on Medium. Donc, si vous lisez une histoire que vous pensez devrait être sur Top Medium Stories mais qui ne l'est pas, veuillez me le faire savoir. Envoyez simplement l'URL de l'histoire à **michaeldeng18@gmail.com**, et je l'ajouterai immédiatement. Ensemble, nous pouvons nous assurer que les classements sont aussi complets que possible.

Il y a toujours le risque que Medium puisse un jour restreindre complètement le scraping, ou même publier son propre classement d'histoires. L'un ou l'autre de ces changements pourrait rendre Top Medium Stories obsolète.

Mais en attendant, je continuerai à maintenir Top Medium Stories, le meilleur site pour découvrir des histoires géniales.

Si à ce stade vous n'avez pas encore vu Top Medium Stories, [allez le découvrir](https://topmediumstories.com/) ! Cela me rendrait très heureux si le site vous aide à trouver des histoires extraordinaires que vous n'auriez autrement jamais découvertes.

Merci d'avoir lu !