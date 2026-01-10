---
title: Comment utiliser Flutter pour créer une calculatrice de pourboire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-20T19:09:44.000Z'
originalURL: https://freecodecamp.org/news/build-a-tip-calculator-with-flutter
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fb5e53749c47664ed822a29.jpg
tags:
- name: Android
  slug: android
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
seo_title: Comment utiliser Flutter pour créer une calculatrice de pourboire
seo_desc: "By Krissanawat\n### \nAs the Flutter mobile app development framework grows\
  \ more and more popular, many business are choosing to use it for their projects.\
  \ \nMany devs appreciate its ability to develop apps with pixel perfect UIs using\
  \ a simple structur..."
---

Par Krissanawat

### 

Alors que le framework de développement d'applications mobiles Flutter devient de plus en plus populaire, de nombreuses entreprises choisissent de l'utiliser pour leurs projets. 

De nombreux développeurs apprécient sa capacité à développer des applications avec des interfaces utilisateur pixel perfect en utilisant une structure simple de widgets. Je pense que Flutter est l'avenir du développement d'applications mobiles grâce à sa simplicité dans le développement des interfaces utilisateur et sa capacité à alimenter la logique des fonctionnalités en utilisant le langage de programmation Dart.

Ce tutoriel se concentre principalement sur l'enseignement des bases du framework Flutter en construisant une simple application de calculatrice de pourboire. Nous aborderons les modèles de codage standard, y compris les classes de widgets Stateful et Stateless, ainsi que certains des widgets que vous utiliserez le plus lors du développement d'applications Flutter. 

L'idée ici est de commencer par configurer un projet Flutter de démarrage. Ensuite, nous passerons à la mise en œuvre de l'interface utilisateur globale et de la fonctionnalité de base.

Alors, commençons !

## Comment configurer votre projet Flutter

Pour créer un nouveau projet Flutter, vous devez avoir le SDK Flutter installé sur votre système. Pour un processus d'installation simple et rapide, vous pouvez suivre la documentation officielle de [Flutter](https://flutter.dev/docs/get-started/install). 

N'oubliez pas qu'il nécessite également Android Studio et le SDK Android si vous développez une application pour la plateforme Android. 

Après avoir tout configuré avec succès selon la documentation, vous pouvez exécuter la commande Flutter suivante dans le terminal :

```bash
flutter create tipCalculator

```

Cette commande téléchargera et configurera automatiquement votre projet Flutter de démarrage. Vous pouvez maintenant ouvrir le projet dans l'IDE Visual Studio Code. 

Si vous avez un simulateur de périphérique ou un périphérique smartphone réel connecté, vous pouvez simplement exécuter la commande suivante pour lancer l'application :

```bash
flutter run

```

Alternativement, vous pouvez appuyer sur 'F5' sur votre clavier, ce qui déclenchera une option de menu dans VSCode. À partir de ce menu, vous pouvez sélectionner le périphérique sur lequel vous souhaitez lancer l'application.

> Notez que vous devez être dans le fichier avec l'extension **.dart** pour exécuter cette commande avec succès.

