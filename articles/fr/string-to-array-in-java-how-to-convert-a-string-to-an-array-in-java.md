---
title: String to Array in Java - Comment convertir des chaînes en tableaux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-06T19:37:24.000Z'
originalURL: https://freecodecamp.org/news/string-to-array-in-java-how-to-convert-a-string-to-an-array-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/Shittu-Olumide-Python-String-to-Array-in-Java
seo_title: String to Array in Java - Comment convertir des chaînes en tableaux
---

How-to-Convert-a-String-to-an-Array-in-Java.png
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: "Par Shittu Olumide\nSavoir convertir une chaîne en un tableau peut être\n  \ très utile lorsque vous développez des applications de traitement de texte ou que vous travaillez\n  \ avec des données. \nUne chaîne en Java est un groupe de caractères, tandis qu'un tableau est une collection\
  \ d'éléments du même type..."
---

Par Shittu Olumide

Savoir convertir une chaîne en un tableau peut être très utile lorsque vous développez des applications de traitement de texte ou que vous travaillez avec des données. 

Une chaîne en Java est un groupe de caractères, tandis qu'un tableau est une collection d'éléments du même type. Vous pouvez déconstruire une chaîne en ses parties en utilisant le processus de conversion, puis stocker ces parties dans un tableau pour une manipulation ou une analyse ultérieure.

Cet article vous donnera une variété de techniques Java pour convertir des chaînes en tableaux. Alors que nous examinons plusieurs stratégies, nous discuterons de leur syntaxe, applications, avantages et inconvénients. Savoir comment utiliser ces méthodes vous permettra de choisir celle qui convient le mieux à vos besoins de programmation.

## Comment convertir une chaîne en un tableau en utilisant la méthode `toCharArray()`

La méthode `toCharArray()` est une fonction intégrée en Java qui vous permet de convertir une chaîne en un tableau de caractères. Cette méthode est disponible dans la classe String et fournit un moyen pratique de convertir chaque caractère d'une chaîne en un élément d'un tableau.

### Syntaxe et utilisation de la méthode `toCharArray()`

```java
public class StringToArrayExample {
    public static void main(String[] args) {
        String str = "Bonjour, Monde!";
        
        // Convertir la chaîne en un tableau de caractères
        char[] charArray = str.toCharArray();
        
        // Afficher les éléments du tableau
        for (char c : charArray) {
            System.out.println(c);
        }
    }
}
```

**Explication** :

1. Déclarer une variable de chaîne `str` et lui assigner la chaîne souhaitée.
2. Utiliser la méthode `toCharArray()` sur la chaîne `str` pour la convertir en un tableau de caractères. Cette méthode divise la chaîne en caractères individuels et retourne un tableau contenant ces caractères.
3. Stocker le tableau de caractères résultant dans la variable `charArray`.
4. Parcourir le `charArray` en utilisant une boucle `for-each` pour afficher chaque caractère individuellement.

**Sortie** :

```java
B
o
n
j
o
u
r
,
 
M
o
n
d
e
!
```

Avantages de l'utilisation de `toCharArray()` :

* **Simplicité** : La méthode `toCharArray()` fournit un moyen simple de convertir une chaîne en un tableau de caractères avec un seul appel de méthode.
* **Lisibilité** : Le tableau de caractères résultant peut être facilement manipulé, traité ou parcouru en utilisant des boucles.
* **Chaînes immuables** : Puisque les chaînes en Java sont immuables, les convertir en un tableau de caractères peut être utile lorsque vous devez modifier des caractères individuels.

Inconvénients de l'utilisation de `toCharArray()` :

* **Surcoût de mémoire** : La méthode `toCharArray()` crée un nouveau tableau de caractères, ce qui nécessite une mémoire supplémentaire. Cela peut être un problème si vous travaillez avec de grandes chaînes.
* **Performance** : Créer un nouveau tableau de caractères et copier les caractères peut introduire un certain surcoût de performance par rapport à d'autres méthodes, en particulier pour les longues chaînes.

## Comment diviser une chaîne en utilisant la méthode `split()`

La méthode `split()` en Java est un moyen pratique de diviser une chaîne en un tableau de sous-chaînes basé sur un délimiteur spécifié. C'est une méthode largement utilisée pour convertir une chaîne en un tableau en Java.

