---
title: Les meilleurs exemples PHP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-01T18:11:00.000Z'
originalURL: https://freecodecamp.org/news/the-best-php-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/php-examples.jpeg
tags:
- name: PHP
  slug: php
seo_title: Les meilleurs exemples PHP
seo_desc: 'PHP is a server-side scripting language created in 1995 by Rasmus Lerdorf.

  PHP is a widely-used open source general-purpose scripting language that is especially
  suited for web development and can be embedded into HTML.

  What is PHP used for?

  As of Oc...'
---

PHP est un langage de script côté serveur créé en 1995 par Rasmus Lerdorf.

PHP est un langage de script généraliste open source largement utilisé, particulièrement adapté au développement web et pouvant être intégré dans du HTML.

### À quoi sert PHP ?

En octobre 2018, PHP était utilisé sur [80 % des sites web dont le langage côté serveur est connu](https://w3techs.com/technologies/overview/programming_language/all). Il est généralement utilisé sur les sites web pour générer du contenu de page web de manière dynamique. Les cas d'utilisation incluent :

* Sites web et applications web (scripting côté serveur)
* Scripting en ligne de commande
* Applications de bureau (GUI)

Typiquement, il est utilisé sous la première forme pour générer du contenu de page web de manière dynamique. Par exemple, si vous avez un site web de blog, vous pourriez écrire des scripts PHP pour récupérer vos articles de blog depuis une base de données et les afficher. D'autres utilisations pour les scripts PHP incluent :

* Traitement et sauvegarde des entrées utilisateur depuis les données de formulaire
* Définition et travail avec les cookies du site web
* Restriction de l'accès à certaines pages de votre site web

La plus grande plateforme de réseautage social, [Facebook](https://www.facebook.com/), est écrite en utilisant PHP.

### Comment fonctionne PHP ?

Tout le code PHP est exécuté uniquement sur un serveur web, et non sur votre ordinateur local. Par exemple, si vous remplissez un formulaire sur un site web et le soumettez, ou cliquez sur un lien vers une page web écrite en PHP, aucun code PHP réel ne s'exécute sur votre ordinateur. Au lieu de cela, les données du formulaire ou la demande de la page web sont envoyées à un serveur web pour être traitées par les scripts PHP. Le serveur web envoie ensuite le HTML traité à votre navigateur (d'où vient le "Hypertext Preprocessor" dans le nom), et votre navigateur affiche les résultats. Pour cette raison, vous ne pouvez pas voir le code PHP d'un site web, seulement le HTML résultant que les scripts PHP ont produit.

Cela est illustré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-283.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/02/PHP-server-model.png)
_Source : https://github.com/xeroxism/_

PHP est un langage interprété. Cela signifie que lorsque vous apportez des modifications à votre code source, vous pouvez immédiatement tester ces modifications, sans avoir besoin de compiler votre code source en forme binaire. Le fait de sauter l'étape de compilation rend le processus de développement beaucoup plus rapide.

Le code PHP est encadré entre les balises `<?php` et `?>` et peut ensuite être intégré dans du HTML.

## Installation

PHP peut être installé avec ou sans serveur web.

### GNU/Linux

Sur les distributions GNU/Linux basées sur Debian, vous pouvez installer en utilisant :

```bash
sudo apt install php
```

Sur Centos 6 ou 7, vous pouvez installer en utilisant :

```bash
sudo yum install php
```

Après l'installation, vous pouvez exécuter n'importe quel fichier PHP en faisant simplement ceci dans le terminal :

```text
php fichier.php
```

Vous pouvez également installer un serveur localhost pour exécuter des sites web PHP. Pour installer le serveur web Apache :

```text
sudo apt install apache2 libapache2-mod-php
```

Ou vous pouvez également installer PHP, MySQL et le serveur web en installant

