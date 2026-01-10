---
title: Utilisation de Java Arrays.sort() pour toute liste d'objets
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-07T16:39:21.000Z'
originalURL: https://freecodecamp.org/news/utilizing-javas-arrays-sort-for-any-list-of-objects-e3e2db61d70b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Aap5LkZQvXhukGZicn8_vA.jpeg
tags:
- name: Java
  slug: java
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Utilisation de Java Arrays.sort() pour toute liste d'objets
seo_desc: 'By Ethan Arrowood

  Sorting can be tricky, especially when your list is not of a primitive Java numeric
  type (Byte, Integer, Short, Long, Double, Float). Now, all situations will vary
  so this method might not be the best case. However, I’ve found it in...'
---

Par Ethan Arrowood

Le tri peut être délicat, surtout lorsque votre liste n'est pas d'un type numérique primitif Java (Byte, Integer, Short, Long, Double, Float). Maintenant, toutes les situations varient, donc cette méthode pourrait ne pas être le meilleur cas. Cependant, je l'ai trouvée incroyablement utile pour des défis de codage simples et des travaux pratiques universitaires.

Pour commencer, choisissez votre liste. Pour cet exemple, j'utiliserai une liste d'`Edges` (arêtes) d'une structure de données `Graph` (graphe) simple :

```
// Classe Edge très simple
public class Edge {
    public Vertex src;
    public Vertex dst;
    public double cost;

    // crée une arête entre deux sommets
    Edge(Vertex s, Vertex d, double c) {
        src = s;
        dst = d;
        cost = c;
    }
}
```

```
// Liste des arêtes
Edge[] edges = graph.getEdges();
```

Ensuite, définissez l'implémentation de l'interface `java.util.Comparator` :

```
class SortByCost implements Comparator<Edge> {
    public int compare(Edge a, Edge b) {
        if ( a.cost < b.cost ) return -1;
        else if ( a.cost == b.cost ) return 0;
        else return 1;
    }
}
```

Dans cet exemple, nous allons trier les `edges` par leur coût, ou distance du sommet `src` (source) au sommet `dst` (destination).

Enfin, utilisez la méthode standard `java.util.Arrays.sort()` :

```
Arrays.sort(edges, new SortByCost())
```

Et voilà, la liste des `Edges` est maintenant triée par ordre ascendant (du plus petit au plus grand).

Si vous avez des questions, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/ArrowoodTech)

Vous pouvez également me trouver sur [GitHub](https://github.com/ethan-arrowood) ou sur mon site personnel [website](https://ethanarrowood.com)

~ Bon codage

— Ethan Arrowood