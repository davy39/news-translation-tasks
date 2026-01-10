---
title: Comment utiliser UISearchController dans les applications iOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-24T15:55:58.000Z'
originalURL: https://freecodecamp.org/news/learn-to-use-uisearchcontroller-in-ios-apps
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-21-at-8.11.31-PM.png
tags:
- name: iOS
  slug: ios
- name: ios app development
  slug: ios-app-development
- name: Swift
  slug: swift
- name: Xcode
  slug: xcode
seo_title: Comment utiliser UISearchController dans les applications iOS
seo_desc: 'By Sai Balaji K

  Hello everyone! In this article we are going to learn how to use UISearchController
  in iOS Apps.

  What are we going to build?

  We are going to build a movie search application which uses the TMDB API to fetch
  movie info and display it u...'
---

Par Sai Balaji K

Bonjour à tous ! Dans cet article, nous allons apprendre à utiliser UISearchController dans les applications iOS.

## Que allons-nous construire ?

Nous allons construire une application de recherche de films qui utilise l'API [TMDB](https://www.themoviedb.org/) pour récupérer les informations sur les films et les afficher à l'aide d'un UICollectionView basé sur la requête de recherche de l'utilisateur.

## Configuration du projet

Ouvrez Xcode et créez un nouveau projet iOS App vierge – assurez-vous de sélectionner UIKit et non SwiftUI.

Dans cette application, nous allons utiliser le MVC Pattern, donc organisez le projet en créant les groupes et fichiers Swift suivants :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-21-at-8.16.02-PM.png)

Maintenant, fermez votre projet Xcode. Ouvrez le terminal et déplacez-vous dans le répertoire de votre projet. Ici, nous devons ajouter les Cocoa Pods [SD WebImage](https://cocoapods.org/pods/SDWebImage) pour télécharger et mettre en cache de manière asynchrone les images d'affiches de films.

Tapez la commande suivante dans le terminal :

```
pod init
```

Maintenant, lorsque vous listez le contenu du répertoire, vous pouvez voir qu'il y a un nouveau Podfile. Ouvrez le fichier à l'aide de n'importe quel éditeur de texte (ici, j'ai utilisé Vim). Modifiez votre Podfile pour qu'il ressemble à l'image ci-dessous. Enregistrez et fermez le Podfile.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-21-at-8.20.28-PM.png)

Maintenant que nous avons spécifié SD WebImage, nous pouvons installer les dépendances en exécutant la commande ci-dessous :

```
pod install
```

Comme vous pouvez le voir, nous avons ajouté avec succès le pod SD WebImage dans notre projet iOS. Exécutez maintenant la commande ci-dessous pour ouvrir notre projet dans Xcode.

```
open NOM_DU_PROJET.xcworkspace
```

Après avoir ouvert Xcode, assurez-vous de compiler votre projet en appuyant sur Command+B.

## **Comment concevoir l'interface utilisateur à l'aide d'UIKit et de l'UI programmatique**

Notre application nécessite trois éléments UI : des barres de navigation pour contenir la barre de recherche, un UISearchBarController pour la recherche réelle, et un UICollectionView pour afficher les résultats de la recherche.

Ouvrez votre fichier Scenedelegate.swift et ajoutez le code suivant à l'intérieur, qui se connectera à la méthode session :

```swift
func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
        guard let scene = (scene as? UIWindowScene) else { return }
        window = UIWindow(windowScene: scene)
        window?.rootViewController=UINavigationController(rootViewController:HomeVC())
        window?.makeKeyAndVisible()
    }
```

Puisque nous utilisons une UI programmatique, nous devons d'abord mentionner notre Root View controller – c'est-à-dire le premier écran qui s'affichera lorsque l'utilisateur lancera l'application.

Ici, dans cette application, nous n'utilisons qu'un seul View Controller, nous l'enveloppons donc dans un UINavigationController. Cela fournit une barre de navigation où nous pouvons placer notre UISearchController.

Ouvrez le fichier HomeVC.swift et ajoutez les propriétés suivantes :

