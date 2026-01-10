---
title: Comment commencer avec Maven
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-05T23:51:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-maven-36851d8cfd96
coverImage: https://cdn-media-1.freecodecamp.org/images/0*e-MWm5xnFFpeo9it
tags:
- name: beginner
  slug: beginner
- name: coding
  slug: coding
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment commencer avec Maven
seo_desc: 'By Aditya Sridhar

  Maven is used very often in the industry and I felt it would be good to cover the
  basics in this article so that it can be used efficiently.

  This article will cover things like maven basics, maven plugins, maven dependencies,
  and ma...'
---

Par Aditya Sridhar

Maven est très souvent utilisé dans l'industrie et j'ai pensé qu'il serait bon de couvrir les bases dans cet article afin qu'il puisse être utilisé efficacement.

Cet article couvrira des sujets tels que les bases de Maven, les plugins Maven, les dépendances Maven et le cycle de vie de construction Maven.

### Qu'est-ce que Maven

Maven a été créé pour fournir une manière standard de construire des projets. L'une de ses fonctionnalités puissantes est la gestion des dépendances.

**Maven est couramment utilisé pour la gestion des dépendances, mais ce n'est pas la seule chose qu'il peut faire.**

Si vous ne savez pas ce que signifie la gestion des dépendances, ne vous inquiétez pas 💡. Je vais également couvrir cela dans cet article.

### Installation de Maven

