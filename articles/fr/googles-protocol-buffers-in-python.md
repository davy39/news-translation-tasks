---
title: Comment utiliser les Protocol Buffers de Google en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-12T11:52:44.000Z'
originalURL: https://freecodecamp.org/news/googles-protocol-buffers-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/unnamed-1.png
tags:
- name: protocol-buffers
  slug: protocol-buffers
- name: Python
  slug: python
seo_title: Comment utiliser les Protocol Buffers de Google en Python
seo_desc: "By Tim Grossmann\nWhen people who speak different languages get together\
  \ and talk, they try to use a language that everyone in the group understands. \n\
  To achieve this, everyone has to translate their thoughts, which are usually in\
  \ their native languag..."
---

Par Tim Grossmann

Lorsque des personnes parlant différentes langues se réunissent et discutent, elles essaient d'utiliser une langue que tout le monde dans le groupe comprend. 

Pour y parvenir, chacun doit traduire ses pensées, généralement dans sa langue maternelle, dans la langue du groupe. Ce processus d'« encodage et décodage » de la langue entraîne cependant une perte d'efficacité, de vitesse et de précision.  
  
Le même concept est présent dans les systèmes informatiques et leurs composants. Pourquoi devrions-nous envoyer des données en XML, JSON ou tout autre format lisible par l'homme s'il n'est pas nécessaire que nous comprenions directement ce dont ils parlent ? Tant que nous pouvons encore les traduire dans un format lisible par l'homme si nécessaire.  
  
Les Protocol Buffers sont un moyen d'encoder les données avant leur transport, ce qui réduit efficacement les blocs de données et augmente donc la vitesse lors de leur envoi. Ils abstraient les données dans un format neutre en termes de langage et de plateforme.

### Table des matières

