---
title: Apprendre la gestion d'état dans Flutter en construisant une application Todo
  simple
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-04-03T13:55:36.000Z'
originalURL: https://freecodecamp.org/news/learn-state-management-in-flutter
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Flutter-State-Management
seo_title: Apprendre la gestion d'état dans Flutter en construisant une application
  Todo simple
---

Todo-App---Banner.png
étiquettes:
- nom: Flutter
  slug: flutter
- nom: développement d'applications mobiles
  slug: developpement-applications-mobiles
- nom: 'Gestion d'état '
  slug: gestion-etat
seo_title: null
seo_desc: "La gestion d'état est un sujet complexe dans le développement d'applications mobiles. \
  \ Mais c'est aussi un sujet nécessaire qui joue un rôle majeur dans la construction d'applications mobiles dynamiques. \nSi vous maîtrisez la gestion d'état, vous serez en mesure de construire tout type d'application dynamique. ..."
---

La gestion d'état est un sujet complexe dans le développement d'applications mobiles. Mais c'est aussi un sujet nécessaire qui joue un rôle majeur dans la construction d'applications mobiles dynamiques. 

Si vous maîtrisez la gestion d'état, vous serez en mesure de construire tout type d'application dynamique. Cela est dû au fait que l'interface utilisateur qui est rendue sur l'appareil mobile sera déterminée par l'état des données que votre application contient à ce moment-là. C'est pourquoi il est crucial de maîtriser la gestion d'état dans le développement d'applications front-end. 

Dans cet article, nous allons apprendre la gestion d'état en construisant une application Todo dans Flutter. 

Tout d'abord, examinons quelques théories sur la gestion d'état avant de plonger dans le développement d'applications. 

## Qu'est-ce que l'état dans les applications Flutter ?

L'état définit l'interface utilisateur de votre application. En d'autres termes, l'interface utilisateur est construite par l'état actuel de l'application. 

Lorsque l'état d'une application Flutter change, cela déclenchera le redessin de l'interface utilisateur. Cela s'appelle l'UI déclarative, que Flutter utilise - alors que les applications mobiles natives (Android et iOS) sont construites avec une UI impérative, où l'interface utilisateur est définie plus tôt. 

## Types d'état

Il existe 2 types d'état. Ils sont :

1. État éphémère
2. État de l'application

### État éphémère

L'état éphémère est l'état qui est contenu dans un seul widget ou un écran/page d'une application. 

### État de l'application

L'état de l'application est l'état qui est partagé entre les sessions utilisateur et est utilisé dans de nombreuses parties de l'application. 

### Comment choisir l'état pour votre application

Il n'existe pas de règle unique quant à l'état à choisir. Cela dépend de votre cas d'utilisation. Il est souvent bon d'utiliser d'abord l'état éphémère, puis de refactoriser votre code à l'avenir si vous avez besoin d'utiliser l'état de l'application. 

## Ce que nous allons construire

