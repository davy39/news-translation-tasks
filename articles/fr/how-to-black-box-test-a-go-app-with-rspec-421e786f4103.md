---
title: Comment tester une application Go en boîte noire avec RSpec
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-16T23:06:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-black-box-test-a-go-app-with-rspec-421e786f4103
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3EftyhurldrDfAe0PuBHZQ.jpeg
tags:
- name: Go Language
  slug: go
- name: General Programming
  slug: programming
- name: Ruby on Rails
  slug: ruby-on-rails
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: Comment tester une application Go en boîte noire avec RSpec
seo_desc: 'By Dmitriy Lutsko

  Automated testing is all the rage in web development these days and goes on across
  the whole industry. A well-written test dramatically reduces the risk of accidentally
  breaking an application when you add new features or fix bugs. ...'
---

Par Dmitriy Lutsko

Les tests automatisés sont très populaires dans le développement web ces jours-ci et s'étendent à travers toute l'industrie. Un test bien écrit réduit considérablement le risque de casser accidentellement une application lorsque vous ajoutez de nouvelles fonctionnalités ou corrigez des bugs. Lorsque vous avez un système complexe construit à partir de plusieurs composants qui interagissent entre eux, il est incroyablement difficile de tester comment chaque composant interagit avec les autres.

Examinons comment écrire de bons tests automatiques pour développer des composants en Go et comment le faire en utilisant la bibliothèque RSpec dans Ruby on Rails.

### Ajout de Go à la stack technologique de notre projet

L'un des projets sur lesquels je travaille dans mon entreprise, [eTeam](https://eteam.io/), peut être divisé en un panneau d'administration, un tableau de bord utilisateur, un générateur de rapports et un processeur de requêtes qui gère les requêtes provenant de différents services intégrés à l'application.

La partie du projet qui traite les requêtes est la plus importante, nous devions donc maximiser sa fiabilité et sa disponibilité.

Dans le cadre d'une application monolithique, il y a un risque élevé qu'un bug affecte le processeur de requêtes, même lorsque des changements de code sont apportés dans des parties de l'application non liées à celui-ci. De même, il y a un risque de planter le processeur de requêtes lorsque d'autres composants sont sous une charge lourde. Le nombre de workers Nginx pour l'application est limité, ce qui peut causer des problèmes à mesure que la charge augmente. Par exemple, lorsque plusieurs pages gourmandes en ressources sont ouvertes simultanément dans le panneau d'administration, le processeur ralentit ou même fait planter toute l'application.

Ces risques, ainsi que la maturité du système en question — nous n'avons pas eu à apporter de changements majeurs pendant des mois — ont fait de cette application un candidat idéal pour créer un service séparé pour traiter les requêtes.

Nous avons décidé d'écrire le service séparé en Go, qui partageait l'accès à la base de données avec l'application Rails, laquelle restait responsable des changements dans la structure des tables. Avec seulement deux applications, un tel schéma avec une base de données partagée fonctionne bien. Voici à quoi cela ressemblait :

