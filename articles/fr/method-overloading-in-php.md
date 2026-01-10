---
title: Comment fonctionne la surcharge de méthodes en PHP
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2023-05-15T17:11:35.000Z'
originalURL: https://freecodecamp.org/news/method-overloading-in-php
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/kisscc0-line-art-drawing-drum-cartoon-overload-5b74068a69e855.7493203415343305064338.png
tags:
- name: PHP
  slug: php
seo_title: Comment fonctionne la surcharge de méthodes en PHP
seo_desc: "As software engineers, we sometimes have to perform certain tasks that\
  \ can be achieved with a variable number of inputs. \nTo solve this problem, you\
  \ can create multiple functions to solve for the different possible number of inputs.\
  \ Or we can write a..."
---

En tant qu'ingénieurs logiciels, nous devons parfois effectuer certaines tâches qui peuvent être réalisées avec un nombre variable d'entrées. 

Pour résoudre ce problème, vous pouvez créer plusieurs fonctions pour résoudre les différents nombres possibles d'entrées. Ou nous pouvons écrire une grande fonction pour résoudre ce problème. 

Une meilleure façon de procéder est de créer différentes variations d'une fonction simple pour résoudre les différents scénarios que vous avez.

Dans ce tutoriel, vous apprendrez comment PHP vous permet de résoudre facilement ce problème en utilisant la surcharge de méthodes et comment vous pouvez utiliser ces variations.

## Qu'est-ce que le polymorphisme ?

Le polymorphisme est un mot grec qui signifie littéralement plusieurs formes. En termes de programmation, il est défini comme la capacité des objets de différentes classes à répondre différemment en fonction du même message. 

Le polymorphisme est le concept qui permet aux classes de partager la même interface et d'avoir différentes définitions pour la même méthode. Le polymorphisme est l'un des concepts clés de la programmation orientée objet (POO).

## Qu'est-ce que la surcharge de méthodes ?

La surcharge de méthodes est un concept qui vous permet d'avoir une méthode qui peut se comporter différemment en fonction de son nombre de paramètres. Elle vous permet d'avoir plusieurs définitions pour une même méthode dans la même classe.  

Cette méthode aura le même nom pour toutes ses utilisations, mais pourrait produire des résultats différents dans différentes situations. La surcharge de méthodes est un concept clé sous l'égide du polymorphisme.

### Surcharge traditionnelle

Par exemple, disons que vous avez une méthode `add` que vous souhaitez utiliser pour additionner quelques nombres de ces manières :

```php
function add(int $a, int $b): int
{
	return $a + $b;
}

function add(int $a, int $b, int $c): int
{
	$sum = $a + $b + $c;
	return $sum > 10 ? 10 : $sum;
}
```

Dans la première définition, la méthode prend deux paramètres et retourne simplement leur somme. Dans la deuxième définition, elle prend trois paramètres et retourne la somme de ceux-ci uniquement lorsque celle-ci est égale à 10 ou moins.

Maintenant, contrairement à d'autres langages de programmation, PHP ne vous permet pas vraiment de redéfinir une méthode plusieurs fois comme ceci :

```php
class SampleClass
{
	function add(int $a, int $b): int
	{
		return $a + $b;
	}

	function add(int $a, int $b, int $c): int
	{
		return $a + $b + $c > 10 ?? 10;
	}
}
```

Vous obtiendriez une erreur comme celle-ci : `PHP Fatal error:  Cannot redeclare SampleClass::add()`. Mais PHP supporte la surcharge de méthodes en utilisant un mot-clé magique, `__call`. 

### Le mot-clé `__call`

Il s'agit d'une méthode magique que PHP appelle lorsqu'il tente d'exécuter une méthode d'une classe et qu'il ne la trouve pas. Ce mot-clé magique prend deux arguments : un nom de fonction et d'autres arguments à passer à la fonction. Sa définition ressemble à ceci :

```php
function __call(string $function_name, array $arguments) {}
```

En utilisant cette méthode magique, vous pouvez créer autant de méthodes et autant de variations de chacune de ces méthodes que vous le souhaitez. 

Par exemple, pour atteindre notre objectif avec la fonction `add`, mettez à jour la définition de `__call` et votre `SampleClass` pour qu'elles ressemblent à ceci :

```php
class SampleClass
{
	function __call($function_name, $arguments)
	{
		$count = count($arguments);

		// Vérifier le nom de la fonction
		if ($function_name == 'add') {
			if ($count == 2) {
				return array_sum($arguments);
			} else if ($count == 3) {
				return array_sum($arguments) > 10 ? 10 : array_sum($arguments);
			}
		}
	}
}
```

Le code est assez explicite. Voici une explication étape par étape :

* Utilisez la méthode `count` pour savoir combien d'arguments sont passés à votre méthode. 
* Vérifiez le nom de la fonction qui est passé. Ce `__call` contiendra toutes les différentes méthodes pour lesquelles vous souhaitez créer des variations, donc le nom doit être unique et utilisé pour regrouper les variations des méthodes.
* Gérez la logique comme vous le souhaitez en fonction du nombre différent d'arguments. Ici, nous retournons la somme telle quelle lorsque nous avons deux arguments. Nous retournons la somme si elle est inférieure à 10 lorsque nous avons trois arguments.
* Lorsque vous appelez la méthode `add`, PHP recherche une méthode avec le même nom dans la classe, s'il ne la trouve pas, il appelle la méthode `__call` à la place, et c'est ainsi que le code est exécuté.

Pour appeler la méthode `add` maintenant, créez une nouvelle instance de la classe `SampleClass` et essayez-la.

```php
$sampleObject = new SampleClass;
echo $sampleObject->add(12, 12) . PHP_EOL; // Affiche 24 
echo $sampleObject->add(12, 2, 6) . PHP_EOL; // Affiche 10
```

Les deux variations fonctionnent parfaitement 
ud83e
udd73.

## Applications de la surcharge de méthodes

* Dans les fonctions de tri : La méthode peut être programmée pour se comporter différemment sans arguments, ou avec un argument, ou avec deux en fonction de ce que vous essayez de résoudre.
* Traitement des paiements : La même méthode peut être utilisée pour gérer différents processeurs de paiement. Et ces processeurs ont souvent besoin d'un nombre différent d'entrées pour fonctionner correctement. Ainsi, la méthode peut déterminer lequel utiliser en fonction du nombre d'arguments passés et réagir en conséquence.
* Enveloppes de base de données : Une classe de base de données pourrait avoir une méthode "query" qui peut gérer différents types de requêtes avec le même nom de méthode. Par exemple, la méthode "query" pourrait prendre une requête SELECT, une requête INSERT ou une requête UPDATE en tant que paramètres et exécuter la requête appropriée en fonction du paramètre passé.

## **Résumé**

J'espère que vous comprenez maintenant ce qu'est la surcharge de méthodes en PHP, et comment vous pouvez l'utiliser pour écrire de meilleures applications PHP.

Si vous avez des questions ou des conseils pertinents, n'hésitez pas à me contacter pour les partager.

Pour lire plus de mes articles ou suivre mon travail, vous pouvez me rejoindre sur [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris), et [Github](https://github.com/Zubs). C'est rapide, c'est facile, et c'est gratuit !