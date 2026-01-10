---
title: Clean Code Expliqué – Une Introduction Pratique au Clean Coding pour Débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-05T21:34:18.000Z'
originalURL: https://freecodecamp.org/news/clean-coding-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/clean-code-image.png
tags:
- name: clean code
  slug: clean-code
- name: Code Quality
  slug: code-quality
seo_title: Clean Code Expliqué – Une Introduction Pratique au Clean Coding pour Débutants
seo_desc: 'By Yiğit Kemal Erinç


  "Any fool can write code that a computer can understand. Good programmers write
  code that humans can understand."                                       – Martin
  Fowler


  Writing clean, understandable, and maintainable code is a s...'
---

Par Yiğit Kemal Erinç

> "N'importe quel idiot peut écrire du code qu'un ordinateur peut comprendre. Les bons programmeurs écrivent du code que les humains peuvent comprendre."                                       – Martin Fowler

Écrire du code propre, compréhensible et maintenable est une compétence cruciale que tout développeur doit maîtriser.

Dans cet article, nous examinerons les principes les plus importants pour améliorer la qualité du code et je vous donnerai des exemples de code pour chacun d'eux.

La plupart des exemples sont tirés du livre _Clean Code_ de Robert J. Martin. C'est un classique de la programmation et je vous suggère de lire le texte complet lorsque vous en aurez le temps.

## Comment Nommer les Variables (et autres éléments)

> "Il n'y a que deux choses difficiles en informatique : l'invalidation du cache et le nommage des choses."                                                                                                                – Phil Karlton

Il y a une raison pour laquelle nous n'utilisons pas les adresses mémoire et avons des noms à la place : les noms sont beaucoup plus faciles à retenir. Et, plus important encore, ils peuvent vous donner plus d'informations sur la variable, afin que quelqu'un d'autre puisse comprendre son importance. 

Cela peut prendre un certain temps pour trouver un bon nom, mais cela vous fera gagner, à vous et à votre équipe, encore plus de temps à l'avenir. Et je suis sûr que la plupart des lecteurs ont déjà été confrontés à la situation où vous revisitez votre code seulement quelques mois plus tard et avez du mal à comprendre ce que vous avez fait auparavant.

### Comment Créer des Noms Significatifs

N'utilisez pas de commentaires pour expliquer pourquoi une variable est utilisée. Si un nom nécessite un commentaire, alors vous devriez prendre le temps de renommer cette variable au lieu d'écrire un commentaire.

> "Un nom doit vous dire pourquoi il existe, ce qu'il fait et comment il est utilisé. Si un nom nécessite un commentaire, alors le nom ne révèle pas son intention."                 – Clean Code

**Mauvais :**

```js
var d; // temps écoulé en jours
```

J'ai vu ce type de code si souvent. C'est une idée fausse courante que vous devriez cacher votre désordre avec des commentaires. N'utilisez pas de lettres comme x, y, a ou b comme noms de variables, sauf s'il y a une bonne raison (les variables de boucle sont une exception à cela).

**Bon :**

```
var elapsedTimeInDays;
var daysSinceCreation;
var daysSinceModification;
```

Ces noms sont bien meilleurs. Ils vous disent ce qui est mesuré et l'unité de cette mesure.

### Éviter la Désinformation

Faites attention aux mots qui ont une signification spécifique. Ne faites pas référence à un regroupement de comptes comme _accountList_ à moins que son type ne soit réellement une Liste. Le mot a une signification spécifique et peut conduire à des conclusions erronées. 

Même si le type est une liste, _accounts_ est un nom plus simple et meilleur.

**Mauvais :**

```js
var accountList = [];
```

**Bon :**

```js
var accounts = []
```

### Éviter les Mots Inutiles

Les mots inutiles sont ceux qui n'apportent aucune information supplémentaire sur la variable. Ils sont redondants et doivent être supprimés. 

Quelques mots inutiles populaires sont :

* The (préfixe) 
* Info
* Data
* Variable
* Object
* Manager

Si votre classe s'appelle UserInfo, vous pouvez simplement supprimer Info et la nommer User. Utiliser BookData au lieu de Book comme nom de classe est une évidence, car une classe stocke des données de toute façon. 

Vous pouvez également lire l'article de blog de Jeff Atwood sur le nommage SomethingManager [ici](https://blog.codinghorror.com/i-shall-call-it-somethingmanager/).

### Utiliser des Noms Prononçables

Si vous ne pouvez pas prononcer un nom, vous ne pouvez pas en discuter sans avoir l'air ridicule.

**Mauvais :**

```js
const yyyymmdstr = moment().format("YYYY/MM/DD");

```

