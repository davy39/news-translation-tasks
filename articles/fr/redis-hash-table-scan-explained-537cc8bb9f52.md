---
title: Comment fonctionne la fonction de balayage de la table de hachage Redis
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-23T13:15:23.000Z'
originalURL: https://freecodecamp.org/news/redis-hash-table-scan-explained-537cc8bb9f52
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eUYhCqLYo_cQpMSQvelQOw.jpeg
tags:
- name: coding
  slug: coding
- name: database
  slug: database
- name: Redis
  slug: redis
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment fonctionne la fonction de balayage de la table de hachage Redis
seo_desc: 'By Ehud Tamir

  One of the big challenges for me as a software developer is reading other people’s
  code. For this post, I read an interesting piece of C code that I didn’t know before,
  and I’m about to present it to you. The code I’m going to talk abou...'
---

Par Ehud Tamir

L'un des grands défis pour moi en tant que développeur logiciel est de lire le code d'autres personnes. Pour cet article, j'ai lu un morceau intéressant de code C que je ne connaissais pas auparavant, et je m'apprête à vous le présenter. Le code dont je vais parler fait partie de la base de données [**Redis**](https://en.wikipedia.org/wiki/Redis), et il peut être trouvé [ici](https://github.com/antirez/redis/blob/e504583b7806d946da9c3627784d551a742be4d0/src/dict.c#L838).

Redis est une base de données clé-valeur. Chaque entrée dans la base de données est un mappage d'une clé à une valeur. Les valeurs peuvent avoir plusieurs types. Il y a des entiers, des listes, des tables de hachage et plus encore. En coulisses, la base de données elle-même est également une table de hachage. Dans cet article, nous allons explorer la commande SCAN dans Redis.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eUYhCqLYo_cQpMSQvelQOw.jpeg)
_Par © User:Colin / Wikimedia Commons, CC BY-SA 4.0, [https://commons.wikimedia.org/w/index.php?curid=30343877](https://commons.wikimedia.org/w/index.php?curid=30343877" rel="noopener" target="_blank" title=")_

### Redis SCAN

SCAN est une commande d'itération basée sur un curseur, permettant à un client de parcourir tous les éléments d'une table. Ce scanner basé sur un curseur accepte un entier **cursor** à chaque appel, et retourne **un lot d'éléments** et la **valeur du curseur** à utiliser lors du prochain appel à SCAN. La valeur initiale du curseur est 0, et lorsque SCAN retourne 0 comme valeur du curseur suivant, cela signifie que le balayage est terminé et que tous les éléments ont été vus par le client.

La commande SCAN a quelques propriétés intéressantes :

1. Elle garantit que tous les éléments présents dans la table seront retournés _au moins une fois_.
2. Elle est **sans état**. La table n'enregistre aucune donnée sur ses scanners actifs. Cela signifie également que les balayages ne verrouillent pas la base de données.
3. Elle est résistante au redimensionnement de la table. Pour maintenir un temps d'accès O(1), les tables de hachage supportent un certain [facteur de charge](https://en.wikipedia.org/wiki/Hash_table#Key_statistics). Le facteur de charge mesure à quel point la table est "pleine" à un moment donné. Lorsque le facteur de charge devient trop grand ou trop petit, la table est redimensionnée. SCAN maintiendra ses garanties même si elle est appelée pendant que la table est redimensionnée.

### Implémentation

SCAN est implémenté dans dict.c, dans la fonction `dictScan()`. Voici la signature de la fonction et d'autres détails :

```c
unsigned long dictScan(dict *d,
                       unsigned long v,
                       dictScanFunction *fn,
                       dictScanBucketFunction* bucketfn,
                       void *privdata)
{
    dictht *t0, *t1;
    const dictEntry *de, *next;
    unsigned long m0, m1;

    if (dictSize(d) == 0) return 0;
    // ...
```

Points à noter :

* La fonction accepte 5 paramètres : `dict *d`, le dictionnaire à scanner, `unsigned long v`, le curseur, et 3 autres paramètres que nous verrons plus tard.
* La fonction retourne la valeur du curseur à utiliser lors du prochain appel à cette fonction. Si la fonction retourne 0, cela signifie que le balayage est terminé.
* `if (dictSize(d) == 0) return 0;`. Lorsque le dictionnaire est vide, la fonction retourne 0 pour indiquer que le balayage est terminé.

#### 1. Balayage normal

Le code suivant scanne un ensemble d'éléments :

```c
if (!dictIsRehashing(d)) {
    t0 = &(d->ht[0]);
    m0 = t0->sizemask;

    /* Émettre les entrées au curseur */
    if (bucketfn) bucketfn(privdata, &t0->table[v & m0]);
    de = t0->table[v & m0];
    while (de) {
        next = de->next;
        fn(privdata, de);
        de = next;
    }
    
    /* Définir les bits non masqués pour que l'incrémentation du curseur inversé
     * opère sur les bits masqués */
    v |= ~m0;

    /* Incrémenter le curseur inversé */
    v = rev(v);
    v++;
    v = rev(v);
    
} else {
    // ...
```

Analysons cela étape par étape. Commençons par la première ligne ci-dessous :

```
if (!dictIsRehashing(d)) {
    t0 = &(d->ht[0]);
    m0 = t0->sizemask;
```

Le rehachage est le processus de répartition uniforme des éléments dans une table après son redimensionnement. La table de hachage dict.c rehache _incrémentalement_, ce qui signifie qu'elle ne rehache pas toute la table en une fois, mais peu à peu. Chaque opération effectuée sur la table, comme ajouter, supprimer, trouver, effectue également une étape de rehachage. Cela permet de garder la table disponible pour les opérations pendant le rehachage. En raison de la manière dont le rehachage est implémenté, la fonction fonctionne différemment pendant le rehachage. Nous allons commencer par voir ce qui se passe lorsque la table n'est pas en cours de rehachage.

Un pointeur vers la table de hachage est sauvegardé dans la variable locale `t0`, et son **masque de taille** est sauvegardé dans `m0`. **Masque de taille** : les tables de hachage dict.c sont toujours de taille `2^n`. Pour une taille de table donnée, le masque de taille est `2^n-1`, qui est un nombre binaire avec ses `n` bits les moins significatifs définis à 1. Par exemple, pour `n=4; 2^n-1 = 00001111`. Pour une clé donnée, son emplacement dans la table de hachage sera les `n` derniers bits du **hachage** de la clé. Nous verrons cela en action dans un instant.

La table de hachage dict.c utilise l'[adressage ouvert](https://en.wikipedia.org/wiki/Open_addressing). Chaque entrée dans la table est une liste chaînée d'éléments avec une valeur de hachage conflictuelle. Cela s'appelle un **bucket**. Dans cette partie suivante, un **bucket** d'éléments est scanné :

```
/* Émettre les entrées au curseur */
if (bucketfn) bucketfn(privdata, &t0->table[v & m0]);
de = t0->table[v & m0];
while (de) {
    next = de->next;
    fn(privdata, de);
    de = next;
}
```

Notez l'utilisation du **masque de taille** : `t0->table[v & m0]`. v peut être en dehors de la plage indexable de la table. v & m0 utilise le masque de taille pour garder uniquement les n derniers chiffres de v, et produit un index valide dans la table.

Vous avez peut-être deviné à quoi sert `bucketfn`. `bucketfn` est fourni par l'appelant et est appliqué à chaque bucket d'éléments. Il reçoit également `privdata`, qui est une donnée arbitraire passée à `dictScan()` par l'appelant. De manière similaire, `fn` est appliqué à toutes les entrées du bucket une par une. Notez qu'un bucket peut être vide, auquel cas sa valeur est `NULL`.

OK, donc nous avons itéré sur un bucket d'éléments. Qu'est-ce qui suit ? Nous allons retourner la valeur du curseur pour le prochain appel à `dictScan()`. Cela se fait en incrémentant le curseur actuel `v`, mais avec une astuce ! Le curseur est d'abord inversé, puis incrémenté, et enfin inversé à nouveau :

```
    /* Définir les bits non masqués pour que l'incrémentation du curseur inversé
     * opère sur les bits masqués */
    v |= ~m0;
    /* Incrémenter le curseur inversé */
    v = rev(v);
    v++;
    v = rev(v);
```

Tout d'abord, `v |= ~m0` définit tous les bits non masqués dans `v` à 1. L'effet est que lors de l'inversion de `v` et de l'incrémentation, ces bits seront effectivement ignorés. Ensuite, `v` est inversé, incrémenté et inversé à nouveau. Regardons un exemple :

```
Taille de la table = 16 (n = 4, m0 = 16-1 = 00001111)
v = 00001000 (Curseur actuel)
v |= ~m0;    // v == 11111000  (~m0 = 11110000)
v = rev(v);  // v == 00011111
v++;         // v == 00100000
v = rev(v);  // v == 00000100
```

Après cette magie de bits, `v` est retourné.

**Pourquoi le curseur est-il inversé avant d'être incrémenté ?** La table peut grandir entre les itérations. Cela garantit que le curseur reste valide. Lorsque la table grandit, des bits supplémentaires sont ajoutés à son masque de taille **à partir de la gauche**. En incrémentant le nombre inversé, nous pouvons étendre les indices de la table plus petite dans la plus grande.

Par exemple : Supposons que l'ancienne taille de la table était de 16 (masque de taille `00001111`) et que le curseur était `00001000`. Lorsque la table grandit à 32 éléments, son masque de taille sera `00011111`. Tous les éléments précédemment dans le slot `00001000` seront mappés soit à `00001000` soit à `00011000` dans la nouvelle table. Ces curseurs sont compatibles avec les tables plus petites et plus grandes !

#### 2. Balayage pendant le rehachage de la table

La dernière partie que nous devons comprendre est comment le balayage fonctionne pendant que la table est en cours de rehachage. Le **rehachage incrémental** est implémenté dans dict.c en ayant deux tables actives en même temps. Une deuxième table est créée lorsque la table de hachage est redimensionnée. Les nouveaux éléments sont ajoutés à la nouvelle table. À chaque étape de rehachage, des éléments de l'ancienne table sont déplacés vers la nouvelle table. Lorsque l'ancienne table devient vide, elle est supprimée.

Lors de l'exécution d'un balayage, les deux tables, ancienne et nouvelle, sont scannées pour les éléments, en commençant par la **plus petite** **table**. Après que les éléments de la plus petite table ont été scannés, les _éléments complémentaires_ de la plus grande table sont scannés. Ainsi, tous les éléments couverts par le curseur `v` sont scannés. Voyons à quoi cela ressemble. Voici l'extrait de code complet, nous allons le décomposer ci-dessous :

```c
    } else {  // dictIsRehashing(d)
        t0 = &d->ht[0];
        t1 = &d->ht[1];

        /* Assurer que t0 est la plus petite table et t1 la plus grande */
        if (t0->size > t1->size) {
            t0 = &d->ht[1];
            t1 = &d->ht[0];
        }

        m0 = t0->sizemask;
        m1 = t1->sizemask;

        /* Émettre les entrées au curseur */
        if (bucketfn) bucketfn(privdata, &t0->table[v & m0]);
        de = t0->table[v & m0];
        while (de) {
            next = de->next;
            fn(privdata, de);
            de = next;
        }

        /* Itérer sur les indices de la plus grande table qui sont l'expansion
         * de l'index pointé par le curseur dans la plus petite table */
        do {
            /* Émettre les entrées au curseur */
            if (bucketfn) bucketfn(privdata, &t1->table[v & m1]);
            de = t1->table[v & m1];
            while (de) {
                next = de->next;
                fn(privdata, de);
                de = next;
            }

            /* Incrémenter le curseur inversé non couvert par le masque plus petit.*/
            v |= ~m1;
            v = rev(v);
            v++;
            v = rev(v);

            /* Continuer tant que les bits couverts par la différence de masque ne sont pas nuls */
        } while (v & (m0 ^ m1));
    }
```

Tout d'abord, `t0` et `t1` sont utilisés pour stocker les tables plus petite et plus grande respectivement, avec `m0` et `m1` les masques de taille pour chacune. Ensuite, la plus petite table est scannée, comme nous l'avons vu précédemment.

Ensuite, le curseur est utilisé pour indexer dans la plus grande table, en utilisant le masque de taille plus grand `m1` : `de = t1->table[v & m1]`. Dans la boucle interne, le curseur est incrémenté pour couvrir toutes les expansions de l'index de la plus petite table.

Par exemple, si l'index du bucket dans la plus petite table était `0100`, et que la plus grande table est deux fois plus grande, les indices couverts dans cette boucle seront `00100` et `10100`. La condition du do-while empêche d'incrémenter le curseur au-delà de la plage couverte par le bucket de la petite table : `while (v & (m0 ^ m1));`. Je vous laisse comprendre ce dernier bit :)

C'est tout ! Nous avons couvert toute la fonction de balayage de la table de hachage. La seule pièce manquante est l'implémentation de `rev(v)`, qui est une fonction générale pour inverser les bits d'un nombre. L'implémentation utilisée dans dict.c est particulièrement intéressante car elle atteint un temps d'exécution O(log n). Je pourrais en parler dans un futur article.

Merci d'avoir lu ! Un grand merci à [Dvir Volk](https://www.freecodecamp.org/news/redis-hash-table-scan-explained-537cc8bb9f52/undefined) pour son inspiration et son soutien ! Merci à [Jason Li](https://www.freecodecamp.org/news/redis-hash-table-scan-explained-537cc8bb9f52/undefined) pour ses commentaires qui m'ont aidé à corriger une erreur dans l'article.