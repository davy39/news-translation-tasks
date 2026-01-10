---
title: Comment utiliser le Model Context Protocol (MCP) avec Flutter et Dart
subtitle: ''
author: Atuoha Anthony
co_authors: []
series: null
date: '2025-10-24T19:46:36.439Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-model-context-protocol-mcp-with-flutter-and-dart
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761335181944/18a2fe98-2d77-490c-8b80-5f254c3f9c99.png
tags:
- name: Flutter
  slug: flutter
- name: Dart
  slug: dart
- name: mcp server
  slug: mcp-server
- name: flutter-aware
  slug: flutter-aware
seo_title: Comment utiliser le Model Context Protocol (MCP) avec Flutter et Dart
seo_desc: Software development is moving fast toward AI-assisted workflows and smarter
  tooling. Whether it’s your IDE completing code, an AI assistant analyzing your project,
  or automated testing pipelines, all these tools need a standardized way to communicat...
---

Le développement logiciel évolue rapidement vers des flux de travail assistés par l'IA et des outils plus intelligents. Qu'il s'agisse de votre IDE complétant le code, d'un assistant IA analysant votre projet ou de pipelines de tests automatisés, tous ces outils ont besoin d'un moyen standardisé pour communiquer. C'est là qu'intervient le **Model Context Protocol (MCP)**.

Si vous avez entendu parler du MCP et que vous vous demandez ce que cela signifie pour vous en tant que développeur Dart ou Flutter, ce guide est fait pour vous. Il explique ce qu'est le MCP et comment il se connecte à Dart via le paquet officiel `dart_mcp`. Vous apprendrez également comment commencer à construire ou à intégrer vous-même des outils basés sur le MCP, afin que l'IA puisse réellement comprendre et agir sur votre projet Flutter/Dart, et pas seulement répondre à des questions sur du code copié-collé.

À la fin de ce guide, vous comprendrez :

* Ce qu'est le Model Context Protocol (MCP) et pourquoi il est important.
    
* Comment le MCP permet à l'IA et aux outils de développement de communiquer de manière structurée et cohérente.
    
* Comment Dart intègre le MCP via le paquet `dart_mcp` et les outils serveur.
    
* Des exemples pratiques sur la façon de construire un serveur et un client MCP en Dart.
    
* Comment débuter, y compris les prérequis et les ressources d'apprentissage.
    

### Table des matières :

