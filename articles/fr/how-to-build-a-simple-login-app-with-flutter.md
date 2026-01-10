---
title: Comment créer une application de connexion simple avec Flutter
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-03-14T16:39:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-simple-login-app-with-flutter
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Flutter-Login-App
seo_title: Comment créer une application de connexion simple avec Flutter
---

Banner.png
tags:
- name: Flutter
  slug: flutter
- name: développement d'applications mobiles
  slug: developpement-applications-mobiles
seo_title: null
seo_desc: 'Flutter est l\''un des Frameworks les plus populaires pour créer des applications mobiles et de bureau. Et de nombreuses entreprises l\''utilisent aujourd\''hui. C\''est en partie dû à ses performances exceptionnelles...'
---

Flutter est l'un des Frameworks les plus populaires pour créer des applications mobiles et de bureau. Et de nombreuses entreprises l'utilisent aujourd'hui.

C'est en partie grâce à ses performances exceptionnelles, avec un benchmark de 60 images par seconde (FPS). Cela lui permet de surpasser d'autres technologies multiplateformes, et il est même plus performant que certains langages natifs.

Je suis un passionné de React Native. Mais après avoir entendu tous les avantages de Flutter, j'ai décidé de l'essayer. J'aimerais partager mon expérience d'apprentissage avec vous à travers ce tutoriel.

Dans cet article, nous allons apprendre à créer une application Flutter avec une mise en page de connexion et quelques fonctionnalités.

## Prérequis {#heading-prerequis}

Dans cet article, je ne couvrirai pas les étapes d'installation de Flutter sur votre machine. Je pense que c'est mieux expliqué sur leur [site de documentation officielle](https://docs.flutter.dev/get-started/install).

Je vous recommande vivement d'essayer cet [exercice](https://docs.flutter.dev/get-started/codelab) proposé par la communauté officielle de Flutter. Il vous donnera une compréhension rapide de Flutter pour que vous puissiez commencer.

Ne vous inquiétez pas si vous ne comprenez pas certains concepts mentionnés là-bas. J'écrirai à leur sujet dans mes prochains tutoriels. J'ai utilisé cet exercice pour commencer mon propre parcours Flutter, et je me suis senti plus confiant après l'avoir terminé par moi-même.

Commençons à construire notre application !

Je crois au dicton : "Se fixer un objectif, c'est la moitié du travail accompli". Ainsi, chaque fois que j'essaie de faire quelque chose, je me fixe un objectif pour voir où je veux en être quand j'aurai fini. Quel est donc votre objectif en lisant ce tutoriel ?

## Outils requis {#heading-outils-requis}

Pour construire cette application, vous devez avoir les éléments suivants installés sur votre machine :

1. Visual Studio Code (L'un des IDE recommandés pour Flutter)
2. Émulateur Android / Simulateur iOS / Appareil réel
3. Flutter installé (je recommanderais de suivre [ce guide](http://docs.flutter.dev/get-started/install) pour l'installer si vous ne l'avez pas déjà)
4. Plugin Flutter pour VS Code ([Guide recommandé](https://docs.flutter.dev/get-started/editor?tab=vscode))

## Comment créer le projet {#heading-comment-creer-le-projet}

Naviguez vers le dossier où vous souhaitez créer votre application.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-61.png)
_Naviguez vers le répertoire du projet_

Ouvrez Visual Studio Code à partir de ce répertoire.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-62.png)
_Ouvrez Visual Studio Code_

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-63.png)
_IDE Visual Studio Code_

Ouvrez la palette de commandes en appuyant sur `CTRL + SHIFT + P` et tapez `Flutter`. Choisissez `Flutter: New Project` parmi les options listées.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-64.png)
_Utilisez la palette de commandes pour créer un projet Flutter_

Sélectionnez `Application` dans la liste suivante.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-65.png)
_Choisissez de construire une `Application` Flutter_

Il vous sera demandé de sélectionner le dossier cible pour créer le projet. Par défaut, ce sera le même dossier que celui où vous avez ouvert VS Code. Tapez le nom de votre application dans la zone de texte et appuyez sur `Entrée`. Je nomme la mienne `loginapp`, mais vous pouvez taper le nom que vous souhaitez.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-66.png)
_Entrez le nom de votre projet_

Dans les secondes qui suivent, VS Code créera un nouveau projet Flutter et vous verrez un écran comme celui ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-67.png)
_Projet Flutter créé_

