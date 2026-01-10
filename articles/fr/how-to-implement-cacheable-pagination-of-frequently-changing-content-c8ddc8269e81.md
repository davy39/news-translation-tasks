---
title: Comment implémenter une pagination "cacheable" pour du contenu fréquemment
  mis à jour
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-13T15:28:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-cacheable-pagination-of-frequently-changing-content-c8ddc8269e81
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZOBmn2PAMPUtQkidXEPjtg.jpeg
tags:
- name: Android
  slug: android
- name: mobile app development
  slug: mobile-app-development
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment implémenter une pagination "cacheable" pour du contenu fréquemment
  mis à jour
seo_desc: 'By Nikita Kozlov

  Whenever we need to display a lot of content that is stored on the backend, we split
  it in chunks and then load them subsequently one piece at a time. This is a common
  approach, and there are multiple reasons why it is so great:


  It ...'
---

Par Nikita Kozlov

Chaque fois que nous devons afficher une grande quantité de contenu stocké sur le backend, nous le divisons en morceaux et les chargeons ensuite un par un. C'est une approche courante, et il y a plusieurs raisons pour lesquelles elle est si efficace :

1. **Elle améliore l'expérience utilisateur**. Le chargement d'une seule petite page prend moins de temps, donc l'utilisateur peut commencer à consulter le contenu plus rapidement.
2. **Elle réduit la charge sur le réseau**. Une seule page est petite et légère en termes de bande passante. De plus, nous pouvons optimiser la consommation de batterie et de réseau pour les appareils mobiles en ajustant la taille d'une seule page.
3. **Elle réduit la charge sur le backend**. Traiter de plus petits morceaux est plus rapide que des plus gros. Les utilisateurs n'ont généralement pas besoin de tout le contenu en une seule fois, donc la charge moyenne par utilisateur est plus faible.

Tout le monde y gagne. Dans la plupart des cas. Mais pas tous. Comme cela arrive souvent avec les solutions génériques, plus le domaine est spécifique, meilleure est la solution qui peut être trouvée. Dans cet article, je souhaite partager une solution intéressante pour un tel cas.

### Définir la tâche

Imaginons une collection qui change fréquemment au fil du temps. Par exemple, nous pourrions examiner une liste d'articles qu'un utilisateur a applaudis sur Medium, ou une liste de souhaits dans une application de shopping, ou un historique d'autres actions des utilisateurs en général. Les utilisateurs peuvent "ajouter" autant d'éléments à cette collection qu'ils le souhaitent.

Notre tâche est d'afficher cette collection de manière pratique, tout en faisant de notre mieux pour éviter de surcharger le réseau et donc la batterie et la bande passante.

#### Problèmes avec la pagination

L'une des façons de minimiser l'utilisation du réseau est de mettre en cache les réponses. La plupart des applications mobiles et web dépendent fortement du cache HTTP. Il sauvegarde les réponses pendant une période de temps spécifiée dans l'en-tête de la réponse. Chaque fois qu'une application fait une requête, le client HTTP tente d'obtenir une réponse correspondante depuis le cache. Ce n'est que si elle n'est pas disponible qu'il fait un appel réel au backend.

Parfois, ce type de mise en cache ne fonctionne pas bien pour le contenu paginé. Si la collection est modifiée fréquemment et que le contenu doit être à jour, alors il ne fait tout simplement pas sens de mettre en cache la réponse _du tout_. Par exemple, imaginons le scénario suivant :

1. L'utilisateur ouvre la liste des articles qu'il a applaudis ici, sur Medium. La première page est récupérée depuis le backend.
2. Après cela, l'utilisateur a recherché quelque chose de nouveau, a trouvé un autre article intéressant et a décidé de le recommander.
3. Maintenant, il veut vérifier à nouveau la liste des articles qu'il a recommandés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kicseJ7nvQxQLOLlOTHYaw.jpeg)

L'application doit effectuer exactement la même requête pour la première page, mais le résultat est différent. La réponse ne peut pas être mise en cache.

Si votre tâche spécifique au domaine vous permet de réorganiser les éléments dans cette collection, alors votre problème est encore pire. Pour la très même raison : la réponse change constamment.

### Une autre approche

Examinons de plus près la première page de données récupérées depuis le backend. La réponse elle-même est une liste d'éléments dans un ordre particulier. Chaque élément est peu susceptible de changer. Ce qui change, c'est l'_ordre_ des éléments et _les_ éléments qui sont sur cette liste.

Cela signifie que si nous pouvons récupérer séparément l'ordre des identifiants des éléments et les détails des éléments, alors le deuxième appel peut potentiellement être mis en cache. En fait, même la mise en cache du deuxième appel n'est pas simple — mais nous y viendrons. Pour l'instant, faisons une requête séparée pour chaque élément :