```swift
 private var SearchBar: UISearchController = {
        let sb = UISearchController()
        sb.searchBar.placeholder = "Entrez le nom du film"
        sb.searchBar.searchBarStyle = .minimal
        return sb
    }()
    
    private var MovieCollectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        layout.scrollDirection = .vertical
        layout.itemSize = CGSize(width: UIScreen.main.bounds.width/3 - 10, height: 200)
        let cv = UICollectionView(frame: .zero, collectionViewLayout: layout)
        cv.register(MovieCell.self, forCellWithReuseIdentifier: MovieCell.ID)
        return cv
    }()
```

D'abord, nous créons notre UISearchController et configurons ses propriétés telles que le texte d'espace réservé (placeholder) et le style.

Ensuite, nous créons un UICollectionView et spécifions le type de mise en page (layout) que notre vue de collection doit utiliser. Dans ce cas, il s'agit d'un UICollectionViewFlowLayout avec d'autres propriétés telles que la direction du défilement, la taille des éléments et la spécification d'une classe de cellule CollectionView personnalisée que nous créerons plus tard dans notre projet.

À l'intérieur de la classe HomeVC, créez une nouvelle fonction et ajoutez le code suivant pour configurer les contraintes d'auto-layout par programmation pour notre UICollectionView :

```swift
    //MARK: - AIDES
    func configureUI(){
        MovieCollectionView.translatesAutoresizingMaskIntoConstraints = false
        MovieCollectionView.topAnchor.constraint(equalTo: view.topAnchor).isActive = true
        MovieCollectionView.bottomAnchor.constraint(equalTo: view.bottomAnchor).isActive = true
        MovieCollectionView.leftAnchor.constraint(equalTo: view.leftAnchor).isActive = true
        MovieCollectionView.rightAnchor.constraint(equalTo: view.rightAnchor).isActive = true
    }

```

D'abord, nous indiquons que nous n'avons pas besoin de convertir le masque de redimensionnement automatique en contraintes. Ensuite, nous épinglons notre vue de collection aux quatre côtés de notre View Controller.

À l'intérieur de la méthode `viewDidLoad()`, ajoutez les lignes de code suivantes :

```swift
  override func viewDidLoad() {
        super.viewDidLoad()
        
        navigationItem.title  = "Recherche de films"
        view.backgroundColor = .systemBackground
        SearchBar.searchResultsUpdater = self
        navigationItem.searchController = SearchBar
        view.addSubview(MovieCollectionView)
        MovieCollectionView.delegate = self
        MovieCollectionView.dataSource = self
        configureUI()
    }
```

Ici, nous spécifions d'abord le titre de notre ViewController, suivi de la couleur d'arrière-plan qui est la couleur systemBackground. Si l'appareil est en mode clair, il affiche un fond blanc. S'il est en mode sombre, il affiche un fond noir.

Ensuite, nous définissons le view controller actuel comme le gestionnaire de mise à jour des résultats de recherche (search result updater), puis nous ajoutons notre SearchController à la barre de navigation, ajoutons l'UICollectionView au ViewController et configurons le delegate et la datasource. Enfin, nous épinglons l'UICollectionView en utilisant l'auto-layout.

Créez une extension pour HomeVC et implémentez le protocole UISearchResultsUpdating et sa méthode stub updateSearchResults.

```swift
extension HomeVC: UISearchResultsUpdating{
    
    func updateSearchResults(for searchController: UISearchController) {
        guard let query = searchController.searchBar.text else{return}
      
        }
        
    }
    
    
}
```

La méthode `updateSearchResults()` sera appelée chaque fois que le texte saisi dans la barre de recherche change ou lorsque l'utilisateur appuie sur le bouton de recherche de son clavier.

Ensuite, nous devons créer cette cellule UICollectionView personnalisée. À l'intérieur du fichier MovieCell.swift, ajoutez le code suivant :

