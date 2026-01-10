---
title: Comment écrire des tests unitaires en Java
subtitle: ''
author: Kunal Nalawade
co_authors: []
series: null
date: '2023-04-03T15:37:52.000Z'
originalURL: https://freecodecamp.org/news/java-unit-testing
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/photo-1498050108023-c5249f4df085.jpeg
tags:
- name: Java
  slug: java
- name: unit testing
  slug: unit-testing
seo_title: Comment écrire des tests unitaires en Java
seo_desc: 'Let''s say you are developing an application. After long hours of coding,
  you manage to create some cool features. Now, you want to make sure the features
  are working as you want.

  This involves testing if each and every piece of code works as expected...'
---

Disons que vous développez une application. Après de longues heures de codage, vous parvenez à créer quelques fonctionnalités intéressantes. Maintenant, vous voulez vous assurer que les fonctionnalités fonctionnent comme vous le souhaitez.

Cela implique de tester si chaque morceau de code fonctionne comme prévu. Cette procédure est connue sous le nom de Test Unitaire. Différents langages fournissent leurs propres frameworks pour les tests.

Dans cet article, je vais vous montrer comment écrire des tests unitaires en Java. Je vais d'abord expliquer ce que le test implique et quelques concepts que vous devez connaître. Ensuite, je vais montrer quelques exemples pour vous aider à mieux comprendre.

Pour cet article, je suppose que vous êtes familier avec Java et l'IDE IntelliJ.

## Installation du Projet

Pour ce projet, j'utiliserai l'IDE IntelliJ. Si vous ne l'avez pas, suivez [ce](https://www.jetbrains.com/help/idea/installation-guide.html#standalone) guide pour installer l'IDE.

Dans ce projet, nous utiliserons les bibliothèques JUnit et Mockito pour les tests. Ce sont les bibliothèques les plus couramment utilisées pour les tests en Java. Vous comprendrez comment ces bibliothèques sont utilisées au fur et à mesure que vous avancerez dans l'article.

Pour configurer JUnit, suivez ces étapes [comme décrit dans ce guide](https://www.jetbrains.com/help/idea/junit.html) :

1. Dans le menu principal, sélectionnez Fichier &gt; Nouveau &gt; Projet.
    
2. Sélectionnez **Nouveau Projet**. Spécifiez un nom pour le projet, je vais l'appeler junit-testing-tutorial.
    
3. Sélectionnez **Maven** comme outil de construction et en langage, sélectionnez Java.
    
4. Dans la liste **JDK**, sélectionnez le JDK que vous souhaitez utiliser dans le projet.
    
5. Cliquez sur **Créer**.
    
6. Ouvrez **pom.xml** dans le répertoire racine de votre projet.
    
7. Dans pom.xml, appuyez sur `⌘ + N`, et sélectionnez **Ajouter une dépendance**.
    
8. Cela ouvrira une fenêtre d'outil, tapez `org.junit.jupiter:junit-jupiter` dans le champ de recherche. Localisez la dépendance nécessaire et cliquez sur **Ajouter** à côté.
    
9. Maintenant, cliquez sur **Charger les modifications Maven** dans la notification qui apparaît dans le coin supérieur droit dans l'éditeur.
    

Maintenant, pour configurer Mockito, ajoutez ces deux dépendances dans votre `pom.xml` :

```xml
<dependency>
    <groupId>org.mockito</groupId>
    <artifactId>mockito-inline</artifactId>
    <version>5.2.0</version>
    <scope>compile</scope>
</dependency>
<dependency>
    <groupId>org.mockito</groupId>
    <artifactId>mockito-junit-jupiter</artifactId>
    <version>5.2.0</version>
	<scope>compile</scope>
</dependency>
```

**Note** : La version peut différer en fonction du moment où vous lisez cet article.

Pour compléter la configuration, créez une classe `Welcome` et définissez votre fonction principale là.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-12-at-6.14.33-PM.png align="left")

*Structure des dossiers et la méthode principale*

## Qu'est-ce que le Test Unitaire ?

Le Test Unitaire implique de tester chaque composant de votre code pour voir s'ils fonctionnent comme prévu. Il isole chaque méthode individuelle de votre code et effectue des tests sur celle-ci. Les tests unitaires aident à s'assurer que votre logiciel fonctionne comme prévu avant de le publier.