![Image](https://cdn-media-1.freecodecamp.org/images/1*3dV9gtMm5kAMTzojZ2Y3hQ.jpeg)

Nous avons écrit et déployé le service dans une instance Rails séparée. Ainsi, il n'était pas nécessaire de s'inquiéter que le processeur de requêtes soit affecté chaque fois que l'application Rails était déployée. Le service accepte directement les requêtes HTTP sans Nginx et n'utilise pas beaucoup de mémoire. On pourrait l'appeler une application minimaliste !

### Le problème avec les tests unitaires en Go

Nous avons créé des tests unitaires pour l'application Go où toutes les requêtes à la base de données étaient mockées. En plus d'autres arguments pour cette solution, l'application Rails principale était responsable de la structure de la base de données, ainsi l'application Go n'avait pas réellement les informations pour créer une base de données de test. La moitié du traitement était de la logique métier, tandis que l'autre moitié était des requêtes à la base de données, toutes mockées.

Les objets mockés sont beaucoup moins lisibles en Go qu'en Ruby. Chaque fois que de nouvelles fonctions étaient ajoutées pour lire des données depuis la base de données, nous devions ajouter des objets mockés lors de nombreux tests échoués qui avaient précédemment fonctionné. En fin de compte, de tels tests unitaires n'ont pas prouvé être très efficaces et étaient extrêmement fragiles.

### Notre solution

Afin de compenser ces inconvénients, nous avons décidé de couvrir le service avec des tests fonctionnels dans l'application Rails et de tester le service en Go comme une boîte noire. Les tests en boîte blanche n'auraient pas fonctionné dans tous les cas, car il était impossible d'utiliser Ruby pour entrer dans le service et voir si une méthode était appelée.

Cela signifie également que les requêtes envoyées via le service de test étaient impossibles à mock, ainsi nous avions besoin d'une autre application pour gérer et écrire ces tests. Quelque chose comme RequestBin aurait fonctionné, mais il devait fonctionner localement. Nous avions déjà écrit un utilitaire qui ferait l'affaire, donc nous avons décidé de l'utiliser.

Voici la configuration résultante :

1. RSpec compile et exécute le binaire Go avec la configuration dans laquelle l'accès à la base de données de test est spécifié ainsi qu'un port particulier pour recevoir les requêtes HTTP, c'est-à-dire 8082.
2. Il exécute également l'utilitaire, qui enregistre les requêtes HTTP arrivant sur le port 8083.
3. Nous écrivons des tests réguliers dans RSpec. Cela crée les données nécessaires dans la base de données et envoie une requête à localhost:8082 comme s'il s'agissait d'un service externe tel que HTTParty.
4. Nous analysons la réponse, vérifions les changements dans la base de données, recevons une liste des requêtes qui ont été enregistrées par le substitut RequestBin et les vérifions.

### Détails de l'implémentation

Voici comment nous avons implémenté cela. À titre de démonstration, appelons le service de test TheService et créons un wrapper :

Il est worth de mentionner que les fichiers d'autochargement doivent être configurés dans le dossier de support lors de l'utilisation de RSpec :

```
Dir[Rails.root.join('spec/support/**/*.rb')].each {|f| require f}
```

La méthode de démarrage :

* Lit les informations de configuration nécessaires pour démarrer TheService. Ces informations peuvent différer parmi les différents développeurs et sont donc exclues de Git. La configuration contient les paramètres nécessaires pour démarrer le programme. Toutes ces différentes configurations sont en un seul endroit afin de ne pas avoir à créer des fichiers inutiles.
* Compile et exécute via `go run <path to main.go> <path to config>`
* Interroge chaque seconde et attend que TheService soit prêt à accepter les requêtes.
* Enregistre l'identifiant de chaque processus afin de ne rien répéter et d'avoir la capacité d'arrêter un processus.

La configuration elle-même :

La méthode "stop" arrête simplement le processus. Il y a un piège cependant ! Ruby exécute une commande "go run", qui compile TheService et lance un binaire dans un processus enfant avec un ID inconnu. Si nous arrêtons simplement le processus qui s'exécute dans Ruby, le processus enfant ne s'arrête pas automatiquement et le port restera en utilisation. Ainsi, l'arrêt de TheService doit passer par le Process Group ID :

Ensuite, nous préparons le "shared_context" où nous définissons les variables par défaut, démarrons TheService s'il n'a pas déjà été lancé et désactivons temporairement VCR puisque VCR verrait ce que nous faisons comme une requête de service externe, mais nous ne voulons pas que VCR mock les requêtes à ce stade :

Et maintenant nous pouvons regarder l'écriture des specs eux-mêmes :

TheService peut faire des requêtes HTTP à des services externes. Nous pouvons le configurer pour rediriger les requêtes vers l'utilitaire local qui les journalise. Pour cet utilitaire, il y a aussi un wrapper pour le démarrer et l'arrêter qui est similaire à 'TheServiceControl', sauf que cet utilitaire peut simplement être démarré comme un binaire sans compilation.

### Points supplémentaires

L'application Go a été écrite de sorte que tous les logs et les informations de débogage soient envoyés à STDOUT. En production, cette sortie est envoyée à un fichier. Lors du lancement depuis RSpec, le log est affiché dans la console, ce qui aide vraiment au débogage.

Si vous exécutez spécifiquement les specs qui n'ont pas besoin de TheService, alors il ne démarrera pas.

Afin de ne pas perdre de temps à lancer TheService chaque fois qu'un spec change, pendant le processus de développement, vous pouvez lancer TheService manuellement dans le terminal et simplement ne pas l'éteindre. Chaque fois que c'est nécessaire, vous pouvez même le lancer en mode débogage dans un IDE. Ensuite, les specs préparent tout, envoient la requête au service, il s'arrête et vous pouvez facilement le déboguer. Cela rend l'approche TDD vraiment pratique.

### Conclusion

Nous utilisons cette configuration depuis environ un an maintenant et n'avons rencontré aucun échec avec celle-ci. Les specs sont beaucoup plus lisibles que les tests unitaires en Go, et ils ne dépendent pas de la connaissance de la structure interne du service. Si nous devons, pour une raison quelconque, réécrire le service dans un autre langage, alors nous n'aurons pas besoin de changer les specs. Seuls les wrappers, qui sont utilisés pour lancer le service de test avec une commande différente, devront être réécrits.