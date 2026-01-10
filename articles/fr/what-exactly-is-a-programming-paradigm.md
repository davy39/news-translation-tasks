---
title: Qu'est-ce qu'un paradigme de programmation exactement ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-12T18:00:34.000Z'
originalURL: https://freecodecamp.org/news/what-exactly-is-a-programming-paradigm
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/Add-a-subheading--1-.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: Qu'est-ce qu'un paradigme de programmation exactement ?
seo_desc: 'By Thanoshan MV


  Any fool can write code that a computer can understand. Good programmers write code
  that humans can understand.― Martin Fowler


  When programming, complexity is always the enemy. Programs with great complexity,
  with many moving parts ...'
---

Par Thanoshan MV

> N'importe quel idiot peut écrire du code qu'un ordinateur peut comprendre. Les bons programmeurs écrivent du code que les humains peuvent comprendre. 
> — Martin Fowler

Lors de la programmation, la complexité est toujours l'ennemie. Les programmes très complexes, avec de nombreuses parties mobiles et des composants interdépendants, semblent initialement impressionnants. Cependant, la capacité à traduire un problème du monde réel en une solution simple ou élégante nécessite une compréhension plus profonde. 

Lors du développement d'une application ou de la résolution d'un problème simple, nous disons souvent « Si j'avais plus de temps, j'aurais écrit un programme plus simple ». La raison en est que nous avons créé un programme avec une plus grande complexité. Moins il y a de complexité, plus il est facile de déboguer et de comprendre. Plus un programme devient complexe, plus il est difficile d'y travailler.

**Gérer la complexité est la principale préoccupation d'un programmeur**. Alors, comment les programmeurs gèrent-ils la complexité ? Il existe de nombreuses approches générales qui réduisent la complexité d'un programme ou la rendent plus gérable. L'une des principales approches est un paradigme de programmation. Plongeons dans les paradigmes de programmation !

## Introduction aux paradigmes de programmation

**Le terme paradigme de programmation** fait référence à **un style de programmation**. Il ne fait pas référence à un langage spécifique, mais plutôt à la manière dont vous programmez. 

Il existe de nombreux langages de programmation bien connus, mais tous doivent suivre une certaine stratégie lorsqu'ils sont implémentés. Et cette stratégie est un paradigme.

## Les types de paradigmes de programmation

