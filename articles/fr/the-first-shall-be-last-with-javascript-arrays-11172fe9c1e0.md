---
title: Le premier sera le dernier avec les tableaux JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-28T15:44:06.000Z'
originalURL: https://freecodecamp.org/news/the-first-shall-be-last-with-javascript-arrays-11172fe9c1e0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qpeU4geKupip-i6jxgxF9Q.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Le premier sera le dernier avec les tableaux JavaScript
seo_desc: 'By Thomas Barrasso


  So the last shall be [0], and the first [length — 1].

  – Adapted from Matthew 20:16


  I’ll skip the Malthusian Catastrophe and get to it: arrays are one of the simplest
  and most important data structures. While terminal elements (fi...'
---

Par Thomas Barrasso

> Ainsi, le dernier sera `[0]`, et le premier [length  1].

>  Adapté de [Matthieu 20:16](https://www.biblegateway.com/passage/?search=Matthew+20%3A16&version=KJV)

Je vais passer la Catastrophe Malthusienne et en venir au fait : les tableaux sont l'une des structures de données les plus simples et les plus importantes. Bien que les éléments terminaux (premier et dernier) soient fréquemment accessibles, JavaScript ne fournit aucune propriété ou méthode pratique pour le faire et l'utilisation des indices peut être redondante et sujette à des effets secondaires et à des [erreurs de décalage](https://en.wikipedia.org/wiki/Off-by-one_error).

Une proposition moins connue, [récente de JavaScript TC39](https://github.com/keithamus/proposal-array-last), offre un réconfort sous la forme de deux propriétés "nouvelles" : `Array.lastItem` & `Array.lastIndex`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*76m-CxmcYIqWbOpln0Za8g.png)
_[Jeff Atwood @codinghorror](https://twitter.com/codinghorror/status/506010907021828096?lang=en" rel="noopener" target="_blank" title=")_

### **Tableaux JavaScript**

Dans de nombreux langages de programmation, y compris JavaScript, les tableaux sont indexés à partir de zéro. Les éléments terminauxpremier et derniersont accessibles via les indices `[0]` et `[length  1]`, respectivement. Nous devons ce plaisir à un [précédent établi par C](https://medium.com/@albertkoz/why-does-array-start-with-index-0-65ffc07cbce8), où un index représente un décalage par rapport à la tête d'un tableau. Cela fait de zéro le premier index parce qu'il _est_ la tête du tableau. De plus, Dijkstra a proclamé "[zéro comme le nombre le plus naturel](https://www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html)". Qu'il en soit ainsi écrit. Qu'il en soit ainsi fait.

Je soupçonne que si vous faisiez la moyenne des accès par index, vous trouveriez que les éléments terminaux sont référencés le plus souvent. Après tout, les tableaux sont couramment utilisés pour stocker une collection triée et cela place les éléments superlatifs (les plus hauts, les plus bas, les plus anciens, les plus récents, etc.) aux extrémités.

Contrairement à d'autres langages de script (comme [PHP](https://secure.php.net/manual/en/function.end.php) ou [Elixir](https://hexdocs.pm/elixir/List.html#last/1)), JavaScript ne fournit pas d'accès pratique aux éléments terminaux des tableaux. Considérez un exemple trivial d'échange des derniers éléments dans deux tableaux :

```
let faces = ["?", "?", "?", "?", "?"];let animals = ["?", "?", "?", "?", "?"];  
```

```
let lastAnimal = animals[animals.length - 1];animals[animals.length - 1] = faces[faces.length - 1];faces[faces.length - 1] = lastAnimal;
```

La logique d'échange nécessite 2 tableaux référencés 8 fois en 3 lignes ! Dans du code réel, cela peut rapidement devenir très répétitif et difficile à analyser pour un humain (bien que ce soit parfaitement lisible pour une machine).

De plus, en utilisant uniquement des indices, vous ne pouvez pas définir un tableau et obtenir le dernier élément dans la même expression. Cela peut ne pas sembler important, mais considérons un autre exemple où la fonction, `getLogins()`, effectue un appel d'API asynchrone et retourne un tableau trié. En supposant que nous voulons l'événement de connexion le plus récent à la fin du tableau :

```
let lastLogin = async () => {  let logins = await getLogins();  return logins[logins.length - 1];};
```

Sauf si la longueur est fixe et connue à l'avance, nous _devons_ assigner le tableau à une variable locale pour accéder au dernier élément. Une façon courante de résoudre ce problème dans des langages comme [Python](http://knowledgehills.com/python/negative-indexing-slicing-stepping-comparing-lists.htm) et [Ruby](http://rubyquicktips.com/post/996814716/use-negative-array-indices) est d'utiliser des indices négatifs. Alors `[length - 1]` peut être raccourci en `[-1]`, supprimant le besoin de référence locale.

Je trouve `-1` seulement légèrement plus lisible que `length  1`, et bien qu'il soit possible d'approximer [les indices de tableau négatifs en JavaScript](https://h3manth.com/new/blog/2013/negative-array-index-in-javascript/) avec [ES6 Proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) ou `Array.slice(-1)[0]`, les deux viennent avec [des implications de performance significatives](https://jsperf.com/last-array-element2/14) pour ce qui devrait autrement constituer un accès aléatoire simple.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Tv90DqFJ1xOyUhbtmm4UXw.png)

#### **Underscore & Lodash**

L'un des principes les plus connus en développement logiciel est Ne vous répétez pas (DRY). Puisque l'accès aux éléments terminaux est si courant, pourquoi ne pas écrire une fonction d'assistance pour le faire ? Heureusement, de nombreuses bibliothèques comme [Underscore](https://underscorejs.org/) et [Lodash](https://lodash.com/) fournissent déjà des utilitaires pour `_.first` & `_.last`.

Cela offre une grande amélioration dans l'exemple `lastLogin()` ci-dessus :

```
let lastLogin = async () => _.last(await getLogins());
```

Mais lorsqu'il s'agit de l'exemple d'échange des derniers éléments, l'amélioration est moins significative :

```
let faces = ["?", "?", "?", "?", "?"];let animals = ["?", "?", "?", "?", "?"];  
```

```
let lastAnimal = _.last(animals);animals[animals.length - 1] = _.last(faces);faces[faces.length - 1] = lastAnimal;
```

Ces fonctions utilitaires ont supprimé 2 des 8 références, mais nous avons maintenant introduit une dépendance externe qui, curieusement, n'inclut pas de fonction pour _définir_ les éléments terminaux.

Très probablement, une telle fonction est délibérément exclue parce que son API serait confuse et difficile à lire. Les premières versions de Lodash fournissaient une méthode `[_.last(array, n)](https://github.com/lodash/lodash/issues/946)` où _n_ était le nombre d'éléments à partir de la fin, mais elle a finalement été supprimée au profit de `[_.take](https://lodash.com/docs#take)(array, n)`.

En supposant que `nums` est un tableau de nombres, quel serait le comportement attendu de `_.last(nums, n)` ? Il pourrait retourner les deux derniers éléments comme `_.take`, ou il pourrait définir la valeur du dernier élément égale à _n_.

Si nous devions écrire une fonction pour définir le dernier élément dans un tableau, il n'y a que quelques approches à considérer en utilisant des fonctions pures, le chaînage de méthodes, ou en utilisant le prototype :

```
let nums = ['d', 'e', 'v', 'e', 'l']; // définir premier = dernier
```

```
_.first(faces, _.last(faces));        // Style Lodash
```

```
$(faces).first($(faces).last());      // Style jQuery
```

```
faces.first(faces.last());            // prototype
```

Je ne trouve aucune de ces approches beaucoup plus améliorée. En fait, quelque chose d'important est perdu ici. Chacune effectue une assignation, mais aucune n'utilise l'opérateur d'assignation (`=`). Cela pourrait être rendu plus apparent avec des conventions de nommage comme `getLast` et `setFirst`, mais cela devient rapidement trop verbeux. Sans parler du [cinquième cercle de l'enfer](https://blog.toggl.com/seven-levels-developer-hell/) qui est rempli de programmeurs forcés de naviguer dans du code hérité "auto-documenté" où la seule façon d'accéder ou de modifier des données est par le biais de getters et de setters.

D'une manière ou d'une autre, il semble que nous soyons coincés avec `[0]` & `[length  1]`

Ou pas ? ?

#### **La Proposition**

Comme mentionné, une proposition de Candidat Technique ECMAScript (TC39) tente de résoudre ce problème en définissant deux nouvelles propriétés sur l'objet `Array` : `lastItem` & `lastIndex`. Cette proposition est [déjà supportée](https://kangax.github.io/compat-table/esnext/) dans [core-js 3](https://github.com/zloirock/core-js) et utilisable aujourd'hui dans Babel 7 & TypeScript. Même si vous n'utilisez pas de transpileur, cette proposition inclut un [polyfill](https://github.com/keithamus/proposal-array-last#polyfill).

Personnellement, je ne trouve pas beaucoup de valeur dans `lastIndex` et je préfère la nomenclature plus courte de Ruby pour `[first](https://stackoverflow.com/questions/18212240/ruby-convention-for-accessing-first-last-element-in-array)` [et `last`](https://stackoverflow.com/questions/18212240/ruby-convention-for-accessing-first-last-element-in-array), bien que cela ait été écarté en raison de [problèmes potentiels de compatibilité web](https://github.com/keithamus/proposal-array-last/issues/4). Je suis également surpris que cette proposition ne suggère pas une propriété `firstItem` pour la cohérence et la symétrie.

En attendant, je peux offrir une approche sans dépendance, à la Ruby, en ES6 :

#### **Premier & Dernier**

Nous avons maintenant deux nouvelles propriétés de tableau`first` & `last`et une solution qui :

 Utilise l'opérateur d'assignation

 Ne clone pas le tableau

 Peut définir un tableau et obtenir un élément terminal en une expression

 Est lisible par l'homme

 Fournit une interface pour obtenir & définir

Nous pouvons réécrire `lastLogin()` à nouveau en une seule ligne :

```
let lastLogin = async () => (await getLogins()).last;
```

Mais la vraie victoire vient lorsque nous échangeons les derniers éléments dans deux tableaux avec la moitié du nombre de références :

```
let faces = ["?", "?", "?", "?", "?"];let animals = ["?", "?", "?", "?", "?"];  
```

```
let lastAnimal = animals.last;animals.last = faces.last;faces.last = lastAnimal;
```

Tout est parfait et nous avons résolu l'un des problèmes les plus difficiles de l'informatique. Il n'y a pas de pactes maléfiques cachés dans cette approche

#### **Paranoïa du Prototype**

> Certes, il n'y a personne [programmeur] sur terre assez juste pour faire le bien sans jamais pécher.
 Adapté de [Ecclésiaste 7:20](https://www.biblegateway.com/passage/?search=Ecclesiastes+7%3A20&version=NRSVA)

Beaucoup considèrent [l'extension du prototype d'un objet natif comme un anti-modèle](https://we-are.bookmyshow.com/prototype-pattern-in-js-5c1f44440081) et un crime passible de 100 ans de programmation en Java. Avant l'introduction de la propriété `[enumerable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Enumerability_and_ownership_of_properties)`, [l'extension de `Object.prototype`](https://javascriptweblog.wordpress.com/2011/12/05/extending-javascript-natives/) pouvait changer le comportement des boucles `for in`. Cela pouvait également conduire à des conflits entre diverses bibliothèques, frameworks et dépendances tierces.

Peut-être que le problème le plus insidieux est que, sans outils de compilation, une simple erreur d'orthographe pourrait [créer involontairement un tableau associatif](https://nemisj.com/why-getterssetters-is-a-bad-idea-in-javascript/).

```
let faces = ["?", "?", "?", "?", "?"];let ln = faces.length  
```

```
faces.lst = "?"; // (5) ["?", "?", "?", "?", "?", lst: "?"]  
```

```
faces.lst("?");  // Uncaught TypeError: faces.lst is not a function 
```

```
faces[ln] = "?"; // (6) ["?", "?", "?", "?", "?", "?"]  
```

Cette préoccupation n'est pas unique à notre approche, elle s'applique à tous les prototypes d'objets natifs (y compris les tableaux). Pourtant, cela offre une sécurité sous une forme différente. Les tableaux en JavaScript ne sont pas fixes en longueur et, par conséquent, il n'y a pas de `IndexOutOfBoundsExceptions`. L'utilisation de `Array.last` garantit que nous n'essayons pas accidentellement d'accéder à `[length]` et d'entrer involontairement dans le territoire `undefined`.

Quelle que soit l'approche que vous adoptez, il y a des pièges. Une fois de plus, le logiciel s'avère être un [art de faire des compromis](https://pragprog.com/articles/the-art-of-tradeoffs).

En continuant avec la référence biblique superflue, en supposant que nous ne croyons pas que l'extension de `Array.prototype` est un péché éternel, ou que nous sommes prêts à croquer le fruit défendu, nous pouvons utiliser cette syntaxe concise et lisible dès aujourd'hui !

### **Derniers Mots**

> Les programmes doivent être écrits pour que les gens les lisent, et seulement accessoirement pour que les machines les exécutent.  [Harold Abelson](https://www.goodreads.com/book/show/43713.Structure_and_Interpretation_of_Computer_Programs?from_choice=false&from_home_module=false)

Dans les langages de script comme JavaScript, je préfère le code qui est fonctionnel, concis et lisible. En ce qui concerne l'accès aux éléments terminaux des tableaux, je trouve que la propriété `Array.last` est la plus élégante. Dans une application front-end de production, je pourrais favoriser Lodash pour minimiser les conflits et les préoccupations de compatibilité multi-navigateurs. Mais dans les services back-end Node où je contrôle l'environnement, je préfère ces propriétés personnalisées.

Je ne suis certainement [pas le premier](https://esdiscuss.org/topic/array-prototype-last), ni ne serai le dernier, à apprécier la valeur (ou à mettre en garde contre les implications) de propriétés comme `Array.lastItem`, qui, espérons-le, arrivera bientôt dans une version d'ECMAScript près de chez vous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z63EqxzV68XKUa3b81d8wg.png)

Suivez-moi sur [LinkedIn](https://www.linkedin.com/in/tombarrasso)  [GitHub](https://github.com/Tombarr)  [Medium](https://medium.com/@tbarrasso)