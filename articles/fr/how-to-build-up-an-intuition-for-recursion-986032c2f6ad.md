---
title: Comment développer une intuition pour la récursivité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-29T01:21:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-up-an-intuition-for-recursion-986032c2f6ad
coverImage: https://cdn-media-1.freecodecamp.org/images/0*qnRpwEoIjgr_h1Hr
tags:
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: Comment développer une intuition pour la récursivité
seo_desc: 'By Dawson Eliasen

  And how to use it to solve problems


  _“white corner building” by [Unsplash](https://unsplash.com/@heysupersimi?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Simone Hutsch on <a href="https://unsplash...'
---

Par Dawson Eliasen

#### Et comment l'utiliser pour résoudre des problèmes

![Image](https://cdn-media-1.freecodecamp.org/images/8aza4Gl8EaNwkDwVTGejjq-QqNXHIHXNNIO-)
_« white corner building » par [Unsplash](https://unsplash.com/@heysupersimi?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Simone Hutsch</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

La récursivité est l'un des sujets les plus intimidants auxquels les étudiants sont confrontés en programmation. Elle est difficile à comprendre parce que le cerveau humain n'est pas capable de performer la récursivité — mais les ordinateurs, si. C'est exactement pourquoi la récursivité est un outil si puissant pour les programmeurs, mais cela signifie aussi que apprendre à l'utiliser est extrêmement difficile. Je veux vous aider à développer une intuition pour la récursivité afin que vous puissiez l'utiliser pour résoudre des problèmes.

Je suis assistant d'enseignement pour le cours d'introduction à l'informatique à mon université. J'ai expliqué la récursivité de la même manière une douzaine de fois cette semaine. Mon explication semble aider la plupart des étudiants. Cet article contient l'explication la plus générale en haut, et l'explication la plus spécifique en bas. Ainsi, vous pouvez commencer au début et vous arrêter dès que vous sentez que vous comprenez bien la récursivité. J'ai fourni quelques exemples en Java, et ils sont suffisamment simples pour que toute personne ayant une certaine expérience en programmation puisse les interpréter.

#### Qu'est-ce que la récursivité ?

Pour comprendre la récursivité, faisons un pas en arrière par rapport à la programmation. Commençons par établir une définition générale du terme. Quelque chose est _récursif_ s'il est défini par sa propre définition dans une certaine mesure. Cela ne vous aide probablement pas beaucoup à comprendre la récursivité, alors regardons une définition mathématique. Vous êtes familier avec les fonctions — un nombre entre, un autre nombre sort. Elles ressemblent à ceci :

_f(x) = 2x_

Changeons légèrement cette idée et pensons plutôt à une séquence. Une séquence prend un nombre entier, et un nombre entier sort.

_A(n) = 2n_

Les séquences peuvent être considérées comme des fonctions avec des entrées et des sorties qui sont limitées aux seuls entiers positifs. Généralement, les séquences commencent avec 1. Cela signifie que A(0) est 1. La séquence ci-dessus est la suivante :

_A(n) = 1, 2, 4, 6, 8, 10, … où n = 0, 1, 2, 3, 4, 5, …_

Maintenant, considérons la séquence suivante :

_A(n) = 2 x A(n-1)_

Cette séquence est _définie récursivement_. En d'autres termes, la valeur de tout élément donné dépend de la valeur d'un autre élément. Cette séquence ressemble à ceci :

_A(n) = 1, 2, 4, 8, 16, … où n = 0, 1, 2, 3, 4, …_

Tout élément est défini comme 2 fois l'élément précédent.

* L'élément n = 4, 16, est défini comme 2 fois l'élément précédent.
* L'élément n = 3, 8, est défini comme 2 fois l'élément précédent.
* L'élément n = 2, 4, est défini comme 2 fois l'élément précédent.
* L'élément n = 1, 2, est défini comme 2 fois l'élément précédent.
* **L'élément n = 0, 1, est défini comme…**

L'élément n = 0 ne peut pas être défini récursivement. Il n'y a pas d'élément précédent. Nous appelons cela un **cas de base**, et c'est une conséquence nécessaire des définitions récursives. **Ils doivent être explicitement représentés dans votre code**. Nous pourrions représenter cette séquence récursive en Java comme suit :

```
public int A(int n){    if (n == 0)        return 1;    return 2 * A(n - 1);}
```

Vous devriez vous familiariser avec l'anatomie d'une méthode récursive. Notez le cas de base : si n est 0, l'élément est défini comme 1. Sinon, l'élément est défini comme 2 fois l'élément précédent. Nous devons appeler récursivement la méthode pour obtenir la valeur de l'élément précédent, puis la multiplier par 2. Toutes les méthodes récursives auront ces deux composants :

* Cas de base, qui retourne une valeur bien définie.
* Cas récursif, qui retourne une valeur définie récursivement.

![Image](https://cdn-media-1.freecodecamp.org/images/0E2HqB2n-Uaz7t4xog-zDG5IbGJdTFEuUN9c)
_« white rose enclosed photograph » par [Unsplash](https://unsplash.com/@anniespratt?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Annie Spratt</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Faisons un autre exemple, en continuant avec le contexte mathématique. La suite de Fibonacci est souvent utilisée pour illustrer la récursivité. Tout élément de la suite de Fibonacci est la somme des deux éléments précédents. Cela se présente comme suit :

_F(n) = 1, 1, 2, 3, 5, 8, … où n = 0, 1, 2, 3, 4, 5, …_

* L'élément n = 5, 8, est défini comme la somme de l'élément n = 4 et de l'élément n = 3…

À ce stade, vous devriez hésiter. Dans l'exemple précédent, chaque élément dépendait d'un seul autre élément, maintenant chaque élément dépend de deux autres éléments. Cela complique les choses.

* L'élément n = 4, 5, est défini comme la somme de l'élément n = 3 et de l'élément n = 2.
* L'élément n = 3, 3, est défini comme la somme de l'élément n = 2 et de l'élément n = 1.
* L'élément n = 2, 2, est défini comme la somme de l'élément n = 1 et de l'élément n = 0.
* **L'élément n = 1, 1, est défini comme la somme de l'élément n = 0 et…**

L'élément n = 1 ne peut pas être défini récursivement. L'élément n = 0 non plus. Ces éléments ne peuvent pas être définis récursivement parce que la définition récursive nécessite deux éléments précédents. L'élément n = 0 n'a pas d'éléments précédents, et l'élément n = 1 n'a qu'un seul élément précédent. Cela signifie qu'il y a deux cas de base. Avant d'écrire du code, j'écrirais quelque chose comme ceci :

_L'élément n = 0 est défini comme 1. L'élément n = 1 est défini comme 1._

_L'élément n est défini comme la somme de l'élément n-1 et de l'élément n-2._

Maintenant, nous avons une idée de la manière dont cette tâche est définie récursivement, et nous pouvons passer à l'écriture de code. Ne commencez jamais à écrire du code sans avoir d'abord une compréhension naturelle de la tâche.

```
public int F(int n){    if (n == 0 || n == 1)        return 1;    return F(n - 1) + F(n - 2);}
```

#### La pile d'appels

![Image](https://cdn-media-1.freecodecamp.org/images/1ddahVRxpZNWjPgx-9mfnaEmalc76XpEG175)
_« assorted-title book lot » par [Unsplash](https://unsplash.com/@gotafli?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">gotafli</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="). C'est une pile de dossiers, vous comprenez ?_

En tant que programmeurs, nous voulons avoir une intuition pour la récursivité afin de pouvoir l'utiliser pour faire des choses. Pour le faire efficacement, nous devons comprendre comment un ordinateur traite la récursivité.

Il existe une structure de données que l'ordinateur utilise pour suivre les appels de méthodes appelée la **pile d'appels**. Chaque appel de méthode crée des **variables locales** à partir des paramètres de la méthode. L'ordinateur doit stocker ces variables pendant que la méthode est exécutée. Ensuite, l'ordinateur se débarrasse des valeurs lorsque la méthode retourne pour éviter de gaspiller de la mémoire.

La pile d'appels (et les piles en général) fonctionne comme vous pourriez imaginer une sorte de pile dans la vie réelle. Imaginez une pile de papiers sur votre bureau — elle commence par rien, puis vous ajoutez des papiers un par un. Vous ne savez rien sur aucun des papiers dans la pile sauf pour le papier du dessus. La seule façon de retirer des papiers de la pile est de les prendre un par un, **dans l'ordre inverse de celui dans lequel ils ont été ajoutés**.

C'est essentiellement comment la pile d'appels fonctionne, sauf que les éléments dans la pile sont des **enregistrements d'activation** au lieu de papiers. Les enregistrements d'activation sont simplement de petits morceaux de données qui stockent le nom de la méthode et les valeurs des paramètres.

Sans récursivité, la pile d'appels est assez simple. Voici un exemple. Si vous aviez un code qui ressemblait à ceci…

```
public static void main(String[] args)    System.out.println(myMethod(1));
```

…La pile d'appels ressemblerait à ceci :

```
*  myMethod(int a)
```

```
*  main(String[] args)
```

Ici, nous voyons deux méthodes en cours d'exécution, `main` et `myMethod`. L'important à noter est que `main` ne peut pas être retiré de la pile tant que `myMethod` n'est pas retiré de la pile. En d'autres termes, `main` ne peut pas se terminer tant que `myMethod` n'est pas appelé, exécuté et retourne une valeur.

Cela est vrai pour tout cas de composition de méthodes (une méthode dans une méthode) — alors regardons un exemple récursif : la méthode `A(int n)` que nous avons écrite précédemment. Votre code pourrait ressembler à ceci :

```
public static void main(String[] args)    System.out.println(A(4));
```

```
public static int A(int n){    if (n == 0)        return 1;    return 2 * A(n - 1);}
```

Lorsque `main` est appelé, `A` est appelé. Lorsque `A` est appelé, il s'appelle lui-même. Donc la pile d'appels va commencer à se construire comme suit :

```
* A(4)* main(String[] args)
```

`A(4)` appelle `A(3)`.

```
* A(3)* A(4)* main(String[] args)
```

Maintenant, il est important de noter que `A(4)` ne peut pas être retiré de la pile d'appels tant que `A(3)` n'est pas retiré de la pile d'appels en premier. Cela a du sens, car la valeur de `A(4)` dépend de la valeur de `A(3)`. La récursivité continue…

```
* A(0)* A(1)* A(2)* A(3)* A(4)* main(String[] args)
```

Lorsque `A(0)` est appelé, nous avons atteint un cas de base. Cela signifie que la récursivité est terminée, et au lieu de faire un appel récursif, une valeur est retournée. `A(0)` sort de la pile, et le reste des appels peut alors sortir de la pile en succession jusqu'à ce que `A(4)` puisse enfin retourner sa valeur à main.

Voici l'intuition : la valeur de retour de tout appel de méthode dépend de la valeur de retour d'un autre appel de méthode. Par conséquent, tous les appels de méthodes doivent être stockés en mémoire jusqu'à ce qu'un cas de base soit atteint. Lorsque le cas de base est atteint, les valeurs commencent à devenir bien définies au lieu d'être définies récursivement. Par exemple, `A(1)` est défini récursivement jusqu'à ce qu'il connaisse la définition du cas de base, 1. Ensuite, il est bien défini comme 2 fois 1.

Lorsque nous essayons de résoudre des problèmes avec la récursivité, il est souvent plus efficace de penser à l'ordre dans lequel les valeurs sont retournées. C'est l'inverse de l'ordre dans lequel les appels sont faits. Cet ordre est plus utile car il consiste en des valeurs bien définies, au lieu de valeurs définies récursivement.

Pour cet exemple, il est plus utile de considérer que `A(0)` retourne 1, puis `A(1)` retourne 2 fois 1, puis `A(2)` retourne 2 fois `A(1)`, et ainsi de suite. Cependant, lorsque nous écrivons notre code, il peut être plus facile de le formuler dans l'ordre inverse (l'ordre dans lequel les appels sont faits). C'est une autre raison pour laquelle je trouve utile d'écrire le cas de base et le cas récursif avant d'écrire du code.

#### Méthodes auxiliaires et récursivité vs boucles

![Image](https://cdn-media-1.freecodecamp.org/images/Aicn9TpaTduZb3eahKIRYtL2DvZzb6cxf6M-)
_« two persons shaking each other's hand » par [Unsplash](https://unsplash.com/@rawpixel?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">rawpixel</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Nous sommes des programmeurs, pas des mathématiciens, donc la récursivité est simplement un outil. En fait, la récursivité est un outil relativement simple. Elle est très similaire aux boucles en ce sens que les boucles et la récursivité induisent une répétition dans le programme.

Vous avez peut-être entendu dire que toute tâche répétitive peut être effectuée en utilisant soit une boucle while, soit une boucle for. Certaines tâches se prêtent mieux aux boucles while et d'autres tâches se prêtent mieux aux boucles for.

Il en va de même avec cet nouvel outil, la récursivité. **Toute tâche répétitive peut être accomplie avec soit une boucle, soit la récursivité, mais certaines tâches se prêtent mieux aux boucles et d'autres se prêtent mieux à la récursivité.**

Lorsque nous utilisons des boucles, il est parfois nécessaire de faire usage d'une variable locale pour « garder une trace » d'un calcul. Voici un exemple.

```
public double sum (double[] a){    double sum = 0.0;    for (int i = 0; i < a.length; i++)        sum += a[i];    return sum;
```

```
}
```

Cette méthode prend un tableau de doubles comme paramètre et retourne la somme de ce tableau. Elle utilise une variable locale, `sum`, pour garder une trace de la somme en cours. Lorsque la boucle est terminée, `sum` contiendra la somme réelle de toutes les valeurs dans le tableau, et cette valeur est retournée. Cette méthode a en fait deux autres variables locales qui sont moins évidentes. Il y a le tableau de doubles `a`, dont la portée est la méthode, et l'itérateur `i` (garde une trace de l'index), dont la portée est la boucle for.

Et si nous voulions accomplir cette même tâche en utilisant la récursivité ?

```
public double recursiveSum(double[] a)    # calculer récursivement la somme
```

Cette tâche est répétitive, donc il est possible de la faire en utilisant la récursivité, bien qu'elle soit probablement accomplie de manière plus élégante en utilisant une boucle. Nous devons simplement créer quelques variables locales pour garder une trace de la somme en cours et de l'index, n'est-ce pas ?

Hélas, cela est impossible. Les variables locales n'existent que dans le contexte d'un seul appel de méthode, et la récursivité utilise des appels de méthode répétés pour accomplir une tâche répétitive. Cela signifie que les variables locales sont pratiquement inutiles lorsque nous utilisons la récursivité. Si vous écrivez une méthode récursive et que vous avez l'impression d'avoir besoin d'une variable locale, vous avez probablement besoin d'une méthode auxiliaire.

Une **méthode auxiliaire** est une méthode récursive qui utilise **des paramètres supplémentaires pour garder une trace des valeurs.** Pour `recursiveSum`, notre méthode auxiliaire pourrait ressembler à ceci :

```
public double recursiveSum(double[] a, double sum, int index){    if (index == a.length)        return sum;    sum += a[index];    return recursiveSum(a, sum, index + 1);}
```

Cette méthode construit la somme en passant la valeur en cours à un nouvel appel de méthode avec l'index suivant. Lorsque qu'il n'y a plus de valeurs dans le tableau, la somme en cours est la somme réelle.

Maintenant, nous avons deux méthodes. La « méthode de démarrage », et la méthode auxiliaire.

```
public double recursiveSum(double[] a)    # calculer récursivement la somme
```

```
public double recursiveSum(double[] a, double sum, int index){    if (index == a.length)        return sum;    sum += a[index];    return recursiveSum(a, sum, index + 1);}
```

Le terme « méthode auxiliaire » est en fait un peu un abus de langage. Il s'avère que la méthode auxiliaire fait tout le travail, et l'autre méthode est juste un démarreur. Elle appelle simplement la méthode auxiliaire avec les valeurs initiales qui démarrent la récursivité.

```
public double recursiveSum(double[] a)    return recursiveSum(a, 0.0, 0);
```

```
public double recursiveSum(double[] a, double sum, int index){    if (index == a.length)        return sum;    sum += a[index];    return recursiveSum(a, sum, index + 1);}
```

Notez que les valeurs utilisées dans l'appel de démarrage à la méthode auxiliaire sont les mêmes valeurs utilisées pour initialiser les variables locales dans l'exemple de boucle. Nous initialisons la variable utilisée pour garder une trace de la somme à `0.0`, et nous initialisons la variable utilisée pour garder une trace de l'index à `0`.

Plus tôt, j'ai dit que les variables locales sont inutiles dans le contexte de la récursivité. Ce n'est pas complètement vrai, car les paramètres de la méthode sont en effet des variables locales. Elles fonctionnent pour la récursivité parce que de nouvelles sont créées chaque fois que la méthode est appelée. Lorsque la récursivité est exécutée, il y a de nombreux appels de méthode stockés dans la pile d'appels, et par conséquent, il y a de nombreuses copies des variables locales.

Vous pourriez demander, « Si la méthode auxiliaire fait tout le travail, pourquoi avons-nous même besoin de la méthode de démarrage ? Pourquoi ne pas simplement appeler la méthode auxiliaire avec les valeurs initiales, et alors vous n'avez besoin d'écrire qu'une seule méthode ? »

Eh bien, rappelez-vous que nous essayions de remplacer la méthode qui utilisait une boucle for. Cette méthode était simple. Elle prenait un tableau comme paramètre et retournait la somme du tableau comme un double. Si nous remplacions cette méthode par une qui prend trois paramètres, nous devrions nous souvenir de l'appeler avec les valeurs de départ appropriées. Si quelqu'un d'autre voulait utiliser votre méthode, ce serait impossible s'il ou elle ne connaissait pas les valeurs de départ.

Pour ces raisons, il est logique d'ajouter une autre méthode qui s'occupe de ces valeurs de départ pour nous.

#### Conclusion

La récursivité est un concept assez difficile, mais vous êtes arrivé jusqu'à la fin de mon explication. J'espère que vous comprenez un peu mieux la magie. Je vous accorde officiellement le titre de « Grand-Sorcier de la Récursivité ». Félicitations !