![Image](https://www.freecodecamp.org/news/content/images/2019/11/types-of-paradigms.png)
_Décrit les différents styles de programmation (Source : geeksforgeeks.org)_

## Paradigme de programmation impérative

Le mot « impératif » vient du latin « impero » signifiant « je commande ».

C'est le même mot dont nous tirons « empereur », et c'est assez approprié. Vous êtes l'empereur. Vous donnez au ordinateur de petits ordres à faire et il les exécute un à la fois et rapporte.

Le paradigme consiste en plusieurs instructions, et après l'exécution de toutes, le résultat est stocké. Il s'agit d'écrire une liste d'instructions pour dire à l'ordinateur quoi faire étape par étape.

Dans un paradigme de programmation impérative, l'ordre des étapes est crucial, car une étape donnée aura des conséquences différentes selon les valeurs actuelles des variables lorsque l'étape est exécutée.

Pour illustrer, trouvons la somme des dix premiers nombres naturels dans l'approche du paradigme impératif. 

Exemple en C :

```c
#include <stdio.h>

int main()
{
    int sum = 0;
    sum += 1;
    sum += 2;
    sum += 3;
    sum += 4;
    sum += 5;
    sum += 6;
    sum += 7;
    sum += 8;
    sum += 9;
    sum += 10;
    
    printf("La somme est : %d\n", sum); // imprime -> La somme est 55

    return 0;
}
```

Dans l'exemple ci-dessus, nous commandons à l'ordinateur quoi faire ligne par ligne. Enfin, nous stockons la valeur et l'imprimons. 

## 1.1 Paradigme de programmation procédurale

La programmation procédurale (qui est également impérative) **permet de diviser ces instructions en procédures**.

**NOTE :** Les procédures ne sont pas des fonctions. La différence entre elles est que les fonctions retournent une valeur, et les procédures non. Plus spécifiquement, les fonctions sont conçues pour avoir des effets secondaires minimaux, et produisent toujours la même sortie lorsqu'on leur donne la même entrée. Les procédures, en revanche, n'ont aucune valeur de retour. Leur but principal est d'accomplir une tâche donnée et de causer un effet secondaire souhaité. 

Un excellent exemple de procédures serait la boucle for bien connue. Le but principal de la boucle for est de causer des effets secondaires et elle ne retourne pas de valeur.

Pour illustrer, trouvons la somme des dix premiers nombres naturels dans l'approche du paradigme procédural.

Exemple en C : 

```c
#include <stdio.h>

int main()
{
    int sum = 0;
    int i =0;
    for(i=1;i<11;i++){
        sum += i;
    }
    
    printf("La somme est : %d\n", sum); // imprime -> La somme est 55

    return 0;
}
```

Dans l'exemple ci-dessus, nous avons utilisé une simple boucle for pour trouver la somme des dix premiers nombres naturels.

Langages qui supportent le paradigme de programmation procédurale :

* C
* C++
* Java
* ColdFusion
* Pascal

### La programmation procédurale est souvent le meilleur choix lorsque :

* Il y a une opération complexe qui inclut des dépendances entre les opérations, et lorsqu'il y a besoin d'une visibilité claire des différents états de l'application ('Chargement SQL', 'SQL chargé', 'Réseau en ligne', 'Aucun matériel audio', etc). Cela est généralement approprié pour le démarrage et l'arrêt de l'application (Holligan, 2016).
* Le programme est très unique et peu d'éléments sont partagés (Holligan, 2016).
* Le programme est statique et n'est pas censé changer beaucoup avec le temps (Holligan, 2016).
* Aucune ou seulement quelques fonctionnalités sont censées être ajoutées au projet avec le temps (Holligan, 2016).

### Pourquoi devriez-vous envisager d'apprendre le paradigme de programmation procédurale ?

* C'est simple.
* Une manière plus facile de suivre le flux du programme.
* Il a la capacité d'être fortement modulaire ou structuré.
* Nécessite moins de mémoire : Il est efficace et effectif.

## 1.2 Paradigme de programmation orientée objet

La POO est le paradigme de programmation le plus populaire en raison de ses avantages uniques comme la modularité du code et la capacité d'associer directement les problèmes commerciaux du monde réel en termes de code.

> La programmation orientée objet offre une manière durable d'écrire du code spaghetti. Elle vous permet d'accumuler des programmes comme une série de correctifs. 
> — Paul Graham

Les caractéristiques clés de la programmation orientée objet incluent Classe, Abstraction, Encapsulation, Héritage et Polymorphisme. 

Une **classe** est un modèle ou un plan à partir duquel les objets sont créés.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/java-oops.png)
_Décrit les concepts clés de la programmation orientée objet (Source : javatpoint.com)_

Les objets sont des instances de classes. Les objets ont des attributs/états et des méthodes/comportements. Les attributs sont des données associées à l'objet tandis que les méthodes sont des actions/fonctions que l'objet peut effectuer.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/oop.png)
_Explique les états et comportements d'un objet (Source : guru99.es)_

**L'abstraction** sépare l'interface de l'implémentation. L'encapsulation est le processus de masquage de l'implémentation interne d'un objet.

**L'héritage** permet de représenter et d'affiner des relations hiérarchiques. Le polymorphisme permet aux objets de différents types de recevoir le même message et de répondre de différentes manières.

Pour illustrer, trouvons la somme des dix premiers nombres naturels dans l'approche du paradigme orienté objet. 

Exemple en Java :

```java
public class Main
{
	public static void main(String[] args) {
		Addition obj = new Addition();
		obj.num = 10;
		int answer = obj.addValues();
		System.out.println("La somme est = "+answer); // imprime -> La somme est 55
	}
}

class Addition {
    int sum =0;
    int num =0;
    int addValues(){
        for(int i=1; i<=num;i++){
            sum += i;
        }
        return sum;
    }
}
```