Construisez et exécutez-le en utilisant la commande ci-dessus ou **F5** pour obtenir le modèle de démarrage suivant dans votre émulateur/périphérique réel :

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/155af4bd-4619-45ad-8739-726b85bc7131/tip1.jpg](https://www.freecodecamp.org/news/content/images/2020/11/tip1.jpg)

Vous devriez maintenant avoir votre application Flutter en cours d'exécution.

Entrons un peu plus dans les détails de ce qui se passe dans le fichier principal du projet, **main.dart**.

Dans le fichier **main.dart**, nous avons deux objets de classe. L'un étend les widgets Stateful et l'autre les widgets Stateless. Alors, que signifie cela ?

* Widget Stateful : la classe qui héberge les états de l'application. Les états peuvent changer et déclencher le rendu des widgets dans cette classe de widget Stateful. Il contribue aux changements d'état dynamiques.
* Widget Stateless : cette classe ne contient aucun état. Il représente la vue du widget qui ne change pas. Il ne contribue à aucun changement d'état dynamique.

Le fichier main.dart contient également la fonction `main()` qui appelle la classe `MyApp` à l'intérieur de la méthode `runApp` afin de déclencher le lancement de l'application Flutter sur le périphérique.

## Comment construire l'interface utilisateur de la calculatrice de pourboire

Pour commencer à implémenter notre interface utilisateur, nous devons supprimer tout ce qui est présent dans la classe `MyHomePageState` par défaut.

Après l'avoir supprimé, nous allons retourner un simple widget `Scaffold` depuis l'intérieur de la fonction build. 

Le widget `Scaffold` fournit les propriétés pour ajouter l'`appBar` ainsi que le `body`. Pour l'instant, nous allons ajouter une simple barre d'application. Vous pouvez voir la mise en œuvre globale dans l'extrait de code ci-dessous :

```dart
class _MyHomePageState extends State<MyHomePage> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title:Text('Calculatrice de Pourboire', style: TextStyle(color: Colors.black87),),
      ),
      body: Container()
    );
  }
}

```

Construisez et exécutez-le après avoir ajouté l'`appBar` en utilisant le widget `AppBar` avec la propriété `title`. Vous obtiendrez le résultat suivant sur l'écran de votre émulateur :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/tip2.jpg)

> Notez que Flutter dispose d'un **rechargement à chaud** lors de l'enregistrement du fichier Dart. Ainsi, chaque fois que vous enregistrez des modifications dans le fichier Dart de votre projet, les modifications sont automatiquement reflétées dans l'émulateur.

### **Étape 1 : Concevoir la barre d'application**

Ici, nous allons modifier le widget `AppBar` en utilisant diverses propriétés qu'il offre. Vous pouvez voir le code modifié dans l'extrait ci-dessous :

```dart
appBar: AppBar(
  title: Text('Calculatrice de Pourboire', style: TextStyle(color: Colors.black87),),
  centerTitle: true,
  elevation: 0.0,
  backgroundColor: Colors.white70,
),

```

Construisez et exécutez-le, et vous obtiendrez le résultat suivant sur l'écran de l'émulateur :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/tip3.jpg)

Ici, nous avons utilisé certaines des propriétés de base du widget `AppBar` telles que 

* `elevation`, qui nous permet de contrôler l'effet d'ombre dans la barre d'application similaire à z-index, 
* `centerTitle` pour centrer le titre, 
* et nous avons également changé la couleur de fond en blanc.

### **Étape 2 : Concevoir le corps de l'échafaudage**

Jusqu'à présent, nous n'avons eu qu'un widget `Container` vide dans la propriété `body`. Maintenant, nous allons ajouter quelques propriétés et widgets enfants au widget `Container` comme indiqué dans l'extrait de code ci-dessous :

```dart
body: Container(
  color: Colors.white70,
  padding: const EdgeInsets.all(16.0),
  child: Center(
    child: Form(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
        ],
      ),
    ),
  ),

```

Construisez et exécutez-le, et vous obtiendrez le résultat suivant sur l'écran de l'émulateur :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/tip4.jpg)

Comme vous pouvez le voir dans la capture d'écran ci-dessus, nous avons changé la couleur de fond du corps en blanc. Nous avons également ajouté un peu de `padding` ainsi que le widget `Center` comme widget enfant qui centralisera toute l'interface utilisateur dans le corps. 

