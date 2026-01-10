---
title: Quelle est la différence entre le codage et la programmation ?
subtitle: ''
author: Hillary Nyakundi
co_authors: []
series: null
date: '2021-03-17T16:28:00.000Z'
originalURL: https://freecodecamp.org/news/difference-between-coding-and-programming
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/key-difference-between-coding-and-programming--2-.png
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
seo_title: Quelle est la différence entre le codage et la programmation ?
seo_desc: "It took me a long time to understand what the terms programming and coding\
  \ really meant, and what each field entailed. And I'm sure I'm not the only one\
  \ who felt confused by those two terms when I was new to tech. \nFor a while I thought\
  \ that they wer..."
---

Il m'a fallu beaucoup de temps pour comprendre ce que les termes **programmation** et **codage** signifiaient vraiment, et ce que chaque domaine impliquait. Et je suis sûr de ne pas être le seul à avoir été confus par ces deux termes lorsque j'étais nouveau dans le domaine de la technologie. 

Pendant un moment, j'ai pensé qu'ils étaient la même chose, et il m'a fallu un certain temps pour comprendre qu'il y avait des différences entre ces deux "mondes". 

Dans cet article, je vais expliquer les différences de base entre le codage et la programmation et comment ils collaborent pour développer des applications et des sites.  

Alors explorons ces termes et comment les professionnels les utilisent en comprenant d'abord ce qu'ils signifient.


