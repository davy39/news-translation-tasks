---
title: Comment j'ai automatisé ma recherche d'emploi en construisant un crawler web
  à partir de zéro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T15:53:01.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-a-web-crawler-to-automate-my-job-search-f825fb5af718
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xzmVR8pbbBgB-f1JR9s1mg.png
tags:
- name: jobs
  slug: jobs
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Comment j'ai automatisé ma recherche d'emploi en construisant un crawler
  web à partir de zéro
seo_desc: 'By Zhia Chong

  The story of how it began

  It was midnight on a Friday, my friends were out having a good time, and yet I was
  nailed to my computer screen typing away.

  Oddly, I didn’t feel left out.

  I was working on something that I thought was genuinel...'
---

Par Zhia Chong

### L'histoire de comment tout a commencé

C'était minuit un vendredi, mes amis étaient dehors en train de s'amuser, et pourtant j'étais cloué à mon écran d'ordinateur en train de taper.

Étrangement, je ne me sentais pas exclu.

Je travaillais sur quelque chose que je trouvais vraiment intéressant et génial.

Je venais tout juste de sortir de l'université, et j'avais besoin d'un emploi. Quand je suis parti pour Seattle, j'avais un sac à dos rempli de manuels universitaires et quelques vêtements. Je pouvais faire tenir tout ce que je possédais dans le coffre de ma Honda Civic de 2002.

Je n'aimais pas beaucoup socialiser à l'époque, alors j'ai décidé de m'attaquer à ce problème de recherche d'emploi de la meilleure façon que je connaissais. J'ai essayé de construire une application pour le faire à ma place, et cet article parle de la façon dont je l'ai fait. ?

### Commencer avec Craigslist