### Syntaxe et utilisation de la méthode `split()` :

La méthode `split()` est disponible dans la classe String en Java et a la syntaxe suivante :

```java
String[] split(String delimiter)
```

La méthode prend un délimiteur comme argument, qui détermine les points auxquels la chaîne doit être divisée. Le délimiteur peut être une expression régulière ou une simple chaîne.

Exemple de code démontrant la conversion en utilisant `split()` :

```java
string = "Bonjour,Monde,Comment,Allez,Vous?"
delimiter = ","

split_string = string.split(delimiter)
print(split_string)
```

**Explication** :

1. Nous définissons une variable de chaîne appelée `string` qui contient le texte que nous voulons diviser : "Bonjour,Monde,Comment,Allez,Vous?".
2. Nous spécifions le délimiteur que nous voulons utiliser pour diviser la chaîne, qui est une virgule (`,`), et nous l'assignons à la variable `delimiter`.
3. Nous utilisons la méthode `split()` sur la variable `string`, en passant le `delimiter` comme argument. Cela divise la chaîne en sous-chaînes partout où le délimiteur est trouvé.
4. La méthode `split()` retourne une liste des sous-chaînes, que nous assignons à la variable `split_string`.
5. Enfin, nous affichons la liste `split_string` pour voir la sortie.

**Sortie** :

```java
['Bonjour', 'Monde', 'Comment', 'Allez', 'Vous?']
```

Avantages de l'utilisation de `split()` :

* Pratique et facile à utiliser.
* Permet de diviser une chaîne basée sur un délimiteur spécifié.
* Supporte les expressions régulières comme délimiteurs, offrant des options de division flexibles.

Inconvénients de l'utilisation de `split()` :

* Si le délimiteur n'est pas trouvé dans la chaîne, la chaîne originale est retournée comme un seul élément dans le tableau résultant.
* Les expressions régulières peuvent être complexes à gérer, et une utilisation incorrecte peut conduire à des résultats inattendus.
* Diviser une grande chaîne en utilisant une expression régulière complexe peut être coûteux en termes de calcul.

## Comment convertir une chaîne en un tableau en utilisant un StringTokenizer

La classe **StringTokenizer** en Java est une classe héritée qui fournit un moyen pratique de tokeniser ou diviser une chaîne en jetons individuels. Elle est couramment utilisée pour convertir une chaîne en un tableau en la divisant basée sur un délimiteur spécifié.

### Syntaxe et utilisation de `StringTokenizer`

Pour utiliser **StringTokenizer**, vous devez suivre ces étapes :

Tout d'abord, créez une instance de la classe **StringTokenizer**, en passant la chaîne et le délimiteur comme paramètres :

```java
StringTokenizer tokenizer = new StringTokenizer(inputString, delimiter);
```

Exemple de code :

