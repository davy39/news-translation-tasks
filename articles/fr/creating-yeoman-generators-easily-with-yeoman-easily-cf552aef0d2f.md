---
title: Créer des générateurs Yeoman facilement avec yeoman-easily
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-01T16:44:51.000Z'
originalURL: https://freecodecamp.org/news/creating-yeoman-generators-easily-with-yeoman-easily-cf552aef0d2f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*80vnFUltjdnV38Owrjr95g.png
tags:
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
- name: yeoman
  slug: yeoman
seo_title: Créer des générateurs Yeoman facilement avec yeoman-easily
seo_desc: 'By Krist Wongsuphasawat

  I’ve used Yeoman to start many of my projects. It’s an amazing web scaffolding tool.

  But after creating my own generators several times, I saw the repetitive tasks,
  somewhat lengthy code, and part of the generator code that co...'
---

Par Krist Wongsuphasawat

J'ai utilisé [Yeoman](http://yeoman.io/) pour démarrer de nombreux projets. C'est un outil incroyable pour l'échafaudage web.

Mais après avoir créé mes propres générateurs plusieurs fois, j'ai remarqué les tâches répétitives, le code quelque peu long et la partie du code du générateur qui me confusait à chaque fois.

À un moment donné, j'ai fini par créer un petit utilitaire que je copiais sans cesse de projet en projet. J'ai passé un week-end à l'organiser et à ajouter plusieurs fonctionnalités pour prendre en charge les tâches répétitives.

### Et yeoman-easily est né.

[yeoman-easily](https://github.com/kristw/yeoman-easily) aide avec les tâches suivantes lors de la création d'un générateur avec Yeoman :

#### Avantages #1 : Confirmation

Souvent, vous souhaitez demander une confirmation à l'utilisateur avant de continuer. Le premier bloc de code ci-dessous montre comment écrire cela avec Yeoman standard. Le deuxième bloc de code montre comment l'écrire avec l'aide de yeoman-easily.

Avec yeoman-easily, vous pouvez demander une confirmation avant de continuer en une seule ligne. `easily.confirmBeforeStart(message)` puis `easily.checkForConfirmation()` retourne le résultat.

#### **Avantages #2 : Invite**

Gérer les résultats de l'invite, puis choisir quelle invite afficher était compliqué.

* `this.prompt()` retourne une promesse qui doit être gérée pour obtenir les réponses et les stocker. Les réponses sont généralement stockées dans `this.props`. Ce bloc de code doit être réécrit encore et encore.
* Un générateur parent passe souvent les paramètres au générateur enfant via des options. D'après ce que j'ai vu, de nombreux générateurs masqueront les invites pour les champs présents dans les options. (Oui, vous devez écrire du code pour vérifier cela.) Ensuite, combinez les réponses des invites et des options dans `this.props`.

Pour plus de commodité, yeoman-easily :

* Gère le stockage des réponses de l'utilisateur à partir des invites dans `this.props`. Il suffit d'appeler `easily.prompt(prompts)` au lieu de `this.prompt(prompts)`
* Peut automatiquement ignorer une invite si une option avec le même nom est présente. Il copiera également la valeur de `this.options[field]` existant dans `this.props[field]`.
* Peut enregistrer des invites courantes via `easily.learnPrompts(prompts)` et permettre de rechercher des invites par nom lors de l'appel de `easily.prompt()`. Cela peut faire gagner beaucoup de temps si vous créez plusieurs générateurs qui posent des questions similaires.

#### **Avantages #3 : Composition**

Le générateur Yeoman peut appeler (`composeWith`) un autre générateur à partir d'un autre package ou d'un sous-générateur local, mais la syntaxe actuelle pour le faire est quelque peu longue. Je ne suis toujours pas sûr de ce que signifie le champ _local_.

yeoman-easily simplifie la syntaxe en `easily.composeWithLocal(name, namespace, options)` et `easily.composeWithExternal(package, namespace, options)`.

#### **Avantages #4 : Gestion des fichiers**

Yeoman fournit des API flexibles pour la gestion des fichiers afin de couvrir de nombreux scénarios. Mais il faut quelques lignes pour effectuer des tâches courantes telles que la copie d'un fichier du répertoire de modèle vers le répertoire de destination. Une fonction pour la copie en masse existe également, mais elle est déconseillée.

Pour résoudre les problèmes ci-dessus, yeoman-easily :

* Fournit des fonctions d'I/O qui enveloppent `this.fs.xxx` et résolvent également les répertoires _template_ et _destination_ pour les cas courants (du modèle à la destination). Ces fonctions incluent `read`, `write`, `writeJSON`, `extendJSON`, `exists`, `copy`, et `copyTemplate`. J'ai une liste complète dans ma [documentation API](https://github.com/kristw/yeoman-easily/blob/master/docs/api.md).
* Fournit des fonctions pour la copie massive de fichiers statiques et dynamiques basées sur des motifs glob. Voir `easily.copyFiles()` dans l'exemple ci-dessous.

#### Avantages #5 : Chaînage de méthodes

yeoman-easily a été créé en pensant au chaînage et prend en charge le chaînage de méthodes pour un codage fluide.

### Mettre tout cela ensemble

Voici un exemple qui démontre tous ces avantages ensemble dans un seul générateur :

Le package yeoman-easily est maintenant disponible sur npm. Visitez le [dépôt github](https://github.com/kristw/yeoman-easily) pour plus de détails, la [documentation API](https://github.com/kristw/yeoman-easily/blob/master/docs/api.md) et des exemples. Je vous invite à soumettre des pull requests et des rapports de bugs.