Dans ce tutoriel, nous allons construire une application Todo. Cette application aura la fonctionnalité de créer un élément todo, de lister tous les éléments ajoutés, de mettre à jour un élément et de supprimer un élément. Voici un aperçu (capture d'écran) pour vous. 



![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-257.png)
_Application Todo_

## Développement de l'application

Mettons nos chaussures de développement et commençons à construire notre application. 

## Créer le projet

Voici les étapes super simples pour créer votre projet Flutter. Si vous voulez une explication détaillée, veuillez lire la section ["Comment créer le projet" dans le blog](https://www.freecodecamp.org/news/how-to-build-a-simple-login-app-with-flutter/) et revenez ici. 

1. Ouvrez votre VS Code
2. Appuyez sur "CTRL+SHIFT+P" (les utilisateurs Mac remplacent CTRL par CMD)
3. Tapez "Flutter"
4. Sélectionnez l'option "Flutter : Nouveau projet"
5. Sélectionnez "Application" dans la liste suivante
6. Sélectionnez le dossier pour créer votre projet dans la prochaine invite
7. Dans la dernière invite, entrez le nom de votre application et appuyez sur "Entrée"

C'est tout ! Notre application de base est prête. 

Sélectionnez l'appareil préféré pour exécuter votre application en bas à droite et appuyez sur "F5". Votre application s'exécutera sur votre appareil sélectionné. Vous devriez voir l'écran suivant en quelques secondes. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-258.png)
_Application de base Flutter_

## Temps de refactoriser le code

Nous avons une application de base Flutter. Par défaut, elle aura beaucoup d'éléments, alors refactorisons notre code. Nous travaillerons sur le fichier `main.dart` dans le dossier `lib/` pour construire cette application entière. 

### Initialiser Git

Initialisez Git en exécutant `git init` dans le dossier racine de votre dépôt. 

### Supprimer les commentaires

J'ai supprimé tous les commentaires dans le fichier `main.dart` et ajouté un commit. 

### Renommer les classes

Renommez `MyApp` en `TodoApp` dans la méthode principale en appuyant sur `F2` dans VS Code. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-263.png)
_Renommer le nom de la classe_

Sur la première page, nous listerons les éléments todo créés. Renommons-la de `MyHomePage` à `TodoList`. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-264.png)
_Renommer la classe `MyHomePage` en `TodoList`_

Dans la capture d'écran ci-dessus, le titre de MaterialApp est défini sur "Flutter Demo" et le titre passé dans TodoList est défini sur "Flutter Demo Home Page". Changeons les deux en "Todo Manager". 

## Comment construire l'application Todo

Construisons la fonctionnalité principale de notre application. 

Nous avons besoin d'une classe `Todo`. Cette classe définira les propriétés d'un todo. Dans notre cas, nous aurons les éléments suivants :

1. Nom du todo
2. Statut du todo (Backlog / Complété)

Définissons une classe `Todo` avec les propriétés ci-dessus :

```dart
class Todo {
  Todo({required this.name, required this.completed});
  String name;
  bool completed;
}
```

Ajoutez le code ci-dessus à la fin du fichier `main.dart`. 

### Comment ajouter un Todo

Regardez votre code pour une classe nommée `_TodoListState`. Dans le corps de la méthode `build`, définissez la propriété children sur un tableau vide. Voir la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/1.-Remove-Center-Text.jpg)
_Avant et après la suppression des widgets `Text`_

Supprimez les deux widgets `Text` à l'intérieur de cette propriété children. 

Maintenant, nous allons remplacer la variable counter par une liste de todos. 

```dart
int _counter = 0;
```

Remplacez la ligne ci-dessus par le code suivant. La première ligne est la liste des todos et la deuxième ligne définit le contrôleur pour obtenir le nom du todo de l'utilisateur :

```dart
final List<Todo> _todos = <Todo>[];
final TextEditingController _textFieldController = TextEditingController();
```

Supprimez la méthode `_incrementCounter` et ajoutez la méthode pour ajouter un todo :

```dart
void _addTodoItem(String name) {
    setState(() {
      _todos.add(Todo(name: name, completed: false));
    });
    _textFieldController.clear();
}
```

Jusqu'à présent, nous avons défini notre liste de todos et un contrôleur d'entrée. Nous avons également créé une méthode qui accepte le texte d'entrée et l'ajoute à la liste des todos avec un statut complété défini sur `false` et un champ d'entrée clair. 

La raison pour laquelle nous avons utilisé la méthode `setState` est de rafraîchir l'UI après avoir mis à jour la liste des todos. Comme notre composant est un widget d'état, chaque fois qu'un changement d'état est détecté, l'UI se rendra à nouveau avec l'état mis à jour. 