[XAMPP](https://www.apachefriends.org/download.html) (package de solution de pile de serveur web multiplateforme gratuit et open-source) ou des packages similaires comme [WAMP](http://www.wampserver.com/en/)

## Frameworks PHP

Étant donné qu'écrire tout le code pour un site web n'est pas vraiment pratique ou réalisable pour la plupart des projets, la plupart des développeurs ont tendance à utiliser des frameworks pour le développement web. L'avantage d'utiliser un framework est que

* Vous n'avez pas besoin de réinventer la roue à chaque fois que vous créez un projet, beaucoup de nuances sont déjà prises en charge pour vous
* Ils sont généralement bien structurés pour aider à la séparation des préoccupations
* La plupart des frameworks suivent les meilleures pratiques du langage
* Beaucoup d'entre eux suivent le modèle MVC (Modèle-Vue-Contrôleur) pour séparer la couche de présentation de la logique

### Frameworks populaires

* [CodeIgniter](https://codeigniter.com/)
* [Laravel](https://laravel.com/)
* [Symfony](https://symfony.com/)
* [Zend](http://www.zend.com/)
* [CakePHP](https://cakephp.org/)
* [FuelPHP](https://fuelphp.com/)
* [Slim](https://www.slimframework.com/)
* [Yii 2](https://www.yiiframework.com/)

## Syntaxe de base

Les scripts PHP peuvent être placés n'importe où dans un document et commencent toujours par `<?php` et se terminent par `?>`. De plus, les instructions PHP se terminent par un point-virgule (;).

Voici un script simple qui utilise la fonction intégrée `echo` pour afficher le texte "Les meilleurs exemples PHP" sur la page :

```
<!DOCTYPE html>
<html>
<body>

<h1>Actualités des développeurs</h1>

<?php echo "Les meilleurs exemples PHP"; ?>

</body>
</html> 
```

Le résultat serait :

```text
Actualités des développeurs

Les meilleurs exemples PHP
```

### Commentaires

PHP prend en charge plusieurs façons de commenter :

* Commentaires sur une seule ligne :
* Commentaires sur plusieurs lignes :

```
<?php
  // Ceci est un commentaire sur une seule ligne
  
  # Vous pouvez également faire des commentaires sur une seule ligne comme ceci
?>
```

```
<?php
/*
Ce bloc de commentaire s'étend
sur plusieurs 
ligne
*/
?>
```

### Sensibilité à la casse

Tous les mots-clés, classes et fonctions ne sont PAS sensibles à la casse.

Dans l'exemple ci-dessous, les trois instructions echo sont valides :

```text
<?php
ECHO "Bonjour!<br>";
echo "Bienvenue sur Actualités des développeurs<br>";
EcHo "Profitez de tous les articles sans publicité<br>";
?>
```

Cependant, tous les noms de variables sont sensibles à la casse. Dans l'exemple ci-dessous, seule la première instruction est valide et affichera la valeur de la variable `$name`. `$NAME` et `$NaMe` sont tous deux traités comme des variables différentes :

```text
<?php
$name = "Quincy";
echo "Salut ! Mon nom est " . $name . "<br>";
echo "Salut ! Mon nom est " . $NAME . "<br>";
echo "Salut ! Mon nom est " . $NaMe . "<br>";
?>
```

## Variables

Les variables sont le principal moyen de stocker des informations dans un programme PHP.

Toutes les variables en PHP commencent par un signe dollar `$` comme `$nom_variable`. Pour assigner une variable, utilisez l'opérateur `=`, avec le nom de la variable à gauche et l'expression à évaluer à droite.

**Syntaxe :**

```php
<?php
// Assigner la valeur "Bonjour !" à la variable "salutation"
$salutation = "Bonjour !";
// Assigner la valeur 8 à la variable "mois"
$mois = 8;
// Assigner la valeur 2019 à la variable "année"
$année = 2019;
?>
```

### Règles pour les variables PHP

* Les déclarations de variables commencent par `$`, suivi du nom de la variable
* Les noms de variables ne peuvent commencer que par une lettre majuscule ou minuscule ou un tiret bas (`_`)
* Les noms de variables ne peuvent contenir que des lettres, des chiffres ou des tirets bas (A-z, 0-9, et `_`). D'autres caractères spéciaux comme `+ - % ( ) . &` sont invalides
* Les noms de variables sont sensibles à la casse

**Quelques exemples de noms de variables autorisés :**

* $ma_variable
* $uneAutreVariable
* $la2emeVariable

### Variables prédéfinies

PHP a plusieurs mots-clés spéciaux qui, bien qu'ils soient des noms de variables "valides", ne peuvent pas être utilisés pour vos variables. La raison en est que le langage lui-même a déjà défini ces variables et qu'elles sont utilisées à des fins spéciales. Plusieurs exemples sont listés ci-dessous, pour une liste complète, voir le [site de documentation PHP](https://secure.php.net/manual/en/language.variables.predefined.php).

* `$this`
* `$_GET`
* `$_POST`
* `$_SERVER`
* `$_FILES`

## Types de données PHP

Les variables peuvent stocker des données de différents types tels que :

* Chaîne de caractères ("Bonjour")
* Entier (5)
* Flottant (aussi appelé double) (1.0)
* Booléen (1 ou 0)
* Tableau (array("I", "am", "an", "array"))
* Objet
* NULL
* Ressource

### Chaînes de caractères

Une chaîne de caractères est une séquence de caractères. Elle peut être n'importe quel texte entre guillemets (simples ou doubles) :

```php
$x = "Bonjour !";
$y = 'Bonjour !';
```

### Entiers

Un type de données entier est un nombre non décimal compris entre -2 147 483 648 et 2 147 483 647.

**Règles pour les entiers :**

* Les entiers doivent avoir au moins un chiffre
* Les entiers ne doivent pas avoir de point décimal
* Les entiers peuvent être positifs ou négatifs

`$x = 5;`

### Flottants

Un flottant, ou nombre à virgule flottante, est un nombre avec un point décimal.

`$x = 5.01;`

### Booléens

Un booléen représente deux états possibles : VRAI ou FAUX. Les booléens sont souvent utilisés dans les tests conditionnels.

```php
$x = true;
$y = false;
```

### Tableaux

Un tableau stocke plusieurs valeurs dans une seule variable.

`$couleurs = array("Magenta", "Jaune", "Cyan");`

### NULL

Null est un type de données spécial qui ne peut avoir que la valeur `null`. Les variables peuvent être déclarées sans valeur ou vidées en définissant la valeur à `null`. De plus, si une variable est créée sans être assignée à une valeur, elle est automatiquement assignée à `null`.

```php
<?php
// Assigner la valeur "Bonjour !" à salutation
$salutation = "Bonjour !";

// Vider la valeur salutation en la définissant à null
$salutation = null;
?>
```

### Classes et Objets

Une classe est une structure de données utile pour modéliser des choses dans le monde réel, et peut contenir des propriétés et des méthodes. Les objets sont des instances d'une classe, et sont un moyen pratique d'emballer des valeurs et des fonctions spécifiques à une classe.

```php
<?php
class Voiture {
    function Voiture() {
        $this->modele = "Tesla";
    }
}

// créer un objet
$Lightning = new Voiture();

// afficher les propriétés de l'objet
echo $Lightning->modele;
?>
```

### Ressource PHP

Une ressource est une variable spéciale, contenant une référence à une ressource externe. Les ressources sont créées et utilisées par des fonctions spéciales. Vous pouvez utiliser la fonction [get_resource_type()](http://php.net/manual/en/function.get-resource-type.php) pour voir le type de ressource.

```php
<?php
// affiche : lien mysql
$c = mysql_connect();
echo get_resource_type($c) . "\n";

// affiche : flux
$fp = fopen("foo", "w");
echo get_resource_type($fp) . "\n";

// affiche : document domxml
$doc = new_xmldoc("1.0");
echo get_resource_type($doc->doc) . "\n";
```

## Chaînes de caractères

Une chaîne de caractères est une série de caractères. Elles peuvent être utilisées pour stocker toute information textuelle dans votre application.

Il existe plusieurs façons différentes de créer des chaînes de caractères en PHP.

### Guillemets simples

Des chaînes de caractères simples peuvent être créées en utilisant des guillemets simples.

```php
$nom = 'Joe';
```

Pour inclure un guillemet simple dans la chaîne de caractères, utilisez une barre oblique inverse pour l'échapper.

```php
$nom_de_famille = 'O\'Brian';
```

### Guillemets doubles

Vous pouvez également créer des chaînes de caractères en utilisant des guillemets doubles.

```php
$nom = "Joe";
```

Pour inclure un guillemet double, utilisez une barre oblique inverse pour l'échapper.

```php
$citation = "Mary a dit, \"Je veux du toast,\" et puis s'est enfuie.";
```

Les chaînes de caractères entre guillemets doubles permettent également les séquences d'échappement. Ce sont des codes spéciaux qui placent des caractères dans votre chaîne de caractères qui représentent généralement des caractères invisibles. Les exemples incluent les nouvelles lignes `\n`, les tabulations `\t`, et les barres obliques inverses réelles `\\`.

Vous pouvez également intégrer des variables PHP dans des chaînes de caractères entre guillemets doubles pour que leurs valeurs soient ajoutées à la chaîne de caractères.

```php
$nom = 'Joe';
$salutation = "Bonjour $nom"; // contient maintenant la chaîne de caractères "Bonjour Joe"
```

### Fonctions de chaînes de caractères

#### Trouver la longueur d'une chaîne de caractères

La fonction `strlen()` retourne la longueur d'une chaîne de caractères.

```text
<?php
echo strlen("Actualités des développeurs"); // affiche 21
?>
```

**Trouver le nombre de mots dans une chaîne de caractères**  
La fonction `str_word_count()` retourne le nombre de mots dans une chaîne de caractères :

```text
<?php
echo str_word_count("Actualités des développeurs"); // affiche 3
?>
```

#### **Inverser une chaîne de caractères**

La fonction `strrev()` inverse une chaîne de caractères :

```text
<?php
echo strrev("Actualités des développeurs"); // affiche sretpéd ed sétiatlucA
?>
```

#### Rechercher du texte dans une chaîne de caractères

La fonction `strpos()` recherche du texte dans une chaîne de caractères :

```text
<?php
echo strpos("Actualités des développeurs", "développeurs"); // affiche 12
?>
```

#### Remplacer du texte dans une chaîne de caractères

La fonction `str_replace()` remplace du texte dans une chaîne de caractères :

```text
<?php
echo str_replace("freeCodeCamp", "Développeur", "freeCodeCamp News"); // affiche Développeur News
?>
```

## Constantes

Les constantes sont un type de variable en PHP. La fonction `define()` pour définir une constante prend trois arguments - le nom de la clé, la valeur de la clé, et un booléen (vrai ou faux) qui détermine si le nom de la clé est insensible à la casse (faux par défaut). La valeur d'une constante ne peut pas être modifiée une fois qu'elle est définie. Elle est utilisée pour des valeurs qui changent rarement (par exemple un mot de passe de base de données ou une clé API).

### Portée

Il est important de savoir que contrairement aux variables, les constantes ont TOUJOURS une portée globale et peuvent être accessibles depuis n'importe quelle fonction dans le script.

```php
<?php
define("freeCodeCamp", "Apprendre à coder et aider les associations", false);
echo freeCodeCamp;
>?

// Sortie : Apprendre à coder et aider les associations
```

De plus, lorsque vous créez des classes, vous pouvez déclarer vos propres constantes.

```php
class Humain {
  const TYPE_HOMME = 'm';
  const TYPE_FEMME = 'f';
  const TYPE_INCONNU = 'u'; // Lorsque l'utilisateur n'a pas sélectionné son genre
  
  .............
}
```

**Note :** Si vous voulez utiliser ces constantes à l'intérieur de la classe `Humain`, vous pouvez les référer comme `self::NOM_CONSTANTE`. Si vous voulez les utiliser en dehors de la classe, vous devez les référer comme `Humain::NOM_CONSTANTE`.

## Opérateurs

PHP contient tous les opérateurs normaux que l'on s'attend à trouver dans un langage de programmation.

Un seul = est utilisé comme opérateur d'assignation et un double == ou triple === est utilisé pour la comparaison.

Les habituels < et > peuvent également être utilisés pour la comparaison et += peut être utilisé pour ajouter une valeur et l'assigner en même temps.

Le plus notable est l'utilisation du . pour concaténer des chaînes de caractères et .= pour ajouter une chaîne de caractères à la fin d'une autre.

Nouveau dans PHP 7.0.X est l'opérateur Spaceship (<=>). L'opérateur Spaceship retourne -1, 0 ou 1 lorsque $a est inférieur, égal ou supérieur à $b.

```php
<?php

echo 1 <=> 1; // 0
echo 1 <=> 2; // -1
echo 2 <=> 1; // 1
```

## Instructions If / Else / Elseif

If / Else est une instruction conditionnelle où, en fonction de la véracité d'une condition, différentes actions seront effectuées.

**Note :** Les accolades `{}` ne sont nécessaires que si la condition a plus d'une instruction d'action ; cependant, il est considéré comme une bonne pratique de les inclure quoi qu'il en soit.

### Instruction If

```text
<?php

  if (condition) {
    instruction1;
    instruction2;
  }
```

**Note :** Vous pouvez imbriquer autant d'instructions dans un bloc "if" que vous le souhaitez ; vous n'êtes pas limité au nombre dans les exemples.

### Instruction If/Else

```text
<?php

  if (condition) {
    instruction1;
    instruction2;
  } else {
    instruction3;
    instruction4;
  }
```

**Note :** L'instruction `else` est facultative.

### Instruction If/Elseif/Else

```text
<?php

  if (condition1) {
    instruction1;
    instruction2;
  } elseif (condition2) {
    instruction3;
    instruction4;
  } else {
    instruction5;
  }
```

**Note :** `elseif` doit toujours être écrit comme un seul mot.

### Instruction If/Else imbriquée

```text
<?php

  if (condition1) {
      if (condition2) {
        instruction1;
        instruction2;
      } else {
        instruction3;
        instruction4;
      }
  } else {
      if (condition3) {
        instruction5;
        instruction6;
      } else {
        instruction7;
        instruction8;
      }
  }
```

### Conditions multiples

Plusieurs conditions peuvent être utilisées simultanément avec les opérateurs logiques "ou" (||), "xor", et "et" (&&).

Par exemple :

```text
<?php

  if (condition1 && condition2) {
    echo 'Les deux conditions sont vraies !';
  } elseif (condition1 || condition2) {
    echo 'Une condition est vraie !';
  } else (condition1 xor condition2) {
    echo 'Une condition est vraie, et une condition est fausse !';
  }
```

**Note :** Il est bon de mettre chaque condition individuelle entre parenthèses lorsque vous en avez plus d'une (cela peut améliorer la lisibilité).

### Syntaxe alternative If/Else

Il existe également une syntaxe alternative pour les structures de contrôle

```php
  if (condition1):
    instruction1;
  else:
    instruction5;
  endif;
```

### Opérateurs ternaires

Les opérateurs ternaires sont essentiellement des instructions if / else sur une seule ligne.

Supposons que vous devez afficher "Bonjour (nom d'utilisateur)" si un utilisateur est connecté, et "Bonjour invité" s'il n'est pas connecté.

**Instruction If / Else :**

```text
if($user == !NULL {
  $message = 'Bonjour '. $user; 
} else {
  $message = 'Bonjour invité';
}
```

**Opérateur ternaire :**

```text
$message = 'Bonjour '.($user == !NULL ? $user : 'Invité');
```

## Switch

En PHP, l'instruction `Switch` est très similaire à l'instruction `Switch` de JavaScript (voir ce [guide de l'instruction switch en JavaScript](https://www.freecodecamp.org/news/javascript-switch-case-js-switch-statement-example/) pour comparer et contraster). Elle permet des tests de cas rapides avec de nombreuses conditions possibles, le code est également plus lisible.

```php
<?php
	// Exemple d'instruction Switch
	switch ($i) {
    	case "free":
    	    echo "i est free";
    	    break;
    	case "code":
    	    echo "i est code";
    	    break;
    	case "camp":
    	    echo "i est camp";
    	    break;
    	default:
    	    echo "i est freecodecamp";
            break;
	}
```

### Break

L'instruction `break;` quitte le switch et continue à exécuter le reste du code de l'application. Si vous n'utilisez pas l'instruction `break;`, vous pourriez finir par exécuter plusieurs cas et instructions, parfois cela peut être souhaité dans lequel cas vous ne devriez pas inclure l'instruction `break;`.

Un exemple de ce comportement peut être vu ci-dessous :

```text
<?php
    $j = 0;

    switch ($i) {
        case '2':
            $j++;
        case '1':
            $j++;
            break;
        default:
            break;
    }
```

Si $i = 1, la valeur de $j serait :

```text
1
```

Si $i = 2, la valeur de $j serait :

```text
2
```

Bien que break puisse être omis sans causer de chute dans certains cas (voir ci-dessous), il est généralement considéré comme une bonne pratique de l'inclure pour la lisibilité et la sécurité (voir ci-dessous) :

```text
<?php
    switch ($i) {
        case '1':
            return 1;
        case '2':
            return 2;
        default:
            break;
     }
```

```text
<?php
    switch ($i) {
        case '1':
            return 1;
            break;
        case '2':
            return 2;
            break;
        default:
            break;
     }
```

### Exemple

```php
<?php
//initialiser avec un entier aléatoire dans la plage
$diceNumber = mt_rand(1, 6);

//initialiser
$numText = "";

//appeler l'instruction switch
  switch($diceNumber) 
  {
  case 1:
    $numText = "Un";
    break;
  case 2:
    $numText = "Deux";
    break;
  case 3:
  case 4:
    // les cas 3 et 4 iront à cette ligne
    $numText = "Trois ou Quatre";
    break;
  case 5:
    $numText = "Cinq";
    echo $numText;
    // break; //sans spécifier break ou return, il continuera à exécuter le cas suivant.
  case 6:
    $numText = "Six";
    echo $numText;
    break;
  default:
    $numText = "inconnu";
  }
  
  //afficher le résultat
  echo 'Le dé montre le nombre '.$numText.'.';

?>
```

### Sortie

```text
si le cas est 1
> Le dé montre le nombre Un.

si le cas est 2
> Le dé montre le nombre Deux.

si le cas est 3
> Le dé montre le nombre Trois ou Quatre.

si le cas est 4
> Le dé montre le nombre Trois ou Quatre.

si le cas est 5
> CinqSixLe dé montre le nombre Six.

si le cas est 6
> SixLe dé montre le nombre Six.

si aucun des cas ci-dessus
> Le dé montre le nombre inconnu.
```

## Boucles

Lorsque vous devez répéter une tâche plusieurs fois, vous pouvez utiliser une boucle au lieu d'ajouter le même code encore et encore.

L'utilisation d'un `break` dans la boucle peut arrêter l'exécution de la boucle.

### Boucle For

Parcourir un bloc de code un nombre spécifique de fois.

```php
<?php
for($index = 0; $index < 5; $index ++)
{
    echo "Compteur de boucle actuel ".$index.".\n";
}
?>

/*
Sortie :

Compteur de boucle actuel 0.
Compteur de boucle actuel 1.
Compteur de boucle actuel 2.
Compteur de boucle actuel 3.
Compteur de boucle actuel 4.
*/
```

### Boucle While

Parcourir un bloc de code si une condition est vraie.

```php
<?php
$index = 10;
while ($index >= 0)
{
    echo "L'index est ".$index.".\n";
    $index--;
}
?>

/*
Sortie :

L'index est 10.
L'index est 9.
L'index est 8.
L'index est 7.
L'index est 6.
L'index est 5.
L'index est 4.
L'index est 3.
L'index est 2.
L'index est 1.
L'index est 0.
*/
```

### Boucle Do...While

Parcourir un bloc de code une fois et continuer à boucler si la condition est vraie.

```php
<?php
$index = 3;
do
{
    // exécuter ceci au moins 1 fois
    echo "Index : ".$index.".\n"; 
    $index --;
}
while ($index > 0);
?>

/*
Sortie :

Index : 3.
Index : 2.
Index : 1.
*/
```

### Boucle Foreach

Parcourir un bloc de code pour chaque valeur dans un tableau.

## Fonctions

Une fonction est un bloc d'instructions qui peut être utilisé à plusieurs reprises dans un programme.

### Fonction simple + Appel

```php
function dire_bonjour() {
  return "Bonjour !";
}

echo dire_bonjour();
```

### Fonction simple + Paramètre + Appel

```php
function dire_bonjour($ami) {
  return "Bonjour " . $ami . " !";
}

echo dire_bonjour('Tommy');
```

### strtoupper - Rend tous les caractères PLUS GRANDS ET PLUS GRANDS !

```php
function rendreGRAND($beaucoup_de_noms) {
  foreach($beaucoup_de_noms as $les_simpson) {
    $GRAND[] = strtoupper($les_simpson);
  }
  return $GRAND;
}

$beaucoup_de_noms = ['Homer', 'Marge', 'Bart', 'Maggy', 'Lisa'];
var_dump(rendreGRAND($beaucoup_de_noms));
```

## Tableaux

Les tableaux sont comme des variables régulières, mais contiennent plusieurs valeurs dans une liste ordonnée. Cela peut être utile si vous avez plusieurs valeurs qui sont toutes liées entre elles, comme une liste de noms d'étudiants ou une liste de capitales.

### Types de tableaux

En PHP, il existe deux types de tableaux : les tableaux indexés et les tableaux associatifs. Chacun a son propre usage et nous allons voir comment créer ces tableaux.

### Tableau indexé

Un tableau indexé est une liste de valeurs ordonnées. Chacune de ces valeurs dans le tableau est assignée à un numéro d'index. Les index pour les tableaux commencent toujours à `0` pour la première valeur et augmentent ensuite de un à partir de là.

```php
<?php
$liste_de_courses = array("oeufs", "lait", "fromage");
?>
```

`$liste_de_courses[0]` retournerait `"oeufs"`, `$liste_de_courses[1]` retournerait `"lait"`, et `$liste_de_courses[2]` retournerait `"fromage"`.

### Tableau associatif

Un tableau associatif est une liste de valeurs qui sont accessibles via une clé au lieu de numéros d'index. La clé peut être n'importe quelle valeur mais elle doit être unique pour le tableau.

```php
<?php
$notes_des_étudiants = array("Joe" => 83, "Frank" => "93", "Benji" => "90");
?>
```

`$notes_des_étudiants['Joe']` retournerait `83`, `$notes_des_étudiants['Frank']` retournerait `93`, `$notes_des_étudiants['Benji']` retournerait `90`.

### Tableau multidimensionnel

Un tableau multidimensionnel est un tableau qui contient d'autres tableaux. Cela vous permet de créer des structures de données complexes qui peuvent modéliser un groupe de données très complexe.

```php
<?php
$étudiants = 
  array(
    array("prénom" => "Joe", "note" => 83, "nom" => "Smith"),
    array("prénom" => "Frank", "note" => 92, "nom" => "Barbson"),
    array("prénom" => "Benji", "note" => 90, "nom" => "Warner")   
  );
?>
```

Maintenant vous pouvez obtenir le `prénom` du premier étudiant avec :

```php
$étudiants[0]['prénom']
```

### Obtenir la longueur d'un tableau - La fonction count()

La fonction `count()` est utilisée pour retourner la longueur (le nombre d'éléments) d'un tableau :

```php
<?php
$voitures = array("Volvo", "BMW", "Toyota");
echo count($voitures);
?>
```

## Tri des tableaux

PHP offre plusieurs fonctions pour trier les tableaux. Cette page décrit les différentes fonctions et inclut des exemples.

### sort()

La fonction `sort()` trie les valeurs d'un tableau dans l'ordre alphabétique/numérique croissant (par exemple A, B, C, D, E... 1, 2, 3, 4, 5...)

```php
<?php
$freecodecamp = array("free", "code", "camp");
sort($freecodecamp);
print_r($freecodecamp);
?>
```

**Sortie :**

```text
Array
(
    [0] => camp
    [1] => code
    [2] => free
)
```

### rsort()

La fonction `rsort()` trie les valeurs d'un tableau dans l'ordre alphabétique/numérique décroissant (par exemple Z, Y, X, W, V... 5, 4, 3, 2, 1...)

```php
<?php
$freecodecamp = array("free", "code", "camp");
rsort($freecodecamp);
print_r($freecodecamp);
?>
```

**Sortie :**

```text
Array
(
    [0] => free
    [1] => code
    [2] => camp
)
```

### asort()

La fonction `asort()` trie un tableau associatif, par ses valeurs, dans l'ordre alphabétique/numérique croissant (par exemple A, B, C, D, E... 1, 2, 3, 4, 5...)

```php
<?php
$freecodecamp = array("zero"=>"free", "one"=>"code", "two"=>"camp");
asort($freecodecamp);
print_r($freecodecamp);
?>
```

**Sortie :**

```text
Array
(
    [two] => camp
    [one] => code
    [zero] => free
)
```

### ksort()

La fonction `ksort()` trie un tableau associatif, par ses clés, dans l'ordre alphabétique/numérique croissant (par exemple A, B, C, D, E... 1, 2, 3, 4, 5...)

```php
<?php
$freecodecamp = array("zero"=>"free", "one"=>"code", "two"=>"camp");
ksort($freecodecamp);
print_r($freecodecamp);
?>
```

**Sortie :**

```text
Array
(
    [one] => code
    [two] => camp
    [zero] => free
)
```

### arsort()

La fonction `arsort()` trie un tableau associatif, par ses valeurs, dans l'ordre alphabétique/numérique décroissant (par exemple Z, Y, X, W, V... 5, 4, 3, 2, 1...)

```php
<?php
$freecodecamp = array("zero"=>"free", "one"=>"code", "two"=>"camp");
arsort($freecodecamp);
print_r($freecodecamp);
?>
```

**Sortie :**

```text
Array
(
    [zero] => free
    [one] => code
    [two] => camp
)
```

### krsort()

La fonction `krsort()` trie un tableau associatif, par ses clés dans l'ordre alphabétique/numérique décroissant (par exemple Z, Y, X, W, V... 5, 4, 3, 2, 1...)

```php
<?php
$freecodecamp = array("zero"=>"free", "one"=>"code", "two"=>"camp");
krsort($freecodecamp);
print_r($freecodecamp);
?>
```

**Sortie :**

```text
Array
(
    [zero] => free
    [two] => camp
    [one] => code
)
```

## Formulaires

Les formulaires sont un moyen pour les utilisateurs de saisir des données ou de sélectionner des données depuis la page web. Les formulaires peuvent stocker des données ainsi que permettre la récupération des informations pour une utilisation ultérieure.

Pour faire fonctionner un formulaire dans des langages comme PHP, vous avez besoin de certains attributs de base en HTML. Dans la plupart des cas, PHP utilise les variables super globales 'post' et 'get' pour obtenir les données du formulaire.

```html
<html>
<body>
  <form method="get" action="target_processeur.php">
      <input type="search" name="search" /><br />
      <input type="submit" name="submit" value="Rechercher" /><br />
  </form>
<body>
</html>
```

L'attribut 'method' ici indique au formulaire la manière d'envoyer les données du formulaire. Ensuite, l'attribut 'action' indique où envoyer les données du formulaire pour traitement. Maintenant, l'attribut 'name' est très important et il doit être unique car dans PHP la valeur du nom fonctionne comme l'identité de ce champ d'entrée.

## Vérification des entrées requises

PHP dispose de quelques fonctions pour vérifier si les entrées requises ont été satisfaites. Ces fonctions sont `isset`, `empty`, et `is_numeric`.

### Vérification du formulaire pour s'assurer qu'il est défini

La fonction `isset` vérifie si le champ a été défini et n'est pas null. Exemple :

```php
$firstName = $_GET['firstName']

if(isset($firstName)){
  echo "Le champ firstName est défini". "<br>";
}
else{
  echo "Le champ n'est pas défini."."<br>";
}
```

## Gestion des entrées de formulaire

On peut obtenir les entrées de formulaire avec les variables globales $_POST et $_GET.

```text
$_POST["prenom"] ou $_GET['nom']
```