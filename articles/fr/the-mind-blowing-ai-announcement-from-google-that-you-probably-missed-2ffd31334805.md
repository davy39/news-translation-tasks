---
title: L'annonce incroyable de Google sur l'IA que vous avez probablement manquée.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-06T05:38:53.000Z'
originalURL: https://freecodecamp.org/news/the-mind-blowing-ai-announcement-from-google-that-you-probably-missed-2ffd31334805
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EhHUu6QJ1KbUDyW9a9ZEog.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Google
  slug: google
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: L'annonce incroyable de Google sur l'IA que vous avez probablement manquée.
seo_desc: 'By Gil Fewster

  Disclaimer: I’m not an expert in neural networks or machine learning. Since originally
  writing this article, many people with far more expertise in these fields than myself
  have indicated that, while impressive, what Google have achiev...'
---

Par Gil Fewster

**_Avertissement_** : Je ne suis pas un expert en réseaux de neurones ou en apprentissage automatique. Depuis la rédaction originale de cet article, de nombreuses personnes bien plus expertes que moi dans ces domaines ont indiqué que, bien qu'impressionnant, ce que Google a accompli est évolutif, et non révolutionnaire. Il est juste de dire que je suis coupable d'anthropomorphisme dans certaines parties du texte.

_J'ai laissé le contenu de l'article inchangé, car je pense qu'il est intéressant de comparer la réaction instinctive que j'ai eue avec les commentaires ultérieurs d'experts dans le domaine. Je vous encourage fortement à parcourir les commentaires après avoir lu l'article pour des perspectives plus sobres et informées que les miennes._

Dans les dernières semaines de 2016, Google a publié un article qui est passé inaperçu pour la plupart des gens. Ce qui est dommage, car il s'agit peut-être de l'article le plus étonnant sur l'apprentissage automatique que j'ai lu l'année dernière.

Ne vous sentez pas mal si vous l'avez manqué. Non seulement l'article devait rivaliser avec la ruée pré-Noël que la plupart d'entre nous naviguaient — il était également caché dans le blog de recherche de Google, sous le titre geek [_Traduction Zero-Shot avec le Système de Traduction Automatique Multilingue de Google_](https://research.googleblog.com/2016/11/zero-shot-translation-with-googles.html).

Cela ne crie pas exactement _à lire absolument_, n'est-ce pas ? Surtout lorsque vous avez des projets à finaliser, des cadeaux à acheter et des querelles familiales à résoudre — tout cela pendant que le calendrier de l'Avent compte impitoyablement les jours jusqu'à Noël comme une sorte d'horloge de l'apocalypse remplie de chocolat.

Heureusement, je suis là pour vous mettre à jour. Voici l'essentiel.

Jusqu'en septembre de l'année dernière, Google Translate utilisait la traduction basée sur des phrases. Il faisait essentiellement la même chose que vous et moi lorsque nous cherchons des mots et des phrases clés dans nos guides linguistiques Lonely Planet. C'est assez efficace, et incroyablement rapide par rapport à la recherche maladroite à travers un tas de pages pour trouver l'équivalent français de « s'il vous plaît, apportez-moi tout votre fromage et ne vous arrêtez pas jusqu'à ce que je tombe ». Mais il manque de nuance.

La traduction basée sur des phrases est un instrument brut. Elle fait le travail assez bien pour s'en sortir. Mais mapper des mots et des phrases approximativement équivalents sans comprendre les structures linguistiques ne peut produire que des résultats grossiers.

Cette approche est également limitée par l'étendue du vocabulaire disponible. La traduction basée sur des phrases n'a pas la capacité de faire des suppositions éclairées sur les mots qu'elle ne reconnaît pas et ne peut pas apprendre de nouvelles entrées.

Tout cela a changé en septembre, lorsque Google a donné à son outil de traduction un nouveau moteur : le système de traduction automatique neuronale de Google (GNMT). Ce nouveau moteur est chargé de tous les mots à la mode de 2016, comme _réseau de neurones_ et _apprentissage automatique_.

La version courte est que Google Translate est devenu intelligent. Il a développé la capacité d'apprendre des personnes qui l'utilisaient. Il a appris à faire des suppositions éclairées sur le contenu, le ton et la signification des phrases en fonction du contexte des autres mots et phrases autour d'elles. Et — voici la partie qui devrait faire exploser votre cerveau — il est devenu créatif.

Google Translate **a inventé sa propre langue** pour l'aider à traduire plus efficacement.