Par défaut, le fichier `main.dart` sera ouvert. C'est ici que Flutter commence à exécuter l'application. En bas, vous verrez une notification disant "Your Flutter project is ready! Press F5 to start running ...".

## Comment lancer l'appareil {#heading-comment-lancer-lappareil}

Pour exécuter votre application, vous devez disposer d'un appareil virtuel ou d'un appareil réel en cours d'exécution et connecté à votre machine.

J'utiliserai un émulateur Android pour exécuter notre application. Vous pouvez soit exécuter un appareil virtuel, soit connecter votre téléphone mobile à votre machine. Mais n'oubliez pas d'activer le "Débogage USB" si vous effectuez le débogage via un téléphone Android.

Une fois que vous êtes connecté ou que vous avez lancé un appareil virtuel, regardez en bas à droite de VS Code et appuyez sur l'option d'appareil.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-68.png)
_Option d'appareils_

Parfois, VS Code sélectionnera l'appareil par défaut, mais pour la première fois, vous devez le sélectionner vous-même. Appuyez sur le texte "No Device" dans la capture d'écran ci-dessus ou quel que soit le nom de l'appareil qui s'affiche.

La liste des appareils virtuels disponibles et connectés s'affiche. Cliquez sur l'appareil sur lequel vous souhaitez exécuter votre application.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-69.png)
_Liste des appareils disponibles pour exécuter l'application_

Une fois que vous avez sélectionné votre appareil, le panneau inférieur affichera le nom de l'appareil sélectionné, comme dans la capture d'écran ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-70.png)
_Émulateur Android sélectionné_

## Comment exécuter l'application {#heading-comment-executer-lapplication}

Êtes-vous prêt pour le lancement de la fusée ?

Appuyez sur `F5` pour exécuter votre application. Cela prendra un certain temps. Le système va compiler et construire votre projet. Une fois prêt, l'application s'exécutera sur votre appareil.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-71.png)
_Exécution de votre application_

Vous verrez un type d'interface similaire. En bas, vous pouvez voir la notification indiquant "Running Gradle task 'assembleDebug...'".

Impatient de voir le résultat ? Le voici :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-72.png)
_Résultat de l'application par défaut_

N'apportez aucune modification au code pour l'instant. Vos modifications ne seront pas suivies car Git n'est pas initialisé pour ce dépôt.

C'est une partie que j'aime chez React Native. Chaque fois que vous créez une application React Native, elle effectue un Commit initial. Vous pouvez simplement continuer et faire vos modifications, et vous pourrez voir tous vos changements suivis.

Ceci n'est pas disponible dans Flutter pour le moment (mars 2023), mais j'espère que l'équipe Flutter ajoutera cela à l'avenir.

Faisons le Commit nous-mêmes.

Naviguez vers l'emplacement du projet dans le terminal :

```bash
cd <emplacement_du_projet>
```

Initialisez Git en exécutant la commande `git init`.

Comme c'est notre premier Commit, nous ferons `git add .` pour ajouter tous les changements à notre Commit.

Faisons le Commit initial :

```
git commit -m "Initial commit"
```

Voici la capture d'écran du processus ci-dessus :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-73.png)
_Commit des modifications sur Git_

Vérifions si nos modifications sont validées en exécutant la commande `git status` :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-74.png)
_Vérification après le Commit_

Tout semble correct. Nos modifications sont validées. Continuons.

## Comment supprimer les commentaires {#heading-comment-supprimer-les-commentaires}

Je n'aime pas les commentaires dans mon code. J'aime écrire du code lisible. Supprimons tous les commentaires dans le fichier `main.dart`. Ne touchez pas aux autres fichiers.

Tous les fichiers Flutter se trouvent dans le répertoire `lib/` et ils ont l'extension de fichier `.dart`. Pour tout ce tutoriel, nous travaillerons uniquement sur le fichier `main.dart`.

Vous pouvez lire les commentaires pour en tirer quelques informations. Ils vous donneront une compréhension claire du fonctionnement de l'application par défaut, ce qui peut être très utile pour les débutants.

Mais cela n'a pas de sens si vous construisez l'application pour la 2e ou 3e fois. Il n'y a aucun intérêt à relire les mêmes commentaires encore et encore une fois que vous avez acquis le contexte lors de votre première lecture.

Vous pouvez ignorer cette étape si vous souhaitez conserver les commentaires tels quels.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Full-code.png)
_Code de l'application_

Mon code est devenu super simple maintenant. J'ai fait un Commit ici (après avoir supprimé les commentaires). Si vous en êtes arrivé là, après avoir validé, assurez-vous simplement que votre application fonctionne bien et qu'il n'y a eu aucun changement sur l'interface utilisateur.