Nous avons une classe `Addition` qui a deux états, `sum` et `num` qui sont initialisés à zéro. Nous avons également une méthode `addValues()` qui retourne la somme des `num` nombres. 

Dans la classe `Main`, nous avons créé un objet, `obj` de la classe Addition. Ensuite, nous avons initialisé `num` à 10 et nous avons appelé la méthode `addValues()` pour obtenir la somme. 

Langages qui supportent le paradigme orienté objet :

* Python
* Ruby
* Java
* C++
* Smalltalk

### La programmation orientée objet est mieux utilisée lorsque :

* Vous avez plusieurs programmeurs qui n'ont pas besoin de comprendre chaque composant (Holligan, 2016).
* Il y a beaucoup de code qui pourrait être partagé et réutilisé (Holligan, 2016).
* Le projet est censé changer souvent et être ajouté au fil du temps (Holligan, 2016).

### Pourquoi devriez-vous envisager d'apprendre le paradigme de programmation orientée objet ?

* Réutilisation du code grâce à l'héritage.
* Flexibilité grâce au polymorphisme.
* Haute sécurité avec l'utilisation de mécanismes de masquage de données (Encapsulation) et d'abstraction.
* Productivité améliorée du développement logiciel : Un programmeur orienté objet peut assembler de nouveaux objets logiciels pour créer des programmes complètement nouveaux (The Saylor Foundation, n.d.).
* Développement plus rapide : La réutilisation permet un développement plus rapide (The Saylor Foundation, n.d.).
* Coût de développement plus bas : La réutilisation du logiciel réduit également le coût de développement. Typiquement, plus d'efforts sont mis dans l'analyse et la conception orientées objet (OOAD), ce qui réduit le coût global de développement (The Saylor Foundation, n.d.).
* Logiciel de meilleure qualité : Le développement plus rapide du logiciel et le coût de développement plus bas permettent plus de temps et de ressources à être utilisés dans la vérification du logiciel. La programmation orientée objet tend à donner un logiciel de meilleure qualité (The Saylor Foundation, n.d.).

## 1.3 Approche de traitement parallèle

Le traitement parallèle est le traitement des instructions de programme en les divisant parmi plusieurs processeurs.

Un système de traitement parallèle permet à de nombreux processeurs d'exécuter un programme en moins de temps en les divisant.

Langages qui supportent l'approche de traitement parallèle :

