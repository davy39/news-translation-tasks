---
title: Une introduction à la programmation orientée objet avec Ruby
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-26T22:49:30.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-object-oriented-programming-with-ruby-d594e1c6eebe
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yk9cvq3T5pHUsObH3XiA1Q.png
tags:
- name: learning to code
  slug: learning-to-code
- name: object oriented
  slug: object-oriented
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: 'tech '
  slug: tech
seo_title: Une introduction à la programmation orientée objet avec Ruby
seo_desc: 'By Saul Costa

  Object-oriented programming (OOP) is a programming paradigm organized around objects.
  At a high level, OOP is all about being able to structure code so that its functionality
  can be shared throughout the application. If done properly, O...'
---

Par Saul Costa

La **programmation orientée objet** (**POO**) est un paradigme de programmation organisé autour d'objets. À un niveau élevé, la POO consiste à structurer le code de manière à ce que sa fonctionnalité puisse être partagée dans toute l'application. Si elle est bien faite, la POO peut conduire à des programmes très élégamment écrits avec un minimum de duplication de code.

Cela s'oppose à la programmation procédurale (PP), dans laquelle vous construisez des programmes dans un ordre séquentiel et appelez des méthodes lorsque vous voulez un comportement partagé entre les pages de l'application. Les langages de programmation procédurale courants incluent [C](https://en.wikipedia.org/wiki/C_(programming_language)) et [Go](https://en.wikipedia.org/wiki/Go_(programming_language)).

Dans ce tutoriel, vous apprendrez les concepts fondamentaux de la POO pour **Ruby**, un langage de programmation orienté objet dans lequel tout est un objet. Nous utiliserons Ruby puisque l'un de ses attributs définissants — en plus de sa syntaxe élégante et de sa lisibilité — est la manière dont il implémente les techniques de POO. Cela en fait un excellent langage pour commencer à apprendre la POO.

Nous aborderons :

* La création de classes
* L'instanciation d'objets
* L'initialisation des arguments
* Le travail avec l'héritage, et
* Les méthodes privées et publiques.

En apprenant ces concepts, nous construirons notre propre application : un connecteur d'API qui communique dynamiquement avec une application qui envoie un message texte. Cela inclura une démonstration de la manière d'utiliser des concepts tels que l'héritage et l'instanciation d'objets pour rendre notre code plus évolutif et réutilisable !

_Ce bref tutoriel est adapté du cours [Introduction à Ruby](https://c.next.tech/2EyLhYk) de Next Tech, qui inclut un environnement sandboxé dans le navigateur et des tâches interactives auto-vérifiées à compléter._

_Vous pouvez suivre les extraits de code de ce tutoriel en utilisant le sandbox de Next Tech qui a déjà Ruby préinstallé. Si vous choisissez d'utiliser votre propre IDE, assurez-vous que Ruby est installé en suivant les instructions sur la [page d'installation](https://www.ruby-lang.org/en/documentation/installation/)._

### Création de classes

Avant de commencer, définissons ce qu'est un **objet**. À sa base, un objet est un morceau de code autonome qui contient des données (« attributs ») et des comportements (« méthodes ») et peut communiquer avec d'autres objets. Les objets du même type sont créés à partir de **classes**, qui agissent comme des plans définissant les propriétés et les comportements.

Créer une classe en Ruby est assez facile. Pour définir une classe, il suffit de taper le mot `class` suivi du nom de la classe, et de la terminer par le mot `end`. Tout ce qui est contenu entre `class` et `end` appartient à cette classe.

Les noms de classes en Ruby ont une exigence de style très spécifique. Ils doivent commencer par une lettre et, s'ils représentent plusieurs mots, chaque nouveau mot doit également être une lettre majuscule — c'est-à-dire en « CamelCase ».

Nous commencerons par créer une classe appelée `ApiConnector` :

Les classes en Ruby peuvent stocker à la fois des données et des méthodes. Dans de nombreux langages OOP traditionnels comme Java, vous devez créer deux méthodes pour chaque élément de données que vous souhaitez inclure dans la classe. Une méthode, le **setter**, définit la valeur dans la classe. L'autre méthode, le **getter**, vous permet de récupérer la valeur.

Le processus de création de méthodes setter et getter pour chaque attribut de données peut être fastidieux et conduit à des définitions de classe incroyablement longues. Heureusement, Ruby dispose d'un ensemble d'outils appelés **accesseurs d'attributs**.

Implémentons quelques setters et getters pour de nouveaux éléments de données pour notre classe. Puisqu'il s'agit d'un connecteur d'API, il serait logique d'avoir des éléments de données tels que `title`, `description` et `url`. Nous pouvons ajouter ces éléments avec le code suivant :

Lorsque vous créez simplement une classe, elle ne fait rien — il s'agit simplement d'une définition. Pour travailler avec la classe, nous devons créer une instance de celle-ci… nous aborderons cela ensuite !

### Instanciation

Pour comprendre ce qu'est l'**instanciation**, considérons une analogie du monde réel. Imaginons que vous construisez une maison. La première tâche consiste à créer un plan pour la maison. Ce plan contiendrait les attributs et les caractéristiques de la maison, tels que les dimensions de chaque pièce, le flux de la plomberie, etc.

Le plan de la maison est-il la maison réelle ? Bien sûr que non, il liste simplement les attributs et les éléments de conception pour la création de la maison. Ainsi, après que le plan est terminé, la maison réelle peut être construite — ou, « instanciée ».

Comme expliqué dans la section précédente, en POO, une classe est le plan d'un objet. Elle décrit simplement à quoi ressemblera un objet et comment il se comportera. Par conséquent, l'instanciation est le processus de prise d'une définition de classe et de création d'un objet que vous pouvez utiliser dans un programme.

Créons une nouvelle instance de notre classe `ApiConnector` et stockons-la dans une variable appelée `api` :

Maintenant que nous avons créé un objet, nous pouvons utiliser la variable `api` pour travailler avec les attributs de la classe. Par exemple, nous pouvons exécuter le code :

```
[Out:]https://next.tech
```

En plus de créer des attributs, vous pouvez également créer des méthodes au sein d'une classe :

Pour accéder à cette méthode, nous pouvons utiliser la même syntaxe que celle utilisée avec les accesseurs d'attributs :

En mettant tout cela ensemble, l'exécution du code complet de la classe ci-dessous donnera comme résultat l'`url` et le message de la `test_method` imprimés :

```
[Out:]"https://next.tech""testing class call"
```

### Méthode d'initialisation

Une chose que vous pourriez trouver utile dans le développement Ruby est la capacité à créer une méthode **d'initialisation**. Il s'agit simplement d'une méthode appelée `initialize` qui s'exécutera chaque fois que vous créerez une instance de votre classe. Dans cette méthode, vous pouvez donner des valeurs à vos variables, appeler d'autres méthodes, et faire à peu près tout ce que vous pensez devoir se produire lorsqu'une nouvelle instance de cette classe est créée.

Mettons à jour notre `ApiConnector` pour utiliser une méthode d'initialisation :

Dans la méthode `initialize`, nous avons créé une variable d'instance pour chacun des paramètres afin de pouvoir utiliser ces variables dans d'autres parties de l'application également.

Nous avons également supprimé la méthode `attr_accessor` puisque la nouvelle méthode `initialize` s'en chargera pour nous. Si vous avez besoin de la capacité à appeler les éléments de données en dehors de la classe, vous devrez toujours avoir l'appel `attr_accessor` en place.

Pour tester si la méthode `initialize` fonctionne, créons une autre méthode dans la classe qui imprime ces valeurs :

Enfin, nous instancierons la classe et testerons la méthode d'initialisation :

```
[Out:]"My title""My cool description""https://next.tech"
```

#### Travailler avec des valeurs optionnelles

Maintenant, que se passe-t-il lorsque nous voulons rendre l'une de ces valeurs optionnelle ? Par exemple, que se passe-t-il si nous voulons donner une valeur par défaut à l'URL ? Pour cela, nous pouvons mettre à jour notre méthode `initialize` avec la syntaxe suivante :

Maintenant, notre programme aura la même sortie même si nous ne passons pas la valeur `url` lors de la création d'une nouvelle instance de la classe :

#### Utilisation d'arguments nommés

Bien que cela semble simple, le passage d'arguments peut devenir complexe dans les applications Ruby du monde réel car certaines méthodes peuvent prendre un grand nombre d'arguments. Dans de tels cas, il devient difficile de connaître l'ordre des arguments et les valeurs à leur attribuer.

Pour éviter cette confusion, vous pouvez utiliser des arguments nommés, comme ceci :

Vous pouvez entrer les arguments sans avoir à regarder l'ordre dans la méthode `initialize`, et même changer l'ordre des arguments sans causer d'erreur :

#### Remplacement des valeurs par défaut

Que se passe-t-il si nous voulons remplacer une valeur par défaut ? Nous mettons simplement à jour notre appel d'instanciation comme ceci :

Cette mise à jour remplacera notre valeur par défaut de `https://next.tech`, et l'appel de `api.testing_initializer` imprimera maintenant `https://next.xyz` comme URL.

### Héritage

Maintenant, nous allons apprendre un principe important de l'orienté objet appelé **héritage**. Avant d'aborder comment il est exécuté en Ruby, voyons pourquoi il est important pour la construction d'applications.

Pour commencer, l'héritage signifie que vos classes peuvent avoir une hiérarchie. Il est préférable de l'utiliser lorsque différentes classes ont certaines responsabilités partagées, car il serait mauvais de dupliquer le code dans chaque classe pour un comportement identique ou même similaire.

Prenons notre classe `ApiConnector`. Supposons que nous avons différentes classes d'API pour diverses plateformes, mais que chaque classe partage un certain nombre de données ou de processus communs. Au lieu de dupliquer le code dans chacune des classes de connecteur d'API, nous pouvons avoir une **classe parente** avec les données et méthodes partagées. À partir de là, nous pouvons créer des **classes enfants** à partir de cette classe parente. Avec le fonctionnement de l'héritage, chacune des classes enfants aura accès aux composants fournis par la classe parente.

Par exemple, disons que nous avons trois API : `SmsConnector`, `PhoneConnector` et `MailerConnector`. Si nous écrivions du code individuellement pour chacune de ces classes, cela ressemblerait à ceci :

Comme vous pouvez le voir, nous répétons simplement le même code dans différentes classes. Cela est considéré comme une mauvaise pratique de programmation qui viole le principe [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) (Ne vous répétez pas) du développement. Au lieu de cela, nous pouvons faire une classe parente `ApiConnector`, et chacune des autres classes peut hériter de la fonctionnalité commune de cette classe :

En tirant parti de l'héritage, nous avons pu supprimer tout le code dupliqué dans nos classes.

La syntaxe pour utiliser l'héritage est de définir le nom de la classe enfant, suivi du symbole `<`, puis le nom de la classe parente — c'est-à-dire que nos classes `SmsConnector`, `MailerConnector` et `PhoneConnector` héritent de la classe `ApiConnector`.

Chacune de ces classes enfants a maintenant accès à l'ensemble complet d'éléments fournis dans la classe parente `ApiConnector`. Par exemple, si nous créons une nouvelle instance de `SmsConnector` avec les paramètres suivants, nous pouvons appeler la méthode `send_sms` :

```
[Out:]Envoi d'un message SMS avec le titre 'Hi there!' et la description 'I'm an SMS message'.
```

Une règle de base en POO est de s'assurer qu'une classe effectue une seule responsabilité. Par exemple, la classe `ApiConnector` ne doit pas envoyer de messages SMS, passer des appels téléphoniques ou envoyer des e-mails, car cela serait trois responsabilités principales.

### Méthodes privées et publiques

Avant de plonger dans les méthodes privées et publiques, revenons d'abord à notre classe `ApiConnector` d'origine et créons une classe `SmsConnector` qui hérite de `ApiConnector`. Dans cette classe, nous créerons une méthode appelée `send_sms` qui exécutera un script qui contacte une API :

Cette méthode enverra un `title` et un `url` à une API, qui enverra à son tour un message SMS. Maintenant, nous pouvons instancier la classe `SmsConnector` et appeler le message `send_sms` :

L'exécution de ce code contactera l'API SMS et enverra le message. Vous pouvez aller en bas de [cette page](http://edutechional-smsy.herokuapp.com/notifications) pour voir votre message !

Maintenant, en utilisant cet exemple, discutons des types de méthodes fournies par les classes.

La méthode `send_sms` est une **méthode publique**. Cela signifie que toute personne travaillant sur notre classe peut communiquer avec cette méthode. Cela peut ne pas sembler important si vous travaillez sur une application sur laquelle personne d'autre ne travaille. Cependant, si vous construisez une API ou une bibliothèque de code open source pour que d'autres l'utilisent, il est vital que vos méthodes publiques représentent des éléments de fonctionnalité que vous voulez réellement que d'autres développeurs utilisent.

Les méthodes publiques ne doivent rarement, voire jamais, être modifiées. Cela est dû au fait que d'autres développeurs peuvent dépendre de vos méthodes publiques pour être cohérentes, et une modification d'une méthode publique peut casser des composants de leurs programmes.

Alors, si vous ne pouvez pas changer les méthodes publiques, comment pouvez-vous travailler sur une application en production ? C'est là que les **méthodes privées** interviennent. Une méthode privée est une méthode qui n'est accessible que par la classe qui la contient. Elle ne doit jamais être appelée par des services externes. Cela signifie que vous pouvez modifier leur comportement, à condition que ces changements n'aient pas un effet domino et ne modifient pas les méthodes publiques à partir desquelles elles peuvent être appelées.

Habituellement, les méthodes privées sont placées à la fin du fichier après toutes les méthodes publiques. Pour désigner les méthodes privées, nous utilisons le mot `private` au-dessus de la liste des méthodes. Ajoutons une méthode privée à notre classe `ApiConnector` :

Remarquez comment nous appelons cette méthode depuis l'intérieur de la méthode `initialize` de la classe `ApiConnector` ? Si nous exécutons ce code, il donnera la sortie suivante :

```
[Out:]Un message secret de la classe parente
```

Maintenant, les classes enfants ont accès aux méthodes de la classe parente, n'est-ce pas ? Eh bien, pas toujours. Retirons la méthode `secret_method` de la méthode `initialize` dans `ApiConnector` et essayons de l'appeler depuis notre classe enfant `SmsConnector`, comme montré ici :

```
[Out:]Traceback (most recent call last):main.rb:29:in `<main>': private method `secret_method' called for #SmsConnector:0x000056188cfe19b0> (NoMethodError)
```

Cela est dû au fait que la classe `SmsConnector` n'a accès qu'aux méthodes publiques de la classe parente. Les méthodes privées sont, par leur nature, privées. Cela signifie qu'elles ne peuvent être accessibles que par la classe dans laquelle elles sont définies.

Une bonne règle de base est donc de créer des méthodes privées lorsqu'elles ne doivent pas être utilisées en dehors de la classe et des méthodes publiques lorsqu'elles doivent être disponibles dans toute l'application ou utilisées par des services externes.

#### Conclusion

J'espère que vous avez apprécié ce rapide tutoriel sur les concepts fondamentaux de la programmation orientée objet en Ruby ! Nous avons couvert la création de classes, les accesseurs d'attributs, l'instanciation, l'initialisation, l'héritage, et les méthodes privées et publiques.

Ruby est un langage orienté objet puissant utilisé par des applications populaires, y compris la nôtre ici chez Next Tech. Avec cette connaissance fondamentale de la POO, vous êtes bien parti pour développer vos propres applications Ruby !

_Si vous êtes intéressé à en apprendre davantage sur la programmation avec Ruby, consultez notre cours Introduction à Ruby [ici](https://c.next.tech/2EyLhYk) ! Dans ce cours, nous couvrons les compétences de programmation de base, telles que les variables, les chaînes de caractères, les boucles et les conditionnelles, des sujets OOP plus avancés, et la gestion des erreurs._