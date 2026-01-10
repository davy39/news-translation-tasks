---
title: Comment implémenter des algorithmes d'arbres binaires lors des entretiens techniques
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-10-19T17:13:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-binary-tree-algorithms-in-technical-interviews
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/binary.png
tags:
- name: coding interview
  slug: coding-interview
- name: youtube
  slug: youtube
seo_title: Comment implémenter des algorithmes d'arbres binaires lors des entretiens
  techniques
seo_desc: 'A binary tree is a common data structure used in software development.
  It is also a frequent topic in technical coding interviews.

  We just published a course on the freeCodeCamp.org YouTube channel that will teach
  you all about binary tree algorithms...'
---

Un arbre binaire est une structure de données courante utilisée dans le développement logiciel. C'est également un sujet fréquent lors des entretiens de codage technique.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous apprendra tout sur les algorithmes d'arbres binaires et vous préparera à les utiliser lors des entretiens de codage et des projets de programmation.

Alvin Zablan de Structy a développé ce cours. Il a créé de nombreux cours techniques, y compris l'un des cours de programmation dynamique les plus populaires sur Internet.

Dans ce cours, vous apprendrez d'abord la théorie derrière les algorithmes, puis vous apprendrez à les implémenter avec du code. Les algorithmes seront enseignés avec des images et des visualisations pour vous aider à vraiment comprendre comment ils fonctionnent.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-57.png)
_Ce type d'arbre binaire ne sera pas couvert dans le cours._

Voici les sujets abordés dans ce cours :

* Qu'est-ce qu'un arbre binaire ?
* Classe de nœuds d'arbre binaire
* Valeurs de profondeur d'abord
* Valeurs de largeur d'abord
* Inclut l'arbre
* Somme de l'arbre
* Valeur minimale de l'arbre
* Somme maximale du chemin de la racine à la feuille

