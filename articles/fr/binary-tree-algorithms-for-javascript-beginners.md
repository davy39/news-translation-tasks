---
title: Algorithmes d'arbre binaire de recherche pour débutants en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-11T23:50:28.000Z'
originalURL: https://freecodecamp.org/news/binary-tree-algorithms-for-javascript-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/binarytree.png
tags:
- name: algorithms
  slug: algorithms
- name: binary search
  slug: binary-search
- name: interview questions
  slug: interview-questions
- name: JavaScript
  slug: javascript
seo_title: Algorithmes d'arbre binaire de recherche pour débutants en JavaScript
seo_desc: 'I recently had the chance to teach high school students how to code. There
  are not that many beginner-friendly tutorials on algorithms coded in JavaScript
  which is the language they were learning. So I decided to make one.

  In this article, I will try...'
---

J'ai récemment eu l'occasion d'enseigner à des lycéens comment coder. Il n'y a pas tant de tutoriels adaptés aux débutants sur les algorithmes codés en JavaScript, qui est la langue qu'ils apprenaient. J'ai donc décidé d'en créer un.

Dans cet article, je vais essayer de mon mieux d'expliquer certains algorithmes de base que vous devriez apprendre avant un entretien de codage.

Si vous n'êtes pas familier avec le concept d'un arbre binaire, je vous encourage à consulter la page [wikipedia](https://en.wikipedia.org/wiki/Binary_tree). Si vous maîtrisez parfaitement ces algorithmes de base, vous aurez plus de facilité à résoudre des problèmes plus complexes.

## Qu'est-ce qu'un arbre binaire de recherche (BST) ?

Communément trouvé dans les entretiens de codage, BST est une structure de données en forme d'arbre avec une seule racine tout en haut. Ils sont un excellent moyen de stocker des valeurs numériques car leur nature ordonnée permet des recherches et des recherches rapides.

Comparé à un arbre normal, BST a les propriétés suivantes :

* chaque enfant gauche a une valeur plus petite que son parent
* chaque enfant droit a une valeur plus grande que son parent
* chaque nœud peut contenir de 0 à 2 enfants.

Le diagramme suivant devrait clarifier un peu plus les choses.

## Définition d'un nœud d'arbre binaire

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Untitled_Artwork-25.png)
_Un arbre binaire de recherche_

Nous définissons généralement un nœud d'arbre binaire avec la fonction suivante en Javascript :

```js
 function TreeNode(val, left, right) {
     this.val = val
     this.left = left
     this.right = right
 }
```

## Parcours de base d'un arbre binaire (Inorder, Postorder, Preorder)

La première chose à savoir est comment parcourir chaque nœud du BST. Cela nous permet d'effectuer une fonction sur tous les nœuds de notre BST. Par exemple, si nous voulons trouver une valeur `x` dans notre BST, nous aurions besoin des nœuds.

Il existe trois façons principales de faire cela. Heureusement, elles partagent des thèmes communs.

### Parcours Inorder

Un algorithme récursif est le moyen le plus simple de commencer avec le parcours inorder d'un arbre binaire. L'idée est la suivante :

* Si le nœud est null, ne faites rien – sinon, appelez récursivement la fonction sur l'enfant gauche du nœud.
* Ensuite, effectuez une opération sur le nœud après avoir parcouru tous les enfants gauches. Notre nœud actuel est garanti d'être le nœud le plus à gauche.
* Enfin, appelez la fonction sur node.right.

L'algorithme Inorder parcourt les nœuds de l'arbre de gauche, à milieu, à droite.

```js
/**
* @param {TreeNode} root
*/
const inorder = (root) => {
    const nodes = []
    if (root) {
        inorder(root.left)
        nodes.push(root.val)
        inorder(root.right)
    }
    return nodes
}
// pour notre exemple d'arbre, cela retourne [1,2,3,4,5,6]
```

### Parcours Postorder

Un algorithme récursif est le moyen le plus simple de commencer avec le parcours postorder.

* Si le nœud est null, ne faites rien – sinon, appelez récursivement la fonction sur l'enfant gauche du nœud.
* Lorsque qu'il n'y a plus d'enfants gauches, appelez la fonction sur node.right.
* Enfin, effectuez une opération sur le nœud.

Le parcours postorder visite les nœuds de l'arbre de gauche, à droite, à milieu.

```js
/**
* @param {TreeNode} root
*/
const postorder = (root) => {
    const nodes = []
    if (root) {
        postorder(root.left)
        postorder(root.right)
        nodes.push(root.val)
    }
    return nodes
}
// pour notre exemple d'arbre, cela retourne [1,3,2,6,5,4]
```

### Parcours Preorder

Un algorithme récursif est le moyen le plus simple de commencer avec le parcours preorder.

