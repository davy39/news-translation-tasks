---
title: Tutoriel sur les f-Strings Python – Formatage de chaînes en Python expliqué
  avec des exemples de code
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-09-14T19:21:11.000Z'
originalURL: https://freecodecamp.org/news/python-f-strings-tutorial-how-to-use-f-strings-for-string-formatting
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/py-fstrings.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Python
  slug: python
seo_title: Tutoriel sur les f-Strings Python – Formatage de chaînes en Python expliqué
  avec des exemples de code
seo_desc: "When you're formatting strings in Python, you're probably used to using\
  \ the format() method. \nBut in Python 3.6 and later, you can use f-Strings instead.\
  \ f-Strings, also called formatted string literals, have a more succinct syntax\
  \ and can be super h..."
---

Lorsque vous formatez des chaînes en Python, vous êtes probablement habitué à utiliser la méthode `format()`.

Mais dans Python 3.6 et versions ultérieures, vous pouvez utiliser les _f-Strings_ à la place. Les f-Strings, également appelées _littéraux de chaîne formatés_, ont une syntaxe plus succincte et peuvent être très utiles pour le formatage de chaînes.

Dans ce tutoriel, vous apprendrez à utiliser les f-strings en Python, et quelques façons différentes de les utiliser pour formater des chaînes.

## Qu'est-ce que les f-Strings en Python ?

Les chaînes en Python sont généralement enfermées dans des guillemets doubles (`""`) ou des guillemets simples (`''`). Pour créer des f-strings, vous devez simplement ajouter un `f` ou un `F` avant les guillemets ouvrants de votre chaîne.

> Par exemple, `"This"` est une chaîne alors que `f"This"` est une f-String.

## Comment afficher des variables en utilisant les f-Strings Python

Lorsque vous utilisez des f-Strings pour afficher des variables, vous devez simplement spécifier les noms des variables à l'intérieur d'un ensemble d'accolades `{}` . Et à l'exécution, tous les noms de variables seront remplacés par leurs valeurs respectives.

> Si vous avez plusieurs variables dans la chaîne, vous devez enfermer chacun des noms de variables à l'intérieur d'un ensemble d'accolades.

La syntaxe est montrée ci-dessous :

```
f"This is an f-string {var_name} and {var_name}."
```

▶ Voici un exemple.

Vous avez deux variables, `language` et `school`, enfermées dans des accolades à l'intérieur de la f-String.

```python
language = "Python"
school = "freeCodeCamp"
print(f"I'm learning {language} from {school}.")
```

Regardons le résultat :

```
#Output
I'm learning Python from freeCodeCamp.
```

Remarquez comment les variables `language` et `school` ont été remplacées par `Python` et `freeCodeCamp`, respectivement.

## Comment évaluer des expressions avec les f-Strings Python

Comme les f-Strings sont évaluées à l'exécution, vous pouvez également évaluer des expressions Python valides à la volée.

▶ Dans l'exemple ci-dessous, `num1` et `num2` sont deux variables. Pour calculer leur produit, vous pouvez insérer l'expression `num1 * num2` à l'intérieur d'un ensemble d'accolades.

```python
num1 = 83
num2 = 9
print(f"The product of {num1} and {num2} is {num1 * num2}.")
```

Remarquez comment `num1 * num2` est remplacé par le produit de `num1` et `num2` dans le résultat.

```
#Output
The product of 83 and 9 is 747.
```

J'espère que vous commencez maintenant à voir le schéma.

Dans toute f-String, `{var_name}`, `{expression}` servent de placeholders pour les variables et les expressions, et sont remplacés par les valeurs correspondantes à l'exécution.

Passez à la section suivante pour en apprendre davantage sur les f-Strings.

## Comment utiliser les conditionnelles dans les f-Strings Python

Commençons par réviser les instructions `if..else` de Python. La syntaxe générale est montrée ci-dessous :

```
if condition:
  # faire ceci si la condition est True <true_block>
else:
  # faire ceci si la condition est False <false_block>
```

Ici, `condition` est l'expression dont la valeur de vérité est vérifiée.

* Si la `condition` évalue à `True`, les instructions dans le bloc if (`<true_block>`) sont exécutées.
* Si la `condition` évalue à `False`, les instructions dans le bloc else (`<false_block>`) sont exécutées.

Il existe un équivalent plus succinct en une ligne aux blocs `if..else` ci-dessus. La syntaxe est donnée ci-dessous :

```
<true_block> if <condition> else <false_block>
```

> Dans la syntaxe ci-dessus, `<true_block>` est ce qui est fait lorsque la `condition` est `True`, et `<false_block>` est l'instruction à exécuter lorsque la condition est `False`.

Cette syntaxe peut sembler un peu différente si vous ne l'avez jamais vue auparavant. Si cela simplifie les choses, vous pouvez la lire comme, "_Faire ceci_ `si` `condition` est `True`; `sinon`, _faire ceci_".

