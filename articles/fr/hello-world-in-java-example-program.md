---
title: Hello World en Java – Exemple de programme
date: '2022-06-07T17:13:21.000Z'
author: Ihechikara Abba
authorURL: https://www.freecodecamp.org/news/author/Ihechikara/
originalURL: https://freecodecamp.org/news/hello-world-in-java-example-program
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/helloWorld.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Java
  slug: java
seo_desc: "When you're learning a new programming language, you'll often see the first\
  \ program called a \"Hello World\" program. It's used in most cases as a simple\
  \ program for beginners. \nI will assume that you're either reading this article\
  \ as a beginner to the..."
---


Lorsque vous apprenez un nouveau langage de programmation, vous verrez souvent le premier programme appelé "Hello World". Il est utilisé dans la plupart des cas comme un programme simple pour les débutants.

<!-- more -->

Je suppose que vous lisez cet article soit en tant que débutant dans le langage de programmation Java, soit pour vous remémorer le bon vieux programme Hello World. Dans les deux cas, ce sera simple et direct.

Cet article ne se contentera pas d'inclure le programme Hello World en Java, nous aborderons également certains termes techniques que vous devriez connaître en tant que débutant apprenant à utiliser Java.

Pour suivre, vous aurez besoin d'un environnement de développement intégré (IDE). C'est là que vous écrivez et compilez votre code. Vous pouvez en installer un sur votre PC ou utiliser n'importe quel IDE en ligne si vous ne souhaitez pas passer par le processus d'installation.

## Programme Hello World en Java

Dans cette section, nous allons créer un programme Hello World simple. Nous le décortiquerons ensuite pour que vous compreniez son fonctionnement.

Voici le code :

```
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World!"); 
        // Hello World!
    }
}
```

Le code de l'exemple ci-dessus affichera "Hello World!" dans la console. Ceci est indiqué en commentaire dans le code. Nous parlerons des commentaires sous peu.

Analysons le code.

### Les classes en Java

Les classes servent de blocs de construction pour l'ensemble de l'application en Java. Vous pouvez avoir des classes distinctes pour différentes fonctionnalités.

Les classes peuvent également avoir des attributs et des méthodes qui définissent ce qu'est la classe et ce qu'elle fait.

Un exemple serait une classe `Human`. Elle peut avoir des attributs comme la couleur des cheveux, la taille, et ainsi de suite. Elle peut avoir des méthodes comme `run`, `eat` et `sleep`.

Dans notre programme Hello World, nous avons une classe appelée `HelloWorld`. Par convention, commencez toujours le nom de vos classes par une lettre majuscule.

Pour créer une classe, vous utilisez le mot-clé `class`, suivi du nom de la classe. Voici un exemple utilisant notre programme Hello World :

```
class HelloWorld {

}
```

### La méthode `main` en Java

Tout programme Java doit avoir une méthode `main`. Lorsque le compilateur Java commence à exécuter notre code, il commence par la méthode `main`.

Voici à quoi ressemble la méthode `main` :

```
public static void main(String[] args) {

    }
```

Afin de garder cet article simple, nous ne discuterons pas des autres mots-clés présents ci-dessus comme `public`, `static` et `void`.

### L'instruction `System.out.println()`

Nous utilisons l'instruction `System.out.println()` pour afficher des informations dans la console. L'instruction prend un argument. Les arguments sont écrits entre les parenthèses.

Voici la syntaxe :

```
System.out.println(Argument)
```

Dans notre cas, nous avons passé "Hello World!" comme argument. Vous remarquerez que le texte est entouré de guillemets. Cela indique au compilateur que l'argument est une `string` (chaîne de caractères). Les chaînes de caractères en programmation sont simplement une collection de caractères – de la même manière que nous écririons un texte ordinaire, mais elles doivent être entre guillemets.

Voici à quoi ressemble notre code :

```
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World!"); 
        // Hello World!
    }
}
```

Lorsque nous exécutons ce code, "Hello World" sera affiché.

Il ne sera pas affiché à l'intérieur du bloc de code ci-dessus. J'ai utilisé `// Hello World!` comme moyen de vous montrer la sortie du code. Cette partie du code ne sera pas exécutée par le compilateur car il s'agit d'un commentaire.

On utilise deux barres obliques (`//`) pour commencer un commentaire sur une seule ligne en Java.

## Conclusion

Dans cet article, nous avons parlé du programme Hello World en Java.

Nous avons commencé par créer le programme, puis nous l'avons décortiqué pour comprendre chaque ligne de code utilisée pour le créer.

Nous avons abordé les classes, la méthode `main`, l'instruction `System.out.println()`, les chaînes de caractères et les commentaires en Java.

Bonne programmation !