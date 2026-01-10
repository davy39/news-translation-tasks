---
title: Le manuel PHP – Apprendre PHP pour débutants
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2022-07-07T16:35:35.000Z'
originalURL: https://freecodecamp.org/news/the-php-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/Group-13--2-.png
tags:
- name: PHP
  slug: php
- name: Web Development
  slug: web-development
seo_title: Le manuel PHP – Apprendre PHP pour débutants
seo_desc: 'PHP is an incredibly popular programming language.

  Statistics say it’s used by 80% of all websites. It’s the language that powers WordPress,
  the widely used content management system for websites.

  And it also powers a lot of different frameworks that...'
---

PHP est un langage de programmation incroyablement populaire.

Les statistiques disent qu'il est utilisé par 80 % de tous les sites web. C'est le langage qui alimente WordPress, le système de gestion de contenu largement utilisé pour les sites web.

Et il alimente également de nombreux frameworks différents qui rendent le développement web plus facile, comme Laravel. À propos de Laravel, il peut être l'une des raisons les plus convaincantes d'apprendre PHP de nos jours.

## Pourquoi apprendre PHP ?

PHP est un langage assez polarisant. Certaines personnes l'adorent, et d'autres le détestent. Si nous faisons un pas au-dessus des émotions et que nous regardons le langage comme un outil, PHP a beaucoup à offrir.

Bien sûr, il n'est pas parfait. Mais laissez-moi vous dire – aucun langage ne l'est.

Dans ce manuel, je vais vous aider à apprendre PHP.

Ce livre est une introduction parfaite si vous êtes nouveau dans le langage. Il est également parfait si vous avez fait "un peu de PHP" dans le passé et que vous souhaitez y revenir.

Je vais expliquer PHP moderne, version 8+.

PHP a beaucoup évolué ces dernières années. Donc si la dernière fois que vous l'avez essayé, c'était PHP 5 ou même PHP 4, vous serez surpris par toutes les bonnes choses que PHP offre maintenant.

C'est parti !

Voici ce que nous allons couvrir dans ce manuel :

