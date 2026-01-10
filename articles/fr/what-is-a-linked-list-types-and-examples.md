---
title: Qu'est-ce qu'une liste chaînée ? Types de liste chaînée avec des exemples de
  code
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2024-03-18T15:25:17.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-linked-list-types-and-examples
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/john-petter-fagerhaug-nlT3NvhGKt8-unsplash.jpg
tags:
- name: data structures
  slug: data-structures
- name: JavaScript
  slug: javascript
- name: PHP
  slug: php
seo_title: Qu'est-ce qu'une liste chaînée ? Types de liste chaînée avec des exemples
  de code
seo_desc: "A linked list is a linear data structure consisting of a sequence of nodes.\
  \ Unlike arrays, linked lists do not require contiguous memory allocation. Instead,\
  \ each node is dynamically allocated its own memory space. \nNodes are connected\
  \ through refere..."
---

Une liste chaînée est une structure de données linéaire composée d'une séquence de nœuds. Contrairement aux tableaux, les listes chaînées ne nécessitent pas une allocation de mémoire contiguë. Au lieu de cela, chaque nœud est alloué dynamiquement dans son propre espace mémoire. 

Les nœuds sont connectés par des références, formant la structure chaînée. Un avantage des listes chaînées est que l'insertion et la suppression d'éléments au début de la liste peuvent être effectuées en temps constant, noté O(1). 

Cette efficacité provient de la capacité à manipuler directement les références sans avoir besoin de déplacer les éléments comme requis dans les tableaux. Les types de données dans une liste chaînée peuvent être n'importe quel type de données disponible pris en charge par un langage de programmation.

Dans ce tutoriel, vous apprendrez ce qui suit :

<ul>
  <li><a href="#comprendre-liste-chainee">Comprendre la liste chaînée</a></li>
  <li><a href="#types-de-liste-chainee">Types de liste chaînée</a></li>
    <li><a href="#resume-des-operations">Résumé des opérations avec leurs complexités temporelles et spatiales respectives sous forme de tableau.</a></li>
  <li><a href="#differences-entre-tableau-et-liste-chainee">Différences entre tableau et liste chaînée.</a></li>
  <li><a href="#comment-resoudre-le-probleme-de-suppression-des-doublons-dune-liste-triee">Algorithme : Résoudre la suppression des doublons d'une liste triée en PHP et JavaScript.</a></li>
</ul>

<h2 id="comprendre-liste-chainee"> Comprendre la liste chaînée </h2>