![Image](https://cdn-media-1.freecodecamp.org/images/1*aY5DZA9XOAH17uDjCGTqAA.jpeg)

Comme vous pouvez le voir sur le diagramme ci-dessus, parce que les éléments sont peu susceptibles de changer, nous pouvons mettre en cache les appels de détails des éléments. Malheureusement, une telle division multipliera la quantité d'appels réseau par un ordre de grandeur. Mais il y a quelque chose que nous pouvons faire à ce sujet.

#### Que voulons-nous réellement ?

Si nous demandons simplement un ensemble d'éléments, nous rencontrerons le même problème que l'approche de pagination générique. Le cache HTTP n'agira pas comme nous le souhaitons, alors écrivons le nôtre en utilisant une logique similaire mais plus délibérée.

Ce cache ne va pas stocker des lots, mais des éléments individuels pendant une période de temps particulière. Nous prendrons la réponse, accéderons à ses en-têtes HTTP et récupérerons les informations sur le temps de mise en cache. Ensuite, nous mettrons chaque élément individuellement dans le cache. La prochaine fois que nous devons afficher des éléments, nous pouvons facilement accéder à ceux en cache et demander le reste. En code, cela semble plus facile que cela ne le paraît :

Passons rapidement en revue le code. La méthode _getOrderedItemsIds()_ retourne l'ordre des éléments et est paginée. La partie la plus importante est la méthode _getItemsByIds()_. C'est ici que nous vérifions d'abord quels éléments sont dans le cache, puis demandons le reste depuis le backend. Veuillez noter que pour des raisons de simplicité, le code ci-dessus est synchrone et ne compilera probablement pas.

Après avoir implémenté cette approche, l'ajout d'un nouvel élément en tête de liste entraînera une requête pour l'ordre des identifiants des éléments et les détails du nouvel élément. Le reste provient du cache.

Une paire similaire d'appels se produira pour chaque page consécutive. L'idée principale est que nous pouvons récupérer la plupart des détails des éléments depuis le cache. Mais malheureusement, nous devons demander l'ordre des identifiants des éléments pour chaque page.

#### Faites-le mieux

Les identifiants des éléments sont généralement de petits objets comme une _String_ ou un _Universally Unique Identifier (UUID)_. Par conséquent, nous pouvons envoyer des pages plus grandes. Augmenter la quantité d'identifiants d'éléments retournés par un appel d'ordre diminue le nombre d'appels, sans abuser de la bande passante du réseau.

Par exemple, au lieu de demander 20 à 40 identifiants d'éléments, nous pouvons en demander 100 à 200. Plus tard, la couche UI peut modérer le nombre de détails d'éléments qui doivent être affichés et les demander en conséquence. Ensuite, une séquence d'appels ressemblera à ceci :

1. Demander les 100 premiers identifiants d'éléments et les garder en mémoire.
2. Demander les détails des 20 premiers éléments (les mettre en cache bien sûr) et les afficher à l'utilisateur.
3. Après que l'utilisateur a fait défiler les 20 premiers éléments, demander le deuxième lot de 20 détails d'éléments.
4. Répéter l'étape précédente trois fois de plus et faire des étapes similaires pour la page suivante d'identifiants d'éléments.

Maintenant, l'ajout d'un nouvel élément en haut entraîne toujours deux requêtes (une pour les identifiants et une autre pour les détails de ce nouvel élément). Mais nous n'aurons pas à demander la page suivante pendant un certain temps, car les pages sont plus grandes. Nous n'aurons pas non plus besoin de demander les détails des éléments car ils sont mis en cache !

Petit avertissement : la manière dont l'UI modère la demande de détails des éléments peut être plus intéressante. Par exemple, elle peut sauter les requêtes pour certains éléments si l'utilisateur fait défiler trop vite, car ils ne s'y intéressent pas. Mais cela mérite un autre article.

### Conclusion

Les solutions générales ne sont généralement pas optimisées pour des cas particuliers. Connaître les spécificités peut nous aider à écrire des applications plus rapides et plus optimisées. Pour ce cas, le savoir était crucial que le contenu change fréquemment et qu'il s'agit d'une collection d'éléments avec des identifiants. Passons en revue toutes les améliorations apportées par la nouvelle approche :

1. Demander l'ordre des éléments séparément nous permet de mettre en cache les détails, même si nous avons dû écrire un cache HTTP modifié.
2. La mise en cache des détails des éléments entraîne une réduction de l'utilisation de la bande passante.
3. L'augmentation de la taille des pages pour la requête d'ordre réduit le nombre d'appels.

Une dernière chose : les optimisations sont géniales, et j'ai trouvé passionnant d'écrire du code efficace — mais n'oubliez pas de le profiler d'abord. L'optimisation prématurée pourrait causer des problèmes et nous devrions tous l'éviter.

[**Nikita Kozlov (@Nikita_E_Kozlov) | Twitter**](https://twitter.com/Nikita_E_Kozlov)  
[_The latest Tweets from Nikita Kozlov (@Nikita_E_Kozlov): "https://t.co/wmGSJ7snW1"_twitter.com](https://twitter.com/Nikita_E_Kozlov)

_Merci pour le temps que vous avez consacré à la lecture de cet article. Si vous l'avez aimé, n'oubliez pas de cliquer sur le_ ? _ci-dessous._