1. [Introduction à PHP](#heading-introduction-a-php)
2. [Quel type de langage est PHP ?](#heading-quel-type-de-langage-est-php)
3. [Comment installer PHP](#heading-comment-installer-php)
4. [Comment coder votre premier programme PHP](#heading-comment-coder-votre-premier-programme-php)
5. [Les bases du langage PHP](#heading-les-bases-du-langage-php)
6. [Comment travailler avec les chaînes de caractères en PHP](#heading-comment-travailler-avec-les-chaines-de-caracteres-en-php)
7. [Comment utiliser les fonctions intégrées pour les nombres en PHP](#heading-comment-utiliser-les-fonctions-integrees-pour-les-nombres-en-php)
8. [Comment fonctionnent les tableaux en PHP](#heading-comment-fonctionnent-les-tableaux-en-php)
9. [Comment fonctionnent les conditionnelles en PHP](#heading-comment-fonctionnent-les-conditionnelles-en-php)
10. [Comment fonctionnent les boucles en PHP](#heading-comment-fonctionnent-les-boucles-en-php)
11. [Comment fonctionnent les fonctions en PHP](#heading-comment-fonctionnent-les-fonctions-en-php)
12. [Comment parcourir les tableaux avec `map()`, `filter()`, et `reduce()` en PHP](#id="comment-parcourir-les-tableaux-avec-map-filter-et-reduce-en-php")
13. [La programmation orientée objet en PHP](#heading-la-programmation-orientee-objet-en-php)
14. [Comment inclure d'autres fichiers PHP](#heading-comment-inclure-d-autres-fichiers-php)
15. [Constantes, fonctions et variables utiles pour le système de fichiers en PHP](#heading-constantes-fonctions-et-variables-utiles-pour-le-systeme-de-fichiers-en-php)
16. [Comment gérer les erreurs en PHP](#heading-comment-gerer-les-erreurs-en-php)
17. [Comment gérer les exceptions en PHP](#heading-comment-gerer-les-exceptions-en-php)
18. [Comment travailler avec les dates en PHP](#heading-comment-travailler-avec-les-dates-en-php)
19. [Comment utiliser les constantes et les énumérations en PHP](#heading-comment-utiliser-les-constantes-et-les-enumerations-en-php)
20. [Comment utiliser PHP comme plateforme de développement d'applications web](#heading-comment-utiliser-php-comme-plateforme-de-developpement-d-applications-web)
21. [Comment utiliser Composer et Packagist](#heading-comment-utiliser-composer-et-packagist)
22. [Comment déployer une application PHP](#heading-comment-deployer-une-application-php)
23. [Conclusion](#heading-conclusion)

Notez que vous pouvez obtenir une version [PDF, ePub, ou Mobi](https://thevalleyofcode.com/download/php/) de ce manuel pour une référence plus facile, ou pour lire sur votre Kindle ou tablette.

## Introduction à PHP

PHP est un langage de programmation que de nombreux développeurs utilisent pour créer des applications web, entre autres.

En tant que langage, il a eu des débuts modestes. Il a été créé pour la première fois en 1994 par Rasmus Lerdorf pour construire son site web personnel. Il ne savait pas à l'époque qu'il deviendrait finalement l'un des langages de programmation les plus populaires au monde. Il est devenu populaire plus tard, en 1997/8, et a explosé dans les années 2000 lorsque PHP 4 est arrivé.

Vous pouvez utiliser PHP pour ajouter un peu d'interactivité à une page HTML.

Ou vous pouvez l'utiliser comme moteur d'application web qui crée des pages HTML dynamiquement et les envoie au navigateur.

Il peut évoluer pour des millions de vues de pages.

Saviez-vous que Facebook est alimenté par PHP ? Avez-vous déjà entendu parler de Wikipedia ? Slack ? Etsy ?

## Quel type de langage est PHP ?

Plongeons dans un peu de jargon technique.

Les langages de programmation sont divisés en groupes en fonction de leurs caractéristiques. Par exemple, interprétés/compilés, typés fortement/faiblement, typés dynamiquement/statiquement.

PHP est souvent appelé un "langage de script" et c'est un **langage interprété**. Si vous avez utilisé des langages compilés comme C ou Go ou Swift, la principale différence est que vous n'avez pas besoin de compiler un programme PHP avant de l'exécuter.

Ces langages sont compilés et le compilateur génère un programme exécutable que vous exécutez ensuite. C'est un processus en 2 étapes.

L'_interpréteur_ PHP est responsable de l'interprétation des instructions écrites dans un programme PHP lorsqu'il est exécuté. C'est juste une étape. Vous dites à l'interpréteur d'exécuter le programme. C'est un flux de travail complètement différent.

PHP est un **langage à typage dynamique**. Les types de variables sont vérifiés à l'exécution, plutôt qu'avant l'exécution du code comme cela se produit pour les langages à typage statique. (Ceux-ci se trouvent également être compilés – les deux caractéristiques vont souvent de pair.)

PHP est également à typage faible. Comparé aux langages à typage fort comme Swift, Go, C ou Java, vous n'avez pas besoin de déclarer les types de vos variables.

Le fait d'être interprété et à typage faible/dynamique rendra les bugs plus difficiles à trouver avant qu'ils ne se produisent à l'exécution.

Dans les langages compilés, vous pouvez souvent attraper les erreurs au moment de la compilation, ce qui ne se produit pas dans les langages interprétés.

Mais d'un autre côté, un langage interprété offre plus de flexibilité.

Fait amusant : PHP est écrit en interne en C, un langage compilé et à typage statique.

Dans sa nature, PHP est similaire à JavaScript, un autre langage à typage dynamique, à typage faible et interprété.

PHP supporte la programmation orientée objet, ainsi que la programmation fonctionnelle. Vous pouvez l'utiliser comme vous préférez.

## Comment installer PHP

Il existe de nombreuses façons d'installer PHP sur votre machine locale.

La manière la plus pratique que j'ai trouvée pour installer PHP localement est d'utiliser MAMP.

MAMP est un outil qui est disponible gratuitement pour tous les systèmes d'exploitation – Mac, Windows et Linux. C'est un package qui vous donne tous les outils dont vous avez besoin pour démarrer.

PHP est exécuté par un serveur HTTP, qui est responsable de la réponse aux requêtes HTTP, celles faites par le navigateur. Vous accédez donc à une URL avec votre navigateur, Chrome ou Firefox ou Safari, et le serveur HTTP répond avec un contenu HTML.

Le serveur est généralement Apache ou NGINX.

Ensuite, pour faire quoi que ce soit de non trivial, vous aurez besoin d'une base de données, comme MySQL.

MAMP est un package qui fournit tout cela, et plus encore, et vous donne une interface agréable pour démarrer/arrêter tout en une seule fois.

Bien sûr, vous pouvez configurer chaque pièce individuellement si vous le souhaitez, et de nombreux tutoriels expliquent comment faire cela. Mais j'aime les outils simples et pratiques, et MAMP en est un.

Vous pouvez suivre ce manuel avec n'importe quelle méthode d'installation de PHP, pas seulement MAMP.

Cela dit, si vous n'avez pas encore installé PHP et que vous souhaitez utiliser MAMP, allez sur [https://www.mamp.info](https://www.mamp.info/) et installez-le.

Le processus dépendra de votre système d'exploitation, mais une fois que vous aurez terminé l'installation, vous aurez une application "MAMP" installée.

Démarrez celle-ci, et vous verrez une fenêtre similaire à celle-ci :

![Screen Shot 2022-06-24 at 15.14.05.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-24_at_15.14.05.jpg)

Assurez-vous que la version de PHP sélectionnée est la plus récente disponible.

Au moment de l'écriture, MAMP vous permet de choisir la version 8.0.8.

NOTE : J'ai remarqué que MAMP a une version qui est un peu en retard, pas la plus récente. Vous pouvez installer une version plus récente de PHP en activant la démo de MAMP PRO, puis installer la dernière version à partir des paramètres de MAMP PRO (dans mon cas, c'était la 8.1.0). Ensuite, fermez-le et rouvrez MAMP (version non-pro). MAMP PRO a plus de fonctionnalités, donc vous pourriez vouloir l'utiliser, mais ce n'est pas nécessaire pour suivre ce manuel.

Appuyez sur le bouton Démarrer en haut à droite. Cela démarrera le serveur HTTP Apache, avec PHP activé, et la base de données MySQL.

Allez à l'URL [http://localhost:8888](http://localhost:8888/) et vous verrez une page similaire à celle-ci :

![Screen Shot 2022-06-24 at 15.19.05.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-24_at_15.19.05.jpg)

Nous sommes prêts à écrire un peu de PHP !

Ouvrez le dossier listé comme "Document root". Si vous utilisez MAMP sur un Mac, il est par défaut `/Applications/MAMP/htdocs`.

Sur Windows, il est `C:\MAMP\htdocs`.

Le vôtre peut être différent selon votre configuration. En utilisant MAMP, vous pouvez le trouver dans l'interface utilisateur de l'application.

Dans ce dossier, vous trouverez un fichier nommé `index.php`.

Celui-ci est responsable de l'impression de la page montrée ci-dessus.

![Screen Shot 2022-06-24 at 15.17.58.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-24_at_15.17.58.jpg)

## Comment coder votre premier programme PHP

Lorsque l'on apprend un nouveau langage de programmation, nous avons cette tradition de créer une application "Hello, World !". Quelque chose qui imprime ces chaînes.

Assurez-vous que MAMP est en cours d'exécution, et ouvrez le dossier `htdocs` comme expliqué ci-dessus.

Ouvrez le fichier `index.php` dans un éditeur de code.

Je recommande d'utiliser [VS Code](https://code.visualstudio.com), car c'est un éditeur de code très simple et puissant. Vous pouvez consulter [https://flaviocopes.com/vscode/](https://flaviocopes.com/vscode/) pour une introduction.

![Screen Shot 2022-06-24 at 15.37.36.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-24_at_15.37.36.jpg)

C'est le code qui génère la page "Bienvenue sur MAMP" que vous avez vue dans le navigateur.

Supprimez tout et remplacez-le par :

```php
<?php
echo 'Hello World';
?>

```

Enregistrez, actualisez la page sur [http://localhost:8888](http://localhost:8888), vous devriez voir ceci :

![Screen Shot 2022-06-24 at 15.39.00.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-24_at_15.39.00.jpg)

Génial ! C'était votre premier programme PHP.

Expliquons ce qui se passe ici.

Nous avons le serveur HTTP Apache qui écoute sur le port `8888` sur localhost, votre ordinateur.

Lorsque nous accédons à [http://localhost:8888](http://localhost:8888) avec le navigateur, nous faisons une requête HTTP, demandant le contenu de la route `/`, l'URL de base.

Apache, par défaut, est configuré pour servir cette route en servant le fichier `index.html` inclus dans le dossier `htdocs`. Ce fichier n'existe pas – mais comme nous avons configuré Apache pour travailler avec PHP, il recherchera alors un fichier `index.php`.

Ce fichier existe, et le code PHP est exécuté côté serveur avant qu'Apache ne renvoie la page au navigateur.

Dans le fichier PHP, nous avons une ouverture `<?php`, qui dit « ici commence un peu de code PHP ».

Nous avons une fermeture `?>` qui ferme le snippet de code PHP, et à l'intérieur, nous utilisons l'instruction `echo` pour imprimer la chaîne enfermée entre guillemets dans le HTML.

Un point-virgule est requis à la fin de chaque instruction.

Nous avons cette structure d'ouverture/fermeture car nous pouvons intégrer PHP dans HTML. PHP est un langage de script, et son objectif est de pouvoir « décorer » une page HTML avec des données dynamiques.

Notez qu'avec PHP moderne, nous évitons généralement de mélanger PHP dans le HTML. Au lieu de cela, nous utilisons PHP comme un « framework pour générer le HTML » – par exemple en utilisant des outils comme Laravel. Mais nous discuterons du _PHP pur_ dans ce livre, donc il est logique de commencer par les bases.

Par exemple, quelque chose comme ceci vous donnera le même résultat dans le navigateur :

```php
Hello
<?php
echo 'World';
?>

```

Pour l'utilisateur final, qui regarde le navigateur et n'a aucune idée du code derrière la scène, il n'y a absolument aucune différence.

La page est techniquement une page HTML, même si elle ne contient pas de balises HTML mais juste une chaîne `Hello World`. Mais le navigateur peut comprendre comment afficher cela dans la fenêtre.

## Les bases du langage PHP

Après le premier « Hello World », il est temps de plonger dans les fonctionnalités du langage avec plus de détails.

### Comment fonctionnent les variables en PHP

Les variables en PHP commencent par le signe dollar `$`, suivi d'un identifiant, qui est un ensemble de caractères alphanumériques et le caractère de soulignement `_`.

Vous pouvez assigner à une variable n'importe quel type de valeur, comme des chaînes (définies en utilisant des guillemets simples ou doubles) :

```php
$name = 'Flavio';

$name = "Flavio";

```

Ou des nombres :

```php
$age = 20;

```

ou tout autre type que PHP permet, comme nous le verrons plus tard.

Une fois qu'une variable est assignée à une valeur, par exemple une chaîne, nous pouvons la réassigner à un type de valeur différent, comme un nombre :

```php
$name = 3;

```

PHP ne se plaindra pas que maintenant le type est différent.

Les noms de variables sont sensibles à la casse. `$name` est différent de `$Name`.

Ce n'est pas une règle stricte, mais généralement les noms de variables sont écrits en format camelCase, comme ceci : `$brandOfCar` ou `$ageOfDog`. Nous gardons la première lettre en minuscule, et les lettres des mots suivants en majuscules.

### Comment écrire des commentaires en PHP

Une partie très importante de tout langage de programmation est la manière d'écrire des commentaires.

Vous écrivez des commentaires sur une seule ligne en PHP de cette manière :

```php
// commentaire sur une seule ligne

```

Les commentaires sur plusieurs lignes sont définis de cette manière :

```php
/*

ceci est un commentaire

*/

//ou

/*
 *
 * ceci est un commentaire
 *
 */

//ou pour commenter une portion de code à l'intérieur d'une ligne :

/* ceci est un commentaire */

```

### Quels sont les types en PHP ?

J'ai mentionné les chaînes et les nombres.

PHP a les types suivants :

* `bool` valeurs booléennes (vrai/faux)
* `int` nombres entiers (sans décimales)
* `float` nombres à virgule flottante (décimaux)
* `string` chaînes
* `array` tableaux
* `object` objets
* `null` une valeur qui signifie « aucune valeur assignée »

et quelques autres plus avancés.

### Comment imprimer la valeur d'une variable en PHP

Nous pouvons utiliser la fonction intégrée `var_dump()` pour obtenir la valeur d'une variable :

```php
$name = 'Flavio';

var_dump($name);

```

L'instruction `var_dump($name)` imprimera `string(6) "Flavio"` sur la page, ce qui nous indique que la variable est une chaîne de 6 caractères.

Si nous utilisions ce code :

```php
$age = 20;

var_dump($age);

```

nous aurions `int(20)` en retour, indiquant que la valeur est 20 et qu'il s'agit d'un entier.

`var_dump()` est l'un des outils essentiels dans votre boîte à outils de débogage PHP.

### Comment fonctionnent les opérateurs en PHP

Une fois que vous avez quelques variables, vous pouvez effectuer des opérations avec elles :

```php
$base = 20;
$height = 10;

$area = $base * $height;

```

Le `*` que j'ai utilisé pour multiplier $base par $height est l'opérateur de multiplication.

Nous avons plusieurs opérateurs – faisons donc un rapide tour d'horizon des principaux.

Pour commencer, voici les opérateurs arithmétiques : `+`, `-`, `*`, `/` (division), `%` (reste) et `**` (exponentiel).

Nous avons l'opérateur d'assignation `=`, que nous avons déjà utilisé pour assigner une valeur à une variable.

Ensuite, nous avons les opérateurs de comparaison, comme `<`, `>`, `<=`, `>=`. Ceux-ci fonctionnent comme en mathématiques.

```php
2 < 1; //faux
1 <= 1; // vrai
1 <= 2; // vrai

```

`==` retourne vrai si les deux opérandes sont égaux.

`===` retourne vrai si les deux opérandes sont identiques.

Quelle est la différence ?

Vous la trouverez avec l'expérience, mais par exemple :

```php
1 == '1'; //vrai
1 === '1'; //faux

```

Nous avons également `!=` pour détecter si les opérandes ne sont pas égaux :

```php
1 != 1; //faux
1 != '1'; //faux
1 != 2; //vrai

//indice : <> fonctionne de la même manière que !=, 1 <> 1

```

et `!==` pour détecter si les opérandes ne sont pas identiques :

```php
1 !== 1; //faux
1 !== '1'; //vrai

```

Les opérateurs logiques fonctionnent avec des valeurs booléennes :

```php
// ET logique avec && ou "and"

true && true; //vrai
true && false; //faux
false && true; //faux
false && false; //faux

true and true; //vrai
true and false; //faux
false and true; //faux
false and false; //faux

// OU logique avec || ou "or"

true || true; // vrai
true || false //vrai
false || true //vrai
false || false //faux

true or true; // vrai
true or false //vrai
false or true //vrai
false or false //faux

// OU exclusif logique (l'un des deux est vrai, mais pas les deux)

true xor true; // faux
true xor false //vrai
false xor true //vrai
false xor false //faux

```

Nous avons également l'opérateur _not_ :

```php
$test = true

!$test //faux

```

J'ai utilisé les valeurs booléennes `true` et `false` ici, mais en pratique vous utiliserez des expressions qui évaluent à vrai ou faux, par exemple :

```php
1 > 2 || 2 > 1; //vrai

1 !== 2 && 2 > 2; //faux

```

Tous les opérateurs listés ci-dessus sont _binaires_, ce qui signifie qu'ils impliquent 2 opérandes.

PHP a également 2 opérateurs unaires : `++` et `--` :

```php
$age = 20;
$age++;
//age est maintenant 21

$age--;
//age est maintenant 20

```

## Comment travailler avec les chaînes de caractères en PHP

J'ai introduit l'utilisation des chaînes de caractères auparavant lorsque nous avons parlé des variables et que nous avons défini une chaîne en utilisant cette notation :

```php
$name = 'Flavio'; //chaîne définie avec des guillemets simples

$name = "Flavio"; //chaîne définie avec des guillemets doubles

```

La grande différence entre l'utilisation de guillemets simples et doubles est qu'avec les guillemets doubles, nous pouvons développer les variables de cette manière :

```php
$test = 'un exemple';

$example = "Ceci est $test"; //Ceci est un exemple

```

et avec les guillemets doubles, nous pouvons utiliser des _caractères d'échappement_ (pensez aux nouvelles lignes `\n` ou aux tabulations `\t`) :

```php
$example = "Ceci est une ligne\nCeci est une ligne";

/*
la sortie est :

Ceci est une ligne
Ceci est une ligne
*/

```

PHP vous offre une bibliothèque standard très complète (la bibliothèque de fonctionnalités que le langage offre par défaut).

Tout d'abord, nous pouvons concaténer deux chaînes en utilisant l'opérateur `.` :

```php
$firstName = 'Flavio';
$lastName = 'Copes';

$fullName = $firstName . ' ' . $lastName;

```

Nous pouvons vérifier la longueur d'une chaîne en utilisant la fonction `strlen()` :

```php
$name = 'Flavio';
strlen($name); //6

```

C'est la première fois que nous utilisons une fonction.

Une fonction est composée d'un identifiant (`strlen` dans ce cas) suivi de parenthèses. À l'intérieur de ces parenthèses, nous passons un ou plusieurs arguments à la fonction. Dans ce cas, nous avons un argument.

La fonction fait _quelque chose_ et lorsqu'elle a terminé, elle peut retourner une valeur. Dans ce cas, elle retourne le nombre `6`. Si aucune valeur n'est retournée, la fonction retourne `null`.

Nous verrons plus tard comment définir nos propres fonctions.

Nous pouvons obtenir une portion d'une chaîne en utilisant `substr()` :

```php
$name = 'Flavio';
substr($name, 3); //"vio" - commence à la position 3, prend tout le reste
substr($name, 2, 2); //"av" - commence à la position 2, prend 2 éléments

```

Nous pouvons remplacer une portion d'une chaîne en utilisant `str_replace()` :

```php
$name = 'Flavio';
str_replace('avio', 'ower', $name); //"Flower"

```

Bien sûr, nous pouvons assigner le résultat à une nouvelle variable :

```php
$name = 'Flavio';
$itemObserved = str_replace('avio', 'ower', $name); //"Flower"

```

Il existe beaucoup d'autres fonctions intégrées que vous pouvez utiliser pour travailler avec les chaînes.

Voici une liste non exhaustive juste pour vous montrer les possibilités :

* [`trim()`](https://www.php.net/manual/en/function.trim.php) supprime les espaces blancs au début et à la fin d'une chaîne
* [`strtoupper()`](https://www.php.net/manual/en/function.strtoupper.php) met une chaîne en majuscules
* [`strtolower()`](https://www.php.net/manual/en/function.strtolower.php) met une chaîne en minuscules
* [`ucfirst()`](https://www.php.net/manual/en/function.ucfirst.php) met le premier caractère en majuscule
* [`strpos()`](https://www.php.net/manual/en/function.strpos.php) trouve la première occurrence d'une sous-chaîne dans la chaîne
* [`explode()`](https://www.php.net/manual/en/function.explode.php) pour diviser une chaîne en un tableau
* [`implode()`](https://www.php.net/manual/en/function.implode.php) pour joindre les éléments d'un tableau dans une chaîne

Vous pouvez trouver une liste complète [ici](https://www.php.net/manual/en/book.strings.php).

## Comment utiliser les fonctions intégrées pour les nombres en PHP

J'ai précédemment listé les quelques fonctions que nous utilisons couramment pour les chaînes.

Faisons une liste des fonctions que nous utilisons avec les nombres :

* [`round()`](https://www.php.net/manual/en/function.round.php) pour arrondir un nombre décimal, vers le haut/bas selon si la valeur est > 0,5 ou plus petite
* [`ceil()`](https://www.php.net/manual/en/function.ceil.php) pour arrondir un nombre décimal vers le haut
* [`floor()`](https://www.php.net/manual/en/function.floor.php) pour arrondir un nombre décimal vers le bas
* [`rand()`](https://www.php.net/manual/en/function.rand.php) génère un entier aléatoire
* [`min()`](https://www.php.net/manual/en/function.min.php) trouve le nombre le plus bas parmi les nombres passés en arguments
* [`max()`](https://www.php.net/manual/en/function.max.php) trouve le nombre le plus élevé parmi les nombres passés en arguments
* [`is_nan()`](https://www.php.net/manual/en/function.is-nan.php) retourne vrai si le nombre n'est pas un nombre

Il existe une tonne de fonctions différentes pour toutes sortes d'opérations mathématiques comme le sinus, le cosinus, les tangentes, les logarithmes, et ainsi de suite. Vous pouvez trouver une liste complète [ici](https://www.php.net/manual/en/book.math.php).

## Comment fonctionnent les tableaux en PHP

Les tableaux sont des listes de valeurs regroupées sous un nom commun.

Vous pouvez définir un tableau vide de deux manières différentes :

```php
$list = [];

$list = array();

```

Un tableau peut être initialisé avec des valeurs :

```php
$list = [1, 2];

$list = array(1, 2);

```

Les tableaux peuvent contenir des valeurs de n'importe quel type :

```php
$list = [1, 'test'];

```

Même d'autres tableaux :

```php
$list = [1, [2, 'test']];

```

Vous pouvez accéder à l'élément dans un tableau en utilisant cette notation :

```php
$list = ['a', 'b'];
$list[0]; //'a' --l'index commence à 0
$list[1]; //'b'

```

Une fois qu'un tableau est créé, vous pouvez ajouter des valeurs à la fin de celui-ci de cette manière :

```php
$list = ['a', 'b'];
$list[] = 'c';

/*
$list == [
  "a",
  "b",
  "c",
]
*/

```

Vous pouvez utiliser `array_unshift()` pour ajouter l'élément au début du tableau au lieu de la fin :

```php
$list = ['b', 'c'];
array_unshift($list, 'a');

/*
$list == [
  "a",
  "b",
  "c",
]
*/

```

Comptez combien d'éléments il y a dans un tableau en utilisant la fonction intégrée `count()` :

```php
$list = ['a', 'b'];

count($list); //2

```

Vérifiez si un tableau contient un élément en utilisant la fonction intégrée `in_array()` :

```php
$list = ['a', 'b'];

in_array('b', $list); //true

```

Si, en plus de confirmer l'existence, vous avez besoin de l'index, utilisez `array_search()` :

```php
$list = ['a', 'b'];

array_search('b', $list) //1

```

### Fonctions utiles pour les tableaux en PHP

Comme pour les chaînes et les nombres, PHP fournit de nombreuses fonctions très utiles pour les tableaux. Nous avons vu `count()`, `in_array()`, `array_search()` – voyons-en quelques autres :

* `is_array()` pour vérifier si une variable est un tableau
* `array_unique()` pour supprimer les valeurs en double d'un tableau
* `array_search()` pour rechercher une valeur dans le tableau et retourner la clé
* `array_reverse()` pour inverser un tableau
* `array_reduce()` pour réduire un tableau à une seule valeur en utilisant une fonction de rappel
* `array_map()` pour appliquer une fonction de rappel à chaque élément du tableau. Typiquement utilisé pour créer un nouveau tableau en modifiant les valeurs d'un tableau existant, sans l'altérer.
* `array_filter()` pour filtrer un tableau en une seule valeur en utilisant une fonction de rappel
* `max()` pour obtenir la valeur maximale contenue dans le tableau
* `min()` pour obtenir la valeur minimale contenue dans le tableau
* `array_rand()` pour obtenir un élément aléatoire du tableau
* `array_count_values()` pour compter toutes les valeurs dans le tableau
* `implode()` pour transformer un tableau en une chaîne
* `array_pop()` pour supprimer le dernier élément du tableau et retourner sa valeur
* `array_shift()` même que `array_pop()` mais supprime le premier élément au lieu du dernier
* `sort()` pour trier un tableau
* `rsort()` pour trier un tableau dans l'ordre inverse
* `array_walk()` de manière similaire à `array_map()` fait quelque chose pour chaque élément du tableau, mais en plus il peut changer les valeurs dans le tableau existant

### Comment utiliser les tableaux associatifs en PHP

Jusqu'à présent, nous avons utilisé des tableaux avec un index numérique incrémental : 0, 1, 2...

Vous pouvez également utiliser des tableaux avec des index nommés (clés), et nous les appelons tableaux associatifs :

```php
$list = ['first' => 'a', 'second' => 'b'];

$list['first'] //'a'
$list['second'] //'b'

```

Nous avons quelques fonctions qui sont particulièrement utiles pour les tableaux associatifs :

* `array_key_exists()` pour vérifier si une clé existe dans le tableau
* `array_keys()` pour obtenir toutes les clés du tableau
* `array_values()` pour obtenir toutes les valeurs du tableau
* `asort()` pour trier un tableau associatif par valeur
* `arsort()` pour trier un tableau associatif par ordre décroissant par valeur
* `ksort()` pour trier un tableau associatif par clé
* `krsort()` pour trier un tableau associatif par ordre décroissant par clé

Vous pouvez voir toutes les fonctions liées aux tableaux [ici](https://www.php.net/manual/en/ref.array.php).

## Comment fonctionnent les conditionnelles en PHP

J'ai précédemment introduit les opérateurs de comparaison : `<`, `>`, `<=`, `>=`, `==`, `===`, `!=`, `!==`... et ainsi de suite.

Ces opérateurs vont être super utiles pour une chose : **les conditionnelles**.

Les conditionnelles sont la première structure de contrôle que nous voyons.

Nous pouvons décider de faire quelque chose, ou autre chose, en fonction d'une comparaison.

Par exemple :

```php
$age = 17;

if ($age > 18) {
  echo 'Vous pouvez entrer dans le pub';
}

```

Le code à l'intérieur des parenthèses ne s'exécute que si la condition évalue à `true`.

Utilisez `else` pour faire quelque chose _d'autre_ au cas où la condition est `false` :

```php
$age = 17;

if ($age > 18) {
  echo 'Vous pouvez entrer dans le pub';
} else {
  echo 'Vous ne pouvez pas entrer dans le pub';
}

```

NOTE : J'ai utilisé `cannot` au lieu de `can't` parce que le guillemet simple terminerait ma chaîne avant qu'il ne le devrait. Dans ce cas, vous pourriez échapper le `'` de cette manière : `echo 'Vous ne pouvez\'t pas entrer dans le pub';`

Vous pouvez avoir plusieurs instructions `if` enchaînées en utilisant `elseif` :

```php
$age = 17;

if ($age > 20) {
  echo 'Vous avez 20+';
} elseif ($age > 18) {
  echo 'Vous avez 18+';
} else {
  echo 'Vous avez <18';
}

```

En plus de `if`, nous avons l'instruction `switch`.

Nous utilisons cela lorsque nous avons une variable qui pourrait avoir quelques valeurs différentes, et nous n'avons pas besoin d'avoir un long bloc if / elseif :

```php
$age = 17

switch($age) {
  case 15:
		echo 'Vous avez 15 ans';
    break;
  case 16:
		echo 'Vous avez 16 ans';
    break;
  case 17:
		echo 'Vous avez 17 ans';
    break;
  case 18:
		echo 'Vous avez 18 ans';
    break;
  default:
    echo "Vous avez $age";
}

```

Je sais que l'exemple n'a aucune logique, mais je pense qu'il peut vous aider à comprendre comment fonctionne `switch`.

L'instruction `break;` après chaque cas est essentielle. Si vous ne l'ajoutez pas et que l'âge est 17, vous verriez ceci :

```php
Vous avez 17 ans
Vous avez 18 ans
Vous avez 17 ans

```

Au lieu de juste ceci :

```php
Vous avez 17 ans

```

comme vous vous y attendriez.

## Comment fonctionnent les boucles en PHP

Les boucles sont une autre structure de contrôle super utile.

Nous avons quelques types de boucles différents en PHP : `while`, `do while`, `for`, et `foreach`.

Voyons-les tous !

### Comment utiliser une boucle `while` en PHP

Une boucle `while` est la plus simple. Elle continue à itérer tant que la condition évalue à `true` :

```php
while (true) {
  echo 'boucle';
}

```

Cela serait une boucle infinie, c'est pourquoi nous utilisons des variables et des comparaisons :

```php
$counter = 0;

while ($counter < 10) {
  echo $counter;
  $counter++;
}

```

### Comment utiliser une boucle `do while` en PHP

`do while` est similaire, mais légèrement différent dans la manière dont la première itération est effectuée :

```php
$counter = 0;

do {
  echo $counter;
  $counter++;
} while ($counter < 10);

```

Dans la boucle `do while`, nous effectuons d'abord la première itération, _puis_ nous vérifions la condition.

Dans la boucle `while`, _d'abord_ nous vérifions la condition, puis nous effectuons l'itération.

Faites un simple test en définissant `$counter` à 15 dans les exemples ci-dessus, et voyez ce qui se passe.

Vous voudrez choisir un type de boucle, ou l'autre, en fonction de votre cas d'utilisation.

### Comment utiliser une boucle `foreach` en PHP

Vous pouvez utiliser la boucle `foreach` pour itérer facilement sur un tableau :

```php
$list = ['a', 'b', 'c'];

foreach ($list as $value) {
  echo $value;
}

```

Vous pouvez également obtenir la valeur de l'index (ou clé dans un tableau associatif) de cette manière :

```php
$list = ['a', 'b', 'c'];

foreach ($list as $key => $value) {
  echo $key;
}

```

### Comment utiliser une boucle `for` en PHP

La boucle `for` est similaire à while, mais au lieu de définir la variable utilisée dans la conditionnelle avant la boucle, et au lieu d'incrémenter manuellement la variable d'index, tout est fait dans la première ligne :

```php
for ($i = 0; $i < 10; $i++) {
  echo $i;
}

//résultat : 0123456789

```

Vous pouvez utiliser la boucle for pour itérer sur un tableau de cette manière :

```php
$list = ['a', 'b', 'c'];

for ($i = 0; $i < count($list); $i++) {
  echo $list[$i];
}

//résultat : abc

```

### Comment utiliser les instructions `break` et `continue` en PHP

Dans de nombreux cas, vous voulez la possibilité d'arrêter une boucle à la demande.

Par exemple, vous voulez arrêter une boucle `for` lorsque la valeur de la variable dans le tableau est `'b'` :

```php
$list = ['a', 'b', 'c'];

for ($i = 0; $i < count($list); $i++) {
	if ($list[$i] == 'b') {
    break;
  }
  echo $list[$i];
}

//résultat : a

```

Cela fait que la boucle s'arrête complètement à ce point, et l'exécution du programme continue à l'instruction suivante après la boucle.

Si vous voulez simplement sauter l'itération actuelle de la boucle et continuer à chercher, utilisez `continue` à la place :

```php
$list = ['a', 'b', 'c'];

for ($i = 0; $i < count($list); $i++) {
	if ($list[$i] == 'b') {
    continue;
  }
  echo $list[$i];
}

//résultat : ac

```

## Comment fonctionnent les fonctions en PHP

Les fonctions sont l'un des concepts les plus importants en programmation.

Vous pouvez utiliser des fonctions pour regrouper plusieurs instructions ou plusieurs lignes de code, et leur donner un nom.

Par exemple, vous pouvez créer une fonction qui envoie un email. Appelons-la `sendEmail`, et nous la définirons comme ceci :

```php
function sendEmail() {
  //envoyer un email
}

```

Et vous pouvez l'_appeler_ n'importe où ailleurs en utilisant cette syntaxe :

```php
sendEmail();

```

Vous pouvez également passer des arguments à une fonction. Par exemple, lorsque vous envoyez un email, vous voulez l'envoyer à quelqu'un – donc vous ajoutez l'email comme premier argument :

```php
sendEmail('test@test.com');

```

À l'intérieur de la définition de la fonction, nous obtenons ce paramètre de cette manière (nous les appelons _paramètres_ à l'intérieur de la définition de la fonction, et _arguments_ lorsque nous appelons la fonction) :

```php
function sendEmail($to) {
  echo "envoyer un email à $to";
}

```

Vous pouvez envoyer plusieurs arguments en les séparant par des virgules :

```php
sendEmail('test@test.com', 'sujet', 'corps de l'email');

```

Et nous pouvons obtenir ces paramètres dans l'ordre où ils ont été définis :

```php
function sendEmail($to, $subject, $body) {
  //...
}

```

Nous pouvons **optionnellement** définir le type des paramètres :

```php
function sendEmail(string $to, string $subject, string $body) {
  //...
}

```

Les paramètres peuvent avoir une valeur par défaut, donc s'ils sont omis, nous pouvons encore avoir une valeur pour eux :

```php
function sendEmail($to, $subject = 'test', $body = 'test') {
  //...
}

sendEmail('test@test.com')

```

Une fonction peut retourner une valeur. Une seule valeur peut être retournée par une fonction, pas plus d'une. Vous faites cela en utilisant le mot-clé `return`. Si omis, la fonction retourne `null`.

La valeur retournée est super utile car elle vous indique le résultat du travail effectué dans la fonction, et vous permet d'utiliser son résultat après l'avoir appelée :

```php
function sendEmail($to) {
	return true;
}

$success = sendEmail('test@test.com');

if ($success) {
  echo 'email envoyé avec succès';
} else {
  echo 'erreur lors de l'envoi de l'email';
}

```

Nous pouvons **optionnellement** définir le type de retour d'une fonction en utilisant cette syntaxe :

```php
function sendEmail($to): bool {
	return true;
}

```

Lorsque vous définissez une variable à l'intérieur d'une fonction, cette variable est **locale** à la fonction, ce qui signifie qu'elle n'est pas visible de l'extérieur. Lorsque la fonction se termine, elle cesse simplement d'exister :

```php
function sendEmail($to) {
	$test = 'a';
}

var_dump($test); //PHP Warning:  Variable non définie $test

```

Les variables définies à l'extérieur de la fonction ne sont **pas** accessibles à l'intérieur de la fonction.

Cela impose une bonne pratique de programmation car nous pouvons être sûrs que la fonction ne modifie pas les variables externes et ne cause pas d'effets secondaires.

Au lieu de cela, vous retournez une valeur de la fonction, et le code externe qui appelle la fonction sera responsable de la mise à jour de la variable externe.

Comme ceci :

```php
$character = 'a';

function test() {
  return 'b';
}

$character = test();

```

Vous pouvez passer la valeur d'une variable en la passant comme argument à la fonction :

```php
$character = 'a';

function test($c) {
  echo $c;
}

test($character);

```

Mais vous ne pouvez pas modifier cette valeur depuis l'intérieur de la fonction.

Elle est **passée par valeur**, ce qui signifie que la fonction reçoit une copie de celle-ci, et non la référence à la variable originale.

Cela est encore possible en utilisant cette syntaxe (remarquez que j'ai utilisé `&` dans la définition du paramètre) :

```php
$character = 'a';

function test(&$c) {
  $c = 'b';
}

test($character);

echo $character; //'b'

```

Les fonctions que nous avons définies jusqu'à présent sont des **fonctions nommées**.

Elles ont un nom.

Nous avons également des **fonctions anonymes**, qui peuvent être utiles dans de nombreux cas.

Elles n'ont pas de nom, à proprement parler, mais elles sont assignées à une variable. Pour les appeler, vous invoquez la variable avec des parenthèses à la fin :

```php
$myfunction = function() {
  //faire quelque chose ici
};

$myfunction()

```

Notez que vous avez besoin d'un point-virgule après la définition de la fonction, mais ensuite elles fonctionnent comme des fonctions nommées pour les valeurs de retour et les paramètres.

Intéressamment, elles offrent un moyen d'accéder à une variable définie à l'extérieur de la fonction via `use()` :

```php
$test = 'test';

$myfunction = function() use ($test) {
  echo $test;
  return 'ok';
};

$myfunction()

```

Un autre type de fonction est une **fonction fléchée**.

Une fonction fléchée est une fonction anonyme qui n'est qu'une expression (une ligne), et retourne implicitement la valeur de cette expression.

Vous la définissez de cette manière :

```php
fn (arguments) => expression;

```

Voici un exemple :

```php
$printTest = fn() => 'test';

$printTest(); //'test'

```

Vous pouvez passer des paramètres à une fonction fléchée :

```php
$multiply = fn($a, $b) => $a * $b;

$multiply(2, 4) //8

```

Notez que, comme le montre l'exemple suivant, les fonctions fléchées ont un accès automatique aux variables de la portée englobante, sans avoir besoin de `use()`.

```php
$a = 2;
$b = 4;

$multiply = fn() => $a * $b;

$multiply()

```

Les fonctions fléchées sont super utiles lorsque vous avez besoin de passer une fonction de rappel. Nous verrons comment les utiliser pour effectuer certaines opérations sur les tableaux plus tard.

Nous avons donc au total 3 types de fonctions : **fonctions nommées**, **fonctions anonymes**, et **fonctions fléchées**.

Chacune d'entre elles a sa place, et vous apprendrez à les utiliser correctement avec le temps, avec la pratique.

## Comment parcourir les tableaux avec `map()`, `filter()`, et `reduce()` en PHP

Un autre ensemble important de structures de boucle, souvent utilisé en programmation fonctionnelle, est l'ensemble `array_map()` / `array_filter()` / `array_reduce()`.

Ces 3 fonctions intégrées de PHP prennent un tableau et une fonction de rappel qui, à chaque itération, prend chaque élément du tableau.

`array_map()` retourne un nouveau tableau qui contient le résultat de l'exécution de la fonction de rappel sur chaque élément du tableau :

```php
$numbers = [1, 2, 3, 4];
$doubles = array_map(fn($value) => $value * 2, $numbers);

//$doubles est maintenant [2, 4, 6, 8]

```

`array_filter()` génère un nouveau tableau en ne prenant que les éléments dont la fonction de rappel retourne `true` :

```php
$numbers = [1, 2, 3, 4];
$even = array_filter($numbers, fn($value) => $value % 2 === 0)

//$even est maintenant [2, 4]

```

`array_reduce()` est utilisé pour _réduire_ un tableau à une seule valeur.

Par exemple, nous pouvons l'utiliser pour multiplier tous les éléments d'un tableau :

```php
$numbers = [1, 2, 3, 4];

$result = array_reduce($numbers, fn($carry, $value) => $carry * $value, 1)

```

Remarquez le dernier paramètre – c'est la valeur initiale. Si vous l'omettez, la valeur par défaut est `0` mais cela ne fonctionnerait pas pour notre exemple de multiplication.

Notez que dans `array_map()` l'ordre des arguments est inversé. D'abord vous avez la fonction de rappel puis le tableau. Cela est dû au fait que nous pouvons passer plusieurs tableaux en utilisant des virgules (`array_map(fn($value) => $value * 2, $numbers, $otherNumbers, $anotherArray);`). Idéalement, nous aimerions plus de cohérence, mais c'est ce que c'est.

## Programmation orientée objet en PHP

Plongeons maintenant dans un grand sujet : la programmation orientée objet avec PHP.

La programmation orientée objet vous permet de créer des abstractions utiles et de rendre votre code plus simple à comprendre et à gérer.

### Comment utiliser les classes et les objets en PHP

Pour commencer, vous avez des classes et des objets.

Une classe est un plan, ou un type, d'objet.

Par exemple, vous avez la classe `Dog`, définie de cette manière :

```php
class Dog {

}

```

Notez que la classe doit être définie en majuscules.

Ensuite, vous pouvez créer des objets à partir de cette classe – des chiens spécifiques, individuels.

Un objet est assigné à une variable, et il est instancié en utilisant la syntaxe `new Classname()` :

```php
$roger = new Dog();

```

Vous pouvez créer plusieurs objets à partir de la même classe, en assignant chaque objet à une variable différente :

```php
$roger = new Dog();
$syd = new Dog();

```

### Comment utiliser les propriétés en PHP

Ces objets partageront tous les mêmes caractéristiques définies par la classe. Mais une fois qu'ils sont instanciés, ils auront une vie propre.

Par exemple, un chien a un nom, un âge et une couleur de pelage.

Nous pouvons donc définir ces propriétés dans la classe :

```php
class Dog {
  public $name;
  public $age;
  public $color;
}

```

Elles fonctionnent comme des variables, mais elles sont attachées à l'objet, une fois qu'il est instancié à partir de la classe. Le mot-clé `public` est le _modificateur d'accès_ et définit la propriété comme étant accessible publiquement.

Vous pouvez assigner des valeurs à ces propriétés de cette manière :

```php
class Dog {
  public $name;
  public $age;
  public $color;
}

$roger = new Dog();

$roger->name = 'Roger';
$roger->age = 10;
$roger->color = 'gray';

var_dump($roger);

/*
object(Dog)#1 (3) {
  ["name"]=> string(5) "Roger"
	["age"]=> int(10)
	["color"]=> string(4) "gray"
}
*/

```

Remarquez que la propriété est définie comme `public`.

Cela s'appelle un modificateur d'accès. Vous pouvez utiliser deux autres types de modificateurs d'accès : `private` et `protected`. Private rend la propriété inaccessible depuis l'extérieur de l'objet. Seules les méthodes définies à l'intérieur de l'objet peuvent y accéder.

Nous verrons plus de détails sur protected lorsque nous parlerons d'héritage.

### Comment utiliser les méthodes en PHP

Ai-je dit méthode ? Qu'est-ce qu'une méthode ?

Une méthode est une fonction définie à l'intérieur de la classe, et elle est définie de cette manière :

```php
class Dog {
  public function bark() {
    echo 'woof!';
  }
}

```

Les méthodes sont très utiles pour attacher un comportement à un objet. Dans ce cas, nous pouvons faire aboyer un chien.

Remarquez que j'utilise le mot-clé `public`. Cela signifie que vous pouvez invoquer une méthode depuis l'extérieur de la classe. Comme pour les propriétés, vous pouvez marquer les méthodes comme `private` ou `protected`, pour restreindre leur accès.

Vous invoquez une méthode sur l'instance de l'objet comme ceci :

```php
class Dog {
  public function bark() {
    echo 'woof!';
  }
}

$roger = new Dog();

$roger->bark();

```

Une méthode, tout comme une fonction, peut définir des paramètres et une valeur de retour, également.

À l'intérieur d'une méthode, nous pouvons accéder aux propriétés de l'objet en utilisant la variable spéciale intégrée `$this`, qui, lorsqu'elle est référencée à l'intérieur d'une méthode, pointe vers l'instance actuelle de l'objet :

```php
class Dog {
  public $name;

  public function bark() {
    echo $this->name . ' a aboyé !';
  }
}

$roger = new Dog();
$roger->name = 'Roger';
$roger->bark();

```

Remarquez que j'ai utilisé `$this->name` pour définir et accéder à la propriété `$name`, et non `$this->$name`.

### Comment utiliser la méthode constructeur en PHP

Un type spécial de méthode nommé `__construct()` est appelé un **constructeur**.

```php
class Dog {
	public function __construct() {

  }
}

```

Vous utilisez cette méthode pour initialiser les propriétés d'un objet lorsque vous le créez, car elle est automatiquement invoquée lorsque vous appelez `new Classname()`.

```php
class Dog {
  public $name;

	public function __construct($name) {
		$this->name = $name;
  }

  public function bark() {
    echo $this->name . ' a aboyé !';
  }
}

$roger = new Dog('Roger');
$roger->bark();

```

C'est une chose si courante que PHP (à partir de PHP 8) inclut quelque chose appelé **promotion du constructeur** où il fait automatiquement cela :

```php
class Dog {
  public $name;

	public function __construct($name) {
		$this->name = $name;
  }

  //...

```

En utilisant le modificateur d'accès, l'assignation du paramètre du constructeur à la variable locale se fait automatiquement :

```php
class Dog {
	public function __construct(public $name) {
  }

  public function bark() {
    echo $this->name . ' a aboyé !';
  }
}

$roger = new Dog('Roger');
$roger->name; //'Roger'
$roger->bark(); //'Roger a aboyé !'

```

Les propriétés peuvent être **typées**.

Vous pouvez exiger que le nom soit une chaîne en utilisant `public string $name` :

```php
class Dog {
  public string $name;

	public function __construct($name) {
		$this->name = $name;
  }

  public function bark() {
    echo $this->name . ' a aboyé !';
  }
}

$roger = new Dog('Roger');
$roger->name; //'Roger'
$roger->bark(); //'Roger a aboyé !'

```

Tout fonctionne bien dans cet exemple, mais essayez de changer cela en `public int $name` pour exiger qu'il soit un entier.

PHP générera une erreur si vous initialisez `$name` avec une chaîne :

```
TypeError: Dog::__construct():
Argument #1 ($name) doit être de type int,
chaîne donnée à la ligne 14

```

Intéressant, n'est-ce pas ?

Nous pouvons imposer aux propriétés d'avoir un type spécifique entre `string`, `int`, `float`, `string`, `object`, `array`, `bool` et [d'autres](https://www.php.net/manual/en/language.types.declarations.php).

### Qu'est-ce que l'héritage en PHP ?

Le plaisir de la programmation orientée objet commence lorsque nous permettons aux classes d'hériter des propriétés et des méthodes d'autres classes.

Supposons que vous avez une classe `Animal` :

```php
class Animal {

}

```

Chaque animal a un âge, et chaque animal peut manger. Donc nous ajoutons une propriété `age` et une méthode `eat()` :

```php
class Animal {
  public $age;

  public function eat() {
    echo 'l'animal est en train de manger';
  }
}

```

Un chien est un animal et a un âge et peut manger aussi, donc la classe `Dog` – au lieu de réimplémenter les mêmes choses que nous avons dans `Animal` – peut étendre cette classe :

```php
class Dog extends Animal {

}

```

Nous pouvons maintenant instancier un nouvel objet de la classe `Dog` et nous avons accès aux propriétés et méthodes définies dans `Animal` :

```php
$roger = new Dog();
$roger->eat();

```

Dans ce cas, nous appelons Dog la **classe enfant** et Animal la **classe parent**.

À l'intérieur de la classe enfant, nous pouvons utiliser `$this` pour référencer n'importe quelle propriété ou méthode définie dans le parent, comme si elles étaient définies à l'intérieur de la classe enfant.

Il est intéressant de noter que bien que nous puissions accéder aux propriétés et méthodes du parent depuis l'enfant, nous ne pouvons pas faire l'inverse.

La classe parent ne sait rien de la classe enfant.

### Propriétés et méthodes `protected` en PHP

Maintenant que nous avons introduit l'héritage, nous pouvons discuter de `protected`. Nous avons déjà vu comment nous pouvons utiliser le modificateur d'accès `public` pour définir des propriétés et des méthodes appelables depuis l'extérieur d'une classe, par le _public_.

Les propriétés et méthodes `private` ne peuvent être accessibles que depuis l'intérieur de la classe.

Les propriétés et méthodes `protected` peuvent être accessibles depuis l'intérieur de la classe et depuis les classes enfants.

### Comment redéfinir les méthodes en PHP

Que se passe-t-il si nous avons une méthode `eat()` dans `Animal` et que nous voulons la personnaliser dans `Dog` ? Nous pouvons **redéfinir** cette méthode.

```php
class Animal {
  public $age;

  public function eat() {
    echo 'l'animal est en train de manger';
  }
}

class Dog extends Animal {
  public function eat() {
    echo 'le chien est en train de manger';
  }
}

```

Maintenant, toute instance de `Dog` utilisera l'implémentation de `Dog` de la méthode `eat()`.

### Propriétés et méthodes statiques en PHP

Nous avons vu comment définir des propriétés et des méthodes qui appartiennent **à l'instance d'une classe**, un objet.

Parfois, il est utile de les assigner à la classe elle-même.

Lorsque cela se produit, nous les appelons **statiques**, et pour les référencer ou les appeler, nous n'avons pas besoin de créer un objet à partir de la classe.

Commençons par les propriétés statiques. Nous les définissons avec le mot-clé `static` :

```php
class Utils {
  public static $version = '1.0';
}

```

Nous les référençons depuis l'intérieur de la classe en utilisant le mot-clé `self`, qui pointe vers la classe :

```php
self::$version;

```

et depuis l'extérieur de la classe en utilisant :

```php

Utils::version

```

C'est ce qui se passe pour les méthodes statiques :

```php
class Utils {
  public static function version() {
    return '1.0';
  }
}

```

Depuis l'extérieur de la classe, nous pouvons les appeler de cette manière :

```php
Utils::version();

```

Depuis l'intérieur de la classe, nous pouvons les référencer en utilisant le mot-clé `self`, qui fait référence à la classe actuelle :

```php
self::version();

```

### Comment comparer les objets en PHP

Lorsque nous avons parlé des opérateurs, j'ai mentionné que nous avons l'opérateur `==` pour vérifier si deux valeurs sont égales et `===` pour vérifier si elles sont identiques.

Principalement, la différence est que `==` vérifie le contenu de l'objet, par exemple la chaîne `'5'` est égale au nombre `5`, mais elle n'est pas identique à celui-ci.

Lorsque nous utilisons ces opérateurs pour comparer des objets, `==` vérifiera si les deux objets ont la même classe et ont les mêmes valeurs qui leur sont assignées.

`===` d'autre part vérifiera s'ils font également référence à la même instance (objet).

Par exemple :

```php
class Dog {
  public $name = 'Bon chien';
}

$roger = new Dog();
$syd = new Dog();

echo $roger == $syd; //vrai

echo $roger === $syd; //faux

```

### Comment itérer sur les propriétés d'un objet en PHP

Vous pouvez parcourir toutes les propriétés publiques d'un objet en utilisant une boucle `foreach`, comme ceci :

```php
class Dog {
  public $name = 'Bon chien';
  public $age = 10;
  public $color = 'gris';
}

$dog = new Dog();

foreach ($dog as $key => $value) {
  echo $key . ': ' . $value . '<br>';
}

```

### Comment cloner des objets en PHP

Lorsque vous avez un objet, vous pouvez le cloner en utilisant le mot-clé `clone` :

```php
class Dog {
  public $name;
}

$roger = new Dog();
$roger->name = 'Roger';

$syd = clone $roger;

```

Cela effectue un _clone superficiel_, ce qui signifie que les références à d'autres variables seront copiées en tant que références – il n'y aura pas de « clonage récursif » de celles-ci.

Pour effectuer un _clone profond_, vous devrez faire un peu plus de travail.

### Quelles sont les méthodes magiques en PHP ?

Les méthodes magiques sont des méthodes spéciales que nous définissons dans les classes pour effectuer un certain comportement lorsque quelque chose de spécial se produit.

Par exemple, lorsqu'une propriété est définie, ou accédée, ou lorsque l'objet est cloné.

Nous avons déjà vu `__construct()`.

C'est une méthode magique.

Il y en a d'autres. Par exemple, nous pouvons définir une propriété booléenne « clonée » à vrai lorsque l'objet est cloné :

```php
class Dog {
  public $name;

  public function __clone() {
    $this->cloned = true;
  }
}

$roger = new Dog();
$roger->name = 'Roger';

$syd = clone $roger;
echo $syd->cloned;

```

D'autres méthodes magiques incluent `__call()`, `__get()`, `__set()`, `__isset()`, `__toString()` et d'autres.

Vous pouvez voir la liste complète [ici](https://www.php.net/manual/en/language.oop5.magic.php)

## Comment inclure d'autres fichiers PHP

Nous avons maintenant terminé de parler des fonctionnalités orientées objet de PHP.

Explorons maintenant d'autres sujets intéressants !

À l'intérieur d'un fichier PHP, vous pouvez inclure d'autres fichiers PHP. Nous avons les méthodes suivantes, toutes utilisées pour ce cas d'utilisation, mais elles sont toutes légèrement différentes : `include`, `include_once`, `require`, et `require_once`.

`include` charge le contenu d'un autre fichier PHP, en utilisant un chemin relatif.

`require` fait la même chose, mais si une erreur se produit, le programme s'arrête. `include` ne générera qu'un avertissement.

Vous pouvez décider d'utiliser l'un ou l'autre en fonction de votre cas d'utilisation. Si vous voulez que votre programme se termine s'il ne peut pas importer le fichier, utilisez `require`.

`include_once` et `require_once` font la même chose que leurs fonctions correspondantes sans `_once`, mais elles s'assurent que le fichier est inclus/requis une seule fois pendant l'exécution du programme.

Cela est utile si, par exemple, vous avez plusieurs fichiers chargeant un autre fichier, et vous souhaitez généralement éviter de charger celui-ci plus d'une fois.

Ma règle générale est de ne jamais utiliser `include` ou `require` car vous pourriez charger le même fichier deux fois. `include_once` et `require_once` vous aident à éviter ce problème.

Utilisez `include_once` lorsque vous souhaitez charger un fichier de manière conditionnelle, par exemple « chargez ce fichier au lieu de celui-ci ». Dans tous les autres cas, utilisez `require_once`.

Voici un exemple :

```php
require_once('test.php');

//maintenant nous avons accès aux fonctions, classes
//et variables définies dans le fichier `test.php`

```

La syntaxe ci-dessus inclut le fichier `test.php` à partir du dossier courant, le fichier où se trouve ce code.

Vous pouvez utiliser des chemins relatifs :

```php
require_once('../test.php');

```

pour inclure un fichier dans le dossier parent ou pour aller dans un sous-dossier :

```php
require_once('test/test.php');

```

Vous pouvez utiliser des chemins absolus :

```php
require_once('/var/www/test/file.php');

```

Dans les bases de code PHP modernes qui utilisent un framework, les fichiers sont généralement chargés automatiquement, donc vous aurez moins besoin d'utiliser les fonctions ci-dessus.

## Constantes, fonctions et variables utiles pour le système de fichiers en PHP

En parlant de chemins, PHP vous offre plusieurs utilitaires pour vous aider à travailler avec les chemins.

Vous pouvez obtenir le chemin complet du fichier actuel en utilisant :

* `__FILE__`, une _constante magique_
* `$_SERVER['SCRIPT_FILENAME']` (plus sur `$_SERVER` plus tard !)

Vous pouvez obtenir le chemin complet du dossier où se trouve le fichier actuel en utilisant :

* la fonction intégrée [`getcwd()`](https://www.php.net/manual/en/function.getcwd.php)
* `__DIR__`, une autre constante magique
* combinez `__FILE__` avec `dirname()` pour obtenir le chemin complet du dossier actuel : `dirname(__FILE__)`
* utilisez `$_SERVER['DOCUMENT_ROOT']`

## Comment gérer les erreurs en PHP

Tout programmeur commet des erreurs. Nous sommes humains, après tout.

Nous pouvons oublier un point-virgule. Ou utiliser le mauvais nom de variable. Ou passer le mauvais argument à une fonction.

En PHP, nous avons :

* Avertissements
* Notices
* Erreurs

Les deux premiers sont des erreurs mineures et n'arrêtent pas l'exécution du programme. PHP imprimera un message, et c'est tout.

Les erreurs mettent fin à l'exécution du programme et imprimeront un message vous indiquant pourquoi.

Il existe de nombreux types d'erreurs différents, comme les erreurs de syntaxe, les erreurs fatales d'exécution, les erreurs fatales de démarrage, et plus encore.

Ce sont toutes des erreurs.

J'ai dit « PHP imprimera un message », mais... où ?

Cela dépend de votre configuration.

En mode développement, il est courant de journaliser les erreurs PHP directement dans la page Web, mais aussi dans un journal d'erreurs.

Vous _voulez_ voir ces erreurs le plus tôt possible, afin de pouvoir les corriger.

En production, en revanche, vous ne voulez pas les afficher dans la page Web, mais vous voulez toujours en être informé.

Alors, que faites-vous ? Vous les journalisez dans le journal des erreurs.

Tout cela est décidé dans la configuration PHP.

Nous n'en avons pas encore parlé, mais il y a un fichier dans la configuration de votre serveur qui décide de nombreuses choses sur la façon dont PHP s'exécute.

Il s'appelle `php.ini`.

L'emplacement exact de ce fichier dépend de votre configuration.

Pour savoir où se trouve le vôtre, le moyen le plus simple est d'ajouter ceci à un fichier PHP et de l'exécuter dans votre navigateur :

```php
<?php
phpinfo();
?>

```

Vous verrez alors l'emplacement sous « Fichier de configuration chargé » :

![Screen Shot 2022-06-27 at 13.42.41.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_13.42.41.jpg)

Dans mon cas, c'est `/Applications/MAMP/bin/php/php8.1.0/conf/php.ini`.

Notez que les informations générées par `phpinfo()` contiennent beaucoup d'autres informations utiles. Retenez cela.

En utilisant MAMP, vous pouvez ouvrir le dossier de l'application MAMP et ouvrir `bin/php`. Allez dans votre version spécifique de PHP (8.1.0 dans mon cas), puis allez dans `conf`. Là, vous trouverez le fichier `php.ini` :

![Screen Shot 2022-06-27 at 12.11.28.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_12.11.28.jpg)

Ouvrez ce fichier dans un éditeur.

Il contient une très longue liste de paramètres, avec une excellente documentation en ligne pour chacun.

Nous nous intéressons particulièrement à `display_errors` :

![Screen Shot 2022-06-27 at 12.13.16.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_12.13.16.jpg)

En production, vous voulez que sa valeur soit `Off`, comme l'indiquent les docs ci-dessus.

Les erreurs n'apparaîtront plus sur le site web, mais vous les verrez dans le fichier `php_error.log` dans le dossier `logs` de MAMP dans ce cas :

![Screen Shot 2022-06-27 at 12.16.01.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_12.16.01.jpg)

Ce fichier se trouvera dans un dossier différent selon votre configuration.

Vous définissez cet emplacement dans votre `php.ini` :

![Screen Shot 2022-06-27 at 12.17.12.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_12.17.12.jpg)

Le journal des erreurs contiendra tous les messages d'erreur que votre application génère :

![Screen Shot 2022-06-27 at 12.17.55.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_12.17.55.jpg)

Vous pouvez ajouter des informations au journal des erreurs en utilisant la fonction [`error_log()`](https://www.php.net/manual/en/function.error-log.php) :

```php
error_log('test');

```

Il est courant d'utiliser un service de journalisation pour les erreurs, comme [Monolog](https://github.com/Seldaek/monolog).

## Comment gérer les exceptions en PHP

Parfois, les erreurs sont inévitables. Comme si quelque chose de complètement imprévisible se produit.

Mais souvent, nous pouvons anticiper et écrire du code qui peut intercepter une erreur et faire quelque chose de sensé lorsque cela se produit. Comme afficher un message d'erreur utile à l'utilisateur, ou essayer une solution de contournement.

Nous le faisons en utilisant des **exceptions**.

Les exceptions sont utilisées pour nous, développeurs, prendre conscience d'un problème.

Nous enveloppons un code qui peut potentiellement lever une exception dans un bloc `try`, et nous avons un bloc `catch` juste après. Ce bloc catch sera exécuté s'il y a une exception dans le bloc try :

```php
try {
  //faire quelque chose
} catch (Throwable $e) {
  //nous pouvons faire quelque chose ici si une exception se produit
}

```

Remarquez que nous avons un objet `Exception` `$e` qui est passé au bloc `catch`, et nous pouvons inspecter cet objet pour obtenir plus d'informations sur l'exception, comme ceci :

```php
try {
  //faire quelque chose
} catch (Throwable $e) {
  echo $e->getMessage();
}

```

Regardons un exemple.

Disons que par erreur je divise un nombre par zéro :

```php
echo 1 / 0;

```

Cela déclenchera une erreur fatale et le programme s'arrêtera à cette ligne :

![Screen Shot 2022-06-26 at 20.12.59.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-26_at_20.12.59.jpg)

En enveloppant l'opération dans un bloc try et en imprimant le message d'erreur dans le bloc catch, le programme se termine avec succès, me disant le problème :

```php
try {
  echo 1 / 0;
} catch (Throwable $e) {
  echo $e->getMessage();
}

```

![Screen Shot 2022-06-26 at 20.13.36.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-26_at_20.13.36.jpg)

Bien sûr, c'est un exemple simple, mais vous pouvez voir le bénéfice : je peux intercepter le problème.

Chaque exception a une classe différente. Par exemple, nous pouvons attraper cela comme [`DivisionByZeroError`](https://www.php.net/manual/en/class.divisionbyzeroerror.php) et cela me permet de filtrer les problèmes possibles et de les traiter différemment.

Je peux avoir un attrape-tout pour toute erreur lançable à la fin, comme ceci :

```php
try {
  echo 1 / 0;
} catch (DivisionByZeroError $e) {
  echo 'Ooops j'ai divisé par zéro !';
} catch (Throwable $e) {
  echo $e->getMessage();
}

```

![Screen Shot 2022-06-26 at 20.15.47.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-26_at_20.15.47.jpg)

Et je peux également ajouter un bloc `finally {}` à la fin de cette structure try/catch pour exécuter du code après que le code ait été exécuté avec succès sans problèmes, ou s'il y avait un _catch_ :

```php
try {
  echo 1 / 0;
} catch (DivisionByZeroError $e) {
  echo 'Ooops j'ai divisé par zéro !';
} catch (Throwable $e) {
  echo $e->getMessage();
} finally {
  echo ' ...terminé !';
}

```

![Screen Shot 2022-06-26 at 20.17.33.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-26_at_20.17.33.jpg)

Vous pouvez utiliser les [exceptions intégrées](https://www.php.net/manual/en/reserved.exceptions.php) fournies par PHP, mais vous pouvez également créer vos propres exceptions.

## Comment travailler avec les dates en PHP

Travailler avec les dates et les heures est très courant en programmation. Voyons ce que PHP fournit.

Nous pouvons obtenir le timestamp actuel (nombre de secondes depuis le 1er janvier 1970 00:00:00 GMT) en utilisant [`time()`](https://www.php.net/manual/en/function.time.php) :

```php
$timestamp = time();

```

Lorsque vous avez un timestamp, vous pouvez le formater comme une date en utilisant [`date()`](https://www.php.net/manual/en/function.date.php), dans le format que vous préférez :

```php
echo date('Y-m-d', $timestamp);

```

`Y` est la représentation à 4 chiffres de l'année, `m` est le numéro du mois (avec un zéro initial) et `d` est le numéro du jour du mois, avec un zéro initial.

Voir la [liste complète des caractères que vous pouvez utiliser pour formater la date ici](https://www.php.net/manual/en/datetime.format.php).

Nous pouvons convertir n'importe quelle date en un timestamp en utilisant [`strtotime()`](https://www.php.net/manual/en/function.strtotime.php), qui prend une chaîne avec une représentation textuelle d'une date et la convertit en nombre de secondes depuis le 1er janvier 1970 :

```php
echo strtotime('now');
echo strtotime('4 May 2020');
echo strtotime('+1 day');
echo strtotime('+1 month');
echo strtotime('last Sunday');

```

...c'est assez flexible.

Pour les dates, il est courant d'utiliser des bibliothèques qui offrent beaucoup plus de fonctionnalités que ce que le langage peut. Une bonne option est [Carbon](https://carbon.nesbot.com).

## Comment utiliser les constantes et les énumérations en PHP

Nous pouvons définir des constantes en PHP en utilisant la fonction intégrée `define()` :

```php
define('TEST', 'une valeur');

```

Et ensuite nous pouvons utiliser `TEST` comme si c'était une variable, mais sans le signe `$` :

```php
define('TEST', 'une valeur');

echo TEST;

```

Nous utilisons des identifiants en majuscules comme convention pour les constantes.

Intéressamment, à l'intérieur des classes, nous pouvons définir des propriétés constantes en utilisant le mot-clé `const` :

```php
class Dog {
  const BREED = 'Siberian Husky';
}

```

Par défaut, elles sont `public` mais nous pouvons les marquer comme `private` ou `protected` :

```php
class Dog {
  private const BREED = 'Siberian Husky';
}

```

Les énumérations permettent de regrouper des constantes sous une racine commune. Par exemple, vous voulez avoir une énumération `Status` qui a 3 états : `EATING` `SLEEPING` `RUNNING`, les 3 états d'une journée de chien.

Donc vous avez :

```php
enum Status {
  case EATING;
  case SLEEPING;
  case RUNNING;
}

```

Maintenant, nous pouvons référencer ces constantes de cette manière :

```php
class Dog {
  public Status $status;
}

$dog = new Dog();

$dog->status = Status::RUNNING;

if ($dog->status == Status::SLEEPING) {
  //...
}

```

Les énumérations sont des objets, elles peuvent avoir des méthodes et beaucoup d'autres fonctionnalités que nous ne pouvons pas aborder ici dans cette courte introduction.

## Comment utiliser PHP comme plateforme de développement d'applications web

PHP est un langage côté serveur et il est typiquement utilisé de deux manières.

L'une est au sein d'une page HTML, donc PHP est utilisé pour « ajouter » des éléments à l'HTML qui est défini manuellement dans le fichier `.php`. C'est une manière parfaitement acceptable d'utiliser PHP.

Une autre manière considère PHP plus comme le moteur qui est responsable de la génération d'une « application ». Vous n'écrivez pas le HTML dans un fichier `.php`, mais vous utilisez plutôt un langage de templating pour générer le HTML, et tout est géré par ce que nous appelons le **framework**.

C'est ce qui se passe lorsque vous utilisez un framework moderne comme Laravel.

Je considérerais la première manière un peu « démodée » de nos jours, et si vous commencez tout juste, vous devriez connaître ces deux styles différents d'utilisation de PHP.

Mais envisagez également d'utiliser un framework comme « mode facile » car les frameworks vous donnent des outils pour gérer le routage, des outils pour accéder aux données d'une base de données, et ils rendent plus facile la construction d'une application plus sécurisée. Et ils rendent tout cela plus rapide à développer.

Cela dit, nous ne parlerons pas d'utiliser des frameworks dans ce manuel. Mais je parlerai des blocs de construction de base, fondamentaux de PHP. Ce sont des éléments essentiels que tout développeur PHP doit connaître.

Sachez simplement que « dans le monde réel », vous pourriez utiliser la manière de faire de votre framework préféré plutôt que les fonctionnalités de _bas niveau_ offertes par PHP.

Cela ne s'applique pas seulement à PHP bien sûr – c'est un « problème » qui se pose avec n'importe quel langage de programmation.

### Comment gérer les requêtes HTTP en PHP

Commençons par la gestion des requêtes HTTP.

PHP offre un routage basé sur les fichiers par défaut. Vous créez un fichier `index.php` et celui-ci répond sur le chemin `/`.

Nous l'avons vu lorsque nous avons fait l'exemple Hello World au début.

De même, vous pouvez créer un fichier `test.php` et automatiquement celui-ci sera le fichier qu'Apache servira sur la route `/test`.

### Comment utiliser `$_GET`, `$_POST` et `$_REQUEST` en PHP

Les fichiers répondent à toutes les requêtes HTTP, y compris GET, POST et autres verbes.

Pour toute requête, vous pouvez accéder à toutes les données de la chaîne de requête en utilisant l'objet `$_GET`. Il est appelé _superglobal_ et est automatiquement disponible dans tous nos fichiers PHP.

Cela est bien sûr surtout utile dans les requêtes GET, mais d'autres requêtes peuvent également envoyer des données sous forme de chaîne de requête.

Pour les requêtes POST, PUT et DELETE, vous êtes plus susceptible d'avoir besoin des données postées sous forme de données encodées en URL ou en utilisant l'objet FormData, que PHP met à votre disposition en utilisant `$_POST`.

Il existe également `$_REQUEST` qui contient toutes les données de `$_GET` et `$_POST` combinées en une seule variable.

### Comment utiliser l'objet `$_SERVER` en PHP

Nous avons également la variable superglobale `$_SERVER`, que vous utilisez pour obtenir beaucoup d'informations utiles.

Vous avez vu comment utiliser `phpinfo()` auparavant. Utilisons-le à nouveau pour voir ce que $_SERVER nous offre.

Dans votre fichier `index.php` à la racine de MAMP, exécutez :

```php
<?php
phpinfo();
?>

```

Puis générez la page à [localhost:8888](http://localhost:8888) et recherchez `$_SERVER`. Vous verrez toute la configuration stockée et les valeurs assignées :

![Screen Shot 2022-06-27 at 13.46.50.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_13.46.50.jpg)

Les plus importantes que vous pourriez utiliser sont :

* `$_SERVER['HTTP_HOST']`
* `$_SERVER['HTTP_USER_AGENT']`
* `$_SERVER['SERVER_NAME']`
* `$_SERVER['SERVER_ADDR']`
* `$_SERVER['SERVER_PORT']`
* `$_SERVER['DOCUMENT_ROOT']`
* `$_SERVER['REQUEST_URI']`
* `$_SERVER['SCRIPT_NAME']`
* `$_SERVER['REMOTE_ADDR']`

### Comment utiliser les formulaires en PHP

Les formulaires sont le moyen par lequel la plateforme Web permet aux utilisateurs d'interagir avec une page et d'envoyer des données au serveur.

Voici un formulaire simple en HTML :

```php
<form>
  <input type="text" name="name" />
  <input type="submit" />
</form>

```

Vous pouvez mettre ceci dans votre fichier `index.php` comme s'il s'agissait de `index.html`.

Un fichier PHP suppose que vous écrivez du HTML avec quelques "pincées de PHP" en utilisant `<?php ?>` afin que le serveur Web puisse poster cela au client. Parfois, la partie PHP prend toute la page, et c'est lorsque vous générez tout le HTML via PHP – c'est un peu l'inverse de l'approche que nous adoptons ici maintenant.

Donc nous avons ce fichier `index.php` qui génère ce formulaire en utilisant du HTML simple :

![Screen Shot 2022-06-27 at 13.53.47.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_13.53.47.jpg)

Appuyer sur le bouton Soumettre fera une requête GET à la même URL en envoyant les données via la chaîne de requête. Remarquez que l'URL a changé pour [localhost:8888/?name=test](http://localhost:8888/?name=test).

![Screen Shot 2022-06-27 at 13.56.46.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_13.56.46.jpg)

Nous pouvons ajouter du code pour vérifier si ce paramètre est défini en utilisant la fonction [`isset()`](https://www.php.net/manual/en/function.isset.php) :

```php
<form>
  <input type="text" name="name" />
  <input type="submit" />
</form>

<?php
if (isset($_GET['name'])) {
  echo '<p>Le nom est ' . $_GET['name'];
}
?>

```

![Screen Shot 2022-06-27 at 13.56.35.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_13.56.35.jpg)

Vous voyez ? Nous pouvons obtenir les informations de la chaîne de requête de la [requête GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET) via `$_GET`.

Ce que vous faites généralement avec les formulaires, c'est effectuer une requête POST :

```php
<form **method="POST"**>
  <input type="text" name="name" />
  <input type="submit" />
</form>

<?php
if (isset($_POST['name'])) {
  echo '<p>Le nom est ' . $_POST['name'];
}
?>

```

Vous voyez, maintenant nous avons obtenu les mêmes informations mais l'URL n'a pas changé. Les informations du formulaire n'ont pas été ajoutées à l'URL.

![Screen Shot 2022-06-27 at 13.59.54.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_13.59.54.jpg)

C'est parce que nous utilisons une [requête POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST), qui envoie les données au serveur d'une manière différente, via des données encodées en URL.

Comme mentionné ci-dessus, PHP servira toujours le fichier `index.php` car nous envoyons toujours des données à la même URL que le formulaire.

Nous mélangeons un tas de code et nous pourrions séparer le gestionnaire de requêtes de formulaire du code qui génère le formulaire.

Donc nous pouvons avoir ceci dans `index.php` :

```php
<form **method="POST" action="/post.php"**>
  <input type="text" name="name" />
  <input type="submit" />
</form>

```

et nous pouvons créer un nouveau fichier `post.php` avec :

```php
<?php
if (isset($_POST['name'])) {
  echo '<p>Le nom est ' . $_POST['name'];
}
?>

```

PHP affichera ce contenu maintenant après que nous ayons soumis le formulaire, car nous avons défini l'attribut HTML `action` sur le formulaire.

Cet exemple est très simple, mais le fichier `post.php` est là où nous pourrions, par exemple, sauvegarder les données dans la base de données, ou dans un fichier.

### Comment utiliser les en-têtes HTTP en PHP

PHP nous permet de définir les en-têtes HTTP d'une réponse via la fonction `header()`.

Les [en-têtes HTTP](https://flaviocopes.com/http-request-headers/) sont un moyen d'envoyer des informations au navigateur.

Nous pouvons dire que la page génère une erreur 500 Internal Server Error :

```php
<?php
header('HTTP/1.1 500 Internal Server Error');
?>

```

Maintenant, vous devriez voir le statut si vous accédez à la page avec les [Outils de développement du navigateur](https://flaviocopes.com/browser-dev-tools/) ouverts :

![Screen Shot 2022-06-27 at 14.10.29.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_14.10.29.jpg)

Nous pouvons définir le `content/type` d'une réponse :

```php
header('Content-Type: text/json');

```

Nous pouvons forcer une redirection 301 :

```php
header('HTTP/1.1 301 Moved Permanently');
header('Location: https://flaviocopes.com');

```

Nous pouvons utiliser les en-têtes pour dire au navigateur "mettre cette page en cache", "ne pas mettre cette page en cache", et bien plus encore.

### Comment utiliser les cookies en PHP

Les cookies sont une fonctionnalité du navigateur.

Lorsque nous envoyons une réponse au navigateur, nous pouvons définir un cookie qui sera stocké par le navigateur, côté client.

Ensuite, chaque requête que le navigateur fait inclura le cookie en retour vers nous.

Nous pouvons faire beaucoup de choses avec les cookies. Ils sont principalement utilisés pour créer une expérience personnalisée sans que vous ayez à vous connecter à un service.

Il est important de noter que les cookies sont spécifiques à un domaine, donc nous ne pouvons lire que les cookies que nous avons définis sur le domaine actuel de notre application, et non les cookies d'autres applications.

Mais JavaScript peut lire les cookies (sauf s'ils sont des _cookies HttpOnly_, mais nous commençons à entrer dans un terrier) donc les cookies ne doivent pas stocker d'informations sensibles.

Nous pouvons utiliser PHP pour lire la valeur d'un cookie en référençant la superglobale `$_COOKIE` :

```php
if (isset($_COOKIE['name'])) {
  $name = $_COOKIE['name'];
}

```

La fonction [`setcookie()`](https://www.php.net/manual/en/function.setcookie.php) vous permet de définir un cookie :

```php
setcookie('name', 'Flavio');

```

Nous pouvons ajouter un troisième paramètre pour indiquer quand le cookie expirera. Si omis, le cookie expire à la fin de la session/lorsque le navigateur est fermé.

Utilisez ce code pour faire expirer le cookie dans 7 jours :

```php
setcookie('name', 'Flavio', time() + 3600 * 24 * 7);

```

Nous ne pouvons stocker qu'une quantité limitée de données dans un cookie, et les utilisateurs peuvent effacer les cookies côté client lorsqu'ils effacent les données du navigateur.

De plus, ils sont spécifiques au navigateur/appareil, donc nous pouvons définir un cookie dans le navigateur de l'utilisateur, mais s'ils changent de navigateur ou d'appareil, le cookie ne sera pas disponible.

Faisons un exemple simple avec le formulaire que nous avons utilisé auparavant. Nous allons stocker le nom entré comme un cookie :

```php
<?php
if (isset($_POST['name'])) {
  setcookie('name', $_POST['name']);
}
if (isset($_POST['name'])) {
  echo '<p>Bonjour ' . $_POST['name'];
} else {
  if (isset($_COOKIE['name'])) {
    echo '<p>Bonjour ' . $_COOKIE['name'];
  }
}
?>

<form method="POST">
  <input type="text" name="name" />
  <input type="submit" />
</form>

```

J'ai ajouté quelques conditionnelles pour gérer le cas où le cookie était déjà défini, et pour afficher le nom juste après la soumission du formulaire, lorsque le cookie n'est pas encore défini (il ne sera défini que pour la prochaine requête HTTP).

Si vous ouvrez les outils de développement du navigateur, vous devriez voir le cookie dans l'onglet Stockage.

À partir de là, vous pouvez inspecter sa valeur, et le supprimer si vous le souhaitez.

![Screen Shot 2022-06-27 at 14.46.09.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_14.46.09.jpg)

### Comment utiliser les sessions basées sur les cookies en PHP

Un cas d'utilisation très intéressant pour les cookies est les sessions basées sur les cookies.

PHP nous offre un moyen très facile de créer une session basée sur les cookies en utilisant `session_start()`.

Essayez d'ajouter ceci :

```php
<?php
session_start();
?>

```

dans un fichier PHP, et chargez-le dans le navigateur.

Vous verrez un nouveau cookie nommé par défaut `PHPSESSID` avec une valeur assignée.

C'est l'identifiant de session. Cela sera envoyé pour chaque nouvelle requête et PHP l'utilisera pour identifier la session.

![Screen Shot 2022-06-27 at 14.51.53.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_14.51.53.jpg)

De manière similaire à l'utilisation des cookies, nous pouvons maintenant utiliser `$_SESSION` pour stocker les informations envoyées par l'utilisateur – mais cette fois-ci, elles ne sont pas stockées côté client.

Seul l'identifiant de session l'est.

Les données sont stockées côté serveur par PHP.

```php
<?php
session_start();

if (isset($_POST['name'])) {
  $_SESSION['name'] = $_POST['name'];
}
if (isset($_POST['name'])) {
  echo '<p>Bonjour ' . $_POST['name'];
} else {
  if (isset($_SESSION['name'])) {
    echo '<p>Bonjour ' . $_SESSION['name'];
  }
}
?>

<form method="POST">
  <input type="text" name="name" />
  <input type="submit" />
</form>

```

![Screen Shot 2022-06-27 at 14.53.24.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_14.53.24.jpg)

Cela fonctionne pour des cas d'utilisation simples, mais bien sûr pour des données intensives, vous aurez besoin d'une base de données.

Pour effacer les données de session, vous pouvez appeler `session_unset()`.

Pour effacer le cookie de session, utilisez :

```php
setcookie(session_name(), '');

```

### Comment travailler avec les fichiers et dossiers en PHP

PHP est un langage côté serveur, et l'une des choses pratiques qu'il fournit est l'accès au système de fichiers.

Vous pouvez vérifier si un fichier existe en utilisant `file_exists()` :

```php
file_exists('test.txt') //true

```

Obtenez la taille d'un fichier en utilisant `filesize()` :

```php
filesize('test.txt')

```

Vous pouvez ouvrir un fichier en utilisant `fopen()`. Ici, nous ouvrons le fichier `test.txt` en **mode lecture seule** et nous obtenons ce que nous appelons un **descripteur de fichier** dans `$file` :

```php
$file = fopen('test.txt', 'r')

```

Nous pouvons terminer l'accès au fichier en appelant `fclose($fd)`.

Lisez le contenu d'un fichier dans une variable comme ceci :

```php
$file = fopen('test.txt', 'r')

fread($file, filesize('test.txt'));

//ou

while (!feof($file)) {
	$data .= fgets($file, 5000);
}

```

`feof()` vérifie que nous n'avons pas atteint la fin du fichier car `fgets` lit 5000 octets à la fois.

Vous pouvez également lire un fichier ligne par ligne en utilisant `fgets()` :

```php
$file = fopen('test.txt', 'r')

while(!feof($file)) {
  $line = fgets($file);
  //faire quelque chose
}

```

Pour écrire dans un fichier, vous devez d'abord l'ouvrir en **mode écriture**, puis utiliser `fwrite()` :

```php
$data = 'test';
$file = fopen('test.txt', 'w')
fwrite($file, $data);
fclose($file);

```

Nous pouvons supprimer un fichier en utilisant `unlink()` :

```php
unlink('test.txt')

```

Ce sont les bases, mais bien sûr, il existe [plus de fonctions pour travailler avec les fichiers](https://www.php.net/manual/en/ref.filesystem.php).

### PHP et les bases de données

PHP offre diverses bibliothèques intégrées pour travailler avec les bases de données, par exemple :

* [PostgreSQL](https://www.php.net/manual/en/book.pgsql.php)
* [MySQL](https://www.php.net/manual/en/set.mysqlinfo.php) / MariaDB
* [MongoDB](https://www.php.net/manual/en/set.mongodb.php)

Je ne couvrirai pas cela dans le manuel car je pense que c'est un sujet vaste et qui nécessiterait également que vous appreniez SQL.

Je suis également tenté de dire que si vous avez besoin d'une base de données, vous devriez utiliser un framework ou un ORM qui vous éviterait des problèmes de sécurité avec l'injection SQL. [Eloquent de Laravel](https://laravel.com/docs/eloquent) est un excellent exemple.

### Comment travailler avec JSON en PHP

[JSON](https://flaviocopes.com/json/) est un format de données portable que nous utilisons pour représenter des données et envoyer des données du client au serveur.

Voici un exemple de représentation JSON d'un objet qui contient une chaîne et un nombre :

```php
{
  "name": "Flavio",
  "age": 35
}

```

PHP nous offre deux fonctions utilitaires pour travailler avec JSON :

* `json_encode()` pour encoder une variable en JSON
* `json_decode()` pour décoder une chaîne JSON en un type de données (objet, tableau…)

Exemple :

```php
$test = ['a', 'b', 'c'];

$encoded = json_encode($test); // "["a","b","c"]" (une chaîne)

$decoded = json_decode($encoded); // [ "a", "b", "c" ] (un tableau)

```

### Comment envoyer des emails avec PHP

L'une des choses que j'aime dans PHP, ce sont les commodités, comme l'envoi d'un email.

Envoyez un email en utilisant [`mail()`](https://www.php.net/manual/en/function.mail.php) :

```php
mail('test@test.com', 'ce sujet', 'le corps');

```

Pour envoyer des emails à grande échelle, nous ne pouvons pas compter sur cette solution, car ces emails ont tendance à atteindre le dossier de spam plus souvent qu'autrement. Mais pour des tests rapides, cela est très utile.

Des bibliothèques comme [https://github.com/PHPMailer/PHPMailer](https://github.com/PHPMailer/PHPMailer) seront très utiles pour des besoins plus solides, en utilisant un serveur SMTP.

## Comment utiliser Composer et Packagist

[Composer](https://getcomposer.org) est le gestionnaire de paquets de PHP.

Il vous permet d'installer facilement des paquets dans vos projets.

Installez-le sur votre machine ([Linux/Mac](https://getcomposer.org/doc/00-intro.md#installation-linux-unix-macos) ou [Windows](https://getcomposer.org/doc/00-intro.md#installation-windows)) et une fois que vous avez terminé, vous devriez avoir une commande `composer` disponible sur votre terminal.

![Screen Shot 2022-06-27 at 16.25.43.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_16.25.43.jpg)

Maintenant, à l'intérieur de votre projet, vous pouvez exécuter `composer require <lib>` et il sera installé localement. Par exemple, installons [la bibliothèque Carbon](https://carbon.nesbot.com) qui nous aide à travailler avec les dates en PHP

```php
composer require nesbot/carbon

```

Il fera un peu de travail :

![Screen Shot 2022-06-27 at 16.27.11.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_16.27.11.jpg)

Une fois terminé, vous trouverez quelques nouvelles choses dans le dossier `composer.json` qui liste la nouvelle configuration pour les dépendances :

```php
{
    "require": {
        "nesbot/carbon": "^2.58"
    }
}

```

`composer.lock` est utilisé pour « verrouiller » les versions du package dans le temps, afin que la même installation exacte que vous avez puisse être répliquée sur un autre serveur. Le dossier `vendor` contient la bibliothèque nouvellement installée et ses dépendances.

Maintenant, dans le fichier `index.php`, nous pouvons ajouter ce code en haut :

```php
<?php
require 'vendor/autoload.php';

use Carbon\Carbon;

```

et ensuite nous pouvons utiliser la bibliothèque !

```php
echo Carbon::now();

```

![Screen Shot 2022-06-27 at 16.34.47.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_16.34.47.jpg)

Vous voyez ? Nous n'avons pas eu à télécharger manuellement un package depuis Internet et à l'installer quelque part... tout a été rapide, simple et bien organisé.

La ligne `require 'vendor/autoload.php';` est ce qui permet le **chargement automatique**. Vous vous souvenez lorsque nous avons parlé de `require_once()` et `include_once()` ? Cela résout tout cela – nous n'avons pas besoin de rechercher manuellement le fichier à inclure, nous utilisons simplement le mot-clé `use` pour importer la bibliothèque dans notre code.

## Comment déployer une application PHP

Lorsque vous avez une application prête, il est temps de la déployer et de la rendre accessible à tous sur le Web.

PHP est le langage de programmation avec la meilleure histoire de déploiement sur le Web.

Croyez-moi, chaque autre langage de programmation et écosystème souhaite être aussi facile que PHP.

La grande chose à propos de PHP, la chose qu'il a bien faite et qui lui a permis d'avoir le succès incroyable qu'il a eu, est le déploiement instantané.

Vous placez un fichier PHP dans un dossier servi par un serveur Web, et _voilà_ – cela fonctionne simplement.

Pas besoin de redémarrer le serveur, d'exécuter un exécutable, rien.

C'est encore quelque chose que beaucoup de gens font. Vous obtenez un hébergement mutualisé pour 3 $/mois, vous téléchargez vos fichiers via FTP, et c'est fait.

Ces jours-ci, cependant, je pense que le déploiement Git est quelque chose qui devrait être intégré à chaque projet, et l'hébergement mutualisé devrait être une chose du passé.

Une solution est toujours d'avoir votre propre VPS privé (Virtual Private Server), que vous pouvez obtenir auprès de services comme DigitalOcean ou Linode.

Mais gérer votre propre VPS n'est pas une blague. Cela nécessite des connaissances sérieuses et un investissement en temps, ainsi qu'une maintenance constante.

Vous pouvez également utiliser ce que l'on appelle le PaaS (Platform as a Service), qui sont des plateformes qui se concentrent sur la prise en charge de toutes les choses ennuyeuses (gestion des serveurs) et vous téléchargez simplement votre application et elle fonctionne.

Des solutions comme **DigitalOcean App Platform** (qui est différent d'un VPS DigitalOcean), Heroku, et bien d'autres sont excellentes pour vos premiers tests.

Ces services vous permettent de connecter votre compte GitHub et de déployer chaque fois que vous poussez un nouveau changement à votre dépôt [Git](https://flaviocopes.com/git/).

Vous pouvez apprendre [comment configurer Git et GitHub à partir de zéro ici](https://flaviocopes.com/github-setup-from-zero/).

C'est un flux de travail bien meilleur par rapport aux téléchargements FTP.

Faisons un exemple minimaliste.

J'ai créé une application PHP simple avec juste un fichier `index.php` :

```php
<?php
echo 'Bonjour !';
?>

```

J'ajoute le dossier parent à mon application GitHub Desktop, j'initialise un dépôt Git, et je le pousse vers GitHub :

![Screen Shot 2022-06-27 at 17.26.24.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_17.26.24.jpg)

Maintenant, allez sur [digitalocean.com](http://digitalocean.com).

Si vous n'avez pas encore de compte, [utilisez mon code de parrainage pour vous inscrire et obtenir 100 $ de crédits gratuits sur les 60 prochains jours](https://m.do.co/c/bd0657b4877c) et vous pourrez travailler sur votre application PHP gratuitement.

Je me connecte à mon compte DigitalOcean et je vais dans Apps → Créer une App.

Je connecte mon compte GitHub et je sélectionne le dépôt de mon application.

Assurez-vous que « Déploiement automatique » est coché, afin que l'application se redéploie automatiquement en cas de modifications :

![Screen Shot 2022-06-27 at 17.31.54.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_17.31.54.jpg)

Cliquez sur « Suivant » puis sur Modifier le Plan :

![Screen Shot 2022-06-27 at 17.32.24.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_17.32.24.jpg)

Par défaut, le plan Pro est sélectionné.

Utilisez le plan de base et choisissez le plan à 5 $/mois.

Notez que vous payez 5 $ par mois, mais la facturation est par heure – donc vous pouvez arrêter l'application à tout moment.

![Screen Shot 2022-06-27 at 17.32.28.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_17.32.28.jpg)

![Screen Shot 2022-06-27 at 17.33.15.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_17.33.15.jpg)

Ensuite, revenez en arrière et appuyez sur « Suivant » jusqu'à ce que le bouton « Créer des ressources » apparaisse pour créer l'application. Vous n'avez pas besoin de base de données, sinon cela coûterait 7 $/mois supplémentaires.

![Screen Shot 2022-06-27 at 17.33.46.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_17.33.46.jpg)

Maintenant, attendez que le déploiement soit prêt :

![Screen Shot 2022-06-27 at 17.35.00.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_17.35.00.jpg)

L'application est maintenant opérationnelle !

![Screen Shot 2022-06-27 at 17.35.31.jpg](https://www.freecodecamp.org/news/content/images/2022/07/Screen_Shot_2022-06-27_at_17.35.31.jpg)

## Conclusion

Vous avez atteint la fin du Manuel PHP !

Merci d'avoir lu cette introduction au merveilleux monde du développement PHP. J'espère qu'elle vous aidera à obtenir votre emploi de développeur web, à devenir meilleur dans votre métier, et à vous donner les moyens de travailler sur votre prochaine grande idée.

Note : vous pouvez obtenir une version [PDF, ePub, ou Mobi](https://thevalleyofcode.com/download/php/) de ce manuel pour une référence plus facile, ou pour lire sur votre Kindle ou tablette.