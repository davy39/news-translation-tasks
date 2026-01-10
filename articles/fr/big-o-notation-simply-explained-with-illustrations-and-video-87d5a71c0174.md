---
title: Notation Big O — Explication simple avec illustrations et vidéo
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2018-08-21T18:58:28.000Z'
originalURL: https://freecodecamp.org/news/big-o-notation-simply-explained-with-illustrations-and-video-87d5a71c0174
coverImage: null
tags:
- name: algorithms
  slug: algorithms
- name: Data Science
  slug: data-science
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Notation Big O — Explication simple avec illustrations et vidéo
seo_desc: 'Illustration (and most in this article) by Adit Bhargava

  Big O notation is used to communicate how fast an algorithm is. This can be important
  when evaluating other people’s algorithms, and when evaluating your own! In this
  article, I’ll explain what...'
---

![Image](https://cdn-media-1.freecodecamp.org/images/0*Z0GAhU_e8tTBnm_C.jpg)
*Illustration (et la plupart dans cet article) par Adit Bhargava*

La notation Big O est utilisée pour communiquer la rapidité d'un algorithme. Cela peut être important lors de l'évaluation des algorithmes d'autres personnes, et lors de l'évaluation des vôtres ! Dans cet article, je vais expliquer ce qu'est la notation Big O et vous donner une liste des temps d'exécution les plus courants pour les algorithmes qui l'utilisent.

### Les temps d'exécution des algorithmes croissent à des rythmes différents

![Image](https://cdn-media-1.freecodecamp.org/images/1*Qd-Lmu7Xyy30i30dA4RnSg.gif)
*Mon fils explique la notation Big 'O'.*

Mon fils Judah a beaucoup de jouets. En fait, il a acquis *un milliard* de jouets ! Vous seriez surpris de voir à quelle vitesse un enfant peut obtenir autant de jouets s'il est le premier petit-enfant des deux côtés de la famille. ??

Quoi qu'il en soit, Judah a un problème. Lorsque ses amis viennent et veulent jouer avec un jouet spécifique, cela peut prendre une éternité pour trouver le jouet. Il veut donc créer un algorithme de recherche pour l'aider à trouver un jouet spécifique le plus rapidement possible. Il essaie de choisir entre deux algorithmes de recherche différents : la recherche simple et la recherche binaire. (Ne vous inquiétez pas si vous n'êtes pas familier avec ces algorithmes.)

L'algorithme choisi doit être à la fois rapide et correct. D'une part, la recherche binaire est plus rapide. Et Judah n'a souvent que 30 secondes avant que son ami ne s'ennuie à chercher un jouet. D'autre part, un algorithme de recherche simple est plus facile à écrire, et il y a moins de risques d'introduire des bugs. Il serait vraiment embarrassant si son ami trouvait des bugs dans son code ! Pour être extra prudent, Judah décide de chronométrer les deux algorithmes avec une liste de 100 jouets.

Supposons qu'il faille 1 milliseconde pour vérifier un jouet. Avec la recherche simple, Judah doit vérifier 100 jouets, donc la recherche prend 100 ms pour s'exécuter. D'autre part, il ne doit vérifier que 7 jouets avec la recherche binaire (log2 100 est environ 7, ne vous inquiétez pas si ce calcul est confus puisque ce n'est pas le point principal de cet article), donc cette recherche prend 7 ms pour s'exécuter. Mais en réalité, la liste contiendra un milliard de jouets. Si c'est le cas, combien de temps prendra la recherche simple ? Combien de temps prendra la recherche binaire ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*B1gUpMQDoauyYBht.jpg)

### Temps d'exécution pour la recherche simple vs. recherche binaire, avec une liste de 100 éléments

Judah exécute la recherche binaire avec 1 milliard de jouets, et cela prend 30 ms (log2 1,000,000,000 est environ 30). « 32 ms ! » pense-t-il. « La recherche binaire est environ 15 fois plus rapide que la recherche simple, car la recherche simple a pris 100 ms avec 100 éléments, et la recherche binaire a pris 7 ms. Donc la recherche simple prendra 30 × 15 = 450 ms, n'est-ce pas ? Bien en dessous des 30 secondes qu'il faut à mon ami pour s'ennuyer. » Judah décide d'opter pour la recherche simple. Est-ce le bon choix ?

Non. Il s'avère que Judah avait tort et a perdu un ami pour la vie. ? Le temps d'exécution pour la recherche simple avec 1 milliard d'éléments sera de 1 milliard de ms, soit 11 jours ! Le problème est que les temps d'exécution de la recherche binaire et de la recherche simple ne croissent pas au même rythme.

![Image](https://cdn-media-1.freecodecamp.org/images/0*GsE3ava8DELYKPhs.jpg)

Les temps d'exécution croissent à des vitesses très différentes ! À mesure que le nombre d'éléments augmente, la recherche binaire prend un peu plus de temps à s'exécuter, mais la recherche simple prend beaucoup plus de temps à s'exécuter. Ainsi, à mesure que la liste de nombres grandit, la recherche binaire devient soudainement beaucoup plus rapide que la recherche simple.

Donc Judah avait tort en disant que la recherche binaire est toujours 15 fois plus rapide que la recherche simple. S'il y a 1 milliard de jouets, c'est plutôt 33 millions de fois plus rapide.

Il est très important de savoir comment le temps d'exécution augmente à mesure que la taille de la liste augmente. C'est là que la notation Big O intervient.

La notation Big O vous indique la rapidité d'un algorithme. Par exemple, supposons que vous avez une liste de taille n. La recherche simple doit vérifier chaque élément, donc elle prendra n opérations. Le temps d'exécution en notation Big O est O(n).

Où sont les secondes ? Il n'y en a pas — Big O ne vous donne pas la vitesse en secondes. La notation Big O vous permet de comparer le nombre d'opérations. Elle vous indique à quelle vitesse l'algorithme croît.

Faisons un autre exemple. La recherche binaire nécessite log n opérations pour vérifier une liste de taille n. Quel est le temps d'exécution en notation Big O ? C'est O(log n). En général, la notation Big O est écrite comme suit.

![Image](https://cdn-media-1.freecodecamp.org/images/0*8IeDKdt-A5ED-hNe.jpg)

Cela vous indique le nombre d'opérations qu'un algorithme effectuera. On l'appelle notation Big O parce que vous mettez un « grand O » devant le nombre d'opérations.

#### Big O établit un temps d'exécution dans le pire des cas

![Image](https://cdn-media-1.freecodecamp.org/images/0*UK86o6VxxJcGHxVw.png)

Supposons que vous utilisez la recherche simple pour chercher un utilisateur dans votre base de données d'utilisateurs. Vous savez que la recherche simple prend O(n) temps pour s'exécuter, ce qui signifie que dans le pire des cas, votre algorithme devra parcourir chaque utilisateur de la base de données. Dans ce cas, vous cherchez un utilisateur avec le nom 'aardvark213'. C'est le premier utilisateur de la liste. Donc votre algorithme n'a pas eu à regarder chaque entrée — il l'a trouvé du premier coup. L'algorithme a-t-il pris O(n) temps ? Ou a-t-il pris O(1) temps parce qu'il a trouvé la personne du premier coup ?

La recherche simple prend toujours O(n) temps. Dans ce cas, l'algorithme a trouvé ce qu'il cherchait instantanément. C'est le meilleur scénario. Mais la notation Big O concerne le scénario du pire cas. Vous pouvez donc dire que, dans le pire des cas, l'algorithme devra parcourir chaque utilisateur de la base de données une fois. C'est O(n) temps. C'est une assurance — vous savez que la recherche simple ne sera jamais plus lente que O(n) temps.

### Quelques temps d'exécution courants de Big O

![Image](https://cdn-media-1.freecodecamp.org/images/1*G3c_ADXB8Klbi8XiRvhhqQ.png)
*De [xkcd](https://xkcd.com/399/" rel="noopener" target="_blank" title="). Si vous ne comprenez pas la blague, apprenez-en plus sur le problème du voyageur de commerce dans mon cours de Manning Publications. :)*

Voici cinq temps d'exécution Big O que vous rencontrerez souvent, classés du plus rapide au plus lent :

* O(log n), également connu sous le nom de temps logarithmique. Exemple : Recherche binaire.
* O(n), également connu sous le nom de temps linéaire. Exemple : Recherche simple.
* O(n * log n). Exemple : Un algorithme de tri rapide, comme quicksort.
* O(n²). Exemple : Un algorithme de tri lent, comme le tri par sélection.
* O(n!). Exemple : Un algorithme vraiment lent, comme le problème du voyageur de commerce.

### Visualisation des différents temps d'exécution Big O

![Image](https://cdn-media-1.freecodecamp.org/images/1*KQByBDNVa547MN6VXVWu9A.png)

Supposons que vous dessinez une grille de 16 cases, et que vous pouvez choisir parmi 5 algorithmes différents pour le faire. Si vous utilisez le premier algorithme, il vous faudra O(log n) temps pour dessiner la grille. Vous pouvez effectuer 10 opérations par seconde. Avec O(log n) temps, il vous faudra 4 opérations pour dessiner une grille de 16 cases (log 16 base 2 est 4). Il vous faudra donc 0,4 seconde pour dessiner la grille. Et si vous devez dessiner 1 024 cases ? Il vous faudra log 1 024 = 10 opérations, soit 1 seconde pour dessiner une grille de 1 024 cases. Ces chiffres utilisent le premier algorithme.

Le deuxième algorithme est plus lent : il prend O(n) temps. Il faudra 16 opérations pour dessiner 16 cases, et il faudra 1 024 opérations pour dessiner 1 024 cases. Combien de temps cela représente-t-il en secondes ?

Voici le temps qu'il faudrait pour dessiner une grille pour le reste des algorithmes, du plus rapide au plus lent :

![Image](https://cdn-media-1.freecodecamp.org/images/0*B42QL_XBJgDGfIFd.jpg)

Il existe d'autres temps d'exécution, mais ce sont les cinq plus courants.

Ceci est une simplification. En réalité, vous ne pouvez pas convertir un temps d'exécution Big O en un nombre d'opérations aussi proprement, mais c'est une bonne estimation.

### Conclusion

Voici les principaux points à retenir :

* La vitesse des algorithmes n'est pas mesurée en secondes, mais en croissance du nombre d'opérations.
* Au lieu de cela, nous parlons de la rapidité avec laquelle le temps d'exécution d'un algorithme augmente à mesure que la taille de l'entrée augmente.
* Le temps d'exécution des algorithmes est exprimé en notation Big O.
* O(log n) est plus rapide que O(n), mais il devient beaucoup plus rapide à mesure que la liste des éléments que vous recherchez grandit.

Et voici une vidéo qui couvre beaucoup de ce qui est dans cet article et plus encore.

J'espère que cet article vous a apporté plus de clarté sur la notation Big O. Cet article est basé sur une leçon de mon cours vidéo de Manning Publications intitulé [Algorithms in Motion](https://www.manning.com/livevideo/algorithms-in-motion?a_aid=algmotion&a_bid=9022d293). Le cours est basé sur le livre *amazing* [Grokking Algorithms](https://www.amazon.com/gp/product/1617292230/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=bcar08-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1617292230&linkId=83471c93327ff24766dd812f9799f95a) d'Adit Bhargava. C'est lui qui a dessiné toutes les illustrations amusantes de cet article.

Si vous apprenez mieux avec des livres, [procurez-vous le livre](https://www.amazon.com/gp/product/1617292230/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=bcar08-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1617292230&linkId=83471c93327ff24766dd812f9799f95a) ! Si vous apprenez mieux avec des vidéos, envisagez [d'acheter mon cours](https://www.manning.com/livevideo/algorithms-in-motion?a_aid=algmotion&a_bid=9022d293). Vous pouvez obtenir 39 % de réduction sur mon cours en utilisant le code '39carnes'.