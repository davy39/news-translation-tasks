---
title: Comment écrire un script PHP pour calculer l'aire d'un triangle
subtitle: ''
author: AYUSH MISHRA
co_authors: []
series: null
date: '2025-06-19T15:33:06.983Z'
originalURL: https://freecodecamp.org/news/use-php-to-calculate-the-area-of-a-triangle
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1750346934679/2e46bebb-9614-4f1a-afb5-9bbe27906b4e.png
tags:
- name: PHP
  slug: php
- name: Mathematics
  slug: mathematics
- name: triangle
  slug: triangle
- name: DSA
  slug: dsa
- name: Programming Blogs
  slug: programming-blogs
- name: MathJax
  slug: mathjax
seo_title: Comment écrire un script PHP pour calculer l'aire d'un triangle
seo_desc: In programming, being able to find the area of a triangle is useful for
  many reasons. It can help you understand logic-building and syntax, and it’s a common
  programming problem used in school assignments. There are also many real-world applications,...
---

En programmation, savoir calculer l'aire d'un triangle est utile pour de nombreuses raisons. Cela peut vous aider à comprendre la construction logique et la syntaxe, et c'est un problème de programmation courant utilisé dans les devoirs scolaires. Il existe également de nombreuses applications réelles, telles que les graphiques informatiques, les simulations basées sur la géométrie ou les calculs liés à la construction.

Dans cet article, nous allons examiner un problème courant : on nous donne les dimensions d'un triangle, et notre tâche est de calculer son aire. Vous pouvez calculer l'aire d'un triangle en utilisant différentes formules, selon les informations dont vous disposez sur le triangle. Ici, vous allez apprendre comment le faire en utilisant PHP.

### Après avoir lu ce tutoriel :

* Vous comprendrez la logique de base derrière le calcul de l'aire d'un triangle.

* Vous saurez comment écrire du code PHP qui calcule l'aire du triangle en utilisant des valeurs prédéfinies et saisies par l'utilisateur.

* Vous saurez comment appliquer cette logique dans de petits projets et devoirs.

## Table des matières

