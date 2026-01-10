---
title: 'Recherche en Profondeur : un Guide de Parcours de Graphe DFS avec 6 Exemples
  Leetcode'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-21T15:39:20.000Z'
originalURL: https://freecodecamp.org/news/dfs-for-your-next-tech-giant-interview
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/graph_theory_design_web_forms_08.png
tags:
- name: algorithms
  slug: algorithms
seo_title: 'Recherche en Profondeur : un Guide de Parcours de Graphe DFS avec 6 Exemples
  Leetcode'
seo_desc: "By Anamika Ahmed\nHave you ever solved a real-life maze? The approach that\
  \ most of us take while solving a maze is that we follow a path until we reach a\
  \ dead end, and then backtrack and retrace our steps to find another possible path.\
  \ \nThis is exactl..."
---

Par Anamika Ahmed

Avez-vous déjà résolu un labyrinthe dans la vie réelle ? L'approche que la plupart d'entre nous adoptons pour résoudre un labyrinthe est de suivre un chemin jusqu'à atteindre une impasse, puis de revenir en arrière et de retracer nos pas pour trouver un autre chemin possible. 

C'est exactement l'analogie de la Recherche en Profondeur (DFS). Il s'agit d'un algorithme populaire de parcours de graphe qui commence au nœud racine et parcourt aussi loin que possible une branche donnée, puis revient en arrière jusqu'à ce qu'il trouve un autre chemin inexploré à explorer. Cette approche est poursuivie jusqu'à ce que tous les nœuds du graphe aient été visités.

Dans le tutoriel d'aujourd'hui, nous allons découvrir un modèle DFS qui sera utilisé pour résoudre certaines des questions importantes sur les arbres et les graphes pour votre prochain entretien avec un Géant de la Tech ! Nous allons résoudre certains problèmes Leetcode de niveau Moyen et Difficile en utilisant la même technique commune.

Alors, commençons, d'accord ?

## Implémentation

Puisque DFS a une nature récursive, il peut être implémenté en utilisant une pile.

Sortilège Magique DFS :

1. Empiler un nœud dans la pile
2. Dépiler le nœud
3. Récupérer les voisins non visités du nœud retiré, les empiler
4. Répéter les étapes 1, 2 et 3 tant que la pile n'est pas vide

## Parcours de Graphes

En général, il existe 3 parcours DFS de base pour les arbres binaires :

1. **Pré-ordre** : Racine, Gauche, Droite **OU** Racine, Droite, Gauche
2. **Post-ordre** : Gauche, Droite, Racine **OU** Droite, Gauche, Racine
3. **In-ordre** : Gauche, Racine, Droite **OU** Droite, Racine, Gauche

### [144. Parcours Pré-ordre d'un Arbre Binaire (Difficulté : Moyen)](https://leetcode.com/problems/binary-tree-preorder-traversal/)

Pour résoudre cette question, tout ce que nous devons faire est de rappeler simplement notre sortilège magique. Comprenons bien la simulation puisque c'est le **modèle de base** que nous utiliserons pour résoudre le reste des problèmes.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-138.png)

Tout d'abord, nous empilons le nœud racine dans la pile. Tant que la pile n'est pas vide, nous le dépilons et empilons ses enfants droit et gauche dans la pile.

Lorsque nous dépilons le nœud racine, nous le plaçons immédiatement dans notre liste de résultats. Ainsi, le premier élément de la liste de résultats est la racine (d'où le nom, Pré-ordre).   
  
L'élément suivant à être dépilé de la pile sera l'élément supérieur de la pile actuellement : l'enfant gauche du nœud racine. Le processus se poursuit de manière similaire jusqu'à ce que le graphe entier ait été parcouru et que toutes les valeurs des nœuds de l'arbre binaire entrent dans la liste résultante.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Sample-2020-04-20_4.jpg)

### [145. Parcours Post-ordre d'un Arbre Binaire (Difficulté : Difficile)](https://leetcode.com/problems/binary-tree-postorder-traversal/)

  
Le parcours pré-ordre est **racine-gauche-droite**, et le post-ordre est **droite-gauche-racine**. Cela signifie que le parcours post-ordre est exactement l'inverse du parcours pré-ordre. 

Donc, une solution qui pourrait venir à l'esprit est simplement d'inverser le tableau résultant du parcours pré-ordre. Mais réfléchissez-y – cela coûterait O(n) en complexité temporelle pour l'inverser.

Une solution plus intelligente est de copier et coller le code exact du parcours pré-ordre, mais de placer le résultat en haut de la liste chaînée (index 0) à chaque itération. Il faut un temps constant pour ajouter un élément à la tête d'une liste chaînée. Cool, non ?

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-143.png)

