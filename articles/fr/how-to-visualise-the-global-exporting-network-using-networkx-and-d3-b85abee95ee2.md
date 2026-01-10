---
title: Comment visualiser le réseau mondial d'exportation à l'aide de NetworkX et
  D3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-15T23:58:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-visualise-the-global-exporting-network-using-networkx-and-d3-b85abee95ee2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OC42Ul4VREUunK-yojnOyA.png
tags:
- name: Data Science
  slug: data-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment visualiser le réseau mondial d'exportation à l'aide de NetworkX
  et D3
seo_desc: 'By Patrick Ferris

  Data-Driven Documents (D3) is a JavaScript library for building powerful graphics
  to communicate information in datasets. It is also fair to say that for many, myself
  included, it has a non-standard approach to building the graphics...'
---

Par Patrick Ferris

Data-Driven Documents (D3) est une bibliothèque JavaScript pour créer des graphiques puissants afin de communiquer des informations contenues dans des ensembles de données. Il est également juste de dire que pour beaucoup, moi y compris, elle a une approche non standard pour construire les graphiques. Souvent, la courbe d'apprentissage peut sembler raide.

Dans cet article, nous allons examiner l'utilisation de NetworkX — une bibliothèque Python pour explorer les structures de graphes — afin de faire une partie du traitement initial des données pour nous. Ensuite, nous ajouterons les touches artistiques finales en JavaScript avec D3. Le code complet peut être trouvé sur mon [GitHub](https://github.com/patricoferris/blog-posts/tree/master/Exporting_Dependencies) et une version interactive peut être trouvée [ici](https://bl.ocks.org/patricoferris/bd646b1122b087cc3ec61de0690625b8/104d0bbfd541851d99d0babdbc0a6f35a6f5a20f).

### Les données