```java
import java.util.StringTokenizer;

public class StringToArrayExample {
    public static void main(String[] args) {
        String inputString = "Bonjour,Monde,Comment,Allez,Vous?";

        // Création d'un objet StringTokenizer avec le délimiteur ","
        StringTokenizer tokenizer = new StringTokenizer(inputString, ",");

        int tokenCount = tokenizer.countTokens();
        String[] stringArray = new String[tokenCount];

        // Conversion de chaque jeton en éléments de tableau
        for (int i = 0; i < tokenCount; i++) {
            stringArray[i] = tokenizer.nextToken();
        }

        // Affichage du tableau de sortie
        for (String element : stringArray) {
            System.out.println(element);
        }
    }
}


**Explication** :

1. Le code commence par créer un objet `StringTokenizer` nommé `tokenizer` avec la chaîne d'entrée et le délimiteur `","`.
2. La méthode `countTokens()` est utilisée pour obtenir le nombre total de jetons présents dans la chaîne d'entrée. Cette valeur est stockée dans la variable `tokenCount`.
3. Un tableau appelé `stringArray` est créé avec une taille égale à `tokenCount`.
4. La méthode `nextToken()` est utilisée dans une boucle pour parcourir chaque jeton et l'assigner à l'index correspondant dans le `stringArray`.
5. Enfin, une boucle `for` est utilisée pour afficher chaque élément dans le `stringArray`.

**Sortie** :

```java
Bonjour
Monde
Comment
Allez
Vous?
```

### Applications de StringTokenizer 

StringTokenizer peut être utile dans divers scénarios, notamment :

* Analyse des données d'entrée qui sont structurées avec un délimiteur cohérent.
* Extraction de mots individuels ou de composants d'une phrase ou d'un paragraphe.
* Division des valeurs séparées par des virgules (CSV) en éléments distincts.
* Tokenisation de texte pour l'analyse lexicale ou les tâches de traitement de langage.

Avantages de l'utilisation de `StringTokenizer` :

* **Simplicité** : La syntaxe de StringTokenizer est simple et facile à comprendre, ce qui la rend accessible aux débutants.
* **Efficacité** : StringTokenizer est efficace en termes de mémoire et de performance par rapport aux expressions régulières ou à la division manuelle basée sur les caractères.
* **Délimiteurs flexibles** : Vous pouvez spécifier plusieurs délimiteurs ou utiliser un ensemble prédéfini de délimiteurs, permettant une tokenisation polyvalente.
* **Traitement itératif** : StringTokenizer vous permet de traiter les jetons de manière itérative, ce qui est pratique pour gérer de grandes chaînes sans tout charger en mémoire à la fois.

Inconvénients de l'utilisation de `StringTokenizer` :

* **Fonctionnalités limitées** : StringTokenizer manque de certaines fonctionnalités avancées trouvées dans les alternatives modernes, telles que les expressions régulières, qui offrent plus de flexibilité dans la tokenisation de motifs complexes.
* **Pas de support pour les expressions régulières** : Contrairement à d'autres méthodes comme la méthode `split()`, StringTokenizer ne peut pas utiliser les expressions régulières comme délimiteurs, limitant ses capacités de tokenisation.
* **Pas de support pour les jetons vides** : StringTokenizer ne gère pas les jetons vides par défaut. Si vous avez des délimiteurs consécutifs, ils sont traités comme un seul délimiteur, ce qui peut entraîner des résultats inattendus.
* **Classe héritée** : StringTokenizer fait partie de l'ancien framework de collections Java et n'implémente pas l'interface Iterable, ce qui signifie qu'il ne peut pas être utilisé dans les boucles for améliorées.

## Comment convertir chaque caractère d'une chaîne en un élément de tableau manuellement

Dans certaines situations, vous pouvez avoir besoin de plus de contrôle sur le processus de conversion ou vouloir le personnaliser selon des exigences spécifiques. 

Dans de tels cas, vous pouvez convertir une chaîne en un tableau en itérant manuellement sur chaque caractère de la chaîne et en les assignant à des éléments individuels dans le tableau.

Exemple de code démontrant la conversion manuelle :

```java
string = "Bonjour, Monde!"
array = []

for char in string:
    array.append(char)