En tant que développeur, vous écrirez des tests unitaires dès que vous aurez fini d'écrire un morceau de code. Maintenant, vous pourriez demander, n'est-ce pas le travail d'un testeur ? D'une certaine manière, oui, un testeur est responsable de tester le logiciel. Mais, couvrir chaque ligne de code ajoute beaucoup de pression sur le testeur. Donc, c'est une bonne pratique pour les développeurs d'écrire des tests pour leur propre code également.

Le but du test unitaire est de s'assurer que toute nouvelle fonctionnalité ne casse pas la fonctionnalité existante. Cela aide également à identifier tout problème ou bug plus tôt dans le processus de développement et aide à garantir que le code répond aux normes de qualité fixées par l'organisation.

### Ce qu'il faut faire et ne pas faire dans les Tests Unitaires

Rappelez-vous les directives suivantes lors de l'écriture de tests pour vos méthodes :

* Testez si la sortie attendue d'une méthode correspond à la sortie réelle.
    
* Testez si les appels de fonction effectués à l'intérieur de la méthode se produisent le nombre de fois souhaité.
    
* N'essayez pas de tester le code qui ne fait pas partie de la méthode sous test.
    
* Ne faites pas d'appels API, de connexions à la base de données ou de requêtes réseau lors de l'écriture de vos tests.
    

Maintenant, passons en revue quelques concepts que vous devez connaître avant de vous lancer dans l'écriture de tests.

### Assertions

Les assertions déterminent si votre test passe ou échoue. Elles comparent la valeur de retour attendue d'une méthode avec la valeur réelle. Il existe un certain nombre d'assertions que vous pouvez faire à la fin de votre test.

La classe `Assertions` dans JUnit se compose de méthodes statiques qui fournissent diverses conditions décidant si le test passe ou non. Nous verrons ces méthodes au fur et à mesure que je vous guiderai à travers chaque exemple.

### Mocking

La classe dont vous testez les méthodes peut avoir certaines dépendances externes. Comme mentionné précédemment, vous ne devriez pas essayer de tester le code qui ne fait pas partie de la fonction sous test.

Mais dans les cas où votre fonction utilise une classe externe, il est bon de mock cette classe – c'est-à-dire, avoir des valeurs mock au lieu des valeurs réelles. Nous utiliserons la bibliothèque Mockito à cette fin.

### Stubbing de Méthode

Les dépendances externes peuvent ne pas se limiter aux classes, mais aussi à certaines méthodes. Le [stubbing de méthode](https://en.wikipedia.org/wiki/Method_stub) doit être fait lorsque votre fonction appelle une fonction externe dans son code. Dans ce cas, vous faites en sorte que cette fonction retourne la valeur que vous voulez au lieu d'appeler la méthode réelle.

Par exemple, la méthode que vous testez (A) appelle une méthode externe (B) dans son implémentation. B effectue une requête de base de données, récupérant tous les étudiants avec des notes supérieures à 80. Faire un appel réel à la base de données n'est pas une bonne pratique ici. Donc, vous stub la méthode et faites en sorte qu'elle retourne une liste factice d'étudiants dont vous avez besoin pour le test.

Vous comprendrez mieux cela avec des exemples. Il existe de nombreux autres concepts qui font partie des tests en Java. Mais, pour l'instant, ces trois sont suffisants pour vous permettre de commencer.

## Étapes à Effectuer Lors des Tests

1. Initialisez les paramètres nécessaires dont vous aurez besoin pour effectuer le test.
    
2. Créez des objets mock et stub les méthodes si nécessaire.
    
3. Appelez la méthode que vous testez avec les paramètres que vous avez initialisés à l'étape 1.
    
4. Ajoutez une assertion pour vérifier le résultat de votre test. Cela décidera si le test passe.
    

Vous comprendrez mieux ces étapes avec des exemples. Commençons par un test de base.

## Comment Écrire le Premier Test

Écrivons une fonction simple qui compare deux nombres. Elle retourne `1` si le premier nombre est supérieur au second et retourne `-1` sinon.

Nous mettrons cette fonction à l'intérieur d'une classe `Basics` :

```java
public class Basics {
    public int compare(int n1, int n2) {
        if (n1 > n2) return 1;
        return -1;
    }
}
```

Très simple ! Écrivons le test pour cette classe. Tous vos tests doivent être situés à l'intérieur du dossier de test.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-13-at-5.12.04-PM.png align="left")

*Structure des dossiers*

À l'intérieur du dossier de test, créez une classe `BasicTests` où vous écrirez vos tests pour cette classe. Le nom de la classe n'a pas d'importance, mais il est bon de séparer les tests selon chaque classe. Suivez également une structure de dossier similaire à celle de votre code principal.

```java
public class BasicTests {
    // Vos tests viennent ici
}
```

Les tests unitaires sont essentiellement un ensemble de méthodes que vous définissez pour tester chaque méthode de votre classe. À l'intérieur de la classe ci-dessus, créez une méthode `compare()` avec un type de retour `void`. Encore une fois, vous pouvez nommer la méthode comme vous le souhaitez.

```python
@Test
public void compare() {
    
}
```

L'annotation `@Test` indique que cette méthode doit être exécutée en tant que cas de test.

Maintenant, pour tester la méthode, vous devez créer l'objet de la classe ci-dessus et appeler la méthode en passant quelques valeurs.

```java
Basics basicTests = new Basics();
int value = basicTests.compare(2, 1);
```

Maintenant, utilisez la méthode `assertEquals()` de la classe `Assertions` pour vérifier si la valeur attendue correspond à la valeur attendue.

```java
Assertions.assertEquals(1, value);
```

Notre test devrait passer, car la valeur retournée par la méthode correspond à celle attendue. Pour le vérifier, exécutez le test en cliquant sur la flèche verte à côté de la méthode de test.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-13-at-5.30.14-PM.png align="left")

