---
title: Le Manuel Java – Apprendre la Programmation Java pour Débutants
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2022-09-07T18:05:02.000Z'
originalURL: https://freecodecamp.org/news/the-java-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Farhan-Java-Handbook-Mockup.png
tags:
- name: beginner
  slug: beginner
- name: beginners guide
  slug: beginners-guide
- name: Java
  slug: java
seo_title: Le Manuel Java – Apprendre la Programmation Java pour Débutants
seo_desc: 'Java has been around since the 90s. And despite its massive success in
  many areas, this cross-platform, object-oriented programming language is often maligned.

  Regardless of how people feel about Java, I can tell you from experience is that
  it is an ...'
---

Java existe depuis les années 90. Et malgré son énorme succès dans de nombreux domaines, ce langage de programmation orienté objet et multiplateforme est souvent critiqué.

Quoi qu'il en soit, je peux vous dire par expérience que Java est un excellent langage de programmation. Après sa première apparition en 1995, il est toujours largement utilisé – et il y a de fortes chances qu'il ne disparaisse pas de sitôt.

Vous pouvez utiliser Java pour construire des serveurs, créer des applications de bureau, des jeux, des applications mobiles et plus encore. Il existe également d'autres langages JVM (nous discuterons de ce que cela signifie très bientôt) tels que [Kotlin](https://kotlinlang.org/), [Groovy](https://groovy-lang.org/), [Scala](https://www.scala-lang.org/), et [Clojure](https://clojure.org/) que vous pouvez utiliser pour différents objectifs.

Java est également multiplateforme, ce qui signifie que le code que vous écrivez et compilez sur une plateforme peut s'exécuter sur toute autre plateforme sur laquelle Java est installé. Nous aborderons ce sujet plus en détail plus tard.

Pour l'instant, je peux vous dire que bien que Java ait sa part de défauts, il a aussi beaucoup à offrir.

## Table des Matières

