---
title: Comment utiliser la fonction d'affichage en Java
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-10-04T21:16:25.000Z'
originalURL: https://freecodecamp.org/news/how-does-print-work-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Print-Statement.png
tags:
- name: Java
  slug: java
seo_title: Comment utiliser la fonction d'affichage en Java
seo_desc: 'Often, you''ll need to print something to the console output when you''re
  coding in Java. And the first thing that likely comes to your mind is the print
  function or print statement.

  But very few people know about the three different print functions/st...'
---

Souvent, vous aurez besoin d'afficher quelque chose sur la console lorsque vous codez en Java. Et la première chose qui vous vient probablement à l'esprit est la fonction d'affichage ou l'instruction print.

Mais très peu de gens connaissent les trois différentes fonctions/instructions d'affichage en Java. Dans cet article, je vais vous en parler et vous montrer comment elles fonctionnent, avec des exemples.

## Comment utiliser la fonction `println()` en Java

La fonction `println()` ajoute une nouvelle ligne après avoir affiché la valeur/donnée qu'elle contient. Ici, le suffixe `ln` fonctionne comme le caractère de nouvelle ligne, `\n`. Si vous considérez l'exemple suivant :

```java
public class Main{
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
```

Vous ne réaliserez peut-être pas exactement ce qui se passe en coulisses car vous n'affichez qu'une seule ligne, et vous obtenez la sortie suivante :

```
Hello World!
```

Mais si vous essayez d'afficher plusieurs expressions différentes en utilisant `println()`, vous verrez clairement la différence !

```java
public class Main{
    public static void main(String[] args) {
        System.out.println("Hello World!");
        System.out.println("Welcome to freeCodeCamp");
    }
}
```

Ici, vous pouvez voir qu'après l'exécution de la première instruction d'affichage, elle ajoute un caractère de nouvelle ligne ( `\n` ). Vous obtenez donc la deuxième instruction d'affichage, `Welcome to freeCodeCamp`, sur la ligne suivante.

Le résultat complet sera le suivant :

```
Hello World!
Welcome to freeCodeCamp
```

Vous pouvez consulter ma vidéo où je parle de cette fonction `println()` en détail.

%[https://youtu.be/_jfnI7yyaPo]

Mais n'y a-t-il pas un moyen d'éviter le caractère de nouvelle ligne généré automatiquement dans la fonction d'affichage ?

OUI ! Il y en a un. Dans ce cas, vous voudrez utiliser l'instruction `print()`.

## Comment utiliser la fonction `print()` en Java

Pour cette fonction, laissez-moi utiliser l'exemple que je viens d'utiliser. Vous devriez pouvoir voir la différence immédiatement :

```java
public class Main{
    public static void main(String[] args) {
        System.out.print("Hello World!");
        System.out.print("Welcome to freeCodeCamp");
    }
}
```

Ici, vous voyez que j'ai utilisé `print` au lieu d'utiliser `println` comme je l'ai fait précédemment. Le `print` n'ajoute pas le `\n` supplémentaire (caractère de nouvelle ligne) après avoir exécuté la tâche. Cela signifie que vous n'aurez pas de nouvelle ligne après l'exécution d'une instruction `print` comme ci-dessus.

La sortie sera la suivante :

```
Hello World!Welcome to freeCodeCamp
```

Si vous le souhaitez, vous pouvez également résoudre ce problème en utilisant `\n` comme ci-dessous :

```java
public class Main{
    public static void main(String[] args) {
        System.out.print("Hello World!\n");
        System.out.print("Welcome to freeCodeCamp");
    }
}
```

Cette fois, le `\n` fonctionnera comme le caractère de nouvelle ligne et vous obtiendrez la deuxième chaîne sur une nouvelle ligne. Le résultat est le suivant :

```
Hello World!
Welcome to freeCodeCamp
```

Vous pouvez également afficher les deux chaînes en utilisant une seule instruction d'affichage comme ci-dessous :

```java
public class Main{
    public static void main(String[] args) {
        System.out.print("Hello World!\nWelcome to freeCodeCamp");
    }
}
```

Le résultat sera le même cette fois-ci :

```
Hello World!
Welcome to freeCodeCamp
```

## Comment utiliser la fonction `printf()` en Java

Cette fonction `printf()` fonctionne comme une **fonction d'affichage formatée**. Pensez aux deux scénarios ci-dessous :

Scénario 1 : Votre ami Tommy veut que vous lui envoyiez le PDF de votre carnet par e-mail. Vous pouvez simplement rédiger un e-mail, indiquer l'objet de votre choix (comme : salut Tommy, c'est Fahim). Vous pouvez également éviter d'écrire quoi que ce soit dans le corps de l'e-mail et envoyer cet e-mail après avoir joint le PDF. C'est aussi simple que cela – vous n'avez pas besoin de maintenir de courtoisie avec votre ami, n'est-ce pas ?

Scénario 2 : Vous n'avez pas pu venir en cours hier. Votre professeur vous a demandé de fournir des raisons valables avec des preuves et de soumettre les documents par e-mail. 

Ici, vous ne pouvez pas envoyer d'e-mail à votre professeur comme vous l'avez fait pour votre ami Tommy. Dans ce cas, vous devez maintenir une certaine formalité et une étiquette appropriée. Vous devez fournir un objet formel et légitime et écrire les informations nécessaires dans le corps de l'e-mail. Enfin, vous devez joindre vos dossiers médicaux à votre e-mail après les avoir renommés selon la convention de nommage appropriée. Ici, vous avez formaté votre e-mail comme l'autorité le souhaite !

Dans la fonction `printf()`, nous suivons le deuxième scénario. Si nous voulons spécifier un format ou un style d'affichage spécifique, nous utilisons la fonction `printf()`.

Laissez-moi vous donner un court exemple de son fonctionnement :

```java
public class Main{
    public static void main(String[] args) {
        double value = 2.3897;
        System.out.println(value);
        System.out.printf("%.2f" , value);
    }
}
```

Ici, je déclare une variable de type double nommée `value` et je lui assigne `2.3897`. Maintenant, quand j'utilise la fonction `println()`, elle affiche la valeur entière avec les 4 chiffres après la virgule.

Voici le résultat :

```
2.3897
2.39
```

Mais après cela, quand j'utilise la fonction `printf()`, je peux modifier le flux de sortie de la manière dont je veux que la fonction affiche la valeur. Ici, je dis à la fonction que je veux exactement 2 chiffres après la virgule. La fonction affiche donc la valeur arrondie à 2 chiffres après la virgule.

Dans ce type de scénario, nous utilisons normalement la fonction `printf()`. Mais gardez à l'esprit qu'elle a une grande variété d'utilisations dans le langage de programmation Java. J'essaierai d'écrire un article détaillé plus tard à ce sujet. 😄

## Conclusion

Dans cet article, je vous ai donné une idée très basique de la différence entre les trois fonctions d'affichage en Java. 

Merci d'avoir lu l'article en entier. S'il vous a aidé, vous pouvez également consulter mes autres articles sur [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

Si vous souhaitez me contacter, vous pouvez le faire via [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), et [GitHub](https://github.com/FahimFBA). 

Vous pouvez également vous [ABONNER à ma chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) si vous voulez apprendre divers langages de programmation avec de nombreux exemples pratiques régulièrement.

Si vous voulez voir mes moments forts, vous pouvez le faire sur ma [chronologie Polywork](https://www.polywork.com/fahimbinamin).

Vous pouvez également [visiter mon site web](https://fahimbinamin.com/) pour en savoir plus sur moi et sur ce sur quoi je travaille.

Merci beaucoup !