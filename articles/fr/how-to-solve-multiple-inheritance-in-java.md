---
title: Comment résoudre le problème de l'héritage multiple en Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-01T14:42:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-solve-multiple-inheritance-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/pexels-edward-jenner-4253062.jpg
tags:
- name: inheritance
  slug: inheritance
- name: Java
  slug: java
seo_title: Comment résoudre le problème de l'héritage multiple en Java
seo_desc: "By Nahla Davies\nJava is one of the most popular object-oriented programming\
  \ languages in use today. \nBecause it is platform-independent, you will find Java\
  \ applications on every type of device and every operating system. And because Java\
  \ is relativel..."
---

Par Nahla Davies

Java est l'un des langages de programmation orientée objet les plus populaires utilisés aujourd'hui. 

Étant indépendant de la plateforme, vous trouverez des applications Java sur tous les types d'appareils et tous les systèmes d'exploitation. Et parce que [Java est relativement facile à apprendre](https://www.freecodecamp.org/news/get-started-coding-with-java/), c'est l'un des premiers langages que de nombreux programmeurs apprennent.

Une caractéristique importante de Java que vous devez connaître est l'héritage de classe. L'héritage permet aux programmeurs d'optimiser le code en facilitant la réutilisation des classes. Lorsque vous pouvez réutiliser du code qui a déjà été testé et débogué, le cycle de vie du développement logiciel devient plus court et moins coûteux.

Bien que théoriquement un concept simple, la codification des relations d'héritage nécessite une attention aux détails. Cela est particulièrement vrai en ce qui concerne l'héritage multiple, où une seule classe enfant hérite des propriétés de plusieurs classes parent. 

Java rejette les relations d'héritage multiple car elles créent des ambiguïtés, mais il existe quelques moyens d'accomplir beaucoup des mêmes effets si vous savez quoi faire.

Dans cet article, nous examinerons les problèmes liés à l'héritage multiple et discuterons des alternatives de codage en Java.

## Terminologie de l'héritage

Parfois, pour être un programmeur performant, vous devez apprendre à résoudre des problèmes afin de trouver des solutions de contournement pour les bugs ou problèmes courants. Cela fait partie intégrante de la programmation sécurisée et intelligente. 

Un tel problème concerne l'héritage multiple (ou plutôt, son absence) en Java.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-73.png)
_[Source de l'image](https://www.tutorialspoint.com/java/java_inheritance.htm)_

Pour comprendre pleinement l'héritage en Java, vous devez vous familiariser avec la terminologie de base de l'héritage en [programmation orientée objet](https://www.freecodecamp.org/news/java-object-oriented-programming-system-principles-oops-concepts-for-beginners/) (OOP). 

* **Classe :** Les classes sont une structure de modèle fondamentale dans les langages de programmation orientée objet. Une classe définit les propriétés communes pour un groupe d'objets.
* **Classe parente :** Également connue sous le nom de classes de base ou superclasses, une classe parente est une classe extensible qui fournit des fonctionnalités à une classe enfant. C'est là que la réutilisabilité entre en jeu. Les définitions et fonctions de la classe parente sont réutilisées lors de la création de classes enfant.
* **Classe enfant :** Plus génériquement appelée sous-classe, une classe enfant hérite des fonctionnalités d'une autre classe. Les classes enfant sont des classes étendues ou dérivées.
* **Héritage :** La relation entre les classes parent et enfant.

## Types d'héritage en OOP

Il existe de nombreux langages de programmation orientée objet populaires utilisés aujourd'hui, notamment [Java, C++](https://stackoverflow.blog/2021/02/22/choosing-java-instead-of-c-for-low-latency-systems/), JavaScript, Python, PHP, Ruby et Perl. Bien que l'héritage soit un concept commun à travers ces langages OOP, tous les types d'héritage n'existent pas dans chaque langage.

Il est crucial de connaître les types généraux d'héritage et les limitations de l'héritage dans le langage spécifique que vous utilisez. Plus vous en savez sur l'héritage, plus vous serez un développeur logiciel efficace. 

Les types d'héritage pris en charge par Java incluent :

* **Héritage à niveau unique :** Lorsqu'une classe enfant dérive des fonctionnalités d'une seule classe parente.
* **Héritage multi-niveaux :** Il s'agit d'une forme hiérarchisée d'héritage à niveau unique. Dans l'héritage multi-niveaux, une classe enfant peut également agir comme une classe parente pour d'autres classes enfant. La relation entre chaque niveau est linéaire - aucune branche ne s'étend au-dessus comme dans l'héritage multiple. La classe enfant ultime a alors des fonctionnalités de chaque niveau au-dessus d'elle.
* **Héritage hiérarchique :** L'opposé de l'héritage multiple. Dans l'héritage hiérarchique, une seule classe parente a plus d'une classe enfant. Ainsi, plutôt que d'avoir des branches au-dessus, elle se ramifie en dessous.
* **Héritage hybride :** Comme son nom l'indique, l'héritage hybride est une combinaison d'autres types d'héritage.

En plus des types d'héritage ci-dessus, il existe d'autres types que Java ne prend pas en charge.

* **Héritage multiple :** Dans l'héritage multiple, une classe enfant a plus d'une classe parente. Bien que Java et [JavaScript](https://www.freecodecamp.org/news/functional-programming-in-javascript-for-beginners/) ne prennent pas en charge l'héritage multiple, des langages OOP tels que C++ le font.
* **Héritage multipath :** Un hybride d'héritage multiple, multi-niveaux et hiérarchique, dans l'héritage multipath, une classe enfant dérive ses fonctionnalités et fonctions d'une classe parente et de plusieurs classes enfant de la classe parente. Parce que l'héritage multipath repose sur l'héritage multiple, Java ne prend pas en charge son utilisation.

## Pourquoi Java ne prend pas en charge l'héritage multiple

Le problème principal avec l'héritage multiple est qu'il a le potentiel de créer des ambiguïtés dans les classes enfant. Dans un livre blanc de 1995, le concepteur principal de Java, James Gosling, a déclaré que les [problèmes avec l'héritage multiple](https://www.researchgate.net/publication/345758345_Java_an_Overview_the_original_Java_whitepaper) étaient l'une des motivations pour la création de Java.

Les difficultés inhérentes à l'héritage multiple sont les plus clairement visibles dans le problème du diamant. Dans [le problème du diamant](https://www.freecodecamp.org/news/multiple-inheritance-in-c-and-the-diamond-problem-7c12a9ddbbec/), la classe parente A a deux classes enfant distinctes B et C ; c'est-à-dire que les classes enfant B et C étendent la classe A.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-74.png)
_[Source de l'image](https://www.dotnettricks.com/learn/oops/understanding-inheritance-and-different-types-of-inheritance)_

Maintenant, nous créons une nouvelle classe enfant D, qui étend à la fois la classe B et la classe C. Notez que nous avons un héritage multiple (D étend B et C), un héritage hiérarchique (B et C étendent A), et un héritage multi-niveaux (D étend A, B et C).

Dans le problème du diamant, les classes enfant B et C héritent d'une méthode de la classe parente A. B et C remplacent tous deux la méthode héritée. Mais les nouvelles méthodes dans B et C entrent en conflit les unes avec les autres. 

La classe enfant ultime D hérite des deux méthodes indépendantes et conflictuelles de ses multiples parents B et C. Il n'est pas clair quelle méthode la classe D doit utiliser, donc il y a une ambiguïté. D'autres langages de programmation OOP mettent en œuvre diverses méthodes pour résoudre l'ambiguïté de l'héritage multiple.

## Comment résoudre le problème de l'héritage multiple en Java

Le fait que l'héritage multiple soit problématique ne signifie pas qu'il n'est pas utile. Il existe de nombreuses situations où vous pouvez vouloir qu'une classe ait des fonctionnalités provenant de plusieurs autres classes. 

Pensez simplement à cette Tesla Roadster que vous achèterez lorsque vous deviendrez un développeur logiciel à succès. Elle tirera des caractéristiques à la fois de la classe des voitures de sport et de la classe des voitures électriques. 

Ou peut-être utilisez-vous un navigateur privé pour lire cet article, qui a des fonctionnalités de la classe des solutions de confidentialité des données en ligne et de la classe des navigateurs internet généraux.

Mais vous ne pouvez pas étendre plusieurs classes en Java. Alors, comment Java gère-t-il le problème de l'héritage multiple ? 

Eh bien, il utilise des structures appelées interfaces. Les interfaces sont des [types abstraits qui spécifient des comportements](https://www.freecodecamp.org/news/java-interfaces-explained-with-examples/) pour que les classes les implémentent. Parce qu'elles sont abstraites, les interfaces ne contiennent pas d'instructions détaillées pour leurs comportements. Au lieu de cela, les classes fournissent des implémentations concrètes des comportements de l'interface.

Les interfaces ont plusieurs caractéristiques définissantes :

* Contrairement aux classes, vous n'instanciez pas les interfaces. Au lieu de cela, les classes implémentent les interfaces
* Les interfaces ne contiennent que des définitions de constantes publiques et des en-têtes de méthodes
* Les interfaces ne peuvent étendre que d'autres interfaces, pas des classes
* Les interfaces peuvent étendre plusieurs interfaces, et les classes peuvent implémenter plusieurs interfaces

Maintenant, nous pouvons effectivement contourner le problème du diamant avec les interfaces. En rappelant que seules les interfaces peuvent étendre d'autres interfaces et que toute classe ayant besoin de caractéristiques d'héritage multiple doit implémenter plusieurs interfaces, nous pouvons redéfinir les classes du problème du diamant. 

Ce qui étaient auparavant les classes A, B et C deviennent maintenant les interfaces A, B et C. Les interfaces B et C étendent toujours l'interface A, mais il n'y a pas de fonctions concrètes dans aucune de ces interfaces, juste des comportements définis. La classe D reste une classe, qui est responsable de l'implémentation concrète des comportements trouvés dans les interfaces B et C. 

Notez une distinction clé ici : La classe D n'étend pas les interfaces B et C. Elle les implémente plutôt. Vous n'avez donc pas réellement un héritage multiple. Au lieu de cela, vous avez simplement redéfini le problème.

## Conclusion

Comprendre l'héritage est nécessaire pour tout codeur efficace. Pour les programmeurs Java, il est tout aussi important de connaître les limitations de l'héritage et le contournement intégré de Java pour les problèmes traditionnels de l'héritage multiple. 

Apprendre [comment mettre en place des interfaces](https://www.freecodecamp.org/news/polymorphism-in-java-tutorial-with-object-oriented-programming-example-code/) pour recréer les effets de l'héritage multiple en Java augmentera votre efficacité et votre employabilité.