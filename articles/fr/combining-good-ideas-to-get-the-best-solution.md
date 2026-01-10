---
title: Comment combiner de bonnes idées pour obtenir la meilleure solution à un problème
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-30T23:22:55.000Z'
originalURL: https://freecodecamp.org/news/combining-good-ideas-to-get-the-best-solution
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fc306db49c47664ed82751b.jpg
tags:
- name: algorithms
  slug: algorithms
- name: '#big o notation'
  slug: big-o-notation
- name: Computer Science
  slug: computer-science
- name: data structures
  slug: data-structures
- name: Problem Solving
  slug: problem-solving
seo_title: Comment combiner de bonnes idées pour obtenir la meilleure solution à un
  problème
seo_desc: 'By Jose J. Rodríguez

  Trade-offs are present in all our activities. Maybe you have heard the so-called
  "No free lunch theorem" in Machine Learning. The theorem states that there is no
  silver bullet when it comes to machine learning models. But in fact...'
---

Par Jose J. Rodríguez

Les compromis sont présents dans toutes nos activités. Peut-être avez-vous entendu parler du soi-disant "No free lunch theorem" en Machine Learning. Le théorème stipule qu'il n'existe pas de solution miracle en matière de modèles d'apprentissage automatique. Mais en fait, il n'existe jamais de solution miracle pour quoi que ce soit. 

Et ce n'est pas un principe de l'informatique mais un principe économique.

Si vous avez écrit du code pendant plus d'un mois, vous avez probablement expérimenté la nécessité des compromis en programmation – ou au moins en avez entendu parler. 

Parfois, vous sacrifiez la performance au nom de la sécurité, la sécurité au nom de la scalabilité, la beauté et la lisibilité au nom de la performance, et ainsi de suite. N'oubliez pas que vous sacrifiez probablement aussi les fêtes et le plaisir en général au nom de la programmation, alors faites en sorte que cela en vaille la peine.

Dans le cas spécifique des algorithmes, les principales ressources sont le temps et la mémoire, donc les compromis impliquent toujours ces ressources. 

Il est courant de trouver plusieurs solutions pour le même problème, car l'une d'entre elles est plus rapide mais l'autre est moins coûteuse en termes de stockage. Et bien sûr, il y a d'autres facteurs comme l'implémentation, la simplicité et la sécurité. 

Dans cet article, je vais écrire sur la manière dont vous pouvez combiner plusieurs solutions pour obtenir celle qui répond à toutes vos exigences.

Tout d'abord, je vais montrer une idée intéressante proposée par E.W. Dijkstra pour trouver des nombres premiers. Ensuite, je vais montrer une idée à laquelle j'ai pensé pour obtenir une structure de données qui combine la puissance des tableaux et des listes chaînées. 

## Exigences

Je suppose que vous avez des compétences de base en programmation ainsi que quelques connaissances sur les structures de données comme les tableaux, les listes chaînées et les tas.

Vous devriez également avoir une certaine compréhension de la notation big-O pour calculer la complexité.

