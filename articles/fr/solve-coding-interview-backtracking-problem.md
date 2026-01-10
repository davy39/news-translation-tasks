---
title: Apprenez à résoudre les problèmes de backtracking des entretiens de codage
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-07-27T17:18:00.000Z'
originalURL: https://freecodecamp.org/news/solve-coding-interview-backtracking-problem
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/backtracking.png
tags:
- name: interview
  slug: interview
- name: youtube
  slug: youtube
seo_title: Apprenez à résoudre les problèmes de backtracking des entretiens de codage
seo_desc: Backtracking is an algorithmic technique that is often used to solve complicated
  coding problems. It considers searching in every possible combination for solving
  a computational problem. Coding interview problems can sometimes be solved with
  backtra...
---

Le backtracking est une technique algorithmique souvent utilisée pour résoudre des problèmes de codage complexes. Elle consiste à rechercher dans toutes les combinaisons possibles pour résoudre un problème computationnel. Les problèmes d'entretiens de codage peuvent parfois être résolus avec le backtracking.

Nous avons publié un cours complet sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à résoudre les problèmes de backtracking.

Lynn Zheng enseigne ce cours. Elle est ingénieure logicielle chez Salesforce et une excellente enseignante.

Vous apprendrez les principes généraux et apprendrez également à résoudre deux problèmes difficiles de LeetCode dans ce cours intensif.