1. [Prérequis](#heading-prerequis)

2. [Trouver l'aire d'un triangle en utilisant des formules directes](#heading-trouver-laire-dun-triangle-en-utilisant-des-formules-directes)

3. [Trouver l'aire d'un triangle en utilisant l'approche base et hauteur](#heading-trouver-laire-dun-triangle-en-utilisant-lapproche-base-et-hauteur)

4. [Trouver l'aire d'un triangle en utilisant la formule de Héron](#heading-trouver-laire-dun-triangle-en-utilisant-la-formule-de-heron)

5. [Trouver l'aire d'un triangle en utilisant deux côtés et l'angle inclus (Formule trigonométrique)](#heading-trouver-laire-dun-triangle-en-utilisant-deux-cotes-et-langle-inclus-formule-trigonometrique)

6. [Conclusion](#heading-conclusion)

## Prérequis

Vous comprendrez ce guide plus facilement si vous avez quelques connaissances sur certains sujets :

### PHP de base

Vous devrez connaître la syntaxe PHP de base pour comprendre pleinement le problème. Si vous savez comment écrire une simple instruction echo ou créer une variable en PHP, alors vous devriez être prêt.

### Environnement PHP local

Pour exécuter le code PHP avec succès, vous devriez avoir un environnement de développement PHP local, tel que XAMPP ou WAMP, sur votre machine. Vous pouvez également utiliser des éditeurs PHP en ligne comme PHP Fiddle ou OnlineGDB pour exécuter un script PHP sans aucune installation.

Dans ce tutoriel, nous allons explorer trois approches pour déterminer l'aire du triangle en PHP en fonction de la quantité d'informations disponibles sur le triangle.

* **Approche par formule de base et hauteur :** Cette approche est applicable lorsque vous avez la hauteur perpendiculaire à partir de la base et la longueur de la base dans le problème.

* **Formule de Héron :** Cette approche est utilisée pour calculer l'aire du triangle lorsque vous avez les longueurs des trois côtés du triangle.

* **Approche par formule trigonométrique :** Cette approche est appliquée au problème lorsque vous avez la longueur de deux côtés et l'angle inclus entre eux.

Tout d'abord, retournons en cours de mathématiques et utilisons quelques formules directes pour trouver l'aire.

## Trouver l'aire d'un triangle en utilisant des formules directes

### Exemple 1 :

Dans ce premier exemple, on vous donne la base et la hauteur d'entrée d'un triangle. Vous devez retourner l'aire du triangle. Pour cet exemple, vous utiliserez une formule directe pour calculer l'aire du triangle.

**Entrée :**

Base = 5,

Hauteur = 10

Vous pouvez calculer l'aire du triangle en utilisant la formule :

$$Aire = (Base * Hauteur) / 2$$

Donc, si vous insérez les valeurs que vous avez, vous obtenez : (5 * 10) / 2 = 25.

**Sortie :**

Aire = 25

### Exemple 2 :

Dans ce deuxième exemple, on vous donne la longueur de deux côtés d'un triangle et un angle entre eux. Vous devez retourner l'aire du triangle. Dans cet exemple, vous utiliserez une autre formule directe pour calculer l'aire du triangle.

**Entrée :**

Côté A = 7, Côté B = 9, Angle entre eux = 60°

Dans ce cas, vous utiliserez la formule :

$$Aire = (1/2) A B * sin(Angle).$$

Ensuite, il suffit de substituer les valeurs que vous avez reçues pour trouver l'aire.

**Sortie :**

Aire = 27.33 (approximativement)

Maintenant, examinons différentes approches pour trouver l'aire d'un triangle en utilisant PHP.

## Trouver l'aire d'un triangle en utilisant l'approche base et hauteur

Il s'agit de l'approche la plus simple et la plus directe pour calculer l'aire d'un triangle lorsque vous connaissez la base et la hauteur. Dans cette approche, vous allez directement mettre les valeurs dans la formule et trouver l'aire du triangle, mais vous le ferez avec du code PHP.

Tout d'abord, définissez la base et la hauteur du triangle. Ensuite, appliquez la formule pour l'aire du triangle. Comme nous l'avons vu ci-dessus, la formule pour l'aire d'un triangle est :

$$Aire = (Base * Hauteur) / 2$$

Après avoir calculé l'aire du triangle, affichez la réponse.

Voici comment nous pouvons implémenter cela en PHP :

```php
<?php
// Définir la base et la hauteur
$base = 5;
$hauteur = 10;

// Calculer l'aire
$aire = ($base * $hauteur) / 2;

// Afficher le résultat
echo "L'aire du triangle est : " . $aire . " unités carrées.";
?>
```

Sortie :

L'aire du triangle est 25 unités carrées.

Dans le code ci-dessus, nous initialisons d'abord la base et la hauteur du triangle dans deux variables. Ensuite, nous insérons ces valeurs dans la formule de l'aire. PHP calcule l'aire du triangle et affiche la réponse.

**Complexité temporelle :** Dans l'approche ci-dessus, nous utilisons la formule directe pour calculer et retourner l'aire du triangle, donc la complexité temporelle sera constante à O(1). La complexité temporelle constante est efficace car elle restera constante, quelle que soit la taille ou les valeurs de la base et de la hauteur.

**Complexité spatiale :** La complexité spatiale sera O(1). L'espace utilisé par le programme ci-dessus est constant, ce qui garantit une utilisation minimale de la mémoire. Cette complexité spatiale est idéale dans les environnements où l'efficacité de la mémoire est une priorité.

Nous utilisons l'approche ci-dessus lorsque nous avons la longueur de la base et de la hauteur du triangle (qu'elles soient directement données ou facilement mesurables dans un triangle rectangle). Cette méthode fonctionne mieux pour les triangles rectangles.

## Trouver l'aire d'un triangle en utilisant la formule de Héron

La formule de Héron porte le nom d'un mathématicien grec nommé Héron d'Alexandrie. La formule de Héron est utile lorsque vous connaissez les longueurs des trois côtés du triangle et que vous souhaitez calculer l'aire sans avoir besoin de la hauteur. Cette formule fonctionne pour tout type de triangle, y compris les triangles scalènes (triangles dont les côtés sont tous de longueurs différentes).

Voici la formule de Héron pour calculer l'aire d'un triangle :

$$\sqrt{s(s-a)(s-b)(s-c)}\ $$

Où :

* s = demi-périmètre = (a+b+c)/2 est le demi-périmètre du triangle.

* a, b et c sont les longueurs des côtés.

Tout d'abord, nous définissons les trois côtés du triangle. Ensuite, nous vérifions les trois conditions du [Théorème de l'inégalité triangulaire](https://fr.wikipedia.org/wiki/In%C3%A9galit%C3%A9_triangulaire) qui stipule que si la somme de deux côtés est supérieure au troisième côté, alors il s'agit d'un triangle valide, et les côtés donnés peuvent former un triangle.

Nous pouvons calculer le demi-périmètre du triangle en utilisant la formule s = a+b+c/2. Ensuite, nous pouvons appliquer la formule de Héron pour calculer l'aire. Après avoir calculé l'aire, nous affichons la réponse.

Voici comment vous pouvez implémenter cela en PHP :

```php
<?php
// Définir les côtés du triangle
$a = 7;
$b = 9;
$c = 10;

// Vérifier si les côtés forment un triangle valide en utilisant le Théorème de l'inégalité triangulaire
if (($a + $b > $c) && ($a + $c > $b) && ($b + $c > $a)) {

    // Calculer le demi-périmètre
    $s = ($a + $b + $c) / 2;

    // Calculer l'aire en utilisant la formule de Héron
    $aire = sqrt($s * ($s - $a) * ($s - $b) * ($s - $c));

    // Afficher le résultat
    echo "L'aire du triangle est : " . $aire . " unités carrées.";

} else {
    // Si les côtés ne peuvent pas former un triangle valide
    echo "Les côtés donnés ne forment pas un triangle valide.";
}
?>
```

Sortie :

L'aire du triangle est : 27.321 unités carrées.

Dans le code ci-dessus, nous créons d'abord trois variables pour stocker les longueurs des côtés du triangle, et nous vérifions si les côtés donnés forment un triangle valide ou non en utilisant le Théorème de l'inégalité triangulaire. Ensuite, nous calculons le demi-périmètre en utilisant la formule : s = a + b + c / 2. Nous mettons la valeur du demi-périmètre et les longueurs de tous les côtés dans la formule de Héron pour calculer l'aire. L'aire du triangle est retournée après le calcul en utilisant la formule.

**Complexité temporelle :** Il y a un nombre total fixe d'opérations telles que l'addition, la soustraction, la multiplication et la racine carrée. Ces opérations ne dépendent pas de la taille de l'entrée car elles sont effectuées seulement un nombre fixe de fois. Cela signifie que la complexité temporelle est constante O(1).

**Complexité spatiale :** Nous avons utilisé un nombre fixe de variables pour calculer l'aire du triangle. Nous n'avons pas utilisé de structures de données supplémentaires telles que des tableaux ou des objets. L'utilisation de la mémoire dans le programme est constante, ce qui est mieux pour les environnements à faible mémoire. La complexité spatiale est constante O(1).

Cette approche fonctionne mieux lorsque les longueurs de tous les côtés sont données. Cette approche est principalement utilisée pour les triangles scalènes ou isocèles où la hauteur n'est pas directement donnée. Cette approche peut fonctionner pour tout type de triangle, cependant, scalène, isocèle ou équilatéral.

## Trouver l'aire d'un triangle en utilisant deux côtés et l'angle inclus (Formule trigonométrique)

Dans cette approche, nous allons voir une variation différente du problème. Lorsque vous connaissez deux côtés d'un triangle et l'angle inclus entre eux, vous pouvez calculer l'aire en utilisant cette formule :

$$Aire = 1/2 × a × b × sin(θ)$$

Où :

* a et b sont les longueurs des deux côtés.

* θ est l'angle inclus entre les deux côtés, mesuré en degrés ou en radians.

En utilisant la formule ci-dessus, vous pouvez calculer l'aire d'un triangle sans avoir besoin de sa hauteur. Tout d'abord, vous définissez les deux côtés du triangle et l'angle entre eux. Ensuite, vous convertissez l'angle de degrés en radians si nécessaire (en PHP, vous pouvez utiliser deg2rad() pour convertir les degrés en radians). Ensuite, vous appliquez la formule.

Après avoir calculé l'aire du triangle, affichez le résultat.

Voici comment implémenter cela en PHP :

```php
<?php
// Définir les deux côtés et l'angle inclus
$a = 7;
$b = 9;
$angle = 60; // Angle en degrés

// Convertir l'angle de degrés en radians
$angle_en_radians = deg2rad($angle);

// Calculer l'aire en utilisant la formule
$aire = 0.5 * $a * $b * sin($angle_en_radians);

// Afficher le résultat
echo "L'aire du triangle est : " . $aire . " unités carrées.";
?>
```

Sortie :

L'aire du triangle est : 27.321 unités carrées.

Explication :

Dans le cas ci-dessus, nous utilisons la formule :

Aire du Triangle = 1/2 × a × b × sin(θ)

Et nous substituons les valeurs suivantes dans la formule :

Aire = 1/2 × 7 × 9 × sin(60°) ≈ 27.321

Dans le code, nous avons déclaré deux variables pour stocker la longueur des deux côtés du triangle, et la variable `$angle` contient l'angle inclus en degrés. Nous avons utilisé `deg2rad()`, une fonction intégrée de PHP qui convertit un angle de degrés en radians. Ensuite, nous avons appliqué la formule réelle : Aire = 1/2 × 7 × 9 × sin(60°). PHP stocke la réponse finale dans la variable `$aire`.

**Complexité temporelle :** Nous utilisons la formule directe pour calculer l'aire d'un triangle lorsque la longueur de deux côtés et l'angle entre eux sont donnés. La complexité temporelle constante est O(1).

**Complexité spatiale :** De même, elle ne prend pas d'espace supplémentaire ni n'utilise de structures de données. Elle utilise une seule variable pour stocker le résultat, c'est pourquoi la complexité spatiale est constante O(1).

Cette approche est parfaite pour le problème dans lequel deux côtés et l'angle inclus (angle entre ces côtés) sont connus. Vous pouvez l'utiliser lorsque vous ne pouvez pas facilement calculer la hauteur du triangle. Ce problème a des applications réelles dans les problèmes de géométrie, les applications de CAO ou les simulations physiques. Cette méthode est très précise et ne nécessite pas la longueur de tous les côtés.

## Conclusion

Dans cet article, vous avez appris comment calculer l'aire d'un triangle, à la fois manuellement et en utilisant PHP. Vous avez vu différentes approches et appris laquelle est la meilleure en fonction des informations dont vous disposez. Tout d'abord, nous avons discuté de l'approche par base et hauteur, puis nous avons examiné la formule de Héron, et enfin nous avons étudié comment gérer les choses lorsque deux côtés et l'angle inclus sont donnés.

Comprendre la logique derrière chacune de ces approches vous aide à choisir la bonne en fonction des données fournies.

Et si vous souhaitez me soutenir directement et mon travail afin que je puisse continuer à créer ces tutoriels, [vous pouvez le faire ici](https://paypal.me/ayushM010). Merci !