Le widget `Center` a un widget `Form` (l'un de ses enfants) pour lequel nous allons créer un simple formulaire avec des champs de texte. 

Et surtout, nous avons le widget `Column` comme widget enfant de `Form`. Le widget `Column` nous fournit la propriété de tableau de widgets `children` dans laquelle nous pouvons intégrer n'importe quel nombre de widgets qui apparaîtront verticalement à l'écran.

### **Étape 3 : Définir les constantes et les variables**

Avant de mettre en œuvre les éléments de formulaire (y compris les champs de texte), nous devons définir quelques constantes afin de gérer les entrées des champs de saisie. 

Vous pouvez voir les constantes et variables requises dans l'extrait de code ci-dessous :

```jsx
// Ceci est le montant de la facture par défaut
  static const defaultBillAmount = 0.0;

  // Ceci est le pourcentage de pourboire par défaut
  static const defaultTipPercentage = 15;

  // Ceci est le TextEditingController qui est utilisé pour suivre le changement du montant de la facture
  final _billAmountController =
      TextEditingController(text: defaultBillAmount.toString());

  // Ceci est le TextEditingController qui est utilisé pour suivre le changement du pourcentage de pourboire
  final _tipPercentageController =
      TextEditingController(text: defaultTipPercentage.toString());

  // Ceci stocke la dernière valeur du montant de la facture calculé
  double _billAmount = defaultBillAmount;

  // Ceci stocke la dernière valeur du pourcentage de pourboire calculé
  int _tipPercentage = defaultTipPercentage;

```

Dans l'extrait de code ci-dessus, vous pouvez voir que nous utilisons la méthode `TextEditingController`. Cette méthode de contrôleur nous permet de gérer les entrées de texte dans le widget `TextFormField` plus tard, qui est initialisé avec des valeurs par défaut.

### **Étape 4 : Ajouter des champs de formulaire d'entrée**

Maintenant, nous allons ajouter deux champs de formulaire d'entrée en utilisant le widget `TextFormField`. 

Lors de l'utilisation de ce widget, nous devons obligatoirement assigner la propriété controller avec nos variables de contrôleur que nous avons définies auparavant. Vous pouvez voir la mise en œuvre globale du codage du widget dans l'extrait de code ci-dessous :

```jsx
body: Container(
        color: Colors.white70,
        padding: const EdgeInsets.all(16.0),
        child: Center(
          child: Form(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                TextFormField(
                  key: Key("billAmount"),
                  controller: _billAmountController,
                  keyboardType: TextInputType.numberWithOptions(decimal: true),
                  decoration: InputDecoration(
                      hintText: 'Entrez le montant de la facture',
                      labelText: 'Montant de la facture',
                      labelStyle: TextStyle(
                        fontSize: 25,
                        letterSpacing: 1,
                        fontWeight: FontWeight.bold
                      ),
                      fillColor: Colors.white,
                      border: new OutlineInputBorder(
                        borderRadius: new BorderRadius.circular(20.0),
                      ),
                    ),
                ),
                SizedBox(height: 25,),
                TextFormField(
                  key: Key("tipPercentage"),
                  controller: _tipPercentageController,
                  keyboardType: TextInputType.number,
                  decoration: InputDecoration(
                    hintText: 'Entrez le pourcentage de pourboire',
                    labelText: 'Pourcentage de pourboire',
                    labelStyle: TextStyle(
                      fontSize: 25,
                      letterSpacing: 1,
                      fontWeight: FontWeight.bold
                    ),
                    fillColor: Colors.white,
                    border: new OutlineInputBorder(
                      borderRadius: new BorderRadius.circular(20.0),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),

```

Ici, nous avons assigné la propriété `keyboardType` qui nous permet d'afficher le type de clavier requis lorsque l'utilisateur appuie sur le champ de saisie. 

Nous avons également des propriétés de décoration avec lesquelles nous pouvons styliser nos champs de saisie en utilisant le widget `InputDecoration`. 

Dans le widget `InputDecoration`, nous avons plusieurs propriétés qui nous aident à afficher le texte de l'espace réservé ainsi que l'étiquette au-dessus de la saisie. Nous avons également appliqué la propriété `border` pour afficher une bordure de contour courbe.

Construisez et exécutez-le, et vous obtiendrez le résultat suivant sur l'écran de votre émulateur :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/tip5.jpg)

### **Étape 5 : Ajouter des écouteurs d'événements et des fonctions**

Puisque nous allons calculer le montant du pourboire dès que l'utilisateur saisit le montant de la facture ou le pourcentage, nous devons écouter les changements dans les champs de saisie de texte. 

Pour cela, nous devons ajouter les écouteurs d'événements aux contrôleurs en utilisant la méthode `addListener`. 

Maintenant, dès qu'un changement se produit dans le champ de saisie, nous voulons également déclencher une certaine fonction pour mettre à jour le montant de la facture et le pourcentage de pourboire. 

Pour cela, nous allons utiliser les fonctions requises avec la méthode `setState` qui nous aide à rendre toute l'interface utilisateur dès que certains changements se produisent.

> Notez que la méthode `setState` déclenche la réexécution de la méthode `build`.

Vous pouvez voir la mise en œuvre globale du codage dans l'extrait de code ci-dessous :

```jsx
@override
void initState() {
  super.initState();
  _billAmountController.addListener(_onBillAmountChanged);
  _tipPercentageController.addListener(_onTipAmountChanged);
}

_onBillAmountChanged() {
  setState(() {
    _billAmount = double.tryParse(_billAmountController.text) ?? 0.0;
  });
}

_onTipAmountChanged() {
  setState(() {
    _tipPercentage = int.tryParse(_tipPercentageController.text) ?? 0;
  });
}

```

Ici, nous avons également la méthode `initState`. Cette méthode s'exécute dès que nous entrons dans cet écran de l'application. Nous ajoutons donc les écouteurs d'événements dès que nous entrons dans l'écran.

### **Étape 6 : Ajouter la section des montants**

Maintenant, revenons à nos widgets d'interface utilisateur. Nous allons ajouter la section des montants juste en dessous des champs de saisie à l'intérieur du widget Column. 

Ici, nous allons également utiliser le widget `SizedBox` qui nous permet de fournir un espacement requis entre les widgets. Vous pouvez voir la mise en œuvre du codage de la section des montants dans l'extrait de code ci-dessous :

```jsx
),
SizedBox(height: 20,),
Container(
  margin: EdgeInsets.all(15),
  padding: EdgeInsets.all(15),
  decoration: BoxDecoration(
    color: Colors.white,
    borderRadius: BorderRadius.all(
      Radius.circular(15),
    ),
    border: Border.all(color: Colors.white),
    boxShadow: [
      BoxShadow(
        color: Colors.black12,
        offset: Offset(2, 2),
        spreadRadius: 2,
        blurRadius: 1,
      ),
    ],
  ),
  child: Column(
    children: [
      Text("Montant du pourboire"),
      Text("Montant total")
    ],
  ),
),

```

Ici, nous avons un `Container` avec quelques décorations de style requises. La propriété `child` contient un autre widget `Column` avec deux widgets `Text` disposés verticalement.

Construisez et exécutez-le, et vous obtiendrez le résultat suivant sur l'écran de votre émulateur :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/tip6.jpg)

### **Étape 7 : Créer un widget Stateless séparé pour afficher les montants**

Puisque nous voulons afficher le montant du pourboire et le montant total avec un peu de style. Il ne contiendra aucun état mais dépendra de la valeur passée depuis le widget Stateful. 

Vous pouvez voir la mise en œuvre globale du codage de la classe de widget Stateless `AmountText` dans l'extrait de code ci-dessous :

```jsx
class AmountText extends StatelessWidget {
  final String text;

  const AmountText(
    this.text, {
    Key key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.all(8),
      child: Text(text.toUpperCase(),
          style: TextStyle(fontWeight: FontWeight.bold, color: Colors.blueAccent, fontSize: 20)),
    );
  }
}

```

Ici, nous avons utilisé la classe de constructeur pour obtenir la valeur du texte réel à afficher. La méthode build de cette classe retourne le widget `Container` avec un simple `padding` et le widget `Text` comme widget enfant.

Puisque notre widget `AmountText` est prêt, nous pouvons maintenant appeler le widget dans le widget Stateful. 

Nous allons ajouter le widget à l'intérieur du widget `Column` que nous avons défini précédemment avec des widgets `Text` simples. Nous devons simplement remplacer le widget Text par le widget `AmountText` et passer les valeurs de texte requises.

Vous pouvez voir la mise en œuvre du codage dans l'extrait de code ci-dessous :

```jsx
Container(
  margin: EdgeInsets.all(15),
  padding: EdgeInsets.all(15),
  decoration: BoxDecoration(
    color: Colors.white,
    borderRadius: BorderRadius.all(
      Radius.circular(15),
    ),
    border: Border.all(color: Colors.white),
    boxShadow: [
      BoxShadow(
        color: Colors.black12,
        offset: Offset(2, 2),
        spreadRadius: 2,
        blurRadius: 1,
      ),
    ],
  ),
  child: Column(
    children: [
      AmountText(
        'Montant du pourboire : ${_getTipAmount()}',
        key: Key('tipAmount'),
      ),
      AmountText(
        'Montant total : ${_getTotalAmount()}',
        key: Key('totalAmount'),
      ),
    ],
  ),
),

```

Ici, nous avons passé la fonction à l'intérieur du widget `AmountText`. La fonction retourne les valeurs respectives du montant du pourboire et du montant total, comme vous pouvez le voir dans l'extrait de code ci-dessous :

```jsx
  _getTipAmount() => _billAmount * _tipPercentage / 100;

  _getTotalAmount() => _billAmount + _getTipAmount();

```

Enfin, nous devons terminer les contrôleurs lors de la sortie de la vue. Pour cela, nous devons utiliser la fonction intégrée `dispose`. Cette fonction s'exécute lorsque nous quittons l'écran actuel. 

À l'intérieur de cette méthode, nous devons appeler les contrôleurs avec les méthodes `dispose` afin de terminer les contrôleurs de texte de saisie. Cela fera en sorte que le contrôleur cesse d'écouter les changements dans les champs de saisie. 

Vous pouvez voir la fonction dispose dans l'extrait de code ci-dessous :

```dart
@override
void dispose() {
  // Pour s'assurer que nous ne laissons rien fuir, disposez de tout TextEditingController utilisé
  // lorsque ce widget est effacé de la mémoire.
  _billAmountController.dispose();
  _tipPercentageController.dispose();
  super.dispose();
}

```

Construisez et exécutez-le pour obtenir le résultat final de notre mise en œuvre de la calculatrice de pourboire, que vous pouvez voir dans la démonstration ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/tipgif.gif)