Enfin, il serait bon que vous soyez familier avec l'algorithme appelé le Crible d'Ératosthène. Dans le cas contraire, vous pouvez consulter cet article [lien](https://www.geeksforgeeks.org/sieve-of-eratosthenes/).

Il n'y a pas d'autres connaissances préalables requises pour comprendre ce que je m'apprête à discuter.

## Deux algorithmes, un problème

Le problème est de trouver tous les nombres premiers de 0 (zéro) à N. C'est le genre de problème que vous apprenez à résoudre lorsque vous commencez votre parcours en programmation. Et je veux commencer par la solution la plus simple.

### L'algorithme naïf

Dans l'algorithme naïf, nous itérons sur tous les nombres ```x``` de 2 à N. Ensuite, nous vérifions si ```x``` a un diviseur autre que lui-même et un. Pour la dernière étape, nous pouvons vérifier pour chaque nombre ```d``` entre 2 et ```x - 1``` s'il est un diviseur ou non.

Il y a de la place pour l'amélioration dans la dernière étape, car nous n'avons besoin de vérifier que les diviseurs qui sont inférieurs ou égaux à la racine carrée de x. Un pseudocode de l'algorithme est écrit ci-dessous :

```
   primes(N):
      prime_numbers <- [] # liste vide
      for x = 2 to N:
          is_prime <- true
          for d = 2 to sqrt(x):
              if d divides x:
                   is_prime <- false # nous avons trouvé un diviseur de x donc x n'est pas un nombre premier
          if is_prime:
               prime_numbers.add(x) # si nous n'avons pas trouvé de diviseur alors x est premier
       return prime_numbers             
```

Quelle est la complexité d'exécution de l'algorithme précédent ? Eh bien, nous prenons chaque nombre de 2 à N et pour chacun, nous itérons sur tous ses diviseurs possibles. Nous effectuons donc ```O(N*sqrt(N))``` opérations, où ```sqrt``` représente la fonction racine carrée.

Qu'en est-il de la mémoire ? Nous stockons uniquement les nombres premiers que nous trouvons. Pour un N suffisamment grand, le nombre de nombres premiers est relativement petit par rapport à N. Donc, désignons la complexité mémoire par ```O(Primes(N))```, où ```Primes(N)``` est le nombre de nombres premiers entre 0 et N. Notez que cela est optimal en termes de mémoire car nous devons au moins stocker tous les nombres premiers.

### Le Crible d'Ératosthène

Vous savez probablement déjà qu'il existe un meilleur algorithme pour trouver tous les nombres premiers dans une plage donnée : le crible d'Ératosthène. Examinons-le.

L'idée est de maintenir un tableau de longueur N où chaque entrée est soit false soit true. Si la i-ème position dans le tableau est true, alors nous disons que ```i``` est un nombre premier, sinon ```i``` n'est pas premier.

Nous commençons avec toutes les positions à true, puis pour chaque position, en commençant par ```i = 2```, nous mettons à false chaque multiple de ```i```. 

Nous obtenons un tableau dans lequel chaque position avec une valeur true représente un nombre premier. Le code avec quelques optimisations est présenté ci-dessous.

```
    primes(N):
        prime_numbers <- [] # liste vide
        sieve <- une liste booléenne de longueur égale à N et tous ses éléments définis à true

        for i = 2 to sqrt(N): # nous n'avons besoin d'analyser que les nombres inférieurs ou égaux à sqrt(N)
            if sieve[i]: # si sieve[i] est true alors i est premier
                prime_numbers.add(i)
                for j = i*i to N: # nous pouvons commencer la boucle interne à i*i
                    sieve[j] <- false
                    j <- j + i
         return prime_numbers
```

Il peut être prouvé que l'algorithme décrit ci-dessus effectue [O(N log(N))](https://www.geeksforgeeks.org/how-is-the-time-complexity-of-sieve-of-eratosthenes-is-nloglogn/) opérations, ce qui est mieux que l'approche naïve. 

Il peut même être amélioré à [O(N)](https://www.geeksforgeeks.org/sieve-eratosthenes-0n-time-complexity)! Mais nous devons stocker un tableau avec tous les N nombres, et ainsi, nous obtenons un algorithme plus coûteux en termes de mémoire. Voici le compromis : le temps en échange de la mémoire.

Pouvons-nous concevoir un algorithme qui est plus rapide que l'idée naïve mais moins coûteux en mémoire que le crible d'Ératosthène ? 

## Dijkstra et la ligne de production

Dans les années 60, E.W. Dijkstra a écrit dans l'un de ses manuscrits [[PDF](https://www.cs.utexas.edu/~EWD/ewd02xx/EWD249.PDF)] un algorithme qui combine les idées naïves et de crible. Mais avant d'en parler, analysons les différences entre les deux algorithmes précédents.  

Lorsque nous appliquons l'algorithme naïf, nous nous concentrons sur l'analyse de chaque nombre pour savoir s'il est premier ou non. Lorsque nous appliquons le crible, nous analysons, pour chaque nombre premier, tous ses multiples. La différence peut être illustrée avec l'analogie suivante.

Imaginez que nous voulons construire plusieurs produits, comme des figurines. Nous avons deux options : les construire un par un ou appliquer une ligne de production et à chaque étape, nous ajoutons un composant de la figurine. Avec cette dernière, nous finissons par produire plus en moins de temps, mais nous avons besoin de "l'infrastructure de ligne".

Dijkstra a combiné ces idées en analysant un nombre à la fois mais en tirant parti des opérations précédentes. Nous pouvons maintenir un ensemble de nombres premiers qui ont déjà été découverts, et, pour chacun de ces nombres premiers, stocker le plus petit multiple qui n'a pas encore été analysé.

Par exemple :

Si nous analysons le nombre 6, alors nous avons stocké les nombres premiers 2, 3 et 5, ainsi que leurs plus petits multiples non analysés qui sont : 6 pour 2, également 6 pour 3, et 10 pour 5.

Ensuite, lorsque nous analysons un nouveau nombre, nous prenons le plus petit multiple stocké jusqu'à ce moment et si ce multiple est supérieur au nouveau nombre, alors nous avons trouvé un nouveau nombre premier. Sinon, nous avons un nombre composé et nous devons mettre à jour les multiples des nombres premiers stockés qui ont le nouveau nombre comme leur plus petit multiple.

Nous commençons par stocker le nombre premier ```2``` avec le plus petit multiple ```4``` également. Ensuite, lorsque nous analysons ```3```, nous trouvons que ```4 > 3``` donc ```3``` est premier. Nous stockons ```3``` ainsi que son plus petit multiple qui n'a pas encore été analysé (```6```). Lorsque nous analysons ```4```, nous trouvons que ```4``` est stocké comme un multiple de ```2```, puis nous mettons à jour le multiple de ```2``` qui sera maintenant ```6```. Lorsque nous analysons ```5```, nous trouvons que ```6 > 5``` donc ```5``` est un nombre premier et nous le stockons avec ```10```, et ainsi de suite... Le code est présenté ci-dessous.

```
    primes(N):
        primes_pool <- Heap( (4, 2) ) # un tas qui contient un tuple avec un nombre premier (2) et son plus petit multiple qui n'a pas encore été analysé (4).
        prime_numbers <- [2] # une liste qui contient le nombre 2
        for i = 3 to N:
            tuple <- getMin(primes_pool) # obtenir le tuple avec le multiple minimum, le nombre premier attaché à celui-ci est sans importance
            mult <- tuple.first # le multiple est stocké dans la première position du tuple
            if mult > i:
                prime_numbers.add(i) # i est premier !
                primes_pool.insert( (i*i, i) ) # nous insérons i ainsi que leur plus petit multiple, mais il peut être inséré i*i à la place et l'algorithme reste correct
                continue
            # sinon i n'est pas premier et alors...
            for t such that t is in primes_pool and t.first is equal to mult:
                t.first <- t.first + t.second # nous mettons à jour chaque tuple dans le pool qui a i comme son plus petit multiple
        return prime_numbers
```

La méthode précédente ne stocke que les nombres premiers et un autre nombre pour chacun de ces nombres premiers. Nous avons donc une complexité mémoire de ```O(Primes(N))``` qui est la même que l'idée naïve. 

Si nous stockons les nombres premiers ainsi que leurs multiples dans une structure comme un tas, nous obtenons une complexité temporelle de ```O(N*log N)``` qui est la même que le crible. Nous avons donc obtenu ce que nous voulions !

L'astuce ici est que nous n'avons pas besoin de marquer chaque multiple du nombre premier donné mais seulement le plus petit multiple.

Je dois dire que ce n'est pas une idée pratique dans le sens où la complexité mémoire du crible d'Ératosthène n'est pas si mauvaise et c'est un algorithme très facile à implémenter. 

Mon point est que parfois, si vous avez plusieurs idées, chacune d'entre elles ne pouvant être appliquée en raison d'un défaut, alors peut-être est-il bon de combiner leurs forces. Cela vous donne une solution hybride pour votre problème. 

L'Usine de Nombres Premiers de Dijkstra m'a appris à penser de cette manière, bien que je n'aie jamais implémenté cet algorithme dans un scénario réel.

## Combiner les tableaux avec les listes chaînées

Les tableaux sont des structures simples qui nous permettent d'obtenir un élément par son index en temps constant. Mais nous avons besoin de ```O(N)``` opérations pour insérer ou supprimer un élément dans le tableau dans le pire des cas, où N est la longueur du tableau.

D'autre part, les listes chaînées sont des structures composées de nœuds. Chaque nœud a une référence au suivant, et, dans le cas des listes doublement chaînées, chaque nœud a également une référence au précédent. 

Dans ce cas, nous avons besoin de ```O(N)``` opérations pour atteindre un nœud dans le pire des cas, mais les opérations d'insertion et de suppression peuvent être effectuées en temps constant. 

Je pense qu'il est naturel de penser à une "structure de données parfaite" qui nous permet de faire les trois opérations en temps constant. Malheureusement, une telle structure n'existe pas, mais j'ai trouvé un point médian entre les deux pôles opposés.

Le "problème" avec les tableaux est qu'ils maintiennent une référence à tous leurs éléments. Cela nous permet de récupérer n'importe quel élément avec le même nombre d'opérations, peu importe où se trouve l'élément. 

Mais le maintien de ces références est ce qui rend les insertions et les suppressions si coûteuses. 

En ce qui concerne les listes chaînées, nous ne maintenons qu'une référence au premier et au dernier nœud et chaque nœud a une référence à ses voisins. Donc, lors de l'insertion ou de la suppression d'un nouvel élément, nous n'avons besoin de changer que quelques références. 

Mais ce manque de références est la raison pour laquelle nous devons dépenser autant d'opérations pour obtenir un élément dans le pire des cas.

En voyant le problème sous cet angle, l'idée de trouver un point médian dans le nombre de références semble naturelle. Que se passe-t-il si nous maintenons une référence à ```sqrt(N)``` nœuds de la liste chaînée au lieu de référencer uniquement le premier et le dernier élément ?

Cela nous permet d'avoir une liste de longueur ```sqrt(N)``` telle que la distance entre chacun de ces nœuds dans la liste réelle est ```sqrt(N)```. Ayant cela, nous pouvons faire chaque opération (index, insertion et suppression) en ```O(sqrt(N))```.

Si vous voulez voir plus de détails sur cette structure et une implémentation en Lisp, vous pouvez le faire [ici](https://github.com/josejorgers/indexed-linked-list).

J'ai également écrit un article à ce sujet dans mon [blog personnel](https://jj.hashnode.dev/combining-good-ideas-to-get-the-best-solution).

## Conclusions

Nous avons vu deux exemples de la manière dont vous pouvez combiner des solutions existantes pour en obtenir une autre qui possède certaines des bonnes qualités de chacune d'entre elles. Mon but était de vous montrer cette façon de penser, pas seulement des exemples spécifiques. 

Notez que dans le cas de l'idée de Dijkstra, nous avons pu obtenir le temps de la solution la plus rapide et la complexité mémoire de l'algorithme naïf. Dans le deuxième exemple, nous avons simplement obtenu un point médian, donc la solution la plus rapide est toujours plus rapide et la solution la moins coûteuse en mémoire est toujours moins chère. 

Mais la nouvelle structure est comme un athlète de décathlon – elle est bonne dans chaque spécificité, mais pas la meilleure dans l'une d'entre elles. 

Donc, n'essayez pas de trouver la solution miracle – rappelez-vous qu'il n'y a pas de repas gratuit. Même l'idée de Dijkstra a l'inconvénient d'être plus difficile à implémenter et à comprendre.

J'espère que vous avez appris quelque chose de cet article. Vous pouvez trouver plus de contenu comme celui-ci dans mon [blog personnel](https://jj.hashnode.dev) et en me suivant sur [Twitter](https://twitter.com/josejorgexl).