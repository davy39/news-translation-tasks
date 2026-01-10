---
title: 'Comment créer un chatbot médical avec Flutter et Gemini : Un guide pour débutants'
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-06-13T17:37:31.507Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-medical-chatbot-with-flutter-and-gemini
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1749830721631/4675d1f6-ad64-46a3-86e1-ce8a2c84323f.png
tags:
- name: Flutter
  slug: flutter
- name: flutter-aware
  slug: flutter-aware
- name: 'AISprint '
  slug: aisprint
- name: AI
  slug: ai
- name: chatbot
  slug: chatbot
seo_title: 'Comment créer un chatbot médical avec Flutter et Gemini : Un guide pour
  débutants'
seo_desc: 'In today''s digital age, the demand for accessible and accurate health
  information is higher than ever. Leveraging the power of artificial intelligence,
  we can create intelligent chatbots that provide reliable health-related guidance.

  This beginner''s ...'
---

À l'ère numérique d'aujourd'hui, la demande d'informations de santé accessibles et précises est plus élevée que jamais. En exploitant la puissance de l'intelligence artificielle, nous pouvons créer des chatbots intelligents qui fournissent des conseils fiables liés à la santé.

Ce guide pour débutants vous guidera à travers la création d'un chatbot médical puissant et spécialisé en utilisant Flutter et l'API Gemini de Google. Le chatbot sera capable de recevoir des entrées de diverses modalités comme le texte, l'audio, la caméra, les fichiers et une galerie, et il sera strictement limité à répondre aux questions liées à la santé.

### Table des matières :

