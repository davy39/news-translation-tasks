---
title: Comment apprendre Prolog en regardant Game of Thrones
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-11T15:41:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-learn-prolog-by-watching-game-of-thrones-4852ea960017
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fVNJJSasfcKnyv1JSM2B_g.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: coding
  slug: coding
- name: game of thrones
  slug: game-of-thrones
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment apprendre Prolog en regardant Game of Thrones
seo_desc: 'By Rachel Wiles

  Are they dead? Are they alive? Is she his aunt? Instead of casting your mind back
  to 2011, save the exhaustion and build your own expert using Prolog.


  Image via HBO

  Obligatory Game of Thrones SPOILER WARNING! Events included are up t...'
---

Par Rachel Wiles

#### Sont-ils morts ? Sont-ils vivants ? Est-elle sa tante ? Au lieu de vous creuser la tête pour vous rappeler 2011, économisez votre énergie et créez votre propre expert en utilisant Prolog.

![Image](https://cdn-media-1.freecodecamp.org/images/0mPIMd4VO0fFg9AA3aOkINfRK4VhuinAGXSZ)
_Image via HBO_

#### Avertissement de spoiler obligatoire pour Game of Thrones ! Les événements inclus vont jusqu'à la saison 7, sans tenir compte de ce qui se passe uniquement dans les livres. Si vous n'êtes pas à jour, procédez avec prudence. Mais, Prolog reste le même depuis 1972, sans rebondissements et avec une structure facile à suivre que ce tutoriel vous aidera à maîtriser.

### Établir les faits

Prolog est un langage de programmation logique, qui forme des règles et des relations à partir de faits. Pour utiliser Prolog, des requêtes sont passées à travers une base de données structurée de faits. Game of Thrones est réputé pour ses arbres généalogiques complexes (et souvent incestueux), donc décomposer les choses en faits simples commence une grande base pour une base de données Prolog.

![Image](https://cdn-media-1.freecodecamp.org/images/7Z4tEvxRINNe9qpbuQJF07WjtPlnAYgFEyoC)
_Personne n'a le temps pour ça. Image via usefulcharts_

Simplifiez les choses en commençant la base de données avec un ensemble de faits, qui peut être appliqué à tous les personnages. Pour les arbres généalogiques, un bon point de départ est de lier les personnages à travers leurs parents. Prenons le cas d'Arya Stark :

```
parent(eddard_stark, arya_stark).
parent(catelyn_stark, arya_stark).
```

Ici, deux faits séparés ont été définis, disant qu'Eddard et Catelyn sont les parents d'Arya. Vous pouvez ensuite extrapoler ces requêtes à travers tout l'univers de Game of Thrones, pour toutes les maisons, afin de créer une base de données complète (ou, piquer l'ensemble du jeu de données depuis mon [GitHub](https://github.com/rachelwiles/GoT-Check)). Ces faits seuls suffisent pour commencer à faire des requêtes. La requête la plus basique vérifie si un fait est présent dans la base de données.

```
?- parent(eddard_stark, arya_stark).
true
```

Si vous entrez des relations qui ne sont pas dans la base de données, elle retourne **false**. Vous pouvez également interroger avec des variables en Prolog en utilisant des majuscules. Pour trouver qui sont les parents d'Arya, demandez :

```
?- parent(Parent, arya_stark).
Parent = eddard_stark ;
Parent = catelyn_stark.
```

Eddard est retourné en premier dans cet exemple, car c'est le premier fait **vrai** listé dans la base de données. Le point-virgule conduit des recherches pour d'autres réponses vraies (catelyn_stark), jusqu'à ce qu'il n'y en ait plus. Un point termine la recherche complètement. Utilisez des underscores comme variables anonymes pour filtrer les informations qui n'ont pas d'importance. Par exemple, si vous vouliez voir qu'Arya a des parents, mais que vous ne vous souciez pas de qui ils sont, interrogez ce qui suit :

```
?- parent(_, arya_stark).
true
```

![Image](https://cdn-media-1.freecodecamp.org/images/3tkjbtN5ezXYqcSN2xqBVuQy6MQ7p5ZnAUXt)
_Saison 1 Épisode 1 : La dernière fois que quelqu'un a souri dans GoT. Image via Fanpop_

### Créer des règles

Maintenant qu'il y a des faits dans la base de données, commencez à créer des règles. Les règles dépendent des faits. En reliant les faits ensemble, on crée des règles. À partir de notre dernier exemple, créez une règle simple à partir du fait parent, pour déterminer une relation enfant ; X est l'enfant de Y **si** (écrit comme **:-** en Prolog) Y est le parent de X.

```
enfant(X, Y) :- parent(Y, X).
```

Cela inverse essentiellement la règle parent, et permet des recherches vers le haut et vers le bas de l'arbre généalogique. Dans un autre cas, supposons que vous voulez faire une règle déterminée par l'_absence_ d'un fait...

```
statut(X, mort) :- not(statut(X, vivant)).
```

Ici, j'ai étendu la base de données pour inclure un ensemble de règles pour chaque personnage qui est encore en vie. La requête recherche dans la base de données toutes les instances où la personne X est en vie. Le **not** indique que, si X n'est pas trouvé en vie, alors X est mort. Cette règle est efficace pour Game of Thrones, car elle ne nécessite qu'une poignée de faits, pour les quelques-uns qui sont encore en vie.

![Image](https://cdn-media-1.freecodecamp.org/images/FFOu992hmDDjc7itq9Bd8o1DGBuJ7wgMRJhM)
_meurt(X) :- joué_par(X, sean_bean). Image via [nova969](http://www.nova969.com.au" rel="noopener" target="_blank" title=")_

Des règles plus intéressantes et spécifiques sont créées en combinant des faits. Par exemple, pour créer une relation mère/père, plus de faits sur le genre de chaque personnage dans Game of Thrones sont nécessaires. Une fois fait, une règle pour identifier les mères est créée par ce qui suit :

```
mère(X, Y) :- parent(X, Y), femme(X).
```

Dans ce qui précède, nous avons déclaré qu'une mère (X) est un parent de quelqu'un **et** (écrit comme une virgule en Prolog) est une femme.

Jusqu'à présent, nous avons couvert le voyage vers le haut et vers le bas de l'arbre généalogique, mais nous n'avons pas touché de gauche à droite. En créant une règle de fratrie, des requêtes peuvent être faites dans tous les sens à travers l'arbre généalogique de Game of Thrones :

```
frère_soeur(X, Y) :- parent(Z, X), parent(Z, Y), dif(X, Y).
```

En termes profanes, cela indique que deux personnes (X et Y) sont frères et sœurs si elles partagent toutes deux le même parent (Z). La fonction **dif** ici est importante pour empêcher le programme de retourner _eux-mêmes_ comme leur propre frère ou sœur. Cependant, il y a des limitations à cette approche. Interroger cela évaluera les deux parents de X **et** les deux parents de Y (souvent, mais pas toujours, les mêmes personnes), par conséquent la recherche complète retournera des doublons. Cela peut être corrigé en introduisant des listes.

![Image](https://cdn-media-1.freecodecamp.org/images/KLLHVm1FdhMM-WM7LHEuOrswL37-0V1WUNF7)
_Tout un autre genre de problèmes de fratrie. Image via wordpress_

### Créer des listes

Revenant au problème de la fratrie, l'ajout de listes permettra une meilleure implémentation, et aura de nombreuses applications en Prolog. Le code utilisé précédemment peut encore être utilisé, cependant les résultats doivent être collectés dans une liste en utilisant ce qui suit :

```
liste_frères_soeurs(X, FrèresSoeurs) :- setof(Y, frère_soeur(X, Y), FrèresSoeurs) ; FrèresSoeurs = aucun.
```

**setof** rassemble toutes les issues possibles pour la requête `frère_soeur(X, Y)`, et les stocke dans une liste appelée FrèresSoeurs. Dans le cas où il n'y a pas de frères et sœurs, le composant **ou** (représenté par un point-virgule en Prolog) retourne aucun. **setof** supprime également les doublons, ne gardant que les valeurs uniques, améliorant ainsi la requête précédente. Maintenant qu'une liste de frères et sœurs peut être générée pour n'importe quel personnage, une requête séparée peut déterminer si 2 personnages sont frères et sœurs :

```
sont_frères_soeurs(X, Y) :- liste_frères_soeurs(X, FrèresSoeurs), member(Y, FrèresSoeurs).
```

Lorsqu'elle est interrogée, cela construit la liste FrèresSoeurs pour X et utilise **member** pour déterminer si Y est dans la liste FrèresSoeurs.

Maintenant qu'il y a des relations de fratrie, des relations parentales et de genre dans la base de données, vous n'avez pas besoin de visiter la Grande Bibliothèque de la Citadelle pour découvrir qui est la tante de Jon Snow.

![Image](https://cdn-media-1.freecodecamp.org/images/3dI6nBbgaPmvcpXKa7fozwtE9bGKF3poObzv)
_Aurait dû simplement utiliser Prolog. Image via usatoday_

### Récursivité

Les arbres généalogiques dans Game of Thrones s'étendent bien au-delà de la famille immédiate. Il est possible de s'aventurer plus loin et de générer des liens entre des relations plus lointaines. En utilisant le prédicat parent, Prolog peut évaluer récursivement la base de données pour trouver l'ascendance. Configurez la récursivité en incluant les 3 sections suivantes dans une base de données :

1. Section de terminaison — Cette section doit se produire avant la section de boucle, pour empêcher le programme de boucler indéfiniment :

```
ancêtre(X, Y) :- parent(X, Y).
```

2. Section de boucle — Cette section s'appelle elle-même de manière répétée, jusqu'à ce que la condition de terminaison ci-dessus soit remplie :

```
ancêtre(X, Y) :- parent(X, Z), ancêtre(Z, Y).
```

3. Section d'appel — requête ?-ancêtres(X, Ancêtre_de) pour commencer à stocker une liste d'ancêtres à travers chaque récursivité comme défini ci-dessus :

```
ancêtres(X, Ancêtre_de) :- findall(A, ancêtre(X, A), Ancêtres_de).
```

La fonction **findall** ici fonctionne de manière similaire à **setof**, cependant elle n'exclut pas les doublons et retourne une liste de personnes dont X est l'ancêtre.

### Impression et mise en forme

Si vous cherchez un guichet unique où vous pouvez obtenir toutes les informations sur un personnage, vous aurez besoin de mise en forme pour l'organiser. Pour retourner un tas d'informations en une seule fois, appelez les règles précédemment définies dans une règle :

```
parle_moi_de(X) :- vivant_ou_mort(X), parents(X, Parents), format("Parents : ~w", [Parents]), nl, enfants(X, Enfants), format("Enfants : ~w", [Enfants]), nl, liste_frères_soeurs(X, FrèresSoeurs), format("Frères et sœurs : ~w", [FrèresSoeurs]), nl, !.
```

**format** retourne toute sortie des crochets en place du ~w, et imprime tout ce qui est enfermé dans les guillemets. **nl** représente une nouvelle ligne. La fonction de coupure (**!**) en Prolog empêche le retour en arrière, donc force le programme à arrêter de trouver des solutions supplémentaires après que la première a été trouvée. Dans ce qui précède, cela garantit que tout est imprimé une fois. Interroger cela avec Stannis Baratheon donne ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/2XYV4yOyu5NiJAx-bdRpne-66sOfDOrMCnvO)

La fonction **print** peut également être utilisée à la place de format, lorsqu'il n'y a pas de variables à sortir.

![Image](https://cdn-media-1.freecodecamp.org/images/VlEjB6izTlNvedDdXOz2bcbvCcApzIXpOeqo)
_Le code est long et plein d'erreurs. Image via HBO_

### Utilisation de l'arithmétique

Les opérations arithmétiques peuvent être utilisées en Prolog pour interpréter et analyser des données. Supposons qu'Arya veuille maintenant être super organisée et utiliser Prolog au lieu de mémoriser sa liste. Elle pourrait utiliser ce qui suit pour garder une trace :

```
liste_arya :- print("LISTE TOP SECRET D'ARYA. INTERDIT."), nl, findall(X, sur_liste(X), ListePrincipale), coché(Liste), format("Fait : ~w", [Liste]), nl, pas_mort_encore(AutreListe), format("Reste à faire : ~w", [AutreListe]), nl, length(AutreListe, LListeComplétée), length(ListePrincipale, LListePrincipale), Pourcent is ((LListePrincipale - LListeComplétée) / LListePrincipale) * 100, Pourcentage is round(Pourcent), format("Pourcentage complété : ~w%", [Pourcentage]), nl.
```

Dans liste_arya, j'ai utilisé les opérateurs suivants :

* * Multiplier
* - Soustraire
* / Diviser
* length(). Générer la longueur de la liste
* round(). Arrondir à l'entier le plus proche

Le résultat est le suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/yqf4CUXcnSht0c9z8W-3hagkkwoccwCO2yut)

![Image](https://cdn-media-1.freecodecamp.org/images/4S0ZSFXJQYC51AGKvHdKdUceVF7P0EA-EZjj)
_est_arya :- fille(X), sans_nom(X). Image via inverse_

Avec tous les outils couverts, il y a beaucoup d'autres façons intéressantes d'explorer l'univers de Game of Thrones en Prolog. Ou, abandonnez complètement le visionnage de la série, après avoir déterminé qui devrait s'asseoir sur le Trône de Fer grâce à une programmation logique incontestable.

```
héritier_légitime(X) :- parent(robert_baratheon, X), statut(X, vivant).
```

Les résultats parlent d'eux-mêmes...

![Image](https://cdn-media-1.freecodecamp.org/images/CNwejVS4LLM8yTdS4EwTjc9QGlUUPgMPEUQQ)
_Ma boîte de réception est ouverte pour le débat._

Si vous voulez étendre la base de données existante, ou jouer à créer vos propres relations, le code est sur mon [GitHub](https://github.com/rachelwiles/GoT-Check).

Suivez mon [LinkedIn](https://www.linkedin.com/in/rachelwiles/) pour les projets futurs.