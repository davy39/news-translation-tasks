---
title: Qu'est-ce que la recherche binaire ?
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-07-07T13:57:56.000Z'
originalURL: https://freecodecamp.org/news/what-is-binary-search
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/binarysearch.png
tags:
- name: C++
  slug: c-2
- name: youtube
  slug: youtube
seo_title: Qu'est-ce que la recherche binaire ?
seo_desc: 'Binary search is a common algorithm used in programming languages and programs.
  It can be very useful for programmers to understand how it works.

  We just released a binary search course on the freeCodeCamp.org YouTube channel.
  You will learn how to i...'
---

La recherche binaire est un algorithme courant utilisé dans les langages de programmation et les programmes. Il peut être très utile pour les programmeurs de comprendre comment il fonctionne.

Nous venons de publier un cours sur la recherche binaire sur la chaîne YouTube freeCodeCamp.org. Vous apprendrez comment implémenter la recherche binaire en C et C++, mais les concepts s'appliquent à n'importe quel langage de programmation.

La recherche binaire est un algorithme de recherche qui trouve la position d'une valeur cible dans un tableau trié. La recherche binaire compare la valeur cible à l'élément central du tableau.

Le cours a été développé par Harsha et Animesh de MyCodeSchool. MyCodeSchool est l'une des plus anciennes chaînes logicielles sur YouTube. Animesh travaille actuellement comme ingénieur dans l'équipe de recherche de Google. Harsha était le programmeur indien le mieux classé sur la plateforme de programmation compétitive Top Coder.

