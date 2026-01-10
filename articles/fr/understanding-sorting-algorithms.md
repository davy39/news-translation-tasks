---
title: Comprendre les algorithmes de tri
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-06-18T13:56:04.000Z'
originalURL: https://freecodecamp.org/news/understanding-sorting-algorithms
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/sorting.png
tags:
- name: algorithms
  slug: algorithms
- name: youtube
  slug: youtube
seo_title: Comprendre les algorithmes de tri
seo_desc: 'Every programming language uses sorting algorithms. While programming languages
  have easy-to-use sorting methods, it can be helpful to understand how they work.

  We just released a course on the freeCodeCamp.org YouTube channel that will teach
  you som...'
---

Chaque langage de programmation utilise des algorithmes de tri. Bien que les langages de programmation disposent de méthodes de tri faciles à utiliser, il peut être utile de comprendre comment elles fonctionnent.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous enseignera certains des algorithmes de tri les plus populaires !

Haris Iftikhar a développé ce cours. Haris gère la chaîne Coding Cleverly et il a beaucoup d'expérience dans la création de tutoriels utiles.

Dans ce cours, vous apprendrez le tri par sélection, le tri à bulles, le tri par insertion, le tri par fusion et leurs ordres de complexité. Ce cours utilise C++ mais les concepts s'appliquent à n'importe quel langage de programmation.

Voici les algorithmes et les sujets abordés dans ce cours :

* Algorithme de tri simple
* Tri par sélection
* Explication diagrammatique
* Tri à bulles
* Explication graphique du tri à bulles
* Tri par insertion
* Implémentation graphique
* Tri par fusion
* Explication approfondie
* Différence entre les algorithmes

