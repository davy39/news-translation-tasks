---
title: 'Mon premier projet Python : comment j''ai converti un fichier texte désorganisé
  en un fichier CSV bien structuré'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-29T03:54:06.000Z'
originalURL: https://freecodecamp.org/news/my-first-python-project-converting-a-disorganized-text-file-into-a-neatly-structured-csv-file-21f4c6af502d
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9caa9b740569d1a4ca8bf7.jpg
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: projects
  slug: projects
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: 'Mon premier projet Python : comment j''ai converti un fichier texte désorganisé
  en un fichier CSV bien structuré'
seo_desc: 'By Pranav Shridhar

  So I decided to learn Python. Turns out this computer programming language isn’t
  so hard (well, until I got this project! :P ).

  Within seconds, I fell in love with its easy, crisp syntax and its automatic indentation
  while writing....'
---

Par Pranav Shridhar

J'ai donc décidé d'apprendre Python. Il s'avère que ce langage de programmation n'est pas si difficile (enfin, jusqu'à ce que je me lance dans ce projet ! :P ).

En quelques secondes, je suis tombé amoureux de sa syntaxe simple et concise et de son indentation automatique lors de l'écriture. J'ai été fasciné lorsque j'ai appris que des structures de données comme les listes, les tuples et les dictionnaires pouvaient être créées et initialisées dynamiquement avec une seule ligne (comme ceci, nom-de-liste = [] ).

De plus, les valeurs contenues dans celles-ci pouvaient être accessibles avec ou sans l'utilisation d'index. Cela rend le code très lisible car l'index est remplacé par un mot anglais de son choix.

Assez parlé du langage. Laissez-moi vous montrer ce que le projet exigeait.

Mon frère m'a donné ce projet. Il est tombé sur un fichier texte contenant des milliers de mots. Beaucoup de ces mots partageaient presque le même sens. Chaque mot avait sa définition et une phrase d'exemple à côté, mais de manière peu organisée. Il y avait des espaces et des sauts de ligne entre un mot et sa phrase. Certains aspects manquaient aux mots. Voici des extraits du fichier texte dont je parle :

![Image](https://cdn-media-1.freecodecamp.org/images/WGYzW5bwRlbKbT1pJrheXmw4fiyw6pZxCygw)
_Ici, 'Glower' est précédé d'un saut de ligne alors que les autres ne le sont pas_

![Image](https://cdn-media-1.freecodecamp.org/images/FN02Y6fnT3JCd7o6-ld2BmvCrjMPjKoicKZ9)
_Ici, l'exemple de 'Shirk' est précédé d'un saut de ligne_

Il voulait que les aspects textuels soient uniformes. Pour cela, il avait besoin que je trie soigneusement tous les mots de sens similaire à côté d'un sujet. Il m'a dit que cela pouvait être réalisé en capturant toutes les données du texte dans un dictionnaire au format suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/KDTCLHvKcVqMomXywBEHEFy-8dTuhgNHsh1o)
_'Topic' est la clé et le reste sont les valeurs de la clé. Le format devient légèrement plus difficile à maintenir car chaque sujet contient plusieurs mots_

et ensuite les écrire dans un fichier CSV (Comma Separated Values).

Il m'a demandé si je pouvais prendre cela comme mon premier projet, maintenant que j'avais appris les bases. J'étais ravi de travailler sur la logique et j'ai donc instantanément accepté. Lorsqu'on m'a demandé le délai, il m'a donné un temps décent de 2 jours pour finir.

Hélas, j'ai fini par prendre le double de temps car j'ai eu du mal à déboguer correctement le code écrit. Franchement, si ce n'avait été pour les courtes visites de mon frère dans ma chambre pour voir l'avancement et me donner des indices sur les mauvaises hypothèses que j'avais faites en écrivant les conditions, j'étais destiné à finir le projet dans l'éternité :P

J'ai commencé par créer des mini-tâches au sein du programme que je cherchais à terminer avant de construire l'ensemble du programme. Elles étaient listées comme suit :

#### 1. Former une Regex pour faire correspondre un nombre et le mot suivant.

J'ai examiné le fichier texte et j'ai remarqué que chaque sujet (ici appelé 'clé') avait un nombre le précédant. J'ai donc écrit quelques lignes de code pour créer une regex (expression régulière - un outil puissant pour extraire du texte) du motif suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/cqV13FJrWa-utLtiM1D-p4ESdMjmw5lIrFGi)
_Le code ci-dessus trouve les correspondances selon la regex et les ajoute à une liste de chaînes._

Cependant, lorsque j'ai exécuté cela, j'ai obtenu une erreur, UnicodeDecodeError, ce qui signifiait que je n'avais pas accès au fichier texte. J'ai cherché sur [https://stackoverflow.com](https://stackoverflow.com) et après une longue recherche sans succès, mon frère est venu et a trouvé une solution. L'erreur a été rectifiée comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/wrNyd79CnlLaKQ2Jvy0ljZQOsEHWF9Zgj0jK)
_Drôle, comment une seule ligne - "errors = 'replace'" a fait le travail_

Pourtant, je n'ai pas obtenu le résultat souhaité. Cela était dû au fait que certaines clés avaient des barres obliques ('/') ou des espaces (' ') dans le texte que ma regex ne pouvait pas faire correspondre. J'ai pensé à améliorer l'expression regex plus tard et j'ai donc écrit un commentaire à côté.

#### 2. Obtenir une liste de lignes sous forme de chaînes à partir du fichier texte

Pour cela, j'ai écrit seulement 1 ligne de code et, heureusement, aucune erreur n'est apparue.

![Image](https://cdn-media-1.freecodecamp.org/images/qIn0n5s6L9QG4OGvy3sHXRbIAH4JxysGGPJq)
_Parfois, tout ce dont vous avez besoin est une ligne de code !_

Cependant, j'ai obtenu une liste non nettoyée. Elle contenait des sauts de ligne ('\n') et des espaces (' '). J'ai ensuite cherché à affiner la liste comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/-JeEJnbwq-Htyg1W0zRIyMjCCBWGB-2BlGrW)
_La première boucle 'for' remplace '\n' par '' et la seconde supprime '', donnant ainsi une liste propre._

#### 3. Extraire les mots, les significations et les phrases d'exemple séparément et les ajouter aux listes correspondantes.

Cela a été de loin la partie la plus difficile à réaliser car elle impliquait une logique appropriée et un jugement précis par reconnaissance de motifs.

Intéressamment, en parcourant le fichier texte, j'ai remarqué d'autres motifs. Chaque mot avait sa signification sur la même ligne, séparée par un signe '='. De plus, chaque exemple était précédé d'un signe ':' et du mot-clé 'Example'.

J'ai pensé à utiliser à nouveau les regex. J'ai trouvé une solution alternative et plus élégante en découpant la ligne (maintenant une chaîne dans la liste) selon l'emplacement des symboles. Le découpage est une autre fonctionnalité cool en Python. J'ai écrit le code comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/OsCkivyCNPKH6p2ntAg5zF-ouq3krcII1AAf)
_Le découpage collecte deux index et extrait la chaîne entre eux_

Le code ci-dessus se lit presque comme de l'anglais. Pour chaque ligne dans la liste propre, il vérifie si elle contient un signe '=' ou un signe ':'. Si c'est le cas, alors l'index du signe est trouvé et le découpage est effectué en conséquence.

Dans le premier 'if', la partie avant le '=' est stockée dans la variable 'word' et la partie après est stockée dans 'meaning'. De même pour le deuxième 'if' ('elif - else if - dans ce cas), la partie après ':' est stockée dans 'example'. Et après chaque itération, le mot, la signification et la phrase d'exemple sont stockés dans les listes correspondantes. De cette manière, toutes les données peuvent être extraites.

Jusqu'à présent, tout va bien. Mais j'ai noté que l'extraction devait être faite de manière à ce que chaque mot (et ses aspects) de la clé particulière soit accumulé ensemble comme une seule valeur pour la clé. Cela signifiait qu'il était nécessaire de stocker chaque mot, signification et exemple à l'intérieur d'un tuple. Chaque tuple devait être stocké à l'intérieur d'une seule liste qui se représenterait comme la valeur pour une clé particulière. Cela est représenté ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/Li4Hhl0IG-o9j7RBl-1NkBOx2y6PD2epxwD6)
_Le format pour stocker toutes les données comme une seule valeur pour une clé particulière_

Pour cela, j'ai prévu de collecter chaque mot, signification et phrase de chaque clé à l'intérieur d'une liste séparée enfermée par une autre liste, disons key-list. Encore une fois, l'image vous le dira plus précisément :

![Image](https://cdn-media-1.freecodecamp.org/images/G-KkcM7xNm0WEvziO9sar31JvRYVYA34IApF)
_Une liste séparée de mots pour chaque clé et de même pour les significations et les exemples_

Pour faire cela, j'ai ajouté le code suivant à celui que j'avais écrit pour le découpage :

![Image](https://cdn-media-1.freecodecamp.org/images/mJ7RVqA9LAd6OGtVi06muhAfceffajLHejDv)
_Faire les bonnes choses n'est pas toujours facile et ce qui semble facile n'est pas toujours correct !_

La logique de ce code (la partie else) s'est avérée incorrecte, malheureusement. J'ai fait une mauvaise hypothèse en supposant que seules 2 conditions ('=' et ':') existaient dans le texte. Il y avait de nombreuses exceptions que je n'ai pas remarquées. J'ai fini par perdre des heures à déboguer les erreurs possibles dans la logique. J'avais supposé que le fichier texte complet suivait le même motif. Mais ce n'était simplement pas le cas.

Incapable de progresser, je suis passé à la partie suivante du programme. J'ai pensé que je pourrais demander de l'aide à mon frère après avoir terminé les autres parties. :P

> À suivre...

#### 4. Créer des valeurs pour les clés en utilisant la fonction Zip et le déballage de paramètres.

À ce stade, je n'étais pas entièrement sûr de ce que je ferais même après avoir atteint la configuration ci-dessus des listes. J'avais appris la fonction 'Zip' et le 'déballage de paramètres' lors de l'une des discussions techniques de mon frère, qui littéralement zippe les listes qui lui sont passées, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/tSOhmVSt8tQUutN0wF6j2W2vFF-5lk0xQIqm)
_Fonction Zip en Python_

J'ai donc pensé que je pourrais combiner ces deux fonctionnalités pour obtenir le résultat souhaité. Après quelques allers-retours, en testant les fonctionnalités et en travaillant sur des listes factices, j'ai réussi. J'ai créé un fichier séparé (bêta) pour cette tâche, dont un extrait est donné ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/WqXdaySyVeD3oLPhqflTj-AEyj0utRmLREnq)
_Ce fragment de code a fonctionné sans faille ! :)_

Le fonctionnement du code ci-dessus peut être compris en regardant la sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/4NPeKGnsn38Pb4zE3hkvrEwYc3k20H6tC10i)
_List5 est la sortie finale requise_

La fonction zip() zippe les listes ou valeurs correspondantes à l'intérieur des listes et les enferme dans un tuple. Les tuples à l'intérieur des listes sont ensuite convertis en listes pour le déballage et un zip supplémentaire. Enfin, la sortie souhaitée est obtenue.

Je me suis senti beaucoup soulagé car le code a fonctionné cette fois. J'étais heureux de pouvoir manipuler les données à extraire et les mouler dans le format requis. J'ai copié le code dans le fichier principal sur lequel je travaillais et j'ai modifié les noms des variables en conséquence. Maintenant, il ne restait plus qu'à assigner des valeurs aux clés dans le dictionnaire (et bien sûr la partie extraction !).

#### 5. Assigner des valeurs aux clés dans le dictionnaire.

Pour cela, je suis arrivé à cette solution après quelques expérimentations avec le code :

![Image](https://cdn-media-1.freecodecamp.org/images/Y4PFIu20LiR4BU2ZdEM4Twg6PDLP9i3v33mW)

Cela a produit la sortie souhaitée comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/mb9BFyytdkVeneMWHhz6bpGspfZx59PldNSK)
_Cette sortie est basée sur le fichier bêta contenant à la fois les fragments de code précédents et actuels._

Le programme était presque terminé. Le principal problème résidait dans la partie extraction des données.

> ... suite de la section 3

Après des heures et des heures de débogage, je suis devenu de plus en plus frustré de voir pourquoi ce truc ne fonctionnait pas. J'ai appelé mon frère et il m'a donné un indice subtil sur les hypothèses que j'avais faites en définissant les boucles conditionnelles et les clauses if-else. Nous avons scruté le fichier texte et remarqué que certains mots avaient des exemples sur deux lignes au lieu d'une.

![Image](https://cdn-media-1.freecodecamp.org/images/YFJG3fz10RxPNE2foL54IrEM9cxvmgRR9fG6)
_Ici, les phrases d'exemple pour 'Incense' et 'Ire' prennent deux lignes au lieu d'une._

Selon la logique de mon code, puisque il n'y a pas de signe ':' dans la deuxième ligne (ni un signe '=', d'ailleurs), le contenu de la ligne ne serait pas traité comme une partie de l'exemple. Par conséquent, cette instruction rendrait vraie la dernière partie 'else' et exécuterait le code écrit dans celle-ci. En tenant compte de tout cela, j'ai modifié le code comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/XOVv2Ct5wZfEbwX5dxHCAEg9zIXFldxBgkRq)
_Modification - inséré une autre condition 'elif' et réécrit le code pour la partie 'else'_

Ici, hasNumbers() est une fonction qui vérifie si une ligne donnée contient des nombres. Je l'ai définie comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/ywXKLxpOnJxn21dZM-hGRcYROoFqDtDTNlNi)

Ce que cela fait, c'est qu'il collecte la deuxième ligne de l'exemple si toutes les autres conditions échouent, la combine avec la première ligne et l'ajoute ensuite à la liste correspondante comme avant.

À ma déception, cela n'a pas fonctionné et a plutôt montré une erreur indiquant que l'index était hors de portée. J'étais stupéfait, car chaque ligne de code semblait être logiquement correcte à mes yeux.

Après des heures de folie, mon frère m'a montré un moyen de récupérer les numéros de ligne où l'erreur s'est produite. L'une des principales compétences en programmation est la capacité à déboguer le programme, à vérifier correctement les erreurs possibles et à maintenir un flux continu.

Intéressamment, l'ajout suivant au code a signalé que l'erreur s'est produite autour de la ligne 1750 du fichier texte.

![Image](https://cdn-media-1.freecodecamp.org/images/rPvQnIMvfADSeUpBNr7PExQy1RFiqvH7PPbl)
_La fonction Enumerate ajoute un compteur à un itérable permettant un débogage facile en vérifiant le numéro de ligne où l'erreur s'est produite._

Cela signifiait que le programme fonctionnait bien jusqu'à ce numéro de ligne et que mon code était correct ! Les problèmes résidaient dans mes mauvaises hypothèses et aussi dans le fichier texte grâce à son hétérogénéité.

Cette fois-ci, j'ai remarqué que certaines clés n'étaient pas suivies de leurs nombres, ce qui causait des problèmes dans le flux logique. J'ai rectifié les erreurs en modifiant davantage le code comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/Ey2TyrvmuVoQZX5TlYPrHDKOXzjhq9Htn3PI)
_Cela a également bien fonctionné pendant un moment mais ensuite, crac !_

Cela a bien fonctionné jusqu'à la ligne 4428 du fichier texte mais a planté juste après. J'ai vérifié ce numéro de ligne dans le fichier texte lui-même mais cela n'a pas beaucoup aidé. Puis j'ai réalisé, à ma grande joie, que cela devait être la dernière ligne. Tout le programme fonctionnait sur la liste propre qui était vide de sauts de ligne et d'espaces. J'ai imprimé la dernière ligne de la liste propre et je l'ai comparée avec la dernière ligne du fichier texte. Elles correspondaient !

J'étais extrêmement heureux de le savoir car cela signifiait que le programme avait été exécuté jusqu'à la fin. La seule raison pour laquelle il a planté était qu'après la dernière phrase, aucune des lignes de code n'avait de sens. Mes conditionnelles étaient conçues pour vérifier à chaque fois la ligne suivante, ainsi que la ligne actuelle. Comme il n'y avait pas de ligne après la dernière ligne, il a planté.

J'ai donc écrit une ligne de code supplémentaire pour couvrir cela :

![Image](https://cdn-media-1.freecodecamp.org/images/ymJP4egnknSAv1QgKxRTl-ugOPQrF0ZVOnke)

Tout fonctionnait maintenant. Enfin ! Maintenant, tout ce que j'avais à faire était d'assigner les clés aux valeurs correspondantes et c'est tout ! J'ai fait une pause à ce moment-là, considérant que mon projet était enfin terminé. J'ajouterais quelques touches finales plus tard.

Mais avant de faire une pause, j'ai décidé d'enfermer chaque code à l'intérieur de diverses fonctions afin de rendre le code propre. J'avais déjà beaucoup de mal à naviguer de haut en bas dans les lignes de code. J'ai donc décidé de faire une pause après avoir fait cela.

Cependant, après l'avoir fait, le programme a commencé à donner des erreurs de portée de variable. J'ai réalisé que c'était parce que les variables déclarées à l'intérieur des fonctions ne peuvent pas être appelées directement de l'extérieur de la fonction car elles sont dans l'espace de noms local. Peu disposé à faire d'autres changements en raison de cette erreur stupide, j'ai décidé de revenir au même code avec lequel je m'étais battu depuis le début.

Cependant, à ma grande incrédulité, le programme n'a pas fonctionné de la même manière qu'avant. En fait, il n'a pas fonctionné du tout ! Je n'ai tout simplement pas pu comprendre la raison (et je ne le peux toujours pas !). J'étais profondément déprimé pour le reste de la journée. C'était comme vivre un cauchemar avant même de s'endormir !

Heureusement et miraculeusement, le code a fonctionné le lendemain après que j'ai fait quelques changements minutieux. J'ai fait en sorte de créer de nombreux fichiers bêta (pour chaque changement effectué) par la suite afin d'éviter un tel chaos inutile.

Après quelques heures de plus, j'ai enfin pu terminer mon programme (mais pas avant d'avoir consommé 4 jours complets). J'ai apporté quelques autres modifications telles que :

i) modifier la fonction 'hasNumbers' en fonction 'hasNumbersDot' et exclure la regex que j'avais faite plus tôt dans le programme. Cela correspondait aux clés plus efficacement car il n'avait pas d'hypothèses et donc pas d'exceptions. Le code pour cela est le suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/IVIaKsOIkEAfhxoL737S0YMNGtUfNfjgIlN5)
_Cela retourne 'True' si cela correspond aux lignes contenant un nombre et un mot au début de la ligne au lieu de la précédente qui correspondrait au même n'importe où dans la ligne._