## Comment changer le nom {#heading-comment-changer-le-nom}

Changeons le nom de la barre de titre et les noms des classes internes. Dans la classe `MyApp`, à l'intérieur de la méthode `build`, changez le titre dans le champ home de "Flutter Demo Home Page" à "Login App".

```dart
class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Login App'),
    );
  }
}
```

Changeons le nom de notre classe de "MyHomePage" à "Login". Placez le curseur sur le texte "MyHomePage" et appuyez sur `F2`. `F2` est la touche de raccourci pour renommer et refactoriser dans VS Code. Cela signifie qu'il renomme à l'endroit actuel et remplace toutes ses utilisations. Voici la capture d'écran de ce à quoi cela ressemble quand vous appuyez sur `F2` (lors de la refactorisation).

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-76.png)
_Renommer le nom de la classe de `MyHomePage` à `Login`_

Validons nos changements avec un Commit.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-77.png)
_Commit des changements de noms_

Vous devriez pouvoir voir le titre "Login App" dans votre application.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-78.png)
_La barre de titre de l'application est devenue "Login App"_

## Comment créer l'application {#heading-comment-creer-lapplication}

Maintenant, construisons notre application. Copiez le code ci-dessous et remplacez la classe `_LoginState` dans le fichier `main.dart`.

<script src="https://gist.github.com/arungogosoon/48c951d288dde4ac6b472c501655b9ad.js"></script>

Immédiatement après avoir collé et enregistré le fichier, votre interface utilisateur changera comme par magie.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-79.png)
_L'interface utilisateur a changé pour demander les identifiants de connexion_

Décortiquons le code que vous avez copié par parties et essayons de comprendre chaque bloc.

```dart
  final _formKey = GlobalKey<FormState>();
  TextEditingController emailController = TextEditingController();
  TextEditingController passwordController = TextEditingController();
```

La première ligne indique que vous créez une clé pour un formulaire. Dans notre contexte, il s'agit du formulaire de connexion. Vous la créez pour identifier le formulaire de manière unique. Elle est définie comme final, de sorte qu'elle ne changera pas.

Les 2 lignes suivantes sont des définitions de contrôleurs. Un contrôleur dans notre contexte est utilisé pour lire les valeurs de l'entrée. À l'aide d'un contrôleur, vous pourrez contrôler son composant associé.

Décortiquons la méthode `build`. Vous utilisez la méthode `build` dans Flutter pour construire l'interface utilisateur. Elle contient le code de conception. Le contenu renvoyé par cette méthode sera rendu sur l'interface utilisateur.

```dart
@override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Form(
        key: _formKey,
```

Le Scaffold est un widget dans Flutter utilisé pour implémenter la structure de base de la mise en page visuelle du Material Design. Considérez le widget comme un simple composant d'interface utilisateur.

Nous définissons le titre passé en paramètre à cette classe. Nous pouvons accéder aux paramètres en utilisant l'objet widget. Donc, cela s'écrit `widget.{nom_de_la_cle}`.

Si vous voulez accéder à la propriété title, ce sera `widget.title`. C'est similaire au passage de `props` dans React.

```
body: Form(
  key: _formKey,
  child: Padding(
    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 16),
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [
```

La section suivante est `body`. Comme nous construisons une application de connexion simple, nous avons besoin d'un formulaire à remplir par l'utilisateur pour s'authentifier. Nous attribuons la clé unique que nous avons créée ci-dessus à ce formulaire. Le `Form` accepte un enfant (child). Il ne peut accepter qu'un seul composant.

Nous créons une mise en page avec un padding horizontal de 8px et un padding vertical de 16px. Ce widget `Padding` n'accepte également qu'un seul enfant.

`Column` est un widget dans Flutter utilisé pour afficher ses enfants dans un tableau vertical. Nous définissons `crossAxisAlignment` pour centrer horizontalement le contenu du widget `Column`.

Comme nous l'avons vu, le widget `Column` affiche ses enfants dans un tableau vertical. Nous pouvons passer plusieurs widgets dans sa propriété `children`.

```dart
Padding(
  padding:
      const EdgeInsets.symmetric(horizontal: 8, vertical: 16),
      child: TextFormField(
        controller: emailController,
        decoration: const InputDecoration(
          border: OutlineInputBorder(), labelText: "Email"),
        validator: (value) {
          if (value == null || value.isEmpty) {
            return 'Please enter your email'; // Veuillez entrer votre email
          }
          return null;
        },
     ),
  ),
```

