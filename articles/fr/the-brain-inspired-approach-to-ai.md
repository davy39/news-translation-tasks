---
title: L'approche inspirée du cerveau pour l'IA - Expliquée pour les développeurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-08T15:43:38.000Z'
originalURL: https://freecodecamp.org/news/the-brain-inspired-approach-to-ai
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-tara-winstead-8386365.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: neural networks
  slug: neural-networks
seo_title: L'approche inspirée du cerveau pour l'IA - Expliquée pour les développeurs
seo_desc: 'By Edem Gold


  "Our intelligence is what makes us human, and AI is an extension of that quality."
  – Yan LeCun


  Since the advent of Neural Networks (also known as artificial neural networks),
  the AI industry has enjoyed unparalleled success. Neural Net...'
---

Par Edem Gold

> "Notre intelligence est ce qui fait de nous des humains, et l'IA est une extension de cette qualité." - Yan LeCun

Depuis l'avènement des réseaux de neurones (également connus sous le nom de réseaux de neurones artificiels), l'industrie de l'IA a connu un succès sans précédent. Les réseaux de neurones sont la force motrice derrière les systèmes d'IA modernes, et ils sont modélisés d'après le cerveau humain.

La recherche moderne en IA implique la création et la mise en œuvre d'algorithmes qui visent à imiter les processus neuronaux du cerveau humain. Leur objectif est de créer des systèmes qui apprennent et agissent de manière similaire aux êtres humains.

Dans cet article, nous tenterons de comprendre l'approche inspirée du cerveau pour construire des systèmes d'IA.

Voici ce que nous allons couvrir :