* NESL (l'un des plus anciens)
* C
* C++

### L'approche de traitement parallèle est souvent la meilleure à utiliser lorsque :

* Vous avez un système qui a plus d'un CPU ou des processeurs multi-cœurs qui sont couramment trouvés sur les ordinateurs aujourd'hui.
* Vous devez résoudre certains problèmes de calcul qui prennent des heures/jours à résoudre même avec l'avantage d'un microprocesseur plus puissant. 
* Vous travaillez avec des données du monde réel qui nécessitent une simulation et une modélisation plus dynamiques.

### Pourquoi devriez-vous envisager d'apprendre l'approche de traitement parallèle ?

* Accélère les performances.
* Souvent utilisé en Intelligence Artificielle. En savoir plus ici : [Intelligence Artificielle et Traitement Parallèle](https://link.springer.com/chapter/10.1007%2F978-1-4612-1220-1_12) par Seyed H. Roosta.
* Cela facilite la résolution de problèmes puisque cette approche semble être une méthode de division et de conquête. 

Voici quelques ressources utiles pour en savoir plus sur le traitement parallèle :

1. [Programmation Parallèle en C](https://www.gribblelab.org/CBootCamp/A2_Parallel_Programming_in_C.html) par Paul Gribble
2. [Introduction à la Programmation Parallèle avec MPI et OpenMP](https://princetonuniversity.github.io/PUbootcamp/sessions/parallel-programming/Intro_PP_bootcamp_2018.pdf) par Charles Augustine
3. [INTRODUCTION À LA PROGRAMMATION PARALLÈLE AVEC MPI ET OPENMP](https://www.fz-juelich.de/SharedDocs/Downloads/IAS/JSC/EN/slides/mpi/mpi-openmp-handouts.pdf?__blob=publicationFile) par Benedikt Steinbusch

## 2. Paradigme de programmation déclarative

La programmation déclarative est un style de construction de programmes qui exprime la logique d'un calcul sans parler de son flux de contrôle. 

La programmation déclarative est un paradigme de programmation dans lequel le programmeur définit ce qui doit être accompli par le programme sans définir comment cela doit être implémenté. En d'autres termes, l'approche se concentre sur ce qui doit être réalisé au lieu d'instruire comment l'atteindre.

Imaginez le président lors du discours sur l'état de l'Union déclarant ses intentions pour ce qu'il veut qu'il se passe. D'autre part, la programmation impérative serait comme un manager d'une franchise McDonald's. Ils sont très impératifs et, par conséquent, cela rend tout important. Ils disent donc à tout le monde comment faire tout, jusqu'aux actions les plus simples. 

Donc les principales différences sont que l'impératif vous dit **comment faire quelque chose** et le déclaratif vous dit **quoi faire**. 

## 2.1 Paradigme de programmation logique

Le paradigme de programmation logique adopte une approche déclarative pour la résolution de problèmes. Il est basé sur la logique formelle. 

Le paradigme de programmation logique n'est pas composé d'instructions - plutôt, il est composé de faits et de clauses. Il utilise tout ce qu'il sait et essaie de trouver un monde où tous ces faits et clauses sont vrais. 

Par exemple, Socrate est un homme, tous les hommes sont mortels, et donc Socrate est mortel. 

Ce qui suit est un simple programme Prolog qui explique l'instance ci-dessus :

```prolog
	man(Socrates).
	mortal(X) :- man(X).

```

La première ligne peut être lue, "Socrate est un homme." C'est une clause de base, qui représente un fait simple.

La deuxième ligne peut être lue, "X est mortel si X est un homme ;" en d'autres termes, "Tous les hommes sont mortels." C'est une clause, ou règle, pour déterminer quand son entrée X est "mortelle." (Le symbole ":-'', parfois appelé un tourniquet, est prononcé "si"). Nous pouvons tester le programme en posant la question :

```prolog
	?- mortal(Socrates).

```

c'est-à-dire, "Socrate est-il mortel ?" (Le "`?-`" est l'invite de l'ordinateur pour une question). Prolog répondra "`yes`". Une autre question que nous pourrions poser est : 

```prolog
?- mortal(X).
```

C'est-à-dire, "Qui (X) est mortel ?" Prolog répondra "`X = Socrates`".

Pour vous donner une idée, John est le père de Bill et Lisa. Mary est la mère de Bill et Lisa. Maintenant, si quelqu'un pose une question comme "qui est le père de Bill et Lisa ?" ou "qui est la mère de Bill et Lisa ?" nous pouvons apprendre à l'ordinateur à répondre à ces questions en utilisant la programmation logique. 

Exemple en Prolog :

```prolog
/*Nous définissons des faits d'arbre généalogique*/
father(John, Bill).
father(John, Lisa).
mother(Mary, Bill).
mother(Mary, Lisa).

/*Nous poserons des questions à Prolog*/
?- mother(X, Bill).
X = Mary 
```

Exemple expliqué :

```prolog
father(John, Bill).
```

Le code ci-dessus définit que John est le père de Bill.

Nous demandons à Prolog quelle valeur de X rend cette déclaration vraie ? X devrait être Mary pour rendre la déclaration vraie. Il répondra `X = Mary`

```prolog
?- mother(X, Bill).
X = Mary 
```

Langages qui supportent le paradigme de programmation logique :

* Prolog
* Absys
* ALF (langage de programmation fonctionnelle logique algébrique)
* Alice
* Ciao

### Le paradigme de programmation logique est souvent le meilleur à utiliser lorsque :

* Si vous prévoyez de travailler sur des projets comme la preuve de théorèmes, les systèmes experts, la réécriture de termes, les systèmes de types et la planification automatisée.

### Pourquoi devriez-vous envisager d'apprendre le paradigme de programmation logique ?

* Facile à implémenter le code.
* Le débogage est facile.
* Puisqu'il est structuré en utilisant des déclarations vrai/faux, nous pouvons développer les programmes rapidement en utilisant la programmation logique.
* Comme il est basé sur la pensée, l'expression et l'implémentation, il peut être appliqué dans des programmes non informatiques aussi.
* Il supporte des formes spéciales de connaissance telles que la méta-connaissance ou la connaissance de niveau supérieur car elle peut être altérée.

## 2.2 Paradigme de programmation fonctionnelle

Le paradigme de programmation fonctionnelle est sous les projecteurs depuis un certain temps grâce à JavaScript, un langage de programmation fonctionnelle qui a gagné en popularité récemment.

Le paradigme de programmation fonctionnelle a ses racines dans les mathématiques et il est indépendant du langage. Le principe clé de ce paradigme est l'exécution d'une série de fonctions mathématiques.

Vous composez votre programme de fonctions courtes. Tout le code est dans une fonction. Toutes les variables sont limitées à la fonction.

Dans le paradigme de programmation fonctionnelle, les fonctions ne modifient aucune valeur en dehors de la portée de cette fonction et les fonctions elles-mêmes ne sont pas affectées par aucune valeur en dehors de leur portée.

Pour illustrer, identifions si le nombre donné est premier ou non dans le paradigme de programmation fonctionnelle.

Exemple en JavaScript :

```javascript
function isPrime(number){
 for(let i=2; i<=Math.floor(Math.sqrt(number)); i++){
  if(number % i == 0 ){
   return false;
  }
 }
 return true;
}
isPrime(15); // retourne false
```

Dans l'exemple ci-dessus, nous avons utilisé les fonctions mathématiques `Math.floor()` et `Math.sqrt()` pour résoudre notre problème efficacement. Nous pouvons résoudre ce problème sans utiliser les fonctions mathématiques intégrées de JavaScript, mais pour exécuter le code efficacement, il est recommandé d'utiliser les fonctions JS intégrées.

`number` est limité à la fonction `isPrime()` et il ne sera pas affecté par aucune valeur en dehors de sa portée. La fonction `isPrime()` produit toujours la même sortie lorsqu'on lui donne la même entrée.

**NOTE :** il n'y a pas de boucles for et while en programmation fonctionnelle. Au lieu de cela, les langages de programmation fonctionnelle s'appuient sur **la récursion pour l'itération** (Bhadwal, 2019).

Langages qui supportent le paradigme de programmation fonctionnelle :

* Haskell
* OCaml
* Scala
* Clojure
* Racket
* JavaScript

### Le paradigme de programmation fonctionnelle est souvent le meilleur à utiliser lorsque :

* Travailler avec des calculs mathématiques.
* Travailler avec des applications visant la concurrence ou le parallélisme.

### Pourquoi devriez-vous envisager d'apprendre le paradigme de programmation fonctionnelle ?

* Les fonctions peuvent être codées rapidement et facilement.
* Les fonctions à usage général peuvent être réutilisables, ce qui conduit à un développement logiciel rapide.
* Les tests unitaires sont plus faciles.
* Le débogage est plus facile.
* L'application globale est moins complexe puisque les fonctions sont assez simples.

## 2.3 Approche de traitement de base de données

Cette méthodologie de programmation est basée sur les données et leur mouvement. Les instructions du programme sont définies par les données plutôt que par le codage en dur d'une série d'étapes.

Une base de données est une collection organisée d'informations structurées, ou données, généralement stockées électroniquement dans un système informatique. Une base de données est généralement contrôlée par un système de gestion de base de données (SGBD) ("Qu'est-ce qu'une base de données", Oracle, 2019).

Pour traiter les données et les interroger, les bases de données utilisent des **tables**. Les données peuvent alors être facilement accessibles, gérées, modifiées, mises à jour, contrôlées et organisées. 

Une bonne approche de traitement de base de données est cruciale pour toute entreprise ou organisation. Cela est dû au fait que la base de données stocke tous les détails pertinents sur l'entreprise tels que les dossiers des employés, les dossiers des transactions et les détails des salaires.

La plupart des bases de données utilisent le langage de requête structuré (SQL) pour écrire et interroger les données.

Voici un exemple d'approche de traitement de base de données (SQL) :

```sql
CREATE DATABASE personalDetails;
CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
```

La colonne `PersonID` est de type int et contiendra un entier. Les colonnes `LastName`, `FirstName`, `Address` et `City` sont de type varchar et contiendront des caractères, et la longueur maximale pour ces champs est de 255 caractères.

La table `Persons` vide ressemblera maintenant à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot-from-2019-11-10-22-37-53.png)
_Décrit à quoi ressemblera la table Persons après l'exécution_

### L'approche de traitement de base de données est souvent la meilleure à utiliser lorsque :

* Travailler avec des bases de données pour les structurer.
* Accéder, modifier, mettre à jour des données dans la base de données.
* Communiquer avec des serveurs.

### Pourquoi les bases de données sont-elles importantes et pourquoi devriez-vous envisager d'apprendre l'approche de traitement de base de données ?

* Une quantité massive de données est gérée par la base de données : Contrairement aux feuilles de calcul ou autres outils, les bases de données sont utilisées pour stocker une grande quantité de données quotidiennement.
* Précis : Avec l'aide des fonctionnalités intégrées dans une base de données, nous pouvons facilement valider. 
* Facile à mettre à jour les données : Les langages de manipulation de données (DML) tels que SQL sont utilisés pour mettre à jour les données dans une base de données facilement.
* Intégrité des données : Avec l'aide des vérifications de validité intégrées, nous pouvons garantir la cohérence des données.

## Conclusion

Les paradigmes de programmation réduisent la complexité des programmes. Chaque programmeur doit suivre une approche de paradigme lors de l'implémentation de son code. Chacun a ses avantages et ses inconvénients.

Si vous êtes débutant, je vous suggérerais d'apprendre d'abord la programmation orientée objet et la programmation fonctionnelle. Comprenez leurs concepts et essayez de les appliquer dans vos projets. 

Par exemple, si vous apprenez la programmation orientée objet, les piliers de la programmation orientée objet sont l'encapsulation, l'abstraction, l'héritage et le polymorphisme. Apprenez-les en les pratiquant. Cela vous aidera à comprendre leurs concepts à un niveau plus profond, et votre code sera moins complexe et plus efficace.

Je vous encourage fortement à lire plus d'articles liés aux paradigmes de programmation. J'espère que cet article vous a aidé. 

N'hésitez pas à me faire savoir si vous avez des questions.

Vous pouvez me contacter et me connecter sur Twitter [@ThanoshanMV](https://twitter.com/ThanoshanMV).

Merci d'avoir lu.

**Bon codage !**

## Références

* Akhil Bhadwal. (2019). [Programmation Fonctionnelle : Concepts, Avantages, Inconvénients et Applications](https://hackr.io/blog/functional-programming)
* Alena Holligan. (2016). [Quand utiliser la POO plutôt que la programmation procédurale](https://teamtreehouse.com/community/when-to-use-oop-over-procedural-coding)
* The Saylor Foundation. (n.d.). [Avantages et Inconvénients de la Programmation Orientée Objet (POO)](https://resources.saylor.org/wwwresources/archived/site/wp-content/uploads/2013/02/CS101-2.1.2-AdvantagesDisadvantagesOfOOP-FINAL.pdf)
* [Qu'est-ce qu'une base de données | Oracle.](https://www.oracle.com/database/what-is-database.html) (2019).