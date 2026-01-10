---
title: Une Introduction Animée à Clojure – Apprendre les Bases de la Programmation
  Clojure
subtitle: ''
author: Mark Mahoney
co_authors: []
series: null
date: '2025-04-09T23:35:39.007Z'
originalURL: https://freecodecamp.org/news/learn-clojure-programming-basics
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744240649396/3e68ef22-3109-4b43-841e-e947f1821a76.png
tags:
- name: Clojure
  slug: clojure
- name: Functional Programming
  slug: functional-programming
- name: jvm
  slug: jvm
seo_title: Une Introduction Animée à Clojure – Apprendre les Bases de la Programmation
  Clojure
seo_desc: 'This tutorial introduces the programming language, Clojure. Clojure is
  an awesome functional programming language that runs on Java''s Virtual Machine
  (JVM). It is sometimes called a LISP, which is short for ''LISt Processing''.

  You''ll need to have some...'
---

Ce tutoriel présente le langage de programmation, Clojure. [Clojure](https://clojure.org/) est un langage de programmation fonctionnel génial qui s'exécute sur la machine virtuelle Java (JVM). Il est parfois appelé un LISP, qui est l'abréviation de '**LIS**t **P**rocessing'.

Vous devrez avoir une certaine expérience de programmation dans un autre langage pour tirer le meilleur parti de ce tutoriel. Clojure est si différent de la plupart des langages de programmation impératifs qu'il n'a pas vraiment d'importance d'où vous venez, tant que vous connaissez les bases (variables, instructions if, boucles et fonctions).

Si vous cherchez un guide complet pour débutants en programmation, vous pouvez trouver certains de mes autres contenus de programmation ci-dessous.

Ici, je couvrirai les fonctions, les structures de données, l'immuabilité, les fermetures, la récursivité terminale, les séquences paresseuses, les macros et la concurrence.

Clojure est un langage de programmation fonctionnel. Dans celui-ci, la fonction est reine et les données sont immuables. Cela peut être un paradigme différent de celui auquel vous êtes habitué, mais il y a des raisons convaincantes de l'utiliser. L'immuabilité de Clojure est particulièrement bonne pour les programmes qui doivent tirer parti du matériel moderne sur les ordinateurs portables et les téléphones mobiles (plusieurs processeurs partageant une seule mémoire).

Clojure s'exécute sur la [JVM](https://en.wikipedia.org/wiki/Java_virtual_machine). Il peut être difficile de configurer Clojure car cela implique d'installer Java, Leiningen et parfois un plugin d'éditeur. Pour simplifier les choses, je recommande de commencer avec un IDE basé sur le web. Il n'y a pas de moyen plus facile de commencer à programmer en Clojure qu'en utilisant [replit](https://replit.com/). Je recommande de l'utiliser pour écrire vos premiers programmes en Clojure. Si vous vous en sentez capable, consultez [ces docs](https://clojure.org/guides/install_clojure) pour commencer sur votre propre machine.

Même si vous n'utilisez pas Clojure tous les jours, l'apprendre changera votre façon de penser à la programmation. Cela vous aidera à comprendre la récursivité, les fonctions d'ordre supérieur et les transformations de données d'une nouvelle manière. Ces idées se transfèrent bien à d'autres langages comme JavaScript, Python ou Rust. En bref, apprendre Clojure fera de vous un meilleur programmeur.

### **Code Playbacks**

Ce matériel ne sera pas livré comme les tutoriels en ligne traditionnels ou les séries vidéo. Chaque section inclut des liens vers des **code playbacks** interactifs qui animent visuellement les changements apportés à un programme de manière étape par étape, vous aidant à comprendre comment il a été écrit.

Un code playback montre comment un programme évolue en rejouant toutes les étapes de son développement. Il dispose d'un récit fourni par l'auteur, de captures d'écran, de dessins de type tableau blanc et de questions à choix multiples auto-évaluées pour rendre le processus d'apprentissage plus dynamique et interactif.

Voici une courte vidéo YouTube expliquant comment visualiser un code playback :

%[https://youtu.be/uYbHqCNjVDM]

### **Playback Press**

[Playback Press](https://playbackpress.com/books) est une plateforme pour partager des parcours de code interactifs que j'ai créée. Je m'appelle Mark, au fait, professeur d'informatique. Ces livres fournissent des leçons de programmation interactives à travers des animations étape par étape, un tutorat IA et des quiz.

Si vous voulez voir le livre complet sur Clojure, vous pouvez aller ici :

> [An Animated Introduction to Clojure](https://playbackpress.com/books/cljbook), par Mark Mahoney

J'ai également construit [Storyteller](https://markm208.github.io/), l'outil gratuit et open-source qui alimente les code playbacks.

### **AI Tutor**

Lors de la visualisation d'un code playback, vous pouvez poser des questions à un tuteur IA sur le code. Il répond aux questions clairement et patiemment, ce qui en fait une ressource utile pour les apprenants. Vous pouvez également demander au tuteur IA de générer de nouvelles questions à choix multiples auto-évaluées pour tester vos connaissances sur ce que vous apprenez.

Pour accéder au tuteur IA et aux quiz auto-évalués, il suffit de créer un compte gratuit sur Playback Press et d'ajouter le [livre](https://playbackpress.com/books/cljbook) à votre bibliothèque.

### **Table des Matières**

* [Introduction à Clojure](#heading-introduction-a-clojure)

* [Fonctions](#heading-fonctions)

* [Fermetures](#heading-fermetures)

* [Récursivité](#heading-recursivite)

* [Séquences Paresseuses](#heading-sequences-paresseuses)

* [Macros](#heading-macros)

* [Concurence](#heading-concurence)

## **Introduction à Clojure**

Ces premiers programmes montrent comment imprimer à l'écran, effectuer des calculs arithmétiques de base et stocker des données. Passez en revue chacun d'eux maintenant :

* [Hello World!!!](https://playbackpress.com/books/cljbook/chapter/1/1)

* [Lecteurs/évaluateurs et arithmétique simple](https://playbackpress.com/books/cljbook/chapter/1/2)

* [Convertisseur d'âge de chien](https://playbackpress.com/books/cljbook/chapter/1/3)

Ce programme montre comment utiliser la capacité Java intégrée dans la JVM.

* [Interopérabilité Java](https://playbackpress.com/books/cljbook/chapter/1/4)

Ces programmes montrent certaines structures de données de base dans Clojure et comment elles sont immuables.

* [Structures de données Clojure](https://playbackpress.com/books/cljbook/chapter/1/5)

* [Immuabilité efficace (plus sur les structures de données)](https://playbackpress.com/books/cljbook/chapter/1/6)

### **Pratique Hands-On**

**Problème 1**

Écrivez un programme Clojure qui demande à l'utilisateur la longueur et la largeur d'une planche de bois en pouces. Ensuite, affichez le nombre de pieds carrés entiers contenus dans la planche. Par exemple, si la hauteur est de 27 pouces et la largeur de 34 pouces, alors le nombre de pieds carrés est de 6,375.

**Problème 2**

Écrivez un programme qui crée une liste vide et utilise `def` pour stocker une référence appelée `empty-list`. Utilisez `cons` pour ajouter votre nom et stockez-le dans une nouvelle liste appelée `my-name`.

Utilisez `conj` pour ajouter tous vos frères et sœurs à une liste appelée `me-and-my-siblings` (si vous n'en avez pas ou pas autant, vous pouvez utiliser certains des [Kardashians](https://en.wikipedia.org/wiki/Kardashian_family#Members_of_the_Kardashian-Jenner_Family)).

Imprimez tous les noms dans `me-and-my-siblings`. Ensuite, imprimez le troisième nom de la liste `me-and-my-siblings`.

Créez une carte avec tous les noms de vos frères et sœurs comme clés et leurs années de naissance comme valeurs. Utilisez `assoc` pour ajouter votre nom et votre année de naissance à la carte. Utilisez la carte pour imprimer le nom de chacun et leur âge en 2050.

**Problème 3**

Créez une carte avec le nombre de jours dans chacun des mois appelée `days-in-months`. Utilisez les mots-clés Clojure comme `:jan` et `:feb` comme clés et le nombre de jours dans les mois comme valeurs.

Créez une deuxième carte à partir de la première qui a 29 jours pour février. Appelez celle-ci `days-in-months-leapyear`. Assurez-vous de le faire efficacement, utilisez `assoc` pour créer une nouvelle valeur pour février. Enfin, imprimez chacune des cartes.

## **Fonctions**

Ensuite, je vais discuter de la création et de l'appel de fonctions dans Clojure. Clojure est un langage de programmation fonctionnel, donc c'est un sujet assez important.

Les deux premiers programmes montrent comment écrire des fonctions dans Clojure.

* [Fonctions dans Clojure](https://playbackpress.com/books/cljbook/chapter/2/1)

* [Fizz Buzz](https://playbackpress.com/books/cljbook/chapter/2/2)

Ce programme montre comment utiliser une carte pour encapsuler des données avec certaines fonctions qui manipulent les données.

* [Cartes comme objets](https://playbackpress.com/books/cljbook/chapter/2/3)

Ces programmes montrent comment lire et écrire dans un fichier en utilisant des fonctions.

* [Lecture à partir d'un fichier (avec poésie CS)](https://playbackpress.com/books/cljbook/chapter/2/4)

* [Écriture dans un fichier](https://playbackpress.com/books/cljbook/chapter/2/5)

### **Pratique Hands-On**

**Problème 1**

Écrivez trois fonctions mathématiques :

* `square` élève au carré un paramètre passé

* `cube` élève au cube un paramètre passé

* `pow` élève un nombre de base à un exposant


Pour ce groupe de fonctions, n'utilisez aucune fonction mathématique intégrée.

Indice : regardez la fonction Clojure `repeat` et `reduce` pour la fonction `pow`. Utilisez la fonction `let` pour contenir des valeurs temporaires afin qu'elles puissent être référencées plus tard.

**Problème 2**

Écrivez une fonction qui prend un nombre et calculera la valeur factorielle pour ce nombre.

```cpp
5! est 5 * 4 * 3 * 2 * 1 = 120

10! est 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3,628,800
```

Indice : ce type de problème est généralement fait avec la récursivité. Mais pour l'instant, essayez de le faire sans récursivité. Regardez les fonctions Clojure `range` et `reduce`.

**Problème 3**

Écrivez une fonction qui détermine si un nombre est premier ou non. Utilisez les fonctions `range` et `filter` pour filtrer les non-premiers dans une plage de valeurs.

Indice : regardez les fonctions `not-any?` et `mod` pour déterminer si un nombre est premier ou non.

**Problème 4**

Écrivez une fonction qui prend un ou plusieurs paramètres de chaîne, les convertit en nombres, puis les additionne et retourne la somme.

```cpp
(println (add-strings "10")) ;imprime 10

(println (add-strings "10" "20")) ;imprime 30

(println (add-strings "10" "20" "30")) ;imprime 60

(println (add-strings "10" "20" "30" "40")) ;imprime 100
```

Utilisez la fonction `reduce` de Clojure ou `apply` pour transformer les chaînes en nombres puis les additionner.

## **Fermetures**

Une fermeture est un moyen d'associer des données de manière permanente à une fonction.

Le premier programme montre comment lier des données à une fonction.

* [Fermetures](https://playbackpress.com/books/cljbook/chapter/3/1)

Le deuxième programme montre un exemple plus complexe d'utilisation des fermetures.

* [Intérêt dans un compte](https://playbackpress.com/books/cljbook/chapter/3/2)

### **Pratique Hands-On**

**Problème 1**

Écrivez une fonction qui retourne une fonction. Les nombres de Fibonacci sont une séquence de nombres générés en additionnant les deux nombres précédents :

```cpp
0 1 1 2 3 5 8 13 21 34 ...
```

Habituellement, les deux premiers nombres sont supposés être 0 et 1. Mais dans ce cas, retournez une fonction qui utilise les deux premiers nombres spécifiés dans la séquence. Ensuite, générez et imprimez les nombres demandés dans la séquence.

```cpp
(defn fibs-fn[firstFib secondFib] ...) ;;remplissez ceci

(def another-fib (fibs-fn 10 15)) ;;crée une fonction fib qui imprime en commençant par 10 et 15

(another-fib 5) ;;imprime les 5 premiers fibs : 10 15 25 40 65
```

## **Récursivité**

Une fonction récursive est une fonction qui s'appelle elle-même. Puisque chaque appel de fonction entraîne un cadre de pile placé sur la pile d'appels, la récursivité régulière risque de "faire exploser la pile d'appels". La récursivité terminale, avec `recur`, est un moyen efficace de simuler la récursivité sans les inconvénients.

* [Récursivité Terminale](https://playbackpress.com/books/cljbook/chapter/4/1)

* [Récursivité et Fizz-Buzz](https://playbackpress.com/books/cljbook/chapter/4/2)

* [Récursivité et Racines Carrées](https://playbackpress.com/books/cljbook/chapter/4/3)

* [Conversion d'une Chaîne en Entier dans les Bases 2-16](https://playbackpress.com/books/cljbook/chapter/4/4)

* [Planificateur d'Hypothèque](https://playbackpress.com/books/cljbook/chapter/4/5)

### **Pratique Hands-On**

**Problème 1**

Écrivez une fonction récursive pour inverser les lettres d'une chaîne.

```cpp
(reverse-string "Mark Mahoney") ;;retourne "yenohaM kraM"
```

Vous devrez peut-être créer une fonction récursive "helper" qui prend un nombre différent de paramètres que la fonction non récursive ou utiliser la forme `loop`. Assurez-vous d'utiliser la récursivité avec la forme `recur` pour ne pas "faire exploser la pile".

**Problème 2**

Écrivez une fonction qui joindra une série de chaînes ensemble séparées par une autre chaîne. La fonction doit créer et retourner une nouvelle chaîne. Utilisez la récursivité avec `recur`.

```cpp
(defn join [separator & parts]
   ;;votre code ici)

(join ", " "Mark" "Laura" "Buddy" "Patrick" "Willy") ;;"Mark, Laura, Buddy, Patrick, Willy"
```

**Problème 3**

Écrivez une fonction qui prend un entier et le convertit en chaîne. L'utilisateur peut spécifier la base de la chaîne de 2 à 10. Le programme doit utiliser la récursivité et `recur` (soit une fonction récursive soit la forme `loop`).

```cpp
(to-string 100 10) ;;"100" décimal
(to-string 7 2) ;;"111" binaire
```

## **Séquences Paresseuses**

Une séquence paresseuse reporte le coût de la création des valeurs jusqu'à ce qu'elles soient nécessaires. Le premier programme montre comment créer une séquence paresseuse. Les deux suivants sont des exemples plus concrets.

* [Séquences paresseuses](https://playbackpress.com/books/cljbook/chapter/5/1)

* [Générateur de Nombres Premiers Paresseux (Fizz Buzz partie 3)](https://playbackpress.com/books/cljbook/chapter/5/2)

* [Probabilités du Poker](https://playbackpress.com/books/cljbook/chapter/5/3)

### **Pratique Hands-On**

**Problème 1**

Créez une fonction qui génère une séquence paresseuse de carrés. Par exemple, (1 4 9 16 ... à l'infini). Utilisez-la pour imprimer les 10 premières valeurs au carré.

Ensuite, écrivez une fonction qui génère une séquence paresseuse de valeurs élevées à une puissance :

```cpp
(defn lazy-pow [start-val power]
  ...)

(take 6 (lazy-pow 10 2)) ;(100 121 144 169 196 225)
(take 6 (lazy-pow 10 3)) ;(1000 1331 1728 2197 2744 3375)
```

**Problème 2**

Écrivez une fonction qui génère une séquence paresseuse infinie de permutations possibles de la séquence passée.

```cpp
(take 3 (lazy-perm ["a" "b" "c"]))
;("a" "b" "c")

(take 12 (lazy-perm ["a" "b" "c"])) 
;("a" "b" "c" "aa" "ab" "ac" "ba" "bb" "bc" "ca" "cb" "cc")

(take 39 (lazy-perm ["a" "b" "c"])) 
;("a" "b" "c" "aa" "ab" "ac" "ba" "bb" "bc" "ca" "cb" "cc" "aaa" "aab" "aac" "aba" "abb" "abc" "aca" "acb" "acc" "baa" "bab" "bac" "bba" "bbb" "bbc" "bca" "bcb" "bcc" "caa" "cab" "cac" "cba" "cbb" "cbc" "cca" "ccb" "ccc")

(take 120 (lazy-perm ["a" "b" "c"]))
;("a" "b" "c" "aa" "ab" "ac" "ba" "bb" "bc" "ca" "cb" "cc" "aaa" "aab" "aac" "aba" "abb" "abc" "aca" "acb" "acc" "baa" "bab" "bac" "bba" "bbb" "bbc" "bca" "bcb" "bcc" "caa" "cab" "cac" "cba" "cbb" "cbc" "cca" "ccb" "ccc" "aaaa" "aaab" "aaac" "aaba" "aabb" "aabc" "aaca" "aacb" "aacc" "abaa" "abab" "abac" "abba" "abbb" "abbc" "abca" "abcb" "abcc" "acaa" "acab" "acac" "acba" "acbb" "acbc" "acca" "accb" "accc" "baaa" "baab" "baac" "baba" "babb" "babc" "baca" "bacb" "bacc" "bbaa" "bbab" "bbac" "bbba" "bbbb" "bbbc" "bbca" "bbcb" "bbcc" "bcaa" "bcab" "bcac" "bcba" "bcbb" "bcbc" "bcca" "bccb" "bccc" "caaa" "caab" "caac" "caba" "cabb" "cabc" "caca" "cacb" "cacc" "cbaa" "cbab" "cbac" "cbba" "cbbb" "cbbc" "cbca" "cbcb" "cbcc" "ccaa" "ccab" "ccac" "ccba" "ccbb" "ccbc" "ccca" "cccb" "cccc")
```

## **Macros**

Une macro spécifie un certain code à exécuter, un peu comme une fonction, mais elle permet également de remplacer une partie de ce code par des valeurs provenant de l'utilisateur.

Le code dans une macro est un peu comme un modèle qui peut être modifié pour répondre aux besoins de l'appelant. Avec cette fonctionnalité puissante, le langage peut être étendu pour faire des choses que l'inventeur du langage n'a jamais pensé à ajouter.

* [Macros](https://playbackpress.com/books/cljbook/chapter/6/1)

* [Set macros](https://playbackpress.com/books/cljbook/chapter/6/2)

### **Pratique Hands-On**

**Problème 1**

Écrivez une macro qui prend une note obtenue lors d'une tâche étudiante (sur une échelle de 0-100) et un certain code à exécuter si la note est réussie ou échouée.

```cpp
(defmacro eval-grade [grade if-passing if-failing] ...)
```

Et utilisez-la pour imprimer ou appeler une fonction en fonction de la valeur de la note

```cpp
(def users-grade 43)

(eval-grade users-grade (println "Passing") (println "Failing")) ;;"Failing"

(eval-grade users-grade (praise users-grade) (warning users-grade)) ;;appelle la fonction d'avertissement
```

## **Concurence**

La concurrence dans Clojure est un grand sujet. Je commence par discuter des threads. Ensuite, je parle des différentes stratégies pour gérer les données partagées entre différents threads.

* [Threads](https://playbackpress.com/books/cljbook/chapter/7/1)

* [Poker avec threads](https://playbackpress.com/books/cljbook/chapter/7/2)

* [refs et threads](https://playbackpress.com/books/cljbook/chapter/7/3)

* [Atomes](https://playbackpress.com/books/cljbook/chapter/7/4)

* [Poker avec atomes](https://playbackpress.com/books/cljbook/chapter/7/5)

* [Journalisation des threads avec agents](https://playbackpress.com/books/cljbook/chapter/7/6)

* [Concurence plus simple](https://playbackpress.com/books/cljbook/chapter/7/7)

### **Pratique Hands-On**

**Problème 1**

Ce laboratoire vous demande de créer un programme Clojure qui comptera le nombre de nombres premiers dans une plage donnée.

Créez un pool de threads et faites en sorte que chaque thread vérifie un seul nombre dans la plage. S'il trouve un nombre premier, il augmentera un compteur (qui doit être un `atom` puisqu'il est partagé par tous les threads). Regardez le programme ci-dessus sur les Atomes comme point de départ.

## Conclusion

Si vous êtes arrivé jusqu'ici, vous avez déjà fait des pas significatifs vers l'apprentissage d'un langage qui peut changer la façon dont vous écrivez et pensez au code.

Clojure offre une perspective fraîche sur la programmation, une qui se concentre sur la simplicité, l'immuabilité et la puissance des fonctions. Apprendre Clojure changera votre cerveau et vous emporterez ces leçons avec vous vers d'autres langages également.

Alors continuez à expérimenter, continuez à poser des questions et continuez à pratiquer pour affûter vos compétences.

## **Commentaires et Retours**

Vous pouvez trouver tous ces code playbacks dans le livre gratuit, [An Animated Introduction to Clojure](https://playbackpress.com/books/cljbook/). Il y a plus de livres gratuits ici :

* [An Animated Introduction to Programming in C++](https://playbackpress.com/books/cppbook/)

* [An Animated Introduction to Programming with Python](https://playbackpress.com/books/pybook)

* [Database Design and SQL for Beginners](https://playbackpress.com/books/sqlbook)

* [Worked SQL Examples](https://playbackpress.com/books/workedsqlbook)

* [Programming with SQLite](https://playbackpress.com/books/sqlitebook)

* [An Introduction to Web Development from Back to Front](https://playbackpress.com/books/webdevbook)

* [An Animated Introduction to Clojure](https://playbackpress.com/books/cljbook)

* [An Animated Introduction to Elixir](https://playbackpress.com/books/exbook)

* [A Brief Introduction to Ruby](https://playbackpress.com/books/rubybook)

* [Mobile App Development with Dart and Flutter](https://playbackpress.com/books/flutterbook)

* [OO Design Patterns with Java](https://playbackpress.com/books/patternsbook)

* [How I Built It: Word Zearch](https://playbackpress.com/books/wordzearchbook)

Les commentaires et retours sont les bienvenus par email : [mark@playbackpress.com](mailto:mark@playbackpress.com).

Si vous souhaitez soutenir mon travail et aider à garder Playback Press gratuit pour tous, envisagez de faire un don en utilisant [GitHub Sponsors](https://github.com/sponsors/markm208). J'utilise toutes les donations pour les coûts d'hébergement. Votre soutien m'aide à continuer à créer du contenu éducatif comme celui-ci. Merci !