---
title: Algorithme de Remplissage par Diffusion Expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-06T00:22:00.000Z'
originalURL: https://freecodecamp.org/news/flood-fill-algorithm-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e26740569d1a4ca3b9a.jpg
tags:
- name: algorithms
  slug: algorithms
seo_title: Algorithme de Remplissage par Diffusion Expliqué
seo_desc: 'Flood fill is an algorithm mainly used to determine a bounded area connected
  to a given node in a multi-dimensional array. It is a close resemblance to the bucket
  tool in paint programs.

  The most approached implementation of the algorithm is a stack-...'
---

Le remplissage par diffusion est un algorithme principalement utilisé pour déterminer une zone délimitée connectée à un nœud donné dans un tableau multidimensionnel. Il ressemble étroitement à l'outil de pot de peinture dans les programmes de dessin.

L'implémentation la plus abordée de l'algorithme est une fonction récursive basée sur une pile, et c'est ce dont nous allons parler ensuite.

### **Comment ça marche ?**

Le problème est assez simple et suit généralement ces étapes :

1. Prendre la position du point de départ.
2. Décider si vous voulez aller dans 4 directions (**N, S, O, E**) ou 8 directions (**N, S, O, E, NO, NE, SO, SE**).
3. Choisir une couleur de remplacement et une couleur cible.
4. Se déplacer dans ces directions.
5. Si la case sur laquelle vous atterrissez est une cible, remplacez-la par la couleur choisie.
6. Répéter les étapes 4 et 5 jusqu'à ce que vous ayez tout exploré dans les limites.

Prenons le tableau suivant comme exemple :

![alt text](https://github.com/firealex2/Codingame/blob/master/small%208%20grid%20paintefffd.png)

Le carré rouge est le point de départ et les carrés gris sont les soi-disant murs.

Pour plus de détails, voici un morceau de code décrivant la fonction :

```c++
int mur = -1;

void remplissage_diffusion(int pos_x, int pos_y, int couleur_cible, int couleur)
{
  
   if(a[pos_x][pos_y] == mur || a[pos_x][pos_y] == couleur) // s'il n'y a pas de mur ou si je n'y suis pas encore allé
      return;                                              // retourne déjà
   
   if(a[pos_x][pos_y] != couleur_cible) // si ce n'est pas la couleur, retourne
      return;
   
   a[pos_x][pos_y] = couleur; // marque le point pour que je sache si je suis passé par là. 
   
   remplissage_diffusion(pos_x + 1, pos_y, couleur);  // puis je peux aller au sud
   remplissage_diffusion(pos_x - 1, pos_y, couleur);  // ou au nord
   remplissage_diffusion(pos_x, pos_y + 1, couleur);  // ou à l'est
   remplissage_diffusion(pos_x, pos_y - 1, couleur);  // ou à l'ouest
   
   return;

}
```

Comme vu ci-dessus, mon point de départ est (4,4). Après avoir appelé la fonction pour les coordonnées de départ **x = 4** et **y = 4**, je peux commencer à vérifier s'il n'y a pas de mur ou de couleur sur place. Si c'est valide, je marque l'endroit avec une **"couleur"** et commence à vérifier les autres cases adjacentes.

En allant vers le sud, nous arriverons au point (5,4) et la fonction s'exécute à nouveau.

### **Problème d'exercice**

J'ai toujours considéré que résoudre un (ou plusieurs) problème(s) en utilisant un algorithme nouvellement appris est la meilleure façon de comprendre pleinement le concept.

Donc en voici un :

**Énoncé :**

Dans un tableau bidimensionnel, on vous donne n nombre d'**"îles"**. Essayez de trouver la plus grande surface d'une île et le numéro d'île correspondant. 0 marque l'eau et tout autre x entre 1 et n marque une case de la surface correspondant à l'île x.

**Entrée**

* **n** - le nombre d'îles.
* **l,c** - les dimensions de la matrice.
* les **l** lignes suivantes, **c** nombres donnant la **l**ième ligne de la matrice.

**Sortie**

* **i** - le numéro de l'île avec la plus grande surface.
* **A** - la surface de la **i**ème île.

**Ex :**

Vous avez l'entrée suivante :

```c++
2 4 4
0 0 0 1
0 0 1 1
0 0 0 2
2 2 2 2
```

Pour laquelle vous obtiendrez l'île n° 2 comme la plus grande île avec une surface de 5 cases.

### **Indices**

Le problème est assez facile, mais voici quelques indices :

```text
1. Utilisez l'algorithme de remplissage par diffusion chaque fois que vous rencontrez une nouvelle île.
2. Contrairement à l'exemple de code, vous devriez parcourir la surface de l'île et non l'océan (cases 0).
```