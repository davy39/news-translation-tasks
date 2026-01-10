---
title: Méthodes d'impression en Java – Comment imprimer dans le terminal
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-04-19T14:28:53.000Z'
originalURL: https://freecodecamp.org/news/print-methods-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/tracy-adams-TEemXOpR3cQ-unsplash.jpg
tags:
- name: Java
  slug: java
- name: terminal
  slug: terminal
seo_title: Méthodes d'impression en Java – Comment imprimer dans le terminal
seo_desc: 'If you''re learning Java, you probably started your coding journey by printing
  the "Hello World" program in the console. And that''s a great way to begin – but
  after that, you need to learn how print methods and functions actually work.

  Well, this arti...'
---

Si vous apprenez Java, vous avez probablement commencé votre parcours de codage en imprimant le programme "Hello World" dans la console. Et c'est une excellente façon de commencer – mais après cela, vous devez apprendre comment les méthodes et fonctions d'impression fonctionnent réellement.

Eh bien, cet article vous montrera comment ces fonctions/méthodes d'impression fonctionnent réellement. Vous apprendrez également les différences entre les méthodes **`println`** et **`print`**.

En Java, les méthodes fonctionnent comme des fonctions dans d'autres langages de programmation. Mais comme les développeurs Java préfèrent généralement le terme "Fonction", je vais utiliser cette terminologie également pour tous mes articles liés à Java.

Si vous voulez imprimer quelque chose dans le terminal, vous devez utiliser l'une des méthodes d'impression. Il existe en fait trois méthodes d'impression différentes en Java. Ce sont les méthodes **`print`**, **`printf`**, et **`println`**. Nous allons voir comment chacune d'elles fonctionne maintenant.

## Comment utiliser la méthode `print` en Java

Il s'agit de la méthode d'impression la plus générique en Java, mais les développeurs ne l'utilisent que s'ils ne veulent pas obtenir de caractères de nouvelle ligne après l'impression de l'instruction à l'intérieur. Par exemple :

```java
System.out.print("Fahim");
System.out.print("Bin Amin");
```

La sortie serait comme ci-dessous :

```
FahimBin Amin
```

Je n'ai pas spécifié explicitement de caractère de nouvelle ligne ici, donc il n'en générera pas explicitement. Ainsi, nous n'obtiendrons pas de nouvelles lignes après l'impression de la première instruction.

Si vous ne savez pas ce que sont les séquences d'échappement et comment elles fonctionnent réellement, j'ai préparé cette vidéo pour vous. Assurez-vous de la regarder si vous avez besoin d'un rappel.

### 🎥 Tutoriel Vidéo

%[https://youtu.be/QqtYTnNxkoM]

Si vous voulez ajouter des espaces entre les deux instructions même si vous voulez les imprimer sur la même ligne, vous pouvez simplement ajouter un espace de fin dans la première instruction ou un espace de début dans la deuxième instruction.

```java
System.out.print("Fahim ");
System.out.print("Bin Amin");
```

La sortie sera :

```
Fahim Bin Amin
```

Ainsi, la méthode **print** est la méthode d'impression la plus basique qui n'ajoute rien de spécifique autre que l'impression simple de l'instruction à l'intérieur de la méthode.

## Comment utiliser la méthode `printf` en Java

Vous utilisez la méthode `printf` pour organiser une instruction différemment. Par exemple :

```java
double value = 5.984;
System.out.println(value);
System.out.printf("%.2f" , value);
```

La sortie est `5.98` car nous avons spécifié que nous voulions imprimer exactement 2 chiffres après le point radix (.). Dans ces cas, nous utilisons la méthode `printf`.

## Comment utiliser la méthode `println` en Java

Cette méthode est la méthode d'impression la plus largement utilisée en Java. Chaque fois que nous voulons imprimer une nouvelle ligne après l'impression de l'instruction à l'intérieur de la méthode, nous utilisons cette méthode **`println`**.

Si vous utilisez l'extension "Extensions for Java" dans Visual Studio Code ou si vous utilisez l'IDE bien connu IntelliJ IDEA, alors vous pouvez obtenir la méthode `println` complète (`System.out.println("")`) dans l'éditeur en utilisant simplement le raccourci "sout".

Maintenant, il est temps pour un exemple :

```java
System.out.println("Fahim");
System.out.println("Bin Amin");
```

La sortie est :

```
Fahim
Bin Amin
```

Comme j'ai utilisé les méthodes `println` dans les deux instructions, chaque instruction fournit un caractère de nouvelle ligne après l'impression de l'instruction à l'intérieur. Ainsi, après avoir imprimé `Fahim`, j'obtiens une nouvelle ligne – dans cette nouvelle ligne, j'obtiens `Bin Amin`.

### 🎥 Tutoriel Vidéo

Vous pouvez regarder la vidéo que j'ai faite pour vous aider à mieux comprendre ces méthodes d'impression :

%[https://youtu.be/_jfnI7yyaPo]

## Conclusion

Merci d'avoir lu cet article entier. J'espère que cela vous aide à commencer votre parcours de programmation Java.

Vous pouvez me suivre sur :

* GitHub : [FahimFBA](https://github.com/FahimFBA)
* LinkedIn : [fahimfba](https://www.linkedin.com/in/fahimfba/)
* Twitter : [Fahim_FBA](https://twitter.com/Fahim_FBA)
* YouTube : [Code With FahimFBA](https://www.youtube.com/@FahimAmin?sub_confirmation=1)
* Site Web : [https://fahimbinamin.com/](https://fahimbinamin.com/)

Si vous voulez me soutenir, alors [vous pouvez aussi m'offrir un café !](https://www.buymeacoffee.com/fahimbinamin)

Couverture : Photo par [Tracy Adams](https://unsplash.com/@tracycodes?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/s/photos/java?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)