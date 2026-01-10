---
title: Comment nous avons construit une application qui utilise l'historique de localisation
  des travailleurs pour lutter contre le vol de salaire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-20T03:15:26.000Z'
originalURL: https://freecodecamp.org/news/i-built-an-app-that-uses-workers-location-history-to-combat-wage-theft-dedca8380ce3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_aZNPDabvxQwQcQFFstppw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: politics
  slug: politics
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment nous avons construit une application qui utilise l'historique de
  localisation des travailleurs pour lutter contre le vol de salaire
seo_desc: 'By Abhinav Suri

  In 2008, the Center for Urban Economic Development surveyed 4,387 low-wage workers
  in Chicago, Los Angeles, and New York City. They wanted to determine the extent
  of violations of employment laws in core sectors of the US economy.

  The...'
---

Par Abhinav Suri

En 2008, le Center for Urban Economic Development a [enquêté](http://nelp.3cdn.net/e470538bfa5a7e7a46_2um6br7o3.pdf) auprès de 4 387 travailleurs à bas salaire à Chicago, Los Angeles et New York. Ils voulaient déterminer l'ampleur des violations des lois sur l'emploi dans les secteurs clés de l'économie américaine.

Ils ont découvert que :

* 76 % de ceux qui ont travaillé plus de 40 heures n'ont pas été payés au taux de heures supplémentaires légalement requis.
* 68 % de l'échantillon a subi au moins une violation liée à la paie au cours de la semaine de travail précédente.
* Le travailleur moyen a perdu 51 $ de ses gains hebdomadaires de 339 $ en raison du vol de salaire. Cette perte se traduit par plus de 2 652 $ de pertes sur un an (sur un salaire annuel moyen total de 17 616 $).

De plus, cette étude estime que les travailleurs à travers le pays perdent collectivement 50 milliards de dollars par an en raison du vol de salaire.

Même si cette étude a été menée il y a huit ans, les résultats sont toujours pertinents : la majorité des travailleurs à bas salaire sont victimes de vol de salaire. S'ils veulent récupérer leurs salaires perdus, ils doivent se tourner vers les tribunaux. Parce que tant de travailleurs à bas salaire travaillent dans des situations d'exploitation, leurs employeurs ne tiennent pas les registres requis qui montreraient le nombre d'heures qu'un travailleur a pu travailler ou le salaire que le travailleur a reçu chaque semaine. Sans ces registres, les travailleurs doivent se fier à leurs propres preuves concernant leurs heures de travail et leur salaire.

Fréquemment, les avocats doivent se fier aux clients pour qu'ils se souviennent et reconstruisent ensuite un calendrier de leurs déplacements sur plusieurs mois, ce qui rend le cas plus faible. C'est là que commence cette histoire.

Au cours du dernier semestre, mon équipe et moi-même chez [Hack4Impact](http://hack4impact.org) avons eu l'opportunité de travailler avec [Community Legal Services of Philadelphia](http://clsphila.org) (CLS), une clinique juridique pro bono qui a servi plus d'un million de Philadelphiens à faible revenu depuis sa création en 1966.

Nous avions pour mission de créer un site web pour analyser l'historique de localisation Google d'un client et créer une feuille de temps pour toutes les fois où un client est entré et sorti d'un lieu de travail saisi par l'utilisateur. L'intention était d'utiliser l'historique de localisation Google du travailleur pour compléter son propre témoignage afin de fournir un cas plus solide quant au montant dû au client. Puisque la plupart des clients potentiels portent des téléphones low-cost (généralement Android) et n'ont pas de suivi de l'historique de localisation, cette solution s'avérerait incroyablement utile comme point de départ pour reconstruire une feuille de temps admissible devant les tribunaux pour leur cas, donnant aux avocats et paralégaux de CLS une source de preuves entièrement nouvelle provenant d'une source fiable.

![Image](https://cdn-media-1.freecodecamp.org/images/KtTfmJ6tv8Whzc9eqe1rb5LyKPGpDjXAXRXl)
_Bureaux des Services Juridiques Communautaires_

#### Flux utilisateur du projet :

Notre flux utilisateur optimal s'est avéré être le suivant (notez que je mets des images de notre produit en direct pour que vous puissiez mieux visualiser ces exigences) :

![Image](https://cdn-media-1.freecodecamp.org/images/Tx7lAOhH8SxNwZoqC8S4qP0iFPCCiUL6qps0)

* Un utilisateur doit pouvoir ajouter son fichier LocationHistory.json (téléchargé depuis Google Takeout).

![Image](https://cdn-media-1.freecodecamp.org/images/j7-Wof55pqbuKdkJ7nbTOU-CP-COF2ea77Mz)

* Un utilisateur doit ensuite pouvoir faire traiter et afficher ses données de localisation sur une carte.

![Image](https://cdn-media-1.freecodecamp.org/images/Av9Xj8i9HIOrZkPVJR8cfhuH9dhWe9y453so)

* Un utilisateur doit ensuite pouvoir sélectionner une zone de délimitation contenant la zone approximative de son lieu de travail.

![Image](https://cdn-media-1.freecodecamp.org/images/2JQxYhgBNFenIqRDqV16kbWbRr-8IFpazhTE)

* Un utilisateur doit ensuite pouvoir sélectionner un jour de début pour la semaine et soumettre le fichier pour traitement.

![Image](https://cdn-media-1.freecodecamp.org/images/-Izn7lKMLazNCeHXOLPCMKMlMtOQJsa26l7q)

* L'historique de localisation doit ensuite être traité dans un fichier .csv. Ce fichier doit contenir des lignes indiquant la durée pendant laquelle un utilisateur est resté dans une zone de délimitation pour un lieu de travail (avec les heures de début et de fin).
* Si un utilisateur quitte puis entre à nouveau sur un lieu de travail, ceux-ci doivent apparaître comme des lignes séparées. À la fin d'une semaine, le nombre total d'heures doit être tabulé et affiché dans une colonne séparée.

En plus de tout cela, tout cela devait être fait sur le front-end pour éviter les problèmes de confidentialité liés au stockage des données de localisation sur nos serveurs. Ces exigences semblaient relativement faciles à réaliser. Peu did I realize que l'analyse et l'affichage d'un fichier LocationHistory.json seraient probablement la tâche la plus difficile.

### Structure de Google LocationHistory.json & Première tentative de chargement :

![Image](https://cdn-media-1.freecodecamp.org/images/Z6ptk0HszsH9rVMkNp-AWLzqfW2uKp10Fbx6)

Au cas où vous ne le sauriez pas, Google surveille presque tout ce que vous faites. Plus précisément, ils suivent votre historique de localisation si vous avez un téléphone Android et que vous ne l'avez pas désactivé jusqu'à présent. Si vous le souhaitez, vous pouvez télécharger votre historique à ce jour en allant sur [takeout.google.com/settings/takeout](http://takeout.google.com/settings/takeout) et en téléchargeant votre fichier au format JSON (attention... il peut être énorme).

Mon fichier LocationHistory.json seul faisait environ 59,9 Mo (j'avais un téléphone Android depuis environ deux ans), mais certains des clients qui utiliseraient notre système pourraient avoir des historiques de localisation de **quelques centaines de mégaoctets**. Essayer de charger l'ensemble du fichier JSON en mémoire fait planter le navigateur pendant environ 30 secondes avant de déclencher l'erreur classique "Aw Snap" sur Chrome (indiquant généralement une erreur de mémoire insuffisante).

![Image](https://cdn-media-1.freecodecamp.org/images/p1FYy4Ntol2vhbNQ09byLw4ldZPBPPWXuwF7)

En fait, lors de l'exécution de cela sur une machine plus puissante, nous pouvons prendre un instantané de la mémoire et essayer de voir ce qui se passe. Pour référence, j'ai utilisé un fichier de 59,9 Mo que j'ai chargé en mémoire.

![Image](https://cdn-media-1.freecodecamp.org/images/bS2Y2TzwFsai9F2zfa3BAEk1IZzhJJHXLZly)

Ici, nous voyons que la taille du tas JS résultant est presque le triple de la taille réelle du fichier. Mais en réalité, nous n'avons pas besoin de stocker l'ensemble du tableau en mémoire, de l'analyser pour les points de données de localisation, puis de transmettre ces points à une fonction qui les affiche sur une carte. Nous pourrions simplement faire tout cela à la volée... cependant, c'est plus facile à dire qu'à faire.

### Chunking & Oboe :

La première solution à laquelle j'ai pensé était d'essayer de diviser le fichier en morceaux plus gérables de 512 kilo-octets à la fois. Cependant, cela présente certains défauts inhérents, principalement que le fichier que j'essaie de charger contient une grande "chaîne" qui a le format d'un objet JSON (mais qui n'est pas encore un objet). Ainsi, lorsque je décide de diviser et de traiter le fichier en morceaux séquentiels de 512 Ko de long, je peux facilement me retrouver dans une situation où je coupe un "objet" en deux.

![Image](https://cdn-media-1.freecodecamp.org/images/-bzPzHJv9iZLizHGv3hsREVckg0z4cEcyW9I)
_Exemple exagéré de la manière dont le chunking peut diviser du texte structuré_

J'avais donc maintenant besoin d'un moyen de suivre les objets à moitié complétés/objets qui ont été coupés et de les préfixer/ajouter aux morceaux suivants en conséquence pour m'assurer que tout serait analysé correctement. Bien que le fichier Google LocationHistory.json soit relativement uniforme, la manière dont les morceaux peuvent être divisés ne l'est pas. Heureusement, il existe une bibliothèque existante pour aider à gérer tous les cas limites qui peuvent survenir. Entrez Oboe.js.

![Image](https://cdn-media-1.freecodecamp.org/images/dGjPLjGIIdfwgIdATflJ3ycwdln28S6bFMUQ)
_Origin 1 et 2 sont des sources JSON en streaming et l'Aggregator est Oboe qui envoie des objets JSON construits complets_

Oboe.js est conçu pour traiter le JSON provenant d'une source de streaming. De plus, il peut charger des arbres JSON plus grands que la mémoire disponible sur le client, car il ne traite qu'un seul nœud JSON à la fois, puis supprime le nœud de l'arbre mémoire. Cependant, je n'ai pas de source de données en streaming. Heureusement, après avoir regardé autour du code source d'Oboe pendant un certain temps, j'ai trouvé qu'oboe peut être instancié et que des données peuvent être transmises via un événement d'émission.

Le code oboe lui-même est relativement facile à configurer. Le fichier JSON que nous examinons a la forme générale suivante.

```
{   "locations": [ {    "timeStampMs": ...,    "latitudeE7": ...,    "longitudeE7": ...,    "accuracy": ...  }, {    "timeStampMs": ...,    "latitudeE7": ...,    "longitudeE7": ...,    "accuracy": ...  },  ...  ]}
```

Selon la documentation d'Oboe, le nœud `locations` doit être ciblé et tout sous-objet de celui-ci sera transmis à la fonction de rappel comme montré dans l'exemple de code ci-dessous.

Ensuite, nous devons trouver un moyen de transmettre des morceaux à cette fonction. La fonction de chunking elle-même est un peu plus compliquée, mais la fonctionnalité principale est de traiter le fichier en portions de 512 Ko à la fois. La fonction prend le fichier lui-même (à partir d'une entrée) et l'instance d'oboe.js (dans notre cas, la variable `os`).

Notez à la ligne 11 ce qui suit :

```
oboeInstance.emit('data', chunk);
```

Cette ligne contient le cœur du traitement par oboe. Le morceau sera envoyé à notre instance oboe dans la variable `os` en tant que quasi-flux de données.

### Affichage des points :

La dernière chose à faire est d'afficher les données. Nous avons choisi d'utiliser leaflet.js car il était assez simple à configurer et il dispose d'un écosystème de bibliothèques tierces beaucoup plus diversifié que Google Maps (ou toute autre bibliothèque de cartes que je connaisse).

L'initialisation de la carte sur une div avec `id='mapid'` est assez simple :

Cependant, l'affichage de plus d'un million de points de données de localisation nécessite beaucoup plus que ce que la bibliothèque de base leaflet.js peut gérer. Heureusement, de nombreuses solutions open source utilisent le clustering hiérarchique glouton pour regrouper les points à des niveaux de zoom bas et les déclusteriser à mesure que le niveau de zoom augmente. Vladimir Agafonkin de Mapbox a écrit un excellent blog sur l'aspect algorithmique de la manière dont ce processus fonctionne, et je vous encourage vivement à [le consulter](https://www.mapbox.com/blog/supercluster/).

![Image](https://cdn-media-1.freecodecamp.org/images/oj5UbZDOLDX2OPm3kOA0yaHBqMPdGf0i7Cnl)
_src : [https://www.mapbox.com/blog/supercluster/](https://www.mapbox.com/blog/supercluster/" rel="noopener" target="_blank" title=")_

Une implémentation existante du clustering de marqueurs pour leaflet existe déjà avec la [bibliothèque PruneCluster](https://github.com/SINTEF-9012/PruneCluster). Cette bibliothèque se distingue des autres car elle n'a pas de limite supérieure réelle quant au nombre de points qu'elle peut traiter (elle est uniquement contrainte par la puissance de calcul du client). Les temps de rendu et de mise à jour résultants sont impressionnants.

![Image](https://cdn-media-1.freecodecamp.org/images/pCbRf93vKE2Di1E8QHjSRS3afVsY5PuIsbKk)
_Temps de mise à jour de PruneCluster. src : [https://github.com/SINTEF-9012/PruneCluster](https://github.com/SINTEF-9012/PruneCluster" rel="noopener" target="_blank" title=")_

En revenant à notre code d'instance oboe.js, nous pouvons le modifier légèrement pour tenir compte de l'ajout de la bibliothèque PruneCluster :

### Résultats :

Après avoir apporté toutes les modifications ci-dessus, j'ai enfin pu effectuer quelques tests de base pour voir si toutes ces optimisations en vaudraient la peine. Voici les résultats (à chaque taille de fichier, cinq essais ont été effectués et le temps est la moyenne).

![Image](https://cdn-media-1.freecodecamp.org/images/2PW95dgJEpuaUejts96vp0GyCDc6pmxkq33n)

Les résultats étaient stupéfiants. Bien que le chargement du fichier directement en mémoire soit plus rapide pour les petits fichiers, le chunking avec le flux oboe a porté ses fruits à la fin et a donné une corrélation presque linéaire entre le temps de chargement et la taille du fichier ! À la fin, nous avons attaché une barre de chargement à l'analyseur pour donner à l'utilisateur un sentiment de progression et nous y avons attaché quelques statistiques de temps de chargement.

![Image](https://cdn-media-1.freecodecamp.org/images/m0dTiU9C04JzmFjBnLtoRjYE4o3QO7i4qdP7)

Et voilà. Analyse de l'historique de localisation Google sur le front-end. Aucun serveur nécessaire. En fait, j'héberge actuellement le site web sur la page github à l'adresse [hack4impact.github.io/cls](http://hack4impact.github.io/cls).

Dans l'ensemble, ce projet a été un énorme succès. Au cours du semestre, j'ai interagi avec certaines des personnes incroyables des Services Juridiques Communautaires pour créer ce produit qui aidera de nombreux travailleurs juridiques pendant des années à venir. Je vous encourage vivement, ceux qui savent programmer, à offrir leurs compétences pour aider les organisations communautaires à mieux atteindre leur mission. C'est une expérience incroyablement enrichissante pour les deux parties et vous challengera à appliquer vos compétences pour créer des produits durables et fonctionnels.

Vous pouvez trouver le code source du projet dans [notre dépôt](http://github.com/hack4impact/cls).

Mon équipe complète est : Chef de produit : [Krishna Bharathala](https://www.freecodecamp.org/news/i-built-an-app-that-uses-workers-location-history-to-combat-wage-theft-dedca8380ce3/undefined), Membres de l'équipe : [Katie Jiang](https://www.freecodecamp.org/news/i-built-an-app-that-uses-workers-location-history-to-combat-wage-theft-dedca8380ce3/undefined), [Daniel Zhang](https://www.freecodecamp.org/news/i-built-an-app-that-uses-workers-location-history-to-combat-wage-theft-dedca8380ce3/undefined), [Santi Buenahora](https://www.freecodecamp.org/news/i-built-an-app-that-uses-workers-location-history-to-combat-wage-theft-dedca8380ce3/undefined), et [Rachel H](https://www.freecodecamp.org/news/i-built-an-app-that-uses-workers-location-history-to-combat-wage-theft-dedca8380ce3/undefined).