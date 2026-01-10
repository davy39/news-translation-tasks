---
title: Algorithmes de graphes pour les entretiens techniques
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-08-04T01:35:10.000Z'
originalURL: https://freecodecamp.org/news/graph-algorithms-for-technical-interviews
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/graph-interview.png
tags:
- name: interview
  slug: interview
- name: youtube
  slug: youtube
seo_title: Algorithmes de graphes pour les entretiens techniques
seo_desc: 'During technical interviews it is common for your interviewer to ask you
  to solve coding challenges. And you should have a good understanding of graph algorithms
  if you want to do well on these challenges.

  We just published a course on the freeCodeCa...'
---

Lors des entretiens techniques, il est courant que votre interlocuteur vous demande de résoudre des défis de codage. Et vous devez avoir une bonne compréhension des algorithmes de graphes si vous voulez bien réussir ces défis.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous apprendra les algorithmes de graphes et comment les utiliser pour résoudre des défis de codage.

Alvin Zablan a créé ce cours. Le cours de programmation dynamique d'Alvin est l'un des cours les plus populaires sur la chaîne freeCodeCamp, et maintenant il est de retour pour vous enseigner les algorithmes de graphes.

Voici les sujets et algorithmes abordés dans ce cours :

* bases des graphes
* parcours en profondeur et en largeur
* a un chemin
* chemin non orienté
* compte des composants connectés
* plus grand composant
* plus court chemin
* compte des îles
* île minimale

