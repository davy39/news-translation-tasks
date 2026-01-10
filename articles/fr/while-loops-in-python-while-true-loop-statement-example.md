---
title: Les boucles While en Python – Exemple de l'instruction While True
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-07-19T16:23:27.000Z'
originalURL: https://freecodecamp.org/news/while-loops-in-python-while-true-loop-statement-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/alex-knight-j4uuKnN43_M-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Les boucles While en Python – Exemple de l'instruction While True
seo_desc: "Python has many tools and features that can help you automate repetitive\
  \ tasks.\nOne of those features is loops.\nLoops are a helpful and frequently used\
  \ feature in all modern programming languages. \nLoops are helpful when you want\
  \ to automate a specif..."
---

Python dispose de nombreux outils et fonctionnalités qui peuvent vous aider à automatiser des tâches répétitives.

L'une de ces fonctionnalités est les boucles.

Les boucles sont une fonctionnalité utile et fréquemment utilisée dans tous les langages de programmation modernes. 

Les boucles sont utiles lorsque vous souhaitez automatiser une tâche répétitive spécifique ou éviter de copier et coller le même code dans votre programme.

En programmation informatique, les boucles répètent le même bloc de code ou la même séquence d'instructions plusieurs fois jusqu'à ce qu'une condition soit remplie ou jusqu'à ce qu'une condition ne soit plus remplie.  

Ainsi, en résumé, les boucles vous évitent d'écrire le même code encore et encore.

Il existe deux types de boucles intégrées dans Python :

- les boucles `for`.
- les boucles `while`.

Dans cet article, vous apprendrez à construire des boucles `while`.

Voici ce que nous allons couvrir :

