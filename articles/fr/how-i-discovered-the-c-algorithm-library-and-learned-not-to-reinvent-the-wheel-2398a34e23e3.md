---
title: Comment j'ai découvert la bibliothèque d'algorithmes C++ et appris à ne pas
  réinventer la roue
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-05T21:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-i-discovered-the-c-algorithm-library-and-learned-not-to-reinvent-the-wheel-2398a34e23e3
coverImage: https://s3.amazonaws.com/cdn-media-1.freecodecamp.org/ghost/2019/05/1_dKpcV4KXSuBhWQLUsNm1gA-1.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment j'ai découvert la bibliothèque d'algorithmes C++ et appris à ne
  pas réinventer la roue
seo_desc: 'By M Chowdhury

  The other day out of curiosity, I looked into the C++ algorithm library. And found
  out quite a good number of cool features!

  This literally amazed me.

  Why? I mean I have mostly written C++ throughout my university life. And it was
  part...'
---

Par M Chowdhury

L'autre jour, par curiosité, j'ai exploré la bibliothèque d'algorithmes C++. Et j'y ai découvert un bon nombre de fonctionnalités intéressantes !

Cela m'a littéralement émerveillé.

Pourquoi ? Je veux dire, j'ai principalement écrit en C++ tout au long de ma vie universitaire. Et c'était particulièrement à cause de ma relation amour-haine avec la [programmation compétitive](https://en.wikipedia.org/wiki/Competitive_programming).

Et très malheureusement, je n'avais jamais vraiment profité de cette bibliothèque incroyable que C++ nous offre.

Mon Dieu, je me suis senti si naïf !

J'ai donc décidé qu'il était temps d'arrêter d'être naïf et de découvrir l'utilité des algorithmes C++ — au moins à un niveau supérieur. Et comme le disait un vieux sage, *partager le savoir, c'est le pouvoir* — alors me voilà.

**_Avertissement_** : J'ai largement utilisé des fonctionnalités de C++11 et au-delà. Si vous n'êtes pas très familiarisé avec les éditions plus récentes du langage, les extraits de code que j'ai fournis ici peuvent sembler un peu maladroits. D'un autre côté, la bibliothèque dont nous parlons ici est bien plus autonome et élégante que tout ce que j'ai écrit ci-dessous. N'hésitez pas à trouver des erreurs et à les signaler. De plus, je n'ai pas vraiment pu prendre en compte de nombreuses ajouts de C++17 dans cet article, car la plupart de ses fonctionnalités ne sont pas encore implémentées dans GCC.

Alors sans plus attendre, commençons !

1. `**all_of any_of none_of**`

Ces fonctions vérifient simplement si **tous**, **au moins un** ou **aucun** des éléments d'un conteneur suit une propriété spécifique définie par vous. Voir l'exemple ci-dessous :

```c++
std::vector<int> collection = {3, 6, 12, 6, 9, 12};

// Tous les nombres sont-ils divisibles par 3 ?
bool divby3 = std::all_of(begin(collection), end(collection), [](int x) {
    return x % 3 == 0;
});
// divby3 est vrai, car tous les nombres sont divisibles par 3

// Au moins un nombre est-il divisible par 2 ?
bool divby2 = std::any_of(begin(collection), end(collection), [](int x) {
    return x % 2 == 0;
});
// divby2 est vrai car 6, 12 sont divisibles par 2

// Aucun nombre n'est-il divisible par 6 ?
bool divby6 = std::none_of(begin(collection), end(collection), [](int x) {
    return x % 6 == 0;
});
// divby6 est faux car 6, 12 sont divisibles par 6
```

Remarquez comment, dans l'exemple, la _propriété spécifique_ est passée sous forme de fonction lambda.

Ainsi, `**all_of, any_of, none_of**` recherchent une propriété spécifique dans votre _collection_. Ces fonctions sont assez explicites quant à leur rôle. Avec l'introduction des **lambdas** en C++11, elles sont très pratiques à utiliser.

2. `**for_each**`

J'ai toujours été si habitué à utiliser la vieille boucle `**for**` que cette petite chose n'a jamais attiré mon attention. En gros, `**for_each**` applique une fonction à une plage d'un conteneur.

```c++
std::vector<int> collection = {2,4,4,1,1,3,9};

// remarquez que nous passons x par référence !
std::for_each(begin(collection), end(collection), [] (int &x) {
    x += 26;
});
```

Si vous êtes un développeur JavaScript, le code ci-dessus devrait vous rappeler quelque chose.

3. `**count count_if**`

Assez similaires aux fonctions décrites au début, `**count**` et `**count_if**` recherchent des propriétés spécifiques dans votre collection de données donnée.

```
std::vector<int> collection={1, 9, 9, 4, 2, 6};

// Combien de 9 y a-t-il dans la collection ?
int nines = std::count(begin(collection), end(collection), 9);
// Combien d'éléments de la collection sont pairs ?
int evens = std::count_if(begin(collection), end(collection), [](int x) {
    return x % 2 == 0;
});
// nines est égal à 2, evens est égal à 3
```

Et en résultat, vous recevez le **compte** qui correspond à votre valeur donnée, ou qui a la propriété donnée que vous fournissez sous forme de fonction lambda.

4. `**find_if**`

Disons que vous voulez trouver le premier élément de votre collection satisfaisant une propriété particulière. Vous pouvez utiliser `**find_if**`.

```c++
std::vector<int> collection = {1, 2, 0, 5, 0, 3, 4};

// itr contient l'itérateur vers le premier élément suivant la propriété spécifique
auto itr = std::find_if(begin(collection), end(collection), [](int x) {
    return x % 2==0; // la propriété
});
```

Rappelez-vous, comme montré dans l'exemple ci-dessus, vous obtiendrez l'**itérateur** vers le **premier élément** qui correspond à votre propriété donnée. Alors, que faire si vous voulez trouver tous les éléments qui correspondent à la propriété en utilisant `**find_if**` ?

![Image](https://s3.amazonaws.com/cdn-media-1.freecodecamp.org/ghost/2019/05/0_C0IjBIkmmXBEqCEk.jpeg)
_Une œuvre d'art abstraite à regarder si vous vous ennuyez. ([Unsplash](https://unsplash.com/@steve_j?utm_source=medium&amp;utm_medium=referral" rel="photo-creator noopener noopener noopener">Steve Johnson</a> sur <a href="https://unsplash.com/?utm_source=medium&amp;utm_medium=referral" rel="photo-source noopener noopener noopener))_

5. `**generate**`

Cette fonction modifie essentiellement les valeurs de votre collection, ou une plage de celle-ci, en fonction du **générateur** que vous fournissez. Le générateur est une fonction de la forme   
`**T f();**` où `**T**` est un type compatible avec notre collection.

```
std::vector<int> collection={1, 2, 0, 5, 0, 3, 4};

int counter=0;

// remarquez que nous capturons counter par référence
std::generate(begin(collection), end(collection), [&]() {
    return counter++;
});

// collection est remplacée par des valeurs commençant à 0
// collection modifiée = {0,1,2,3,4,5,6}
```

Dans l'exemple ci-dessus, remarquez que nous modifions effectivement notre collection _en place_. Et le générateur ici est la fonction lambda que nous avons fournie.

6. `**shuffle**`

À partir de la norme C++17, `**random_shuffle**` a été supprimé. Maintenant, nous préférons `**shuffle**` qui est plus efficace, étant donné qu'il tire parti de l'en-tête `**random**`.

```c++
std::vector<int> collection = {1, 2, 13, 5, 12, 3, 4};

std::random_device rd;
std::mt19937 rand_gen(rd());
std::shuffle(begin(collection), end(collection), rand_gen);
```

Notez que nous utilisons [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister), un générateur de nombres pseudo-aléatoires introduit dans C++11.

Les générateurs de nombres aléatoires sont devenus bien plus matures en C++ avec l'introduction de la bibliothèque `**random**` et l'inclusion de meilleures méthodes.

7. `**nth_element**`

Cette fonction est assez utile, étant donné qu'elle a une complexité intéressante.

Disons que vous voulez connaître le _n-ième_ élément de votre collection si elle était triée, mais que vous ne voulez pas trier la collection pour faire une opération en **_O(n log(n))_**.

Que feriez-vous ?

Alors `**nth_element**` est votre ami. Il trouve l'élément souhaité en **_O(n)_**_._

```c++
std::vector<int> collection = {1, 2, 13, 5, 12, 3, 4};

auto median_pos = collection.begin() + collection.size() / 2;
std::nth_element(begin(collection), median_pos, end(collection));

// notez que le vecteur original sera modifié en raison des opérations
// effectuées par nth_element
```

Intéressamment, `**nth_element**` peut ou non trier votre collection. Il fera simplement ce qu'il faut pour trouver le n-ième élément. Voici une discussion intéressante sur [StackOverflow](https://stackoverflow.com/questions/10352442/whats-the-practical-difference-between-stdnth-element-and-stdsort).

Et aussi, vous pouvez toujours ajouter votre propre fonction de comparaison (comme nous avons ajouté des lambdas dans les exemples précédents) pour le rendre plus efficace.

8. `**equal_range**`

Alors, disons que vous avez une collection triée d'entiers. Vous voulez trouver la plage dans laquelle tous les éléments ont une valeur spécifique. Par exemple :

```c++
// collection triée
std::vector<int> collection={1, 2, 5, 5, 5, 6, 9, 12};

// nous cherchons une plage où tous les éléments sont égaux à 5
auto range = std::equal_range(begin(collection), end(collection), 5);

// la plage requise est imprimée comme ceci
std::cout << (range.first - begin(collection)) << " " <<
          (range.second - begin(collection)) << std::endl;
```

Dans ce code, nous cherchons une **plage** dans le `**vector**` qui contient tous les `**5**`. La réponse est `**(2~4)**`.

Bien sûr, nous pouvons utiliser cette fonction pour notre propre propriété personnalisée. Vous devez vous assurer que la propriété que vous avez alignée avec l'ordre des données. Voir [cet article pour référence](https://en.cppreference.com/w/cpp/algorithm/equal_range).

Enfin, `**lower_bound**` et `**upper_bound**` peuvent tous deux vous aider à atteindre le même résultat que celui obtenu avec `**equal_range**`.

9. `**merge inplace_merge**`

Imaginez que vous avez deux collections triées (quelle chose amusante à imaginer, n'est-ce pas ?), vous voulez les fusionner, et vous voulez aussi que la collection fusionnée reste triée. Comment feriez-vous cela ?

Vous pouvez simplement ajouter la deuxième collection à la première et retrier le résultat, ce qui ajoute un facteur supplémentaire **O(log(n))**. Au lieu de cela, nous pouvons simplement utiliser `**merge**`.

```c++
std::vector<int> c1 = {1, 2, 5, 5, 5, 6, 9, 12};
std::vector<int> c2 = {2, 4, 4, 5, 7, 15};

std::vector<int> result; // contient les éléments fusionnés
std::merge(begin(c1), end(c1), begin(c2), end(c2), std::back_inserter(result));

// result = {1, 2, 2, 4, 4, 5, 5, 5, 5, 6, 7, 9, 12, 15}
```

D'un autre côté, vous vous souvenez lorsque nous implémentons le _tri fusion_, nous devons fusionner les deux côtés de notre tableau ? `**inplace_merge**` peut être utilisé commodément pour cela.

Regardez ce petit _tri fusion_ basé sur l'exemple donné dans [cppreference](https://en.cppreference.com/w/cpp/algorithm/inplace_merge) :

```c++
void merge_sort(auto l, auto r)
{
    if(r - l > 1)
    {
        auto mid = l+(r-l)/2;
        merge_sort(l, mid);
        merge_sort(mid, r);
        std::inplace_merge(l, mid, r);
    }
}

std::vector<int> collection = {2, 4, 4, 1, 1, 3, 9};
merge_sort(begin(collection), end(collection));
```

N'est-ce pas génial ?

![Image](https://s3.amazonaws.com/cdn-media-1.freecodecamp.org/ghost/2019/05/0_zgexhkawrSJNYfNM.jpeg)
_En parlant de cool, voici un gars cool. 😎 ([Unsplash](https://unsplash.com/@davealmine?utm_source=medium&amp;utm_medium=referral" rel="photo-creator noopener noopener noopener noopener">Dawid Zawiła</a> sur <a href="https://unsplash.com/?utm_source=medium&amp;utm_medium=referral" rel="photo-source noopener noopener noopener noopener))_

10. `**minmax minmax_element**`

`**minmax**` retourne le minimum et le maximum des deux valeurs données, ou de la liste donnée. Il retourne une paire et peut également fournir la fonctionnalité de votre propre méthode de comparaison. `**minmax_element**` fait de même pour votre conteneur.

```c++
int a = 9, b = 12;

// out.first contient l'élément minimum, out.second est le maximum
auto out = std::minmax(a, b);

std::vector<int> collection = {6, 5, 3, 2, 1, 4, 6, 7};
auto result = std::minmax_element(begin(collection), end(collection));

// vous pouvez également ajouter une fonction de comparaison comme troisième argument
// (result.first - collection.begin()) est l'index de l'élément minimum
// (result.second - collection.begin()) est l'index de l'élément maximum
```

11. `**accumulate partial_sum**`

`**accumulate**` fait ce qu'il dit, il _accumule_ les valeurs de votre collection dans la plage donnée, en utilisant la valeur initiale et une fonction d'opération binaire. Voyez par vous-même :

```c++
std::vector<int> collection = {6, 5, 3, 2, 1, 4, 6, 7};

// Notez que nous fournissons 0 comme valeur initiale, comme il se doit.
// std::plus<int>() indique que la fonction doit faire des sommes
int sum = std::accumulate(begin(collection), end(collection), 0, std::plus<int>());

// Que se passerait-il si la valeur initiale était 0 au lieu de 1 dans cet appel ?
int prod = std::accumulate(begin(collection), end(collection), 1, std::multiplies<int>());

// Vous pouvez également utiliser votre propre opération binaire personnalisée.
int custom = std::accumulate(begin(collection), end(collection), 0, [](int x, int y) {
    return x+y;
});
```

Alors, comment la valeur de `**custom**` est-elle calculée ?

Au début, accumulate prend la valeur initiale (0) pour l'argument `**x**`, la première valeur de la collection (6) pour l'argument `**y**`, effectue l'opération, puis l'assigne à la valeur accumulée. Dans le deuxième appel, il passe la valeur accumulée à `**x**` et l'élément suivant de la collection à `**y**`, et ainsi de suite.

`**partial_sum**` fait des choses très similaires à accumulate, mais il conserve également le résultat des premiers `**n**` termes dans un conteneur de destination.

```c++
std::vector<int> collection = {6, 5, 3, 2, 1, 4, 6, 7};
std::vector<int> sums, mults;

// contient la somme partielle de la collection dans le résultat
std::partial_sum(begin(collection), end(collection), std::back_inserter(sums));

// contient le produit partiel
std::partial_sum(begin(collection), end(collection), std::back_inserter(mults), std::multiplies<int>());
```

Et bien sûr, comme vous vous y attendez, vous pouvez utiliser votre propre opération personnalisée.

12. `**adjacent_difference**`

Vous voulez trouver les différences adjacentes dans vos valeurs, vous pouvez simplement utiliser cette fonction.

```c++
std::vector<int> collection = {6, 5, 3, 2, 1, 4, 6, 7};
std::vector<int> diffs;
std::adjacent_difference(begin(collection), end(collection), std::back_inserter(diffs));
// Le premier élément de diffs sera le même que le premier élément de la collection
```

Assez simple, n'est-ce pas ?

Mais il peut faire bien plus. Regardez ceci :

```c++
std::vector<int> fibs(10, 1);
std::adjacent_difference(begin(fibs), end(fibs) - 1, begin(fibs) + 1, std::plus<>{});
```

Que font ces deux lignes ? Elles trouvent les 10 premiers nombres de Fibonacci ! Voyez-vous comment ? 😉

---

C'est tout pour aujourd'hui. Merci d'avoir lu ! J'espère que vous avez appris quelque chose de nouveau.

Je serais ravi de vous apporter de nouvelles choses à l'avenir.

Santé !