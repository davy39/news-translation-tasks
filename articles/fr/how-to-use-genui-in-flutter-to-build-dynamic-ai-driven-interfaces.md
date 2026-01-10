---
title: Comment utiliser GenUI dans Flutter pour créer des interfaces dynamiques pilotées
  par l'IA
author: Atuoha Anthony
date: '2025-12-23T16:58:51.235Z'
originalURL: https://freecodecamp.org/news/how-to-use-genui-in-flutter-to-build-dynamic-ai-driven-interfaces
description: 'Dans le développement d''applications standard, l''interface utilisateur
  (UI) est statique. Vous écrivez le code d''un bouton, vous le compilez, et il reste
  un bouton pour toujours. GenUI bouleverse ce modèle.

  Avec GenUI, le SDK d''UI générative de Google, l''interface de votre application
  devient...'
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1766509116517/64c3ad0a-9328-4731-8292-90cc7fdbb60b.png
tags:
- name: Flutter
  slug: flutter
- name: Dart
  slug: dart
- name: genui
  slug: genui
- name: flutter-aware
  slug: flutter-aware
seo_desc: 'In standard app development, the User Interface (UI) is static. You write
  code for a button, compile it, and it remains a button forever. GenUI flips this
  model on its head.

  With GenUI, Google’s Generative UI SDK, your application''s interface becomes...'
---


Dans le développement d'applications standard, l'interface utilisateur (UI) est statique. Vous écrivez le code d'un bouton, vous le compilez, et il reste un bouton pour toujours. GenUI bouleverse ce modèle.

Avec GenUI, le SDK d'UI générative de Google, l'interface de votre application devient dynamique. Vous ne codez pas en dur les arbres de widgets. Au lieu de cela, vous fournissez à un agent d'IA, tel que Gemini de Google, un "kit" de composants UI appelé un Catalog et un objectif. L'IA génère ensuite l'UI en temps réel, décidant d'afficher un curseur, un champ de texte ou une carte complexe en fonction des besoins de l'utilisateur à ce moment précis.

Ce guide vous accompagne de zéro jusqu'à un générateur de cartes de Noël fonctionnel alimenté par l'IA, qui fait plus que générer du texte. Il génère également les véritables widgets Flutter pour les afficher.

Votre créateur de cartes de vœux de Noël utilisera l'UI générative et l'IA pour créer instantanément des cartes personnalisées de haute qualité. Les utilisateurs fournissent des entrées simples telles que le nom du destinataire, la relation et le thème de couleur préféré, et l'IA produit dynamiquement une interface de carte festive et soignée, complétée par un texte sincère, un style saisonnier et une mise en page structurée.

En combinant le modèle de données réactif de l'UI générative avec des widgets de catalogue personnalisés, ce projet vous montrera comment guider l'IA pour produire des interfaces utilisateur cohérentes et prêtes pour la production plutôt que des composants assemblés de manière lâche.

Il est important de noter que le package GenUI est actuellement en version Alpha et est hautement expérimental. Comme il en est aux premiers stades de développement, voici ce que vous devez garder à l'esprit :

*   **Stabilité de l'API :** Les classes, les signatures de méthodes et l'architecture globale décrites dans ce guide sont susceptibles de changer à mesure que l'équipe Flutter recueille les commentaires de la communauté.
    
*   **Sécurité et garde-fous :** Puisque l'UI est générée par un LLM, il existe toujours un risque non nul d'"hallucinations" où l'IA pourrait tenter d'utiliser des widgets ou des propriétés qui n'existent pas dans votre catalogue.
    
*   **Prêt pour la production :** Bien que GenUI soit incroyablement excitant pour le prototypage et les outils internes, il nécessite une gestion des erreurs robuste et des UI de secours pour garantir une expérience utilisateur fluide si le service d'IA est indisponible ou renvoie une structure invalide.
    

Pendant que vous travaillez sur ce guide, GenUI doit être compris comme un système collaboratif plutôt qu'autonome. Vous êtes toujours responsable de la définition du Catalog que l'IA peut utiliser, de la révision de la manière dont ces composants sont assemblés et du test de l'interface résultante dans des scénarios réels.

Ce guide présente GenUI dans une configuration guidée, où Flutter fournit la structure et les contraintes, et l'IA opère à l'intérieur de celles-ci pour assembler dynamiquement l'UI. L'objectif n'est pas de supprimer le jugement du développeur, mais de le déplacer de l'écriture manuelle d'arbres de widgets vers la conception, le façonnage et la validation du système qui les produit.

### **Table des matières**