### [94. Parcours In-ordre d'un Arbre Binaire (Difficulté : Moyen)](https://leetcode.com/problems/binary-tree-inorder-traversal/)

Notre approche pour résoudre ce problème est similaire aux problèmes précédents. Mais ici, nous allons visiter tout ce qui se trouve sur le côté gauche d'un nœud, imprimer le nœud, puis visiter tout ce qui se trouve sur le côté droit du nœud.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-145.png)

### [323. Nombre de Composants Connectés dans un Graphe Non Orienté  
(Difficulté : Moyen)](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

Notre approche ici est de créer une variable appelée **ans** qui stocke le nombre de composants connectés. 

Tout d'abord, nous allons initialiser tous les sommets comme non visités. Nous allons commencer par un nœud, et tout en effectuant un DFS sur ce nœud (bien sûr, en utilisant notre sortilège magique), il marquera tous les nœuds connectés à celui-ci comme visités. La valeur de **ans** sera incrémentée de 1. 

```java

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class NumberOfConnectedComponents {
    public static void main(String[] args){
        int[][] edge = {{0,1}, {1,2},{3,4}};
        int n = 5;
        System.out.println(connectedcount(n, edge));

    }

    public static int connectedcount(int n, int[][] edges) {

        boolean[] visited = new boolean[n];
        List[] adj = new List[n];
        for(int i=0; i<adj.length; i++){
            adj[i] = new ArrayList<Integer>();
        }

        // créer la liste d'adjacence
        for(int[] e: edges){
            int from = e[0];
            int to = e[1];
            adj[from].add(to);
            adj[to].add(from);

        }
        Stack<Integer> stack = new Stack<>();
        int ans = 0; // ans = compte du nombre de fois où DFS est effectué

        // cette boucle for parcourt le graphe entier
        for(int i = 0; i < n; i++){
            // si un nœud n'est pas visité
            if(!visited[i]){
                ans++;
                // l'empiler dans la pile
                stack.push(i);

             
                while(!stack.empty()) {

                    int current = stack.peek();
                    stack.pop(); // dépiler le nœud
                    visited[current] = true; // marquer le nœud comme visité

                    List<Integer> list1 = adj[current];

        // empiler les composants connectés du nœud actuel dans la pile
                    for (int neighbours:list1) {
                        if (!visited[neighbours]) {
                            stack.push(neighbours);
                        }
                    }
                }

        }
    }
        return ans;
    }
}
```

### [200. Nombre d'Îles (Difficulté : Moyen)](https://leetcode.com/problems/number-of-islands/)

Cela relève d'une catégorie générale de problèmes où nous devons trouver le nombre de composants connectés, mais les détails sont un peu modifiés.

Instinctivement, vous pourriez penser que dès que nous trouvons un "1", nous initiions un nouveau composant. Nous faisons un DFS à partir de cette cellule dans les 4 directions (haut, bas, droite, gauche) et atteignons tous les 1 connectés à cette cellule. Tous ces 1 connectés entre eux appartiennent au même groupe, et ainsi, notre valeur de **count** est incrémentée de 1. Nous marquons ces cellules de 1 comme visitées et passons à compter d'autres composants connectés.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-149.png)

### [547. Cercles d'Amis (Difficulté : Moyen)](https://leetcode.com/problems/friend-circles/description/)

Cela suit le même concept que la recherche du nombre de composants connectés. Dans cette question, nous avons une matrice NxN mais seulement N amis au total. Les arêtes sont directement données via les cellules, donc nous devons parcourir une ligne pour obtenir les voisins pour un "ami" spécifique. 

Remarquez que ici, nous utilisons le même modèle de pile que dans nos problèmes précédents.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-148.png)

C'est tout pour aujourd'hui ! J'espère que cela vous a aidé à mieux comprendre DFS et que vous avez apprécié le tutoriel. Veuillez recommander cet article si vous pensez qu'il peut être utile pour quelqu'un d'autre !