Nous avons construit le code de fonctionnalité pour ajouter un todo. Construisons le code UI. Demandons à l'utilisateur le nom du todo en appuyant sur le bouton d'action flottant en bas à droite. Lorsque l'utilisateur essaie d'enregistrer le todo, nous appellerons la méthode `_addTodoItem` définie ci-dessus. 

```dart
floatingActionButton: FloatingActionButton(
    onPressed: () => _displayDialog(),
    tooltip: 'Ajouter un Todo',
    child: const Icon(Icons.add),
),
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/2.-Floating-Action-Button.jpg)
_Avant et après du code du bouton d'action flottant_

Dans la méthode ci-dessus, nous avons changé la propriété `onPressed` pour appeler la méthode `_displayDialog`. Comme elle n'est pas encore définie, elle affichera une erreur. Nous définirons la méthode ensuite. Nous avons également changé la propriété `tooltip` en "Ajouter un Todo". 

Voici le code (méthode `_displayDialog`) pour afficher une boîte de dialogue avec un champ de saisie, ajouter et annuler le bouton. Ajoutez cette méthode à l'intérieur de la classe `_TodoListState` :

```
Future<void> _displayDialog() async {
    return showDialog<void>(
      context: context,
      T: false,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Ajouter un todo'),
          content: TextField(
            controller: _textFieldController,
            decoration: const InputDecoration(hintText: 'Tapez votre todo'),
            autofocus: true,
          ),
          actions: <Widget>[
            OutlinedButton(
              style: OutlinedButton.styleFrom(
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
              ),
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: const Text('Annuler'),
            ),
            ElevatedButton(
              style: ElevatedButton.styleFrom(
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
              ),
              onPressed: () {
                Navigator.of(context).pop();
                _addTodoItem(_textFieldController.text);
              },
              child: const Text('Ajouter'),
            ),
          ],
        );
      },
    );
  }
```

Comprenons ce gros morceau de code. 

La classe `Future` est utilisée pour le calcul asynchrone. 

En citant la [documentation](https://api.flutter.dev/flutter/dart-async/Future-class.html), 

> "Un calcul asynchrone peut avoir besoin d'attendre quelque chose d'externe au programme (lecture d'un fichier, interrogation d'une base de données, récupération d'une page web) qui prend du temps. Au lieu de bloquer tous les calculs jusqu'à ce que le résultat soit disponible, le calcul asynchrone retourne immédiatement un `Future` qui 'complétera' **_éventuellement_** avec le résultat. "

Dans notre cas, il attendra que l'utilisateur appuie sur le bouton Ajouter ou Annuler. 

La méthode `_displayDialog` retournera la méthode `showDialog` en construisant l'UI. 

La propriété `barrierDismissible` est utilisée pour définir si la fenêtre contextuelle doit être fermée si l'utilisateur appuie en dehors de la boîte de dialogue d'alerte. Nous l'avons définie sur `false`, ce qui signifie que la boîte de dialogue d'alerte ne sera pas fermée en appuyant à l'extérieur. 

Le `builder` de cette méthode `showDialog` retourne un `AlertDialog` composé des propriétés `title`, `content` et `actions`. Le `title` est défini pour afficher le texte "Ajouter un todo". La propriété `content` rendra un champ de saisie de texte avec un focus automatique activé et l'indice "Tapez votre todo". 

La propriété `actions` rendra 2 boutons, `Annuler` et `Ajouter`. Le bouton `Annuler` est un bouton en contour, et appuyer dessus fermera la boîte de dialogue. Le bouton `Ajouter` ajoute le texte à la liste des todos et ferme la boîte de dialogue. 

Testons notre application. Cliquez sur le bouton d'action flottant et vous devriez voir l'UI similaire à celle ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-262.png)
_UI Ajouter Todo_

Si vous essayez d'ajouter un todo, il sera ajouté à notre liste de todos. Mais vous ne pourrez pas voir de changement sur l'UI. 

### Comment lister les Todos

Nous avons ajouté le code pour ajouter des todos à la liste. Mais attendez, comment pouvons-nous vérifier cela ? Nous devons vérifier si le todo a été ajouté à la liste. 

Vérifions cela en rendant la liste des éléments todo dans l'UI. Pour ce faire, nous devons concevoir l'UI pour un seul todo. Faisons cela. 

Ajoutez le code suivant à la fin du fichier `main.dart` :

```dart
class TodoItem extends StatelessWidget {
  TodoItem({required this.todo}) : super(key: ObjectKey(todo));

