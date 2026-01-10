---
title: Ce que j'ai appris lors de mon premier stage en développement logiciel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-25T16:27:43.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-from-my-first-ever-software-development-internship-701aa756a72f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*IPx0r2K1gi55ZWAx
tags:
- name: internships
  slug: internships
- name: Ruby on Rails
  slug: ruby-on-rails
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Ce que j'ai appris lors de mon premier stage en développement logiciel
seo_desc: 'By Viraj Chavan

  I was a student at an engineering college in India. After 3 and a half years years
  of learning computer science academically, I now had a chance to test my knowledge
  in the real world through an internship.

  In this article, I’ll be sh...'
---

Par Viraj Chavan

J'étais étudiant dans une école d'ingénieurs en Inde. Après 3 ans et demi d'apprentissage académique en informatique, j'ai enfin eu l'occasion de tester mes connaissances dans le monde réel grâce à un stage.

Dans cet article, je vais partager mon expérience de stage chez [Josh Software](http://joshsoftware.com/), à Pune, dans l'espoir que cela soit utile à d'autres étudiants en informatique et en génie logiciel qui recherchent des stages.

Comme la plupart de mes collègues à l'université, j'avais une vision très limitée du développement logiciel en général et je ne savais pas à quoi m'attendre d'un stage.

Heureusement pour moi, on m'a assigné un projet en cours, basé sur Ruby on Rails, un sujet pour lequel je m'étais déjà intéressé.

Après avoir appris PHP et MySQL en deuxième année de mes études, j'ai construit une application web basique, et tout ce qu'elle faisait était quelques opérations CRUD (Create, Read, Update, Destroy). Je me souviens avoir parlé avec un ami qui avait des compétences similaires aux miennes, et avoir dit « Même nous pouvons construire Facebook maintenant que nous connaissons PHP et MySQL ! »

À l'époque, les choses semblaient ridiculement simples. Maintenant, je comprends à quel point la construction et la maintenance d'un logiciel peuvent être complexes.

Voici donc ce que j'ai appris lors de mon stage en travaillant sur un projet en cours.

### Leçons générales

#### L'échelle fait une énorme différence

![Image](https://cdn-media-1.freecodecamp.org/images/1*SsdGma80xb-AXYYFbEle5A.png)

* Combien d'utilisateurs vont utiliser le logiciel ?
* Quelle quantité de données sera traitée ?
* Quels sont les temps de réponse attendus pour une fonction ?

Ce sont des questions auxquelles nous, en tant qu'étudiants, pensons rarement. Nos projets universitaires étaient généralement à court terme. Dans les projets du monde réel, cependant, les questions ci-dessus affectent fondamentalement les décisions concernant le matériel, les technologies/outils à utiliser, l'architecture du système, les algorithmes, et ainsi de suite.

#### Travailler avec une grande base de code

À l'université, nous travaillions sur des projets qui avaient environ 15 à 20 fichiers. Construit en moins d'une semaine, l'ensemble du projet pouvait être **compris** en quelques heures.

Maintenant, le projet sur lequel je travaille compte des centaines de fichiers répartis dans des dizaines de dossiers. Il peut prendre des mois pour comprendre l'ensemble du projet, et des heures pour déboguer un bug qui s'étend sur plusieurs fichiers. Et la première fois que vous regardez l'ensemble du répertoire du projet, vous ne savez pas par où commencer pour comprendre le code.

#### Écrire du code maintenable

Savoir que le code que vous écrivez sera lu, compris et amélioré/modifié par quelqu'un d'autre (ou même par vous-même) à l'avenir vous incite à écrire du code maintenable.

À l'université, je me concentrais uniquement sur l'achèvement de la fonctionnalité attendue, sans jamais me soucier de savoir si le code que j'écrivais était maintenable.

Cela a abouti à des morceaux de code désorganisés qui fonctionnaient d'une manière ou d'une autre à ce moment-là. Mais deux jours plus tard, même moi, je ne comprenais plus pourquoi j'avais écrit un certain morceau de code de cette façon. Et modifier une partie du code cassait presque toujours d'autres parties. ?

**La maintenabilité du code est plus facile à reconnaître par son absence**, comme lorsque quelque chose que vous pensiez devoir prendre une heure finit par prendre une semaine.

#### Utiliser un système de contrôle de version - correctement

Lorsque j'ai commencé à construire de petits logiciels, tous les fichiers existaient sur ma propre machine de développement, et peut-être étaient-ils sauvegardés sur Google Drive en tant que fichiers réguliers.

Ensuite, j'ai découvert GitHub, mais je l'utilisais simplement comme un endroit sûr pour stocker mon code. J'utilisais l'application de bureau GitHub pour commiter toutes les modifications uniquement sur la branche master. Je hésitais même à l'utiliser via la ligne de commande.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0o9GZUzXiNnI4poEvxvy8g.png)

Maintenant, il ne se passe pas un jour sans que j'utilise Git. C'est un outil formidable pour écrire du code de manière collaborative, le développement distribué, la création de branches pour de nouvelles fonctionnalités, les pull requests, et ainsi de suite.

Voici un [petit article](https://www.git-tower.com/learn/git/ebook/en/command-line/basics/why-use-version-control) sur pourquoi les systèmes de contrôle de version sont géniaux !

#### L'importance d'utiliser une approche de développement piloté par les tests

Lors de mon stage, on m'a assigné à travailler sur une nouvelle fonctionnalité qui devait être ajoutée au projet principal.

J'ai écrit le code et j'ai testé s'il fonctionnait comme prévu. Il fonctionnait parfaitement, ou du moins le pensais-je. J'ai déployé la fonctionnalité en production avec confiance, et je suis passé à autre chose.

Après quelques heures, [Rollbar](https://rollbar.com), un outil de rapport d'erreurs en temps réel, a explosé avec un nombre d'erreurs dans notre code déployé en production. J'ai vérifié les erreurs et elles semblaient sans rapport avec quoi que ce soit sur quoi j'avais travaillé.

Après un certain débogage, toutes ces erreurs remontaient à une seule méthode. Une méthode qui était appelée à de nombreux endroits, et dans laquelle j'avais modifié une seule ligne, sans avoir vérifié où ailleurs elle était utilisée.

Cela aurait pu être évité si le code qui utilisait cette méthode avait des cas de test écrits pour lui, et si j'avais vérifié si tous les cas de test s'exécutaient avec succès avant de déployer le code. Cela m'a fait réaliser l'importance du développement piloté par les tests.

[Voici un article](http://sd.jtimothyking.com/2006/07/11/twelve-benefits-of-writing-unit-tests-first/) pour comprendre pourquoi l'écriture de cas de test est importante.

### Choses spécifiques à Ruby on Rails / Développement Web

#### L'architecture MVC

À l'époque de l'université, lorsque je développons des applications en PHP, je n'avais aucune idée de ce que étaient le Modèle, la Vue et le Contrôleur. Tout projet était si complexe et désorganisé que je ne pouvais pas trouver dans quel fichier un morceau de logique important était écrit. Les scripts PHP intégrés dans le HTML à des endroits étranges et j'avais placé tous les fichiers dans un seul dossier.

Ensuite, j'ai appris le framework Rails, et je me suis familiarisé avec l'architecture MVC.

> Modèle-Vue-Contrôleur (MVC) est un modèle architectural qui sépare une application en trois composants logiques principaux - Modèle, Vue et Contrôleur. Chacun de ces composants est conçu pour gérer des aspects spécifiques du développement d'une application ([source](https://medium.freecodecamp.org/model-view-controller-mvc-explained-through-ordering-drinks-at-the-bar-efcba6255053))

MVC simplifie vraiment les choses et est une partie importante de nombreux frameworks majeurs.

#### Travailler avec des bases de données

Au cours des 6 derniers mois, je n'ai écrit aucune requête SQL directe pour une base de données. Pourtant, je travaille avec des bases de données tous les jours, même en effectuant des opérations complexes. Cela est grâce à l'ORM (Object Relational Mapper) que Ruby On Rails utilise.

Les ORM convertissent un langage de programmation orienté objet tel que Ruby en langage de base de données pour effectuer des opérations. Ce qui rend l'accès aux données plus portable et abstrait des requêtes de base de données nécessaires lors de la manipulation des données.

Grâce à l'ORM, il est beaucoup plus facile d'interroger la base de données. Cela offre un grand [avantage aux débutants](https://m.signalvnoise.com/conceptual-compression-means-beginners-dont-need-to-know-sql-hallelujah-661c1eaed983), qui peuvent commencer à écrire des applications sans même connaître SQL.

#### Écrire/Utiliser des API REST (Interfaces de Programmation d'Applications)

Les [API](https://hackernoon.com/what-are-web-apis-c74053fa4072) facilitent la communication entre les applications.

Les API rendent les fonctionnalités d'autres applications facilement accessibles à notre application. Par exemple, j'ai une fois développé une application de planification de road trip qui utilisait l'API Google Maps pour montrer divers lieux sur une carte qu'un utilisateur pouvait visiter sur un itinéraire particulier.

Les API peuvent également être utilisées pour séparer complètement le front-end et le back-end. Par exemple, nous pouvons écrire le back-end comme une application Rails uniquement API qui peut être utilisée par un site web, une application Android/iOS, ou même certaines applications tierces.

#### Utiliser ElasticSearch pour la recherche

Bien que je ne sache pas encore grand-chose sur ElasticSearch, j'ai appris que c'est une base de données NOSQL distribuée en texte intégral. Il agit comme un moteur de recherche distribué qui est incroyablement facile à mettre à l'échelle et retourne des résultats à une vitesse fulgurante.

Pourquoi en aurions-nous besoin pour la recherche ? Parce qu'avoir des millions d'enregistrements dans une base de données régulière peut rendre les recherches efficaces vraiment complexes.   
Avec Elasticsearch, nous pouvons indexer les documents à rechercher et il peut effectuer des requêtes sur tous ces millions de documents et retourner des résultats précis en une **fraction de seconde**.

Elasticsearch dispose d'une API Restful, ce qui facilite grandement l'interrogation des recherches et l'obtention des résultats.

[Voici un tutoriel](http://joelabrahamsson.com/elasticsearch-101/) qui m'a aidé, et voici quelques [cas d'utilisation](https://www.elastic.co/blog/found-uses-of-elasticsearch) d'Elasticsearch.

#### Utiliser des tâches asynchrones/en arrière-plan

Parfois, l'utilisateur effectuera une action sur notre application qui prend un temps considérable à compléter. Nous ne voulons pas que l'utilisateur attende là que cette action se termine, nous l'envoyons donc à un worker en arrière-plan.

[Voici un lien](https://blog.iron.io/every-web-application-needs-background/) qui explique cela mieux.

Dans Ruby On Rails, je suis tombé sur [Sidekiq](https://sidekiq.org/), qui rend [facile la gestion des tâches en arrière-plan de manière efficace](https://medium.com/@aledalgrande/3-ways-to-make-your-web-pages-more-responsive-with-sidekiq-a3fcb1e9dcef).

Merci d'avoir lu ! Si vous avez trouvé cet article utile, donnez-moi quelques applaudissements. ?

Il reste encore un long chemin à parcourir !

Consultez mon profil Github [ici](https://github.com/virajvchavan).