De plus, personne ne le lui a dit. Il n'a pas développé une langue (ou [interlingua](https://en.wikipedia.org/wiki/Interlingua), comme Google l'appelle) parce qu'il était codé pour le faire. Il a développé une nouvelle langue parce que le logiciel a déterminé au fil du temps que c'était le moyen le plus efficace de résoudre le problème de la traduction.

Arrêtez-vous et réfléchissez à cela un moment. Laissez-le s'imprégner. Un système de calcul neuronal conçu pour traduire du contenu d'une langue humaine à une autre a développé sa propre langue interne pour rendre la tâche plus efficace. Sans qu'on le lui dise. En quelques semaines. _(J'ai ajouté une correction/rétractation de ce paragraphe dans les notes)_

Pour comprendre ce qui se passe, nous devons comprendre ce qu'est la capacité de traduction zero-shot. Voici Mike Schuster, Nikhil Thorat et Melvin Johnson de Google, extraits de l'article original du blog :

> Supposons que nous entraînons un système multilingue avec des exemples japonais↔anglais et coréen↔anglais. Notre système multilingue, de la même taille qu'un système GNMT unique, partage ses paramètres pour traduire entre ces quatre paires de langues différentes. Ce partage permet au système de transférer les « connaissances de traduction » d'une paire de langues à une autre. Cet apprentissage par transfert et la nécessité de traduire entre plusieurs langues obligent le système à mieux utiliser sa puissance de modélisation.

> Cela nous a inspiré pour poser la question suivante : pouvons-nous traduire entre une paire de langues que le système n'a jamais vue auparavant ? Un exemple de cela serait les traductions entre le coréen et le japonais où les exemples coréen↔japonais n'ont pas été montrés au système. Impressionnant, la réponse est oui — il peut générer des traductions coréen↔japonais raisonnables, même s'il n'a jamais été enseigné pour le faire.

Ici, vous pouvez voir un avantage du nouveau système neuronal de Google par rapport à l'ancienne approche basée sur les phrases. Le GMNT est capable d'apprendre à traduire entre deux langues sans être explicitement enseigné. Cela ne serait pas possible dans un modèle basé sur les phrases, où la traduction dépend d'un dictionnaire explicite pour mapper les mots et les phrases entre chaque paire de langues traduites.

Et cela amène les ingénieurs de Google à cette découverte véritablement étonnante de création :

> Le succès de la traduction zero-shot soulève une autre question importante : le système apprend-il une représentation commune dans laquelle les phrases de même signification sont représentées de manière similaire, indépendamment de la langue — c'est-à-dire une « interlingua » ? En utilisant une représentation tridimensionnelle des données internes du réseau, nous avons pu jeter un coup d'œil au système alors qu'il traduit un ensemble de phrases entre toutes les paires possibles des langues japonaise, coréenne et anglaise.

> Au sein d'un seul groupe, nous voyons une phrase de même signification mais dans trois langues différentes. Cela signifie que le réseau doit encoder quelque chose sur la sémantique de la phrase plutôt que de simplement mémoriser des traductions phrase à phrase. Nous interprétons cela comme un signe de l'existence d'une interlingua dans le réseau.

Donc, voilà. Dans les dernières semaines de 2016, alors que les journalistes du monde entier commençaient à rédiger leurs articles « était-ce la pire année de la mémoire vivante », les ingénieurs de Google documentaient tranquillement une véritable percée étonnante en ingénierie logicielle et en linguistique.

Je pensais simplement que vous aimeriez le savoir.

D'accord, pour _vraiment_ comprendre ce qui se passe, nous avons probablement besoin de plusieurs diplômes en informatique et en linguistique. Je ne fais que gratter la surface ici. Si vous avez le temps d'obtenir quelques diplômes (ou si vous les avez déjà), n'hésitez pas à me contacter et à tout m'expliquer. Lentement.

**_Mise à jour 1_** : dans mon excitation, il est juste de dire que j'ai exagéré l'idée de ce système comme étant « intelligent » — du moins en ce qui concerne l'intelligence et la prise de décision humaines. Assurez-vous de lire [le commentaire de Chris McDonald](https://medium.com/@chrismcdonald_94568/ok-slow-down-516f93f83ac8?source=linkShare-36020d726097-1483872852) après l'article pour une perspective plus sobre.

**_Mise à jour 2_** : [La réponse excellente et détaillée de Nafrondel](https://medium.com/@nafrondel/you-requested-someone-with-a-degree-in-this-holds-up-hand-d4bf18e96ff?source=linkShare-36020d726097-1483995348) est également une lecture incontournable pour une explication experte du fonctionnement des réseaux de neurones.