Regardez le cours ci-dessous ou [sur la chaîne YouTube freeCodeCamp.org](https://youtu.be/l7-f9gS8VOs) (1 heure de visionnage).

%[https://youtu.be/l7-f9gS8VOs]

## **Transcription complète**

(Note : générée automatiquement)

Les algorithmes de tri sont utilisés régulièrement en informatique et en programmation.

Dans ce cours, vous apprendrez comment fonctionnent les algorithmes de tri les plus populaires en utilisant des diagrammes et du code. Codage avec Coding Cleverly, mais cette fois, nous sommes sur une chaîne différente. C'est exact, Coding Cleverly est mis en avant par Free Code Camp.

Cette vidéo portera sur certains des différents algorithmes de tri que vous pouvez appliquer à presque n'importe quel langage de programmation.

Le langage mis en avant dans cette vidéo sera le C++, cependant, comme je l'ai dit, vous pouvez appliquer les concepts à n'importe quel autre langage de votre choix comme Java, Python, C, et ainsi de suite, vous devriez au moins connaître les concepts fondamentaux de la programmation, surtout les structures de programmation de base, comme la séquence, la sélection et l'itération.

Pour comprendre cette vidéo, assurez-vous également de consulter ma chaîne Coding Cleverly, où j'ai couvert presque tous les concepts, des fondamentaux de la programmation à la programmation orientée objet, en passant par les structures de données et les algorithmes et au-delà.

D'accord, alors commençons par écrire un algorithme simple pour trier un tableau.

Tout d'abord, incluons notre iostream et encouragez-vous à taper avec moi pour obtenir la pratique maximale.

Donc, #include <iostream>.

Et ensuite nous avons notre espace de noms standard.

Et ensuite nous avons notre entier main.

Et nous avons aussi notre retour zéro ici.

Nous allons donc commencer par un algorithme très simple.

Et nous allons regarder son implémentation visuelle.

Supposons donc que nous avons un tableau de quatre éléments.

Et ce sont les quatre côtés que nous avons : 2, 3, 1 et cinq.

Et essentiellement, il s'agit d'un tableau, qui est essentiellement indexé avec des valeurs de zéro jusqu'à trois.

Notre travail est de le trier dans l'ordre croissant, nous savons que ce n'est pas dans l'ordre croissant.

Nous allons donc utiliser un algorithme très simple.

Et je vais créer, en fait, l'implémentation ici.

Ensuite, nous retournons à notre éditeur de code, et nous allons taper avec, et cela va avoir beaucoup plus de sens.

Supposons donc que nous avons deux variables, et nous allons avoir une variable, qui va être inscrite en haut, donc nous allons avoir cela comme AI.

Donc, ce sera le premier, qui est l'emplacement zéro.

Et ensuite nous avons j, qui sera le deuxième, qui sera i plus un.

Donc, juste après l'AI sera le J et nous allons appliquer une boucle for imbriquée.

Donc, la première boucle for aura une condition, bien que après à l'intérieur, il y aura une prémonition qui dit j est inférieur à I.

Donc, ici, ce que cela signifie est que le tableau de ce j m, la valeur de ce j est inférieure à la valeur de ce I maintenant, c'est ce que je voulais dire par array sub j et inférieur à arrays de valeur absolue de j inférieur à la valeur I, c'est notre condition qui va être à l'intérieur de notre boucle for imbriquée, celle interne.

Et c'est la condition si elle est vraie, nous allons créer une variable temporaire, et nous allons stocker la valeur de i donc ce qu'il y a dedans, donc dans ce cas, ce serait deux est dedans.

Donc, deux va être stocké dans temp, donc ensuite nous allons l'échanger en utilisant une méthodologie d'échange rapide est égal à j et j est égal à la variable temp.

Donc, quelle que soit la valeur de temp était en fait était si la valeur était deux, cela va être dans J.

Donc, en fait, nous venons d'implémenter une méthodologie d'échange ici.

Donc, juste après cela, nous allons vérifier cette condition.

Donc, dans ce cas, nous avons deux et trois, donc une valeur de trois est en fait supérieure à la valeur de deux.

Donc, dans ce cas, la condition ne sera pas vraie, et elle ne s'exécutera pas.

Donc, cela va simplement sauter la valeur.

Et nous allons simplement faire en sorte que notre j s'incrémente maintenant à la portion suivante.

Donc, nous allons sauter cela.

Donc, je viens de barrer cela.

Et maintenant, je vais mettre ce pointeur suivant ici et J.

Donc, maintenant, I et J, maintenant vous pouvez voir que la valeur de J est inférieure, maintenant nous avons un et nous avons une comparaison avec deux.

Donc, g un est inférieur à deux.

Donc, cette condition est maintenant vraie, vous pourriez voir que un et deux vont être situés en parlant des valeurs.

Et maintenant que la condition va être satisfaite ici.

Donc, nous allons regarder ici que temp est égal à i, et ensuite nous avons la valeur qui est I donc qu'est-ce que I à deux donc cela va être dans cette variable temp est égale à j maintenant j est en fait un, donc i est égal à un, donc nous allons avoir ici i est égal à la valeur un.

Maintenant, après cela, nous avons j donc j est égal à la valeur de temp.

Maintenant, la valeur de temp était en fait deux.

Donc, maintenant vous pouvez voir que cette valeur échangée.

Donc, nous avons I, qui est maintenant un sauf pour deux maintenant deux, et maintenant ici dans la position J au lieu de un.

Maintenant, nous avons la valeur de deux.

Maintenant, vous pouvez voir que cela a été échangé et maintenant la valeur de J va être incrémentée.

Donc, vous pouvez voir que l'index ne va plus être ici.

Et maintenant, il va être dans la cinquième baie, en fait la dernière, qui est là où la cinquième valeur se trouve.

Et nous allons vérifier à nouveau, nous allons dire i et j, nous allons dire j est inférieur à I, bien, non, ce n'est pas j est supérieur à I.

Donc, maintenant cette portion de cette boucle for imbriquée va être terminée.

Et ce qui va se passer maintenant, c'est que nos yeux vont être incrémentés.

Donc, I plus plus, et nous allons avoir I savoir, plus un.

Donc, à l'origine, où j était à droite, donc maintenant là, c'est là que i va être.

Et en fait, ce que nous voyons ici, c'est que j va toujours être i plus un, comme nous l'avons mentionné avant, c'est notre processus d'algorithme de tri dont nous avons besoin.

Donc, cela va simplement être côte à côte, ou ils vont être adjacents l'un à l'autre initialement, et ensuite après cela, ils vont simplement s'incrémenter.

Donc, comme, juste comme la position de J, donc nous avons j ici, et nous avons i et j.

Donc, si je regarde ici, nous avons I, qui est trois et J, qui est pour vérifier la condition.

Maintenant, c'est vrai à nouveau.

Donc, ce qui va se passer, c'est que j est inférieur à i, c'est vrai.

Et nous allons traiter cela, temp est-il, temp est égal à maintenant, vous pourriez deviner ce qui se passe ici.

Maintenant, temp est égal à la valeur de i, qui est trois maintenant, donc trois va être placé ici.

Donc, vous avez trois.

Et ensuite après cela, nous avons i est égal à maintenant la valeur de j, j est en fait deux, donc nous allons simplement avoir deux ici, i est égal à deux.

Et puis le dernier, qui est j est égal à la valeur de 10 plus 10, plus trois, donc cela se place ici, donc maintenant nous venons de l'échanger à nouveau.

Donc, nous avons au lieu de trois, nous avons deux ici, et au lieu de deux, nous avons trois ici.

Donc, vous pouvez voir maintenant que j va être incrémenté à nouveau jusqu'au dernier, et nous pouvons voir i est juste dans la même position exacte, et zéro va comparer deux et cinq.

Eh bien, cette condition n'est pas satisfaite pour cette condition, donc elle va simplement incrémenter ce processus à nouveau, i et j vont maintenant comparer et dire trois et cinq, tandis que cette condition n'est également pas vraie pour que la boucle while soit exécutée.

Donc, maintenant nous avons ce i et j en rouge.

Donc, vous verrez qu'il n'y a rien à changer.

Donc, nous avons en fait, notre algorithme fonctionne.

Et nous voyons que 123 et cinq, voir 123 et cinq, ils sont dans l'ordre croissant.

Et c'est ainsi que notre algorithme était censé fonctionner.

Donc, cette implémentation visuelle de cet algorithme nous a aidés et maintenant nous pourrions la mapper dans notre code.

Donc, nous allons taper maintenant, donc je vous encourage à taper avec moi.

Donc, commençons.

D'accord, donc la chose ici est que nous allons devoir créer un tableau, et je l'appelle un tableau, et je suppose qu'il a une taille.

Donc, je pourrais définir quelque chose ici en haut.

Donc, je dis hash define, et je dis Max, et je dis que c'est 100.

D'accord, donc c'est la valeur maximale, donc je viens de mettre max ici.

Et ce que je pourrais dire ici, c'est que je pourrais demander à l'utilisateur d'entrer un nombre et, et cela sera la taille et elle devrait être entre zéro et 100.

Donc, ce sera l'entrée, et ensuite ce sera n maintenant, je dois définir un N ici, donc je vais simplement dire entier.

Et donc c'est l'entier et maintenant l'entrée de valeurs dans un tableau.

Donc, en mettant des valeurs dans le tableau avec un nouveau for, ne dites pas int i est égal à zéro est inférieur à n, je dirais i plus plus vraiment simple.

Et ensuite nous avons la fonction RAND qui va mettre des valeurs aléatoires à l'intérieur de chaque index, donc nous pourrions dire array sub, je dirais, juste la fonction RAND.

Et c'est tout.

Donc, cela va donner un nombre entre zéro et RAND Max, quelle que soit la valeur maximale entière.

Donc, ce que nous pourrions mettre ici, c'est maintenant que nous devons inclure un autre fichier d'en-tête pour la fonction RAND.

Donc, il s'appelle C standard library.

Et voilà.

Donc, les bibliothèques C standard ne savent pas que nous avons des valeurs à l'intérieur de cela, sortons notre tableau.

Donc, en sortant le tableau non trié, donc le tableau non trié, nous dirions simplement de base pour int, i est égal à zéro, i est inférieur à n, et ensuite nous avons i plus plus, et ensuite nous disons console, sortie array sub sub i, et nous mettons cet espace.

Et espérons que nous obtiendrons un tableau, mettons simplement une ligne de fin ici à la fin.

Et maintenant, j'enregistre mon code.

Donc, je vais l'exécuter en utilisant mon compilateur G plus plus.

Donc, ici, je vais écrire g plus plus mon nom, qui est partie un, et nous avons CPP, et espérons qu'il va être compilé.

Maintenant, nous disons simplement a pour l'exécuter, et à travers un nombre n.

Donc, en fait, je pourrais dire 10.

Maintenant, il va me donner 10 nombres aléatoires pour mon tableau de huit.

Donc, il a 41, ceci, ceci et ceci et tout le chemin jusqu'à 10.

Donc, vous pouvez voir que ce sont 10.

Exécutons cela une fois de plus.

Et maintenant, je vais entrer 20.

Maintenant, il devrait me donner 20 entiers aléatoires.

Donc, maintenant, les voilà.

Et si nous avions 50, non, 50 entiers aléatoires.

Maintenant, vous avez compris mon point ici.

Il crée un tableau aléatoire.

Et met des valeurs aléatoires.

Mais vous pouvez voir ici que celles-ci ne sont pas triées dans un ordre quelconque.

Elles ne sont pas dans le nœud ascendant ou sont dans l'ordre décroissant.

Et c'est notre travail de le mettre.

Donc, c'est 41.

Et vous pouvez voir que c'est un nombre qui est plus grand, mais ensuite vous pouvez voir un nombre plus petit.

Et que signifie cela.

Donc, nous avons besoin d'un tableau correctement géré.

Donc, créons un tableau correctement géré.

Donc, ce que nous pouvons faire ici, c'est juste après cela, créer un algorithme de tri.

Donc, trier, et tableau.

Donc, comment allons-nous trier ce tableau ? Tout d'abord, allons-y et ouvrons une boucle for.

Donc, disons pour int i est égal à zéro, i est inférieur à n, et ensuite nous disons i plus plus.

Et ensuite juste après cela, nous pouvons mettre un autre tableau d'entrée.

Donc, nous pourrions dire, cette autre boucle, qui va être imbriquée à l'intérieur de la première, donc ce sera J.

Mais cela est prudent.

C'est la valeur suivante après le tableau.

Et je vous dirai, quelle est la raison derrière cela, disons j inférieur à n, et nous disons j plus plus.

Et maintenant à l'intérieur de cela, c'est essentiellement notre concept qui va être appliqué avec array sub j est inférieur à array sub i.

Maintenant, que signifie cela ? Je vous dirai tout cela.

Donc, supposons que nous avons un tableau.

Et cela dit que si array sub j est inférieur à arrays, parce que regardez cela, donc c'est un tableau, et vous verrez que c'est un ordre.

Donc, vous pouvez voir que c'est cette valeur I qui commence à zéro, et c'est un j qui commence, qui est supérieur à I une fois, donc vous verriez que j est cela.

Et maintenant, si j'avais un tableau aléatoire ou un tableau, oh, disons cinq ici.

Donc, vous pourriez voir que ce n'est pas dans l'ordre croissant, c'est essentiellement 10.

Et ensuite c'est cinq, pourquoi cinq est ici, quelque chose de plus grand devrait apparaître.

Donc, la condition ici est que erase sub j est inférieur à array sub i.

Donc, si array sub j, qui est cela, est inférieur à array sub i.

Et c'est le cas.

Maintenant, ce que nous voulons faire, nous voulons échanger les valeurs.

Donc, ce que nous pourrions faire en échangeant les valeurs, donc var cinq pourrait être ici, et la valeur originale 10 devrait être placée ici.

Comment faisons-nous cela, parce que 510 30 et 40 seront alors triés.

Et le problème est que nous allons devoir créer un entier d'entrée, temporaire, quelque chose.

Donc, nous allons mettre cela en l'assignant avec I.

Maintenant, une fois que nous avons cela assigné avec I, ce que nous pourrions faire ici, c'est que nous pourrions changer un race de AI.

Et nous pourrions dire à cela à un race de J.

Donc, nous assignons la valeur de race de yeux avec la valeur de array sub J.

Et maintenant nous pouvons avoir la valeur de race de J.

Et nous aimerions la mettre comme une valeur de temp.

Donc, cela va improviser notre tableau de manière triée.

Et cela va être dans l'ordre croissant a sc n di, N D, ou D er.

Donc, cela va être dans l'ordre croissant.

Donc, cela va vérifier et ensuite après cela, cela va faire cela, cela va aller dans notre prochaine itération, qui va être est égal à un.

Donc, plus plus incrémente à cela, donc cela va être cette valeur, et ensuite cela va être vérifier avec cette valeur.

Et cela va voir si c'est le cas que ce n'est pas correct, cela va l'échanger, cela va simplement faire cette prochaine itération jusqu'à ce que le tableau soit terminé.

Donc, une fois que c'est fait, vous pouvez simplement sortir de la boucle.

Et une fois que vous sortez, comme vous êtes libre, donc une fois que vous êtes libre, vous retournez à zéro.

Donc, cela va me donner mon tableau dans l'ordre croissant.

Mais maintenant nous n'avons rien qui l'affiche.

Donc, affichons ce tableau.

Donc, je vais simplement écrire des commentaires courts sur le tableau, maintenant nous allons afficher le, donc disons simplement le tableau trié.

Donc, en affichant le tableau trié, nous faisons simplement une boucle for de base, i est égal à zéro, je vais dire i inférieur à n, et nous disons i plus plus.

Et ensuite ici, ce que nous pourrions ajouter, c'est essentiellement console output, et nous disons array sub i.

Et ensuite nous disons cela.

Et maintenant, mettons simplement une ligne de fin ici.

Maintenant, exécutons le code.

Donc, en fait, retournons à notre compilateur G plus plus.

Et nous allons exécuter notre code.

Mais tout d'abord, compilons-le.

Et je vais simplement donner un drapeau hyphen o pour indiquer que c'est un nouvel exécutable, et je vais simplement l'appeler run.

Donc, je vais appuyer sur le bouton de compilation, la compilation est réussie.

Maintenant, nous allons simplement l'exécuter.

Donc, maintenant vous verrez entrer un nombre et donc entrer un nombre et cela signifie que nous allons simplement entrer un nombre aléatoire et il va créer un tableau avec des valeurs aléatoires dans chaque index, donc prenons 20.

Maintenant, ce sont 20 nombres aléatoires.

Vous verrez ici pour 2041 et tout cela qui est non trié.

Cela va dans un ordre aléatoire.

Et ensuite après cela, il le trie.

Et vous pouvez voir que mon algorithme de tri fait le travail et les trie dans l'ordre croissant.

C'est assez incroyable.

D'accord, maintenant faisons une autre chose pour nous avoir une manière d'ordre décroissant.

Une autre chose que je veux faire ici, c'est que je veux dire que c'est le genre de, donc je pourrais simplement écrire une sortie de console, et je dirais trié.

Donc, trié.

Et ici, afficher le tableau trié.

Et l'autre chose que je veux faire, c'est que je veux simplement vous montrer comment fonctionne le descendant.

Donc, ce signe inférieur, qui est les tableaux de J, inférieur aux tableaux de I, sera simplement transformé en tableaux de j supérieur aux tableaux de I.

Donc, si c'est supérieur, échangez-le, donc c'est essentiellement l'ordre décroissant, donc je vais simplement changer cet ascendant en d, e, s, e, n, di, N, G.

Donc, cela va maintenant être dans l'ordre décroissant.

Donc, cela va s'exécuter à nouveau.

Donc, je vais simplement compiler cela, en fait.

Et ensuite nous allons l'exécuter.

Et maintenant, prenons une valeur comme 22.

Maintenant, vous avez ces valeurs, qui sont 41.

Et tout cela dans un ordre aléatoire.

Et ensuite après cela, vous appelez le trié, essentiellement affiché sur l'écran du terminal.

Et ensuite après cela, vous les triez dans une manière d'ordre décroissant, et regardez à quel point c'était génial.

Donc, c'est tout pour celui-ci.

Et maintenant, continuons avec les autres algorithmes de tri.

Donc, le prochain algorithme de tri s'appelle le tri par sélection, l'un des algorithmes de tri les plus courants et les plus célèbres au monde.

Donc, comment nous allons l'implémenter est essentiellement d'abord taper avec moi, et nous allons expliquer côte à côte, ainsi que donner une brève explication à la fin.

Donc, continuez à taper avec moi.

Donc, #include, nous allons avoir input output stream, et ensuite nous allons avoir using namespace standard.

Et ensuite nous avons aussi integer main.

Et nous avons aussi le retour zéro.

Maintenant, ce que nous allons faire ici est essentiellement, d'abord nous allons créer une fonction d'échange.

Donc, ce que je vais implémenter est essentiellement une fonction d'échange, donc void, et ensuite nous avons swap.

Et ensuite nous avons essentiellement un tableau que nous allons avoir, et il va échanger.

Donc, je vais vous montrer qu'il va avoir une valeur x, et il va avoir une valeur y.

Donc, il va implémenter ce processus de fonction d'échange célèbre que nous avons fait.

Donc, ce qu'il va faire est essentiellement, integer temp va avoir un sub x comme première valeur, donc un sub x, donc un sub x va être égal à un sub y, et ensuite nous allons avoir est un sub y égal à la variable 10ème.

Donc, et c'est ainsi que nous échangeons quelque chose.

Donc, supposons que nous avons un tableau à l'intérieur, et nous l'appelons simplement un tableau.

Et nous allons avoir quelques valeurs.

Donc, disons quelques valeurs aléatoires.

Et ce que nous voulons faire est essentiellement, nous voulons échanger le processus ici, si nous avons quelques valeurs aléatoires qui ne correspondent pas, et nous voulons les échanger, nous pourrions utiliser une fonction d'échange comme nous l'avons fait dans l'algorithme de base au début où nous avons fait l'ordre croissant.

Donc, essentiellement, nous implémentons le tri par sélection.

Donc, nous avons créé notre première fonction, qui est swap, la deuxième fonction que nous allons faire est essentiellement le tri par sélection.

Donc, comment cela va se passer est essentiellement nous allons avoir un void.

Et nous allons appeler cela comme un tri par sélection.

Et il va avoir deux paramètres d'entrée.

Le premier va être le tableau, et le second va être essentiellement la taille du tableau.

Maintenant, à l'intérieur de cela, il va avoir l'index de localisation, qui est zéro, il va toujours commencer à zéro, le tableau commence à zéro, juste cela et maintenant après cela, il va boucler à travers cela, donc il va être i inférieur à n moins un, nous allons boucler jusqu'au dernier élément, donc n moins un est le dernier élément, et ensuite nous allons devoir trouver la valeur qui devrait être plus petite que la valeur que nous spécifions comme étant zéro, et elle devrait être comme la fonction d'échange, donc nous allons devoir indiquer un j ici.

Donc, il va être appelé, et nous allons utiliser une autre fonction, qui va être appelée l'emplacement du plus petit.

Et ne vous inquiétez pas, je vais vous enseigner ce que c'est.

Donc, essentiellement, nous allons avoir un sub i, et nous allons avoir n moins un.

Donc, nous allons simplement avoir trois paramètres d'entrée, ici, nous allons avoir le tableau passé en référence, et vous savez, cela est passé par référence.

Donc, ce sera toujours le même tableau peu importe où vous allez.

Et ensuite nous avons iron, qui va être l'emplacement actuel, il va toujours s'incrémenter.

Et il va être zéro ici, il va changer.

Et ici, c'est le point de fin.

Donc, c'est le dernier, le dernier élément.

Donc, swap va être implémenté ici.

Et il va avoir trois paramètres d'entrée comme nous l'avons fait avant.

Donc, il va avoir le tableau, qui est small a, et ensuite il va avoir la taille de l'œil et il va avoir ce J.

Donc, essentiellement, I qui va être l'index, donc il va être le premier élément et le deuxième élément et veut les échanger.

Donc, il va implémenter la fonction d'échange et il va incrémenter i plus plus ici.

Donc, c'est ainsi que cela va se faire maintenant, nous avons besoin ici de la fonction de localisation du plus petit.

Donc, cela ne le rend pas oh ici.

Donc, ce que nous allons faire ici dans la localisation du plus petit est essentiellement avoir un type de retour.

Bonjour, d'accord, parce qu'il va retourner une valeur de J.

Donc, vous pouvez voir que j est un entier, donc il a besoin d'un type de retour à la fin.

Donc, ici, la localisation du plus petit, prenons quelques paramètres d'entrée, le premier paramètre d'entrée est le tableau.

Et le deuxième paramètre est le s.

Et le troisième paramètre d'entrée est le point de fin.

Et vous pourriez vous demander pourquoi j'ai fait cela.

Et vous pouvez voir ici que le point de départ va être I, le point de fin va être n moins un.

Donc, il va toujours vérifier à la fin.

Donc, il va boucler à travers ce tableau entier et essayer de trouver le plus petit.

Et quand il trouve le plus petit à partir de I, alors il va échanger les valeurs dans la fonction d'échange.

Et c'est ainsi que nous allons implémenter cet algorithme de tri par sélection.

Donc, si je vais créer un AI ici, je vais simplement créer des variables intermédiaires.

L'une va être Isaac s, donc I S.

Donc, AI va être comme le point de départ, et ensuite nous allons avoir j, qui va être égal à essentiellement I not s, donc nous allons l'implémenter, et nous allons dire ce que c'est, cela va être dans j et I ici est le point de départ.

Et ensuite ce que nous faisons ici, c'est que essentiellement, nous allons avoir une boucle à nouveau.

Donc, pendant que nous allons avoir i inférieur ou égal à E, qui est le point de fin, maintenant, si A et ensuite nous avons un sub i, qui est le premier élément, si cela est inférieur à un sub j, si nous trouvons une sorte de chose qui est plus grande, donc un sub j est plus grand.

Donc, nous dirions que j est égal à, je veux juste échanger à droite, nous voulons le localiser.

Et ensuite après cela, ce que nous voulons faire est essentiellement l'incrémenter en utilisant i plus un, à droite, donc cela va être incrémenté.

Et ensuite nous allons retourner la valeur de l'objet.

Et ne vous inquiétez pas, je vais expliquer cela à travers une représentation graphique.

Donc, vous êtes, c'est ainsi que cela se fait.

Donc, nous avons nos trois fonctions, nous avons une fonction d'échange, et nous avons une fonction de localisation du plus petit.

Et nous avons aussi une fonction de tri par sélection, créons une fonction d'affichage pour afficher le contenu du tableau.

Donc, elle va être appelée display, elle va avoir un tableau d'entiers, et elle va avoir une taille de tableau, qui est n.

Et ce que vous allez faire ici, c'est essentiellement commencer à zéro.

Et comment elle va être implémentée, c'est essentiellement pendant que le i est inférieur à n, et ensuite nous allons afficher le contenu du tableau en utilisant un sub i.

Et nous allons avoir les guillemets doubles ici, qui est l'espace et juste aller, il va continuer à les lister.

Et ensuite il va imprimer une ligne de fin ici juste pour rendre le format un peu plus joli.

Donc, juste après cela, ce que nous ferons, c'est essentiellement avoir le tableau ici spécifié, créons simplement un tableau, qui va être appelé arr.

Et il va avoir quelques valeurs aléatoires.

Donc, il va avoir 100 à 12, je donne simplement des valeurs aléatoires ici, c'est juste au format aléatoire, il doit être trié en utilisant ma fonction de tri par sélection.

Donc, je vais simplement passer cela.

Donc, vous pouvez voir que c'est aléatoire.

Et maintenant, ce que je fais, c'est essentiellement calculer la taille, comment calculer la taille, l'un des processus que je veux utiliser est essentiellement l'opérateur de taille, l'opérateur de taille va passer, et il va avoir un tableau, et ensuite il va avoir la taille de la variable entière.

Donc, essentiellement, vous verrez que c'est le type de données, et il va être pour le tableau, c'est essentiellement tout.

Donc, nous verrons 1234567 et huit et neuf, neuf, multiplié par quatre, qui est essentiellement 36.

Et maintenant, 36 sera essentiellement divisé par l'entier, qui va être quatre.

Donc, 36 divisé par quatre va vous donner la valeur, qui est neuf.

Donc, neuf va être la réponse ici.

Donc, une fois que c'est la taille, je vais simplement commenter ici et dire taille égale à neuf.

Pourquoi ne voulons-nous pas faire ici, c'est essentiellement que nous voulons implémenter notre sélection.

Donc, tout d'abord, affichons-le.

Donc, affichons et nous allons simplement passer la variable et la taille.

Donc, cela va simplement s'afficher automatiquement parce que c'est une fonction void, et son but est de l'afficher.

Et ensuite juste après cela, cela s'appelle notre fonction de tri par sélection.

Et elle va demander le tableau et aussi une taille.

Et ensuite après cela, nous allons simplement afficher notre sélection, le tableau trié en utilisant le tableau, et ensuite lorsque vous avez la taille.

Donc, une fois que je fais cela, je vais simplement exécuter et courir.

Donc, en fait, je vais à mon écran de terminal ici, je vais écrire g plus plus, je vais utiliser le point de tri par sélection cpp.

Et tout ce que nous savons, par défaut, ce sera un, donc je vais simplement l'exécuter et je vais dire O et je vais dire tri par sélection.

Donc, maintenant, il est compilé, et j'ai exécuté un tri par sélection.

Maintenant, vous verrez ici, nous avons des trucs aléatoires, qu'est-ce qui se passe.

D'accord, donc quelque chose a mal tourné Ctrl T, pour casser le code, quelque chose a mal tourné dans ce code, et vérifions simplement ce qui ne va pas.

Qu'est-ce qui ne va pas ici.

Donc, nous avons iOS et ensuite il s'incrémente.

Donc, ce processus est correct.

Et moins un est correct, il y a une boucle infinie qui a été créée en utilisant des tableaux de sélection ou de tri, puis la taille.

Et donc, regardons simplement ici.

D'accord, donc j'ai oublié d'incrémenter ce i plus plus.

Donc, juste ici, je ne l'ai pas commis.

Et maintenant, cela va fonctionner.

Donc, en fait, nous avons fait cela, et exécutons simplement ce code une fois de plus, tri par sélection.

Et maintenant, appelons-nous et regardons cela, nous avions ce tableau, qui était non trié, qui est 102 12 193 90, peu importe 32.

Et maintenant, ce que nous avons fait, c'est passé dans le tri par sélection, et il a trié le tableau pour nous, je veux dire, 11 1239, dans l'ordre croissant, maintenant croissant, qu'est-ce que c'est, comme, si vous avez la même valeur, cela pourrait être égal, ou demandé d'être plus grand.

Donc, juste au cas où, si j'ai une valeur, comme 11, et 11, ils vont être dans les mêmes emplacements adjacents.

Et ensuite après cela, cela pourrait être une valeur plus grande.

Donc, c'est trié.

Dans le tri par sélection, j'espère vraiment que vous avez apprécié et compris, donc ce que je veux faire, c'est une autre chose, c'est essentiellement vous montrer comment l'implémentation est faite.

Donc, supposons que les tableaux sont triés comme ceci dans la mémoire.

Donc, nous avons quelques indices.

Donc, nous avons comme cinq, et nous avons quatre, et nous avons trois, nous avons sept, nous avons neuf.

Donc, nous voulons trier cela dans l'ordre croissant.

Donc, ce que nous allons faire par défaut, avec le tri par sélection, c'est que le tri fait de cet œil l'index de zéro, et il vérifiera pour J.

Donc, mon processus ici est comme celui de l'emplacement du plus petit qui sera appelé.

Et vous verrez dans mon code, qui est essentiellement ici, donc je vais simplement vous montrer ici, ce que je vois ici, c'est que l'emplacement est zéro, et le Y n'est pas inférieur à n moins un, le dernier élément, ce que nous faisons, c'est que nous obtenons le J et nous le mettons dans l'emplacement du plus petit en passant un, nous avons la variable I, qui va être essentiellement zéro et n moins un, qui est le dernier élément, et il va être l'emplacement du plus petit.

Donc, l'emplacement du plus petit va localiser la variable, qui va être celle-ci, la plus petite, même si i est inférieur ou égal à E si c'est inférieur ou égal.

Donc, si elle la trouve, elle va la trier comme j et elle va retourner cette valeur.

Donc, vous pouvez voir ce qui se passe, c'est qu'elle trouve la plus petite.

Donc, vous voyez que la plus petite ici est trois, donc j va pointer ici.

Et ensuite, il va appliquer cet algorithme de tri, qui va couper et échanger cela.

Donc, vous pouvez voir ici qu'il va échanger, donc nous avons trois ici.

Et ensuite, initialement, cinq va être ici.

Mais ce que nous voulons voir ici, c'est que dans cet éditeur de texte, c'est essentiellement l'affichage, donc nous avons un tri par sélection.

Et ensuite, une fois que nous retournons dans notre algorithme de tri par sélection, nous avons une fonction d'échange, l'échange va obtenir cette valeur par l'énergie qui est retournée d'ici, et il va l'échanger.

Donc, essentiellement, l'algorithme d'échange simple, il va échanger les deux valeurs.

Et ensuite après cela, il va incrémenter et il va aller à notre prochain emplacement.

Donc, vous pouvez voir la place ici va No, non, elle ne va plus pointer ici.

Et elle va pointer ici.

Et maintenant, ce j ne va plus être ici.

Donc, je veux simplement indiquer que ce j va maintenant pointer ailleurs.

Donc, nous avons cela maintenant implémenté ici.

Donc, je vais être incrémenté ici.

Maintenant, c'est sa base.

Et ce que nous allons vérifier maintenant, c'est que cela ne va pas être trié avec trois.

Donc, maintenant, nous sommes toujours essentiellement ici.

Donc, maintenant, nous allons chercher une valeur qui va être plus petite que quatre.

Donc, essentiellement, y a-t-il quelque chose de plus petit que quatre, ce n'est pas le cas, donc nous incrémentons simplement, et nous disons que I va être ici.

Maintenant, c'est cinq, s'il y a quelque chose d'étranger, c'est bon, donc il va vérifier tout et il va aller à travers la boucle jusqu'à ce que le tableau entier soit trié.

Donc, j'espère que vous avez compris ce concept de tri par sélection à travers cette implémentation graphique.

Maintenant, nous allons passer à notre prochain algorithme de tri.

Et allons-y.

D'accord, donc maintenant, regardons un autre algorithme de tri.

Celui-ci s'appelle l'algorithme de tri à bulles.

Et cela va se passer comme suit.

Donc, essentiellement, vous devez inclure votre flux d'entrée-sortie, et vous allez devoir faire votre espace de noms standard.

Et allons-y, écrivons simplement notre code de base.

D'accord, donc, ce tri à bulles va aussi traiter avec l'échange.

Donc, nous allons devoir inclure cette méthodologie d'échange, qui est essentiellement swap, et ensuite nous avons un tableau d'entiers, nous avons une valeur x, nous avons une valeur a y.

Et essentiellement, lorsque nous allons ici, nous avons en fait un temporaire, qui va être assigné à la première valeur, et ensuite nous avons la première valeur, qui est un sub x va être assigné à la valeur a sub y, et ensuite la valeur a sub y sera égale à la valeur 10ème.

Donc, c'est ainsi que fonctionne l'échange.

Et maintenant, ayons un processus de bulle.

Donc, le processus de bulle est un peu différent.

Comment il est différent, c'est que du tri par sélection que nous avons déjà couvert, nous sommes en fait allés du haut à droite, donc nous sommes allés du haut et ensuite nous sommes allés de notre chemin vers le bas.

Donc, dans le tri à bulles, nous allons aller du bas vers le haut, donc je vais simplement l'expliquer.

Donc, d'abord, tapez simplement avec moi.

Donc, ce sera bu BB le Baba.

Et ensuite ce que ce processus va faire, c'est qu'il va faire un processus spécifique, il va obtenir un tableau.

Et il va aussi obtenir la taille du tableau.

Et nous allons revenir à cela un peu plus tard.

Donc, laissez-moi simplement, je viens d'écrire une signature pour l'instant.

Et je vais aller et parler de la fonction void bubble process.

Donc, les fonctions réelles de tri à bulles, c'est la fonction réelle de tri à bulles.

Et ce que nous allons faire est essentiellement, elle va avoir ce même tableau d'entiers, qui est ici, et ensuite nous avons la taille.

Et donc maintenant ici, ce que nous voulons faire est essentiellement commencer à partir de la portion dont je parlais, que le tri à bulles va adopter.

Donc, le tri à bulles va dire, entier I entier i est égal à zéro.

Et ce dont nous avons besoin, c'est que pendant que nous avons i est inférieur à n moins un, le dernier élément, nous allons avoir bubble process.

Donc, BB, BB le bubble, et il va avoir le taux et la valeur de fin, qui est n va être la taille va être le taux et il va l'incrémenter au poids.

Donc, il va simplement aller et incrémenter.

Donc, dans la bulle, ce que nous allons avoir est ici, maintenant nous allons l'ouvrir, et nous voulons commencer donc le processus de bulle va être à partir du I.

Donc, il va commencer à partir du dernier élément.

Donc, c'est ce dont je parlais, n moins un est le dernier élément.

Et il va aller comme pendant que nous avons essentiellement i supérieur à zéro, donc i supérieur à zéro.

Et maintenant à l'intérieur de cela, si nous avons une condition que si un sub est maintenant un sub i devrait être inférieur à un sub i moins un.

Maintenant, cela signifie qu'il y a un A sub II, si la portion supérieure est plus grande.

Donc, ce que vous voulez faire, c'est que si un sub i est inférieur à l'ACI moins un, ce que vous voulez faire, c'est l'échanger, donc nous allons l'échanger en utilisant cette fonction d'échange que nous avons déjà, elle va prendre un, elle va prendre l'élément AI, et elle va prendre i moins un.

Donc, c'est ainsi qu'il va l'échanger.

Et nous allons avoir génériquement en allant moins moins parce que nous commençons par n moins un, il va aller jusqu'à zéro.

Donc, ce processus devrait fonctionner.

Donc, maintenant après cela, nous devrions avoir notre fonction d'affichage.

Et nous sommes prêts à partir.

Donc, en fait, affichons ici un tableau.

Et nous avons aussi la taille du tableau, qui est une sorte de taille, je vais simplement l'appeler comme cela.

Et maintenant à l'intérieur, nous avons besoin d'une entrée.

Donc, je vais simplement dire une sorte de est égal à zéro entier.

Et ensuite nous avons le processus de boucle, qui va commencer par i inférieur à n.

Et ensuite, allez-y, donc en fait, il est inférieur à n et vous voulez le traiter. Donc tableau. Et ensuite nous avons la valeur ISO.

Et nous allons simplement continuer comme cela, jusqu'à ce que nous atteignions notre point de fin.

Donc, qui est la sortie de la console ici.

Oui, juste pour le rendre un peu plus similaire au précédent, je vais simplement changer cela en juste et parce que celui-ci correspond ici.

Donc, maintenant, créons un tableau ici.

Et je vais simplement l'appeler comme un tableau d'entiers.

Et je vais simplement lui donner quelques éléments aléatoires.

Donc, disons simplement cela.

Et puis c'est et puis quelque chose comme cela, cela, cela et 33.

D'accord, ce sont simplement des choses aléatoires.

Maintenant, je veux trier cela, donc je vais simplement d'abord afficher.

Donc, je vais afficher, je vais dire tableau et alterner mon type de données de taille.

Donc, en fait, ma variable de taille.

Donc, je vais avoir la taille n ici, je vais dire la taille de n, je vais avoir le tableau et je vais dire la taille de et je vais avoir l'INT, cela va me donner la taille.

Maintenant, ce que je peux faire ici, c'est essentiellement avoir l'appel de la fonction d'affichage et ensuite la fonction triée, donc elle est appelée bubblesort.

Donc, je vais simplement la nommer bubblesort.

Je vais passer mon tableau, je vais passer ma taille.

Je vais afficher une fois de plus.

Donc, je vais afficher le tableau, et ensuite je vais passer la taille.

Maintenant, cela devrait fonctionner.

Donc, allons simplement à notre compilateur c++ ici, tapez simplement bubblesort bbls o r t, et nous disons point cpp.

Et donnons-lui simplement un nom comme hyphen o bl s o r t.

Et voilà, écrivez, compilez.

Et voilà.

Il a fonctionné, Whoa, qu'est-ce qui s'est passé ici, je pense que nous avons fait la même erreur exacte.

Donc, retournons simplement ici et voyons où nous avons fait une erreur.

D'accord, donc nous avons simplement oublié d'incrémenter sur les boucles sauvages pour nous souvenir de faire cela.

C'est vraiment important.

D'accord, donc i plus plus ici.

Donc, cela fait simplement sortir les boucles et cela ne cause pas de boucle infinie.

Donc, ici, et retournons simplement ici pour le compiler, le recompiler et l'exécuter à nouveau.

Vous pouvez voir que mon tableau original était 102 et ensuite 293, et ensuite 1939, et tout cela et ensuite une fois que nous avons passé notre bubblesort, il a en fait trié de 1138 102.

Et tout le chemin jusqu'au dernier élément.

Donc, c'était assez cool.

Uh, trier un tableau dans l'ordre croissant en utilisant le tri à bulles, le tri par sélection, parce que la méthodologie était essentiellement un peu différente.

Donc, je veux simplement vous montrer comment cela est implémenté dans une attente graphique.

Donc, l'implémentation du processus de bulle est essentiellement similaire à ce que nous avons fait avec le tri par sélection.

Mais en fait, dans l'ordre inverse, nous avons cette fonction d'échange qui se déroule, mais nous avons cette visualisation qui pourrait nous aider à comprendre comment ce processus fonctionne.

Donc, supposons que nous avons quelques valeurs aléatoires ici, nous avons trois, nous avons cinq, nous avons un, nous avons quatre, et nous avons, disons trois.

Maintenant, le processus de bulle va fonctionner comme ceci.

Donc, laissez-moi simplement passer par ici.

Et maintenant, voyons.

Donc, il va commencer par le bas, et il va comparer ces deux valeurs.

Maintenant, il voit que trois et quatre, maintenant que voulez-vous dire, c'est essentiellement des bulles, ce qui signifie que la partie liquide est en bas et la partie liquide est essentiellement plus lourde que la bulle, la bulle est plus légère, la bulle la fait flotter en haut.

Donc, lorsque vous comparez un liquide et une bulle, la bulle est plus légère, donc les bulles devraient être en haut.

Donc, ce n'est pas exactement la même chose.

Ils parlent des poids.

Donc, le poids de quatre est plus lourd que le poids de trois, donc quatre devrait être en bas, et trois devrait être en haut.

Donc, c'est un processus réel, ce qui se passe ici, c'est que la fonction d'échange sera appelée, et cela va être changé en trois.

Et cela va être changé en quatre.

Et ensuite après cela, la bulle va monter ici d'un niveau, donc elle va aller d'ici.

Et maintenant, elle va aller ici.

Donc, maintenant, elle va comparer trois et un.

Donc, trois, et un, en fait, qu'est-ce qui est différent maintenant. Donc, vous avez ici, c'est essentiellement un et trois, donc en fait, c'est bon, donc trois est plus lourd qu'un.

Donc, quand c'est bon, allez à nouveau, nous avons un et cinq.

Donc, cinq est plus lourd.

Donc, en fait, cinq ira en bas, et un ira en haut maintenant.

Maintenant ici, maintenant un et trois.

Donc, en fait, trois est plus lourd.

Donc, trois ira en bas à droite ici.

Donc, juste trois est en bas à droite ici, et ensuite le un sera en haut.

Donc, c'est un processus de bulle réel.

Et vous verrez 1353 et quatre, maintenant, nous avons fait notre processus ici et nous avons trié jusqu'à cette portion, il y a plus de processus.

Et vous devrez faire un autre processus de bulle.

Donc, encore une fois, vous allez devoir partir du bas.

Donc, vous allez vérifier comme ceci.

Donc, en fait, nous allons recommencer, et nous allons voir les valeurs une fois de plus.

Donc, pardonnez mon écriture, donc quatre, et ensuite nous avons trois, et nous avons cinq, puis nous avons trois à nouveau ici, et nous avons un, donc maintenant quatre et trois, qui est plus lourd, c'est bon, allez ici, comparez ces deux valeurs.

Maintenant trois et cinq.

Donc, trois et cinq, en fait, cinq est plus lourd.

Donc, cinq ira en bas.

Donc, cinq est ici, barrez simplement celui-ci, et cette portion aura trois maintenant.

Maintenant trois et trois, eh bien, en fait, c'est la même chose, égal, donc ce sera bon, donc un, bon, donc c'est bon, donc 13354.

Maintenant, un autre processus.

Donc, après un autre processus, donc nous allons avoir un autre processus.

Donc, laissez-moi simplement effacer tout cela, comment nous allons avoir encore un autre processus.

Et maintenant, cela devrait être notre dernier processus de bulle.

Donc, regardez simplement les valeurs à nouveau, ici, et ensuite ici, et ensuite ici, et ensuite ici.

Donc, c'est un, et ensuite c'est trois, et maintenant c'est trois aussi.

Et maintenant c'est cinq, c'est quatre, donc il va commencer par le bas, et vous voyez que cinq et quatre, eh bien, cinq, et quatre, c'est différent, c'est plus lourd, donc la partie plus lourde devrait être en bas et la partie plus légère devrait être en haut.

Donc, quatre va être ici, et ensuite cinq devrait être ici.

Donc, cinq, quatre, et ensuite 3311 pouce.

D'accord, donc c'est notre tableau trié exact.

Et c'est ainsi que nous allons trier notre tableau en tri à bulles, plus lent et cela dépend du nombre d'entrées.

Donc, cela pourrait varier et croître exponentiellement à mesure que les entrées augmentent.

Donc, c'était le processus de bulle.

D'accord, donc maintenant, passons au tri par insertion.

Cela est assez différent des deux autres que nous avons inclus pour l'instant, l'un était le tri par sélection, l'autre était le tri à bulles.

Donc, je vous encouragerais simplement à taper avec moi.

Et l'explication se fera côte à côte.

Donc, allons-y et incluons ce main et ensuite passons par ici et ensuite retournons le zéro.

D'accord, d'accord.

Maintenant, ce qui va se passer ici, c'est que nous n'allons pas avoir une fonction d'échange comme nous l'avons fait avec les autres, ce que nous allons avoir, c'est essentiellement quelques différences.

Maintenant, la différence est que nous allons avoir une fonction de tri par insertion, et le tri par insertion va essentiellement avoir un tableau, il va avoir une chose de plus qui va être à l'intérieur.

Donc, la première chose qu'il va avoir va être la taille.

Cela est assez similaire.

Et une chose ici, c'est qu'il va commencer à un et non à zéro, comme les autres, car nous supposons quelque chose et cette supposition est que la supposition est essentiellement qu'une partie du taux est déjà triée au préalable.

Et nous devons simplement insérer des éléments B dans ce tableau trié, et c'est ainsi que notre processus va être fait.

Donc, nous allons y aller et nous allons avoir une boucle while pour que je puisse vous dire qu'elle va aller dans une boucle while, elle va aller à la fin et elle va dire insérer Insérer ight.

Maintenant, ce sera la fonction qui sera appelée.

Et cette fonction va prendre un tableau, elle va prendre la taille, elle va prendre l'élément, qui va être la portion dont je vais parler.

Et ensuite cela va continuer à incrémenter i plus plus, n'est-ce pas ? Comme dans d'autres langages, comme I est égal, i plus un, peu importe, je n'arrive pas à obtenir le plus.

D'accord.

D'accord, donc comme cela.

Donc, I plus plus, peu importe, comme cela.

Donc, maintenant, ayons l'élément insert ICT, comment faisons-nous cet insert, je pense donc allons-y.

Et après cela, parlons simplement de l'insertion.

Donc, c'est en fait quelque chose qui est aussi void, et il va avoir l'élément d'insertion, donc juste ici, et maintenant à l'intérieur, nous allons avoir le tableau, nous allons avoir, essentiellement nous allons avoir la taille n, nous allons avoir la taille entière, qui est spécifiée ici, nous allons avoir cette variable clé, une variable intermédiaire qui va stocker notre emplacement, ou essentiellement la valeur de notre œil.

Et maintenant, il va dire int j, et ce j va être le dernier élément de ce tableau trié.

Donc, le dernier élément de cette manière triée va être i moins un, parce que j'ai en fait après le tableau trié, et i moins un, ce sera le dernier élément, donc nous allons avoir une boucle à nouveau, et nous allons avoir deux conditions.

Pour ce cas, nous avons j est supérieur ou égal à, nous avons j est supérieur ou égal à zéro.

Et nous avons aussi une autre condition que j devrait être en fait supérieur à la clé.

Donc, si j est supérieur à la clé, nous allons simplement continuer à boucler cela, donc pas un G j, ou ce que c'est une clé.

Donc, un sub j, donc laissez-moi simplement avoir ce huit, et ensuite un j ici, pas juste jouer j, d'accord, donc un sub j devrait être supérieur, et ensuite le J devrait être supérieur ou égal à, donc ce qui va se passer ici, c'est que huit sub j plus un, cela va être implémenté, et cela va être égal à j, et je tiens, je vais simplement vous enseigner cela, ne vous inquiétez pas.

Donc, maintenant, nous allons avoir j est égal à j moins un, maintenant cela va simplement continuer à décrémenter, aller vers le haut, comme une bulle va monter et monter et monter jusqu'à ce que vous atteigniez ce inférieur ou égal à zéro, ou si un sub j est gate, essentiellement, supérieur si c'est inférieur à quelque chose comme, si c'est inférieur, alors cela va simplement casser inférieur à la clé.

Et naturellement, ce qui va se passer ici, c'est que si cette condition est fausse, nous allons avoir un sub j plus un ou deux que nous essayons d'implémenter, et nous allons mettre cette chose clé à l'intérieur de celle-ci, cette valeur perdue.

Et maintenant, nous avons simplement cette fonction d'affichage, qui va être ici, ayons-la ici.

Donc, void, ayons un display.

Et ayons un tableau d'entiers.

Et ensuite ayons la taille de celui-ci.

Et ensuite ayons quelque chose qui va être le AI, il va commencer à zéro, il va aller essentiellement de while et il va simplement vérifier que est inférieur à n.

Et ensuite il va aller et dire que notre sortie de console va dire AR AR, en fait, ce n'est pas AR AR, cela va être un sub i, et cela va être AI.

Et ensuite il va y avoir une virgule juste là.

Et ensuite il y aura un N line, point-virgule juste ici.

Et en fait, pas cela, je ne veux pas cela, je veux simplement un point-virgule.

Et cela va s'incrémenter.

Donc, I plus plus.

Et ensuite nous allons avoir un comp end line ici.

Et maintenant, obtenons simplement quelques données de notre algorithme de tri précédent.

Comme un tri à bulles, obtenons simplement une partie des données, juste la portion de tableau, rien d'autre.

Donc, obtenons simplement cette portion ici.

Allons simplement ici, et nous allons simplement la coller ici.

Donc, je vais simplement aller ici, et nous allons simplement la coller ici.

Donc, la seule chose que je vais changer ici, tout est correct.

Je veux simplement trier en utilisant ma fonction.

Donc, je vais simplement l'appeler avec mon tri par insertion, en fait.

Oui, donc le tri par insertion va être appelé.

D'accord, donc le tri par insertion devrait être ici.

Voyons.

Oui, le tri par insertion est ici, il va aller et il va appeler celui-ci, insérer, n'est-ce pas ? Il va, il va effectuer une opération, et ensuite il va revenir plus plus, il va continuer à faire et il va continuer à appeler cet insérer tant de fois jusqu'à ce que la chose soit triée.

Et ensuite après cela, nous l'affichons simplement.

Donc, exécutons simplement ce code.

Je vais aller ici mon ci plus plus, et effaçons simplement cet écran.

Et compilons simplement, donc en fait, g plus plus est court Insertion Sort dot cpp.

Et ensuite nous pouvons dire, le drapeau hyphen O, et ensuite dire est court.

D'accord, cela devrait fonctionner, en train de compiler.

D'accord, donc il y a un avertissement ici et 25, aucune instruction de retour dans la fonction retournant non void. 25. Voyons. 25.

Où êtes-vous ? 25 est ici.

Et il devrait y avoir quelque chose ici, le tri par insertion n'a pas de type de retour.

Wow, devrait-on avoir un void, donc mettons simplement un void ici.

Et retournons simplement ici.

Et maintenant, compilons-le, recompilons-le.

Et voilà.

Maintenant, nous avons un ins short, donc Insertion Sort, et si je l'exécute, vous allez avoir ceci trié.

Donc, 192 290-319-3918 32 Yo, yo, yo 1138 102 293 311.

Et cela est également trié dans l'ordre croissant.

Maintenant, ayons l'implémentation.

Donc, c'est essentiellement un tableau, juste un échantillon aléatoire, et nous avons 379.

Et d'une certaine manière, cela est essentiellement trié à partir d'ici, comment cela s'est produit, juste aléatoirement, cela s'est simplement trié au préalable.

Et maintenant, notre is va être ici.

Donc, il va être après ce tri, et ensuite j va en fait être ici, rappelez-vous, j'ai dit que cela va être i moins un, donc c'est J, et le premier processus va se produire.

Donc, si je vais ici dans mon code, donc mon code est ici, et si je vois ici que cela va être le processus d'insertion, si cela a un tableau, cela a l'intérieur, cela a un élément I, et cela dit qu'une clé est égale à un sub i, donc il y aura une variable qui sera stockée, et j est égal à i moins un, et cela dit que j est supérieur ou égal à zéro, et un sub j est supérieur à la clé.

Donc, cela devrait fonctionner comme cela.

Et voyons si je pourrais implémenter ici, ici.

Donc, nous avons une variable clé.

Donc, cela aura une clé ici.

Donc, clé k, e, y, stockez cette valeur à l'intérieur, qui va être quelque chose à l'intérieur.

Donc, qu'est-ce que cela va être, cela va être la valeur de, cela va être un sub i.

Donc, c'est quatre.

Donc, quatre est ici.

Ignorez cela.

Maintenant, ce que vous allez faire, c'est essentiellement, vous allez vérifier la condition et la condition est vraie, pourquoi ? Parce qu'un sub j est supérieur ou égal à zéro.

En fait, si je, si je retourne ici, où suis-je ? D'accord, donc vous pouvez voir que c'est j est supérieur ou égal à zéro, c'est parfait.

Et ensuite un sub j est supérieur à la clé.

Maintenant, si je parle d'un sub j, maintenant si je parle de cela, laissez-moi simplement voir, un sub j est essentiellement ce neuf maintenant.

Et nous avons une clé, qui est quatre, donc ce j sub j est supérieur.

Donc, non, non, les fans où nous travaillons toujours.

D'accord, donc le travail, la chose va toujours fonctionner.

Si je retourne ici, nous allons avoir un sub j plus un est égal à un sub j.

Donc, cela signifie que nous allons avoir quelque chose que nous allons implémenter, donc un sub j va être ici.

Donc, nous allons aller ici.

Donc, cela va signifier que j plus un est cette portion, et il va l'égaler, il va signer cette ligne ici.

Et ce qui va se passer, c'est qu'il va aller moins un, donc j ne va plus être ici.

Non, il va aller ici.

D'accord, donc c'était maintenant un processus de cette boucle.

Donc, c'était un processus de celle-ci.

Et allons-y à nouveau.

Donc, un sub j est supérieur à ceci est supérieur à j est supérieur ou égal à zéro, et un sub j est supérieur à la clé, parce que la clé est pour nj sept.

Donc, c'est parfait.

Maintenant, retournons ici.

Et nous voyons qu'un sub j plus un est égal à un sub j, et nous avons j moins un un processus à nouveau, donc quelle que soit cette valeur, donc nous avons sept ici, ce sept va être maintenant ici.

D'accord, donc le J va aller là maintenant, et il va le supprimer.

Donc, vous pouvez voir qu'il y a encore ici à cet endroit.

Et vous pouvez voir que le quatre a été supprimé, donc nous n'avons plus cette valeur.

Qu'elle vient de changer en neuf.

Voir ici, c'est neuf.

Et d'où vient neuf ? Il vient de ici.

Donc, avec sept campervan est venu de ici, donc cela se passe, donc nous avons cette dernière valeur ici stockée dans notre clé.

Donc, c'était le but de la clé, bien, pas sympa clé.

Donc, maintenant, nous allons faire est essentiellement aller ici.

Et nous allons voir un sub j plus un, et il va, il va voir cette condition, est j supérieur ou égal à zéro.

Eh bien, c'est vrai.

Si je regarde cette position ici, elle est ici, elle est supérieure ou égale à zéro, mais elle est égale à zéro.

Donc, c'est vrai.

Mais la deuxième condition n'est pas vraie, pourquoi un sub j est supérieur à la clé.

Et en fait, ce n'est pas supérieur.

Comment ce n'est pas supérieur, c'est inférieur parce que c'est vrai sur cette clé est supérieur.

Donc, cela termine simplement cette boucle.

Et ce qui va se passer maintenant, c'est que la clé va être triée à l'intérieur de cette portion ici, qui est j plus un.

Donc, cette valeur de clé, qui est quatre, va être ici.

Maintenant, ce quatre va être ici, 3479.

Eh bien, cela est trié.

Et maintenant, cela va, cela va passer à une nouvelle position de i et cela va être un nouveau processus.

Donc, c'est ainsi que cela va commencer, si je regarde ici.

Donc, vous pouvez voir qu'un sub j plus un va être la clé et ensuite le processus recommence, si vous voulez le faire.

Et c'est ainsi que nous allons essentiellement le trier, insérer le tri, il va incrémenter sa valeur I à nouveau, il va être une nouvelle PlayStation, et ensuite après cette position, et ensuite après cela, nous l'avons inséré et ensuite le processus recommence encore et encore jusqu'à ce que le tableau entier soit trié.

Et ensuite nous obtenons cet ordre croissant.

Donc, j'espère que vous avez compris ce concept de tri par insertion.

Vraiment, si vous avez pris ce concept et globalement, comme, prenez une pratique de celui-ci, je sais définitivement que vous pouvez le faire.

Donc, ensuite, nous allons plonger dans un autre algorithme.

Plongeons dans l'algorithme de tri par fusion.

Donc, tapons simplement avec iostream namespace standard main.

Et le retour zéro point-virgule.

D'accord, donc créons quelques fonctions ici.

Et expliquons-les de la manière dont nous le faisons.

Donc, tout d'abord, trouvons notre chemin pour le tri par fusion.

Donc, comment cela va fonctionner est essentiellement que nous allons dire void, Mr g s o r t, et nous allons dire que nous allons avoir un tableau à l'intérieur, et nous allons avoir la taille de celui-ci.

D'accord, donc cela va avoir une autre fonction à l'intérieur, elle va appeler une autre fonction.

Et ce processus est appelé, est appelé, en fait, cela s'appelle une fonction wrapper, et elle va passer dans une fonction auxiliaire.

Donc, c'est une fonction wrapper.

D'accord, donc ce que nous allons dire, c'est que c'est merge sort, et il va avoir le tableau à l'intérieur, il va avoir la taille de ce tableau.

Et il va aussi avoir un autre paramètre supplémentaire.

Donc, la chose supplémentaire est qu'elle va avoir la taille, mais avant cela, elle va avoir une autre chose, elle devrait avoir l'index du premier élément, donc elle va être le tableau, l'index du premier élément, et ensuite la taille de cela, essentiellement, taille moins un.

Et c'est ainsi que le tri par fusion va être ici, nous allons avoir cette fonction auxiliaire appelée.

Donc, en haut, nous pouvons simplement spécifier notre fonction auxiliaire, donc une fonction AUXILY.

Et ce que nous allons dire ici, c'est que nous avons simplement le même void, Mr g, s, o, r t, et maintenant les mêmes paramètres d'entrée, où nous avons un tableau.

Donc, nous avons ce tableau d'entrée, nous avons essentiellement la valeur de départ, et nous avons la valeur de fin.

D'accord, ce sont essentiellement les index.

Et nous appelons cela la fonction auxiliaire, ou nous la connaissons aussi sous le nom de fonction d'aide.

Ce sont quelques-uns des noms que nous allons utiliser.

Donc, ayons un cas de base à cela.

Oui, je ne sais pas ce qu'est un tri par fusion, n'est-ce pas ? Maintenant, nous avons simplement dessiné la chose ici.

Donc, nous avons cette fonction qui appelle une autre fonction.

Un autre scénario ici, c'est essentiellement un même tableau.

Et d'une certaine manière, il est trié en section.

Donc, vous avez une première partie, qui est triée, et la deuxième partie est triée.

Et notre travail ici est de ne pas penser à cela comme deux tableaux, c'est un seul tableau.

Et d'une certaine manière, nous avons cette première partie triée, et nous avons la deuxième partie triée.

Et notre travail est de rendre cela trié en un seul trou.

Et comment nous pouvons faire cela, c'est le processus de fusion.

Donc, nous allons utiliser l'algorithme de tri par fusion pour faire cela.

Donc, ce que nous pouvons faire, c'est que nous devons savoir à l'avance comment la première partie est triée, ou la deuxième partie triée, et nous devons mettre une confiance, nous devons mettre la foi dans un processus.

Et ce thème est appelé récursion.

Et maintenant, c'est ce que nous allons appliquer.

Donc, vous allez vérifier, et le processus va se dérouler comme suit.

Donc, nous allons avoir ce premier élément deux, et nous allons vérifier cette troisième partie ici.

Donc, d'abord, ces deux sous-tableaux, et je vais dire deux et trois, lequel est le plus grand, je veux dire, lequel est le plus petit, donc essentiellement deux est plus petit, donc deux va être planté ici.

Et ensuite, cela va être incrémenté.

Donc, cet index de sous-tableau va être incrémenté.

Donc, il va être plus un, qui va être sept maintenant, et cette partie va rester la même, maintenant trois et sept vont être comparés.

Et nous pouvons voir que trois est plus petit, donc trois va être placé ici.

Et maintenant, cela va être incrémenté à quatre.

Donc, vous pourriez voir que quatre et sept vont être comparés, et nous avons quatre ici.

Donc, quatre va être et cela va être incrémenté à cinq, donc cinq, et sept, et cinq va maintenant être ajouté.

Donc, cinq va être ici.

Maintenant, cela va être 15, et sept, donc sept va être ici, donc sept va être ici maintenant 11 et 15, vous verrez 11 est plus petit, donc 11 va être ici.

Donc, cela va être incrémenté à 19.

Donc, nous avons 15 et 19.

Donc, maintenant nous avons 15 ici.

Donc, 15 va être ici.

Et ensuite nous avons cette comparaison 15 va être commise à plus plus.

Donc, nous avons 18 et 19.

Donc, qu'est-ce que c'est 18.

Donc, maintenant vous pouvez voir ici, nous avons supposé que cette partie est déjà pleine maintenant.

Maintenant, que faisons-nous ? Eh bien, maintenant, ce que nous allons faire, c'est essentiellement, cette dernière partie, nous allons simplement l'ajouter à la fin.

Donc, c'est notre processus ici, ce que nous allons faire, c'est ajouter ces 19 et 21 à la fin, comment nous allons faire cela.

Et vous pourriez voir par cela, c'est simplement trié dans notre manière d'ordre croissant.

Et c'est ce que nous avons requis.

Et comment faisons-nous cela ? Et vous me demanderiez, maintenant, si c'était formulé comme cela, pourquoi ne pas simplement mettre un algorithme de tri préexistant comme une fusion, comme quelque chose comme le tri par insertion, le tri par sélection ? Eh bien, ce processus va prendre plus de temps, et ce processus est beaucoup plus court.

C'est le cœur du tri par fusion.

Et c'est pourquoi cela le rend plus rapide.

C'est beaucoup plus rapide par rapport à n'importe quel algorithme de tri que nous avons discuté jusqu'à présent.

Donc, maintenant, retournons dans notre code.

Et maintenant, commençons à taper avec moi.

Donc, tout d'abord, ayons ce tri par fusion et à l'intérieur de celui-ci, nous avons un tableau, nous avons ce int s, nous avons ce int E, nous avons une fonction d'aide dans la condition, nous avons un cas de base, maintenant nous avons ce s supérieur ou égal à E.

C'est un cas qui n'est pas vrai.

Cela ne peut jamais être vrai.

Dans ce cas, il va simplement retourner.

Donc, c'est notre cas de base.

Et cela, vous pourriez dire que cela ne va simplement pas être vrai parce que le début n'est jamais supérieur ou égal à manger.

Cela signifie qu'il est simplement toujours logique que vous ayez un début, qui est inférieur ou égal à E, et je parle des index ici, et non de la valeur.

Donc, vous avez un début, comme par exemple, nous avons un début ici, et nous avons une fin ici, évidemment, ceux-ci sont des index, les index commencent à zéro jusqu'à n, à droite, et le C, commence à n moins un, il ne fait jamais l'inverse.

Donc, c'est simplement illogique.

Et maintenant, nous allons avoir l'implémentation Harry, nous allons trouver la valeur du point médian de ce tableau.

Donc, c'est notre fonction ici.

Donc, ce que nous devons faire ici, c'est essentiellement, laissez-moi simplement remettre ces parcelles en place, d'accord, donc notre processus ici est, nous devons trouver la valeur du point médian, qui est ici.

Donc, vous pouvez voir ici, si j'observe ici, que j'ai 1-234-567-8910, 10 éléments, et si je, si je vais d'ici, comme la valeur de début serait zéro index, et la dernière valeur, qui est neuf, et si je divise cette façon, deux, je vais obtenir un 4.5, à droite, et je vais obtenir la division entière de celui-ci.

Donc, je vais simplement obtenir une partie quatre, la partie décimale est simplement exclue.

Donc, nous allons avoir 401234, c'est notre quatrième index.

Donc, c'est notre quatrième index ici.

Et ce que je vais faire ici, c'est que je vais placer cette valeur.

Donc, essentiellement, c'est notre quatrième index.

Et nous allons, nous allons diviser cela ici.

Et maintenant, vous pouvez voir que c'est notre m, à l'extérieur, c'est notre m, et, et les choses qui sont avant vont être les choses.

Donc, 0123 va être quatre et ensuite après cela, c'est 01234.

Donc, c'est cinq ici, et c'est quatre, et c'est notre point médian.

Maintenant, supposons que nous avons ajouté quelque chose comme, avions un nombre impair, alors nous aurions des cas pairs ici, mais dans ce cas, nous n'en avons pas, mais c'est toujours notre processus.

C'est ainsi que cela va être implémenté.

Retournez ici, et nous avons ce mid.

Et cela va être une fonction simple où nous allons faire, cela va être s plus E.

Maintenant, cela va être l'index de début et le dernier index et nous divisons par deux, comme nous l'avons discuté.

Et je sais que c'est assez simple, parce que c'est n moins un, je vous l'ai dit ici, et c'est le dernier élément qui indique le dernier élément, et il va simplement le diviser par deux, ce qui donne un 4.5, il va être quatre parce que c'est une division entière.

D'accord, donc maintenant, ayons ce Merge Sort qui vous appelle en utilisant la récursion, ce dont je parlais.

Donc, il va commencer par un, c'est notre point de départ.

Attention ici, il va, c'est ce tableau, le point de départ est S, mais le point médian est maintenant M.

Pourquoi parce que maintenant nous allons essayer de diviser en deux sous-tableaux avec des processus triés.

Donc, nous allons appeler à nouveau.

Et la deuxième fois, nous allons avoir un tableau, il va commencer par m n et il va aller jusqu'à la fin.

Donc, ce sera non m mais n plus un, parce que maintenant nous allons avoir ce processus supplémentaire.

Ici, nous avons cette portion que nous voulons triée, et nous voulons que cette portion soit triée.

Donc, nous discutons simplement, pas cela, pas cette chose ici, pas cela pour l'instant, nous regardons simplement le haut.

Donc, je pense que vous avez compris le point ici, nous voulions trier de manière ascendante ici et de manière ascendante ici.

D'accord, donc ici, nous avons ce m plus un.

Et maintenant, nous appelons une fonction de plus.

Et cette fonction est essentiellement la fonction combinée.

Et la fonction combinée va être assez similaire à cela, nous avons un tableau A, nous avons le S qui est la valeur de départ, nous avons la valeur médiane qui est m, nous avons la dernière valeur qui est e et cette combinaison sera définie ici quelque part.

Donc, ayons cette combinaison définie.

Donc, maintenant, nous allons faire est essentiellement, nous allons dire void combine.

Et si je l'ai spécifié ici, je dirais int a, et nous avons ce tableau ici, nous avons un int s valeur de départ, nous avons un int et qui est la valeur médiane. Oubliez cela.

Et ensuite j'ai obtenu le dernier élément, qui est end.

Et ce que nous pourrions faire ici, c'est que nous voulons un tampon temporaire.

Et je vous dirai pourquoi, attendez un moment.

Donc, créons simplement un tampon ici.

Et ce qu'il va faire, c'est essentiellement obtenir une valeur du tas ou il va obtenir une valeur.

Donc, ce sera un tableau du tas que nous allons obtenir.

Et essentiellement, cela va représenter la taille totale du tableau fusionné, dont nous parlons.

Et ce que nous allons faire ici, c'est que nous allons avoir un kz aller à S et nous allons dire pendant que nous avons k inférieur ou égal à E et ce que nous faisons ici, c'est buffer Et nous disons buffer sub k est égal à a sub k.

Et nous pourrions dire k est égal à k plus un.

Maintenant, que voulez-vous dire par cela ? Maintenant, je vais vous dire ce que cela signifie.

Le problème est que nous créons un tampon temporaire que nous allouons à partir du tas.

Et ensuite nous allons le désallouer en utilisant le mot-clé Delete.

Mais avant cela, nous l'utilisons parce que nous ne voulons pas le réassigner dans ce tableau existant.

Donc, nous voulons qu'il soit essentiellement stocké.

Et ensuite nous voulons quelque chose ici.

Donc, je vais simplement dire cette portion ici, b, u, s, s, e r, c'est le tampon, cette portion, et cette chose entière, je parle de la chose entière.

Donc, c'est le tampon, et cela va être notre tableau de sortie.

Donc, cela va être le tableau trié, nous le faisons en deux choses séparées.

Parce que si nous balancions simplement un seul tableau, cela va causer des complexités, beaucoup plus de complexités que simplement copier les éléments.

Donc, supposons que nous avons ce tableau.

Donc, ignorez simplement cette partie, parce qu'elle n'est pas triée maintenant.

Et nous venons de créer un tableau dupliqué qui avait toutes les valeurs.

Donc, il a commencé à K, et il est allé, donc il a dit, zéro jusqu'à la valeur.

Dernier.

Donc, si je retourne ici, vous pourriez voir que k a commencé avec une valeur de départ, et il était inférieur ou égal à la valeur n.

Et il a simplement dit que buffer sub k est égal à buffer sub k.

Donc, a sub k, quelle que soit la valeur, où il va la stocker dans le tampon, donc il a simplement initialisé tous, et il a simplement k plus un jusqu'à la fin.

Donc, simplement copié, fait un duplicata, n'est-ce pas.

Donc, maintenant après cela, nous pourrions faire est que nous allons avoir quelque chose spécifié ici, juste après cela.

Donc, une fois qu'il est copié, bam, i est égal à s.

Maintenant, nous allons avoir une chose ici, qui est J, et nous allons dire m plus un.

Maintenant, je vais vous dire pourquoi nous avons fait cela.

Et nous avons aussi, qui est K.

Et nous avons dit que comme S, i est égal à s, revenez ici, et nous avons ce IO.

Et il va être ici, qui est la valeur de départ, donnez-moi simplement une autre couleur ici, je vais simplement prendre un peu plus sombre.

D'accord, donc j'ai ici, qui est ici.

Et le second, ce que nous avons, c'est ce mid, nous savons que, d'accord, donc l'autre que nous avons, j est égal à n plus un.

Donc, si je retourne ici, nous avons ce j est ici.

Et nous savons que c'est le point final ici, il, donc vous pouvez voir que cet AI doit aller en commit tout le chemin jusqu'à M, c'est son dernier élément.

Et ce j doit incrémenter tout le chemin jusqu'à la portion de fin ici.

Donc, c'est ainsi que nous allons comparer les valeurs comme deux et trois, lequel est similaire à planté ici, allez et commettez à deux plus sept.

Et ensuite nous allons dire sept et trois, qu'est-ce qui est plus petit, trois plus petit planté ici, et ensuite mettez le reste.

Donc, c'est le processus que j'essaie d'implémenter en code, je dois le cartographier.

Donc, c'est pourquoi j'utilise ce diagramme.

C'est ce que nous faisons.

Donc, nous allons avoir indiqué s, pendant que nous allons avoir une boucle while.

Et c'est ainsi que ce processus va se dérouler, I qui est cette valeur, ce que je vous ai dit, Ce ici est inférieur ou égal à m, et j est inférieur ou égal à E, ce processus va continuer.

Donc, si i inférieur ou égal à m, et nous avons j inférieur ou égal à E, nous voulons un processus en cours.

Donc, si c'est le cas, buffer, be u FF, er, FF er est E I, et ensuite nous avons inférieur ou égal à bu FF er sub j, si ce processus est fait, donc si un buffer sub i est inférieur ou égal à buffer sub k, alors ce que nous allons faire, c'est un sub k, ce processus dont je parlais, que si c'est inférieur ou égal, alors copiez-le simplement à l'intérieur de ce, Kate, puis le tableau qui est ici, nous voulons le trier, donc nous allons simplement le copier ici à travers le buffer.

Donc, c'est un bu FF, er sub i.

Donc, dans le cas où c'est inférieur, à droite, si c'est inférieur ou égal, et ensuite nous incrémentons simplement est égal à i plus un, juste ce que nous avons fait là-bas, juste ce que nous avons fait là-bas.

Donc, si ce n'est pas le cas, nous aurons simplement un else.

Et quand je mets quelque chose ici, donc laissez-moi simplement mettre ici, donc je vais simplement mettre ici, le cas ici est que a sub k, a sub k va être ici, et il va être égal à buffer.

Donc, il va être buffer, et ensuite nous allons avoir sub j ici.

Donc, nous allons avoir ce j ici, qui est un sub k, parce que si ce n'est pas le cas, il va être inférieur, à droite.

Donc, cela signifie qu'il est inférieur, mais s'il est supérieur à J, il va être là.

Et évidemment, nous allons avoir j qui s'incrémente, au lieu de s'incrémenter.

Donc, nous avons cela et nous avons k est égal à k plus un.

Laissez-moi simplement avoir cela.

Et maintenant, nous avons la condition ici.

Donc, c'est ce cas ici.

C'est une boucle while.

Et nous avons une autre boucle while après cette condition.

Maintenant, je vais vous dire la raison derrière cela.

Donc, nous avons cette boucle while et après cela, nous avons deux boucles while.

De plus, je vais vous dire pourquoi nous avons besoin de ces deux.

Le problème est que si nous comparons ces deux, comme, supposons que nous avions cet outil, et nous avions ce trois, nous comparons cela à deux était inférieur.

Et ensuite nous avons incrémenté.

Cela, nous faisons simplement plus plus, ne l'avons-nous pas fait, mais le cas où nous sommes venus ici à ce 19 et 21, comment ces deux viennent, ce tableau vient de se remplir, tout cela était plein, rappelez-vous cette portion, mais ensuite nous avons simplement ajouté ces deux derniers à l'intérieur de cela, comment faisons-nous ce processus automatique, ce processus automatique va être fait à travers deux boucles while, nous allons inclure, et cette condition est comme si est inférieur à bon, ou si j est inférieur ou égal à manger.

Maintenant, ce sont les deux conditions et regardez cela attentivement.

Donc, pendant que nous disons i est inférieur ou égal à m, donc si cette condition est comme, encore là, comme c'est vrai, comme elle a cassé.

Donc, le processus ici est que ces deux ne deviendront jamais faux ensemble, c'est toujours l'un d'eux et pas l'autre.

D'accord.

Donc, si ce cas est comme Jays écoutant, il est venu et ensuite après nous avons toujours i inférieur ou égal à m, ce que nous pourrions faire ici, c'est que a sub k, et c'est le même scénario, ce que nous avons fait avec l'exemple, a sub k est égal à nous allons dire, buffer donc nous avons obtenu la chose du buffer, et nous avons dit cela comme J.

Et ce que nous faisons, c'est essentiellement, en fait, nous allons avoir cela défini avec I parce que c'est l'œil ici.

Et nous allons définir cela avec l'œil, et ensuite nous allons faire, nous allons incrémenter i plus un, et nous allons incrémenter le K est égal à k plus un.

Et si les autres cas, ils sont comme, pendant que j est inférieur ou égal à E, nous allons avoir a sub k est égal à buffer.

Et nous allons avoir cela comme J.

Sub, voilà.

Et nous avons Jay Z allant à j plus un.

Et nous avons k est égal à k plus un, il va simplement incrémenter la valeur K.

Et vous savez déjà d'où k commence.

C'est k ici.

Donc, cette portion est K.

Et j va aller 1-234-567-8910.

Tout le chemin quand c'est fait.

Donc, il continue simplement à incrémenter, vous pouvez voir que j est ici, il est là.

Et c'est le processus qui se cache derrière.

Et ensuite une fois que nous avons terminé, nous ne voulons pas cette mémoire supplémentaire, nous la supprimons simplement.

Donc, nous supprimons simplement notre buffer et en utilisant cette syntaxe delete, c'est essentiellement que nous allons la désallouer de la mémoire.

Et c'est tout.

Maintenant, ayons simplement cette fonction supplémentaire dont nous avons besoin, c'est essentiellement, je pense, donc c'est une imprimée, donc Oh, j'ai oublié ma logique principale ici.

Je veux dire, donc c'est la moyenne, peut-être que je l'ai laissée en haut, oui, c'est une erreur courante.

D'accord, donc effacez simplement cette portion ici.

Et ayons simplement une fonction d'affichage en bas ici.

Donc, en bas de la valeur, ici, ayons une fonction d'affichage.

Donc, elle va être appelée void, nous allons avoir un display, et nous faisons essentiellement avoir un tableau, comme les autres petits, donc avoir la taille n.

Et nous allons avoir quelque chose qui va être implémenté, comme nous avons temporaire, et nous allons avoir cela associé à un sub.

Que fais-je x non en fait que i est égal à zéro, mon père.

Donc, nous allons avoir pendant que i est inférieur à n, et ensuite nous allons dire, la sortie de la console va dire AR AR, en fait, ce n'est pas AR AR, cela va être un sub i, et cela va être AI.

Et ensuite il y aura une virgule juste là.

Et ensuite il y aura un N line, point-virgule juste ici.

Et en fait, pas cela, je ne veux pas cela, je veux simplement un point-virgule.

Et cela va s'incrémenter.

Donc, I plus plus.

Et ensuite nous allons avoir un comp end line ici.

Et maintenant, ce que nous allons faire, c'est essentiellement exécuter le code ici.

Donc, obtenez un tableau aléatoire à nouveau.

Donc, laissez-moi simplement obtenir ce tableau, qui est ici, copiez ici, copiez et collez-le ici.

Et changeons simplement la chose ici, qui est l'insertion ou l'épée, nous allons avoir Mr. G, Mr. G, Mr. g sort, tri par fusion. Donc, retournons à notre compilateur c++, c++, Mr. g, s, o r t dot cpp, Ivan Oh, Mr. G, Mr. g, s, o r t, et compilé Mr. g s.o RT.

Et voilà, 110 et ensuite 100 à peu importe 293 et ensuite tout cela, et trié dans l'ordre croissant.

Donc, c'était tout avec le tri par fusion.

Et c'est beaucoup, beaucoup plus rapide par rapport à n'importe quel algorithme de tri que nous avons fait jusqu'à présent.

Donc, même le tri par sélection, le tri à bulles, le tri par insertion, même le problème que nous avons fait au début, parce que ceux-ci étaient de complexité temporelle, vieux n carré sur n carré sur n carré sur n carré.

Mais ce tri par fusion est d'une certaine manière plus rapide, parce qu'il fait la complexité temporelle.

Dans tous les n log de n, donc Oh, et ensuite nous avons n, et ensuite nous avons log, et ensuite nous avons ce n à l'intérieur.

Et c'est beaucoup, beaucoup plus rapide par rapport à n'importe quel autre algorithme de tri.

Maintenant, si vous obtenez comme un ensemble de tableaux à partir d'un fichier texte que je pourrais faire dans mes autres vidéos, donc restez à l'écoute.

Pour mes prochaines vidéos à venir sur ma chaîne, vous allez voir que nous allons avoir un fichier texte, et nous allons comparer à quel point cela est rapide par rapport à d'autres algorithmes de tri.

Parce que si nous avons ces algorithmes de tri O de n carré, ceux-ci vont prendre beaucoup, beaucoup plus de temps à mesure que la valeur d'entrée augmente, cela va croître exponentiellement.

Mais par rapport au tri par fusion, cela va être rapide comme l'éclair parce qu'il est dans tous les n log de n, quelle que soit la complexité.

Donc, j'espère que vous avez apprécié cette vidéo, j'espère que vous l'avez aimée.

Et assurez-vous de visiter ma chaîne qui s'appelle Coding Cleverly, où j'ai tant de contenu sur le c++, et j'ai fait des structures de données et des algorithmes.

J'ai fait de la programmation orientée objet, fait les bases, niveau débutant, programmation procédurale, et mon objectif est de compléter les structures de données.

Et ensuite après cela, j'ai avancé vers d'autres vidéos basées sur des projets ainsi que de nouveaux langages et technologies.

Donc, assurez-vous de vous abonner à cette chaîne.

Et oui, merci beaucoup d'avoir regardé.

J'apprécie vraiment le soutien.

Donc, merci beaucoup, et merci à Free Code Camp pour avoir mis ma vidéo sur leur chaîne.

Je l'apprécie vraiment.