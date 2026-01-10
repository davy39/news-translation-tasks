---
title: Apprendre la syntaxe PHP, les commentaires, les variables et les types de données
  – avec des exemples
subtitle: ''
author: Okoro Emmanuel Nzube
co_authors: []
series: null
date: '2022-06-10T20:18:35.000Z'
originalURL: https://freecodecamp.org/news/php-syntax-comments-variables-data-types-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/PHP--SYNTAX--COMMENTS-1.png
tags:
- name: PHP
  slug: php
seo_title: Apprendre la syntaxe PHP, les commentaires, les variables et les types
  de données – avec des exemples
seo_desc: 'Welcome to today''s tutorial, everyone. In my last article, I walked you
  through what PHP is and how to get it set up along with XAMPP.

  And today, we''ll review those introductory PHP concepts and then dive into the
  language a bit more in depth. We''ll ...'
---

Bienvenue dans le tutoriel d'aujourd'hui, tout le monde. [Dans mon dernier article](https://www.freecodecamp.org/news/how-to-get-started-with-php/), je vous ai expliqué ce qu'est PHP et comment l'installer avec XAMPP.

Et aujourd'hui, nous allons passer en revue ces concepts introductifs de PHP, puis plonger un peu plus en profondeur dans le langage. Nous examinerons la syntaxe PHP, les commentaires, les types de données et les variables, entre autres.

## Installation de PHP

Voici un bref aperçu de la manière d'installer et de faire fonctionner PHP dans votre projet.

Allez sur le [site web de PHP](https://www.php.net/), cliquez sur télécharger dans la barre de navigation en haut, faites défiler jusqu'à ce que vous voyiez Windows Downloads, et cliquez dessus.

Lorsque vous cliquez sur Windows Download, une nouvelle page devrait s'afficher. Faites simplement défiler jusqu'à ce que vous voyiez VS16 x64 Thread Safe (2022-Jun-07 22:31:20), puis cliquez sur le fichier zip pour télécharger PHP.

Lorsque le téléchargement est terminé, allez dans le dossier de téléchargements de votre ordinateur, extrayez le dossier PHP du fichier zip, ouvrez le dossier PHP extrait, faites un clic droit sur php.exe, et choisissez exécuter en tant qu'administrateur.

[Vous pouvez lire plus ici](https://www.freecodecamp.org/news/how-to-get-started-with-php/) pour une description détaillée de la manière d'installer PHP pour votre code.

## Syntaxe PHP

Vous pouvez intégrer du code PHP n'importe où dans un document. Il commence avec une balise d'ouverture `<?php (le code PHP va ici)` et se termine avec une balise de fermeture `?>`.

Toutes les instructions PHP se terminent par un point-virgule `;`. Un fichier PHP est toujours nommé avec l'extension de fichier `.php` – par exemple, `index.php` ou `home.php`.

Le code PHP contient généralement du code HTML à l'intérieur, par exemple :

```php
<?php
	echo "<h1> AU REVOIR MONDE, À LA PROCHAINE </h1>";
	echo "<p> C'est moi qui quitte le site à ce moment de la journée </p>";
?>
```

D'après le code ci-dessus, nous pouvons voir que notre code PHP contient deux lignes de code HTML – la balise `h1` et la balise `p`. La balise `h1` (titre 1) sera affichée dans un format très grand et gras, tandis que la balise `p` (paragraphe) sera affichée normalement dans le navigateur. Notez que tout le code ci-dessus se termine par un point-virgule `;`.

## Commentaires en PHP

En tant que développeur, les commentaires sont cruciaux. Ajouter des commentaires à votre code le rend plus facile à lire et à comprendre.

Dans certains cas, vous devrez peut-être revenir à un code que vous avez écrit précédemment, mais vous aurez du mal à résoudre le problème si vous n'avez pas expliqué ce que vous faisiez avec des commentaires.

Lorsque vous commentez quelque chose, cela n'apparaîtra pas dans le navigateur web. En PHP, vous pouvez écrire des commentaires sur une seule ligne et des commentaires sur plusieurs lignes.

### Comment écrire des commentaires sur une seule ligne en PHP

Comme le nom l'indique, un commentaire sur une seule ligne commente simplement tout ce qui se trouve sur une ligne. Vous pouvez utiliser la barre oblique (`/`) ou le symbole dièse (`#`) en PHP pour désigner un commentaire sur une seule ligne. Par exemple :

```php
<?php
//Ceci est un titre PHP 1 
echo "<h1> Titre PHP 1</h1>";

#Ceci est un titre PHP 2
echo "<h1> Titre PHP 2</h1>";
?>
```

Le code ci-dessus montre les deux façons d'exécuter un commentaire sur une seule ligne en PHP.

### Comment écrire des commentaires sur plusieurs lignes en PHP

Cela commente tout ce qui se trouve sur plusieurs lignes. Vous pouvez utiliser le symbole `/* (le commentaire va entre les deux)` */` pour inclure un commentaire sur plusieurs lignes.

Lorsque vous commentez plusieurs lignes de code, elles ne seront pas affichées dans le navigateur web. Par exemple :

```php
<?php
	/*Ceci est un titre PHP
	la balise h1 affiche le texte en très gras et grand, et la balise p ci-dessous est la balise de paragraphe et sera affichée sous le titre.
	*/
	echo "<h1> Titre PHP</h1>";
	echo "<p> Ceci est le paragraphe </p>";
?>
```

Le commentaire sur plusieurs lignes que vous pouvez voir dans le code ci-dessus peut être dit avoir deux balises : l'une est la balise d'ouverture qui est `/*` et l'autre est la balise de fermeture `*/`. Votre texte/commentaire de code va entre les deux balises.

## Variables en PHP

Une variable est un conteneur qui stocke ou contient des données ou des valeurs. En PHP, vous créez une variable avec le symbole dollar `$` suivi du nom de la variable.

Pour qu'une variable soit assignée à une valeur, nous utilisons le symbole `=`. Voici quelques points importants à noter sur les variables PHP :

* Une variable est déclarée/exécutée avec un symbole dollar `$` puis le nom de la variable.

* Les noms de variables sont sensibles à la casse. Par exemple, `$Derek` est très différent de `$DEREK`.

* Un nom de variable ne doit pas et ne peut pas commencer par un nombre, mais plutôt par une lettre (Aa – Zz) ou un trait de soulignement (`_`).

Voici quelques exemples de nommage de variables en PHP :

```php
<?php
	$color = "red";
	echo "$color"; //CE CODE AFFICHE LA COULEUR ROUGE DANS LE NAVIGATEUR WEB
	echo "</br>";

	$COLOR = "Blue";
	echo "$COLOR"; //CE CODE AFFICHE LA COULEUR BLEUE DANS LE NAVIGATEUR WEB
	echo "</br>";

	$_price = "1000";
	echo "$_price"; //CE CODE AFFICHE LE PRIX 1000 DANS LE NAVIGATEUR WEB
	echo "</br>";

	$_PRICE = "900";
	echo "$_PRICE"; //CE CODE AFFICHE LE PRIX 900 DANS LE NAVIGATEUR WEB
?>
```

Le code ci-dessus montre les différentes façons de nommer les variables en PHP.

## Types de données en PHP

Les variables en PHP stockent des valeurs de différents types de données. Maintenant, discutons de quelques types de données qui fonctionnent avec PHP :

* `String`

* `Integer`

* `Float`

* `Boolean`

### Type de données String

Une chaîne de caractères est un type de données qui est représenté avec du texte à l'intérieur de guillemets doubles `" "`. Une chaîne de caractères peut également contenir des nombres et des caractères spéciaux, mais ils doivent être enfermés dans les guillemets. Par exemple :

```php
<?php
	$name = "Derek Emmmanel";
	echo "$name";

    echo "<br>";

	$price = "1234567";
	Echo "$price";
?>
```

D'après le code ci-dessus, les valeurs des variables `"Derek Emmanuel"` et `"1234567"` sont du type de données `string` parce qu'elles sont enfermées dans des guillemets.

Nous pouvons utiliser une autre méthode pour exécuter le code ci-dessus dans notre navigateur web. Par exemple :

```php
<?php
$name = "Derek Emmmanel";
var_dump($name);
?>
```

Dans le code ci-dessus, j'ai utilisé le mot-clé `var_dump` pour exécuter mon code PHP. `Var_dump` non seulement affiche votre code dans votre navigateur web, mais vous aide également à identifier le type de données avec lequel vous travaillez et combien de valeurs il contient.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/localhost_Demo_test.php---Google-Chrome-6_8_2022-7_49_26-AM.png align="left")

*mot-clé var_dump*

### Type de données Integer

Les entiers sont des nombres entiers qui n'ont pas de point décimal. Les entiers peuvent être des nombres négatifs (-34567) ou des nombres positifs (34567). Par exemple :

```php
<?php
	$ad = 12345;
	var_dump($ad);
?>
```

Le code ci-dessus est un exemple du type de données entier.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/localhost_Demo_test.php---Google-Chrome-6_8_2022-8_36_54-AM.png align="left")

### Type de données Float

Les floats ne sont pas des nombres entiers, mais plutôt des nombres avec des points décimaux. Les floats peuvent également être des nombres décimaux négatifs (-34.567) ou des nombres décimaux positifs (34.567). Par exemple :

```python
<?php
	$fl = 34.567;
	var_dump($fl);
?>
```

### Type de données Boolean

Le booléen est un type de données qui représente deux résultats possibles, `true` ou `false`. Les booléens sont principalement utilisés lorsque nous travaillons avec des instructions conditionnelles comme `if`, `else`, `elseif`, et `switch`. Par exemple :

```php
$house = true;
$city = false;
```

## Conclusion

J'espère que vous avez beaucoup appris du tutoriel d'aujourd'hui. Restez à l'écoute pour notre prochain sujet.

Bon codage !