print(array)
```

**Explication** :

1. Nous définissons une variable de chaîne nommée `string` avec la valeur "Bonjour, Monde!".
2. Nous initialisons une liste vide appelée `array`.
3. Nous utilisons une boucle `for` pour itérer sur chaque caractère `char` dans la `string`.
4. À l'intérieur de la boucle, nous utilisons la méthode `append()` pour ajouter chaque caractère `char` à la `array`.
5. Après que la boucle soit terminée, nous affichons la `array` pour voir la sortie.

 Sortie :

```java
['B', 'o', 'n', 'j', 'o', 'u', 'r', ',', ' ', 'M', 'o', 'n', 'd', 'e', '!']
```

Avantages de l'approche de conversion manuelle : 

* Fournit un contrôle total sur le processus de conversion.
* Permet la personnalisation ou la manipulation des caractères avant de les assigner au tableau.
* Fonctionne bien lorsque vous devez effectuer des opérations supplémentaires pendant la conversion.

Inconvénients de l'approche de conversion manuelle :

* Nécessite plus de code et une manipulation manuelle par rapport aux méthodes intégrées comme `toCharArray()` ou `split()`.
* Peut être moins efficace pour les grandes chaînes en raison du processus d'itération manuelle.
* Augmente le risque d'erreurs si elle n'est pas implémentée correctement.

Note : vous devriez choisir l'approche de conversion manuelle lorsque vous avez spécifiquement besoin d'effectuer des opérations personnalisées pendant le processus de conversion. Sinon, les méthodes intégrées comme `toCharArray()` ou `split()` sont recommandées pour leur simplicité et leur efficacité.

## Comparaison des différentes méthodes

1. **`toCharArray()`** :

* Méthode simple et directe.
* Retourne un tableau de caractères représentant la chaîne.
* Adaptée pour les conversions générales sans exigences spécifiques.

2.   **`split()`** :

* Divise la chaîne en un tableau basé sur un délimiteur spécifié.
* Utile lorsque vous voulez séparer la chaîne en sous-chaînes.
* Fournit de la flexibilité dans le choix du motif de délimiteur.

3.   **StringTokenizer** :

* Spécifiquement conçu pour tokeniser les chaînes basées sur des délimiteurs.
* Permet la personnalisation des caractères de délimiteur.
* Adapté lorsque vous avez besoin d'un contrôle fin sur le processus de tokenisation.

4.   **Conversion manuelle** :

* Fournit un contrôle total sur le processus de conversion.
* Permet la personnalisation et des opérations supplémentaires sur les caractères.
* Recommandé lorsque des exigences ou des manipulations spécifiques sont nécessaires pendant la conversion.

## Pourquoi devriez-vous savoir comment convertir une chaîne en un tableau en Java ?

L'importance de convertir une chaîne en un tableau en Java réside dans la polyvalence et la flexibilité qu'elle offre pour manipuler et traiter les données. Voici quelques raisons clés pour lesquelles savoir convertir une chaîne en un tableau est important en Java :

* **Manipulation de données** : Les tableaux fournissent un moyen structuré de stocker et de manipuler des données en Java. En convertissant une chaîne en un tableau, vous pouvez accéder à des caractères ou des sous-chaînes individuels, modifier les données et effectuer diverses opérations telles que le tri, la recherche ou le filtrage.
* **Opérations algorithmiques** : De nombreux algorithmes et structures de données en Java nécessitent des données d'entrée sous forme de tableaux. En convertissant une chaîne en un tableau, vous pouvez facilement appliquer ces algorithmes et effectuer des opérations comme le tri, l'inversion ou l'extraction d'éléments spécifiques.
* **Analyse et traitement de texte** : Les chaînes contiennent souvent des données structurées ou délimitées, telles que CSV (Comma-Separated Values) ou JSON (JavaScript Object Notation). Convertir une chaîne en un tableau vous permet de diviser et d'analyser les données, permettant une analyse, un traitement ou une extraction d'informations spécifiques.
* **Manipulation de chaînes** : Bien que les chaînes aient leur propre ensemble de méthodes de manipulation, les tableaux offrent une flexibilité supplémentaire. Convertir une chaîne en un tableau vous permet de tirer parti des opérations spécifiques aux tableaux comme l'indexation, le découpage ou la jointure pour manipuler les données plus efficacement ou atteindre des exigences de formatage spécifiques.
* **Interopérabilité** : Dans certains scénarios, vous pouvez avoir besoin de convertir une chaîne en un tableau pour interfacer avec des bibliothèques ou des API qui attendent une entrée basée sur des tableaux. En effectuant la conversion, vous pouvez intégrer de manière transparente vos données de chaîne avec des composants externes, assurant la compatibilité et permettant un échange de données transparent.

## Conclusion

Dans cet article, nous avons discuté de diverses méthodes pour convertir une chaîne en un tableau en Java. 

Nous avons commencé par une introduction à l'importance de cette conversion entre les chaînes et les tableaux en Java. 

Ensuite, nous avons exploré quatre approches différentes : l'utilisation de la méthode `toCharArray()`, la division de la chaîne en utilisant la méthode `split()`, l'utilisation d'un `StringTokenizer`, et la conversion manuelle de chaque caractère en un élément de tableau. Nous avons couvert chaque méthode en détail, y compris leur syntaxe, leur utilisation, leur exemple de code, ainsi que leurs avantages et inconvénients.

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !