---
title: Comment ajouter la base de données Realm à une application CRUD iOS avec Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-27T18:21:00.000Z'
originalURL: https://freecodecamp.org/news/add-realm-database-to-ios-crud-app-with-with-swift
coverImage: https://cdn-media-2.freecodecamp.org/w1280/605aa5a8687d62084bf6b611.jpg
tags:
- name: database
  slug: database
- name: iOS
  slug: ios
- name: ios app development
  slug: ios-app-development
- name: Swift
  slug: swift
seo_title: Comment ajouter la base de données Realm à une application CRUD iOS avec
  Swift
seo_desc: "By Sai Balaji K\nHello, everyone! In this article we are going to learn\
  \ how to add the Realm database to an iOS app. \nWe'll create a simple ToDo app\
  \ so you can learn how to perform CRUD (Create, Read, Update, Delete) operations\
  \ in the Realm database.\n..."
---

Par Sai Balaji K

Bonjour à tous ! Dans cet article, nous allons apprendre à ajouter la base de données Realm à une application iOS.

Nous allons créer une application ToDo simple afin que vous puissiez apprendre à effectuer des opérations CRUD (Create, Read, Update, Delete) dans la base de données Realm.

## Qu'est-ce que Realm ?

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-24-at-8.09.31-AM.png)

Realm est une base de données mobile open-source, conviviale pour les développeurs et facile à utiliser. Vous pouvez également l'utiliser comme alternative à Core Data dans les applications iOS.

Realm est une base de données mobile multiplateforme, ce qui signifie que vous pouvez l'utiliser dans des applications natives Android et iOS, ainsi que dans des applications multiplateformes comme celles créées avec React Native. Elle prend en charge Objective-C, Swift, Java, Kotlin, C# et JavaScript.

## Comment configurer Realm dans votre projet iOS

Nous pouvons ajouter Realm à notre projet iOS en utilisant SPM (le Swift Package Manager), Cocoa Pods ou Carthage. Ici, nous allons utiliser Cocoa Pods pour ajouter le Pod Realm à notre projet iOS.

1. Ouvrez Xcode et créez un projet d'application iOS vide avec UIKit et Swift sans utiliser Core Data.
2. Fermez maintenant Xcode et ouvrez le terminal. Naviguez vers le répertoire de votre projet à l'aide du terminal.
3. Exécutez la commande suivante pour créer un Podfile.

```command
pod init
```

4. Maintenant, lorsque vous listez le contenu du répertoire, vous pouvez voir qu'il y a un nouveau Podfile. Ouvrez le fichier à l'aide de n'importe quel éditeur de texte (ici, j'ai utilisé Vim). Modifiez votre Podfile pour qu'il ressemble à l'image ci-dessous. Enregistrez et fermez le Podfile.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-24-at-8.23.07-AM.png)

Maintenant que nous avons spécifié la dépendance pour Realm DB, nous pouvons installer les dépendances en exécutant la commande ci-dessous :

```command
pod install 

```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-24-at-8.26.21-AM.png)

Comme vous pouvez le voir, nous avons ajouté avec succès la dépendance Realm DB dans notre projet iOS. Maintenant, exécutez la commande ci-dessous pour ouvrir notre projet dans Xcode.

```command
open YOUR_APP_NAME.xcworkspace
```

Remarque : après avoir ouvert Xcode, assurez-vous de compiler votre projet en appuyant sur Command+B.

## Comment concevoir votre interface utilisateur dans Realm

Nous allons garder l'interface utilisateur de notre application simple. Ouvrez Main.storyboard et créez une interface utilisateur simple comme indiqué ci-dessous en ajoutant une table view avec une cellule prototype. Ensuite, intégrez un navigation controller et créez les IBOutlets pour la table view dans le fichier ViewController.swift :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-24-at-8.32.42-AM.png)

## Comment créer un modèle de données dans Realm

Dans notre application ToDo, chaque tâche a un nom et un identifiant. Nous allons créer une classe Modèle pour représenter la tâche todo. Dans le navigateur de projet, faites un clic droit et créez un nouveau fichier Swift, puis ajoutez le code ci-dessous.

```swift
import Foundation
import RealmSwift


class ToDoTask:Object
{
    @objc dynamic var tasknote: String?
    @objc dynamic var taskid: String?
}
```

Ici, nous avons créé notre classe de modèle nommée ToDoTask. Elle hérite de la classe Object, qui est une classe fournie avec RealmDB. Cette classe gère tous les processus en arrière-plan pour sauvegarder les données créées à l'aide de cette classe de modèle dans la base de données.

Nous avons également ajouté deux propriétés : `tasknote`, qui est la tâche à effectuer, et `taskid` – toutes deux de type string. `@objc` signifie que votre code Swift est visible par Objective-C et `dynamic` signifie que vous souhaitez utiliser le dynamic dispatch d'Objective-C.

## Fonctions de base de l'application CRUD

Notre application effectuera les fonctions suivantes :

1. Obtenir une saisie de l'utilisateur à l'aide d'AlertViewController.
2. Ajouter la saisie à la base de données et également à la table view.
3. Permettre à l'utilisateur de modifier sa saisie.
4. Utiliser le swipe to delete pour supprimer une ligne afin de retirer les données de la table view et de la base de données.
5. Récupérer toutes les données (si présentes) de la base de données et les afficher dans la table view.

### Comment obtenir une saisie de l'utilisateur à l'aide d'AlertViewController

Ouvrez `ViewController.swift` et ajoutez le code ci-dessous à l'intérieur de la méthode `ViewDidLoad()`. Créez ensuite une nouvelle fonction appelée `addTask()` et ajoutez le code pour afficher l'alert view controller avec une zone de texte pour obtenir la saisie de l'utilisateur.

Maintenant, lorsque le bouton de barre droit est pressé, il appellera la fonction `addTask()` qui affichera l'alertviewcontroller avec un champ de texte pour obtenir la saisie de l'utilisateur.

```swift
navigationItem.rightBarButtonItem = UIBarButtonItem(image: .add, style: .done, target: self, action: #selector(addTask))

navigationController?.navigationBar.prefersLargeTitles = true

title = "RealmDB"
```

```swift
@objc
    func addTask()
    { 
        let ac = UIAlertController(title: "Add Note", message: nil, preferredStyle: .alert)
        
        ac.addTextField(configurationHandler: .none)
        
        ac.addAction(UIAlertAction(title: "Add", style: .default, handler: { (UIAlertAction) in
          
              if let text = ac.textFields?.first?.text
            {
                print(text)
            }
            
        }))
        ac.addAction(UIAlertAction(title: "Cancel", style: .cancel, handler: nil))
        present(ac, animated: true, completion: nil)
    }
```

### Comment ajouter la saisie à la base de données et à la table view

Pour sauvegarder des données dans Realm, nous devons d'abord obtenir une instance de Realm par laquelle nous pouvons accéder à toutes les méthodes nécessaires aux opérations CRUD. Créez une propriété de type Realm dans le fichier `ViewController.swift` et initialisez-la dans la méthode `viewDidLoad()`.

```swift
 var realmDB: Realm!
```

```swift
 override func viewDidLoad() {
        super.viewDidLoad()
        
        navigationItem.rightBarButtonItem = UIBarButtonItem(image: .add, style: .done, target: self, action: #selector(addTask))
        navigationController?.navigationBar.prefersLargeTitles = true
        title = "RealmDB"
        
        realmDB = try! Realm()
       
    }
```

Créez un tableau vide de type notre DataModel (ToDoTask). Ce tableau contiendra toutes les tâches qui doivent être ajoutées à la table view et à la base de données.

Maintenant, à l'intérieur de la fonction `addTask()`, modifiez la closure de l'action Add pour qu'elle récupère la saisie de l'utilisateur et crée un identifiant aléatoire pour cette saisie. Ensuite, ajoutez-la à notre tableau et sauvegardez-la dans la base de données.

```swift
var tasks = [ToDoTask]()
```

```swift
 if let text = ac.textFields?.first?.text
            {
            	//Ajouter les données au tableau du modèle de données
                let t = ToDoTask()
                t.taskid = UUID().uuidString
                t.tasknote = text
                self.tasks.append(t)
                
                //Ajouter les données à la base de données
                try! self.realmDB.write {
                    self.realmDB.add(t)
                }
                //Mettre à jour l'interface utilisateur de la table view
                self.tasktv.reloadData()
            }
```

Maintenant, lorsque vous lancez l'application, les données seront sauvegardées dans la base de données. Mais elles ne s'afficheront pas dans la table view car nous n'avons pas implémenté les méthodes de délégué.

Faites en sorte que la classe ViewController implémente les protocoles `UITableViewDelegate` et `UITableViewDataSource` et ajoutez les stubs de protocole.

Maintenant, à l'intérieur de la méthode `numberOfRowsInSection`, retournez le nombre d'éléments de notre tableau tasks, ce qui donne le nombre de lignes à ajouter à la table view. C'est égal au nombre d'éléments dans le tableau tasks.

```swift
 func tableView(_ tableView: UITableView, numberOfRowsInSection section: 
 Int) -> Int 
 {
        return tasks.count;
 }
```

La prochaine chose que nous devons faire est de spécifier le contenu de chaque ligne. Nous pouvons le faire en utilisant la méthode de délégué `cellForRowAt`. Ici, nous récupérons une cellule en utilisant l'identifier que nous avons mentionné dans le storyboard et spécifions le texte du label comme la propriété tasknote de l'élément du tableau tasks.

```swift
 func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        if let cell = tableView.dequeueReusableCell(withIdentifier: "cell")
        {
            cell.textLabel?.text = tasks[indexPath.row].tasknote
            return cell
        }
        return UITableViewCell()
    }
```

### Comment permettre aux utilisateurs de modifier leur saisie

Maintenant, nous devons permettre à l'utilisateur de modifier ses tâches saisies et de mettre à jour les modifications à la fois dans la base de données et dans l'interface utilisateur. Nous pouvons le faire en utilisant des méthodes similaires pour obtenir la saisie de l'utilisateur. Implémentez la méthode de délégué `didSelectRowAt` qui sera appelée lorsque l'utilisateur appuie sur la ligne de la table view.

Ajoutez le code ci-dessous qui affiche un `AlertViewController` avec une vue texte. Ensuite, mettez à jour le contenu de la cellule avec le texte saisi, et en même temps, mettez à jour le contenu de la base de données.

```swift
func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {

        let tasktomodify = tasks[indexPath.row]
        let ac = UIAlertController(title: "Update task", message: nil, preferredStyle: .alert)
        
        ac.addTextField(configurationHandler: .none)
        ac.addAction(UIAlertAction(title: "Ok", style: .default, handler: { (UIAlertAction) in
            if let text = ac.textFields?.first?.text
            {
                if(!text.isEmpty)
                {
                try! self.realmDB.write({
                    tasktomodify.tasknote = text
                })
                self.tasktv.reloadData()
                }
            }
        }))
        
        present(ac, animated: true, completion: nil)
    }
```

### Comment balayer pour supprimer une ligne et retirer les données de la table view et de la base de données

Ici, nous allons implémenter une fonctionnalité swipe to delete dans notre table view afin que les utilisateurs puissent supprimer leurs tâches. Mais en arrière-plan, lorsque l'utilisateur effectue un swipe to delete sur une ligne de la table view, cela doit supprimer les données de la base de données, du tableau du modèle de données et mettre à jour l'interface utilisateur de la table view.

Nous pouvons le faire en implémentant la méthode de délégué **commit editingStyle** et en ajoutant le code suivant :

```swift
 func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath) {
        if editingStyle == .delete
        {
            let tasktoDelete = tasks[indexPath.row]
            try! realmDB.write({
                realmDB.delete(tasktoDelete)
                self.tasks.remove(at: indexPath.row)
                self.tasktv.deleteRows(at: [indexPath], with: .fade)
            })
        }
    }
```

### Comment récupérer toutes les données (si présentes) de la base de données et les afficher dans la table view

Maintenant, nous allons implémenter notre dernière opération, Read. Chaque fois que l'utilisateur lance l'application, elle doit récupérer les données de la base de données (si des données sont présentes) et les afficher dans la table view.

Nous pouvons le faire en créant une fonction `getTodos` dans le fichier Swift du view controller et en y ajoutant le code suivant :

```swift
func getTodos()
    {
       //Récupérer toutes les données de la base de données
        let notes = realmDB.objects(ToDoTask.self)
        
        //Vider le tableau de données du modèle pour éviter les doublons
        self.tasks.removeAll()
        
        /* Si les données récupérées ne sont pas vides, les ajouter au tableau de données du modèle et mettre à jour l'interface utilisateur */
        if(!notes.isEmpty)
        {
        for n in notes
        {
            
            self.tasks.append(n)
            
        }
            self.tasktv.reloadData()
        }
        
        
    }
```

## Astuce bonus : Comment visualiser le contenu de votre base de données dans un simulateur iOS

Maintenant, lorsque vous lancez votre application, vous pouvez voir qu'elle fonctionne comme prévu. Mais comment pouvons-nous vérifier si les données sont réellement stockées dans la base de données ? Nous pouvons utiliser une application appelée MongoDB Realm Studio grâce à laquelle nous pouvons visualiser nos données stockées dans la base de données Realm du simulateur.

> Notez que cette méthode ne fonctionne que lorsque vous testez l'application à l'aide du simulateur iOS

Dans la méthode `viewDidLoad()`, ajoutez la ligne de code ci-dessous qui affichera le chemin d'accès réel au fichier de notre application :

```swift
 print(realmDB.configuration.fileURL!)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-24-at-9.48.59-AM.png)

Maintenant, copiez le chemin du fichier affiché dans la console, ouvrez le terminal et exécutez la commande suivante :

```command
open REALM_FILE_PATH_HERE

```

> Assurez-vous d'avoir téléchargé MongoDB Realm Studio depuis votre navigateur avant d'exécuter la commande ci-dessus.

Cela ouvrira alors le fichier Realm de l'application dans MongoDB Realm Studio. Cela affichera les données stockées dans la base de données sous forme de tableau.

Si vous apportez des modifications à vos données en modifiant ou en supprimant la tâche, les changements seront reflétés dans l'application MongoDB Realm Studio :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-24-at-9.55.29-AM.png)

Félicitations ! Vous avez créé une application simple qui implémente les opérations CRUD dans les applications iOS.