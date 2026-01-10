---
title: Bonjour le monde ! À la manière Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-06T07:26:11.000Z'
originalURL: https://freecodecamp.org/news/hello-world-the-pythonic-way-ea006c56038c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FkG7dPq9aReiWXbrcmL_1g.png
tags:
- name: learning
  slug: learning
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Bonjour le monde ! À la manière Python
seo_desc: 'By Thomas Noe

  Hello world

  The first program developers are often introduced to is the infamous Hello World.
  It doesn’t matter what language you’re using, you have probably seen one. If not
  in a tutorial, than out in the wild.

  The why

  This post is to ...'
---

Par Thomas Noe

### Bonjour le monde

Le premier programme auquel les développeurs sont souvent initiés est le célèbre Bonjour le monde. Peu importe le langage que vous utilisez, vous en avez probablement déjà vu un. Si ce n'est pas dans un tutoriel, alors peut-être dans la nature.

#### Le pourquoi

Ce post est pour célébrer l'expansion de [Free Code Camp](https://www.freecodecamp.com) vers la prise en charge de Python, parmi d'autres langages cool. Consultez l'[annonce](https://medium.freecodecamp.com/java-ruby-and-go-oh-my-6b5577ba2bc2) par vous-même.

Notez que ce post n'est pas destiné à être un tutoriel pour les tout nouveaux programmeurs. J'ai inclus des liens pour aider les lecteurs à commencer avec Python.

### Montrez-moi du code

Assez parlé. Regardons comment vous écriviez Bonjour le monde en Python. Prenez une grande inspiration. Et c'est parti.

#### Python3

```
print('Bonjour le monde!');
```

Fascinant, n'est-ce pas ? Ceux d'entre vous qui sont habitués à JavaScript ne seront peut-être pas très impressionnés. L'exemple Bonjour le monde en JS ne serait pas très différent.

#### JavaScript

```
console.log('Bonjour le monde!');
```

#### Ruby

Celui de Ruby est dans le même registre

```
puts "Bonjour le monde!"
```

Pour mettre la simplicité de ceux-ci en contexte, regardons deux autres exemples.

#### C

```
#include <stdio.h>
```

```
int main(int argc, char* argv[]){    printf("Bonjour le monde!\n");    return 0;}
```

#### Java

```
public class BonjourMonde {    public static void main(String[] args) {        System.out.prinln("Bonjour le monde!");    }}
```

Il y a eu un changement au cours des dernières années où la communauté de la programmation a commencé à pencher vers les trois premiers langages comme langages d'introduction plutôt que les deux derniers. Peut-être que ces Bonjour le monde vous donnent un petit aperçu du pourquoi. Qu'en pensez-vous ?

D'accord, retour à Python.

### Qu'en est-il de cette chose Pythonique ?

Je vais utiliser cette dernière section pour effleurer la surface de ce que signifie le mot Pythonique et nous allons regarder un Bonjour le monde Pythonique.

#### Qu'est-ce que c'est que ce Pythonique ?

Lorsque les gens pensent à cette question, ils peuvent penser à l'exemple célèbre de Python

```
import this
```

qui, lorsqu'il est exécuté, vous donne ceci :

```
Beautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!
```

Prenez-en ce que vous voulez. Concentrons-nous sur une ligne du texte.

> Il devrait y avoir une -- et de préférence une seule -- façon évidente de le faire.

Pour moi, cette ligne décrit la mentalité derrière le mot Pythonique et le Python idiomatique.

Si vous vous endormez devant le clavier, au moins [ajoutez ceci à votre liste de lecture](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html).

#### Ne devrait-il pas toujours y avoir 'une seule façon de le faire' ?

C'est à vous de décider. Peu importe le langage que vous utilisez. Regardons un exemple de la communauté Perl (que Ruby a hérité.)

> **Il y a plus d'une façon de le faire** (**TMTOWTDI** ou **TIMTOWTDI**, prononcé _Tim Toady_)

