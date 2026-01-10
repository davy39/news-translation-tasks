---
title: Pagination infinie dans Flutter avec Firebase, Riverpod et Freeze
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-14T23:46:42.000Z'
originalURL: https://freecodecamp.org/news/infinite-pagination-in-flutter-with-riverpod
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/Firebase-Security-Rules-Introduction--1-.png
tags:
- name: app development
  slug: app-development
- name: Flutter
  slug: flutter
seo_title: Pagination infinie dans Flutter avec Firebase, Riverpod et Freeze
seo_desc: "By Rutvik Tak\nWhen you're developing an app, you'll have to decide how\
  \ you want to load data. And this will typically bring up the issue of infinite\
  \ pagination. \nYou likely won't be showing all of the available items in your DB\
  \ to your users. You may..."
---

Par Rutvik Tak

Lorsque vous développez une application, vous devrez décider comment vous souhaitez charger les données. Et cela soulèvera généralement la question de la pagination infinie. 

Vous ne montrerez probablement pas tous les éléments disponibles dans votre base de données à vos utilisateurs. Vous pouvez récupérer les 10 à 20 premiers éléments et charger les suivants au fur et à mesure que l'utilisateur fait défiler. 

Cela permet non seulement d'éviter des lectures inutiles sur votre base de données, mais améliore également les performances car vous chargez les éléments à la demande.  
  
Bien faire cela est crucial si vous essayez de construire des applications de haute qualité. J'ai eu l'occasion de travailler sur une application B2B pour l'un de mes clients, et avoir une bonne expérience de pagination était essentiel pour notre application – à la fois en termes d'opérations de récupération et d'expérience utilisateur.

Dans ce tutoriel, je vais vous guider à travers l'approche que j'ai adoptée afin que vous puissiez construire cette fonctionnalité dans vos propres applications.  
  
Cet article s'adresse aux lecteurs qui ont déjà une compréhension de base des Slivers Flutter, Firebase, Riverpod et Freezed et qui souhaitent les utiliser pour construire quelque chose de cool. 

Cela ressemble moins à un tutoriel et est plutôt quelque chose que je voulais partager et que je pense être une approche intéressante de l'implémentation de la pagination avec ces packages. 

Une fois que vous comprendrez les raisons derrière ces implémentations, vous pourrez peut-être les reproduire avec d'autres solutions de gestion d'état et de base de données de votre choix. 

De plus, j'ai essayé de rendre les choses aussi claires que possible tout en restant dans le cadre de l'article et j'ai ajouté des liens vers des articles/documentations de support à suivre.

## Ce que nous allons couvrir ici :

1. Aperçu des outils/packages que nous utilisons
2. Décomposition des fonctionnalités
3. Comment récupérer et limiter les éléments
4. Comment récupérer les données lors du défilement
5. Comment mettre en cache ou stocker les éléments récupérés
6. Comment gérer les OnGoingStates
7. Quelques améliorations que vous pouvez apporter

## Voici les outils et packages que nous allons utiliser :