* [Le pouvoir de l'IA dans les soins de santé](#heading-le-pouvoir-de-lia-dans-les-soins-de-sante)
    
* [Comment configurer votre environnement de développement](#heading-comment-configurer-votre-environnement-de-developpement)
    
* [Structure du projet](#heading-structure-du-projet)
    
* [Implémentation et explication du code](#heading-implementation-et-explication-du-code)
    
* [Considérations importantes et améliorations futures](#heading-considerations-importantes-et-ameliorations-futures)
    
* [Captures d'écran et projet terminé](#heading-captures-decran)
    
* [Conclusion](#heading-conclusion)
    

## Le pouvoir de l'IA dans les soins de santé

Les chatbots alimentés par l'IA transforment diverses industries, et les soins de santé ne font pas exception. Ils offrent un moyen évolutif et efficace de diffuser des informations, de répondre aux questions fréquemment posées et même de fournir des évaluations initiales. En se concentrant sur les requêtes liées à la santé, notre chatbot agira en tant qu'assistant spécialisé, fournissant des informations concises et précises aux utilisateurs.

### Technologies principales

Nous construirons notre chatbot médical en utilisant les technologies clés suivantes :

* **Flutter :** La boîte à outils UI de Google pour construire des applications compilées nativement pour mobile, web et bureau à partir d'une seule base de code.**<sup>1</sup>** Son ensemble riche de widgets et son UI expressive en font un outil idéal pour créer des interfaces de chat engageantes.
    
* **API Google Gemini :** Le modèle d'IA le plus capable et flexible de Google. Gemini est multimodal, ce qui signifie qu'il peut traiter et comprendre différents types d'informations, y compris le texte, les images, l'audio et la vidéo. Cette capacité est cruciale pour que notre chatbot gère les diverses entrées des utilisateurs.
    
* `flutter_ai_toolkit` : Un package Flutter qui fournit un ensemble de widgets liés aux chats IA et une API abstraite de fournisseur LLM, simplifiant l'intégration des modèles IA dans votre application Flutter. Il offre un support prêt à l'emploi pour Gemini.
    
* `google_generative_ai` : Le package Dart officiel pour interagir avec les modèles d'IA générative de Google (Gemini).
    

## Comment configurer votre environnement de développement

Avant de plonger dans le code, assurez-vous d'avoir Flutter installé et configuré sur votre système. Si ce n'est pas le cas, suivez le [guide d'installation officiel de Flutter ici](https://flutter.dev/docs/get-started/install).

### Obtenez votre clé API Gemini

Pour interagir avec l'API Gemini, vous avez besoin d'une clé API. Cette clé authentifie votre application et lui permet d'envoyer des requêtes au modèle Gemini.

Voici comment obtenir votre clé API Gemini :

1. **Allez sur Google AI Studio :** Ouvrez votre navigateur web et rendez-vous sur [https://aistudio.google.com/](https://aistudio.google.com/).
    
2. **Connectez-vous avec votre compte Google :** Si vous n'êtes pas déjà connecté, vous serez invité à vous connecter avec votre compte Google.
    
3. **Cliquez sur "Obtenir une clé API dans Google AI Studio" :** Sur la page d'accueil de Google AI Studio, vous verrez un bouton prominent avec ce texte. Cliquez dessus.
    
4. **Passez en revue et acceptez les conditions de service :** Une fenêtre contextuelle apparaîtra vous demandant de consentir aux Conditions de service des API Google et aux Conditions supplémentaires de service de l'API Gemini. Lisez-les attentivement, cochez les cases nécessaires et cliquez sur "Continuer".
    
5. **Créez votre clé API :** Vous aurez maintenant la possibilité de "Créer une clé API dans un nouveau projet" ou "Créer une clé API dans un projet existant". Choisissez celle qui convient à vos besoins. Votre clé API sera générée automatiquement.
    
6. **Copiez votre clé API :** **Il est crucial de copier cette clé API immédiatement et de la stocker en sécurité.** Elle ne sera plus affichée. **Ne codez pas en dur votre clé API directement dans votre code de production, surtout pour les applications côté client.** À des fins de développement, nous l'utiliserons directement dans notre `MedicalChatScreen` pour simplifier, mais pour une application réelle, envisagez d'utiliser des variables d'environnement ou un backend sécurisé pour gérer votre clé API.
    

### Ajouter des dépendances (`pubspec.yaml`)

Ouvrez votre fichier `pubspec.yaml` (situé à la racine de votre projet Flutter) et ajoutez les dépendances suivantes sous `dependencies` :

```bash
dependencies:
  flutter:
    sdk: flutter
  flutter_ai_toolkit: ^0.6.8
  google_generative_ai: ^0.4.6
```

Après avoir ajouté celles-ci, exécutez `flutter pub get` dans votre terminal pour récupérer les packages.

## Structure du projet

Notre projet aura une structure simple :

* `lib/main.dart` : Le point d'entrée de notre application Flutter.
    
* `lib/screens/chat.dart` : Contient l'interface de chat principale pour notre chatbot médical.
    

## Implémentation et explication du code

Décortiquons le code fourni et comprenons chaque partie.

#### `lib/main.dart`

```dart
import 'package:ai_demo/screens/chat.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Medical ChatBot',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      home: const MedicalChatScreen(),
    );
  }
}
```

Voici ce qui se passe dans ce code :

* `import 'package:ai_demo/screens/chat.dart';` : Cette ligne importe le fichier `chat.dart` du dossier `screens`. C'est là que notre widget `MedicalChatScreen` est défini.
    
* `import 'package:flutter/material.dart';` : Cela importe les widgets fondamentaux de Flutter Material Design, essentiels pour construire l'UI.
    
* `void main() { runApp(const MyApp()); }` : C'est le point d'entrée de toute application Flutter. `runApp()` prend un widget comme argument et en fait la racine de l'arbre de widgets.
    
* `class MyApp extends StatelessWidget` : `MyApp` est le widget racine de notre application. `StatelessWidget` signifie que ses propriétés ne changent pas au fil du temps.
    
* `Widget build(BuildContext context)` : Cette méthode est l'endroit où l'UI du widget `MyApp` est construite.
    
* `MaterialApp` : Ce widget fournit la structure visuelle de base de Material Design pour une application Flutter.
    
    * `title: 'Medical ChatBot'` : Définit le titre de l'application, qui peut être affiché dans le sélecteur de tâches de l'appareil ou l'onglet du navigateur.
        
    * `theme: ThemeData(...)` : Définit le thème visuel de l'application.
        
        * `colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple)` : Génère un schéma de couleurs basé sur une couleur "seed" primaire (`Colors.deepPurple`), assurant un look cohérent et harmonieux dans toute l'application.
            
    * `home: const MedicalChatScreen()` : Définit l'écran initial de l'application sur notre widget `MedicalChatScreen`.
        

#### `lib/screens/chat.dart`

```dart
import 'package:flutter/material.dart';
import 'package:flutter_ai_toolkit/flutter_ai_toolkit.dart';
import 'package:google_generative_ai/google_generative_ai.dart';

class MedicalChatScreen extends StatefulWidget {
  const MedicalChatScreen({super.key});

  @override
  State<MedicalChatScreen> createState() => _MedicalChatScreenState();
}

class _MedicalChatScreenState extends State<MedicalChatScreen> {
  String apiKey = ""; // IMPORTANT : Remplacez par votre véritable clé API Gemini

  @override
  void initState() {
    super.initState();
    // Il est bon de charger la clé API à partir d'une source sécurisée
    // plutôt que de la coder en dur, surtout pour les applications de production.
    // Pour cette démonstration, nous allons garder cela simple.
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.white,
        automaticallyImplyLeading: false,
        title: const Text("Medical ChatBot"),
      ),
      body: LlmChatView(
        suggestions: const [
          "J'ai des vertiges ces derniers temps. Que faire ?",
          "Comment savoir si je dois consulter un médecin ?",
          "Que dois-je manger pour renforcer mon immunité ?"
        ],
        style: LlmChatViewStyle(
          backgroundColor: Colors.white,
          chatInputStyle: ChatInputStyle(
            hintText: "Entrez votre message",
            decoration: const BoxDecoration().copyWith(
              borderRadius: BorderRadius.circular(50),
            ),
          ),
        ),
        provider: GeminiProvider(
          model: GenerativeModel(
            model: "gemini-2.0-flash",
            apiKey: apiKey,
            systemInstruction: Content.system(
              "Vous êtes un assistant médical professionnel. Répondez uniquement aux questions liées à la santé et à la médecine et faites-les concises et directes sans trop d'explications."
                  "Si une question n'est pas liée à la santé ou à la médecine, informez poliment l'utilisateur que vous ne pouvez répondre qu'aux requêtes médicales.",
            ),
          ),
        ),
        welcomeMessage:
        "Bonjour\ud83d\udc4b Je suis là pour vous aider avec vos questions médicales. Dites-moi comment je peux vous aider."
      ),
    );
  }
}
```

Ce qui se passe dans `chat.dart` :

* `import 'package:flutter/material.dart';` : Importe les widgets Material Design.
    
* `import 'package:flutter_ai_toolkit/flutter_ai_toolkit.dart';` : Importe le package `flutter_ai_toolkit`, qui fournit `LlmChatView` et `GeminiProvider`.
    
* `import 'package:google_generative_ai/google_generative_ai.dart';` : Importe le package `google_generative_ai`, qui nous permet d'interagir avec le modèle Gemini.
    
* `class MedicalChatScreen extends StatefulWidget` : Notre écran de chat est un `StatefulWidget` car sa `apiKey` et potentiellement d'autres états liés au chat peuvent changer.
    
* `_MedicalChatScreenState createState() => _MedicalChatScreenState();` : Crée l'état mutable pour ce widget.
    
* `String apiKey = "";` : **C'est ici que vous devez coller votre clé API Gemini.** Remplacez `""` par la clé réelle que vous avez obtenue de Google AI Studio. Par exemple : `String apiKey = "VOTRE_CLE_API_GEMINI_ICI";`.
    
    * **Note de sécurité :** Comme mentionné précédemment, le codage en dur des clés API n'est pas recommandé pour les applications de production. Envisagez d'utiliser des variables d'environnement, un service de gestion des secrets (comme Firebase Remote Config ou Google Cloud Secret Manager), ou un serveur backend pour gérer les requêtes API de manière sécurisée.
        
* `initState()` : Cette méthode est appelée une fois lorsque le widget est inséré dans l'arbre de widgets. C'est un bon endroit pour l'installation initiale. Dans ce cas, elle est vide mais sert de placeur pour une initialisation potentielle future comme le chargement sécurisé de la clé API.
    
* `Scaffold` : Implémente la structure de mise en page visuelle de base de Material Design.
    
    * `appBar` : Affiche une barre d'application supérieure.
        
        * `backgroundColor: Colors.white` : Définit la couleur de fond de la barre d'application en blanc.
            
        * `automaticallyImplyLeading: false` : Empêche Flutter d'ajouter automatiquement un bouton de retour si cet écran est poussé sur une pile de navigation.
            
        * `title: const Text("Medical ChatBot")` : Définit le texte du titre de la barre d'application.
            
* `body: LlmChatView(...)` : C'est le widget principal de `flutter_ai_toolkit` qui fournit l'UI de chat et gère l'interaction avec le LLM.
    
    * `suggestions: const [...]` : Fournit une liste de suggestions initiales à l'utilisateur lorsque le chat est vide. Ces suggestions guident l'utilisateur sur les types de questions auxquelles le chatbot peut répondre.
        
    * `style: LlmChatViewStyle(...)` : Personnalise l'apparence de la vue de chat.
        
        * `backgroundColor: Colors.white` : Définit la couleur de fond de la zone de chat.
            
        * `chatInputStyle: ChatInputStyle(...)` : Style le champ de saisie de texte.
            
            * `hintText: "Entrez votre message"` : Texte de l'espace réservé dans le champ de saisie.
                
            * `decoration: const BoxDecoration().copyWith(borderRadius: BorderRadius.circular(50))` : Style le champ de saisie avec des coins arrondis.
                
    * `provider: GeminiProvider(...)` : C'est ici que nous configurons notre modèle Gemini comme fournisseur d'IA pour `LlmChatView`.
        
        * `model: GenerativeModel(...)` : Crée une instance du modèle Gemini.
            
            * `model: "gemini-2.0-flash"` : Spécifie le modèle Gemini particulier à utiliser. "gemini-2.0-flash" est un modèle léger et rapide adapté à de nombreuses applications. D'autres modèles comme "gemini-pro" sont également disponibles, offrant différentes capacités et coûts.
                
            * `apiKey: apiKey` : Transmet votre clé API Gemini obtenue au modèle.
                
            * `systemInstruction: Content.system(...)` : **Cela est crucial pour définir la persona du chatbot et ses limitations.** C'est un message système envoyé au modèle Gemini au début de la conversation (et potentiellement à chaque tour, selon les détails d'implémentation de `flutter_ai_toolkit` et `google_generative_ai`).
                
                * `"Vous êtes un assistant médical professionnel. Répondez uniquement aux questions liées à la santé et à la médecine et faites-les concises et directes sans trop d'explications."` : C'est l'instruction principale. Elle indique à Gemini d'agir en tant qu'assistant médical et d'être précis dans ses réponses liées à la santé.
                    
                * `"Si une question n'est pas liée à la santé ou à la médecine, informez poliment l'utilisateur que vous ne pouvez répondre qu'aux requêtes médicales."` : Cette instruction garantit que le chatbot reste dans son champ défini et ne fournit pas de réponses hallucinées ou non pertinentes aux questions non médicales, ce qui est vital pour un bot de santé spécialisé.
                    
    * `welcomeMessage: "Bonjour\ud83d\udc4b Je suis là pour vous aider avec vos questions médicales. Dites-moi comment je peux vous aider."` : Un message convivial affiché à l'utilisateur lorsqu'il ouvre pour la première fois l'écran de chat, établissant le contexte de la conversation.
        

### Comment gérer les entrées multimodales

Le package `flutter_ai_toolkit`, lorsqu'il est utilisé avec `GeminiProvider`, supporte intrinsèquement les entrées multimodales. Le `LlmChatView` fournit automatiquement des éléments d'UI pour :

* **Saisie de texte :** Le champ de texte standard pour taper des messages.
    
* **Saisie audio :** Une icône de microphone sera généralement présente, permettant aux utilisateurs d'enregistrer des messages vocaux qui sont ensuite transcrits et envoyés à Gemini.
    
* **Saisie de caméra :** Une icône de caméra permettra aux utilisateurs de prendre une photo et de l'envoyer au chatbot. Gemini peut ensuite traiter l'image et fournir une réponse.
    
* **Saisie de fichier :** Une icône de pièce jointe (souvent une épingle) permettra aux utilisateurs de sélectionner des fichiers (comme des documents ou des images) depuis leur appareil pour les envoyer au chatbot.
    
* **Saisie de galerie :** Similaire à la saisie de fichier, mais spécifiquement pour sélectionner des images ou des vidéos depuis la galerie photo de l'appareil.
    

Le `flutter_ai_toolkit` abstrait les complexités de la gestion de ces différents types de saisie, les convertissant dans un format que le package `google_generative_ai` et ensuite le modèle Gemini peuvent comprendre et traiter. Par exemple, les images sont envoyées en tant que `ImagePart` dans l'objet `Content`, et l'audio peut être transcrit en texte avant d'être envoyé, ou envoyé en tant que `AudioPart` si le modèle supporte la saisie audio directe.

La `systemInstruction` que nous avons définie pour le `GenerativeModel` est cruciale ici. Bien que le `flutter_ai_toolkit` gère la saisie, la capacité de Gemini à comprendre diverses modalités dans le contexte des questions de santé dépend de sa formation et de nos instructions claires.

Par exemple, si un utilisateur télécharge une image d'une éruption cutanée, l'instruction système aide à guider Gemini pour l'interpréter d'un point de vue médical (bien qu'il soit important de se rappeler qu'un chatbot IA n'est pas un substitut au diagnostic médical professionnel).

### Comment exécuter votre chatbot

1. **Remplacez** `apiKey` : Dans `lib/screens/chat.dart`, remplacez `""` par votre véritable clé API Gemini.
    
2. **Exécutez l'application :** Dans votre terminal, naviguez jusqu'au répertoire racine de votre projet et exécutez : **Bash**
    
    ```bash
    flutter run
    ```
    

Cela lancera l'application sur un appareil connecté ou un émulateur. Vous devriez voir l'application "Medical ChatBot" avec le message de bienvenue et les suggestions de prompts. Essayez de taper quelques questions liées à la santé, et expérimentez également avec les options d'entrée multimodales (microphone, caméra, icône de pièce jointe) si votre appareil/émulateur les supporte.

## Considérations importantes et améliorations futures

* **Sécurité de la clé API :** Juste pour réitérer l'importance de ne pas coder en dur les clés API en production. Pour une application déployée, envisagez d'utiliser des variables d'environnement, des services backend, ou les configurations de build de Flutter pour injecter la clé API de manière sécurisée.
    
* **Gestion des erreurs :** Le code actuel ne montre pas explicitement la gestion des erreurs pour les appels API. Dans une application réelle, vous voudriez gérer les erreurs réseau, les clés API invalides, ou les limites de taux de manière élégante. Les packages `flutter_ai_toolkit` et `google_generative_ai` fournissent des mécanismes pour cela.
    
* **Expérience utilisateur (UX) :**
    
    * **Indicateurs de chargement :** Affichez un indicateur de chargement pendant que l'IA génère une réponse.
        
    * **Validation de la saisie :** Pour certaines saisies (par exemple, les types de fichiers), vous pourriez vouloir ajouter une validation côté client.
        
    * **Effacement/historique :** Implémentez des fonctionnalités pour effacer l'historique de chat ou sauvegarder les conversations passées.
        
* **Avertissement médical :** Crucialement, tout chatbot médical devrait inclure un avertissement prominent indiquant qu'il ne remplace pas les conseils médicaux professionnels, le diagnostic ou le traitement. Il devrait toujours conseiller aux utilisateurs de consulter un professionnel de santé qualifié pour toute préoccupation de santé.
    
* **Confidentialité et sécurité des données :** Lorsque l'on traite des informations liées à la santé, la confidentialité des données est primordiale. Assurez-vous que votre application respecte les réglementations pertinentes (par exemple, HIPAA aux États-Unis, RGPD en Europe) et que les données des utilisateurs sont traitées de manière sécurisée. L'API Gemini a ses propres politiques de données que vous devriez examiner.
    
* **Instructions système avancées :** Pour un chatbot médical plus sophistiqué, vous pourriez étendre la `systemInstruction` pour inclure des domaines spécifiques de connaissances médicales, des formats de réponse préférés (par exemple, toujours lister des points à puces pour les symptômes), ou même diriger l'IA à poser des questions de clarification.
    
* **Utilisation d'outils/appel de fonctions :** Gemini supporte l'utilisation d'outils (appel de fonctions), permettant à l'IA d'interagir avec des services externes. Pour un bot de santé, cela pourrait signifier :
    
    * Rechercher des informations sur les médicaments dans une base de données.
        
    * Trouver des cliniques ou des pharmacies à proximité.
        
    * Accéder à des recherches médicales à jour.
        
    * Cela nécessiterait une configuration plus complexe avec des fonctions backend que l'IA peut appeler.
        
* **Reconnaissance vocale et synthèse vocale (STT et TTS) :** Bien que `flutter_ai_toolkit` gère la saisie audio, vous pourriez vouloir un contrôle plus fin sur les services STT et TTS pour une meilleure interaction vocale.
    
* **Traitement d'image et imagerie médicale :** Pour des applications médicales vraiment avancées, vous pourriez intégrer des bibliothèques spécialisées de traitement d'image pour analyser des images médicales (par exemple, des radiographies, des IRM), mais cela est un domaine complexe nécessitant des connaissances expertes et une conformité réglementaire. Notre configuration actuelle permet à Gemini d'interpréter des images, mais elle repose sur les capacités de vision générale de Gemini.
    

## Captures d'écran

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1749131323671/5768237e-2f4b-4c6b-aae6-23486dc8bb46.png align="center")

Vous pouvez consulter le projet complet ici : [https://github.com/Atuoha/ai\_medical\_assistant](https://github.com/Atuoha/ai_medical_assistant)

## Conclusion

Vous avez maintenant réussi à construire un chatbot médical de base en utilisant Flutter et Google Gemini ! Cette application démontre comment intégrer un modèle d'IA puissant avec une interface utilisateur multimodale, tout en appliquant des contraintes comportementales spécifiques (questions uniquement liées à la santé).

En étendant cette base avec une gestion robuste des erreurs, une UX améliorée et potentiellement des fonctionnalités avancées d'IA comme l'utilisation d'outils, vous pouvez créer des applications de soins de santé encore plus sophistiquées et précieuses.

N'oubliez pas de toujours privilégier la sécurité des utilisateurs et la confidentialité des données lors du développement de solutions d'IA dans le domaine médical.

### **Packages Flutter et Dart :**

* `flutter_ai_toolkit` :
    
    * Page Pub.dev : [https://pub.dev/packages/flutter\_ai\_toolkit](https://pub.dev/packages/flutter_ai_toolkit)
        
    * Documentation Flutter (AI Toolkit) : [https://docs.flutter.dev/ai-toolkit](https://docs.flutter.dev/ai-toolkit)
        
* `google_generative_ai` :
    
    * Page Pub.dev : [https://pub.dev/packages/google\_generative\_ai](https://www.google.com/search?q=https://pub.dev/packages/google_generative_ai)
        

**API Google Gemini et AI Studio :**

* Google AI Studio : [https://aistudio.google.com/](https://aistudio.google.com/)
    
* Obtenir une clé API Gemini (Google AI pour les développeurs) : [https://ai.google.dev/gemini-api/docs/api-key](https://ai.google.dev/gemini-api/docs/api-key)
    
* Documentation de l'API Gemini (Google AI pour les développeurs) : [https://ai.google.dev/api](https://ai.google.dev/api) (Documentation générale de l'API)
    

**Documentation Flutter :**

* Site officiel de Flutter (Guide d'installation) : [https://flutter.dev/docs/get-started/install](https://flutter.dev/docs/get-started/install)
    

**Concepts généraux (pour lecture supplémentaire) :**

* **Material Design :** [https://m3.material.io/](https://m3.material.io/) (Pour comprendre les principes de l'UI de Flutter)
    
* **Grandes modèles de langage (LLM) :** Un sujet large, mais comprendre les bases du fonctionnement des LLM améliorera la compréhension de la `systemInstruction` et du comportement du modèle.
    
* **IA multimodale :** La recherche sur l'IA multimodale fournit un contexte sur la raison pour laquelle Gemini peut gérer divers types de saisie (texte, image, audio, etc.).
    
* **Meilleures pratiques de sécurité des clés API :** Pour les applications de production, il est crucial de comprendre la gestion sécurisée des clés API (par exemple, variables d'environnement, services de gestion des secrets). Un bon point de départ serait les meilleures pratiques générales de sécurité pour les clés API.