```swift
import Foundation
import UIKit
import SDWebImage

class MovieCell: UICollectionViewCell{
    
    static let ID = "MovieCell"
    private var MoviePosterImageView: UIImageView = {
        let imageView = UIImageView()
        imageView.contentMode = .scaleAspectFit
      //  imageView.image = UIImage(systemName: "house")
        return imageView
    }()
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        addSubview(MoviePosterImageView)
        configureUI()
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
}

extension MovieCell{
    func configureUI(){
        MoviePosterImageView.translatesAutoresizingMaskIntoConstraints = false
        MoviePosterImageView.topAnchor.constraint(equalTo: topAnchor).isActive = true
        MoviePosterImageView.bottomAnchor.constraint(equalTo: bottomAnchor).isActive = true
        MoviePosterImageView.leftAnchor.constraint(equalTo: leftAnchor).isActive = true
        MoviePosterImageView.rightAnchor.constraint(equalTo: rightAnchor).isActive = true
    }
    func updateCell(posterURL: String?){
        if let posterURL = posterURL {
            guard let CompleteURL = URL(string: "https://image.tmdb.org/t/p/w500/\(posterURL)") else {return}
            self.MoviePosterImageView.sd_setImage(with: CompleteURL)
        }
       
    }
}
```

Ici, nous créons notre cellule de vue de collection personnalisée en sous-classant la classe UICollectionView et en implémentant les fonctions `init()`.

Nous créons un UIImageView pour afficher l'image de l'affiche du film et configurons les contraintes d'auto-layout pour celui-ci. Ensuite, nous créons une fonction personnalisée qui prend la chaîne URL de l'affiche du film comme paramètre et la télécharge de manière asynchrone sans affecter le thread UI/Main thread. Elle le fait en utilisant le CocoaPod SD WebImage que nous avons ajouté précédemment.

## Comment configurer notre API

Avant de continuer, vous devrez obtenir votre clé API pour l'API [TMDB](https://www.themoviedb.org/) en créant un compte (c'est gratuit). Nous allons utiliser le point de terminaison de recherche de films (Movie Search) de l'API qui prend la clé API et le nom du film comme paramètres.

```url
https://api.themoviedb.org/3/search/movie?api_key=VOTRE_CLE_API_ICI&query=batman

```

Vous pouvez examiner la réponse de l'API en l'exécutant dans Postman.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-22-at-8.52.57-PM.png)

## Comment créer un modèle pour la réponse API

Nous recevons maintenant une réponse JSON de l'API. Nous devons la décoder en Swift, ce que nous pouvons faire en créant une structure de modèle qui implémente le protocole Codable.

Nous pouvons générer facilement la structure du modèle pour notre réponse JSON en utilisant des sites Web de conversion JSON vers Swift. Voici le code du modèle pour la réponse de l'API – vous pouvez simplement le copier et le coller à l'intérieur du fichier Model.swift :

```swift
import Foundation

struct TrendingTitleResponse: Codable {
    let results: [Title]
}

struct Title: Codable {
    let id: Int
    let media_type: String?
    let original_name: String?
    let original_title: String?
    let poster_path: String?
    let overview: String?
    let vote_count: Int
    let release_date: String?
    let vote_average: Double
}

struct YoutubeSearchResponse: Codable {
    let items: [VideoElement]
}


struct VideoElement: Codable {
    let id: IdVideoElement
}


struct IdVideoElement: Codable {
    let kind: String
    let videoId: String
}


```

## Comment effectuer des requêtes HTTP en utilisant Swift

Maintenant, nous devons écrire du code Swift pour effectuer des requêtes HTTP GET qui renvoient la réponse JSON de l'API.

Swift fournit une classe URLSession qui facilite l'écriture de code réseau sans avoir besoin de bibliothèques tierces comme AFNetworking, AlamoFire, et ainsi de suite.

Ouvrez APIService.swift et ajoutez le code suivant :

