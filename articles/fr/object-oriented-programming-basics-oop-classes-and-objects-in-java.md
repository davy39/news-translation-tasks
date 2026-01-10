---
title: Les bases de la programmation orientée objet – OOP, classes et objets en Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-02T07:33:30.000Z'
originalURL: https://freecodecamp.org/news/object-oriented-programming-basics-oop-classes-and-objects-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Gradient-Modern-Digital-Marketing-Facebook-Cover--51-.png
tags:
- name: Java
  slug: java
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: Les bases de la programmation orientée objet – OOP, classes et objets en
  Java
seo_desc: 'By Avdhoot Fulsundar

  Java is a powerful programming language to develop software in. And if you''re trying
  to learn it, that''s great.

  The first thing you''ll need to know to develop software in Java is Object Oriented
  Programming, or OOP for short.

  Now...'
---

Par Avdhoot Fulsundar

Java est un langage de programmation puissant pour développer des logiciels. Et si vous essayez de l'apprendre, c'est génial.

La première chose que vous devrez connaître pour développer des logiciels en Java est la programmation orientée objet, ou OOP en abrégé.

Maintenant, si vous vous demandez : "Qu'est-ce que l'OOP ?", ne vous inquiétez pas. Nous allons couvrir les concepts clés maintenant.

## Qu'est-ce que la programmation orientée objet ?

Un langage orienté objet possède deux éléments très importants : les classes et les objets. Vous utilisez les deux lorsque vous écrivez un programme en Java.

L'OOP vous permet de créer des blocs de code réutilisables appelés objets. Vous pouvez les considérer comme de petites machines.

Imaginez que vous construisez une voiture. Vous ne pouvez pas simplement jeter toutes les pièces ensemble et espérer qu'elles fonctionnent magiquement.

Au lieu de cela, vous décomposez la voiture en parties plus petites comme le moteur, les roues et le châssis. Chacune de ces parties a un travail spécifique à faire et peut être travaillée indépendamment.

De même, l'OOP vous permet de diviser un grand programme en petits morceaux de code. Cela rend le code plus facile à comprendre et à maintenir.

D'accord, alors qu'est-ce que les classes et les objets ? 😶

### Qu'est-ce que les classes en Java ?

Les classes sont simplement des plans pour créer des objets. Pensez à une classe comme au plan d'un architecte pour construire une maison.

Le plan d'un architecte définit la structure, la disposition et la forme de la maison. De même, une classe définit la structure et le comportement d'un objet.

Vous pouvez également penser à une classe comme à une recette pour créer des objets. Tout comme une recette vous indique quels ingrédients utiliser, comment les préparer et combien de temps les cuire, une classe vous indique quelles propriétés l'objet possède, ce qu'il peut faire, et ainsi de suite.

La beauté des classes est qu'elles vous permettent de créer des objets qui se comportent de manière cohérente et prévisible.

Une classe a ses propres attributs, objets et méthodes.

En termes simples :

* **Attributs** : À quoi ressemble la classe
* **Méthodes** : Ce que fait la classe
* **Objets** : Ce qu'est la classe

Disons que vous définissez une classe appelée `Avengers`.