*Exécution d'un Test*

Les résultats de votre test seront affichés ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-13-at-5.32.06-PM.png align="left")

*Résultats des Tests*

## Plus d'Exemples de Tests

Dans le test ci-dessus, nous n'avons testé qu'un seul scénario. Lorsqu'il y a des branches dans la fonction, vous devez écrire des tests pour chaque condition. Introduisons quelques branches supplémentaires dans la fonction ci-dessus.

```java
public int compare(int n1, int n2) {
    if (n1 > n2) return 1;
    else if (n1 < n2) return -1;
    return 0;
}
```

Nous avons déjà testé la première branche, alors écrivons des tests pour les deux autres.

```python
@Test
@DisplayName("Le premier nombre est inférieur au second")
public void compare2() {
    Basics basicTests = new Basics();
    int value = basicTests.compare(2, 3);
    Assertions.assertEquals(-1, value);
}
```

L'annotation `@DisplayName` affiche le texte au lieu du nom de la méthode ci-dessous. Exécutons le test.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-13-at-6.01.15-PM.png align="left")

*Test Réussi*

Pour le cas où les deux nombres sont égaux :

```java
@Test
@DisplayName("Le premier nombre est égal au second")
public void compare3() {
    Basics basicTests = new Basics();
    int value = basicTests.compare(2, 2);
    Assertions.assertEquals(0, value);
}
```

### Tri d'un Tableau

Maintenant, écrivons le test pour le code suivant qui trie un tableau.

```java
public void sortArray(int[] array) {
        int n = array.length;
        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n-i-1; j++) {
                if (array[j] > array[j+1]) {
                    int temp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp;
                }
            }
        }
    }
```

Pour écrire le test pour cela, nous suivrons une procédure similaire : appelez la méthode et passez-lui un tableau. Utilisez `assertArrayEquals()` pour écrire votre assertion.

```java
@Test
@DisplayName("Tableau trié")
public void sortArray() {
    Basics basicTests = new Basics();
    int[] array = {5, 8, 3, 9, 1, 6};
    basicTests.sortArray(array);
    Assertions.assertArrayEquals(new int[]{1, 3, 5, 6, 8, 9}, array);
}
```

Un défi pour vous : écrivez du code qui inverse une chaîne et écrivez un cas de test pour cela.

## Comment Créer des Mocks et des Stubs pour les Tests

Nous avons vu quelques exemples de base de tests unitaires où vous avez fait des assertions simples. Cependant, les fonctions que vous testez peuvent contenir des dépendances externes comme des classes de modèle et des connexions à la base de données ou au réseau.

Maintenant, vous ne pouvez pas faire de connexions réelles dans vos tests, car cela serait très chronophage. Dans de tels cas, vous mock ces implémentations. Regardons quelques exemples de mocking.

### Mocking d'une Classe

Prenons une classe User avec les propriétés suivantes :

```java
public class User {
    private String username;
    private String password;
    private String role;
    private List<String> posts;    
}
```

