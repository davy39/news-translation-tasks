---
title: Erreur de saut de l'appel à la méthode Java scanner.nextLine() [RÉSOLU]
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2022-08-26T21:01:37.000Z'
originalURL: https://freecodecamp.org/news/java-scanner-nextline-call-gets-skipped-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/java-scanner-nextline-call-gets-skipped-solved.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: Java
  slug: java
seo_title: Erreur de saut de l'appel à la méthode Java scanner.nextLine() [RÉSOLU]
seo_desc: 'There''s a common error that tends to stump new Java programmers. It happens
  when you group together a bunch of input prompts and one of the scanner.nextLine()
  method calls gets skipped – without any signs of failure or error.

  Take a look at the follo...'
---

Il existe une erreur courante qui tend à déconcerter les nouveaux programmeurs Java. Elle se produit lorsque vous regroupez plusieurs invites de saisie et que l'un des appels à la méthode `scanner.nextLine()` est ignoré – sans aucun signe d'échec ou d'erreur.

Prenons l'exemple suivant de code :

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Quel est votre nom ? ");
        String name = scanner.nextLine();

        System.out.printf("Donc %s. Quel âge avez-vous ? ", name);
        int age = scanner.nextInt();

        System.out.printf("Cool ! %d est un bon âge pour commencer à programmer. \nQuel langage préférez-vous ? ", age);
        String language = scanner.nextLine();

        System.out.printf("Ah ! %s est un langage de programmation solide.", language);

        scanner.close();

    }

}

```

Le premier appel à `scanner.nextLine()` invite l'utilisateur à entrer son nom. Ensuite, l'appel à `scanner.nextInt()` invite l'utilisateur à entrer son âge. Le dernier appel à `scanner.nextLine()` invite l'utilisateur à entrer son langage de programmation préféré. Enfin, vous fermez l'objet scanner et c'est tout.

C'est un code Java très basique impliquant un objet `scanner` pour prendre des entrées de l'utilisateur, n'est-ce pas ? Essayons d'exécuter le programme et voyons ce qui se passe.

Si vous avez exécuté le programme, vous avez peut-être remarqué que le programme demande le nom, puis l'âge, et ensuite ignore la dernière invite pour le langage de programmation préféré et se termine brusquement. C'est ce que nous allons résoudre aujourd'hui.

## Pourquoi l'appel à `scanner.nextLine()` est-il ignoré après l'appel à `scanner.nextInt()` ?

Ce comportement n'est pas exclusif à la méthode `scanner.nextInt()`. Si vous appelez la méthode `scanner.nextLine()` après l'une des autres méthodes `scanner.nextWhatever()`, le programme ignorera cet appel.

Eh bien, cela est dû à la manière dont les deux méthodes fonctionnent. Le premier `scanner.nextLine()` invite l'utilisateur à entrer son nom.

Lorsque l'utilisateur entre le nom et appuie sur Entrée, `scanner.nextLine()` consomme le nom et le caractère de nouvelle ligne à la fin.

Ce qui signifie que le tampon d'entrée est maintenant vide. Ensuite, `scanner.nextInt()` invite l'utilisateur à entrer son âge. L'utilisateur entre l'âge et appuie sur Entrée.

Contrairement à la méthode `scanner.nextLine()`, la méthode `scanner.nextInt()` ne consomme que la partie entière et laisse le caractère de nouvelle ligne dans le tampon d'entrée.

Lorsque le troisième `scanner.nextLine()` est appelé, il trouve le caractère de nouvelle ligne toujours présent dans le tampon d'entrée, le prend pour une entrée de l'utilisateur et retourne immédiatement.

Comme vous pouvez le voir, comme de nombreux problèmes de la vie réelle, cela est causé par un malentendu entre l'utilisateur et le programmeur.

Il existe deux façons de résoudre ce problème. Vous pouvez soit consommer le caractère de nouvelle ligne après l'appel à `scanner.nextInt()`, soit prendre toutes les entrées sous forme de chaînes et les analyser pour obtenir le type de données correct plus tard.

## Comment vider le tampon d'entrée après l'appel à `scanner.nextInt()`

C'est plus facile que vous ne le pensez. Tout ce que vous avez à faire est d'ajouter un appel supplémentaire à `scanner.nextLine()` après l'appel à `scanner.nextInt()`.

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Quel est votre nom ? ");
        String name = scanner.nextLine();

        System.out.printf("Donc %s. Quel âge avez-vous ? ", name);
        int age = scanner.nextInt();

        // consomme le caractère de nouvelle ligne restant
        scanner.nextLine();

        System.out.printf("Cool ! %d est un bon âge pour commencer à programmer. \nQuel langage préférez-vous ? ", age);
        String language = scanner.nextLine();

        System.out.printf("Ah ! %s est un langage de programmation solide.", language);

        scanner.close();

    }

}

```

Bien que cette solution fonctionne, vous devrez ajouter des appels supplémentaires à `scanner.nextLine()` chaque fois que vous appelez l'une des autres méthodes. C'est bien pour les petits programmes, mais dans les plus grands, cela peut devenir très compliqué très rapidement.

## Comment analyser les entrées prises en utilisant la méthode `scanner.nextLine()`

Toutes les classes d'emballage en Java contiennent des méthodes pour analyser les valeurs de chaîne. Par exemple, la méthode `Integer.parseInt()` peut analyser une valeur entière à partir d'une chaîne donnée.

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Quel est votre nom ? ");
        String name = scanner.nextLine();

        System.out.printf("Donc %s. Quel âge avez-vous ? ", name);
        // analyse l'entier à partir de la chaîne
        int age = Integer.parseInt(scanner.nextLine());

        System.out.printf("Cool ! %d est un bon âge pour commencer à programmer. \nQuel langage préférez-vous ? ", age);
        String language = scanner.nextLine();

        System.out.printf("Ah ! %s est un langage de programmation solide.", language);

        scanner.close();

    }

}

```

C'est une manière plus propre de mélanger plusieurs types d'invites de saisie en Java. Tant que vous êtes prudent quant à ce que l'utilisateur entre, l'analyse devrait bien se passer.

## **Conclusion**

Je tiens à vous remercier du fond du cœur pour l'intérêt que vous portez à mon écriture. J'espère que cela vous a aidé d'une manière ou d'une autre.

Si c'est le cas, n'hésitez pas à partager avec vos contacts. Si vous souhaitez entrer en contact, je suis disponible sur [Twitter](https://twitter.com/frhnhsin) et [LinkedIn](https://www.linkedin.com/in/farhanhasin/).