La première question est, à quoi ressemblera-t-elle (c'est-à-dire, quels sont ses attributs) ?

La classe `Avengers` aura une combinaison spéciale, une arme incroyable et une histoire d'origine incroyable. 🦸‍♀️ Ce sont les attributs de la classe `Avengers`.

Examinons de plus près les attributs maintenant.

## Qu'est-ce que les attributs ?

Imaginez que vous avez un puzzle. Chaque pièce de puzzle a sa propre forme, couleur et design uniques.

En OOP, les attributs sont comme les différentes caractéristiques d'une pièce de puzzle. Ils définissent les propriétés d'un objet, tout comme la forme, la couleur et le design d'une pièce de puzzle définissent son rôle dans la complétion du puzzle.

De même, la forme de chaque pièce de puzzle détermine où elle s'insère, les attributs aident à définir l'identité et le but d'un objet. Par exemple, un objet chat peut avoir des attributs comme la race, l'âge et la couleur du pelage, tandis qu'un objet livre peut avoir des attributs comme le titre, l'auteur et le genre.

Ces attributs aident à différencier un objet d'un autre, et leurs attributs uniques pour créer un programme complet.

Revenons à nos trois questions. La prochaine chose à demander est : que fera un Avenger ?

Un Avenger sauvera le monde, vaincra les méchants, accomplira des tâches impossibles, prétendra être un être humain normal, et bien d'autres choses.

Ce sont les méthodes de la classe `Avengers`.

## Qu'est-ce que les méthodes ?

En OOP, les méthodes définissent les actions que les objets peuvent effectuer.

Les méthodes peuvent prendre des arguments, tout comme les fonctions, et elles peuvent également retourner des valeurs. Cela permet aux objets d'interagir avec d'autres objets et d'effectuer des tâches complexes dans un programme.

Par exemple, un objet voiture peut avoir des méthodes comme `demarrer_moteur()` et `arreter_moteur()` pour manipuler ses attributs comme la vitesse et le niveau de carburant, tandis qu'un objet compte bancaire peut avoir des méthodes comme `deposer()` et `retirer()` pour manipuler son solde.

La question finale est : qui sera un Avenger ?

Eh bien, vous pourriez avoir Ironman, Captain America, Superman, et...

![Homelander de The Boys](https://www.freecodecamp.org/news/content/images/2023/04/image-150.png)
_Homelander de The Boys_

Désolé, pas lui. Il est un peu méchant. 😅

Tous les super-héros mentionnés ci-dessus (sauf Homelander) sont des objets de la classe `Avengers`.

Mais qu'est-ce que les objets, techniquement ?

## Qu'est-ce que les objets ?

Imaginez que vous planifiez un road trip unique avec vos amis, et que vous voulez emporter tous les articles nécessaires pour le voyage.

Vous commencez par faire une liste de toutes les choses dont vous avez besoin, comme des snacks, des boissons, des vêtements, et ainsi de suite.

En programmation orientée objet (OOP), les objets sont comme les articles sur votre liste d'emballage. Ils ont leurs propres caractéristiques et comportements uniques.

Comme un sac de chips a une saveur spécifique, une taille et des informations nutritionnelles, un objet en OOP a son propre ensemble d'attributs et de méthodes.

Ou similaire à la façon dont vous pouvez utiliser différents articles sur votre road trip pour différents usages, les objets peuvent également être utilisés de différentes manières dans un programme. Par exemple, vous pouvez utiliser un objet voiture pour conduire d'un endroit à un autre, ou un objet lecteur de musique pour écouter vos morceaux préférés.

Alors, pensez aux objets en OOP comme les blocs de construction qui composent un programme, chacun avec sa propre personnalité et son propre but distincts, tout comme les articles sur votre liste d'emballage.

D'accord, comprenez-vous les concepts de base ? Maintenant, écrivons un peu de code.

## Comment créer une classe

Tout d'abord, nous utiliserons l'exemple des Avengers et créerons une classe `Avengers` :

```java
class Main {
    public static void main(String[] args) {

    }
}

class Avengers {

}

```

Maintenant, nous allons créer quelques attributs pour notre propre super-héros :

```java
class Avengers {
    String name;
    int power;
    
}

```

Et nous allons créer une méthode pour notre super-héros afin qu'il puisse arrêter les méchants :

```java
class Avengers {
    String name;
    int power;

    void Punch() {
        System.out.println("Je peux faire ça toute la journée.");
    }
}

```

Ensuite, créons un objet Captain America :

```java
class Main {
    public static void main(String[] args) {
        Avengers hero1 = new Avengers();
        hero1.name = "Captain America";
        System.out.println(hero1.name);
    }
}

```

Voici la syntaxe pour créer un objet :

```java
ClassName ObjectName = new ClassName();
```

Dans le code ci-dessus, j'ai créé un objet de la classe `Avengers` appelé `hero1`.

Comme vous pouvez le voir, en utilisant l'opérateur point (`.`) j'ai assigné une valeur à la variable `name` de l'objet `hero1`.

Appelons la méthode `punch` pour voir si notre Captain America peut vraiment arrêter les méchants :

```java
class Main {
    public static void main(String[] args) {
        Avengers hero1 = new Avengers();
        hero1.name = "Captain America";
        System.out.println(hero1.name);

        // Appel de la méthode sur hero1
        hero1.Punch();
    }
}

```

Enfin, lorsque vous exécutez votre code, vous verrez cette sortie :

```shell
$ java -classpath .:target/dependency/* Main
Captain America
Je peux faire ça toute la journée.

```

Hourra ! Il semble que notre propre Captain America personnel puisse réellement sauver le monde. 😁

## Conclusion

J'espère que vous avez apprécié apprendre comment créer votre propre Avenger avec l'OOP en Java. Créez votre propre super-héros et donnez-lui des pouvoirs incroyables. 😎

Si vous voulez discuter du développement web ou logiciel, vous pouvez me contacter sur [LinkedIn](https://www.linkedin.com/m/in/avdhoot-fulsundar). 😉 Je partage également des conseils géniaux sur le marketing de contenu.