  final Todo todo;

  TextStyle? _getTextStyle(bool checked) {
    if (!checked) return null;

    return const TextStyle(
      color: Colors.black54,
      decoration: TextDecoration.lineThrough,
    );
  }

  @override
  Widget build(BuildContext context) {
    return ListTile(
      onTap: () {},
      leading: Checkbox(
        checkColor: Colors.greenAccent,
        activeColor: Colors.red,
        value: todo.completed,
        onChanged: (value) {},
      ),
      title: Row(children: <Widget>[
        Expanded(
          child: Text(todo.name, style: _getTextStyle(todo.completed)),
        ),
        IconButton(
          iconSize: 30,
          icon: const Icon(
            Icons.delete,
            color: Colors.red,
          ),
          alignment: Alignment.centerRight,
          onPressed: () {},
        ),
      ]),
    );
  }
}
```

Voici une brève explication du code ci-dessus. 

Tout d'abord, nous avons créé une classe avec `TodoItem` et nous l'avons étendue à partir de la classe `StatelessWidget` car nous n'avons pas besoin de maintenir l'état pour cette classe. 

Nous acceptons un `Todo`, qui est passé via le constructeur à notre classe. Le code dans la méthode `build` détermine l'UI. Il rend le widget `ListTile` avec le widget `Checkbox` passé à la propriété `leading`. 

La propriété `title` rend une ligne de widgets `Text` et `IconButton`. Le widget `Text` affiche le nom du todo et le widget `IconButton` affiche l'icône `delete`. 

Remarquez la méthode `_getTextStyle` passée à la propriété `style` du widget `Text`. Cette méthode barre le texte si le todo est marqué comme complété. Rien ne change en appuyant sur l'un de ces widgets, car les propriétés correspondantes sont laissées vides (onTap, onChanged et onPressed). 

Changez la propriété `body` de la méthode `build` dans `_TodoListState` avec le code suivant :

```dart
ListView(
    padding: const EdgeInsets.symmetric(vertical: 8.0),
    children: _todos.map((Todo todo) {
      return TodoItem(
        todo: todo,
      );
    }).toList(),
),
```

Voici la capture d'écran mise en évidence montrant les changements dans la méthode `build` de la classe `_TodoListState` :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-265.png)
_Rendu de la liste des éléments todo_

Le code ci-dessus définit un widget `ListView` itérant sur les todos créés et passant chaque todo au widget `TodoItem`. 

Nous avons terminé avec la liste des todos. Vérifions si la création et la visualisation d'un todo fonctionnent correctement. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-266.png)
_Liste des todos créés_

Cool ! Voici nos todos. 

Mais appuyer sur la case à cocher ou le bouton Supprimer n'aura aucun effet. 

J'espère que vous pouvez deviner ce que nous allons faire ensuite. Oui, nous allons ajouter le code pour marquer le todo comme complété et supprimer un élément todo. 

### Comment mettre à jour un Todo

Marquons le todo comme complété en appuyant sur la case à cocher près de chaque todo. 

Nous avons 2 champs dans notre classe Todo. Ce sont le nom et le statut complété. Chaque fois qu'un Todo est créé, la valeur par défaut du champ complété est définie sur `false`. Cela signifie que le todo est en cours. Nous pouvons changer cela en `true` chaque fois que nous complétons la tâche. 

Définissez une méthode appelée `_handleTodoChange` dans la classe `_TodoListState`. Ajoutez cette méthode sous la méthode `_addTodoItem` que nous avons définie pour ajouter un todo à la liste. 

```dart
void _handleTodoChange(Todo todo) {
  setState(() {
    todo.completed = !todo.completed;
  });
}
```

Dans le code ci-dessus, nous acceptons un todo et changeons le statut complété du todo. Ainsi, chaque fois que cette méthode est appelée avec un todo, son statut complété changera de `true` à `false` ou vice versa. N'oubliez pas que nous avons enveloppé cela dans une méthode `setState` pour rendre l'UI après avoir effectué le changement. 

Nous devons déclencher cette méthode lorsque l'utilisateur appuie sur un todo ou sur une case à cocher. Nous devons passer cette méthode à la classe `TodoItem`. Lors de l'appel de `TodoItem` dans la méthode build de la classe `_TodoListState`, passez la méthode `_handleTodoChange` comme indiqué ci-dessous :

```dart
return TodoItem(
    todo: todo,
    onTodoChanged: _handleTodoChange,
);
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/4.-Change-Todo-Status-2.jpg)
_Avant et après l'ajout d'une méthode pour changer le statut du todo_