Cliquez sur `⌘ + N` pour générer les getters et setters pour les propriétés ci-dessus.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-18-at-8.34.34-PM.png align="left")

*Options de Génération*

Prenons une nouvelle classe `Mocking` qui utilise l'objet ci-dessus.

```java
public class Mocking {
    User user;

    public void setUser(User user) {
        this.user = user;
    }
}
```

Cette classe a une méthode qui attribue certaines permissions en fonction du rôle de l'utilisateur. Elle retourne `1` si la permission est attribuée avec succès, sinon elle retourne `-1`.

```java
public int assignPermission() {
        if(user.getRole().equals("admin")) {
            String username = user.getUsername();
            System.out.println("Assign special permissions for user " + username);
            return 1;
        } else {
            System.out.println("Cannot assign permission");
            return -1;
        }
    }
```

À des fins de démonstration, j'ai simplement ajouté des instructions `println()`. L'implémentation réelle peut impliquer la définition de certaines propriétés.

Dans le fichier de tests, nous ajouterons une annotation `@ExtendWith` en haut puisque nous utilisons Mockito. Je n'ai pas montré les imports ici car IntelliJ les fait automatiquement.

```python
@ExtendWith(MockitoExtension.class)
public class MockingTests {

}
```

Alors, comment écrivons-nous le test pour la méthode ? Nous aurons besoin de mock l'objet `User`. Vous pouvez faire cela en ajoutant une annotation `@Mock` lors de la déclaration de l'objet.

```java
@Mock
User user;
```

Vous pouvez également utiliser la méthode `mock()`, car elle est similaire.

```java
User user = mock(User.class);
```

Écrivons la méthode de test.

```java
@Test
@DisplayName("Permission attribuée avec succès")
public void assignPermissions() {
    Mocking mocking = new Mocking();
    Assertions.assertEquals(1, mocking.assignPermission());
}
```

Lorsque vous exécutez le test, il lance une `NullPointerException`.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-18-at-8.51.26-PM.png align="left")

*L'objet User est Null*

Cela est dû au fait que l'objet user n'a pas encore été initialisé. La méthode que vous avez appelée n'a pas pu utiliser l'objet mock. Pour cela, vous devrez appeler la méthode `setUser`.

```java
mocking.setUser(user);
```

Maintenant, le test donne l'erreur suivante car l'objet mock est initialement rempli de valeurs nulles.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-18-at-8.53.53-PM.png align="left")

*La valeur de retour de getRole() est Null*

Cela signifie-t-il que vous devez remplir des valeurs réelles dans l'objet mock ? Non, vous avez simplement besoin que la méthode `getRole()` retourne une valeur non nulle. Pour cela, nous utiliserons le **stubbing de méthode**.

```python
when(user.getRole()).thenReturn("admin");
```

L'utilisation de `when()...thenReturn()` indique au test de retourner une valeur lorsqu'une méthode est appelée. Vous devez stub les méthodes uniquement pour les objets mock.

Nous ferons de même pour la méthode `getUsername()`.

```python
when(user.getUsername()).thenReturn("kunal");
```

Maintenant, si vous exécutez le test, il passera.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-18-at-9.00.21-PM.png align="left")

*Test Réussi*

### Exemple de Stubbing de Méthode

Dans l'exemple ci-dessus, j'ai simplement stub les méthodes getter pour démontrer le stubbing de méthode. Au lieu de stub les getters, vous pourriez définir le rôle et le nom d'utilisateur avec un constructeur paramétré ou des méthodes setter si elles sont disponibles.

```java
user.setRole("admin");
user.setUsername("kunal");
```

Mais que se passe-t-il si la classe utilisateur a une méthode qui retourne tous les posts contenant un certain mot ?

```java
public List<String> getAllPostsContainingWord(String word) {
        List<String> filteredPosts = new ArrayList<>();
        for(String post: posts) {
            if(post.contains(word))
                filteredPosts.add(post);
        }
        return filteredPosts;
    }
```

Nous voulons que cette méthode retourne tous les posts contenant le mot "awesome". Si vous appelez l'implémentation réelle de cette méthode, cela pourrait prendre beaucoup de temps car le nombre de posts pourrait être énorme. De plus, si vous mock l'objet User, le tableau des posts serait null.

Dans ce cas, vous stub la méthode et faites en sorte qu'elle retourne la liste que vous voulez.