[**Il y a plus d'une façon de le faire - Wikipedia, l'encyclopédie libre**](https://en.wikipedia.org/wiki/There's_more_than_one_way_to_do_it)  
[_Il y a plus d'une façon de le faire (TMTOWTDI ou TIMTOWTDI, prononcé Tim Toady) est une devise de programmation Perl. Le
2026_en.wikipedia.org](https://en.wikipedia.org/wiki/There's_more_than_one_way_to_do_it)

(TIL il y a une prononciation !)

#### Retour au code

Sautons le reste de la leçon de philosophie et plongeons dans l'exemple de code Bonjour le monde Pythonique. Je vais inclure une fonction très basique (_oh my!_) pour que ce ne soit pas si confus lorsque nous regarderons les lignes.

# est ainsi que vous commencez un commentaire Python

```
# section un
def main():  print("Bonjour le monde!")
```

```
# section deux
```

```
if __name__ == "__main__":  main()
```

D'accord ?

#### Décomposons-le

**Section une**

```
def main():  print("Bonjour le monde!")
```

définir une fonction qui ne prend aucun argument et ne retourne aucune valeur nommée main

afficher Bonjour le monde! sur la console lorsque main est appelée

**Section deux**

```
if __name__ == "__main__":  main()
```

__name__ est assigné au module appelant...

En bref :

* si le module est importé, __name__ sera défini sur le module importateur
* si le fichier est exécuté directement, alors exécuter l'instruction if

Regardons un autre exemple modifié avant de conclure

```
# fcc-greet.py
```

```
def greet(name):  print("Bonjour {}, bienvenue à Free Code Camp!".format(name))
```

```
if __name__ == "__main__":  from sys import argv  greet(argv[1]) # premier argument de commande
```

L'instruction print et la dernière ligne peuvent être un peu trop pour certains nouveaux utilisateurs. Au lieu de les expliquer, je vais vous montrer deux façons différentes d'utiliser notre nouveau programme Python.

La première est via le terminal/invite de commande :

```
$ python fcc-greet.py t3h2mas
```

qui imprime ceci sur la console

> Bonjour t3h2mas, bienvenue à Free Code Camp!

Utilisation de `fcc-greet.py` comme module :

```
# my-program.py
```

```
import fcc-greet
```

```
users = ["t3h2mas", "BoilingOil", "mamptecnocrata"]map(fcc-greet.greet, users)
```

_merci aux utilisateurs ci-dessus pour leur permission d'utiliser leur nom d'utilisateur :+1:_

ce qui donnerait

> Bonjour t3h2mas, bienvenue à Free Code Camp!

> Bonjour BoilingOil, bienvenue à Free Code Camp!

> Bonjour mamptecnocrata, bienvenue à Free Code Camp!

Cet dernier exemple peut avoir un peu trop de choses en cours. Concentrez-vous simplement sur la sortie !

Cela complète notre programme d'exemple utilisant des idiomes Pythoniques. Nous avons terminé avec un programme qui peut être appelé à partir de l'invite avec un argument fourni ainsi qu'être utilisé comme un module facilement à partir de différents programmes.

### Conclusion

Cela conclut notre petit aperçu de Python idiomatique. Ce post était destiné à être une lecture complémentaire plutôt qu'un tutoriel complet. La communauté Python sait certainement ce qu'elle aime. Voir

_guide de style Python pep8_

[**Bienvenue sur Python.org**](https://www.python.org/dev/peps/pep-0008/)  
[_Ce document donne des conventions de codage pour le code Python comprenant la bibliothèque standard dans le principal Python
2026_www.python.org](https://www.python.org/dev/peps/pep-0008/)

_pep257_

[**Bienvenue sur Python.org**](https://www.python.org/dev/peps/pep-0257/)  
[_Le but de ce PEP est de standardiser la structure de haut niveau des docstrings : ce qu'elles doivent contenir, et comment le dire
2026_www.python.org](https://www.python.org/dev/peps/pep-0257/)

pour plus de guides Pythoniques.

#### Nouveau sur Python ?

Cela semble être un bon point de départ

[**Commencer avec python - The Python Guru**](http://thepythonguru.com/getting-started-with-python/)  
[_Python est un langage de programmation polyvalent créé par Guido Van Rossum. Python est surtout loué pour son élégance
2026_thepythonguru.com](http://thepythonguru.com/getting-started-with-python/)

Voici une grande liste de tutoriels...

Pour les programmeurs :

[**BeginnersGuide/Programmers - Python Wiki**](https://wiki.python.org/moin/BeginnersGuide/Programmers)  
[_Parce que c'est une page Wiki, les utilisateurs peuvent l'éditer. Vous êtes donc libre d'ajouter des détails de matériel que d'autres Python
2026_wiki.python.org](https://wiki.python.org/moin/BeginnersGuide/Programmers)

Pour les débutants

[**BeginnersGuide/NonProgrammers - Python Wiki**](https://wiki.python.org/moin/BeginnersGuide/NonProgrammers)  
[_Si vous n'avez jamais programmé auparavant, les tutoriels sur cette page sont recommandés pour vous ; ils ne supposent pas que vous avez
2026_wiki.python.org](https://wiki.python.org/moin/BeginnersGuide/NonProgrammers)

#### Communautés Python

**Reddit :**

[**Python Education * /r/learnpython**](http://reddit.com/r/learnpython)  
[_Subreddit pour poster du contenu, des questions, et demander des conseils généraux sur l'apprentissage du langage de programmation Python._reddit.com](http://reddit.com/r/learnpython)[**Python * /r/Python**](http://reddit.com/r/python)  
[_nouvelles sur le langage de programmation dynamique, interprété, interactif, orienté objet, extensible Python_reddit.com](http://reddit.com/r/python)[**learn programming * /r/learnprogramming**](http://reddit.com/r/learnprogramming)  
[_Un subreddit pour toutes les questions liées à la programmation dans n'importe quel langage._reddit.com](http://reddit.com/r/learnprogramming)

**Gitter :**

[**FreeCodeCamp/FreeCodeCamp**](http://gitter.im/FreeCodeCamp/FreeCodeCamp)  
[_Bienvenue dans notre salle de chat principale. Nous avons de nombreuses salles de chat officielles pour traîner et obtenir de l'aide. Voici la liste
2026_gitter.im](http://gitter.im/FreeCodeCamp/FreeCodeCamp)[**FreeCodeCamp/python**](http://gitter.im/FreeCodeCamp/Python)  
[_C'est le meilleur endroit pour discuter de Python et obtenir de l'aide avec. Assurez-vous de consulter https://github.com/freecodecamp
2026_gitter.im](http://gitter.im/FreeCodeCamp/Python)

IRC :

[**Python.org -IRCGuide**](https://www.python.org/community/irc/)  
[_La maison officielle du langage de programmation Python_www.python.org](https://www.python.org/community/irc/)