Regardez le cours complet ci-dessous ou sur la [chaîne YouTube freeCodeCamp.org](https://youtu.be/A80YzvNwqXA) (1 heure de visionnage).

%[https://youtu.be/A80YzvNwqXA]

## Transcription

(générée automatiquement)

Lynne est une ingénieure logicielle chez Salesforce et une excellente enseignante.

Dans ce cours, vous apprendrez à résoudre les problèmes de backtracking, qui sont courants dans les entretiens et les défis de codage.

Bonjour à tous.

Je suis Leanne.

Je suis ingénieure logicielle, développeuse de jeux à mes heures perdues et récente diplômée de l'Université de Chicago.

Bienvenue dans ce cours sur la résolution des problèmes de backtracking.

Que vous soyez nouveau dans les entretiens de codage ou que vous ayez déjà de l'expérience avec les problèmes de backtracking, ce cours intensif est fait pour vous.

Nous apprendrons un modèle polyvalent qui vous aide à résoudre tout type de problèmes de backtracking, et nous appliquerons ce modèle à des problèmes classiques, comme le problème des huit reines ou le problème du solveur de Sudoku.

C'est exactement le modèle que j'utilise pour mes problèmes de codage lorsque je développe des algorithmes pour mes jeux, ou même une fois dans mes recherches sur un problème d'optimisation non convexe.

J'espère que vous êtes excité et plongeons directement dans ce modèle polyvalent.

Vous pouvez trouver ce modèle dans mon GitHub, le lien est dans la description de la vidéo ci-dessous.

Commençons par quelques mots-clés et concepts des problèmes de backtracking qui nous aideront à mieux comprendre le modèle.

Le premier mot-clé est l'état.

Essentiellement, un problème de backtracking vous demande de trouver un état valide.

Prenons l'exemple des N reines que nous résoudrons plus tard dans cette vidéo.

Un exemple d'état est simplement de placer arbitrairement n reines sur un plateau de n par n.

Par exemple, ici nous plaçons quatre reines sur un plateau de quatre par quatre.

En revanche, un exemple d'état valide nécessite que les reines soient placées de manière à ce qu'elles ne puissent pas s'attaquer mutuellement.

Si vous n'êtes pas familier avec les règles des échecs, ne vous inquiétez pas.

Les mouvements des reines sont assez simples.

Une reine peut se déplacer horizontalement, verticalement ou en diagonale.

Par conséquent, pour que le placement des N reines soit valide, elles ne peuvent pas se trouver sur la même ligne, la même colonne ou les deux diagonales.

Alors, comment construisons-nous un état valide comme celui-ci ? Eh bien, nous construisons à partir des états précédents.

Supposons que nous commençons par un plateau vide de n par n où aucune reine n'est présente, nous pouvons placer notre première reine arbitrairement, où nous voulons.

Disons que nous la plaçons ici.

Ensuite, où pouvons-nous placer une deuxième reine, vous pouvez voir maintenant que nos choix sont limités.

Ou en termes de backtracking, nos états candidats sont limités.

Parce que nous avons placé la première reine ici, cette colonne entière, cette ligne entière et les deux diagonales ne sont pas disponibles pour les nouvelles reines.

Disons que nous plaçons simplement la deuxième reine ici où c'est disponible.

Ensuite, nous essayons de voir où nous pouvons placer la troisième reine.

Nos candidats sont maintenant plus limités parce que nous avons placé la deuxième reine ici, cette colonne, cette ligne et cette diagonale ne sont pas disponibles.

Donc notre troisième reine ne peut aller que ici.

Enfin, plaçons la quatrième reine.

Parce que cette troisième reine est ici, elle bloque cette diagonale et cette ligne et cette colonne, laissant notre quatrième reine à placer ici.

Super.

Maintenant, cette disposition globale est-elle une solution valide telle qu'aucune reine ne peut s'attaquer mutuellement ? Eh bien, nous l'avons déjà vu dans nos vérifications.

Ainsi, nous avons trouvé une solution valide à ce problème des N reines.

À titre de contre-exemple, considérons si nous avons placé les deux premières reines comme ceci.

Maintenant, toutes ces cellules marquées en rouge sont disponibles, et il ne nous en reste qu'une pour la troisième reine et nous savons où placer la quatrième reine.

Cela signifie que la recherche d'états réussie échoue à conduire à une solution valide.

Et c'est à peu près tout ce qu'il y a à savoir sur les états, l'identification des candidats pour construire l'état suivant et la validation d'une solution finale.

Maintenant, voyons comment ces procédures sont définies dans notre modèle.

Il y a quatre fonctions dans notre modèle.

Les trois premières, ainsi que les candidats d'état, recherchent nos fonctions d'aide.

La dernière et la plus importante, donc c'est le point d'entrée de notre programme.

La fonction seule est en effet celle qu'un petit problème vous demande d'écrire.

Elle est responsable du retour des solutions valides.

Regardons les fonctions d'aide une par une.

Cet état valide, cette fonction prend un état et retourne un booléen.

Il valide si un état peut être utilisé comme solution finale dans notre problème de reines. L'état est une solution validée.

Si toutes les n reines sont placées sur un plateau, et qu'aucune d'entre elles ne peut s'attaquer mutuellement, obtenez des candidats.

Cette fonction trouve une liste de candidats qui peuvent être utilisés pour construire l'état suivant de la recherche.

C'est une fonction récursive.

Elle a causé les deux fonctions d'aide précédentes et vérifie si l'état est une solution valide à notre problème de backtracking.

Si c'est le cas, elle enregistre la solution en faisant une copie profonde de cet état.

Notez que nous avons besoin d'une copie profonde, car nous continuerons à modifier l'état au fur et à mesure de notre recherche.

Mais nous avons besoin d'un instantané statique de l'état valide ici.

Cette ligne de retour est commentée, car selon la nature du problème, nous pourrions avoir besoin de trouver toutes les solutions valides ou seulement une.

Si nous n'avons besoin que d'une seule, nous pouvons retourner dès que nous l'avons trouvée.

Sinon, nous continuons jusqu'à ce que nous ayons épuisé tous les états de recherche possibles.

Continuez vers le bas ici.

Si l'état n'est pas encore une solution valide, nous trouvons des candidats pour construire l'état suivant.

Rappelons que les candidats retournent une liste de candidats.

Pour chacun d'eux, nous ajoutons le candidat à l'état.

Dans un problème de quiz.

Par exemple, supposons que notre état ne contient que la position de la première reine.

Ici, nous ajoutons une position candidate pour le deuxième point.

Maintenant, nous prendrons cet état modifié et nous récurserons dessus en appelant la méthode de recherche sur cet état modifié.

Si l'état modifié est valide, la solution est enregistrée.

Comme ici, sinon, la fonction de recherche récupère les candidats pour cet état modifié et récurse.

De plus, finalement, pour certains états, il n'y a plus de candidats possibles.

Pensez à l'exemple où nous ne pouvons placer une quatrième reine nulle part, car tous les espaces ont été occupés.

Après être revenu de la recherche récursive, nous avons restauré un état modifié à l'original en supprimant le candidat de l'état.

Encore une fois, l'exemple des reines, nous annulons le placement de la deuxième requête.

Et maintenant, nous n'avons plus que la première requête.

Donc, cela commence avec une liste vide de solutions et un état vide.

Il coûte la recherche sur un état et cette liste de solutions vides.

La recherche remplira finalement cette liste de solutions vides, puis retournera la liste des solutions.

Et rappelez-vous, c'est la fonction que le problème de code nous demande d'écrire.

Nous utilisons ce modèle en gardant à l'esprit que ce n'est qu'un modèle.

Donc vos fonctions d'aide, ainsi que l'état, obtiennent des candidats, ils peuvent prendre des paramètres supplémentaires.

La recherche peut également retourner un booléen indiquant si une solution a été trouvée et retourner tôt s'il y a une seule solution globale valide, comme dans un problème de Sudoku que nous verrons éventuellement.

Cela conclut notre brève introduction au modèle.

Ensuite, résolvons le problème des reines en codant.

Ici, nous codons uniquement le problème 51 des N reines, qui est un problème de cœur d'Alico.

Lisons d'abord l'énoncé du problème, étant donné un entier, et nous voulons retourner toutes les solutions distinctes au puzzle des n reines, et nous pouvons retourner la réponse dans n'importe quel ordre.

Et Alico a un format spécifique pour nous représenter le plateau.

Pour l'exemple des quatre reines, voici les deux solutions valides.

Et ici, avec les notes, la première case de la première ligne n'est pas occupée, la deuxième case est occupée par une reine, la troisième n'est pas occupée, la quatrième n'est pas occupée.

Et sur la deuxième ligne, les trois premières cases ne sont pas occupées, et la dernière est occupée par une reine, et ainsi de suite.

Et dans le cas où n est un, la reine ne peut être que sur une seule grille.

Donc c'est la solution.

Avant de sauter dans le code, réfléchissons d'abord à la manière dont nous pouvons représenter ce problème.

Logiquement.

Nous pourrions être tentés de représenter cette structure de données de plateau comme un tableau 2d, mais c'est en fait un peu gaspillage d'espace.

Puisque aucune reine ne peut être sur la même ligne ou la même colonne, nous pouvons simplement garder une liste d'un jour qui suit la position de la reine dans chaque ligne.

Concrètement, pour cet exemple ici à gauche, la reine est dans la deuxième cellule de la première ligne, donc le premier index est un.

Pour la deuxième ligne, l'index est trois, puisque la reine est dans la quatrième cellule, et ici c'est zéro.

Ici c'est deux, suivant la même logique.

Pour l'exemple de droite, le premier index est deux, le deuxième index est zéro, le troisième est trois, et le dernier est un, parce que la troisième cellule, la première cellule, la quatrième cellule, et la deuxième cellule.

Donc c'est la manière dont nous représentons chaque état comme une liste 1d.

Pour ce problème de backtracking.

Maintenant, je vais prendre mon modèle et le mettre dans le code.

Je vais déplacer la méthode surf en haut.

Comme déjà mentionné, la méthode surf est essentiellement celle que le code nous demande d'écrire.

Donc pour le problème des reines et du savon, nous adapterons simplement la fonction de savon aux solutions qui est initialement une liste vide, car nous pouvons retourner toutes les solutions valides dans n'importe quel ordre, puis mon état de départ est simplement une liste vide car nous n'avons pas encore placé aucune des reines sur le plateau.

Maintenant, nous appelons self dot search sur cette date, en lui donnant une liste de solutions à ajouter et le paramètre n pour les N reines.

Après que la recherche soit terminée, nous retournons aux solutions.

Allons-y et supprimons cette partie.

Super.

Maintenant, nous allons écrire cela ainsi que la fonction d'état, elle prendra comme paramètre self, state et add pour que l'état soit valide, il doit placer toutes les n reines sur le plateau.

Donc si la longueur de l'état est n, alors nous savons que nous avons déjà placé toutes les n reines sur le plateau.

Quant à la condition où aucune reine ne peut s'attaquer mutuellement, nous la gérerons dans la fonction get candidate.

Essentiellement, nous ne retournerons que les candidats qui signifient tous les scores valides qui ne seront pas attirés par les reines précédemment placées self state.

Super.

Donc ici, nous construisons des candidats en fonction de l'état qui nous a été donné.

S'il n'y a pas d'état, ce qui signifie que nous commençons par un plateau vide, nous pouvons placer la première requête n'importe où nous voulons.

Donc si ce n'est pas l'état, nous retournons tous les indices possibles.

Si l'état n'est pas vide, nous trouvons la position suivante dans cet état à remplir la position comme la longueur de l'état.

Si nous avons déjà placé la première reine, nous voulons placer la deuxième requête.

Donc les candidats commencent initialement par tous les indices et ensuite nous réduisons les candidats qui ne sont pas valides.

J'utilise un ensemble car c'est mieux que de parcourir une liste et un ensemble garantit l'unicité.

D'accord, réduisons les candidats qui placent la reine dans les attaques.

Donc pour la ligne, la colonne énumère l'état avec le rejet de l'index de colonne s'il est occupé, donc les candidats que cette partie rappelle que notre état enregistre l'index de colonne pour chaque ligne.

Maintenant, nous discutons des diagonales.

Donc ce test est la distance entre la position et un index de ligne.

Parce que nous essayons de mettre une reine dans la deuxième ligne, maintenant que nous avons déjà rempli la première ligne, nous la voulons à la place qui ne peut pas être attaquée par la première reine en diagonale.

Donc celle-ci est hors de question.

Et c'est la colonne plus la distance.

Celle-ci est également hors de question et la colonne moins la distance.

Et à la toute fin, nous retournons les candidats.

Maintenant, définissons notre fonction de recherche récursive est votre prise d'états de solution de solutions, et nous adaptons simplement le modèle.

Donc si self.is valid state state, et nous l'ajoutons simplement aux solutions, et nous retournons.

Sinon, si nous descendons ici, pour les candidats, un sel de candidats d'état, et nous récursons.

Parce que notre état est dans la liste et n'est plus défini, nous faisons append candidate, puis appelons self dot search, state solutions, et it puis pour restaurer l'état modifié à notre original repop le dernier entrée.

Super.

Donc c'est la seule chose dont nous devons nous occuper, car lico veut que nous produisions des chaînes.

Et ici nous avons une liste d'indices de colonnes.

Donc définissons quelques fonctions d'aide supplémentaires ici.

State to string state, nous attendons que la sortie soit exactement comme ici.

Donc voici comment nous convertissons notre liste d'indices.

Pour cette sortie de chaîne spécifiée légèrement code, le retour total est simplement une liste pour I am state parce qu'un signifie que la reine est dans la deuxième cellule et les autres cellules sont vides, nous ajoutons simplement les chaînes pour les cellules vides ainsi qu'une chaîne pour le code de la reine cat knows ensemble pour obtenir la valeur de retour.

string est ce point signifiant le carré vide fois i plus la position de la reine était les cellules vides restantes.

Et rats straight.

were returned direct.

Et voici self solution at Penn State copy.

Nous faisons state string et string est produit par self dot script to string sticked.

Super.

Exécutons maintenant le code exemple pour voir comment nous nous en sommes sortis.

D'accord, cool.

Il semble que notre sortie soit acceptée.

Soumettons et voyons si nous pouvons passer tous les cas de test. Super, vous pouvez voir que notre temps d'exécution est meilleur que presque 70 % des soumissions et que l'utilisation de la mémoire est meilleure que 7 % des autres soumissions.

Nous utilisons définitivement de la mémoire à cause de la récursivité, mais c'est tout à fait acceptable pour les problèmes de backtracking.

Ensuite, nous résoudrons un autre problème de cœur d'aliquoter appelé le problème du solveur de Sudoku.

Nous sommes maintenant uniquement co-problème 37 le problème du solveur de Sudoku, qui est un problème difficile.

Si vous ne savez pas déjà ce qu'est un puzzle de Sudoku, vous pouvez lire la description.

Donc une solution de Sudoku doit satisfaire toutes les règles suivantes.

Chacun des chiffres de un à neuf doit apparaître exactement une fois dans chaque ligne.

Et chaque colonne.

Aussi neuf des trois par trois sous-boîtes de la grille, et liko utilise le caractère point pour indiquer les cellules vides.

Donc par exemple, ici, le code veut que nous écrivions un programme qui remplit ce puzzle de Sudoku.

De manière valide, le plateau est représenté comme un tableau 2d de chaînes, certaines peuvent être des nombres, certaines cellules vides, et liko veut que nous résolvions le problème et modifiions le plateau en place.

Les contraintes ne sont pas parce que c'est un problème de Sudoku, la forme est neuf par neuf.

Et chaque cellule est soit une chaîne de chiffres, soit la chaîne vide.

Et il est garanti que le plateau d'entrée n'a qu'une seule solution.

Donc nous pouvons retourner tôt.

Si nous trouvons une seule solution.

Laissez-moi copier-coller mon modèle et sauter dans le problème.

D'accord, donc encore une fois, nous adoptons la fonction de trempage comme ceci, parce qu'elle nous demande de ne rien retourner et de simplement modifier le port en place, je pense que nous devons simplement faire socket search board.

Et puis nous nous débarrasser de cette petite fonction.

Je vais devoir définir quelques constantes ici.

Donc la forme est neuf par neuf.

La longueur de la grille est trois par trois, si nous essayons de valider les sous-boîtes, et vide est représenté comme ce point ici.

Et toutes les chaînes de chiffres sont comme faux.

Donc l'écran numéro quatre nombre dans la plage.

Un shape, plus un.

Donc cela nous donne la chaîne de un à neuf.

Et je vais l'envelopper dans un ensemble, car l'ordre n'est pas important.

Et je sais que je vais en avoir besoin lorsque je traverse le Great.

Super.

Donc commençons par écrire que la fonction d'état valide.

Donc elle devrait prendre self et le board et vérifier si le board est une solution valide.

Donc validons d'abord toutes les lignes.

Pour la ligne a, je vais simplement définir une fonction d'aide plus tard.

Donc faisons d'abord soft get rows, qui retourne chaque ligne du board une par une.

Si, si ma ligne est équivalente à tous les chiffres, c'est une ligne valide.

Sinon, c'est une ligne invalide et le board n'est pas valide.

Si ce n'est pas le cas, la ligne est égale à soft digit.

retourner faux valider.

De même, nous validons les colonnes, les appels retournent faux.

Ou enfin, nous validerons les sous-boîtes.

Pour la grille, la grille, ou.

Et si toutes les lignes sont validées, toutes les colonnes sont validées et toutes les grilles sont validées sans causer ce faux retour déjà, nous retournons vrai, ce qui signifie que le board est une solution valide.

Maintenant, écrivons pour obtenir des candidats.

Donc self board a row et la colonne, j'utilise une ligne et la colonne parce que pour une cellule, je veux savoir quelle ligne et quelle colonne elle est toutes pour déterminer quels chiffres ont déjà été utilisés, et quels sont ceux qui nous restent à utiliser comme prochain état.

Donc les chiffres utilisés sont un ensemble de chiffres.

Et je vais supprimer les chiffres utilisés supprimés par la même ligne.

Donc les chiffres utilisés. Mise à jour self. Obtenir la ligne, c'est une autre fonction d'aide que je définirai plus tard, les chiffres utilisés par cette même colonne.

Donc utilisé la mise à jour self. Obtenir la colonne quatre, et la colonne supprimée, les chiffres utilisés par le même par cette boîte de sous-totaux de trois par trois, les budgets, la mise à jour get graded roll column.

Donc nous devons identifier pour une vente arbitraire, laquelle est sur le tableau de bord.

Et enfin, parce que nous avons peut-être déjà utilisé la chaîne vide, ici, lorsque nous faisons les mises à jour, nous soustrayons celles de nos chiffres utilisés.

Vide est la constante que nous avons définie pour la chaîne vide.

Et les candidats sont simplement ce qui nous reste à utiliser.

Donc cela inutile et cela conclut notre fonction get candidates.

Maintenant, nous passons à la recherche.

Parce que nous n'avons qu'une seule solution, nous n'en avons pas besoin, la liste des solutions ici.

Donc, donc forth.

Nous avons Isabel à l'étape.

Donc si self.is valid state board, nous retournons true solution.

Sinon, nous trouvons le prochain emplacement vide et faisons une supposition.

Donc pour l'index de ligne, l'énumération de ligne ou l'index de colonne, l'élément réel énumère la ligne.

Si l'élément est la chaîne vide, donc soft, cet espace vide si c'est vide, trouve les dates pour construire un X ray.

Prochaine date candidate a self. Obtenir les candidats board.

Maintenant que nous avons l'index de ligne et l'index de colonne, nous les passons, nous modifions le board en place comme le problème nous l'a instruit de faire.

Donc.

candidat, rappelez-vous que le candidat est simplement l'une des chaînes de chiffres.

Et parce que ici notre recherche retourne un booléen, si l'une des recherches se termine effectivement, cela signifie que le board a été modifié en place, et notre problème est résolu.

Donc c'est résolu est maintenant égal à self. Recherche.

Et juste pour ajouter quelques commentaires ici, nous récursons sur le côté MADI.

Si c'est le cas, si c'est le cas, maintenant nous retournons simplement à la signification que la recherche entière est terminée.

Sinon, nous faisons tous les mauvaises suppositions.

Et recommencez.

Donc nous faisons en sorte que cette entrée redevienne la chaîne vide qu'elle était.

Et ici nous avons épuisé tous les candidats.

Mais aucun ne résout le problème.

Nous retournons faux car c'est une succession invalide de recherches.

Et si aucun emplacement vide au départ, cela retournera simplement.

Maintenant, nous pouvons nous débarrasser de ce code standard de notre modèle.

Maintenant, la structure est assez claire.

Et tout ce que je dois faire est de remplir ces fonctions d'aide.

Fonctions d'aide pour récupérer les lignes, les colonnes et les groupes.

Donc voici mes fonctions d'aide pour récupérer les lignes, les colonnes et les grilles.

C'est assez simple car notre board est simplement un tableau 2d.

Et pour récupérer la cape row, column, ou grid à nos indices de ligne et de colonne centraux, nous faisons essentiellement des indices très intelligents et parfois nous nous appuyons sur la puissance des outils.

Je vais poster mon code complet sur mon GitHub, le lien est dans la description, donc vous pouvez digérer ces fonctions d'aide par vous-même.

Maintenant, exécutons le code et voyons ce que nous obtenons.

Super, notre sortie est acceptée, soumettons et testons-la contre tous les cas de test.

Génial.

Avec ce modèle, nous avons résolu deux problèmes difficiles de lico.

Pour résumer, un problème de backtracking consiste à trouver des états valides.

Pour résoudre un état valide, nous identifions les candidats qui satisfont les contraintes du problème et les utilisons pour construire notre état actuel.

Une fois qu'un état modifié est valide, nous l'ajoutons comme solution finale.

Maintenant que nous avons résolu deux problèmes, résolvons un autre problème de backtracking.

Rappelons que nous avons ces quatre fonctions, ainsi que l'état est une fonction d'aide avec une valeur de retour booléenne qui valide si un état donné est une solution finale.

Get candidates est une autre fonction d'aide retournant une liste de candidats satisfaisant la contrainte du problème basée sur notre état actuel.

Search est une fonction récursive ou coûte les deux fonctions d'aide ainsi que l'état et obtient des candidats et récurse sur elle-même.

Enfin, solve est la fonction qu'un autre problème lico vous demande d'écrire, elle ne fait rien de fantaisiste autre que l'initialisation d'une liste vide de solutions.

Et puis à l'état et aux collègues de recherche sur eux.

Pour plus de problèmes de pratique sur le backtracking, allez sur leak co.com et intacs recherchez backtracking.

Cela filtre une liste de questions qui partagent toutes une idée de backtracking.

Vous voyez, nous avons déjà résolu Sudoku solver, et n queens.

Si vous cherchez un problème de difficulté moyenne, je recommande le problème des sous-ensembles.

Il s'agit de trouver tous les sous-ensembles possibles ou les ensembles de puissance souvent donnés un tableau d'entiers.

Il est assez facile d'identifier un problème de backtracking lorsque nous devons trouver toutes les solutions possibles et pouvons retourner une solution dans n'importe quel ordre.

Comme vous pouvez le voir, dans les détails de ma soumission, j'ai résolu le problème des sous-ensembles en utilisant le modèle exact.

Au fur et à mesure que vous passez par de plus en plus de problèmes légaux et testez votre compréhension du modèle, vous serez mieux préparé à identifier un problème de backtracking une fois que vous en rencontrerez un dans vos entretiens de codage.

Cela conclut notre vidéo et le seul cours intensif dont vous aurez jamais besoin pour résoudre les problèmes de backtracking lors de vos entretiens de codage.

Pour plus de contenu comme celui-ci, veuillez vous abonner à ma chaîne YouTube, liens ci-dessous.

Je poste également des tutoriels de projets de formulaire et des démos de développement de jeux sur ma chaîne.

Mon dernier tutoriel concerne la création d'un chatbot IA Discord avec la personnalité de votre personnage préféré en utilisant entièrement des technologies basées sur le cloud, et je suis sûr que vous l'apprécierez.

Merci d'avoir regardé et bonne chance pour la préparation des entretiens de codage.