**Bon :**

```js
const currentDate = moment().format("YYYY/MM/DD");
```

### Utiliser des Noms Recherchables

Évitez d'utiliser des nombres magiques dans votre code. Optez pour des constantes nommées et recherchables. N'utilisez pas de noms à une seule lettre pour les constantes, car ils peuvent apparaître à de nombreux endroits et ne sont donc pas facilement recherchables.

### Mauvais:

```java
if (student.classes.length < 7) {
   // Faire quelque chose
}
```

**Bon:**

```java
if (student.classes.length < MAX_CLASSES_PER_STUDENT) {
    // Faire quelque chose
}
```

C'est beaucoup mieux car **MAX_CLASSES_PER_STUDENT** peut être utilisé à de nombreux endroits dans le code. Si nous devons le changer pour 6 à l'avenir, nous pouvons simplement changer la constante. 

Le mauvais exemple crée des points d'interrogation dans l'esprit du lecteur, comme quelle est l'importance de 7 ?

Vous devriez également utiliser les conventions de nommage et de déclaration des constantes de votre langage, comme **private static final** en Java ou **const** en JavaScript.

### Soyez Cohérent

Suivez la règle **un mot pour chaque concept**. N'utilisez pas _fetch_, _retrieve,_ et _get_ pour la même opération dans différentes classes. Choisissez-en un et utilisez-le dans tout le projet afin que les personnes qui maintiennent la base de code ou les clients de votre API puissent facilement trouver les méthodes qu'ils recherchent.

## Comment Écrire des Fonctions

### Gardez-les Petites

Les fonctions doivent être petites, vraiment petites. Elles ne devraient rarement faire 20 lignes de long. Plus une fonction est longue, plus il est probable qu'elle fasse plusieurs choses et ait des effets secondaires.

### Assurez-vous Qu'elles Ne Font Qu'une Chose

> Les fonctions doivent faire une chose. Elles doivent la faire bien. Elles doivent faire seulement cela. – Clean Code

Vos fonctions doivent ne faire qu'une seule chose. Si vous suivez cette règle, il est garanti qu'elles seront petites. La seule chose que la fonction fait doit être indiquée dans son nom.

Parfois, il est difficile de regarder la fonction et de voir si elle fait plusieurs choses ou non. Une bonne façon de vérifier est d'essayer d'extraire une autre fonction avec un nom différent. Si vous pouvez la trouver, cela signifie qu'elle devrait être une fonction différente.

C'est probablement le concept le plus important de cet article, et il faudra un certain temps pour s'y habituer. Mais une fois que vous aurez compris, votre code aura l'air beaucoup plus mature, et il sera plus facilement refactorable, compréhensible et testable.

### Encapsulez les Conditionnelles dans des Fonctions

Refactoriser la condition et la mettre dans une fonction nommée est un bon moyen de rendre vos conditionnelles plus lisibles.

Voici un morceau de code d'un projet scolaire. Ce code est responsable de l'insertion d'un jeton sur le plateau du jeu Connect4. 

La méthode _isValidInsertion_ se charge de vérifier la validité du numéro de colonne et nous permet de nous concentrer sur la logique d'insertion du jeton.

```java
public void insertChipAt(int column) throws Exception {
        if (isValidInsertion(column)) {
            insertChip(column);
            boardConfiguration += column;
            currentPlayer = currentPlayer == Chip.RED ? Chip.YELLOW : Chip.RED;
        } else {
            if (!columnExistsAt(column))
                throw new IllegalArgumentException();
            else if (isColumnFull(column - 1) || getWinner() != Chip.NONE)
                throw new RuntimeException();
        }
    }
```

Voici le code pour isValidInsertion, si vous êtes intéressé.

```java
    private boolean isValidInsertion(int column) {
        boolean columnIsAvailable = column <= NUM_COLUMNS && column >= 1 && numberOfItemsInColumn[column - 1] < NUM_ROWS;
        boolean gameIsOver = getWinner() != Chip.NONE;
        return columnIsAvailable && !gameIsOver;
    }

```

Sans la méthode, la condition if ressemblerait à ceci:

```
if (column <= NUM_COLUMNS
 && column >= 1
 && numberOfItemsInColumn[column - 1] < NUM_ROWS 
 && getWinner() != Chip.NONE)
```

Dégoutant, n'est-ce pas ? Je suis d'accord.

### Moins d'Arguments

Les fonctions doivent avoir deux arguments ou moins, moins c'est mieux. Évitez trois arguments ou plus lorsque c'est possible. 