Comme nous passons la méthode à la classe `TodoItem`, nous devons recevoir la même méthode dans la classe `TodoItem`. Pour ce faire, nous devons définir cette méthode dans le constructeur de la classe `TodoItem`. Allez dans `TodoItem` et changez le constructeur pour inclure la méthode `onTodoChanged`. 

```dart
TodoItem({required this.todo, required this.onTodoChanged})
      : super(key: ObjectKey(todo));
```

Vous pouvez remarquer dans le code ci-dessus que nous utilisons `**this**.onTodoChanged`, ce qui signifie que nous liaisons la méthode passée à une méthode dans cette classe `TodoItem`. 

Définissons une méthode avec le même nom et définissons le type de retour sur `void` (car nous n'attendons rien de cette méthode). 

```dart
final void Function(Todo todo) onTodoChanged;
```

Ainsi, partout où nous appelons cette méthode dans notre code, le statut de notre todo sera changé en son opposé. Appelons cette méthode dans la propriété `onTap` du widget `ListTile` et la propriété `onChanged` du widget `Checkbox`. 

```dart
onTap: () {
    onTodoChanged(todo);
},
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/4.-Change-Todo-Status---Method-Call.jpg)
_Appeler la méthode `onTodoChanged` en appuyant sur le todo ou la case à cocher_

C'est tout. Nous avons terminé. Exécutons notre application et vérifions si nous sommes en mesure de compléter le todo. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-267.png)
_Marquer le todo comme complété_

C'est génial, n'est-ce pas ? Nous sommes en mesure de marquer le todo comme complété et de revenir en arrière. 

### Comment supprimer un Todo

Il ne nous reste plus qu'un élément à compléter pour cette application. Nous devons être en mesure de supprimer un todo, si nous en créons un par erreur ou s'il n'est plus applicable. 

Les étapes pour supprimer un todo sont similaires à la mise à jour d'un todo. Nous allons faire exactement les 4 étapes que nous avons faites pour mettre à jour un todo. 

1. Définir la méthode `_deleteTodo`
2. Passer la méthode lors du rendu de `TodoItem`
3. Recevoir la méthode dans le constructeur de `TodoItem`
4. Lier la méthode
5. Appeler la méthode lors de l'appui sur le bouton

Je vous recommande d'essayer cela par vous-même car nous allons répéter les étapes que nous avons faites précédemment. Une fois que vous avez terminé, vous pouvez vérifier votre implémentation en croisant avec mes étapes. 

Voici la méthode pour supprimer le todo. Ajoutez ceci dans la classe `_TodoListState` sous la méthode `_handleTodoChange` :

```dart
void _deleteTodo(Todo todo) {
  setState(() {
    _todos.removeWhere((element) => element.name == todo.name);
  });
}
```

Cette méthode accepte un todo, le compare avec la liste des todos et identifie le todo qui correspond à ce nom. Ensuite, elle le supprime de la liste et met enfin à jour l'état. 

Passons la référence de la méthode à `TodoItem` dans la méthode `build` de la classe `_TodoListState`. 

```dart
return TodoItem(
  todo: todo,
  onTodoChanged: _handleTodoChange,
  removeTodo: _deleteTodo);
```

Changez le constructeur pour accepter la méthode `removeTodo`. 

```
  TodoItem(
      {required this.todo,
      required this.onTodoChanged,
      required this.removeTodo})
      : super(key: ObjectKey(todo));
```

Définissez une méthode avec le même nom et définissez le type de retour sur `void` (car nous n'attendons rien de cette méthode). 

Notre dernière étape consiste à appeler cette méthode en appuyant sur le bouton de suppression. 

```dart
IconButton(
  iconSize: 30,
  icon: const Icon(
    Icons.delete,
    color: Colors.red,
  ),
  alignment: Alignment.centerRight,
  onPressed: () {
    removeTodo(todo);
  },
),
```

C'est tout. J'espère que c'est super simple. Testons notre application. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/5.-Delete-Todo.jpg)
_Dernier todo supprimé_

Waouh ! Cela fonctionne. 

Dans la capture d'écran ci-dessus, vous pouvez voir que j'ai créé un todo avec le nom "Call SC service men" qui devrait être créé comme "Call AC service men". Donc, c'était une erreur. Je ne veux plus de ce todo car il me confondra. Je préférerais créer un nouveau todo avec l'orthographe correcte. Donc, j'ai appuyé sur le bouton de suppression qui a presque instantanément supprimé mon todo. 

Cool ! Nous avons construit notre propre application todo. 

## Conclusion

Dans cet article, vous avez appris la gestion d'état dans Flutter. En plus de cela, nous avons construit une application todo simple dans Flutter en implémentant la fonctionnalité CRUD. 

CRUD signifie Create, Read, Update et Delete. Nous avons créé un todo, l'avons listé sur l'UI, mis à jour son statut et finalement supprimé. 

Ce [dépôt](https://github.com/5minslearn/Flutter-Todo-App) contient mon code. Vous pouvez l'utiliser pour référence. 

Voici quelques exercices pour vous challenger. Essayez d'étendre cette application en ajoutant les fonctionnalités suivantes. 

1. Afficher un message disant "Aucun todo n'existe. Veuillez en créer un et suivre votre travail", si aucun todo n'a été créé.
2. Je connais un bug dans cette application. J'espère que vous ne le connaissez pas - alors je le révèle ici. Mais vous devez le corriger. Créez deux todos avec le même nom et essayez d'en supprimer un. Vous serez surpris de voir les deux supprimés ensemble. Voici un conseil pour vous pour le corriger. Attribuez un identifiant aléatoire pour chaque todo et lors de la suppression, filtrez le todo par identifiant. 
3. Ajoutez une fonctionnalité pour modifier le nom d'un todo
4. Cette application a été entièrement construite sur un état éphémère. Donc, si vous fermez et rouvrez l'application, vos anciens éléments todo ne seront pas là. Ajoutez une fonctionnalité pour stocker le todo dans le stockage de l'appareil. Montrez les todos à l'utilisateur lorsqu'ils rouvrent l'application en les lisant depuis votre stockage de l'appareil. 

Pour en savoir plus sur Flutter, abonnez-vous à ma newsletter par e-mail sur mon [site](https://5minslearn.gogosoon.com/?ref=fcc_flutter_todo_app) ([https://5minslearn.gogosoon.com](https://5minslearn.gogosoon.com/?ref=fcc_flutter_todo_app)) et suivez-moi sur les réseaux sociaux.