Regardez le cours complet ci-dessous ou sur [la chaîne YouTube freeCodeCamp.org](https://youtu.be/tWVWeAqZ0WU) (2 heures de visionnage).

%[https://youtu.be/tWVWeAqZ0WU]

## Transcription

(générée automatiquement)

Ce cours vous aidera à apprendre ce dont vous avez besoin pour implémenter des algorithmes de graphes et les utiliser pour résoudre des défis de codage.

Le cours de programmation dynamique d'Alvin est l'un des cours les plus populaires sur notre chaîne.

Et maintenant il est de retour pour vous enseigner les algorithmes de graphes.

Hey, programmeurs, je suis Alvin de Structy.

Bienvenue dans notre cours sur les graphes.

Et en particulier, cela va concerner les graphes pour vos entretiens techniques.

Bien sûr, les graphes sont un sujet très courant lorsqu'il s'agit de ces entretiens techniques.

Et en particulier, ce que je veux souligner tout au long de ce cours, c'est la poignée de motifs qui reviennent encore et encore, lors de ces entretiens techniques.

En juste environ deux heures et demie, je vais vous donner tous les outils dont vous avez besoin pour couvrir, je dirais, environ 80 % de tous les problèmes de graphes.

Et donc ce que j'ai en réserve pour ce cours, eh bien, je pense que la clé de la victoire pour vos structures de données et algorithmes, et surtout vos graphes, est de visualiser les choses, n'est-ce pas.

Donc ce que nous allons faire, c'est tracer à travers de nombreux algorithmes différents, et être sûr de les comprendre à un niveau élevé.

Et cela signifie passer à travers différentes animations ici, je pense que les graphes ont une assez mauvaise réputation pour être un sujet difficile.

Parce que pour un débutant, vous pouvez avoir des récits très, très différents autour d'un problème, et ne pas vraiment comprendre.

Ils sont tous vraiment basés sur une prémisse de graphe.

Donc nous allons réaliser qu'un tas de choses différentes peuvent être comprises comme des graphes.

Donc lorsqu'il s'agit des prérequis de ce cours, je vais supposer que vous ne savez rien sur les graphes.

Mais vous savez comment coder, n'est-ce pas, donc je vais avoir l'attente que vous compreniez un peu de récursivité.

Donc au fur et à mesure que vous travaillez à travers le cours, et apprenez les différents motifs de graphes, nous allons utiliser ces motifs pour résoudre certains problèmes classiques d'entretien sur les graphes, n'est-ce pas.

Et je vais vous donner beaucoup d'opportunités pour pratiquer ces motifs dans différents problèmes que nous aurons prêts lorsque vous les aurez lors d'un entretien technique.

Ce que j'aime dans le sujet des graphes, c'est qu'en utilisant juste une poignée d'algorithmes différents, vous pouvez couvrir la majorité des problèmes de graphes, n'est-ce pas.

Pour chaque problème de graphe que nous couvrons, nous allons le diviser en deux sections, la section une va concerner l'approche pour la vidéo.

Donc nous allons passer en revue la stratégie et la théorie globale, et être sûr de dessiner une belle image significative.

Nous allons également parler de la complexité de l'algorithme dans la vidéo d'approche.

Suite à chaque approche, nous allons également implémenter le code bien sûr, je vais écrire tout mon code en JavaScript, vous pourrez suivre dans n'importe quel langage que vous aimez.

Donc cela signifie que parfois je vais passer à mon éditeur de code où vous pourrez bien sûr suivre.

Nous allons également être sûr de fournir des liens dans la description ainsi que des liens à l'écran.

De cette façon, vous pouvez formellement lire les invites pour chaque problème, ainsi que regarder les différents cas de test.

D'accord, je pense que c'est assez d'introduction.

Pour l'instant, plongeons directement dans le cours.

D'accord, programmeurs.

Donc plongeons directement dans le cours, je veux commencer par vous donner quelques informations sur vos graphes, nous allons passer en revue les bases des graphes dont vous avez besoin pour commencer à attaquer les problèmes lors d'un entretien technique.

Tout d'abord, qu'est-ce qu'un graphe ? Un graphe est vraiment juste une collection de nœuds et d'arêtes.

En ce qui concerne les nœuds, vous pouvez les visualiser comme typiquement juste quelques cercles avec des données à l'intérieur.

Donc je vais mettre quelques valeurs de lettres dans mes nœuds ici.

Et lorsque nous faisons référence aux arêtes, cela serait juste n'importe quelles connexions entre les nœuds.

Par exemple, s'il y avait une connexion entre A et C, cela ressemblerait à quelque chose comme ceci, n'est-ce pas ? Ce que je peux dire formellement, c'est qu'il y a une arête entre A et C, je peux créer de nombreuses arêtes entre n'importe quels nœuds que je veux dans ce graphe.

Un autre mot que vous pourriez entendre dans la nature en ce qui concerne la description des nœuds, vous pourriez entendre le mot sommet être utilisé, n'est-ce pas, ils sont vraiment la même chose.

Dans ce cours, je vais m'en tenir au mot nœud.

Et une arête est juste une connexion entre une paire de nœuds.

Et c'est vraiment tout ce qu'un graphe est à un niveau élevé, là où les choses deviennent intéressantes, c'est comment nous pouvons utiliser ce cadre de graphe pour résoudre un problème, n'est-ce pas.

Donc si vous pensez à ces nœuds comme à des choses et aux arêtes comme à des relations, un graphe est une grille décrivant la relation entre les choses.

Par exemple, nous pouvons dire que les nœuds ici sont des villes et les arêtes seraient des routes reliant les villes de manière similaire, peut-être que nos nœuds ici sont des cours, et ensuite les arêtes représentent les prérequis.

Et donc à l'avenir, nous allons utiliser les graphes comme un moyen d'illustrer et de cadrer un problème narratif.

Parlons de ce graphe.

En particulier, ici, j'ai vraiment dessiné un graphe dirigé.

Et c'est parce que j'ai quelques flèches le long des arêtes.

Cela serait une comparaison à un graphe non dirigé.

Donc ici, j'ai vraiment la même structure, sauf que je n'ai pas de flèches sur les arêtes ici.

Et cela signifie qu'il n'y a pas de directionnalité, n'est-ce pas.

Si je regarde le graphe dirigé, disons que j'étais au nœud A, eh bien, alors je peux voyager vers B ou C, disons que je me déplace vers C.

Cependant, une fois que je suis à C, je ne peux pas voyager vers A, je ne peux voyager que vers E, n'est-ce pas ? C'est parce que je dois obéir à la direction des flèches ici.

En prenant un coup d'œil à mon graphe non dirigé, disons que j'étais actuellement situé à la scène ici, que j'ai l'option de voyager vers A ou E, n'est-ce pas ? Donc si je voyageais vers A, c'est bon, je peux même revenir à C.

Donc pensez à un graphe non dirigé comme une rue à double sens.

Pour l'instant, nous allons juste continuer avec notre version dirigée.

Je vais également introduire quelques termes utiles que nous pouvons utiliser lorsque nous parlons des nœuds dans notre graphe.

Si j'étais actuellement situé à ce nœud A, je peux me référer à B et C comme des nœuds voisins.

D'accord, donc un nœud voisin est vraiment n'importe quel nœud qui est accessible par une arête, bien sûr, en obéissant à la direction de l'arête.

En d'autres termes, si j'étais actuellement situé au nœud C, j'ai seulement un voisin E, n'est-ce pas, si je suis à C, vous savez, alors je ne considérerai pas A comme un voisin.

Super.

Lorsque vous visualisez des algorithmes de graphes, vous devriez vraiment esquisser une image qui ressemble exactement à ceci, littéralement déposez des nœuds comme des cercles et des flèches comme vos arêtes ici.

Cependant, lorsqu'il s'agit de la manière dont nous implémentons cet algorithme dans du code, nous allons devoir le représenter de manière plus programmatique.

N'est-ce pas ? Dans mon esprit, je pense à cette image de nœuds et de flèches entre eux.

Cependant, dans mon programme, je vais utiliser typiquement une liste d'adjacence, c'est probablement notre manière préférée de représenter et d'informer les graphes, n'est-ce pas.

Selon le langage de programmation de choix que nous allons utiliser typiquement, nous utiliserions une structure de données de type hash map pour représenter une liste d'adjacence.

Vraiment, nous attendons avec impatience d'utiliser une structure de données de recherche en temps constant, je vais chercher une structure de données de mappage clé-valeur, n'est-ce pas.

Donc si vous êtes en JavaScript, ce sera un objet, si vous êtes en Python, ce sera un dictionnaire.

Si vous êtes dans un langage comme Java, ou C, vous utiliserez une carte non ordonnée.

En regardant cette carte de hachage, j'ai dessiné ou cette liste d'adjacence, les clés de cette liste d'adjacence vont être chaque nœud de mon graphe, n'est-ce pas, donc j'ai juste toutes les valeurs de nœuds A à F disposées comme les clés.

Cependant, si vous regardez les valeurs correspondantes, les valeurs vont en fait être un tableau, n'est-ce pas ? Donc si je regarde cette toute première entrée, elle dit que j'ai un nœud A et ensuite dans le tableau peuplé de tous les voisins de A, c'est-à-dire que A a deux voisins B et C.

C'est pourquoi j'ai cette correspondance dans ma liste d'adjacence.

Cela est vrai pour chaque entrée dans mes listes d'adjacence.

Par exemple, disons que je regarde l'entrée pour E.

Donc je vais à l'endroit et fais une liste adjacente où la clé est E, elle n'a qu'une seule arête sortante vers B.

C'est pourquoi le tableau pour E ne contient que B.

Une chose à noter également est que même si un nœud n'a pas de voisins, il doit toujours apparaître comme une clé dans ma liste d'adjacence.

Par exemple, si vous regardez le nœud D, le nœud D n'a pas d'arêtes sortantes.

C'est pourquoi son tableau de voisins est vide.

Cependant, il doit toujours apparaître au moins comme une clé dans mes listes d'adjacence, n'est-ce pas, de cette façon, vous pouvez toujours savoir que le nœud D existe.

Au début du cours, nous allons généralement prendre une liste d'adjacence comme information pour représenter un graphe, n'est-ce pas.

Mais lorsque nous esquissons les choses sur le tableau blanc, nous devons les visualiser en utilisant une belle image comme celle-ci.

Super.

Donc plongeons dans notre première paire d'algorithmes.

Pour moi, l'algorithme à connaître pour un graphe va vraiment être de faire une sorte de parcours dessus.

Pourquoi ne pas commencer par parler d'un parcours en profondeur, quelque chose que vous avez peut-être déjà entendu, maintenant nous allons parler de l'algorithme de parcours en profondeur qui opère sur un graphe.

Donc commençons par comprendre à un niveau élevé l'ordre qu'un parcours en profondeur vous donnerait.

Donc disons que j'avais un nœud de départ, et je vais choisir A comme mon nœud de départ, donc je vais le colorier ici en jaune.

Si je suivais un parcours en profondeur.

Maintenant que je l'ai choisi comme mon point de départ, je peux soit choisir B ou C.

Ensuite, je vais simplement m'engager à utiliser B.

Donc disons que j'avais la séquence jusqu'à présent A, B.

Et à ce stade, si je suivais vraiment un parcours en profondeur, je dois aller plus profondément vers le nœud D.

En d'autres termes, je ne vais pas encore au nœud C.

Cool, ce serait un vrai parcours en profondeur, n'est-ce pas.

À ce stade, maintenant que j'ai atteint le fond à D, D est une impasse, n'est-ce pas ? Je ne peux pas voyager vers F depuis D, car cela désobéirait à la flèche.

Et donc maintenant je peux me déplacer vers cet autre voisin de C.

Et à partir de là, l'algorithme continuerait, n'est-ce pas, je vais de C à E, puis de E à B.

Et techniquement, je devrais parcourir deux fois certains nœuds comme B et D ici.

Donc globalement, dans cette coloration jaune, j'ai coloré la région complète qu'un parcours en profondeur explorerait en partant de A, notez que si vous partiez de A, il serait impossible d'atteindre F.

Et c'est assez normal, n'est-ce pas ? C'est un peu pourquoi nous utilisons ces algorithmes de parcours qui peuvent vous dire si vous pouvez voyager entre certains nœuds ou non.

Et nous verrons ce problème littéral plus tard.

N'est-ce pas ? Donc vous vous demandez probablement, exactement comment implémentons-nous cela, mais pour l'instant, je veux juste rester concentré sur l'ordre que nous avons obtenu, n'est-ce pas.

Donc concernant notre parcours en profondeur, nous nous souvenons des trois premières itérations de l'algorithme, nous avons la séquence A, B, D, n'est-ce pas, c'est indicatif d'un parcours en profondeur.

Maintenant, comparons cela au parcours en largeur.

Donc je vais poser le même graphe exact, nous allons également commencer un parcours au nœud A, mais cette fois suivre un ordre en largeur d'abord.

Donc j'ai A en premier et disons, vous savez, j'ai choisi B comme mon prochain nœud lorsqu'il s'agit d'un parcours en largeur d'abord.

Cela n'a pas d'importance, comme quel voisin initial vous choisissez, donc je vais simplement choisir B.

Mais maintenant que j'ai choisi B, si je suivais un vrai parcours en largeur d'abord, je dois frapper C ensuite, n'est-ce pas.

Et c'est la principale différence entre nos parcours en profondeur et en largeur pour le même graphe, mon parcours en profondeur commencerait par A, B, D, tandis que mon parcours en largeur commencerait par A, B, C.

Et donc vous vous demandez probablement, y a-t-il une importance entre cette nuance ? Quand préférerais-je la profondeur à la largeur, ou vice versa ? Un parcours en profondeur ou en largeur explorerait les mêmes nœuds exacts dans un graphe.

Cependant, il les explorerait dans un ordre différent, n'est-ce pas ? Et cela est plus évident à voir lorsque nous avons un graphe plus grand avec beaucoup plus d'arêtes.

Et donc regardons comment le parcours en profondeur explore à nouveau, mais cette fois sur un graphe beaucoup plus grand, regardons celui-ci.

Donc je vais choisir un nœud aléatoire comme point de départ, disons que j'ai choisi ce nœud en jaune, qui faisait un parcours en profondeur, ce que je vais faire, c'est choisir une direction et voyager dans cette même direction aussi loin que possible avant de changer de direction.

Donc disons que je me déplace vers la droite, à ce stade, je devrais continuer à me déplacer vers la droite, jusqu'à ce que je ne puisse plus me déplacer vers la droite, auquel cas, je dois choisir de nouvelles directions, disons que c'était vers le bas.

Je vais continuer à faire cela jusqu'à ce que je ne puisse plus me déplacer vers le bas.

Et donc je devrais me déplacer vers la gauche maintenant, maintenant je vais continuer à poursuivre ce seul chemin dans une direction très profonde.

Donc c'est un comportement indicatif d'un parcours en profondeur, n'est-ce pas, vous explorez une direction aussi loin que possible avant de changer de direction.

Comparons cela à un parcours en largeur.

Donc disons que nous commençons au même nœud en rose, si je suivais un parcours en largeur, cela ressemblerait à quelque chose comme ceci.

À partir du point de départ, j'explorerais tous les voisins immédiats de ce nœud, un peu comme un cercle.

Maintenant, je continue simplement à appliquer ce comportement.

Donc comme vous le remarquez à propos du parcours en largeur, c'est qu'il tendra à explorer toutes les directions de manière égale, n'est-ce pas, au lieu de simplement favoriser une seule direction tout au long.

C'est vraiment la seule différence entre un parcours en profondeur et un parcours en largeur.

Plus tard dans le cours, je soulèverai des problèmes explicites où vous pourriez préférer l'un à l'autre.

D'accord, mais pour l'instant, ce que je veux faire est de vous donner toutes les bases dont vous avez besoin.

Donc vous pouvez réellement construire cet algorithme, nous allons en parler à un niveau élevé, considérons cela comme le pseudocode, puis, bien sûr, nous l'exprimerons dans du code JavaScript plus tard.

Donc lorsqu'il s'agit de l'implémenter réellement en code, ces deux algorithmes, la clé est de comprendre qu'un parcours en profondeur utilise une pile, et un parcours en largeur utilise une file d'attente, rappelez-vous qu'une pile est quelque chose où vous ajoutez au sommet et retirez du sommet également, ou est-ce qu'une file d'attente est quelque chose où vous ajoutez à l'arrière et retirez de l'avant, et cela vous donne deux ordonnancements très différents.

C'est vraiment la seule différence entre ces deux algorithmes.

Donc commençons par tracer notre parcours en profondeur, bien sûr, en utilisant une pile, donc je vais utiliser un graphe légèrement différent.

Et pour visualiser ma pile, je vais utiliser cette barre pour représenter le bas de ma pile, évidemment, pour moi, au moins je pense à une pile comme une structure de données verticale.

Cool.

Donc disons que j'ai arbitrairement choisi A comme mon nœud de départ pour effectuer mon parcours en profondeur, n'est-ce pas, à long terme, je veux simplement imprimer toutes les différentes valeurs de nœuds dans ce graphe.

Donc ce que je vais faire, c'est prendre mon nœud de départ A, et je vais simplement l'initialiser sur ma pile.

Donc maintenant, comme la seule chose sur ma pile, c'est aussi au sommet de ma pile.

Et maintenant je peux entrer dans le flux de l'algorithme principal ici, parce que j'ai une pile, ce que je peux faire est de retirer le sommet de ma pile.

Donc cela signifie que je retire A de la pile, et considère le nœud A, mon nœud actuel étant regardé, n'est-ce pas ? À ce stade, disons que j'imprime A sur ma console.

Et à partir de là, ce que je veux faire est de considérer les voisins de A, n'est-ce pas.

Donc si je regarde le nœud C, ce que je devrais faire est simplement pousser C vers la pile, puis aussi pousser B vers la pile, n'est-ce pas.

Et cela n'a pas d'importance comme l'ordre dans lequel vous poussez ces voisins.

Si je veux frapper B en premier, alors je vais les pousser en second, n'est-ce pas ? Super.

Cela mettrait fin à ma première itération de ce parcours en profondeur.

Cool.

Donc à ce stade, je peux regarder ma pile, et ma pile a encore des données dessus.

Donc je devrais faire est encore, retirer le sommet de ma pile.

Donc je vais retirer B de ma pile.

Et cela devient mon courant, je vais aussi l'imprimer.

À ce stade, je regarde les voisins de B, B a un voisin D et donc je pousse D au sommet de la pile.

Remarquez que parce que j'ai une pile, D se retrouve au-dessus de C, n'est-ce pas.

Et donc maintenant lorsque j'arrive à une autre itération, lorsque je retire le sommet de ma pile, je regarde le nœud D comme mon courant, n'est-ce pas, et je peux imprimer D.

Et cela semble bien parce que jusqu'à présent, mon ordre d'impression serait A, B, D, remarquez que j'ai poursuivi ce chemin unique profondément en suivant A, B, D.

Mais je dois regarder les voisins de D, je peux prendre F et simplement le pousser au sommet de ma pile.

Prochaine itération, ma pile n'est toujours pas vide.

Donc je devrais retirer le sommet, F est maintenant mon courant, je peux imprimer F, mais F n'a pas de voisins.

Donc F ne va pas pousser autre chose au sommet de la pile.

N'est-ce pas ? À ce stade, j'arrive à cette prochaine passe, et je retire le sommet de ma pile.

Et cela signifie que C est maintenant mon courant, je peux imprimer la valeur de C.

Et puis je peux regarder les voisins de C.

Et je pousse simplement E au sommet de ma pile.

Lors de cette dernière itération, j'ai retiré E de ma pile, E est maintenant mon courant, je l'imprime, puisque E n'a pas de voisins, je ne pousse rien d'autre au sommet de ma pile.

Et à ce stade, j'ai atteint l'état où ma pile est vide.

Et cela signifie que mon algorithme est terminé, n'est-ce pas, cela signifie que vous avez exploré aussi loin que possible dans votre graphe.

Remarquez que ce n'est pas nécessairement le cas que vous puissiez atteindre chaque nœud du graphe.

Dans cet exemple particulier, c'était possible, super.

Donc refaisons cette trace en utilisant notre algorithme de parcours en largeur, ce qui signifie que nous ajustons légèrement les choses.

Et nous utilisons un ordre de file d'attente.

Rappelez-vous qu'une file d'attente est une structure de données premier entré, premier sorti, ce qui signifie que les choses entrent par l'arrière, puis sortent par l'avant.

Et donc disons que j'utilise cette flèche pour représenter la directionnalité de ma file d'attente, n'est-ce pas.

Et je commence l'algorithme de la même manière pour mon parcours en largeur.

Disons que je veux qu'il commence au nœud A.

Donc je vais simplement initialiser ma file d'attente avec A, cool, donc je commence par retirer le front de ma file d'attente.

Donc A devient mon nœud actuel, je peux aussi imprimer A.

Et maintenant je considère les voisins de A, n'est-ce pas.

Donc je considère B et C.

Si je voulais aller à B avant C, alors je devrais pousser B dans ma file d'attente en premier, n'est-ce pas, donc j'ajoute B à l'arrière de ma file d'attente, n'est-ce pas.

Et je devrais aussi ajouter C à l'arrière de ma file d'attente, n'est-ce pas.

Et cela mettrait effectivement fin à ma première itération.

Donc maintenant je regarde ma file d'attente qui a encore des éléments.

Donc je retire le front de ma file d'attente, cela signifie que B devient mon nœud actuel.

Bien sûr, j'imprime B.

Maintenant je considère les voisins de B.

Donc je regarde simplement le nœud D, et je pousse D à l'arrière de la file d'attente, puisque D entre par l'arrière et se retrouve derrière C, et c'est vraiment un comportement important.

Prochaine itération, je retire le front de ma file d'attente.

Donc mon nœud actuel est maintenant C, n'est-ce pas, je peux imprimer C, et puis regarder les voisins de C qui sont juste E et j'ajoute E à l'arrière de la file d'attente, ce qui signifie que dans l'ordre de ma file d'attente, E se retrouve derrière mon prochain itération, je retire D de la file d'attente, et j'imprime les voisins de D qui est F à l'arrière de la file d'attente.

Prochaine itération, je retire E du front de ma file d'attente, je l'imprime.

Puisque E n'a pas de voisins, il ne va pas ajouter autre chose à l'arrière de la file d'attente.

Et bien sûr, finalement, F quitte le front de ma file d'attente, j'imprime F, F n'a pas de voisins, auquel point maintenant ma file d'attente est totalement vide.

Et puisque notre file d'attente est vide, ce serait la fin de notre algorithme.

D'accord, et c'est tout ce qu'il y a à nos algorithmes de parcours en profondeur et en largeur, ils vont être le code de base agréable que nous utilisons pour résoudre de nombreux problèmes de graphes différents.

Je pense que c'est assez de théorie.

Pour l'instant, ce que je veux faire est de passer maintenant à mon éditeur de code, où vous pouvez réellement implémenter ceux-ci en JavaScript, hey, programmeurs, me voilà dans mon éditeur, ce que je veux faire est de vous montrer comment implémenter ces algorithmes de parcours en profondeur et en largeur.

Donc nous allons commencer par le parcours en profondeur.

Et mon objectif est vraiment de construire une fonction qui imprimera toutes mes valeurs dans le graphe, selon un parcours en profondeur, n'est-ce pas, nous allons définir cette fonction depth first print, en faisant une fonction fléchée en JavaScript, elle va prendre le graphe, qui va être donné sous forme de liste d'adjacence.

Et c'est en fait le même graphe.

Maintenant, le dernier exemple que nous avons tracé, je vais également avoir besoin de spécifier un nœud de départ ici, je l'appellerai un nœud source, nous allons commencer le parcours.

En commençant à ce nœud.

Cool.

Et donc nous savons qu'inhérent à un parcours en profondeur va être une pile.

Donc je vais vous montrer comment implémenter cela de manière itérative, ce qui signifie que vous avez besoin d'une pile explicite.

Pour moi en JavaScript, c'est aussi simple que d'utiliser un tableau JavaScript, n'est-ce pas ? Je vais le rendre vide au début.

Et je peux utiliser ce tableau comme une pile, si je m'engage simplement à utiliser des opérations qui manipulent la même extrémité du tableau.

En d'autres termes, si j'utilise simplement push et pop, cela manipulera toujours la fin du tableau, n'est-ce pas, en retirant et en ajoutant à la fin de ce tableau.

Ce que je veux vraiment m'assurer de faire est d'initialiser la pile avec mon nœud de départ, c'est-à-dire avec mon nœud source.

Rappelez-vous qu'un nœud ici est vraiment juste désigné par un caractère.

Cool.

Et lorsqu'il s'agit de concevoir la boucle principale de l'algorithme ici, voulez-vous continuer à exécuter l'algorithme tant que la pile n'est pas vide ? En d'autres termes, tant que la longueur de la pile est supérieure à zéro, je dois continuer à exécuter.

Cela rappelle beaucoup ce que nous avons exprimé sur le tableau blanc.

Donc lorsqu'il s'agit d'effectuer une seule itération de ce parcours en profondeur, ce que je veux faire est de retirer le sommet de ma pile.

Donc si je fais pile.pop, cela retirera le dernier élément d'un tableau, dans ce cas, comme le sommet de ma pile, et le retournera également.

Donc je vais sauvegarder cela dans une variable, je l'appellerai mon courant.

Et donc ce point serait en fait une excellente opportunité de simplement imprimer ce courant.

Donc je vais faire console.log(current), n'est-ce pas ? En regardant, vous savez, cet exemple ici, puisque j'initialise une pile pour contenir juste la note source de A, lors de la toute première itération, cette boucle while, je vais bien sûr, retirer A, puis je vais l'imprimer, n'est-ce pas.

Et à partir de ce point, ce que je veux faire est de considérer les voisins de A, B et C.

Donc si je veux regarder le tableau associé à A, je peux simplement le cliquer dans mon graphe, n'est-ce pas, car mon graphe est un objet maintenant.

Donc si je dis graph[source], si source est A, cela signifie que graph[source] me donnerait ce tableau.

Je veux itérer à travers chaque nœud ou chaque voisin dans ce tableau.

Donc je vais imbriquer une boucle ici.

Et je dis pour let neighbor de ce tableau.

Donc si vous êtes familier avec JavaScript, si vous utilisez simplement une boucle for of, ils itèrent un ordre à travers un tableau.

Donc maintenant je rencontre un voisin comme B et un voisin comme C.

Ce que je veux faire avec ces voisins est simplement les pousser au sommet de ma pile.

Donc ce sera simplement stack.push(neighbor).

Super, je vais m'assurer de pousser chaque voisin qu'il a.

Donc parfois j'aurai deux voisins.

D'autres fois j'aurai un voisin, ou même aucun voisin.

C'est vraiment tout ce qu'il y a à implémenter une belle base de parcours en profondeur.

Une chose que je veux souligner, ma manière préférée d'implémenter cet algorithme est de considérer le traitement de votre nœud, lorsqu'il quitte la pile, et non lorsqu'il entre dans la pile.

En d'autres termes, j'écris généralement mon instruction d'impression, juste après qu'un élément est retiré.

Et la chose que je retire est exactement ce que j'imprime.

N'est-ce pas.

Donc allons-y et donnons un essai à cela, voyons ce que nous obtenons.

Il semble que dans mon terminal, j'ai obtenu l'ordre AC e b df, ce qui est légèrement différent de ce que j'attendais.

Cependant, ce serait également un parcours en profondeur valide, nous devons garder à l'esprit que, selon l'ordre arbitraire des valeurs dans le même tableau de voisins, vous pourriez tendre vers une direction différente au début, n'est-ce pas ? La chose la plus importante que je recherche lorsqu'il s'agit de vérifier un parcours en profondeur est de m'assurer que je poursuis la même direction avant de changer de direction, n'est-ce pas.

Donc puisque j'ai commencé avec A C, je vais A et puis à C ici, le prochain mouvement serait d'aller à E et c'est exactement ce qui s'est passé dans mon code, n'est-ce pas.

Et une fois que j'ai atteint E, c'est en fait une impasse.

Donc je peux ensuite passer à mon autre voisin latéral comme B, n'est-ce pas.

Et donc je peux obtenir le même ordre attendu ici, si je retourne simplement cela.

Et donc je mets C suivi de B.

Je vais donner un essai.

Ils sont tous les deux valides.

Parcours en profondeur.

Voir ce que nous avons maintenant.

Cool, maintenant j'obtiens l'ordre exact de A, B, D, F, C.

Et réfléchissez vraiment à pourquoi c'est le cas, n'est-ce pas.

Donc disons que je viens de retirer A de ma pile.

Donc j'ai imprimé A, ce n'est rien de fantaisiste, n'est-ce pas.

Et à partir de là, je commence à itérer à travers le tableau qui est associé à A, n'est-ce pas, donc lors de la première itération, j'itère à travers C, n'est-ce pas ? Si je pousse C sur la pile, disons que c'est le bas de ma pile, en poussant sur la pile, c'est juste ici.

Puis suivi par cela, j'ai poussé B sur la pile.

Maintenant B est au sommet.

Puisque B est au sommet, je sais que la prochaine itération de haut niveau, cette boucle while, je devrais retirer B et ce sera le prochain nœud que je visite.

Et donc ils sont vraiment tous les deux des parcours en profondeur.

Bien.

Donc deux choses à noter, vous allez définitivement utiliser une pile pour implémenter le parcours en profondeur.

Et vous pouvez utiliser la pile de quelques manières différentes.

N'est-ce pas ? Donc ici j'utilise une pile explicite comme un tableau.

Et je l'implémente en utilisant un code itératif.

N'est-ce pas.

Donc en utilisant quelques boucles, n'est-ce pas, ce que vous pouvez aussi faire est implémenter le parcours en profondeur de manière récursive, car je sais que toute récursion utilise la pile d'appels sous-jacente.

Donc laissez-moi vous montrer comment implémenter cela également.

Et lorsqu'il s'agit d'avoir toutes ces différentes outils dans votre arsenal, je vous recommande définitivement de pratiquer les deux versions itérative et récursive.

Nous verrons cela plus tard dans ce cours.

Donc disons que je voulais résoudre le même problème.

Mais maintenant de manière récursive, ce sera en fait moins de code.

Donc je vais avoir les mêmes arguments, je vais avoir le graphe qui est la liste d'adjacence ainsi qu'un nœud source, considérons le nœud source comme votre position actuelle.

Donc si je suis à un nœud, peut-être que la première chose que je devrais faire est simplement l'imprimer, n'est-ce pas, imprimer ce nœud, donc je vais faire console.log de ce nœud source.

Et cela semble bien dès le départ car lorsque nous faisons un appel de haut niveau à cette fonction récursive, ils passent A comme nœud source.

Donc je veux commencer par A comme premier nœud dans mon impression, et à partir de là, je dois regarder les voisins de A.

Eh bien, si vous voulez regarder les voisins comme avant, il suffit de cliquer dans le graphe, la liste d'adjacence en utilisant ce nœud, n'est-ce pas, et cela me donnerait un tableau de CNB.

Maintenant, je vais simplement itérer à travers ce tableau.

Donc je vais dire pour que le voisin de ce tableau.

Et à ce stade, ce que je veux faire est maintenant faire la récursion, n'est-ce pas, donc je fais un appel récursif sur chacun de ces voisins.

Donc pour moi, cela signifie simplement appeler depth first print, vous donnez le même graphe, n'est-ce pas, l'objet graphe ne change pas, mais vous devriez changer le nœud source.

Maintenant, vous voulez passer ce voisin comme nœud source.

Et vous allez faire un appel récursif pour chaque voisin dans ce tableau.

Et cela serait en fait tout ce dont nous avons besoin.

Allons-y et exécutons simplement cette version.

Diviseur d'exécution ici.

Il semble que maintenant nous obtenons l'ordre AC E, B, D, F.

Et c'est vraiment encore un autre type de depth first print, n'est-ce pas, pas exactement cet ordre, parce que cette fois nous avons poursuivi C en premier, n'est-ce pas, nous sommes allés A C, je veux obtenir exactement cet ordre dans ma récursion, alors je devrais mettre B en premier, vraiment le même type de motif.

Maintenant, obtenons cela dans l'exécution.

Bien AB de FC.

Une chose que je veux souligner à propos de cette récursion en premier, c'est qu'elle n'a pas de cas de base explicite, ce qui signifie qu'il n'y a pas de déclaration if évidente qui retourne simplement comme vous le verriez typiquement dans la plupart des récursions.

C'est parce que dans ce problème, j'ai un cas de base implicite lorsqu'un nœud comme E est une impasse.

D'accord, disons que mon source actuel qui arrive est E, eh bien, alors lorsque j'itère dans cette boucle for, j'itère à travers ce tableau vide, je veux dire avoir zéro itération.

Si vous avez zéro itération, alors vous ne faites jamais d'appel récursif.

N'est-ce pas ? C'est la même chose que d'avoir un cas de base, n'est-ce pas ? Un cas de base est vraiment juste un scénario où nous n'avons pas d'appel récursif.

C'est ainsi que ce code fonctionne encore.

D'accord, donc maintenant vous savez comment implémenter la profondeur en premier de deux manières, n'est-ce pas, itéré et récursivement.

Et ils utilisent tous les deux définitivement une pile.

Laissez-moi maintenant vous montrer comment implémenter votre largeur en premier, n'est-ce pas, commenter aussi une partie de ce code.

Maintenant, nous allons faire une belle largeur en premier, me donner un peu d'espace ici.

Donc pour une largeur en premier, nous voulons résoudre le swan de manière itérative.

Et c'est vraiment seulement possible de manière itérative, n'est-ce pas.

Donc je sais qu'un parcours en largeur exige une file d'attente, si vous essayez de faire un parcours en largeur en utilisant une sorte de récursion, et sous le capot, il y a une structure de données de pile, cela va lutter contre l'ordre de la file d'attente que vous voulez, n'est-ce pas ? Donc pour un parcours en largeur, vous allez toujours typiquement écrire un code itératif.

Donc quelques boucles, n'est-ce pas ? Laissez-moi définir cela, je vais dire breadth first print, prendre le graphique complet, la liste d'adjacence, ainsi que le nœud source, je veux initialiser ma file d'attente.

Avec ce nœud source, encore une fois, la file d'attente ici va juste être un tableau en JavaScript.

Donc je vais dire const q equals un tableau qui commence avec juste le nœud source.

Super.

Et je vais utiliser cette file d'attente en m'engageant simplement à deux méthodes spécifiques sur mes tableaux en JavaScript.

Donc si j'utilise array dot shift, cela retire le premier élément d'un tableau.

Si je fais array dot push, cela ajoute à la dernière position d'un tableau.

Et utiliser ces deux méthodes en combinaison me donnerait une belle file d'attente, n'est-ce pas, ajouter à une extrémité et retirer de l'autre extrémité.

Donc comme avant, nous allons avoir une boucle while, nous allons itérer tant que notre file d'attente n'est pas vide.

Et donc tant que la longueur de la file d'attente est supérieure à zéro, c'est bien.

Et comme notre itératif, vous savez, au début, vous voulez commencer par simplement retirer le front de votre file d'attente.

Donc je vais dire q dot shift, cela retirera le premier élément ainsi que me le retourner.

Donc je peux le sauvegarder dans une variable, j'aime l'appeler current, comme le tableau blanc, n'est-ce pas ? Et à partir de là, peut-être que je vais l'imprimer.

Donc console dot log, ce nœud actuel.

Et à partir de là, considérez simplement vos voisins, n'est-ce pas.

Donc si je clique dans mon graphe, en utilisant ce nœud actuel, cela me donne un tableau de ses voisins, je veux boucler à travers chacun de ces voisins.

Donc je peux dire quatre, je vais dire let neighbor de ce tableau.

Et pour ce voisin, je veux les ajouter à l'arrière de ma file d'attente.

Donc pour moi, ce serait simplement q dot push, je vais ajouter ce voisin.

Super.

Donc je retire de l'avant, et j'ajoute à l'arrière.

Donc cela semble assez bien.

Allons-y et donnons-lui un essai.

Et en fait, avant de faire cela, je vais changer l'ordre de cela, mettre CNB.

Cela n'a vraiment pas d'importance l'ordre relatif des voisins, je veux simplement cette sortie exacte, et nous parlerons de pourquoi c'est le cas.

Donnez-lui un essai.

Donc je reçois ACB EDF comme je m'y attendais ACB EDF, n'est-ce pas.

Donc disons que vous êtes à la première itération de cette impression en largeur, je sais que je viens de retirer A parce que j'ai initialisé A sur la file d'attente, n'est-ce pas ? Donc mon courant est A et j'imprime A et à partir de là, je commence à itérer à travers ce tableau, n'est-ce pas.

Donc à la première itération, j'ai C, cela signifie que je mets C dans ma file d'attente, n'est-ce pas ? Et ensuite, je mets B, si vous mettez C puis B, cela signifie que C est au front de la file d'attente, c'est pourquoi à la deuxième itération, j'ai C en premier, n'est-ce pas ? C'est ainsi que vous pouvez manipuler potentiellement l'ordre latéral d'une impression en largeur.

Super.

C'est tout ce qu'il y a à cet algorithme de parcours, ce que je veux vraiment souligner, surtout si vous regardez le code itératif pomme à pomme, vous comparez la profondeur ou la largeur en premier, c'est presque un code identique.

Vous changez vraiment juste la façon dont vous accédez aux éléments dans votre tableau, n'est-ce pas ? Vous poppez ou poussez ou vous déplacez et poussez plus fort que cela, toute la structure de ce code est identique, n'est-ce pas ? D'accord.

Donc voici notre introduction sur la profondeur et la largeur pour nos graphes.

Dans la section suivante, nous allons commencer à résoudre un problème, n'est-ce pas, ce qui sera vraiment amusant.

Je vais simplement utiliser ce code comme notre outil de base.

Et cette section a également promis que nous allons commencer à faire l'analyse pour bego de ces algorithmes.

Donc sautons à ce tableau blanc.

Hey, programmeurs, bienvenue, et passons en revue l'approche pour ce problème de chemin.

Donc dans ce problème, nous allons prendre une liste d'adjacence représentant un graphe pour ce problème, et vraiment tous les problèmes de graphes, vous voulez définitivement visualiser celui-ci avec une image.

Et donc ce que nous allons faire, c'est interpréter chaque clé de cette liste d'adjacence comme représentant un nœud distinct.

Et si je regarde n'importe quelle liste particulière, je peux voir que ce nœud F devrait pointer vers G et I.

Et ils nous disent dans ce problème que j'ai un graphe dirigé.

Donc je vais dessiner des flèches sur ces arêtes ici.

Donc F pointe vers G, ainsi que F pointe vers I.

Et je vais créer des arêtes similaires basées sur les informations dans le graphe donné.

Donc nous obtenons une image comme celle-ci, jusqu'à ce qu'ils nous disent que c'est un graphe dirigé, ce qui explique les flèches, mais ils nous disent aussi que ce graphe est acyclique.

Donc si vous n'êtes pas familier, acyclique signifie simplement pas de cycles, ce qui pose la question, qu'est-ce qu'un cycle dans un graphe.

Donc un cycle serait un chemin à travers les nœuds, où je peux finir là où j'ai commencé.

En d'autres termes, si je commençais au nœud A ici, je pourrais aller à B, puis de là, je pourrais aller à C, puis revenir à A, et ainsi de suite.

Donc si je faisais un parcours, sur le graphe Sigma, j'obtiendrais une boucle infinie.

Et ce qu'ils disent, c'est que notre entrée de graphe est garantie d'être dirigée.

Donc elle a des flèches, mais aussi acyclique, donc nous n'avons pas à considérer de cycles infinis ici.

Cela dit, dans ce problème, nous voulons également prendre non seulement les informations du graphe, mais aussi un nœud source et de destination, nous voulons faire est de retourner vrai ou faux indiquant si nous pouvons voyager du nœud source au nœud de destination.

En d'autres termes, existe-t-il un chemin entre ces deux nœuds ? Pour ce problème, vous pouvez utiliser soit une recherche en profondeur soit en largeur pour résoudre le problème ici, je vais tracer dans cette vidéo d'approche, juste la recherche en profondeur.

Mais dans le walkthrough, je vais m'assurer de le coder des deux manières.

Donc disons que j'ai commencé à mon nœud source, je sais que si je faisais un parcours en profondeur, je peux choisir soit le IRG, disons que j'ai choisi G ensuite.

Maintenant je n'ai pas le choix, n'est-ce pas ? Si je fais vraiment un parcours en profondeur, je devrais aller plus profondément vers le H.

Donc je frappe ce H.

Et au fur et à mesure que je traverse ces différents nœuds, je dois me demander si mon nœud actuel est égal à ma destination.

Jusqu'à présent, cela n'a pas été vrai.

À ce stade, j'ai atteint le fond avec mon nœud H, je ne peux pas voyager plus profondément.

Donc maintenant je peux me déplacer latéralement vers un nœud comme I, à ce stade depuis I je peux soit me déplacer vers un K ou un G, disons par chance, je me suis retrouvé à G, cela me mènerait en fait sur un chemin que j'ai exploré précédemment, que nous pouvons optimiser plus tard, mais ce ne serait pas trop grave.

Éventuellement, si je continuais cette recherche en profondeur à travers le graphe, je finirais par un nœud qui correspond à ma destination, auquel point je peux retourner vrai signifiant qu'il doit y avoir un chemin de F à K, en faisant simplement une recherche en profondeur.

Et au fur et à mesure que nous faisons cette recherche en profondeur, il est vraiment important que vous obéissiez aux directions de vos flèches.

Donc je ne devrais jamais essayer de voyager en amont.

C'était un scénario où nous avons pu trouver un chemin de la source à la destination.

C'est pourquoi nous retournons vrai.

Réinitialisons et disons que maintenant, je devrais retourner faux.

D'accord, donc disons que ma source était J.

Donc je commence à J.

Et j'essaie d'atteindre ma destination F.

Si je commence un parcours en profondeur ici, désolé, mon nœud J a voyagé vers le nœud AI.

À ce stade, je peux frapper soit le G, d'accord, disons que je me retrouve à K, ce point de fond maintenant.

Donc maintenant je peux me déplacer vers le G.

Et de là vers le H.

Et à ce stade, il n'y a en fait nulle part ailleurs où je puisse aller, n'est-ce pas.

Donc si je termine mon parcours à travers le graphe, en utilisant soit un parcours en profondeur ou en largeur et que je n'atteins jamais ma destination, alors je peux simplement retourner faux, n'est-ce pas ? Il doit être le cas qu'il n'y a pas de tel chemin de ma source à ma destination.

Lorsque cela vient à implémenter les parcours en profondeur et en largeur sur ce graphe, cela va être exactement ce à quoi nous sommes habitués, vous pouvez soit utiliser une pile et le résoudre de manière récursive.

Ou vous pouvez le faire de manière itérative.

Et utiliser une file d'attente dans laquelle vous feriez le parcours en largeur.

Nous avons parlé de la complexité de cela, disons que n est le nombre de nœuds de notre graphe, une chose courante que vous pouvez aussi faire avec ces problèmes de graphes est de définir e comme le nombre d'arêtes ici et les arêtes se réfèrent à une connexion entre deux nœuds, essentiellement juste les flèches.

Donc si nous utilisons ces deux termes de nombre de nœuds et nombre d'arêtes, nous aurions une complexité temporelle de notre V o du nombre d'arêtes car nous devrions parcourir chaque arête de notre graphe.

Ici, la complexité spatiale serait basée sur le nombre de nœuds, n'est-ce pas ? Si je l'ai résolu, de manière récursive, ou même de manière itérative, avec une sorte de pile de profondeur d'abord, alors dans le pire des cas, je devrais avoir chaque nœud sur la pile, n'est-ce pas ? De même, si je voyais l'éternité avec une largeur d'abord, j'aurais chaque nœud sur la file d'attente.

Donc c'est juste une façon dont nous pouvons définir les termes pour analyser le temps et l'espace de ce graphe.

Typiquement, pour les problèmes de graphes, une autre façon acceptable d'analyser le temps et l'espace de votre algorithme est de simplement utiliser une seule variable et de définir n comme le nombre de nœuds.

C'est parce que si vous dites que n est le nombre de nœuds, alors nous pouvons aussi dire que n au carré serait le nombre d'arêtes, ou que big O.

C'est le pire cas.

Donc imaginons le pire cas de graphe.

Disons que je n'avais que ces nœuds ABC.

Eh bien, si je voulais créer autant d'arêtes que possible, comment ferais-je pour créer une seule arête ? Eh bien, une arête est juste une connexion entre deux nœuds.

Donc vous pourriez simplement dessiner une arête pour chaque paire de nœuds dans votre graphe, quelque chose comme ceci.

Et c'est pourquoi nous pouvons dire que n au carré est le nombre d'arêtes de n'importe quel graphe particulier.

Et donc si vous vouliez simplement utiliser n pour définir la complexité ici, alors vous pourriez dire que votre temps va être O de n au carré, et votre complexité spatiale serait encore O de n.

Sachez que ce sont deux façons valides de définir la complexité pour des problèmes de graphes très typiques.

Cela dit, je pense que c'est assez simple.

Sautons dans la vidéo de walkthrough où nous allons réellement implémenter à la fois une solution en profondeur et en largeur pour ceux-ci.

Je vous verrai là.

Hey, programmeurs, Alvin ici, maintenant.

Passons en revue une solution JavaScript pour ce problème de chemin.

Et donc nous allons plonger directement, nous allons commencer par résoudre celui-ci en utilisant un parcours en profondeur, ce qui, je le sais, nécessite une structure de données de pile sous-jacente, je vais simplement l'implémenter en utilisant la récursion.

Donc je peux exploiter la pile d'appels pour obtenir mon ordonnancement.

Et donc je vais résoudre cela de manière récursive, je vais considérer mon argument source comme ma position actuelle pendant le parcours.

Et donc je peux avoir un cas de base à vérifier.

D'accord, si ma source est égale à ma destination, alors je dois avoir trouvé ce que je cherche.

Donc retourne simplement vrai.

Ce cas de base signifie que j'ai trouvé ma destination.

Donc il doit exister un chemin.

Et donc je retourne vrai, en faisant toujours attention au type qu'ils veulent que nous retournions pour cette fonction.

Disons que ce n'est pas vrai, eh bien, ils doivent continuer à chercher.

Donc ce que je devrais faire est de considérer mon nœud actuel, qui est la source, considérer ses voisins.

Si je clique dans ma liste d'adjacence, je sais que cela va être un objet.

Donc je clique dedans en utilisant ma source, cela me donnerait un tableau de tous ses voisins.

Par exemple, disons que c'était en regardant celui-ci, si ma source actuelle était F, et que je dis graph square bracket, F, je recevrais un tableau de gi.

Donc maintenant je veux regarder à travers les voisins, n'est-ce pas ? Donc je peux voir ici qu'il nous a transformés en une boucle et dire pour ce voisin de ces voisins, je veux les parcourir, ce qui signifie que je les appelle de manière récursive.

N'est-ce pas, appelez has path, gardez votre graphique le même, mais mettez à jour votre position actuelle.

Maintenant, je vais me situer au voisin.

Et la destination reste la même, n'est-ce pas, toujours le même objectif d'atteindre la résolution de celui-ci de manière récursive.

Donc réfléchissez à ce que ce type va retourner, je sais qu'il va donner un booléen, n'est-ce pas, il va me dire s'il y a un chemin entre mon voisin et la destination, n'est-ce pas.

Donc s'il y a un point de connexion, ou un chemin de connexion entre mon voisin et la destination, alors je sais qu'il doit y avoir un chemin de ma source à la destination, car votre source est définitivement à côté de votre voisin, n'est-ce pas.

Donc il y aurait un chemin entre nous tous.

Et donc ce que je vais faire, c'est vérifier si cet appel récursif retourne vrai, je vais l'expliciter ici, peut-être que c'est clair.

Et donc s'il y a un chemin à travers mon voisin vers la destination, alors je peux retourner vrai, juste passer ce vrai vers le haut.

Parce qu'une fois que j'ai trouvé un chemin, vous pouvez simplement sortir et retourner cette chaussure tout le chemin jusqu'à l'appel de couleur de haut niveau.

Mais disons que cet appel a retourné faux, cela signifie qu'il n'y a pas de chemin à travers mon voisin vers la destination.

Mais il ne pourrait pas être le cas qu'un autre voisin fonctionne en fait.

Et donc ce que je ne veux pas faire, c'est simplement dire comme sinon retourner faux, vous devriez pouvoir immédiatement repérer un code comme celui-ci comme suspect parce qu'il n'y a pas de point d'avoir une boucle for alors, n'est-ce pas ? Si dans les deux cas, vous allez toujours retourner, alors vous n'allez jamais avoir une deuxième itération de cette boucle for, n'est-ce pas ? Donc si je ne trouve pas de chemin à travers mon voisin, donc si cet appel retourne faux, alors ce n'est pas grave.

Continuez simplement à l'itération suivante, et recherchez à travers votre autre voisin.

Cela pose la question, où devrions-nous retourner faux, il faut que ce soit après la boucle for ? Donc seulement après avoir recherché tous mes voisins, et n'avoir jamais trouvé un chemin gagnant ? Devrais-je retourner faux, et ce serait notre belle traversée en profondeur.

Donnons-lui un essai.

Super.

Nous y voilà.

Une chose à garder à l'esprit ici, nous tirons parti des hypothèses du problème, n'est-ce pas, ils nous disent directement que le graphe qui va être donné est un graphe acyclique, donc il n'y a pas de cycles.

C'est pourquoi dans notre code, nous ne nous sommes pas vraiment inquiétés de nous retrouver dans une boucle infinie.

Dans nos problèmes à venir, nous aurons des graphes plus difficiles pour traiter ce cas acyclique.

Mais pour l'instant, c'est une bonne solution de base.

Pendant que nous sommes ici, faisons aussi une solution de référence, qui, comme vous le savez maintenant, devrait être itérée, n'est-ce pas, il n'y a pas moyen de faire comme une largeur d'abord de manière récursive.

Et donc j'ai besoin de créer ma propre file d'attente.

Donc je peux créer une file d'attente, un peu à la hâte, je vais toujours utiliser un tableau en JavaScript, je vais initialiser cette file d'attente avec ma source dessus.

Donc je vais me référer à la source et à la destination, ils sont vraiment des nœuds.

Mais dans le contexte de notre problème, ils nous sont vraiment donnés comme des chaînes, mais ils représentent des nœuds, n'est-ce pas ? Donc réfléchissez à l'information qu'ils représentent.

Je vais itérer tant que ma file d'attente n'est pas vide.

Donc tant que q dot length est supérieur à zéro, cela devrait être un code familier, très similaire à nos algorithmes d'arbres.

Et je commence une seule itération de référence en retirant le front de ma file d'attente.

Donc je peux dire q dot shift une partie du front, je peux l'appeler mon nœud actuel que je traverse.

Et maintenant qu'une chose a quitté la file d'attente, typiquement ici c'est où je vérifie, je peux vérifier.

D'accord, si la chose que je viens de visiter, si c'est ma destination, alors je peux simplement retourner vrai, n'est-ce pas, j'ai trouvé la chose que je cherche.

Donc il doit y avoir un chemin qui relie ma source originale et ma destination.

Bien.

Mais disons que ce n'était pas vrai.

Eh bien, alors je dois considérer ses voisins.

Donc comme avant, regardez les voisins, il suffit de cliquer dans votre graphe en utilisant la source comme si c'était un graphe, un crochet source.

Cela me donne un tableau de tous les nœuds voisins.

C'est ce que je veux faire ici, c'est itérer à travers chaque voisin là-bas.

Et puis je peux simplement les ajouter dans ma file d'attente.

Donc q dot push ce voisin unique, et soyez sûr d'implémenter votre vrai largeur d'abord.

Donc vous devez faire en sorte que les choses quittent une extrémité de votre file d'attente, et vous ajoutez à l'autre extrémité.

Donc ce code a l'air bien.

Donc vous devriez réaliser à quel point cela est similaire à notre ancien parcours en largeur d'un arbre binaire, sauf que maintenant nous devons tenir compte du fait que nous pourrions avoir une quantité dynamique de voisins ici, pas juste dot left et dot right.

Donc je parcours simplement tous ces voisins en les ajoutant, je dois attendre pour retourner faux.

Et vous l'avez deviné, le mouvement est après avoir terminé cette boucle while entière, si votre cube devient vide, alors vous devez avoir exploré aussi loin que vous le pouviez.

Et si vous ne retournez jamais vrai, et maintenant vous pouvez retourner faux, parce qu'il doit être le cas qu'il n'y a pas de chemin entre la source originale et votre cible.

Donc donnons un essai à cela.

Et je reçois une petite erreur.

Voyons ce que nous avons fait de mal ici.

Donc il semble que j'ai dépassé le temps ici.

Voyons ce bug ensemble, j'ai dû deviner que cela signifie que j'ai fait quelque chose de mal en me retrouvant dans une boucle infinie.

Cette condition semble correcte, n'est-ce pas, q dot length supérieur à zéro.

Et donc ici, il doit être le cas que je ne parcoure pas correctement les voisins ici, j'ai juste écrit source.

Au lieu de cela, je dois dire current, parce que maintenant je fais cela de manière itérative, n'est-ce pas.

Donc quel que soit le nœud qui vient de quitter ma file d'attente, je considère les voisins de ce nœud et je les ajoute à visiter ensuite à travers ma file d'attente.

Donc donnons un essai à cela.

Erreur honnête là.

Cool.

Et voici notre solution en largeur d'abord pour ce problème de chemin.

Donc ce que je veux que vous fassiez, c'est pratiquer à la fois le parcours en profondeur et en largeur, comme vous vous y attendez, nous allons faire beaucoup de problèmes de graphes à venir.

Et selon ce que le problème demande parfois, nous préférerons un type d'algorithme à l'autre.

Donc il est vraiment important que vous pratiquiez ces deux algorithmes.

Maintenant, tous les problèmes sont relativement faciles.

Donc pratiquez cela, essayez par vous-même.

Et je vous retrouverai dans le prochain problème.

À bientôt.

Hey, programmeurs, Alvin ici, maintenant.

Passons en revue l'approche pour ce problème de chemin non orienté.

Donc nous allons plonger directement.

Dans ce problème, nous allons recevoir une liste d'arêtes pour un graphe non orienté.

Donc si vous êtes familier avec la terminologie ici, ce que nous disons vraiment, c'est que chaque paire dans cette liste d'arêtes représente une connexion entre deux nœuds.

Par exemple, si je regarde la première arête de la liste, je vois i virgule j, cela signifie qu'il y a une arête ou une connexion entre i et j.

Et puisque c'est un graphe non orienté, non seulement je peux voyager directement de i à j, mais je peux bien sûr me déplacer de j à i.

Donc cela représente vraiment une connexion dans les deux directions.

Et donc, au fur et à mesure que nous commençons à attaquer ce problème, nous allons vouloir convertir cette liste d'arêtes en un format plus favorable, comme une liste d'adjacence.

C'est parce que typiquement, lorsque nous effectuons nos algorithmes de parcours, ils fonctionnent mieux sur une forme de liste d'adjacence.

Donc commençons par faire cette conversion ici.

Et ce sera en fait assez facile à coder.

Donc je veux essentiellement générer un graphe où j'ai des nœuds comme clés, je veux qu'ils pointent vers un tableau de leurs voisins.

Par exemple, si je voulais convertir la première arête en une forme de liste d'adjacence, ce que je peux faire est créer des clés pour i et j.

Maintenant que I est un voisin de J, et aussi j est un voisin de I, donc je vais remplir ces voisins respectivement.

Maintenant, suivez simplement ce processus pour une autre arête.

Donc si je regarde l'arête, k virgule i, je dois créer une nouvelle clé pour K.

Et je vais la remplir avec I et puis pour la clé existante de I, je vais simplement ajouter k dans cette collection.

Donc gardez à l'esprit, la chose la plus importante à propos de cette conversion est que parce que nous savons que le graphe va être non orienté, chaque fois que vous mettez une connexion dans votre graphe, assurez-vous que vous avez la connexion inverse.

Donc si j'ai une arête de k à AI, ils ont aussi besoin d'avoir des informations pour elle.

D'accord.

Et ce processus continuerait pour toute la liste des arêtes.

Et à la fin de cette conversion, nous allons finir avec une liste d'adjacence comme celle-ci.

Et maintenant nous sommes prêts à effectuer notre algorithme principal.

Lorsque nous passerons par le code de walkthrough pour cela, je vous montrerai en profondeur comment vous pouvez réellement créer cette liste d'adjacence.

Et donc lorsque nous voulons réellement trouver un algorithme de parcours pour résoudre un problème de graphe, cela aide vraiment si vous visualisez réellement la forme de votre graphe.

Donc je veux réellement visualiser cela en termes de nœuds et d'arêtes.

Cela signifie un tas de cercles et de lignes entre eux.

Si vous avez dessiné une belle image pour cette information de graphe, vous finirez avec un diagramme comme celui-ci.

Et donc nous allons passer le reste de cette vidéo d'approche en nous référant simplement à ce diagramme.

Une chose importante que je veux souligner à ce stade est que pour ce graphe, un cas très courant que nous allons devoir gérer est le suivant : que se passe-t-il si votre graphe contient un cycle.

Et c'est particulièrement vrai pour vos graphes non orientés.

Et donc juste pour les besoins de cette vidéo d'approche, je vais ajouter une arête supplémentaire afin que nous puissions parler d'un cycle explicite.

Donc je vais ajouter une nouvelle arête de k à J.

Cool.

La raison est qu'il y a maintenant un joli grand cycle de longueur trois en surbrillance en rouge.

Et ce cycle est important à surveiller car si nous ne faisons aucun traitement spécial, nous pourrions nous retrouver dans une traversée infinie.

Donc imaginez que je commence à ce nœud clé, et ensuite je me déplace vers J, puis je me déplacerais vers i, puis je reviendrais à k, puis je reviendrais à J, puis à i, et ainsi de suite.

Donc maintenant cela me donne un cycle, nous devrons nous en protéger.

Et donc je peux avoir un cycle de trois nœuds ici, n'est-ce pas, et vous pouvez vraiment avoir un cycle de presque n'importe quelle taille, tant qu'il est supérieur à un.

Par exemple, si je jetais un coup d'œil ici, remarquez que mon graphe contient en fait techniquement comme deux îles séparées, mais nous les considérerions comme juste un géant graphe, n'est-ce pas ? Donc j'ai la petite île de O et N, ils forment en fait un cycle trivial, n'est-ce pas ? Si je commençais un parcours, à o.

De là, je peux me déplacer vers n.

Et parce que je sais que l'arête entre o et n est bidirectionnelle, c'est un graphe non orienté, cela signifie que je peux revenir à O, puis revenir à n.

Et cela me donnerait un comportement cyclique.

Donc il faut se méfier de tous les types de cycles dans ce problème.

Dans le contexte de ce problème, non seulement on nous donne un graphe, mais on nous donne aussi deux nœuds.

Donc passons en revue un exemple où je veux retourner vrai ou faux, y a-t-il un chemin entre I et L.

Donc je vais les marquer dans mon graphe Israël.

Donc je vais commencer au nœud.

Et pour résoudre celui-ci, vous pouvez utiliser n'importe quel type de parcours.

Donc soit en profondeur d'abord soit en largeur d'abord, je vais passer explicitement par le parcours en profondeur d'abord.

Bien.

Maintenant, afin d'éviter tout parcours infini, je veux marquer mes nœuds comme visités au fur et à mesure que je les traverse.

Donc non seulement je me situe à ce nœud source de I, mais je vais le marquer comme visité.

Et vous pouvez implémenter ce motif de marquage visité de quelques manières différentes.

Lorsque nous coderons cela plus tard, nous allons probablement utiliser un ensemble pour représenter ce que nous avons visité.

Mais pour l'instant, je vais simplement les cocher dans mon diagramme.

Et donc dans mon diagramme, si vous voyez une coche à côté d'un nœud, cela signifie que je l'ai déjà visité.

Donc puisque je suis à ce nœud de I, je veux me déplacer vers ses voisins, donc je vais me déplacer vers le voisin de J.

Et je vais également m'assurer de le cocher comme visité.

À ce stade, je peux me déplacer vers l'un des voisins de J, disons que je me déplace vers k.

Et je vais également le marquer comme visité.

Maintenant, à k, je peux me déplacer vers quelques voisins différents, je pourrais soit me déplacer vers I, LRM.

Disons par hasard que j'ai choisi I, une fois que j'arrive à cela, je sais que je vais pouvoir voir immédiatement que, oh, j'ai visité ce nœud précédemment.

Donc ce que je devrais faire, c'est ne pas le traverser à nouveau.

Au lieu de cela, je devrais revenir à K, n'est-ce pas, parce que ce nœud I est déjà visité.

Et c'est là que j'évite en fait la boucle infinie.

Donc au lieu de cela, je me suis déplacé vers certains des autres voisins de K, disons que j'ai choisi L.

À ce stade, je le marquerais comme visité.

Si je fais une vérification rapide, je peux voir que ce nœud où je suis à L est également mon nœud de destination.

Donc je dois avoir trouvé un chemin entre ma source et la destination.

Donc à ce stade, si je trouve ma destination, je peux simplement retourner vrai, ce qui était un motif dont nous avons parlé dans un problème précédent, le seul critère supplémentaire dont nous avons besoin est de marquer les nœuds comme visités.

De cette façon, nous ne nous retrouvons pas dans une boucle infinie.

Et cela ne sera nécessaire que si nous avons des cycles dans notre graphe, ce qui, s'ils ne nous donnent aucune hypothèse, nous devons toujours nous en protéger.

Donc regardons un autre exemple.

Disons que j'avais une source de K.

Et ma destination était Oh, en regardant visuellement dans le graphe, vous pouvez déjà voir qu'il n'y a aucun moyen d'aller de k à O, car ils sont déconnectés, n'est-ce pas, ils sont sur des îles séparées, les deux passent par l'algorithme, peu importe, donc je vais commencer à K, je vais le marquer comme visité, je vais visiter certains des voisins de K.

Donc je peux me déplacer vers i, puis je peux me déplacer vers J.

Et à ce stade, je me déplacerais vers K et je m'assurerais vraiment qu'ils n'explorent aucun des voisins visités de K, donc je ne me déplace pas vers I, n'est-ce pas, au lieu de cela, je devrais me déplacer vers un voisin non visité, comme l, le marquer comme visité, puis je n'ai qu'un autre nœud à visiter, qui serait ce nœud m.

Et à ce stade, j'ai en fait épuisé cette région complète du graphe, n'est-ce pas, il n'y a nulle part ailleurs où je puisse aller.

Et une fois que j'ai terminé mon parcours, si je n'ai jamais trouvé mon nœud de destination, alors je peux simplement retourner faux, n'est-ce pas ? Il doit être le cas qu'il n'y a pas de chemin qui existe de mon nœud source à mon nœud de destination.

C'est vraiment tout ce qu'il y a à cet algorithme.

Parlons de la complexité.

Si nous disons que n est un nombre de nœuds, définissons également que e est un nombre d'arêtes.

Comme nous l'avons dit précédemment, c'est quelque chose de typiquement acceptable à faire pour nos problèmes de graphes.

Je sais que la complexité temporelle va être approximativement celle du nombre d'arêtes.

Et ma complexité spatiale va être O de n, c'est-à-dire le nombre de nœuds.

Je pense qu'il vaut la peine de passer en revue, vous savez, ce que cette complexité signifie vraiment, vous savez, big O se réfère au pire cas.

Donc réfléchissons à un graphe de pire cas que nous pouvons avoir.

Et il y a quelques graphes différents que vous pouvez concevoir et penser, je vais vous en montrer un exemple.

Donc disons que j'avais un graphe comme celui-ci, n'est-ce pas ? Remarquez que bien que z soit un peu sur sa propre île, tous ces nœuds, c'est-à-dire les trois ainsi qu'un nœud C.

Ils sont tous membres du même graphe.

Donc disons que je voulais savoir s'il y a un chemin entre A et z.

Donc si je faisais mon algorithme de parcours d'ici, je commencerais à a puis je me déplacerais vers B, puis vers C, puis vers D, puis vers E.

À ce stade, j'ai couvert toutes les arêtes du graphe.

Rappelez-vous que les arêtes sont les flèches ici, parce que je dois traverser chaque arête de ce graphe.

C'est pourquoi nous avons dit que la complexité temporelle dans le pire des cas va être o de E, n'est-ce pas, o du nombre d'arêtes.

et ici nous pouvons dire que la complexité spatiale est O de n.

Parce que si vous faites cela avec soit une pile de profondeur d'abord, soit une file d'attente de largeur d'abord, dans le pire des cas, vous devriez ajouter tout ce que vous avez visité, c'est-à-dire tous les nœuds sur votre pile ou file d'attente.

C'est pourquoi nous disons pour les algorithmes de parcours de graphe réguliers, nous avons une complexité temporelle de o v, et une complexité spatiale de O de n.

D'accord, je pense que nous avons l'approche pour cet algorithme bien en main.

À ce stade, je veux me joindre à vous dans les vidéos de walkthrough, où nous pouvons réellement voir comment implémenter ces motifs visités dans du code.

Je vous verrai là.

Hey, programmeurs, Alan ici, maintenant.

Passons en revue une solution JavaScript pour ce problème de chemin non orienté.

Donc nous allons plonger directement, comme nous l'avons dit, dans la vidéo d'approche, il y aura une partie en deux.

Tout d'abord, nous allons convertir notre liste d'arêtes en une liste d'adjacence.

De cette façon, il est plus facile de faire un parcours classique à travers elle.

Donc je vais faire semblant d'avoir une fonction d'aide ici.

Qui me donne une liste d'adjacence.

Je l'appellerai graph.

Et je vais appeler cette fonction d'aide, nous allons dire build graph.

Et si je lui passe, juste toutes mes arêtes, je veux qu'elle fasse cette conversion pour moi.

Donc travaillons sur cette fonction d'aide maintenant.

Et puis nous sauterons à undirected path.

Donc je vais créer ma fonction build graph, je vais simplement prendre les arêtes, n'est-ce pas.

Et je sais que je veux que ma liste d'adjacence soit sous la forme d'un bon vieux objet JavaScript.

Donc créez cet objet graph ici.

Et je vais le retourner par la fin comme ceci.

Et ce que je veux faire est de remplir ce graph avec des informations provenant des arêtes.

Donc je vais itérer à travers chaque arête.

Donc pour chaque arête des arêtes, en itérant, à travers chaque arête unique, je sais qu'une seule arête serait une paire.

Donc je vais simplement déstructurer cela, peut-être juste mes deux identifiants de nœud, nous les appellerons a et b, de l'arête.

Bien.

Ce que je veux faire est maintenant initialiser ces nœuds comme clés de cet objet graph.

Donc a serait quelque chose comme ceci, je note ou ce nœud k, n'est-ce pas.

Donc ce que je vais faire est vérifier si A est dans mon graph, je pense que cela nettoie vraiment ce code, mieux si je vérifie s'il n'est pas dans le graph.

Donc si le nœud a n'est pas dans le graph, alors ce que je peux faire est de l'initialiser dans le graph.

Donc utilisez-le comme une clé et assigner-le à un tableau vide.

Et je vais faire de même pour B ici.

Bien, donc j'initialise A et B dans le graph s'ils n'existent pas, et une fois que je l'ai fait, alors je peux simplement ajouter des voisins dans leurs arêtes, n'est-ce pas ? Donc je peux dire, le graph square bracket a dot push B.

Donc maintenant je dis que, n'est-ce pas, B devrait être un voisin de a, mais je sais que ce graphe est non orienté, n'est-ce pas ? Donc cela devrait être symétrique.

En d'autres termes, assurez-vous de pousser a dans les voisins de B.

Donc il est vraiment important que vous remarquiez que ce graphe est non orienté.

Donc votre liste d'adjacence doit être symétrique de cette manière.

Donc si a est dans les voisins de B, B devrait aussi être dans les voisins de A.

Donc cela semble assez bien.

Allons-y et voyons à quoi ressemble ce graphe avec une petite vérification ici.

Donc je dois voler peut-être ce snippet, obtenir ce snippet complet ici, je pourrais simplement l'exécuter manuellement, j'adorerais m'assurer que je peux tester ces petites fonctions d'aide avant de les utiliser.

Donc nous allons lui donner un essai, nous devrions simplement voir la forme de liste d'adjacence de ces arêtes ici.

Voir à quoi cela ressemble.

Donc cela semble assez bien.

Donc je vois que d'accord, I est connecté à J et K.

N'est-ce pas ? Et cela semble correct basé sur ces arêtes.

Super.

Et je veux aussi m'assurer que c'est symétrique, n'est-ce pas.

Donc si i et j sont ici, alors je devrais avoir JNI ici aussi, n'est-ce pas, cela devrait être une rue à double sens.

D'accord, maintenant travaillons dans notre vrai algorithme ici, qui serait une sorte de parcours.

Maintenant que vous avez une belle liste d'adjacence, vous pouvez faire soit un parcours en largeur soit en profondeur.

Je vais implémenter, je pense, un parcours en profondeur.

Typiquement pour moi, c'est juste plus facile de pousser si je le fais de manière récursive.

Et donc je vais faire semblant d'avoir une fonction appelée has path, elle va prendre les informations de mon graphe.

Ainsi qu'un nœud de départ et un nœud de fin.

Donc je veux trouver un chemin du nœud A au nœud B, bien sûr, je vais supposer que cette fonction retourne un booléen.

Mais bien sûr, je dois écrire cette fonction moi-même.

Donc restons organisés dans notre code, nous allons dire has path.

Je vais prendre le graphe ainsi que le nœud A et le nœud B.

Et je pense qu'un meilleur nom pour ces arguments pendant que je fais cela de manière récursive.

Appelons celui-ci source et celui-ci destination.

Donc avec le temps, nous allons appeler de manière récursive et mettre à jour ce nœud source.

Et cela devrait être un motif familier pour certains autres problèmes résolus.

Récemment.

Donc réfléchissez à mon cas de base.

D'accord, je sais que j'ai trouvé un chemin avec succès lorsque ma source est égale à mon nœud de destination, si c'est le cas, je retourne vrai, parce que je viens de trouver un chemin.

Sinon, je dois continuer à chercher.

Donc je devrais pouvoir regarder à travers les voisins de mon nœud source.

Donc je pourrais dire graph square brackets source, n'est-ce pas ? Rappelez-vous qu'à tout moment à travers cette récursion, la source représente ma position actuelle.

Si je dis graph, square bracket source, disons que la source était I, j'accéderais à tous les voisins de I, n'est-ce pas ? Donc ce que je veux faire, c'est vraiment itérer pour laisser le voisin et, ou plutôt avoir le graphique de la source.

Donc si les sources sont I à la première itération, le voisin serait j, à la deuxième itération, le voisin pourrait être K.

Et pour chacun de mes voisins, je veux voyager vers eux.

Donc appelez has path, vous pouvez garder votre argument graphique le même, il faut changer votre source, vous êtes maintenant situé au voisin, et votre destination est fixe, vous essayez toujours d'atteindre le même nœud exact.

Je vais réfléchir au type que cela va retourner, je sais que cela va donner un booléen, n'est-ce pas, vrai ou faux ? Y a-t-il un chemin de mon voisin à la destination, je vais vérifier.

D'accord, si cet appel retourne vrai, je vais être explicite ici, alors je viens de trouver un chemin.

Donc je retourne simplement ce vrai, n'est-ce pas, je le passe tout le chemin vers le haut.

Et le raisonnement que nous formons ici est, je sais que par définition, la source et le voisin sont définitivement connectés.

Donc il y a définitivement un chemin entre eux.

Ils sont connectés par une arête directe.

Donc si mon voisin a un chemin vers la destination, alors je sais, alors la source a aussi un chemin vers la destination.

Super.

Et donc après que cette boucle for ait fini de s'exécuter, disons que nous n'avons jamais trouvé que l'un de nos voisins fait un chemin gagnant, alors cela signifie que j'ai fini cette boucle for sans jamais retourner vrai, ce qui signifie que je peux retourner faux, n'est-ce pas, il doit être le cas que ce nœud source n'a pas de chemin vers la destination.

Donc je pense que nous pouvons aller de l'avant et donner un essai à ce code.

Si vous avez regardé la vidéo d'approche, vous avez remarqué qu'il y a quelque chose d'important qui manque dans ce code.

Mais nous allons simplement l'exécuter et vous montrer comment pêcher ici.

Donc ici, j'obtiens une erreur, les arêtes ne sont pas définies, ce que j'ai horriblement mal fait, il y a 34 lignes, il y a 34 lignes ici.

Donc il faut enlever cet appel, je n'en ai plus besoin.

C'est de ma faute.

Donnons un essai à ce test.

Donc ce n'était pas l'erreur à laquelle je m'attendais.

Je m'attendais à une sorte de boucle infinie, cependant.

Parfait, j'obtiens une taille de pile d'appels maximale dépassée.

Donc j'ai comme une récursion infinie.

Et cela va se produire parce que nous n'avons pas tenu compte du cas où nous avons des cycles dans notre graphe, n'est-ce pas, nous devons éviter cela.

Parce que si j'ai un cycle dans mon graphe, je ne vais jamais atteindre l'un de ces cas de base, je vais simplement continuer à voyager en cercle.

Et si ce n'est pas clair, assurez-vous de regarder la vidéo d'approche, n'est-ce pas.

Et donc comme nous l'avons dit, le mouvement ici est d'ajouter une sorte de données qui montrent où vous êtes allé précédemment.

Typiquement, la façon dont nous faisons cela pour nos problèmes de graphes est de suivre un ensemble visité.

Donc lorsque je fais mon appel de haut niveau à cette maison de chemin, je sais que c'est la fonction réelle qui fait ce parcours, je vais passer un nouvel argument ici.

Et je vais en faire un nouvel ensemble JavaScript.

Donc si vous n'êtes pas familier avec les ensembles, et JavaScript, ils sont vraiment juste une collection d'éléments.

Et ce qui est vraiment génial avec un ensemble, c'est qu'en o d'un temps, je peux ajouter quelque chose dans l'ensemble.

Et je peux également vérifier quelque chose dans l'ensemble, ce qui va être très, très rapide pour notre parcours.

Je ne veux pas utiliser quelque chose de lent comme un tableau, car pour faire une recherche ou une vérification dans un tableau, cela prendrait en fait O de n temps, ou c'est pour un ensemble, c'est o de un.

Donc je vais créer un nouvel argument ici pour recevoir une colonne visitée.

Ce que je veux faire est de vérifier si mon nœud source est déjà dans l'ensemble visité pour faire cela en JavaScript, je peux vérifier visité out has.

Donc si le nœud source est à l'intérieur de l'ensemble visité, alors je pourrais retourner faux ici, n'est-ce pas, il n'y a aucune raison de traverser ce nœud plus longtemps.

Parce que s'il est visité, alors je dois l'avoir traversé précédemment.

Et c'est ainsi que je peux éviter une récursion infinie, je peux aussi déplacer cette ligne vers le bas si je le voulais.

Et disons que je passe cette instruction if.

Donc cela signifie que d'accord, ce nœud source n'a pas été visité.

Mais je le visite maintenant.

Donc je dois faire visit a dot add source.

Donc cette expression vérifie si la source est dans visited, et cette expression ajoute la source à l'ensemble visited.

Je veux changer quelques autres détails ici.

Assurez-vous de passer le même ensemble visited à travers tous vos appels récursifs ici.

Parce que vous voulez que cet ensemble visited soit comme global pour tout le parcours, n'est-ce pas, j'ai besoin de savoir exactement où je suis allé dans le passé.

Et une fois que nous avons cela en place, cela devrait être tout ce dont nous avons besoin pour empêcher tout cycle de nous donner une récursion infinie ici.

Donnons-lui un essai.

Super.

Et voici une solution pour notre problème de chemin non orienté.

Donc des choses importantes à retenir ici, considérons ce problème comme une partie en deux, n'est-ce pas ? La phase un est vraiment simple, il suffit de convertir une liste d'arêtes en une liste d'adjacence, ce qui est en fait une compétence importante à pratiquer.

Parce que lorsqu'il s'agit de, vous savez, certains problèmes que vous rencontrerez dans la nature, ils seront tous basés sur des problèmes de graphes.

Mais parfois, ils vous donneront le graphe dans un format différent, et vous pouvez toujours le convertir dans un format avec lequel vous êtes à l'aise.

Et à partir de là, nous avons un motif vraiment central de faire simplement un parcours à travers un graphe, mais aussi de nous protéger contre les boucles infinies, n'est-ce pas.

Et pour cela, nous utilisons simplement une sorte d'ensemble visité.

Hey, programmeurs, bienvenue, maintenant je veux passer en revue l'approche pour ce problème de compte des composants connectés.

Donc dans ce problème, ce que nous voulons faire est de prendre une liste d'adjacence représentant un graphe non orienté.

Comme toujours, avec n'importe quel problème de graphe, vous voulez commencer par visualiser le graphe réel.

Et donc si vous avez pris une photo de cette information, cela finirait par ressembler à un graphe avec cette structure.

La première chose que nous devrions remarquer à propos de ce graphe visuel est qu'il a plusieurs composants connectés.

Par exemple, je peux regarder ce composant en rose couvrant simplement les nœuds un et deux, je peux regarder un autre composant couvrant les nœuds quatre ou 5678.

Et enfin, un troisième composant couvrant simplement le nœud trois.

Et c'est pourquoi nous disons que votre résultat pour votre fonction ici devrait être trois, n'est-ce pas ? Parce qu'il y a trois composants connectés différents.

Donc trouvons un algorithme que nous pouvons utiliser pour compter les composants, nous savons qu'un algorithme de comptage général va utiliser une variable, et nous allons initialiser cette variable de comptage à zéro.

Et l'astuce ici est d'utiliser une combinaison à la fois d'un code de parcours de graphe standard, peut-être une profondeur d'abord ainsi que d'un code itératif.

Donc je vais faire le long du côté gauche est simplement lister tous mes différents nœuds.

Et ce que je vais faire est commencer par itérer, à travers chaque nœud de cette liste.

Et ce que je vais faire est, lorsque je suis actuellement à un nœud de cette liste itérative, je vais commencer un parcours à ce nœud.

Donc en commençant au nœud un, je commence, disons un parcours en profondeur, vous pouvez vraiment implémenter ce motif en utilisant soit une profondeur d'abord soit une largeur d'abord.

Donc disons que je commence au nœud un ici.

Ce que je devrais faire maintenant est de continuer ce parcours aussi loin que possible, c'est la clé de la victoire ici.

Donc à partir de ce nœud un, je peux me déplacer vers un voisin de deux.

Et bien sûr, au fur et à mesure que je traverse ces nœuds, je veux m'assurer que je les marque comme visités, afin que je puisse éviter les boucles.

Et marquer les choses comme visitées garantira également que nous ne comptons pas deux fois les composants ici.

Une fois que j'ai atteint ce nœud deux, j'ai en fait complété ce composant complet, il n'y a nulle part ailleurs où je puisse explorer.

Donc à ce stade, je devrais incrémenter mon compte de un.

Donc chaque fois que je termine un nouveau parcours sur une région du graphe, j'ai besoin d'incrémenter mon compte.

À ce stade, je retombe maintenant sur mon code itératif du côté gauche, et j'itère à travers le nœud suivant.

Donc je regarde maintenant le nœud numéro deux.

Si je regarde le nœud numéro deux, je vois qu'il est déjà marqué comme visité.

Donc cela signifie que je n'ai pas besoin de commencer un parcours à ce nœud.

Donc effectivement, je saute le deux et je garde le compte le même.

Prochaine itération, j'ai un trois, trois n'est pas visité maintenant.

Donc je devrais commencer un nouveau parcours en commençant à ce nœud trois, ce qui signifie que je le marque simplement comme visité.

Et puisque ce trois est un nœud singleton, n'est-ce pas, il n'est connecté à personne, je devrais en fait compléter leur parcours, juste sur le nœud trois.

À ce stade, j'ai complété un parcours.

Donc j'incrémente mon compte de un.

Donc maintenant j'ai un compte total de deux, je retombe sur mon code itératif.

Donc je suis passé du nœud trois au nœud quatre.

Et je vois que ce nœud quatre n'est pas visité, ce qui signifie encore que je dois commencer un parcours à partir de ce nœud quatre.

Et je vais développer ce parcours.

En commençant à quatre aussi loin que je peux, avant de revenir à mon code itératif, n'est-ce pas, donc je vais explorer le six, explorer ce cinq, explorer le sept, et enfin explorer ce huit.

À ce stade, j'ai complété un parcours.

Donc je peux incrémenter mon compte jusqu'à trois.

Et puis je dois continuer et retomber sur mon code itératif.

Donc regardez le nœud cinq, je vois que le nœud cinq est déjà marqué comme visité, donc je ne commence pas de parcours.

Et je vois que le nœud six, même chose, je n'ai pas besoin de commencer de parcours, le nœud sept est déjà visité, le nœud huit est déjà visité.

À ce stade, j'aurais terminé avec l'algorithme entier.

Et voici mon compte final de trois.

Donc quelques mécanismes intéressants ici, n'est-ce pas, vous allez devoir définitivement implémenter un code ou une fonction qui fait un parcours à travers un composant aussi loin que possible, puis vous avez également besoin d'un code itératif juste pour commencer potentiellement un parcours à chaque point de départ unique.

Et ce que vous voulez faire est de vous assurer de marquer les nœuds comme visités au fur et à mesure que vous les parcourez, car seulement lorsque vous avez marqué un nouveau nœud comme visité et complété ce parcours devriez-vous incrémenter votre compte.

Vous vous demandez probablement les détails exacts de la manière dont nous implémentons cela dans du code, mais ne vous inquiétez pas, vous réaliserez que ce n'est vraiment qu'une variation de nos algorithmes de graphes précédents dans la vidéo de walkthrough, mais pour l'instant, nous voyons que n est un nombre de nœuds et e est un nombre d'arêtes comme d'habitude, nous savons que cela consiste vraiment à parcourir tout le graphe.

Donc nous pouvons dire que la complexité temporelle est simplement o v, et la complexité spatiale est O de n, n'est-ce pas, selon que vous faites une largeur d'abord ou une profondeur d'abord, vous allez utiliser cet espace, puis en termes de votre pile ou de votre cube.

Et nous pouvons également considérer l'utilisation de l'espace dans notre ensemble si vous utilisez un ensemble pour marquer vos nœuds comme visités, mais dans l'ensemble, cela conduira toujours à une solution linéaire en temps et en espace.

D'accord, je pense que je suis prêt à coder celui-ci.

Je vous verrai dans la vidéo de walkthrough.

Hey, programmeurs, Alvin ici, maintenant passons en revue une solution JavaScript pour ce problème de compte des composants connectés.

Et donc nous allons implémenter exactement la stratégie dont nous avons parlé dans la vidéo d'approche.

Donc assurez-vous de la regarder en premier, nous savons que cela va nécessiter vraiment deux mécanismes différents, nous allons avoir besoin de notre code interactif pour sauter vers différents composants connectés.

Et nous avons également besoin d'un code de parcours pour explorer un seul composant aussi loin que possible.

Et donc ce que je vais faire ici, c'est de commencer par le code itératif.

Donc je dois commencer un parcours à chaque nœud potentiel.

Donc je peux dire pour chaque nœud de mon graphe, je vais dire dans mon graphe ici, parce que pour ce problème, nous avons donné l'air d'objets JavaScript.

Donc si je dis pour chaque nœud dans le graphe, cela me donnerait chacune de ces clés comme 015, et ainsi de suite.

Et donc pour chaque nœud du graphe, ce que je veux faire est de commencer un parcours.

Donc nous allons supposer que j'ai une fonction ici, je l'appellerai explore.

Je vais passer, bien sûr, le graphe, ainsi que ce nœud.

Et ce que je veux que cette fonction fasse est de faire comme un, nous allons dire, un parcours en profondeur, à partir de ce nœud aussi loin que possible, n'est-ce pas, donc probablement devoir ajouter plus de logique dans cette fonction principale.

Mais pour l'instant, je pense qu'il est temps de développer explore.

Donc je choisis de faire cette méthode explore de manière récursive.

Donc nous allons définir explore, cela va prendre un graphe, ainsi que mon nœud actuel, je vais simplement l'appeler current, n'est-ce pas.

Et puis à partir de là, je veux résoudre celui-ci, en utilisant une profondeur d'abord.

Donc la récursion est bien.

Et il n'y a pas grand-chose à faire ici, mais vraiment passer par mes voisins, je veux itérer à travers chaque voisin de ce nœud.

Donc je peux dire comme voisin de graphique de courant, je me souviens que graphique serait une liste d'adjacence.

Donc si le courant est étalé.

Donc si le courant était un nœud comme huit, alors à la première itération, le voisin serait zéro, à l'itération suivante, le voisin serait cinq.

Donc ici, je passe simplement par tous les voisins de mon nœud actuel, je dois simplement ne pas me déplacer vers eux.

Donc je peux appeler explore, passer le même graphe.

Mais maintenant votre nouveau nœud actuel serait ce voisin, juste comme cela, et cela effectuera la base de ligne de juste le genre de parcours en profondeur.

Mais nous devons également marquer les choses comme visitées, comme nous l'avons dit, dans la vidéo d'approche, c'est une partie vraiment importante de la solution.

Et je veux que cet ensemble visité soit global pour tout mon parcours.

Donc je vais devoir le créer, peut-être dans ma fonction principale ici.

Donc je peux créer ma constante visitée, en faire un ensemble JavaScript, parce que les ensembles JavaScript offrent pour moi un temps de recherche O de un, mais aussi un temps d'insertion O de un.

Cela va être une structure de données vraiment rapide à utiliser.

Et à partir de là, nous devons probablement ajouter plus de logique ici pour faire quelque chose avec la taille, mais pour l'instant, je pense que je vais changer de vitesse et regarder comment construire cette fonction d'aide, n'est-ce pas.

Donc je pense que la meilleure façon de construire ce parcours est de l'utiliser comme une sourde, typiquement mon choix pour un problème comme celui-ci, il va prendre en, je sais le graphique, la ligne et la colonne et aussi visité, j'ai besoin de quelques cas de base, c'est des cas de base très classiques, je vais commencer par vérifier si cette ligne de colonne de position est dans les limites.

Donc mon motif préféré pour cela est de le diviser en quelques variables, cela le rend juste plus facile à lire et à déboguer.

Donc je vais dire est ma ligne dans les limites et juste faire que comme une variable booléenne.

Donc je vais vérifier si, disons, zéro est inférieur ou égal à la ligne, je dois dire et, n'est-ce pas, et que la ligne devrait être strictement inférieure à la longueur de la grille.

Donc ce booléen ne serait vrai que s'il est dans les limites, n'est-ce pas ? Et quelque chose de très similaire pour mes colonnes de limites devrait être entre zéro et la longueur de la grille zéro.

Bien, juste comme ceci, je crois.

Et puis je peux écrire une belle instruction if en utilisant les deux clauses.

Donc je peux dire, d'accord, si disons votre ligne n'est pas dans les limites, ou votre colonne n'est pas dans les limites, alors vous êtes définitivement à une limite.

Donc vous devriez probablement utiliser un cas de base ici, n'est-ce pas ? Donc nous allons tous choisir de retourner ici est zéro, parce que je veux garder un nombre cohérent, n'est-ce pas, un type de retour cohérent.

C'est-à-dire que je sais que cette fonction a un objectif de retourner la taille des îles explorées, la taille est un nombre.

Donc même dans mon cas de base, je dois m'assurer que je retourne un type de nombre, retourner zéro pour représenter que, hey, si c'est hors des limites, cela ne va pas contribuer à quoi que ce soit dans le compte de la taille, n'est-ce pas, ce qui est bon à faire.

J'ai besoin d'un autre cas de base ici.

Que se passe-t-il si ma position est dans les limites.

Mais que se passe-t-il si c'est en fait de l'eau, je ne veux pas compter cela non plus.

Je ne veux compter que les îles.

Donc la terre, n'est-ce pas.

Donc une correction rapide, ce que je vais faire est d'ajouter un nouveau cas de base, je peux vérifier si ma grille à la ligne de la colonne, si elle est égale au caractère de l'eau.

Donc un W majuscule, je peux aussi retourner zéro.

Si vous voulez, vous pouvez aussi peut-être fusionner ceux-ci en une seule instruction if, juste écrire un tas de OU, j'aime bien les séparer parce que c'est juste facile pour moi de me souvenir de ce que chacun fait, écrire une conditionnelle ici est d'accord, si je passe ces deux cas de base, il pourrait être le cas que cette position est de la terre, mais c'est de la terre que j'ai déjà visitée.

Donc voici pourquoi je travaille dans ma logique visitée, je vais représenter une position, comme nous l'avons dit dans le dernier épisode, vraiment juste une chaîne.

Donc je peux la mettre comme les membres de mon ensemble visité.

Donc je vais dire position pour avoir à être la ligne plus une virgule plus la colonne.

Donc je représente simplement la position, c'est parce que je ne peux pas ajouter une sorte de tableau dans un ensemble visité, puis le chercher plus tard.

Et donc si visité a la position, alors c'est une position en double que j'ai explorée.

Donc retourne zéro.

Sinon, ce n'est pas encore visité.

Donc je dois le visiter maintenant.

Donc je peux l'ajouter.

Bien.

Donc j'ai posé mes cas de base.

Maintenant, j'aurai besoin de mon code récursif réel.

Donc je vais explorer mes quatre voisins.

À ce stade, vous devriez être familier avec ce motif.

Donc allez vers le haut, une ligne moins un, une colonne, passez la même visite.

Donc je vais explorer mes voisins haut, bas, gauche, droite respectivement.

Et je fais ma théorie récursive, n'est-ce pas.

Donc quel type je m'attends à recevoir de ces appels, ils vont me donner un nombre représentant la taille de l'île dont mon voisin fait partie.

Mais si mon voisin fait partie d'une île plus grande, alors moi aussi parce que nous sommes connectés, n'est-ce pas.

Et donc je veux créer le grand total de toutes ces valeurs de retour.

Donc je vais créer une variable de taille, disons let size, je vais l'initialiser à un ici, il va être un et non zéro, parce que le un représente ma position actuelle, ma ligne de colonne.

Et ce que ces appels retournent, quel que soit le nombre, je vais simplement incrémenter ma taille par ce nombre, comme ceci.

Ensuite, enfin, je peux retourner ma taille totale ici.

Donc cela fera mon parcours en profondeur, parce que c'est récursif, mais nous allons aussi additionner la taille de cette région de l'île.

Cool.

Donc maintenant que j'ai un explorateur de taille de travail, utilisons-le dans notre fonction principale ici.

Donc je vais obtenir un nombre de cet appel.

Je l'appellerai ma taille respective.

Et ce qui est génial avec cette logique, c'est que si j'ai une île ou une position que j'ai déjà vue avant, et que je la rencontre à nouveau dans cette boucle for, alors je vais simplement retourner tôt parce que je vais frapper ce cas de base, n'est-ce pas ? Si quelque chose a déjà été visité, retourne simplement automatiquement zéro, parce que je l'ai déjà considéré, il n'y a aucune raison de le considérer à nouveau.

Mais maintenant j'ai besoin de ma logique de minimisation, n'est-ce pas, je veux la taille de la plus petite île.

Et ils nous disent dans le problème que nous pouvons totalement supposer que votre grille contient au moins une île.

Donc je pense qu'une valeur par défaut géniale ici est d'utiliser l'infini positif, donc je peux définir une variable de taille min.

L'initialiser à l'infini positif, JavaScript, si je la rends infinie positive, je sais que lorsque je rencontre une taille d'île valide, elle sera inférieure à l'infini.

Et elle devrait la remplacer.

Donc maintenant je peux faire une logique min ici et vérifier.

D'accord, si la taille de cette île est inférieure à la taille minimale que j'ai vue jusqu'à présent, alors remplacez simplement cette taille min par cette île.

Ensuite, après avoir terminé tous ces parcours potentiels, je vais retourner ma taille min.

Donc quelques motifs classiques ici.

Il y a une nuance que nous ne considérons pas, comment exécuter le code, et nous pouvons le déboguer ensemble.

Donc il semble que nous avons échoué à l'exemple.

00.

Donc le tout premier exemple, nous nous attendions à une réponse de deux, nous avons accidentellement donné zéro.

Si vous regardez cet exemple, il est assez évident que oui, la taille minimale est deux représentant cette île ici.

La raison pour laquelle nous donnons zéro est selon notre code.

Donc je vais répondre, je sais que la ligne va être zéro, la colonne va être zéro, cela signifie que ma position serait cette w ici.

Lorsque je fais l'appel récursif, et que je passe la position 00, je sais qu'il va immédiatement retourner zéro parce que cette position est de l'eau.

Et je vais vérifier, d'accord, est-ce que ce zéro est inférieur à l'infini, oui, donc je vais remplacer la taille min par zéro.

Mais si j'y réfléchis, zéro ne représente même pas une vraie île.

Si une île a une taille de zéro, alors ce n'est pas une île du tout, c'était un morceau d'eau, n'est-ce pas ? Et donc je veux ajouter une logique supplémentaire ici pour ne considérer que les quantités non nulles.

Donc ne faites la comparaison que si cette taille est également valide.

Donc la taille doit être supérieure à zéro, bien sûr.

Et nous allons vouloir les ajouter ensemble.

Donc essayons cela à nouveau.

Juste un petit détail ici dont nous avons besoin.

Super.

Et voici une solution pour ce problème d'île minimale.

Donc nous avons vu ce motif quelques fois maintenant, n'est-ce pas, notre logique classique de saut d'île.

Donc lorsque vous pensez aux îles comme des composants connectés d'un graphe, cela devrait être votre premier algorithme de choix.

D'accord, programmeurs.

Donc cela conclut notre cours sur les graphes.

J'espère que vous avez appris beaucoup pendant le cours.

J'ai définitivement passé un bon moment à le faire, assurez-vous de vous rendre sur Shruti dotnet, où vous pouvez continuer à pratiquer plus de problèmes de graphes, ainsi qu'explorer d'autres sujets sur les structures de données et les algorithmes.

Je vous verrai là.