Les arguments rendent la lecture et la compréhension de la fonction plus difficiles. Ils sont encore plus difficiles du point de vue des tests, car ils créent le besoin d'écrire des cas de test pour chaque combinaison d'arguments.

### Ne pas Utiliser d'Arguments de Drapeau

Un argument de drapeau est un argument booléen qui est passé à une fonction. Deux actions différentes sont entreprises en fonction de la valeur de cet argument.

Par exemple, supposons qu'il y ait une fonction responsable de la réservation de billets pour un concert et qu'il y ait 2 types d'utilisateurs : Premium et Regular. Vous pouvez avoir un code comme ceci :

```java
    public Booking book (Customer aCustomer, boolean isPremium) {
      if(isPremium) 
       // logique pour la réservation premium
      else
       // logique pour la réservation régulière
    }
```

Les arguments de drapeau contredisent naturellement le principe de responsabilité unique. Lorsque vous les voyez, vous devriez envisager de diviser la fonction en deux.

### Ne pas Avoir d'Effets Secondaires

Les effets secondaires sont des conséquences involontaires de votre code. Ils peuvent modifier les paramètres passés, en cas de passage par référence, ou peut-être modifier une variable globale. 

Le point clé est qu'ils ont promis de faire autre chose et vous devez lire le code attentivement pour remarquer l'effet secondaire. Ils peuvent entraîner des bugs désagréables.

Voici un exemple du livre :

```java
public class UserValidator {
      private Cryptographer cryptographer;
      public boolean checkPassword(String userName, String password) { 
        User user = UserGateway.findByName(userName);
        if (user != User.NULL) {
          String codedPhrase = user.getPhraseEncodedByPassword();
          String phrase = cryptographer.decrypt(codedPhrase, password);
          if ("Valid Password".equals(phrase)) {
            Session.initialize();
            return true; 
          }
        }
        return false; 
      }
}
```

Pouvez-vous voir l'effet secondaire de cette fonction ?

Elle vérifie le mot de passe, mais lorsque le mot de passe est valide, elle initialise également la session, ce qui est un effet secondaire. 

Vous pouvez changer le nom de la fonction en quelque chose comme _checkPasswordAndInitializeSession_ pour rendre cet effet explicite. Mais lorsque vous faites cela, vous devriez remarquer que votre fonction fait en réalité deux choses et vous ne devriez pas initialiser la session ici.

### Ne vous Répétez Pas

La répétition de code peut être la racine de tous les maux en logiciel. Le code dupliqué signifie que vous devez changer les choses à plusieurs endroits lorsqu'il y a un changement de logique et c'est très sujet aux erreurs. 

Utilisez les fonctionnalités de refactorisation de votre IDE et extrayez une méthode chaque fois que vous rencontrez un segment de code répété.

![Image](https://erinc.io/wp-content/uploads/2020/10/extract_method-1024x576.jpg)
_IntelliJ Extract Method_

## Bonus

### Ne laissez pas de code en commentaires

S'il vous plaît, ne le faites pas. Celui-ci est sérieux car les autres qui voient le code auront peur de le supprimer parce qu'ils ne savent pas s'il est là pour une raison. Ce code commenté restera là pendant longtemps. Ensuite, lorsque les noms de variables ou de méthodes changent, il devient obsolète mais personne ne le supprime.

Supprimez-le simplement. Même s'il était important, il y a le contrôle de version pour cela. Vous pouvez toujours le trouver.

### Connaissez les Conventions de votre Langage

Vous devez connaître les conventions de votre langage en termes d'espacement, de commentaires et de nommage. Il existe des guides de style disponibles pour de nombreux langages. 

Par exemple, vous devriez utiliser camelCase en Java mais snake_case en Python. Vous mettez les accolades ouvrantes sur une nouvelle ligne en C# mais vous les mettez sur la même ligne en Java et JavaScript. 

Ces choses changent d'un langage à l'autre et il n'y a pas de norme universelle.

Voici quelques liens utiles pour vous :

* [Guide de Style Python](https://www.python.org/dev/peps/pep-0008/)
* [Guide de Style Javascript de Google](https://google.github.io/styleguide/jsguide.html)
* [Guide de Style Java de Google](https://google.github.io/styleguide/javaguide.html)

# Conclusion

Le clean coding n'est pas une compétence qui peut être acquise du jour au lendemain. C'est une habitude qui doit être développée en gardant ces principes à l'esprit et en les appliquant chaque fois que vous écrivez du code.

Merci d'avoir pris le temps de lire et j'espère que cela a été utile.

Si vous êtes intéressé à lire plus d'articles comme celui-ci, vous pouvez vous abonner à mon [blog](http://erinc.io/).