J'étais dans ma chambre, en train de construire furieusement un logiciel qui m'aiderait à collecter et à répondre aux personnes qui cherchaient des ingénieurs logiciels sur [Craigslist](https://seattle.craigslist.org/). Craigslist est essentiellement le marché de l'Internet, où vous pouvez aller et trouver des choses à vendre, des services, des publications communautaires, et ainsi de suite.

![Image](https://cdn-media-1.freecodecamp.org/images/8blgV5gKhKM7Y1XtRALuFLDM1Gwref00CSLs)
_Craigslist_

À ce moment-là, je n'avais jamais construit une application complète. La plupart des choses sur lesquelles j'ai travaillé à l'université étaient des projets académiques qui impliquaient la construction et l'analyse d'arbres binaires, de graphiques informatiques et de modèles simples de traitement du langage.

J'étais vraiment un "newb".

Cela dit, j'avais toujours entendu parler de ce nouveau langage de programmation "hot" appelé Python. Je ne connaissais pas beaucoup Python, mais je voulais me salir les mains et en apprendre davantage à ce sujet.

Alors j'ai mis deux et deux ensemble, et j'ai décidé de construire une petite application en utilisant ce nouveau langage de programmation.

![Image](https://cdn-media-1.freecodecamp.org/images/xsXLiP4vQtB4idFgLrFFFmYsMonJHAzY2nrE)

### Le parcours pour construire un prototype (fonctionnel)

J'avais un ordinateur portable [BenQ](https://www.engadget.com/2007/11/19/benq-intros-the-joybook-r43-laptop/) d'occasion que mon frère m'avait donné quand je suis parti pour l'université que j'utilisais pour le développement.

Ce n'était pas le meilleur environnement de développement, loin de là. J'utilisais Python 2.4 et une ancienne version de [Sublime text](https://www.sublimetext.com/2), mais le processus d'écriture d'une application à partir de zéro était vraiment une expérience exaltante.

Je ne savais pas encore ce que je devais faire. J'essayais diverses choses pour voir ce qui fonctionnait, et ma première approche était de trouver comment je pouvais accéder facilement aux données de Craigslist.

J'ai cherché sur Craigslist pour voir s'ils avaient une API REST disponible publiquement. À mon grand dam, ils n'en avaient pas.

Cependant, j'ai trouvé la _prochaine meilleure chose_.

Craigslist avait un [flux RSS](https://www.craigslist.org/about/rss) qui était disponible publiquement pour un usage personnel. Un flux RSS est essentiellement un **résumé lisible par ordinateur** des mises à jour qu'un site web envoie. Dans ce cas, le flux RSS me permettrait de récupérer les nouvelles offres d'emploi dès qu'elles étaient publiées. C'était **parfait** pour mes besoins.

![Image](https://cdn-media-1.freecodecamp.org/images/2i0Kuh464TY2icrXndbP8YA91H3LEXCSh6YH)
_Exemple de ce à quoi ressemble un flux RSS_

Ensuite, j'avais besoin d'un moyen de lire ces flux RSS. Je ne voulais pas les parcourir manuellement moi-même, car cela aurait été une perte de temps et cela n'aurait pas été différent de naviguer sur Craigslist.

À cette époque, j'ai commencé à réaliser la puissance de Google. Il y a une blague récurrente selon laquelle les ingénieurs logiciels passent la plupart de leur temps à chercher des réponses sur Google. Je pense qu'il y a définitivement une part de vérité là-dedans.

Après un peu de recherche sur Google, j'ai trouvé ce post utile sur [StackOverflow](https://stackoverflow.com/questions/10353021/is-there-a-developers-api-for-craigslist-org) qui décrivait comment rechercher dans un flux RSS de Craigslist. C'était une sorte de fonctionnalité de filtrage que Craigslist fournissait gratuitement. Tout ce que je devais faire était de passer un paramètre de requête spécifique avec le mot-clé qui m'intéressait.

Je me concentrais sur la recherche d'emplois liés au logiciel à Seattle. Avec cela, j'ai tapé cette URL spécifique pour rechercher des annonces à Seattle contenant le mot-clé "software".

> [https://seattle.craigslist.org/search/sss?format=rss&query=software](https://seattle.craigslist.org/search/sss?format=rss&query=software)

Et voilà ! Cela a fonctionné **magnifiquement**.

![Image](https://cdn-media-1.freecodecamp.org/images/ygmbnQQRIoY4p7hY8MJmrgXIZcKvBT6nkbAj)
_Exemple de flux RSS pour Seattle avec "software" dans le titre_

### La plus belle soupe que j'ai jamais goûtée

Je n'étais cependant pas convaincu que mon approche fonctionnerait.

Premièrement, le **nombre d'annonces était limité**. Mes données ne contenaient pas **toutes** les offres d'emploi disponibles à Seattle. Les résultats retournés n'étaient qu'un sous-ensemble du tout. Je cherchais à jeter le filet le plus large possible, donc j'avais besoin de connaître toutes les offres d'emploi disponibles.

Deuxièmement, j'ai réalisé que le flux RSS **ne contenait aucune information de contact**. C'était un bummer. Je pouvais trouver les annonces, mais je ne pouvais pas contacter les annonceurs à moins de filtrer manuellement ces annonces.

![Image](https://cdn-media-1.freecodecamp.org/images/k-Rk7q-1b8bSgOqcNodm7xMMvbxNbYkRw75z)
_Capture d'écran du lien de réponse de Craigslist_

Je suis une personne aux multiples compétences et intérêts, mais faire un travail manuel répétitif n'en fait pas partie. J'aurais pu embaucher quelqu'un pour le faire à ma place, mais je survivais à peine avec des nouilles ramen à 1 dollar. Je ne pouvais pas me permettre de dépenser pour ce projet secondaire.

C'était une impasse. Mais ce n'était pas **la** fin.

### Itération continue

De ma première tentative ratée, j'ai appris que Craigslist avait un flux RSS que je pouvais filtrer, et que chaque annonce avait un lien vers l'annonce elle-même.

Eh bien, si je pouvais accéder à l'annonce réelle, alors peut-être que je pourrais extraire l'adresse e-mail de celle-ci ? ? Cela signifiait que je devais trouver un moyen de récupérer les adresses e-mail des annonces originales.

Une fois de plus, j'ai ouvert mon fidèle Google et j'ai recherché "façons de parser un site web".

Avec un peu de recherche sur Google, j'ai trouvé un petit outil Python cool appelé [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/). C'est essentiellement un outil pratique qui vous permet de parser un arbre [DOM](https://www.w3schools.com/js/js_htmldom.asp) entier et vous aide à comprendre comment une page web est structurée.

Mes besoins étaient simples : j'avais besoin d'un outil facile à utiliser qui me permettrait de collecter des données à partir d'une page web. BeautifulSoup cochait les deux cases, et plutôt que de passer plus de temps à choisir **le meilleur outil**, j'ai choisi un outil qui fonctionnait et j'ai continué. Voici une [liste d'alternatives](https://www.quora.com/What-are-some-good-Python-libraries-for-parsing-HTML-other-than-Beautiful-Soup) qui font quelque chose de similaire.

![Image](https://cdn-media-1.freecodecamp.org/images/-KvuqnYZ0chIKSyEuBZhJyqdhDz36xCFcQeY)
_Page d'accueil de BeautifulSoup_

> Note de côté : J'ai trouvé ce tutoriel génial [tutoriel](https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe) qui parle de la façon de scraper des sites web en utilisant Python et BeautifulSoup. Si vous êtes intéressé à apprendre à scraper, alors je vous recommande de le lire.

Avec cet nouvel outil, mon flux de travail était prêt.

![Image](https://cdn-media-1.freecodecamp.org/images/VEYEIzhRPaaR21nH5IKSYy6Peza95XD0OlEr)
_Mon flux de travail_

J'étais maintenant prêt à m'attaquer à la prochaine tâche : extraire les adresses e-mail des annonces réelles.

Maintenant, voici le truc cool à propos des technologies open-source. Elles sont gratuites et fonctionnent très bien ! C'est comme obtenir une glace gratuite par une chaude journée d'été, **et** un cookie aux pépites de chocolat fraîchement sorti du four.

BeautifulSoup vous permet de rechercher des balises HTML spécifiques, ou des marqueurs, sur une page web. Et Craigslist a structuré leurs annonces de telle manière qu'il était facile de trouver des adresses e-mail. La balise était quelque chose comme "email-reply-link", qui indique essentiellement qu'un lien de courriel est disponible.

À partir de ce moment, tout a été facile. Je me suis appuyé sur la fonctionnalité intégrée fournie par BeautifulSoup, et avec juste quelques manipulations simples, j'ai pu extraire facilement les adresses e-mail des publications de Craigslist.

### Mettre les choses ensemble

En une heure environ, j'avais mon premier MVP. J'avais construit un scraper web qui pouvait collecter des adresses e-mail et répondre aux personnes recherchant des ingénieurs logiciels dans un rayon de 100 miles autour de Seattle.

![Image](https://cdn-media-1.freecodecamp.org/images/mTnFGw-linWi0nN4uWoCgQ7TLJ8n0OkZ9-tX)
_Capture d'écran du code_

J'ai ajouté divers modules complémentaires au script original pour faciliter la vie. Par exemple, j'ai sauvegardé les résultats dans un fichier CSV et une page HTML afin de pouvoir les analyser rapidement.

Bien sûr, il manquait de nombreuses autres fonctionnalités notables, telles que :

* la capacité à journaliser les adresses e-mail que j'ai envoyées
* des règles de fatigue pour éviter d'envoyer trop d'e-mails aux personnes que j'avais déjà contactées
* des cas particuliers, comme certains e-mails nécessitant un Captcha avant d'être affichés pour dissuader les bots automatisés (ce que j'étais)
* Craigslist n'autorisait pas les scrapers sur leur plateforme, donc je me faisais bannir si j'exécutais le script trop souvent. (J'ai essayé de changer entre divers VPN pour essayer de "tricher" Craigslist, mais cela n'a pas fonctionné), et
* Je ne pouvais toujours pas récupérer **toutes** les annonces sur Craigslist

La dernière était un coup dur. Mais je me suis dit que si une annonce était là depuis un moment, peut-être que la personne qui l'avait publiée ne cherchait plus. C'était un compromis avec lequel je pouvais vivre.

Toute l'expérience ressemblait à une partie de [Tetris](https://fr.wikipedia.org/wiki/Tetris). Je savais quel était mon objectif final, et mon vrai défi était d'assembler les bonnes pièces pour atteindre cet objectif spécifique. Chaque pièce du puzzle m'a emmené dans un voyage différent. C'était difficile, mais agréable néanmoins et j'ai appris quelque chose de nouveau à chaque étape.

### Leçons apprises

Ce fut une expérience révélatrice, et j'ai fini par en apprendre un peu plus sur le fonctionnement d'Internet (et de Craigslist), sur la façon dont divers outils différents peuvent travailler ensemble pour résoudre un problème, et j'ai obtenu une petite histoire cool que je peux partager avec des amis.

D'une certaine manière, c'est un peu comme le fonctionnement des technologies de nos jours. Vous trouvez un gros problème épineux que vous devez résoudre, et vous ne voyez aucune solution immédiate et évidente. Vous décomposez le gros problème épineux en plusieurs morceaux gérables, puis vous les résolvez un par un.

En regardant en arrière, mon problème était le suivant : **comment puis-je utiliser ce répertoire génial sur Internet pour atteindre rapidement des personnes ayant des intérêts spécifiques** ? Il n'y avait aucun produit ou solution connu disponible pour moi à l'époque, alors je l'ai décomposé en plusieurs morceaux :

1. Trouver toutes les annonces sur la plateforme
2. Collecter les informations de contact de chaque annonce
3. Leur envoyer un e-mail si les informations de contact existent

C'est tout ce qu'il y avait à faire. **La technologie n'a servi que de moyen pour atteindre le but**. Si j'avais pu utiliser une feuille de calcul Excel pour le faire à ma place, j'aurais opté pour cela à la place. Cependant, je ne suis pas un guru d'Excel, et j'ai donc choisi l'approche qui avait le plus de sens pour moi à l'époque.

#### Domaines d'amélioration

Il y avait de nombreux domaines dans lesquels je pouvais m'améliorer :

* J'ai choisi un langage que je ne connaissais pas très bien au début, et il y avait une courbe d'apprentissage au début. Ce n'était pas trop terrible, car Python est très facile à apprendre. Je recommande vivement à tout enthousiaste du logiciel débutant d'utiliser cela comme premier langage.
* **Trop dépendre des technologies open-source. Les logiciels open source ont aussi leurs propres problèmes**. Il y avait plusieurs bibliothèques que j'ai utilisées qui n'étaient plus en développement actif, donc j'ai rencontré des problèmes tôt. Je ne pouvais pas importer une bibliothèque, ou la bibliothèque échouait pour des raisons apparemment anodines.
* **S'attaquer à un projet seul peut être amusant, mais peut aussi causer beaucoup de stress**. Vous aurez besoin de beaucoup d'élan pour livrer quelque chose. Ce projet était rapide et facile, mais il m'a tout de même pris quelques week-ends pour ajouter les améliorations. Au fur et à mesure que le projet avançait, j'ai commencé à perdre ma motivation et mon élan. Après avoir trouvé un emploi, j'ai complètement abandonné le projet.

### Ressources et outils que j'ai utilisés

[The Hitchhiker's Guide to Python](https://amzn.to/2J73RtJ) — Un excellent livre pour apprendre Python en général. Je recommande Python comme premier langage de programmation pour les débutants, et je parle de la façon dont je l'ai utilisé pour obtenir des offres de plusieurs entreprises de premier plan dans mon article [ici](https://medium.freecodecamp.org/how-i-landed-offers-from-microsoft-amazon-and-twitter-without-an-ivy-league-degree-d62cfe286eb8).

[DailyCodingProblem](http://dailycodingproblem.com/zhiachong) : C'est un service qui envoie des problèmes de codage quotidiens à votre e-mail, et qui propose certains des problèmes de programmation les plus récents des entreprises technologiques de premier plan. Utilisez mon code de réduction, zhiachong, pour obtenir 10 $ de réduction !

[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) — L'outil utilitaire pratique que j'ai utilisé pour construire mon crawler web

[Web Scraping with Python](https://amzn.to/2sa43xR) — Un guide utile pour apprendre comment fonctionne le web scraping avec Python.

[Lean Startup](https://amzn.to/2GLnRN6) - J'ai appris le prototypage rapide et la création d'un MVP pour tester une idée à partir de ce livre. Je pense que les idées présentées ici sont applicables dans de nombreux domaines différents et m'ont également aidé à mener à bien le projet.

[Evernote](http://evernote.com/) — J'ai utilisé Evernote pour compiler mes pensées pour cet article. Je le recommande vivement — je l'utilise pour pratiquement _tout_ ce que je fais.

[Mon ordinateur portable](https://amzn.to/2s9sziy)- C'est mon ordinateur portable actuel à la maison, configuré comme une station de travail. Il est beaucoup, _beaucoup plus facile_ à utiliser qu'un ancien ordinateur portable BenQ, mais les deux fonctionneraient pour le travail général de programmation.

**Crédits :**

[Brandon O'Brien](https://twitter.com/hakczar), mon mentor et bon ami, pour la relecture et les commentaires précieux sur la façon d'améliorer cet article.

[Leon Tager](https://twitter.com/OSPortfolio), mon collègue et ami qui relit et me comble de sagesse financière tant nécessaire.

Vous pouvez vous inscrire pour recevoir des nouvelles de l'industrie, des anecdotes aléatoires et être le premier à savoir quand je publie de nouveaux articles en vous inscrivant [ici](http://eepurl.com/dnt9Sf).

---

_Zhia Chong est ingénieur logiciel chez Twitter. Il travaille au sein de l'équipe Ads Measurement à Seattle, mesurant l'impact des publicités et le retour sur investissement pour les annonceurs. L'équipe est en train de recruter !_

_Vous pouvez le trouver sur [Twitter](https://twitter.com/zhiachong) et [LinkedIn](https://www.linkedin.com/in/zhiachong/)._