1. [Comment nous allons aborder cela](#heading-comment-nous-allons-aborder-cela)
2. [L'histoire de l'approche inspirée du cerveau pour l'IA](#heading-lhistoire-de-lapproche-inspiree-du-cerveau-pour-lia)
3. [Comment le cerveau humain fonctionne et comment il est lié aux systèmes d'IA](#heading-comment-le-cerveau-humain-fonctionne-et-comment-il-est-lie-aux-systemes-dia)
4. [Principes de base de l'approche inspirée du cerveau pour l'IA](#heading-principes-de-base-de-lapproche-inspiree-du-cerveau-pour-lia)
5. [Défis dans la construction de systèmes d'IA inspirés du cerveau](#heading-defis-dans-la-construction-de-systemes-dia-inspires-du-cerveau)
6. [Résumé](#heading-resume)

## Comment nous allons aborder cela

Cet article commencerà par fournir un historique de la manière dont les chercheurs ont commencé à modéliser l'IA pour imiter le cerveau humain et se terminera par une discussion sur les défis actuellement rencontrés par les chercheurs dans leur tentative d'imiter le cerveau humain. Voici une description détaillée de ce à quoi s'attendre dans chaque section.

Il est important de noter que, bien que ce sujet soit intrinsèquement vaste, je vais essayer d'être aussi bref et concis que possible pour garder cela engageant. Je prévois de traiter les sous-sujets qui ont des sous-branches plus complexes comme des articles autonomes. Je laisserai également des références à la fin de l'article.

Voici un bref aperçu de ce que nous allons couvrir :

**Histoire de l'approche inspirée du cerveau pour l'IA :** Ici, nous discuterons de la manière dont les scientifiques Norman Weiner et Warren McCulloch ont amené la convergence des neurosciences et de l'informatique. Nous discuterons également de la manière dont le Perceptron de Frank Rosenblatt a été la première véritable tentative de mimétisme de l'intelligence humaine. Et nous apprendrons comment son échec a amené des travaux révolutionnaires qui serviraient de plateforme pour les réseaux de neurones.

**Comment le cerveau humain fonctionne et comment il se rapporte aux systèmes d'IA :** Dans cette section, nous plongerons dans la base biologique de l'approche inspirée du cerveau pour l'IA. Nous discuterons de la structure et des fonctions de base du cerveau humain, comprendrons son bloc de construction de base, le neurone, et comment ils travaillent ensemble pour traiter l'information et permettre des actions complexes.

**Les principes de base de l'approche inspirée du cerveau pour l'IA :** Ici, nous discuterons des concepts fondamentaux derrière l'approche inspirée du cerveau pour l'IA. Nous expliquerons des concepts tels que les réseaux de neurones, le traitement hiérarchique et le travail de plasticité. Nous apprendrons également comment les techniques de traitement parallèle, de représentations distribuées et de rétroaction récurrente aident l'IA à imiter le fonctionnement du cerveau.

**Défis dans la construction de systèmes d'IA modélisés d'après le cerveau humain :** Ici, nous parlerons des défis et des limitations inhérents à la tentative de construire des systèmes qui imitent le cerveau humain. Des défis tels que la complexité du cerveau et le manque d'une théorie unifiée de la cognition, et nous explorerons les moyens par lesquels ces défis et limitations sont abordés.

Commençons !

## L'histoire de l'approche inspirée du cerveau pour l'IA

L'envie de construire des machines capables de comportements intelligents doit beaucoup à l'inspiration du professeur du MIT [Norbert Weiner](https://en.wikipedia.org/wiki/Norbert_Wiener). Norbert Weiner était un enfant prodige qui pouvait lire à l'âge de trois ans. Il avait une vaste connaissance de divers domaines tels que les mathématiques, la neurophysiologie, la médecine et la physique.

Norbert Weiner croyait que les principales opportunités en science résidaient dans l'exploration de ce qu'il appelait les _Régions Frontalières_. Ce sont des domaines d'étude qui ne sont pas clairement dans une certaine discipline mais plutôt un mélange de disciplines, comme l'étude de la médecine et de l'ingénierie se combinant pour créer le domaine de l'Ingénierie Médicale. Il a été cité disant :

> "Si la difficulté d'un problème physiologique est de nature mathématique, dix physiologistes ignorant les mathématiques iront précisément aussi loin qu'un physiologiste ignorant les mathématiques."

En 1934, Weiner et quelques autres universitaires se réunissaient mensuellement pour discuter de documents impliquant la science des régions frontalières.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0fc008a7-d0e0-4d6f-83ed-ab2a320263e0_2048x1251.jpeg)
_Norman Weiner_

Il l'a décrit comme "une catharsis parfaite pour les idées à moitié cuites, l'autocritique insuffisante, la confiance en soi exagérée et la pomposité."

De ces sessions et de ses propres recherches personnelles, Weiner a appris de nouvelles recherches sur les systèmes nerveux biologiques ainsi que sur les travaux pionniers sur les ordinateurs électroniques.

Son inclination naturelle était de fusionner ces deux domaines, donc une relation entre les neurosciences et l'informatique a été formée. Cette relation est devenue la pierre angulaire de la création de l'intelligence artificielle telle que nous la connaissons.

Après la Seconde Guerre mondiale, Wiener a commencé à formuler des théories sur l'intelligence chez les humains et les machines, et ce nouveau domaine a été nommé [_Cybernétique_](https://en.wikipedia.org/wiki/Cybernetics). L'incursion de Wiener dans la cybernétique a réussi à faire parler les scientifiques de la possibilité de fusionner la biologie avec l'ingénierie.

L'un de ces scientifiques était un neurophysiologiste nommé [Warren McCulloch](https://en.wikipedia.org/wiki/Warren_Sturgis_McCulloch). Il a abandonné l'Université de Haverford et est allé à Yale pour étudier la philosophie et la psychologie. En assistant à une conférence scientifique à New York, il a découvert des articles écrits par des collègues sur les mécanismes de rétroaction biologique.

L'année suivante, en collaboration avec son protégé brillant de 18 ans nommé Walter Pitts, McCulloch a proposé une théorie sur le fonctionnement du cerveau. Cette théorie aiderait à favoriser la perception généralisée que les ordinateurs et les cerveaux fonctionnent essentiellement de la même manière.

Ils ont basé leurs conclusions sur des recherches de McCulloch sur la possibilité pour les neurones de traiter les nombres binaires (les ordinateurs communiquent via des nombres binaires). Cette théorie est devenue la base de ce qui est devenu le premier modèle d'un réseau de neurones artificiels, qui a été nommé le neurone McCulloch-Pitts (MCP).

Le MCP a servi de base à la création du premier réseau de neurones, connu sous le nom de [le perceptron](https://edemgold.substack.com/p/the-history-of-ai). Le Perceptron a été créé par le psychologue [Frank Rosenblatt](https://en.wikipedia.org/wiki/Frank_Rosenblatt). Inspiré par les synapses dans le cerveau, il a décidé que puisque le cerveau humain pouvait traiter et classer l'information à travers les synapses (communication entre les neurones), alors peut-être qu'un ordinateur numérique pourrait faire de même via un réseau de neurones.

Le Perceptron a essentiellement mis à l'échelle le neurone MCP d'un neurone artificiel à un réseau de neurones. Mais malheureusement, le perceptron avait quelques défis techniques qui limitaient son application pratique. La plus notable de ces limitations était son incapacité à effectuer des opérations complexes (comme classer entre plus d'un élément - par exemple, le perceptron ne pouvait pas effectuer de classification entre un chat, un chien et un oiseau).

En 1969, un livre publié par [Marvin Minsky](https://en.wikipedia.org/wiki/Marvin_Minsky) et [Seymour Papert](https://en.wikipedia.org/wiki/Seymour_Papert) intitulé _Perceptron_ expose en détail les défauts du Perceptron. À cause de cela, la recherche sur les réseaux de neurones artificiels a stagné jusqu'à la proposition de la rétropropagation par [Paul Werbos](https://en.wikipedia.org/wiki/Paul_Werbos).

La rétropropagation espère résoudre le problème de la classification des données complexes qui a entravé l'application industrielle des réseaux de neurones à l'époque. Elle a été inspirée par la plasticité synaptique - la manière dont le cerveau modifie les forces des connexions entre les neurones et améliore ainsi les performances.

La rétropropagation a été conçue pour imiter le processus dans le cerveau qui renforce les connexions entre les neurones via un processus appelé ajustement des poids.

Malgré la proposition précoce de Paul Werbos, le concept de rétropropagation n'a gagné une adoption généralisée que lorsque des chercheurs tels que [David Rumelheart](https://en.wikipedia.org/wiki/David_Rumelhart), [Geoffrey Hinton](https://en.wikipedia.org/wiki/Geoffrey_Hinton) et [Ronald Williams](https://en.wikipedia.org/wiki/Ronald_J._Williams) ont publié des articles démontrant son efficacité pour l'entraînement des réseaux de neurones.

La mise en œuvre de la rétropropagation a conduit à la création de l'apprentissage profond qui alimente la plupart des systèmes d'IA disponibles dans le monde.

> "Les gens sont plus intelligents que les ordinateurs d'aujourd'hui parce que le cerveau emploie une architecture computationnelle de base qui est plus adaptée pour traiter un aspect central des tâches de traitement de l'information naturelle que les gens maîtrisent si bien." - Traitement Distribué Parallèle

## Comment le cerveau humain fonctionne et comment il est lié aux systèmes d'IA

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8360703d-bbe7-4637-ba4a-5e898d5e3110_602x376.png)
_Illustration de la manière dont les cellules du cerveau traitent l'information_

Nous avons discuté de la manière dont les chercheurs ont commencé à modéliser l'IA pour imiter le cerveau humain. Maintenant, regardons comment le cerveau fonctionne et définissons la relation entre le cerveau et les systèmes d'IA.

### Comment le cerveau fonctionne - une description simplifiée

Le cerveau humain traite essentiellement les pensées via l'utilisation de neurones. Un neurone est composé de 3 sections principales : la dendrite, l'axone et le soma.

La dendrite est responsable de la réception des signaux d'autres neurones. Le soma traite l'information reçue de la dendrite, et l'axone est responsable du transfert de l'information traitée à la dendrite suivante dans la séquence.

Pour comprendre comment le cerveau traite la pensée, imaginez que vous voyez une voiture venir vers vous. Vos yeux envoient immédiatement des signaux électriques à votre cerveau par le nerf optique. Ensuite, le cerveau forme une chaîne de neurones pour donner un sens au signal entrant.

Ainsi, le premier neurone de la chaîne collecte le signal par ses **dendrites** et l'envoie au **soma** pour traiter le signal. Après que le soma ait terminé sa tâche, il envoie le signal à l'**axone** qui l'envoie ensuite à la dendrite du neurone suivant dans la chaîne.

La connexion entre les axones et les dendrites lors de la transmission d'informations est appelée une synapse. Ainsi, le processus entier continue jusqu'à ce que le cerveau trouve une **Entrée Synaptique Sapiotemporelle** (c'est le jargon scientifique pour dire que le cerveau continue de traiter jusqu'à ce qu'il trouve une réponse optimale au signal qui lui est envoyé). Ensuite, il envoie des signaux aux effecteurs nécessaires, par exemple vos jambes, et le cerveau envoie un signal à vos jambes pour vous éloigner de la voiture qui arrive.

### La relation entre le cerveau et les systèmes d'IA

La relation entre le cerveau et l'IA est largement mutuellement bénéfique. Le cerveau est la principale source d'inspiration derrière la conception des systèmes d'IA, et les avancées en IA conduisent à une meilleure compréhension du cerveau et de son fonctionnement.

Il existe un échange réciproque de connaissances et d'idées en ce qui concerne le cerveau et l'IA. Il existe plusieurs exemples qui attestent de la nature positivement symbiotique de cette relation :

* **Réseaux de neurones :** Arguablement l'impact le plus significatif apporté par le cerveau humain au domaine de l'intelligence artificielle est la création des réseaux de neurones. En essence, les réseaux de neurones sont des modèles computationnels qui imitent la fonction et la structure des neurones biologiques. L'architecture des réseaux de neurones et leurs algorithmes d'apprentissage sont largement inspirés de la manière dont les neurones du cerveau interagissent et s'adaptent.
* **Simulations du cerveau :** Les systèmes d'IA ont été utilisés pour [simuler](https://www.frontiersin.org/articles/10.3389/fncom.2020.00016/full) le cerveau humain et étudier ses interactions avec le monde physique. Par exemple, les chercheurs ont utilisé des techniques de Machine Learning pour simuler l'activité des neurones biologiques impliqués dans le traitement visuel. Le résultat a fourni des informations sur la manière dont le cerveau traite les informations visuelles.
* **Informations sur le cerveau :** Les chercheurs ont commencé à utiliser des algorithmes de Machine Learning pour analyser et obtenir des informations à partir des données cérébrales et des scans IRMf. Ces informations servent à identifier des schémas et des relations qui seraient autrement restés cachés. Ces informations peuvent nous aider à comprendre les fonctions cognitives internes, la mémoire et la prise de décision. Elles aident également dans le traitement des maladies natives du cerveau telles que la maladie d'Alzheimer.

## Principes de base de l'approche inspirée du cerveau pour l'IA

Ici, nous allons discuter de plusieurs concepts qui aident l'IA à imiter le fonctionnement du cerveau humain. Ces concepts ont aidé les chercheurs en IA à créer des systèmes plus puissants et intelligents capables d'effectuer des tâches complexes.

### Réseaux de neurones

Comme discuté précédemment, les réseaux de neurones ont probablement tiré l'inspiration la plus significative du cerveau humain et ont eu le plus grand impact sur le domaine de l'intelligence artificielle.

En essence, les réseaux de neurones sont des modèles computationnels qui imitent la fonction et la structure des neurones biologiques. Les réseaux sont composés de diverses couches de nœuds interconnectés, appelés neurones artificiels, qui aident au traitement et à la transmission de l'information. Cela est similaire à ce qui est fait par les dendrites, les somas et les axones dans les réseaux de neurones biologiques.

Les réseaux de neurones sont conçus pour apprendre des expériences passées de la même manière que le cerveau.

### Représentations distribuées

Les représentations distribuées sont simplement une manière d'encoder des concepts ou des idées dans un réseau de neurones sous forme de motif le long de plusieurs nœuds du réseau afin de former un motif.

Par exemple, le concept de fumer pourrait être représenté (encodé) en utilisant un certain ensemble de nœuds dans un réseau de neurones. Donc, si un réseau rencontre une image d'une personne fumant, il utilise alors ces nœuds sélectionnés pour donner un sens à l'image (c'est beaucoup plus complexe que cela, mais pour simplifier, nous en resterons là).

Cette technique aide les systèmes d'IA à se souvenir de concepts complexes ou de relations entre concepts de la même manière que le cerveau reconnaît et se souvient de stimuli complexes.

### Rétroaction récurrente

Il s'agit d'une technique utilisée dans l'entraînement des modèles d'IA où la sortie d'un réseau de neurones est renvoyée en entrée pour permettre au réseau d'intégrer sa sortie comme donnée d'entrée supplémentaire dans l'entraînement. Cela est similaire à la manière dont le cerveau utilise des boucles de rétroaction afin d'ajuster son modèle en fonction des expériences précédentes.

### Traitement parallèle

Le traitement parallèle implique de diviser les tâches computationnelles complexes en petits morceaux dans un effort pour traiter les petits morceaux sur un autre processeur dans une tentative d'améliorer la vitesse. Cette approche permet aux systèmes d'IA de traiter plus de données d'entrée plus rapidement, similaire à la manière dont le cerveau est capable d'effectuer différentes tâches en même temps (multitâche).

### Mécanismes d'attention

Il s'agit d'une technique utilisée qui permet aux modèles d'IA de se concentrer sur des parties spécifiques des données d'entrée. Elle est couramment employée dans des secteurs tels que le traitement du langage naturel qui contient des données complexes et encombrantes.

Elle est inspirée par la capacité du cerveau à ne prêter attention qu'à des parties spécifiques d'un environnement largement distractif - comme votre capacité à vous concentrer et à interagir dans une conversation parmi un cacophonie de conversations.

### Apprentissage par renforcement

L'apprentissage par renforcement est une technique utilisée pour entraîner les systèmes d'IA. Elle a été inspirée par la manière dont les êtres humains apprennent des compétences par essai et erreur. Elle implique qu'un agent d'IA reçoive des récompenses ou des punitions en fonction de ses actions. Cela permet à l'agent d'apprendre de ses erreurs et d'être plus efficace dans ses actions futures (cette technique est généralement utilisée dans la création de jeux).

### Apprentissage non supervisé

Le cerveau reçoit constamment de nouveaux flux de données sous forme de sons, de contenu visuel, de sensations sensorielles sur la peau, et ainsi de suite. Il doit donner un sens à tout cela et tenter de former une compréhension cohérente et logique de la manière dont tous ces événements apparemment disparates affectent son état physique.

Prenez cette analogie comme exemple : vous sentez une goutte d'eau sur votre peau, vous entendez le son des gouttes d'eau tombant rapidement sur les toits, vous sentez vos vêtements devenir lourds et à cet instant, vous savez qu'il pleut.

Vous recherchez ensuite dans votre banque de mémoire pour vérifier si vous avez apporté un parapluie. Si c'est le cas, vous êtes en sécurité, sinon vous vérifiez pour voir la distance entre votre emplacement actuel et votre domicile. Si c'est proche, vous êtes en sécurité, mais sinon vous essayez d'évaluer à quel point la pluie va devenir intense. Si c'est une bruine légère, vous pouvez tenter de continuer le voyage de retour à votre domicile, mais si c'est une averse plus forte, alors vous devez trouver un abri.

La capacité de donner un sens à des points de données apparemment disparates (eau, son, sensation, distance) est mise en œuvre dans l'intelligence artificielle sous la forme d'une technique appelée apprentissage non supervisé. Il s'agit d'une technique d'entraînement de l'IA où les systèmes d'IA sont enseignés pour donner un sens à des données brutes et non structurées sans étiquetage explicite (personne ne vous dit qu'il pleut quand il pleut, n'est-ce pas ?).

## Défis dans la construction de systèmes d'IA inspirés du cerveau

Jusqu'à présent, vous avez appris comment les chercheurs ont utilisé le cerveau comme inspiration pour les systèmes d'IA. Nous avons également discuté de la manière dont le cerveau se rapporte à l'IA et des principes de base de l'IA inspirée du cerveau.

Dans cette section, nous allons parler de certains des défis techniques et conceptuels inhérents à la construction de systèmes d'IA modélisés d'après le cerveau humain.

### Complexité

C'est un défi assez redoutable. L'approche inspirée du cerveau pour l'IA est basée sur la modélisation du cerveau et la construction de systèmes d'IA après ce modèle. Mais le cerveau humain est un système intrinsèquement complexe avec 100 milliards de neurones et environ 600 billions de connexions synaptiques (chaque neurone a, en moyenne, 10 000 connexions synaptiques avec d'autres neurones). Ces synapses interagissent constamment de manière dynamique et imprévisible.

Construire des systèmes d'IA qui visent à imiter, et peut-être dépasser, cette complexité est en soi un défi et nécessite des modèles statistiques tout aussi complexes.

### Exigences de données pour l'entraînement de grands modèles

Le GPT 4 d'Open AI, qui est, à l'heure actuelle, le fer de lance des modèles d'IA basés sur le texte, nécessite 47 GigaOctets de données. En comparaison, son prédécesseur GPT3 a été entraîné sur 17 Gigaoctets de données, ce qui est environ 3 ordres de grandeur inférieur. Imaginez sur combien de données GPT 5 sera entraîné.

Pour obtenir des résultats acceptables, les systèmes d'IA inspirés du cerveau nécessitent d'énormes quantités de données pour les tâches, en particulier les tâches auditives et visuelles. Cela met un accent particulier sur la création de pipelines de collecte de données. Par exemple, Tesla dispose de 780 millions de miles de données de conduite et son pipeline de collecte de données ajoute un million de plus toutes les 10 heures.

### Efficacité énergétique

Construire des systèmes d'IA inspirés du cerveau qui émulent l'efficacité énergétique du cerveau est un énorme défi. Le cerveau humain consomme environ 20 watts de puissance. En comparaison, l'Autopilot de Tesla, sur des puces spécialisées, consomme environ 2 500 watts par seconde et [il faut environ](https://ts2.space/en/exploring-the-environmental-footprint-of-gpt-4-energy-consumption-and-sustainability/#:~:text=The%20paper%20found%20that%20the,hours%20(MWh)%20of%20energy.) 7,5 mégawatts-heures (MWh) pour entraîner un modèle d'IA de la taille de ChatGPT.

### Le problème d'explicabilité

Développer des systèmes d'IA inspirés du cerveau qui peuvent être dignes de confiance par les utilisateurs est crucial pour la croissance et l'adoption de l'IA - mais c'est là que réside le problème.

Le cerveau, que les systèmes d'IA sont censés modéliser, est essentiellement une boîte noire. Le fonctionnement interne du cerveau n'est pas facile à comprendre, en partie à cause d'un manque d'informations sur la manière dont le cerveau traite la pensée.

Il ne manque pas de recherches sur la structure biologique du cerveau humain, mais il y a un certain manque d'informations empiriques sur les qualités fonctionnelles du cerveau - c'est-à-dire, comment la pensée est formée, comment le déjà-vu se produit, et ainsi de suite. Cela conduit à des problèmes dans la construction de systèmes d'IA inspirés du cerveau.

### Les exigences interdisciplinaires

L'acte de construire des systèmes d'IA inspirés du cerveau nécessite les connaissances d'experts dans différents domaines, comme les neurosciences, l'informatique, l'ingénierie, la philosophie et la psychologie.

Mais cela présente des défis, à la fois logistiques et fondamentaux : obtenir des experts de différents domaines est financièrement coûteux. De plus, il y a le problème de conflit de connaissances - il peut être vraiment difficile de faire en sorte qu'un ingénieur se soucie des effets psychologiques de ce qu'il construit, sans parler du problème des egos qui entrent en collision.

## Résumé

Bien que l'approche inspirée du cerveau semble être la voie évidente pour construire des systèmes d'IA, elle a ses défis. Mais nous pouvons regarder vers l'avenir avec l'espoir que des efforts sont faits pour résoudre ces problèmes.

Si vous avez aimé cet article, envisagez de vous abonner à ma [newsletter](https://www.freecodecamp.org/news/p/863dd550-5476-4d67-b6cd-93c316dd804a/edemgold.substack.com) pour obtenir plus d'articles comme celui-ci.

## Références

* [Certification en Machine Learning de freeCode Camp](https://www.freecodecamp.org/learn/machine-learning-with-python)
* [Rapport de sécurité des véhicules de Tesla](https://www.tesla.com/VehicleSafetyReport#:~:text=Because%20every%20Tesla%20is%20connected,the%20different%20ways%20accidents%20happen.)
* [Unités neuronales de base du cerveau : Neurones, Synapses et Potentiel d'Action](https://arxiv.org/abs/1906.01703)
* [Quand l'IA inspirée du cerveau rencontre l'AGI](https://arxiv.org/pdf/2303.15935.pdf)
* [Perceptron : Le neurone artificiel (Une mise à niveau essentielle du neurone McCulloch-Pitts)](https://towardsdatascience.com/perceptron-the-artificial-neuron-4d8c70d5cc8d)
* [Neurone McCulloch-Pitts - Le premier modèle mathématique de l'humanité d'un neurone biologique](https://medium.com/towards-data-science/mcculloch-pitts-model-5fdf65ac5dd1)
* [Rétropropagation à travers le temps : Ce qu'elle fait et comment la faire](https://axon.cs.byu.edu/Dan/678/papers/Recurrent/Werbos.pdf)
* [L'histoire de l'IA](https://edemgold.substack.com/p/the-history-of-ai)
* [BrainOS : Un nouveau cadre d'apprentissage automatique automatique inspiré du cerveau](https://www.frontiersin.org/articles/10.3389/fncom.2020.00016/full)