```java
List<String> filteredPosts = new ArrayList<>();
filteredPosts.add("Awesome Day");
filteredPosts.add("This place is awesome");
when(user.getAllPostsContainingWord("awesome")).thenReturn(filteredPosts);
```

### Stubbing de Méthode dans les Requêtes de Base de Données

Voyons comment tester les méthodes qui impliquent de faire des connexions à la base de données. Tout d'abord, créez une classe `ApplicationDao` qui contient toutes les méthodes effectuant des requêtes de base de données.

```java
public class ApplicationDao {  }
```

Définissez une méthode qui récupère l'utilisateur par `id` et retourne `null` si l'utilisateur n'est pas trouvé.

```java
public User getUserById(String id) {
	// Faire une requête de base de données ici        
}
```

Créez une autre méthode pour sauvegarder un utilisateur dans la base de données. Cette méthode lance une exception si l'objet utilisateur que vous essayez de sauvegarder est `null`.

```java
public void save(User user) throws Exception {
	// Faire une requête de base de données ici
}
```

Notre classe Mocking utilisera ces méthodes pour implémenter ses propres fonctionnalités. Nous implémenterons une fonction qui met à jour le nom d'un utilisateur.

```java
public int updateUsername(String id, String username) throws Exception{
            ApplicationDao applicationDao = new ApplicationDao();
            User user = applicationDao.getUserById(id);
            if(user!=null)
                user.setUsername(username);
            applicationDao.save(user);
            return 1;
    }
```

L'implémentation de la méthode est assez simple. Tout d'abord, obtenez l'utilisateur par `id`, changez son nom d'utilisateur et sauvegardez l'objet utilisateur mis à jour. Nous écrirons les cas de test pour cette méthode.

Il y a deux cas que nous devons tester. Le premier est lorsque l'utilisateur est mis à jour avec succès. Le second est lorsque la mise à jour échoue, c'est-à-dire lorsqu'une exception est lancée.

Avant d'écrire les tests, créez un mock de l'objet `ApplicationDao` car nous ne voulons pas faire de connexions réelles à la base de données.

```java
@Mock
ApplicationDao applicationDao;
```

Écrivons notre premier test.

```python
@Test
    @DisplayName("Utilisateur mis à jour avec succès")
    public void updateUsername() throws Exception {
        ...
    }
```

Créez un objet utilisateur pour le test.

```java
User user = new User();
user.setUsername("kunal");
```

Puisque nous appelons une méthode externe, stub la méthode pour qu'elle retourne l'objet `User` ci-dessus.

```java
when(applicationDao.getUserById(Mockito.anyString())).thenReturn(user);
```

Passez `Mockito.anyString()` à la méthode car nous voulons que le stub fonctionne pour tout paramètre de chaîne. Maintenant, ajoutez une assertion pour vérifier si la méthode fonctionne correctement.

```java
Assertions.assertEquals(1, mocking.updateUsername("3211", "allan"));
```

La méthode retourne 1 en cas de mise à jour réussie, donc le test passe.

Maintenant, testons un autre scénario où la méthode échoue et lance une exception. Simulez ce scénario en faisant en sorte que la méthode `getUserById()` retourne null.

```java
lenient().when(applicationDao.getUserById(Mockito.anyString())).thenReturn(null);
```

Cette valeur est ensuite passée à la méthode `save()` qui, à son tour, lance une exception. Dans notre assertion, nous utiliserons la méthode `assertThrows()` pour tester si une exception a été lancée. Cette méthode prend le type de l'exception et une expression lambda comme paramètres.

```java
Assertions.assertThrows(Exception.class, () -> {
            mocking.updateUsername("3412","allan");
        });
```

Puisque l'exception est lancée, notre test passe.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-26-at-4.27.07-PM.png align="left")

*Tests Réussis*

Vous pouvez trouver le code complet ici sur [GitHub](https://github.com/KunalN25/junit-testing-tutorial).

## Conclusion

En tant que développeur, écrire des tests unitaires pour votre code est important. Cela vous aide à identifier les bugs plus tôt dans le processus de développement.

Dans cet article, j'ai commencé par introduire les Tests Unitaires et expliqué trois concepts importants impliqués dans le processus de test. Ceux-ci vous ont donné un peu de contexte avant de vous lancer dans le code.

Après cela, je vous ai montré, avec des exemples, comment vous pouvez tester différents scénarios en utilisant les mêmes techniques de base en test. J'ai également montré comment utiliser des classes et méthodes mock pour tester des implémentations complexes.