Cela est souvent appelé l'opérateur _ternaire_ en Python car il prend 3 opérandes dans un certain sens – le _true block_, la _condition_ sous test, et le _false block_.

▶ Prenons un exemple simple en utilisant l'opérateur ternaire.

Étant donné un nombre `num`, vous souhaitez vérifier s'il est pair. Vous savez qu'un nombre est pair s'il est divisible par 2. Utilisons cela pour écrire notre expression, comme montré ci-dessous :

```python
num = 87;
print(f"Is num even? {True if num%2==0 else False}")
```

Dans l'extrait de code ci-dessus,

* `num%2==0` est la condition.
* Si la condition est `True`, vous retournez simplement `True` indiquant que `num` est effectivement pair, et `False` sinon.

```
#Output
Is num even? False
```

Dans l'exemple ci-dessus, `num` est 87, qui est impair. Par conséquent, l'instruction conditionnelle dans la f-String est remplacée par `False`.

## Comment appeler des méthodes avec les f-Strings Python

Jusqu'à présent, vous n'avez vu que comment afficher les valeurs des variables, évaluer des expressions et utiliser des conditionnelles à l'intérieur des f-Strings. Et il est temps de passer au niveau supérieur.

▶ Prenons l'exemple suivant :

```python
author = "jane smith"
print(f"This is a book by {author}.")
```

Le code ci-dessus affiche `This is a book by jane smith.`

Ne serait-ce pas mieux s'il affichait `This is a book by Jane Smith.` à la place ? Oui, et en Python, les méthodes de chaîne retournent des chaînes modifiées avec les changements requis.

> La méthode `title()` en Python retourne une nouvelle chaîne qui est formatée en cas de titre - la façon dont les noms sont généralement formatés (`First_name Last_name`).

Pour afficher le nom de l'auteur formaté en cas de titre, vous pouvez faire ce qui suit :

* utiliser la méthode `title()` sur la chaîne `author`,
* stocker la chaîne retournée dans une autre variable, et
* l'afficher en utilisant une f-String, comme montré ci-dessous :

```python
author = "jane smith"
a_name = author.title()
print(f"This is a book by {a_name}.")

#Output
This is a book by Jane Smith.
```

Cependant, vous pouvez faire cela en une seule étape avec les f-Strings. Vous devez simplement appeler la méthode `title()` sur la chaîne `author` à l'intérieur des accolades dans la f-String.

```python
author = "jane smith"
print(f"This is a book by {author.title()}.")
```

Lorsque la f-String est analysée à l'exécution,

* la méthode `title()` est appelée sur la chaîne `author`, et
* la chaîne retournée qui est formatée en cas de titre est affichée.

Vous pouvez vérifier cela dans le résultat montré ci-dessous.

```
#Output
This is a book by Jane Smith.

```

Vous pouvez placer des appels de méthodes sur n'importe quel objet Python valide à l'intérieur des accolades, et ils fonctionneront très bien.

## Comment appeler des fonctions à l'intérieur des f-Strings Python

En plus d'appeler des méthodes sur des objets Python, vous pouvez également appeler des fonctions à l'intérieur des f-Strings. Et cela fonctionne très similaire à ce que vous avez vu auparavant.

De la même manière que les noms de variables sont remplacés par des valeurs, et les expressions sont remplacées par le résultat de l'évaluation, les appels de fonctions sont remplacés par la valeur de retour de la fonction.

▶ Prenons la fonction `choice()` montrée ci-dessous :

```python
def choice(c):
  if c%2 ==0:
    return "Learn Python!"
  else:
    return "Learn JavaScript!"
```

La fonction ci-dessus retourne `"Learn Python!"` si elle est appelée avec un nombre pair comme argument. Et elle retourne `"Learn JavaScript!"` lorsque l'argument dans l'appel de fonction est un nombre impair.

▶ Dans l'exemple montré ci-dessous, vous avez une f-String qui contient un appel à la fonction choice à l'intérieur des accolades.

```python
print(f"Hello Python, tell me what I should learn. {choice(3)}")
```

Comme l'argument était un nombre impair (`3`), Python suggère que vous appreniez JavaScript, comme indiqué ci-dessous :

```
#Output
Hello Python, tell me what I should learn. Learn JavaScript!
```

Si vous appelez la fonction `choice()` avec un nombre pair, vous voyez que Python vous dit d'apprendre Python à la place. 🤒

```python
print(f"Hello Python, tell me what I should learn. {choice(10)}")
```

```
#Output
Hello Python, tell me what I should learn. Learn Python!
```

Et cela termine notre tutoriel sur une note heureuse !

## Conclusion

Dans ce tutoriel, vous avez appris comment utiliser les f-Strings pour :

* afficher les valeurs des variables,
* évaluer des expressions,
* appeler des méthodes sur d'autres objets Python, et
* faire des appels à des fonctions Python.

### Articles connexes

Voici un [article](https://www.freecodecamp.org/news/python-string-format-python-s-print-format-example/) de Jessica qui explique le formatage de chaînes en utilisant la méthode `format()`.