## Qu'est-ce que le codage ? 
![qu'est-ce que le codage](https://www.freecodecamp.org/news/content/images/2021/10/Untitled-design.png)
Vous avez peut-être vu des cours, des bootcamps ou des articles parler de codage – pourquoi l'accent est-il mis sur ce terme ?

C'est parce que l'acte réel de coder nous permet de faire toutes les choses cool que nous faisons chaque jour. Cela nous permet d'utiliser des applications mobiles, de travailler avec différents logiciels et systèmes d'exploitation, et même de jouer aux jeux que nous aimons ou de visiter le site web sur lequel vous lisez cet article. Tout cela est rendu possible grâce au codage. 

Alors, qu'est-ce que le codage en termes simples ?

Nous pouvons définir le codage comme l'acte de traduire des instructions pour un ordinateur d'un langage humain vers un langage qu'une machine peut comprendre. Ce code indique à l'ordinateur comment se comporter et quelles actions effectuer.

Si vous voulez devenir codeur, vous devrez avoir quelques connaissances de base sur les langages de programmation. Lorsque je parle de langages de programmation, je veux dire des langages comme : Python, Java, Go, PHP ou JavaScript, pour n'en citer que quelques-uns.

Voici un bon exemple de code écrit en langage Python, qui convertira tout *PDF* en *livre audio* :
```python
import PyPDF2                     # pip install pypdf
import pyttsx3                    # pip install pyttsx3
from tkinter.filedialog import *  # pip install tkinter

book = askopenfilename()
pdfReader = PyPDF2.PdfFileReader(book)

pages = pdfReader.numPages

for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()
```

## Qu'est-ce que la programmation ? 
![qu'est-ce que la programmation](https://www.freecodecamp.org/news/content/images/2021/10/fresh.png)
Vous avez probablement aussi entendu des gens dire, *"Je suis programmeur"*. Et certains d'entre eux qui utilisent ce terme comprennent ce que le terme signifie, tandis que d'autres non. Si vous ne savez pas exactement ce que signifie la programmation, essayons d'éclaircir cela en comprenant ce qu'est la programmation.

La programmation est le processus de création des instructions qui indiqueront à l'ordinateur comment effectuer une tâche particulière qui lui est donnée. Vous faites cela en utilisant des langages de programmation comme : 

![Langages de programmation](https://www.freecodecamp.org/news/content/images/2021/10/fresh--1-.png)

Lorsque nous parlons de programmation, pensez à quelque chose comme une télécommande pour votre télévision – elle attendra que vous lui donniez des instructions en appuyant sur différents boutons qui indiquent ensuite à la télévision d'effectuer une tâche spécifique (comme changer de chaîne, augmenter le volume, etc.). Eh bien, c'est la même façon dont les programmeurs peuvent instruire un ordinateur à faire diverses choses. 

Avec la programmation, vous pouvez presque tout faire – comme programmer des robots pour aider aux tâches ménagères, ou même programmer des voitures autonomes comme Tesla. 

Pour qu'un programmeur développe un programme qui implémentera son idée, il doit effectuer les étapes suivantes : 

* Planifier la structure de l'application (*à l'aide d'outils comme Trello*)
* La concevoir (*en utilisant des outils comme Figma ou Adobexd*)
* La développer (*en utilisant leur langage de programmation de choix*)
* Tester ses fonctionnalités
* La déployer (*sur des services d'hébergement gratuits ou payants*)
* La maintenir après sa finalisation.

Ainsi, comme vous pouvez le voir, nous pouvons dire que la programmation ne traite pas seulement de l'écriture réelle du code. Elle implique également l'utilisation de structures de données et d'algorithmes, et en général, elle traite de la vision plus large de la création et du développement de systèmes complexes.

## La différence entre le codage et la programmation 
![DIFFÉRENCES ENTRE LA PROGRAMMATION ET LE CODAGE](https://www.freecodecamp.org/news/content/images/2021/10/fresh--2-.png)
Nous allons diviser les différences en quatre catégories principales qui nous aideront à décomposer les concepts et à mieux les comprendre. 

### La terminologie

*__Le codage__* consiste à écrire du code dans un langage compris à la fois par les machines et les humains. Le principal objectif du codage est de fournir une communication entre les deux (humains et ordinateurs). 

*__La programmation__* implique la création d'un plan et d'une structure pour le code du programme qui suit certaines normes, avant que le code réel ne soit écrit pour effectuer la tâche qu'il doit accomplir.

### Les outils que vous utilisez

En ce qui concerne le *__codage__*, l'un de vos outils les plus importants sera votre éditeur de texte (comme le Bloc-notes, ou quelque chose de plus complexe et riche en fonctionnalités comme Visual Studio Code, Sublime, Atom ou Vim). 

Lorsque vous parlez de *__programmation__*, en revanche, vous aurez besoin de certains outils supplémentaires. En tant que programmeur, vous effectuerez des revues de documents, ferez beaucoup de planification, réfléchirez à la conception, et ainsi de suite. 

Pour vous aider dans ces tâches, vous utiliserez des outils comme des éditeurs de code plus avancés, des outils d'analyse, des débogueurs, des frameworks de modélisation, des assembleurs, des algorithmes de modélisation et plus encore.

En tant que programmeur, vous devrez avoir beaucoup d'expérience dans l'utilisation de ces outils et plus d'exposition aux processus que les développeurs utilisent pour construire des applications et d'autres produits.

### Votre niveau de connaissance

En tant que *__codeur__*, avoir des connaissances de base d'un langage de programmation et de sa syntaxe est un bon début. Une fois que vous savez comment coder dans un langage, il est plus facile d'apprendre les autres. Et encore une fois, votre principal objectif est d'écrire le code réel qui indique à la machine quoi faire.

En revanche, les *__programmeurs__* ont besoin de plus de connaissances pour commencer. Vous devrez savoir comment créer et travailler avec des algorithmes, comment concevoir des sites web, comment déboguer et tester votre code, comment gérer des projets, et bien sûr comment travailler avec des langages de programmation. 

La résolution de problèmes, la pensée critique et les compétences analytiques sont également essentielles lorsque vous développez des systèmes complexes.

### Le produit final

En tant que *__codeur__*, votre résultat attendu est généralement une solution simple qui, après compilation, donnera avec succès le résultat souhaité. Un bon exemple est celui que nous avons donné précédemment – convertir un PDF en un fichier audio. 

En revanche, un *__programmeur__* travaillera pour fournir une application complète ou un logiciel que les gens utiliseront sur le marché. Ils sont également responsables du suivi et de la maintenance de ce qu'ils construisent pour s'assurer qu'il fonctionne sans accroc.

## Comment le codage et la programmation fonctionnent ensemble
À ce stade, j'espère que vous êtes en mesure de faire la différence entre le codage et la programmation et ce que les deux traitent. Maintenant, voyons comment les deux peuvent (et doivent) travailler en étroite collaboration pour accomplir beaucoup. 

Pour mieux comprendre le comment, commençons par fournir un scénario réel où le codage et la programmation seront nécessaires pour travailler en étroite collaboration afin de produire une application complète et fonctionnelle.

Imaginez que vous avez été chargé de créer une application qui aidera à surveiller ou à suivre votre routine quotidienne ou à surveiller vos dépenses quotidiennes. En utilisant les concepts de ces deux mondes, voici comment vous accomplirez la tâche.

Vous aurez besoin d'un programmeur, qui sera capable de :
* planifier la structure de l'application (*à l'aide d'outils comme Trello*) 
* Écrire les principales fonctionnalités de l'application, ce que les utilisateurs sont censés utiliser, etc.
* Concevoir l'application (*en utilisant des outils comme Figma ou Adobexd*) 

Après avoir terminé ces étapes, le rôle du codeur entre en jeu. Ils prennent les idées créées par le programmeur et les transforment en une forme lisible par la machine en écrivant du code pour effectuer les tâches spécifiées. Après le processus magique du codage, le programmeur revient en jeu. 

Le programmeur évaluera ensuite le code et vérifiera les erreurs, exécutera des tests et vérifiera que tout fonctionne correctement et que le code donne le résultat attendu. Si tout cela est vérifié, l'application est maintenant prête pour le déploiement et la maintenance – ce qui reste entre les mains du programmeur.

Cet exemple simple explique comment les deux compétences peuvent être utilisées ensemble pour la productivité.

Et juste un dernier point : un "codeur" et un "programmeur" ne sont pas toujours deux personnes distinctes. Ils peuvent être une seule et même personne qui effectue toutes ces tâches.

## Conclusion

Où vous situez-vous dans ces deux mondes ? Il m'a fallu du temps pour comprendre ce qui m'intéressait vraiment. 

Si vous êtes plus intéressé par la logique, essayez de mettre votre énergie dans le processus complet de la programmation. Si vous aimez vraiment lire et écrire du code, alors investissez votre temps dans le codage. 

Comme nous le savons, l'informatique est un domaine très vaste et il est encore en évolution. Travaillez à trouver le chemin que vous voulez explorer et concentrez-vous dessus – assurez-vous simplement de l'apprécier et de vous amuser aussi. 

Si vous avez encore des difficultés, j'espère que cet article a éclairci certaines choses et vous a aidé à trouver votre place. 

Merci d'avoir lu jusqu'ici. Si vous avez aimé cet article, veuillez le partager pour aider un autre développeur à trouver son chemin.

Connectez-vous avec moi sur :  [Twitter](https://twitter.com/larymak1) | [LinkedIn](https://www.linkedin.com/in/hillary-nyakundi-3a64b11ab/) | [GitHub](https://github.com/larymak)

Amusez-vous à coder F49A