```swift
import Foundation

class APIService{
    static var shared = APIService()
    let session = URLSession(configuration: .default)
    
    func getMovies(for Query: String,completion:@escaping([Title]?,Error?)->Void){
        guard let FormatedQuery = Query.addingPercentEncoding(withAllowedCharacters: .urlHostAllowed)  else{return}
        
        guard let  SEARCH_URL = URL(string: "https://api.themoviedb.org/3/search/movie?api_key=VOTRE_CLE_API_ICI&query=\(FormatedQuery)") else {print("INVALIDE")
            return}
        
        
        
        let task = session.dataTask(with: SEARCH_URL) { data, response, error in
            if let error = error {
                print(error.localizedDescription)
                completion(nil,error)
            }
            if let data = data {
                do{
                    let decodedData = try JSONDecoder().decode(TrendingTitleResponse.self, from: data)
                 //   print(decodedData)
                    completion(decodedData.results,nil)
                }
                catch{
                    print(error)
                }
            }
        }
        task.resume()
    }
}

```

Ici, nous avons créé une classe nommée API Service avec le pattern singleton, nous avons donc besoin d'une instance pour cette classe en tant que membre statique de la classe. Ensuite, nous avons créé une session pour notre tâche réseau avec la configuration par défaut, suivie d'une méthode personnalisée getMovies().

Ensuite, nous avons créé notre tâche réseau – dans ce cas, nous devons effectuer des requêtes HTTP GET qui peuvent être effectuées à l'aide de la méthode `dataTask()` de la classe URLSession. Elle prend l'URL comme paramètre et fournit un gestionnaire de complétion (completion handler) qui contient les données renvoyées par l'API, les données d'erreur si une erreur s'est produite, et une réponse qui contient les informations de réponse HTTP telles que les codes d'état et leurs messages correspondants.

S'il y a une erreur, nous sortons de cette fonction avec les données d'erreur. Sinon, nous décodons nos données JSON basées sur notre modèle Swift et sortons de cette fonction avec les données décodées.

## Comment afficher les résultats de la recherche sur l'UICollectionView

Dans HomeVC.swift, créez une propriété privée qui est un tableau d'objets Title. Ceux-ci contiendront les informations de chaque film renvoyées par l'API.

```swift
private var Movies = [Title]()
```

Dans HomeVC.swift, créez une extension pour la classe HomeVC et implémentez les protocoles UIColletionViewDelegate et UICollectionViewDatasource. Ensuite, implémentez numberOfItemsInSection (qui est égal au nombre de films renvoyés par l'API) et cellForItemAt (qui remplit réellement la cellule avec les réponses de l'API, comme le téléchargement et la définition de l'image de l'affiche).

```swift
 func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return Movies.count
    }
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        if let cell = collectionView.dequeueReusableCell(withReuseIdentifier: MovieCell.ID, for: indexPath) as? MovieCell{
           // cell.backgroundColor = .systemBackground
            
            cell.updateCell(posterURL: Movies[indexPath.row].poster_path)
            return cell
        }
        return UICollectionViewCell()
        
    }
```

Enfin, nous devons effectuer l'appel API réel, ce que nous faisons à l'intérieur de la méthode de délégué `updateSearchResults()` que nous avons implémentée précédemment. À l'intérieur de cette méthode, ajoutez le code suivant :

```swift
    func updateSearchResults(for searchController: UISearchController) {
        guard let query = searchController.searchBar.text else{return}
        APIService.shared.getMovies(for:query.trimmingCharacters(in: .whitespaces)) { titles, error in
            if let titles = titles {
                self.Movies = titles
                DispatchQueue.main.async {
                    self.MovieCollectionView.reloadData()
                }
       
            }
        }
        
    }
```

Ici, chaque fois que l'utilisateur tape dans la barre de recherche ou appuie sur le bouton de recherche, nous effectuons une requête HTTP GET pour récupérer un film (basé sur le nom saisi dans la barre de recherche). Ensuite, nous rechargeons la CollectionView qui met à jour les cellules de la vue de collection avec l'affiche du film.

Notez que nous devons faire cela dans le Main Thread/UI Thread, car par défaut iOS effectue automatiquement les requêtes HTTP dans un thread d'arrière-plan. Cela signifie que nous devons utiliser le thread UI/Main pour mettre à jour nos éléments UI.

Maintenant, lancez votre application dans le simulateur pour voir le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/ezgif.com-gif-maker--3-.gif)

Félicitations ! Vous avez appris à utiliser UISearchController dans les applications iOS.