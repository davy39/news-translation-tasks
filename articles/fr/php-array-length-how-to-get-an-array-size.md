---
title: Tutoriel sur la longueur des tableaux PHP – Comment obtenir la taille d'un
  tableau
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-27T19:10:13.000Z'
originalURL: https://freecodecamp.org/news/php-array-length-how-to-get-an-array-size
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/count.jpg
tags:
- name: arrays
  slug: arrays
- name: PHP
  slug: php
seo_title: Tutoriel sur la longueur des tableaux PHP – Comment obtenir la taille d'un
  tableau
seo_desc: "By Jonathan Bossenger\nArrays are a powerful data type in PHP. And knowing\
  \ how to quickly determine the size of an array is a useful skill. \nIn this article\
  \ I'll give you a quick overview of how arrays work, and then I'll dive into how\
  \ to get the size..."
---

Par Jonathan Bossenger

Les tableaux sont un type de données puissant en PHP. Et savoir comment déterminer rapidement la taille d'un tableau est une compétence utile. 

Dans cet article, je vais vous donner un aperçu rapide du fonctionnement des tableaux, puis je vais me pencher sur la manière d'obtenir la taille des tableaux PHP.

Si vous savez déjà ce que sont les tableaux, vous pouvez passer directement à la section **[Comment obtenir la taille d'un tableau ?](#comment-obtenir-la-taille-dun-tableau)**.

## Qu'est-ce qu'un tableau en PHP ?

Avant de nous plonger dans l'obtention de la taille d'un tableau, nous devons nous assurer de comprendre ce qu'est un tableau. Un [tableau en PHP](https://www.php.net/manual/en/language.types.array.php) est un type de variable qui permet de stocker plus d'une donnée. 

Par exemple, si vous stockiez une simple chaîne de caractères, vous utiliseriez un type de chaîne PHP :

```php
$heading = 'Tutoriel sur la longueur des tableaux PHP';
```

Cependant, si vous vouliez stocker quelques données séparées supplémentaires, vous pourriez envisager d'utiliser plusieurs variables de chaîne.

```
$heading = 'Tutoriel sur la longueur des tableaux PHP';
$subheading = 'Comment obtenir la taille d'un tableau';
$author = 'Jonathan Bossenger'
```

C'est bien beau, mais que faire si vous devez stocker plus de données et rappeler rapidement l'une de ces données ailleurs dans votre code ? C'est là qu'un tableau devient pratique. Vous pouvez toujours stocker les données individuelles mais en utilisant une seule variable.

```php
$post_data = array(
    'Tutoriel sur la longueur des tableaux PHP',
    'Comment obtenir la taille d'un tableau',
    'Jonathan Bossenger'
);
```

Chaque élément de ce tableau peut être référencé par sa clé numérique. Ainsi, au lieu de devoir rappeler les variables individuelles, vous pourriez référencer un seul élément de tableau par sa clé numérique.

```
echo $post_data[0];
```

Pour encore plus de contrôle, les tableaux permettent également de définir vos propres clés de tableau, en utilisant une chaîne de caractères.

```
$post_data = array(
    'heading' => 'Tutoriel sur la longueur des tableaux PHP',
    'subheading' => 'Comment obtenir la taille d'un tableau',
    'author' => 'Jonathan Bossenger'
);
```

Cela permet également de référencer l'élément du tableau par sa clé de chaîne.

```php
echo $post_data['heading'];
```

Vous pouvez également définir des tableaux en utilisant la nouvelle notation courte de tableau, similaire à JavaScript :

```
$post_data = [
    'heading' => 'Tutoriel sur la longueur des tableaux PHP',
    'subheading' => 'Comment obtenir la taille d'un tableau',
    'author' => 'Jonathan Bossenger'
];
```

Les tableaux peuvent également être imbriqués, formant des variables de tableau plus complexes :

```
$post_data = [
    'heading' => 'Tutoriel sur la longueur des tableaux PHP',
    'subheading' => 'Comment obtenir la taille d'un tableau',
    'author' => [
        'name' => 'Jonathan Bossenger',
        'twitter' => 'jon_bossenger',
    ]
];

```

Et vous pouvez rappeler une valeur de tableau spécifique en utilisant sa clé imbriquée :

```php
echo $post_data['author']['name'];
```

Cependant, si vous vous retrouvez à faire cela régulièrement, vous pourriez envisager d'utiliser des [objets](https://www.php.net/manual/en/language.types.object.php) plutôt que des tableaux.

Les tableaux sont utiles si vous devez rapidement rassembler puis utiliser différentes données liées dans une fonction, ou transmettre ces données à une autre fonction. 

En mettant ces données dans un tableau, vous avez moins de variables définies, et cela peut rendre votre code plus facile à lire et à comprendre plus tard. Il est également beaucoup plus facile de transmettre une seule variable de tableau à une autre fonction que de transmettre plusieurs chaînes.

```
$post_data = [
    'heading' => 'Tutoriel sur la longueur des tableaux PHP',
    'subheading' => 'Comment obtenir la taille d'un tableau',
    'author' => [
        'name' => 'Jonathan Bossenger',
        'twitter' => 'jon_bossenger',
    ]
];

$filtered_post_data = filter_post_data($post_data)
```

## Comment obtenir la taille d'un tableau en PHP

Habituellement, lorsque nous parlons de la taille d'un tableau, nous parlons du nombre d'éléments existant dans ce tableau. Il existe deux méthodes courantes pour obtenir la taille d'un tableau.

La méthode la plus populaire consiste à utiliser la fonction PHP [count()](https://www.php.net/manual/en/function.count.php). Comme le nom de la fonction l'indique, `count()` retournera un compte des éléments d'un tableau. Mais la manière dont nous utilisons la fonction `count()` dépend de la structure du tableau.

Examinons les deux exemples de tableaux que nous avons définis précédemment.

```
$post_data = array(
	'heading' => 'Tutoriel sur la longueur des tableaux PHP',
	'subheading' => 'Comment obtenir la taille d'un tableau',
	'author' => 'Jonathan Bossenger'
);

echo count($post_data);
```

Dans cet exemple, `count($post_data)` donnera 3. Cela est dû au fait qu'il y a 3 éléments dans ce tableau : 'heading', 'subheading' et 'author'. Mais qu'en est-il de notre deuxième exemple de tableau imbriqué ?

```
$post_data = [
	'heading' => 'Tutoriel sur la longueur des tableaux PHP',
	'subheading' => 'Comment obtenir la taille d'un tableau',
	'author' => [
		'name' => 'Jonathan Bossenger',
		'twitter' => 'jon_bossenger',
	]
];
echo count($post_data);
```

Croyez-le ou non, dans cet exemple, `count($post_data)` retournera également 3. Cela est dû au fait que, par défaut, la fonction `count()` ne compte que les éléments de tableau de premier niveau.

Si vous regardez la [définition de la fonction](https://www.php.net/manual/en/function.count.php), vous verrez qu'elle accepte deux arguments – le tableau à compter et un entier `mode`. La valeur par défaut de ce mode est la constante prédéfinie `COUNT_NORMAL`, qui indique à la fonction de ne compter que les éléments de tableau de premier niveau.

Si nous passons la constante prédéfinie `COUNT_RECURSIVE` à la place, elle parcourra tous les niveaux d'imbrication et les comptera.

```
$post_data = [
	'heading' => 'Tutoriel sur la longueur des tableaux PHP',
	'subheading' => 'Comment obtenir la taille d'un tableau',
	'author' => [
		'name' => 'Jonathan Bossenger',
		'twitter' => 'jon_bossenger',
	]
];
echo count($post_data, COUNT_RECURSIVE);
```

Maintenant, le résultat de `count($post_data, COUNT_RECURSIVE)` sera, comme prévu, 5.

"Mais attendez !", je vous entends crier. "Vous avez mentionné qu'il y avait une autre méthode ?".

Eh bien oui, l'autre fonction que vous pouvez utiliser est [sizeof()](https://www.php.net/manual/en/function.sizeof.php). Cependant, `sizeof()` n'est qu'un alias de `count()`, et beaucoup de gens supposent (à juste titre) que `sizeof()` retournerait l'utilisation de la mémoire d'un tableau. 

Il est donc préférable de rester avec `count()`, qui est un nom beaucoup plus adapté à ce que vous faites – compter les éléments d'un tableau.

Merci d'avoir lu ! J'espère que vous avez maintenant une meilleure compréhension de la manière de trouver la taille d'un tableau en PHP.