1. [Qu'est-ce qu'une boucle `while` ?](#definition)
    1. [Syntaxe d'une boucle `while`](#syntaxe)
    2. [Exemple d'une boucle `while`](#exemple)
2. [Qu'est-ce qu'une boucle `while True` ?](#while-true)


## Qu'est-ce qu'une boucle `while` en Python ? Une définition pour débutants <a name="definition"></a>

Une boucle `while` répète un bloc de code un nombre inconnu de fois jusqu'à ce qu'une condition ne soit plus remplie. Les boucles `for`, en revanche, répètent un bloc de code un nombre fixe de fois. 

Ainsi, une boucle `while` est utile lorsque vous ne savez pas combien de fois vous voulez qu'un bloc de code s'exécute au préalable.

Une boucle `while` répète le bloc de code en fonction d'une condition booléenne donnée.

Une condition booléenne est une condition qui évalue à `True` ou `False`. 

Une boucle `while` vérifiera toujours d'abord la condition avant de s'exécuter. Si la condition évalue à `True`, alors la boucle exécutera le code dans le corps de la boucle et continuera à exécuter le code tant que la condition reste `True`.

Elle continuera à exécuter l'ensemble souhaité d'instructions de code jusqu'à ce que cette condition ne soit plus `True`.

Prenons un exemple hypothétique.

Vous pouvez demander à un utilisateur de soumettre un mot-clé secret pour qu'il puisse accéder à une partie spécifique de votre site. 

Disons que pour qu'ils puissent voir un certain contenu, ils doivent d'abord entrer le mot-clé 'Python'.

Pour ce faire, vous leur demanderez d'entrer ce mot-clé. Cela dit, vous ne savez pas combien de fois l'utilisateur entrera le mauvais mot-clé. 

Chaque fois qu'ils entrent le mauvais, vous continuez à leur demander le bon mot-clé. Et tant qu'ils entrent le mauvais mot-clé, vous ne leur permettrez pas de continuer. 

Lorsque ils entrent enfin le mot-clé 'Python', vous leur permettrez de voir ce contenu, vous cesserez de leur demander, et ce bloc de code cessera de s'exécuter.

Pour faire quelque chose de similaire à cet exemple, vous devriez utiliser la boucle `while` de Python.

### Comment écrire une boucle `while` en Python - Une analyse syntaxique pour débutants <a name="syntaxe"></a>

La syntaxe générale pour écrire une boucle `while` en Python ressemble à ceci :

```
while condition:
    corps de la boucle while contenant du code qui fait quelque chose
```

Décomposons cela :

- Vous commencez la boucle `while` en utilisant le mot-clé `while`.
- Ensuite, vous ajoutez une condition qui sera une expression booléenne. Une expression booléenne est une expression qui évalue à `True` ou `False`.
- La condition est suivie d'un deux-points, `:`.
- Sur une nouvelle ligne, vous ajoutez un niveau d'indentation. De nombreux éditeurs de code le feront automatiquement pour vous. Par exemple, lorsque vous utilisez l'éditeur [Visual Studio Code](https://code.visualstudio.com/) avec l'[extension Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python), juste après avoir écrit les deux-points de l'étape précédente et avoir appuyé sur `Enter`, il indentera automatiquement votre code avec le bon niveau d'indentation. Ce niveau d'indentation est la façon dont Python sait que les instructions de code que vous allez écrire sont associées à l'instruction `while`.
- Ensuite, le code que vous voulez exécuter va dans le corps de l'instruction `while`.
- Tant que la condition évalue à `True`, le code à l'intérieur du corps de la boucle `while` s'exécutera. Le code à l'intérieur du corps continuera à s'exécuter jusqu'à ce que la condition ne soit plus remplie et évalue à `False`.

### Quel est un exemple de boucle `while` en Python ? <a name="exemple"></a>

Maintenant, écrivons l'exemple que j'ai mentionné précédemment en utilisant une boucle while en Python.

Tout d'abord, je vais stocker le mot-clé secret `Python` dans une variable nommée `secret_keyword`.

```python
secret_keyword = "Python"
```

Ensuite, je vais demander à l'utilisateur d'entrer le mot-clé secret requis qu'il est censé connaître pour accéder au reste du contenu.

Pour ce faire, je vais utiliser la fonction `input()` et stocker le résultat dans une variable nommée `user_input`.

```python
user_input = input("Veuillez entrer le mot-clé secret : ")
```

Une chose à noter ici est que la saisie de l'utilisateur est par défaut sensible à la casse, ce qui signifie que si l'utilisateur entre 'python' au lieu de 'Python', il ne pourra toujours pas continuer.

Pour corriger cela, vous pouvez utiliser une méthode de chaîne telle que `.capitalize()` pour mettre en majuscule la première lettre du mot que l'utilisateur entre.

```python
user_input = input("Veuillez entrer le mot-clé secret : ").capitalize()
```

Ensuite, il est temps de construire la boucle `while`. 

Je vais vérifier si la variable `user_input` n'est *pas* égale au contenu de la variable `secret_keyword`. 

Essentiellement, je vérifie si ce que l'utilisateur a entré n'est pas égal à la chaîne 'Python'.

Pour écrire cette condition en Python, je vais utiliser l'opérateur `!=`, qui vérifie l'inégalité.

```python
secret_keyword = "Python"

user_input = input("Veuillez entrer le mot-clé secret : ").capitalize()

while user_input != secret_keyword:
```

À l'intérieur du corps de la boucle `while`, je vais à nouveau demander à l'utilisateur d'entrer le mot-clé secret.

```python
secret_keyword = "Python"

user_input = input("Veuillez entrer le mot-clé secret : ").capitalize()

while user_input != secret_keyword:
    user_input = input("Veuillez entrer le mot-clé secret : ").capitalize()
```

Le fonctionnement est le suivant : si l'utilisateur entre la chaîne 'Python', la boucle se terminera et le programme ne s'exécutera plus. Cependant, si la chaîne que l'utilisateur entre n'est pas égale à 'Python', la boucle continuera.

Ainsi, si `user_input` n'est *pas* égal à `secret_keyword`, la boucle continuera à s'exécuter. 

Et il n'y a pas de nombre défini de fois où cela s'exécutera puis s'arrêtera, ce qui signifie que tant que l'utilisateur *ne* saisit *pas* la chaîne 'Python', la boucle `while` continuera à s'exécuter. Cela est dû au fait que la condition que j'ai définie continue à évaluer à `True`.


```
Veuillez entrer le mot-clé secret : Bonjour
Veuillez entrer le mot-clé secret : Salut
Veuillez entrer le mot-clé secret : CSS
Veuillez entrer le mot-clé secret : css
Veuillez entrer le mot-clé secret :
..
..
..
```

Si vous suivez et souhaitez terminer le programme, tapez `Control C` pour échapper à la boucle infinie. Une boucle infinie est lorsque une boucle ne s'arrête jamais d'exécuter.

Maintenant, si je relance le programme et entre enfin le bon mot-clé secret, la boucle se terminera et le code cessera de s'exécuter.

```
Veuillez entrer le mot-clé secret : Java
Veuillez entrer le mot-clé secret : Python
```

Et cela se produit également si j'entre 'python' grâce à la méthode `capitalize()` :

```
Veuillez entrer le mot-clé secret : java
Veuillez entrer le mot-clé secret : python
```

La boucle se termine car la condition n'évalue plus à `True`.

## Qu'est-ce qu'une boucle `while True` en Python ? <a name="while-true"></a>

Plus tôt, vous avez vu ce qu'est une boucle infinie.

Essentiellement, une boucle `while True` est une boucle qui est continuellement `True` et donc s'exécute indéfiniment. Elle ne s'arrêtera jamais à moins que vous ne la forciez à s'arrêter.

```python
#ci-ce crée une boucle infinie

while True:
    print("Je suis toujours vrai")
```

Comme vous l'avez vu précédemment, la façon de sortir de cela est de taper `Control C`.

Une autre façon de sortir explicitement de cela est d'utiliser l'instruction `break`.

Puisque `True` évaluera toujours à `True` et donc s'exécutera de manière répétée, l'instruction `break` forcerait la boucle à s'arrêter lorsque cela est nécessaire.

Prenons l'exemple suivant :

```python
i = 0

#ci-ce crée une boucle infinie

while True:
    print(i)
    i = i + 1
```

Dans cet exemple, `i` continuera à augmenter de un de manière répétée – il n'y a pas de condition pour l'empêcher d'augmenter puisque `True` évaluera toujours à `True`.

Pour empêcher cela d'être une boucle infinie, j'introduis d'abord une instruction `if`.

L'instruction `if` vérifie si `i` est égal à `5`. Si c'est le cas, alors la boucle prendra fin grâce à l'instruction `break` à l'intérieur de l'instruction `if`, qui indique essentiellement à la boucle de s'arrêter.

```python
i = 0

while True:
    print(i)
    i = i + 1

    if i == 5:
        break
```

## Conclusion

Et voilà ! Vous savez maintenant comment écrire des boucles `while` et `while True` en Python.

J'espère que vous avez trouvé ce tutoriel utile.

Pour en savoir plus sur le langage de programmation Python, consultez la [certification Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) de freeCodeCamp.

Vous commencerez par les bases et apprendrez de manière interactive et adaptée aux débutants. Vous construirez également cinq projets à la fin pour mettre en pratique et renforcer ce que vous avez appris.

Merci d'avoir lu et bon codage !