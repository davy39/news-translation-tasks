---
title: Comment créer un flux d'authentification utilisateur sécurisé dans Flutter
  avec Firebase et la gestion d'état Bloc
subtitle: ''
author: Justice Nwogu
co_authors: []
series: null
date: '2023-11-21T15:21:20.000Z'
originalURL: https://freecodecamp.org/news/user-authentication-flow-in-flutter-with-firebase-and-bloc
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Group-1--3-.png
tags:
- name: BLoC
  slug: bloc
- name: Firebase
  slug: firebase
- name: Flutter
  slug: flutter
- name: 'State Management '
  slug: state-management
seo_title: Comment créer un flux d'authentification utilisateur sécurisé dans Flutter
  avec Firebase et la gestion d'état Bloc
seo_desc: 'User authentication is critical to mobile app development. It helps make
  sure that only authorized users can access sensitive information and perform actions
  within an application.

  In this tutorial, we will explore how to build secure user authentica...'
---

L'authentification des utilisateurs est cruciale pour le développement d'applications mobiles. Elle permet de s'assurer que seuls les utilisateurs autorisés peuvent accéder à des informations sensibles et effectuer des actions au sein d'une application.

Dans ce tutoriel, nous allons explorer comment créer une authentification utilisateur sécurisée dans Flutter en utilisant Firebase pour l'authentification et le modèle de gestion d'état Bloc pour gérer l'état de l'application. À la fin, vous aurez une solide compréhension de l'intégration de l'authentification Firebase et de la mise en œuvre d'un processus de connexion et d'inscription sécurisé en utilisant Bloc.

### Prérequis :

Pour tirer le meilleur parti de ce tutoriel, vous devez avoir les éléments suivants :

* Une bonne compréhension de Flutter et Dart
* Un compte Firebase : Créez un compte Firebase si vous n'en avez pas. Vous pouvez configurer un projet Firebase via la [Console Firebase](https://console.firebase.google.com/).

## **Comment fonctionne l'authentification Firebase**

L'authentification Firebase est un service puissant qui simplifie le processus d'authentification des utilisateurs dans votre application. Elle prend en charge diverses méthodes d'authentification, y compris l'email/mot de passe, les réseaux sociaux, et plus encore.

L'un des principaux avantages de l'authentification Firebase est ses fonctionnalités de sécurité intégrées, telles que le stockage sécurisé des informations d'identification des utilisateurs et le chiffrement des données sensibles.

## **Description du diagramme**

Visualisons le flux des actions à l'aide d'un diagramme pour comprendre le concept que vous allez apprendre. Jetez un coup d'œil au diagramme ci-dessous pour mieux comprendre :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Flowcharts.png)
_Img 1 : Le diagramme de l'application_

L'image ci-dessus est un diagramme pour visualiser le flux de l'application. Discutons de ce que représente chaque partie. Les rectangles arrondis représentent les points de départ et de fin du flux ; les rectangles violets représentent les écrans ; les rectangles bleus clair représentent les processus qui ont lieu ; et enfin, le losange représente la prise de décision.

* L'application commence à l'`AuthenticationFlowScreen`.
* Le `StreamBuilder` écoute les changements d'état d'authentification.
* Si un utilisateur est authentifié, il dirige vers le `HomeScreen` ; sinon, il mène à l'`SignupScreen`.
* `AuthenticationBloc` gère les événements et les états d'authentification de l'utilisateur.
* Lorsque l'utilisateur s'inscrit (l'événement `SignUpUser` est déclenché) :
* Il initie l'état de chargement de l'authentification (`AuthenticationLoadingState`).
* Appelle `signUpUser` depuis `AuthService` pour l'inscription de l'utilisateur.
* Si cela réussit, il émet `AuthenticationSuccessState` avec les données de l'utilisateur ; sinon, il émet `AuthenticationFailureState`.
* Lorsque l'utilisateur initie le processus de déconnexion (l'événement `SignOut` est déclenché) :
* Il commence l'état de chargement de l'authentification (`AuthenticationLoadingState`).
* Appelle `signOutUser` depuis `AuthService` pour déconnecter l'utilisateur.
* Si une erreur se produit pendant la déconnexion, il enregistre le message d'erreur.

## **Configuration du projet**

Pour commencer avec l'authentification Firebase, vous devez configurer Firebase dans votre projet Flutter.