Le premier élément que nous voulons afficher dans l'interface utilisateur est une zone de saisie pour obtenir l'adresse e-mail d'un utilisateur. Nous avons donc utilisé le widget `TextFormField` et défini le contrôleur sur `emailController`.

Afin d'obtenir le texte flottant, nous devons utiliser l'option de décoration qui demande le type de bordure (`border`) et le texte de l'étiquette (`labelText`) de l'entrée.

Nous pouvons ajouter toute validation par défaut à appliquer lors de la soumission de ce formulaire dans le champ `validator`. Nous validons s'il s'agit d'une valeur `null` ou vide et nous renvoyons une erreur si l'une d'elles correspond. S'il y a une valeur, nous ne renvoyons aucune erreur et retournons `null`.

```
Padding(
  padding:
  const EdgeInsets.symmetric(horizontal: 8, vertical: 16),
    child: TextFormField(
      controller: passwordController,
      obscureText: true,
      decoration: const InputDecoration(
        border: OutlineInputBorder(), labelText: "Password"),
      validator: (value) {
        if (value == null || value.isEmpty) {
          return 'Please enter your password'; // Veuillez entrer votre mot de passe
        }
        return null;
      },
   ),
),
```

Le deuxième élément est la zone de saisie pour obtenir le mot de passe (`Password`) de l'utilisateur. Ceci est similaire au champ `email`, sauf pour une chose : nous devons masquer le mot de passe dans le champ de saisie et afficher un point pour chaque caractère tapé.

Pour ce faire, nous devons passer une propriété `obscureText` au widget `TextFormField` et la définir sur `true`. La décoration, la validation et les autres éléments restent les mêmes que pour l'e-mail.

```dart
Padding(
  padding:
    const EdgeInsets.symmetric(horizontal: 8, vertical: 16.0),
      child: Center(
        child: ElevatedButton(
          onPressed: () {
            if (_formKey.currentState!.validate()) {
              // Naviguer l'utilisateur vers la page d'accueil
            } else {
              ScaffoldMessenger.of(context).showSnackBar(
                const SnackBar(content: Text('Please fill input')),
              );
            }
          },
        child: const Text('Submit'),
      ),
    ),
),
```

C'est la dernière pièce de notre formulaire, qui est un bouton de soumission. Nous utilisons un widget `ElevatedButton` et passons le texte du bouton dans la propriété `child` du bouton. Nous définissons l'action qui doit être suivie lors de l'appui sur ce bouton dans la propriété `onPressed`.

Dans notre cas, nous validons les champs de saisie (rappelez-vous de la propriété `validator` que nous avons définie pour les zones de saisie `email` et `password`). Si la validation réussit, nous devrions diriger l'utilisateur vers l'écran suivant (que nous ajouterons plus tard). Sinon, nous affichons un message demandant à l'utilisateur de remplir les champs ("Please fill input").

Il est temps de vérifier si notre code fonctionne correctement. Vérifiez votre application. Essayez de soumettre sans entrer d'informations et vous devriez remarquer le Snackbar en bas avec le texte "Please fill input". Remplissez les zones de saisie avec des valeurs aléatoires et essayez de soumettre, l'erreur ne devrait plus s'afficher.

Si vous rencontrez des erreurs lors de l'affichage de l'interface utilisateur, la plupart du temps (presque 90 %), cela proviendra des parenthèses ou accolades. Nous utilisons beaucoup de parenthèses dans Flutter, ce qui est souvent déroutant pour les débutants. Assurez-vous d'avoir les parenthèses d'ouverture et de fermeture appropriées. L'application Flutter peut s'arrêter au milieu en cas d'erreurs. Dans ces cas, après avoir appliqué le correctif, appuyez sur `F5` pour redémarrer l'application.

## Naviguer lors de la connexion {#heading-naviguer-lors-de-la-connexion}

Dirigeons l'utilisateur vers la page d'accueil après une connexion réussie et affichons l'adresse e-mail qu'il a saisie sur la page de connexion. Quelque chose de similaire à la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-87.png)
_Page d'accueil_

Allez à la dernière ligne du fichier `main.dart` et copiez et collez le contenu ci-dessous :

<script src="https://gist.github.com/arungogosoon/4677275a5265981967362825da714f32.js"></script>

Dans ce code, nous créons une nouvelle classe appelée "HomePage" et l'étendons à partir de "StatelessWidget". Nous recevons un e-mail de la page précédente.