MyCodeSchool a une histoire inspirante et triste. Vous pouvez en lire plus [ici dans cet article écrit par Quincy Larson](https://www.freecodecamp.org/news/mycodeschool-youtube-channel-history/).

Voici les sujets abordés dans ce cours :

* Qu'est-ce que la recherche binaire ?
* Implémentation et erreurs courantes
* Implémentation récursive
* Trouver la première ou la dernière occurrence d'un nombre
* Compter les occurrences d'un nombre dans un tableau trié avec des doublons
* Combien de fois un tableau trié est-il tourné ?
* Rechercher un élément dans un tableau circulaire trié

Regardez le cours complet ci-dessous ou [sur la chaîne YouTube freeCodeCamp.org](https://youtu.be/KsoUiNv1SZA) (1,5 heure de visionnage).

%[https://youtu.be/KsoUiNv1SZA]

## Transcription

(autogénérée)

Dans cette leçon, nous allons parler de l'un des algorithmes les plus célèbres et fondamentaux en informatique, la recherche binaire. Nous trouvons l'application de la recherche binaire dans un grand nombre de problèmes dans une grande variété de problèmes en informatique.

Mais ici, essayons de l'apprendre sous sa forme la plus simple.

Et pour ce faire, nous allons d'abord définir un problème. Le problème est le suivant : étant donné un tableau trié d'entiers, un tableau trié signifie que les éléments du tableau sont disposés soit dans l'ordre croissant soit dans l'ordre décroissant comme dans ce tableau. Ici, les éléments sont disposés dans l'ordre croissant. Disons que le nom de ce tableau est a et la taille de ce tableau est neuf.

Nous avons donc un index commençant à zéro jusqu'à huit.

Maintenant, étant donné un tel tableau et un nombre ou un entier x, nous voulons savoir si x existe dans ce tableau ou non.

Et si x existe dans ce tableau, alors nous voulons trouver la position à laquelle x existe dans ce tableau.

Par exemple, si x est à un, existe-t-il même dans le tableau ? Oui, il existe même dans le tableau et il existe à l'index sept. Est-ce que 25 existe dans le tableau ? Non, 25 n'existe pas dans le tableau. Est-ce que 21 existe dans le tableau ? Oui, 21 existe dans le tableau à la position trois à l'index trois.

Maintenant, quelle serait la logique pour savoir si x existe dans ce tableau ou non ? Une approche la plus simple peut être que nous pouvons scanner tout le tableau pour trouver le nombre souhaité.

Nous commençons donc à l'index zéro et comparons cet élément avec x.

S'il est égal à x, alors nous avons terminé notre recherche, nous avons trouvé l'élément dans le tableau.

Si ce n'est pas le cas, nous passons à l'élément suivant.

Et nous continuons à comparer avec l'élément suivant jusqu'à ce que nous ayons terminé avec le tableau ou que nous trouvions le nombre.

Donc, disons que si nous voulions trouver 63 dans ce tableau, alors notre recherche sera terminée lorsque nous atteindrons l'index six. Nous commençons à l'index zéro et notre recherche sera terminée à l'index six.

Si nous voulions trouver un 25, notre recherche sera terminée à l'index huit avec la conclusion que 25 n'existe pas dans le tableau.

Cette approche fonctionnera indépendamment du fait que le tableau soit trié ou non.

Et si je dois écrire le code pour cela, ce sera assez simple.

Disons que je veux écrire une méthode de recherche qui prend un tableau A, sa taille N et l'élément, désolé, le nombre x à rechercher, et le code serait que nous exécuterons une boucle commençant à zéro jusqu'à n moins un.

Donc pour I commençant à zéro jusqu'à n moins un, si l'élément à l'index i est égal à x, alors nous retournons I, ce qui signifie retourner la position à laquelle nous avons trouvé l'élément x et notre recherche sera terminée.

Et si nous ne pouvons pas trouver un tel AI, alors nous retournons moins un. Disons que retourner moins un signifie que nous n'avons pas pu trouver l'élément, nous n'avons pas pu trouver x dans le tableau.

Maintenant, dans ce cas, si nous avons de la chance, nous trouverons x à la première position elle-même.

Donc dans le meilleur des cas, nous ne ferons qu'une seule comparaison et nous pourrons trouver le résultat. Dans le pire des cas, lorsque x ne serait même pas présent dans le tableau, nous scannerons tout le tableau, nous ferons n comparaisons avec tous les éléments du tableau et ensuite nous pourrons donner un résultat que x n'existe pas dans le tableau.

Donc le temps pris dans le pire des cas est définitivement proportionnel à la taille d'entrée du tableau, désolé, à la taille du tableau.

Ou en d'autres termes, nous disons que cela serait grand O de n en termes de complexité temporelle. Il est toujours bon d'analyser le temps d'exécution d'un algorithme dans le pire des cas et de trouver la limite supérieure du temps pris.

Maintenant, dans ce cas, le temps pris croît comme une fonction linéaire de n.

Donc, nous appelons également cette recherche une recherche linéaire.

Et une fois de plus, si nous utilisons la recherche linéaire, nous n'utilisons aucune propriété comme le tableau trié ou non, qu'il soit trié ou non, cela fonctionnera.

Maintenant, essayons d'améliorer cet algorithme en utilisant la propriété supplémentaire du tableau qu'il est trié et je vais d'abord faire un peu de place ici.

Disons que nous voulons trouver si le nombre 13 existe dans le tableau.

Donc x est 13.

Et nous voulons trouver si x existe dans le tableau.

Maintenant, nous utiliserons une approche différente cette fois-ci, au lieu de comparer x avec le premier élément, comme nous le faisons dans le cas de la recherche linéaire, nous le comparerons avec l'élément du milieu dans le tableau.

Maintenant, la taille de ce tableau est de neuf, donc l'élément du milieu sera à l'index quatre. Il peut y avoir trois cas ici.

Le cas un peut être que x est égal à l'élément du milieu.

Si x est égal à l'élément du milieu, nous avons déjà trouvé x dans le tableau.

Le cas deux peut être lorsque x est inférieur à l'élément du milieu, et le cas trois peut être que x est supérieur à l'élément du milieu.

Clairement, si x est égal à l'élément du milieu, notre recherche est terminée.

Parce que nous avons trouvé x dans le tableau, si x est inférieur à l'élément du milieu, alors parce que le tableau est trié, il se trouve avant l'élément du milieu.

Et nous pouvons écarter les éléments du milieu, l'élément du milieu et tous les éléments après l'élément du milieu.

De même, si x est supérieur à l'élément du milieu, il se trouve après les éléments du milieu.

Donc, nous pouvons écarter tous les éléments avant l'élément du milieu, et bien sûr, l'élément du milieu également.

Donc, dans les cas deux et trois, nous écartons la moitié des éléments de notre espace de recherche et réduisons notre espace de recherche.

Donc, dans cet exemple, lorsque x est 13, initialement, notre espace de recherche est tout le tableau, X peut exister n'importe où dans le tableau.

Maintenant, nous le comparons avec l'élément du milieu, qui est 36.

Maintenant, x est inférieur à 36.

Donc, il existe, il devrait exister quelque part avant 36.

Donc, nous écartons tous les éléments après 36 et 36 également.

Donc, maintenant le problème est redéfini, nous devons rechercher x uniquement entre l'index zéro et trois.

Donc, comment gardons-nous une trace de l'espace de recherche, nous gardons une trace de l'espace de recherche en utilisant deux indices start et end.

Donc, initialement, le start serait zéro, et n serait le dernier élément du tableau, dans ce cas, l'index huit parce qu'initialement tout le tableau est notre espace de recherche.

Et nous calculons made comme start plus n divisé par deux.

Maintenant, une fois que nous avons trouvé notre espace de recherche réduit, nous ajustons Start et End en conséquence.

Donc, dans ce cas, après avoir comparé 13 avec 36, et écarté la moitié du tableau, notre end devient maintenant l'index trois, qui n'est rien d'autre qu'un de moins que l'élément du milieu.

Maintenant, nous trouvons à nouveau l'élément du milieu dans cet espace de recherche réduit.

Donc, ici l'élément du milieu serait trois plus zéro divisé par deux, si nous prenons seulement la partie intégrale, trois plus zéro divisé par deux serait 1,5.

Et si nous prenons la partie intégrale, l'élément du milieu sera l'index un. Une fois de plus, est-il égal à x ? Non, six n'est pas égal à 13. Est-ce que x est inférieur à l'élément du milieu ? Est-ce le cas deux ? Non, ce n'est pas le cas, x est supérieur à l'élément du milieu.

Donc, cette fois-ci, nous écartons l'élément du milieu et tous les éléments vers sa gauche et cette fois-ci nous déplaçons start pour marquer notre nouvel espace de recherche.

Maintenant, le nouvel espace de recherche commence à l'index deux et se termine à l'index trois.

Maintenant, quel est l'élément du milieu, trois plus deux est cinq, cinq divisé par deux est 2,5 et la partie intégrale est deux.

Donc, c'est notre élément du milieu.

Donc, x n'est pas égal à l'élément du milieu, nous avons trouvé notre élément.

Donc, nous avons terminé notre recherche.

Ce type de recherche où nous réduisons l'espace de recherche de moitié à chaque comparaison est appelé recherche binaire.

Une fois de plus, nous sommes capables de réduire l'espace de recherche de deux ou en d'autres termes, nous sommes capables de réduire l'espace de recherche de moitié seulement parce que le tableau est trié. Le fait que le tableau soit trié est une condition préalable pour la recherche binaire.

D'accord, alors écrivons maintenant le code pour cet algorithme.

Je vais écrire une méthode de recherche binaire qui prendra comme argument un tableau A, sa taille N et un nombre x à rechercher dans le tableau, et j'initialiserai deux variables start à zéro et end à n moins un.

Donc, start et end définissent notre espace de recherche, initialement tout le tableau est l'espace de recherche.

Maintenant, je vais écrire une condition ici tant que start est inférieur ou égal à end, et je reviendrai sur pourquoi j'écris cette condition.

Donc, tant que cela est vrai, start est inférieur ou égal à end, et nous trouverons l'index du milieu de l'espace de recherche comme start plus end divisé par deux.

Et maintenant, nous allons écrire trois cas.

Si l'élément du milieu est égal à x, alors notre recherche est terminée.

Nous retournons l'index stocké dans la variable made et sortons de la fonction.

Si x est inférieur à l'élément du milieu, alors nous devons écarter tous les éléments ayant un index supérieur ou égal à made.

Donc, notre fin de l'espace de recherche devient maintenant mid moins un.

Et dans la troisième condition, qui sera x supérieur à l'élément du milieu, qui sera la condition par défaut après ces deux si et sinon si, nous devons écarter tous les éléments avec un index inférieur ou égal à mid, donc, notre start devient mid plus un.

Et si nous sortons de cette boucle while sans rien retourner, alors nous retournons moins un, ce qui signifiera que nous n'avons pas pu trouver l'élément x dans le tableau.

Maintenant, pourquoi cette instruction while ici avec une condition start inférieur ou égal à end, ce que nous faisons essentiellement dans notre algorithme, c'est que nous réduisons notre espace de recherche de manière récursive en ajustant le pointeur start et end.

Maintenant, il doit y avoir une condition de sortie à notre récursion, la condition de sortie peut être soit nous trouvons l'élément dans le tableau, donc, nous retournons et sortons, soit nous épuisons tout l'espace de recherche lorsque start est égal à end ou start est inférieur à E et ensuite nous avons encore un tel espace, lorsque start est égal à n alors notre espace n'a qu'un seul élément.

Donc, lorsque cette condition devient fausse, nous avons épuisé notre espace de recherche, nous devons sortir de la boucle et nous devons retourner moins un pour dire que l'élément, le nombre x n'existe pas dans le tableau.

Maintenant, une fois de plus dans ce cas, dans le meilleur des cas, nous pouvons trouver l'élément x en une seule comparaison, lorsque le premier élément du milieu lui-même sera l'élément x dans le pire des cas, nous continuerons à réduire l'espace de recherche jusqu'à ce que l'espace de recherche devienne un élément.

Donc, de n nous réduisons à n divisé par deux et de n divisé par deux nous réduisons à n divisé par quatre et nous continuons jusqu'à ce que notre espace de recherche devienne un.

Maintenant, combien d'étapes cela prend-il ? Faisons un peu de maths ici.

Disons qu'il faut k étapes pour réduire n à un en divisant par deux à chaque étape.

Donc, n divisé par deux divisé par K sera égal à un et si vous résolvez cela, alors k sera égal à log de n la base sera deux.

Donc, dans le pire des cas, la recherche binaire prendra log n comparaisons et donc, le temps pris également dans le pire des cas est proportionnel à log in ou en d'autres termes, il est grand O de log n en termes de complexité temporelle et grand O de log n est beaucoup plus efficace qu'un algorithme o n.

Donc, c'était la recherche binaire, nous prendrons plus de problèmes sur la recherche binaire dans les leçons à venir.

Merci d'avoir regardé.

Dans la leçon précédente, nous avons appris la recherche binaire comme un algorithme efficace pour trouver ou rechercher un élément dans une donnée triée dans une collection triée.

Dans cette leçon, dans un vrai code, nous verrons comment implémenter la recherche binaire.

Et nous verrons également quelles sont les erreurs courantes qui se produisent lors de l'implémentation de la recherche binaire.

Mais avant cela, un rapide récapitulatif, disons que nous avons un tableau trié d'entiers quelque chose comme ceci, les éléments sont disposés dans l'ordre croissant et la taille du tableau est six.

Donc les indices vont de zéro à cinq.

Maintenant, disons que nous voulons trouver si le nombre 10 existe dans ce tableau ou non de manière programmatique en utilisant la recherche binaire.

Maintenant, dans la recherche binaire, ce que nous faisons, c'est que nous prenons deux pointeurs vers des variables qui pointent initialement vers le premier et le dernier élément du tableau, nous pouvons les appeler pointeurs start et end, nous pouvons appeler cette variable start et end ou nous pouvons également les appeler low et high pour marquer l'index inférieur et l'index supérieur.

Maintenant, start et end, ces deux variables à n'importe quel stade de notre algorithme nous donnent la plage dans laquelle l'élément peut exister.

Donc, au début de l'algorithme, l'élément peut exister n'importe où dans le tableau.

C'est pourquoi Start et End pointent vers le premier et le dernier élément.

Maintenant, nous calculons le point milieu en utilisant l'équation middle est égal à low plus high divisé par deux ou start plus end divisé par deux et nous prenons seulement la partie intégrale.

Donc, ici, cinq plus 0,2 serait 2,5.

Et en prenant la partie intégrale, nous donnerons cet index deux comme index milieu.

Donc, nous recherchons le nombre 10.

Et initialement, nous sommes dans un état où l'index inférieur est zéro, l'index supérieur est cinq et donc l'index milieu est deux.

Maintenant, nous voyons que l'élément à l'index milieu est l'élément souhaité.

S'il est l'élément souhaité, notre recherche est terminée.

Donc, l'élément à l'index milieu est six, est-ce que six est égal à 10.

Non, ce n'est pas le cas.

Maintenant, nous voyons si cet élément est supérieur à l'élément cible ou inférieur à l'élément cible, maintenant six est inférieur à l'élément cible qui est 10.

Donc, nous écartons six et tous les éléments avant six, car ils sont également inférieurs à 10.

Et nous déplaçons start pour pointer à l'index trois.

Donc, nous allons à cet état, l'index inférieur trois, l'index supérieur cinq et maintenant nous recherchons notre nombre dans cette partie du tableau seulement.

Maintenant, si nous calculons mid, mid serait quatre, cinq plus trois divisé par deux, est-il égal à l'élément cible 10 ? Oui, il est égal, donc nous avons trouvé notre élément, notre recherche est terminée, nous avons trouvé 10 à l'index quatre.

D'accord, que se passe-t-il si nous recherchions le nombre neuf dans le tableau, si nous recherchions neuf jusqu'à cette étape, ce serait la même chose.

Maintenant, à cette étape, l'élément du milieu est 10, nous le comparons avec neuf et je vais aussi le modifier ici maintenant 10 est supérieur à neuf.

Donc, définitivement, neuf ne peut exister qu'avant 10, nous devons écarter cette partie du tableau et nous devons aller à un état où notre espace de recherche est défini par low égal à trois et high égal à trois, maintenant trois est à la fois low et high et l'élément du milieu de cette plage serait également trois seulement.

Maintenant, cet élément du milieu n'est également pas égal à notre nombre souhaité neuf n'est pas égal à huit.

Maintenant, une fois que nous avons un seul élément dans notre espace de recherche et que nous n'avons toujours pas trouvé notre élément souhaité, notre recherche est terminée et nous n'avons pas pu trouver l'élément.

Implémentons maintenant la recherche binaire et j'écrirai un programme C maintenant.

D'accord.

Donc, ce que je vais faire ici, c'est d'abord écrire une méthode nommée binary search qui prendra un tableau d'entiers, sa taille, disons que la taille du tableau est n et disons que l'élément à rechercher est x, et cette méthode retourne un entier qui sera l'index de x s'il est trouvé dans le tableau.

Maintenant, nous allons déclarer deux variables low et high et les initialiser à zéro et n moins un respectivement, low et high à tout moment nous donnent le segment dans lequel x peut se trouver.

Donc, maintenant nous déclarons une autre variable made qui est calculée comme low plus high divisé par deux.

Maintenant, nous comparons x à l'élément à l'index made et il peut y avoir trois conditions ici. La première condition sera lorsque x est égal à l'élément du milieu, l'élément à l'index made, et dans ce cas, notre recherche est terminée, nous allons simplement retourner l'index made et lorsque nous retournons de notre méthode, nous en sortons. Maintenant, le deuxième cas peut être lorsque x est inférieur à a made, parce que x est inférieur à l'élément du milieu, il se trouvera avant made.

Donc, maintenant nous redéfinissons notre segment en déplaçant end vers mid moins un et cela devrait être correct.

Et le troisième et dernier cas, qui sera la condition par défaut ici lorsque x sera supérieur à l'élément du milieu, dans ce cas, nous redéfinirons le segment en ajustant le début, l'index inférieur, et l'index inférieur sera égal à mid plus un.

Maintenant, nous devons répéter ces trois étapes encore et encore.

Donc, comment faisons-nous cela, nous aurons définitivement besoin d'une boucle.

Donc, nous mettrons une boucle while ici.

Maintenant, quand arrêtons-nous l'exécution de ces étapes ? Nous arrêtons soit lorsque nous trouvons des éléments.

Donc, soit lorsque nous retournons, soit lorsque nous avons terminé de regarder tous les éléments.

Donc, je vais mettre une condition ici tant que low est inférieur ou égal à high, lorsque low devient supérieur à high, alors le segment défini par low et high ne sera pas un segment valide, Melo est égal à hi alors nous n'aurons qu'un seul élément dans le segment.

Maintenant, si nous sortons de cette boucle while sans rien retourner, alors nous pouvons dire que l'élément x n'est pas dans le tableau, disons que nous retournons moins un pour dire que x n'existe pas dans le tableau.

Donc, c'est la méthode de recherche binaire.

Et écrivons maintenant la méthode principale et essayons d'utiliser cette fonction.

Dans la méthode principale, je vais d'abord déclarer et initialiser un tableau, disons que le nom du tableau est a et nous remplissons certains éléments dans ce tableau dans l'ordre trié.

Rappelez-vous, le fait que le tableau soit trié est une condition préalable pour la recherche binaire.

D'accord, donc c'est un tableau de taille huit.

Maintenant, demandons à l'utilisateur d'entrer un nombre que nous rechercherons dans le tableau.

Donc, nous allons écrire une instruction printf ici et maintenant, essayons de prendre l'entrée de ce nombre.

Maintenant, je vais appeler binary search pour rechercher si ce nombre existe dans le tableau ou non, la taille du res est huit et nous voulons trouver x. Je vais plutôt le nommer x, parce que nous avons nommé l'élément cible x tout au long.

Donc, maintenant si l'index, qui est le retour de la méthode binary search, n'est pas égal à moins un, alors nous avons trouvé l'élément x dans a.

Donc, à ce stade, nous allons imprimer quelque chose comme le nombre x est à l'index index, index est également le nom de la variable, sinon nous allons imprimer que nous n'avons pas pu trouver x dans le tableau.

Essayons maintenant d'exécuter ce programme et voyons ce qui se passe.

Donc, on nous demande d'entrer un nombre, disons que nous voulons rechercher le nombre 15 dans le tableau.

Donc, cela dit que le nombre 15 est à l'index six et essayons maintenant de rechercher un nombre qui n'existe pas dans le tableau, disons que nous voulons rechercher 18 et le résultat est que le nombre 18 n'est pas trouvé. Il y a quelques erreurs courantes qui se produisent dans l'implémentation de la recherche binaire, la réinitialisation de ces index low et high doit être faite correctement et nous devons toujours être prudents quant à cette condition de sortie de la boucle.

Une autre erreur courante est lorsque les gens ne mettent pas cette accolade ici, maintenant, ce qui se passera ici, c'est que la priorité de l'opérateur de division est plus élevée, donc high divisé par deux sera calculé en premier et ensuite il sera ajouté à low, donc cette accolade est importante, nous devons mettre cette accolade ici et certaines personnes calculent également mid au lieu de le calculer comme low plus high divisé par deux, nous l'avons également calculé parfois comme low plus high moins low divisé par deux et c'est une meilleure façon de le faire parce que parfois low plus high peut dépasser la valeur maximale qu'un entier peut stocker.

Donc, comme un entier 32 bits ou un entier signé 32 bits peut stocker une valeur maximale de deux à la puissance 31.

Maintenant, si low et high sont assez élevés, alors high plus low dépassera deux à la puissance 31 et causera des problèmes dans l'exécution de notre programme, il devrait être assez évident que cette expression évalue à high plus low divisé par deux seulement.

La seule différence est que nous évitons le débordement en ne calculant pas high plus low dans cette expression.

D'accord.

Donc, c'était l'implémentation de la recherche binaire.

Et dans cette implémentation, nous avons utilisé une boucle, donc nous avons écrit une implémentation itérative, vous pouvez écrire une recherche binaire en utilisant la récursion également, je vous recommande d'essayer cela par vous-même.

Dans les leçons à venir, nous verrons plus de variations de la recherche binaire et son application dans d'autres scénarios.

Donc merci d'avoir regardé.

Dans notre leçon précédente, nous avons appris la recherche binaire et nous avons également implémenté la recherche binaire, mais nous avons implémenté une version itérative de la recherche binaire dans laquelle nous avons utilisé une boucle pour écrire notre programme.

Maintenant, dans cette leçon, nous allons écrire la recherche binaire en utilisant la récursion.

Commençons par écrire rapidement une version itérative de la recherche binaire.

Donc, je vais écrire une méthode de recherche binaire qui prendra comme argument un tableau trié, la taille du tableau n et un élément x qui doit être recherché. Ensuite, nous initialisons deux variables low et high, low à zéro et high à n moins un.

Et nous disons que tant que low est inférieur ou égal à high, nous calculons l'index du milieu comme low plus high divisé par deux.

C'est une meilleure pratique de calculer mid comme low plus high moins low divisé par deux, ce qui est la même chose sauf que nous ne calculons pas low plus high, parfois low et high individuellement sont dans la limite, dans la plage d'une variable entière mais high plus low dépasse la plage ou la limite d'une variable entière.

Maintenant, il y a trois conditions : si x est égal à l'élément du milieu, nous avons trouvé x dans le tableau, donc notre recherche est terminée, nous retournons l'index mid et sortons, sinon si x est inférieur à l'élément du milieu, nous définissons high à mid moins un pour dire que nous écartons tout ce qui est sur ou après mid, parce que x est inférieur à l'élément du milieu et que le tableau est trié, si x est supérieur à a mid, ce qui devrait être implicite ici.

Pour la troisième condition.

Comme la troisième condition, dans ce cas, nous avons défini low comme mid plus un.

Et si nous sortons de cette boucle while sans trouver quoi que ce soit, nous retournerons moins un pour dire que x n'existe pas.

Dans le tableau, ce que nous faisons essentiellement ici, c'est que si nous avons un tableau dans lequel les éléments sont dans l'ordre croissant, alors nous comparons d'abord x avec l'élément du milieu.

Et si x est égal à l'élément du milieu, c'est bien.

Si x est inférieur à l'élément du milieu, il doit exister avant cet élément dans cette section mise en évidence, et si x est supérieur, il doit exister après l'élément du milieu dans cette section particulière mise en évidence.

Et nous continuons à répéter ce processus dans le nouveau segment.

jusqu'à ce que nous trouvions x ou que nous ne puissions plus diviser l'espace de recherche, lorsque low est égal à high, notre espace de recherche devient ou plutôt se réduit à une taille de un, se réduit à un seul élément.

Après cela, nous ne pouvons plus le diviser.

La recherche binaire est un exemple typique d'un algorithme de type diviser pour régner dans lequel, à chaque étape, nous divisons le problème en deux.

Écrivons maintenant l'implémentation récursive.

Donc, une fois de plus, je vais écrire une méthode de recherche binaire qui prendra un tableau trié A et cette fois les arguments changeront un peu, nous prendrons deux arguments low et high pour marquer le segment du tableau dans lequel x peut se trouver à n'importe quel stade, x est l'élément à rechercher.

Et la logique serait quelque chose comme, une fois de plus, nous allons calculer l'index du milieu.

Et puis nous aurons trois conditions.

Si nous trouvons x, c'est bien, nous retournons l'index auquel nous l'avons trouvé.

Si x est inférieur à a mid, nous appelons la recherche binaire de manière récursive sur la plage low.

Et je manque d'espace ici.

Donc je vais créer un peu d'espace ici.

Et nous allons exécuter, nous allons appeler la recherche binaire de manière récursive pour l'index low à mid moins un.

Donc x doit maintenant être recherché entre l'index low et mid moins un, sinon si x est supérieur à a mid, ce qui sera la troisième condition de toute façon, nous allons retourner la recherche binaire de mid plus un à high, donc nous faisons un appel récursif pour rechercher x de l'index mid plus un à high. Lorsque nous écrivons la récursion, nous devons toujours rechercher un cas de base, une condition de base où nous arrêterions notre récursion. Dans ce cas, nous arrêterons notre récursion si nous trouvons l'élément.

Donc, ce cas retournera une sortie et nous ne ferons aucun autre appel récursif, mais que se passe-t-il si nous ne trouvons pas l'élément ? Que se passe-t-il si nous ne trouvons pas x dans le tableau ? Nous avons une autre condition de base pour cela où nous devons sortir si low est supérieur à high, alors nous n'avons pas un segment valide dans le tableau.

Et dans ce cas, nous pouvons dire que nous avons épuisé notre espace de recherche.

Donc, nous retournons moins un pour dire que x n'existe pas dans le tableau, je manque d'espace ici.

Donc, j'écris ces deux instructions sur la même ligne.

Donc, ces deux conditions sont nos conditions de base qui feront que la récursion s'arrête ou sorte, et cette condition low supérieur à high est la même condition que nous vérifions ici pour arrêter la boucle.

Simulons maintenant rapidement cette récursion à l'aide d'un exemple.

Disons que nous avons ce tableau A, un tableau trié de taille neuf, et nous voulons rechercher le nombre 63 dans ce tableau.

Donc, nous faisons un appel à la fonction binary search et j'écrirai b s ici, un raccourci pour binary search. Nous passons à la fonction le tableau et l'index inférieur doit être zéro et l'index supérieur doit être, disons, que initialement le nombre peut exister n'importe où dans le tableau de l'index zéro à huit, et le nombre à rechercher est 63. Maintenant, nous allons à l'intérieur de la fonction, est-ce que low est supérieur à high ? Non.

Donc, nous continuons et calculons mid, mid serait calculé comme quatre, l'élément à l'index mid, l'index quatre est 36 et 63 est supérieur à 36.

Donc, nous arrivons à cette condition else, la troisième condition, et nous faisons un appel récursif pour rechercher 63 dans la plage mid plus un, qui serait cinq à huit.

Maintenant, une fois de plus pour cette fonction, low est-il supérieur à high ? Non.

Donc, nous calculons mid, mid serait six si nous prenons seulement la partie intégrale et l'élément à l'index six est 63.

Donc, nous avons trouvé cet élément, nous allons retourner mid, donc nous retournons six ici et cette méthode se termine et cette méthode retourne également six à son appelant, peut-être la méthode principale.

Essayons maintenant de dire que nous voulons rechercher le nombre 25, donc nous faisons cet appel à binary search depuis la méthode principale.

Maintenant, une fois de plus, nous calculons mid, maintenant l'élément à l'index 4 est 36, qui est supérieur à 25.

Donc, nous faisons un appel récursif pour rechercher 25 de l'index zéro à trois.

D'accord, maintenant est-ce que low est supérieur à high ? Est-ce que zéro est supérieur à trois ? Non, donc nous continuons et calculons mid. Mid serait un, l'élément à l'index un est 6, 25 est supérieur à six.

Donc, nous faisons un appel récursif pour rechercher 25 entre les indices deux et trois, maintenant mid serait deux, et cette fois-ci, nous allons faire un appel récursif pour trouver 25 dans la plage trois à trois, c'est toujours une plage valide, low n'est pas supérieur à high, mid serait trois.

Et maintenant 25 est supérieur à 21.

Donc, nous faisons un appel récursif en utilisant la troisième condition à mid plus un, qui serait quatre et low high serait trois encore, et cette fois-ci low est supérieur à high.

Donc, nous arrivons à cette condition, où cette méthode retourne simplement moins un et se termine.

Maintenant, cette méthode retourne également moins un et cela se propage tout au long.

Et finalement, cette méthode retourne moins un à son appelant, la méthode principale. Lorsque nous écrivons de la récursion, nous devons être très prudents quant aux conditions de base, comme nous avons ces deux conditions de base ici.

Si nous n'obtenons pas nos conditions de base correctement, notre récursion peut continuer indéfiniment, provoquant le débordement de la mémoire du programme et le faisant planter.

La complexité temporelle de cet algorithme est grand O de log n, le temps pris est proportionnel à log n.

Et cela vient du fait que si nous continuons à diviser la taille du tableau par deux à chaque étape, alors il nous faudra log n étapes pour atteindre une taille de tableau égale à un.

Maintenant, une question évidente : laquelle est la meilleure, l'implémentation récursive ou l'implémentation récursive ou une implémentation itérative ? Eh bien, tout ce que nous pouvons écrire en utilisant la récursion, nous pouvons l'écrire en utilisant l'itération et tout ce que nous pouvons écrire en utilisant l'itération, nous pouvons l'écrire en utilisant la récursion. L'itération est légèrement plus performante.

C'est mieux en performance, car nous n'avons pas à stocker tous ces états de toutes ces fonctions, les fonctions supplémentaires dans la mémoire.

Mais écrire de la récursion peut parfois être très intuitif et facile à écrire.

Pour la plupart des raisons pratiques, vous pouvez choisir l'une ou l'autre selon votre confort.

Donc, ce n'est pas un problème.

D'accord, donc c'était l'implémentation récursive de la recherche binaire pour vous.

Merci d'avoir regardé.

Dans la leçon précédente, nous avons vu l'implémentation de la recherche binaire sous sa forme de base, nous avons résolu un problème dans lequel, si nous avons un tableau trié d'entiers, quelque chose comme ceci, et si nous voulons trouver si un nombre existe dans ce tableau ou non.

Donc, disons que nous voulons trouver si le nombre 10 existe dans ce tableau ou non, alors notre algorithme nous retourne que 10 existe à l'index trois.

Et si nous voulons rechercher un nombre qui n'existe pas dans le tableau, alors notre algorithme nous retourne que le nombre que nous cherchons n'existe pas dans un tableau.

Donc, si nous voulons rechercher 11 dans ce tableau, alors notre algorithme dit que 11 n'existe pas dans le tableau.

D'accord, donc maintenant, je vais modifier ce tableau.

Maintenant, ce tableau est toujours trié, mais la seule différence est que nous avons trois occurrences du nombre 10 dans le tableau.

Maintenant, disons que nous voulons rechercher le nombre 10 en utilisant la recherche binaire, alors quel sera l'index de 10 qui sera retourné ? Nous pourrions retourner l'index deux, nous pourrions aussi retourner l'index trois.

Ou nous pourrions retourner l'index quatre, l'implémentation normale de la recherche binaire que nous avons vue précédemment sort dès qu'elle trouve une occurrence d'un nombre dans le tableau, donc il n'y a aucune garantie que nous trouverons la première occurrence ou la dernière occurrence.

Maintenant, dans cette leçon, nous verrons deux variations différentes de la recherche binaire, une variation nous donnera toujours la première occurrence d'un nombre dans le tableau.

Et une autre variation nous donnera toujours la dernière occurrence du nombre que nous recherchons dans le tableau.

D'accord, écrivons d'abord l'implémentation de base que nous avions écrite précédemment.

Je vais rapidement écrire une méthode de recherche binaire qui prend trois arguments : un tableau, sa taille N, et l'élément à rechercher x.

Et nous allons initialiser deux variables low et high à zéro et n moins un pour marquer le segment du tableau dans lequel x est susceptible de se trouver.

Et tant que low est inférieur ou égal à high, nous calculons l'index du milieu comme low plus high divisé par deux, et ensuite nous comparons x avec l'élément du milieu.

Et si x est égal à l'élément du milieu, alors nous avons trouvé x et notre recherche est terminée.

Nous sortons de la méthode en retournant cet index mid.

Donc, nous sortons dès que nous avons trouvé une occurrence de x, pas nécessairement la première ou la dernière occurrence, mais n'importe quelle occurrence.

Si x est inférieur à l'élément du milieu, nous ajustons simplement high à mid moins un pour dire que x est maintenant susceptible de se trouver avant l'élément du milieu et la troisième et dernière condition.

Lorsque x est supérieur à l'élément du milieu, donc, dans ce cas, nous avons ajusté low à mid plus un.

Et si nous sortons de cette boucle while sans trouver x, alors nous retournons moins un pour dire que nous n'avons pas pu trouver x dans le tableau.

D'accord, regardons une simulation de cela pour cet exemple particulier, une simulation de cet algorithme pour cet exemple particulier, je vais dessiner trois colonnes ici, low, high et mid.

Et disons que le nombre à rechercher est 10.

Donc x est 10, la taille du tableau est six, donc initialement low est zéro, donc la taille du tableau est sept.

Donc, initialement low est zéro, high est six.

Maintenant, nous avons commencé à exécuter cette boucle while, nous calculons mid comme low plus high divisé par deux, donc mid serait trois.

Je vais aussi dessiner une colonne A mid, d'accord, cela semble mieux.

Maintenant, a trois est 10.

Donc, est-ce que x est égal à A mid ? Oui, c'est le cas.

Donc, nous retournons trois, nous retournons trois.

Et nous allons dire que c'est terminé parce que nous avons trouvé une blessure et nous retournons immédiatement, nous ne nous soucions pas qu'il y ait un autre 10 à l'index deux.

Maintenant, si nous voulons trouver, si nous voulions trouver la première occurrence de 10 dans le tableau, nous n'aurions pas dû dire gameover, nous aurions dû dire que j'ai trouvé 110 à l'index trois, laissez-moi aller voir vers la gauche, s'il y a un autre 10 à un index inférieur.

Et s'il y est, je retournerai celui-là.

Donc, je vais modifier légèrement cet algorithme ici.

Au début, disons que nous prenons une variable result, et l'initialisons à moins un.

Je reviendrai sur pourquoi je l'initialise à moins un.

Et je manque d'espace ici.

Donc, j'écris deux instructions sur la même ligne avec une virgule.

Maintenant, lorsque la condition est que x est égal à l'élément du milieu, au lieu de retourner et de sortir de l'exécution de la fonction, nous modifions result en x.

Désolé, nous modifions result en mid, l'index auquel x se trouve, et nous ajustons high à mid moins un.

Une fois de plus, je manque d'espace ici, donc j'écris deux instructions sur la même ligne.

Donc, ces deux instructions s'exécuteront pour cette condition si x est égal à l'élément du milieu.

Maintenant, que veux-je vraiment dire ici, ce que je veux dire, c'est que si nous avons trouvé x dans le tableau, alors nous avons stocké l'index dans la variable result à laquelle nous avons trouvé x et ensuite nous modifions notre segment, nous n'arrêtons pas notre recherche et nous modifions notre espace de recherche en ajustant high à mid moins un.

Donc, nous continuons à rechercher x avant cet élément du milieu.

Donc, si nous regardons la simulation maintenant, alors nous ne nous arrêtons pas ici, nous faisons highest deux et continuons notre recherche maintenant mid serait un, a mid serait pour, je vais aussi écrire la valeur de result à n'importe quel état.

Jusqu'à présent, notre result est, jusqu'à présent, nous avons trouvé 10 à l'index trois.

Donc, notre result est trois maintenant pour ce cas low zéro high deux et mid un, nous irons à la condition cette une lorsque x est supérieur à l'élément du milieu, donc low devient mid plus un donc low devient trop high est déjà trop maintenant mid serait aussi à a mid serait 10 Maintenant nous arrivons à cette condition, nous avons de nouveau trouvé x égal à l'élément du milieu du segment.

Donc, nous modifions maintenant result à l'index auquel nous avons trouvé x, donc results sera maintenant deux et high devient mid moins un qui sera un low est deux maintenant cette condition lower moins que ou égal à high échoue.

Donc, nous sortons de la boucle ici, il devrait y avoir une autre modification à mon code, je vais retourner result ici.

Donc, nous voyons ici que nous avons trouvé 10 à l'index deux.

Ainsi, nous avons trouvé la première occurrence de l'élément 10 dans le tableau, nous retournons result ici une fois que nous avons terminé la boucle while et nous ne retournons pas result à l'intérieur de la boucle, le result est initialement moins un.

Donc, si nous ne trouvons aucun x, il n'est jamais modifié.

Et nous retournons moins un pour dire que nous n'avons pas pu trouver x dans le tableau.

Et si nous trouvons un x dans le tableau et je vais mettre des accolades ici pour marquer que ces deux instructions s'exécutent pour cette condition if, nous avons stocké cet index dans cette variable, en quelque sorte disant que jusqu'à présent, c'est le résultat le plus à gauche que j'ai.

Et puis nous continuons à chercher vers la gauche, vers les index inférieurs.

Donc, nous modifions high à mid moins un, si nous trouvons un autre x, alors cet x est à gauche de l'index précédent.

Donc, nous écartons le résultat précédent et modifions notre résultat.

Donc, c'est la recherche binaire pour trouver l'occurrence du premier élément dans le tableau.

Si nous voulons trouver la dernière occurrence dans le tableau, alors il y aura seulement une légère modification à ce code.

Lorsque nous trouvons x, nous n'arrêtons pas la recherche comme nous le faisons ici.

Et nous continuons à chercher vers la droite, vers les indices supérieurs, en modifiant notre fenêtre, la fenêtre ou le segment ou l'espace de recherche en ajustant l'index inférieur à mid plus un, et c'est le seul changement que nous devons faire pour trouver la dernière occurrence dans le tableau.

Donc, regardons rapidement la simulation pour cette implémentation également.

Donc, une fois de plus, nous commençons avec low zéro high six et nous commençons également avec le résultat moins un moins un signifie que nous n'avons pas trouvé x dans le tableau jusqu'à présent, maintenant mid serait trois et l'élément du milieu serait 10, nous exécutons la boucle while ici, maintenant, nous arrivons à cette condition x est égal à a mid, donc d'abord nous modifions notre résultat, nous avons trouvé un x à l'index trois et ensuite nous modifions low à mid plus un qui serait quatre.

Donc, plus tôt notre fenêtre était tout le tableau.

Maintenant, notre espace de recherche est celui-ci et nous avons déjà des informations sur le 10 le plus à droite qui est apparu jusqu'à présent. D'accord, donc, maintenant mid serait cinq, a mid serait 18, maintenant, nous allons à cette condition x est inférieur à a mid, donc, maintenant high devient mid moins un, donc nous avons cette plage, notre fenêtre ou espace de recherche est maintenant celui-ci et jusqu'à présent nous avons trouvé 110 à l'index trois, maintenant mid serait cinq plus quatre divisé par deux et si nous prenons seulement la partie intégrale, alors c'est pour a mid serait 10.

Donc, une fois de plus, nous arrivons à la condition lorsque x est égal à l'image, donc nous modifions le résultat à l'index quatre et nous modifions low à mid plus un, donc low devient cinq, high devient cinq.

Jusqu'à présent, l'index le plus élevé de 10 que nous avons trouvé est quatre et notre fenêtre de recherche est maintenant seulement l'index cinq.

Donc, mid serait également cinq et a mid serait 18.

Maintenant, 80 est supérieur à 10.

Donc, nous allons de nouveau, une fois de plus, à cette condition particulière.

Donc, low est toujours cinq et high devient quatre maintenant.

Maintenant, ce n'est pas un espace de recherche valide, ce n'est pas un segment valide, la condition low inférieur ou égal à high échoue, donc nous allons sortir de la boucle, sortir de la boucle while et notre jeu est terminé, nous méritons, nous retournons ce que nous avons dans le résultat.

Donc, nous allons dire que nous avons trouvé 10 à l'index quatre.

Donc, c'est la recherche binaire pour trouver la dernière occurrence d'un élément dans le tableau dans un tableau trié.

La complexité temporelle de cet algorithme est grand O de log n.

Ou en d'autres termes, nous pouvons dire que le temps pris est proportionnel au log de n.

Dans les leçons à venir, nous verrons plus de variations de la recherche binaire, nous verrons d'autres scénarios dans lesquels la recherche binaire est appliquée.

Donc merci d'avoir regardé.

Dans cette leçon, nous allons résoudre une question très célèbre d'entretien de programmation.

Et la question est la suivante : étant donné une liste triée d'entiers, nous voulons trouver combien de fois un élément particulier apparaît dans cette liste.

Donc, disons que nous avons une liste sous la forme d'un tableau.

Ici, nous avons un tableau de taille 12.

Et les éléments sont dans l'ordre croissant.

Maintenant, combien de fois le nombre cinq apparaît-il dans ce tableau ? Cinq apparaît cinq fois et combien de fois le nombre deux apparaît-il dans ce tableau ? Deux n'apparaît pas dans le tableau.

Donc, nous aurons un tel tableau trié et un nombre x.

Et nous devons trouver combien de fois ce nombre x existe dans ce tableau.

Maintenant, nous voulons résoudre ce problème de manière programmatique.

Donc, réfléchissons aux différentes approches que nous pourrions vouloir suivre.

L'approche la plus simple est de scanner tout le tableau et de compter les occurrences de x dans le tableau.

Donc, si je dois écrire une fonction find count qui prendra comme arguments un tableau, sa taille N, et l'élément x à rechercher, l'élément x pour lequel nous voulons trouver le compte.

Donc, la logique serait assez simple, nous allons prendre une variable initialement, disons que le nom de la variable est count et nous l'initialisons à zéro.

Et puis nous exécutons une boucle commençant à zéro jusqu'à n moins un.

Et si a I ou l'élément à l'index i est égal à l'élément x, nous incrémentons count.

Donc, count devient count plus un et finalement lorsque nous sortons de cette boucle, nous retournons count.

Donc, nous effectuons une recherche linéaire où nous scannons tout le tableau pour rechercher l'élément x.

Nous pourrions optimiser cet algorithme un peu, quelque chose comme ceci, parce que le tableau est trié, une fois que nous atteignons un stade, lorsque AI devient supérieur à x, nous pouvons arrêter de compter.

Mais dans le pire des cas, cette boucle s'exécutera n fois.

Lorsque tous les éléments du tableau sont identiques, alors cette boucle s'exécutera n fois.

Donc, dans le pire des cas, cet algorithme, le temps d'exécution de cet algorithme est proportionnel à n.

En d'autres termes, la complexité temporelle est grand O de n.

C'est une solution très simple pour ce problème.

Et si vous donnez cette solution dans un entretien de programmation, l'intervieweur serait comme, je n'aime pas ça, donnez-moi quelque chose de mieux.

Donc, comment trouvons-nous une meilleure solution ? Chaque fois que dans un problème, nous avons une donnée triée ou une collection triée, nous devons essayer de penser à appliquer un algorithme très célèbre qui fait le meilleur usage de cette propriété que la donnée est triée.

Et cet algorithme est la recherche binaire.

Donc, pouvons-nous utiliser la recherche binaire dans ce problème ? Une chose que nous pouvons faire est que, en utilisant la recherche binaire, nous pouvons trouver une occurrence du nombre x dans le tableau.

Donc, disons que dans cet exemple, nous voulons trouver le compte du nombre cinq.

Donc, disons que nous trouvons, en utilisant la recherche binaire en temps grand O de log n, que le nombre cinq existe à l'index six.

Maintenant, parce que le tableau est trié, toutes les occurrences de cinq seront adjacentes à celui-ci.

Donc, nous pouvons aller vers les indices supérieurs en commençant par cet index, et chercher tous les cinq, puis nous pouvons aller vers les indices inférieurs, et chercher toutes les occurrences de cinq.

Mais une fois de plus, si tout le tableau est le nombre cinq, seulement, tous les éléments étant identiques, c'est toujours un tableau trié, alors nous allons scanner tous les éléments, nous allons accéder à tous les éléments du tableau, et finalement la complexité temporelle sera grand O de n, seulement le temps pris sera proportionnel à N seulement dans le pire des cas.

Donc, utiliser la recherche binaire ne nous donne pas beaucoup d'avantage si nous utilisons la recherche binaire sous sa forme de base, grand O de n, car pour effectuer une recherche binaire, nous prendrons un temps grand O de log n.

Et puis pour trouver toutes les occurrences adjacentes de x, nous prendrons grand O de n dans le pire des cas.

Donc, pour des valeurs plus élevées de n, log n est négligeable en comparaison à.

Et donc, cela est finalement grand O de n, nous ne sommes pas en train d'écrire le pseudocode pour cette approche, nous allons laisser cela comme un exercice pour vous.

Avec ces deux approches, nous sommes toujours grand O de n dans le pire des cas.

Donc, que faisons-nous ? Eh bien, si vous vous souvenez de nos leçons précédentes sur la recherche binaire, nous pouvons écrire une recherche binaire pour trouver la première occurrence d'un élément dans un tableau.

Et de manière similaire, nous pouvons écrire une variation de la recherche binaire pour trouver la dernière occurrence d'un élément dans un tableau.

Et cela forme la base de notre troisième approche.

Et je vais effacer un peu de cela et faire un peu de place.

D'accord, donc nous pouvons utiliser une variante de la recherche binaire pour trouver la première occurrence d'un élément dans un tableau.

Et nous pouvons utiliser une autre variation de la recherche binaire pour trouver la dernière occurrence.

Et si nous connaissons le dernier et le premier index auxquels l'élément se produit, alors nous connaissons également le compte de celui-ci dans le tableau.

Donc, une fois de plus, nous allons écrire une méthode find count qui prendra un tableau, sa taille N et l'élément x.

Et disons que nous trouvons la première occurrence de l'élément dans le tableau en utilisant une méthode find first, qui est une variation de la recherche binaire.

Et nous allons utiliser une autre méthode appelée une autre variante de la recherche binaire, qui nous donnera la dernière occurrence de l'élément dans le tableau, puis nous pouvons retourner le compte comme last index moins first index plus un.

Et je ne gère pas le cas ici lorsque l'élément n'est pas présent dans le tableau.

Disons que nous allons bien le gérer dans notre implémentation réelle.

D'accord, donc le premier appel de méthode si nous utilisons la recherche binaire fonctionnera en grand O de log n et le deuxième appel de méthode pour trouver la dernière occurrence fonctionnera également en grand O de log n.

Donc, globalement, la complexité temporelle pour trouver le compte d'un élément dans le tableau serait grand O de log n.

Et c'est vraiment génial.

Nous avons décrit comment trouver la première ou la dernière occurrence d'un élément dans un tableau trié en utilisant la recherche binaire.

Nous avions écrit du pseudocode pour l'algorithme dans notre leçon précédente et il y a un lien vers la leçon précédente dans la description de cette leçon.

Mais écrivons maintenant du vrai code.

Pour résoudre ce problème.

Je vais écrire un programme C.

Commençons par écrire une recherche binaire simple et normale, puis nous la modifierons pour trouver la première ou la dernière occurrence.

Disons que nous avons une méthode binary search qui me donne l'index de l'élément x dans le tableau.

Dans la recherche binaire, nous définissons d'abord deux indices low et high, deux variables low et high initialement définies à zéro et n moins un, respectivement.

Et puis nous trouvons l'élément du milieu et l'index du milieu comme low plus high divisé par deux, et puis nous comparons l'élément du milieu avec le nombre x.

Et si nous trouvons, si l'élément du milieu est égal à x, nous avons trouvé notre élément.

Donc, nous retournons simplement l'index mid, sinon, si x est inférieur à l'élément du milieu, parce que le tableau est trié, rappelez-vous que le fait que le tableau soit trié est une condition préalable à la recherche binaire, nous définissons high comme mid moins un, en quelque sorte disant que nous recherchons dans le segment à gauche de l'élément du milieu.

Et si x est supérieur à l'élément du milieu, nous ajustons low à mid plus un.

Et nous répétons ce processus encore et encore jusqu'à ce que nous ayons un segment valide et un segment valide est jusqu'à ce que low soit inférieur ou égal à high.

Et si nous sortons de cette boucle sans trouver quoi que ce soit, alors nous retournons moins un pour dire que x n'existe pas dans le tableau.

Le problème avec cette implémentation est que dès que nous trouvons un x, nous retournons.

Donc, il n'y a aucune garantie que nous trouverons le premier index ou le dernier index, s'il y a des doublons dans les doublons de x dans le tableau.

Donc, ce que nous faisons, c'est que nous allons, ce que nous allons faire, c'est modifier légèrement l'algorithme, nous allons avoir une autre variable, l'initialiser à moins un.

Et maintenant, lorsque nous trouvons x, alors nous ne retournons pas et ne sortons pas, nous mettons à jour la variable result pour dire que, d'accord, c'est l'index le plus bas de x jusqu'à présent, et puis nous continuons la recherche.

Donc, si nous voulons trouver la première occurrence, alors nous ajustons high à mid moins un.

Donc, nous mettons à jour result et continuons à chercher vers le segment inférieur.

Et finalement, si lorsque nous sortons de cette boucle, alors nous retournons result.

Donc, si nous ne trouvons rien, aucune occurrence de x, nous retournons simplement moins un, parce que cela a été initialisé à moins un.

Maintenant, cette implémentation nous donnera la première occurrence de x dans le tableau.

Et si nous voulions la dernière occurrence, la seule différence serait que nous continuerions à chercher vers la droite ou les indices supérieurs, donc nous dirions que low est égal à eight plus un, maintenant continuons à chercher vers les indices supérieurs.

Maintenant, je veux deux fonctions différentes pour trouver la première ou la dernière occurrence.

Mais si vous voyez, il y a une différence seulement dans une ligne dans ces deux implémentations.

Donc, ce que je vais faire, c'est utiliser la même fonction pour récupérer à la fois le premier et le dernier index en fonction d'un autre argument de flag.

Donc, disons que nous avons un flag comme un paramètre booléen.

Search First, s'il est vrai, nous voulons rechercher la première occurrence et s'il est faux, alors nous voulons rechercher la dernière occurrence.

Donc, si nous voulons rechercher la première occurrence, alors nous voulons, dans le cas où a mid est égal à x, nous voulons ajuster high à mid moins un, sinon nous voulons ajuster low à mid plus un.

D'accord, écrivons maintenant la méthode principale.

Ce que je vais faire, c'est d'abord initialiser un tableau.

Et je vais demander à l'utilisateur d'entrer un nombre x.

Maintenant, nous voulons trouver le compte de x.

Donc, nous allons d'abord faire un appel à la méthode binary search pour trouver le premier index dans le tableau.

Donc, nous allons passer le tableau, le nombre d'éléments dans le tableau, qui est 12.

Et nous allons également calculer le nombre d'éléments en utilisant cette équation particulière, la taille de a divisée par la taille de a zéro, la taille du nombre d'octets dans tout le tableau divisée par le nombre d'octets dans chaque élément entier.

Et nous voulons rechercher x et nous allons passer true parce que dans notre déclaration de méthode, si ce flag est passé comme true, alors nous recherchons le premier index, sinon nous recherchons le dernier index.

Maintenant, si le premier index est retourné comme moins un, alors l'élément n'est pas dans le tableau.

Donc, pas besoin de trouver le dernier index, nous pouvons simplement imprimer que le compte est zéro.

Sinon, nous trouvons le dernier index et cette fois nous faisons l'appel à la même fonction binary search avec seulement la différence que cette fois nous allons passer le flag comme false.

Donc, nous allons dire que, hé, donnez-moi le dernier index.

Et nous allons imprimer le compte comme dernier index moins premier index plus un.

Donc, c'est notre code.

C'est notre méthode binary search.

Et nous avons fait appel à binary search deux fois pour trouver le premier et le dernier index et nous décidons du premier ou du dernier index en utilisant ce flag.

Essayons maintenant d'exécuter ce code et voyons ce qui se passe.

Disons que nous voulons trouver le compte du nombre trois, alors cela nous donne que trois apparaît deux fois, ce qui est correct.

Essayons maintenant le nombre cinq et le compte de cinq est cinq.

Et essayons x égal à deux, deux n'est pas présent dans le tableau donc le compte sera zéro.

Donc, c'est un algorithme optimisé pour trouver le compte d'un élément dans un tableau trié.

C'est une implémentation classique de la recherche binaire.

Dans les leçons à venir, nous verrons plus de problèmes sur la recherche binaire.

Donc merci d'avoir regardé.

Dans cette leçon, nous allons résoudre une autre question d'entretien de programmation.

Et la question est la suivante : nous avons un tableau trié qui a été tourné.

Donc, disons que nous avons un tableau trié avec ces éléments, la taille du tableau est six, donc nous avons des indices de zéro à cinq.

Et disons que nous voulons faire tourner ce tableau dans le sens inverse des aiguilles d'une montre, faire tourner ce tableau vers la droite.

Donc, chaque élément se décalera d'une position vers la droite, sauf le dernier élément qui se décalera à la première position dans le tableau, et le tableau résultant serait celui-ci, et celui-ci est tourné une fois, et si nous tournons le tableau deux fois, le tableau résultant serait celui-ci, et celui-ci est bien sûr tourné deux fois.

Et un tel tableau est souvent également appelé tableau trié de manière circulaire.

Donc, nous avons un tel tableau trié de manière circulaire, et il y a une autre condition, il n'y a pas de doublons dans le tableau, tous les éléments du tableau sont distincts.

Donc, étant donné un tel tableau, nous devons trouver combien de fois le tableau a été tourné.

Donc, comment résolvons-nous ce problème ? Une chose qui devrait être assez évidente est que si nous connaissons le premier élément ou l'élément minimum de la séquence triée dans le tableau, alors nous savons combien de fois le tableau a été tourné.

Et lorsque nous disons le nombre de fois que 30 a été tourné, pour ce problème, nous entendons la rotation dans le sens inverse des aiguilles d'une montre ou la rotation vers la droite, le nombre de rotations du tableau serait le nombre d'éléments avant l'élément le plus petit ou l'élément minimum dans le tableau.

Donc, dans ce cas, il n'y a qu'un seul élément avant deux, qui est le minimum.

Donc, clairement, ce tableau est tourné une fois, ici nous avons deux éléments avant l'élément minimum.

Donc, celui-ci est tourné deux fois.

En fait, si nous regardons, alors le nombre de rotations est égal à l'index de l'élément minimum.

Donc, notre problème est essentiellement de trouver l'élément minimum dans le tableau, l'index de l'élément minimum dans le tableau.

Et nous avons terminé.

Nous savons combien de fois le tableau a été tourné.

Donc, comment trouvons-nous l'index de l'élément minimum ? L'approche la plus simple serait de scanner tout le tableau, d'effectuer ce que nous appelons également une recherche linéaire.

Et le pseudocode serait quelque chose comme nous aurons deux variables, une pour stocker l'élément minimum et une autre pour stocker l'index minimum.

Disons que initialement, le premier élément est l'élément minimum, puis nous exécutons une boucle de un à n moins un où n est la taille du tableau.

Et si l'élément à l'index est inférieur au minimum, nous mettons à jour le minimum et l'index minimum.

Et finalement, lorsque nous sortons de cette boucle, nous aurons l'index de l'élément minimum. Clairement, le temps d'exécution de cet algorithme serait grand O de n, le temps d'exécution sera proportionnel à n.

Maintenant, cela nous donnera la bonne réponse, c'est une solution correcte.

Mais dans cette solution, nous n'avons pas utilisé la propriété du tableau qu'il est trié de manière circulaire, pouvons-nous utiliser cette propriété du tableau et améliorer cet algorithme, améliorer la complexité temporelle de cet algorithme ? Eh bien, voyons voir.

Maintenant, nous allons utiliser la propriété que le tableau est trié de manière circulaire, et nous allons utiliser une variation ou une modification de l'algorithme de recherche binaire pour résoudre ce problème.

Maintenant, que faisons-nous dans un algorithme de recherche binaire normal ? Disons que nous avons un tableau trié comme ceci, nous trouvons d'abord l'élément du milieu dans l'index dans le tableau.

Et puis nous voyons si c'est l'élément que nous cherchons ou non.

Si ce n'est pas l'élément que nous cherchons, nous allons soit chercher vers la gauche, soit nous allons chercher vers la droite en fonction du fait que l'élément que nous cherchons est supérieur ou inférieur à l'élément du milieu.

Donc, à chaque étape, nous divisons le problème en cherchant quelque chose dans la moitié du tableau.

À chaque étape, nous écartons la moitié des éléments, nous écartons la moitié de l'espace de recherche, et nous continuons jusqu'à ce que nous trouvions l'élément.

Maintenant, dans une liste triée de manière circulaire comme celle-ci, notre problème est de trouver le premier élément de la séquence triée.

Cet élément particulier est une sorte de pivot ou de jonction dans le tableau trié de manière circulaire.

Donc, maintenant, nous allons utiliser une variation de la recherche binaire pour trouver cet élément pivot qui est également l'élément minimum dans le tableau.

Ce que nous faisons essentiellement dans une recherche binaire, c'est redéfinir un espace de recherche ou un segment dans lequel notre élément désiré est susceptible de se trouver par deux variables low et high, l'index inférieur et l'index supérieur, et à chaque étape, nous trouvons soit un élément, soit nous réduisons l'espace de recherche de moitié en écartant la moitié des éléments dans le segment et en créant un nouveau segment.

Et maintenant, nous regardons le nouveau segment, nous divisons le problème à chaque étape en deux.

Maintenant, dans ce problème, pour chaque segment, nous allons regarder quelques éléments, il peut y avoir un cas où l'élément inférieur à l'index inférieur est inférieur ou égal à l'élément à l'index supérieur.

Maintenant, cela ne sera possible que si le segment est déjà trié, si le segment est déjà trié, l'élément minimum dans le segment et c'est ce que nous trouvons, l'élément minimum dans le tableau, et si nous pouvons trouver l'élément minimum dans le segment, ce sera également l'élément minimum dans le tableau.

Donc, nous retournerons simplement l'index low parce que le tableau est déjà trié.

Donc, l'élément à l'index inférieur est le minimum si le segment n'est pas trié, nous calculons l'index du milieu.

Et maintenant, nous essayons de voir si notre index du milieu est le pivot ou non.

Maintenant, comment trouvons-nous le pivot ? Si vous regardez, il y a une propriété spéciale de l'élément pivot ou de l'élément minimum dans le tableau, si nous regardons les éléments suivant et précédent de l'élément pivot de manière circulaire.

Donc, si c'est le dernier élément, l'élément suivant sera le premier élément, alors pour l'élément pivot, les éléments suivant et précédent dans le tableau sont tous deux supérieurs à lui, comme ici 18 et cinq sont tous deux supérieurs à deux.

Aucun autre élément dans le tableau n'aura cette propriété sauf l'élément pivot.

Définissons cette propriété comme la propriété du pivot.

Donc, ici nous calculons next comme MIT plus un modulo n modulo n parce que si mid est le dernier index dans le tableau, nous devons aller au premier élément.

Donc, l'opération modulo fait cela et previous serait mid moins un modulo n et nous ajouterons aussi n ici pour que mid moins un ne devienne pas un nombre négatif.

Donc, notre cas deux est que a mid est inférieur ou égal à a next et il est aussi inférieur ou égal à l'élément précédent dans le tableau circulaire dans le tableau trié de manière circulaire.

Si c'est le cas, une fois de plus nous avons le pivot ou l'élément minimum dans le tableau.

Donc, nous allons retourner l'index mid.

Jusqu'à présent, dans ces deux cas, nous avons trouvé notre élément directement et nous n'avons pas ressenti le besoin de diviser le tableau, de diviser l'espace de recherche du segment.

Si l'élément du milieu n'est pas le pivot, alors pouvons-nous utiliser une propriété où nous pouvons dire que nous pouvons écarter la moitié droite ou nous pouvons écarter la moitié gauche et nous pouvons aller dans l'une des moitiés pour rechercher l'élément pivot.

Eh bien, oui, c'est possible de le faire, si l'élément du milieu, l'élément à l'index mid est inférieur ou égal à l'élément le plus élevé à l'index high, alors le segment commençant à l'index mid et s'étendant vers la droite jusqu'à l'index high, ce segment entier est trié et le pivot ne peut pas exister dans le segment droit.

Donc, dans ce cas, nous allons dire que nous devons rechercher le pivot dans la moitié gauche.

Donc, nous allons ajuster high à mid moins un et le cas quatre serait lorsque l'élément mid est supérieur ou égal à l'élément à l'index le plus bas.

Maintenant, dans ce cas, il n'est pas possible que le pivot soit dans la gauche.

Donc, nous allons chercher dans la droite, donc nous allons ajuster low à mid plus un.

Donc, nous continuons à réduire nos segments à chaque étape et essayons de trouver la réponse.

Maintenant, simulons cette approche, cet algorithme pour cet exemple particulier.

Donc, pour cet exemple, le cas un est évidemment faux initialement.

Donc, nous trouvons l'index du milieu.

Maintenant, la propriété du pivot n'est pas vraie pour l'index du milieu.

Donc, nous regardons le cas trois, lorsque nous regardons le cas trois, nous regardons essentiellement si toute cette partie de la séquence est triée ou non, y compris 18 et tous les éléments vers la droite.

Donc, 18 n'est pas inférieur ou égal à huit.

Maintenant, nous cherchons le cas quatre.

Et lorsque nous cherchons le cas quatre, nous voulons vérifier si cette séquence complète est triée ou non.

Eh bien, celle-ci est triée.

En fait, si le tableau n'est pas trié, alors l'une de ces deux séquences sera toujours triée.

Vous pouvez prendre quelques exemples, essayer de voir et c'est ce qui forme la base de notre approche diviser pour régner.

C'est ce qui forme la base sur laquelle nous écartons la moitié des éléments.

Donc maintenant, nous devons ajuster low à mid plus un.

Donc, nous avons écarté ces éléments de notre espace de recherche, notre nouvel espace de recherche commence à deux.

Maintenant, ce tableau est trié.

Le cas un est vrai pour ce segment, désolé, ce segment est trié.

Donc, nous retournons simplement l'index de deux qui est 0123, et quatre, donc nous retournons quatre ici et notre recherche est terminée, nous avons trouvé l'élément pivot.

Donc, nous savons que le tableau est tourné quatre fois, égal à l'index de l'élément pivot. Quelques choses à propos de cet algorithme, cet algorithme ne fonctionnera que s'il n'y a pas de doublons dans le tableau.

Et c'était aussi notre condition initiale dans le problème, s'il y a des doublons, cette réduction de l'espace de recherche en deux n'est pas possible.

Et écrivons maintenant le code pour cet algorithme et voyons s'il fonctionne ou non.

Donc, je vais écrire une méthode find rotation count, qui me donnera combien de fois un tableau trié de manière circulaire A est tourné, et n est le nombre d'éléments dans le tableau.

Donc, nous définissons d'abord low et high.

Et puis, tant que notre espace de recherche est valide, nous voyons d'abord si le segment est déjà trié.

S'il est trié, nous retournons l'index inférieur.

Donc, c'est notre cas un, sinon nous calculons mid comme low plus high divisé par deux, et puis nous calculons également le next et le previous de mid.

Et si mid satisfait la propriété du pivot, nous retournons mid.

Sinon, si l'élément du milieu est inférieur ou égal à l'élément le plus élevé, alors nous écartons la moitié droite, et nous ajustons l'index le plus élevé à mid moins un, sinon, si a mid est supérieur ou égal à a low, alors nous écartons la première moitié, la moitié gauche.

Si le tableau n'est pas trié, l'une de ces deux conditions sera toujours vraie.

Et seulement l'une de ces conditions sera vraie, pas les deux.

Disons que si nous ne sommes pas capables de retourner quoi que ce soit, si nous ne sommes pas capables de retourner quoi que ce soit dans la boucle while, alors nous retournons moins un, moins un sera retourné seulement pour un scénario invalide lorsque peut-être le tableau n'est pas trié de manière circulaire, ses propriétés ne sont pas vraies.

Maintenant, dans la méthode principale, j'ai initialisé un tableau de taille 11.

Et j'ai appelé cette fonction find rotation count.

Et j'essaie d'imprimer le compte.

Voyons ce qui se passe si j'exécute le programme.

Cela dit que le tableau est tourné six fois, ce qui semble être correct.

Modifions maintenant ce tableau.

Exécutons ceci pour un cas de test lorsque les éléments sont déjà triés.

D'accord, cela semble aussi bien.

Donc, nous sommes bons.

Maintenant, j'ai utilisé quatre cas pour résoudre ce problème.

Il y a quelques autres approches de mise en œuvre également, l'idée sous-jacente serait la même, utiliser la recherche binaire.

Mais nous pouvons l'implémenter en utilisant quelques conditions différentes.

Je vous encourage à les essayer par vous-même ou à faire une recherche rapide sur Google pour des extraits de code.

Donc, c'était un problème intéressant résolu en utilisant la recherche binaire, dans les leçons à venir, nous verrons plus de tels problèmes intéressants.

Merci d'avoir regardé.

Dans cette leçon, nous allons résoudre une autre question très célèbre d'entretien de programmation.

Et la question est la suivante : nous avons un tableau trié de manière circulaire, ce qui signifie qu'un tableau trié a été tourné.

Et dans la leçon précédente, nous avions également résolu un problème où nous voulions trouver le nombre de rotations dans un tableau trié de manière circulaire.

C'est un exemple de tableau trié de manière circulaire, le premier élément dans la séquence triée est à l'index quatre, et puis nous allons vers la droite.

Et puis après le dernier élément, nous allons au premier élément.

Donc, c'est le début de la séquence triée.

Et c'est la fin de la séquence triée.

Chaque élément dans la séquence triée a été décalé de quatre positions, le tableau est tourné quatre fois dans le sens inverse des aiguilles d'une montre ou vers la droite.

Maintenant, étant donné un tel tableau, nous devons trouver si un nombre x existe dans ce tableau ou non.

Donc, comment résolvons-nous ce problème ? L'approche la plus simple serait d'effectuer une recherche linéaire, où nous scannons tout le tableau à la recherche de x.

Mais dans cette approche, nous n'utiliserons pas la propriété du tableau qu'il est trié de manière circulaire.

Et la complexité temporelle pour cette approche serait grand O de n, où n est le nombre d'éléments dans le tableau.

Donc, que pouvons-nous faire d'autre ? Chaque fois que nous avons une donnée triée, et que nous devons rechercher quelque chose, nous devons toujours penser à la recherche binaire comme l'une des approches possibles.

La recherche binaire, comme nous le savons, s'exécute en grand O de n log n.

Au plus, nous faisons log n comparaisons pour trouver notre élément dans le tableau.

Et grand O de log n est la meilleure complexité temporelle à avoir pour une solution.

Donc, voyons si nous pouvons appliquer la recherche binaire sous une certaine forme.

Pour résoudre ce problème, prenons cet exemple de tableau trié de manière circulaire, l'exemple que nous avons à gauche, et maintenant nous allons utiliser une variation de la recherche binaire pour trouver un élément x dans le tableau, comme nous le faisons dans la recherche binaire normale, nous allons d'abord définir deux indices low et high initialement au premier et au dernier élément du tableau respectivement.

Et puis nous trouvons l'élément du milieu comme low plus high divisé par deux, l'index du milieu.

Jusqu'à présent, la logique est la même.

Maintenant, le premier cas serait que l'élément à l'index du milieu a mid est égal à x.

Comme nous le faisons dans une recherche binaire normale, nous allons comparer l'élément du milieu avec le nombre que nous cherchons x, et si celui-ci est égal à x, notre recherche est terminée, nous allons retourner mid en disant que x existe à l'index mid, si a mid n'est pas égal à x, alors si le tableau était un tableau trié normal, alors nous serions allés soit dans la moitié gauche, soit dans la moitié droite selon que x est supérieur ou inférieur à l'élément du milieu.

Mais nous ne pouvons pas appliquer cette logique directe pour écarter l'une des moitiés dans ce cas, mais il y a une propriété que nous pouvons explorer et écarter la moitié des éléments.

Si vous regardez, alors les éléments du tableau sont toujours croissants sauf seulement à ce point particulier, qui est le point de jonction ou le point de pivot, où nous avons le premier élément ou l'élément minimum dans la séquence triée.

Maintenant, si nous prenons n'importe quel segment ou n'importe quel sous-tableau, alors s'il ne contient pas ce point de pivot, s'il ne contient pas ces deux éléments, qui forment la frontière, le point de rupture, alors tous les éléments de ce segment seront triés.

Et si le segment contient ces deux éléments qui forment le point de rupture, alors le segment ne sera pas trié.

Maintenant, l'élément du milieu divise le segment en deux moitiés et ce point de rupture ou le point de pivot se trouvera seulement dans l'une de ces moitiés.

Donc, au moins l'une de ces moitiés sera toujours triée, nous allons utiliser cette propriété et nous allons écarter la moitié du tableau, la moitié de l'espace de recherche à chaque itération de la recherche binaire.

Donc, notre cas deux sera si a mid est inférieur ou égal à a high, nous regardons essentiellement cette partie particulière du tableau, nous incluons l'élément du milieu et cherchons le segment s'étendant jusqu'à l'élément le plus élevé.

Si cette condition est vraie, alors tout ce segment est trié.

Dans cet exemple, ce segment n'est pas trié.

Mais si le segment était trié, la moitié droite était triée, alors il y aurait deux conditions, disons que ces conditions sont 2a et 2b, nous savons que x n'est pas égal à a mid, mais si x est supérieur à a mid et x est inférieur ou égal à a high, alors il se trouve définitivement dans cette moitié triée.

Donc, nous ajustons low à mid plus un pour dire que nous allons de l'avant et cherchons dans la moitié droite comme si ce n'était pas le cas, nous aurons une condition lorsque nous dirons d'aller chercher dans la moitié gauche, dans la moitié non triée.

Cela sera le cas lorsque la moitié droite du tableau est triée. Le cas trois serait lorsque a low ou le premier élément dans la séquence est inférieur ou égal à l'élément du milieu, inférieur ou égal à a mid.

Maintenant, dans ce cas, nous regardons si ce segment particulier commençant à l'index low jusqu'à l'index mid est trié ou non.

Maintenant, une fois de plus, nous aurons deux conditions pour vérifier si cette moitié est triée, il est très facile de vérifier si x est susceptible de se trouver dans ce segment ou non, dans ce sous-segment ou non, ici si x est supérieur ou égal à a low et x est inférieur à a mid, x ne peut pas être égal à l'élément du milieu car alors nous n'atteindrions pas le cas trois, alors x est susceptible de se trouver dans la moitié gauche pour cette condition.

Donc, dans cette condition, nous ajustons high à mid moins un, sinon nous cherchons dans la moitié non triée en ajustant low à mid plus un.

Donc, c'est notre stratégie de diviser pour régner pour la recherche binaire.

Écrivons maintenant le code pour cela et voyons si cela fonctionne. Je vais écrire une fonction circular array search qui recherchera un nombre x dans un tableau de taille n, et elle retournera l'index de x s'il est trouvé dans le tableau.

Donc, comme nous le faisons dans une recherche binaire normale, nous allons d'abord définir deux variables low à zéro et high à n moins un.

Et tant que low est inférieur ou égal à high, tant que notre espace de recherche est valide, tant que notre segment est valide, un segment valide aura au moins un élément lorsque low sera égal à high, nous calculons l'index du milieu comme low plus high divisé par deux.

Maintenant, si x est égal à l'élément du milieu, alors nous avons trouvé x, nous retournons l'index mid.

Sinon, nous devons décider si nous allons dans la moitié gauche ou la moitié droite, si nous allons chercher vers les indices supérieurs ou inférieurs.

Et nous le faisons en trouvant d'abord quelle partie du tableau, quelle partie de l'espace de recherche est triée.

Si a mid est inférieur ou égal à a high, l'élément à l'index high, alors la moitié droite est triée.

La moitié droite est triée, alors nous pouvons facilement vérifier si x est susceptible de se trouver dans cette moitié triée ou non.

Donc, si x est supérieur à l'élément du milieu, et x est inférieur ou égal à l'élément à l'index high, nous allons chercher dans la moitié droite triée en ajustant low à mid plus un.

Sinon, nous savons que l'élément n'est pas dans la moitié droite, donc il est définitivement dans la moitié gauche.

Donc, nous allons ajuster high à mid moins un pour aller dans la moitié gauche.

Maintenant, la moitié droite est triée, c'est sûr, nous le savons, mais la moitié gauche, elle pourrait être soit triée, soit non triée, peu importe.

Pour un cas spécial, lorsque le segment lui-même est trié, la moitié gauche pourrait aussi être triée.

Mais indépendamment de cela, en utilisant ces deux conditions, nous écartons l'une des moitiés et nous choisissons l'un des sous-segments.

D'accord, donc maintenant si la moitié droite n'est pas triée, alors la moitié gauche sera définitivement triée.

Donc, soit nous écrivons cette condition a mid supérieur ou égal à a low.

Soit je devrais écrire a low inférieur ou égal à a mid comme nous l'avons écrit précédemment.

Donc, c'est le cas trois, même si nous n'écrivons pas cette condition et écrivons simplement un else, nous allons bien parce que cela sera vrai de toute façon, à ce stade.

Donc, maintenant la moitié gauche est triée.

Donc, nous pouvons voir si notre x est susceptible de se trouver dans la moitié gauche.

Maintenant, si x est entre a low et a mid, inférieur ou égal à supérieur ou égal à a low et inférieur à a mid, alors il est susceptible de se trouver dans cette moitié.

Donc, nous allons ajuster high à mid moins un.

Sinon, si x n'est pas susceptible de se trouver dans la moitié gauche, alors nous allons chercher vers la droite en ajustant low à mid plus un.

Et finalement, si nous sortons de cette boucle while sans trouver x, sans rien retourner, nous retournons moins un pour dire que nous n'avons pas pu trouver x dans le tableau.

Écrivons maintenant la méthode principale, nous allons d'abord initialiser un tableau et c'est le même tableau.

Les éléments sont les mêmes que ceux que nous avons utilisés dans nos exemples tout au long.

Maintenant, demandons à l'utilisateur d'entrer un nombre x depuis la console.

Et maintenant, nous appelons la méthode pour rechercher x, la taille du tableau est huit.

Donc, nous passons huit comme deuxième argument.

Maintenant, si cette méthode retourne moins un, nous allons dire que nous n'avons pas pu trouver l'élément dans le tableau, le nombre dans le tableau.

Et si ce n'est pas moins un, nous imprimons l'index.

Donc, c'est notre programme C.

Et maintenant, exécutons-le et voyons ce qui se passe.

Recherchons le nombre huit dans le tableau.

Et cela semble être correct.

L'élément huit est à l'index six.

Exécutons cela à nouveau et recherchons le nombre 12 dans le tableau.

Et cela est également correct.

Et cela semble fonctionner pour d'autres cas également.

Et modifions ce tableau.

Disons que nous voulons prendre un tableau dans lequel les éléments sont déjà triés.

Prenons huit éléments à nouveau.

Recherchons l'élément quatre dans ce tableau, d'accord, cela est également correct.

Donc, nous semblons être bons pour tous les cas de test.

Eh bien, en fait, non, nous ne sommes pas bons pour tous les cas de test.

Si nous avons un tableau avec des doublons, comme celui-ci, ce tableau est toujours trié de manière circulaire.

C'est le premier élément dans la séquence triée zéro.

Mais si nous avons des doublons dans le tableau trié de manière circulaire, il ne sera pas possible de décider si la moitié gauche est triée ou la moitié droite est triée.

En utilisant les conditions ci-dessus que nous avons utilisées avec ces conditions.

Donc, le tableau doit être strictement croissant de manière circulaire, et tous les éléments doivent être distincts.

Si nous exécutons cela, disons que nous voulons rechercher un nombre zéro, alors cela dit zéro non trouvé dans le tableau, ce qui n'est pas correct.

Si nous avons des doublons, nous ne pouvons pas faire mieux que grand O de n, nous devrons effectuer une recherche linéaire seulement si les éléments sont distincts, nous pouvons effectuer une recherche binaire.

D'accord, donc c'était la recherche d'un élément dans un tableau trié de manière circulaire sans doublons en utilisant la recherche binaire.

Merci d'avoir regardé.