1. [Prérequis](#heading-prerequis)
    
2. [Le modèle mental : comment GenUI réfléchit](#heading-le-modele-mental-comment-genui-reflechit)
    
3. [Associer les composants GenUI à l'application de carte de Noël](#heading-associer-les-composants-genui-a-lapplication-de-carte-de-noel)
    
    * [1. GenUiConversation dans l'application de carte de Noël](#heading-1-genuiconversation-dans-lapplication-de-carte-de-noel)
        
    * [2. Catalog comme contrainte de conception](#heading-2-catalog-comme-contrainte-de-conception)
        
    * [3. DataModel au cœur de la personnalisation](#heading-3-datamodel-au-coeur-de-la-personnalisation)
        
    * [4. ContentGenerator comme passerelle vers l'IA](#heading-4-contentgenerator-comme-passerelle-vers-lia)
        
    * [5. A2uiMessage comme intention, pas comme UI](#heading-5-a2uimessage-comme-intention-pas-comme-ui)
        
4. [Pourquoi cette architecture fonctionne](#heading-pourquoi-cette-architecture-fonctionne)
    
5. [Aperçu du projet : ce que nous construisons](#heading-apercu-du-projet-ce-que-nous-construisons)
    
6. [Structure du projet](#heading-structure-du-projet)
    
    * [Étape 1 : Créer un nouveau projet Flutter](#heading-etape-1-creer-un-nouveau-projet-flutter)
        
    * [Étape 2 : Configurer votre fournisseur d'agent](#heading-etape-2-configurer-votre-fournisseur-dagent)
        
    * [Étape 3 : Ajouter les dépendances](#heading-etape-3-ajouter-les-dependances)
        
    * [Étape 4 : Obtenir une clé API Google Gemini](#heading-etape-4-obtenir-une-cle-api-google-gemini)
        
    * [Étape 5 : Point d'entrée de l'application (main.dart)](#heading-etape-5-point-dentree-de-lapplication-maindart)
        
    * [Le widget racine de l'application](#heading-le-widget-racine-de-lapplication)
        
    * [Étape 6 : Le contrôleur logique (écran Stateful)](#heading-etape-6-le-controleur-logique-ecran-stateful)
        
    * [Étape 7 : Initialisation de GenUI et Firebase](#heading-etape-7-initialisation-de-genui-et-firebase)
        
    * [Étape 8 : Envoi d'un prompt dynamique à l'IA](#heading-etape-8-envoi-dun-prompt-dynamique-a-lia)
        
7. [Construction de la vue](#heading-construction-de-la-vue)
    
    * [Dossier : lib/screen/data/](#heading-dossier-libscreendata)
        
    * [Dossier : lib/extensions/](#heading-dossier-libextensions)
        
    * [Dossier : lib/screen/components/](#heading-dossier-libscreencomponents)
        
8. [Ajouter vos propres widgets au catalogue GenUI](#heading-ajouter-vos-propres-widgets-au-catalogue-genui)
    
    * [Pourquoi ajouter un widget personnalisé ?](#heading-pourquoi-ajouter-un-widget-personnalise)
        
    * [Étape 1 : Ajouter json\_schema\_builder](#heading-etape-1-ajouter-jsonschemabuilder)
        
    * [Étape 2 : Définir le schéma de la carte de vœux](#heading-etape-2-definir-le-schema-de-la-carte-de-voeux)
        
    * [Étape 3 : Créer le CatalogItem](#heading-etape-3-creer-le-catalogitem)
        
    * [Étape 4 : Enregistrer le widget dans votre application](#heading-etape-4-enregistrer-le-widget-dans-votre-application)
        
    * [Étape 5 : Apprendre à l'IA à utiliser le widget](#heading-etape-5-apprendre-a-lia-a-utiliser-le-widget)
        
    * [Comment cela s'intègre dans votre écran existant](#heading-comment-cela-sintegre-dans-votre-ecran-existant)
        
9. [Captures d'écran :](#heading-captures-decran)
    
10. [Dernières réflexions](#heading-dernieres-reflexions)
    
11. [Références](#heading-references)
    

## Prérequis

Pour suivre ce guide efficacement, vous avez besoin de :

1.  **Environnement de développement Flutter :** SDK Flutter installé (canal stable recommandé) et un IDE comme VS Code ou Android Studio configuré.
    
2.  **Connaissances de base de Flutter :** Vous devez comprendre comment les widgets se composent (Rows, Columns, Containers) et la gestion d'état de base (`setState` ou `FutureBuilder`).
    
3.  **Clé API Google AI Studio :** Nous utiliserons le modèle Gemini de Google. Vous devrez obtenir une clé API gratuite sur [Google AI Studio](https://aistudio.google.com/).
    

## Le modèle mental : comment GenUI réfléchit

Avant d'écrire du code, il est important de comprendre comment GenUI voit *conceptuellement* votre application. GenUI ne réfléchit pas en termes d'arbres de widgets ou d'écrans. Il réfléchit en termes de **surfaces**, d'**état** et de **conversations**.

Une surface est simplement un endroit où l'UI générée par l'IA peut apparaître. Une conversation contrôle la manière dont ces surfaces évoluent au fil du temps. Le modèle de données détient la vérité, et les messages font avancer le tout.

Voici le flux complet en un passage :

```dart
Action Utilisateur
   |
   v
GenUiConversation
   |
   v
ContentGenerator (IA)
   |
   v
Flux A2uiMessage
   |
   v
GenUiManager
   |
   v
DataModel + Surfaces UI
   |
   v
GenUiSurface (reconstruction Flutter)
```

Rien dans ce flux ne contourne Flutter. GenUI ne rend pas l'UI "en dehors" de Flutter – il décide seulement de **ce que Flutter doit rendre**.

## Associer les composants GenUI à l'application de carte de Noël

Maintenant, ancrons cela dans le générateur de cartes de Noël que nous allons construire. C'est ici que GenUI devient vraiment concret.

### 1. GenUiConversation dans l'application de carte de Noël

Dans le projet que nous allons construire, `GenUiConversation` représente l'interaction continue entre l'utilisateur et le générateur de cartes de Noël.

Lorsque l'utilisateur tape le nom d'un proche, sélectionne une relation, choisit une couleur et appuie sur **Generate Card**, votre application envoie ce prompt via `GenUiConversation`.

À ce moment-là, `GenUiConversation` connaît déjà l'historique de la conversation. Il sait s'il s'agit de la première carte générée ou si l'utilisateur régénère une carte avec un message différent. Ce contexte est ce qui permet à l'IA de créer des **cartes uniques pour chaque personne** au lieu de répéter une sortie générique.

Sans `GenUiConversation`, chaque requête serait sans état (stateless). Avec lui, l'application semble intentionnelle et personnelle.

### 2. Catalog comme contrainte de conception

Dans l'application de carte de Noël, le `Catalog` définit le langage visuel de vos cartes.

Vous pourriez autoriser l'IA à utiliser des widgets de texte pour les salutations, des widgets d'image pour les arrière-plans festifs, des widgets de conteneur pour la mise en page et des boutons pour la régénération ou le partage. Ce qui importe, c'est que l'IA ne peut pas s'échapper de ces contraintes.

C'est ainsi que vous garantissez que :

*   Les cartes ressemblent toujours à des cartes
    
*   L'IA n'invente pas d'UI non supportée
    
*   Votre application reste visuellement cohérente
    

Du point de vue de l'IA, le catalogue est la seule boîte à outils dans laquelle elle est autorisée à piocher. De votre point de vue, c'est le filet de sécurité qui maintient l'UI native à Flutter et prévisible.

### 3. DataModel au cœur de la personnalisation

Le `DataModel` est l'endroit où la personnalisation vit réellement.

Dans le projet que nous allons construire, des valeurs telles que le nom du destinataire, le message de vœux, le thème de la carte ou même les drapeaux d'animation vivent dans le modèle de données. Lorsque l'utilisateur modifie le nom ou régénère la carte, seules les parties de l'UI liées à ces valeurs changent.

C'est pourquoi GenUI semble dynamique sans être inefficace. Vous ne reconstruisez pas tout l'écran de la carte – vous ne mettez à jour que ce qui dépend des données modifiées.

Cela signifie également que l'IA n'a pas besoin de recréer toute l'UI à chaque fois. Elle peut simplement mettre à jour le modèle de données et laisser Flutter faire ce qu'il fait de mieux.

### 4. ContentGenerator comme passerelle vers l'IA

Le `ContentGenerator` est la seule partie de votre application qui sait comment parler à l'IA.

Dans l'exemple de la carte de Noël, ce composant envoie la requête de l'utilisateur au modèle avec des instructions système telles que "Générer une UI de carte de Noël festive en utilisant les widgets disponibles". Il écoute ensuite la réponse de l'IA.

Comme les réponses arrivent sous forme de flux (streams), l'UI peut commencer le rendu dès que les premières instructions arrivent. C'est particulièrement utile si vous ajoutez plus tard des animations ou des révélations progressives à vos cartes.

D'un point de vue conception, cette séparation est critique. Votre application Flutter ne dépend jamais directement du SDK de l'IA. Elle dépend de GenUI, et GenUI dépend du ContentGenerator.

### 5. A2uiMessage comme intention, pas comme UI

C'est l'un des concepts les plus importants à intérioriser : lorsque l'IA décide de générer une carte de Noël, elle n'envoie pas de widgets Flutter. Elle envoie plutôt des instructions `A2uiMessage`.

Un message pourrait dire "commencer le rendu d'une nouvelle surface". Un autre pourrait dire "mettre à jour le texte de salutation dans le modèle de données". Un autre encore pourrait dire "remplacer l'image d'arrière-plan".

Ces messages sont traités par le `GenUiManager`, qui traduit l'intention en changements réels de l'UI. Cette couche supplémentaire est ce qui empêche GenUI de devenir fragile ou imprévisible.

## Pourquoi cette architecture fonctionne

Ce qui rend GenUI puissant n'est pas le fait qu'il utilise l'IA. Beaucoup d'outils le font. Ce qui le rend puissant, c'est que **l'IA ne rompt jamais les règles de Flutter**, car l'état est centralisé, le rendu est contrôlé, les événements sont explicites et les mises à jour sont incrémentielles.

Dans l'application de carte de Noël, cela signifie que chaque carte semble personnalisée, chaque interaction semble réactive, et votre application reste maintenable même si la logique de l'IA devient plus complexe.

Une fois que vous comprenez ce flux, vous cessez de voir GenUI comme "l'IA générant de l'UI" et commencez à le voir comme **l'IA participant à la machine à états de votre application**.

## Aperçu du projet : ce que nous construisons

Dans ce tutoriel, nous allons construire un générateur de cartes de Noël en utilisant Flutter et GenUI. L'idée est simple mais intuitive : un utilisateur tape un nom, sélectionne une relation et une description de couleur de carte, et l'IA génère dynamiquement un arbre de widgets Flutter qui représente une carte de Noël personnalisée.

Ce projet démontre trois idées fondamentales de GenUI travaillant ensemble : la boucle de conversation, le rendu d'UI piloté par l'IA et les mises à jour d'état réactives sans câblage manuel des widgets.

À la fin, vous comprendrez non seulement comment utiliser GenUI, mais aussi comment structurer une véritable application Flutter autour de lui.

## Structure du projet

Nous garderons la structure intentionnellement simple afin qu'elle soit facile à suivre et à étendre plus tard.

```dart
lib/
 ├── extensions/
 │    ├── loading.dart
 ├── screen/
 │    ├── components/
 │    │    ├── color_picker_list.dart       // Widget pour la sélection de couleur
 │    │    ├── custom_input_section.dart    // Champs de formulaire de saisie
 │    │    ├── error_section.dart           // Affichage des messages d'erreur
 │    │   
 │    ├── data/
 │    │    └── static_list_data.dart        // Données codées en dur ou constantes
 │    ├── card_generator_screen.dart        // Logique UI principale pour générer des cartes
 │    └── christmas_card.dart               // Le widget/vue spécifique de la carte
 ├── firebase_options.dart                  // Fichier de configuration Firebase
 └── main.dart                              // Point d'entrée de l'application
```

### Étape 1 : Créer un nouveau projet Flutter

Commencez par créer une nouvelle application Flutter.

```bash
flutter create genui_christmas_card
cd genui_christmas_card
```

Cela nous donne une base propre avec le support de Material 3 et une configuration de plateforme appropriée.

### Étape 2 : Configurer votre fournisseur d'agent

`genui` peut se connecter à une variété de fournisseurs d'agents. Choisissez la section ci-dessous pour votre fournisseur préféré.

#### Configurer Firebase AI Logic

Pour utiliser le `FirebaseAiContentGenerator` intégré afin de se connecter à Gemini via Firebase AI Logic, suivez ces instructions :

1.  Créez un nouveau [projet Firebase](https://support.google.com/appsheet/answer/10104995) via la console Firebase.
    
2.  [Activez l'API Gemini](https://firebase.google.com/docs/gemini-in-firebase/set-up-gemini) pour ce projet.
    
3.  Suivez les trois premières étapes de la [configuration Flutter de Firebase](https://firebase.google.com/docs/flutter/setup) pour ajouter Firebase à votre application.
    
4.  Activez **Gemini Developer API**
    
    ![Firebase Dashboard](https://cdn.hashnode.com/res/hashnode/image/upload/v1766152091749/500feb24-bdb5-4126-a05e-287a945c0ed9.png align="center")
    

### Étape 3 : Ajouter les dépendances

GenUI est modulaire. Vous installez toujours le framework de base, puis vous ajoutez un générateur de contenu qui sait comment parler à votre fournisseur d'IA.

Ouvrez `pubspec.yaml` et mettez à jour vos dépendances :

```yaml
dependencies:
  flutter:
    sdk: flutter

  genui: ^0.6.0
  logging: ^1.2.0
  genui_firebase_ai: ^0.6.0
  firebase_core: ^4.3.0
  loader_overlay: ^5.0.0
  flutter_spinkit: ^5.2.2
```

Ensuite, récupérez les packages :

```bash
flutter pub get
```

À ce stade, votre projet a tout ce dont il a besoin pour générer de l'UI dynamiquement.

### Étape 4 : Obtenir une clé API Google Gemini

GenUI lui-même ne fournit pas de modèles d'IA. Vous devrez en connecter un. Pour ce faire, allez sur Google AI Studio, créez une nouvelle clé API et copiez-la.

Note importante : Pour les applications de production réelles, ne codez jamais les clés API en dur. Utilisez `--dart-define`, des variables d'environnement ou un proxy backend.

### Étape 5 : Point d'entrée de l'application (`main.dart`)

Nous allons maintenant commencer à écrire du code réel.

Remplacez le contenu de `lib/main.dart` par ce qui suit :

```dart
import 'package:flutter/material.dart';
import 'package:genui_flutter/screen/christmas_card.dart';
import 'package:logging/logging.dart';
import 'package:firebase_core/firebase_core.dart';
import 'firebase_options.dart';

void main() async{
  // Activer la journalisation verbeuse pour voir exactement
  // ce que l'IA renvoie à GenUI.
  Logger.root.level = Level.ALL;
  Logger.root.onRecord.listen((record) {
    debugPrint(
      '${record.level.name}: ${record.time}: ${record.message}',
    );
  });

    WidgetsFlutterBinding.ensureInitialized();
    await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);
    runApp(const ChristmasCardApp());
}
```

Cette configuration de journalisation est facultative, mais fortement recommandée. Lorsque quelque chose ne va pas, les journaux sont souvent le moyen le plus rapide de comprendre pourquoi l'IA n'a pas généré ce que vous attendiez.

### Le widget racine de l'application

Ensuite, nous définissons le widget racine de notre application.

```dart
import 'package:flutter/material.dart';
import 'package:loader_overlay/loader_overlay.dart';
import 'card_generator_screen.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';

class ChristmasCardApp extends StatelessWidget {
  const ChristmasCardApp({super.key});

  @override
  Widget build(BuildContext context) {
    return Directionality(
      textDirection: TextDirection.ltr,
      child: LoaderOverlay(
        overlayWholeScreen: true,
        overlayWidgetBuilder: (_) {
          return const Center(
            child: SpinKitWaveSpinner(color: Colors.red, size: 50.0),
          );
        },
        child: MaterialApp(
          title: 'GenUI Christmas Card Generator',
          theme: ThemeData(
            colorScheme: ColorScheme.fromSeed(
              seedColor: Colors.red,
              primary: Colors.red,
            ),
            useMaterial3: true,
          ),
          home: const CardGeneratorScreen(),
        ),
      ),
    );
  }
}
```

C'est du Flutter standard – rien de spécifique à GenUI pour l'instant. Le vrai travail se passe à l'intérieur de `CardGeneratorScreen`.

### Étape 6 : Le contrôleur logique (écran Stateful)

Cet écran est l'endroit où nous relions Flutter, Firebase AI et la logique GenUI. Il gère les entrées utilisateur (Nom, Relation, Couleur) et orchestre la génération par l'IA.

```dart
class CardGeneratorScreen extends StatefulWidget {
  const CardGeneratorScreen({super.key});

  @override
  State<CardGeneratorScreen> createState() => _CardGeneratorScreenState();
}
```

Maintenant la classe d'état, qui contient toute la logique GenUI et l'état du formulaire :

```dart
class _CardGeneratorScreenState extends State<CardGeneratorScreen> {
  // 1. Gestion de l'état du formulaire
  final TextEditingController nameController = TextEditingController();
  String selectedRelationship = 'Friend';
  String selectedColorName = 'Gold';
  Color selectedColorUi = Colors.amber;

  // 2. Composants de base GenUI
  late final A2uiMessageProcessor _a2uiMessageProcessor;
  late final FirebaseAiContentGenerator _contentGenerator;
  late final GenUiConversation _conversation;

  // 3. État de l'UI
  String? currentSurfaceId;
  String? errorMessage;
```

L'application gère les entrées utilisateur via un état de formulaire qui permet l'injection de prompts dynamiques, tandis que le `_a2uiMessageProcessor` agit comme un décodeur pour convertir les données brutes de l'IA en widgets Flutter spécifiques.

La connexion backend est gérée par le `FirebaseAiContentGenerator`, qui gère les instructions système et les catalogues d'outils, tandis que l'objet `_conversation` sert de chef d'orchestre pour gérer l'historique du chat et router les données entre l'IA et l'UI.

Enfin, le `currentSurfaceId` suit l'arbre de widgets spécifique affiché, garantissant que la `GenUiSurface` rend le contenu correct généré par l'IA.

### Étape 7 : Initialisation de GenUI et Firebase

Toute la configuration se fait dans `initState` :

```dart
  @override
  void initState() {
    super.initState();
    // 1. Configurer le processeur avec les widgets autorisés
    _a2uiMessageProcessor = A2uiMessageProcessor(
      catalogs: [CoreCatalogItems.asCatalog()],
    );

    // 2. Configurer la personnalité et les règles de l'IA
     _contentGenerator = FirebaseAiContentGenerator(
      catalog: CoreCatalogItems.asCatalog(),
      systemInstruction: '''
          Vous êtes un expert en design d'UI festive et un rédacteur de vœux.
          
          VOTRE OBJECTIF : Générer une carte de Noël haut de gamme et visuellement attrayante en utilisant l'outil `surfaceUpdate`, adaptée à l'impression ou au partage numérique. La carte doit sembler personnalisée, chaleureuse et festive.
          
          DIRECTIVES DE DESIGN :
          - Mise en page : Utilisez une Column verticale à l'intérieur d'un Container avec des coins arrondis, un rembourrage généreux et une bordure. Remplissez le Container avec une couleur qui **mélange le Rouge avec $selectedColorName ** pour créer un arrière-plan riche sur le thème des fêtes.
          - Typographie : Utilisez des graisses de police distinctes (Gras pour les en-têtes, normal pour le corps). Centrez tout le texte.
          - Visuels : Incluez des icônes saisonnières (🎄, ✨, ❄️) comme éléments décoratifs. Placez un emoji de sapin de Noël de manière stratégique sans encombrer la mise en page.
          - Personnalisation : Affichez le nom du destinataire de manière proéminente au milieu de la carte de façon visuellement frappante.
          
          DIRECTIVES DE RÉDACTION :
          - Créez un message de vœux profondément personnel et sincère (3-4 phrases) qui correspond au type de relation (amusant pour les amis, romantique pour le conjoint, chaleureux pour la famille).
          - Incluez une clôture/signature appropriée.
          - Ne JAMAIS utiliser de textes de remplacement. Générez toujours le **texte final prêt à être affiché**.
          
          INSTRUCTIONS DE SORTIE :
          - Utilisez l'outil `surfaceUpdate` pour construire l'UI.
          - Assurez-vous que tous les éléments (Container, texte, emojis) sont visuellement alignés et harmonieux.
          - La carte doit sembler festive, élégante et équilibrée.
          ''',
    );

    // 3. Démarrer la conversation et écouter les mises à jour
    _conversation = GenUiConversation(
      contentGenerator: _contentGenerator,
      a2uiMessageProcessor: _a2uiMessageProcessor,
      onSurfaceAdded: _onSurfaceAdded,
      onSurfaceDeleted: _onSurfaceDeleted,
    );
  }

  void _onSurfaceAdded(SurfaceAdded update) {
    setState(() {
      currentSurfaceId = update.surfaceId;
    });
  }
```

Dans la méthode `initState`, nous configurons d'abord l' `A2uiMessageProcessor` avec `CoreCatalogItems`, donnant à l'IA l'accès aux widgets standard. Ensuite, nous initialisons `FirebaseAiContentGenerator`.

Notez la `systemInstruction` : vous donnez à l'IA deux rôles distincts ici ; "Designer UI" et "Rédacteur". Vous lui dites explicitement d'écrire un contenu spécifique basé sur les relations et de concevoir un texte centré.

Enfin, nous les lions dans `GenUiConversation` et attachons un écouteur (`_onSurfaceAdded`). Lorsque l'IA crée une nouvelle UI, nous mettons à jour `currentSurfaceId` à l'intérieur de `setState`, ce qui indique à Flutter de dessiner la nouvelle carte.

### Étape 8 : Envoi d'un prompt dynamique à l'IA

Cette méthode lance la génération, en utilisant les données du formulaire de l'utilisateur pour construire un prompt spécifique.

```dart
  Future<void> generateCard() async {
    if (nameController.text.trim().isEmpty) {
      setState(() {
        errorMessage = "Veuillez d'abord entrer un nom !";
      });
      return;
    }
    FocusScope.of(context).unfocus();
    setState(() {
      errorMessage = null;
      currentSurfaceId = null;
    });

    try {
      context.showLoader();
       final prompt = '''
        Créez une carte de Noël personnalisée pour mon/ma $selectedRelationship, ${nameController.text}.
        Thème : Mélangez le Rouge et le $selectedColorName pour un arrière-plan festif.
        Mise en page : Column verticale dans un Container arrondi avec rembourrage et bordure ; placez le nom du destinataire de manière proéminente au centre.
        Visuels : Ajoutez des sapins de Noël (🎄), des étincelles (✨) ou des flocons de neige (❄️) là où c'est approprié.
        Typographie : En-têtes en gras, texte de corps normal, tout centré.
        Message : Écrivez un message de vœux chaleureux et personnel de 3-4 phrases qui correspond au type de relation, se terminant par une signature appropriée.
        Design : Faites en sorte qu'elle ressemble à une carte de Noël élégante et festive, prête à être affichée ou partagée.
        ''';


      await _conversation.sendRequest(UserMessage.text(prompt));
    } catch (e) {
      debugPrint('Erreur : $e');
      if (mounted) {
        setState(() {
          errorMessage = "Oups ! Échec de la création de la carte.\nErreur : $e";
        });
      }
    } finally {
      if (mounted) {
        context.hideLoader();
      }
    }
  }
```

La méthode `generateCard` est l'endroit où l'ingénierie de prompt rencontre le code. D'abord, elle valide qu'un nom existe. Ensuite, elle construit une chaîne multiligne en utilisant l'interpolation de chaîne (`$selectedRelationship`, `$selectedColorName`). Au lieu d'une requête générique, vous envoyez un brief détaillé : "Faites une carte pour ma maman nommée Alice en utilisant des couleurs dorées."

Enfin, `_conversation.sendRequest` envoie ce prompt à Firebase. Nous enveloppons cela dans un bloc try/catch pour gérer les erreurs réseau avec élégance en affichant le message d'erreur dans l'UI.

## Construction de la vue

Nous allons maintenant rendre l'UI complexe en utilisant les composants d'aide que nous avons créés dans le dossier `components/`. Voici le code – mais ne vous inquiétez pas, nous couvrirons chaque composant personnalisé individuellement après cela.

```dart
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('🎄 Créateur de cartes de vœux')...),
      body: Stack(
        children: [
          Column(
            children: [
              // 1. Le formulaire de saisie (refactorisé en composant)
              CustomInputSection(
                nameController: nameController,
                selectedRelationship: selectedRelationship,
                selectedColorName: selectedColorName,
                selectedColorUi: selectedColorUi,
                onColorSelected: onColorSelected,
                generateCard: generateCard,
                selectRelationship: selectRelationship,
              ),
              
              const Divider(height: 1),
              
              // 2. La zone de dessin GenUI
              Expanded(
                child: Container(
                  color: Colors.grey[100],
                  child: currentSurfaceId != null
                      ? GenUiSurface(
                          host: _conversation.host,
                          surfaceId: currentSurfaceId!,
                        )
                      : const Center(child: Text('Remplissez les détails...')),
                ),
              ),
            ],
          ),


          if (errorMessage != null)
            ErrorSection(errorMessage: errorMessage!, clearError: clearError),
        ],
      ),
    );
  }
}
```

Dans la méthode build, nous utilisons un Stack pour nous permettre de faire flotter le `LoadingWidget` et l' `ErrorSection` au-dessus du contenu principal.

Au lieu d'écrire toute la logique de saisie ici, vous avez utilisé `CustomInputSection`. Cela garde l'écran principal propre et concentré sur l'orchestration de l'IA.

La moitié inférieure de l'écran contient la `GenUiSurface`. Si `currentSurfaceId` existe, elle rend l'arbre de widgets de l'IA en utilisant `_conversation.host`. Sinon, elle affiche une instruction de remplacement.

À ce stade, vous avez vu la méthode `build()` complète qui rend l'écran. Remarquez que l'écran lui-même fait très peu de travail visuel direct. Au lieu de cela, il compose l'UI à partir de widgets plus petits et ciblés et de fichiers d'aide. C'est intentionnel.

Plutôt que d'entasser les champs de formulaire, les sélecteurs de couleurs, la gestion des erreurs et les constantes dans un seul fichier d'écran, l'UI est divisée en dossiers clairs et axés sur un but précis. Chaque dossier représente une **préoccupation UI**, et non une couche de gestion d'état ou un modèle architectural.

Dans les sections suivantes, nous parcourrons ces dossiers un par un, en montrant comment chaque pièce contribue à l'écran final que vous venez de construire. Vous verrez où vivent les widgets réutilisables, où les données UI statiques sont définies et comment l'écran principal lie le tout sans devenir encombré.

### Dossier : `lib/screen/data/`

Ce dossier contient les données statiques utilisées pour remplir les listes déroulantes et les listes de couleurs.

#### StaticListData : `lib/screen/data/static_list_data.dart`

```dart
import 'package:flutter/material.dart';

class StaticListData {
  // Liste des relations pour le menu déroulant
  static final List<String> relationships = [
    'Mari',
    'Femme',
    'Fils',
    'Fille',
    'Grand-mère',
    'Grand-père',
    'Oncle',
    'Tante',
    'Ami(e)',
    'Parent',
    'Cousin(e)',
    'Petit-fils',
    'Petite-fille',
    'Maman',
    'Papa',
  ];

  // Map des noms de couleurs vers les objets Color Flutter réels
  static final Map<String, Color> colorOptions = {
    'Or': Colors.amber,
    'Vert': Colors.green,
    'Bleu': Colors.blue,
    'Violet': Colors.deepPurple,
    'Argent': Colors.grey,
    'Jaune': Colors.yellow,
    'Rose': Colors.pink,
  };
}
```

Cette classe sert de dépôt central pour les données constantes, hébergeant la liste `relationships` pour permettre des mises à jour faciles de l'UI, comme l'ajout de "Collègue" ou "Voisin", sans modifier le code de base, et la map `colorOptions`, qui traduit des noms conviviaux comme "Or" en objets `Color` fonctionnels comme `Colors.amber` pour le style.

### Dossier : `lib/extensions/`

Ce dossier contient les données statiques utilisées pour remplir les listes déroulantes et les listes de couleurs.

#### LoaderOverlayExtension : `lib/extensions/loading.dart`

```dart
import 'package:flutter/material.dart';
import 'package:loader_overlay/loader_overlay.dart';

extension LoaderOverlayExtension on BuildContext {
  void showLoader() {
    loaderOverlay.show();
  }

  void hideLoader() {
    loaderOverlay.hide();
  }
}
```

L' `LoaderOverlayExtension` ajoute deux méthodes à tout objet `BuildContext` : `showLoader()`, qui affiche un `LoaderOverlay`, et `hideLoader()`, qui le cache. Cela vous permet d'appeler `context.showLoader()` ou `context.hideLoader()` n'importe où dans vos widgets sans référencer directement `loaderOverlay` à chaque fois, améliorant la lisibilité et réduisant le code répétitif chaque fois qu'un état de chargement doit être affiché.

### Dossier : `lib/screen/components/`

Ce dossier contient des composants UI réutilisables qui sont utilisés spécifiquement sur les écrans de votre application, en particulier le `CardGeneratorScreen`. Ce sont des widgets plus petits et modulaires qui encapsulent une partie de l'UI, rendant le code de l'écran principal plus propre, plus facile à lire et maintenable.

#### ErrorSection : `error_section.dart`

```dart
import 'package:flutter/material.dart';

class ErrorSection extends StatelessWidget {
  final String errorMessage;
  final VoidCallback clearError;

  const ErrorSection({
    super.key,
    required this.errorMessage,
    required this.clearError,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      // Arrière-plan à haute opacité pour bloquer l'UI derrière
      color: Colors.white.withOpacity(0.95),
      child: Center(
        child: Padding(
          padding: const EdgeInsets.all(32.0),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              const Icon(Icons.error_outline, color: Colors.red, size: 60),
              const SizedBox(height: 16),
              // Affiche le message d'erreur spécifique transmis par le parent
              Text(
                errorMessage,
                textAlign: TextAlign.center,
                style: const TextStyle(fontSize: 16, color: Colors.red),
              ),
              const SizedBox(height: 20),
              // Bouton pour fermer l'erreur
              ElevatedButton(
                onPressed: () {
                  clearError();
                },
                child: const Text("Réessayer"),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

Cette vue de gestion des erreurs robuste utilise une grande icône rouge et un texte descriptif pour signaler clairement un problème, tout en incorporant un rappel `clearError` qui se déclenche lorsque le bouton "Réessayer" est cliqué pour réinitialiser la variable `errorMessage` de l'état parent et fermer la vue.

#### ColorPickerList : `color_picker_list.dart`

```dart
import 'package:flutter/material.dart';

class ColorPickerList extends StatelessWidget {
  const ColorPickerList({
    super.key,
    required String selectedColorName,
    required Color selectedColorUi,
    required Map<String, Color> colorOptions,
    required this.onColorSelected,
  })  : _selectedColorName = selectedColorName,
        _colorOptions = colorOptions;

  final String _selectedColorName;
  final Map<String, Color> _colorOptions;
  final void Function(String colorName, Color colorUi) onColorSelected;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 85,
      // Liste à défilement horizontal pour les couleurs
      child: ListView(
        scrollDirection: Axis.horizontal,
        physics: const BouncingScrollPhysics(),
        children: _colorOptions.entries.map((entry) {
          final isSelected = _selectedColorName == entry.key;

          return GestureDetector(
            onTap: () {
              // Renvoie la couleur sélectionnée au parent
              onColorSelected(entry.key, entry.value);
            },
            child: Container(
              margin: const EdgeInsets.only(right: 15),
              width: 50,
              child: Column(
                mainAxisSize: MainAxisSize.min,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  // Animation de l'anneau extérieur
                  AnimatedContainer(
                    duration: const Duration(milliseconds: 250),
                    padding: const EdgeInsets.all(3),
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      // Affiche la bordure seulement si sélectionné
                      border: Border.all(
                        color: isSelected ? entry.value : Colors.transparent,
                        width: 2.5,
                      ),
                    ),
                    // Cercle de couleur intérieur
                    child: Container(
                      width: 35,
                      height: 35,
                      decoration: BoxDecoration(
                        color: entry.value,
                        shape: BoxShape.circle,
                        boxShadow: [
                          if (isSelected)
                            BoxShadow(
                              color: entry.value.withOpacity(0.3),
                              blurRadius: 6,
                              offset: const Offset(0, 3),
                            ),
                        ],
                        border: Border.all(color: Colors.white, width: 2),
                      ),
                    ),
                  ),
                  const SizedBox(height: 6),
                  // Libellé du nom de la couleur
                  Text(
                    entry.key,
                    textAlign: TextAlign.center,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(
                      fontSize: 10,
                      color: isSelected ? entry.value : Colors.grey[600],
                      fontWeight:
                          isSelected ? FontWeight.bold : FontWeight.normal,
                    ),
                  ),
                ],
              ),
            ),
          );
        }).toList(),
      ),
    );
  }
}
```

Cette liste horizontale de cercles de couleurs utilise un `ListView` avec `scrollDirection: Axis.horizontal` pour permettre aux utilisateurs de parcourir diverses options, tandis qu'un `AnimatedContainer` fournit un retour visuel soigné en animant la bordure extérieure lors d'un appui sur une couleur en 250ms.

Le widget incorpore également une logique de sélection qui vérifie l'état `isSelected` pour déterminer s'il faut afficher le texte en gras et une bordure colorée, indiquant clairement le choix actuel de l'utilisateur.

#### CustomInputSection `custom_input_section.dart`

```dart
import 'package:flutter/material.dart';
import '../data/static_list_data.dart';
import 'color_picker_list.dart';

class CustomInputSection extends StatelessWidget {
  final TextEditingController nameController;
  final String selectedRelationship;
  final String selectedColorName;
  final Color selectedColorUi;
  final void Function(String colorName, Color colorUi) onColorSelected;
  final VoidCallback generateCard;
  final Function selectRelationship;

  const CustomInputSection({
    super.key,
    required this.nameController,
    required this.selectedRelationship,
    required this.selectedColorName,
    required this.selectedColorUi,
    required this.onColorSelected,
    required this.generateCard,
    required this.selectRelationship,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: Colors.white,
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.05),
            blurRadius: 10,
            offset: const Offset(0, 5),
          ),
        ],
      ),
      child: LayoutBuilder(
        builder: (context, constraints) {
          bool isSmallScreen = constraints.maxWidth < 600;

          return Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 18.0,vertical: 20),
                child: Flex(
                  direction: isSmallScreen ? Axis.vertical : Axis.horizontal,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Expanded(
                      flex: isSmallScreen ? 0 : 3,
                      child: SizedBox(
                        width: isSmallScreen ? double.infinity : null,
                        child: TextField(
                          controller: nameController,
                          decoration: const InputDecoration(
                            labelText: "Nom (ex: Alice)",
                            prefixIcon: Icon(Icons.person),
                            border: OutlineInputBorder(),
                            contentPadding: EdgeInsets.symmetric(
                              horizontal: 12,
                              vertical: 8,
                            ),
                          ),
                        ),
                      ),
                    ),
                    // Espaceur dynamique
                    isSmallScreen
                        ? const SizedBox(height: 12)
                        : const SizedBox(width: 10),
                    Expanded(
                      flex: isSmallScreen ? 0 : 2,
                      child: SizedBox(
                        width: isSmallScreen ? double.infinity : null,
                        child: DropdownButtonFormField<String>(
                          initialValue: selectedRelationship,
                          decoration: const InputDecoration(
                            labelText: 'Relation',
                            border: OutlineInputBorder(),
                            contentPadding: EdgeInsets.symmetric(
                              horizontal: 12,
                              vertical: 8,
                            ),
                          ),
                          items: StaticListData.relationships.map((String rel) {
                            return DropdownMenuItem(value: rel, child: Text(rel));
                          }).toList(),
                          onChanged: (val) => selectRelationship(val),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 20),
              Padding(
                padding: const EdgeInsets.only(left: 18.0),
                child: Text(
                  "Choisissez une couleur de thème :",
                  style: TextStyle(
                    color: Colors.grey[700],
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              const SizedBox(height: 8),

              Padding(
                padding: const EdgeInsets.only(left: 16.0),
                child: Flex(
                  direction: isSmallScreen ? Axis.vertical : Axis.horizontal,
                  crossAxisAlignment: isSmallScreen
                      ? CrossAxisAlignment.stretch
                      : CrossAxisAlignment.center,
                  children: [
                    isSmallScreen
                        ? ColorPickerList(
                            selectedColorName: selectedColorName,
                            selectedColorUi: selectedColorUi,
                            colorOptions: StaticListData.colorOptions,
                            onColorSelected: onColorSelected,
                          )
                        : Expanded(
                            child: ColorPickerList(
                              selectedColorName: selectedColorName,
                              selectedColorUi: selectedColorUi,
                              colorOptions: StaticListData.colorOptions,
                              onColorSelected: onColorSelected,
                            ),
                          ),

                    if (isSmallScreen) const SizedBox(height: 16),

                    // Bouton Générer
                    Padding(
                      padding: const EdgeInsets.all(18.0),
                      child: SizedBox(
                        width: isSmallScreen ? double.infinity : null,
                        child: ElevatedButton.icon(
                          onPressed: generateCard,
                          style: ElevatedButton.styleFrom(
                            backgroundColor: Colors.red,
                            foregroundColor: Colors.white,
                            padding: const EdgeInsets.symmetric(
                              horizontal: 24,
                              vertical: 16,
                            ),
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(8),
                            ),
                          ),
                          icon: const Icon(Icons.auto_awesome),
                          label: const Text(
                            "Générer la carte",
                            style: TextStyle(fontWeight: FontWeight.bold),
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ],
          );
        },
      ),
    );
  }
}
```

En tant que composant le plus complexe de l'architecture, ce widget agrège toutes les entrées en utilisant un `LayoutBuilder` pour surveiller les contraintes parentes, changeant dynamiquement la direction du `Flex` entre `Axis.horizontal` pour les tablettes et le web et `Axis.vertical` pour l'empilement mobile lorsque la `maxWidth` est inférieure à 600.

Pour assurer une mise en page fluide sur tous les appareils, il exploite `Expanded` sur les grands écrans pour remplir l'espace disponible tout en utilisant `SizedBox(width: double.infinity)` sur les écrans plus petits pour forcer les entrées sur toute la largeur de l'appareil, tout en maintenant un code propre en intégrant la `ColorPickerList` et `StaticListData`.

## Ajouter vos propres widgets au catalogue GenUI

Jusqu'à présent dans ce projet, nous nous sommes entièrement appuyés sur les widgets fournis par `CoreCatalogItems`. Ceux-ci incluent des blocs de construction UI courants comme `Text`, `Column`, `Container` et `Image`, qui suffisent pour obtenir des résultats étonnamment riches.

Mais GenUI brille vraiment lorsque vous apprenez à l'IA à connaître **vos propres widgets spécifiques à votre domaine**.

Dans notre cas, nous ne générons pas seulement une UI arbitraire – nous générons des cartes de Noël personnalisées haut de gamme. Cela en fait un candidat parfait pour un élément de catalogue personnalisé.

Au lieu d'espérer que l'IA assemble la mise en page parfaite à chaque fois à partir de widgets primitifs, nous pouvons introduire un widget "Holiday Card" de premier ordre et laisser le modèle générer des données pour celui-ci.

### Pourquoi ajouter un widget personnalisé ?

Dans l'implémentation actuelle, l'IA génère des UI festives en utilisant des widgets à usage général, ce qui fonctionne mais conduit à une structure de carte incohérente, des instructions de style répétées et une liberté de mise en page excessive.

En introduisant un widget personnalisé dans le catalogue, les décisions de mise en page et de style sont encodées directement dans Flutter. Cela permet à l'IA de se concentrer sur le contenu et la personnalisation tout en produisant des résultats plus prévisibles et prêts pour la production.

### Étape 1 : Ajouter `json_schema_builder`

Pour définir un widget personnalisé, GenUI doit savoir quelles données il accepte. Vous pouvez lui dire cela en utilisant un schéma JSON.

Ajoutez `json_schema_builder` comme dépendance, en utilisant la même référence de dépôt que GenUI :

```yaml
dependencies:
  json_schema_builder:
    git:
      url: https://github.com/flutter/genui.git
      path: packages/json_schema_builder
```

Cela garantit la compatibilité du schéma avec le runtime GenUI.

### Étape 2 : Définir le schéma de la carte de vœux

Une carte de Noël dans notre application a besoin de quelques données de base :

*   Le nom du destinataire
    
*   La relation (ami, conjoint, famille, etc.)
    
*   Le corps du message
    
*   Une signature de clôture
    

En utilisant `json_schema_builder`, nous pouvons définir cela explicitement :

```dart
final holidayCardSchema = S.object(
  properties: {
    'recipientName': S.string(
      description: 'Nom de la personne recevant la carte',
    ),
    'relationship': S.string(
      description: 'Relation avec le destinataire (ami, conjoint, famille)',
    ),
    'message': S.string(
      description: 'Message de vœux principal et sincère',
    ),
    'signature': S.string(
      description: 'Signature de clôture pour la carte',
    ),
  },
  required: [
    'recipientName',
    'relationship',
    'message',
    'signature',
  ],
);
```

Ce schéma devient le contrat entre votre application Flutter et l'IA.

### Étape 3 : Créer le CatalogItem

Chaque widget personnalisé est enregistré en tant que `CatalogItem`. Cela lie ensemble :

*   Un **nom** (utilisé par l'IA)
    
*   Le **schéma**
    
*   Un **widget builder** qui rend l'UI Flutter
    

Voici à quoi pourrait ressembler un élément de catalogue `HolidayCard` :

```dart
final holidayCardItem = CatalogItem(
  name: 'HolidayCard',
  dataSchema: holidayCardSchema,
  widgetBuilder: (context) {
    final name = context.dataContext.subscribeToString(
      context.data['recipientName'] as Map<String, Object?>?,
    );
    final message = context.dataContext.subscribeToString(
      context.data['message'] as Map<String, Object?>?,
    );
    final signature = context.dataContext.subscribeToString(
      context.data['signature'] as Map<String, Object?>?,
    );

    return ValueListenableBuilder<String?>(
      valueListenable: name,
      builder: (context, recipientName, _) {
        return ValueListenableBuilder<String?>(
          valueListenable: message,
          builder: (context, body, _) {
            return ValueListenableBuilder<String?>(
              valueListenable: signature,
              builder: (context, signOff, _) {
                return Container(
                  margin: const EdgeInsets.all(24),
                  padding: const EdgeInsets.all(24),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(20),
                    border: Border.all(color: Colors.redAccent),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      const Text(
                        '🎄 Joyeux Noël 🎄',
                        style: TextStyle(
                          fontSize: 24,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      const SizedBox(height: 16),
                      Text(
                        'Cher/Chère ${recipientName ?? ''},',
                        style: const TextStyle(fontSize: 18),
                      ),
                      const SizedBox(height: 12),
                      Text(
                        body ?? '',
                        textAlign: TextAlign.center,
                      ),
                      const SizedBox(height: 24),
                      Text(
                        signOff ?? '',
                        style: const TextStyle(fontWeight: FontWeight.w600),
                      ),
                    ],
                  ),
                );
              },
            );
          },
        );
      },
    );
  },
);
```

Remarquez qu'**aucun état n'est stocké dans le widget lui-même**. Tout provient du modèle de données GenUI.

### Étape 4 : Enregistrer le widget dans votre application

Nous allons maintenant brancher le widget personnalisé dans votre configuration existante.

Dans votre `initState`, au lieu d'utiliser uniquement `CoreCatalogItems`, étendez le catalogue :

```dart
_a2uiMessageProcessor = A2uiMessageProcessor(
  catalogs: [
    CoreCatalogItems.asCatalog().copyWith([
      holidayCardItem,
    ]),
  ],
);
```

Cela rend `HolidayCard` disponible pour l'IA.

### Étape 5 : Apprendre à l'IA à utiliser le widget

Enfin, nous mettrons à jour l'instruction système pour que l'IA sache quand et comment utiliser le nouveau widget.

Dans votre `FirebaseAiContentGenerator` existant, l'instruction peut être affinée comme ceci :

```text
      _contentGenerator = FirebaseAiContentGenerator(
      catalog: CoreCatalogItems.asCatalog(),
      systemInstruction: '''
          Vous êtes un expert en design d'UI festive et un rédacteur de vœux.
          
          VOTRE OBJECTIF : Générer une carte de Noël haut de gamme et visuellement attrayante en utilisant l'outil `surfaceUpdate`, adaptée à l'impression ou au partage numérique. La carte doit sembler personnalisée, chaleureuse et festive.
          
          DIRECTIVES DE DESIGN :
          - Mise en page : Utilisez une Column verticale à l'intérieur d'un Container avec des coins arrondis, un rembourrage généreux et une bordure. Remplissez le Container avec une couleur qui **mélange le Rouge avec $selectedColorName ** pour créer un arrière-plan riche sur le thème des fêtes.
          - Typographie : Utilisez des graisses de police distinctes (Gras pour les en-têtes, normal pour le corps). Centrez tout le texte.
          - Visuels : Incluez des icônes saisonnières (🎄, ✨, ❄️) comme éléments décoratifs. Placez un emoji de sapin de Noël de manière stratégique sans encombrer la mise en page.
          - Personnalisation : Affichez le nom du destinataire de manière proéminente au milieu de la carte de façon visuellement frappante.
          
          DIRECTIVES DE RÉDACTION :
          - Créez un message de vœux profondément personnel et sincère (3-4 phrases) qui correspond au type de relation (amusant pour les amis, romantique pour le conjoint, chaleureux pour la famille).
          - Incluez une clôture/signature appropriée.
          - Ne JAMAIS utiliser de textes de remplacement. Générez toujours le **texte final prêt à être affiché**.
          
          INSTRUCTIONS DE SORTIE :
          - Utilisez l'outil `surfaceUpdate` pour construire l'UI.
          - Assurez-vous que tous les éléments (Container, texte, emojis) sont visuellement alignés et harmonieux.
          - La carte doit sembler festive, élégante et équilibrée. Lors de la génération d'une carte de Noël, utilisez toujours le widget HolidayCard.
          ''',
    );
```

Maintenant, l'IA ne devine plus – elle est explicitement guidée vers votre widget personnalisé.

### Comment cela s'intègre dans votre écran existant

Cette intégration ne nécessite **aucun changement structurel** à votre `CardGeneratorScreen` existant : `GenUiConversation` continue de gérer le cycle de vie de l'interaction, `GenUiSurface` gère toujours le rendu, et votre formulaire de saisie reste entièrement responsable du façonnage du prompt. Le seul changement est ce que l'IA est autorisée à générer, ce qui améliore considérablement le contrôle et la cohérence.

En ajoutant des widgets personnalisés au catalogue GenUI, votre application passe d'une IA assemblant des fragments d'UI vaguement définis à une IA remplissant des composants structurés et prêts pour la production, ce qui se traduit par une interface plus propre, une identité visuelle plus forte, une ingénierie de prompt réduite et des sorties beaucoup plus prévisibles. C'est à ce stade que GenUI cesse de ressembler à une démo et commence à fonctionner comme un véritable framework de produit.

## Captures d'écran :

![App Screenshot 1 - Entrée](https://cdn.hashnode.com/res/hashnode/image/upload/v1766152202325/f14bf403-1b72-4e71-b6de-e0966cd51da2.png align="center")

![App Screenshot 2 - État d'erreur](https://cdn.hashnode.com/res/hashnode/image/upload/v1766155136764/bd14dd42-43cd-4897-a881-274376258935.png align="center")

![App Screenshot 3 - Choix de couleur](https://cdn.hashnode.com/res/hashnode/image/upload/v1766152181735/adc30203-f4ce-4228-9d52-4edc15c62731.png align="center")

![App Screenshot 4 - État de chargement](https://cdn.hashnode.com/res/hashnode/image/upload/v1766157240628/e31a49db-4143-4e70-9d69-e63a81e722d0.png align="center")

![App Screenshot 1 - Affichage réussi de la carte de Noël](https://cdn.hashnode.com/res/hashnode/image/upload/v1766157250344/64938d48-e73f-405f-8050-c20dfc6ecd6a.png align="center")

## Dernières réflexions

Ce projet démontre comment vous pouvez tirer parti de GenUI dans sa forme la plus pratique : non pas simplement comme une démo technique, mais comme un paradigme Flutter fonctionnel qui comble le fossé entre le code statique et l'intention de l'utilisateur.

En déplaçant la responsabilité de l'orchestration de la mise en page du développeur vers un agent intelligent, nous débloquons un niveau de personnalisation qui n'était auparavant pas possible dans le développement mobile.

Une fois que vous maîtrisez la boucle de conversation (comment l'IA réfléchit), les surfaces (comment l'IA dessine) et les limites du catalogue (ce que l'IA est autorisée à utiliser), GenUI devient un ajout transformateur à votre boîte à outils Flutter. Il vous permet de construire des interfaces qui ne sont pas seulement "réactives" aux tailles d'écran, mais "réactives" aux besoins humains.

En tant qu'adoptant précoce, vous êtes à la pointe des interfaces utilisateur générées par l'IA. Vos explorations et vos commentaires aideront à façonner l'avenir de la construction d'applications à l'ère de l'intelligence générative. Vous pouvez trouver le [projet complet sur Github ici](https://github.com/Atuoha/christmas-card-genui-flutter).

## Références

1.  Équipe Flutter. *GenUI: Build AI-powered user interfaces in Flutter*. Dépôt GitHub.  
    Disponible sur : [https://github.com/flutter/genui/](https://github.com/flutter/genui/)
    
2.  Documentation Flutter. *Getting started with GenUI*.  
    Disponible sur : [https://docs.flutter.dev/ai/genui/get-started](https://docs.flutter.dev/ai/genui/get-started)
    
3.  Écosystème Dart & Flutter. *Package genui*. pub.dev.  
    Disponible sur : [https://pub.dev/packages/genui](https://pub.dev/packages/genui)
    
4.  Écosystème Dart & Flutter. *Package genui\_firebase\_ai*. pub.dev.  
    Disponible sur : [https://pub.dev/packages/genui\_firebase\_ai](https://pub.dev/packages/genui_firebase_ai)