```dart
@override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text('Home Page'),
        ),
        body: Column(
          children: [
            Text(email),
            Center(
              child: ElevatedButton(
                onPressed: () {
                  Navigator.pop(context);
                },
                child: const Text("Go back!"),
              ),
            ),
          ],
        ));
```

Dans la méthode `build`, nous définissons le titre de la page comme "Home Page" et son corps contient un widget `Text` et un widget `ElevatedButton`. Le widget `Text` affichera l'adresse e-mail transmise depuis l'écran précédent. Le widget `ElevatedButton` ramènera l'utilisateur à l'écran précédent chaque fois qu'il sera pressé. Nous utilisons `Navigator.pop(context);` pour revenir à l'écran précédent.

Comprenons comment naviguer de la page `Login` à la page `Home`.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-89.png)
_Code pour naviguer vers la page suivante_

Supprimez le commentaire que nous avons fait sur la condition de `validation` ("Navigate the user to the Home page") comme indiqué dans la capture d'écran ci-dessus et remplacez-le par le contenu ci-dessous.

```dart
if (emailController.text == "arun@gogosoon.com" && passwordController.text == "qazxswedcvfr") {
  Navigator.push(
    context,
    MaterialPageRoute(
      builder: (context) => HomePage(
        email: emailController.text,
    )),
  );
} else {
  ScaffoldMessenger.of(context).showSnackBar(
    const SnackBar(
      content: Text('Invalid Credentials')),
    );
}
```

Voici le code final pour le bouton Submit.

```
Padding(
  padding:
    const EdgeInsets.symmetric(horizontal: 8, vertical: 16.0),
      child: Center(
        child: ElevatedButton(
          onPressed: () {
            if (_formKey.currentState!.validate()) {
              if (emailController.text == "arun@gogosoon.com" &&
                            passwordController.text == "qazxswedcvfr") {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => HomePage(
                      email: emailController.text,
                    )),
                );
              } else {
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(
                    content: Text('Invalid Credentials')),
                  );
              }
            } else {
              ScaffoldMessenger.of(context).showSnackBar(
                const SnackBar(content: Text('Please fill input')),
              );
            }
          },
        child: const Text('Submit'),
      ),
    ),
),
```

Essayons de comprendre ce code.

En plus de la validation du formulaire, nous ajoutons une autre couche de validation qui vérifie si l'utilisateur a tapé l'adresse e-mail "arun@gogosoon.com", (qui est mon adresse e-mail, vous pouvez la remplacer par ce que vous voulez) et le mot de passe "qazxswedcvfr". Nous dirigeons l'utilisateur vers la page d'accueil si les identifiants saisis correspondent, et affichons "Invalid Credentials" dans le Snackbar sinon.

C'est tout. Nous avons couvert une validation de connexion très basique. Essayez d'exécuter l'application et vérifiez si votre application fonctionne comme prévu.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-91.png)
_Page de connexion_

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-92.png)
_Page d'accueil_

## Conclusion {#heading-conclusion}

Dans cet article, vous avez appris à construire une version de base d'une application de connexion à l'aide de Flutter. J'espère que vous avez compris le flux de construction d'une application Flutter.

Si vous êtes curieux d'en apprendre davantage sur Flutter, essayez l'exercice que j'ajoute ci-dessous. Chercher, appliquer le code et obtenir le résultat par vous-même vous rendra plus confiant dans le développement d'applications Flutter.

1. Essayez d'ajouter une icône d'œil à la fin du champ de saisie "Password". Cliquer dessus devrait alterner entre l'affichage du mot de passe en texte clair et en texte masqué.
2. Effacez les champs de saisie Email et Password avant de naviguer vers la page d'accueil.
3. Ajoutez une validation regex supplémentaire pour la saisie de l'e-mail.
4. Ajoutez une validation au champ du mot de passe pour vérifier si l'utilisateur a entré au moins un chiffre, une lettre et un symbole.
5. Ajoutez un bouton "Signup" sous le bouton "Submit" qui devrait diriger l'utilisateur vers une nouvelle page "Signup".

Pour en savoir plus sur Flutter, abonnez-vous à ma newsletter par e-mail sur mon [site](https://5minslearn.gogosoon.com/?ref=fcc_flutter_login_app) ([https://5minslearn.gogosoon.com](https://5minslearn.gogosoon.com/?ref=fcc_flutter_login_app)) et suivez-moi sur les réseaux sociaux.