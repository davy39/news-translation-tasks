---
title: Projet Java – Comment construire un système simple de gestion de parking
subtitle: ''
author: Kunal Nalawade
co_authors: []
series: null
date: '2024-02-07T00:25:39.000Z'
originalURL: https://freecodecamp.org/news/java-project-parking-lot-management-system
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/java-article-image.jpeg
tags:
- name: Java
  slug: java
- name: projects
  slug: projects
seo_title: Projet Java – Comment construire un système simple de gestion de parking
seo_desc: 'Hello everyone! It''s good to be back with another tutorial – this time
  on Java, one of the most popular programming languages out there today.

  Java is used by developers and enterprises to build powerful applications that serve
  many different purpose...'
---

Bonjour à tous ! C'est un plaisir d'être de retour avec un autre tutoriel – cette fois sur Java, l'un des langages de programmation les plus populaires aujourd'hui.

Java est utilisé par les développeurs et les entreprises pour construire des applications puissantes qui servent à de nombreuses fins différentes. La nature orientée objet de Java rend l'écriture de code propre, modulaire et réutilisable très facile.

Si vous n'êtes pas encore à l'aise avec Java, il existe de nombreuses ressources en ligne qui peuvent vous aider à commencer. Vous pouvez consulter [cette collection de ressources](https://www.freecodecamp.org/news/learn-java-free-java-courses-for-beginners/) mise en place par l'un de nos membres de freeCodeCamp. [Voici un cours Java adapté aux débutants](https://www.freecodecamp.org/news/learn-the-basics-of-java-programming/). Et [voici un autre tutoriel utile](https://www.javatpoint.com/java-tutorial) pour vous aider à travailler sur les bases. Il n'est jamais trop tard !

Dans ce tutoriel, nous allons construire une application simple en ligne de commande pour un système de parking. Je commencerai par les exigences, puis listerai les classes nécessaires et expliquerai le flux de travail de l'application. Après cela, je vous montrerai comment implémenter chaque fonctionnalité.

## Voici ce que nous allons couvrir :

1. [Comment configurer le projet](#heading-installation-du-projet)

2. [Exigences du projet](#heading-exigences-du-projet)

3. [Classes Java](#heading-classes-java)

4. [Flux de travail de l'application](#heading-flux-de-travail-de-lapplication)

5. [Comment construire l'application](#heading-comment-construire-lapplication)

6. [Comment tester l'application](#heading-comment-tester-lapplication)

7. [Portée future](#heading-portee-future)

## Comment configurer le projet

Vous devez avoir Java 8 installé sur votre système. Si ce n'est pas le cas, téléchargez-le depuis [ici](https://www.oracle.com/java/technologies/downloads/) et suivez [ce](https://phoenixnap.com/kb/install-java-windows) guide d'installation. Installez également [Visual Studio Code](https://code.visualstudio.com/) et ajoutez l'extension [Support de langage pour Java](https://marketplace.visualstudio.com/items?itemName=redhat.java) sur VS Code.

Il n'est pas nécessaire de configurer une connexion à une base de données, un serveur externe ou un framework. Nous utiliserons une structure de données en mémoire pour stocker les données. De plus, nous n'allons pas créer d'interface utilisateur, car l'accent est uniquement mis sur la logique métier.

Cela étant dit, nous sommes prêts à commencer.

## Exigences du projet

Notre objectif est de créer une application pour un système de parking. Comme chacun visualise les projets différemment, il peut y avoir de nombreuses fonctionnalités qui vous viennent à l'esprit.

Mais avant de passer à l'implémentation, nous devons d'abord établir des exigences spécifiques. Il est toujours important de commencer par les exigences de base, c'est donc ce que nous allons faire ici.

Voici une liste de toutes les exigences :

* Un parking doit avoir un identifiant de parking, un nombre d'étages et un nombre de places sur chaque étage.

* Chaque place dans le parking a un type de véhicule qui peut s'y garer. Les types valides sont *voiture, moto* et *camion*. Vous pouvez inclure tout type de véhicule selon vos besoins. Vous pouvez également décider quelles places doivent être attribuées à chaque type. Ici, j'attribue la première place de chaque étage à un camion, les deux suivantes à des motos et le reste à des voitures.

* Lorsqu'un véhicule entre dans le parking, l'application prend le type de véhicule, le numéro d'immatriculation et sa couleur. Vous pouvez également avoir des détails supplémentaires comme le nom du véhicule, le nom du conducteur, etc.

* Après cela, une place est attribuée au véhicule. La stratégie de sélection peut être ce que vous voulez. Ici, nous choisirons l'étage le plus bas et la première place disponible.

* Lorsqu'une place est attribuée à un véhicule, l'application doit retourner un ticket. Le ticket doit être une chaîne de la forme . Par exemple, le véhicule garé à l'étage 2, place 5 serait *PR123\_2\_5.*

* Pour libérer le véhicule, l'utilisateur doit présenter le ticket valide. Après cela, le véhicule est retiré de la place.

* L'application doit être capable d'afficher le nombre de places disponibles et une liste des places disponibles et indisponibles pour un type de véhicule spécifique.

## Classes Java

Comprenons comment nous allons concevoir l'application. Puisqu'il s'agit d'une application en ligne de commande, nous allons uniquement écrire la logique métier d'un parking et afficher les sorties sur une console.

Nous aurons des classes séparées représentant les entités de notre application : `Vehicle` et `Slot`. Ensuite, nous créerons une classe `ParkingLot` qui contient la logique métier principale de notre application. Notre classe principale interagira avec cette classe pour toutes les fonctionnalités.

Maintenant, définissons nos classes. Chaque classe aura un constructeur pour initialiser leurs champs.

**Classe Vehicle :**

* `type`, `registration`, `color` (Tous sont de type chaîne)

**Classe Slot :**

* `type` (chaîne)

* `vehicle` (Vehicle) : type de véhicule garé dans la place

* `ticketId` (chaîne) : identifiant de ticket attribué au véhicule garé dans cette place, initialement null.

**Classe ParkingLot :**

**Champs :**

* `parkingLotId` (chaîne)

* `slots` (List&lt;List&gt;) : Il s'agit d'une liste de toutes les places dans le parking. La liste de listes représente les places sur plusieurs étages. Les étages et les places sont numérotés selon l'index de la liste.

**Constructeur :** `ParkingLot(parkingLotId, nfloors, noOfSlotsPerFlr)`

**Méthodes :**

* `parkVehicle(type, regNo, color)` : prend tous les paramètres d'un véhicule, attribue une place et retourne le ticket

* `unPark(ticketId)` : prend l'identifiant de ticket et retire le véhicule de la place

* `getNoOfOpenSlots(type)` : retourne le nombre de places pour le type de véhicule

* `displayOpenSlots(type)` : affiche toutes les places disponibles pour le type de véhicule

* `displayOccupiedSlots(type)` : affiche toutes les places occupées pour le type de véhicule

Cela contiendra notre logique métier principale, y compris les méthodes qui seront exposées au client, c'est-à-dire la méthode principale dans notre cas. La logique d'initialisation à l'intérieur du constructeur fonctionne différemment par rapport aux classes `Vehicle` et `Slot`.

Vous en apprendrez plus sur ces classes dans la section implémentation.

## Flux de travail de l'application

Maintenant que nous avons défini nos classes, comprenons le flux de travail de notre application.

Lorsqu'un véhicule entre dans le parking, le système prend les détails du véhicule et recherche une place disponible. S'il trouve une place libre, il attribue cette place au véhicule et retourne un ticket.

Cela est géré par la méthode `parkVehicle()`. Si une place n'est pas disponible, la méthode imprime un message d'erreur.

Maintenant, si le véhicule veut se libérer, il doit présenter le ticket. Le système analyse le ticket, découvre dans quelle place le véhicule est garé et libère la place. La méthode `unPark()` prend le ticket et libère la place correspondante.

Plongeons maintenant dans le code.

## Comment construire l'application

Écrivons d'abord nos classes `Vehicle` et `Slot` avec les champs mentionnés précédemment :

```java
public class Vehicle {
    String type;
    String registration;
    String color;
    public Vehicle(String type, String registration, String color) {
        this.type = type;
        this.registration = registration;
        this.color = color;
    }
}
```

```java
public class Slot {
    String type;
    Vehicle vehicle;
    String ticketId;
    public Slot(String type) {
        this.type = type;
        this.vehicle=null;
        this.ticketId=null;
    }
}
```

Maintenant, implémentons la classe `ParkingLot`. Nous avons discuté des champs et des méthodes que la classe contiendra. Écrivons d'abord les champs.

```java
public class ParkingLot {
    String parkingLotId;
    List<List<Slot>> slots;
 	
    ... constructeur et méthodes ...
 }
```

Je vais vous montrer, étape par étape, comment implémenter chaque fonctionnalité.

### Initialiser la classe

Initialisez la classe `ParkingLot` via le constructeur. C'est ici que nous construisons notre parking. Comme mentionné précédemment, le parking aura un nombre donné d'étages et un nombre de places par étage.

```java
ParkingLot(String parkingLotId, int nfloors, int noOfSlotsPerFlr) {
		... code ici ...
    }
```

Commencez par définir l'identifiant du parking.

```java
this.parkingLotId=parkingLotId;
```

Ensuite, initialisez toutes les places. Sur chaque étage, la première place est attribuée à un camion, les deux suivantes à des motos et le reste à des voitures.

```java
slots = new ArrayList<>();
for(int i=0;i<nfloors;i++){
	slots.add(new ArrayList<>());
	List<Slot> floorSlots = slots.get(i);
    floorSlots.add(new Slot("truck"));
    floorSlots.add(new Slot("bike"));
    floorSlots.add(new Slot("bike"));

    for(int j=3;j<noOfSlotsPerFlr;j++){
	    slots.get(i).add(new Slot("car"));
    }
}
```

Ici, nous avons fait une initialisation simple pour chaque objet `Slot` dans la liste.

### Garer le véhicule

Implémentons maintenant la méthode `parkVehicle()`.

```java
public String parkVehicle(String type, String regNo, String color) {
        ... Implémentation ici ...
    }
```

Tout d'abord, créez un objet `Vehicle` avec les détails donnés.

```java
Vehicle vehicle = new Vehicle(type, regNo, color);
```

Parcourez toute la liste des places et trouvez la première place vide. Pour déterminer si une place est vide ou non, vérifiez si la place peut prendre le type de véhicule donné et si le champ `vehicle` de la place est null (ce qui signifie qu'elle est vide).

```java
for(int i=0; i<slots.size();i++){
            for(int j=0;j<slots.get(i).size(); j++){
                Slot slot = slots.get(i).get(j);
                if(slot.type.equals(type) && slot.vehicle == null) {
                    ... attribuez la place ici ...
                }
            }
        }
```

Pour attribuer cette place au véhicule, définissez simplement le champ `vehicle` sur l'objet `Vehicle` que nous avons créé ci-dessus. Ensuite, générez et retournez un ticket en utilisant les numéros d'étage et de place.

```java
slot.vehicle=vehicle;
slot.ticketId=generateTicketId(i+1, j+1);
return slot.ticketId;
```

```java
private String generateTicketId(int flr, int slno){
        return parkingLotId + "_" + flr + "_" + slno;
    }
```

Cette méthode n'a pas besoin d'être exposée à l'extérieur de la classe, elle est donc privée.

Si une place n'est pas disponible, retournez null ou lancez une exception. Faites cela après que la boucle for soit terminée.

```java
System.out.println("Aucune place disponible pour le type donné");
return null;
```

### Libérer le véhicule

Pour libérer le véhicule, analysez l'identifiant de ticket pour obtenir le numéro d'étage et de place où la voiture est garée.

```java
public void unPark(String ticketId){
        String[] extract = ticketId.split("_");
        int flr_idx=Integer.parseInt(extract[1])-1;
        int slot_idx=Integer.parseInt(extract[2])-1;
        
         ...
    }
```

Entourez la logique d'analyse avec un try-catch au cas où l'utilisateur passerait un identifiant de ticket invalide.

Avec le numéro d'étage et de place, trouvez la place où le véhicule est garé et désattribuez le véhicule.

```java
for(int i=0; i<slots.size();i++){
            for(int j=0;j<slots.get(i).size(); j++){
                if(i==flr_idx && j==slot_idx) {
                    Slot slot = slots.get(i).get(j);
                    slot.vehicle=null;
                    slot.ticketId=null;
                    System.out.println("Véhicule libéré");
                }
            }
        }
```

### Afficher les informations du parking

Nous avons défini trois méthodes pour afficher les informations du parking sous différentes formes.

**Retourner le nombre de places disponibles pour un type de véhicule.**

```java
int getNoOfOpenSlots(String type){
        int count=0;
        for(List<Slot> floor: slots){
            for(Slot slot: floor){
                if(slot.vehicle == null && slot.type.equals(type)) count++;
            }
        }

        return count;
    }
```

Ici, nous parcourons toutes les places et vérifions deux conditions. Tout d'abord, nous vérifions si le champ `vehicle` est null, indiquant une place vide. Ensuite, nous vérifions si le type de la place correspond au type de véhicule demandé par le client.

Nous retournons ensuite simplement le nombre de places vides pour le type donné.

**Afficher toutes les places disponibles pour un type de véhicule :**

```java
void displayOpenSlots(String type){
        for(int i=0;i<slots.size();i++){
            for(int j=0;j<slots.get(i).size();j++){
                Slot slot=slots.get(i).get(j);
                if(slot.vehicle == null && slot.type.equals(type)) 
                    System.out.println("Étage " + (i+1) + " place " + (j+1));
            }
        }   
    }
```

C'est une amélioration par rapport à la fonction précédente. Au lieu du compte, nous retournons les places vides réelles avec le numéro d'étage et de place.

**Afficher toutes les places occupées pour un type de véhicule :**

```java
void displayOccupiedSlots(String type){
        for(int i=0;i<slots.size();i++){
            for(int j=0;j<slots.get(i).size();j++){
                Slot slot=slots.get(i).get(j);
                if(slot.vehicle != null && slot.type.equals(type)) 
                    System.out.println("Étage " + (i+1) + " place " + (j+1));
            }
        }   
    }
```

Ici, nous vérifions la condition opposée pour le champ `vehicle`. S'il n'est pas null, alors cette place est occupée par un véhicule. Nous vérifions ensuite si le type de véhicule correspond au type demandé et affichons le numéro d'étage et de place.

Avec cela, nous avons notre implémentation de base d'un parking. Il est temps de tester chaque fonctionnalité.

## Comment tester l'application

Puisque nous n'avons pas d'interface utilisateur ou de framework de test, nous allons tester chaque fonctionnalité manuellement à partir du code pilote. Comme toute application Java, la nôtre démarrera également à partir de la méthode principale.

Tout d'abord, créons un objet `ParkingLot`. Chaque fonctionnalité du parking sera accessible via cet objet.

```java
int nFloors=4;
int nSlotsPerFloor=6;
ParkingLot parkingLot = new ParkingLot("PR1234", nFloors, nSlotsPerFloor);
```

Cela crée un parking avec 4 étages et 6 places par étage, pour un total de 24 places.

```java
parkingLot.getNoOfOpenSlots("car")

String ticket1 = parkingLot.parkVehicle("car", "MH-03", "red");
String ticket2 = parkingLot.parkVehicle("car", "MH-04", "purple");

parkingLot.displayOccupiedSlots("car");
```

Tout d'abord, nous affichons le nombre de places disponibles pour une voiture. Ensuite, nous garons deux voitures et obtenons les tickets. Après le stationnement, nous affichons les places occupées.

Pour exécuter le programme, cliquez sur le bouton d'exécution en haut à droite.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/blg1.png align="left")

*Éditeur VS Code*

Cela donne la sortie suivante.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-34.png align="left")

*Sortie pour les cas de test ci-dessus*

Ici, vous pouvez voir que les premières places disponibles ont été attribuées à la voiture.

Maintenant, libérez le deuxième véhicule et affichez les places occupées.

```java
parkingLot.unPark(ticket2);
parkingLot.displayOccupiedSlots("car");
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-35.png align="left")

*Après libération*

Essayons maintenant de garer un camion. Affichons les places disponibles pour un camion, garons le camion et affichons les places occupées.

```java
parkingLot.displayOpenSlots("truck");
parkingLot.parkVehicle("truck", "MH-01", "black");
parkingLot.displayOccupiedSlots("truck");
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-36.png align="left")

*Sortie après avoir garé un camion*

Je vais garer trois autres camions et essayer ensuite d'en garer un autre. Comme il n'y a plus de places pour camions disponibles, cela affiche le message suivant :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-38.png align="left")

*Sortie si le parking est plein*

## Portée future

Dans cet article, nous avons créé une application très basique en ligne de commande pour un parking. L'application ne fait qu'une seule chose – attribuer et désattribuer un véhicule d'une place de parking. Mais il y a beaucoup d'autres choses que vous pouvez ajouter à cette application de base :

* Utilisez l'encapsulation partout où c'est possible. Techniquement, cela ne devrait pas figurer dans la portée future. Je n'ai pas utilisé l'encapsulation ici car je voulais me concentrer uniquement sur la partie conception et logique. Mais en travaillant sur des applications réelles, n'oubliez pas d'encapsuler tous les champs et d'y accéder via des getters et des setters.

* Implémentez une gestion des exceptions appropriée pour les scénarios où une place n'est pas disponible, où un type de véhicule n'est pas autorisé ou où le ticket est invalide.

* Vous pouvez ajouter plus de types de véhicules au parking et utiliser une stratégie différente pour attribuer les types de places.

* Vous pouvez utiliser une stratégie différente pour trouver la première place disponible.

* Vous pouvez exposer toute la logique dont nous avons discuté ici en tant que service backend et créer une interface utilisateur pour votre parking avec une base de données également.

Vous pouvez trouver le code sur GitHub [ici](https://github.com/KunalN25/parking-lot-app).

## Conclusion

Dans cet article, nous avons créé une application simple en ligne de commande avec Java à partir des exigences. À partir de la liste des exigences, nous avons déterminé la conception de l'application et défini les classes nécessaires. Ensuite, nous avons compris le flux de travail de notre application.

Après avoir finalisé la conception et le flux de travail, nous sommes passés à l'implémentation. Cette application simple était un exemple de la manière dont vous définissez les exigences et, sur la base de ces exigences, déterminez la conception et le flux de travail de votre application.

Avant d'écrire le code, vous devez savoir quelles classes vous allez utiliser et le but de chaque classe. Cela est vrai, peu importe la taille de l'application que vous souhaitez créer. J'espère que cela vous aidera dans vos futurs projets.

Si vous n'êtes pas en mesure de comprendre le contenu ou si vous trouvez l'explication insatisfaisante, commentez vos pensées ci-dessous. Les nouvelles idées sont toujours appréciées ! N'hésitez pas à me contacter sur Twitter. En attendant, au revoir !

### Ressources utiles

* [workat.tech](https://workat.tech/machine-coding/practice/design-parking-lot-qm6hwq4wkhp8) dispose de nombreuses ressources pour réussir les entretiens dans les meilleures entreprises basées sur des produits. Cet article est inspiré par l'une de ces ressources.

* [Voici un manuel Java pour débutants](https://www.freecodecamp.org/news/the-java-handbook/) qui vous enseignera de nombreux concepts fondamentaux.

* Et [voici un manuel Java plus avancé](https://www.freecodecamp.org/news/object-oriented-programming-in-java/) qui couvre des concepts de programmation orientée objet plus avancés.