* Si le nœud est null, ne faites rien – sinon, effectuez une opération sur le nœud.
* Parcourez l'enfant gauche du nœud et répétez.
* Parcourez l'enfant droit du nœud et répétez.

Le parcours postorder visite les nœuds de l'arbre de milieu, à gauche, à droite.

```js
/**
* @param {TreeNode} root
*/
const preorder = (root) => {
    const nodes = []
    if (root) {
        nodes.push(root.val)
        preorder(root.left)
        preorder(root.right)
    }
    return nodes
}
// pour notre exemple d'arbre, cela retourne [4,2,1,3,5,6]
```

## Qu'est-ce qu'un arbre binaire de recherche valide ?

Un arbre binaire de recherche valide (BST) a TOUS les enfants gauches avec des valeurs inférieures au nœud parent, et TOUS les enfants droits avec des valeurs supérieures au nœud parent.

Pour vérifier si un arbre est un arbre binaire de recherche valide :

* Définissez la valeur minimale et maximale que le nœud actuel peut avoir
* Si la valeur d'un nœud n'est pas dans ces limites, retournez false
* Validez récursivement les enfants gauches du nœud, avec la limite maximale définie à la valeur du nœud
* Validez récursivement les enfants droits du nœud, avec la limite minimale définie à la valeur du nœud

```js
/**
* @param {TreeNode} root
*/
const isValidBST = (root) => {
    const helper = (node, min, max) => {
        if (!node) return true
        if (node.val <= min || node.val >= max) return false
        return helper(node.left, min, node.val) && helper(node.right, node.val, max)
    }
    return helper(root, Number.MIN_SAFE_INTEGER, Number.MAX_SAFE_INTEGER)
}
```

## Comment trouver la profondeur maximale d'un arbre binaire

Ici, l'algorithme tente de trouver la hauteur/profondeur de notre BST. En d'autres termes, nous regardons combien de 'niveaux' un BST contient.

* Si le nœud est null, nous retournons 0 car il n'ajoute aucune profondeur
* Sinon, nous ajoutons + 1 à notre profondeur actuelle (nous avons parcouru un niveau)
* Calculez récursivement la profondeur des enfants du nœud et retournez la somme maximale entre node.left et node.right

```js
/**
* @param {TreeNode} root
*/
const maxDepth = function(root) {
    const calc = (node) => {
        if (!node) return 0
        return Math.max(1 + calc(node.left), 1 + calc(node.right))
    }
    return calc(root)
};
```

## Comment trouver l'ancêtre commun le plus bas entre deux nœuds d'arbre

Augmentons la difficulté. Comment trouver l'ancêtre commun entre deux nœuds d'arbre dans notre arbre binaire ? Regardons quelques exemples.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Untitled_Artwork-25.png)
_Un arbre binaire de recherche_

Dans cet arbre, l'ancêtre commun le plus bas de 3 et 1 est 2. L'ACB de 3 et 2 est 2. L'ACB de 6 et 1 et 6 est 4.

Voyez-vous le schéma ici ? L'ACB entre deux nœuds d'arbre est soit l'un des nœuds lui-même (le cas de 3 et 2), soit un nœud parent où le premier enfant est trouvé quelque part dans son sous-arbre gauche, et le second enfant quelque part dans son sous-arbre droit.

L'algorithme pour trouver l'ancêtre commun le plus bas (ACB) entre deux nœuds d'arbre p et q est le suivant :

* Vérifiez si p ou q est trouvé dans le sous-arbre gauche ou droit
* Ensuite, vérifiez si le nœud actuel est p ou q
* Si l'un de p ou q est trouvé dans le sous-arbre gauche ou droit, et que l'un de p ou q est le nœud lui-même, nous avons trouvé l'ACB
* Si p et q sont tous deux trouvés dans le sous-arbre gauche ou droit, nous avons trouvé l'ACB

```js
/**
* @param {TreeNode} root
* @param {TreeNode} p
* @param {TreeNode} q
*/
const lowestCommonAncestor = function(root, p, q) {
    let lca = null
    const isCommonPath = (node) => {
        if (!node) return false
        var isLeft = isCommonPath(node.left)
        var isRight = isCommonPath(node.right)
        var isMid = node == p || node == q
        if (isMid && isLeft || isMid && isRight || isLeft && isRight) {
            lca = node
        }
        return isLeft || isRight || isMid
    }
    isCommonPath(root)
    return lca
};
```

## Conclusion

En résumé, nous avons appris comment parcourir, vérifier et calculer la profondeur d'un BST.

Ces algorithmes sont souvent demandés lors des entretiens de codage. Il est important de les comprendre avant de pratiquer des applications BST plus avancées, comme trouver l'ACB de deux nœuds.