Je me souviens quand on m'a présenté pour la première fois le [CIA World Factbook](https://www.cia.gov/library/publications/the-world-factbook/), et je l'ai adoré. Il contient une mine d'informations sur tous les pays du monde. Il ne demande qu'à être visualisé. En plus de cela, il a été converti dans différents formats sur [GitHub](https://github.com/factbook) et — surtout pour nous — en JSON.

Les données sont fournies par pays en utilisant leur codage ISO à deux caractères. Nous aurons besoin du continent auquel chaque pays appartient pour accéder aux données. Tout d'abord, nous allons créer ce dictionnaire :

Le dictionnaire simplifie beaucoup les choses lorsque nous voulons accéder à l'URL des données de chaque pays.

L'étape suivante consiste à définir une classe `Country` simple pour stocker les données. Pendant que nous y sommes, cela améliorerait la visualisation si nous pouvions utiliser les noms réels des pays — et non leur code à deux caractères — nous pouvons donc trouver ces informations et les stocker pour une utilisation ultérieure.

Et maintenant, nous sommes enfin prêts à ajouter les informations sur les exportateurs — cette méthode n'est pas parfaite, mais elle obtient la majorité des informations.

Ne vous inquiétez pas trop des fonctions `split()` sur les partenaires exportateurs. Cela nettoie simplement certaines des données afin que nous obtenions uniquement les noms et les pourcentages que nous voulons. Consultez la page GitHub pour voir les noms supplémentaires que j'ai dû ajouter pour que la construction du graphe fonctionne.

### NetworkX

[NetworkX](https://networkx.github.io/) est une bibliothèque Python assez sophistiquée pour construire, analyser et — dans une certaine mesure — exporter des structures de données de graphes. Elle est également très simple à utiliser.

Maintenant que nous avons les données que nous voulons stockées dans nos objets `Country`, le code pour créer notre graphe orienté est très simple.

Nous pouvons également ajouter des attributs à nos nœuds comme le degré du nœud et le nom (pas le code ISO). Une fois que nous avons notre structure de données, nous pouvons l'exporter au format JSON et la stocker dans un fichier prêt à être utilisé avec D3.

### Qu'est-ce qui est différent avec D3 ?

Dès le départ, Mike Bostock (le fondateur de D3) voulait créer un "graphique réutilisable". Dans son [article](https://bost.ocks.org/mike/chart/) sur le sujet, il met en lumière les objectifs clés et les missions du projet D3. Ceux-ci peuvent nous aider à comprendre la structure syntaxique qu'il a.

Le premier, et **le plus important**, point à retenir est que les graphiques doivent être implémentables "comme des fermetures avec des méthodes getter-setter". Si vous êtes nouveau en programmation, vous pourriez être confus quant à ce qu'est une [fermeture](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures). Ne vous inquiétez pas ! Le grand concept associé aux fermetures est la portée lexicale, qui semble beaucoup plus effrayante qu'elle ne l'est réellement. L'idée de base derrière tout cela est les fonctions imbriquées et la manière dont la fonction interne a accès aux variables de la fonction externe.

Jetez un coup d'œil à `EXEMPLE 1` dans le code ci-dessous. Ici, nous retournons simplement la fonction interne, qui a accès aux arguments passés à la fonction externe. La variable que nous déclarons, `closureOne`, est une fonction et lorsque nous l'exécutons avec `closureOne()`, nous `console.log(config.name)`.

Dans `EXEMPLE 2`, nous déclarons des variables dans la portée de la fonction externe, permettant à la fonction interne `my` d'y avoir accès. Dans la fonction `fullName` associée à la fonction `my` — une méthode — nous pouvons **soit** définir ou obtenir le `nameOfPerson` selon les arguments passés. Remarquez comment le développeur n'a pas accès à la variable `nameOfPerson`. Le développeur est forcé d'utiliser nos méthodes définies pour la mettre à jour et y accéder, fournissant un niveau de sécurité à notre fonction.

Cette méthode d'utilisation des fermetures est la manière dont D3 est codé. Jetez un coup d'œil à la fonction [line](https://github.com/d3/d3-shape/blob/master/src/line.js) pour voir cela en action. Cette [vidéo](https://www.youtube.com/watch?v=-jysK0nlz7A&t=647s) peut également éclairer le sujet.

### Programmer avec D3

Heureusement, vous **n'avez pas besoin d'être un maître des fermetures et de D3** pour créer une visualisation. En fait, tant que vous pouvez copier et coller, vous pouvez généralement obtenir quelque chose de fonctionnel en un rien de temps grâce aux [Blocs de Mike Bostock](https://bl.ocks.org/mbostock). Ce site contient de nombreux exemples open-source de construction de visualisations de données avec D3. Vous pouvez utiliser le code pour créer les vôtres avec vos données.

Pour créer le réseau de ce tutoriel, j'ai utilisé [cet exemple](https://bl.ocks.org/mbostock/4062045). Pour le faire fonctionner à l'écran, tout ce que j'ai dû changer était le nom du fichier .csv.

Examinons certaines des **lignes de code clés** qui font fonctionner cette visualisation, ainsi que les parties que j'ai ajoutées pour, je l'espère, l'améliorer davantage.

Juste avant de plonger, Andrew Dunkman a écrit un excellent article aidant à expliquer les [sélections D3](https://techtime.getharvest.com/blog/understanding-d3-selection-operations) que je recommande de lire.

Pour voir les fonctions que nous appelons comme `dragstarted`, `scaledSize`, ou `mouseOut`, assurez-vous de consulter le code complet [ici](https://github.com/patricoferris/blog-posts/blob/master/Exporting_Dependencies/index.js). À titre d'exemple, voyons ce qui se passe lorsque nous cliquons sur un nœud.

### Conclusion

Le code est désordonné, la visualisation n'est pas parfaite, et il reste tant à discuter et à apprendre.

Mais ce n'est pas le point. Espérons que cet article vous a permis de vous familiariser avec NetworkX et D3 sans vous submerger. Nous devons tous commencer quelque part, et cela peut être votre début pour créer des visualisations de données perspicaces et puissantes.

Si vous êtes bloqué en vous demandant quoi aborder ensuite, voici quelques suggestions :

* [Vers des graphiques réutilisables de Mike Bostock](https://bost.ocks.org/mike/chart/) — c'est un excellent exemple de quelqu'un expliquant son processus de réflexion puis son implémentation. Cela montre comment ses objectifs pour le projet ont affecté son implémentation.
* [D3 et React](https://www.smashingmagazine.com/2018/02/react-d3-ecosystem/) — deux bibliothèques se disputant le DOM, c'est ce que je lis actuellement, et je vois quelles sont les meilleures façons d'utiliser les deux sur un projet.
* [Elijah Meeks, Senior Data Visualization Engineer chez Netflix](https://medium.com/@Elijah_Meeks/d3-is-not-a-data-visualization-library-67ba549e8520) — tous les articles d'Elijah Meeks sont une excellente ressource et éclairent souvent le monde de la visualisation de données.

Merci de m'avoir suivi jusqu'à la fin. Bonne visualisation !