1. [Prérequis](#heading-prerequis)
    
2. [Qu'est-ce que le MCP (Model Context Protocol) ?](#heading-quest-ce-que-le-mcp-model-context-protocol)
    
3. [Pourquoi le MCP est important pour les développeurs Dart et Flutter](#heading-pourquoi-le-mcp-est-important-pour-les-developpeurs-dart-et-flutter)
    
4. [Le MCP dans l'écosystème Dart](#heading-le-mcp-dans-lecosysteme-dart)
    
    * [Qu'est-ce que le paquet dart\_mcp ?](#heading-quest-ce-que-le-paquet-dartmcp)
        
5. [Cas d'utilisation réels](#heading-cas-dutilisation-reels)
    
6. [Comment le MCP fonctionne réellement](#heading-comment-le-mcp-fonctionne-reellement)
    
7. [Guide de démarrage, étape par étape](#heading-guide-de-demarrage-etape-par-etape)
    
    * [1) Prérequis](#heading-1-prerequis)
        
    * [2) Démarrer le serveur MCP Dart & Flutter localement](#heading-2-demarrer-le-serveur-mcp-dart-amp-flutter-localement)
        
    * [3) Configurer un client MCP](#heading-3-configurer-un-client-mcp)
        
    * [4) Essayer une requête simple depuis votre assistant IDE](#heading-4-essayer-une-requete-simple-depuis-votre-assistant-ide)
        
    * [5) Créer une capacité personnalisée (optionnel)](#heading-5-creer-une-capacite-personnalisee-optionnel)
        
8. [Exemple pratique](#heading-exemple-pratique-corriger-un-debordement-de-mise-en-page)
    
    * [Explication étape par étape](#heading-explication-etape-par-etape)
        
9. [Comment construire un serveur MCP simple en Dart](#heading-comment-construire-un-serveur-mcp-simple-en-dart)
    
    * [Étape 1 : Ajouter la dépendance](#heading-etape-1-ajouter-la-dependance)
        
    * [Étape 2 : Créer le serveur](#heading-etape-2-creer-le-serveur)
        
10. [Exemple : Création d'un client MCP](#heading-exemple-creation-dun-client-mcp)
    
11. [MCP vs Serveurs HTTP personnalisés](#heading-mcp-vs-serveurs-http-personnalises)
    
12. [Bonnes pratiques, sécurité et permissions](#heading-bonnes-pratiques-securite-et-permissions)
    
13. [Débuter en tant que débutant](#heading-debuter-en-tant-que-debutant)
    
14. [Aller au-delà du niveau débutant](#heading-aller-au-dela-du-niveau-debutant)
    
15. [Conclusion](#heading-conclusion)
    
16. [Références](#heading-references)
    

## Prérequis

Pour suivre ce guide, vous devez disposer des éléments suivants :

1. SDK Dart 3.9 ou ultérieur / Flutter 3.35 beta ou ultérieur installé sur votre machine.
    
2. Compréhension de base de la programmation asynchrone en Dart (utilisation de `async` / `await`).
    
3. Familiarité avec les flux d'E/S standard (`stdin`, `stdout`) car le client MCP communique par leur biais.
    
4. Accès à un serveur compatible MCP (par exemple, Dart MCP Server ou une implémentation personnalisée).
    
5. Dépendances Pub correctement configurées avec `dart_mcp` ajouté à votre `pubspec.yaml`.
    

## Qu'est-ce que le MCP (Model Context Protocol) ?

Le MCP (Model Context Protocol) est un standard qui permet aux modèles d'IA (agents) de communiquer avec les outils de développement, les éditeurs et les projets de manière structurée et autorisée. Au lieu de demander à une IA de raisonner sur du code que vous collez dans un chat, le MCP permet à l'IA d'appeler des capacités spécifiques (outils) que votre projet expose, par exemple, « exécuter l'analyseur », « obtenir le contenu du fichier », « exécuter les tests » ou « rechercher sur pub.dev ». Cela transforme l'IA en un collaborateur contextuel capable d'inspecter, d'exécuter et même de modifier votre base de code de manière contrôlée.

En termes plus simples, c'est un protocole qui aide les **agents d'IA et les outils à se parler**. Il élimine le besoin d'intégrations ponctuelles et standardise la manière dont les capacités telles que « exécuter cet outil », « récupérer ce fichier » ou « obtenir ces logs » sont décrites et utilisées.

## Pourquoi le MCP est important pour les développeurs Dart et Flutter

Pour les développeurs travaillant avec Dart et Flutter, le MCP ouvre de nouvelles possibilités :

1. Vous pouvez construire vos propres outils pilotés par l'IA (par exemple, des analyseurs, des processeurs de fichiers ou des assistants de revue de code) qui s'intègrent aux éditeurs et assistants via le MCP.
    
2. Vous pouvez étendre votre flux de travail de développement, en laissant les assistants IA interagir directement avec vos projets Dart locaux, exécuter des commandes, analyser des fichiers ou déclencher des builds Flutter.
    
3. Vous pouvez automatiser des tâches au sein de votre environnement de développement local (comme le linting, l'analyse de dépendances ou la génération de rapports) sans avoir besoin d'un serveur API dédié.
    

Il ne s'agit pas seulement d'IA, mais aussi d'automatisation standardisée dans votre chaîne d'outils.

## Le MCP dans l'écosystème Dart

L'équipe Dart a commencé à adopter le MCP directement via un paquet expérimental officiel appelé `dart_mcp`. Ce paquet donne aux développeurs Dart les outils nécessaires pour créer à la fois des serveurs MCP et des clients MCP, permettant une communication bidirectionnelle entre vos outils Dart et les assistants IA ou les IDE.

### Qu'est-ce que le paquet `dart_mcp` ?

Le paquet [`dart_mcp`](https://pub.dev/packages/dart_mcp) fournit des API pour implémenter des serveurs et des clients MCP en utilisant Dart. Il est publié par [`labs.dart.dev`](https://pub.dev/publishers/labs.dart.dev/packages), ce qui signifie qu'il s'agit d'une expérience officielle de Dart Labs, en évolution active et soutenue par l'équipe Dart.

**Caractéristiques clés :**

1. Construire des serveurs MCP qui exposent des outils et des capacités.
    
2. Construire des clients MCP qui se connectent à ces serveurs.
    
3. Support du transport STDIO, permettant une communication locale à faible latence.
    
4. Support des capacités de Prompts, Resources et Tools.
    
5. Structure alignée sur le protocole pour l'initialisation, la validation de schéma et la gestion des requêtes/réponses.
    

**Limitations (à partir de la version 0.3.3) :**

1. Les transports HTTP et streamables sont encore expérimentaux.
    
2. L'autorisation et le traitement par lots ne sont pas encore entièrement pris en charge.
    
3. L'API du paquet peut changer à mesure qu'elle mûrit.
    

## Cas d'utilisation réels

Voici quelques situations où le MCP passe de « gadget » à véritablement utile :

1. **Corriger un bug d'interface utilisateur au runtime.** L'IA inspecte les logs d'exécution et l'arbre de widgets, puis suggère et applique un correctif pour un débordement `RenderFlex`.
    
2. **Ajouter un paquet et générer un exemple d'utilisation.** Vous pouvez demander à l'assistant d'ajouter des graphiques, et il recherche sur `pub.dev`, met à jour le `pubspec.yaml`, exécute `dart pub get` et génère l'utilisation de base du widget.
    
3. **Revue de code automatisée.** Sur chaque PR, un agent IA exécute `dart analyze` et `flutter test`, et commente avec des suggestions d'amélioration.
    
4. **Apprentissage et mentorat.** L'outil peut inspecter le projet d'un apprenant puis suggérer des patterns Flutter idiomatiques et ajouter des tests unitaires.
    
5. **Outils de développement personnalisés.** Il peut construire des outils internes : par exemple, « lister toutes les routes et générer un test de navigation », exposé comme une capacité et appelable par l'assistant.
    

## Comment le MCP fonctionne réellement

Avant de plonger dans le flux, il est important de comprendre ce qui se passe en coulisses. Le MCP définit comment un assistant IA communique de manière sécurisée avec votre environnement local. Il permet des interactions structurées et basées sur des permissions entre votre IDE, votre assistant IA et vos outils de développement, sans donner au modèle un accès illimité.

Regardons un exemple :

```dart
Assistant IA (LLM)  ⇄  Client MCP (dans l'IDE/agent)  ⇄  Serveur MCP Dart/Flutter (dart mcp-server)  ⇄  Outils & Base de code
```

* Le serveur MCP s'exécute dans votre environnement et expose des outils (capacités).
    
* Le client MCP (par exemple, Gemini CLI, GitHub Copilot, Firebase Studio, Cursor) communique avec le serveur.
    
* L'IA émet des appels d'outils structurés. Le serveur s'exécute et renvoie des résultats structurés.
    

Vous gardez le contrôle, et les outils sont explicites et autorisés (au lieu d'avoir un accès éphémère de type « donnez tout au modèle »).

## Guide de démarrage, étape par étape

Suivez les instructions ci-dessous pour passer de zéro à un projet fonctionnel compatible MCP.

### 1) Prérequis

Tout d'abord, vous devrez installer le SDK Dart 3.9+ et Flutter (si vous souhaitez expérimenter l'introspection au runtime de Flutter). Le serveur MCP Dart nécessite Dart 3.9 ou ultérieur.

Vous pouvez utiliser VS Code, IntelliJ ou un autre éditeur. De nombreux clients/plugins s'intégreront au MCP.

### 2) Démarrer le serveur MCP Dart & Flutter localement

Vous pouvez exécuter le serveur MCP Dart avec la commande suivante :

```bash
dart mcp-server
```

Cette commande lance le serveur MCP, le composant auquel les outils clients (comme les IDE ou les assistants IA) se connectent pour communiquer avec votre environnement local.

### 3) Configurer un client MCP

Vous pouvez configurer des clients comme Gemini CLI, Firebase Studio, GitHub Copilot et Cursor pour parler à votre serveur. Voici un exemple pour le Gemini CLI (à ajouter à `~/.gemini/settings.json` ou au fichier projet `.gemini/settings.json`) :

```json
{
  "mcpServers": {
    "dart": {
      "command": "dart",
      "args": ["mcp-server"]
    }
  }
}
```

Cela indique au client de démarrer le processus `dart mcp-server` et de l'utiliser comme fournisseur d'outils.

### 4) Essayer une requête simple depuis votre assistant IDE

Ouvrez votre projet dans VS Code (avec un assistant IA activé). Demandez quelque chose de pratique, comme :

> « Trouve les fonctions non testées et crée un squelette de fichier de test pour elles. »

L'assistant utilisera les outils MCP pour inspecter le code, exécuter l'analyse et pourra générer l'échafaudage de test que vous pourrez réviser.

### 5) Créer une capacité personnalisée (optionnel)

L'un des aspects les plus puissants du MCP est que vous pouvez l'étendre avec vos propres capacités. Par exemple, vous pourriez vouloir exposer un script qui liste toutes les routes Flutter, vérifie les API obsolètes ou exécute des contrôles de qualité de code internes, le tout depuis votre IDE ou votre assistant IA.

Dans l'exemple ci-dessous, un simple serveur MCP Dart enregistre un outil personnalisé appelé `list_routes`. Lorsque le client appelle cet outil, le serveur exécute une fonction qui scanne votre projet à la recherche de définitions de routes et les renvoie sous forme de données structurées. Cela permet à votre assistant IA d'interagir directement avec votre base de code de manière sûre et contrôlée.

```dart
import 'package:dart_mcp_server/dart_mcp_server.dart';

void main() async {
  final server = McpServer();

  // Définir une capacité personnalisée
  server.registerTool(
    'list_routes',
    (context, params) async {
      // Logique d'exemple : extraire tous les noms de routes dans votre projet
      final routes = await extractRoutesFromProject();
      return {'routes': routes};
    },
  );

  await server.start();
}

Future<List<String>> extractRoutesFromProject() async {
  // Votre logique ici — par ex., scanner lib/ pour les définitions de routes
  return ['/', '/login', '/dashboard'];
}
```

Une fois enregistré, votre client MCP (par exemple, Gemini, Cursor ou Copilot) peut appeler cet outil tout comme n'importe quelle capacité intégrée, permettant à l'assistant IA de comprendre les routes de votre application ou de détecter les API obsolètes.

Au-delà des scripts personnalisés, vous pouvez adapter le MCP aux besoins de votre équipe en intégrant des linters internes, des scripts CI ou des vérificateurs de système de design. Vous pouvez également le connecter à des API internes telles que des serveurs d'analyse ou de configuration, ou créer des commandes spécifiques au domaine qui reflètent la manière dont votre équipe construit, teste et déploie des projets. Cela fait du MCP non seulement un protocole, mais une fondation flexible que vous pouvez façonner autour de votre flux de travail.

## Exemple pratique

Avant de regarder le code, clarifions ce que signifie **exposer une capacité MCP en Dart**. Dans le monde du MCP, une **capacité** est simplement un outil ou une fonction qu'un assistant IA peut appeler, par exemple, pour analyser du code, lire un fichier ou exécuter un build. **Exposer** une capacité signifie rendre cet outil accessible via une interface bien définie (généralement via HTTP ou un autre protocole structuré) afin que l'IA ou le client MCP puisse le demander, l'exécuter et recevoir des résultats structurés en retour.

Dans cet exemple, vous verrez comment simuler cette idée à l'aide d'un petit script Dart. Au lieu d'utiliser la pile MCP complète, nous allons créer un simple serveur HTTP local qui expose deux capacités de base : `analyze`, qui exécute `dart analyze` sur votre projet, et `getFileContent`, qui lit et renvoie le contenu d'un fichier donné.

Cela montre le même schéma sous-jacent que celui utilisé par le MCP : des requêtes structurées arrivent, votre serveur effectue une action et des réponses structurées repartent.

Créez un fichier `simple_mcp_server.dart` :

```dart
// simple_mcp_server.dart
import 'dart:convert';
import 'dart:io';

Future<void> main() async {
  final server = await HttpServer.bind(InternetAddress.loopbackIPv4, 8081);
  print('Simple serveur de type MCP écoutant sur http://localhost:8081');

  await for (final request in server) {
    try {
      final body = await utf8.decoder.bind(request).join();
      final data = jsonDecode(body) as Map<String, dynamic>;

      final command = data['command'] as String? ?? '';
      if (command == 'analyze') {
        final result = await Process.run('dart', ['analyze']);
        request.response
          ..statusCode = 200
          ..headers.contentType = ContentType.json
          ..write(jsonEncode({'output': result.stdout.toString(), 'exitCode': result.exitCode}));
      } else if (command == 'getFileContent') {
        final path = data['args']?['path'] as String?;
        if (path == null) {
          request.response
            ..statusCode = 400
            ..write(jsonEncode({'error': 'Chemin manquant'}));
        } else {
          final file = File(path);
          if (!await file.exists()) {
            request.response
              ..statusCode = 404
              ..write(jsonEncode({'error': 'Fichier non trouvé'}));
          } else {
            final content = await file.readAsString();
            request.response
              ..statusCode = 200
              ..headers.contentType = ContentType.json
              ..write(jsonEncode({'content': content}));
          }
        }
      } else {
        request.response
          ..statusCode = 400
          ..write(jsonEncode({'error': 'Commande inconnue'}));
      }
    } catch (e, st) {
      request.response
        ..statusCode = 500
        ..write(jsonEncode({'error': e.toString(), 'stack': st.toString()}));
    } finally {
      await request.response.close();
    }
  }
}
```

Ce script Dart crée un simple serveur HTTP local qui écoute les commandes JSON sur le port 8081. Il accepte des commandes spécifiques telles que `"analyze"` et `"getFileContent"`, exécute les actions correspondantes sur votre machine et renvoie une réponse JSON.

Il s'agit d'une démonstration simplifiée de la manière dont un serveur MCP (Model Context Protocol) gère les requêtes et exécute des outils ou des actions.

Passons-le en revue pièce par pièce pour bien comprendre le code.

#### 1\. Imports

```dart
import 'dart:convert';
import 'dart:io';
```

* `dart:io` donne accès au système de fichiers, aux processus et aux fonctionnalités réseau (utilisé ici pour démarrer le serveur HTTP et interagir avec le système).
    
* `dart:convert` permet l'encodage et le décodage des données JSON (utilisé pour analyser le corps de la requête entrante et envoyer des réponses JSON structurées).
    

#### 2\. Démarrage du serveur

```dart
final server = await HttpServer.bind(InternetAddress.loopbackIPv4, 8081);
print('Simple serveur de type MCP écoutant sur http://localhost:8081');
```

`HttpServer.bind` démarre un serveur HTTP sur la machine locale (`127.0.0.1`) et le port `8081`. Le serveur ne sera accessible que depuis votre propre ordinateur, pas depuis Internet, et le message confirme que le serveur fonctionne et écoute les requêtes entrantes.

#### 3\. Gestion des requêtes

```dart
await for (final request in server) {
```

Ceci écoute en continu les requêtes HTTP entrantes. Chaque requête déclenche une nouvelle itération de la boucle, permettant plusieurs requêtes au fil du temps.

#### 4\. Lecture du corps de la requête

```dart
final body = await utf8.decoder.bind(request).join();
final data = jsonDecode(body) as Map<String, dynamic>;
```

Ceci lit le corps complet de la requête (en supposant qu'il s'agisse de texte encodé en UTF-8) et convertit la chaîne JSON en une map Dart (`data`) afin qu'elle puisse être consultée par programme.

Exemple d'entrée attendue :

```json
{
  "command": "analyze"
}
```

#### 5\. Analyse et routage de la commande

```dart
final command = data['command'] as String? ?? '';
```

Ceci extrait la clé `command` du corps de la requête. Si elle est manquante ou nulle, elle prend par défaut une chaîne vide.

Le serveur utilise cette valeur pour déterminer l'action à effectuer.

#### 6\. Gestion de la commande "analyze"

```dart
if (command == 'analyze') {
  final result = await Process.run('dart', ['analyze']);
  request.response
    ..statusCode = 200
    ..headers.contentType = ContentType.json
    ..write(jsonEncode({'output': result.stdout.toString(), 'exitCode': result.exitCode}));
}
```

Si la commande est `"analyze"`, le script exécute la commande de terminal `dart analyze` en utilisant `Process.run()`. Cela vérifie votre projet Dart pour les erreurs, les avertissements ou les lints. La sortie de cette commande (`stdout`) et son code de sortie sont renvoyés sous forme de JSON dans la réponse HTTP.

Exemple de réponse attendue :

```json
{
  "output": "Analyzing project...\nNo issues found!",
  "exitCode": 0
}
```

#### 7\. Gestion de la commande "getFileContent"

```dart
else if (command == 'getFileContent') {
  final path = data['args']?['path'] as String?;
```

Cette commande attend un objet `"args"` contenant une clé `"path"`.

Exemple de requête :

```json
{
  "command": "getFileContent",
  "args": { "path": "lib/main.dart" }
}
```

Le reste du bloc :

```dart
if (path == null) {
  request.response
    ..statusCode = 400
    ..write(jsonEncode({'error': 'Chemin manquant'}));
} else {
  final file = File(path);
  if (!await file.exists()) {
    request.response
      ..statusCode = 404
      ..write(jsonEncode({'error': 'Fichier non trouvé'}));
  } else {
    final content = await file.readAsString();
    request.response
      ..statusCode = 200
      ..headers.contentType = ContentType.json
      ..write(jsonEncode({'content': content}));
  }
}
```

Si aucun chemin n'est fourni, il renvoie une erreur HTTP 400. Si le fichier n'existe pas, il renvoie un 404. Et si le fichier existe, il lit son contenu et le renvoie au format JSON.

Exemple de réponse :

```json
{
  "content": "void main() { print('Hello World'); }"
}
```

#### 8\. Gestion des commandes inconnues

```dart
else {
  request.response
    ..statusCode = 400
    ..write(jsonEncode({'error': 'Commande inconnue'}));
}
```

Si le champ `command` ne correspond à aucune option connue, le serveur renvoie une erreur.

#### 9\. Gestion des erreurs

```dart
} catch (e, st) {
  request.response
    ..statusCode = 500
    ..write(jsonEncode({'error': e.toString(), 'stack': st.toString()}));
}
```

Si une exception non gérée se produit (comme un JSON invalide ou des erreurs d'exécution), le serveur la capture. Il répond avec un statut 500 et inclut à la fois le message d'erreur et la trace de la pile pour le débogage.

#### 10\. Fermeture de la réponse

```dart
finally {
  await request.response.close();
}
```

Garantit que la réponse est correctement fermée après chaque requête pour éviter les fuites de ressources.

#### Résumé

Il s'agit d'un serveur HTTP local qui imite un flux de travail MCP très basique. Il accepte des commandes via HTTP, effectue des opérations système ou de fichiers et renvoie des résultats JSON structurés. Il démontre comment un assistant IA pourrait interagir avec un environnement Dart par programme (par exemple, en analysant du code ou en lisant des fichiers) via un protocole sûr et structuré.

**Comment l'exécuter :**

1. Enregistrez le fichier à la racine d'un projet Dart.
    
2. Exécutez `dart run simple_mcp_server.dart`.
    
3. Dans un autre terminal, testez la commande `analyze` :
    

```bash
curl -X POST http://localhost:8081 -H "Content-Type: application/json" -d '{"command":"analyze"}'
```

Vous recevrez la sortie de l'analyseur sous forme de JSON. Dans un véritable flux de travail MCP, le client IA effectuerait des appels structurés de manière similaire, sauf que ces appels sont gérés par un client MCP et suivent la spécification MCP pour les outils/ressources/racines. Le serveur MCP Dart officiel fournit beaucoup plus d'outils intégrés et une implémentation complète qui s'intègre aux clients pris en charge.

## Comment construire un serveur MCP simple en Dart

Dans la section précédente, nous avons construit une version simplifiée et conceptuelle d'un serveur de type MCP en utilisant du Dart pur et HTTP. Cet exemple a permis d'illustrer l'idée de base : recevoir des requêtes structurées, exécuter des actions spécifiques et renvoyer des résultats structurés.

Maintenant, poussons ce concept plus loin et voyons comment construire un véritable serveur MCP en utilisant le paquet officiel `dart_mcp`. Cette version suit la véritable spécification MCP et peut interagir avec de réels clients MCP, vous donnant une base pour étendre, tester ou personnaliser la façon dont vos outils de développement communiquent avec l'assistant IA.

### Étape 1 : Ajouter la dépendance

Ajoutez ceci à votre `pubspec.yaml` :

```dart
dependencies:
  dart_mcp: ^0.3.3
```

### Étape 2 : Créer le serveur

```dart
import 'package:dart_mcp/server.dart';

class MyServer extends MCPServer with ToolsSupport, ResourcesSupport {
  MyServer()
      : super(Implementation(
          name: 'my-dart-mcp-server',
          version: '1.0.0',
        ));

  @override
  Future<void> initialize() async {
    // Enregistrer un outil simple
    registerTool(
      'analyzeCode',
      description: 'Analyser le code Dart à l\'aide de l\'analyseur.',
      inputSchema: {
        'type': 'object',
        'properties': {
          'path': {'type': 'string'}
        },
        'required': ['path']
      },
      callback: (args, extra) async {
        final path = args['path'];
        // Vous pouvez appeler `dart analyze` ici ou intégrer les API de l'analyseur
        return {'message': 'Projet analysé avec succès à l\'emplacement $path.'};
      },
    );

    await super.initialize();
  }
}

void main() {
  final server = MyServer();
  server.connect(StdioServerTransport());
}
```

Ce code Dart définit un serveur MCP de base en utilisant le paquet officiel `dart_mcp`.

C'est un exemple de travail minimal qui démontre comment créer un serveur MCP personnalisé, enregistrer une commande (« outil ») que les assistants IA ou les clients peuvent appeler, et l'exposer via une connexion locale (en utilisant l'entrée/sortie standard, `stdio`).

Décomposons-le ligne par ligne.

**1\. Importer le paquet**

```dart
import 'package:dart_mcp/server.dart';
```

Ceci importe les API côté serveur du paquet `dart_mcp`. Ces API vous permettent de créer et de configurer un serveur MCP, d'enregistrer des outils (commandes) et des ressources, et de gérer les requêtes entrantes des clients MCP (par exemple, des éditeurs ou des assistants IA).

**2\. Créer une classe de serveur**

```dart
class MyServer extends MCPServer with ToolsSupport, ResourcesSupport {
```

Ceci définit une classe personnalisée nommée `MyServer` qui étend `MCPServer`.

`MCPServer` est la classe de base qui gère la communication, l'initialisation et la découverte des capacités. Les mots-clés `with` ajoutent des capacités supplémentaires. `ToolsSupport` vous permet d'enregistrer des outils, des commandes appelables qui effectuent des actions. `ResourcesSupport` vous permet d'enregistrer des ressources, des données accessibles comme des fichiers de projet ou des jeux de données.

Ainsi, ce serveur prend en charge à la fois les outils (commandes) et les ressources (données).

**3\. Le constructeur**

```dart
MyServer()
    : super(Implementation(
        name: 'my-dart-mcp-server',
        version: '1.0.0',
      ));
```

Ici, le constructeur transmet des informations sur l'implémentation à la classe parente `MCPServer`.

`Implementation` est un objet de métadonnées qui décrit le serveur, incluant :

* `name`, un nom unique pour votre serveur, et
    
* `version`, le numéro de version.
    

Ces métadonnées aident les clients à identifier le serveur MCP avec lequel ils communiquent.

**4\. Surcharge de la méthode d'initialisation**

```dart
@override
Future<void> initialize() async {
```

Cette méthode s'exécute au démarrage du serveur. C'est là que vous enregistrez les outils et les ressources avant que le serveur ne commence à écouter les commandes.

**5\. Enregistrement d'un outil**

```dart
registerTool(
  'analyzeCode',
  description: 'Analyser le code Dart à l\'aide de l\'analyseur.',
  inputSchema: {
    'type': 'object',
    'properties': {
      'path': {'type': 'string'}
    },
    'required': ['path']
  },
  callback: (args, extra) async {
    final path = args['path'];
    // Vous pouvez appeler `dart analyze` ici ou intégrer les API de l'analyseur
    return {'message': 'Projet analysé avec succès à l\'emplacement $path.'};
  },
);
```

Cette section définit un outil appelé `"analyzeCode"`.

Expliquons chaque partie :

* `'analyzeCode'` : le nom de l'outil (comment un client l'identifie).
    
* `description` : une courte explication de ce que fait l'outil.
    
* `inputSchema` : un schéma JSON qui définit l'entrée attendue par cet outil. Il attend un objet avec une propriété `"path"`, qui doit être une chaîne de caractères.
    
* `callback` : une fonction qui s'exécute lorsque le client appelle cet outil.
    
* `args` contient l'entrée du client, et vous pouvez utiliser `args['path']` pour accéder au chemin fourni. Dans une implémentation réelle, vous pourriez appeler `dart analyze` ou utiliser les API de l'analyseur Dart pour vérifier le code à ce chemin. Le callback renvoie une réponse (dans ce cas, un message de succès).
    

Cet outil pourra plus tard être invoqué par un client MCP connecté, par exemple :

```json
{
  "command": "analyzeCode",
  "args": { "path": "lib/" }
}
```

Et le serveur répondrait :

```json
{
  "message": "Projet analysé avec succès à l'emplacement lib/."
}
```

**6\. Appel de l'initialiseur parent**

```dart
await super.initialize();
```

Ceci garantit que la classe de base (`MCPServer`) effectue sa propre logique d'initialisation après votre configuration personnalisée (par exemple, l'enregistrement d'outils intégrés ou la préparation de structures internes).

**7\. Point d'entrée principal**

```dart
void main() {
  final server = MyServer();
  server.connect(StdioServerTransport());
}
```

C'est le point d'entrée de l'application. Il crée une instance de votre classe `MyServer`. Ensuite, il se connecte en utilisant `StdioServerTransport()` qui permet au serveur de communiquer via l'entrée/sortie standard (stdio), le même mécanisme utilisé par les assistants IA locaux et les outils en ligne de commande.

En pratique, cela signifie que le serveur n'a pas besoin d'exécuter un serveur HTTP. Il peut parler directement à d'autres outils locaux qui utilisent le MCP, tels que des extensions d'IDE ou des assistants IA qui le lancent.

Ce type de serveur MCP pourrait être connecté à un IDE comme VS Code ou JetBrains via MCP pour exécuter l'analyse Dart automatiquement. Il permettrait à un assistant IA d'accéder à votre projet Dart local, d'analyser des fichiers et de renvoyer des informations, servant de pont entre votre projet Flutter et des outils d'automatisation externes.

C'est un exemple simple qui crée une commande (`analyzeCode`) qu'un client MCP (comme un assistant IA) peut appeler. Le client enverra l'entrée via le protocole MCP, et votre serveur Dart répondra en conséquence.

## Connexion à votre serveur MCP avec un client

Maintenant que vous avez construit un serveur MCP simple, l'étape logique suivante est de voir comment un client interagit avec lui. Le client est l'autre moitié de l'équation : il se connecte à votre serveur, initialise la communication et appelle les outils (capacités) que vous avez enregistrés.

L'exemple ci-dessous montre comment créer un client MCP de base basé sur Dart qui parle au serveur que vous avez construit précédemment et invoque l'un de ses outils.

```dart
import 'package:dart_mcp/client.dart';

void main() async {
  final client = await MCPClient.connectStdioServer(stdin, stdout);
  final initResult = await client.initialize(
    Implementation(name: 'my-client', version: '1.0.0'),
  );

  print('Connecté au serveur : ${initResult.serverCapabilities.tools}');
  final result = await client.callTool('analyzeCode', {'path': 'lib/'});
  print(result);
}
```

Ce code crée un client MCP simple qui se connecte à un serveur MCP (comme celui que vous avez construit précédemment) et appelle l'un de ses outils enregistrés.

Voici ce qu'il fait, étape par étape :

```dart
import 'package:dart_mcp/client.dart';
```

Ceci importe l'API côté client du paquet `dart_mcp`. Cela vous permet de vous connecter à un serveur MCP et d'appeler ses outils.

```dart
final client = await MCPClient.connectStdioServer(stdin, stdout);
```

Ceci crée un nouveau client MCP et se connecte à un serveur en utilisant l'entrée/sortie standard (stdio). Encore une fois, c'est ainsi que les outils locaux ou les assistants IA communiquent avec les serveurs MCP s'exécutant sur votre système.

```dart
final initResult = await client.initialize(
  Implementation(name: 'my-client', version: '1.0.0'),
);
```

Ceci envoie une requête d'initialisation au serveur. L'objet `Implementation` identifie ce client par son nom et sa version. Le serveur répond avec ses capacités disponibles (comme les outils et ressources enregistrés).

```dart
print('Connecté au serveur : ${initResult.serverCapabilities.tools}');
```

Ceci affiche la liste des outils que le serveur a enregistrés, par exemple, `["analyzeCode"]`.

```dart
final result = await client.callTool('analyzeCode', {'path': 'lib/'});
```

Ceci appelle l'outil `analyzeCode` du serveur, en passant `{'path': 'lib/'}` comme entrée. Le serveur exécute le callback enregistré pour cet outil et renvoie une réponse.

```dart
print(result);
```

Et ceci affiche le résultat renvoyé par le serveur (par exemple : `{"message": "Projet analysé avec succès à l'emplacement lib/."}`).

**Résumé :**
Ce client se connecte à un serveur MCP via stdio, initialise la communication, liste les outils disponibles, en appelle un (`analyzeCode`) et affiche la réponse. C'est le pendant côté client de l'exemple de serveur précédent. Ensemble, ils démontrent comment deux programmes Dart peuvent communiquer en utilisant le protocole MCP.

Ceci se connecte au serveur MCP via stdin/stdout, initialise la communication et appelle l'outil `analyzeCode`.

## MCP vs Serveurs HTTP personnalisés

Si vous avez déjà construit un simple serveur HTTP Dart qui gère des commandes comme « analyze » ou « getFileContent », vous avez déjà fait quelque chose de similaire au MCP. La différence est que le MCP fournit une structure et un protocole formels qui standardisent la manière dont ces interactions se produisent.

Au lieu d'une analyse JSON manuelle et de commandes ad hoc, la couche MCP gère :

* L'enregistrement et la découverte des outils
    
* La validation basée sur des schémas
    
* Les types de requêtes et de réponses standardisés
    
* L'initialisation intégrée et la négociation des capacités
    

Ainsi, alors qu'une approche HTTP personnalisée fonctionne pour des expériences rapides, `dart_mcp` vous permet de construire des outils MCP conformes et pérennes qui s'intègrent proprement aux éditeurs et assistants.

## Bonnes pratiques, sécurité et permissions

* **Commencez en lecture seule.** Donnez d'abord à l'assistant des outils qui lisent l'état du projet (analyser, lire un fichier, exécuter des tests). N'activez les actions d'écriture (modifier des fichiers, git commit) qu'une fois que vous avez confiance en l'automatisation.
    
* **Révisez chaque changement.** Même si l'IA peut appliquer des correctifs, traitez-la comme un co-auteur : inspectez les diffs et exécutez vos tests.
    
* **Limitez les portées.** N'exposez pas de secrets ou de clés au serveur MCP. Utilisez la séparation des environnements (dev vs CI) et le filtrage explicite des capacités.
    
* **Journaux d'audit.** Conservez des logs pour les appels MCP et les modifications effectuées par les agents afin de pouvoir tracer qui a fait quoi et quand.
    
* **Établissez des règles d'équipe.** Définissez des politiques d'équipe pour les modifications automatisées, par exemple : « L'IA peut appliquer le formatage et des corrections mineures de lint, mais pas de changements architecturaux majeurs sans approbation humaine. »
    

## Débuter en tant que débutant

Si vous êtes nouveau dans ce domaine, voici une feuille de route simple :

1. **Lisez les bases du MCP :** Visitez la page [officielle Dart MCP](https://dart.dev/tools/mcp-server) pour comprendre ce que c'est et où il s'insère dans votre flux de travail.
    
2. **Installez et explorez** `dart_mcp` : Essayez d'exécuter l'un des exemples sur [pub.dev](https://pub.dev/packages/dart_mcp/example). Expérimentez en construisant votre propre outil simple.
    
3. **Connectez-le à votre assistant IA ou IDE :** Des outils comme Gemini ou les plugins MCP de VS Code vous permettent d'enregistrer votre serveur MCP Dart local dans le fichier de configuration `mcpServers`.
    
4. **Développez vos outils :** Construisez des commandes plus complexes comme « exécuter les tests », « formater le code », « récupérer les dépendances » ou « générer des rapports ».
    
5. **Contribuez ou suivez le dépôt Dart Labs :** Le support MCP dans Dart évolue rapidement. Se tenir au courant des mises à jour vous aide à garder une longueur d'avance.
    

## Aller au-delà du niveau débutant

Une fois que vous avez compris les bases :

* Commencez à intégrer vos outils MCP dans les pipelines de développement Flutter.
    
* Construisez un assistant alimenté par l'IA qui interagit directement avec vos fichiers de projet Flutter.
    
* Explorez les discussions GitHub sur le MCP et la spécification du contexte de modèle d'OpenAI pour des informations plus approfondies.
    
* Vous pouvez même contribuer votre propre paquet basé sur le MCP à la communauté.
    

## Conclusion

Le Model Context Protocol façonne la prochaine génération d'outils de développement, permettant des flux de travail plus intelligents, pilotés par l'IA et mieux intégrés. En tant que développeur Dart ou Flutter, apprendre le MCP dès maintenant vous positionne en avance sur la courbe.

En tirant parti du paquet `dart_mcp`, vous pouvez commencer à construire des outils conformes, extensibles et automatisés dès aujourd'hui, transformant la façon dont votre environnement de développement interagit avec le code, l'analyse et l'IA.

## Références

* « [Dart and Flutter MCP Server » (docs officielles)](https://dart.dev/tools/mcp-server)
    
* [Paquet `dart_mcp`](https://pub.dev/packages/dart_mcp) sur pub.dev
    
* Article Medium « [Supercharge Your Dart & Flutter Development Experience with the Dart and Flutter MCP Server](https://medium.com/flutter/supercharge-your-dart-flutter-development-experience-with-the-dart-mcp-server-2edcc8107b49) »
    
* [Dépôt GitHub](https://github.com/its-dart/dart-mcp-server) pour une implémentation de serveur MCP Dart