* **[Cloud Firestore](https://firebase.google.com/docs/firestore)** : Solution de base de données NoSQL de Firebase.
* **[Riverpod](https://riverpod.dev/)** : une bibliothèque de gestion d'état de l'auteur de Provider.
* **[Freezed](https://pub.dev/packages/freezed)** : un générateur de code pour les unions/pattern-matching/copy. Communément utilisé pour générer des modèles de classe avec des méthodes from et to json. 

Et voici le code source si vous souhaitez y jeter un coup d'œil : [Pagination infinie dans Flutter avec Riverpod, Freezed, Firebase](https://github.com/rutvik110/infinite_pagination).

## Décomposition des fonctionnalités

Pour faciliter la compréhension et le travail, j'essaie toujours de les décomposer en leurs différents états. De cette façon, vous obtiendrez l'idée abstraite de ce qui se passe et nous pourrons gérer chaque tâche une par une afin de ne pas être submergés.  
  
Notre fonctionnalité de pagination a les différents états suivants :

### États de récupération initiaux

Voici à quoi devraient ressembler les états de chargement, de données et d'erreur :

![Image](https://www.freecodecamp.org/news/content/images/2024/08/loadingState-1.gif)
_Chargement initial_

![Image](https://www.freecodecamp.org/news/content/images/2024/08/dataState-1.gif)
_Données chargées_

![Image](https://www.freecodecamp.org/news/content/images/2024/08/errorState-1.gif)
_État d'erreur_

###   
Après les états de première récupération (OnGoingStates)

Voici à quoi devraient ressembler les états OnGoingLoading, OnGoingData et OnGoingError :

![Image](https://www.freecodecamp.org/news/content/images/2024/08/onGoingLoadingState-3.gif)
_État OnGoingLoading_

![Image](https://www.freecodecamp.org/news/content/images/2024/08/onGoingDataState-2.gif)
_État OnGoingData_

![Image](https://www.freecodecamp.org/news/content/images/2024/08/onGoingErrorState-2.gif)
_État OnGoingError_

D'accord, maintenant que nous avons vu à quoi ressembleront nos différents états, plongeons-nous dedans.

## Comment récupérer et limiter les données 

J'ai une application d'exemple en cours d'exécution – elle ne fait rien de spécial sauf récupérer les données telles qu'elles sont de Firebase. 

Nous utilisons [Slivers pour le comportement de défilement](https://docs.flutter.dev/development/ui/advanced/slivers) et nous utilisons [Consumer de Riverpod](https://riverpod.dev/docs/concepts/reading/#consumer-and-hookconsumer-widgets) pour charger les données via un fournisseur de futur qui récupère les éléments de Firebase. J'ai déjà ajouté des données dans Firebase (*Firestore), donc nous allons simplement utiliser cela.

Chargement des éléments via Consumer :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/initial_paginatedview-1.png)
_Chargement des éléments initiaux via un consumer en utilisant Slivers_

  
Déclaration des fournisseurs :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/init_providers.png)
_Déclaration du fournisseur de classe de base de données et du futureProvider qui retourne les éléments de la base de données._

  
Ma classe MyDatabase :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/MyDatabase_initiali.png)
_Classe de base de données avec une méthode appelée fetchItems() qui récupère les éléments d'une collection Firestore appelée "items" et les retourne._

Voici un aperçu de ce à quoi cela ressemblera :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/fetching_all_items-1.gif)
_Chargement des éléments de Firebase dans l'application. Affichage du chargement initial, des états de données._

Comme vous pouvez le voir, nous récupérons tout ce qui est disponible, ce qui n'est pas très bon ! Nous voulons limiter le nombre d'éléments que nous récupérons. 

Nous pouvons le faire en utilisant **`.limit(n)`** sur notre requête Firebase. Nous allons définir cette limite à 20 éléments et ordonner nos éléments par le champ **createdAt** dans l'ordre décroissant. 

![Image](https://www.freecodecamp.org/news/content/images/2022/02/limiting_items.png)
_Limitation du nombre d'éléments récupérés à l'aide de .limit(n) et ordonnancement des éléments en fonction de la valeur "createdAt"._

Maintenant, nous ne récupérons que les 20 éléments les plus récents de notre base de données. 👍   
  
L'ordonnancement des éléments par rapport à un champ qui est unique et qui peut être utilisé pour trier est important ici. C'est l'une des façons de paginer les éléments. Cela s'appelle également la pagination basée sur le curseur.

### Comment ajouter le mécanisme pour le rappel de défilement 

Pour obtenir les informations sur le défilement, nous allons créer un ScrollController et le passer à notre CustomScrollView.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/adding_scroll_controller-1.png)
_Ajout de ScrollListener et écoute des événements de défilement pour faire un appel lorsque la position de défilement est proche de la fin de la liste des éléments._

* **maxScroll** : Quantité maximale de distance que l'utilisateur peut faire défiler dans l'axe de défilement.
* **currentScroll** : Position actuelle de l'utilisateur dans la vue de défilement.
* **delta** : Quantité d'espace depuis le bas.

Nous allons écouter les événements de défilement, et lorsque la différence entre **maxScroll** et **currentScroll** devient inférieure à **delta**, nous faisons l'appel pour récupérer le lot suivant d'éléments.

## Comment stocker et récupérer le lot suivant

Cela va être intéressant. Voyons ce que nous devons gérer ici :

1. Comment stocker les éléments déjà récupérés.
2. Comment construire la logique pour récupérer le lot suivant d'éléments en fonction de ce que nous avons récupéré précédemment.

Pour gérer ces deux fonctionnalités, nous allons utiliser [StateNotifiersProvider](https://riverpod.dev/docs/providers/state_notifier_provider/) dans Riverpod. Les utiliser nous aidera à séparer notre logique d'implémentation principale de la couche UI et nous donnera plus de flexibilité dans la gestion des différents états de récupération et la construction de la logique pour les appels de récupération.

C'est également la solution recommandée par Riverpod pour gérer l'état qui peut changer en réaction à l'interaction de l'utilisateur.

Voici le fournisseur d'éléments mis à jour :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/itemsProvider.png)
_Fournisseur d'éléments mis à jour en StateNotifierProvider qui crée un PaginationNotifier avec le nombre initial d'éléments et le rappel fetchNextItems._

Voici PaginationStateNotifier :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/paginated_state_notifier-1.png)
_PaginationNotifier qui contiendra les éléments récupérés et gérera toute la logique liée aux différents états de pagination et aux rappels de récupération._

Dans ce code, nous avons créé notre **PaginationNotifier** en l'étendant à la classe StateNotifier. Nous l'avons rendu générique en représentant le type avec **T** pour le rendre réutilisable. 

Alors, laissez-moi passer en revue les choses ici :

* **_items** : Tous les éléments récupérés sont ajoutés à cette liste.
* **itemsPerBatch** : Nombre maximal d'éléments dans un lot. Identique au nombre que nous avons défini dans la limite de la requête firebase dans le backend.
* **fetchItems (T? item)** : Cette fonction sera celle qui fera réellement l'appel pour récupérer les éléments, et elle accepte un élément nullable. Cet **item** est le dernier élément de la liste **_items**. Si c'est la première fois que nous récupérons des éléments ou si **_items** est vide, alors il sera **null**. 
* **fetchFirstBatch()** : Récupérera le premier lot d'éléments et mettra à jour l'état.
* **fetchNextBatch()** : Récupérera le lot suivant d'éléments et mettra à jour l'état. L'implémentation est presque la même que **fetchFirstBatch** pour l'instant, à l'exception de deux choses importantes :  
– Tout d'abord, nous mettons à jour l'état en **.data(_items)**. Cela est dû au fait que nous voulons toujours montrer les éléments précédemment récupérés pendant que le lot suivant est en cours de chargement.  
– Deuxièmement, nous passons le dernier élément de la liste **_items** lors de l'appel pour récupérer les éléments. Cette section s'améliorera dans la section suivante où nous ajouterons des OnGoingStates pour gérer cela mieux.
* **init()** : Appelé lorsque le notifier est initialisé. Nous faisons simplement l'appel pour récupérer le premier lot ici si les éléments sont vides.

Maintenant, voyons ce que nous devons mettre à jour dans la logique backend :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/MyDatabase_final-1.png)
_Méthode fetchItems de la classe de base de données mise à jour pour récupérer les 20 éléments suivants en fonction du dernier élément récupéré._

Donc, nous acceptons un élément ici maintenant. Si l'élément est null, nous récupérons les 20 premiers éléments. Si ce n'est pas le cas, alors nous utilisons un filtre **.startAfter()** sur notre requête, qui dit essentiellement : "Hey ! Je veux les éléments qui commencent après l'élément qui correspond à cette valeur que j'envoie. Cool !"

Une réponse un peu plus professionnelle ici : 😅

> [startAfter()](https://firebase.google.com/docs/firestore/query-data/query-cursors) : Prend une liste de [valeurs], crée et retourne une nouvelle [Query] qui commence après les champs fournis par rapport à l'ordre de la requête. (D'après la documentation Firebase)

Côté UI, nous n'aurons rien à changer. Exécutons cela et voyons ce que nous obtenons !

![Image](https://www.freecodecamp.org/news/content/images/2022/02/ezgif.com-gif-maker.gif)
_Chargement des éléments suivants à la demande lorsque l'utilisateur fait défiler vers la fin de la liste des éléments._



Super ! Nous chargeons les lots suivants au fur et à mesure que nous faisons défiler vers la fin de la liste. N'est-ce pas cool ? 😁

Maintenant, nous voulons travailler sur l'affichage. Nous voulons montrer un indicateur de chargement ou d'erreur en cours au bas de notre liste qui représentera les OnGoingStates.

## Comment gérer les états en cours

Alors, comment gérons-nous ces OnGoingStates et les représentons-nous à l'utilisateur ?  
  
Eh bien, cela n'a pas de réponse unique. Une approche consiste à créer une variable dans StateNotifier qui représente ces états sous forme d'énumération et les met à jour pour indiquer les OnGoingStates. C'est ce que j'ai fait dans ma première itération, et cela s'est avéré ne pas être une très bonne approche. 

Alors, au lieu de cela, passons à la chose qui a fonctionné pour moi.  
  
Comme nous avons plus de trois états à gérer ici, pourquoi ne pas créer notre propre version de AsyncValue qui inclura deux états supplémentaires appelés OnGoingLoading et OnGoingError ? AsyncValue est simplement une union qui mappe à différents états. Nous pourrions créer quelque chose de similaire.

Nous pouvons le faire en utilisant [Freezed](https://pub.dev/packages/freezed), qui est une bibliothèque de génération de code pour créer des unions et bien plus encore. 

![Image](https://www.freecodecamp.org/news/content/images/2022/02/pagination_state.png)
_Création de notre union PaginationState personnalisée avec Freezed._

  
Les trois premiers états ici sont explicites – ce sont les états réguliers avec lesquels vous interagissez lorsque vous utilisez AsyncValue.  
  
Comme nos états OnGoingLoading et OnGoingError se produisent après notre premier appel, nous voulons également afficher les éléments précédemment récupérés dans cet état, donc nous avons le paramètre items. Et un paramètre d'erreur et de trace de pile supplémentaire pour l'état OnGoingError.

Je crois que de cette manière, nous sommes plus déclaratifs sur ce que nous faisons à la fois sur les côtés UI et logique métier. De plus, la représentation pour l'utilisateur devient assez facile et propre avec cela.  
  
Maintenant, mettons à jour notre StateNotifier pour utiliser cet nouvel objet PaginationState au lieu de AsyncValue.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/adding_ongoing_states-2.png)
_PaginationNotifier mis à jour pour utiliser PaginationState au lieu de AsyncValue._

Dans la fonction **fetchNextBatch**, nous mettrons à jour notre état en **.onGoingLoading** et **.onGoingError** en remplaçant les états **.data()** et **.error()**.

Côté UI, vous verrez quelques erreurs de compilation. Nous devrons également gérer ces deux nouveaux états dans notre Consumer.

PaginatedListView mis à jour :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/paginatedlistview-5.png)
_Code UI mis à jour pour PaginatedListView_

ItemsList : J'ai donc extrait ma logique de chargement des éléments dans son widget séparé.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/itemslist.png)
_Code UI mis à jour pour ItemsList gérant maintenant les états initiaux et en cours._

ItemsListBuilder : Et la logique de construction de la liste des éléments ou SliverList est également extraite dans son propre widget, ce qui la rend réutilisable dans différents états de pagination.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/itemslistbbuilder.png)
_Builder qui construit la liste sliver des éléments._

  
L'étape finale qui reste est l'ajout de cet indicateur de chargement/erreur en bas de la **ItemsList.** 

Pour cela, nous allons simplement ajouter un autre consumer qui ne gérera que les états **OnGoingLoading** et **OnGoingError.**

![Image](https://www.freecodecamp.org/news/content/images/2022/02/adding_ongoing_bottom_widget.png)
_Ajout de OnGoingBottomWidget sous notre liste d'éléments qui montre un message approprié en fonction de l'état en cours._

Nous y voilà ! Cela a l'air beaucoup mieux.

Voyons cela en action dans un simulateur iOS montrant la gestion des différents états de pagination en cours : 🚀

![Image](https://www.freecodecamp.org/news/content/images/2024/08/onGoingLoadingState-4.gif)

![Image](https://www.freecodecamp.org/news/content/images/2024/08/onGoingDataState-3.gif)

![Image](https://www.freecodecamp.org/news/content/images/2024/08/onGoingErrorState-3.gif)

## Quelques améliorations que vous pouvez apporter

Maintenant que nous avons une application fonctionnelle avec pagination, les prochaines étapes consistent à améliorer ce que nous avons fait jusqu'à présent. 

Cela inclut des choses liées à la limitation de nos appels de récupération lorsqu'il y a déjà un appel de récupération en cours, à la temporisation des appels dans une certaine durée, et à informer l'utilisateur s'il a atteint la fin de la liste et qu'il n'y a plus d'éléments à afficher.

De plus, qui ne veut pas d'un bouton de défilement vers le haut 😅.

### Comment rejeter les requêtes concurrentes

Tout d'abord, nous allons rejeter toute requête concurrente qui se produit dans une certaine durée après qu'une requête a été faite. Nous pouvons le faire en créant un minuteur et en vérifiant si ce minuteur est actif à chaque requête. Si c'est le cas, nous rejetons la requête, sinon nous procédons et réinstancions le minuteur. 

Deuxièmement, nous pouvons également vérifier notre état – si nous traitons déjà la requête précédente, alors nous rejetons la requête entrante. Pour cela, nous pouvons simplement vérifier si notre état est égal à l'état de chargement et gérer cela.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/adding_timer_with_state_check.png)
_Ajout d'un minuteur et vérification de l'état pour temporiser tout appel immédiat après qu'un appel a été fait ou lorsque l'état est en cours de chargement._

### A atteint la fin de la liste (plus d'éléments à récupérer)

Nous pouvons maintenir un booléen qui indique cela. Chaque fois que nous obtenons nos résultats, nous pouvons vérifier si les résultats sont inférieurs à notre compte **itemsPerBatch**. 

Côté UI, nous pouvons présenter un message approprié en fonction de cela. Voici le notifier de pagination mis à jour :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/nomoreitems_addition.png)
_Déclaration d'un booléen noMoreItems pour savoir quand il n'y a plus d'éléments à récupérer._

Et le code UI mis à jour : 

![Image](https://www.freecodecamp.org/news/content/images/2022/03/noMoreItems.png)
_Affichage d'un message approprié en fonction de l'état du booléen noMoreItems._

![Aucun autre élément trouvé !](https://www.freecodecamp.org/news/content/images/2022/03/nomoreitems.gif)
_Démo Aucun autre élément trouvé._

### Comment ajouter un bouton de défilement vers le haut

Ces boutons sont utiles et évitent à l'utilisateur de faire défiler une grande quantité de contenu. Voici comment nous pouvons en implémenter un dans notre application : 

![Image](https://www.freecodecamp.org/news/content/images/2022/03/scroll_to_top_button_addition.dart.png)
_Ajout d'un bouton ScrollToTop_

Nous utilisons AnimatedBuilder pour écouter les mises à jour de défilement. AnimatedBuilder accepte un objet listenable et comme notre ScrollController est en fait un ChangeNotifier qui implémente Listenable, nous pouvons le passer ici.

Si le **décalage de défilement** est supérieur à une certaine valeur, alors nous affichons le bouton **ScrollToTop**. Lorsqu'il est appuyé, nous animons le défilement vers le haut.  


![Image](https://www.freecodecamp.org/news/content/images/2022/03/scroll_to_top.gif)
_Démo montrant l'utilisation du bouton ScrollToTop ajouté ci-dessus._

## Résumé

Cela conclut notre article ! Voici quelques-unes des choses que vous avez apprises dans cet article :

* Comment gérer les différents états de pagination efficacement avec Riverpod et Freezed.
* Comment utiliser la technique de pagination basée sur le curseur avec Firebase. La même chose peut être appliquée à la base de données que vous utilisez avec seulement des changements dans la fonction de récupération backend. Les autres implémentations restent les mêmes. 

**Encore une fois, voici le code source :** [Pagination infinie dans Flutter avec Riverpod, Freezed, Firebase](https://github.com/rutvik110/infinite_pagination)

J'espère que vous avez apprécié l'article. ☺️ C'était mon premier article ici sur freeCodeCamp et j'ai vraiment apprécié l'écrire. Cela a pris 😅 beaucoup plus de temps à écrire que je ne l'avais imaginé, mais finalement, il est là pour que vous puissiez le lire ! 👍 

J'espère écrire plus d'articles comme celui-ci 👨‍💻 ainsi que quelques défis de design Flutter 🧑‍🎨 alors que j'explore moi-même le développement d'applications en tant que développeur en croissance et que je vous apporte des choses intéressantes ! 😁

Je suis également actif sur Twitter [@TakRutvik](https://twitter.com/TakRutvik) 💙 en partageant mes créations et les choses sur lesquelles j'ai travaillé. N'hésitez pas à me contacter ☺️.