Vous pouvez installer Maven depuis [https://maven.apache.org/](https://maven.apache.org/)

Assurez-vous également que Maven est défini dans le PATH afin que les commandes `mvn` fonctionnent.

Vous pouvez vérifier s'il est installé et accessible en utilisant la commande

```bash
mvn -v
```

Assurez-vous également que [JAVA_HOME](https://docs.oracle.com/cd/E19182-01/820-7851/inst_cli_jdk_javahome_t/) est défini.

Par défaut, Maven utilisera le JDK que vous avez fourni dans JAVA_HOME. Cela peut être remplacé, mais pour cet article, nous utiliserons le JDK fourni dans JAVA_HOME.

### Créer votre projet Maven

Normalement, un IDE comme Eclipse peut être utilisé pour créer facilement des projets Maven. Mais dans cet article, je vais exécuter les commandes depuis la ligne de commande afin que les étapes soient clairement comprises.

Exécutez la commande suivante pour créer le projet.

```bash
mvn -B archetype:generate -DarchetypeGroupId=org.apache.maven.archetypes -DgroupId=com.first.app -DartifactId=first-maven-app

```

Archetype dans la commande ci-dessus n'est rien d'autre qu'un modèle de projet échantillon. **groupId** indique à quel groupe votre projet appartient et **artifactId** est le nom du projet.

Une fois que vous avez exécuté la commande ci-dessus, il peut falloir une minute ou deux à Maven pour télécharger les plugins nécessaires et créer le projet.

Un dossier appelé first-maven-app est maintenant créé. Ouvrez le dossier et vous verrez un fichier appelé **pom.xml**

### pom.xml

POM signifie Project Object Model. pom.xml contient tous les détails de votre projet, et c'est ici que vous direz à Maven ce qu'il doit faire.

Le contenu de ce fichier est montré ci-dessous :

```xml
 <project xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.first.app</groupId>
  <artifactId>first-maven-app</artifactId>
  <packaging>jar</packaging>
  <version>1.0-SNAPSHOT</version>
  <name>first-maven-app</name>
  <url>http://maven.apache.org</url>
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>3.8.1</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
</project>
```

**groupId** et **artifactId** sont les mêmes valeurs que nous avons données dans la ligne de commande.

**packaging** est le format de package de l'artefact. La valeur par défaut est **jar**. Il peut avoir d'autres valeurs comme ear, war, tar, etc.

**version** indique le numéro de version de l'artefact. Si **SNAPSHOT** est présent, cela indique que la version est encore en développement et peut ne pas être stable. Si le numéro de version ne contient pas **SNAPSHOT**, alors c'est la version de publication réelle.

**name** est le nom du projet.

Je vais expliquer les dépendances et les plugins dans Maven ci-dessous.

### Super POM

Comme vous pouvez le voir, pom.xml est assez petit. La raison en est qu'une grande partie de la configuration est présente dans quelque chose appelé Super POM, qui est maintenu en interne par Maven.

pom.xml étend Super Pom pour obtenir toute la configuration présente dans Super Pom.

L'une des configurations présentes dans Super Pom indique ce qui suit :

* Tout le code source Java est présent dans **src/main/java**
* Tout le code de test Java est présent dans **src/test/java**

Je mentionne seulement cette configuration ici, puisque nous allons traiter à la fois le code source et le code de test dans cet article.

### Code

L'ensemble du code discuté ici est disponible dans ce dépôt : [https://github.com/aditya-sridhar/first-maven-app](https://github.com/aditya-sridhar/first-maven-app)

Ajoutons un peu de code Java simple. Créez la structure de dossiers suivante :

**src/main/java/com/test/app/App.java**

**App.java** est le code Java que nous allons ajouter.

Copiez le code suivant dans App.java :

```java
package com.first.app;

import java.util.List;
import java.util.ArrayList;

public class App 
{
    public static void main( String[] args )
    {
        List<Integer> items = new ArrayList<Integer>();
        items.add(1);
        items.add(2);
        items.add(3);
        printVals(items);
        System.out.println("Sum: "+getSum(items));
    }

    public static void printVals(List<Integer> items){
        items.forEach( item ->{
            System.out.println(item);
        });
    }

    public static int getSum(List<Integer> items){
        int sum = 0;
        for(int item:items){
            sum += item;
        }
        return sum;
    }
}

```

C'est un code simple qui a 2 fonctions.

Mais une chose à observer est que le code utilise des expressions lambda à l'intérieur de la boucle forEach dans la fonction **printVals**.

Les expressions lambda nécessitent au minimum Java 8 pour fonctionner. Mais par défaut, Maven 3.8.0 fonctionne avec la version Java 1.6.

Nous devons donc dire à Maven d'utiliser Java 1.8 à la place. Pour ce faire, nous allons utiliser les plugins Maven.

### Plugins Maven

Nous allons utiliser le plugin Maven Compiler pour indiquer quelle version de Java utiliser. Ajoutez les lignes suivantes à pom.xml :

```xml
<project>
...
<build>
  <plugins>
     <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.8.0</version>
        <configuration>
          <source>1.8</source>
          <target>1.8</target>
        </configuration>
      </plugin>
  <plugins>
</build>
...
</project>
```

Vous pouvez voir que les versions Java **source** et **target** sont définies sur **1.8**.

**Les plugins exécutent essentiellement certaines actions dans Maven. Le plugin compiler compile les fichiers sources.**

Le fichier pom.xml complet est disponible [ici](https://github.com/aditya-sridhar/first-maven-app/blob/master/pom.xml).

**Il existe de nombreux plugins Maven disponibles. En sachant comment utiliser les plugins, Maven peut être utilisé pour faire des choses incroyables.** ✨

### Dépendances Maven

Normalement, lors de l'écriture de code, nous utiliserons beaucoup de bibliothèques existantes. Ces bibliothèques existantes ne sont rien d'autre que des dépendances. Maven peut être utilisé pour gérer facilement les dépendances.

Dans le pom.xml de notre projet, vous pouvez voir la dépendance suivante :

```xml
 <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>3.8.1</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
```

Cette dépendance indique que nous aurons besoin de **junit**. Junit est utilisé pour écrire des tests unitaires pour le code Java. De même, de nombreuses autres dépendances peuvent être ajoutées.

Supposons que vous souhaitiez gérer le JSON dans le code. Vous pouvez alors ajouter la dépendance **gson** comme suit :

```xml
<dependency>
    <groupId>com.google.code.gson</groupId>
    <artifactId>gson</artifactId>
    <version>2.8.5</version>
</dependency>
```

Vous pouvez rechercher des artefacts Maven sur [https://search.maven.org](https://search.maven.org/)

### Dépendances transitives

Supposons que vous ajoutiez une dépendance **A** au projet. Maintenant, **A** dépend d'une dépendance appelée **B**. **B** dépend d'une dépendance appelée **C**.

Puisque vous utilisez **A** dans le projet, vous aurez également besoin de **B** et **C**.

Mais heureusement, il suffit d'ajouter uniquement **A** dans pom.xml. Parce que Maven peut déterminer que A dépend de B et que B dépend de C. Ainsi, Maven téléchargera automatiquement **B** et **C** en interne.

Ici, **B** et **C** sont des dépendances transitives.

### Dépôt Maven personnalisé

Toutes ces dépendances sont disponibles dans un dépôt central public Maven [http://repo.maven.apache.org/maven2](http://repo.maven.apache.org/maven2)

Il est possible que certains artefacts soient privés pour votre entreprise. Dans ce cas, vous pouvez maintenir un dépôt Maven privé au sein de votre organisation. Je ne couvrirai pas cette partie dans ce tutoriel.

### Ajout de la classe de test

Puisque la dépendance junit est présente dans le projet, nous pouvons ajouter des classes de test.

Créez la structure de dossiers suivante :

**src/test/java/com/test/app/AppTest.java**

**AppTest.java** est la classe de test.

Copiez le code suivant dans AppTest.java :

```java
package com.first.app;
import junit.framework.TestCase;
import java.util.List;
import java.util.ArrayList;

public class AppTest extends TestCase
{
    public AppTest( String testName )
    {
        super( testName );
    }

    public void testGetSum()
    {
        List<Integer> items = new ArrayList<Integer>();
        items.add(1);
        items.add(2);
        items.add(3);
        assertEquals( 6, App.getSum(items) );
    }
}
```

Cette classe teste la fonction getSum() présente dans la classe App.

### Cycle de vie de construction Maven et phases

Maven suit un cycle de vie de construction pour construire et distribuer des artefacts. Il existe trois cycles de vie principaux :

1. **Cycle de vie par défaut** : Cela traite de la construction et du déploiement de l'artefact.
2. **Cycle de vie de nettoyage** : Cela traite du nettoyage du projet
3. **Cycle de vie du site** : Cela traite de la documentation du site. **Je couvrirai cela dans un article différent.**

Un cycle de vie est composé de phases. Voici quelques-unes des phases importantes du **cycle de vie par défaut** :

* **validate** : Vérifie si toutes les informations nécessaires sont disponibles pour le projet
* **compile** : Utilisé pour compiler les fichiers sources. Exécutez la commande suivante pour compiler :

```bash
mvn compile
```

* Après avoir exécuté cette commande, un dossier appelé target est créé avec tous les fichiers compilés.
* **test** : Utilisé pour exécuter tous les tests unitaires présents dans le projet. C'est pourquoi la dépendance Junit était nécessaire. En utilisant Junit, des tests unitaires peuvent être écrits. Les classes de test peuvent être exécutées en utilisant la commande

```bash
mvn test
```

* **package** : Cela exécutera toutes les phases ci-dessus puis emballera l'artefact. Ici, il l'emballera dans un fichier **jar** puisque pom indique qu'un jar est nécessaire. Exécutez la commande suivante pour cela :

```bash
mvn package
```

* Le fichier **jar** est créé dans le dossier **target**
* **verify** : Cela garantira que les critères de qualité sont respectés dans le projet
* **install** : Cela installera le package dans un dépôt local. L'emplacement du dépôt local est généralement **${user.home}/.m2/repository**. Utilisez la commande suivante pour cela :

```bash
mvn install
```

* **deploy** : Cela est utilisé pour déployer le package dans un dépôt distant

Une autre commande couramment utilisée est la commande clean qui est donnée ci-dessous :

```bash
mvn clean
```

Cette commande nettoie tout ce qui se trouve dans le dossier **target**

### Références

Guide officiel de Maven : [https://maven.apache.org/guides/getting-started/](https://maven.apache.org/guides/getting-started/)

Plus sur POM : [https://maven.apache.org/guides/introduction/introduction-to-the-pom.html](https://maven.apache.org/guides/introduction/introduction-to-the-pom.html)

Plus sur le cycle de vie de construction : [https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html)

### Félicitations 🎉

Vous savez maintenant comment utiliser Maven. Cet article a couvert les bases de pom, des plugins, des dépendances et du cycle de vie de construction. Pour en savoir plus sur Maven, consultez les liens que j'ai donnés ci-dessus.

Bon codage 🚀

### À propos de l'auteur

J'aime la technologie et je suis les avancées dans ce domaine. J'aime aussi aider les autres avec mes connaissances technologiques.

N'hésitez pas à me contacter sur mon compte LinkedIn [https://www.linkedin.com/in/aditya1811/](https://www.linkedin.com/in/aditya1811/)

Vous pouvez également me suivre sur Twitter [https://twitter.com/adityasridhar18](https://twitter.com/adityasridhar18)

Mon site web : [https://adityasridhar.com/](https://adityasridhar.com/)

_Publié à l'origine sur [adityasridhar.com](https://adityasridhar.com/posts/how-to-get-started-with-maven)._