---
title: Comment je n'ai PAS codé une application d'écriture collaborative
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-18T17:19:33.000Z'
originalURL: https://freecodecamp.org/news/how-i-did-not-code-a-collaborative-writing-app
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/code-free-1200-2.png
tags:
- name: bubble
  slug: bubble
- name: code
  slug: code
- name: Entrepreneurship
  slug: entrepreneurship
- name: lean startup
  slug: lean-startup
- name: web
  slug: web
seo_title: Comment je n'ai PAS codé une application d'écriture collaborative
seo_desc: 'By Eric Burel

  Twaikura, haikus but funnier

  As easy as ABC: some stranger on the Internet starts a 120 characters story, some
  stranger on the Internet finishes it. And that makes a Twaiku (tweet + haiku). Twaikus
  can be funny, serious, artistic, it’s ...'
---

Par Eric Burel

## Twaikura, des haikus mais plus drôles

Aussi simple que ABC : un inconnu sur Internet commence une histoire de 120 caractères, un autre inconnu sur Internet la termine. Et cela fait un Twaiku (tweet + haiku). Les Twaikus peuvent être drôles, sérieux, artistiques, c'est à vous de voir. 

![Image](https://www.freecodecamp.org/news/content/images/2020/02/logo_256.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/02/twaiku.png)

Alors, en tant que développeur, implémenter quelque chose comme ça ne devrait pas être difficile, n'est-ce pas ? Oui, mais non. Voici l'histoire de comment cela m'a pris plusieurs années pour créer Twaikura et comment vous pourriez faire la même chose en quelques heures.

## Retour sur TwentyParts et pourquoi il n'a jamais vu le jour

TwentyParts était mon premier "concept entrepreneurial" en 2015. Comme vous pouvez l'imaginer, l'idée est d'écrire une histoire en 20 parties, chaque partie étant écrite par un auteur différent. 

J'étais étudiant en informatique à l'époque et il m'a fallu 2 mois pour sortir une première ébauche. Le résultat était désastreux. Je ne connaissais même pas le concept de "framework", imaginez le code. Le concept était trop complexe, l'interface inutilisable.

Je n'ai pas abandonné. Quelques mois plus tard, en 2016, j'ai eu une version simplifiée de TwentyParts, HiKoo. J'ai limité la longueur d'une histoire à 3 tweets. Et au lieu de me précipiter sur le développement, j'ai créé des maquettes en utilisant un outil merveilleux nommé MarvelApp.

Maintenant, j'avais une super UI et tout, mais pas de code fonctionnel. Une autre application qui n'a jamais vu le jour.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/hikoo.png)
_Ça a l'air bien, mais ça ne fonctionne pas_

Avance rapide jusqu'à aujourd'hui. J'ai obtenu mon diplôme. J'ai créé ma société de conseil, LBKE. J'ai développé des plateformes SaaS complexes pour plusieurs clients. Et j'ai gardé cette question en tête :

> Qu'est-ce qui m'empêche de recréer TwentyParts, maintenant que je suis rapide, compétent et surconfiant ?

Après tout, cela ne prendrait qu'une semaine de travail complète de nos jours. Pourtant, il y a un problème : je ne suis plus étudiant. Avec une heure de libre ici et là, une "semaine de travail complète" peut s'étendre sur plusieurs mois. Trop lent.

## Comment coder vite : ne le faites pas.

J'ai exploré en profondeur les domaines du développement web rapide. Vous avez peut-être lu mes articles précédents sur freeCodeCamp à propos de [Vulcan, un framework basé sur Meteor qui me rend très productif.](https://www.freecodecamp.org/news/how-i-built-an-app-with-vulcan-js-in-four-days-6368814077b1/)

Toutes ces recherches m'ont conduit à la même conclusion : le meilleur code est celui que vous n'écrivez pas. 

Il existe de nombreuses façons de NE PAS écrire de code, même pour un développeur. L'échafaudage, la programmation déclarative, l'utilisation de snippets ou l'utilisation d'un ORM sont autant de méthodes pour contourner l'écriture de code. L'utilisation de l'open source est un autre excellent exemple. Certains pourraient même penser que les développeurs sont un peu paresseux – mais ne le sont-ils pas ?

Pourtant, des compétences minimales en développement web sont encore nécessaires. Cela signifie une réflexion minutieuse, beaucoup de lecture de documentation, du débogage, etc. En fin de compte, le temps nécessaire pour créer une application entièrement fonctionnelle ne peut être réduit que jusqu'à un certain point.

Vous savez quoi ? Utiliser un framework massif pour accélérer les développements donne parfois l'impression de tricher. Et si je n'avais pas ces compétences ? Et si je n'étais pas développeur ? Je n'aurais pas d'autre choix que d'embrasser la "voie sans code". Et c'est ce que j'ai fait.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/code-free-1200.png)
_Détendez-vous, le code sera en vacances pour le reste de cet article_

## Innovations étincelantes pour les non-développeurs web