Suivez ces étapes pour ajouter Firebase et bloc à votre projet :

### Ajouter des dépendances à votre projet

Ouvrez votre projet dans votre éditeur de code préféré.

Ajoutez les dépendances suivantes à votre fichier `pubspec.yaml` :

```yaml
dependencies:
firebase_core: ^2.20.0
firebase_auth: ^4.12.0
flutter_bloc: ^8.1.3

```

Ensuite, enregistrez le fichier `pubspec.yaml` pour récupérer les dépendances.

### Configurer Firebase

Créez un nouveau projet Firebase via la [Console Firebase](https://www.freecodecamp.org/news/p/9b9114d1-6fce-4349-a755-fdaa04b2d4ae/console.firebase.google.com). Cliquez sur l'authentification dans le projet, et suivez les instructions fournies.

Pour plus d'informations, vous pouvez consulter le site [Firebase](https://firebase.google.com/docs/auth).

### Initialiser Firebase

Tout d'abord, ouvrez le fichier `main.dart` dans le dossier `lib`.

Ajoutez le code suivant au fichier pour initialiser Firebase :

```dart

void main() async {
WidgetsFlutterBinding.ensureInitialized();
await Firebase.initializeApp(
  options: DefaultFirebaseOptions.currentPlatform
);

```

Le code ci-dessus montre le code pour exécuter l'application. Il n'y a rien d'inhabituel dans ce code, sauf que nous avons ajouté du code à `void main` pour initialiser Firebase.

### Le modèle utilisateur

Avant de créer la classe Firebase pour communiquer avec le service Firebase, définissons un UserModel pour représenter les données de l'utilisateur.

Commencez par créer un fichier `user.dart` dans le répertoire `lib` de votre projet.

Ajoutez ensuite le code ci-dessous dans le fichier :

```dart
class UserModel {
final String? id;
final String? email;
final String? displayName;
UserModel({ this.id, this.email, this.displayName, });
}

```

Maintenant que vous avez configuré Firebase et créé un modèle utilisateur, vous devez créer une classe de service pour communiquer directement avec Firebase.

### Le service d'authentification

Créez un dossier appelé `services`, créez un fichier dans ce dossier appelé `authentication.dart`. Vous pouvez maintenant ajouter ce code au fichier.

```dart
import 'package:firebase_auth/firebase_auth.dart';

import '../models/user.dart';

class AuthService {
  final FirebaseAuth _firebaseAuth = FirebaseAuth.instance;


  /// créer un utilisateur
  Future<UserModel?> signUpUser(
    String email,
    String password,
  ) async {
    try {
      final UserCredential userCredential =
          await _firebaseAuth.createUserWithEmailAndPassword(
        email: email.trim(),
        password: password.trim(),
      );
      final User? firebaseUser = userCredential.user;
      if (firebaseUser != null) {
        return UserModel(
          id: firebaseUser.uid,
          email: firebaseUser.email ?? '',
          displayName: firebaseUser.displayName ?? '',
        );
      }
    } on FirebaseAuthException catch (e) {
      print(e.toString());
    }
    return null;
  } 

   ///signOutUser 
   Future<void> signOutUser() async {
      final User? firebaseUser = FirebaseAuth.instance.currentUser;
    if (firebaseUser != null) {
      await FirebaseAuth.instance.signOut();
    }
  }
  // ... (autres méthodes)}
}

```

L'extrait de code ci-dessus est une méthode pour créer un utilisateur dans l'application en utilisant Firebase. Avec cette méthode, la méthode `signUpUser` prend deux paramètres de chaîne : `email` et `password` respectivement. Ensuite, vous appelez la méthode Firebase pour créer un utilisateur en utilisant les paramètres que nous avons ajoutés.

Maintenant que vous savez comment créer la méthode d'inscription, vous pouvez également créer la méthode de connexion. La classe représente finalement la communication entre Firebase et l'application.

La partie suivante consiste à connecter le service à votre gestion d'état, ce que nous allons voir comment faire maintenant.

## **Comment fonctionne la gestion d'état Bloc**

Bloc est un modèle de gestion d'état populaire pour Flutter qui aide à gérer les états complexes des applications de manière prévisible et testable. Bloc signifie "**Business Logic Component**" et il divise la logique métier et l'interface utilisateur. Bloc sera le pont entre votre application et Firebase.

Il existe une extension pour [VScode](https://marketplace.visualstudio.com/items?itemName=FelixAngelov.bloc) qui crée le code boilerplate pour Bloc. Vous pouvez utiliser l'extension pour accélérer le processus de développement.

### Configurer le Bloc d'authentification Firebase

Bloc se compose d'événements et d'états. Commençons par créer les états et les événements pour le Bloc. Ensuite, nous créerons un `AuthenticationBloc` qui gérera la logique en utilisant les événements, les états et le service que nous avons créés.

#### La classe `AuthenticationState`

La classe `AuthenticationState` est responsable des différents états du processus d'authentification. Comme nous le verrons dans le code, il existe des états initiaux, de chargement, de succès et d'échec pour nous assurer de savoir ce qui se passe pendant le processus d'authentification.

Tout d'abord, créez un fichier `authentication_state.dart` dans le répertoire `bloc` de votre projet.

```dart
part of 'authentication_bloc.dart';


abstract class AuthenticationState {
  const AuthenticationState();

  List<Object> get props => [];
}

class AuthenticationInitialState extends AuthenticationState {}

class AuthenticationLoadingState extends AuthenticationState {
 final bool isLoading;

  AuthenticationLoadingState({required this.isLoading});
}

class AuthenticationSuccessState extends AuthenticationState {
  final UserModel user;

  const AuthenticationSuccessState(this.user);
  @override
  List<Object> get props => [user];
}
class AuthenticationFailureState extends AuthenticationState {
  final String errorMessage;

  const AuthenticationFailureState(this.errorMessage);

  @override
  List<Object> get props => [errorMessage];
}

```

Analysons le code :

Classe abstraite `AuthenticationState` :

* `AuthenticationState` est la classe de base pour différents états où le processus d'authentification peut se trouver à tout moment.
* Elle contient une méthode `props` qui retourne une liste d'objets. Cette méthode est utilisée pour la vérification d'égalité lors de la comparaison des instances de cette classe.

Classe `AuthenticationInitialState` :

* `AuthenticationInitialState` représente l'état initial du processus d'authentification.

Classe `AuthenticationLoadingState` :

* `AuthenticationLoadingState` représente un état où le processus d'authentification est en cours, et l'interface utilisateur peut afficher un indicateur de chargement.
* Elle prend un paramètre booléen, `isLoading`, pour indiquer si le processus d'authentification est actuellement en cours de chargement ou non.

Classe `AuthenticationSuccessState` :

* `AuthenticationSuccessState` représente un état où le processus d'authentification a été complété.
* Elle inclut une propriété utilisateur de type UserModel représentant l'utilisateur authentifié.

Classe `AuthenticationFailureState` :

* `AuthenticationFailureState` représente un état où le processus d'authentification a échoué.
* Elle inclut une propriété `error message` contenant des informations sur l'échec.

#### La classe `AuthenticationEvent`

`AuthenticationEvent` est responsable des événements que `AuthenticationBloc` exécutera. Dans ce cas, il s'agit de l'événement de connexion. Vous pouvez écrire les autres événements, comme l'inscription et la déconnexion, ici.

Créez un fichier `authentication_Event.dart` dans le répertoire `bloc` de votre projet.

```dart
part of 'authentication_bloc.dart';



abstract class AuthenticationEvent {
  const AuthenticationEvent();

  List<Object> get props => [];
 
}

class SignUpUser extends AuthenticationEvent {
  final String email;
  final String password;

  const SignUpUser(this.email, this.password);

  @override
  List<Object> get props => [email, password];
}


class SignOut extends AuthenticationEvent {}

```

La classe `AuthenticationEvent` est similaire à `AuthenticationState`. Examinons le code pour voir ce qu'il fait :

Classe abstraite `AuthenticationEvent` :

* Il s'agit de la classe de base pour différents événements qui déclenchent des changements d'état d'authentification.

Classe `SignUpUser` :

* Cette classe représente un événement où un utilisateur tente de s'inscrire.
* Elle prend deux paramètres, `email` et `password`, représentant les informations d'identification que l'utilisateur utilise pour s'inscrire.
* Les instances de cette classe signaleront au `Bloc` qu'un utilisateur essaie de s'inscrire, et le `Bloc` peut répondre en initiant le processus d'inscription et en faisant la transition de l'état d'authentification en conséquence.

Classe `SignOut` :

* Les instances de cette classe signaleront au `Bloc` qu'un utilisateur essaie de se déconnecter. Le `bloc` peut répondre en initiant le processus de déconnexion et en mettant à jour l'état d'authentification en conséquence.

#### La classe `AuthenticationBloc`

Le `AuthenticationBloc` gérera l'état global de l'authentification, depuis ce qui se passe lorsqu'un utilisateur clique sur un bouton jusqu'à ce qui s'affiche à l'écran. Il interagit également directement avec le service Firebase que nous avons créé.

Tout d'abord, créez un fichier appelé `authentication_bloc.dart` dans le répertoire `bloc` de votre projet.

Ajoutez le code suivant pour définir la classe `AuthenticationBloc` :

```dart
import 'package:bloc/bloc.dart';
import 'package:meta/meta.dart';

import '../models/user.dart';
import '../services/authentication.dart';

part 'authentication_event.dart';
part 'authentication_state.dart';



class AuthenticationBloc extends Bloc<AuthenticationEvent, AuthenticationState> {
  final AuthService authService = AuthService();
  
  AuthenticationBloc() : super(AuthenticationInitialState()) {
    on<AuthenticationEvent>((event, emit) {});

    on<SignUpUser>((event, emit) async {
      emit(AuthenticationLoadingState(isLoading: true));
      try {
          final UserModel? user =
          await authService.signUpUser(event.email, event.password);
      if (user != null) {
        emit(AuthenticationSuccessState(user));
        
      } else {
        emit(const AuthenticationFailureState('création de l\'utilisateur échouée'));
      }
      } catch (e) {
        print(e.toString());
      }
     emit(AuthenticationLoadingState(isLoading: false));
    });

     on<SignOut>((event, emit) async {
      emit(AuthenticationLoadingState(isLoading: true));
      try {
        authService.signOutUser();
      } catch (e) {
        print('erreur');
        print(e.toString());
      } 
       emit(AuthenticationLoadingState(isLoading: false));
     });
}
}

```

Dans cet extrait de code, nous avons créé une instance de la classe `AuthService`, qui gère les opérations d'authentification des utilisateurs, telles que l'inscription et la déconnexion.

`on<SignUpUser>((event, emit) async { ... }` définit un gestionnaire pour l'événement `SignUpUser`. Lorsque cet événement est déclenché, le `bloc` passe par les étapes suivantes :

* Il émet un `AuthenticationLoadingState` pour indiquer que le processus d'authentification est en cours.
* Il appelle la méthode `signUpUser` du `authService` pour tenter de créer un compte utilisateur avec l'email et le mot de passe fournis.
* Si la création du compte utilisateur réussit (c'est-à-dire que l'utilisateur n'est pas null), il émet un `AuthenticationSuccessState` avec les données de l'utilisateur.
* Si la création du compte utilisateur échoue, il émet un `AuthenticationFailureState` avec un message d'erreur et enregistre l'erreur.
* Qu'il réussisse ou échoue, il émet un autre `AuthenticationLoadingState` pour signaler la fin du processus d'authentification.

`on<SignOut>((event, emit) async { ... }` définit un gestionnaire pour l'événement `SignOut`. Lorsque cet événement est déclenché, le `bloc` passe par les étapes suivantes :

* Il émet un `AuthenticationLoadingState` pour indiquer que le processus de déconnexion est en cours.
* Il appelle la méthode `signOutUser` du `authService` pour déconnecter l'utilisateur.
* Si des erreurs se produisent pendant le processus de déconnexion, il enregistre l'erreur.
* Il émet un autre `AuthenticationLoadingState` pour signaler la fin du processus de déconnexion.

Le `AuthenticationBloc` gère l'état du processus d'authentification, y compris les états de chargement, de succès et d'échec, en fonction des événements déclenchés par les actions de l'utilisateur. Le `authService` est responsable de l'exécution des opérations d'authentification réelles.

Avec le Bloc configuré, nous pouvons implémenter le flux d'authentification en utilisant Bloc.

## **Comment implémenter le flux d'authentification avec Bloc**

Pour implémenter le flux d'authentification, vous allez créer un widget Stateless dédié pour vérifier si un utilisateur est déjà connecté afin que nous sachions quel écran montrer à l'utilisateur. La page affichera différents écrans en fonction de l'état d'authentification de l'utilisateur.

### `AuthenticationFlowScreen` :

Créez un nouveau fichier appelé `authentication_page.dart` dans le répertoire `screens` de votre projet.

```dart
import 'package:bloc_authentication_flow/screens/home.dart';
import 'package:bloc_authentication_flow/screens/sign_up.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

class AuthenticationFlowScreen extends StatelessWidget {
  const AuthenticationFlowScreen({super.key});
  static String id = 'main screen';
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: StreamBuilder<User?>(
        stream: FirebaseAuth.instance.authStateChanges(),
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            return const HomeScreen();
          } else {
            return const SignupScreen();
          }
        },
      ),
    );
  }
}

```

Dans le code ci-dessus, vous avez un `StatelessWidget` avec un `StreamBuilder` comme enfant. Le `StreamBuilder` agit comme un juge, utilisant Firebase pour vérifier les changements d'état et si un utilisateur est connecté ou non. Si un utilisateur est connecté, il le dirige vers l'écran d'accueil, sinon il va à l'écran d'inscription.

Changez la route d'accueil en `AuthenticationFlowScreen` pour permettre à l'application de vérifier avant de router vers une page.

```dart
   home: const AuthenticationFlowScreen() 

```

### Écran d'inscription

Tout d'abord, créez un nouveau fichier appelé `sign_up.dart` dans le répertoire `screens`.

```dart
import 'package:bloc_authentication_flow/screens/home.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import '../bloc/authentication_bloc.dart';

class SignupScreen extends StatefulWidget {
  static String id = 'login_screen';

  const SignupScreen({
    Key? key,
  }) : super(key: key);

  @override
  State<SignupScreen> createState() => _SignupScreenState();
}

class _SignupScreenState extends State<SignupScreen> {
  // Text Controllers
  final emailController = TextEditingController();
  final passwordController = TextEditingController();

  @override
  void dispose() {
    emailController.dispose();
    passwordController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Connexion à votre compte',
          style: TextStyle(
            color: Colors.deepPurple,
          ),
        ),
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const SizedBox(height: 20),
            const Text('Adresse email'),
            const SizedBox(height: 10),
            TextFormField(
              controller: emailController,
              decoration: const InputDecoration(
                border: OutlineInputBorder(),
                hintText: 'Entrez votre email',
              ),
            ),
            const SizedBox(height: 10),
            const Text('Mot de passe'),
            TextFormField(
              controller: passwordController,
              decoration: const InputDecoration(
                border: OutlineInputBorder(),
                hintText: 'Entrez votre mot de passe',
              ),
              obscureText: false,
            ),
            const SizedBox(height: 10),
            GestureDetector(
              onTap: () {},
              child: const Text(
                'Mot de passe oublié ?',
                style: TextStyle(
                  color: Colors.deepPurple,
                ),
              ),
            ),
            const SizedBox(height: 20),
            BlocConsumer<AuthenticationBloc, AuthenticationState>(
              listener: (context, state) {
                if (state is AuthenticationSuccessState) {
                  Navigator.pushNamedAndRemoveUntil(
                    context,
                    HomeScreen.id,
                    (route) => false,
                  );
                } else if (state is AuthenticationFailureState) {
                  showDialog(
                      context: context,
                      builder: (context) {
                        return const AlertDialog(
                          content: Text('erreur'),
                        );
                      });
                }
              },
              builder: (context, state) {
                return SizedBox(
                  height: 50,
                  width: double.infinity,
                  child: ElevatedButton(
                    onPressed: () {
                      BlocProvider.of<AuthenticationBloc>(context).add(
                        SignUpUser(
                          emailController.text.trim(),
                          passwordController.text.trim(),
                        ),
                      );
                    },
                    child:  Text(
                      state is AuthenticationLoadingState
                            ? '.......',
                            : "S'inscrire",
                      style: TextStyle(
                        fontSize: 20,
                      ),
                    ),
                  ),
                );
              },
            ),
            const SizedBox(height: 20),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Text("Vous avez déjà un compte ? "),
                GestureDetector(
                  onTap: () {},
                  child: const Text(
                    'Connexion',
                    style: TextStyle(
                      color: Colors.deepPurple,
                    ),
                  ),
                )
              ],
            ),
          ],
        ),
      ),
    );
  }
}

```

Ce code est simplement une interface utilisateur de connexion avec deux champs de texte et un bouton surélevé. Le widget `BlocConsumer` enveloppe le bouton "S'inscrire" et écoute les changements dans l'état `AuthenticationBloc`. Lorsque l'utilisateur appuie sur le bouton, il envoie un événement au `AuthenticationBloc` pour initier le processus d'inscription de l'utilisateur.

En fonction de l'état d'authentification, ce bouton peut afficher différents retours ou naviguer vers un autre écran. Il vérifie les états `AuthenticationSuccessState`, `AuthenticationLoadingState` et `AuthenticationFailureState` pour répondre en conséquence.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/ezgif.com-video-to-gif--1-.gif)
_Img 2 : Un écran de connexion montrant un processus de connexion avec 2 des 3 états._

### Écran d'accueil

Créez un autre fichier appelé `home_screen.dart` dans le répertoire `screens` et ajoutez le code ci-dessous au fichier.

```dart
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import '../bloc/authentication_bloc.dart';

class HomeScreen extends StatelessWidget {
  static String id = 'home_screen';
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              'Bonjour Utilisateur',
              style: TextStyle(
                fontSize: 20,
              ),
            ),
            const SizedBox(
              height: 20,
            ),
            BlocConsumer<AuthenticationBloc, AuthenticationState>(
              listener: (context, state) {
                if (state is AuthenticationLoadingState) {
                   const CircularProgressIndicator();
                } else if (state is AuthenticationFailureState){
                    showDialog(context: context, builder: (context){
                          return const AlertDialog(
                            content: Text('erreur'),
                          );
                        });
                }
              },
              builder: (context, state) {
                return ElevatedButton(
                    onPressed: () {
                      BlocProvider.of<AuthenticationBloc>(context)
                      .add(SignOut());
                    }, child: const Text(
                      'Déconnexion'
                      ));
              },
            ),
          ],
        ),
      ),
    );
  }
}

```

Le code ci-dessus représente l'`HomeScreen` et c'est aussi une page simple qui consiste en un scaffold, une colonne et un widget de texte, mais la partie intéressante est le `BlocConsumer` qui se trouve au niveau du bouton surélevé qui dit Déconnexion. Examinons cela de plus près.

Le `BlocConsumer` écoute les changements d'état provenants du `AuthenticationBloc`. Il a deux paramètres - listener et builder.

* **listener** : Écoute les changements d'état et réagit en fonction de l'état actuel reçu du `AuthenticationBloc`.
* Si l'état est `AuthenticationLoadingState`, il affiche un `CircularProgressIndicator`.
* Si l'état est `AuthenticationFailureState`, il affiche un `AlertDialog` avec le message 'Erreur'.
* **builder** : Construit l'interface utilisateur en fonction de l'état actuel reçu du `AuthenticationBloc`.
* Il rend un `ElevatedButton` étiqueté "Déconnexion".
* Lorsqu'il est pressé, il déclenche l'événement `SignOut` dans le `AuthenticationBloc` via BlocProvider.

Avec le flux d'authentification Bloc implémenté, vous pouvez exécuter votre application Flutter et tester les fonctionnalités d'enregistrement. Assurez-vous de gérer d'autres scénarios liés à l'authentification, tels que la connexion de l'utilisateur et la récupération du mot de passe, comme requis par les spécifications de votre application. De plus, vous voudrez gérer les erreurs avec élégance pour offrir une bonne expérience à l'utilisateur.

Si vous souhaitez cloner le dépôt, vous pouvez le consulter sur GitHub [ici](https://github.com/emjaycodes/bloc_authentication_flow_article) et laisser un like.

## **Conclusion**

Dans cet article, nous avons exploré la création d'un flux d'authentification utilisateur dans Flutter en utilisant Firebase pour l'authentification et le modèle de gestion d'état Bloc pour gérer l'état de l'application.

Nous avons appris comment configurer Firebase dans un projet Flutter, créer des Blocs pour l'authentification et implémenter le flux d'authentification en utilisant Bloc.

En tirant parti de la puissance de Firebase et de la prévisibilité de Bloc, vous pouvez garantir une expérience d'authentification utilisateur sécurisée et transparente dans vos applications Flutter.