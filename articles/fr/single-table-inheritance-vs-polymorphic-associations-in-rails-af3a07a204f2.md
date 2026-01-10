---
title: 'Héritage à table unique vs. associations polymorphiques dans Rails : trouvez
  ce qui vous convient'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-16T22:43:27.000Z'
originalURL: https://freecodecamp.org/news/single-table-inheritance-vs-polymorphic-associations-in-rails-af3a07a204f2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*THwLoeqaLjU3IRE83n8TAA.jpeg
tags:
- name: database
  slug: database
- name: Ruby
  slug: ruby
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Héritage à table unique vs. associations polymorphiques dans Rails : trouvez
  ce qui vous convient'
seo_desc: 'By Haley Mnatzaganian

  If you’ve ever created an application with more than one model, you’ve had to think
  about what type of relationships to use between those models.

  As an application’s complexity grows, it can be difficult to decide which relation...'
---

Par Haley Mnatzaganian

Si vous avez déjà créé une application avec plus d'un modèle, vous avez dû réfléchir au type de relations à utiliser entre ces modèles.

À mesure que la complexité d'une application augmente, il peut être difficile de décider quelles relations doivent exister entre vos modèles.

Une situation qui se présente fréquemment est lorsque plusieurs de vos modèles doivent avoir accès à la fonctionnalité d'un troisième modèle. Deux méthodes que Rails nous donne pour gérer cet événement sont **l'héritage à table unique** et **l'association polymorphique.**

