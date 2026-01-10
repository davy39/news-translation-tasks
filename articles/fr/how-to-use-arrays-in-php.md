---
title: Tableaux PHP – Comment utiliser les tableaux dans vos projets PHP
subtitle: ''
author: Okoro Emmanuel Nzube
co_authors: []
series: null
date: '2022-06-22T17:30:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-arrays-in-php
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/Arrays-in-PHP-final.png
tags:
- name: arrays
  slug: arrays
- name: PHP
  slug: php
seo_title: Tableaux PHP – Comment utiliser les tableaux dans vos projets PHP
seo_desc: 'An array is a special variable that we use to store or hold more than one
  value in a single variable without having to create more variables to store those
  values.

  To create an array in PHP, we use the array function array( ).

  By default, an array of...'
---

Un tableau est une variable spéciale que nous utilisons pour stocker ou contenir plus d'une valeur dans une seule variable sans avoir à créer plus de variables pour stocker ces valeurs.

Pour créer un tableau en PHP, nous utilisons la fonction `array( )`.

Par défaut, un tableau de toute variable commence avec l'index `0`. Donc, chaque fois que vous voulez appeler la première valeur d'un tableau, vous commencez par `0`, puis la suivante est `1`... et ainsi de suite.

Il existe différents types de tableaux en PHP. Ils sont :

* Tableaux numériques/indexés

* Tableaux associatifs

* Tableaux multidimensionnels

Examinons comment chacun fonctionne plus en détail.

## Qu'est-ce que les tableaux numériques ou indexés ?

Un tableau numérique est un type de tableau qui peut stocker des chaînes de caractères, des nombres et des objets. Voici un exemple de tableau numérique :

```php
<?php
// Tableaux numériques/indexés
$cars = array('Mecedes Benz', 'Hilux', 'Highlander', 'Hummer', 'Limozien');
var_dump($cars);
?>
```

Dans le code ci-dessus, j'ai une variable `$cars` qui stocke un tableau de 5 éléments. Le mot-clé `var_dump($cars)` ci-dessus nous montrera le nombre total d'éléments que nous avons dans le tableau, le numéro d'index de chaque tableau, ainsi que la longueur de chaque élément dans le tableau.

Vous pouvez également choisir d'utiliser le mot-clé `echo( )`, mais dans mon cas, je préfère utiliser `var_dump( )` car il donne une explication plus détaillée des résultats que nous obtenons.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/localhost_CODE_Arrays_arrays.php---Google-Chrome-6_15_2022-8_44_07-PM.png align="left")

Vous pouvez également choisir d'afficher un seul élément/objet d'un tableau dans le navigateur web en faisant ceci :

```php
<?php
$numbers = array('8', '20', '40', '58', '88', '200', '400', '500');
var_dump ($numbers [4]);
?>
```

Le code ci-dessus suit le même schéma que notre définition d'un tableau, qui stipule qu'il compte à partir de zéro. Nous voulons afficher l'élément avec l'index `4`. En comptant de `0 à 4`, nous pouvons voir que `88` tombe sous l'index `4`, indiquant que `88` est le nombre que nous cherchons et qui sera affiché dans le navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/localhost_CODE_Arrays_arrays.php---Google-Chrome-6_17_2022-8_17_58-PM.png align="left")

## Qu'est-ce que les tableaux associatifs ?

Un tableau associatif est un type de tableau où la clé a sa propre valeur. Dans un tableau associatif, nous utilisons `clé` et `valeur`.

Les `clé`s sont des légendes descriptives de l'élément de tableau utilisées pour accéder à la valeur du tableau. Et `valeur` est la valeur assignée à l'élément du tableau.

Il existe des situations où vous ne devriez pas utiliser le tableau numérique/indexé, telles que :

* Lorsque vous voulez stocker l'âge de différents étudiants avec leurs noms.

* Lorsque vous voulez enregistrer les salaires de vos employés.

* Lorsque vous voulez stocker les notes d'un étudiant dans différentes matières

et ainsi de suite.

Supposons que nous voulons assigner des âges à un groupe d'étudiants du secondaire avec leurs noms.

Nous pouvons utiliser la méthode de tableau associatif pour le faire. Par exemple :

```php
<?php
$student_age = array (
'Scott_Mcall' => 17,
'Stalenski' => 18,
'Lydia' => 16,
'Allision' => 17,
);

echo $student_age ['Scott_Mcall']; // ce code affichera l'âge de Scot_Mcall comme 17
echo $student_age ['Stalenski']; // ce code affichera l'âge de Stalenski comme 18
echo $student_age ['Lydia']; // ce code affichera l'âge de Lydia comme 16
echo $student_age ['Allision']; // ce code affichera l'âge de Allision comme 17
?>
```

Le code ci-dessus est un exemple de tableau associatif. Les `clé`s du tableau sont `scott_Mcall`, `Stalenski`, `Lydia`, `Allision`, et nous les avons utilisées pour assigner l'âge à chaque étudiant. Les `valeur`s du tableau sont `17`, `18`, `16`, et `17`.

## Qu'est-ce que les tableaux multidimensionnels ?

Vous pouvez penser à un tableau multidimensionnel comme un tableau de tableaux. Cela signifie que chaque élément du tableau contient un sous-tableau. En général, les tableaux multidimensionnels vous permettent de stocker plusieurs tableaux dans une seule variable.

Supposons que nous voulons stocker les noms, les numéros d'immatriculation et les emails de certains membres du personnel travaillant dans une entreprise particulière. Nous pouvons utiliser des tableaux multidimensionnels pour archiver cela.

Par exemple :

```php
<?php
$Staffs = [
	[
		'Name' => 'Derek Emmanuel',
		'Reg_No' => 'FE/30304',
		'Email' => 'derekemmanuel@gmail.com'
	],
	[
		'Name' => 'Rubecca Michealson',
		'Reg_No' => 'FE/20003',
		'Email' => 'rmichealsongmail.com'
	],
	[
		'Name' => 'Frank Castle',
		'Reg_No' => 'FE/10002',
		'Email' => 'fcastle86@gmail.com'
	]
];
echo $Staffs [2] ['Email']; // Cela affiche l'email du dernier membre du personnel qui est fcastle86@gmail.com

echo $staffs [0] ['Name']; // Cela affiche le nom du membre du personnel dans le premier tableau (index 0) qui est Derek Emmanuel

// vous pouvez accéder aux informations de n'importe quel membre du personnel que vous souhaitez en utilisant echo $(nom de la variable) [numéro d'index] ['clé de l'élément du tableau'].


?>
```

Rappelez-vous, un tableau commence à compter à partir de l'index `0`. Le code ci-dessus est un exemple de tableau multidimensionnel car il contient plus d'un tableau (un tableau de tableaux) avec une seule variable `$staff`.

Le `echo $staff [2] ['Email']` affiche l'email du membre du personnel qui tombe sous l'index `2`. Dans notre cas, il affichera [`fcastle86@gmail.com`](mailto:fcastle86@gmail.com).

Si je veux accéder à l'email du membre du personnel dans le premier tableau, nous ferons ce qui suit :

`echo $staff [0] ['Email'];`

En utilisant la méthode ci-dessus, vous pouvez accéder et afficher n'importe quelle information dans le tableau à partir du code ci-dessus.

## Conclusion

À ce stade, vous devriez être en mesure d'utiliser les trois différents types de tableaux lorsque vous travaillez sur un projet PHP.

Merci d'avoir lu.

Amusez-vous bien à coder !