- [Prérequis](#heading-prerequis)
- [Comment Écrire Hello World en Java](#heading-comment-ecrire-hello-world-en-java)
    - [Que se Passe-t-il dans le Code ?](#heading-que-se-passe-t-il-dans-le-code)
    - [Qu'est-ce que la JVM ?](#heading-quest-ce-que-la-jvm)
    - [Qu'est-ce que JRE et JDK ?](#heading-quest-ce-que-jre-et-jdk)
- [Comment Installer Java sur Votre Ordinateur ?](#heading-comment-installer-java-sur-votre-ordinateur)
- [Comment Installer un IDE Java sur Votre Ordinateur ?](#heading-comment-installer-un-ide-java-sur-votre-ordinateur)
- [Comment Créer un Nouveau Projet sur IntelliJ IDEA](#heading-comment-creer-un-nouveau-projet-sur-intellij-idea)
- [Comment Travailler avec les Variables en Java](#heading-comment-travailler-avec-les-variables-en-java)
    - [Quelles Sont les Règles pour Déclarer des Variables ?](#heading-quelles-sont-les-regles-pour-declarer-des-variables)
    - [Quelles Sont les Variables final ?](#heading-quelles-sont-les-variables-final)
- [Quels sont les Types de Données Primitifs en Java ?](#heading-quels-sont-les-types-de-donnees-primitifs-en-java)
    - [Qu'est-ce que la Conversion de Type ou le Casting ?](#heading-quest-ce-que-la-conversion-de-type-ou-le-casting)
    - [Quelles sont les Classes Wrapper en Java](#heading-quelles-sont-les-classes-wrapper-en-java)
- [Comment Utiliser les Opérateurs en Java](#heading-comment-utiliser-les-operateurs-en-java)
    - [Quels Sont les Opérateurs Arithmétiques ?](#heading-quels-sont-les-operateurs-arithmetiques)
    - [Quels Sont les Opérateurs d'Affectation ?](#heading-quels-sont-les-operateurs-d-affectation)
    - [Quels Sont les Opérateurs Relationnels ?](#heading-quels-sont-les-operateurs-relationnels)
    - [Quels Sont les Opérateurs Logiques ?](#heading-quels-sont-les-operateurs-logiques)
    - [Quels Sont les Opérateurs Unaires ?](#heading-quels-sont-les-operateurs-unaires)
- [Comment Travailler avec les Chaînes de Caractères en Java](#heading-comment-travailler-avec-les-chaines-de-caracteres-en-java)
    - [Comment Formater une Chaîne de Caractères](#heading-comment-formater-une-chaine-de-caracteres)
    - [Comment Obtenir la Longueur d'une Chaîne de Caractères ou Vérifier si Elle est Vide ou Non](#heading-comment-obtenir-la-longueur-d-une-chaine-de-caracteres-ou-verifier-si-elle-est-vide-ou-non)
    - [Comment Diviser et Joindre des Chaînes de Caractères](#heading-comment-diviser-et-joindre-des-chaines-de-caracteres)
    - [Comment Convertir une Chaîne de Caractères en Majuscules ou Minuscules](#heading-comment-convertir-une-chaine-de-caracteres-en-majuscules-ou-minuscules)
    - [Comment Comparer Deux Chaînes de Caractères](#heading-comment-comparer-deux-chaines-de-caracteres)
    - [Comment Remplacer des Caractères ou une Sous-chaîne dans une Chaîne de Caractères](#heading-comment-remplacer-des-caracteres-ou-une-sous-chaine-dans-une-chaine-de-caracteres)
    - [Comment Vérifier si une Chaîne de Caractères Contient une Sous-chaîne ou Non](#heading-comment-verifier-si-une-chaine-de-caracteres-contient-une-sous-chaine-ou-non)
- [Quelles Sont les Différentes Façons de Saisir et de Sortir des Données ?](#heading-quelles-sont-les-differentes-facons-de-saisir-et-de-sortir-des-donnees)
- [Comment Utiliser les Instructions Conditionnelles en Java](#heading-comment-utiliser-les-instructions-conditionnelles-en-java)
- [Qu'est-ce qu'une Instruction switch-case ?](#heading-quest-ce-qu-une-instruction-switch-case)
- [Qu'est-ce que la Portée des Variables en Java ?](#heading-quest-ce-que-la-portee-des-variables-en-java)
- [Quelles Sont les Valeurs par Défaut des Variables en Java ?](#heading-quelles-sont-les-valeurs-par-defaut-des-variables-en-java)
- [Comment Travailler avec les Tableaux en Java](#heading-comment-travailler-avec-les-tableaux-en-java)
    - [Comment Trier un Tableau](#heading-comment-trier-un-tableau)
    - [Comment Effectuer une Recherche Binaire sur un Tableau](#heading-comment-effectuer-une-recherche-binaire-sur-un-tableau)
    - [Comment Remplir un Tableau](#heading-comment-remplir-un-tableau)
    - [Comment Faire des Copies d'un Tableau](#heading-comment-faire-des-copies-d-un-tableau)
    - [Comment Comparer Deux Tableaux](#heading-comment-comparer-deux-tableaux)
- [Comment Utiliser les Boucles en Java](#heading-comment-utiliser-les-boucles-en-java)
    - [Boucle For](#heading-boucle-for)
    - [Boucle For-Each](#heading-boucle-for-each)
    - [Boucle While](#heading-boucle-while)
    - [Boucle Do-While](#heading-boucle-do-while)
- [Comment Travailler avec les ArrayLists en Java](#heading-comment-travailler-avec-les-arraylists-en-java)
    - [Comment Ajouter ou Supprimer Plusieurs Éléments](#heading-comment-ajouter-ou-supprimer-plusieurs-elements)
    - [Comment Supprimer des Éléments Basés sur une Condition](#heading-comment-supprimer-des-elements-bases-sur-une-condition)
    - [Comment Cloner et Comparer des ArrayLists](#heading-comment-cloner-et-comparer-des-arraylists)
    - [Comment Vérifier si un Élément est Présent ou si l'ArrayList est Vide](#heading-comment-verifier-si-un-element-est-present-ou-si-l-arraylist-est-vide)
    - [Comment Trier un ArrayList](#heading-comment-trier-un-arraylist)
    - [Comment Conserver les Éléments Communs de Deux ArrayLists](#heading-comment-conserver-les-elements-communs-de-deux-arraylists)
    - [Comment Effectuer une Action sur Tous les Éléments d'un ArrayList](#heading-comment-effectuer-une-action-sur-tous-les-elements-d-un-arraylist)
- [Comment Travailler avec les HashMaps en Java](#heading-comment-travailler-avec-les-hashmaps-en-java)
    - [Comment Ajouter ou Remplacer Plusieurs Éléments dans une HashMap](#heading-comment-ajouter-ou-remplacer-plusieurs-elements-dans-une-hashmap)
    - [Comment Vérifier si une HashMap Contient un Élément ou si Elle est Vide](#heading-comment-verifier-si-une-hashmap-contient-un-element-ou-si-elle-est-vide)
    - [Comment Effectuer une Action sur Tous les Éléments d'une HashMap](#heading-comment-effectuer-une-action-sur-tous-les-elements-d-une-hashmap)
- [Classes et Objets en Java](#heading-classes-et-objets-en-java)
    - [Qu'est-ce qu'une Méthode ?](#heading-quest-ce-qu-une-methode)
    - [Qu'est-ce que la Surcharge de Méthode ?](#heading-quest-ce-que-la-surcharge-de-methode)
- [Quels sont les Constructeurs en Java ?](#heading-quels-sont-les-constructeurs-en-java)
- [Quels Sont les Modificateurs d'Accès en Java ?](#heading-quels-sont-les-modificateurs-d-acces-en-java)
- [Quelles Sont les Méthodes Getter et Setter en Java ?](#heading-quelles-sont-les-methodes-getter-et-setter-en-java)
- [Qu'est-ce que l'Héritage en Java ?](#heading-quest-ce-que-l-heritage-en-java)
- [Comment Redéfinir une Méthode en Java](#heading-comment-redefinir-une-methode-en-java)
- [Conclusion](#heading-conclusion)

## **Prérequis**

Le seul prérequis pour ce cours est la familiarité avec un autre langage de programmation tel que Python, JavaScript, etc.

Bien que j'expliquerai les concepts de programmation cruciaux dans le contexte de Java, je n'expliquerai pas des choses comme ce qu'est une variable dans le contexte de la programmation en général.

## Comment Écrire Hello World en Java

Idéalement, la première étape aurait dû être l'installation de Java sur votre ordinateur, mais je ne veux pas vous ennuyer avec le téléchargement et l'installation d'un tas de logiciels dès le début. Pour cet exemple, vous utiliserez [https://replit.com/](https://replit.com/) comme plateforme.

Tout d'abord, rendez-vous sur [https://replit.com/](https://replit.com/) et créez un nouveau compte si vous n'en avez pas déjà un. Vous pouvez utiliser votre compte Google/GitHub/Facebook existant pour vous connecter. Une fois connecté, vous arriverez sur votre page d'accueil. À partir de là, utilisez le bouton **Créer** sous **Mes Repls** pour créer un nouveau repl.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-201.png)

Dans la fenêtre modale **Créer un Repl**, choisissez **Java** comme **Modèle**, donnez un **Titre** descriptif tel que **HelloWorld** et cliquez sur le bouton **Créer Repl**.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-202.png)

Un éditeur de code apparaîtra avec un terminal intégré comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-203.png)

Sur le côté gauche se trouve la liste des fichiers de ce projet, au milieu se trouve l'éditeur de code, et sur le côté droit se trouve le terminal.

Le modèle contient du code par défaut. Vous pouvez exécuter le code en cliquant sur le bouton **Exécuter**. Allez-y et faites cela, exécutez le programme.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-205.png)

Si tout se passe bien, vous verrez les mots "Hello world!" imprimés sur le côté droit. Félicitations, vous avez exécuté avec succès votre premier programme Java.

### Que se Passe-t-il dans le Code ?

Le programme hello world est probablement le programme exécutable Java le plus basique que vous puissiez écrire – et comprendre ce programme est crucial.

```java
class Main {
  public static void main(String[] args) {
    System.out.println("Hello world!");
  }
}
```

Commençons par la première ligne :

```java
class Main {
  //...
}
```

Cette ligne crée une classe `Main`. Une classe regroupe un ensemble de code lié au sein d'une seule unité.

Il s'agit d'une classe `public`, ce qui signifie que cette classe est accessible n'importe où dans la base de code. Un fichier source Java (fichiers avec l'extension `.java`) ne peut contenir qu'une seule classe `public` de niveau supérieur.

Cette classe publique de niveau supérieur doit être nommée exactement de la même manière que le nom du fichier source. C'est pourquoi le fichier nommé `Main.java` contient la classe `main` dans ce projet.

Pour comprendre pourquoi, cliquez sur les trois points dans la liste des fichiers et cliquez sur l'option **Afficher les fichiers cachés**.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-204.png)

Cela révélera de nouveaux fichiers dans le projet. Parmi eux se trouve le fichier `Main.class`. Cela s'appelle un bytecode. Lorsque vous cliquez sur le bouton Exécuter, le compilateur Java a compilé votre code du fichier `Main.java` en ce bytecode.

Maintenant, modifiez le code Hello World existant comme suit :

```java
class Main {
  public static void main(String[] args) {
    System.out.println("Hello world!");
  }
}

class NotMain {
  public static void main(String[] args) {
    System.out.println("Not hello world!");
  }
}
```

Comme vous pouvez le voir, une nouvelle classe appelée `NotMain` a été ajoutée. Allez-y et cliquez à nouveau sur le bouton **Exécuter** tout en gardant un œil sur le menu **Fichiers**.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-206.png)

Un nouveau bytecode nommé `NotMain.class` est apparu. Cela signifie que pour chaque classe que vous avez dans votre base de code entière, le compilateur créera un bytecode séparé.

Cela crée une confusion sur quelle classe est le point d'entrée de ce programme. Pour résoudre ce problème, Java utilise la classe qui correspond au nom du fichier source comme point d'entrée de ce programme.

Assez parlé de la classe, regardons maintenant la fonction à l'intérieur :

```java
class Main {
  public static void main(String[] args) {
    System.out.println("Hello world!");
  }
}
```

La fonction `public static void main (String[] args)` est spéciale en Java. Si vous avez de l'expérience avec des langages comme C, C++ ou Go, vous devriez déjà savoir que chaque programme dans ces langages a une fonction principale. L'exécution du programme commence à partir de cette fonction principale.

En Java, vous devez écrire cette fonction exactement comme `public static void main (String[] args)` sinon cela ne fonctionnera pas. En fait, si vous la modifiez même un peu, Java commencerà à crier.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-207.png)

Le type de retour est passé de `void` à `int` et la fonction retourne maintenant `0` à la fin. Comme vous pouvez le voir dans la console, il est écrit :

```
Erreur : La méthode principale doit retourner une valeur de type void dans la classe Main, veuillez 
définir la méthode principale comme suit :
   public static void main(String[] args)
```

Écoutez cette suggestion et revenez à votre programme tel qu'il était avant.

```java
class Main {
  public static void main(String[] args) {
    System.out.println("Hello world!");
  }
}

```

La méthode `main` est une méthode `public` et le `static` signifie que vous pouvez l'appeler sans instancier sa classe.

Le `void` signifie que la fonction ne retourne aucune valeur et le `String[] args` signifie que la fonction prend un tableau de chaînes de caractères comme argument. Ce tableau contient les arguments de ligne de commande passés au programme lors de l'exécution.

Le `System.out.println` imprime des chaînes de caractères sur le terminal. Dans l'exemple ci-dessus, `"Hello world!"` a été passé à la fonction, donc vous obtenez `Hello world!` imprimé sur le terminal.

En Java, chaque instruction se termine par un point-virgule. **Contrairement à JavaScript ou Python, les points-virgules en Java sont obligatoires**. Oublier un point-virgule entraînera l'échec de la compilation.

C'est à peu près tout pour ce programme. Si vous n'avez pas compris chaque aspect de cette section mot à mot, ne vous inquiétez pas. Les choses deviendront beaucoup plus claires à mesure que vous avancerez.

Pour l'instant, retenez que la classe `public` de niveau supérieur dans un fichier source Java doit correspondre au nom du fichier, et la fonction principale de tout programme Java doit être définie comme `public static void main(String[] args)`.

### Qu'est-ce que la JVM ?

J'ai déjà prononcé le mot "bytecode" plusieurs fois dans la section précédente. J'ai également dit que Java est "multiplateforme", ce qui signifie que le code écrit et compilé sur une plateforme peut s'exécuter sur n'importe quelle plateforme sur laquelle Java est installé.

Vous voyez, votre processeur ne comprend pas l'anglais. En fait, la seule chose qu'il comprend ce sont les zéros et les uns, aka le binaire.

Lorsque vous écrivez et compilez un programme C++, cela résulte en un fichier binaire. Votre processeur le comprend et, en fonction de la plateforme ciblée par le programme, ce fichier peut être différent.

Prenez un processeur AMD64 et un ARMv8-A par exemple. Ces processeurs ont des jeux d'instructions différents. Donc, pour exécuter votre programme sur ces deux plateformes différentes, vous devrez les compiler séparément.

Mais un programme Java peut être écrit une fois et exécuté partout. J'espère que vous vous souvenez des bytecodes dont nous avons parlé dans la section précédente. Lorsque vous compilez du code Java, cela ne résulte pas en binaire mais plutôt en bytecode.

Ce bytecode n'est pas entièrement binaire mais il n'est pas non plus lisible par l'homme. En fait, votre processeur ne peut pas le lire non plus.

Au lieu de lancer ce bytecode au CPU, nous le faisons plutôt passer par la Machine Virtuelle Java ou JVM pour faire court. La JVM lit et interprète ensuite le bytecode pour le CPU.

Si vous souhaitez comprendre l'architecture de la JVM à un niveau plus profond, je vous suggère l'article approfondi de [Siben Nayak](https://www.freecodecamp.org/news/author/theawesomenayak/) sur le sujet.

### Qu'est-ce que JRE et JDK ?

JRE signifie Java Runtime Environment et JDK signifie Java Development Kit.

Le JRE ou Java Runtime Environment regroupe une implémentation de la JVM ainsi qu'un ensemble de bibliothèques nécessaires pour exécuter des programmes Java.

Le JDK, quant à lui, regroupe le JRE ainsi que toutes les bibliothèques nécessaires pour développer des programmes Java.

Donc, si vous voulez exécuter des programmes Java sur votre ordinateur, vous installez le JRE. Si vous voulez développer des programmes Java vous-même, vous installez le JDK. Il existe plusieurs implémentations du JDK.

Il y a le [Java SE (Standard Edition) Development Kit](https://www.oracle.com/java/technologies/downloads/) d'Oracle, puis il y a l'[OpenJDK](https://openjdk.org/), une implémentation de référence officielle du Java SE (Standard Edition) Development Kit.

Comme vous pouvez le deviner d'après le nom d'OpenJDK, il est open-source. Il existe donc plusieurs versions de celui-ci. Si vous êtes sur une machine Linux et utilisez le gestionnaire de paquets de votre distribution pour installer JDK, il est très probable que vous installiez une version OpenJDK telle que [Adoptium](https://adoptium.net/), [Microsoft Build of OpenJDK](https://docs.microsoft.com/en-us/java/openjdk/) et ainsi de suite.

J'espère que vous comprenez que JRE est un sur-ensemble de JVM et que JDK est un sur-ensemble de JRE. Ne vous inquiétez pas des différentes implémentations ou versions pour l'instant, vous les manipulerez lorsque le moment sera venu.

## Comment Installer Java sur Votre Ordinateur

Tout d'abord, rendez-vous sur [https://www.oracle.com/java/technologies/downloads/](https://www.oracle.com/java/technologies/downloads/) et téléchargez la dernière version du **Java SE Development Kit** selon la plateforme que vous utilisez :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-208.png)

Une fois le téléchargement terminé, lancez l'installateur et suivez le processus d'installation en cliquant sur les boutons Suivant. Terminez-le en cliquant sur le bouton Fermer sur la dernière page.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-235.png)

Le processus d'installation peut varier sur macOS et Linux, mais vous devriez pouvoir le comprendre par vous-même.

Une fois l'installation terminée, exécutez la commande suivante sur votre terminal :

```
java --version

# java 18.0.2 2022-07-19
# Java(TM) SE Runtime Environment (build 18.0.2+9-61)
# Java HotSpot(TM) 64-Bit Server VM (build 18.0.2+9-61, mixed mode, sharing)
```

Si cela fonctionne, vous avez installé avec succès le Java SE Development Kit sur votre ordinateur. Si vous préférez utiliser OpenJDK, n'hésitez pas à télécharger [Microsoft Build of OpenJDK](https://docs.microsoft.com/en-us/java/openjdk/) ou [Adoptium](https://adoptium.net/) et à suivre le processus d'installation. 

Pour les simples exemples de programmes que nous allons écrire dans cet article, peu importe quel JDK vous utilisez. Mais dans la vie réelle, assurez-vous que votre version de JDK est compatible avec le type de projet sur lequel vous travaillez.

## Comment Installer un IDE Java sur Votre Ordinateur

En ce qui concerne Java, [IntelliJ IDEA](https://www.jetbrains.com/idea/) est sans conteste le meilleur IDE disponible. Même Google l'utilise comme base pour leur [Android Studio](https://developer.android.com/studio).

La version ultime de l'IDE peut [coûter jusqu'à 149,00 $ par an pour un particulier](https://www.jetbrains.com/idea/buy/). Mais si vous êtes étudiant, vous pouvez obtenir [des licences éducatives](https://www.jetbrains.com/community/education/#students) pour tous les produits JetBrains gratuitement.

Il existe également l'édition communautaire complètement gratuite et open-source. C'est celle que nous utiliserons tout au long du livre.

Rendez-vous sur la [page de téléchargement d'IntelliJ IDEA](https://www.jetbrains.com/idea/download/), et téléchargez l'édition communautaire pour votre plateforme.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-344.png)

Une fois le téléchargement terminé, utilisez l'installateur pour installer IntelliJ IDEA comme tout autre logiciel.

## Comment Créer un Nouveau Projet sur IntelliJ IDEA

Utilisez le raccourci de votre menu démarrer pour lancer IntelliJ IDEA. La fenêtre suivante apparaîtra :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-346.png)

Utilisez le bouton **Nouveau Projet** et une fenêtre **Nouveau Projet** apparaîtra :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-347.png)

Donnez un nom descriptif à votre projet. Laissez les autres options telles qu'elles sont et appuyez sur le bouton **Créer**.

La création du projet ne devrait pas prendre plus d'un instant et une fois terminée, la fenêtre suivante apparaîtra :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-348.png)

C'est la fenêtre d'outils de projet sur le côté gauche. Tout votre code source vivra à l'intérieur de ce dossier `src`.

Faites un clic droit sur le dossier `src` et allez dans **Nouveau > Classe Java**.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-349.png)

À l'étape suivante, donnez un nom, tel que `Main` pour votre classe et assurez-vous que **Classe** est mis en surbrillance comme type.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-350.png)

Une nouvelle classe sera créée avec quelques lignes de code.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-351.png)

Mettez à jour le code comme suit :

```java
public class Main {
    public static void main (String[] args) {
        System.out.println("Hello World!");
    }
}

```

Pour exécuter ce code, utilisez le bouton de lecture vert sur le côté droit de la barre supérieure.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-352.png)

Le code s'exécutera et le résultat sera affiché dans le terminal intégré en bas de la fenêtre.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-353.png)

Félicitations, vous avez recréé avec succès le programme `HelloWorld` précédemment discuté dans IntelliJ IDEA.

## Comment Travailler avec les Variables en Java

Pour travailler avec différents types de données en Java, vous pouvez créer des variables de différents types. Par exemple, si vous souhaitez stocker votre âge dans une nouvelle variable, vous pouvez le faire comme suit :

```java
public class Main {

	public static void main(String[] args) {
		// <type> <name>
		int age;

	}

}

```

Vous commencez par écrire le type de données ou de variable. Puisque `age` est un nombre entier, son type sera entier ou `int` en abrégé, suivi du nom de la variable `age` et d'un point-virgule.

Pour l'instant, vous avez déclaré la variable mais vous ne l'avez pas initialisée. En d'autres termes, la variable n'a aucune valeur. Vous pouvez initialiser la variable comme suit :

```java
public class Main {

	public static void main(String[] args) {
		// <type> <name>
		int age;
		
		// <name> = <value>
		age = 27;
        
		// prints the age on the terminal
		System.out.println("I am " + age + " years old.");

	}

}
```

Lors de l'attribution d'une valeur, vous commencez par écrire le nom de la variable que vous souhaitez initialiser, suivi d'un signe égal (il est appelé l'opérateur d'affectation), puis la valeur que vous souhaitez attribuer à la variable. Et n'oubliez pas le point-virgule à la fin.

L'appel de fonction `System.out.println();` imprimera la ligne `I am 27 years old.` sur la console. Au cas où vous vous poseriez la question, utiliser un signe plus est l'une des nombreuses façons d'imprimer dynamiquement des variables au milieu d'une phrase.

Une chose que vous devez garder à l'esprit est que vous ne pouvez pas utiliser une variable non initialisée en Java. Donc si vous commentez la ligne `age = 27` en mettant deux barres obliques devant et essayez de compiler le code, le compilateur vous lancera le message d'erreur suivant :

```
Exception in thread "main" java.lang.Error: Unresolved compilation problem: 
	The local variable age may not have been initialized

	at variables.Main.main(Main.java:13)
```

La ligne `The local variable age may not have been initialized` indique que la variable n'a pas été initialisée.

Au lieu de déclarer et d'initialiser la variable dans différentes lignes, vous pouvez le faire en une seule fois comme suit :

```java
public class Main {

	public static void main(String[] args) {
		// <type> <name> = <value>
		int age = 27;
        
		// prints the age on the terminal
		System.out.println("I am " + age + " years old.");

	}

}
```

Le code devrait être de nouveau normal. De plus, vous pouvez changer la valeur d'une variable autant de fois que vous le souhaitez dans votre code.

```java
public class Main {

	public static void main(String[] args) {
		int age = 27;
        
		// updates the value to be 28 instead of 27
		age = 28;
        
		System.out.println("I am " + age + " years old.");

	}

}
```

Dans ce code, la valeur de `age` changera de 27 à 28 car vous la réécrivez juste avant l'impression.

Gardez à l'esprit que, bien que vous puissiez attribuer des valeurs à une variable autant de fois que vous le souhaitez, vous ne pouvez pas déclarer la même variable deux fois.

```java
public class Main {

	public static void main(String[] args) {
		// <type> <name> = <value>
		int age = 27;
        
		int age = 28;
        
		// prints the age on the terminal
		System.out.println("I am " + age + " years old.");

	}

}
```

Si vous essayez de compiler ce code, le compilateur vous lancera le message d'erreur suivant :

```
Exception in thread "main" java.lang.Error: Unresolved compilation problem: 
	Duplicate local variable age

	at variables.Main.main(Main.java:9)

```

La ligne `Duplicate local variable age` indique que la variable a déjà été déclarée.

Outre les variables, vous pouvez trouver le terme "littéral" sur Internet. Les littéraux sont des variables avec des valeurs codées en dur.

Par exemple, ici, `age = 27` et il n'est pas calculé dynamiquement. Vous avez écrit la valeur directement dans le code source. Donc `age` est un littéral entier.

### Quelles Sont les Règles pour Déclarer des Variables ?

Il y a certaines règles lorsque vous nommez vos variables en Java. Vous pouvez les nommer comme vous voulez tant qu'elles ne commencent pas par un chiffre et qu'elles ne contiennent pas d'espaces dans le nom.

Bien que vous puissiez commencer un nom de variable par un soulignement (_) ou un signe dollar ($), ne pas être attentif à leur utilisation peut rendre votre code difficile à lire. Les noms de variables sont également sensibles à la casse. Donc `age` et `AGE` sont deux variables différentes.

Une autre chose importante à retenir est que vous ne pouvez pas utiliser l'un des mots-clés réservés par Java. Il y en a environ 50 actuellement. Vous pouvez en apprendre davantage sur ces mots-clés à partir de la [documentation officielle](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/_keywords.html), mais ne vous inquiétez pas de les mémoriser.

À mesure que vous pratiquez, les plus importants s'imprimeront automatiquement dans vos neurones. Et si vous arrivez encore à vous tromper dans une déclaration de variable, le compilateur sera là pour vous rappeler que quelque chose ne va pas.

Outre les règles, il y a certaines conventions que vous devez suivre :

* Commencez le nom de votre variable par une lettre minuscule et non par un caractère spécial (comme un soulignement ou un signe dollar).
* Si le nom de la variable contient plusieurs mots, utilisez la casse camel : `firstName`, `lastName`
* N'utilisez pas de noms à une seule lettre : `f`, `l`

Tant que vous suivez ces règles et conventions, vous êtes prêt à partir. Si vous souhaitez en savoir plus sur les conventions de nommage en général, [consultez mon article sur le sujet](https://www.freecodecamp.org/news/programming-naming-conventions-explained/).

### Quelles Sont les Variables `final` ?

Une variable `final` en Java ne peut être initialisée qu'une seule fois. Donc si vous déclarez une variable comme `final`, vous ne pouvez pas la réaffecter.

```java
public class Main {

	public static void main(String[] args) {
		// final <type> <name> = <value>
		final int age = 27;
		
		age = 28;
        
		System.out.println("I am " + age + " years old.");

	}

}
```

Puisque la variable `age` a été déclarée comme `final`, le code lancera le message d'erreur suivant :

```
Exception in thread "main" java.lang.Error: Unresolved compilation problem: 
	The final local variable age cannot be assigned. It must be blank and not using a compound assignment

	at variables.Main.main(Main.java:9)

```

Cependant, si vous laissez la variable non initialisée lors de la déclaration, le code fonctionnera :

```
public class Main {

	public static void main(String[] args) {
		// final <type> <name>
		final int age;
		
		age = 28;
        
		// prints the age on the terminal
		System.out.println("I am " + age + " years old.");

	}

}
```

Ainsi, déclarer une variable comme `final` limitera votre capacité à réaffecter sa valeur. Si vous la laissez non initialisée, vous pourrez l'initialiser comme d'habitude.

## Quels sont les Types de Données Primitifs en Java ?

À un niveau élevé, il existe deux types de données en Java. Il y a les "types primitifs" et les "types non primitifs" ou "types de référence".

Les types primitifs stockent des valeurs. Par exemple, `int` est un type primitif et il stocke une valeur entière.

Un type de référence, en revanche, stocke la référence à un emplacement mémoire où un objet dynamique est stocké.

Il existe huit types de données primitifs en Java.

| TYPE      | EXPLICATION                                                                                            |
|-----------|--------------------------------------------------------------------------------------------------------|
| `byte`    | Entier signé sur 8 bits dans la plage de -128 à 127                                                  |
| `short`   | Entier signé sur 16 bits dans la plage de -32,768 à 32,767                                           |
| `int`     | Entier signé sur 32 bits dans la plage de -2147483648 à 2147483647                                   |
| `long`    | Entier signé sur 64 bits dans la plage de -9223372036854775808 à 9223372036854775807                 |
| `float`   | Nombre à virgule flottante sur 32 bits de précision simple dans la plage de 1.4E-45 à 3.4028235E38    |
| `double`  | Nombre à virgule flottante sur 64 bits de précision double dans la plage de 4.9E-324 à 1.7976931348623157E308         |
| `boolean` | Il peut être soit `true` soit `false`                                                                     |
| `char`    | Caractère Unicode unique sur 16 bits dans la plage de `\u0000` (ou 0) à `\uffff` (ou 65,535 inclus) |

Oui, je sais que le tableau semble effrayant, mais ne vous stressez pas. Vous n'avez pas à les mémoriser.

Vous n'aurez pas besoin de penser à ces plages très fréquemment, et même si vous le faites, il existe des moyens de les imprimer dans votre code Java.

Cependant, si vous ne comprenez pas ce qu'est un bit, je vous recommande [cet article court](https://www.freecodecamp.org/news/binary-definition/) pour en apprendre davantage sur le binaire.

Vous avez déjà appris à déclarer un entier dans la section précédente. Vous pouvez déclarer un `byte`, un `short` et un `long` de la même manière.

La déclaration d'un `double` fonctionne également de la même manière, sauf que vous pouvez attribuer un nombre avec un point décimal au lieu d'un entier :

```java
public class Main {

	public static void main(String[] args) {
		double gpa = 4.8;
		
		System.out.println("My GPA is " + gpa + ".");

	}
}
```

Si vous attribuez un `int` au `double`, comme `4` au lieu de `4.8`, la sortie sera `4.0` au lieu de `4`, car `double` aura toujours un point décimal.

Puisque `double` et `float` sont similaires, vous pourriez penser que remplacer le mot-clé `double` par `float` convertira cette variable en un nombre à virgule flottante – mais ce n'est pas correct. Vous devrez ajouter un `f` ou `F` après la valeur :

```java
public class Main {

	public static void main(String[] args) {
		float gpa = 4.8f;
		
		System.out.println("My GPA is " + gpa + ".");

	}
}
```

Cela se produit parce que, par défaut, chaque nombre avec un point décimal est traité comme un `double` en Java. Si vous n'ajoutez pas le `f`, le compilateur pensera que vous essayez d'attribuer une valeur `double` à une variable `float`.

Les données `boolean` peuvent contenir soit des valeurs `true` soit `false`.

```java
public class Main {

	public static void main(String[] args) {
		boolean isWeekend = false;
		
		System.out.println(isWeekend); // false

	}
}
```

Comme vous pouvez l'imaginer, `false` peut être traité comme un non et `true` peut être traité comme un oui. 

Les booléens deviendront beaucoup plus utiles une fois que vous aurez appris les instructions conditionnelles. Donc pour l'instant, rappelez-vous simplement ce qu'ils sont et ce qu'ils peuvent contenir.

Le type `char` peut contenir n'importe quel caractère Unicode dans une certaine plage.

```java
public class Main {

	public static void main(String[] args) {
		char percentSign = '%';
		
		System.out.println(percentSign); // %

	}
}
```

Dans cet exemple, vous avez enregistré le signe de pourcentage dans une variable `char` et l'avez imprimé sur le terminal.

Vous pouvez également utiliser des séquences d'échappement Unicode pour imprimer certains symboles.

```java
public class Main {

	public static void main(String[] args) {
		char copyrightSymbol = '\u00A9';
		
		System.out.println(copyrightSymbol); // 
9

	}
}
```

La séquence d'échappement Unicode pour le symbole de copyright, par exemple, est `\u00A9` et vous pouvez trouver plus de séquences d'échappement Unicode sur [ce site web](https://www.rapidtables.com/code/text/unicode-characters.html).

Parmi ces 8 types de données, vous travaillerez avec `int`, `double`, `boolean` et `char` la majorité du temps.

### Qu'est-ce que la Conversion de Type ou le Casting ?

La conversion de type en Java peut être soit "implicite" soit "explicite". Lorsque le compilateur convertit un type de données plus petit en un type plus grand automatiquement, cela est connu comme une conversion implicite ou une conversion de type rétrécissante.

```java
public class Main {

	public static void main(String[] args) {
		int number1 = 8;
		double number2 = number1;
		
		System.out.println(number2); // 8.0
	}

}

```

Puisqu'un double est plus grand qu'un entier, le compilateur a pu effectuer la conversion facilement. Si vous essayez de faire l'inverse, cependant, vous serez confronté à l'erreur suivante du compilateur :

```
Exception in thread "main" java.lang.Error: Unresolved compilation problem: 
	Type mismatch: cannot convert from double to int

	at operators.Main.main(Main.java:7)

```

Lors de l'exécution d'une conversion implicite, le flux de conversion doit être le suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/widening-conversion.svg)

Vous pouvez bien sûr passer d'un `short` à un `double`, par exemple, en sautant les autres entre les deux. 

Vous pouvez également passer de types de données plus petits à des types plus grands. Cela s'appelle une conversion explicite ou élargissante de type.

```java
package datatypes;

public class Main {

	public static void main(String[] args) {
		double number1 = 8.5;
		int number2 = (int) number1;
		
		System.out.println(number2); // 8
	}

}
```

Auparavant, vous avez vu que si vous essayez de convertir un type de données plus grand en un type plus petit, le compilateur se plaint. Mais lorsque vous ajoutez l'opérateur de conversion `(int)` explicitement, vous montrez au compilateur qui est le patron.

En faisant cela, vous perdez une partie de vos données. Si vous changez le nombre `double` initial de `8.5` à simplement `8.0`, vous ne perdrez aucune information. Donc, chaque fois que vous effectuez une conversion explicite, soyez prudent.

Vous pouvez également convertir un `char` en un `int` comme suit :

```java
public class Main {

	public static void main(String[] args) {
		char character = 'F';
		int number = character;
		
		System.out.println(number); // 70
	}

}

```

`70` est le code ASCII pour le caractère `F` – c'est pourquoi la sortie était comme cela. Si vous souhaitez en savoir plus sur les codes ASCII, mon collègue [Kris Koishigawa](https://www.freecodecamp.org/news/author/kris/) a écrit [un excellent article](https://www.freecodecamp.org/news/ascii-table-hex-to-ascii-value-character-code-chart-2/) sur le sujet.

Le flux de conversion dans ce cas sera l'inverse de ce que vous avez déjà vu.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/narrowing-conversion.svg)

Je vous suggère d'expérimenter en convertissant diverses valeurs d'un type à un autre et de voir ce qui se passe. Cela approfondira votre compréhension et vous rendra confiant.

### Quelles sont les Classes Wrapper en Java ?

Les classes wrapper peuvent envelopper les types de données primitifs et les transformer en types de référence. Les classes wrapper sont disponibles pour les huit types de données primitifs.

| Type Primitif | Classe Wrapper |
|----------------|---------------|
| `int`          | `Integer`     |
| `long`         | `Long`        |
| `short`        | `Short`       |
| `byte`         | `Byte`        |
| `boolean`      | `Boolean`     |
| `char`         | `Character`   |
| `float`        | `Float`       |
| `double`       | `Double`      |

Vous pouvez utiliser ces classes wrapper comme suit :

```java
public class Main {
    public static void main (String[] args) {
        Integer age = 27;
        Double gpa = 4.8;

        System.out.println(age); // 27
        System.out.println(gpa); // 4.8
    }
}
```

Tout ce que vous avez à faire est de remplacer le type de données primitif par la classe wrapper équivalente. Ces types de référence ont également des méthodes pour extraire le type primitif d'eux.

Par exemple, `age.intValue()` retournera l'âge sous forme d'entier primitif et `gpa.doubleValue()` retournera le GPA sous forme de type double primitif.

Il existe de telles méthodes pour les huit types de données. Bien que vous utilisiez les types primitifs la plupart du temps, ces classes wrapper seront pratiques dans certains scénarios que nous discuterons dans une section ultérieure.

## Comment Utiliser les Opérateurs en Java

Les opérateurs en programmation sont certains symboles qui indiquent au compilateur d'effectuer certaines opérations telles que des opérations arithmétiques, relationnelles ou logiques.

Bien qu'il existe six types d'opérateurs en Java, je ne parlerai pas des opérateurs bit à bit ici. Discuter des opérateurs bit à bit dans un guide pour débutants peut le rendre intimidant.

### Quels Sont les Opérateurs Arithmétiques ?

Les opérateurs arithmétiques sont ceux que vous pouvez utiliser pour effectuer des opérations arithmétiques. Il y en a cinq :

| OPÉRATEUR | OPÉRATION                  |
|----------|----------------------------|
| `+`      | Addition                   |
| `-`      | Soustraction                |
| `*`      | Multiplication             |
| `/`      | Division                   |
| `%`      | Reste (Modulo/Modulus) |

Les opérations d'addition, de soustraction, de multiplication et de division sont assez explicites. Jetez un coup d'œil à l'exemple de code suivant pour comprendre :

```java
public class Main {

	public static void main(String[] args) {
		int number1 = 10;
		int number2 = 5;
		
		System.out.println(number1 + number2); // 15
		System.out.println(number1 - number2); // 5
		System.out.println(number1 * number2); // 50
		System.out.println(number1 / number2); // 2
		System.out.println(number1 % number2); // 0

	}

}
```

Les résultats des quatre premières opérations ne nécessitent aucune explication. Dans la dernière opération, vous avez effectué une opération modulo/modulus en utilisant le symbole `%`. Le résultat est `0` car si vous divisez 10 par 2, il ne restera rien (pas de reste).

Les opérations d'addition et de multiplication sont assez simples. Mais, lors de l'exécution d'une soustraction, si le premier opérande est plus grand que le second opérande, le résultat sera un nombre négatif, tout comme dans la vie réelle.

Le type de données avec lequel vous travaillez fait une différence dans le résultat des opérations de division et de modulo.

```java
public class Main {

	public static void main(String[] args) {
		int number1 = 8;
		int number2 = 5;
		
		System.out.println(number1 / number2); // 1
	}

}
```

Bien que le résultat de cette opération aurait dû être 1,6, cela ne s'est pas produit car en Java, si vous divisez un entier par un autre entier, le résultat sera un entier. Mais si vous changez les deux ou l'un d'eux en float/double, tout redeviendra normal.

```java
public class Main {

	public static void main(String[] args) {
		double number1 = 8;
		double number2 = 5;
		
		System.out.println(number1 / number2); // 1.6
	}

}

```

Ce principe s'applique également aux opérations modulo. Si les deux opérandes ou l'un d'eux sont un float/double, le résultat sera un float/double.

### Quels Sont les Opérateurs d'Affectation ?

Vous avez déjà travaillé avec l'opérateur d'affectation dans une section précédente.

```java
public class Main {

	public static void main(String[] args) {
		// <type> <name> = <value>
		int age = 27;
        
		// prints the age on the terminal
		System.out.println(age);

	}

}
```

Lorsque vous utilisez le symbole `=` pour attribuer une valeur à une variable, il fonctionne comme un opérateur d'affectation. Mais ce n'est pas la seule forme de cet opérateur.

En combinant l'opérateur d'affectation régulier avec les opérateurs arithmétiques, vous pouvez obtenir différents résultats.

| OPÉRATEUR | OPÉRATION | ÉQUIVALENT À |
|----------|-----------|---------------|
| `+=`     | `a += b`  | `a = a + b`   |
| `-=`     | `a -= b`  | `a = a - b`   |
| `*=`     | `a *= b`  | `a = a * b`   |
| `/=`     | `a /= b`  | `a = a / b`   |
| `%=`     | `a %= b`  | `a = a % b`   |

L'exemple de code suivant devrait rendre les choses plus claires :

```java
package operators;

public class Main {

	public static void main(String[] args) {
		double number1 = 10;
		double number2 = 5;
		
		number1 += number2;
		
		System.out.println(number1); // 15
	}

}

```

Les autres opérateurs fonctionnent de la même manière. Ils opèrent puis attribuent la valeur résultante à l'opérande de gauche.

Je pourrais démontrer les autres en utilisant du code, mais je pense que si vous les essayez vous-même, vous obtiendrez une meilleure compréhension. Après tout, l'expérimentation et la pratique sont les seules façons de solidifier vos connaissances.

### Quels Sont les Opérateurs Relationnels ?

Les opérateurs relationnels sont utilisés pour vérifier la relation entre les opérandes. Par exemple, si un opérande est égal à un autre opérande ou non.

Ces opérateurs relationnels retournent soit `true` soit `false` en fonction de l'opération que vous avez effectuée.

Il existe six opérateurs relationnels en Java.

| OPÉRATEUR | EXPLICATION | USAGE |
|-----------|-------------|-------|
| `==` | Est Égal À | `5 == 8` retourne `false` |
| `!=` | N'est Pas Égal À | `5 != 8` retourne `true` |
| `>` | Est Supérieur À | `5 > 8` retourne `false` |
| `<` | Est Inférieur À | `5 < 8` retourne `true` |
| `>=` | Supérieur Ou Égal À | `5 >= 8` retourne `false` |
| `<=` | Inférieur Ou Égal À | `5 <= 8` retourne `true` |

L'exemple de code suivant démontre l'utilisation de ces opérateurs :

```java
public class Main {

	public static void main(String[] args) {
		double number1 = 10;
		double number2 = 5;
		
		System.out.println(number1 == number2); // false
		System.out.println(number1 != number2); // true
		System.out.println(number1 > number2); // true
		System.out.println(number1 < number2); // false
		System.out.println(number1 >= number2); // true
		System.out.println(number1 <= number2); // false
	}

}

```

L'utilisation pratique de ces opérateurs deviendra beaucoup plus évidente pour vous une fois que vous aurez appris les instructions conditionnelles dans une section ultérieure.

Vous pouvez également utiliser ces opérateurs avec des caractères.

```java
public class Main {

	public static void main(String[] args) {
		char smallLetter = 'a';
		char capitalLetter = 'A';
		
		System.out.println(smallLetter > capitalLetter); // ???
	}

}

```

Que pensez-vous que sera la sortie de ce code ? Découvrez-le par vous-même. Vous vous souvenez des valeurs ASCII des caractères ? Elles jouent un rôle dans la sortie de ce programme.

### Quels Sont les Opérateurs Logiques ?

Imaginez un scénario où un programme que vous avez créé ne peut être utilisé que par des personnes âgées de 18 ans et plus mais pas plus de 40 ans. Donc la logique devrait être la suivante :

```
peut exécuter le programme si ->
	age >= 18 et age <= 40
```

Ou dans un autre scénario, un utilisateur doit être un étudiant de votre école ou un membre de la bibliothèque pour emprunter des livres. Dans ce cas, la logique devrait être la suivante :

```
peut emprunter des livres si ->
	isSchoolStudent ou isLibraryMember
```

Ces décisions logiques peuvent être prises à l'aide d'opérateurs logiques. Il existe trois opérateurs de ce type en Java.

| OPÉRATEUR            | USAGE                                  | EXPLICATION                                                                |
|---------------------|----------------------------------------|----------------------------------------------------------------------------|
| Logical And (`&&`)  | `age >= 18 && age <= 40`               | Évalue à vrai, seulement si les deux conditions sont vraies                        |
| Logical Or (`||`) | `isSchoolStudent || isLibraryMember` | Évalue à vrai si l'une des deux ou les deux conditions sont vraies              |
| Not (`!`)          | `!isLibraryMember`                            | Évalue à faux si la condition interne évalue à vrai et vice versa |

Voyons ces opérateurs en code. D'abord, l'opérateur logique `and` :

```java
public class Main {

	public static void main(String[] args) {
		int age = 20;
		
		System.out.println(age >= 18 && age <= 40); // true
	}

}

```

Dans ce cas, il y a deux conditions de chaque côté de l'opérateur `&&`. Si et seulement si les deux conditions évaluent à `true`, l'opération `and` évalue à `true`.

Si la première condition évalue à `false`, l'ordinateur n'évaluera pas le reste des conditions et retournera `false`. Parce que si la première évalue à `false`, alors il n'y a aucun moyen pour que l'opération entière évalue à `true`.

L'opérateur logique `or` fonctionne de manière similaire, mais dans ce cas, si l'une des conditions est vraie, alors l'opération entière évaluera à vrai :

```java
public class Main {

	public static void main(String[] args) {
		boolean isSchoolStudent = true;
		boolean isLibraryMember = false;
		
		System.out.println(isSchoolStudent || isLibraryMember); // true
	}

}

```

Si la première condition d'une opération logique `or` évalue à `true`, l'ordinateur n'évaluera pas le reste des conditions et retournera `true`. Parce que si la première condition évalue à `true`, l'opération évaluera à `true` indépendamment de ce que les autres conditions évaluent.

Enfin, l'opérateur `not` évalue à l'inverse de ce que sa condition évalue. Jetez un coup d'œil à l'exemple de code suivant :

```java
public class Main {

	public static void main(String[] args) {
		boolean isLibraryMember = true;
		
		System.out.println(isLibraryMember); // true
		System.out.println(!isLibraryMember); // false
	}

}

```

Comme vous pouvez le voir, l'opérateur not retourne l'inverse de la valeur `boolean` donnée. L'opérateur not est un opérateur unaire, ce qui signifie qu'il opère sur un seul opérande.

```java
public class Main {

	public static void main(String[] args) {
		boolean isLibraryMember = true;
		boolean isSchoolStudent = false;
		
		System.out.println(!isSchoolStudent || isLibraryMember); // true
	}

}

```

Dans cet exemple, l'opérateur not transforme `isSchoolStudent` en `true`, donc l'opération évalue à `true`. Cependant, si vous modifiez le code comme suit :

```java
public class Main {

	public static void main(String[] args) {
		boolean isLibraryMember = true;
		boolean isSchoolStudent = false;
		
		System.out.println(!(isSchoolStudent || isLibraryMember)); // false
	}

}

```

D'abord, l'opération logique ou aura lieu et évaluera à `true`. L'opérateur not la transformera en `false`.

Bien que vous ayez utilisé deux opérandes avec chaque opérateur, vous pouvez en utiliser autant que vous le souhaitez. Vous pouvez également mélanger et assortir plusieurs opérateurs ensemble.

```java
public class Main {

	public static void main(String[] args) {
		boolean isSchoolStudent = true;
		boolean isLibraryMember = false;
		int age = 10;
		
		System.out.println(isSchoolStudent || isLibraryMember && age > 18); // ???
	}

}

```

Que pensez-vous que sera la sortie de ce code ? Je vous recommande de le découvrir par vous-même. :)

### Quels Sont les Opérateurs Unaires ?

Il existe certains opérateurs qui sont utilisés avec un opérande à la fois et ceux-ci sont appelés les opérateurs unaires. Bien qu'il y en ait cinq, je n'en discuterai que deux.

| OPÉRATEUR          | EXPLICATION                                                                              |
|-------------------|------------------------------------------------------------------------------------------|
| Incrément (`++`)  | Incrémente une valeur donnée de 1                                                            |
| Décrément (`--`)  | Décrémente une valeur donnée de 1                                                            |

L'exemple de code suivant les démontrera bien :

```java
public class Main {

	public static void main(String[] args) {
		int score = 95;
		int turns = 11;
		
		score++;
		turns--;
		
		System.out.println(score); // 96
		System.out.println(turns); // 10
	}

}

```

Vous pouvez également utiliser les opérateurs comme préfixes :

```java
public class Main {

	public static void main(String[] args) {
		int score = 95;
		int turns = 11;
		
		++score;
		--turns;
		
		System.out.println(score); // 96
		System.out.println(turns); // 10
	}

}

```

Jusqu'à présent, c'est simple. Mais il y a quelques légères différences entre les syntaxes postfix et prefix que vous devez comprendre. Regardez le code suivant :

```java
package operators;

public class Main {

	public static void main(String[] args) {
		int score = 95;
		
		
		System.out.println(++score); // 96
		System.out.println(score); // 96
	}

}

```

C'est le comportement attendu. L'opérateur de décrément de préfixe fonctionnera de la même manière. Mais regardez ce qui se passe si vous passez à la version postfix :

```java
package operators;

public class Main {

	public static void main(String[] args) {
		int score = 95;
		
		
		System.out.println(score++); // 95
		System.out.println(score); // 96
	}

}

```

Confus, n'est-ce pas ? Quelle est, selon vous, la valeur réelle de la variable en ce moment ? C'est 96. Laissez-moi expliquer.

Lorsque vous utilisez la syntaxe postfix dans une fonction d'impression, la fonction d'impression rencontre la variable en premier, puis l'incrémente. C'est pourquoi la deuxième ligne imprime la valeur nouvellement mise à jour.

Dans le cas de la syntaxe de préfixe, la fonction rencontre l'opérateur d'incrément en premier et effectue l'opération. Ensuite, elle passe à l'impression de la valeur mise à jour.

Cette petite différence peut vous prendre au dépourvu si vous n'êtes pas prudent. Ou vous pouvez essayer d'éviter d'incrémenter ou de décrémenter dans les appels de fonction.

## Comment Travailler avec les Chaînes de Caractères en Java

Le type `String` en Java est l'un des types de référence les plus couramment utilisés. C'est une collection de caractères que vous pouvez utiliser pour former des lignes de texte dans votre programme.

Il existe deux façons de créer de nouvelles chaînes de caractères en Java. La première est la manière littérale :

```java
public class Main {
	public static void main(String[] args) {
		String name = "Farhan";
        
		System.out.println("My name is " + name + ".");
	}

}
```

Comme vous pouvez le voir, déclarer et utiliser une `String` de cette manière n'est pas très différent de la déclaration des types primitifs en Java.

La deuxième façon de créer une nouvelle `String` est d'utiliser l'opérateur `new`.

```java
public class Main {
	public static void main(String[] args) {
		// <type> <name> = new <type>(<value>)
		String name = new String("Farhan");
        
		System.out.println("My name is " + name + ".");
	}

}
```

Ce programme fonctionnera exactement comme le précédent, mais il y a une légère différence entre les deux.

La JVM maintient une partie de la mémoire de votre ordinateur pour stocker les chaînes de caractères. Cette partie est appelée le pool de chaînes.

Chaque fois que vous créez une nouvelle `String` de manière littérale, la JVM vérifie d'abord si cette `String` existe déjà dans le pool. Si c'est le cas, la JVM la réutilisera. Si ce n'est pas le cas, alors la JVM la créera.

En revanche, lorsque vous utilisez l'opérateur `new`, la JVM créera toujours un nouvel objet `String` quoi qu'il arrive. Le programme suivant démontre clairement ce concept :

```java
public class Main {

	public static void main(String[] args) {
		String literalString1 = "abc";
		String literalString2 = "abc";
		
		String objectString1 = new String("abc");
		String objectString2 = new String("abc");
		
		System.out.println(literalString1 == literalString2);
		System.out.println(objectString1 == objectString2);

	}

}

```

Comme vous le savez peut-être déjà, l'opérateur `==` est utilisé pour vérifier l'égalité. La sortie de ce programme sera :

```
true
false
```

Puisque `abc` était déjà dans le pool de chaînes, la variable `literalString2` le réutilise. Dans le cas des chaînes d'objets, cependant, les deux sont des entités différentes.

### Comment Formater une Chaîne de Caractères

Vous avez déjà vu l'utilisation de l'opérateur `+` pour assembler des chaînes de caractères ou les formater d'une manière spécifique.

Cette approche fonctionne jusqu'à ce que vous ayez beaucoup d'additions à une chaîne. Il est facile de se tromper dans le placement des guillemets.

Une meilleure façon de formater une chaîne est la méthode `String.format()`.

```java
public class Main {
	public static void main(String[] args) {
		String name = "Farhan";
		int age = 27;
		
		String formattedString = String.format("My name is %s and I'm %d years old.", name, age);
        
		System.out.println(formattedString);
	}

}
```

La méthode prend une chaîne avec des spécificateurs de format comme premier argument et des arguments pour remplacer ces spécificateurs comme arguments ultérieurs.

Dans le code ci-dessus, les caractères `%s` et `%d` sont des spécificateurs de format. Ils sont responsables de dire au compilateur que cette partie de la chaîne sera remplacée par quelque chose.

Ensuite, le compilateur remplacera `%s` par `name` et `%d` par `age`. L'ordre des spécificateurs doit correspondre à l'ordre des arguments et les arguments doivent correspondre au type du spécificateur.

Les spécificateurs `%s` et `%d` ne sont pas aléatoires. Ils sont spécifiques pour les données de type chaîne et les entiers décimaux. Un tableau des spécificateurs couramment utilisés est le suivant :

| Spécificateur  | Type de Données              |
|------------|------------------------|
| `%b`, `%B` | Booléen                |
| `%s`, `%S` | Chaîne de caractères                 |
| `%c`, `%C` | Caractère Unicode      |
| `%d`       | Entier Décimal        |
| `%f`       | Nombres à Virgule Flottante |

Il existe également `%o` pour les entiers octaux, `%x` ou `%X` pour les nombres hexadécimaux, et `%e` ou `%E` pour les notations scientifiques. Mais puisque nous ne les discuterons pas dans ce livre, je les ai laissés de côté.

Tout comme les spécificateurs `%s` et `%d` que vous avez vus, vous pouvez utiliser l'un de ces spécificateurs pour leur type de données correspondant. Et juste au cas où vous vous poseriez la question, ce spécificateur `%f` fonctionne pour les floats et les doubles.

### Comment Obtenir la Longueur d'une Chaîne de Caractères ou Vérifier si Elle est Vide ou Non

Vérifier la longueur d'une chaîne de caractères ou s'assurer qu'elle n'est pas vide avant d'effectuer une opération est une tâche courante.

Chaque objet chaîne dispose d'une méthode `length()` qui retourne la longueur de cette chaîne. C'est comme la propriété `length` pour les tableaux.

```java
public class Main {
	public static void main(String[] args) {
		String name = "Farhan";
        
		System.out.println(String.format("Length of this string is: %d.", name.length())); // 6
	}

}
```

La méthode retourne la longueur sous forme d'entier. Vous pouvez donc l'utiliser librement en conjonction avec le spécificateur de format entier.

Pour vérifier si une chaîne est vide ou non, vous pouvez utiliser la méthode `isEmpty()`. Comme la méthode `length()`, elle est également disponible avec chaque objet chaîne.

```java
public class Main {
	public static void main(String[] args) {
		String name = "Farhan";
		
		if (name.isEmpty()) {
			System.out.println("There is no name mentioned here");
		} else {
			System.out.println(String.format("Okay, I'll take care of %s.", name));
		}
	}

}
```

La méthode retourne une valeur booléenne, vous pouvez donc l'utiliser directement dans les instructions if. Le programme vérifie si le nom est vide ou non et imprime différentes réponses en fonction de cela.

### Comment Diviser et Joindre des Chaînes de Caractères

La méthode `split()` peut diviser une chaîne de caractères en fonction d'une expression régulière.

```java
import java.util.Arrays;

public class Main {
	public static void main(String[] args) {
		String name = "Farhan Hasin Chowdhury";

		System.out.println(Arrays.toString(name.split(" ")));
	}

}
```

La méthode retourne un tableau de chaînes de caractères. Chaque chaîne de caractères dans ce tableau sera une sous-chaîne de la chaîne de caractères originale. Ici, par exemple, vous divisez la chaîne de caractères `Farhan Hasin Chowdhury` à chaque espace. Donc la sortie sera `[Farhan, Hasin, Chowdhury]`.

Juste un rappel que les tableaux sont des collections de plusieurs données du même type.

Puisque la méthode prend un regex comme argument, vous pouvez utiliser des expressions régulières pour effectuer des opérations de division plus complexes.

Vous pouvez également rejoindre ce tableau en une seule chaîne de caractères comme ceci :

```java
public class Main {
	public static void main(String[] args) {
		String name = "Farhan Hasin Chowdhury";
		
		String substrings[] = name.split(" ");
		
		String joinedName = String.join(" ", substrings);

		System.out.println(joinedName); // Farhan Hasin Chowdhury
	}

}
```

La méthode `join()` peut également vous aider à joindre plusieurs chaînes de caractères ensemble en dehors d'un tableau.

```java
public class Main {
	public static void main(String[] args) {
		System.out.println(String.join(" ", "Farhan", "Hasin", "Chowdhury")); // Farhan Hasin Chowdhury
	}

}
```

### Comment Convertir une Chaîne de Caractères en Majuscules ou Minuscules

Convertir une chaîne de caractères en majuscules ou minuscules est très simple en Java. Il existe les méthodes `toUpperCase()` et `toLowerCase()` pour effectuer ces tâches :

```java
public class Main {
	public static void main(String[] args) {
		String name = "Farhan Hasin Chowdhury";

		System.out.println(name.toUpperCase()); // FARHAN HASIN CHOWDHURY
		
		System.out.println(name.toLowerCase()); // farhan hasin chowdhury
	}

}
```

### Comment Comparer Deux Chaînes de Caractères

Puisque les chaînes de caractères sont des types de référence, vous ne pouvez pas les comparer en utilisant l'opérateur `=`.

La méthode `equals()` vérifie si deux chaînes de caractères sont égales ou non et la méthode `equalsIgnoreCase()` ignore leur casse lors de la comparaison.

```java
public class Main {
	public static void main(String[] args) {
		String name = "Farhan Hasin Chowdhury";
		String nameUpperCase = name.toUpperCase();

		System.out.println(name.equals(nameUpperCase)); // false
		
		System.out.println(name.equalsIgnoreCase(nameUpperCase)); // true
	}

}
```

### Comment Remplacer des Caractères ou des Sous-chaînes dans une Chaîne de Caractères

La méthode `replace()` peut remplacer des caractères ou des sous-chaînes entières d'une chaîne de caractères donnée.

```java
package strings;

public class Main {
	public static void main(String[] args) {
		String loremIpsumStd = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.";

		System.out.println(String.format("Standard lorem ipsum text: %s", loremIpsumStd));
		
		String loremIpsumHalfTranslated = loremIpsumStd.replace("Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium", "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system");
		
		System.out.println(String.format("Translated lorem ipsum text: %s", loremIpsumHalfTranslated));
	}

}
```

Ici, la chaîne `loremIpsumStd` contient une portion du texte original lorem ipsum. Ensuite, vous remplacez la première ligne de cette chaîne et enregistrez la nouvelle chaîne dans la variable `loremIpsumHalfTranslated`.

### Comment Vérifier si une Chaîne de Caractères Contient une Sous-chaîne ou Non

La méthode `contains()` peut vérifier si une chaîne de caractères donnée contient une certaine sous-chaîne ou non.

```java
public class Main {
	public static void main(String[] args) {
		String lyric = "Roses are red, violets are blue";

		if (lyric.contains("blue")) {
			System.out.println("The lyric has the word blue in it.");
		} else {
			System.out.println("The lyric doesn't have the word blue in it.");
		}
	}

}
```

La méthode retourne une valeur booléenne, vous pouvez donc utiliser la fonction dans n'importe quelle instruction conditionnelle.

Il s'agissait de certaines des méthodes de chaîne les plus courantes. Si vous souhaitez en apprendre davantage sur les autres, n'hésitez pas à consulter [la documentation officielle](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html).

## Quelles Sont les Différentes Façons de Saisir et de Sortir des Données ?

Jusqu'à présent, vous avez appris à utiliser la méthode `System.out.println()` pour imprimer des informations sur le terminal. Vous avez également appris à utiliser la méthode `String.format()` dans une section précédente.

Dans cette section, vous apprendrez quelques méthodes apparentées à `System.out.println()`. Vous apprendrez également à prendre des entrées de l'utilisateur.

Prendre des entrées de l'utilisateur est extrêmement facile dans des langages comme Python. Cependant, en Java, cela prend quelques lignes de code supplémentaires.

```java
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("What's your name? ");
		String name = scanner.nextLine();
		
		System.out.printf("So %s. How old are you? ", name);
		int age = scanner.nextInt();
		
		System.out.printf("Cool! %d is a good age to start programming.", age);
		
		scanner.close();

	}

}

```

La classe `java.util.Scanner` est nécessaire pour prendre des entrées utilisateur. Vous pouvez importer la classe dans votre programme en utilisant le mot-clé `import`.

Ensuite, vous devrez créer une nouvelle instance de la classe `Scanner` en utilisant le mot-clé `new`. Lors de la création de la nouvelle instance, vous devrez lui indiquer votre flux d'entrée souhaité.

Vous pouvez vouloir prendre une entrée de l'utilisateur ou d'un fichier. Quoi qu'il en soit, vous devrez informer le compilateur à ce sujet. Le flux `System.in` est le flux d'entrée et de sortie standard.

L'objet scanner dispose de méthodes comme `nextLine()` pour prendre une entrée de chaîne, `nextInt()` pour prendre une entrée d'entier, `nextDouble()` pour prendre une entrée de double, et ainsi de suite.

Dans le code ci-dessus, la méthode `scanner.nextLine()` demandera une chaîne à l'utilisateur et retournera l'entrée donnée avec un caractère de nouvelle ligne ajouté.

Ensuite, la méthode `scanner.nextInt()` demandera un entier et retournera le nombre donné par l'utilisateur.

Vous pouvez voir la méthode `System.out.printf()` pour la première fois ici. Eh bien, en plus de la méthode `System.out.println()`, il y a aussi la méthode `System.out.print()` qui imprime une chaîne donnée sans ajouter de caractère de nouvelle ligne.

La méthode `System.out.printf()` est une sorte de combinaison des méthodes `System.out.print()` et `String.format()`. Vous pouvez utiliser les spécificateurs de format précédemment discutés dans cette méthode également.

Une fois que vous avez terminé de prendre des entrées, vous devrez fermer l'objet scanner. Vous pouvez le faire en appelant simplement la méthode `scanner.close()`.

Simple, n'est-ce pas ? Laissez-moi le compliquer un peu.

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("What's your name? ");
        String name = scanner.nextLine();

        System.out.printf("So %s. How old are you? ", name);
        int age = scanner.nextInt();

        System.out.printf("Cool! %d is a good age to start programming. \nWhat language would you prefer? ", age);
        String language = scanner.nextLine();

        System.out.printf("Ah! %s is a solid programming language.", language);

        scanner.close();

    }

}

```

J'ai ajouté une nouvelle instruction `scanner.nextLine()` après l'appel de la méthode `scanner.nextInt()`. Cela fonctionnera-t-il ?

Non, cela ne fonctionnera pas. Le programme ignorera simplement la dernière invite d'entrée et imprimera la dernière ligne. Ce comportement n'est pas exclusif à `scanner.nextInt()`. Si vous utilisez `scanner.nextLine()` après l'une des autres méthodes `nextWhatever()`, vous rencontrerez ce problème.

En bref, cela se produit parce que lorsque vous appuyez sur Entrée dans la méthode `scanner.nextInt()`, elle consomme l'entier et laisse le caractère de nouvelle ligne dans le tampon d'entrée.

Ainsi, lorsque `scanner.nextLine()` est invoqué, il consomme ce caractère de nouvelle ligne comme la fin de l'entrée. La solution la plus simple à ce problème est d'écrire un appel supplémentaire à `scanner.nextLine()` après les autres appels de méthode de scanner.

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("What's your name? ");
        String name = scanner.nextLine();

        System.out.printf("So %s. How old are you? ", name);
        int age = scanner.nextInt();

        // consumes the dangling newline character
        scanner.nextLine();

        System.out.printf("Cool! %d is a good age to start programming. \nWhat language would you prefer? ", age);
        String language = scanner.nextLine();

        System.out.printf("Ah! %s is a solid programming language.", language);

        scanner.close();

    }

}

```

Il existe une autre façon de résoudre ce problème. Mais je n'entrerai pas dans les détails ici. Si vous êtes intéressé, [consultez mon article sur ce sujet](https://www.freecodecamp.org/news/java-scanner-nextline-call-gets-skipped-solved/).

## Comment Utiliser les Instructions Conditionnelles en Java

Vous utilisez des instructions conditionnelles pour prendre des décisions basées sur des conditions.

Cela se fait en utilisant l'instruction `if` comme suit :

```java
public class Main {

	public static void main(String[] args) {
		int age = 20;
		
		// if (condition) {...}
		if (age >= 18 && age <= 40) {
			System.out.println("you can use the program");
		}
		
	}

}

```

L'instruction commence par un `if` puis il y a la condition à l'intérieur d'une paire de parenthèses. Si la condition évalue à vrai, le code à l'intérieur des accolades sera exécuté.

Le code enfermé entre un ensemble d'accolades est connu sous le nom de bloc de code.

Si vous changez la valeur de `age` à `50`, l'instruction d'impression ne sera pas exécutée et il n'y aura aucune sortie sur la console. Pour ces types de situations où la condition évalue à `false`, vous pouvez ajouter un bloc `else` :

```java
public class Main {

	public static void main(String[] args) {
		int age = 20;
		
		if (age >= 18 && age <= 40) {
			System.out.println("you can use the program");
		} else {
			System.out.println("you can not use the program");
		}
		
	}

}

```

Maintenant, si la condition évalue à `false`, le code à l'intérieur du bloc `else` sera exécuté et vous verrez `you can not use the program` imprimé sur votre terminal.

Vous pouvez également avoir plusieurs conditions dans une échelle `if-else if-else` :

```java
public class Main {

	public static void main(String[] args) {
		int age = 50;
		boolean isSchoolStudent = true;
		boolean isLibraryMember = false;
		
		// if (condition) {...}
		if (age >= 18 && age <= 40) {
			System.out.println("you can use the program");
		} else if (isSchoolStudent || isLibraryMember) {
			System.out.println("you can use the program for a short time");
		} else {
			System.out.println("you can not use the program");
		}
		
	}

}

```

Maintenant, si la première condition évalue à `false`, alors la deuxième condition sera testée. Si la deuxième évalue à `true`, alors le code à l'intérieur des accolades sera exécuté. Si les conditions des deux instructions `if` évaluent à `false`, alors le bloc `else` sera exécuté.

Vous pouvez également imbriquer des instructions `if` dans d'autres instructions `if` comme suit :

```java
package operators;

public class Main {

	public static void main(String[] args) {
		int age = 20;
		
		if (age >= 18 && age <= 40) {
			boolean isSchoolStudent = true;
			boolean isLibraryMember = false;
			
			if (isSchoolStudent || isLibraryMember) {
				System.out.println("you can use the program");
			}
		} else {
			System.out.println("you can not use the program");
		}
		
	}

}

```

Dans ce cas, seulement si la première instruction `if` évalue à vrai, l'instruction `if` interne sera testée.

## Qu'est-ce qu'une Instruction switch-case ?

En plus des blocs if-else, il existe également des cas switch où vous pouvez définir plusieurs cas basés sur un seul switch.

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("What is the first operand? ");
        int a =scanner.nextInt();

        // consumes the dangling newline character
        scanner.nextLine();

        System.out.print("What is the second operand? ");
        int b = scanner.nextInt();

        // consumes the dangling newline character
        scanner.nextLine();

        System.out.print("What operation would you like to perform? ");
        String operation = scanner.nextLine();

        switch (operation) {
            case "sum":
                System.out.printf("%d + %d = %d", a, b, a+b);
                break;
            case "sub":
                System.out.printf("%d - %d = %d", a, b, a-b);
                break;
            case "mul":
                System.out.printf("%d * %d = %d", a, b, a*b);
                break;
            case "div":
                if (b == 0) {
                    System.out.print("Can't divide by zero!");
                } else {
                    System.out.printf("%d / %d = %d", a, b, a / b);
                }
                break;
            default:
                System.out.printf("Invalid Operation!");
        }

        scanner.close();

    }

}

```

Ceci est un programme de calculatrice très simple. Le programme demande à l'utilisateur deux nombres puis demande quelle opération ils souhaitent effectuer.

Chaque instruction switch-case aura un switch et plusieurs cas. Lorsque vous dites `case "sum"`, le programme vérifie si la valeur du switch ou de la variable `operation` dans ce cas est `sum` ou non.

Si cela correspond, le corps du cas sera exécuté. Si aucun des cas ne correspond, le cas `default` sera exécuté. 

Et à propos de cette instruction `break`. Elle fait ce qu'elle semble faire : arrête le programme de passer au cas suivant.

Si vous supprimez les instructions `break`, tous les cas seront exécutés les uns après les autres jusqu'à ce que le cas `default` soit atteint.

## Qu'est-ce que la Portée des Variables en Java ?

La portée est la durée de vie et l'accessibilité d'une variable. Selon l'endroit où vous déclarez une variable, vous pourrez peut-être y accéder ou non depuis d'autres endroits.

Prenez l'extrait de code suivant comme exemple :

```java
public class Main {

	public static void main(String[] args) {
		int age = 20;
		
		if (age >= 18 && age <= 40) {
			// age variable is accessible here
			// booleans are not accessible here

			boolean isSchoolStudent = true;
			boolean isLibraryMember = false;
			
			if (isSchoolStudent || isLibraryMember) {
				// booleans are accessible here
				// age variable is accessible here

				System.out.println("you can use the program");
			}
		} else {
			// age variable is accessible here
			// booleans are not accessible here
            
			System.out.println("you can not use the program");
		}
		
	}

}

```

Ici, la variable `age` est déclarée dans le bloc de code de la `class`. Cela signifie que vous pouvez accéder à cette variable dans toute la classe sans aucun problème. Puisque la variable est accessible dans toute l'instance de la classe, c'est une variable d'instance.

Cependant, les variables `isSchoolStudent` et `isLibraryMember` ont été déclarées dans le bloc de code de la première instruction `if`. Donc elles ne seront pas accessibles en dehors de ce bloc de code.

Mais elles seront accessibles dans tout bloc de code imbriqué à l'intérieur du premier bloc `if`. Ce sont ce qu'on appelle des variables locales.

Il existe également des variables de classe déclarées en utilisant le mot-clé `static`, mais vous en apprendrez davantage à leur sujet dans les sections sur la programmation orientée objet.

Donc pour l'instant, la règle générale est qu'une variable sera accessible dans le bloc de code où elle a été déclarée et dans tout autre bloc de code imbriqué dans le bloc parent.

## Quelles Sont les Valeurs par Défaut des Variables en Java ?

Vous avez appris que dans Java, vous devez initialiser une variable après l'avoir déclarée. Sinon, vous ne pourrez pas l'utiliser. Eh bien, ce n'est pas vrai dans tous les cas.

Si vous déclarez une variable au niveau de la classe, cette variable se verra attribuer une valeur par défaut par le compilateur.

```java
public class Main {
	
	// gets 0 as the value by default
	static int age;

	public static void main(String[] args) {
		System.out.println(age); // 0
	}
}

```

Puisque la méthode `main` est `static`, elle ne peut accéder qu'aux variables `static` au niveau de la classe. Je discuterai de `static` plus en détail dans la section sur la programmation orientée objet.

Mais si vous déplacez la déclaration de variable à l'intérieur de la méthode `main`, elle devient locale à cette méthode et ne reçoit aucune valeur par défaut.

```java
public class Main {
	public static void main(String[] args) {
		// remains uninitialized
		int age;
    
		System.out.println(age); // fails to compile
	}
}

```

Ce code lancera l'erreur `The local variable age may not have been initialized` lors de la compilation.

Les variables reçoivent leurs valeurs par défaut en fonction de leur type. Dans la plupart des cas, ce sera `0` ou `null`. Je donne une liste de tous les types primitifs et de leurs valeurs par défaut :

| Type de Données | Valeur par Défaut |
|-----------|---------------|
| `byte`    | `0`           |
| `short`   | `0`           |
| `int`     | `0`           |
| `long`    | `0L`          |
| `float`   | `0.0f`        |
| `double`  | `0.0d`        |
| `char`    | `'\u0000'`    |
| `boolean` | `false`       |

Tout type de référence se verra attribuer la valeur `null` par défaut. Nous discuterons des types de référence, des classes et des objets dans les sections sur la programmation orientée objet.

## Comment Travailler avec les Tableaux en Java

Vous avez déjà appris à déclarer des variables simples et à les utiliser dans votre programme. C'est là que les tableaux interviennent.

Les tableaux sont des structures de données contenant plusieurs valeurs du même type de données dans des emplacements mémoire séquentiels. Les tableaux peuvent être de n'importe quel type de données primitif ou non primitif.

Vous pouvez créer un tableau en Java comme suit :

```java
public class Main {

	public static void main(String[] args) {
		// <type> <name>[] = new <type>[<length>]
		char vowels[] = new char[5];

	}
}

```

Vous commencez par taper le type de données que vous souhaitez stocker dans le tableau, `char` dans ce cas. Ensuite, vous écrivez le nom du tableau, `vowels` suivi d'une paire de crochets ici. Cette paire de crochets indique à Java que vous déclarez un tableau de caractères et non une variable de caractère régulière.

Ensuite, vous mettez un signe égal suivi de l'opérateur `new` utilisé pour créer de nouveaux objets en Java. Puisque les tableaux sont des types de référence en Java, `new` est nécessaire pour créer de nouvelles instances.

Vous terminez la déclaration en écrivant le type à nouveau, suivi d'une autre paire de crochets contenant la longueur du tableau. Ici, `5` signifie que le tableau contiendra cinq éléments et pas plus.

Lorsque vous travaillez avec une seule variable, vous pouvez faire référence à la variable simplement par son nom. Mais dans le cas d'un tableau, chaque élément aura un index et les tableaux sont basés sur zéro. Cela signifie que le premier élément d'un tableau aura `0` comme index et non `1`.

Pour accéder à un élément dans un tableau, vous commencez par écrire le nom du tableau – dans ce cas `vowels` suivi d'une paire de crochets contenant votre index souhaité. Donc si vous voulez accéder au premier élément du tableau, vous pouvez le faire comme suit :

```java
public class Main {

	public static void main(String[] args) {
		char vowels[] = new char[5];
		
		vowels[0] = 'a';
	}
}

```

À ce stade, `vowels[0]` est similaire à une variable de caractère régulière. Vous pouvez l'imprimer, lui attribuer une nouvelle valeur, effectuer des calculs dans le cas des types numériques, et ainsi de suite. 

Puisque le tableau est vide à ce moment, j'attribue le caractère `a` au premier index. Vous pouvez attribuer le reste des voyelles aux autres index comme suit :

```java
public class Main {

	public static void main(String[] args) {
		char vowels[] = new char[5];
		
		vowels[0] = 'a';
		vowels[1] = 'e';
		vowels[2] = 'i';
		vowels[3] = 'o';
		vowels[4] = 'u';

	}
}

```

Puisque les index commencent à `0`, ils se termineront à la longueur du tableau - 1, qui dans ce cas est `4`. Si vous essayez d'attribuer un autre élément au tableau comme `vowels[4] = 'x';`, le compilateur lancera l'erreur suivante :

```
Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: Index 5 out of bounds for length 5
	at arrays.Main.main(Main.java:18)

```

Les tableaux ne peuvent pas être imprimés comme des variables régulières. Vous devrez utiliser une boucle ou vous devrez convertir le tableau en une chaîne. Puisque je n'ai pas encore discuté des boucles, j'utiliserai la deuxième méthode.

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		char vowels[] = new char[5];
		
		vowels[0] = 'a';
		vowels[1] = 'e';
		vowels[2] = 'i';
		vowels[3] = 'o';
		vowels[4] = 'u';
		
		System.out.println("These are the vowels: " + Arrays.toString(vowels));

	}
}

```

Vous devrez d'abord importer `java.util.Arrays;` et utiliser la méthode `Arrays.toString()` pour convertir le tableau en une chaîne. Cette classe a un tas d'autres méthodes intéressantes, mais avant de les discuter, j'aimerais vous montrer comment vous pouvez déclarer et initialiser un tableau en une seule fois.

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		char vowels[] = {'a', 'e', 'i', 'o', 'u'};
		
		System.out.println("These are the vowels: " + Arrays.toString(vowels));

	}
}

```

La syntaxe de déclaration du côté gauche reste inchangée. Cependant, après l'opérateur d'affectation, au lieu d'utiliser `new`, vous écrivez les éléments individuels du tableau séparés par des virgules et enfermés dans une paire d'accolades.

Dans ce cas, le compilateur comptera le nombre d'éléments dans le tableau et l'utilisera comme longueur du tableau.

Si vous ne connaissez pas la longueur d'un tableau, vous pouvez jeter un coup d'œil à la propriété `length`.

Dans ce cas, `vowels.length` sera `5` puisque il y a cinq éléments dans le tableau. La propriété `length` est un entier et est présente dans chaque tableau en Java.

Les tableaux peuvent également être multidimensionnels. Jusqu'à présent, vous avez travaillé avec des tableaux qui ressemblent à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/single-dimensional-array.svg)

Les tableaux à une seule dimension comme celui-ci sont parfaits lorsque vous souhaitez stocker une série de valeurs. Mais imaginez la routine quotidienne de médicaments de quelqu'un sous forme de tableau :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/multi-dimensional-array-1.svg)

La première ligne représente les sept jours de la semaine et les colonnes représentent combien de fois le patient doit prendre ses médicaments sur trois fois par jour. `0` signifie non et `1` signifie oui.

Vous pouvez mapper cette routine en utilisant un tableau multidimensionnel dans votre programme :

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {		
		int medicineRoutine[][] = {
				{1, 2, 3, 4, 5, 6, 7},
				{0, 1, 1, 0, 1, 1, 0},
				{1, 0, 1, 0, 1, 0, 0},
				{0, 0, 1, 1, 0, 1, 0},
		};
		
		System.out.println(Arrays.deepToString(medicineRoutine)); // [[1, 2, 3, 4, 5, 6, 7], [0, 1, 1, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0, 0], [0, 0, 1, 1, 0, 1, 0]]

	}
}

```

Les tableaux multidimensionnels ne peuvent pas être imprimés en utilisant la méthode `Arrays.toString()` régulière, vous devez creuser plus profondément.

Bien que la sortie ne ressemble en rien au tableau, vous pouvez la faire ressembler à un tableau en utilisant une programmation astucieuse :

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {		
		int medicineRoutine[][] = {
				{1, 2, 3, 4, 5, 6, 7},
				{0, 1, 1, 0, 1, 1, 0},
				{1, 0, 1, 0, 1, 0, 0},
				{0, 0, 1, 1, 0, 1, 0},
		};
		
		System.out.println(Arrays.deepToString(medicineRoutine).replace("], ", "]\n"));
	}
}

// [[1, 2, 3, 4, 5, 6, 7]
// [0, 1, 1, 0, 1, 1, 0]
// [1, 0, 1, 0, 1, 0, 0]
// [0, 0, 1, 1, 0, 1, 0]]
```

Vous avez déjà appris la méthode `replace()` pour les chaînes de caractères. Vous remplacez simplement le crochet de fermeture de chaque ligne par un crochet de fermeture et un caractère de nouvelle ligne.

La première ligne représente les 7 jours de la semaine et le reste des lignes sont les routines de médicaments pour chaque jour. Chaque ligne de ce tableau représente un tableau.

Pour accéder à une seule valeur d'un tableau multidimensionnel, vous aurez besoin de deux indices. Le premier indice détermine la ligne et le second détermine la colonne.

Ainsi, `medicineRoutine[2][3]` sélectionnera l'élément à l'index `3` du troisième tableau. Cet élément sera `0`. Travailler avec un tableau multidimensionnel peut sembler un peu délicat, mais la pratique le rendra beaucoup plus facile. 

Puisque vous pouvez créer des tableaux de n'importe quel type en Java, pourquoi ne pas essayer de créer d'autres types de tableaux par vous-même, hein ?

### Comment Trier un Tableau

L'une des tâches les plus courantes que vous effectuerez sur les tableaux est de les trier. La classe `java.utils.Arrays` dispose de la méthode `Arrays.sort()` pour faire exactement cela :

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {		
		char vowels[] = {'e', 'u', 'o', 'i', 'a'};
		
		Arrays.sort(vowels);
		
		System.out.println("The sorted array: " + Arrays.toString(vowels)); // [a, e, i, o , u]

	}
}

```

La méthode `Arrays.sort()` prend le tableau non trié comme argument et le trie en place. Ainsi, au lieu d'obtenir un nouveau tableau trié en retour, votre tableau original sera trié dans l'ordre croissant.

Par défaut, la méthode traite le premier index du tableau comme son index de départ et la longueur du tableau comme son index de fin.

Vous pouvez spécifier ces deux indices manuellement. Par exemple, si vous souhaitez trier uniquement `u, o, i` dans l'ordre croissant et laisser `e, a` tels quels, vous pouvez le faire comme suit :

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {		
		char vowels[] = {'e', 'u', 'o', 'i', 'a'};
		
		int startIndex = 1;
		int endIndex = 4;
		
		Arrays.sort(vowels, startIndex, endIndex);
		
		System.out.println("The sorted array: " + Arrays.toString(vowels)); // [e, i, o, u , a]

	}
}

```

Cette fois, la méthode prend le tableau comme premier paramètre, l'index de départ comme deuxième paramètre et l'index de fin comme troisième paramètre. Le reste des comportements reste le même qu'avant.

### Comment Effectuer une Recherche Binaire sur un Tableau

La recherche de valeurs dans une valeur triée est une autre tâche courante. La méthode `Arrays.binarySearch()` vous permet de rechercher des éléments dans un tableau trié en utilisant l'algorithme de recherche binaire.

```java
public class Main {

	public static void main(String[] args) {
		char vowels[] = {'a', 'e', 'i', 'o', 'u'};
        
        char key = 'i';
		
		int foundItemIndex = Arrays.binarySearch(vowels, key);
		
		System.out.println("The vowel 'i' is at index: " + foundItemIndex); // 2

	}
}

```

La méthode `Arrays.binarySearch()` prend un tableau comme premier paramètre et la clé de recherche (c'est-à-dire l'élément que vous recherchez) comme deuxième paramètre. Elle retournera l'index de l'élément trouvé sous forme d'entier.

Vous pouvez stocker cet index dans un `int` et l'utiliser pour accéder à l'élément du tableau comme `vowels[foundItemIndex]`.

Notez que le tableau doit être trié dans l'ordre croissant. Si vous n'êtes pas sûr de l'ordre du tableau, utilisez la méthode `Arrays.sort()` pour le trier d'abord.

Par défaut, la méthode traite le premier index du tableau comme son index de départ et la longueur du tableau comme son index de fin. Mais vous pouvez également spécifier ces indices manuellement.

Par exemple, si vous souhaitez que la recherche ait lieu de l'index `2` à l'index `4`, vous pouvez le faire comme suit :

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		char vowels[] = {'a', 'e', 'i', 'o', 'u'};
        
        char key = 'i';
		int startIndex = 2;
		int endIndex = 4;
		
		int foundItemIndex = Arrays.binarySearch(vowels, startIndex, endIndex, key);
		
		System.out.println("The vowel 'i' is at index: " + foundItemIndex); // 2

	}
}

```

Cette fois, la méthode prend le tableau que vous souhaitez rechercher comme premier paramètre, l'index de départ comme deuxième paramètre, l'index de fin comme troisième paramètre et la clé de recherche comme quatrième paramètre.

Maintenant, la recherche aura lieu dans `i`, `o` et `u`. Donc si vous cherchez `a`, il ne sera pas trouvé. Dans les cas où l'élément donné n'est pas trouvé, vous obtiendrez un index négatif. L'index négatif résultant variera en fonction de plusieurs facteurs, mais je n'entrerai pas dans les détails ici. Si vous êtes intéressé à en apprendre davantage, [consultez mon article sur le sujet](https://www.freecodecamp.org/news/how-to-use-arrays-binarysearch-in-java/).

### Comment Remplir un Tableau

Vous avez déjà appris à initialiser un tableau avec des valeurs, mais vous pouvez parfois vouloir remplir un tableau entier avec la même valeur. La méthode `Arrays.fill()` peut le faire pour vous :

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {		
		char vowels[] = {'e', 'u', 'o', 'i', 'a'};
		
		Arrays.fill(vowels, 'x');
		
		System.out.println("The filled array: " + Arrays.toString(vowels)); // [x, x, x, x, x]

	}
}

```

Comme la méthode `Arrays.sort()`, `Arrays.fill()` effectue également son opération en place. Elle prend votre tableau comme premier paramètre, la valeur avec laquelle vous souhaitez remplir le tableau comme deuxième paramètre, et met à jour le tableau original en place.

Cette méthode traite également le premier index comme l'index de départ et la longueur du tableau comme l'index de fin. Vous pouvez spécifier ces indices manuellement comme suit :

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {		
		char vowels[] = {'e', 'u', 'o', 'i', 'a'};
		
		int startIndex = 1;
		int endIndex = 4;
		
		Arrays.fill(vowels, startIndex, endIndex, 'x');
		
		System.out.println("The filled array: " + Arrays.toString(vowels)); // [e, x, x, x, a]

	}
}

```

Cette fois, la méthode prend votre tableau comme premier argument, l'index de départ comme deuxième argument, l'index de fin comme troisième argument et le remplisseur comme quatrième argument.

### Comment Faire des Copies d'un Tableau

Puisque les tableaux en Java sont des types de référence, les copier en utilisant l'opérateur d'affectation peut causer un comportement inattendu.

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		int oddNumbers[] = {1, 3, 5};
		int copyOfOddNumbers[] = oddNumbers;
		
		Arrays.fill(oddNumbers, 0);
		
		System.out.println("The copied array: " + Arrays.toString(copyOfOddNumbers)); // [0, 0, 0]

	}
}

```

Bien que vous ayez apporté des modifications au tableau source, la copie les reflète également. Cela se produit parce que lorsque vous utilisez l'opérateur d'affectation pour copier un tableau, la copie référence le tableau original dans la mémoire.

Pour copier correctement un tableau, vous pouvez utiliser la méthode `Arrays.copyOf()` comme suit :

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		int oddNumbers[] = {1, 3, 5};
		int copyOfOddNumbers[] = Arrays.copyOf(oddNumbers, oddNumbers.length);
		
		Arrays.fill(oddNumbers, 0);
		
		System.out.println("The copied array: " + Arrays.toString(copyOfOddNumbers)); // [1, 3, 5]

	}
}

```

La méthode prend le tableau source comme premier argument et la longueur souhaitée du nouveau tableau comme deuxième argument. Si vous voulez que la longueur soit la même, passez simplement la longueur du tableau original en utilisant la propriété `length`.

Si vous mettez une longueur plus petite, toute valeur après celle-ci sera coupée et si vous mettez une longueur plus grande, les nouveaux indices seront remplis avec la valeur par défaut du type de données du tableau.

Il existe une autre méthode `Arrays.copyOfRange()` qui peut copier une portion d'un tableau dans un nouveau :

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		int oddNumbers[] = {1, 3, 5, 7, 9, 11, 13, 15};
		
		int startIndex = 2;
		int endIndex = 7;
		
		int copyOfOddNumbers[] = Arrays.copyOfRange(oddNumbers, startIndex, endIndex);
		
		System.out.println("The copied array: " + Arrays.toString(copyOfOddNumbers)); // [5, 7, 9, 11, 13]

	}
}

```

Cette méthode prend le tableau source comme premier argument, puis l'index de départ et enfin l'index de fin. 

Gardez à l'esprit, l'index de fin n'est pas inclusif. C'est pourquoi 15 est absent du nouveau tableau. Mais si vous voulez inclure le dernier index du tableau, utilisez la longueur du tableau original comme index de fin.

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		int oddNumbers[] = {1, 3, 5, 7, 9, 11, 13, 15};
		
		int startIndex = 2;
		int endIndex = oddNumbers.length;
		
		int copyOfOddNumbers[] = Arrays.copyOfRange(oddNumbers, startIndex, endIndex);
		
		System.out.println("The copied array: " + Arrays.toString(copyOfOddNumbers)); // [5, 7, 9, 11, 13, 15]

	}
}

```

Maintenant, le nouveau tableau inclura également 15. Vous pouvez également mettre un nombre plus élevé que la longueur du tableau source. Dans ce cas, les indices nouvellement ajoutés contiendront la valeur par défaut du type de données du tableau.

### Comment Comparer Deux Tableaux

Si vous essayez de vérifier si deux tableaux sont identiques ou non en Java en utilisant l'opérateur relationnel égal, vous obtiendrez des résultats inattendus.

```java
public class Main {

	public static void main(String[] args) {		
		int oddNumbers1[] = {1, 3, 5, 7, 9, 11, 13, 15};
		int oddNumbers2[] = {1, 3, 5, 7, 9, 11, 13, 15};
		
		System.out.println(oddNumbers1 == oddNumbers2); // false
	}
}

```

Même si les deux tableaux sont identiques, la sortie du programme est `false`. Puisque les tableaux sont des types de référence, l'opérateur relationnel vérifiera s'ils sont la même instance ou non.

Pour comparer deux tableaux en Java, vous pouvez utiliser la méthode `Arrays.equals()` :

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {		
		int oddNumbers1[] = {1, 3, 5, 7, 9, 11, 13, 15};
		int oddNumbers2[] = {1, 3, 5, 7, 9, 11, 13, 15};
		
		System.out.println(Arrays.equals(oddNumbers1, oddNumbers2)); // true
	}
}

```

Cependant, si vous changez même un seul élément dans l'un de ces tableaux, la sortie sera `false` puisque les tableaux ne resteront plus identiques.

Vous pouvez également comparer des tableaux multidimensionnels, mais pour cela, vous devrez utiliser la méthode `Arrays.deepEquals()` au lieu de la méthode régulière.

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {		
		int medicineRoutine[][] = {
				{1, 2, 3, 4, 5, 6, 7},
				{0, 1, 1, 0, 1, 1, 0},
				{1, 0, 1, 0, 1, 0, 0},
				{0, 0, 1, 1, 0, 1, 0},
		};
		
		int medicineRoutine2[][] = {
				{1, 2, 3, 4, 5, 6, 7},
				{0, 1, 1, 0, 1, 1, 0},
				{1, 0, 1, 0, 1, 0, 0},
				{0, 0, 1, 1, 0, 1, 0},
		};
		
		System.out.println(Arrays.deepEquals(medicineRoutine, medicineRoutine2)); // true
	}
}

```

Cette méthode s'appelle elle-même chaque fois qu'elle rencontre un nouveau tableau à l'intérieur du tableau parent. 

Ce sont quelques-unes des méthodes les plus courantes de la classe `java.util.Arrays`. Vous pouvez consulter [la documentation officielle](https://docs.oracle.com/javase/7/docs/api/java/util/Arrays.html) si vous souhaitez en apprendre davantage.

## Comment Utiliser les Boucles en Java

Si vous devez répéter une tâche un certain nombre de fois, vous pouvez utiliser une boucle. Les boucles peuvent être de trois types : les boucles `for`, les boucles `for...each` et les boucles `while`.

### Boucle For

Les boucles for sont probablement les types de boucles les plus courants que vous verrez sur Internet.

Chaque boucle for se compose de trois parties. L'initialisation, la condition et l'expression de mise à jour. La boucle se fait en plusieurs étapes.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/for-loop-generic-2.svg)

Si vous voulez imprimer les nombres de 0 à 10 en utilisant une boucle for, vous pouvez le faire comme suit :

```java
public class Main {

	public static void main(String[] args) {
		for (int number = 0; number <= 10; number++) {
			System.out.println(number);
		}
	}
}

// 0
// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
// 9
// 10
```

Le schéma de cette boucle ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/for-loop-number-1.svg)

1. Au début de la boucle, vous initialisez un nouvel entier nommé `number` avec la valeur initiale de `0`.
2. Ensuite, vous vérifiez si `number` est inférieur ou égal à `10` ou non.
3. S'il est inférieur ou égal à `10`, vous exécutez l'instruction à l'intérieur du bloc de boucle et imprimez le nombre sur le terminal.
4. Ensuite, vous mettez à jour la variable number en incrémentant sa valeur de 1.
5. La boucle revient à vérifier si la valeur de number est toujours inférieure ou égale ou non.

Tant que la valeur de number reste inférieure ou égale à 10, la boucle continue. Le moment où la valeur de la variable `number` devient `11`, la boucle se termine.

Vous pouvez utiliser une boucle for pour parcourir un tableau comme suit :

```java
public class Main {

	public static void main(String[] args) {
		int fibonacciNumbers[] = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55};
		
		for(int index = 0; index < fibonacciNumbers.length; index++) {
			System.out.println(fibonacciNumbers[index]);
		}
	}
}

```

Le schéma de cette boucle sera le suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/for-loop-fibo.svg)

Puisque le dernier index du tableau est un de moins que sa longueur, vous exécutez la boucle tant que l'index est inférieur à la longueur du tableau. Le moment où l'index devient égal à la longueur du tableau, vous quittez la boucle.

L'une des choses amusantes que vous pouvez faire avec les boucles est d'imprimer des tables de multiplication. Par exemple, la table de multiplication pour 5 sera la suivante :

```java
public class Main {

	public static void main(String[] args) {
		int number = 5;
		
		for (int multiplier = 1; multiplier <= 10; multiplier++) {
			System.out.println(String.format("%d x %d = %d", number, multiplier, number * multiplier));
		}
	}
}

// 5 x 1 = 5
// 5 x 2 = 10
// 5 x 3 = 15
// 5 x 4 = 20
// 5 x 5 = 25
// 5 x 6 = 30
// 5 x 7 = 35
// 5 x 8 = 40
// 5 x 9 = 45
// 5 x 10 = 50
```

Les boucles peuvent également être imbriquées. Ce qui signifie que vous pouvez mettre une boucle à l'intérieur d'une autre. Vous pouvez imprimer la table de multiplication de tous les nombres de 1 à 10 en utilisant des boucles imbriquées :

```java
public class Main {

	public static void main(String[] args) {
		for (int number = 1; number <= 10; number++) {
			System.out.println(String.format("\nmultiplication table of %d", number));
			for (int multiplier = 1; multiplier <= 10; multiplier++) {
				System.out.println(String.format("%d x %d = %d", number, multiplier, number * multiplier));
			}
		}
	}
}

```

Je n'oserais pas imprimer la sortie ici. Au lieu de cela, essayez le code par vous-même. Dessinez chaque itération de la boucle sur une feuille de papier afin de comprendre ce qui se passe à chaque étape.

### Boucle For-Each

Si vous souhaitez itérer sur une collection comme un tableau et effectuer une opération sur chaque élément de cette collection, vous pouvez utiliser une boucle for...each.

```java
public class Main {

	public static void main(String[] args) {
		int fibonacciNumbers[] = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55};
		
		for(int number : fibonacciNumbers) {
			System.out.println(number);
		}
	}
}

```

Dans le cas d'une boucle for-each, le type de l'élément doit correspondre au type de la collection avec laquelle vous travaillez. Ici, le tableau est de type entier, donc l'élément dans la boucle est de type entier.

Cela effectue la même tâche que la boucle for précédemment montrée. Mais dans celle-ci, vous n'avez pas à suivre l'index ou utiliser les crochets pour accéder aux éléments. Cela semble plus propre et est moins sujet aux erreurs.

### Boucle While

Si vous souhaitez exécuter un ensemble de code jusqu'à ce qu'une certaine condition soit remplie, vous pouvez utiliser une boucle while.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/while-loop-generic.svg)

Il n'y a pas d'étapes d'initialisation ou de mise à jour dans une boucle while. Tout ce qui se passe, se passe à l'intérieur du corps de la boucle. Si vous réécrivez le programme pour imprimer la table de multiplication de 5 en utilisant une boucle while, il sera comme suit :

```
public class Main {

	public static void main(String[] args) {
		int number = 5;
		int multiplier = 1;
		
		while (multiplier <= 10) {
			System.out.println(String.format("%d x %d = %d", number, multiplier, number*multiplier));
			
			multiplier++;
		}
	}
}

// 5 x 1 = 5
// 5 x 2 = 10
// 5 x 3 = 15
// 5 x 4 = 20
// 5 x 5 = 25
// 5 x 6 = 30
// 5 x 7 = 35
// 5 x 8 = 40
// 5 x 9 = 45
// 5 x 10 = 50
```

Bien que les boucles while ne soient pas aussi courantes que les boucles for dans le monde réel, apprendre à les utiliser en vaut la peine.

### Boucle Do-While

Le dernier type de boucle que vous apprendrez est la boucle do-while. Elle inverse un peu l'ordre de la boucle while régulière – au lieu de vérifier la condition avant d'exécuter le corps de la boucle, vous exécutez d'abord le corps de la boucle puis vous vérifiez la condition.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/do-while-loop-generic.svg)

Le code de la table de multiplication implémenté en utilisant une boucle do-while sera comme suit :

```java
public class Main {

	public static void main(String[] args) {
		int number = 5;
		int multiplier = 1;
		
		do {
			System.out.println(String.format("%d x %d = %d", number, multiplier, number*multiplier));
			
			multiplier++;
		} while (multiplier <= 10);
	}
}

// 5 x 1 = 5
// 5 x 2 = 10
// 5 x 3 = 15
// 5 x 4 = 20
// 5 x 5 = 25
// 5 x 6 = 30
// 5 x 7 = 35
// 5 x 8 = 40
// 5 x 9 = 45
// 5 x 10 = 50
```

Les boucles do-while sont très utiles lorsque vous devez effectuer une opération jusqu'à ce que l'utilisateur donne une entrée spécifique. Par exemple, afficher un menu jusqu'à ce que l'utilisateur appuie sur la touche "x".

## Comment Travailler avec les ArrayLists en Java

Les tableaux en Java ne sont pas redimensionnables. Une fois que vous avez défini une longueur pour un tableau, vous ne pouvez pas la modifier. La classe `ArrayList` en Java atténue cette limitation.

```java
import java.util.ArrayList;

public class Main {
    public static void main (String[] args) {
        ArrayList<Integer> oddNumbers = new ArrayList<>();

        oddNumbers.add(1);
        oddNumbers.add(3);
        oddNumbers.add(5);
        oddNumbers.add(7);
        oddNumbers.add(9);

        System.out.println(oddNumbers.toString()); // [1, 3, 5, 7, 9]
    }
}


```

Pour créer des ArrayLists, vous devrez importer la classe `java.util.ArrayList` en haut de votre fichier source.

Ensuite, vous commencez par écrire `ArrayList` puis, à l'intérieur d'une paire de signes inférieur-supérieur, vous écrirez le type de données pour les éléments. Ensuite, vous ajouterez le nom de l'ArrayList lui-même suivi de l'opérateur d'affectation et de `new ArrayList<>()`.

Vous ne pouvez pas créer d'ArrayLists de types primitifs, vous devrez donc utiliser la classe wrapper correspondante.

Bien que ces éléments aient des indices basés sur zéro comme les tableaux, vous ne pouvez pas utiliser la notation des crochets pour y accéder. Au lieu de cela, vous devrez utiliser la méthode `get()` :

```java
import java.util.ArrayList;

public class Main {
    public static void main (String[] args) {
        ArrayList<Integer> oddNumbers = new ArrayList<>();

        oddNumbers.add(1);
        oddNumbers.add(3);
        oddNumbers.add(5);
        oddNumbers.add(7);
        oddNumbers.add(9);

        System.out.println(oddNumbers.get(2)); // 5
    }
}
```

La méthode `get()` obtiendra la valeur à l'index donné. Tout comme `get()`, vous pouvez utiliser la méthode `set()` pour mettre à jour la valeur d'un élément.

```java
import java.time.LocalDate;
import java.util.ArrayList;

public class Main {
    public static void main (String[] args) {
        ArrayList<Integer> oddNumbers = new ArrayList<>();

        oddNumbers.add(1);
        oddNumbers.add(3);
        oddNumbers.add(5);
        oddNumbers.add(7);
        oddNumbers.add(9);

        oddNumbers.set(2, 55);

        System.out.println(oddNumbers.get(2)); // 55
    }
}
```

Le premier paramètre de la méthode `set()` est l'index et le second est la valeur mise à jour.

Il n'y a pas de propriété `length` comme dans un tableau, mais vous pouvez utiliser la méthode `size()` sur n'importe quel ArrayList pour connaître sa longueur.

```
import java.util.ArrayList;

public class Main {
    public static void main (String[] args) {
        ArrayList<Integer> oddNumbers = new ArrayList<>();

        oddNumbers.add(1);
        oddNumbers.add(3);
        oddNumbers.add(5);
        oddNumbers.add(7);
        oddNumbers.add(9);

        System.out.println(oddNumbers.size()); // 5
    }
}
```

Vous pouvez supprimer des éléments d'un ArrayList en utilisant la méthode remove :

```java
import java.util.ArrayList;

public class Main {
    public static void main (String[] args) {
        ArrayList<Integer> oddNumbers = new ArrayList<>();

        oddNumbers.add(1);
        oddNumbers.add(3);
        oddNumbers.add(5);
        oddNumbers.add(7);
        oddNumbers.add(9);

        oddNumbers.remove(Integer.valueOf(7));
        oddNumbers.remove(Integer.valueOf(9));

        System.out.println(oddNumbers.toString()); // [1, 3, 5]
    }
}


```

La méthode `remove()` peut supprimer un élément par valeur ou par index. Si vous passez une valeur entière primitive à la méthode, elle supprimera l'élément à l'index donné.

Mais si vous passez un objet comme dans ce code, la méthode trouvera et supprimera cet élément donné. La méthode `valueOf()` est présente dans toutes les classes wrapper et elle peut convertir une valeur primitive en un type de référence.

### Comment Ajouter ou Supprimer Plusieurs Éléments

Vous avez déjà vu des exemples des méthodes `add()` et `remove()`. Il existe deux autres méthodes `addAll()` et `removeAll()` pour travailler avec plusieurs éléments.

```java
import java.util.ArrayList;

public class Main {
    public static void main (String[] args) {
        ArrayList<Integer> oddNumbers = new ArrayList<>();

        oddNumbers.add(1);
        oddNumbers.add(3);
        oddNumbers.add(5);

        ArrayList<Integer> moreOddNumbers = new ArrayList<>();

        moreOddNumbers.add(7);
        moreOddNumbers.add(9);
        moreOddNumbers.add(11);

        oddNumbers.addAll(moreOddNumbers); // [1, 3, 5, 7, 9, 11]

        System.out.println(oddNumbers.toString());

        oddNumbers.removeAll(moreOddNumbers);

        System.out.println(oddNumbers.toString()); // [1, 3, 5]
    }
}


```

Les deux méthodes acceptent des collections comme paramètre. Dans le code ci-dessus, vous créez deux ArrayLists séparés et les joignez en utilisant la méthode `addAll()`. 

Ensuite, vous supprimez les éléments du deuxième ArrayList en utilisant la méthode `removeAll()` et l'ArrayList revient à son état initial.

Vous pouvez également supprimer tous les éléments d'un ArrayList en utilisant la méthode `clear()` :

```java
import java.util.ArrayList;

public class Main {
    public static void main (String[] args) {
        ArrayList<Integer> oddNumbers = new ArrayList<>();

        oddNumbers.add(1);
        oddNumbers.add(3);
        oddNumbers.add(5);

        oddNumbers.clear();
        
        System.out.println(oddNumbers.toString()); // []
    }
}
```

La méthode ne nécessite aucun paramètre et ne retourne aucune valeur. Elle vide simplement votre ArrayList en un seul appel.

### Comment Supprimer des Éléments Basés sur une Condition

La méthode `removeIf()` peut supprimer des éléments d'un ArrayList s'ils répondent à une certaine condition :

```java
import java.util.ArrayList;

public class Main {
    public static void main (String[] args) {
        ArrayList<Integer> numbers = new ArrayList<>();

        for (int i = 0; i <= 10; i++) {
            numbers.add(i);
        }

        System.out.println(numbers.toString()); // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        numbers.removeIf(number -> number % 2 == 1);

        System.out.println(numbers.toString()); // [0, 2, 4, 6, 8, 10]
    }
}
```

La méthode prend une expression lambda comme paramètre. Les expressions lambda sont comme des méthodes sans nom. Elles peuvent recevoir des paramètres et travailler avec eux.

Ici, la méthode `removeIf()` parcourra l'ArrayList et passera chaque élément à l'expression lambda comme valeur de la variable `number`.

Ensuite, l'expression lambda vérifiera si le nombre donné est divisible par 2 ou non et retournera `true` ou `false` en fonction de cela.

Si l'expression lambda retourne `true`, la méthode `removeIf()` conservera la valeur. Sinon, la valeur sera supprimée.

### Comment Cloner et Comparer des ArrayLists

Pour faire une copie d'un ArrayList, vous pouvez utiliser la méthode `clone()`.

```java
import java.util.ArrayList;

public class Main {
    public static void main (String[] args) {
        ArrayList<Integer> numbers = new ArrayList<>();

        for (int i = 0; i <= 10; i++) {
            numbers.add(i);
        }

        ArrayList<Integer> numbersCloned = (ArrayList<Integer>)numbers.clone();

        System.out.println(numbersCloned.equals(numbers)); // true
    }
}


```

La méthode `clone()` retourne un objet, vous devrez donc le convertir en un ArrayList approprié manuellement. Vous pouvez comparer deux ArrayLists en utilisant la méthode `equals()` comme pour les tableaux.

### Comment Vérifier si un Élément est Présent ou si l'ArrayList est Vide

Vous pouvez utiliser la méthode `contains()` pour vérifier si un ArrayList contient un élément donné ou non :

```java
import java.util.ArrayList;

public class Main {
    public static void main (String[] args) {
        ArrayList<Integer> oddNumbers = new ArrayList<>();

        oddNumbers.add(1);
        oddNumbers.add(3);
        oddNumbers.add(5);
        oddNumbers.add(7);
        oddNumbers.add(9);

        System.out.println(oddNumbers.isEmpty()); // false
        System.out.println(oddNumbers.contains(5)); // true
    }
}
```

Si vous voulez vérifier si un ArrayList est vide ou non, appelez simplement la méthode `isEmpty()` sur celui-ci et vous obtiendrez un booléen en retour.

### Comment Trier un ArrayList

Vous pouvez trier un ArrayList dans différents ordres en utilisant la méthode `sort()` :

```java
import java.util.ArrayList;
import java.util.Comparator;

public class Main {
    public static void main (String[] args) {
        ArrayList<Integer> oddNumbers = new ArrayList<>();

        oddNumbers.add(5);
        oddNumbers.add(7);
        oddNumbers.add(1);
        oddNumbers.add(9);
        oddNumbers.add(3);

        System.out.println(oddNumbers.toString()); [5, 7, 1, 9, 3]

        oddNumbers.sort(Comparator.naturalOrder());

        System.out.println(oddNumbers.toString()); [1, 3, 5, 7, 9]
    }
}
```

La méthode `sort()` prend un comparateur comme paramètre. Un comparateur impose l'ordre de tri à l'ArrayList.

Vous pouvez trier l'ArrayList dans l'ordre inverse en changeant simplement le comparateur passé :

```java
import java.util.ArrayList;
import java.util.Comparator;

public class Main {
    public static void main (String[] args) {
        ArrayList<Integer> oddNumbers = new ArrayList<>();

        oddNumbers.add(5);
        oddNumbers.add(7);
        oddNumbers.add(1);
        oddNumbers.add(9);
        oddNumbers.add(3);

        System.out.println(oddNumbers.toString()); // [5, 7, 1, 9, 3]

        oddNumbers.sort(Comparator.reverseOrder());

        System.out.println(oddNumbers.toString()); // [9, 7, 5, 3, 1]
    }
}
```

Les comparateurs ont d'autres usages également, mais ceux-ci sont hors du cadre de ce livre.

### Comment Conserver les Éléments Communs de Deux ArrayLists

Imaginez un scénario où vous avez deux ArrayLists. Maintenant, vous devrez trouver quels éléments sont présents dans les deux ArrayLists et supprimer le reste du premier ArrayList.

```java
import java.util.ArrayList;

public class Main {
    public static void main (String[] args) {
        ArrayList<Integer> oddNumbers = new ArrayList<>();

        oddNumbers.add(1);
        oddNumbers.add(3);
        oddNumbers.add(5);

        ArrayList<Integer> moreOddNumbers = new ArrayList<Integer>();

        moreOddNumbers.add(5);
        moreOddNumbers.add(7);
        moreOddNumbers.add(9);

        oddNumbers.retainAll(moreOddNumbers);

        System.out.println(oddNumbers.toString()); // [5]
    }
}
```

La méthode `retainAll()` peut se débarrasser des éléments non communs du premier ArrayList pour vous. Vous devrez appeler la méthode sur l'ArrayList que vous souhaitez manipuler et passer le deuxième ArrayList comme paramètre.

### Comment Effectuer une Action sur Tous les Éléments d'un ArrayList

Vous avez déjà appris à faire des boucles dans les sections précédentes. Eh bien, les ArrayLists ont leur propre méthode `forEach()` qui prend une expression lambda comme paramètre et peut effectuer une action sur tous les éléments de l'ArrayList.

```java
import java.util.ArrayList;

public class Main {
    public static void main (String[] args) {
        ArrayList<Integer> oddNumbers = new ArrayList<>();

        oddNumbers.add(1);
        oddNumbers.add(3);
        oddNumbers.add(5);
        oddNumbers.add(7);
        oddNumbers.add(9);

        oddNumbers.forEach(number -> {
            number = number * 2;
            System.out.printf("%d ", number); // 2 6 10 14 18
        });

        System.out.println(oddNumbers.toString()); // [1, 3, 5, 7, 9]
    }
}
```

La dernière fois, l'expression lambda que vous avez vue était sur une seule ligne – mais elles peuvent être plus grandes. Ici, la méthode `forEach()` parcourra l'ArrayList et passera chaque élément à l'expression lambda comme valeur de la variable `number`.

L'expression lambda multipliera ensuite la valeur fournie par 2 et l'imprimera sur le terminal. Cependant, l'ArrayList original restera inchangé.

## Comment Travailler avec les HashMaps en Java

Les HashMaps en Java peuvent stocker des éléments sous forme de paires clé-valeur. Ce type de collection est comparable aux dictionnaires en Python et aux objets en JavaScript.

```java
import java.util.HashMap;

public class Main {
    public static void main (String[] args) {
        HashMap<String, Double> prices = new HashMap<>();

        prices.put("apple", 2.0);
        prices.put("orange", 1.8);
        prices.put("guava", 1.5);
        prices.put("berry", 2.5);
        prices.put("banana", 1.0);

        System.out.printf(prices.toString()); // {orange=1.8, banana=1.0, apple=2.0, berry=2.5, guava=1.5}
    }
}
```

Pour créer des HashMaps, vous devrez d'abord importer la classe `java.util.HashMap` en haut de votre fichier source.

Ensuite, vous commencez par écrire `HashMap` puis, à l'intérieur d'une paire de signes inférieur-supérieur, vous écrirez le type de données pour la clé et la valeur.

Ici, les clés seront des chaînes de caractères et les valeurs seront des doubles. Après cela, l'opérateur d'affectation, suivi de `new HashMap<>()`.

Vous pouvez utiliser la méthode `put()` pour insérer un enregistrement dans le HashMap. La méthode prend la clé comme premier paramètre et sa valeur correspondante comme deuxième paramètre.

Il existe également la méthode `putIfAbsent()` qui ajoute l'élément donné uniquement s'il n'existe pas déjà dans le HashMap.

```java
import java.util.HashMap;

public class Main {
    public static void main (String[] args) {
        HashMap<String, Double> prices = new HashMap<>();

        prices.put("apple", 2.0);
        prices.put("orange", 1.8);
        prices.put("guava", 1.5);
        prices.put("berry", 2.5);
        prices.put("banana", 1.0);

        prices.putIfAbsent("guava", 2.9);

        System.out.println(prices.toString()); // {orange=1.8, banana=1.0, apple=2.0, berry=2.5, guava=1.5}
    }
}
```

Vous pouvez utiliser la méthode `get()` pour extraire une valeur du HashMap. La méthode prend la clé comme paramètre.

```java
import java.util.HashMap;

public class Main {
    public static void main (String[] args) {
        HashMap<String, Double> prices = new HashMap<>();

        prices.put("apple", 2.0);
        prices.put("orange", 1.8);
        prices.put("guava", 1.5);
        prices.put("berry", 2.5);
        prices.put("banana", 1.0);

        System.out.println(prices.get("banana")); // 1.000000
    }
}
```

Il existe une autre variation de cette méthode. La méthode `getOrDefault()` fonctionne comme `get()` mais si la clé donnée n'est pas trouvée, elle retournera une valeur par défaut spécifiée.

```java
import java.util.HashMap;

public class Main {
    public static void main (String[] args) {
        HashMap<String, Double> prices = new HashMap<>();

        prices.put("apple", 2.0);
        prices.put("orange", 1.8);
        prices.put("guava", 1.5);
        prices.put("berry", 2.5);
        prices.put("banana", 1.0);

        System.out.println(prices.getOrDefault("jackfruit", 0.0)); // 0.0
    }
}
```

La valeur par défaut doit correspondre au type des valeurs dans le HashMap. Vous pouvez mettre à jour une valeur dans un HashMap en utilisant la méthode `replace()` :

```java
import java.util.HashMap;

public class Main {
    public static void main (String[] args) {
        HashMap<String, Double> prices = new HashMap<>();

        prices.put("apple", 2.0);
        prices.put("orange", 1.8);
        prices.put("guava", 1.5);
        prices.put("berry", 2.5);
        prices.put("banana", 1.0);

        prices.replace("berry", 2.8);

        System.out.printf(prices.toString()); // {orange=1.8, banana=1.0, apple=2.0, berry=2.8, guava=1.5}
    }
}
```

Pour supprimer des éléments d'un HashMap, vous pouvez utiliser la méthode `remove()` :

```java
import java.util.HashMap;

public class Main {
    public static void main (String[] args) {
        HashMap<String, Double> prices = new HashMap<>();

        prices.put("apple", 2.0);
        prices.put("orange", 1.8);
        prices.put("guava", 1.5);
        prices.put("berry", 2.5);
        prices.put("banana", 1.0);

        prices.remove("guava");

        System.out.printf(prices.toString()); // {orange=1.8, banana=1.0, apple=2.0, berry=2.5}
    }
}
```

Si vous devez savoir combien d'entrées il y a dans un HashMap, vous pouvez le faire en utilisant la méthode `size()` :

```java
import java.util.HashMap;

public class Main {
    public static void main (String[] args) {
        HashMap<String, Double> prices = new HashMap<>();

        prices.put("apple", 2.0);
        prices.put("orange", 1.8);
        prices.put("guava", 1.5);
        prices.put("berry", 2.5);
        prices.put("banana", 1.0);

        System.out.println(prices.size()); // 5
    }
}
```

Enfin, si vous souhaitez vider un HashMap en Java, vous pouvez le faire en utilisant la méthode `clear()`.

```java
import java.util.HashMap;

public class Main {
    public static void main (String[] args) {
        HashMap<String, Double> prices = new HashMap<>();

        prices.put("apple", 2.0);
        prices.put("orange", 1.8);
        prices.put("guava", 1.5);
        prices.put("berry", 2.5);
        prices.put("banana", 1.0);

        prices.clear();

        System.out.println(prices.toString()); // {}
    }
}
```

Tout comme dans les ArrayLists, la méthode ne prend aucun argument et ne retourne aucune valeur.

### Comment Ajouter ou Remplacer Plusieurs Éléments dans une HashMap

Si vous souhaitez ajouter plusieurs éléments dans une HashMap en une seule fois, vous pouvez le faire en utilisant la méthode `putAll()` :

```java
import java.util.HashMap;

public class Main {
    public static void main (String[] args) {
        HashMap<String, Double> prices = new HashMap<>();

        prices.put("apple", 2.0);
        prices.put("orange", 1.8);
        prices.put("guava", 1.5);
        prices.put("berry", 2.5);
        prices.put("banana", 1.0);

        HashMap<String, Double> morePrices = new HashMap<>();

        prices.put("jackfruit", 2.9);
        prices.put("pineapple", 1.1);
        prices.put("tomato", 0.8);

        prices.putAll(morePrices);

        System.out.println(prices.toString()); // {orange=1.8, banana=1.0, apple=2.0, berry=2.5, pineapple=1.1, tomato=0.8, guava=1.5, jackfruit=2.9}
    }
}
```

La méthode prend une autre HashMap comme paramètre et ajoute ses éléments à celle sur laquelle la méthode a été appelée.

Vous pouvez également utiliser la méthode `replaceAll()` pour mettre à jour plusieurs valeurs dans une HashMap.

```java
import java.util.HashMap;

public class Main {
    public static void main (String[] args) {
        HashMap<String, Double> prices = new HashMap<>();

        prices.put("apple", 2.0);
        prices.put("orange", 1.8);
        prices.put("guava", 1.5);
        prices.put("berry", 2.5);
        prices.put("banana", 1.0);

        prices.replaceAll((fruit, price) -> price * 2);

        System.out.println(prices.toString()); // {orange=3.6, banana=2.0, apple=4.0, berry=5.0, guava=3.0}
    }
}
```

La méthode replaceAll parcourt le HashMap et passe chaque paire clé-valeur à l'expression lambda.

Le premier paramètre de l'expression lambda est la clé et le second est la valeur. À l'intérieur de l'expression lambda, vous effectuez vos actions.

### Comment Vérifier si une HashMap Contient un Élément ou si Elle est Vide

Vous pouvez utiliser les méthodes `containsKey()` et `containsValue()` pour vérifier si une HashMap contient une valeur ou non.

```java
import java.util.HashMap;

public class Main {
    public static void main (String[] args) {
        HashMap<String, Double> prices = new HashMap<>();

        prices.put("apple", 2.0);
        prices.put("orange", 1.8);
        prices.put("guava", 1.5);
        prices.put("berry", 2.5);
        prices.put("banana", 1.0);

        System.out.println(prices.containsKey("banana")); // true
        System.out.println(prices.containsValue(2.5)); // true
    }
}
```

La différence entre les deux méthodes est que la méthode `containsKey()` vérifie si la clé donnée existe ou non et la méthode `containsValue()` vérifie si la valeur donnée existe ou non.

Et si vous voulez vérifier si une HashMap est vide ou non, vous pouvez le faire en utilisant la méthode `isEmpty()` :

```java
import java.util.HashMap;

public class Main {
    public static void main (String[] args) {
        HashMap<String, Double> prices = new HashMap<>();

        prices.put("apple", 2.0);
        prices.put("orange", 1.8);
        prices.put("guava", 1.5);
        prices.put("berry", 2.5);
        prices.put("banana", 1.0);

        System.out.println(prices.isEmpty()); // false
    }
}
```

Puisque la méthode retourne une valeur booléenne, vous pouvez l'utiliser dans des instructions if-else.

### Comment Effectuer une Action sur Tous les Éléments d'une HashMap

Comme les ArrayLists, les HashMaps ont également leur propre méthode `forEach()` que vous pouvez utiliser pour parcourir la HashMap et répéter une certaine action sur chaque entrée.

```java
import java.util.HashMap;

public class Main {
    public static void main (String[] args) {
        HashMap<String, Double> prices = new HashMap<>();

        prices.put("apple", 2.0);
        prices.put("orange", 1.8);
        prices.put("guava", 1.5);
        prices.put("berry", 2.5);
        prices.put("banana", 1.0);

        System.out.println("prices after discounts");

        prices.forEach((fruit, price) -> {
            System.out.println(fruit + " - " + (price - 0.5));
        });
    }
}

// prices after discounts
// orange - 1.3
// banana - 0.5
// apple - 1.5
// berry - 2.0
// guava - 1.0
```

La méthode parcourt chaque entrée et passe la clé et la valeur à l'expression lambda. À l'intérieur du corps de l'expression lambda, vous pouvez faire ce que vous voulez.

## Classes et Objets en Java

Voici une [définition utile de la programmation orientée objet](https://fr.wikipedia.org/wiki/Programmation_orientée_objet) :

> La POO (Programmation Orientée Objet) est un paradigme de programmation basé sur le concept d'"objets", qui peuvent contenir des données et du code : des données sous forme de champs (souvent appelés attributs ou propriétés), et du code, sous forme de procédures (souvent appelées méthodes).

Imaginez un système de gestion de bibliothèque où les membres de la bibliothèque peuvent se connecter, consulter les livres qu'ils ont déjà empruntés, en demander de nouveaux, et ainsi de suite.

Dans ce système, les utilisateurs et les livres peuvent tous être des objets. Ces objets auront leurs propres propriétés telles que le nom et la date de naissance (dans le cas d'un utilisateur) et le titre et l'auteur dans le cas des livres.

Les classes en programmation orientée objet sont des plans pour les objets susmentionnés. Nous avons déjà discuté des propriétés possibles des objets utilisateur et livre.

Pour créer une nouvelle classe `User`, faites un clic droit sur le dossier `src` une fois de plus. Ensuite, allez dans **Nouveau > Classe Java**, nommez-la `User`, et appuyez sur Entrée.

En gardant à l'esprit les propriétés précédemment discutées, votre code pour la classe `User` devrait être le suivant :

```java
import java.time.LocalDate;

public class User {
    String name;
    LocalDate birthDay;
}
```

Le `LocalDate` est un type de données de référence qui représente une date. Retournez maintenant au fichier `Main.java` et créez une nouvelle instance de cette classe :

```java
import java.time.LocalDate;

public class Main {
    public static void main (String[] args) {
        User user = new User();

        user.name = "Farhan";
        user.birthDay = LocalDate.parse("1996-07-15");

        System.out.printf("%s was born on %s.", user.name, user.birthDay.toString()); // Farhan was born on 15th July 1996.
    }
}


```

Créer un nouvel utilisateur n'est pas très différent de créer une nouvelle chaîne ou un tableau. Vous commencez par écrire le nom de la classe puis le nom de l'instance ou de l'objet.

Ensuite, vous mettez l'opérateur d'affectation suivi du mot-clé `new` et de l'appel au constructeur. Le constructeur est une méthode spéciale qui initialise l'objet.

Le constructeur a initialisé les propriétés de l'objet avec des valeurs par défaut qui est `null` pour tous ces types de référence.

Vous pouvez accéder aux propriétés de l'objet en écrivant le nom de l'objet suivi d'un point puis le nom de la propriété.

La méthode `LocalDate.parse()` peut analyser une date à partir d'une chaîne donnée. Puisque `birthDay` est un type de référence, vous devrez utiliser la méthode `toString()` pour l'imprimer sur la console.

### Qu'est-ce qu'une Méthode ?

Les variables ou propriétés d'une classe décrivent l'état de ses objets. Les méthodes, en revanche, décrivent le comportement.

Par exemple, vous pouvez avoir une méthode dans votre classe `User` qui calcule l'âge de l'utilisateur.

```java
import java.time.Period;
import java.time.LocalDate;

public class User {
    String name;
    LocalDate birthDay;

    int age() {
        return Period.between(this.birthDay, LocalDate.now()).getYears();
    }
}
```

Ici, le mot-clé `this` représente l'instance actuelle de la classe. Vous commencez par écrire le type de retour de la méthode. Puisque l'âge d'un utilisateur est un entier, le type de retour de cette méthode sera `int`.

Après le type de retour, vous écrivez le nom de la méthode, suivi d'une paire de parenthèses.

Ensuite, vous écrivez le corps de la méthode à l'intérieur d'une paire d'accolades. La classe `Period` en Java exprime un cadre temporel dans le système de calendrier ISO-8601. La méthode `LocalDate.now()` retourne la date actuelle.

Ainsi, l'appel de méthode `Period.between(this.birthDay, LocalDate.now()).getYears()` retournera la différence entre la date actuelle et la date de naissance en années.

Maintenant, dans le fichier `Main.java`, vous pouvez appeler cette méthode comme suit :

```java
import java.time.LocalDate;

public class Main {
    public static void main (String[] args) {
        User user = new User();

        user.name = "Farhan";
        user.birthDay = LocalDate.parse( "1996-07-15");

        System.out.printf("%s is %s years old.", user.name, user.age()); // Farhan a 26 ans.
    }
}


```

Les méthodes peuvent également accepter des paramètres. Par exemple, si vous souhaitez créer une méthode `borrow()` pour insérer de nouveaux livres dans la liste des livres empruntés pour cet utilisateur, vous pouvez le faire comme suit :

```java
import java.time.LocalDate;
import java.time.Period;
import java.util.ArrayList;

public class User {
    String name;
    LocalDate birthDay;
    
    ArrayList<String> borrowedBooks = new ArrayList<String>();

    int age() {
        return Period.between(this.birthDay, LocalDate.now()).getYears();
    }

    void borrow(String bookTitle) {
        this.borrowedBooks.add(bookTitle);
    }
}
```

Dans le fichier `Main.java`, vous pouvez appeler cette méthode comme suit :

```java
public class Main {
    public static void main (String[] args) {
        User user = new User();

        user.name = "Farhan";

        user.borrow("Carmilla");
        user.borrow("Hard West");

        System.out.printf("%s has borrowed these books: %s", user.name, user.borrowedBooks.toString()); // Farhan has borrowed these books: [Carmilla, Hard West]
    }
}


```

Créons également une classe pour les livres :

```java
import java.util.ArrayList;

public class Book {
    String title;
    ArrayList<String> authors = new ArrayList<String>();
}

```

Les livres ont souvent plusieurs auteurs. Maintenant, vous pouvez créer une nouvelle instance de livre dans le fichier `Main.java`.

```java
import java.time.LocalDate;

public class Main {
    public static void main (String[] args) {
        User user = new User();
        user.name = "Farhan";
        user.birthDay = LocalDate.parse( "1996-07-15");

        Book book = new Book();
        book.title = "Carmilla";
        book.authors.add("Sheridan Le Fanu");

        System.out.printf("%s is written by %s", book.title, book.authors.toString()); // Carmilla is written by [Sheridan Le Fanu]

    }
}


```

Maintenant, retournons au fichier `User.java` et créons une relation entre les utilisateurs et les livres :

```java
import java.time.LocalDate;
import java.time.Period;
import java.util.ArrayList;

public class User {
    String name;
    LocalDate birthDay;
    
    ArrayList<Book> borrowedBooks = new ArrayList<Book>();

    int age() {
        return Period.between(this.birthDay, LocalDate.now()).getYears();
    }

    void borrow(Book book) {
        this.borrowedBooks.add(book);
    }
}
```

Au lieu d'utiliser une ArrayList de chaînes, vous utilisez maintenant une ArrayList de livres pour stocker les livres empruntés par cet utilisateur.

Puisque le type d'argument de la méthode a changé, vous devrez mettre à jour le code dans le fichier `Main.java` en conséquence :

```java
import java.time.LocalDate;

public class Main {
    public static void main (String[] args) {
        User user = new User();
        user.name = "Farhan";
        user.birthDay = LocalDate.parse( "1996-07-15");

        Book book = new Book();
        book.title = "Carmilla";
        book.authors.add("Sheridan Le Fanu");

        user.borrow(book);

        System.out.printf("%s has borrowed these books: %s", user.name, user.borrowedBooks.toString()); // Farhan has borrowed these books: [Book@30dae81]
    }
}
```

Tout fonctionne bien sauf le fait que les informations sur le livre n'ont pas été imprimées correctement.

J'espère que vous vous souvenez de la méthode `toString()`. Lorsque vous appelez `user.borrowedBooks.toString()`, le compilateur réalise que les éléments stockés dans l'ArrayList sont des objets ou des types de référence. Il commence donc à appeler les méthodes `toString()` à l'intérieur de ces éléments.

Le problème est qu'il n'y a pas d'implémentation correcte de `toString()` dans votre classe `Book`. Ouvrez `Book.java` et mettez à jour son code comme suit :

```java
import java.util.ArrayList;

public class Book {
    String title;
    ArrayList<String> authors = new ArrayList<String>();

    public String toString() {
        return String.format("%s by %s", this.title, this.authors.toString());
    }
}

```

La méthode `toString()` retourne maintenant une chaîne bien formatée au lieu de la référence de l'objet. Exécutez le code une fois de plus et cette fois la sortie devrait être `Farhan has borrowed these books: [Carmilla by [Sheridan Le Fanu]]`.

Comme vous pouvez le voir, être capable de concevoir votre logiciel autour d'entités de la vie réelle le rend beaucoup plus facile à comprendre. Bien qu'il n'y ait qu'une ArrayList et un tas de chaînes en jeu, cela donne l'impression qu'une véritable opération d'emprunt de livre est en cours.

### Qu'est-ce que la Surcharge de Méthode ?

En Java, plusieurs méthodes peuvent avoir le même nom si leurs paramètres sont différents. Cela s'appelle la surcharge de méthode.

Un exemple peut être la méthode `borrow()` de la classe `User`. Pour l'instant, elle accepte un seul livre comme paramètre. Créons une version surchargée qui peut accepter un tableau de livres à la place.

```java
import java.time.LocalDate;
import java.time.Period;
import java.util.ArrayList;
import java.util.Arrays;

public class User {
    private String name;
    private LocalDate birthDay;
    private ArrayList<Book> borrowedBooks = new ArrayList<Book>();

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getBorrowedBooks() {
        return this.borrowedBooks.toString();
    }

    User (String name, String birthDay) {
        this.name = name;
        this.birthDay = LocalDate.parse(birthDay);
    }

    int age() {
        return Period.between(this.birthDay, LocalDate.now()).getYears();
    }

    void borrow(Book book) {
        borrowedBooks.add(book);
    }

    void borrow(Book[] books) {
        borrowedBooks.addAll(Arrays.asList(books));
    }
}
```

Le type de retour et le nom de la nouvelle méthode sont identiques à la précédente, mais celle-ci accepte un tableau d'objets `Book` au lieu d'un seul objet.

Mettons à jour le fichier `Main.java` pour utiliser cette méthode surchargée.

```java
public class Main {
    public static void main (String[] args) {
        User user = new User("Farhan", "1996-07-15");

        Book book1 = new Book("Carmilla", new String[]{"Sheridan Le Fanu"});
        Book book2 = new Book("Frankenstein", new String[]{"Mary Shelley"});
        Book book3 = new Book("Dracula", new String[]{"Bram Stoker"});

        user.borrow(new Book[]{book1, book2});

        user.borrow(book3);

        System.out.printf("%s has borrowed these books: %s", user.getName(), user.getBorrowedBooks());
    }
}
```

Comme vous pouvez le voir, la méthode `borrow()` accepte maintenant un tableau de livres ou un seul objet livre sans aucun problème.

## Quels sont les Constructeurs en Java ?

Les constructeurs sont un type spécial de méthode qui existe dans chaque classe, et chaque fois que vous créez un nouvel objet à partir d'une classe, le compilateur l'appelle.

Puisque la méthode est appelée pendant la construction d'un objet, elle est appelée un constructeur. Par défaut, un constructeur attribue des valeurs par défaut à toutes ses propriétés.

Pour remplacer le constructeur par défaut, vous devez créer une nouvelle méthode sous vos classes avec le même nom que la classe.

```java
import java.time.LocalDate;
import java.time.Period;
import java.util.ArrayList;

public class User {
    public String name;
    public LocalDate birthDay;
    public ArrayList<Book> borrowedBooks = new ArrayList<Book>();

    User (String name, String birthDay) {
        this.name = name;
        this.birthDay = LocalDate.parse(birthDay);
    }

    int age() {
        return Period.between(this.birthDay, LocalDate.now()).getYears();
    }

    void borrow(Book book) {
        this.borrowedBooks.add(book);
    }
}
```

Maintenant que vous avez un constructeur, au lieu d'analyser la date à partir d'une chaîne dans le fichier `Main.java`, vous pouvez le faire ici.

C'est parce que le format de l'anniversaire est la préoccupation de la classe `User` et la classe `Main` n'a pas besoin de s'en soucier.

Même traitement pour la classe de livre également :

```java
import java.util.ArrayList;
import java.util.Arrays;

public class Book {
    public String title;
    public ArrayList<String> authors = new ArrayList<String>();

    Book(String title, String[] authors) {
        this.title = title;
        this.authors = new ArrayList<String>(Arrays.asList(authors));
    }

    public String toString() {
        return String.format("%s by %s", this.title, this.authors.toString());
    }
}

```

Encore une fois, le type de la collection `authors` n'est pas une préoccupation de la classe `Main`. La manière la plus basique de travailler avec un ensemble de valeurs en Java est un tableau.

Donc, vous recevrez les noms des auteurs sous forme de tableau de la classe `Main` et créerez une ArrayList à partir de celui-ci dans la classe `Book`.

Maintenant, vous devrez passer ces paramètres au constructeur lors de la création d'un nouvel objet utilisateur ou livre dans le fichier `Main.java`.

```java
import java.util.ArrayList;

public class Main {
    public static void main (String[] args) {
        User user = new User("Farhan", "1996-07-15");

        Book book = new Book("Carmilla", new String[]{"Sheridan Le Fanu"});

        user.borrow(book);

        System.out.printf("%s has borrowed these books: %s", user.name, user.borrowedBooks.toString()); // Farhan has borrowed these books: [Carmilla, Hard West]
    }
}
```

Regardez comme c'est déjà plus propre. Mais bientôt, cela aura l'air encore mieux.

## Quels Sont les Modificateurs d'Accès en Java ?

Vous avez déjà vu le mot-clé `public` à plusieurs reprises. C'est l'un des modificateurs d'accès en Java. 

Il existe quatre modificateurs d'accès en Java :

| Type Primitif | Classe Wrapper                              |
|----------------|--------------------------------------------|
| Par Défaut        | Accessible dans le package              |
| Public         | Accessible partout                      |
| Privé        | Accessible dans la classe                |
| Protégé      | Accessible dans la classe et les sous-classes |

Pour l'instant, je vais discuter des modificateurs d'accès `Par Défaut`, `Public` et `Privé`. `Protégé` sera discuté dans une section ultérieure.

Vous avez déjà appris les classes. Les packages sont des collections de plusieurs classes séparées par leur fonctionnalité.

Par exemple, si vous créez un jeu, vous pouvez mettre toutes les classes liées à la physique dans un package séparé et celles liées à la graphique dans un autre.

Les packages sont hors du cadre de ce livre, mais à mesure que vous travaillerez sur des projets de plus en plus grands, vous vous y habituerez.

Le modificateur d'accès `Public` est assez explicite. Ces variables, méthodes ou classes sont accessibles depuis n'importe quelle autre classe ou package dans votre projet.

Les `Privé`, en revanche, sont l'inverse. Ils ne sont disponibles qu'à l'intérieur de leur classe.

Prenez la classe `User`, par exemple. Le nom et la date de naissance d'un utilisateur ne devraient pas être accessibles de l'extérieur.

```java
import java.time.LocalDate;
import java.time.Period;
import java.util.ArrayList;

public class User {
    private String name;
    private LocalDate birthDay;
    private ArrayList<Book> borrowedBooks = new ArrayList<Book>();

    User (String name, String birthDay) {
        this.name = name;
        this.birthDay = LocalDate.parse(birthDay);
    }

    int age() {
        return Period.between(this.birthDay, LocalDate.now()).getYears();
    }

    void borrow(Book book) {
        borrowedBooks.add(book);
    }
}
```

C'est mieux. Mettez également à jour la classe `Book` pour masquer les informations sur le titre et l'auteur du monde extérieur.

```java
import java.util.ArrayList;
import java.util.Arrays;

public class Book {
    private String title;
    private ArrayList<String> authors = new ArrayList<String>();

    Book(String title, String[] authors) {
        this.title = title;
        this.authors = new ArrayList<String>(Arrays.asList(authors));
    }

    public String toString() {
        return String.format("%s by %s", this.title, this.authors.toString());
    }
}

```

Puisque les propriétés sont devenues privées maintenant, la ligne `System.out.println()` dans le fichier `Main.java` échouera à y accéder directement et causera un problème.

La solution à ce programme est d'écrire des méthodes publiques que d'autres classes peuvent utiliser pour accéder à ces propriétés.

## Quelles Sont les Méthodes Getter et Setter en Java ?

Les getters et setters sont des méthodes publiques dans les classes utilisées pour lire et écrire des propriétés privées.

```java
import java.time.LocalDate;
import java.time.Period;
import java.util.ArrayList;

public class User {
    private String name;
    private LocalDate birthDay;
    private ArrayList<Book> borrowedBooks = new ArrayList<Book>();

    public String getName() {
        return this.name;
    }

    public String getBirthDay() {
        return this.birthDay.toString();
    }

    public String getBorrowedBooks() {
        return this.borrowedBooks.toString();
    }

    User (String name, String birthDay) {
        this.name = name;
        this.birthDay = LocalDate.parse(birthDay);
    }

    int age() {
        return Period.between(this.birthDay, LocalDate.now()).getYears();
    }

    void borrow(Book book) {
        borrowedBooks.add(book);
    }
}
```

Les méthodes `getName()` et `getBorrowedBooks()` sont responsables de retourner la valeur des variables `name` et `borrowedBooks`.

Vous n'accédez jamais réellement à la variable de date de naissance en dehors de la méthode `age()`, donc un getter n'est pas nécessaire.

Puisque le type de la variable `borrowedBooks` n'est pas une préoccupation de la classe `Main`, le getter s'assure de retourner la valeur dans le format approprié.

Maintenant, mettez à jour le code dans le fichier `Main.java` pour utiliser ces méthodes :

```java
public class Main {
    public static void main (String[] args) {
        User user = new User("Farhan", "1996-07-15");

        Book book = new Book("Carmilla", new String[]{"Sheridan Le Fanu"});

        user.borrow(book);

        System.out.printf("%s has borrowed these books: %s", user.getName(), user.getBorrowedBooks());
    }
}
```

Excellent. Cela est devenu encore plus propre et plus facile à lire. Comme les getters, il y a des setters pour écrire des valeurs dans les propriétés privées.

Par exemple, vous pouvez vouloir permettre à l'utilisateur de changer son nom ou sa date de naissance. La méthode `borrow()` fonctionne déjà comme un setter pour l'ArrayList `borrowedBooks`.

```java
import java.time.LocalDate;
import java.time.Period;
import java.util.ArrayList;

public class User {
    private String name;
    private LocalDate birthDay;
    private ArrayList<Book> borrowedBooks = new ArrayList<Book>();

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }
    
    public void setBirthDay(String birthDay) {
        this.birthDay = LocalDate.parse(birthDay);
    }

    public String getBorrowedBooks() {
        return this.borrowedBooks.toString();
    }

    User (String name, String birthDay) {
        this.name = name;
        this.birthDay = LocalDate.parse(birthDay);
    }

    int age() {
        return Period.between(this.birthDay, LocalDate.now()).getYears();
    }

    void borrow(Book book) {
        borrowedBooks.add(book);
    }
}
```

Maintenant, vous pouvez appeler la méthode `setName()` avec le nom que vous souhaitez attribuer à l'utilisateur. De même, la méthode `setBirthDay()` peut définir la date de naissance.

Vous pouvez implémenter quelques getters et setters pour la classe `Book` également.

```java
import java.util.ArrayList;
import java.util.Arrays;

public class Book {
    private String title;
    private ArrayList<String> authors = new ArrayList<String>();

    public String getTitle() {
        return this.title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getAuthors() {
        return this.authors.toString();
    }

    public void setTitle(String[] authors) {
        this.authors = new ArrayList<String>(Arrays.asList(authors));
    }
    
    Book(String title, String[] authors) {
        this.title = title;
        this.authors = new ArrayList<String>(Arrays.asList(authors));
    }

    public String toString() {
        return String.format("%s by %s", this.title, this.authors.toString());
    }
}
```

Maintenant, vous ne pouvez pas accéder à ces propriétés directement. Au lieu de cela, vous devrez utiliser l'un des getters ou setters.

## Qu'est-ce que l'Héritage en Java ?

L'héritage est une autre grande caractéristique de la programmation orientée objet. Imaginez que vous avez trois types de livres. Les livres réguliers, les livres électroniques et les livres audio.

Bien qu'ils aient des similitudes telles que le titre et l'auteur, ils ont aussi des différences. Par exemple, les livres réguliers et les livres électroniques ont un nombre de pages alors que les livres audio ont une durée d'exécution. Les livres électroniques ont également un format tel que PDF ou EPUB.

Donc, utiliser la même classe pour les trois n'est pas une option. Cela ne signifie pas que vous devrez créer trois classes séparées avec des différences mineures, cependant. Vous pouvez simplement créer des classes séparées pour les livres électroniques et les livres audio et les faire hériter des propriétés et méthodes de la classe `Book`.

Commençons par ajouter le nombre de pages dans la classe `Book` :

```java
import java.util.ArrayList;
import java.util.Arrays;

public class Book {
    private String title;
    private int pageCount;
    private ArrayList<String> authors = new ArrayList<String>();

    Book(String title, int pageCount, String[] authors) {
        this.title = title;
        this.pageCount = pageCount;
        this.authors = new ArrayList<String>(Arrays.asList(authors));
    }

    public String length() {
        return String.format("%s is %d pages long.", this.title, this.pageCount);
    }

    public String toString() {
        return String.format("%s by %s", this.title, this.authors.toString());
    }
}
```

Puisque vous n'allez pas utiliser les getters et setters dans ces exemples, nettoyer semblait être une bonne idée. La méthode `length()` retourne la longueur du livre sous forme de chaîne.

Maintenant, créez une nouvelle classe Java nommée `AudioBook` et mettez le code suivant dedans :

```java
public class AudioBook extends Book{
    private int runTime;

    AudioBook(String title, String[] authors, int runTime) {
        super(title, 0, authors);

        this.runTime = runTime;
    }
}
```

Le mot-clé `extends` permet au compilateur de savoir que cette classe est une sous-classe de la classe `Book`. Cela signifie que cette classe hérite de toutes les propriétés et méthodes de la classe parente.

À l'intérieur de la méthode constructeur `AudioBook`, vous définissez le temps d'exécution pour le livre audio, ce qui est bien – mais vous devrez également appeler manuellement le constructeur de la classe parente.

Le mot-clé `super` en Java fait référence à la classe parente, donc `super(title, 0, authors)` appelle essentiellement la méthode constructeur parente avec les paramètres nécessaires.

Puisque les livres audio n'ont pas de pages, définir le nombre de pages à zéro peut être une solution facile.

Ou vous pouvez créer une version surchargée de la méthode constructeur `Book` qui ne nécessite pas le nombre de pages.

Ensuite, créez une autre classe Java nommée `Ebook` avec le code suivant :

```java
public class Ebook extends Book{
    private String format;

    Ebook(String title, int pageCount, String[] authors, String format) {
        super(title, pageCount, authors);

        this.format = format;
    }
}
```

Cette classe est largement identique à la classe `Book` sauf qu'elle a une propriété de format.

```java
public class Main {
    public static void main (String[] args) {
        Book book = new Book("Carmilla", 200, new String[]{"Sheridan Le Fanu"});
        Ebook ebook = new Ebook("Frankenstein", 220, new String[]{"Mary Shelley"}, "EPUB");
        AudioBook audioBook = new AudioBook("Dracula", new String[]{"Bram Stoker"}, 160);

        System.out.println(book.toString()); // Carmilla by [Sheridan Le Fanu]
        System.out.println(ebook.toString()); // Frankenstein by [Mary Shelley]
        System.out.println(audioBook.toString()); // Dracula by [Bram Stoker]
    }
}
```

Jusqu'à présent, tout fonctionne bien. Mais vous vous souvenez de la méthode `length()` que vous avez écrite dans la classe `Book` ? Elle fonctionnera pour les livres réguliers mais se cassera dans les e-books.

C'est parce que la propriété pageCount est marquée comme `private` et aucune autre classe sauf `Book` ne pourra y accéder. Le titre est également une propriété `private`.

Ouvrez le fichier `Book.java` et marquez les propriétés `title` et `pageCount` comme protégées.

```java
import java.util.ArrayList;
import java.util.Arrays;

public class Book {
    protected String title;
    protected int pageCount;
    private ArrayList<String> authors = new ArrayList<String>();

    Book(String title, int pageCount, String[] authors) {
        this.title = title;
        this.pageCount = pageCount;
        this.authors = new ArrayList<String>(Arrays.asList(authors));
    }

    public String length() {
        return String.format("%s is %d pages long.", this.title, this.pageCount);
    }

    public String toString() {
        return String.format("%s by %s", this.title, this.authors.toString());
    }
}
```

Cela les rendra accessibles depuis les sous-classes. Les livres audio ont un autre problème avec la méthode `length()`.

Les livres audio n'ont pas de nombre de pages. Ils ont des durées d'exécution et cette différence cassera la méthode de longueur.

Une façon de résoudre ce problème est de redéfinir la méthode `length()`.

## Comment Redéfinir une Méthode en Java

Comme le nom l'indique, la redéfinition signifie annuler l'effet d'une méthode en la remplaçant par autre chose.

```java
public class AudioBook extends Book{
    private int runTime;

    AudioBook(String title, String[] authors, int runTime) {
        super(title, 0, authors);

        this.runTime = runTime;
    }

    @Override
    public String length() {
        return String.format("%s is %d minutes long.", this.title, this.runTime);
    }
}
```

Vous redéfinissez une méthode de la classe parente en réécrivant la méthode dans la sous-classe. Le mot-clé `@Override` est une annotation. Les annotations en Java sont des métadonnées.

Il n'est pas obligatoire d'annoter la méthode de cette manière. Mais si vous le faites, le compilateur saura que la méthode annotée redéfinit une méthode parente et s'assurera que vous suivez toutes les règles de redéfinition.

Par exemple, si vous faites une erreur dans le nom de la méthode et qu'il ne correspond à aucune méthode de la classe parente, le compilateur vous informera que la méthode ne redéfinit rien.

```java
public class Main {
    public static void main (String[] args) {
        AudioBook audioBook = new AudioBook("Dracula", new String[]{"Bram Stoker"}, 160);

        System.out.println(audioBook.length()); // Dracula is 160 minutes long.
    }
}
```

Cool, n'est-ce pas ? Chaque fois que vous redéfinissez une méthode en Java, gardez à l'esprit que la méthode originale et la méthode redéfinie doivent avoir le même type de retour, le même nom et les mêmes paramètres.

## Conclusion

Je tiens à vous remercier du fond du cœur pour le temps que vous avez passé à lire ce livre. J'espère que vous avez apprécié votre temps et que vous avez appris tous les concepts fondamentaux de Java.

Ce manuel n'est pas figé dans le temps. Je continuerai à travailler dessus et je le mettrai à jour avec des améliorations, du nouveau contenu et plus encore. Vous pouvez fournir des opinions et des suggestions anonymes sur le manuel [dans ce formulaire](https://forms.gle/RYPzQybBEYNc5q9g9).

En plus de celui-ci, j'ai écrit des manuels complets sur d'autres sujets compliqués disponibles gratuitement sur [freeCodeCamp](https://www.freecodecamp.org/news/author/farhanhasin/).

Ces manuels font partie de ma mission de simplifier les technologies difficiles à comprendre pour tout le monde. Chacun de ces manuels prend beaucoup de temps et d'efforts à écrire.

Si vous avez apprécié mon écriture et souhaitez me motiver, envisagez de laisser des étoiles sur [GitHub](https://github.com/fhsinchy/) et de m'endosser pour des compétences pertinentes sur [LinkedIn](https://www.linkedin.com/in/farhanhasin/).

Je suis toujours ouvert aux suggestions et aux discussions sur [Twitter](https://twitter.com/frhnhsin) ou [LinkedIn](https://www.linkedin.com/in/farhanhasin/). Envoyez-moi des messages directs.

Enfin, envisagez de partager les ressources avec les autres, car :

> Dans l'open source, nous pensons fermement que pour vraiment faire quelque chose de bien, vous devez impliquer beaucoup de gens. — Linus Torvalds

Jusqu'au prochain, restez en sécurité et continuez à apprendre.