![Untitled-2024-01-31-1554](https://www.freecodecamp.org/news/content/images/2024/02/Untitled-2024-01-31-1554.png)

head => Pointe vers la première boîte de la liste  
tail => Pointe vers la dernière boîte de la liste

Pour accéder aux données de la première boîte

head.data => 6

Pour accéder aux données de la deuxième boîte, nous devons d'abord définir le pointeur (flèche) pour pointer vers la boîte. Donc, nous avons besoin de (next)  
head.next => Cela pointe vers l'élément suivant de la liste  
head.next.data => 4

Pour accéder aux données de la troisième boîte, nous devons d'abord définir le pointeur (flèche) pour pointer vers la boîte. Donc, nous avons besoin de (next.next)  
head.next.next => Cela pointe vers l'élément suivant > suivant de la liste  
head.next.next.data => 5

### Qu'est-ce qu'un nœud ?

![node](https://www.freecodecamp.org/news/content/images/2024/02/node.png)

Un nœud dans une liste chaînée est un exemple de structure auto-référentielle en programmation. Cette structure est composée d'éléments appelés nœuds, où chaque nœud contient à la fois des données et une référence à un autre nœud du même type. Cette référence, souvent appelée 'pointeur', facilite la création d'une structure en chaîne, où les nœuds sont interconnectés, formant la liste chaînée.

La nature auto-référentielle des nœuds permet un parcours et une manipulation efficaces des données au sein de la liste chaînée. La structure peut être implémentée en utilisant des classes ou des tableaux.

### Comment implémenter une liste chaînée en utilisant des classes

```php
class Node {
    public function __construct(
        public $data,
        public ?Node $next = null
    ) {}
}

// Création des nœuds

$node1 = new Node(10);
$node2 = new Node(20);
$node3 = new Node(30);

// Liaison des nœuds

$node1->next = $node2;
$node2->next = $node3;

// Parcours de la liste chaînée

$current = $node1;
while ($current != null) {
    echo $current->data . " ";
    $current = $current->next;
}
```

### Comment implémenter une liste chaînée en utilisant des tableaux

```php
// création des nœuds sous forme de tableau associatif

$node1 = ['data' => 10, 'next' => null];
$node2 = ['data' => 20, 'next' => null];
$node3 = ['data' => 30, 'next' => null];

// liaison des nœuds

$node1['next'] = &$node2;
$node2['next'] = &$node3;

// Parcours de la liste chaînée

$current = $node1;
while ($current != null) {
  echo $current["data"] . " ";
  $current = &$current["next"];
}
```

Dans les deux cas, nous créons une structure où chaque élément (nœud) contient des données et une référence (next) à un autre élément du même type. Cela crée une structure auto-référentielle. Nous relions ensuite ces éléments pour former une structure de données comme une liste chaînée. Enfin, nous parcourons la structure pour accéder et manipuler ses éléments.

Contrairement à un tableau, une liste chaînée ne fournit pas un accès en temps constant à un index particulier au sein de la liste. Cela signifie que si vous souhaitez trouver le n-ième élément de la liste, vous devrez parcourir jusqu'au n-ième élément. 

Parcourir une liste chaînée signifie itérer à travers chaque nœud de la liste jusqu'à atteindre le nœud final.

<h2 id="types-de-liste-chainee"> Types de liste chaînée</h2>

Nous discuterons des types sous les catégories Parcours, Mémoire et Complexité.

## Liste chaînée simplement

Chaque nœud contient des données et une référence au nœud suivant. 

![singly linked list](https://www.freecodecamp.org/news/content/images/2024/02/singly-2.png)

### Explication non technique

Imaginez que vous effectuez un voyage en train, où chaque train représente une partie de votre voyage, et chaque station représente un point où vous devez effectuer un changement.

* Le train A représente la première partie de votre voyage, vous emmenant de la station A à la station B. Lorsque vous arrivez à la station B, il y a un panneau indiquant de changer de train pour continuer votre voyage.
* Le train B représente la deuxième partie de votre voyage, vous emmenant de la station B à la station C. Encore une fois, lorsque vous arrivez à la station C, il n'y a pas de panneau pour un autre train car vous êtes arrivé à votre destination finale.

Dans cette analogie :

* Chaque segment de train (Train A, Train B et Train C) représente un nœud dans la liste chaînée simplement.
* La tâche de chaque train est analogue aux données stockées dans chaque nœud, représentant un segment de votre voyage.
* La transition entre les trains à chaque station est analogue au pointeur "next" dans une liste chaînée, indiquant le segment suivant de votre voyage.
* À la destination finale (Station C), il n'y a pas besoin de pointeur ou de panneau pour un autre train car c'est la fin de votre voyage.

En termes plus simples, une liste chaînée simplement est comme un voyage en train avec différents segments, où chaque train (nœud) a pour tâche de vous emmener d'une station à la suivante jusqu'à ce que vous atteigniez votre destination finale. Les transitions entre les trains sont comme des pointeurs, vous guidant à travers chaque segment de votre voyage.

### Caractéristiques de performance des listes chaînées simplement

1. **Parcours** : Le parcours n'est autorisé que dans une seule direction (c'est-à-dire uniquement vers l'avant). Vous pouvez avancer dans la liste, mais vous ne pouvez pas facilement reculer. 
2. **Efficacité mémoire** : La liste chaînée simplement est généralement plus efficace en mémoire car elle ne nécessite qu'une seule référence par nœud. 
3. **Complexité** : L'opération d'insertion et de suppression est plus facile car vous n'avez besoin de mettre à jour les références que dans une seule direction.

### Complexité temporelle et spatiale

J'ai écrit sur la complexité temporelle constante et linéaire [ici](https://www.freecodecamp.org/news/what-is-a-hash-map/), et nous allons utiliser cela pour discuter des complexités temporelles et spatiales générales pour certaines opérations courantes :

#### Parcours

Complexité temporelle O(n), où n est le nombre de nœuds dans la liste. Complexité spatiale O(1), elle ne nécessite pas d'espace supplémentaire proportionnel à la taille de l'entrée.

#### Insertion au début

Complexité temporelle O(1), elle implique la mise à jour des références au début. Complexité spatiale O(1), elle ne nécessite pas d'espace supplémentaire proportionnel à la taille de l'entrée.

#### Insertion à la fin

Complexité temporelle O(n), elle peut nécessiter de parcourir toute la liste pour atteindre la fin. Complexité spatiale O(1), elle ne nécessite pas d'espace supplémentaire proportionnel à la taille de l'entrée.

#### Suppression au début

Complexité temporelle O(1), elle implique la mise à jour des références au début. Complexité spatiale O(1), constante.

#### Suppression à la fin

Complexité temporelle O(n), elle peut nécessiter de parcourir toute la liste pour atteindre la fin. Complexité spatiale O(1), constante.

## Liste doublement chaînée

Dans une liste doublement chaînée, le nœud `head` n'a généralement pas de référence `prev` car il est le premier nœud et n'a donc pas de nœud précédent. 

Cependant, le nœud `head` a une référence `next` pointant vers le nœud suivant dans la liste. Chaque nœud contient des données et des références à la fois au nœud suivant et au nœud précédent.

![doubly-1inked-list](https://www.freecodecamp.org/news/content/images/2024/02/doubly-1.png)

### Explication non technique 

Imaginez que vous avez un livre où chaque page représente une tâche que vous devez accomplir, comme les éléments de votre liste de tâches.

Chaque page ne contient pas seulement des informations sur la tâche écrite dessus, mais a également des connexions aux pages avant et après elle dans le livre.

* La page 1 (Tâche A) représente la première tâche du livre. Elle contient des informations sur la Tâche A et a une flèche pointant vers la Page 2 (Tâche B), indiquant que la Tâche B vient après la Tâche A dans le livre. Cependant, la Page 1 n'a pas de flèche vers l'arrière car c'est la première page du livre et n'a pas de page précédente.
* La page 2 (Tâche B) contient des informations sur la Tâche B et a des flèches pointant à la fois vers la Page 3 (Tâche C) et vers la Page 1 (Tâche A), indiquant que la Tâche C vient après la Tâche B et que la Tâche A vient avant la Tâche B dans le livre.
* La page 3 (Tâche C) représente la dernière tâche du livre. Elle contient des informations sur la Tâche C et a une flèche pointant vers la Page 2 (Tâche B), indiquant que la Tâche B vient avant la Tâche C dans le livre.

Avec cela en tête, vous pouvez penser à une liste doublement chaînée comme un livre où chaque page contient non seulement des informations sur une tâche, mais fournit également une navigation facile vers les tâches avant et après elle. La première page, similaire à la tête d'une liste doublement chaînée, n'a pas de référence précédente, tandis que la dernière page, similaire à la queue d'une liste doublement chaînée, n'a pas de référence suivante.

### Caractéristiques de performance des listes doublement chaînées

1. **Parcours** : Les listes doublement chaînées permettent un parcours dans les deux directions — avant et arrière. Ce parcours bidirectionnel permet une navigation plus flexible à travers la liste, permettant des opérations telles que l'itération dans l'ordre inverse.
2. **Efficacité mémoire** : Les listes doublement chaînées nécessitent généralement plus de mémoire par rapport aux listes simplement chaînées car chaque nœud contient deux références (pointeurs) — une pour le nœud suivant et une pour le nœud précédent. Cette surcharge mémoire supplémentaire par nœud peut affecter l'efficacité mémoire globale, en particulier pour les grandes listes.
3. **Complexité** : Les listes doublement chaînées offrent un parcours bidirectionnel et de la flexibilité. Les opérations d'insertion et de suppression peuvent nécessiter la mise à jour des références dans les deux directions (avant et arrière), ce qui peut augmenter la complexité et potentiellement affecter les performances.

### Complexité temporelle et spatiale

#### Parcours

La complexité temporelle et spatiale pour cette opération est la même que pour la liste simplement chaînée.

#### Insertion au début

La complexité temporelle et spatiale pour cette opération est la même que pour la liste simplement chaînée.

#### Insertion à la fin

Complexité temporelle pour cette opération prend O(1) temps. Cela est dû au fait que vous avez un accès direct au nœud de queue, donc vous pouvez mettre à jour les références sans avoir besoin de parcourir toute la liste. Complexité spatiale O(1), elle ne nécessite pas d'espace supplémentaire proportionnel à la taille de l'entrée.

#### Suppression au début

La complexité temporelle et spatiale pour cette opération est la même que pour la liste simplement chaînée.

#### Suppression à la fin

Complexité temporelle pour cette opération prend O(1) temps. Cela est dû au fait que vous avez un accès direct au nœud de queue, donc vous pouvez mettre à jour les références sans avoir besoin de parcourir toute la liste. Complexité spatiale O(1), elle ne nécessite pas d'espace supplémentaire proportionnel à la taille de l'entrée.

## Liste chaînée circulaire

Une liste chaînée circulaire est un type de liste chaînée où le dernier nœud de la liste pointe vers le premier nœud, formant un cercle ou une boucle. Cette caractéristique la distingue d'une liste chaînée traditionnelle, où le dernier nœud pointe généralement vers null, indiquant la fin de la liste. Dans une liste chaînée circulaire, il n'y a pas de pointeur null à la fin ; au lieu de cela, le dernier nœud pointe vers le premier nœud, créant une structure de boucle. Ce comportement de boucle permet un parcours continu à travers la liste. L'image ci-dessous montre comment fonctionne une liste chaînée circulaire simplement.

![circular-linked-list-1](https://www.freecodecamp.org/news/content/images/2024/02/circular-linked-list-1.png)


### Explication non technique

Imaginez une ligne de train qui forme une boucle, avec des passagers montant et descendant à diverses stations le long du chemin. Cette boucle représente une liste chaînée circulaire, où chaque station est un nœud et le train voyage continuellement autour de la boucle, prenant et déposant des passagers. 

Tout comme dans une liste chaînée circulaire, la boucle assure un parcours continu sans point de fin, et les passagers (données) peuvent être ajoutés ou retirés à n'importe quelle station (nœud).  
  
La liste chaînée circulaire offre des avantages dans certaines applications mais nécessite une manipulation minutieuse des pointeurs et de la gestion de la mémoire pour maintenir sa structure circulaire et prévenir des problèmes tels que les boucles infinies.

### Caractéristiques de performance des listes chaînées circulaires

1. **Parcours** : Les listes chaînées circulaires permettent un parcours en boucle, permettant une navigation fluide d'un nœud à un autre indépendamment de la direction. Cette structure circulaire facilite un parcours efficace sans avoir besoin de revenir au début lorsque la fin est atteinte, améliorant ainsi les performances de parcours.
2. **Efficacité mémoire** : Les listes chaînées circulaires simplement offrent généralement une efficacité mémoire similaire aux listes chaînées simplement, car elles nécessitent seulement un pointeur par nœud pour se connecter au nœud suivant dans la séquence. Cette structure à pointeur unique entraîne une surcharge mémoire plus faible par nœud par rapport aux listes doublement chaînées, améliorant potentiellement l'efficacité mémoire pour les grandes listes.
3. **Complexité** : Dans les listes chaînées circulaires simplement, les opérations d'insertion et de suppression nécessitent la mise à jour des références pour maintenir la structure circulaire, introduisant une complexité modérée par rapport aux listes chaînées linéaires.

### Complexité temporelle et spatiale

#### Parcours

Complexité temporelle : O(n) – Puisque vous devez parcourir tous les nœuds de la liste pour atteindre la fin. 

Complexité spatiale : O(1) – Seulement une quantité constante d'espace supplémentaire est requise pour une variable temporaire pour parcourir la liste.

#### Insertion au début

Complexité temporelle : O(1) – L'insertion au début implique simplement la mise à jour des références au début. 

Complexité spatiale : O(1) – Aucun espace supplémentaire n'est requis.

#### Insertion à la fin

Complexité temporelle : O(n) – Il peut être nécessaire de parcourir toute la liste pour atteindre la fin où l'insertion doit avoir lieu.

Complexité spatiale : O(1) – Aucun espace supplémentaire n'est requis.

#### Suppression au début

Complexité temporelle O(1), elle implique la mise à jour des références au début. 

Complexité spatiale O(1), constante.

#### Suppression à la fin

Complexité temporelle O(n), elle peut nécessiter de parcourir toute la liste pour atteindre la fin.

Complexité spatiale O(1), constante.

<h2 id="resume-des-operations"> Résumé des opérations pour la complexité temporelle </h2>

<table>
<thead>
<tr>
<th>Opération</th>
<th>Liste chaînée simplement</th>
<th>Liste doublement chaînée</th>
<th>Liste chaînée circulaire</th>
</tr>
</thead>
<tbody>
<tr>
<td>Parcours</td>
<td>O(n)</td>
<td>O(n)</td>
<td>O(n)</td>
</tr>
<tr>
<td>Insertion au début</td>
<td>O(1)</td>
<td>O(1)</td>
<td>O(1)</td>
</tr>
<tr>
<td>Insertion à la fin</td>
<td>O(n)</td>
<td>O(1)</td>
<td>O(n)</td>
</tr>
<tr>
<td>Suppression au début</td>
<td>O(1)</td>
<td>O(1)</td>
<td>O(1)</td>
</tr>
<tr>
<td>Suppression à la fin</td>
<td>O(n)</td>
<td>O(1)</td>
<td>O(n)</td>
</tr>
</tbody>
</table>


<h2 id="resume-des-operations"> Résumé des opérations pour la complexité spatiale </h2>

<table>
<thead>
<tr>
<th>Opération</th>
<th>Liste chaînée simplement</th>
<th>Liste doublement chaînée</th>
<th>Liste chaînée circulaire</th>
</tr>
</thead>
<tbody>
<tr>
<td>Parcours</td>
<td>O(1)</td>
<td>O(1)</td>
<td>O(1)</td>
</tr>
<tr>
<td>Insertion au début</td>
<td>O(1)</td>
<td>O(1)</td>
<td>O(1)</td>
</tr>
<tr>
<td>Insertion à la fin</td>
<td>O(1)</td>
<td>O(1)</td>
<td>O(1)</td>
</tr>
<tr>
<td>Suppression au début</td>
<td>O(1)</td>
<td>O(1)</td>
<td>O(1)</td>
</tr>
<tr>
<td>Suppression à la fin</td>
<td>O(1)</td>
<td>O(1)</td>
<td>O(1)</td>
</tr>
</tbody>
</table>

<h2 id="differences-entre-tableau-et-liste-chainee"> Différences entre tableau et liste chaînée </h2>

Une liste chaînée est une manière dynamique de représenter une liste, où l'ajout et la suppression d'éléments au début de la liste impliquent généralement de changer seulement quelques pointeurs. Cette opération peut être effectuée en temps constant, noté O(1), indépendamment de la taille de la liste.

En revanche, les tableaux sont une représentation séquentielle d'une liste. L'ajout ou la suppression d'éléments au début de la liste nécessite de déplacer tous les éléments suivants pour accommoder le changement. Cette opération a une complexité temporelle de O(n), où n est le nombre d'éléments dans le tableau. Par conséquent, pour les grands tableaux, l'ajout ou la suppression d'éléments au début peut être relativement lent par rapport aux listes chaînées.

<h2 id="comment-resoudre-le-probleme-de-suppression-des-doublons-dune-liste-triee"> Comment résoudre le problème de suppression des doublons d'une liste triée </h2>

Explication du problème : Étant donné la `head` d'une liste chaînée triée, supprimez tous les doublons de sorte que chaque élément apparaisse une seule fois. Retournez la liste chaînée triée également.

![algo-sample-3](https://www.freecodecamp.org/news/content/images/2024/02/algo-sample-3.png)


### Solution en PHP

```php
/**
 * Définition pour une liste simplement chaînée.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */


class Solution {

    /**
     * @param ListNode $head
     * @return ListNode
     */
    function deleteDuplicates($head) {
        $node = $head;

        while($node !== null && $node->next !== null) {
         
            if ($node->val == $node->next->val) {
                $node->next = $node->next->next;
            }else {
                $node = $node->next;
            }   
        }

        return $head;
    }
}

```

### Solution en JavaScript

```javascript
/**
 * Définition pour une liste simplement chaînée.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */


var deleteDuplicates = function(head) {
    let node = head;

    while(node?.next) {

        if (node.val === node.next.val) {
            node.next = node.next.next
        } else {
            node = node.next
        }
    }

    return head
};

```

**Explication du code**

Étant donné la méthode `deleteDuplicates` :

* `node` est initialisé à la tête de la liste chaînée.
* Une boucle while itère à travers la liste chaînée jusqu'à la fin ou jusqu'à ce que la propriété `next` du nœud courant soit `null`.
* À l'intérieur de la boucle, elle vérifie si la valeur du nœud courant est égale à la valeur du nœud suivant. Si elles sont égales, elle saute le nœud suivant en définissant la propriété `next` du nœud courant sur la propriété `next` du nœud suivant.
* Si les valeurs ne sont pas égales, elle passe au nœud suivant en mettant à jour la valeur de `node` à `node->next`.
* Enfin, la méthode retourne la tête de la liste chaînée modifiée.

L'opérateur null safe (`?.`) utilisé dans la solution de code JS est également disponible à partir de PHP 8.0. 

Ce code supprime efficacement les doublons d'une liste simplement chaînée en ajustant les pointeurs et a une complexité temporelle de `_O_(_n_)` et une complexité spatiale de `_O_(1)`, où _`n`_ est le nombre de nœuds dans la liste chaînée.

## Référence

* [Comment fonctionne une liste chaînée](https://www.freecodecamp.org/news/how-linked-lists-work/)

## Conclusion

Dans cet article, vous avez appris ce qu'est une liste chaînée, les types de listes chaînées et un problème réel qui implique la suppression des doublons d'une liste triée.

Continuez à apprendre, et bon codage !

Vous pouvez me trouver sur [LinkedIn](https://www.linkedin.com/in/suleolanrewaju/) et [Twitter](https://twitter.com/bigdevlarry).