Les solutions sans code ont été assez mauvaises dans le passé. Limitées, difficiles à étendre, propriétaires, chères, la liste est longue. Mais certains outils récents commencent à être dignes d'intérêt.

Je vais me concentrer spécifiquement sur Bubble. Son système de plugins couplé à ses fonctionnalités de gestion de données en fait la solution la plus complète sur le marché actuellement. Voici quelques fonctionnalités clés et comment je les ai utilisées pour construire Twaikura.

### L'éditeur d'interface utilisateur

Bubble propose un éditeur WYSIWYG (What You See Is What You Get) pour créer l'interface utilisateur de l'application. Vous placez vos blocs de contenu où vous le souhaitez et configurez leur contenu.

Il est basé sur une grille, vous pouvez donc avoir un alignement parfait au pixel près. Il gère la réactivité. Vous devriez donc être en mesure de créer des designs aussi complexes que vous le souhaitez.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/ui-bubble.png)
_Construction de l'interface de Twaikura en utilisant l'éditeur WYSIWYG._

Mais je vais être honnête, je ne suis pas un énorme fan. Plus précisément, je ne suis pas très doué avec ça. C'est très différent à la fois de l'écriture de HTML/CSS et de l'utilisation d'outils de design basés sur le web comme Figma, donc il y a une courbe d'apprentissage.

J'ai fini par m'en tenir à un style old school Windows 98. Avec un peu d'imagination, vous pourriez même croire qu'il a une certaine esthétique "V a p o r w a v e".

### Penser en workflows

La fonctionnalité la plus impressionnante de Bubble pour moi est ses "Workflows". Cela vous permet de décrire des processus complexes dans un langage visuel. Il peut mélanger la gestion des données (validation et stockage d'un Twaiku, envoi d'un email) et l'expérience utilisateur (réinitialisation d'un formulaire, rafraîchissement de la page) de manière transparente. Vous n'avez pas besoin de diviser mentalement le workflow entre le frontend et le backend comme vous le feriez dans une application web traditionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/workflows.png)
_Workflow de création de Twaiku_

Ce workflow d'exemple est déclenché lorsque l'utilisateur souhaite soumettre la deuxième partie d'un Twaiku. Il créera une "Fin de Twaiku" dans la base de données, la liera à un "Début de Twaiku" et réinitialisera le formulaire. Je pourrais également afficher un message de succès, envoyer un email à un modérateur, etc. Visualiser l'ensemble du workflow dans une seule timeline est très intuitif.

### Gestion complète des données

Bubble est livré avec une base de données relationnelle et des fonctionnalités de filtrage complètes. Cela signifie que vous pouvez facilement créer à la fois des formulaires et des listes de données. Par exemple, le bloc "Lire les derniers Twaikus" chargera tous les Twaikus valides.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/twaikus-list.png)

Les plugins peuvent aider à sécuriser votre contenu. Par exemple, il existe un plugin ReCaptcha pour ajouter des CAPTCHAs à votre formulaire en quelques minutes. Cela est important car la sécurité est généralement laissée de côté dans les étapes de prototypage. Les bots malveillants et les hackers ne se soucient pas que vous soyez un "lean startup-er", et ils ne manqueront pas une opportunité de spammer ou de pirater votre site web.

## Quelques heures de travail pour une application qui fonctionne

Je ne vais pas décrire toutes les fonctionnalités de Bubble, car il en a beaucoup plus. La conclusion est qu'il a été suffisamment puissant pour écrire une application comme Twaikura. Au lieu d'écrire des tonnes de code médiocre qui finira à la poubelle, au lieu de créer un prototype visuel aussi vivant que la créature de Frankenstein, j'ai simplement créé quelque chose qui fonctionne.

Mon site web est-il génial ? Honnêtement, pas encore. Fait-il le travail ? Absolument. J'ai pris du plaisir à le créer, cela ne m'a coûté que quelques heures, et je suis en mesure de tester le concept de la manière la plus directe possible. La partie la plus longue a été d'écrire cet article.

Je recommande particulièrement les outils sans code pour les personnes qui veulent apprendre le développement web. Prendre beaucoup de temps pour produire des fonctionnalités simples peut sembler frustrant au début. Utiliser un outil sans code parallèlement à la programmation traditionnelle est un moyen de continuer à s'amuser. C'est aussi instructif, car même si vous n'écrivez pas de code, vous devez toujours penser comme un développeur : concevoir des workflows conditionnels, structurer une base de données, valider des formulaires... C'est un gagnant-gagnant.

Je ne vais pas devenir un évangéliste du sans code, mais Bubble est un excellent ajout à ma ceinture d'outils. Et cela pourrait être un excellent ajout à la vôtre aussi !

Merci pour la lecture. Si vous avez aimé cet article, venez essayer une application Bubble en créant votre premier Twaiku sur [twaikura.com](http://twaikura.com) !

<a href="https://twitter.com/lbke_fr">
<img src="https://www.freecodecamp.org/news/content/images/2019/10/Medium-follow-2019.png" alt="Bannière Twitter LBKE" />
</a>