![Image](https://cdn-media-1.freecodecamp.org/images/DTM68ANtS7ExFvaAe8D9OFXE1nKiVDF8dCVQ)

**Dans l'Héritage à Table Unique (STI),** de nombreuses sous-classes héritent d'une superclasse avec toutes les données dans la même table de la base de données. La superclasse a une colonne "type" pour déterminer à quelle sous-classe un objet appartient.

Dans une **association polymorphique**, un modèle "appartient à" plusieurs autres modèles en utilisant une seule association. Chaque modèle, y compris le modèle polymorphique, a sa propre table dans la base de données.

Examinons chaque méthode pour voir quand nous les utiliserions.

### **Héritage à Table Unique**

Un excellent moyen de savoir quand STI est approprié est lorsque vos modèles ont des **données/états partagés**. Le comportement partagé est facultatif.

Imaginons que nous créons une application qui liste différents véhicules en vente chez un concessionnaire local. Ce concessionnaire vend des voitures, des motos et des vélos.

(Je sais que les concessionnaires ne vendent pas de vélos, mais suivez-moi un instant — vous verrez où je veux en venir.)

Pour chaque véhicule, le concessionnaire souhaite suivre le prix, la couleur et si le véhicule a été acheté. Cette situation est un candidat parfait pour STI, car nous utilisons les mêmes données pour chaque classe.

Nous pouvons créer une superclasse `Vehicle` avec les attributs pour la couleur, le prix et l'achat. Chacune de nos sous-classes peut hériter de `Vehicle` et peut obtenir tous ces mêmes attributs en une seule fois.

Notre migration pour créer la table des véhicules pourrait ressembler à ceci :

```
class CreateVehicles < ActiveRecord::Migration[5.1]
  def change
    create_table :vehicles do |t|
      t.string :type, null: false
      t.string :color
      t.integer :price
      t.boolean :purchased, default: false
    end
  end
end
```

Il est important que nous créions la colonne `type` pour la superclasse. Cela indique à Rails que nous utilisons STI et que nous voulons que toutes les données pour `Vehicle` et ses sous-classes soient dans la même table de la base de données.

Nos classes de modèles ressembleraient à ceci :

```
class Vehicle < ApplicationRecord
end
```

```
class Bicycle < Vehicle
end
```

```
class Motorcycle < Vehicle
end
```

```
class Car < Vehicle
end
```

Cette configuration est idéale car toutes les méthodes ou validations dans la classe `Vehicle` sont partagées avec chacune de ses sous-classes. Nous pouvons ajouter des méthodes uniques à l'une des sous-classes selon les besoins. Elles sont indépendantes les unes des autres et leur comportement n'est pas partagé horizontalement.

De plus, puisque nous savons que les sous-classes partagent les mêmes champs de données, nous pouvons faire les mêmes appels sur des objets de différentes classes :

```
mustang = Car.new(price: 50000, color: red)
harley = Motorcycle.new(price: 30000, color: black)
```

```
mustang.price
=> 50000
```

```
harley.price
=> 30000
```

![Image](https://cdn-media-1.freecodecamp.org/images/0g6EmTW86Pjlpxg6PSODx4lr4JREv3lchFn3)
_Umm, où puis-je trouver ce concessionnaire ? ([source](https://www.flickr.com/photos/bagogames/14870700349" rel="noopener" target="_blank" title="))_

#### **Ajout de fonctionnalités**

Maintenant, supposons que le concessionnaire décide de collecter plus d'informations sur les véhicules.

Pour les `Bicycles`, elle veut savoir si chaque vélo est un vélo de route, de montagne ou hybride. Et pour les `Cars` et `Motorcycles`, elle veut suivre la puissance en chevaux.

Nous créons donc une migration pour ajouter `bicycle_type` et `horsepower` à la table `Vehicles`.

Tout à coup, nos modèles ne partagent plus parfaitement les champs de données. Tout objet `Bicycle` n'aura pas d'attribut `horsepower`, et tout `Car` ou `Motorcycle` n'aura pas de `bicycle_type` (espérons-le — j'y viendrai dans un instant).

Pourtant, chaque vélo de notre table aura un champ `horsepower`, et chaque voiture et moto aura un champ `bicycle_type`.

C'est là que les choses peuvent devenir compliquées. Plusieurs problèmes peuvent survenir dans cette situation :

1. Notre table aura beaucoup de valeurs nulles (`nil` dans le cas de Ruby) puisque les objets auront des champs qui ne leur sont pas applicables. Ces `nulls` peuvent causer des problèmes lorsque nous ajoutons des validations à nos modèles.
2. À mesure que la table grandit, nous pouvons rencontrer des coûts de performance lors de la requête si nous n'ajoutons pas de filtres. Une recherche pour un certain `bicycle_type` examinera **chaque élément** de la table — donc non seulement les `Bicycles`, mais aussi les `Cars` et `Motorcycles`.
3. Tel quel, rien n'empêche un utilisateur d'ajouter des données "inappropriées" au mauvais modèle. Par exemple, un utilisateur avec quelques connaissances pourrait créer un `Bicycle` avec une `horsepower` de 100. Nous aurions besoin de validations et d'une bonne conception d'application pour empêcher la création d'un objet invalide.

Ainsi, comme nous pouvons le voir, STI a quelques défauts. Il est idéal pour les applications où vos modèles partagent des champs de données et ne sont pas susceptibles de changer.

**AVANTAGES DE STI :**

* Simple à implémenter
* DRY — économise du code dupliqué en utilisant l'héritage et les attributs partagés
* Permet aux sous-classes d'avoir leur propre comportement si nécessaire

**INCONVÉNIENTS DE STI :**

* Ne s'adapte pas bien : à mesure que les données augmentent, la table peut devenir grande et éventuellement difficile à maintenir/interroger
* Nécessite des soins lors de l'ajout de nouveaux modèles ou de champs de modèle qui s'écartent des champs partagés
* (conditionnel) Permet la création d'objets invalides si les validations ne sont pas en place
* (conditionnel) Peut être difficile à valider ou à interroger si de nombreuses valeurs nulles existent dans la table

### Associations Polymorphiques

Avec les associations polymorphiques, un modèle peut `appartenir_a` plusieurs modèles avec une seule association.

![Image](https://cdn-media-1.freecodecamp.org/images/YgakgeaPyCa0SWLFcxPmUERwET59Js3Jr9tI)
_C'est l'heure de la morphose. ([source](https://www.flickr.com/photos/bagogames/14916041475" rel="noopener" target="_blank" title="))_

Cela est utile lorsque plusieurs modèles n'ont pas de relation ou ne partagent pas de données entre eux, mais ont une relation avec la classe polymorphique.

Par exemple, pensons à un site de médias sociaux comme Facebook. Sur Facebook, les individus et les groupes peuvent partager des publications.

Les individus et les groupes ne sont pas liés (autre que le fait d'être tous deux un type d'utilisateur), et ont donc des données différentes. Un groupe a probablement des champs comme `member_count` et `group_type` qui ne s'appliquent pas à un individu, et vice-versa).

Sans associations polymorphiques, nous aurions quelque chose comme ceci :

```
class Post
  belongs_to :person
  belongs_to :group
end
```

```
class Person
  has_many :posts
end
```

```
class Group
  has_many :posts
end
```

Normalement, pour savoir qui possède un certain profil, nous regardons la colonne qui est la `foreign_key`. Une `foreign_key` est un identifiant utilisé pour trouver l'objet lié dans la table du modèle lié.

Cependant, notre table Posts aurait deux clés étrangères en compétition : `group_id` et `person_id`. Cela poserait problème.

Lorsque nous essayons de trouver le propriétaire d'une publication, nous devrions faire un point pour vérifier les deux colonnes afin de trouver la bonne foreign_key, plutôt que de nous fier à une seule. Que se passe-t-il si nous rencontrons une situation où les deux colonnes ont une valeur ?

Une association polymorphique résout ce problème en condensant cette fonctionnalité en une seule association. Nous pouvons représenter nos classes comme ceci :

```
class Post
  belongs_to :postable, polymorphic: true
end
```

```
class Person
  has_many :posts, as: :postable
end
```

```
class Group
  has_many :posts, as: :postable
end
```

La convention Rails pour nommer une association polymorphique utilise « -able » avec le nom de la classe (`:postable` pour la classe `Post`). Cela rend clair dans vos relations quelle classe est polymorphique. Mais vous pouvez utiliser n'importe quel nom pour votre association polymorphique que vous aimez.

Pour indiquer à notre base de données que nous utilisons une association polymorphique, nous utilisons des colonnes spéciales « type » et « id » pour la classe polymorphique.

La colonne `postable_type` enregistre à quel modèle la publication appartient, tandis que la colonne `postable_id` suit l'id de l'objet propriétaire :

```
haley = Person.first
=> returns Person object with name: "Haley"
```

```
article = haley.posts.first
article.postable_type
=> "Person"
```

```
article.postable_id
=> 1 # L'objet qui possède ceci a un id de 1 (dans ce cas une Person)
```

```
new_post = haley.posts.new()
# Remplit automatiquement postable_type et postable_id en utilisant l'objet haley
```

Une association polymorphique est simplement une combinaison de deux ou plusieurs associations belongs_to. Grâce à cela, vous pouvez agir de la même manière que lorsque vous utilisez deux modèles qui ont une association belongs_to.

Note : les associations polymorphiques fonctionnent avec les associations has_one et has_many.

```
haley.posts
# returns ActiveRecord array of posts
```

```
haley.posts.first.content
=> "The content from my first post was a string..."
```

Une différence est d'aller « en arrière » d'une publication pour accéder à son propriétaire, puisque son propriétaire pourrait provenir de l'une des plusieurs classes.

Pour le faire rapidement, vous devez [ajouter une colonne de clé étrangère et une colonne de type à la classe polymorphique](http://guides.rubyonrails.org/association_basics.html#polymorphic-associations). Vous pouvez trouver le propriétaire d'une publication en utilisant `postable` :

```
new_post.postable
=> returns Person object
```

```
new_post.postable.name
=> "Haley"
```

De plus, Rails implémente une certaine sécurité au sein des relations polymorphiques. Seules les classes qui font partie de la relation peuvent être incluses comme `postable_type` :

```
new_post.update(postable_type: "FakeClass")
=> NameError: uninitialized constant FakeClass
```

#### Avertissement

Les associations polymorphiques comportent un énorme drapeau rouge : **l'intégrité des données compromise**.

![Image](https://cdn-media-1.freecodecamp.org/images/muZSd9uTpviItuoWh7aR83AVSRZJahsE6AjG)
_Par Scott Adams de [http://dilbert.com/](http://dilbert.com/" rel="noopener" target="_blank" title=")_

Dans une relation belongs_to normale, nous utilisons des clés étrangères pour la référence dans une association.

Elles ont plus de pouvoir que de simplement former un lien, cependant. Les clés étrangères empêchent également les erreurs de référence en exigeant que l'objet référencé dans la table étrangère existe, en fait.

Si quelqu'un essaie de créer un objet avec une clé étrangère qui référence un objet null, il obtiendra une erreur.

Malheureusement, les classes polymorphiques ne peuvent pas avoir de clés étrangères pour les [raisons que nous avons discutées](https://medium.com/p/af3a07a204f2#6a54). Nous utilisons les colonnes `type` et `id` à la place d'une clé étrangère. Cela signifie que nous perdons la protection que les clés étrangères offrent.

Rails et ActiveRecord nous aident en surface, mais toute personne ayant un accès direct à la base de données peut créer ou mettre à jour des objets qui référencent des objets null.

Par exemple, consultez cette commande SQL où une publication est créée même si le groupe auquel elle est associée n'existe pas.

```
Group.find(1000)
=> ActiveRecord::RecordNotFound: Couldn't find Group with 'id'=1000
```

```
# SQL
INSERT INTO POSTS (postable_type, postable_id) VALUES ('Group', 1000)
=> # returns success even though the associated Group doesn't exist
```

Heureusement, une configuration appropriée de l'application peut empêcher cela d'être possible. Parce que c'est un problème sérieux, vous ne devriez utiliser des associations polymorphiques que lorsque votre base de données est contenue. Si d'autres applications ou bases de données doivent y accéder, vous devriez envisager d'autres méthodes.

**AVANTAGES DES ASSOCIATIONS POLYMORPHIQUES :**

* Facile à mettre à l'échelle en quantité de données : les informations sont réparties sur plusieurs tables de base de données pour minimiser le gonflement de la table
* Facile à mettre à l'échelle le nombre de modèles : plus de modèles peuvent être facilement associés à la classe polymorphique
* DRY : crée une classe qui peut être utilisée par de nombreuses autres classes

**INCONVÉNIENTS DES ASSOCIATIONS POLYMORPHIQUES**

* Plus de tables peuvent rendre les requêtes plus difficiles et coûteuses à mesure que les données augmentent. (Trouver toutes les publications créées dans un certain laps de temps devrait scanner toutes les tables associées)
* Ne peut pas avoir de clé étrangère. La colonne `id` peut référencer l'une des tables de modèles associées, ce qui peut ralentir les requêtes. Elle doit fonctionner en conjonction avec la colonne `type`.
* Si vos tables sont très grandes, beaucoup d'espace est utilisé pour stocker les valeurs de chaîne pour `postable_type`
* Votre intégrité des données est compromise.

### Comment savoir quelle méthode utiliser

STI et les associations polymorphiques ont un certain chevauchement en ce qui concerne les cas d'utilisation. Bien que ce ne soient pas les seules solutions à une relation de modèle "en arbre", elles ont toutes deux des avantages évidents.

Les exemples `Vehicle` et `Postable` auraient pu être implémentés en utilisant l'une ou l'autre méthode. Cependant, il y avait quelques raisons qui ont rendu clair quelle méthode était la meilleure dans chaque situation.

Voici quatre facteurs à considérer lorsque vous décidez si l'une de ces méthodes correspond à vos besoins.

1. **Structure de la base de données.** STI utilise une seule table pour toutes les classes dans la relation, tandis que les associations polymorphiques utilisent une table par classe. Chaque méthode a ses propres avantages et inconvénients à mesure que l'application grandit.
2. **Données ou état partagé.** STI est une excellente option si vos modèles ont de nombreux attributs partagés. Sinon, une association polymorphique est probablement le meilleur choix.
3. **Préoccupations futures.** Considérez comment votre application pourrait changer et grandir. Si vous envisagez STI mais pensez que vous ajouterez des modèles ou des champs de modèle qui s'écartent de la structure partagée, vous pourriez vouloir reconsidérer votre plan. Si vous pensez que votre structure est susceptible de rester la même, STI sera _généralement_ plus rapide pour les requêtes.
4. **Intégrité des données.** Si les données ne seront pas contenues (une application utilisant votre base de données), l'association polymorphique est probablement un mauvais choix car vos données seront compromises.

### **Réflexions finales**

Ni STI ni les associations polymorphiques ne sont parfaites. Elles ont toutes deux des avantages et des inconvénients qui rendent souvent l'une ou l'autre plus adaptée aux associations avec de nombreux modèles.

J'ai écrit cet article pour m'enseigner ces concepts autant que pour les enseigner à quelqu'un d'autre. Si quelque chose est incorrect ou si vous pensez que certains points devraient être mentionnés, aidez-moi et tout le monde en partageant dans les commentaires !

**Si vous avez appris quelque chose ou trouvé cela utile, veuillez cliquer sur le bouton** ? **pour montrer votre soutien !**