Vous remarquerez que la valeur des deux montants change lorsque nous modifions les entrées dans les champs de saisie. 

Nous sommes maintenant arrivés à la fin de ce tutoriel. Vous avez réussi à implémenter une simple calculatrice de pourboire en utilisant le framework Flutter et Dart.

## Où aller à partir d'ici ?

L'objectif principal de ce tutoriel était de vous enseigner les modèles de programmation de base dans le framework de développement d'applications Flutter en construisant une simple calculatrice de pourboire. 

Il existe de nombreux autres widgets et ajouts intéressants que vous pouvez explorer. Vous pouvez changer l'interface utilisateur de votre application tout en gardant les composants fonctionnels identiques. 

Dans l'ensemble, Flutter simplifie la conception d'interfaces utilisateur complexes avec le modèle de widget. Vous pouvez simplement créer une excellente interface utilisateur en empilant les widgets ensemble en utilisant leurs propriétés enfants. 

Une prochaine étape pourrait être d'utiliser les mécanismes de navigation de Flutter pour naviguer vers différents écrans. Flutter simplifie également l'ajout de menus de tiroir personnalisés et d'onglets inférieurs.

Ce n'est que le point de départ du développement Flutter. Il y a plus à découvrir que ce que l'on voit. Nous devons simplement continuer à explorer et à coder.

La démonstration de l'ensemble du projet est disponible sur [Codepen](https://codepen.io/razorabhu1995/pen/OJXwONm).

 Vous pouvez vous inspirer pour votre application [Flutter](http://instaflutter.com) à partir de celles qui existent déjà.

_Bon codage !_