Regardez le cours complet ci-dessous ou [sur la chaîne YouTube freeCodeCamp.org](https://youtu.be/fAAZixBzIAI) (2 heures de visionnage).

%[https://youtu.be/fAAZixBzIAI]

## Transcription

(générée automatiquement)

Un arbre binaire est une structure de données courante utilisée dans le développement logiciel.

C'est aussi un sujet fréquent et des entretiens de codage technique dans ce cours, Alvin expliquera les algorithmes d'arbres binaires et vous préparera à les utiliser à la fois lors des entretiens et des projets de codage.

Hey programmeurs, Hamilton de Shruthi, elk à notre cours sur les arbres binaires, je veux vous montrer comment vous pouvez bien réussir ces entretiens techniques qui ont des problèmes d'arbres binaires.

Alors, ce que j'ai en réserve pour ce cours, comme d'habitude, nous allons passer en revue à la fois les théories pines et les algorithmes d'arbres binaires, ainsi que, bien sûr, être plus pratique et venir avec une implémentation de code de ces algorithmes vraiment un coup de poing.

Pour chaque section, nous allons nous assurer de dessiner des images et de visualiser et de vraiment comprendre l'algorithme sur le tableau blanc, les notes se sentent à l'aise avec cela, nous passerons à l'implémentation du code.

En termes de prérequis pour ce cours, je vais supposer que vous n'êtes pas nouveau en programmation.

Et peut-être que vous avez dabblé dans certaines structures de données et algorithmes précédents.

Et vous êtes également familier avec une certaine récursivité.

Mais cela dit, je vais supposer que vous ne savez rien sur les arbres binaires, et même juste les arbres en général.

sans plus tarder, plongeons-nous directement.

Donc, première ordre des affaires, comprenons ce que le mot arbre signifie même.

Et comme le concept de programmation, n'est-ce pas.

Donc, lorsque nous visualisons un arbre, un arbre contient de nombreux nœuds, généralement nous dessinons des nœuds comme des cercles, n'est-ce pas.

Et ces nœuds peuvent également pointer vers d'autres nœuds.

Donc, ici, j'ai un nœud.

Et je pourrais pointer vers un autre nœud, n'est-ce pas, je pourrais pointer vers n'importe quel nombre de nœuds.

Donc, voici les cercles, je vais les appeler des nœuds, et les lignes ou heures entre eux, je vais les appeler des arêtes, n'est-ce pas.

Donc, c'est un exemple d'un arbre.

Et les arbres peuvent, bien sûr, venir dans de nombreuses formes et tailles différentes.

Donc, voici un arbre assez grand.

Essayons de comprendre quelques termes que nous pouvons utiliser lors de nos entretiens techniques.

Et c'est quelque chose que je recommande vivement, n'est-ce pas ? Cela aide si vous parlez la langue, cela montre que vous avez une maîtrise de la structure de données, nous pourrions stocker des valeurs dans les nœuds de notre arbre.

Pour l'instant, je vais juste mettre quelques lettres.

Lorsque cela concerne vos programmes, vous pouvez stocker n'importe quel type que vous voulez, vous pouvez stocker des entiers, des nombres, ou même d'autres objets.

Parce que nous avons un arbre, nous aimons utiliser des relations familiales.

En d'autres termes, je pense à un arbre généalogique, n'est-ce pas ? Donc si je regarde le nœud B, disons que je les appelle le parent.

Si b est le parent, je sais que les enfants de B sont simplement les nœuds D, n'est-ce pas ? Leur parent et enfant est comme une relation relative.

Disons que j'ai changé mon cadre de référence.

Et disons que j'ai regardé a comme le parent, eh bien, ce scénario, alors B et C sont les enfants de a.

pour le cas du nœud C, si je pense à CSM parent, il n'a qu'un seul enfant, son enfant unique étant le nœud F.

Donc, n'hésitez pas à utiliser cette relation parent-enfant lorsque vous décrivez la relation entre les nœuds d'un arbre.

Un autre terme est une racine dans le contexte des arbres est le mot racine, n'est-ce pas ? Donc une racine va être un nœud qui n'a pas de parent.

Donc, dans cet arbre, A est la racine parce que a n'a pas de parent, n'est-ce pas ? Il n'y a pas de flèches allant dans le nœud a.

De l'autre côté, si je regarde les nœuds dans DNF, nous les appelons nœuds feuilles.

Un nœud feuille est un nœud qui n'a pas d'enfants, n'est-ce pas, donc d et f n'ont pas de flèches sortantes.

Typiquement, dans un arbre binaire, nous allons avoir une seule racine et nous pourrions avoir de nombreuses feuilles.

Une chose que je veux m'assurer de faire est de m'assurer que vous généralisez votre compréhension d'une feuille, n'est-ce pas ? Donc dans cet exemple particulier, il semble que chaque feuille est à deux arêtes de la racine, en comptant le nombre de flèches depuis les racines, n'importe quelle feuille, il pourrait être le cas que mes feuilles se produisent à différents niveaux, n'est-ce pas ? Donc j'ai supprimé ce nœud F, auquel cas C est maintenant une feuille, n'est-ce pas ? Bien que C soit sur un niveau différent de D et E, ce n'est pas le niveau le plus bas, il est toujours le cas qu'il s'agit d'une feuille, n'est-ce pas ? Un nœud feuille est simplement un nœud qui a zéro enfants.

D'accord.

Donc, avec tous ces termes hors de propos, concentrons-nous sur le vrai sujet ici.

À droite, j'ai beaucoup parlé des arbres.

Mais vraiment dans ce cours, je veux passer en revue les bases des arbres binaires.

N'est-ce pas ? Donc, regardons cette partie binaire pour commencer.

C'est vraiment un indice.

Nous savons que binaire a à voir avec le nombre deux.

Un arbre binaire est un arbre où chaque nœud a au plus deux enfants.

N'est-ce pas ? Donc actuellement à l'écran, j'ai un arbre binaire.

Si je donnais un autre enfant, disons un troisième nœud ici de f, ce serait un arbre mais pas un arbre binaire.

N'est-ce pas ? Ce serait comme un arbre ternaire parce que j'ai au plus trois enfants.

Donc, disons que j'enlève ce nœud supplémentaire.

Maintenant, c'est de retour à un arbre binaire.

Et il pourrait être le cas qu'un nœud ait moins de deux enfants mais soit toujours un arbre binaire, n'est-ce pas ? Donc si je donnais C, juste un enfant de f, ce serait toujours un arbre binaire.

C'est si je regarde n'importe quel nœud dans mon arbre, ce nœud aura 0, 1 ou deux enfants, et personne n'a plus de deux enfants, n'est-ce pas ? Donc vous voulez vous assurer de vous souvenir qu'un nœud dans un arbre binaire pourrait avoir moins de deux enfants.

D'accord.

Donc, je serai le premier critère pour comprendre ce qu'est un arbre binaire, n'est-ce pas ? C'est probablement le critère le plus facile et le plus d'enfants par nœud, je vais aussi vouloir m'assurer d'ajouter dans notre définition une compréhension robuste, c'est aussi de se souvenir que, au moins pour nous en informatique, nous pensons à nos arbres binaires comme ayant exactement une racine, ce qui signifie qu'il devrait y avoir seulement un seul nœud qui n'a pas de parent, n'est-ce pas ? Typiquement, lorsque nous dessinons, ce serait comme le nœud le plus haut.

Donc, pour l'instant, c'est définitivement jusqu'à présent un arbre binaire.

Si j'avais un autre nœud dans ce dessin, comme G, n'est-ce pas, g n'a aussi pas de parents, je ne considérerais plus cela comme un arbre binaire classique, n'est-ce pas ? Donc, faites attention à cela.

Passons à notre dernier critère, nous avons aussi besoin d'un autre ingrédient.

Et c'est exactement un chemin entre la racine et n'importe quel nœud, n'est-ce pas.

Donc, en regardant mon exemple à gauche, c'est effectivement un arbre binaire qui répond à tous les trois critères.

Et disons que j'ai choisi la racine et n'importe quel nœud, évidemment, il n'y a qu'une seule racine, donc nous considérons définitivement le nœud a, disons que j'ai choisi un nœud aléatoire comme E, c'est vraiment un arbre binaire, alors nous sommes garantis d'avoir seulement un seul chemin qui relie A à E, un chemin est vraiment juste une série de nœuds connectés que je peux traverser, n'est-ce pas, donc pour aller de la racine a au nœud E, je peux aller de A à B à E, et ce serait un chemin.

Et c'est la seule façon d'aller de A à E.

C'est ce que je veux dire par exactement un chemin.

Disons que j'ai choisi un autre nœud comme F.

Il y a aussi exactement une façon d'aller de la racine à F, et c'est juste a CF, ce serait le seul chemin.

Si j'ajoutais quelques connexions ou arêtes supplémentaires dans mon arbre, je pourrais obtenir un scénario comme celui-ci, ce ne serait plus un arbre binaire.

Pour une chose, nous pouvons voir que B a trois enfants, mais aussi ne pas avoir un chemin unique entre la route et n'importe quel nœud.

Par exemple, si j'ai choisi a et la note de f, une façon d'y arriver est en allant ACF.

Mais une autre façon d'y arriver serait a, b, c, f, n'est-ce pas ? Et donc faites attention à tous les trois critères lorsque vous considérez un arbre binaire.

Génial.

Donc, regardons quelques exemples plus petits.

Et c'est là que je pense que certains étudiants ont tendance à avoir des difficultés avec leur compréhension des arbres binaires.

Donc, si j'enlevais quelques nœuds ici, ce serait définitivement encore un arbre binaire, n'est-ce pas ? Juste en regardant nos différentes règles, n'est-ce pas ? Disons que le nœud racine A n'avait qu'un seul enfant, ce serait toujours un arbre binaire, n'est-ce pas ? Parce que l'arbre binaire exige seulement que nous ayons au plus deux enfants, nous avons toujours une racine, et nous avons toujours seulement un chemin de la racine à n'importe quel nœud.

Disons que j'ai le plus petit arbre qui a un nœud, ce qui serait l'arbre singleton, cela est toujours considéré comme un arbre binaire, n'est-ce pas, a une racine.

Et il n'y a pas vraiment de chemin à avoir ici sauf le chemin vers lui-même.

Et chaque nœud a au plus deux enfants.

Ici, nous avons zéro enfant, n'est-ce pas ? Le dernier cas limite que nous voulons considérer est ce qui se passe lorsque nous n'avons pas de nœuds, n'est-ce pas ? Nous considérons cela comme l'arbre vide.

C'est un cas très spécial.

Et nous devrions considérer tout arbre vide comme étant en fait un arbre binaire.

Cela va être très utile lorsque nous viendrons avec quelques algorithmes plus tard, n'est-ce pas.

Donc, un cas limite courant à considérer est ce qui se passe lorsque nous avons un arbre vide, c'est un arbre avec zéro nœuds, n'est-ce pas ? Regardons un autre exemple.

Disons que j'avais cette structure, prenez un moment pour la regarder, et voyez si cela répond à nos critères.

Cela ne serait pas considéré comme un arbre binaire.

Donc, nous regardons vos différents critères.

En regardant le premier, il a au plus deux enfants par nœud, donc c'est bon.

Mais nous ne pouvons pas identifier exactement une racine ici.

Rappelez-vous qu'un nœud racine est un nœud qui n'a pas de parent, n'est-ce pas ? Si vous regardez chaque nœud dans cette image, chaque nœud a exactement une flèche entrante.

Cela signifie que chaque nœud a au moins un parent, n'est-ce pas ? Donc, cela ne répond pas à ce critère.

Et de plus, il n'y a pas exactement un chemin entre la racine et n'importe quel nœud, parce que nous avons un cycle dans la structure.

Donc, par exemple, disons que je commençais à a et que je voulais voyager jusqu'à c, une façon d'y arriver serait d'aller A, B, C, ce serait un chemin.

Mais je pourrais aussi avoir un autre chemin ou je fais juste le tour deux fois et je vais A, B, C, encore, il y aurait en fait un nombre infini de chemins dans ce scénario.

À cause de cela, ce n'est définitivement pas un arbre binaire.

Et il y a plusieurs raisons pour cela.

Si j'avais un exemple différent, en regardant celui-ci, maintenant j'ai besoin des critères un et deux, n'est-ce pas, j'ai au plus deux enfants pour chaque nœud.

Mais j'ai aussi toujours exactement un nœud racine ici, je considérerais z comme le nœud racine.

Cependant, il n'y a pas un chemin entre les racines et n'importe quel nœud et parce que j'ai ce cycle.

Donc, ces règles valent vraiment la peine d'être retenues, elles vont vraiment vous aider à résoudre des problèmes d'arbres binaires beaucoup plus difficiles.

Et si vous vous souvenez de ces trois règles, vous pouvez identifier différents problèmes dans un cadre d'arbre binaire.

En d'autres termes, les problèmes les plus difficiles que vous rencontrerez lors de vos entretiens sont des problèmes où ils ne vous disent pas directement avec quelle structure de données vous traitez, vous allez simplement devoir remarquer le motif.

En d'autres termes, que se passe-t-il si je vous donne une structure comme celle-ci, prenez un moment et découvrez si c'est un arbre binaire.

Si vous regardez de près, cela répond à tous les trois critères pour être un arbre binaire.

Je peux simplement traiter a comme la racine parce qu'il n'a pas de parent.

Je peux traiter les nœuds D et F comme les feuilles parce qu'ils n'ont pas d'enfants.

Je viens de le dessiner de manière assez intéressante.

N'est-ce pas ? Si vous rangez vraiment les choses dans un sens classique d'arbre binaire, cela ressemblerait à ceci.

Plus important encore, cela a les mêmes relations qu'un dessin précédent, je l'ai juste montré de manière descendante, n'est-ce pas ? Donc, peu importe ce que vous comprenez de ces trois règles pour un arbre binaire, n'est-ce pas ? Parce que parfois, cela peut ne pas être aussi explicite qu'un joli dessin en forme de triangle.

Génial.

Donc, nous avons beaucoup parlé de la théorie de la façon de, vous savez, regarder et raisonner à travers certaines définitions d'arbres binaires.

Allons-y et commençons à parler de la façon dont nous pourrions représenter un arbre binaire de manière programmatique.

En d'autres termes, comment pouvons-nous faire cela dans un certain code ? Eh bien, peu importe votre langage de programmation de choix, je pense que vous allez représenter ceux-ci comme des objets.

En d'autres termes, chaque nœud ici va être un objet.

Donc, cela pourrait être comme une instance d'une classe, les propriétés à stocker dans cet objet seraient la valeur actuelle.

Donc, j'ai besoin de quelque chose pour stocker comme le A de mon nœud actuel.

Mais j'ai aussi besoin de faire référence à certains enfants.

Donc, nous aurons aussi besoin de certains pointeurs gauche et droit vers les enfants, n'est-ce pas, ceux-ci vont simplement être des propriétés sur cet objet.

Dans un arbre binaire classique, il est très courant de faire référence aux deux enfants en utilisant une direction gauche et droite.

Remarquez que certains nœuds ici, comme le nœud C, n'auront qu'un seul enfant, n'est-ce pas ? C n'a qu'un nœud point, n'est-ce pas ? Il n'a pas de gauche.

Donc, nous allons devoir utiliser une valeur vide, comme null ou undefined.

Pour représenter un enfant qui n'existe pas, n'est-ce pas ? Surtout pour un nœud comme lui, il n'a pas de gauche et aussi pas de droite.

Donc, voici ce que nous allons faire, allons-y et sautons dans mon éditeur de texte.

Et je vous montrerai comment vous pourriez représenter un arbre binaire de manière programmatique.

Donc, transition, nous voici dans mon éditeur de texte.

Commençons par créer notre classe de nœuds, n'est-ce pas.

Donc, vous pourrez suivre dans n'importe quel langage que vous choisissez, je vais le faire en JavaScript, n'est-ce pas.

Donc, je pense que la meilleure façon de présenter un nœud est d'utiliser une classe.

Donc, espérons familier avec une syntaxe de classe classique, créons une classe de nœuds, il y aura un constructeur rapide, je pense que ce serait précieux de prendre la valeur initiale qui sera stockée dans les notes, je prendrai les ns comme argument du constructeur, je peux simplement définir this dot Val à cette valeur, et j'aurai aussi besoin de deux propriétés supplémentaires, une pour ma gauche, donc je peux dire this dot left, je vais l'initialiser à null, cela signifie que par défaut, un nœud n'aura pas d'enfant gauche de la même manière.

Par défaut, un nœud n'aura pas d'enfant droit, n'est-ce pas ? Donc lorsque vous utilisez no pour représenter les enfants qui n'existent pas ici, génial.

C'est tout ce dont vous avez besoin pour créer, vous savez, un arbre binaire de base, n'est-ce pas, nous allons utiliser cette classe beaucoup pendant le cours pour tester nos algorithmes.

Donc, je vais créer un nœud et éventuellement connecter un arbre.

Eh bien, je vais juste appeler mon constructeur quelques fois, je vais créer différents nœuds, je vais juste les stocker dans quelques noms de variables.

Et bien sûr, un nouveau nœud pour créer une nouvelle instance de nœud, et je vais stocker une valeur à l'intérieur, je vais stocker quelques caractères à l'intérieur, je vais créer un tas de ces différents nœuds, ce que nous allons vouloir nous assurer de faire est de nous assurer que vous définissez également leurs pointeurs correctement.

Donc, je vais donner à chacun de ceux-ci des valeurs différentes ABC, D, E, aussi faire F.

Et puis je vais juste manuellement pour l'instant définir leurs pointeurs correctement.

Donc, que se passe-t-il si je fais une syntaxe comme celle-ci puisque je suis en JavaScript, je peux facilement assigner ces pointeurs, je peux dire, la gauche de A va être B.

Je peux dire la droite de A ? est C peut aussi dire la gauche de B D.

et puis la droite de B est E.

Et peut-être finalement je peux dire la droite de C est F.

Donc, en faisant ces assignations, je connecte certains nœuds ensemble, je devrais finir avec une structure comme celle-ci, n'est-ce pas ? Avoir a comme racine, parce que rien ne pointe vers a, il n'a pas de parent.

Mais a a deux enfants de NC.

Et puis avec cela, B a deux enfants de D et E.

Enfin, C a juste un enfant droit de f, c'est en fait le même arbre que nous avons regardé beaucoup pendant la session de tableau blanc, n'est-ce pas ? Et c'est comment vous pouvez représenter cet arbre de manière programmatique, n'est-ce pas ? Donc, je pense toujours que c'est précieux d'essayer de visualiser vos arbres, n'est-ce pas ? Évidemment, nous avons créé cet arbre de manière très manuelle, probablement à long terme, nous créerons des applications pour simplement maintenir et créer des arbres dynamiquement pendant une certaine entrée.

Mais pour l'instant, nous commencerons par créer tous nos arbres de cette manière très statique.

N'est-ce pas ? Et donc, avec cela, maintenant que nous avons une compréhension de la façon de représenter un arbre binaire, allons-y et retournons au tableau blanc.

Et je peux vous montrer notre tout premier algorithme.

Hey, programmeurs, Alvin ici, n'est-ce pas ? Maintenant, je veux passer en revue ce problème de valeurs de profondeur d'abord.

Donc, ce sera une bonne révision de l'algorithme de parcours en profondeur d'abord.

Donc, que voulez-vous faire dans ce problème ? Eh bien, ce que nous voulons faire, c'est prendre un arbre binaire, et en particulier, votre fonction va prendre la racine de l'arbre binaire.

Et rappelez-vous simplement que, étant donné le nœud racine d'un arbre binaire, nous savons que ce nœud aura des pointeurs vers ses enfants gauche et droit, qui peuvent pointer vers d'autres nœuds.

Cependant, si, disons, un nœud n'a pas d'enfant gauche ou droit, alors son pointeur sera défini sur No.

Donc, c'est ainsi que je représente notre arbre binaire de manière programmatique.

Mais pour l'instant, contentons-nous de la représentation visuelle de notre arbre.

Donc, pour un parcours en profondeur d'abord, nous pouvons commencer avec le nœud racine de a, ce que nous ferons, c'est simplement l'ajouter à une collection.

Et nous allons devoir les maintenir dans un ordre très particulier.

Et à partir de là, selon un parcours en profondeur d'abord, je pourrais aller à B.

Et voici où nous prenons notre décision vraiment importante, n'est-ce pas, nous pouvons soit aller à C, soit à D, si je fais un parcours en profondeur d'abord, je dois aller plus profondément dans l'arbre avant de me déplacer latéralement.

Donc, cela signifie que je vais de B à D.

Et une fois que je les ai achetés à D, il n'y a nulle part plus profond, je peux aller de D.

Et donc maintenant je me déplace latéralement vers le nœud E.

Et ce motif continue, n'est-ce pas ? Je n'ai rien de plus profond de E.

Donc maintenant je vais à C.

Et puis de C, je vais à f.

Donc, ce serait un parcours en profondeur d'abord sur cet arbre binaire.

Remarquez qu'il va A, B, D, E, C, F, et encore, la caractéristique vraiment importante est que nous devons aller plus profondément dans l'arbre jusqu'à ce que nous ne puissions plus et ensuite nous pouvons traverser l'arbre.

Cela dit, comment pouvons-nous réellement parvenir à implémenter cet algorithme.

Si vous êtes familier avec la profondeur d'abord, traditionnellement, alors nous savons qu'il va utiliser une structure de données comme une pile.

Donc, installons-nous ici.

Donc, nous allons retracer cela à nouveau.

Mais cette fois, en regardant de très près comment nous pouvons utiliser une pile pour accomplir cet ordre direct.

Et donc, rappelez-vous simplement qu'une pile est une structure de données séquentielle où nous ne pouvons ajouter des choses qu'au sommet de la pile et retirer des choses du sommet de la pile.

Donc, une caractéristique vraiment importante est que nous ne pouvons vraiment pas insérer ou retirer des éléments de n'importe où sauf du sommet de la pile.

Donc, lorsque j'ajoute des choses à la pile, je les ai ajoutées au sommet comme ceci.

Lorsque je retire des choses, c'est aussi du sommet comme ceci.

D'accord, donc lorsque je commence cet algorithme de parcours en profondeur d'abord, je vais commencer avec le nœud racine de a.

Et par défaut, je prends simplement ce nœud racine et je le stocke sur ma pile.

Donc, c'est la seule chose sur ma pile en ce moment, je vais utiliser ces rectangles pour représenter mes différentes piles de cadres.

Et vraiment dans mon programme, cela signifierait simplement stocker l'instance réelle du nœud ou un pointeur vers celui-ci.

Cool.

Et à partir de là, je commence réellement mon algorithme principal.

Donc, le flux principal d'un parcours en profondeur d'abord, nous allons vérifier si la pile est vide.

Pour l'instant, la pile n'est pas vide, car j'ai au moins un élément.

Et donc ce que je fais, c'est que je commence par retirer ou dépiler l'élément du haut de ma pile.

Donc, je vais retirer le A, et je vais l'étiqueter comme mon nœud actuel en cours d'exploration.

Et lorsqu'une chose quitte la pile, alors je peux la considérer comme étant visitée maintenant.

Donc, j'ai besoin de lister mes valeurs, car c'est tout le but de ce problème, n'est-ce pas ? Donc maintenant, je viens de visiter le nœud a.

À ce stade, je peux regarder les enfants de ce nœud maintenant.

Donc, je regarde le nœud a dans l'arbre, et je vois qu'il a un enfant B à sa gauche et un enfant C à sa droite.

Et à partir de là, je pousse ou ajoute ces deux enfants à ma pile.

Donc, je vais mettre c en premier, et je mets B ensuite.

Et remarquez que si je pousse mon enfant droit en premier, suivi de mon enfant gauche, cela fait en sorte que mon enfant gauche soit au sommet de ma pile, ce qui signifie que je le frapperais ensuite.

Et cela se termine sur ma première itération de ce parcours en profondeur d'abord.

Et maintenant, je pose cette même question : ma pile est-elle vide, elle ne l'est pas.

Donc, je retire le haut de ma pile, je l'appellerai B, mon courant, ce qui signifie que je pourrais l'imprimer ou l'insérer dans ma liste de valeurs.

Bien.

À partir de là, je considère les enfants de B, B a deux enfants.

Donc, je les ajoute tous les deux, je pousse E, suivi de D.

Cela termine cette itération.

Maintenant, quelque chose d'intéressant se produit, ma pile n'est toujours pas vide.

Donc, je sais que j'ai retiré le haut, donc j'appelle D, mon courant, j'ajoute D à ma liste de valeurs.

Mais si je regarde ces enfants, il n'a en fait aucun enfant, n'est-ce pas, et donc il n'y a rien à ajouter à la pile à partir d'ici.

Et donc, techniquement, j'ai terminé cette itération.

Et maintenant, j'ai encore des choses sur ma pile.

Donc, maintenant, je retire he du haut de ma pile.

Même chose qu'avant, n'est-ce pas, je l'ajoute à mes valeurs, he n'a pas d'enfants.

Donc, j'ai terminé cette itération.

Enfin, FC, j'ai retiré C de la pile, et je l'ai imprimé dans mes valeurs.

Et à ce moment-là, je vois que le nœud C n'a qu'un seul enfant, donc je vais simplement pousser l'enfant qui existe, donc je pousserais le nœud F sur ma pile.

Et c'est une chose vraiment importante à retenir lorsqu'il s'agit de mettre en œuvre votre parcours en profondeur d'abord, vous allez devoir vérifier si vos enfants existent avant de les ajouter à votre pile.

Et maintenant, lors de la toute dernière itération, nous avons le nœud F, nous le retirons de la pile, nous l'ajoutons à notre liste de valeurs, f n'a pas d'enfants.

Et donc, je termine cette itération et maintenant ma pile est vide et je vais simplement sortir à droite une fois la pile vide.

Je sais que j'ai parcouru tout l'arbre binaire.

Donc, nous y voilà et nous obtenons la bonne sortie ici.

Donc, simplement en utilisant une pile et en obéissant aux règles de la pile, c'est-à-dire que nous avons poussé vers le haut et retiré du haut, nous obtiendrons le bon ordre.

Une chose importante à retenir est que vous devez ajouter vos valeurs dans votre liste de valeurs lorsque quelque chose quitte la pile.

Cela dit, que pouvons-nous dire sur la complexité temporelle et spatiale de cet algorithme ? Eh bien, c'est en fait assez simple.

Disons que nous définissons n comme le nombre de nœuds dans cet arbre binaire, alors nous pouvons dire que la complexité temporelle de ceci est O de n.

Et pourquoi dis-je cela ? Eh bien, nous allons simplement ajouter chaque nœud éventuellement à notre pile.

Et ce nœud va aussi quitter la pile exactement une fois.

Donc, ce n'est pas comme si nous visitions deux fois l'un des nœuds.

Donc, je suis garanti de ne fonctionner qu'en O de n étapes.

De manière similaire, nous pouvons voir que la complexité spatiale est O de n, la seule chose que nous avons stockée était vraiment la pile, qui est une structure de données linéaire.

Et nous savons que nous ne allons pas mettre plus de n choses sur la pile.

Donc, dans l'ensemble, nous avons une solution linéaire en temps et en espace pour ce problème de parcours en profondeur d'abord.

D'accord, je pense que nous avons une bonne compréhension de l'approche pour un parcours en profondeur d'abord.

Maintenant, passons à la vidéo de démonstration.

Et nous allons l'implémenter ensemble de quelques manières.

Hey, programmeurs, Alvin ici, n'est-ce pas.

Et je veux passer en revue une solution JavaScript pour ce problème de valeurs de profondeur d'abord.

Et donc, ce que nous allons faire ici, c'est vraiment juste implémenter cette même stratégie que nous avons tracée dans la vidéo d'approche, presque à la lettre.

Et nous allons commencer avec la version itérative.

Et cela signifie, bien sûr, que nous allons résoudre celui-ci de deux manières différentes, n'est-ce pas, nous allons le résoudre de manière itérative d'abord, et ensuite, nous allons passer à la solution récursive.

D'accord, alors plongeons-nous directement ici.

Comme nous l'avons dit, dans la vidéo d'approche, nous savons que la version itérative repose vraiment sur nous créant une pile.

Et pour la plupart de vos langages de programmation, vous pouvez simplement aller de l'avant et utiliser votre structure de données de type tableau pour cela.

Donc, je vais utiliser un simple vieux tableau JavaScript, je vais de l'avant et nommer celui-ci pile.

Et nous pouvons simplement utiliser un tableau pour représenter une pile tant que nous nous en tenons à deux méthodes particulières, n'est-ce pas, je vais utiliser array push, qui ajoute à la fin d'un tableau, et aussi array pop, qui retire de la fin du tableau également.

Donc, je vais considérer la fin de mon tableau pour représenter le haut de ma pile.

Cool, ce que nous allons faire, c'est initialiser la pile avec le nœud racine au sommet.

Bien, puis je peux avoir ma boucle principale pour l'algorithme.

Donc, nous savons que nous devons continuer à exécuter l'algorithme tant qu'il y a des choses sur notre pile.

Donc, je peux simplement vérifier tant que stack dot length est supérieur à zéro.

Donc, tant que j'ai au moins un élément sur ma pile, il y a du travail à faire ici.

Et cela va parcourir une seule itération de cet algorithme, nous savons que nous commençons l'itération en retirant simplement le haut de notre pile, en d'autres termes, stack dot pop en JavaScript, cela va également nous retourner l'élément que nous venons de retirer.

Donc, je vais appeler cela mon nœud actuel const current.

Et cela va être une instance de nœuds, cela va être l'un de ces objets.

Cool.

Donc, maintenant que j'ai retiré cet élément du haut de ma pile, disons pour l'instant, je ne sais pas, je l'imprime, peut-être que nous allons déboguer celui-ci au fur et à mesure.

Donc, console dot log, current dot Val, parce que je sais que chaque instance de nœud a une propriété dot Val à l'intérieur.

Et à partir de là, je dois ajouter les enfants de ce nœud.

Donc, vous pourriez deviner que pour cela, nous pourrions simplement faire stack dot push, je vais pousser l'enfant gauche, un ici, donc node ou current dot left, suivi de l'enfant droit.

Mais nous devons aussi nous assurer que ces enfants existent, n'est-ce pas ? Regardez l'invite.

Il pourrait y avoir des instances, par exemple, comme ce nœud C ici, ce nœud C n'a qu'un enfant droit, mais n'a pas d'enfant gauche, n'est-ce pas.

Donc, ce que je ne veux pas faire, c'est pousser le gauche de C, car cela pousserait null sur ma pile, ce qui me donnerait une erreur plus tard.

N'est-ce pas ? Donc, je veux seulement pousser les enfants s'ils existent.

Et j'ai besoin de vérifier individuellement si le gauche existe et le pousser et aussi si le droit existe et le pousser, je vais juste ajouter quelques instructions de garde pour les deux.

Donc, nous allons de l'avant et insérerons, nous dirons, d'accord, si le courant a un côté gauche et droit, current dot left, appelé justice pour le côté droit, cool, peut-être que nous pouvons l'inclure en ligne, si vous préférez.

D'accord, donc je vais seulement pousser les enfants s'ils existent.

Et cela devrait être le cœur de notre algorithme de profondeur d'abord.

Donc, nous ne mettons pas nos valeurs à l'intérieur d'un tableau comme le problème le demande, mais nous devrions au moins pouvoir voir le bon ordre d'impression ici, parce que je vais imprimer la valeur d'un nœud dès qu'il est retiré de ma pile.

Donc, je vais de l'avant et peut-être apporter un cas de test littéral, donc je pourrais juste voler ce petit stub ici.

Et cela va juste imprimer les valeurs.

D'accord, donc je vais tester cela, je peux appuyer sur Exécuter, si j'appuie sur Exécuter, cela va simplement exécuter ce fichier comme un script.

Donc, cela ne va pas exécuter de cas de test automatique, juste exécuter mon fichier tel quel.

Donc, si vous voulez le tester de cette manière, en quelque sorte de manière manuelle, vous allez devoir vous assurer d'appeler votre fonction.

J'ai une console dot log à l'intérieur.

Donc, je vais juste exécuter cela manuellement.

Et lorsque je le fais, je devrais voir une sortie ici qui ressemble à node is not defined parce que j'ai oublié d'apporter ma définition de classe.

Donc, je vais le faire.

Essayons cela.

D'accord, en regardant notre sortie, nous n'avons pas obtenu notre parcours en profondeur d'abord exact comme nous l'attendions, n'est-ce pas ? J'ai obtenu ACF, B, D, si vous regardez ce que nous avons vraiment imprimé, nous avons techniquement imprimé une impression en profondeur d'abord, mais nous avons favorisé le côté droit.

Donc, nous avons fait a, c, f, et puis B, E, D.

Donc, disons que nous voulions vraiment la version de gauche à droite de cela, et tout ce que vous avez à faire est d'inverser l'ordre dans lequel vous poussez les enfants, n'est-ce pas, cela devrait être clair en regardant ces deux lignes, n'est-ce pas ? Lorsque j'ajoute mes enfants, il semble que je pousse l'enfant gauche, puis l'enfant droit.

Si vous poussez l'enfant gauche en premier, puis vous poussez l'enfant droit ensuite, cela signifie que l'enfant droit va être au sommet pour l'itération suivante.

Donc, si vous le faites comme ceci, cela favorisera le côté droit et le parcourra en premier.

Mais si vous le faisiez comme ceci, maintenant vous parcourriez en fait la branche gauche en premier, vers la droite.

Avec ce petit changement, voyons simplement ce que notre impression donne.

Et nous avons un joli AB de ECF.

Cependant, dans ce problème, ils veulent que nous retournions ces valeurs dans un tableau.

Donc, je peux me débarrasser de ce petit test manuel ici, je n'ai plus besoin de cette définition de classe.

Et maintenant, au lieu de cela, je vais simplement rassembler toutes mes valeurs dans un tableau de résultats.

Donc, je vais dire, peut-être résultat ici commence comme un tableau vide.

Et ensuite, lorsque je retire des éléments du haut de ma pile, au lieu de les logger, je vais de l'avant et faire result dot push, et je vais pousser cette valeur dans le tableau de résultats.

Une fois que j'ai terminé cette boucle while, cela signifie que tout mon arbre a été exploré.

Ce qui signifie que je peux retourner, assurez-vous de bien l'écrire, retourner mes résultats.

Cool.

Donc, cela devrait être une belle solution, cela exécute réellement les cas de test sur cela.

Essayons cela.

Donc, il semble que nous nous en sortions plutôt bien.

Mais pour cet exemple tout à fait dernier, il semble que nous obtenons ne peut pas lire la propriété Val de na, et cela exécute le cas de test 04.

Donc, si vous allez dans l'invite, ces cas de test sont en fait explicitement présentés ici.

Donc, je veux aller à zéro maintenant, regardons le cas de test zéro quatre.

Ils passent ma fonction, non, un type de représentation comme un arbre vide ou un nœud vide.

Et nous pouvons en quelque sorte tracer ce qui se passe ici pour notre code.

Disons que root était null.

Cela signifie que lorsque nous initialisons notre pile, notre pile contient littéralement une valeur nulle.

Donc, ce n'est même pas une instance de note pour l'instant.

Cela signifie que lorsque j'entre dans cette boucle, nous allons vérifier, vous savez, ai-je quelque chose dans ma pile, et j'en ai parce que la longueur de ma pile est un.

Et lorsque je pop, l'élément du haut de ma pile current va être no, puis sur cette ligne 14, il est dit null dot Val.

Et c'est en fait là que notre code explose, à droite sur la ligne 14, n'est-ce pas ? Vous ne pouvez pas référencer la propriété Val, de null.

Et donc pour gérer ce scénario, nous devons nous assurer que nous n'autorisons jamais quoi que ce soit No, à entrer dans la pile.

C'est un peu pourquoi nous avions cette garde ici.

Il pourrait aussi être vrai pour même le niveau supérieur de la route, au cas où ils nous donneraient l'arbre vide.

Cela semble un peu ringard, vous savez, un cas limite.

Mais c'est un cas assez courant, lorsque vous allez réellement à vos entretiens, n'est-ce pas ? Que se passe-t-il si vous avez une entrée vide.

Et donc, je vais simplement le garder explicitement, je vais vérifier, hey, si ma route, donc si tout mon arbre est vide.

Donc, si route est égal à null, alors ce que je vais faire, c'est simplement retourner un tableau vide, n'est-ce pas ? Parce que cela signifie qu'il n'y a pas de valeurs à l'intérieur.

Et c'est en fait la réponse attendue, selon cela, n'est-ce pas, devrait retourner un tableau vide.

Donc, essayons maintenant, cela devrait être plutôt bien.

Bien.

Et nous avons notre belle solution itérative pour ce problème de valeurs de profondeur d'abord.

D'accord, donc voici ce que nous allons faire.

C'était une solution.

Laissez-moi vous montrer une autre façon.

Implémentons cela.

Et ce serait notre version récursive.

Donc, je vais simplement le redéfinir ci-dessous.

Et je recommande vraiment de pratiquer les deux versions, car elles vont servir de base pour résoudre de nombreux problèmes d'arbres différents.

Et donc, lorsque je pense à la version récursive, comme tout notre code récursif, je dois penser au cas le plus simple de mon entrée, et cela agira comme mon cas de base, n'est-ce pas ? Donc, dans le cas d'un arbre binaire, l'arbre le plus simple que vous pouvez recevoir va être l'arbre vide ou juste un nœud racine, n'est-ce pas ? Donc, ce ne sera même pas question d'un nœud qui est un nœud unique à l'intérieur d'un arbre binaire.

Ce sera question d'un arbre vide, n'est-ce pas, un arbre avec zéro nœuds.

Je vais vérifier si ma racine est nulle, et j'ai un arbre vide.

Et je pense à ce cas de base, comme s'il s'agissait de sa propre entrée, parce que c'est vraiment le cas, n'est-ce pas, et donc si quelqu'un vous demandait de lui retourner un tableau de toutes les valeurs dans l'arbre vide, il serait toujours question que cela doit être un tableau vide, n'est-ce pas ? Parce qu'il n'y a pas de valeurs, il n'y a même pas de nœuds dans l'arbre vide.

Et à partir de là, je peux générer mon appel récursif réel, n'est-ce pas.

Et je sais ce que j'appelle mes trucs récursivement.

Cela signifie que je dois référencer une fonction et encore, aller de l'avant et l'invoquer.

Et je vais appeler route dot left, ainsi que route dot, right ? Cela ferait, cet appel ici me donnerait un tableau contenant toutes les valeurs dans le sous-arbre de gauche.

Et cela me donnerait un tableau de toutes les valeurs dans le sous-arbre de droite.

Et donc, disons que je vois ces valeurs dans leurs propres variables respectivement, vous n'avez pas à faire cette partie.

Mais je suis un peu fan de cela, surtout si c'est la première fois que vous l'implémentez.

Donc, je vais appeler cela mes valeurs de gauche.

Je vais appeler celle-ci mes valeurs de droite.

Et voici comment je peux créer rapidement des codes récursifs, il s'agit de faire un saut de foi récursif ici.

Donc, disons que nous parcourons le test 00.

Et donc, c'est notre arbre visuel, n'est-ce pas ? Donc, nous savons que notre racine va être un nœud.

Donc, lorsque je fais cet appel de niveau supérieur, ce cas de base ne se déclenche pas.

Et donc, je fais mes appels récursifs, n'est-ce pas ? Je sais que lorsque je fais depth first value, ou values, plutôt, laissez-moi corriger cela depth first values de root dot left, cela signifie que je vais passer dans le nœud B, n'est-ce pas, et voici comment je dois prétendre que mon code se comporte, je vais simplement obtenir le bon résultat de cet appel, n'est-ce pas ? Donc, si je passais le nœud B dans cet appel, ce que j'attends en retour, c'est le tableau complet représentant le parcours en profondeur d'abord de ce sous-arbre, en commençant par B, n'est-ce pas.

Donc, si j'avais des données correctes ici, à quoi cela ressemblerait, ce serait juste B, D, et E.

Cela serait en fait le parcours en profondeur d'abord complet, à partir de ce sous-arbre, n'est-ce pas.

Et ce serait une histoire similaire pour mon appel de droite, n'est-ce pas ? Si je suis à A, donc A est toujours ma racine, et je passe mon enfant droit C, à cet appel, ce que j'attends en retour, c'est juste un tableau de CF, qui serait le parcours en profondeur d'abord de ce sous-arbre de gauche.

Et maintenant que j'ai, vous savez, mes valeurs de sous-arbre de gauche et mes valeurs de sous-arbre de droite, je dois réfléchir à la façon de tout combiner, n'est-ce pas ? Comment puis-je m'intégrer dans cette sortie en combinant les deux résultats de mes enfants, n'est-ce pas, ce que je dois faire, c'est simplement me prendre, me mettre dans le tableau, suivi de mes enfants de gauche, suivi de mes enfants de droite.

Donc, je peux faire une belle syntaxe JavaScript pour cela chaque fois que je retourne le droit lorsque je me jette là-dedans, donc je vais jeter un root dot Val, c'est moi.

Donc, ce serait comme le nœud a que je prends simplement toutes les valeurs dans mon résultat de gauche, je les mets ici et j'utilise simplement l'opérateur de propagation pour déballer ce tableau.

Et je ferai la même chose pour les valeurs de droite de CF, n'est-ce pas.

Donc, dot dot, dot, spread out right values juste pour que je retourne un seul tableau, et ce motif lui-même correspond à cette sortie, n'est-ce pas, en faisant un peu un saut de foi et en supposant la justesse de ces appels récursifs ici, n'est-ce pas, j'ai un, et je substitue B, D, E, et puis pour la droite, j'ai CF.

Et même avant de l'exécuter, je ne vais pas, vous savez, supposer trop de connaissances JavaScript.

Donc, peut-être que vous êtes un peu nouveau dans cet opérateur de propagation.

Donc, en général, un rapide à part ici, disons que j'avais un tableau de certaines choses.

Donc, je vais dire, peeps là et quelques personnes ici.

Donc, nous allons lancer fleabay, nous allons lancer Jason, lancer Raj, lancer heavy.

Et ce que je peux faire, c'est chaque fois que j'ai un tableau, je peux simplement utiliser un opérateur de propagation pour déballer ce tableau.

Donc, par exemple, je peux dire const, nous allons dire new peeps.

Et je vais créer un nouveau tableau littéral.

Donc, chaque fois que je dis des crochets, cela me donne un nouveau tableau littéral.

Et ce que je vais faire, je ne sais pas, mettre un élément au début, nous allons l'appeler Alvin.

Cela va étaler les éléments de peeps, n'est-ce pas ? Donc, imaginez simplement que j'ai pris tous les éléments ici et que j'ai simplement retiré les crochets.

De cette façon, je n'ajoute aucune imbrication initiale.

Et puis à la fin, je ne sais pas, je peux ajouter quelqu'un d'autre.

Comme, n'est-ce pas ? Eh bien, console dot log, à quoi ressemble new peeps, donc je ne vais pas exécuter les cas de test, nous allons simplement exécuter ce fichier comme un script, juste pour que nous puissions passer en revue cet indice de propagation.

Donc, si je donne un coup de pouce, nous faisons un peu plus grand.

Remarquez que j'ai correctement étalé les choses, n'est-ce pas ? J'ai Alvin au début, et j'ai toutes les choses de peeps au milieu, n'est-ce pas, suivi de Brian à la fin.

Donc, vous pouvez faire cela.

Vous pouvez également utiliser la méthode concat sur les tableaux.

Vous allez probablement me voir utiliser cette syntaxe de propagation beaucoup parce que je suis un peu fan, n'est-ce pas.

Mais avec cela à l'esprit, allons-y et testons réellement ce code.

Donc, nous allons exécuter tous les cas de test.

Bien.

Et voici une autre solution fonctionnelle pour nos valeurs de profondeur d'abord.

Et cela devrait être assez naturel que nous pouvons résoudre ce problème également de manière récursive.

Donc, je sais que la solution itérative pour ce parcours en profondeur d'abord nécessite une structure de données de pile.

Et je sais que lorsque j'écris du code récursif, sous le capot, votre langage de programmation va en fait suivre tous ces appels récursifs, en utilisant la pile d'appels, n'est-ce pas ? Ce comportement de la pile d'appels vous donne le même type d'ordre, ce qui est vraiment pratique.

Cool.

D'accord.

Donc, avant de vous envoyer au problème suivant, je veux que vous pratiquiez les deux solutions pour ce code de valeurs de profondeur d'abord, il va être très nécessaire de maîtriser certains concepts ultérieurs qui arrivent bientôt.

Donc, passez du temps sur cette pratique rend parfait, n'est-ce pas, et je vous rattraperai dans le prochain.

Hey, programmeurs, Alan ici, n'est-ce pas ? Maintenant, je veux passer en revue ce problème de valeurs de largeur d'abord.

Donc, ce sera vraiment juste une petite variation de celui de profondeur d'abord que nous venons de faire, bien sûr, mais il est vraiment important que, pour l'avenir, pour tous nos algorithmes d'arbres et autres structures de données, que nous maîtrisions les deux versions.

Donc, dans ce problème, nous allons prendre un arbre binaire, encore une fois, une structure d'arbre binaire très classique, cette fois, je veux retourner un tableau ou une liste de toutes les valeurs selon un ordre de parcours en largeur d'abord.

Donc, un parcours en largeur d'abord commence avec le nœud racine de a, donc ce n'est rien de nouveau.

Et à partir de là, je pourrais aller à B.

Donc, pour l'instant, j'ai mon nœud a, et aussi mon nœud B.

Et voici où nous divergeons de notre problème précédent dans un parcours en largeur d'abord.

Et la largeur fait simplement référence à la largeur de quelque chose, je voyage à travers avant d'aller plus profondément.

Donc, dans notre parcours en largeur d'abord, je vais me déplacer vers C et pas vers D pour l'instant.

Donc, j'ajoute la valeur de mon nœud C à ma liste.

Et à partir de là, une fois que j'ai terminé ce niveau entier, et qu'il n'y a plus d'endroits où aller à travers l'arbre, maintenant je peux descendre au niveau suivant.

Maintenant, j'ai D, puis E, puis F.

Donc, il y a une distinction vraiment importante ici, le parcours en largeur d'abord commence avec ABC, alors que le parcours en profondeur d'abord aurait commencé A, B, D.

C'est une distinction vraiment, vraiment importante.

Et donc, comment pouvons-nous nous y prendre pour implémenter la version en largeur d'abord de ceci ? Eh bien, rappelez-vous que la profondeur d'abord utilisait une structure de données de pile, eh bien, est-ce le cas que la largeur d'abord va maintenant utiliser la structure de données de file d'attente, vraiment juste la version partenaire de cette structure.

Et donc, passons en revue cela de manière plus programmatique.

Donc, je vais utiliser et suivre ma file d'attente.

Et rappelez-vous simplement qu'une file d'attente n'a pas de sens de direction, elle a le dos de ma file d'attente et le devant de ma file d'attente, les choses entrent à l'arrière de la file d'attente, et elles sortent par le devant de la file d'attente.

D'accord.

Et donc, personne ne saute la ligne non plus.

Cela me donne un bel ordre équitable, pensez à une file d'attente comme simplement attendre en ligne à la caisse d'une épicerie ou quelque chose.

Donc, comment je commence mon algorithme, je vais commencer par initialiser ma file d'attente avec le nœud racine.

Donc, je vais simplement commencer avec un a sur ma file d'attente.

Et à partir de là, maintenant je peux commencer mon algorithme principal.

Donc, mon algorithme principal devrait vérifier à chaque itération si ma file d'attente est vide, pour l'instant elle ne l'est pas parce que j'ai au moins un élément.

Et donc je retire l'élément de devant de ma file d'attente.

Et donc nous savons que a serait retiré, et nous l'étiquetons comme notre courant.

Un nœud étant exploré lorsqu'une chose quitte la file d'attente et est marquée comme notre courant, nous dirons que maintenant il est visité.

Donc, je l'ajouterais à la liste en cours de mes valeurs.

Ensuite, à partir de là, je dois regarder ses enfants.

Il a deux enfants B et C, je dois aller de l'avant et les ajouter dans ma file d'attente.

Et donc, disons que j'ai ajouté B dans la file d'attente en premier, suivi de C.

Remarquez que C doit entrer derrière B, n'est-ce pas.

Et maintenant j'ai terminé cette itération.

À ce stade, j'ai l'itération suivante de mon algorithme, je prends l'élément de devant de ma file d'attente, et il part, n'est-ce pas ? Donc b est maintenant mon courant, j'ajoute B à ma liste en cours, puis je regarde les enfants de B de D, je pousse D suivi de he derrière.

À ce stade, j'ai une autre itération à faire, n'est-ce pas.

Et ainsi de suite.

À partir de là, c'est parti de l'avant de ma file d'attente, je l'ajoute à ma liste de valeurs, et je regarde les enfants de c, c n'a qu'un seul enfant.

Donc pour cet enfant qui existe, je vais de l'avant et je les ajoute à l'arrière de ma file d'attente.

Et il est vraiment important que je les ajoute à l'arrière, n'est-ce pas ? À ce stade, j'avais ma prochaine itération.

À ce stade, je continue, ma file d'attente n'est toujours pas vide, donc j'ai encore des choses à retirer.

Donc D quitte le devant de ma file d'attente, je l'ajoute à ma liste de valeurs.

Puisque D n'a pas d'enfants, il n'y a rien à ajouter ici.

Prochaine itération, il quitte le devant de ma file d'attente, je l'ajoute à ma liste de valeurs, pas d'enfants, donc je n'ai pas besoin d'ajouter quoi que ce soit.

Et enfin, f quitte le devant de ma file d'attente, je l'ajoute simplement à ma liste de valeurs et encore, f n'a pas d'enfants.

Donc, maintenant ma file d'attente est vide, ce qui doit signifier que, hé, j'ai dû compléter l'algorithme, n'est-ce pas ? Il n'y a plus de nœuds à explorer, j'ai exploré et ajouté chaque nœud à ma liste de valeurs.

D'accord, et cette sortie semble correcte, n'est-ce pas, j'obtiens abcdef, comme nous le disons.

Mais qu'en est-il de la complexité de cet algorithme.

Donc, regardons de plus près ici.

Eh bien, nous savons dès le départ, que n va être le nombre de nœuds dans cet arbre binaire.

Donc, ce sera le terme pour nos côtés d'entrée.

Et nous pouvons dire que la complexité temporelle est simplement O de n, environ, parce que nous savons que lorsque cela concerne la visite de ces nœuds, et vous savez, l'utilisation de notre boucle, nous allons ajouter chaque nœud à la file d'attente une fois, ce qui signifie également que ce nœud va quitter la file d'attente une fois, donc ce n'est pas comme si nous ajoutions deux fois un nœud à la file d'attente, n'est-ce pas, nous n'allons pas visiter deux fois l'un de ceux-ci.

De manière similaire, la complexité spatiale va être O de n au plus, parce que, vous savez, nous allons simplement ajouter au plus tous les nœuds dans notre file d'attente.

Et en général, cela va probablement être moins que O, un événement d'espace en termes de combien d'espace nous utilisons dans notre file d'attente.

Une chose importante que je vais simplement mentionner maintenant en ce qui concerne la complexité temporelle de celui-ci, ici, nous allons dire que la complexité temporelle est O de n.

Et c'est si nous pouvons supposer que l'ajout de quelque chose maintenant à la file d'attente s'exécute en temps constant.

Et le retrait de quelque chose de la file d'attente se produit en temps constant.

Donc, selon la façon dont vous l'implémentez, si vous utilisez en fait, une structure de données de file d'attente intégrée et efficace, vous obtiendrez cette complexité temporelle O de n pour notre largeur d'abord.

Mais si vous utilisez une structure de données moins optimale, comme une structure de données, peut-être pas une file d'attente parfaite, alors vous pourriez avoir une complexité réelle pire.

Donc, encore une fois, cette complexité temporelle de O de n suppose que nous avons une file d'attente maximement efficace qui a des opérations d'ajout et de retrait en o de un.

Cela dit, je me sens plutôt bien à coder celui-ci.

Je vous attrape dans la vidéo de démonstration, et je vous montrerai quelques façons différentes de l'implémenter.

Hey, programmeurs, Alvin ici, n'est-ce pas ? Maintenant, je veux passer en revue la solution JavaScript pour cette fonction de valeurs de largeur d'abord.

Donc, espérons que vous venez de terminer la version de profondeur d'abord, auquel cas, celle-ci devrait être une promenade de santé.

Mais bien sûr, nous allons quand même passer par les mouvements, car cela va être utile pour résoudre des problèmes beaucoup plus difficiles plus tard, comme vous m'entendez toujours dire, d'accord, donc pour aborder celui-ci, nous allons commencer avec notre structure de données de file d'attente, n'est-ce pas ? Rien de fantaisiste en JavaScript, ce que je ferais, c'est simplement utiliser un tableau et m'en tenir à utiliser des méthodes très spécifiques, n'est-ce pas ? Donc, je vais créer un tableau, je l'appellerai ma cube.

Et nous allons initialiser cette file d'attente avec la route par défaut.

Et nous allons également nous protéger contre l'avant, imaginez qu'ils nous donnent un arbre vide pour commencer.

Donc, en d'autres termes, la route initiale est non, ce qui serait comme ce test 04.

Et ils veulent simplement que nous retournions un tableau vide.

Donc, je vais me protéger explicitement contre cela.

Donc, je vais vérifier, hey, est-ce que ma route est non.

Et si c'est le cas, allez-y et retournez un tableau vide comme ça.

Bien.

Ensuite, à partir de là, je dois commencer dans ma boucle principale de l'algorithme.

Donc, j'itère tant que ma file d'attente n'est pas vide, comme nous en avons parlé dans la vidéo d'approche, n'est-ce pas ? Donc, tant que q dot length est supérieur à zéro, continuez.

Maintenant, je commence une seule itération de cet algorithme en retirant simplement le devant de ma file d'attente, n'est-ce pas ? Donc, c'est vraiment à vous de choisir les méthodes que vous utilisez, vous devez simplement vous assurer de retirer d'une extrémité et d'ajouter à l'extrémité opposée.

Donc, pour moi, je vais traiter l'index zéro comme s'il était le devant de mon tableau, je vais traiter le dernier index comme s'il était l'arrière de mon tableau, n'est-ce pas ? Donc, si je veux retirer le devant et dire, array dot shift, ou pour moi maintenant, Q dot shift, cela retire le devant et me le retourne également, donc je vais appeler cela mon nœud actuel, x.

Et à partir de là, je dois ajouter les enfants de ce nœud dans ma file d'attente.

Et cela me donnera mon flux principal pour ce parcours en largeur d'abord.

D'accord.

Donc, je vais de l'avant et vérifier, hey, si mon enfant gauche existe, donc si, disons current dot left, qui n'est pas égal à no, alors ce que je devrais faire, c'est aller de l'avant et le pousser dans ma file d'attente.

Donc, je vais dire q dot push mon current dot left, et ce sera symétrique pour le côté droit, bien sûr.

Donc, si le droit existe, alors poussez le droit dans la file d'attente.

Comme ça.

Génial.

Et donc, cela semble assez bien.

Et à partir de là, je veux en fait stocker les nœuds que je visite dans un tableau pour le retour final, comme le problème le demande, donc rien de trop fantaisiste.

Je veux vraiment insérer un peu de code ici et donc je vais créer un tableau de résultats, je vais l'appeler valeurs, un peu vide lorsque quelque chose quitte la file d'attente.

Je vais simplement prendre cela et le pousser dans mes valeurs.

Donc, je dis valeurs dot push.

Je vais pousser cette valeur actuelle dans ma file d'attente.

Et notez que, ce que vous ne pouvez pas faire, c'est simplement prendre comme la file d'attente et la traiter comme votre valeur de retour finale, cela doit être une chose totalement séparée, n'est-ce pas, j'utilise la file d'attente juste pour le bien de voyager à travers dans un ordre de largeur d'abord.

Et l'ordre que vous visitez est en fait dérivé de l'ordre dans lequel les choses quittent la file d'attente.

Donc, c'est pourquoi je le fais ici, n'est-ce pas, dès qu'une chose quitte une file d'attente, c'est ce que je considère comme visité.

Donc, je l'ai ajouté à ma liste de valeurs.

Bien.

Et après que mon while ait fini de s'exécuter, je vais de l'avant et retourner mon tableau de valeurs entier.

Donc, je vais tester cela.

Je vais exécuter tous les cas de test, ce que nous obtenons, nous avons quelques cas de test à passer.

Et nous y voilà.

Voici une belle solution itérative pour notre parcours en largeur d'abord.

Juste quelque chose que je veux mentionner, en passant, regardons l'invite.

Donc, en regardant, je ne sais pas, comme le tout premier exemple, dans cette sorte de rendition de largeur d'abord, ce qu'ils nous demandent de faire, c'est vraiment de nous donner un parcours en largeur d'abord, qui se déplace de gauche à droite, donc remarquez qu'il va A, B, C en termes de sortie résultante, et non a CB, n'est-ce pas, ceux-ci seraient tous les deux techniquement corrects, commencez à une largeur d'abord.

Et puis vous pouvez choisir en fonction du problème que vous résolvez, si vous voulez aller de gauche à droite ou de droite à gauche.

Pour moi, parce que je pousse le gauche suivi du droit, cela signifie que le gauche va quitter la file d'attente en premier, n'est-ce pas, parce que rappelez-vous, la file d'attente est comme une ligne et une caisse.

Donc, si quelqu'un entre en premier, c'est-à-dire que le gauche entre en premier, ils vont être servis avant que le droit ne parte.

Et vous pouvez simplement les inverser.

Et je vous donnerai le but universel de droite à gauche.

Donc, selon ce que votre problème garantit, vous pouvez toujours manipuler un peu ce code.

Et c'est en fait probablement comme la seule solution que vous pouvez avoir.

Vous savez, peut-être à part quelques changements superficiels comme le style de code, cela va être votre solution de référence et votre seule solution pour un parcours en largeur d'abord sur un arbre binaire, n'est-ce pas ? Une erreur courante que je vois les gens essayer de faire beaucoup, c'est qu'il n'y a pas vraiment de moyen simple d'implémenter un parcours en largeur d'abord de manière récursive.

Et cela devrait avoir du sens, car un parcours en largeur d'abord a besoin d'un ordre de file d'attente, il a besoin d'utiliser une file d'attente.

Si vous écrivez un code récursif, vous savez, sous le capot, il utilise une pile.

Et donc cette pile contre file d'attente va vraiment vous combattre.

Et vous allez avoir un temps vraiment difficile à essayer d'implémenter le bon ordre.

Donc, écrivez toujours la version itérative pour votre parcours en largeur d'abord.

D'accord, donc je recommande avant de sauter dans la vidéo suivante, assurez-vous de pouvoir écrire ce code par vous-même, car nous allons augmenter un peu la difficulté, mais je vous attraperai dans la prochaine.

Hey programmeurs, Alvin ici, n'est-ce pas ? Maintenant, je veux passer en revue l'approche pour ce problème d'inclusion d'arbre.

Donc, le principe de ce problème est que je vais vous donner un arbre binaire, et aussi une valeur cible à rechercher.

Je veux simplement que vous me disiez Vrai ou Faux ? Cette valeur cible est-elle trouvée dans l'arbre binaire ? Donc pour cet exemple d'entrée particulier, la réponse est évidemment vrai ou Oui, n'est-ce pas, vous pourriez définitivement trouver e dans cet arbre binaire pour vous donner une autre valeur cible comme j, vous répondriez avec faux, n'est-ce pas ? Parce que cette valeur j est introuvable dans l'arbre binaire.

Et vraiment, ce que je vous demande de faire ici, c'est que nous passons en revue les recherches en largeur d'abord et en profondeur d'abord canoniques.

Et je pense que je vais passer en revue les deux approches pour vous maintenant.

Donc, disons que je testais ou que je voulais plutôt tracer l'entrée où la cible était IE, comment puis-je m'y prendre pour attaquer celui-ci, n'est-ce pas ? Nous savons que dans la plupart de ces problèmes, lorsqu'ils vous donnent un arbre binaire en entrée, ils ne vont vous donner que la racine.

Mais cela dit, si vous avez accès au nœud racine, alors vous savez que vous avez accès à tous les nœuds qui composent l'arbre, n'est-ce pas.

Donc, ce que je peux faire, c'est simplement effectuer l'un de mes algorithmes de parcours.

Donc, peut-être pour commencer.

Maintenant, faisons soit la recherche en largeur d'abord ou la recherche en profondeur d'abord de style itératif.

Donc, je pense que pour cette trace, je vais m'en tenir à la version en largeur d'abord, ce qui signifie que nous allons utiliser une file d'attente, n'est-ce pas ? Donc, lorsque nous traçons cela, je pense à cela de manière itérative.

Pour l'instant, espérons que vous vous souvenez de nos problèmes précédents, lorsqu'il s'agit de votre parcours en largeur d'abord, vous commencez avec votre nœud racine sur votre file d'attente.

Et lorsqu'une chose quitte la file d'attente, vous la marquez comme votre courant, n'est-ce pas.

Et voici où je travaille dans la nouvelle logique pour ce problème particulier.

Lorsque quelque chose quitte le devant de ma file d'attente, je vais vérifier, hey, est-ce que cette valeur actuelle est la même que ma valeur cible, donc est-ce que a est la même que E.

Ce n'est pas.

Donc, je n'ai pas trouvé la chose que je cherche, n'est-ce pas ? Et ce que je peux faire, c'est maintenant considérer ses enfants.

N'est-ce pas ? Donc, je regarde ses enfants.

Ils existent tous les deux, je les ajoute à la file d'attente.

Donc, je mettrais b dans ma file d'attente, j'ajouterais c dans ma file d'attente.

Et maintenant, je passe à mon itération suivante, n'est-ce pas ? L'élément de devant B quitte la file d'attente, et je dois vérifier, hey, est-ce que B est ma cible, ce n'est pas ma cible t.

Donc, je continue à courir, je regarde les enfants de B.

Donc, je prends ce D et je l'ajoute, je prends le E et je l'ajoute aussi.

Et ce processus continue simplement, c'est parti du devant de ma file d'attente, est-ce que c'est ma cible, ce n'est pas.

Donc, continuez, j'ajouterais les enfants de c à ma file d'attente.

Donc, je viens d'ajouter F à ma file d'attente.

Et ce processus continue.

Et donc, d quitte le devant de ma file d'attente, je vérifie si d est ma cible, ce n'est pas, et D n'a pas d'enfants à ajouter, n'est-ce pas ? Rappelez-vous que dans notre parcours en largeur d'abord, je n'ajoute les enfants que s'ils existent, car je ne veux pas ajouter de pointeurs nuls dans ma file d'attente.

Et donc, je continue simplement mon algorithme, n'est-ce pas ? J'ai encore des choses dans ma file d'attente à vérifier.

Et enfin, quand il quitte le devant de ma file d'attente, je vérifie si c'est ma cible.

Et en effet, c'est le cas, à ce stade, je viens de confirmer que he est trouvé à l'intérieur de mon arbre binaire.

Donc, ce que je peux faire, c'est simplement mettre fin à mon algorithme en retournant la valeur vraie, n'est-ce pas ? Il n'y a pas de point à regarder le reste de l'arbre, car j'ai déjà découvert que, hey, ma valeur cible est effectivement dans l'arbre.

N'est-ce pas ? Une chose que vous pourriez remarquer, c'est qu'il semble que je n'ai vérifié pour IE qu'une fois qu'il a quitté le devant de ma file d'attente, et non lorsqu'il a été initialement ajouté à ma file d'attente.

Techniquement, vous auriez pu retourner tôt lorsque vous l'avez ajouté à la file d'attente.

Mais nous allons voir lorsque je vais passer en revue le code complet pour celui-ci, cela se terminerait avec un code plus propre si vous vérifiiez simplement votre valeur cible lorsque quelque chose quitte votre file d'attente.

Donc, nous allons voir cela lorsque nous passerons en revue le code.

C'est juste un petit détail d'implémentation.

Cela dit, pour cette stratégie itérative de largeur d'abord, que pouvons-nous dire de la complexité ? Eh bien, si nous définissons n comme le nombre de nœuds, alors nous savons que la complexité temporelle est simplement O de n, c'est vraiment juste un parcours en largeur d'abord classique.

Donc, les nœuds vont entrer dans la file d'attente une fois et quitter la file d'attente une fois, c'est ouvert, n'est-ce pas.

Et encore une fois, cela en supposant que nous utilisons une file d'attente efficace, n'est-ce pas, où nos opérations d'ajout et de retrait de file d'attente s'exécutent en O de un temps constant.

Donc, nous avons un temps linéaire.

Et pour la complexité spatiale, elle sera également O de n linéaire, n'est-ce pas ? Parce que nous allons simplement stocker nos nœuds dans la file d'attente.

Et donc, nous venons de regarder l'approche pour une belle solution itérative de largeur d'abord, non pas pour ce problème, mais je veux vous montrer la version de profondeur d'abord, et la version de profondeur d'abord, ce serait récursive, n'est-ce pas ? Donc, évidemment, vous pourriez écrire la solution itérative de la dette par personne, auquel cas vous utilisez simplement le même code dont nous venons de parler, mais vous utilisez simplement une pile au lieu de la file d'attente.

Mais essayons de résoudre celui-ci.

De manière récursive, n'est-ce pas.

Et la raison pour laquelle je pense qu'il est vraiment important de s'exposer à la récursivité comme celle-ci, c'est que, lorsque nous passons à des sujets plus complexes, vous allez trouver ce style de récursivité.

Très, très utile, n'est-ce pas ? Donc, nous avons la même entrée, n'est-ce pas ? Disons que ma cible est E, et j'ai le même arbre binaire.

Et maintenant, je veux vérifier de manière récursive si E est dans cet arbre ? Et donc, comment commençons-nous à attaquer cela ? Eh bien, nous allons devoir penser à nos cas de base, n'est-ce pas ? Donc, nous allons avoir vraiment deux types de cas de base, nous aurons comme le cas de base affirmatif, ce qui signifie Hey, nous avons trouvé une correspondance.

Et donc, chaque fois que je rencontre un nœud dont la valeur est he, ou dont la valeur correspond à ma cible, alors je vais faire en sorte que ce nœud ou cet appel récursif retourne vrai, n'est-ce pas ? Donc, c'est mon cas de base affirmatif.

Donc, je vais simplement brancher cette valeur de retour visuellement dans mon arbre, vous savez que ce nœud II va retourner vrai.

Et maintenant, je vais penser à mon cas de base négatif, n'est-ce pas ? Quatre fois où j'appelle un nœud vide, ou le nœud nul, je devrais retourner faux.

Et rappelez-vous de nos conférences précédentes, nous avons dit que nous allons parfois représenter explicitement nos nœuds nuls.

Donc, je vais remplir ceux-ci, par exemple, le nœud C dans mon image aurait un enfant gauche qui est nul.

Donc, je vais dessiner celui-ci explicitement.

Et je sais qu'un nœud comme celui-ci va retourner faux.

Parce que logiquement, je ne devrais pas être capable de penser à tous mes appels récursifs comme s'ils étaient leurs propres sous-problèmes.

N'est-ce pas ? Donc, si quelqu'un me demandait, Hey, pouvez-vous trouver cette valeur E dans un arbre vide ? N'est-ce pas ? Un nœud nul représente un arbre vide ? La réponse serait non, je ne peux pas trouver la valeur dans un arbre vide, car il n'y a rien là.

Et donc, à partir de là, je vais également dessiner explicitement tous ces nœuds nuls similaires, ces pointeurs nuls, n'est-ce pas ? Donc, cela ressemble à ceci.

Remarquez que, à partir du nœud E, je n'ai pas besoin de lui donner un gauche et un droit nuls, car j'ai déjà dit que ce nœud allait retourner vrai, n'est-ce pas ? C'est pourquoi je dessine mon arbre comme ceci.

Et j'ai toutes ces valeurs de retour fausses.

Cool.

Donc, nous venons d'étiqueter tous les cas de base, n'est-ce pas, comme les feuilles de notre arbre, et rappelez-vous qu'une feuille est simplement un nœud sans enfants, n'est-ce pas ? Et à partir de là, comment puis-je combiner toutes ces valeurs booléennes pour obtenir le vrai tout en haut, je sais que pour mon appel de niveau supérieur, qui est au nœud a, ou l'appel récursif a, j'ai besoin de récupérer cette valeur de vrai, n'est-ce pas ? Et la logique que nous devrions utiliser est vraiment juste le OU logique, donc comment cela fonctionne-t-il.

Donc, commençons à évaluer nos valeurs de retour et à les combiner au parent.

Donc, cela devrait être un motif quelque peu similaire au problème de somme d'arbre que je vous ai montré.

Et donc, ce que vous pourriez faire, c'est vous concentrer sur ce nœud D ici, ce nœud a des valeurs prêtes à gauche et à droite, et à droite, il a deux faux.

Et lorsqu'il obtient réellement ces faux qui lui sont retournés, il devrait simplement faire le OU logique, donc il fait faux ou faux, ce qui évalue à faux, n'est-ce pas ? Ce qui signifie que hey, dans ce sous-arbre enraciné en D, je ne peux pas trouver la valeur, ce qui a du sens.

C'est pourquoi c'est faux.

Je vais continuer ce processus.

Si je regarde ce nœud B, maintenant ce nœud B a des valeurs prêtes à gauche et à droite.

Et ils vont remonter un peu.

Et je prends l'ordre d'eux, donc je fais faux ou vrai, ce qui évalue à vrai.

Et ce processus continue partout dans l'arbre, n'est-ce pas ? Donc, à ce nœud f, faux ou faux, c'est moi faux.

Au nœud C, faux ou faux me donne faux.

Enfin, au niveau supérieur de la racine A, je fais vrai ou faux, ce qui me donne un vrai final, ce qui est effectivement la bonne réponse.

Donc, espérons que vous réalisez à quel point la solution est similaire à notre problème précédent de somme d'arbre, n'est-ce pas ? Dans le problème de somme d'arbre, j'ai combiné mes valeurs de retour gauche et droite en faisant l'addition arithmétique.

Mais cette fois-ci, je dois simplement utiliser l'opération booléenne de ou, n'est-ce pas ? Donc, en ajustant simplement le type en booléen, nous avons une solution très élégante, bravo à George Boole.

Et donc, avec cela, je pense que nous allons de l'avant et implémenter cela dans un peu de code, et je vous le montrerai en utilisant la saveur de l'intérêt ou en utilisant peut-être un souffle pour nous, et aussi la version récursive, qui est ma préférée personnelle, en utilisant cette structure d'arbre récursive.

Hey, programmeurs, bienvenue.

D'accord, et je veux passer en revue une solution JavaScript pour ce problème d'inclusion d'arbre, n'est-ce pas ? Eh bien, résolvons cela à la fois en profondeur d'abord, et aussi en largeur d'abord.

Et je pense que nous allons commencer avec la version itérative en largeur d'abord.

Et donc, ce sera vraiment juste l'implémentation de l'algorithme classique de recherche en largeur d'abord, je vais simplement poser mon code classique de parcours en largeur d'abord, puis ajouter une logique conditionnelle ensuite, n'est-ce pas ? Vous devriez être familier avec cela maintenant.

Mais pour mon parcours en largeur d'abord, je vais utiliser une cube.

Donc, je vais dire const, q est égal à un tableau vide, vraiment un tableau avec la route jetée à l'intérieur.

Et à partir de là, vous avez besoin de votre algorithme principal, n'est-ce pas, donc je boucle tant que ma file d'attente n'est pas vide.

Donc, tant que la longueur de la file d'attente est plus grande que zéro, et continuez.

Et sur une seule itération de ce parcours, ce que je fais, c'est q dot shift, donc je retire du devant de ma file d'attente, le devant de mon tableau, je retire le premier élément.

Et je vais sauvegarder cela dans une variable appelée current.

Donc, ce sera juste une instance de nœud.

Et pour l'instant, pourquoi ne pas simplement construire ma solution lentement, je vais simplement, je ne sais pas, console dot log, ce que current dot Val est.

Mais une fois que j'ai considéré ce nœud, ce que je veux faire, c'est vraiment ajouter ses enfants dans ma file d'attente seulement s'ils existent, n'est-ce pas ? Donc, en général, je vais écrire comme q dot push, je vais ajouter à l'arrière de ma file d'attente, donc j'obtiens un bel ordre de file d'attente, je pousse l'enfant gauche, donc current left, de même, l'enfant droit.

Mais imaginez que j'ai un nœud asymétrique ou juste un nœud feuille, n'est-ce pas ? Quelque chose comme C n'aurait qu'un enfant droit, donc son gauche serait non.

Donc, si current est c, alors je pousserais non dans ma file d'attente comme le gauche, ce qui n'est pas bon, n'est-ce pas.

Et donc, je dois me protéger ici et ne pousser les enfants que s'ils existent.

Donc, quelque chose comme ceci, hey, si le courant a ce, correspondant à gauche et à droite, alors je peux aller de l'avant et le pousser.

Donc, cela semble assez bien.

Et cela devrait être la partie principale du code de parcours.

Donc, je vais simplement le tester manuellement.

Donc, très manuellement, donc peut-être juste cet appel, donc je ne vais pas retourner de booléens pour l'instant.

Nous allons construire jusqu'à cela.

Mais je devrais au moins voir mes valeurs imprimées.

Si je fais un test manuel, je vais apporter ma classe de nœud, je devrais voir les valeurs imprimées dans un ordre de largeur d'abord correct, ce qui signifie A, B, C, D, E, F, rappelez-vous que le parcours en largeur d'abord traverse notre arbre avant d'aller plus bas, donc je dois finir un niveau avant de voyager au niveau suivant.

Donc, exécutons simplement cela manuellement comme un script.

Voyons ce que nous obtenons ici.

A, B, C, D, E, F, bien, donc j'obtiens le bon ordre de parcours.

Et maintenant, je peux travailler dans la logique conditionnelle, car ils veulent que nous retournions des booléens ici.

Donc, des choses assez simples.

Nous allons vérifier une fois que quelque chose quitte la file d'attente.

Je peux vérifier si la valeur du nœud actuel est égale à ma cible, alors j'ai trouvé la chose que je cherche.

Donc, retournez simplement vrai, n'est-ce pas, vous avez terminé, vous n'avez pas besoin de parcourir le reste de l'arbre car vous pouvez retourner vrai.

Mais d'un autre côté, si ma valeur actuelle n'est pas la valeur cible, alors je dois continuer à chercher dans le reste de l'arbre, n'est-ce pas.

Donc, si j'ai terminé toute la boucle while, cela signifie que j'ai parcouru tout l'arbre.

Et je n'ai jamais trouvé la chose que je cherche, je devrais retourner faux.

Donc, j'ai besoin d'un retour tardif faux ici ou d'une erreur courante que les gens ont tendance à faire, c'est ce que vous ne voulez pas faire, c'est simplement faire comme, sinon retourner faux ici.

Donc, cela va être faux.

N'est-ce pas ? Parce que cela ne vérifierait que le premier nœud, normalement vérifier la racine, puis vérifier si la racine n'est pas égale à la valeur.

Si ce n'est pas le cas, vous retournez simplement faux, ce qui n'est pas vraiment utile, car cela pourrait être ailleurs dans l'arbre.

Donc, vous allez avoir besoin de ce modèle de retour faux tardif ici.

Mais avec cela, je pense que nous allons passer certains des cas de test, ainsi que exécuter les cas de test en appuyant sur ce bouton de test.

Et il y a probablement un scénario que nous n'avons pas fait C.

Cool, et nous y voilà, n'est-ce pas ? Peut-on lire la propriété valeur ? Non, nous échouons les tests.

055, regardez cette spécification.

Le test cinq nous donne un nœud nul comme racine, n'est-ce pas ? Donc, juste l'arbre vide, vous ne pouvez pas trouver le caractère B à l'intérieur de l'arbre vide.

Donc, le retour semble être faux ici.

Et donc, je peux simplement gérer cela explicitement.

Je vais vérifier en haut.

Si ma racine est non, n'est-ce pas, si c'est le cas, alors retournez simplement faux.

Je ne peux pas trouver de cible dans un arbre vide.

N'est-ce pas ? La raison pour laquelle notre code échouait avant, c'est que si root est null, alors j'initialise ma file d'attente avec no.

Et lorsque cette chose est pop, et que ce null est pop, ou plutôt décalé de la file d'attente dans la première itération, alors je vérifie null dot Val, ce qui est une opération JavaScript illégale.

Donc, je vais exécuter tous ces cas de test maintenant.

Bien.

Et nous avons notre solution en largeur d'abord pour ce problème d'inclusion d'arbre.

D'accord, maintenant, travaillons sur la version récursive en profondeur d'abord de cela, c'est en fait ma préférée personnelle, car elle utilise un motif que je trouve assez élégant, et que j'utilise beaucoup pour des problèmes beaucoup plus difficiles.

Donc, comme nous l'avons dit, dans la vidéo d'approche, si vous n'avez pas regardé l'approche, vous devez absolument la vérifier.

Pour cette version récursive, n'est-ce pas ? Ce que je devrais faire, c'est vérifier, hey, si ma racine est nulle, si j'ai l'arbre vide, en gros, alors retourne simplement faux, n'est-ce pas, parce que je ne peux pas trouver ma cible dans un arbre vide, n'est-ce pas, c'est juste donné.

Et à partir de là, je sais que je vais avoir la forme générale d'un code de parcours en profondeur d'abord, ce qui signifie que vous appelez la même fonction parce que c'est récursif.

C'est ce que signifie récursif.

Et vous passez votre route dot left et un appel séparé votre route, right.

Et ce que je dois m'assurer de faire, c'est de ne pas oublier de passer votre cible, écrivez la cible que vous recherchez, elle ne change jamais.

Et je sais que ces deux appels vont me retourner des données booléennes.

Et je sais que le booléen que j'obtiens de cet appel représenterait si j'ai trouvé la cible dans ce sous-arbre, n'est-ce pas.

Donc, cela me donne le résultat si je l'ai trouvé dans le sous-arbre de gauche.

Ou le résultat si je l'ai trouvé dans le sous-arbre de droite.

Et je peux simplement faire le OU logique sur les deux, n'est-ce pas.

Donc, si je le trouve dans l'un ou l'autre sous-arbre, alors retourne vrai.

Donc, je pourrais simplement écrire en ligne return true ici, n'est-ce pas ? Donc, disons qu'il est dans mon sous-arbre de droite, alors ce côté gauche s'invite à faux.

Et cela est vrai, auquel cas, tout cela évalue à vrai.

Et disons dans un mauvais scénario, disons qu'il n'est pas trouvé dans l'un ou l'autre sous-arbre.

Donc, cela évalue à faux.

Ce côté droit évalue également à faux, faux ou faux me donne faux.

Cependant, une chose que je dois m'assurer d'ajouter est aussi un cas de base supplémentaire, après avoir vérifié si ma route est non, ce que je veux faire, c'est aussi vérifier, hey, peut-être que cette route que je suis actuellement, peut-être qu'elle a en fait la cible, n'est-ce pas ? Donc, si la valeur de la route est égale à la cible, alors vous avez aussi terminé, sauf que vous pouvez retourner vrai.

Cool, et c'était très réminiscent de notre vidéo d'approche.

Donc, essayons cela.

Vous devriez être capable de passer bien, et j'aime à quel point ce code est propre.

Je dois admettre, vous savez, c'est assez délicat.

Si vous n'êtes pas fan d'écrire de la récursivité, auquel cas, je vous convaincreai totalement de devenir fan de la récursivité.

Mais remarquez à quel point ce code est propre, il utilise vraiment la récursivité.

Une chose très importante que je veux souligner, c'est qu'il est vraiment important que je place ce cas de base à la ligne 26 après la vérification nulle, n'est-ce pas ? Donc, disons que j'ai inversé l'ordre de ceux-ci.

Disons que vous avez fait cela.

Je crois que cela ne fonctionnerait pas toujours parce que cela suppose que vous avez même une route, d'accord ? Donc, je me sens un test 00.

Mais en général, si vous regardez ce code, disons que la route était non, n'est-ce pas ? Vous allez commencer par vérifier null dot Val, et cela va lancer une erreur, n'est-ce pas ? Peut-on lire la propriété valve ? Non.

Donc, vous voulez en fait toujours commencer par votre cas de base qui vérifie si votre racine est nulle, n'est-ce pas ? Parce que cela devrait protéger vraiment l'ensemble de notre code.

Donc, c'est en fait le code que vous voulez.

Ici.

D'accord, programmeurs.

C'est tout ce que j'ai pour cette solution d'inclusion d'arbre, je veux que vous pratiquiez les deux versions, et je vous attraperai dans la prochaine.

Hey, programmeurs, Alvin ici, n'est-ce pas ? Maintenant, je veux passer en revue l'approche pour ce problème de somme minimale d'arbre.

Et donc, dans ce problème, je veux prendre un arbre binaire, comme nous l'avons fait ces derniers temps, cette fois, les valeurs à l'intérieur des nœuds de cet arbre binaire vont être des nombres, n'est-ce pas, ce que je veux que vous fassiez, c'est calculer la somme totale de toutes les valeurs de cet arbre.

Donc, pour cet exemple, nous devrions obtenir 25.

Et donc, espérons que vous rassemblez comment attaquer ce problème, surtout étant donné que vous connaissez les algorithmes que je vous ai montrés ces derniers temps.

Donc, si vous avez étudié nos problèmes et y êtes, espérons que vous connaissez une solution directe pour résoudre celui-ci, nous pourrions bien sûr utiliser n'importe quel type d'algorithme de parcours.

Donc, nous pouvons utiliser soit un parcours en largeur d'abord ou en profondeur d'abord.

Et nous pouvons simplement ajouter toutes ces valeurs dans une somme en cours.

Et bien sûr, nous allons probablement initialiser cette somme à zéro, n'est-ce pas ? Donc, la solution itérative en largeur d'abord ou en profondeur d'abord, je pense, est très simple, n'est-ce pas.

Et je ne vais pas vraiment passer en revue cette approche avec vous ici, je pense que vous avez celle-ci bien en main, surtout si vous avez fait les deux problèmes précédents.

Mais ce que je vais vous montrer ici, c'est comment résoudre celui-ci de manière récursive, ce qui serait un type de parcours en profondeur d'abord, car nous savons que hey, le parcours en profondeur d'abord repose sur une pile.

Et si vous faites quelque chose de récursif, il utilise la pile d'appels sous-jacente.

Donc, j'aurai un type d'ordre similaire.

Et donc, lorsque nous traçons cette solution récursive pour ce problème de somme d'arbre, nous allons essayer d'être très explicites, je pense que c'est vraiment utile, surtout si vous avez du mal avec la récursivité, n'est-ce pas ? Étant donné cet arbre binaire, je sais que pour des nœuds particuliers de mon arbre, comme le nœud quatre, il n'a pas d'enfant gauche, n'est-ce pas.

Et je sais que, programmatiquement, ce que cela signifie, c'est que le pointeur gauche de ce nœud pointe vers, non, ou c'est un pointeur nul.

Et donc, je vais simplement le dessiner explicitement, un peu comme ceci.

Encore une fois, ils vont simplement nous aider à vraiment comprendre comment notre code récursif se comporte sur ce type d'entrée.

Et donc, si je sais que je peux mettre un nœud inconnu à gauche de quatre, alors il pourrait être le cas que d'autres nœuds comme les feuilles ont deux et un, ils ont également des enfants gauche et droit qui sont aussi des nœuds nuls.

Donc, si je dessinais tous mes pointeurs nuls explicitement, cela ressemblerait à ceci.

Cool.

Et c'est vraiment quelque chose qui m'a aidé à me sentir à l'aise avec les problèmes récursifs, surtout ceux sur les arbres binaires.

Et ce que nous faisons maintenant, c'est que nous savons que lorsque cela concerne la résolution de n'importe quel problème de manière récursive, il s'agit d'écrire un cas de base, qui est comme la version la plus simple de notre entrée.

Et ici, je vais soutenir que notre cas de base doit être à propos du nœud nul, n'est-ce pas ? Le nœud nul représente en fait aucun nœud du tout, ou représente l'arbre vide en quelque sorte.

En d'autres termes, si quelqu'un me demandait de calculer la somme d'un nœud nul ou la somme d'un arbre vide, alors pour moi, cette somme serait simplement zéro, pour écrire un code récursif élégant, essayez de penser à votre cas de base comme un problème en lui-même, n'est-ce pas ? Donc, si quelqu'un vous donnait un arbre vide, c'est-à-dire un nœud nul, vous retourneriez la somme totale de zéro.

Et ce que cela signifie, c'est que je sais que tous ces nœuds nuls, ils retourneraient zéro comme leurs sommes calculées.

Bien.

Et à partir de là, comment puis-je utiliser cette information pour construire ma solution principale ? N'est-ce pas ? Donc, allons-y et ciblons ce nœud quatre à gauche.

Et ce que je dois faire, c'est déterminer, hey, quelle est la somme totale de ce sous-arbre, et je peux la calculer étant donné les valeurs à gauche et à droite.

En d'autres termes, si je retourne ces deux valeurs nulles, elles retournent à zéro.

Maintenant, je dois faire zéro plus quatre plus zéro, ce qui équivaut simplement à quatre, n'est-ce pas ? Et cela est en fait correct en soi, n'est-ce pas ? Donc, ce que le nombre vert au-dessus d'un nœud représente la somme totale de ce sous-arbre.

Et donc, il est question que, hey, la somme totale de ce nœud quatre est simplement quatre.

Et je ferais quelque chose de similaire pour ce nœud ici, n'est-ce pas ? Lorsque ces cas de base retournent à leur couleur ou retournent à leur parent, je dois simplement ajouter mes enfants gauche et droit ensemble avec moi-même.

Donc, zéro plus deux plus zéro, me donne deux, ne fais pas cela.

Pour ce nœud 11, nous sommes ici.

Et maintenant, les choses deviennent intéressantes, n'est-ce pas ? Pour calculer la somme totale enracinée à ce sous-arbre 11, je vais simplement retourner ces valeurs vers le haut.

Et maintenant, je fais quatre plus 11 plus deux, ce qui me donne une réponse de 17.

Et si vous faites une vérification rapide, n'est-ce pas, ce 17 représente bien la somme totale, juste dans ce sous-arbre, n'est-ce pas, et nous allons continuer sur ce nœud un, nous savons que cela va simplement retourner une valeur de un.

Et maintenant, à ce nœud quatre, je peux calculer sa somme totale.

Et rappelez-vous que ce nœud quatre avait un enfant gauche de zéro, n'est-ce pas ? Parce qu'il a un nœud nul.

Et donc, lorsque je calcule la somme, j'obtiens cinq, ce qui est parfait.

Et enfin, à la racine principale, maintenant je remonte ces deux valeurs.

Et je calcule 17 plus trois plus cinq.

Et cela me donne une réponse finale de 25.

Ce qui est effectivement la bonne réponse.

N'est-ce pas ? Donc, c'est ainsi que nous devrions vraiment penser à nos algorithmes récursifs pour nos arbres binaires, n'est-ce pas ? Je le dessine un peu, je pense aux cas de base, qui sont généralement, mais pas toujours, à propos du nœud nul.

Et à partir de là, j'ai compris comment un parent peut calculer son résultat étant donné les réponses de ses enfants.

D'accord, donc si nous regardons la complexité de cela, c'est assez simple.

Nous allons de l'avant et définissons n comme le nombre de nœuds dans notre arbre d'entrée, auquel cas, je peux voir que ma complexité temporelle est simplement O de n, n'est-ce pas ? Nous savons que nous allons faire un appel récursif pour chaque nœud de l'arbre.

Et nous n'allons pas appeler de nœuds en double, n'est-ce pas, nous allons avoir juste un appel pour chaque nœud.

Et à l'intérieur de n'importe quel nœud, nous allons simplement faire une arithmétique simple, n'est-ce pas, nous avons simplement ajouté environ trois nombres ensemble.

Donc, ce n'est pas comme si nous allions avoir une boucle à l'intérieur de nos appels du tout.

De manière similaire, nous allons dire que la complexité spatiale est O de n, juste parce que nous avons cet espace de pile d'appels implicite, parce que nous allons résoudre celui-ci de manière récursive.

Et donc, nous le résolvons en O de n temps et espace, ce qui serait en fait une solution maximale efficace pour ce problème.

Et donc, avec cela, je pense, passons à la vidéo de démonstration, et je vous montrerai comment coder cela.

Hey, programmeurs, Alvin ici, n'est-ce pas ? Maintenant, je veux passer en revue la solution JavaScript pour ce problème de somme d'arbre, je pense que cette fois-ci, et je vais sauter directement dans la version récursive, n'est-ce pas ? Donc, nous allons commencer de manière récursive.

Et nous allons commencer par notre cas de base, n'est-ce pas ? Mon cas de base est toujours à propos de la version la plus simple de l'entrée, où je connais simplement la réponse sans avoir besoin de calculs supplémentaires, n'est-ce pas ? Je sais que l'arbre le plus simple ici que je pourrais recevoir va être l'arbre vide, n'est-ce pas ? J'ai l'arbre vide.

Cela signifie que ma racine est non.

Et si votre racine est non, vous avez l'arbre vide.

Quelle est la somme de l'arbre vide ? Eh bien, c'est simplement zéro.

Donc, ce sera mon cas de base.

Bien.

Et à partir de là, je vais réfléchir à la façon dont je peux calculer ma réponse, étant donné les résultats de mes enfants.

Donc, je dois trouver les résultats de la somme de mon sous-arbre de gauche.

Et aussi la somme de mon sous-arbre de droite.

Donc, appelez simplement de manière récursive.

Donc, tree, some de root left, ainsi que tree, some de root.

N'est-ce pas ? Cool.

Et je sais que ces deux appels, ils retournent des nombres, n'est-ce pas, représentant la somme de mon sous-arbre de gauche.

Et la somme de mon sous-arbre de droite.

En tant que parent, c'est-à-dire si rude, comment puis-je trouver ma somme totale ? Eh bien, ce n'est que moi-même.

Donc, root out value, plus tout dans mon sous-arbre de gauche plus tout dans mon sous-arbre de droite.

N'est-ce pas.

Et nous allons de l'avant et simplement tester cela dès le départ.

Mais ce n'est rien de fantaisiste, vraiment du code élégant pour regarder les cas de test ici, nous avons une sortie diverse.

Donc, ce code fonctionne sur des arbres de toutes formes et tailles.

Quelque chose qui m'aide à croire en la magie de la récursivité, c'est simplement d'analyser les hypothèses ici, n'est-ce pas ? Donc, disons que je parcours tree some et que ma racine est ce trois ici, n'est-ce pas ? Donc, j'ai vérifié le cas de base, est-ce que ce nœud trois ? Non, ce n'est pas.

Donc, je dois faire l'appel récursif, n'est-ce pas.

Et je sais que lorsque je décompose ce code de manière récursive, je sais que ma route dot Val va être comme trois, donc je correspond à ce commentaire avec la chose en dessous, n'est-ce pas ? Et ensuite, lorsque je fais l'appel récursif sur tree, some root dot left, cela signifie que je demande la somme totale de ce sous-arbre commençant à 11.

Donc, je regarde le 11 pour le sous-arbre négatif deux.

N'est-ce pas, si je prends la somme totale de ce sous-arbre de gauche, il semble que ce soit juste 13.

C'est maintenant que je dis plus 13 ici, n'est-ce pas ? Si je fais la même chose sur le sous-arbre de droite, je sais que cet appel est pour ce nœud quatre, n'est-ce pas, tous ses enfants, cela devrait simplement retourner par la puissance de la récursivité, cela devrait retourner cinq, n'est-ce pas ? Je vais supposer que cet appel récursif fonctionne simplement.

Donc, vous êtes hors du cinq, n'est-ce pas ? Si je prends la somme totale de ceux-ci, trois plus 13 16 16 plus cinq est 21.

Cela me donnerait la bonne réponse, n'est-ce pas.

Donc, pour avoir une certaine confiance dans mon code récursif, j'écris simplement le code.

Et ensuite, j'assume la justesse de mes appels récursifs.

Et je découvre comment je peux prendre ces sous-valées pour mes enfants, les combiner avec ma propre valeur, et cela devrait être ma réponse finale.

Donc, voici la version récursive de cette solution, qui serait une sorte de parcours en profondeur d'abord, techniquement, parce qu'elle est récursive.

Et si vous le souhaitez, je peux également vous montrer la version itérative.

Donc, faisons simplement cela.

Et je pratique habituellement mes problèmes en faisant à la fois la version récursive et itérative, si c'est raisonnable, et c'est vraiment raisonnable ici.

Espérons que vous êtes familier avec notre code en largeur d'abord maintenant, n'est-ce pas ? Donc, je vais simplement commencer par vérifier, hey, si vous avez une racine qui est déjà non, c'est un peu un cas limite, je vais simplement aller de l'avant et retourner zéro, n'est-ce pas ? Parce que la somme de ce sous-arbre vide, ou plutôt cet arbre vide, est simplement zéro, cela peut commencer mon code principal.

Donc, tant que ma file d'attente n'est pas vide, donc je vais commencer avec un Q, qui commence avec la Route Route, je veux boucler tant que ma file d'attente n'est pas vide.

Donc, tant que q dot length est plus grand que zéro, je vais commencer une seule itération de ma boucle while en décalant simplement le devant de ma file d'attente.

Donc, en JavaScript, pour moi, c'est q dot shift qui retire l'élément de devant, et me le retourne également.

Donc, je vais sauvegarder en current.

Et à partir de là, maintenant que j'ai ce current, je sais qu'il contient la valeur qui m'intéresse réellement.

Donc, ce que je ferais, c'est aller de l'avant et suivre une somme en cours.

Donc, je vais dire let some member say let total sum equals zéro.

Et lorsque je retire quelque chose du devant de la file d'attente, je prends sa valeur et je l'ajoute à mon total, quelque chose qui accumulera toutes les valeurs dans une somme.

Et à partir de là, je dois simplement ajouter ma logique classique de vérification de mes enfants, n'est-ce pas ? S'ils existent.

Donc, si j'ai un gauche, donc si current dot left n'est pas égal à no, alors ce que je vais faire, c'est ajouter cet enfant gauche dans ma file d'attente.

Donc, q dot, pousse mon current dot left, encore une fois, assurez-vous de suivre vos règles de file d'attente, n'est-ce pas ? Donc, shift retire du devant, push ajoute à l'arrière, il est vraiment important que mes méthodes shift et push ou mes méthodes add et remove fonctionnent sur des côtés opposés de ma file d'attente.

Sinon, ce n'est pas une file d'attente, n'est-ce pas ? Donc, cela semble bon à faire.

Je vais écrire quelque chose de symétrique.

Pour le côté droit ici.

À la fin de ma fonction, je vais simplement retourner ma somme totale.

Bien, ce serait ma diversion itérative.

Bien sûr, c'est techniquement une largeur d'abord, et nous allons donner un test.

Bien.

Et nous avons cette solution.

Donc, une chose à noter, je pense qu'il est assez important d'être cohérent dans la façon dont vous implémentez ces algorithmes, je jure possible.

Donc, vous remarquerez que je suis toujours un fan de l'écriture de ma logique de traitement de nœud.

Ici, je considère la logique de traitement, où j'ajoute la valeur de mon nœud actuel à ma somme totale.

Je fais cette logique de traitement, généralement lorsqu'un nœud quitte la file d'attente, et non lorsque le nœud est ajouté à la file d'attente, et cela finit par être moins répétitif de cette façon, par exemple, j'ai vu certaines personnes écrire du code comme ceci, où c'est comme, d'accord, eh bien, vous savez, je suppose que puisque j'ajoute mon enfant gauche dans ma file d'attente, cela signifie qu'il existe.

Donc, non seulement je vais le pousser, mais je vais l'ajouter, donc je ne sais pas, total sum, plus equals current dot left dot Val, n'est-ce pas, donc je suis un peu en train d'ajouter la valeur de l'enfant dès qu'il est ajouté à la file d'attente.

Et vous pouvez écrire quelque chose de symétrique pour le côté droit, vous pouvez voir que à cause de cela, je dois doubler tout mon code, ce qui ne le rend pas super propre.

Et je pense que quelque chose qui est encore pire que cela, c'est que vous n'avez jamais ajouté votre valeur de racine dans votre somme totale.

Donc, vous allez devoir commencer votre somme totale comme root dot value à ce stade, je suis comme, je déteste un peu ce code, n'est-ce pas ? Donc, vous pouvez exécuter cela, cela fonctionnerait probablement.

Donc, ce code fonctionne totalement, mais ce n'est pas ce que je pense être la meilleure conception pour ce motif.

Donc, je préférerais l'écrire comme ceci, n'est-ce pas ? Consommez vos valeurs lorsqu'elles quittent votre file d'attente parce que vous savez, éventuellement, tout va partir, n'est-ce pas ? Donc, je le préférerais au moins comme ceci.

Cool.

Donc, avant de passer au problème suivant, je vous recommande de pratiquer les deux versions.

Je sais que ce problème.

Donc, faites-le de manière récursive, faites-le de manière itérative, maîtrisez-les toutes les deux parce que nous allons augmenter la difficulté maintenant.

Hey, programmeurs, Alan ici, n'est-ce pas ? Maintenant, je veux passer en revue l'approche pour ce problème de valeur minimale de l'arbre.

Et donc, comme nous l'avons fait ces derniers temps, nous allons devoir prendre un arbre binaire comme entrée dans notre fonction.

Et nous voulons faire est de déterminer quelle est la plus petite valeur dans l'arbre.

C'est-à-dire que nous voulons trouver la valeur minimale.

Donc, nous pouvons totalement supposer que l'arbre ne sera pas vide, n'est-ce pas ? Et étant donné ces informations, en regardant cet exemple d'arbre particulier, il est assez évident pour nous de voir que le plus petit nombre dans l'arbre est simplement ce trois.

D'accord, donc notre fonction doit simplement retourner le nombre trois.

Donc, il est évident que la réponse est trois.

Mais comment pouvons-nous trouver un algorithme pour le faire pour nous ? Eh bien, nous devrions regarder nos outils dans notre boîte à outils d'arbres binaires.

Et cela serait principalement soit un parcours en largeur d'abord ou en profondeur d'abord.

Une façon évidente de résoudre celui-ci est d'utiliser un code itératif en profondeur d'abord ou en largeur d'abord qui fait un parcours et traverse l'arbre, puis vous devez simplement maintenir une variable externe pour suivre le minimum actuel.

Et chaque fois que vous atteignez un nœud qui est plus petit que votre minimum actuel, alors vous remplacez cette variable de minimum.

Et à la fin du code, vous devriez avoir le vrai minimum.

Donc, la version itérative, je pense, est assez simple.

Et je m'assurerai de passer en revue cela lorsque nous arriverons à la démonstration du code.

Mais pour l'instant, en termes de notre approche visuelle, je pense que nous allons passer en revue celle-ci de manière récursive, n'est-ce pas, car cela se révèle être un code assez concis.

Et donc, regardons cet arbre.

Et faisons semblant que nous avons rempli tous les pointeurs nuls, comme d'habitude, n'est-ce pas ? Donc, ces nœuds sombres ici représentent des nœuds qui n'existent pas, ce qui signifie qu'il n'y a pas de droite.

Donc, par exemple, si je regarde le nœud trois, son enfant gauche est non, mais son enfant droit est 12.

Et cela va être très utile pour nous de visualiser au moins parce que je devrais faire un cas de base sur ces nœuds nuls, n'est-ce pas ? Donc, je sais qu'à long terme, ce que je veux faire, c'est déterminer quelle est la plus petite valeur dans l'arbre.

Et donc, une bonne valeur par défaut pour nos nœuds nuls serait de retourner l'infini.

Et voici le raisonnement pourquoi je sais que je ne devrais vraiment pas considérer les nœuds nuls.

Et donc, si je les fais retourner un infini positif, je sais que l'infini positif ne va définitivement pas être le minimum comparé à n'importe quel nombre qui est réellement dans l'arbre.

Donc, nous allons commencer par remplir toutes ces valeurs infinies.

En d'autres termes, chaque fois que nous appelons un nœud nul, ou un pointeur nul, nous allons retourner l'infini.

Donc, je vais remplir tous ceux-ci.

Maintenant, en utilisant ces infinis comme notre base, nous pouvons en fait construire nos valeurs de retour.

Donc, en regardant ce nœud quatre à gauche, ce que je dois faire, c'est considérer les deux enfants qu'il a reçus, n'est-ce pas, et aussi la valeur dans le nœud actuel.

Et donc, ce que je fais, c'est que je vérifie, d'accord, comparé entre l'infini pour un infini, quelle est la plus petite valeur parmi eux ? Eh bien, je sais que l'infini positif est un très grand nombre.

Donc, vraiment, le plus petit nombre ici devrait être quatre.

Et donc, cet appel devrait retourner quatre, n'est-ce pas ? Ce nœud devrait retourner une histoire similaire pour ce nœud 15.

Une fois que j'ai mes valeurs de retour gauche et droite prêtes, je fais une comparaison avec ces valeurs contre moi-même, n'est-ce pas ? Donc, je vérifie, quel est le minimum parmi l'infini ? 15 et l'infini, le minimum est 15.

Je pense que cela devient intéressant maintenant que nous évaluons ce nœud 11, n'est-ce pas ? Maintenant, j'ai quelques nombres réels.

Et donc, je fais cette comparaison, n'est-ce pas ? Je compare ma valeur de sous-arbre gauche, qui est quatre, et ma valeur de sous-arbre droit, qui est 15.

Et aussi moi-même, qui est 11.

Donc, parmi 4, 11 et 15.

Quel est le plus petit nombre ? Eh bien, ce serait simplement le quatre, n'est-ce pas ? Donc, ce nœud devrait retourner quatre.

Et si je fais une vérification rapide, cela a du sens, car j'ai cette réponse pour au-dessus du nœud 11, qui me dit que, dans ce sous-arbre enraciné à 11, la plus petite valeur était quatre, ce qui est totalement correct.

Maintenant, nous allons simplement évaluer le reste de cet arbre.

En regardant ce 12 ici, je sais que je ne peux pas évaluer le trois parce que j'ai besoin d'une valeur prête du côté droit.

Donc, je dois évaluer ce 12.

Et je fais simplement la comparaison, n'est-ce pas ? Quel est le minimum parmi l'infini, 12 et l'infini ? Eh bien, c'est simplement définitivement 12.

Enfin, à ce nœud trois, je prends le minimum de l'infini, trois et 12, le minimum là est trois.

Et enfin, à la racine ultime, je fais la comparaison.

Et je vérifie quel est le plus petit parmi quatre, ou cinq et trois ? Et la réponse va être le trois, n'est-ce pas, ce qui est exactement ce que nous attendions.

Et donc, simplement en ajoutant une petite variation à notre classique récursion en profondeur d'abord, nous pouvons totalement résoudre ce problème.

La logique que nous devons utiliser pour combiner nos sous-solutions enfants dans notre solution principale est de simplement faire une comparaison, n'est-ce pas ? Donc, dans l'ensemble, à chaque point de cet arbre, nous nous demandons, n'est-ce pas, étant donné la plus petite valeur dans le sous-arbre de gauche et étant donné la plus petite valeur dans le sous-arbre de droite.

Je compare ceux-ci à moi-même, et je retourne le plus petit parmi ceux-ci.

Et ensuite, en ce qui concerne la complexité de cela, c'est assez simple.

Nous allons de l'avant et disons que n est le nombre de nœuds dans notre arbre d'entrée.

Et nous savons que nous allons avoir un appel pour chaque nœud de cet arbre.

Donc, cela semble être un temps O de n.

En termes de nombre d'appels récursifs, n'est-ce pas, et nous savons qu'à l'intérieur de n'importe quel appel récursif particulier, il semble que nous allons simplement faire une logique conditionnelle, n'est-ce pas, simplement trouver le minimum parmi trois choses.

Puisque trois est un nombre constant, je suis assez sûr que nous allons avoir simplement une complexité temporelle globale de O de n, en considérant le nombre d'appels que nous faisons.

Maintenant, cela dit, nous aurons également une complexité spatiale O de n, simplement due à la pile d'appels que nous utilisons pour le parcours en profondeur d'abord de base.

Et cela semble être une solution optimale pour ce problème.

Parce que ce que nous allons faire, nous allons de l'avant et coder cela, et je vous attraperai dans le prochain.

Hey, programmeurs, Alvin ici, n'est-ce pas ? Maintenant, je veux passer en revue une solution JavaScript pour ce problème de valeur minimale de l'arbre.

Et bien sûr, nous allons résoudre celui-ci de quelques manières différentes.

Je pense que je vais commencer par vous montrer peut-être quelques solutions itératives.

Et donc, nous allons simplement faire un classique en profondeur d'abord et aussi en largeur d'abord, en cours de route, n'est-ce pas.

Donc, vous savez, vous allez devoir itérer ou frapper chaque nœud dans votre arbre binaire.

Donc, allez-y et configurez soit une pile soit une file d'attente.

Donc, je vais choisir de commencer avec une pile ici.

Donc, je vais dire Kant's, stack equals empty.

Et une chose dont je dois être conscient, c'est de regarder les hypothèses dans le problème, ils nous disent que nous pouvons supposer que l'arbre d'entrée n'est pas vide.

Et donc, cela signifie que je n'aurai pas besoin d'ajouter une instruction if initiale vérifiant si la racine de niveau supérieur est nulle.

Donc, je peux simplement aller de l'avant et initialiser ma pile avec le nœud racine à l'intérieur.

Cool.

Et à partir de là, vous avez besoin de votre boucle principale pour itérer à travers les différents nœuds.

Donc, je vais boucler tant que ma pile n'est pas vide.

Donc, tout stack dot length est plus grand que zéro.

Cool.

Donc, si c'est le cas, et qu'il y a encore des nœuds à visiter, et commencer une seule itération de cet algorithme, disons en profondeur d'abord, en faisant stack dot pop, donc je retire le haut de ma pile, allez-y et appelez cela mon courant.

Et à partir de là, bien sûr, nous devons vérifier si nos enfants existent.

Et s'ils le font, je les ajouterai au haut de ma pile, n'est-ce pas ? Donc, je vais écrire un motif comme celui-ci, je vais dire si, disons current dot left, qui n'est pas égal à No, alors je peux aller de l'avant et pousser cet enfant existant sur la pile, n'est-ce pas ? Donc, stack dot push, et je vais pousser current left retinas quelques fois maintenant, devrait-ce être une seconde nature, je vais faire un peu le même code pour le côté droit.

Et c'est un peu ma base de parcours en profondeur d'abord, n'est-ce pas.

Mais lorsque je regarde ce nœud actuel et sa valeur, je veux, à la fin de ma boucle, avoir accès à la valeur minimale dans l'arbre.

Et donc, parce que je dois trouver la valeur minimale dans cette fonction, nous allons utiliser une variable que je vais mettre à jour au fil du temps, n'est-ce pas, pour suivre la plus petite chose que j'ai vue.

Donc, je vais l'initialiser comme let smallest, je vais devoir réfléchir à une bonne valeur par défaut pour cela.

Et donc, je vais l'initialiser à l'infini positif.

Donc, si vous n'êtes pas familier avec JavaScript, l'infini est essentiellement un nombre qui est garanti d'être plus grand que tous les autres nombres, sauf lui-même, l'infini, n'est-ce pas ? Et la raison pour laquelle je choisis un grand nombre, comme l'infini positif, pour ma valeur par défaut pour la variable la plus petite, c'est parce que lorsque je vois des valeurs réelles de mon arbre, je sais qu'elles sont garanties d'être inférieures à l'infini.

Donc, ces nombres remplaceraient mon infini, cela me donne simplement une bonne valeur initiale, n'est-ce pas ? C'est un motif assez courant, n'est-ce pas ? Si vous cherchez la chose minimale, et typiquement votre valeur par défaut est l'infini positif.

Si vous cherchez une chose maximale, alors votre valeur par défaut pourrait être zéro ou l'infini négatif, selon le problème que vous essayez de résoudre.

Et donc, avec cette valeur par défaut, où est-ce que je veux réellement la remplacer, n'est-ce pas.

Et je vais choisir de le faire juste après ou quelque chose quitte ma pile.

De cette façon, vous n'avez à le dire qu'une seule fois.

Si je l'écrivais, lorsque j'ai ajouté mes enfants dans la pile, ce que je dis deux fois, n'est-ce pas, ce qui est un peu ennuyeux.

Donc, je vais simplement vérifier, hey, si la valeur actuelle, donc assurez-vous de comparer la valeur numérique réelle, la valeur actuelle est inférieure à la plus petite, alors je viens de trouver une nouvelle plus petite, n'est-ce pas ? Donc, remplacez simplement cette variable par la valeur actuelle.

Bien sûr, à la fin de notre boucle while, nous devrions simplement retourner cette variable, n'est-ce pas ? Et nous devrions avoir le vrai minimum.

Donc, essayons cela, exécutons ces cas de test.

Et c'est notre version itérative de profondeur d'abord, n'est-ce pas ? Génial.

Donc, si vous vouliez changer, vous savez, écrire le largeur d'abord est super trivial en termes de changement que nous faisons, vous pouvez simplement vous assurer de faire stack dot shift, n'est-ce pas, parce que cela retirerait l'élément de devant de votre file d'attente maintenant et si vous poussez, vous l'ajoutez toujours à l'arrière.

Et je suppose que vous devriez probablement renommer ce gars en file d'attente.

Donc, une différence très minime.

Bien, tests que nous allons simplement essayer cela.

Cool, passe tous.

Bien.

Et une chose à noter.

Donc, Alex en JavaScript, il n'y a pas immédiatement lorsque j'ai enregistré cette vidéo, il y a une structure de données de file d'attente optimale immédiatement disponible, comme vous ne pouvez pas l'importer via une bibliothèque standard.

Et donc, lorsque vous faites réellement la méthode array dot shift, cette ligne elle-même va s'exécuter en O de n temps, n'est-ce pas, parce que si vous retirez l'élément de devant d'un tableau en JavaScript, il devra en fait décaler tous les autres éléments d'une position.

En d'autres termes, l'index un devient l'index zéro, l'index deux devient l'index un, et ainsi de suite.

Et donc, techniquement, si vous avez implémenté votre largeur d'abord exactement comme ceci, en utilisant simplement un tableau régulier, et que vous décalez, alors cela serait probablement comme une solution O n carré, ce qui n'est pas le plus rapide, mais nous serons en mesure de passer les spécifications, typiquement n carré pour la plupart des problèmes est un peu acceptable.

Mais vous pouvez l'éviter si vous voulez obtenir la solution ultra-rapide.

Mais maintenant, allons-y et implémentons ma version préférée, qui serait une version récursive, n'est-ce pas, qui est techniquement de la profondeur d'abord.

N'est-ce pas ? Donc, nous allons dire const, trimming value, chattering min value, dream and value.

Et pour établir celui-ci de manière récursive, nous allons toujours commencer par notre cas de base, n'est-ce pas ? C'est lorsque vous avez vu ces gars courbés.

Donc, je vais commencer mon cas de base, je vais dire si mes routes est égal à null, alors cela signifie que j'ai l'arbre vide, quelle est la valeur minimale dans l'arbre vide ? Alors que cela doit être l'infini, n'est-ce pas ? Pour la même raison que nous avons choisi l'infini avant, n'est-ce pas ? C'est juste une bonne valeur par défaut, parce que je vais minimiser à long terme.

Cool.

Et maintenant, ce que je veux faire, c'est que je veux faire mon appel récursif.

Donc, si j'appelle treeman value sur mon enfant gauche, et que je l'appelle sur mon enfant droit, je vais simplement penser à ce que ces appels de fonction retournent.

N'est-ce pas ? Bien qu'ils soient récursifs, si ces appels fonctionnent, ils devraient me donner la plus petite valeur dans le sous-arbre de gauche.

Et la plus petite valeur dans le sous-arbre de droite.

Donc, peut-être, juste pour être clair, je vais de l'avant et sauvegarder les variables système.

Donc, je vais dire const, je vais dire, left.

Min.

Et aussi, cela devrait être le right men, n'est-ce pas ? Donc, j'ai trouvé le plus petit à gauche et le plus petit à droite.

Mais je dois aussi penser à moi-même, n'est-ce pas ? Je suis ru dot Val.

Donc, je dois choisir le plus petit de root Val left men et Reitman, n'est-ce pas, donc vous pouvez écrire comme une condition.

Donc, juste quelques instructions if si vous voulez, je pense que la meilleure façon de l'implémenter en JavaScript est d'utiliser la fonction math dot min.

Donc, JavaScript, vous avez toujours accès à l'objet global capital math, il a quelques méthodes utiles dessus.

L'une que nous allons trouver utile maintenant est math dot min.

Si vous faites cela, vous pouvez passer quelques arguments et un nombre arbitraire d'arguments.

Donc, donnez-moi le plus petit entre route dot Val et assurez-vous d'accéder à la valeur parce que vous devez donner des nombres à men, n'est-ce pas ? Le plus petit entre route dot Val, mon left men et mon right man.

Cool.

Et cela ressemble quelque peu à l'approche que nous avons faite, où nous devions choisir le plus petit de ces trois nombres.

Donc, avant de l'exécuter, peut-être que vous n'êtes pas familier avec math dot min, je peux rapidement vous le démontrer.

Disons que j'avais quelques nombres, nous avions 10, nous avions trois, nous avions six, et nous avions moins 12.

Et aussi 100.

Et si je console log avec ce que cela retourne, je vais simplement exécuter ce fichier comme un script.

Donc, je ne vais pas exécuter les tests pour l'instant.

Donc, je devrais obtenir moins 12.

Parce que c'est le plus petit parfait.

Et maintenant, je pense que nous sommes prêts à aller de l'avant et à tester cela.

Donc, notre version récursive, la voici.

Cool.

D'accord, donc, nous avons notre démonstration JavaScript pour ce problème de valeur minimale de l'arbre, je vous recommande de pratiquer toutes ces différentes solutions, et ensuite de choisir une préférée, peut-être juste à avoir dans votre poche.

De cette façon, vous pouvez toujours résoudre ce problème à l'avenir, n'est-ce pas ?

Donc, vous ne devriez avoir aucun problème à penser à la façon de résoudre un problème de valeur maximale de l'arbre.

Et maintenant, vous savez, nous nous sentons assez à l'aise avec les arbres.

Et typiquement, nous allons toujours revenir à un parcours en largeur d'abord ou en profondeur d'abord.

Mais dans les prochains problèmes, nous allons définitivement regarder quelques dérivés et quelques variations sur la façon dont nous pouvons accomplir une logique plus complexe en utilisant ces algorithmes comme notre base.

Donc, je vous attraperai dans le prochain.

Hey, programmeurs, Alvin ici, n'est-ce pas ? Maintenant, je veux passer en revue ce problème de somme maximale du chemin de la racine à la feuille.

Et donc, dans ce problème, nous allons prendre un arbre binaire comme entrée, et nous voulons vraiment parler des chemins dans cet arbre en particulier, des chemins de la racine à la feuille.

Donc, juste pour réviser, nous savons qu'un arbre binaire a typiquement pour nous une seule racine et vous pouvez identifier la racine en regardant simplement le nœud le plus haut, c'est-à-dire le nœud sans parent, n'est-ce pas ? Et étant donné cet arbre, il y a trois feuilles, n'est-ce pas ? Une feuille est un nœud qui n'a pas d'enfants.

Donc, gardez à l'esprit qu'une racine n'a pas de parent.

Un nœud feuille n'a pas d'enfants, comme 11, et trois dans cette image, il y en a qui ne sont ni des racines ni des feuilles, n'est-ce pas.

Donc, il pourrait être le cas qu'un arbre ait de nombreuses feuilles, comme cet arbre, n'est-ce pas, a trois feuilles.

Mais un arbre pour nous a typiquement une seule racine.

Et donc, ce que nous voulons faire, c'est considérer les trois chemins différents de la racine à la feuille, n'est-ce pas, donc vous devez commencer à la racine, et vous devez terminer à une feuille.

Donc, l'un de ces chemins serait simplement celui-ci, n'est-ce pas, 511 pour, ce que nous voulons faire, c'est considérer sa somme totale.

Donc, en additionnant simplement les valeurs dans les nœuds le long de ce chemin.

Si je fais cinq plus 11, plus quatre, cela me donnerait une somme totale de 20.

Donc, c'est l'une des possibilités.

Si je regarde un autre chemin, disons ce chemin de 511 à cinq plus 11, plus deux, cela me donnerait 18.

C'est une autre option.

La seule autre option est le chemin final de cinq à un, cinq à cinq plus trois plus un.

Cela me donne une somme totale de neuf, n'est-ce pas ? Et maintenant, parmi ces trois options, je veux choisir la somme maximale du chemin, n'est-ce pas ? Donc, ce serait une réponse finale de 20.

Donc, à long terme, nous devons trouver un code qui calcule la somme maximale du chemin de la racine à n'importe quelle feuille.

Et cela semble être un problème assez difficile, n'est-ce pas ? Comment pouvons-nous nous y prendre ? Eh bien, espérons que vous remarquez quelques motifs similaires, n'est-ce pas ? Juste en regardant le nom de ce problème, je me souviens de quelques motifs différents, n'est-ce pas ? Je peux penser au problème de la somme de l'arbre qui semble assez lié ici.

Et puis-je aussi penser au problème de la valeur minimale.

Problème où nous avions une logique de minimisation, sauf que maintenant, je veux maximiser quelque chose ici.

Et donc, probablement ce que je vais devoir faire dans celui-ci, c'est combiner certaines de mes connaissances précédentes pour venir avec une solution assez nouvelle, mais c'est bon de s'appuyer fortement sur nos expériences précédentes, n'est-ce pas.

Et donc, commençons par quelque chose de classique, je pense que nous allons résoudre celui-ci de manière récursive.

Et dans le grand schéma des choses, typiquement, pour les problèmes d'arbres, c'est-à-dire un code récursif est généralement votre meilleur pari lorsqu'il s'agit de trouver des chemins, n'est-ce pas, et de construire des chemins et de déterminer des chemins.

Et donc, nous allons regarder ce que nos cas de base devraient être, si nous allons encadrer celui-ci de manière récursive.

Donc, ils nous disent que, d'accord, vous devez considérer les chemins, mais pas n'importe quels chemins, n'est-ce pas ? Vous voulez toujours finir à un nœud feuille.

Donc, les nœuds feuilles, comme le point de fin, croyez-le ou non, le cas de base.

Donc, mon cas de base va être littéralement à propos d'un nœud feuille.

Et rappelez-vous que c'est un nœud sans enfants.

Donc, par exemple, disons que nous avions un nœud comme entrée qui n'avait pas d'enfants, alors quelle est la somme totale de ce nœud feuille ? Eh bien, ce serait simplement sa valeur interne n, n'est-ce pas ? Donc, pensez à vos cas de base comme s'ils étaient leurs propres entrées, n'est-ce pas ? Comme une rapide mise à part, n'est-ce pas, donc un scénario totalement séparé, n'est-ce pas ? Maintenant, disons que je vous donne un arbre qui ne contient qu'un seul nœud, et sa valeur était 42.

Et je vous demande, d'accord, dites-moi, quelle est la somme maximale du chemin de cet arbre, cet arbre est très petit, n'est-ce pas ? Si vous identifiez la racine dans cet arbre, c'est simplement le nœud 42, n'est-ce pas ? Parce qu'il n'a pas de parent.

Et je vous ai également demandé les feuilles, il n'y a qu'une seule feuille ici.

Et c'est aussi le 42, n'est-ce pas ? Parce qu'il n'a pas d'enfants, n'est-ce pas ? Donc, le nœud unique de 42, dans cet exemple, est la racine et la feuille, ce qui signifie que la somme maximale du chemin serait simplement 42.

Cool.

Donc, je pense à mes cas de base comme s'ils étaient leurs propres entrées.

Bien.

Et ce que vous reconnaîtriez probablement ici, c'est que, dans ce scénario, nous considérons un cas de base qui n'est pas à propos d'un nœud nul, n'est-ce pas, nous aurons besoin d'au moins un cas de base séparé qui vérifie si nous avons un nœud feuille réel.

Et cela est très, très inhérent et donné dans le problème, n'est-ce pas ? Ils disent chemin de la racine à la feuille.

Génial.

Donc, si c'est le cas, je vais simplement localiser tous mes nœuds feuilles dans ce diagramme.

Et je sais qu'ils vont retourner les valeurs qui s'y trouvent.

Donc, en les branchant simplement, n'est-ce pas ? Et maintenant, je peux commencer à reconstruire mes solutions de niveau supérieur, n'est-ce pas ? Donc, étant donné ce nœud 11, quelle décision ce nœud 11 doit-il prendre pour calculer sa réponse, n'est-ce pas ? Donc, lisons-nous à ce nœud 11.

Et nous devons considérer nos valeurs gauche et droite, n'est-ce pas.

Et donc, si je route moi-même à 11, le quatre représente ma somme maximale de chemin à travers mon sous-arbre de gauche.

Et le côté droit à deux représente maintenant la somme maximale de chemin à travers mon sous-arbre de droite.

Puisque je veux maximiser ici, la clé est de simplement choisir entre quatre et deux, n'est-ce pas ? Je choisis le plus grand d'entre eux, n'est-ce pas ? Donc, quatre est plus grand que deux, donc je dois utiliser le quatre.

Et ce que je fais, c'est que je prends ce quatre, et je ajoute ma valeur actuelle de 11 dedans, et cela me donne 15.

Et cela serait en fait la réponse pour ce sous-arbre.

En d'autres termes, je peux vérifier la justesse maintenant, si je me route à 11.

Je retourne 15 pour représenter ce chemin, n'est-ce pas ? Je peux soit faire 11 plus quatre, ce qui est 15.

Ou je peux faire 11 plus deux, ce qui est 13.

D'accord, et ce 13 est plus petit, donc je ne le préférerais pas ici.

Cool.

Donc, jusqu'à présent, il semble que nous soyons en bonne forme.

Maintenant, regardons un autre nœud prêt à évaluer.

Regardons ce.

Nœud trois.

Donc, il a une valeur sur son côté droit, n'est-ce pas ? Il reçoit un un de son enfant droit, mais l'enfant gauche n'existe pas, n'est-ce pas ? Et si vous voulez être un peu plus explicite, nous savons que l'enfant gauche ou trois points à gauche va être un pointeur nul.

D'accord ? Donc, branchez cela ici.

Et voici où nous devrions travailler dans un autre cas de base, parfois il est très naturel de corriger le cap en cours de route.

Et donc, pour un nœud nul, que devrions-nous retourner ? Eh bien, nous savons que chaque fois que nous avons un nœud nul, il ne devrait jamais contribuer à notre réponse finale, nous pouvons simplement l'ignorer, je suppose, nous voulons nous assurer qu'il est compatible avec le reste de notre logique interne.

Gardez à l'esprit dans ce problème, je veux prendre le maximum, n'est-ce pas ? Rappelez-vous de notre problème précédent, n'est-ce pas, le problème de la valeur minimale, nous voulions prendre le minimum.

Et donc, nous avons fait en sorte que nos nœuds nuls retournent l'infini, n'est-ce pas ? Parce que si je veux trouver le minimum, et que mes nœuds nuls retournent l'infini, par défaut, je sais que l'infini ne va jamais gagner une comparaison, n'est-ce pas ? Parce que l'infini est très grand.

Et nous allons simplement inverser cette logique ici, n'est-ce pas ? Donc, parce qu'à long terme, je veux trouver le maximum, je vais faire en sorte que mon cas de base pour les nœuds nuls retourne l'infini négatif, n'est-ce pas ? Parce que je sais que l'infini négatif ne va jamais gagner un concours où nous comparons les choses, en cherchant la plus grande des valeurs, n'est-ce pas ? Donc, pour ce nœud nul, je vais brancher cet infini négatif.

Et maintenant, je ne devrais pas être capable de faire la même logique commerciale qu'avant, n'est-ce pas ? Donc, je me route à moi-même au nœud trois, et je peux regarder les résultats que j'obtiens pour mes enfants, n'est-ce pas.

Donc, entre mes deux enfants dans mon chemin de gauche, j'obtiens un infini négatif, ou dans mon chemin de droite, j'obtiens un un, et je choisis le maximum entre eux, n'est-ce pas ? Un est plus grand que l'infini négatif.

Donc, je devrais utiliser le un, n'est-ce pas.

Et ce que je fais avec ce un, c'est que je l'ajoute à ma valeur actuelle de trois.

Donc, trois plus un me donne quatre, n'est-ce pas.

Et cela a du sens, car si je regarde ce petit sous-arbre, enraciné en trois, le plus grand chemin de la racine à la feuille, ou sous-racine à la feuille, serait effectivement un quatre.

Bien, et maintenant nous nous trouvons à la racine ultime ici, je fais cette comparaison similaire, n'est-ce pas ? Je vérifie le plus grand de mes deux enfants, donc je vais garder le 15.

Mais ensuite, j'ajoute moi-même à cela, ce qui donne 20.

Comme nous l'avons dit avant, ce 20 représente logiquement ce chemin de cinq plus 11 plus quatre.

Cool, donc nous y voilà.

Et si vous voulez regarder la complexité de cela, cela semble être quelque chose d'inhabituel.

Donc, nous allons avoir n comme le nombre de nœuds, nous allons avoir un temps O de n, parce que nous allons devoir faire un appel récursif pour chaque nœud de l'arbre.

Et si je pense à n'importe quel appel particulier, nous allons faire un nœud étranger, nous allons simplement faire une comparaison, n'est-ce pas, je choisis simplement le plus grand de mes deux enfants.

Donc, ce n'est pas comme si nous allions avoir des boucles dans nos appels, je crois.

Cool.

Donc, cela semble être un temps O de n.

Comme nous le disons toujours, la complexité spatiale est O de n, simplement due à la pile d'appels.

Bien.

Donc, allons-y et codons cela.

Et cela devrait ressembler à une combinaison de nos problèmes précédents de somme d'arbre, ainsi qu'à une logique de valeur minimale et maximale.

Hey, programmeurs, bienvenue, Ryan, je veux passer en revue une solution JavaScript pour ce problème de somme maximale du chemin de la racine à la feuille.

Donc, ce sera un problème d'arbre assez intéressant.

Et nous allons sauter directement dans le code, veuillez vous assurer de regarder la vidéo d'approche avant celle-ci.

Donc, je pense que vous devriez être tous prêts avec la logique que nous voulons implémenter ici.

N'est-ce pas ? Et donc, nous allons commencer par faire cela de manière récursive.

Et je dirais que c'est probablement la meilleure façon de résoudre celui-ci.

Donc, je pense que c'est la seule façon que je vais vous montrer, ce que je veux faire, c'est commencer par un cas de base, n'est-ce pas ? Nous avons dit que nous voulons déterminer nos chemins de la racine à la feuille.

Donc, notre cas de base devrait être de savoir si j'ai une feuille, n'est-ce pas ? Donc, je vais vérifier, disons, si ma racine gauche est égale à No, n'est-ce pas ? Et racine, droite ? Est égal à No, n'est-ce pas ? C'est la définition d'une feuille.

Donc, si j'ai l'enfant gauche et que j'ai l'enfant droit, alors je devrais retourner la valeur stockée à ce nœud, n'est-ce pas ? Donc, racine, point Val.

Bien.

Donc, encore une fois, nous soulignons ici que le cas de base capture un scénario.

Si nous sommes à une feuille, n'est-ce pas, nous n'avons pas d'enfants.

Bien.

Et nous aurons besoin d'un autre cas de base à long terme.

Pour l'instant, disons que nous l'avons laissé comme ça, n'est-ce pas ? Nous avons dit que dans le contexte de la résolution de celui-ci de manière récursive, la décision que nous prenons à chaque note est que je choisis le plus grand résultat de mon appel de colonne A droit, et ensuite je m'ajoute à lui, n'est-ce pas ? Donc, je sais que je vais faire cela de manière récursive, donc je vais appeler la même fonction.

Et maintenant, vous devriez être familier avec tout, n'est-ce pas, vous appelez votre fonction sur root left, et aussi root right ? Cela, je pense à ce que ces appels retournent, n'est-ce pas ? Ils me donnent le max pass some à travers mon sous-arbre de gauche sur le max path, some à travers mon sous-arbre de droite, je veux simplement choisir les plus grands résultats entre les deux.

Donc, non, je vous jure que je vous ai vu utiliser la fonction math dot min ici, j'utiliserai la fonction math dot max.

Et je sais que ces appels, ces expressions évaluent à des nombres.

Donc, je peux en fait simplement les passer en ligne.

Donc, je vais simplement déplacer cela comme ça.

Donc, lorsque je trouve le max entre ces deux résultats, et je vais de l'avant et je vais appeler cela, nous allons dire, le max, votre enfant, n'est-ce pas ? Peut-être que je vais écrire cela en ligne, ils préfèrent.

Et à partir de là, je m'ajoute simplement à ce max enfant, n'est-ce pas ? Donc, je vais retourner route dot valance moi-même, plus max enfant.

Et nous allons appeler cela max enfant path.

Et cela devrait être tout sauf une chose que nous oublions.

Donc, prenez un moment, voyez si vous pouvez lire entre les lignes ici.

Et quel scénario est-ce que je manque ? Nous l'avons mentionné dans la vidéo d'approche.

Donc, pouvez-vous repérer ce qui n'est pas présent ici ? Et c'est quelque chose que je trouve que je fais souvent, n'est-ce pas ? Si je suis capable de vraiment créer une belle image cohérente et significative, alors tout ce que j'ai dessiné dans l'image devrait se traduire par un morceau de code ici.

Donc, essayons cela.

Attendez-vous à échouer celui-ci.

Voyez ce que nous obtenons ? Oui, donc nous obtenons une erreur ne peut pas lire la propriété left have no, n'est-ce pas, trouvé sur le tout premier exemple.

Donc, je vais vous dire que cela est causé par un nœud asymétrique, comme ce quatre ici, n'est-ce pas ? Ce quatre n'a pas d'enfant gauche.

Donc, imaginez ce qui se passerait dans cette instance, n'est-ce pas ? Donc, si nous évaluons ce code, nous savons que notre route va être ce nœud quatre.

Et cette instruction if à la ligne 10, n'est pas atteinte, n'est-ce pas ? Parce que quatre n'est pas une feuille, n'est-ce pas ? Parce qu'il a un enfant droit, l'enfant droit ne sait pas.

Donc, au lieu de cela, il va s'exécuter jusqu'à 11.

Et il va essayer d'exécuter max path, some of root dot left root that left is no.

Et donc, lorsque nous évaluons réellement cet appel, maintenant nous voyons est no, et nous allons vérifier no dot left ici.

Et cela va casser, n'est-ce pas ? C'est exactement la ligne qui est cassée.

Et donc, en plus de ce cas de base, n'est-ce pas, lorsque nous avons atteint un nœud feuille, que se passe-t-il si nous finissons simplement par un nœud nul, donc si root est null, alors nous avons dit qu'une bonne valeur à retourner serait l'infini négatif, n'est-ce pas ? Parce que je choisis, à long terme, de faire une logique maximale et je veux choisir le max.

Donc, si je choisis un infini négatif, cela n'interférera pas avec l'un de nous prenant un max, n'est-ce pas ? Parce que imaginez que cette chose était un infini négatif.

Et je préférerais simplement le côté droit s'il n'était pas l'infini, n'est-ce pas ? L'infini négatif.

Et donc, avec cela, allons-y et essayons cela.

Cool.

Et nous avons une belle solution pour notre problème de somme maximale du chemin de la racine à la feuille.

Donc, remarquez à quel point le code est court, en aucun cas je ne pense que ce code est simple, n'est-ce pas ? À ce stade, c'est bon si cela semble un peu difficile.

Mais vous comprenez comment nous avons quelques motifs familiers, n'est-ce pas, j'ai toujours ces deux appels récursifs ici.

Et nous varions généralement dans la façon dont nous prenons ces appels récursifs ou les résultats de ceux-ci, et les combinons dans notre réponse de niveau supérieur.

Donc, continuez à pratiquer ce problème et je vous attraperai dans le prochain.

D'accord, programmeurs.

Cela conclut notre cours d'introduction aux arbres binaires.

Si vous souhaitez explorer ce sujet des arbres binaires, ou vraiment n'importe quel autre sujet de structures de données et d'algorithmes plus profondément.

Assurez-vous de vous rendre sur destructing dotnet où nous avons tous ces sujets couverts à travers des tonnes de problèmes où nous avons des démonstrations vidéo et des illustrations pour chaque problème.

Je pense que vous trouverez cela particulièrement utile si vous vous préparez et que vous bachotez vraiment pour ces entretiens techniques.

Merci d'avoir regardé, et je vous verrai là-bas.