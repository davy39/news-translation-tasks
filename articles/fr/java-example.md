---
title: Les meilleurs exemples Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-25T00:31:00.000Z'
originalURL: https://freecodecamp.org/news/java-example
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f11740569d1a4ca40a6.jpg
tags:
- name: Java
  slug: java
seo_title: Les meilleurs exemples Java
seo_desc: "What is Java?\nJava is a programming language developed by Sun Microsystems\
  \ in 1995, which later got acquired by Oracle. It’s now a full platform with lots\
  \ of standard APIs, open source APIs, tools, and a huge developer community. \n\
  It is used to build..."
---

## Qu'est-ce que Java ?

[Java](https://www.oracle.com/java/index.html) est un langage de programmation développé par [Sun Microsystems](https://en.wikipedia.org/wiki/Sun_Microsystems) en 1995, qui a ensuite été acquis par [Oracle](http://www.oracle.com/index.html). C'est maintenant une plateforme complète avec de nombreuses API standard, des API open source, des outils et une énorme communauté de développeurs. 

Il est utilisé pour construire les solutions d'entreprise les plus fiables par les grandes et petites entreprises. Le développement d'applications [Android](https://www.android.com/) est entièrement réalisé avec Java et son écosystème. 

Pour en savoir plus sur les bases de Java, lisez [ceci](https://java.com/en/download/faq/whatis_java.xml) et [ceci](http://tutorials.jenkov.com/java/what-is-java.html).

## **Version**

La dernière version est [Java 11](http://www.oracle.com/technetwork/java/javase/overview), qui a été publiée en 2018 avec [diverses améliorations](https://www.oracle.com/technetwork/java/javase/11-relnote-issues-5012449.html) par rapport à la version précédente, Java 10. Mais pour toutes les intentions et tous les objectifs, nous utiliserons Java 8 dans ce wiki pour tous les tutoriels.

Java est également divisé en plusieurs "éditions" :

* [SE](http://www.oracle.com/technetwork/java/javase/overview/index.html) - Standard Edition - pour les applications de bureau et les applications serveur autonomes
* [EE](http://www.oracle.com/technetwork/java/javaee/overview/index.html) - Enterprise Edition - pour le développement et l'exécution de composants Java qui s'exécutent intégrés dans un serveur Java
* [ME](http://www.oracle.com/technetwork/java/embedded/javame/overview/index.html) - Micro Edition - pour le développement et l'exécution d'applications Java sur les téléphones mobiles et les appareils embarqués

## **Installation : JDK ou JRE ?**

Téléchargez les dernières binaires Java depuis le [site officiel](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html). Ici, vous pourriez être confronté à une question, lequel télécharger, JDK ou JRE ? JRE signifie Java Runtime Environment, qui est la machine virtuelle Java dépendante de la plateforme pour exécuter les codes Java, et JDK signifie Java Development Kit, qui comprend la plupart des outils de développement, notamment le compilateur `javac`, et également le JRE. Donc, pour un utilisateur moyen, le JRE serait suffisant, mais puisque nous allons développer avec Java, nous téléchargerons le JDK.

## **Instructions d'installation spécifiques à la plateforme**

### **Windows**

* Téléchargez le fichier [.msi](https://en.wikipedia.org/wiki/Windows_Installer) pertinent (x86 / i586 pour 32 bits, x64 pour 64 bits)
* Exécutez le fichier .msi. C'est un fichier exécutable auto-extractible qui installera Java dans votre système !

### **Linux**

* Téléchargez le fichier [tar.gz](http://www.cyberciti.biz/faq/linux-unix-bsd-extract-targz-file/) pertinent pour votre système et installez :

`bash $ tar zxvf jdk-8uversion-linux-x64.tar.gz`

* Les [plateformes Linux basées sur RPM](https://en.wikipedia.org/wiki/List_of_Linux_distributions#RPM-based) téléchargent le fichier [.rpm](https://en.wikipedia.org/wiki/RPM_Package_Manager) pertinent et installent :

`bash $ rpm -ivh jdk-8uversion-linux-x64.rpm`

* Les utilisateurs ont le choix d'installer une version open source de Java, OpenJDK ou le JDK Oracle. Bien qu'OpenJDK soit en développement actif et synchronisé avec Oracle JDK, ils diffèrent uniquement en termes de [licence](http://openjdk.java.net/faq/). Cependant, quelques développeurs se plaignent de la stabilité d'Open JDK.

### Instructions pour **Ubuntu** :

Installation d'Open JDK :  
`bash sudo apt-get install openjdk-8-jdk`

Installation d'Oracle JDK :  
`bash sudo add-apt-repository ppa:webupd8team/java sudo apt-get update sudo apt-get install oracle-java8-installer`

### **Mac**

* Soit téléchargez l'exécutable Mac OSX .dmg depuis les téléchargements Oracle
* Ou utilisez [Homebrew](http://brew.sh/) pour [installer](http://stackoverflow.com/a/28635465/2861269) :

```bash
brew tap caskroom/cask  
brew install brew-cask  
brew cask install java
```

### **Vérifier l'installation**

Vérifiez que Java a été correctement installé dans votre système en ouvrant l'invite de commande (Windows) / Windows Powershell / Terminal (Mac OS et *Unix) et en vérifiant les versions de l'environnement d'exécution et du compilateur Java :

```text
$ java -version
java version "1.8.0_66"
Java(TM) SE Runtime Environment (build 1.8.0_66-b17)
Java HotSpot(TM) 64-Bit Server VM (build 25.66-b17, mixed mode)

$ javac -version
javac 1.8.0_66
```

**Astuce** : Si vous obtenez une erreur telle que "Commande introuvable" pour `java` ou `javac` ou les deux, ne paniquez pas, il suffit que le PATH de votre système ne soit pas correctement défini. Pour Windows, voir [cette réponse StackOverflow](http://stackoverflow.com/questions/15796855/java-is-not-recognized-as-an-internal-or-external-command) ou [cet article](http://javaandme.com/) sur la façon de le faire. Il existe également des guides pour [Ubuntu](http://stackoverflow.com/questions/9612941/how-to-set-java-environment-path-in-ubuntu) et [Mac](http://www.mkyong.com/java/how-to-set-java_home-environment-variable-on-mac-os-x/). Si vous ne parvenez toujours pas à comprendre, ne vous inquiétez pas, demandez-nous simplement dans notre [salon Gitter](https://gitter.im/FreeCodeCamp/java) !

## **JVM**

Maintenant que nous avons terminé les installations, commençons à comprendre les détails de l'écosystème Java. Java est un langage [interprété et compilé](http://stackoverflow.com/questions/1326071/is-java-a-compiled-or-an-interpreted-programming-language), c'est-à-dire que le code que nous écrivons est compilé en bytecode et interprété pour s'exécuter. Nous écrivons le code dans des fichiers .java, Java les compile en [bytecodes](https://en.wikipedia.org/wiki/Java_bytecode) qui sont exécutés sur une machine virtuelle Java ou JVM. Ces bytecodes ont généralement une extension .class.

Java est un langage assez sécurisé car il ne permet pas à votre programme de s'exécuter directement sur la machine. Au lieu de cela, votre programme s'exécute sur une machine virtuelle appelée JVM. Cette machine virtuelle expose plusieurs API pour les interactions de bas niveau avec la machine que vous pouvez effectuer, mais autre que cela, vous ne pouvez pas jouer avec les instructions machine explicitement. Cela ajoute un énorme bonus de sécurité.

De plus, une fois que votre bytecode est compilé, il peut s'exécuter sur n'importe quelle machine virtuelle Java. Cette machine virtuelle est dépendante de la machine, c'est-à-dire qu'elle a différentes implémentations pour Windows, Linux et Mac. Mais votre programme est garanti de s'exécuter sur n'importe quel système grâce à cette VM. Cette philosophie est appelée ["Write Once, Run Anywhere"](https://en.wikipedia.org/wiki/Write_once,_run_anywhere).

## **Hello World !**

Écrivons une application Hello World de exemple. Ouvrez n'importe quel éditeur / IDE de votre choix et créez un fichier `HelloWorld.java`.

```text
public class HelloWorld {

    public static void main(String[] args) {
        // Affiche "Hello, World" dans la fenêtre du terminal.
        System.out.println("Hello, World");
    }

}
```

**N.B.** Gardez à l'esprit que dans Java, le nom du fichier doit être le **nom exact de la classe publique** afin de compiler !

Ouvrez maintenant le terminal / l'invite de commande. Changez votre répertoire actuel dans le terminal / l'invite de commande vers le répertoire où se trouve votre fichier. Et compilez le fichier :

```text
$ javac HelloWorld.java
```

Maintenant, exécutez le fichier en utilisant la commande `java` !

```text
$ java HelloWorld
Hello, World
```

Félicitations ! Votre premier programme Java a été exécuté avec succès. Ici, nous imprimons simplement une chaîne en la passant à l'API `System.out.println`. Nous couvrirons tous les concepts du code, mais vous êtes les bienvenus pour [regarder de plus près](https://docs.oracle.com/javase/tutorial/getStarted/application/) ! Si vous avez un doute ou avez besoin d'aide supplémentaire, n'hésitez pas à nous contacter à tout moment dans notre [salon de discussion Gitter](https://gitter.im/FreeCodeCamp/java) !

## **Documentation**

Java est largement [documenté](https://docs.oracle.com/javase/8/docs/), car il prend en charge une énorme quantité d'API. Si vous utilisez un IDE majeur tel qu'Eclipse ou IntelliJ IDEA, vous trouverez la documentation Java incluse.

De plus, voici une liste d'IDE gratuits pour le codage Java :

* [NetBeans](https://netbeans.org/)
* [Eclipse](https://eclipse.org/)
* [IntelliJ IDEA](https://www.jetbrains.com/idea/features/)
* [Android Studio](https://developer.android.com/studio/index.html)
* [BlueJ](https://www.bluej.org/)
* [jEdit](http://www.jedit.org/)
* [Oracle JDeveloper](http://www.oracle.com/technetwork/developer-tools/jdev/overview/index-094652.html)

## Opérations de base

Java prend en charge les opérations suivantes sur les variables :

* **Arithmétique** : `Addition (+)`, `Soustraction (-)`, `Multiplication (*)`, `Division (/)`, `Modulo (%)`, `Incrément (++)`, `Décrément (--)`.
* **Concatenation de chaînes** : `+` peut être utilisé pour la concaténation de chaînes, mais la soustraction `-` sur une chaîne n'est pas une opération valide.
* **Relationnel** : `Égal à (==)`, `Différent de (!=)`, `Supérieur à (>)`, `Inférieur à (<)`, `Supérieur ou égal à (>=)`, `Inférieur ou égal à (<=)`
* **Bitwise** : `ET bitwise (&)`, `OU bitwise (|)`, `XOR bitwise (^)`, `Complément bitwise (~)`, `Déplacement à gauche (<<)`, `Déplacement à droite (>>)`, `Déplacement à droite avec remplissage de zéro (>>>`)
* **Logique** : `ET logique (&&)`, `OU logique (||)`, `NON logique (!)`
* **Affectation** : `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`, `&=`, `^=`, `|=`
* **Autres** : `Conditionnel/Ternaire(?:)`, `instanceof`

Alors que la plupart des opérations sont explicites, l'opérateur conditionnel (ternaire) fonctionne comme suit :

`expression qui résulte en une sortie booléenne ? retourne cette valeur si vrai : retourne cette valeur si faux ;`

Exemple : Condition vraie :

```java
    int x = 10;
    int y = (x == 10) ? 5 : 9; // y sera égal à 5 puisque l'expression x == 10 est évaluée à vrai
    
```

Condition fausse :

```java
    int x = 25;
    int y = (x == 10) ? 5 : 9; // y sera égal à 9 puisque l'expression x == 10 est évaluée à faux
```

L'opérateur instanceof est utilisé pour vérifier le type. Il peut être utilisé pour tester si un objet est une instance d'une classe, d'une sous-classe ou d'une interface. Format général - *objet **instance** de classe/sous-classe/interface*

Voici un programme pour illustrer l'opérateur instanceof :

```java
  Person obj1 = new Person();
        Person obj2 = new Boy();
 
        // Comme obj est de type person, ce n'est pas une
        // instance de Boy ou interface
        System.out.println("obj1 instanceof Person: " +  (obj1 instanceof Person)); /*il retourne vrai puisque obj1 est une instance de person */
                           
       
```

# Exemples de variables

Les variables stockent des valeurs. Elles sont l'entité la plus basique utilisée pour stocker des données telles que du texte, des nombres, etc. dans un programme.

En Java, les variables sont fortement typées, ce qui signifie que vous devez définir le type pour chaque variable chaque fois que vous la déclarez. Sinon, le compilateur générera une erreur au moment de la compilation. Par conséquent, chaque variable a un "type de données" associé parmi les suivants :

Type primitif : int, short, char, long, boolean, byte, float, double

Type wrapper : Integer, Short, Character, Long, Boolean, Byte, Float, Double

Type référence : String, StringBuilder, Calendar, ArrayList, etc.

Vous avez peut-être remarqué que le type wrapper est composé de types orthographiés exactement comme le type primitif, à l'exception de la lettre majuscule au début (comme le type référence). Cela est dû au fait que les types wrapper font en réalité partie des types référence plus généraux, mais sont étroitement liés à leurs homologues primitifs via l'autoboxing et l'unboxing. Pour l'instant, vous devez simplement savoir qu'un tel "type wrapper" existe.

Généralement, vous pouvez déclarer (c'est-à-dire créer) des variables selon la syntaxe suivante : <data-type> <variableName>;

```java
// Type de données primitif
int i;

// Type de données référence
Float myFloat;
```

Vous pouvez assigner une valeur à la variable soit simultanément lorsque vous la déclarez (ce qui s'appelle l'initialisation), soit n'importe où dans le code après l'avoir déclarée. Le symbole = est utilisé pour cela.

```java
// Initialise la variable de type de données primitif 'int' pour stocker la valeur 10
int i = 10;
double amount = 10.0;
boolean isOpen = false;
char c = 'a'; // Notez les guillemets simples

// Les variables peuvent également être déclarées dans une instruction, et des valeurs leur être assignées plus tard.
int j;
j = 10;

// initialise un objet Float avec la valeur 1.0
// la variable myFloat pointe maintenant vers l'objet
Float myFloat = new Float(1.0);

// Les bytes sont l'un des types en Java et peuvent être
// représentés avec ce code
int byteValue = 0B101;
byte anotherByte = (byte)0b00100001;
```

Comme le montre l'exemple ci-dessus, les variables de type primitif se comportent légèrement différemment des variables de type référence (et wrapper) - tandis que les variables primitives stockent la valeur réelle, les variables de référence font référence à un "objet" contenant la valeur réelle. Vous pouvez en savoir plus dans les sections liées ci-dessous.

# **Tableau**

Un tableau est une collection de valeurs (ou d'objets) de types de données similaires (les formes de types de données primitives et de référence sont autorisées) stockées dans des adresses mémoire séquentielles. Un tableau est utilisé pour stocker une collection de types de données similaires. Les tableaux commencent toujours avec l'index 0 et sont instanciés avec un nombre fixe d'index. Toutes les variables du tableau doivent être du même type, déclaré lors de l'instanciation.

**Syntaxe :**

```java
dataType[] arrayName;   // manière préférée
```

Ici, `java datatype[]` décrit que toutes les variables déclarées après lui seront instanciées comme des tableaux du type de données spécifié. Donc, si nous voulons instancier plus de tableaux du même type de données, nous devons simplement les ajouter après le `java arrayName` spécifié (n'oubliez pas de les séparer par des virgules uniquement). Un exemple est donné ci-dessous dans la section suivante pour référence.

```java
dataType arrayName[];  // fonctionne mais n'est pas la manière préférée
```

Ici, `java datatype` décrit uniquement que les variables déclarées après lui appartiennent à ce type de données. De plus, `java []` après le nom de la variable décrit que la variable est un tableau du type de données spécifié (pas seulement une valeur ou un objet de ce type de données). Donc, si nous voulons instancier plus de tableaux du même type de données, nous ajouterons les noms des variables juste après celui déjà spécifié, séparés par des virgules et chaque fois nous devrons ajouter `java []` après le nom de la variable, sinon la variable sera instanciée comme une variable de stockage de valeur ordinaire (pas un tableau). Pour une meilleure compréhension, un exemple est donné dans la section suivante.

## **Extraits de code de la syntaxe ci-dessus :**

```java
double[] list1, list2; // manière préférée
```

L'extrait de code ci-dessus instancie 2 tableaux de type double nommés list1 et list2.

```java
double list1[], list2; // fonctionne mais n'est pas la manière préférée
```

L'extrait de code ci-dessus instancie un tableau de type double nommé list1 et une simple variable de type double nommée list2 (ne soyez pas confus avec le nom **list2**. Les noms de variables n'ont rien à voir avec le type de variable).

Note : Le style `double list[]` n'est pas préféré car il provient du langage C/C++ et a été adopté en Java pour accommoder les programmeurs C/C++. De plus, il est plus lisible : vous pouvez lire qu'il s'agit d'un "tableau double nommé list" plutôt que d'un "double appelé list qui est un tableau"

## **Création de tableaux :**

```java
dataType[] arrayName = new dataType[arraySize];
```

## **Extraits de code de la syntaxe ci-dessus :**

```java
double[] List = new double[10];
```

## **Autre façon de créer un tableau :**

```java
dataType[] arrayName = {value_0, value_1, ..., value_k};
```

## **Extraits de code de la syntaxe ci-dessus :**

```java
double[] list = {1, 2, 3, 4};

Le code ci-dessus est équivalent à :
double[] list = new double[4];
*NOTE IMPORTANTE : Veuillez noter la différence entre les types de crochets
qui sont utilisés pour représenter les tableaux de deux manières différentes.
```

## **Accès aux tableaux :**

```java
arrayName[index]; // vous donne la valeur à l'index spécifié
```

## **Extraits de code de la syntaxe ci-dessus :**

```java
System.out.println(list[1]);
```

Sortie :

```text
2.0
```

## **Modification des tableaux :**

```java
arrayName[index] = value; 
```

Note : Vous ne pouvez pas changer la taille ou le type d'un tableau après l'avoir initialisé. Note : Vous pouvez cependant réinitialiser le tableau comme suit

```java
arrayName = new dataType[] {value1, value2, value3};
```

## **Taille des tableaux :**

Il est possible de trouver le nombre d'éléments dans un tableau en utilisant l'attribut "length". Il faut noter ici que `java length` est un **attribut** de chaque tableau, c'est-à-dire une variable nommée stockant la longueur de la variable. Il ne doit pas être confondu avec une **méthode** de tableau puisque le nom est le même que la méthode `java length()` correspondant aux classes String.

```java
int[] a = {4, 5, 6, 7, 8}; // déclare le tableau
System.out.println(a.length); // imprime 5
```

## **Extraits de code de la syntaxe ci-dessus :**

```java
list[1] = 3; // maintenant, si vous accédez au tableau comme ci-dessus, il affichera 3 plutôt que 2
```

_Exemple de code :_

```java
int[] a = {4, 5, 6, 7, 8}; // déclare le tableau
for (int i = 0; i < a.length; i++){ // la boucle passe par chaque index
    System.out.println(a[i]); // imprime le tableau
}
```

Sortie :

```java
    4
    5
    6
    7
    8
```

### **Tableaux multidimensionnels**

Les tableaux à deux dimensions (2D) peuvent être considérés comme un tableau avec des lignes et des colonnes. Bien que cette représentation ne soit qu'un moyen de visualiser le tableau pour une meilleure résolution de problèmes. Les valeurs sont en réalité stockées dans des adresses mémoire séquentielles uniquement.

```java
int M = 5;
int N = 5;
double[][] a = new double [M][N]; //M = lignes N = colonnes
for(int i = 0; i < M; i++) {
    for (int j = 0; j < N; j++) {
        //Faire quelque chose ici à l'index 
    }
}
```

Cette boucle s'exécutera M ^ N fois et construira ceci :

[0 | 1 | 2 | 3 | 4](https://guide.freecodecamp.org/java/arrays)   
[0 | 1 | 2 | 3 | 4](https://guide.freecodecamp.org/java/arrays)   
[ 0 | 1 | 2 | 3 | 4 ]

De même, un tableau 3D peut également être créé. Il peut être visualisé comme un cuboïde au lieu d'un rectangle (comme ci-dessus), divisé en petits cubes, chaque cube stockant une valeur. Il peut être initialisé comme suit :

```java
int a=2, b=3, c=4;
int[][][] a=new int[a][b][c];
```

De manière similaire, on peut créer un tableau de autant de dimensions que l'on souhaite, mais visualiser un tableau de plus de 3 dimensions est difficile à visualiser de manière particulière.

### **Tableaux irréguliers**

Les tableaux irréguliers sont des tableaux multidimensionnels qui ont un nombre fixe de lignes mais un nombre variable de colonnes. Les tableaux irréguliers sont utilisés pour économiser l'utilisation de la mémoire du tableau. Voici un exemple de code :

```java
int[][] array = new int[5][]; //initialise un tableau 2D avec 5 lignes
array[0] = new int[1]; //crée 1 colonne pour la première ligne
array[1] = new int[2]; //crée 2 colonnes pour la deuxième ligne
array[2] = new int[5]; //crée 5 colonnes pour la troisième ligne
array[3] = new int[5]; //crée 5 colonnes pour la quatrième ligne
array[4] = new int[5]; //crée 5 colonnes pour la cinquième ligne
```

Sortie :

[0](https://guide.freecodecamp.org/java/arrays)   
[0 | 1 | 2 | 3 | 4](https://guide.freecodecamp.org/java/arrays)   
[ 0 | 1 | 2 | 3 | 4 ]

# **Contrôle de flux**

Les instructions de contrôle de flux sont exactement ce que le terme signifie. Ce sont des instructions qui modifient le flux d'exécution en fonction des décisions, des boucles et des branchements afin que le programme puisse exécuter conditionnellement des blocs de code.

Principalement, Java a les constructions suivantes pour le contrôle de flux :

* `if`
* `if...else`

```java
if( <expression qui résulte en un booléen> ){
    // le code entre dans ce bloc si l'expression ci-dessus est 'vraie'
}
```

```java
if( <expression qui résulte en un booléen> ){
    // exécute ce bloc si l'expression est 'vraie'
} else{
    // exécute ce bloc si l'expression est 'fausse'
}
```

`switch`

Switch est une alternative à la construction `if...else` lorsqu'il y a plusieurs valeurs et cas à vérifier.

```java
switch( <entier / String / Enum > ){
    case <int/String/Enum>: 
        <instructions>
        break;
    case <int/String/Enum>:
        <instructions>
        break;
    default:
        <instructions>
}
```

Note : Le flux du programme "tombe" dans le `case` suivant si l'instruction `break` est manquante. Par exemple, disons que vous dites le standard "Bonjour" à tout le monde au bureau, mais que vous êtes extra gentil avec la fille qui est assise à côté de vous et que vous semblez grincheux avec votre patron. La façon de représenter cela serait quelque chose comme :

```java
switch(person){
    case 'boss': 
        soundGrumpy();
        break;
    case 'neighbour': 
        soundExtraNice();
        break;
    case 'colleague':
        soundNormal();
        break;
    default:
        soundNormal();
}
```

```text
Note : Le cas `default` s'exécute lorsqu'aucun des `case` ne correspond. Rappelez-vous que lorsqu'un cas n'a pas d'instruction `break`, il "tombe" dans le cas suivant et continuera aux `cases` suivants jusqu'à ce qu'un `break` soit rencontré. À cause de cela, assurez-vous que chaque cas a une instruction `break`. Le cas `default` ne nécessite pas d'instruction `break`. 
```

* `instructions imbriquées`

N'importe lequel des flux de contrôle précédents peut être imbriqué. Ce qui signifie que vous pouvez avoir des instructions `if`, `if..else` et `switch..case` imbriquées. C'est-à-dire que vous pouvez avoir n'importe quelle combinaison de ces instructions à l'intérieur des autres et il n'y a pas de limitation à la profondeur de l'imbrication.

Par exemple, considérons le scénario suivant :

* Si vous avez moins de 25 dollars, vous vous offrez une tasse de café.
* Si vous avez plus de 25 dollars mais moins de 60 dollars, vous vous offrez un repas décent.
* Si vous avez plus de 60 dollars mais moins de 100 dollars, vous vous offrez un repas décent avec un verre de vin.
* Cependant, lorsque vous avez plus de 100 dollars, selon avec qui vous êtes, vous allez soit pour un dîner aux chandelles (avec votre femme) soit vous allez dans un bar sportif (avec vos amis).

L'une des façons de représenter cela sera :

```java
int cash = 150;
String company = "friends";

if( cash < 25 ){
    getCoffee();
} else if( cash < 60 ){
    getDecentMeal();
} else if( cash < 100 ){
    getDecentMeal();
    getGlassOfWine();
} else {
    switch(company){
        case "wife":
            candleLitDinner();
            break;
        case "friends": 
            meetFriendsAtSportsBar();
            break;
        default:
            getDecentMeal();
    }
}
```

Dans cet exemple, `meetFriendsAtSportsBar()` sera exécuté.



# **Boucles**

Chaque fois que vous devez exécuter un bloc de code plusieurs fois, une boucle sera souvent utile.

Java a 4 types de boucles :

# **Boucle While**

La boucle `while` exécute répétitivement le bloc d'instructions jusqu'à ce que la condition spécifiée dans les parenthèses soit évaluée à `false`. Par exemple :

```java
while (some_condition_is_true)
{
    // faire quelque chose
}
```

  
Chaque "itération" (exécution du bloc d'instructions) est précédée par l'évaluation de la condition spécifiée dans les parenthèses - Les instructions sont exécutées uniquement si la condition est évaluée à `true`. Si elle est évaluée à `false`, l'exécution du programme reprend à partir de l'instruction juste après le bloc `while`.

**Note** : Pour que la boucle `while` commence à s'exécuter, vous aurez besoin que la condition soit `true` initialement. Cependant, pour sortir de la boucle, vous devez faire quelque chose dans le bloc d'instructions pour atteindre éventuellement une itération où la condition est évaluée à `false` (comme fait ci-dessous). Sinon, la boucle s'exécutera pour toujours. (En pratique, elle s'exécutera jusqu'à ce que la [JVM](https://guide.freecodecamp.org/java/the-java-virtual-machine-jvm) manque de mémoire.)

## **Exemple**

Dans l'exemple suivant, l'`expression` est donnée par `iter_While < 10`. Nous incrémentons `iter_While` de `1` chaque fois que la boucle est exécutée. La boucle `while` se termine lorsque la valeur de `iter_While` atteint `10`.

```java
int iter_While = 0;
while (iter_While < 10)
{
    System.out.print(iter_While + " ");
    // Incrémente le compteur
    // Itéré 10 fois, iter_While 0,1,2...9
    iter_While++;
}
System.out.println("iter_While Value: " + iter_While);
```

Sortie :

```
1 2 3 4 5 6 7 8 9
iter_While Value: 10
```