* [Pourquoi avons-nous besoin des Protocol Buffers ?](#heading-pourquoi-protocol-buffers)
* [Qu'est-ce que les Protocol Buffers et comment fonctionnent-ils ?](#heading-quest-ce-que-protocol-buffers-et-comment-fonctionnent-ils)
* [Protocol Buffers en Python](#heading-python-et-protocol-buffers)
* [Remarques finales](#heading-remarques-finales)

## Pourquoi les Protocol Buffers ?

L'objectif initial des Protocol Buffers était de simplifier le travail avec les protocoles de requête/réponse. Avant ProtoBuf, Google utilisait un format différent qui nécessitait une gestion supplémentaire du [marshaling](https://en.wikipedia.org/wiki/Marshalling_(computer_science)) pour les messages envoyés. 

En outre, les nouvelles versions de l'ancien format exigeaient que les développeurs s'assurent que les nouvelles versions soient comprises avant de remplacer les anciennes, ce qui rendait le travail avec celles-ci fastidieux.

Cette surcharge a motivé Google à concevoir une interface qui résout précisément ces problèmes. 

ProtoBuf permet d'introduire des modifications dans le protocole sans rompre la compatibilité. De plus, les serveurs peuvent transmettre les données et exécuter des opérations de lecture sur les données sans modifier leur contenu.

Étant donné que le format est en partie auto-descriptif, ProtoBuf est utilisé comme base pour la génération automatique de code pour les sérialiseurs et désérialiseurs.

Un autre cas d'utilisation intéressant est la manière dont Google l'utilise pour les appels de procédure à distance (RPC) de courte durée et pour stocker des données de manière persistante dans Bigtable. En raison de leur cas d'utilisation spécifique, ils ont intégré des interfaces RPC dans ProtoBuf. Cela permet une génération rapide et simple de squelettes de code qui peuvent être utilisés comme points de départ pour l'implémentation réelle. (Plus d'informations sur [ProtoBuf RPC](https://medium.com/@EmperorRXF/evaluating-performance-of-rest-vs-grpc-1b8bdf0b22da)).

D'autres exemples où ProtoBuf peut être utile sont les appareils IoT connectés via des réseaux mobiles où la quantité de données envoyées doit être maintenue faible, ou pour des applications dans des pays où les haut débits sont encore rares. L'envoi de charges utiles dans des formats binaires optimisés peut entraîner des différences notables en termes de coût et de vitesse d'opération.

L'utilisation de la compression `gzip` dans votre communication HTTPS peut encore améliorer ces métriques.

## Qu'est-ce que les Protocol Buffers et comment fonctionnent-ils ?

De manière générale, les Protocol Buffers sont une interface définie pour la sérialisation de données structurées. Ils définissent une manière normalisée de communiquer, totalement indépendante des langages et des plateformes.

Google présente son ProtoBuf [comme ceci](https://developers.google.com/protocol-buffers) :

> _Les Protocol Buffers sont le mécanisme neutre en termes de langage, de plateforme et extensible de Google pour la sérialisation de données structurées - pensez XML, mais plus petit, plus rapide et plus simple. Vous définissez une fois comment vous voulez que vos données soient structurées..._

L'interface ProtoBuf décrit la structure des données à envoyer. Les structures de charge utile sont définies comme des « messages » dans ce qu'on appelle les fichiers Proto. Ces fichiers se terminent toujours par une extension `.proto`.  
  
Par exemple, la structure de base d'un fichier **todolist.proto** ressemble à ceci. Nous examinerons également un exemple complet dans la section suivante.

```javascript
syntax = "proto3";

// Pas nécessaire pour Python, doit encore être déclaré pour éviter les collisions de noms 
// dans l'espace de noms des Protocol Buffers et les langages non-Python
package protoblog;

message TodoList {
   // Les éléments de la liste de tâches seront définis ici
   ...
}
```

Ces fichiers sont ensuite utilisés pour générer des classes d'intégration ou des squelettes pour le langage de votre choix en utilisant des générateurs de code dans le compilateur protoc. La version actuelle, Proto3, prend déjà en charge tous les principaux langages de programmation. La communauté en prend en charge beaucoup d'autres dans des implémentations open-source tierces.

Les classes générées sont les éléments centraux des Protocol Buffers. Elles permettent la création d'éléments en instanciant de nouveaux messages, basés sur les fichiers `.proto`, qui sont ensuite utilisés pour la sérialisation. Nous verrons comment cela est fait avec Python en détail dans la section suivante.

Indépendamment du langage de sérialisation, les messages sont sérialisés dans un format binaire non auto-descriptif qui est assez inutile sans la définition de structure initiale.

Les données binaires peuvent ensuite être stockées, envoyées sur le réseau et utilisées de toute autre manière comme les données lisibles par l'homme telles que JSON ou XML. Après transmission ou stockage, le flux d'octets peut être désérialisé et restauré en utilisant **n'importe quelle** classe protobuf spécifique au langage, compilée que nous générons à partir du fichier .proto.  
  
En prenant Python comme exemple, le processus pourrait ressembler à ceci :

![Image](https://lh4.googleusercontent.com/1cHvUkBU5WKklD0ErnHpdVIdal-SBh5wfLQr5n-75jE6mj62ScOZ7mTc-AZLu9LBeYRaKxLim0OWQi4GNKgmYHFtd-AVQjlE6pX2O3j7wa-9wX69JkcetgQt5fAHqM1gNCGo-iv8)

Tout d'abord, nous créons une nouvelle liste de tâches et la remplissons avec quelques tâches. Cette liste de tâches est ensuite sérialisée et envoyée sur le réseau, enregistrée dans un fichier ou stockée de manière persistante dans une base de données.

Le flux d'octets envoyé est désérialisé en utilisant la méthode parse de notre classe compilée spécifique au langage.  
  
La plupart des architectures et infrastructures actuelles, en particulier les microservices, sont basées sur la communication REST, WebSockets ou GraphQL. Cependant, lorsque la vitesse et l'efficacité sont essentielles, les RPC de bas niveau peuvent faire une grande différence.

Au lieu de protocoles à forte surcharge, nous pouvons utiliser un moyen rapide et compact pour déplacer des données entre les différentes entités de notre service sans gaspiller beaucoup de ressources. 

### **Mais pourquoi n'est-il pas encore utilisé partout ?**

Les Protocol Buffers sont un peu plus compliqués que d'autres formats lisibles par l'homme. Cela les rend comparativement plus difficiles à déboguer et à intégrer dans vos applications.

Les temps d'itération en ingénierie tendent également à augmenter puisque les mises à jour des données nécessitent la mise à jour des fichiers proto avant utilisation.

Des considérations attentives doivent être faites puisque ProtoBuf pourrait être une solution surdimensionnée dans de nombreux cas.

### Quelles alternatives ai-je ?

Plusieurs projets adoptent une approche similaire à celle des Protocol Buffers de Google.

[Les Flatbuffers de Google](https://google.github.io/flatbuffers/) et une implémentation tierce, appelée [Cap'n Proto](https://capnproto.org/), sont plus axés sur la suppression de l'étape d'analyse et de dépaquetage, qui est nécessaire pour accéder aux données réelles lors de l'utilisation de ProtoBufs. Ils ont été conçus explicitement pour les applications critiques en termes de performance, les rendant encore plus rapides et plus efficaces en mémoire que ProtoBuf.  
  
Lorsque l'on se concentre sur les capacités RPC de ProtoBuf (utilisées avec gRPC), il existe des projets d'autres grandes entreprises comme Facebook (Apache Thrift) ou Microsoft (Bond protocols) qui peuvent offrir des alternatives.

## Python et les Protocol Buffers

Python offre déjà quelques moyens de persistance des données en utilisant le pickling. Le pickling est utile dans les applications Python uniquement. Il n'est pas bien adapté aux scénarios plus complexes où le partage de données avec d'autres langages ou la modification de schémas est impliqué.  
  
Les Protocol Buffers, en revanche, sont développés précisément pour ces scénarios.  
Les fichiers `.proto`, que nous avons rapidement abordés précédemment, permettent à l'utilisateur de générer du code pour de nombreux langages pris en charge.

Pour compiler le fichier `.proto` en classe de langage de notre choix, nous utilisons **protoc**, le compilateur proto.  
  
Si vous n'avez pas le compilateur protoc installé, il existe d'excellents guides sur la façon de le faire :

* [MacOS / Linux](http://google.github.io/proto-lens/installing-protoc.html)
* [Windows](https://github.com/protocolbuffers/protobuf/blob/master/src/README.md#c-installation---windows) 

Une fois que nous avons installé protoc sur notre système, nous pouvons utiliser un exemple étendu de notre structure de liste de tâches précédente et générer la classe d'intégration Python à partir de celle-ci.

```javascript
syntax = "proto3";

// Pas nécessaire pour Python mais doit encore être déclaré pour éviter les collisions de noms 
// dans l'espace de noms des Protocol Buffers et les langages non-Python
package protoblog;

// Le guide de style préfère préfixer les valeurs enum au lieu de les entourer
// avec un message englobant
enum TaskState {
    TASK_OPEN = 0;
    TASK_IN_PROGRESS = 1;
    TASK_POST_PONED = 2;
    TASK_CLOSED = 3;
    TASK_DONE = 4;
}

message TodoList {
    int32 owner_id = 1;
    string owner_name = 2;

    message ListItems {
        TaskState state = 1;
        string task = 2;
        string due_date = 3;
    }

    repeated ListItems todos = 3;
}

```

Examinons plus en détail la structure du fichier `.proto` pour mieux le comprendre.  
Dans la première ligne du fichier proto, nous définissons si nous utilisons Proto2 ou 3. Dans ce cas, nous utilisons [Proto3](https://developers.google.com/protocol-buffers/docs/proto3).

Les éléments les plus inhabituels des fichiers proto sont les nombres attribués à chaque entité d'un message. Ces nombres dédiés rendent chaque attribut unique et sont utilisés pour identifier les champs assignés dans la sortie encodée binaire. 

Un concept important à comprendre est que seules les valeurs 1-15 sont encodées avec un octet de moins (Hex), ce qui est utile à comprendre afin que nous puissions attribuer des nombres plus élevés aux entités moins fréquemment utilisées. Les nombres ne définissent **ni** **l'ordre** d'encodage **ni la position** de l'attribut donné dans le message encodé.

La définition du package aide à prévenir les conflits de noms. En Python, les packages sont définis par leur répertoire. Par conséquent, fournir un attribut de package n'a aucun effet sur le code Python généré. 

Veuillez noter que cela doit encore être déclaré pour éviter les collisions de noms liées aux Protocol Buffers et pour d'autres langages comme Java.

Les énumérations sont des listes simples de valeurs possibles pour une variable donnée.  
Dans ce cas, nous définissons une énumération pour les états possibles de chaque tâche dans la liste de tâches.  
Nous verrons comment les utiliser un peu plus tard lorsque nous examinerons l'utilisation en Python.  
  
Comme nous pouvons le voir dans l'exemple, nous pouvons également imbriquer des messages dans des messages.  
Si nous voulons, par exemple, avoir une liste de tâches associée à une liste de tâches donnée, nous pouvons utiliser le mot-clé **repeated**, qui est comparable à des tableaux de taille dynamique.

Pour générer un code d'intégration utilisable, nous utilisons le compilateur proto qui compile un fichier .proto donné en classes d'intégration spécifiques au langage. Dans notre cas, nous utilisons l'argument **--python-out** pour générer du code spécifique à Python.

`protoc -I=. --python_out=. ./todolist.proto`

Dans le terminal, nous invoquons le compilateur de protocole avec trois paramètres :

1. **-I** : définit le répertoire où nous recherchons les dépendances (nous utilisons . qui est le répertoire courant)
2. **--python_out** : définit l'emplacement où nous voulons générer une classe d'intégration Python (nous utilisons à nouveau **.** qui est le répertoire courant)
3.  Le dernier **paramètre sans nom** définit le fichier .proto qui sera compilé (nous utilisons le fichier todolist.proto dans le répertoire courant)

![Image](https://lh6.googleusercontent.com/eZJUxepo7Ath2NalDKS75Aezx7DFnZlt0IuvfteCIczCgZBkBg2sgdoMVxr8FSiQf6u4gDkEDFcewGyrvqZqzoYUzdZnGi_WoU8-lXKamFrnGudnZy31pmQkt1LaLNCTWOTB3y3v)

  
Cela crée un nouveau fichier Python appelé <nom_du_fichier_proto>_pb2.py. Dans notre cas, il s'agit de todolist_pb2.py. En examinant de plus près ce fichier, nous ne pourrons pas comprendre grand-chose de sa structure immédiatement. 

Cela est dû au fait que le générateur ne produit pas d'éléments d'accès direct aux données, mais abstrait davantage la complexité en utilisant des [metaclasses](https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python) et des descripteurs pour chaque attribut. Ils décrivent comment une classe se comporte au lieu de chaque instance de cette classe.  
  
La partie la plus intéressante est comment utiliser ce code généré pour créer, construire et sérialiser des données. Une intégration simple faite avec notre classe récemment générée est visible dans ce qui suit :

```python
import todolist_pb2 as TodoList

my_list = TodoList.TodoList()
my_list.owner_id = 1234
my_list.owner_name = "Tim"

first_item = my_list.todos.add()
first_item.state = TodoList.TaskState.Value("TASK_DONE")
first_item.task = "Test ProtoBuf for Python"
first_item.due_date = "31.10.2019"

print(my_list)
```

Il crée simplement une nouvelle liste de tâches et y ajoute un élément. Nous imprimons ensuite l'élément de la liste de tâches lui-même et pouvons voir la version non binaire, non sérialisée des données que nous venons de définir dans notre script.

```json
owner_id: 1234
owner_name: "Tim"
todos {
  state: TASK_DONE
  task: "Test ProtoBuf for Python"
  due_date: "31.10.2019"
}
```

Chaque classe Protocol Buffer possède des méthodes pour lire et écrire des messages en utilisant un [encodage spécifique aux Protocol Buffers](https://developers.google.com/protocol-buffers/docs/encoding), qui encode les messages au format binaire.  
Ces deux méthodes sont `SerializeToString()` et `ParseFromString()`.

```python
import todolist_pb2 as TodoList

my_list = TodoList.TodoList()
my_list.owner_id = 1234

# ...

with open("./serializedFile", "wb") as fd:
    fd.write(my_list.SerializeToString())


my_list = TodoList.TodoList()
with open("./serializedFile", "rb") as fd:
    my_list.ParseFromString(fd.read())

print(my_list)
```

Dans l'exemple de code ci-dessus, nous écrivons la chaîne sérialisée d'octets dans un fichier en utilisant les indicateurs **wb**.

Puisque nous avons déjà écrit le fichier, nous pouvons relire le contenu et le parser en utilisant ParseFromString. ParseFromString appelle une nouvelle instance de notre classe sérialisée en utilisant les indicateurs **rb** et le parse.

Si nous sérialisons ce message et l'imprimons dans la console, nous obtenons la représentation en octets qui ressemble à ceci.

`b'\x08\xd2\t\x12\x03Tim\x1a(\x08\x04\x12\x18Test ProtoBuf for Python\x1a\n31.10.2019'`

Remarquez le b devant les guillemets. Cela indique que la chaîne suivante est composée d'octets en Python.

Si nous comparons directement cela avec, par exemple, XML, nous pouvons voir l'impact de la sérialisation ProtoBuf sur la taille.

```xml
<todolist>
	<owner_id>1234</owner_id>
	<owner_name>Tim</owner_name>
	<todos>
		<todo>
			<state>TASK_DONE</state>
			<task>Test ProtoBuf for Python</task>
			<due_date>31.10.2019</due_date>
		</todo>
	</todos>
</todolist>
```

La représentation JSON, non uglifiée, ressemblerait à ceci.

```json
{
	"todoList": {
		"ownerId": "1234",
		"ownerName": "Tim",
		"todos": [
			{
				"state": "TASK_DONE",
				"task": "Test ProtoBuf for Python",
				"dueDate": "31.10.2019"
			}
		] 
	}
}
```

En jugeant les différents formats uniquement par le nombre total d'octets utilisés, en ignorant la mémoire nécessaire pour la surcharge de formatage, nous pouvons bien sûr voir la différence.  
  
Mais en plus de la mémoire utilisée pour les données, nous avons également **12 octets supplémentaires dans ProtoBuf** pour le formatage des données sérialisées. En comparaison avec XML, nous avons **171 octets supplémentaires dans XML** pour le formatage des données sérialisées.

Sans schéma, nous avons besoin de **136 octets supplémentaires dans JSON** pour le formatage des données sérialisées**.**

Si nous parlons de plusieurs milliers de messages envoyés sur le réseau ou stockés sur disque, ProtoBuf peut faire une différence.

Cependant, il y a un piège. La plateforme Auth0.com a créé une comparaison extensive entre ProtoBuf et JSON. Elle montre que, lorsqu'ils sont compressés, la différence de taille entre les deux peut être marginale (seulement environ 9%).

Si vous êtes intéressé par les chiffres exacts, veuillez vous référer à l'[article complet](https://auth0.com/blog/beating-json-performance-with-protobuf/), qui donne une analyse détaillée de plusieurs facteurs comme la taille et la vitesse.

Une note intéressante est que chaque type de données a une valeur par défaut. Si les attributs ne sont pas assignés ou modifiés, ils conserveront les valeurs par défaut. Dans notre cas, si nous ne changeons pas l'état de TaskState d'un ListItem, il a l'état de « TASK_OPEN » par défaut. L'avantage significatif de cela est que les valeurs non définies ne sont pas sérialisées, économisant ainsi de l'espace supplémentaire.

Si nous, par exemple, changeons l'état de notre tâche de TASK_DONE à TASK_OPEN, il ne sera pas sérialisé.

```json
owner_id: 1234
owner_name: "Tim"
todos {
  task: "Test ProtoBuf for Python"
  due_date: "31.10.2019"
}
```

`b'\x08\xd2\t\x12\x03Tim\x1a&\x12\x18Test ProtoBuf for Python\x1a\n31.10.2019'`

## Remarques finales

Comme nous l'avons vu, les Protocol Buffers sont assez pratiques lorsqu'il s'agit de vitesse et d'efficacité lors de la manipulation de données. En raison de leur nature puissante, il peut falloir un certain temps pour s'habituer au système ProtoBuf, même si la syntaxe pour définir de nouveaux messages est simple. 

En guise de dernière remarque, je veux souligner qu'il y avait/il y a des discussions sur le fait de savoir si les Protocol Buffers sont « utiles » pour les applications régulières. Ils ont été développés spécifiquement pour les problèmes que Google avait en tête.  
  
Si vous avez des questions ou des commentaires, n'hésitez pas à me contacter sur les réseaux sociaux comme [twitter](https://twitter.com/timigrossmann) ou [email](mailto:contact.timgrossmann@gmail.com) :)