ii) remplacer la condition regex et le code pour obtenir les clés à partir de la liste propre.

![Image](https://cdn-media-1.freecodecamp.org/images/Cd-MM7Zu99xYidQZ82J1duxfyuejp8xtvphe)
_Remplacé ceci par le code ci-dessous_

![Image](https://cdn-media-1.freecodecamp.org/images/dDKUZ56tPnPXy7K2eSCDX-YkGsOJW0prraFX)
_Ceci est beaucoup plus efficace que le précédent car il utilise la fonction déjà définie 'hasNumbersDot'. De plus, il correspond à la ligne complète (clé complète)_

iii) combiner les conditions 'if' dans la partie 'extraction des exemples'

![Image](https://cdn-media-1.freecodecamp.org/images/L4mhW4jQTRtYajUyi1SPyfhCP9hQxorFshok)
_Avant cette modification, la dernière phrase d'exemple ne pouvait pas être extraite de chaque clé_

iv) concrétiser le code pour l'assignation des clés du dictionnaire

![Image](https://cdn-media-1.freecodecamp.org/images/ee6HfHmapwAOpPMVcQOlRLB9-4CBKmNlizdI)

De plus, après quelques essais et erreurs, j'ai pu convertir les données obtenues en un fichier CSV magnifiquement structuré :

![Image](https://cdn-media-1.freecodecamp.org/images/SEdcM6tUH30EzegWEn4W44KOiwaMW7Pqoj7T)

![Image](https://cdn-media-1.freecodecamp.org/images/8rTek-mWVCF4izuq8mNX8a3cHsfcguXtFgV8)
_Code pour obtenir un fichier CSV_

> Vous pouvez consulter mon dépôt github sur mon [profil](https://github.com/pranavmodx) pour voir le code complet du programme, y compris le fichier texte et le fichier csv.

Dans l'ensemble, ce fut une grande expérience. J'ai appris tellement de choses grâce à ce projet. J'ai également gagné plus de confiance en mes compétences. Malgré quelques événements malheureux (la programmation implique de telles choses :P), j'ai finalement pu accomplir la tâche donnée.

Une dernière chose ! Récemmment, je suis tombé sur un mème hilarant concernant les étapes du débogage qui est si relatable à mon expérience que je ne peux pas m'empêcher de le partager. xD

![Image](https://cdn-media-1.freecodecamp.org/images/wliLCjiLP7NjE27uYnBliU7ovlILBPI-xc6r)

Merci d'être arrivé jusqu'ici (même si vous avez sauté la plupart pour vérifier le résultat final :P).