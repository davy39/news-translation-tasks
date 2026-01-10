---
title: Comment ajouter rapidement l'authentification à vos applications Flutter avec
  Supabase Auth UI
subtitle: ''
author: Fatuma Abdullahi
co_authors: []
series: null
date: '2024-06-03T19:55:22.000Z'
originalURL: https://freecodecamp.org/news/add-auth-to-flutter-apps-with-supabase-auth-ui
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/supa-auth-2.png
tags:
- name: authentication
  slug: authentication
- name: Flutter
  slug: flutter
- name: supabase
  slug: supabase
seo_title: Comment ajouter rapidement l'authentification à vos applications Flutter
  avec Supabase Auth UI
seo_desc: In this article, you will learn how to use Supabase's auth package to quickly
  and efficiently add authentication functionality to your Flutter apps. We will go
  through the entire process, from setting up a Flutter project to configuring Email/Passwor...
---

Dans cet article, vous apprendrez à utiliser le [package d'authentification](https://pub.dev/packages/supabase_auth_ui) de Supabase pour ajouter rapidement et efficacement des fonctionnalités d'authentification à vos applications Flutter. Nous passerons par l'ensemble du processus, de la configuration d'un projet Flutter à la configuration des flux Email/Mot de passe, OAuth et Magic link.

À la fin, vous aurez un système d'authentification complet avec thématiques, localisation et support natif.

## Table des matières

<ul>
<li>
        <a href="#prerequis">Prérequis</a>
    </li>
    <li>
        <a href="#quest-ce-que-supabase-auth-ui">Qu'est-ce que Supabase Auth UI</a>
    </li>
    <li>
		<a href="#methodes-dauthentification-prises-en-charge
        ">Méthodes d'authentification prises en charge
        </a>
	</li>
    <li>
		<a href="#comment-configurer-un-projet-flutter
        ">Comment configurer un projet Flutter
        </a>
	</li>

    <li>
		<a href="#comment-se-connecter-a-un-projet-supabase
        ">Comment se connecter à un projet Supabase
        </a>
	</li>
    <li>
		<a href="#comment-implementer-lauthentification-dans-une-application-flutter
        ">Comment implémenter l'authentification dans une application Flutter
        </a>
	</li>

    <li>
        <a href="#comment-configurer-lauthentification-supabase-email-et-fournisseur-oauth
                 ">Comment configurer l'authentification Supabase Email et fournisseur OAuth
        </a>
        <ul>
            <li><a href="#comment-configurer-github-comme-fournisseur-oauth">Comment configurer GitHub comme fournisseur OAuth</a>
			</li>
            <li><a href="#comment-configurer-google-comme-fournisseur-oauth">Comment configurer Google comme fournisseur OAuth</a>
            </li>
        </ul>
</li>


<li><a href="#comment-connecter-un-utilisateur-en-utilisant-le-package-auth-ui
    ">Comment connecter un utilisateur en utilisant le package Auth UI
    </a></li>

<li><a href="#comment-ajouter-lauthentification-par-lien-magique
    ">Comment ajouter l'authentification par lien magique
    </a></li>
<li><a href="#support-dauthentification-native-comment-se-connecter-avec-google
    ">Support d'authentification native - Comment se connecter avec Google
    </a></li>

   <li>
        <a href="#comment-thematiser-votre-supabase-auth-ui
                 ">Comment thématiser votre Supabase Auth UI
        </a>
        <ul>
            <li><a href="#options-de-mise-en-page-flexibles">Options de mise en page flexibles</a>
			</li>
            <li><a href="#localisation-et-traduction-pretes">Localisation et traduction prêtes</a>
            </li>
        </ul>
</li>



    <li>
        <a href="#resume">
            Résumé
        </a>
    </li>
  <li>
        <a href="#ressources">
            Ressources
        </a>
    </li>

</ul>

## 

## Prérequis

Cet article suppose que vous avez :

* Une compréhension de base de [Flutter](https://docs.flutter.dev/)
* Flutter [installé](https://docs.flutter.dev/get-started/install) et prêt à l'emploi
* Une compréhension de base des [concepts de Backend-as-a-Service](https://www.cloudflare.com/en-gb/learning/serverless/glossary/backend-as-a-service-baas/)
* Une compréhension de base de [l'authentification](https://www.freecodecamp.org/news/set-up-authentication-in-apps-with-supabase/)
* Un IDE (Environnement de Développement Intégré) ou un [éditeur de texte](https://code.visualstudio.com/download) pour travailler

## Qu'est-ce que Supabase Auth UI ?

Supabase Auth UI est un package Flutter open-source soutenu par la communauté qui offre des widgets préconfigurés et thématiques pour simplifier le processus de création de formulaires d'authentification.

Et ce n'est pas tout ? Il est prêt pour la traduction.

## Méthodes d'authentification prises en charge

L'interface utilisateur d'authentification Supabase prend en charge les méthodes d'authentification suivantes dès la sortie de la boîte :

* Liens magiques
* Authentification par email et mot de passe
* Authentification OAuth/connexion sociale
* Se connecter avec Google
* Se connecter avec Apple

## Comment configurer un projet Flutter

La première chose dont vous aurez besoin est un projet Flutter configuré. Ouvrez votre éditeur de texte préféré à l'emplacement où vous souhaitez conserver le projet Flutter, puis ouvrez le terminal intégré et exécutez `flutter create auth_example`. Cela créera un dossier appelé "auth_example" au même endroit.

Ouvrez le dossier nouvellement créé et collez ce qui suit dans le fichier `pubspec.yaml` dans le cadre des dépendances : `supabase_auth_ui: ^0.4.4`. 

Le fichier devrait ressembler à ceci :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1716931528734/b4e92507-4427-4945-a74e-de8edd0c1107.png)
_Un extrait de code montrant un fichier `pubspec.yaml` de Flutter avec des dépendances. La dépendance `supabase_auth_ui` est mise en évidence avec une flèche rose, indiquant la version `^0.4.4`._

De retour dans le terminal intégré, exécutez `cd auth_example` pour changer de dossier, puis exécutez `flutter pub get` pour obtenir la dépendance d'authentification dans votre projet.

## Comment se connecter à un projet Supabase

Allez dans votre tableau de bord Supabase ou [créez un compte](https://supabase.com/) si vous n'en avez pas. Dans le tableau de bord, allez dans les paramètres du projet en bas, puis cliquez sur API sous configuration. Copiez l'URL et la clé anon du projet du côté droit de la page comme illustré ci-dessous :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1716932440241/1f5c49a5-5ef8-449f-8bec-557e0492e950.png)
_Une capture d'écran de la page des paramètres de l'API dans le tableau de bord Supabase. La barre latérale gauche montre diverses options de menu sous "Paramètres du projet", "Configuration" et "Facturation". L'option "API" sous "Configuration" est mise en évidence. La section principale affiche les champs pour "URL du projet" et "Clés API du projet", avec des options pour copier ou révéler les clés._

De retour dans votre application Flutter, créez un fichier `.env` à la racine du dossier et collez ce qui suit, en remplaçant par les valeurs que vous avez copiées ci-dessus :

```bash
SUPABASE_URL=votre_url
SUPABASE_ANON_KEY=votre_clé_anon_projet
```

Ajoutez le fichier d'environnement au fichier .`gitignore` pour le garder hors du contrôle de version, puis ajoutez le package `flutter_dotenv` à la liste des dépendances juste en dessous de la dépendance `supabase_auth_ui`. Enfin, ajoutez le fichier `.env` comme chemin sous la clé des assets dans le fichier pubspec.yaml. 

Le fichier devrait ressembler à ceci :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1716933569314/2beb83cc-f8fc-406a-ac39-dedb5d32d42d.png)
_Une capture d'écran d'un éditeur de code affichant un fichier `pubspec.yaml` pour un projet Flutter. Le fichier liste les dépendances telles que `flutter`, `supabase_auth_ui` et `flutter_dotenv`. Deux flèches roses pointent vers les dépendances `supabase_auth_ui: ^0.4.4` et `flutter_dotenv: ^5.1.0`. Le fichier comprend également des sections pour `dev_dependencies`, `flutter_lints` et `assets`._

Dans le fichier `main.dart`, remplacez la fonction `main` par le code suivant :

```dart
void main() async {
  await dotenv.load(fileName: ".env");
  await Supabase.initialize(
      url: dotenv.env['SUPABASE_URL']!,
      anonKey: dotenv.env['SUPABASE_ANON_KEY']!);
  runApp(
    const MyApp(),
  );
}
```

Cela charge le fichier `.env` et initialise Supabase.

## Comment implémenter l'authentification dans une application Flutter

Remplacez le reste du code sous la fonction `main` par ce qui suit :

```dart
class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Supabase Auth UI',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.purple),
      ),
      initialRoute: '/',
      routes: {
        '/': (context) => const SplashScreen(),
        '/auth': (context) => AuthScreen(),
        '/home': (context) => HomeScreen(),
      },
    );
  }
}
```

Créez un fichier `splash_screen.dart` dans le dossier `lib` et collez ce qui suit dedans :

```dart
import 'package:auth_ui_example/auth_screen.dart';
import 'package:auth_ui_example/home_screen.dart';
import 'package:flutter/material.dart';

import 'package:supabase_auth_ui/supabase_auth_ui.dart';

final activeSession = Supabase.instance.client.auth.currentSession;

class SplashScreen extends StatelessWidget {
  const SplashScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(child: activeSession == null ? AuthScreen() : HomeScreen()),
    );
  }
}
```

Cela redirige l'utilisateur vers un écran différent selon qu'il a ou non une session active.

Maintenant, créez un nouveau fichier dans le dossier `lib` appelé `home_screen.dart` et collez ce qui suit dedans :

```dart
import 'package:flutter/material.dart';
import 'package:supabase_auth_ui/supabase_auth_ui.dart';

final supabase = Supabase.instance.client;
final activeSession = supabase.auth.currentSession;

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  @override
  void initState() {
    super.initState();
    if (activeSession == null) {
      Navigator.pushNamed(context, '/auth');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Home')),
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(
              'Vous êtes à la maison - ${activeSession?.user.id}',
              style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 18),
            ),
            const SizedBox(height: 24.0),
            ElevatedButton(
              onPressed: () async {
                await supabase.auth.signOut();
                Navigator.pushNamed(context, '/');
              },
              child: const Text('Se déconnecter'),
            ),
          ],
        ),
      ),
    );
  }
}

```

Cela crée un widget stateful qui vérifie la présence d'une session active et redirige vers l'écran d'authentification s'il n'y a pas de session active. Il affiche également du texte et un bouton qui permet à l'utilisateur de se déconnecter de l'application.

Enfin, créez `auth_screen.dart` dans le dossier `lib` et collez ce qui suit dedans :

```dart
import 'package:flutter/material.dart';
import 'package:supabase_auth_ui/supabase_auth_ui.dart';

class AuthScreen extends StatelessWidget {
  const AuthScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: ListView(
        padding: const EdgeInsets.fromLTRB(24.0, 96.0, 24.0, 24.0),
        children: [
          Column(
            children: [
              const Text(
                'Supabase Auth UI',
                style: TextStyle(
                  fontWeight: FontWeight.bold,
                  fontSize: 18,
                ),
              ),
              const SizedBox(height: 24.0),
              SupaEmailAuth(
                redirectTo:
                    kIsWeb ? null : "myapptest://com.example.auth_ui_example",
                onSignInComplete: (res) => Navigator.pushNamed(context, '/home'),
                onSignUpComplete: (res) => Navigator.pushNamed(context, '/home'),
                onError: (error) => SnackBar(content: Text(error.toString())),
              ),
              SupaSocialsAuth(
                socialProviders: const [
                  OAuthProvider.google,
                  OAuthProvider.github,
                ],
                redirectUrl:
                    kIsWeb ? null : "myapptest://com.example.auth_ui_example",
                onSuccess: (session) => Navigator.pushNamed(
                  context,
                  '/home',
                ),
                onError: (error) => SnackBar(
                  content: Text(
                    error.toString(),
                  ),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
```

Cela affiche du texte et des widgets spéciaux du package `supabase_auth_ui` qui affichent un formulaire d'inscription/connexion et quelques options de connexion sociale.

Dans le terminal intégré, exécutez `flutter run` pour démarrer l'application. Il vous donnera plusieurs plateformes sur lesquelles exécuter, alors choisissez simplement chrome pour ce cas. Vous devriez voir cette belle interface dès la sortie de la boîte 🎉:

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1716935543736/501f4324-0bde-4aac-bc07-a54301d049a7.png)
_Écran de connexion de l'interface utilisateur d'authentification Supabase avec des champs pour l'email et le mot de passe, des options pour se connecter, réinitialiser le mot de passe, s'inscrire et des boutons pour continuer avec Google ou GitHub._

En regardant de plus près le code dans le fichier d'écran d'authentification, vous verrez que nous utilisons les widgets `SupaEmailAuth` et `SupaSocialsAuth` pour y parvenir. Le widget d'authentification par email prend un rappel lui indiquant quoi faire en cas d'échec et de succès de l'action d'authentification. Le widget de connexion sociale prend les mêmes paramètres, plus une liste de fournisseurs OAuth que vous souhaitez utiliser dans votre application.

## Comment configurer l'authentification Supabase Email et fournisseur OAuth

Pour que l'interface utilisateur d'authentification Supabase fonctionne correctement sur mobile et web, vous devrez configurer des liens profonds et une URL de site.

Sous authentification > Configurations d'URL, ajoutez "[http://localhost:3000/](http://localhost:3000/)" comme URL du site.

Puis sous "URL de redirection" ajoutez "YOUR_SCHEME://YOUR_HOSTNAME" comme valeur, où YOUR_SCHEME est un identifiant unique que vous décidez pour votre application et YOUR_HOSTNAME est le nom du package dans votre fichier `build.gradle` en tant qu'applicationID sous android > src > build.gradle. Quelque chose comme ceci : "myapptest://com.example.auth_ui_example".

Terminez la configuration d'Android en allant dans le fichier `AndroidManifest` sous android > src > main > AndroidManifest.xml, et en ajoutant ce code sous le `<intent-filter>` existant, au-dessus de la balise `</activity>` de fermeture :

```xml
 <intent-filter>
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
                <data
                android:scheme="myapptest"
                android:host="com.example.auth_ui_example" />
 </intent-filter>
```

Terminez la configuration iOS en collant le code suivant au bas du fichier `info.plist`, juste au-dessus de la balise `</dict>` de fermeture, sous ios > Runner > info.plist :

```xml
<key>CFBundleURLTypes</key>
<array>
	<dict>
		<key>CFBundleTypeRole</key>
		<string>Editor</string>
		<key>CFBundleURLSchemes</key>
		<array>
			<!-- Ajoutez votre schéma d'URL personnalisé ici -->
        	<string>myapptest</string>
		</array>
	</dict>
</array>
```

Cela termine la configuration sur le web et le mobile.

Pour configurer l'authentification par email, dans le tableau de bord Supabase, allez dans authentification > fournisseurs, et cherchez email. Assurez-vous qu'il est activé. C'est tout pour la configuration de l'email.

### Comment configurer GitHub comme fournisseur OAuth

Pour activer GitHub comme fournisseur d'authentification, faites défiler la liste des fournisseurs jusqu'à ce que vous arriviez à GitHub. Ouvrez le menu déroulant, activez-le et copiez l'URL de rappel. Suivez ensuite ces étapes :

1. Créez une nouvelle application OAuth [ici](https://github.com/settings/developers), remplissez les informations requises et ajoutez l'URL copiée sous le champ d'URL d'autorisation.
2. Ajoutez l'URL de la page d'accueil comme "[http://localhost:3000/](http://localhost:3000/)".
3. Copiez l'ID client de GitHub et ajoutez-le aux paramètres du fournisseur GitHub de Supabase.
4. Générez un nouveau secret et collez-le dans le champ de secret client dans les paramètres du fournisseur GitHub de Supabase.

Enregistrez-le, et vous avez terminé la configuration de GitHub comme fournisseur.

### Comment configurer Google comme fournisseur OAuth

Retournez au tableau de bord Supabase et activez le fournisseur Google. Copiez l'URL de rappel, puis suivez ces étapes :

1. Créez un nouveau [projet Google cloud](https://www.cloud.google.com/).
2. Allez dans Identifiants, cliquez sur le bouton créer des identifiants, puis choisissez ID client OAuth.
3. Continuez et configurez l'écran de consentement pour les utilisateurs externes.
4. Retournez aux identifiants, cliquez sur créer des identifiants, et choisissez application web dans le champ de type d'application.
5. Copiez l'URL de rappel des paramètres Supabase, collez-la sous le champ des URL autorisées et laissez le reste tel quel et enregistrez.
6. Une fenêtre s'ouvrira avec l'ID client et le secret. Copiez-les et collez-les dans les champs pertinents dans les paramètres du fournisseur Google de Supabase.

Enregistrez-le, et vous avez terminé la configuration de Google comme fournisseur.

## Comment connecter un utilisateur en utilisant le package Auth UI

Pour tester que l'authentification fonctionne jusqu'à présent, retournez à votre application, exécutez `flutter run -d chrome --web-port=3000` dans la fenêtre du terminal intégré, et cliquez sur l'un des boutons de connexion sociale.

Vous devriez voir une fenêtre vous demandant de confirmer les permissions, après quoi l'application vous connectera. La connexion via email/mot de passe devrait également fonctionner.

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1717072136518/6aed0f14-595a-49f4-9999-f04977d5463f.png)
_Écran d'autorisation pour "Test Flutter auth ui" demandant l'accès à un compte GitHub. Les options pour "Annuler" ou "Autoriser FatumaA" sont disponibles._

Maintenant, déconnectez-vous de l'application et essayez de naviguer manuellement vers l'écran d'accueil. Il vous redirigera vers l'écran d'authentification.

## Comment ajouter l'authentification par lien magique

Si vous souhaitez uniquement connecter un utilisateur en utilisant un lien magique, remplacez le contenu dans le fichier `auth_screen` par ceci :

```dart
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:supabase_auth_ui/supabase_auth_ui.dart';

class AuthScreen extends StatelessWidget {
  const AuthScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: ListView(
        padding: const EdgeInsets.fromLTRB(24.0, 96.0, 24.0, 24.0),
        children: [
          Column(
            children: [
              const Text(
                'Supabase Auth UI',
                style: TextStyle(
                  fontWeight: FontWeight.bold,
                  fontSize: 18,
                ),
              ),
              const SizedBox(height: 24.0),
              SupaMagicAuth(
                redirectUrl:
                    kIsWeb ? null : "myapptest://com.example.auth_ui_example",
                onSuccess: (session) => Navigator.pushNamed(context, '/home'),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
 
```

Exécutez l'application et vous devriez voir ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-06-01-at-00.16.25.png)
_Interface d'authentification Supabase avec un champ de saisie d'email et un bouton 'Continuer avec le lien magique'._

Connectez-vous et vous devriez recevoir un email et être redirigé vers l'application.

## Support d'authentification native – Comment se connecter avec Google

Pour ajouter une connexion native avec Google sur Android, Web et iOS, vous devrez ajouter quelques configurations supplémentaires.

Retournez à votre projet Google cloud et créez un nouvel identifiant. Choisissez ID client OAuth. Cliquez sur Android dans le menu déroulant du type d'application.

Ensuite, ajoutez le nom du package. Vous pouvez le trouver dans le fichier `AndroidManifest.xml` sous android > src > main > AndroidManifest.xml ou dans le fichier `build.gradle` en tant qu'applicationID sous android > src > build.gradle.

Pour générer l'empreinte de certificat SHA1, collez le code suivant dans une fenêtre de terminal.

```bash
keytool -list -v \
-alias androiddebugkey -keystore ~/.android/debug.keystore
```

Lorsque vous êtes invité à entrer un mot de passe, entrez "android". Copiez le certificat SHA-1 généré et collez-le dans le champ correspondant dans la configuration de votre ID client OAuth ci-dessus et créez le projet. Fermez la fenêtre contextuelle avec l'ID client Android.

Retournez et créez un nouvel ID client OAuth, mais cette fois, définissez-le comme une application iOS. Fournissez-lui la même valeur que le nom du package d'avant et créez-le. Fermez la fenêtre contextuelle comme précédemment.

Dans votre application Flutter, collez le code suivant au-dessus du schéma d'URL personnalisé que vous avez ajouté précédemment dans le fichier `info.plist`. Remplacez la partie en majuscules par la première partie de l'ID client iOS que vous avez créé ci-dessus, moins la partie apps.google...

```xml

			<string>com.googleusercontent.apps.FIRST_PART_OF_IOS_CLIENT_ID_MINUS_apps.googleusercontent.com_PART</string>
            <!-- Laissez le reste intact -->           
            <!-- Ajoutez votre schéma d'URL personnalisé ici -->
        	<string>myapptest</string>
```

Dans le fichier `auth_screen`, remplacez le widget `SupaSocialsAuth` par ceci :

```dart
              SupaSocialsAuth(
                redirectUrl:
                    kIsWeb ? null : "myapptest://com.example.auth_ui_example",
                nativeGoogleAuthConfig: NativeGoogleAuthConfig(
                    iosClientId: dotenv.env['IOS_CLIENT_ID']!,
                    webClientId: dotenv.env['WEB_CLIENT_ID']!),
                socialProviders: const [
                  OAuthProvider.google,
                  OAuthProvider.github,
                ],
                onSuccess: (session) => Navigator.pushNamed(
                  context,
                  '/home',
                ),
                onError: (error) => SnackBar(
                  content: Text(
                    error.toString(),
                  ),
                ),
              ),
```

Ajoutez l'ID client iOS et Web de Google cloud à votre fichier `.env` et vous êtes prêt à tester.

Démarrez l'émulateur Android ou iOS. Puis, dans votre projet Flutter, exécutez `flutter run` dans votre terminal intégré. Quelque chose comme ceci devrait s'afficher :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-06-01-at-00.19.35.png)
_Écran d'une application mobile affichant l'interface utilisateur d'authentification Supabase sur un émulateur iOS. L'interface comprend des champs pour entrer un email et un mot de passe, un bouton "Se connecter", des options pour la récupération du mot de passe, l'inscription au compte et des boutons de connexion pour Google et GitHub._

Cliquez sur l'icône Google et vous devriez être connecté.

## Comment thématiser votre interface utilisateur d'authentification Supabase

Maintenant que vous avez confirmé que le package fonctionne réellement, il est temps pour la partie amusante. Supabase auth UI vous permet de personnaliser l'apparence et la disposition des widgets.

Dans `main.dart`, remplacez le widget `ThemeData` sous `MaterialApp` par ce qui suit :

```dart
ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.purple),
        inputDecorationTheme: const InputDecorationTheme(
          border: OutlineInputBorder(),
          focusedBorder: OutlineInputBorder(
            borderSide: BorderSide(color: Colors.purple, width: 2.0),
          ),
        ),
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(
            backgroundColor: Colors.deepPurple,
            foregroundColor: Colors.white,
          ),
        ),
      ),
```

Remarquez comment le formulaire d'inscription répond aux changements de thème :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1716941053665/46606dcf-386f-4abf-98e1-464bfd4b2955.png)
_Interface de connexion pour Supabase Auth UI. Elle comprend des champs pour entrer un email et un mot de passe, avec des icônes indiquant leurs finalités respectives. Sous les champs se trouve un bouton "Se connecter" violet. Les liens pour "Mot de passe oublié ?" et "Vous n'avez pas de compte ? Inscrivez-vous" sont situés en bas._

### Options de mise en page flexibles

Supabase auth UI vous permet de disposer les boutons de connexion sociale verticalement et horizontalement. Pour voir cela en action, ajoutez la ligne suivante dans le widget `SupaSocialsAuth` : `socialButtonVariant: SocialButtonVariant.icon,`. La disposition devrait passer de ceci :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1717081837364/49584d9b-aac2-412c-b197-bbd2edeac8b1.png)
_Interface de connexion pour Supabase Auth UI avec des champs pour l'email et le mot de passe, un bouton "Se connecter", des options pour réinitialiser le mot de passe ou s'inscrire, et des boutons pour continuer avec Google ou GitHub disposés verticalement avec du texte et des icônes._

À ceci :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1717081856997/ec454669-c11c-4861-83cc-9cd7ca805140.png)
_Écran de connexion pour Supabase Auth UI avec des champs pour l'email et le mot de passe, un bouton "Se connecter", des options pour la récupération du mot de passe, la création de compte et la connexion via Google ou GitHub en icônes circulaires disposées horizontalement_

### Localisation et traduction prêtes

Supabase auth UI est [prête pour la traduction](https://github.com/supabase-community/flutter-auth-ui/pull/76), et vous pouvez changer les étiquettes dans n'importe quelle langue que vous souhaitez.

Remplacez le code dans `auth_screen` par ce qui suit :

```dart
import 'package:flutter/material.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:supabase_auth_ui/supabase_auth_ui.dart';

class AuthScreen extends StatelessWidget {
  const AuthScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: ListView(
        padding: const EdgeInsets.fromLTRB(24.0, 96.0, 24.0, 24.0),
        children: [
          Column(
            children: [
              const Text(
                'Supabase Auth UI',
                style: TextStyle(
                  fontWeight: FontWeight.bold,
                  fontSize: 18,
                ),
              ),
              const SizedBox(height: 24.0),
              SupaEmailAuth(
                redirectTo:
                    kIsWeb ? null : "myapptest://com.example.auth_ui_example",
                localization: const SupaEmailAuthLocalization(
                    enterEmail: "Ingiza barua pepe yako",
                    validEmailError: "'389 389 389 389 389 389 389 389",
                    enterPassword: "Ingresa tu contrase F1a",
                    passwordLengthError:
                        'Tafadhali ingiza nenosiri lenye herufi angalau 6',
                    signIn: '389 389 389 389 389 389',
                    signUp: 'Registrarse',
                    forgotPassword: 'Umesahau nenosiri lako?',
                    dontHaveAccount: '389 389 389 389 389 389',
                    haveAccount: ' BFYa tienes una cuenta? Inicia sesi F3n',
                    sendPasswordReset:
                        'Tuma barua pepe ya kurekebisha nenosiri',
                    backToSignIn: '389 389 389 389 389 389',
                    unexpectedError: 'Se produjo un error inesperado'),
                onSignInComplete: (e) => Navigator.pushNamed(context, '/home'),
                onSignUpComplete: (e) => Navigator.pushNamed(context, '/home'),
                onError: (error) => SnackBar(content: Text(error.toString())),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
```

L'écran est maintenant traduit en swahili, arabe et espagnol. Exécutez `flutter run -d chrome --web-port=3000` et vous devriez voir ceci :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1717083375350/55e1129c-3216-4997-af9d-bf4c3a1e1828.png)
_Interface de connexion intitulée "Supabase Auth UI" avec des champs pour entrer l'email et le mot de passe dans différentes langues. Le champ email est étiqueté "Ingiza barua pepe yako" et le champ mot de passe est étiqueté "Ingresa tu contrase F1a." Il y a un bouton de connexion violet avec du texte en arabe. En dessous du bouton, il y a des liens pour le mot de passe oublié et l'inscription de compte en swahili et arabe._

Saisissez un email incorrect et appuyez sur le bouton de connexion pour déclencher les messages d'erreur. Votre application devrait maintenant être polyglotte, comme montré ci-dessous :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1717083621863/93ebfce6-c6ff-4d2b-9709-46e429a08f3f.png)
_Interface de connexion intitulée "Supabase Auth UI" avec des champs pour l'email et le mot de passe. Le champ email contient "ggg" et a un message d'erreur dans plusieurs langues. Le champ mot de passe est vide avec un texte de remplacement en espagnol. En dessous, il y a un bouton de connexion violet avec du texte en arabe. Du texte supplémentaire en swahili et arabe est présent en dessous du bouton._

## Résumé

Supabase auth UI est un package qui facilite grandement l'ajout de flux d'authentification dans vos applications Flutter. Il fournit des widgets personnalisables et prêts pour la traduction dès la sortie de la boîte.

Il est open-source et toujours à la recherche de plus de contributions. N'oubliez pas de laisser une étoile sur le [dépôt](https://github.com/supabase-community/flutter-auth-ui).

## Ressources

Voici quelques liens qui pourraient être utiles :

* [Docs Supabase sur le deep linking natif](https://supabase.com/docs/guides/auth/native-mobile-deep-linking?platform=flutter&queryGroups=platform&queryGroups=os&os=android#setting-up-deep-linking)
* [Docs Supabase Flutter auth UI](https://supabase.com/docs/guides/auth/auth-helpers/flutter-auth-ui)
* [Vidéo Supabase sur la connexion Google](https://www.youtube.com/watch?v=utMg6fVmX0U)