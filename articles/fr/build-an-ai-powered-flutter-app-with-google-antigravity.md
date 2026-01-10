---
title: 'Comment créer une application Flutter alimentée par IA avec Google Antigravity
  : Un tutoriel pratique'
subtitle: ''
author: Anna Muzykina
co_authors: []
series: null
date: '2026-01-07T17:26:39.288Z'
originalURL: https://freecodecamp.org/news/build-an-ai-powered-flutter-app-with-google-antigravity
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1767806742391/846769af-4cbe-482c-b884-8f9ca50d7456.png
tags:
- name: AI
  slug: ai
- name: '#ai-tools'
  slug: ai-tools
- name: Google Antigravity
  slug: google-antigravity
- name: Flutter
  slug: flutter
- name: gemma
  slug: gemma
- name: Gemma3
  slug: gemma3
seo_title: 'Comment créer une application Flutter alimentée par IA avec Google Antigravity
  : Un tutoriel pratique'
seo_desc: 'As a Flutter developer who’s building a cloud-based ecosystem for digital
  media lifecycle management, I’m constantly looking for ways to speed up the transition
  from idea to prototype.

  In November 2025, Google launched antigravity, a new interactive ...'
---

En tant que développeur Flutter qui construit un écosystème basé sur le cloud pour la gestion du cycle de vie des médias numériques, je cherche constamment des moyens d'accélérer la transition de l'idée au prototype.

En novembre 2025, Google a lancé [**antigravity**](https://antigravity.google/blog/introducing-google-antigravity), une nouvelle plateforme de codage interactive qui a fondamentalement changé mon flux de travail.

Antigravity a complètement [changé la rapidité avec laquelle vous pouvez prototyper](https://www.youtube.com/watch?v=SVCBA-pBgt0&t=2s) et itérer sur des projets. Au lieu d'écrire du code boilerplate ou de passer des heures à chercher dans la documentation, vous pouvez décrire vos besoins en langage naturel, examiner le plan et laisser les agents IA créer, tester et même exécuter le code.

Cette approche de "codage en l'air" crée la sensation de travailler avec un développeur junior très capable qui ne se fatigue jamais.

Sur la base de mon expérience positive, j'ai décidé de partager mes premiers pas et mes réflexions sur Antigravity. Dans ce tutoriel pratique, nous créerons Water Tracker, une belle application Flutter moderne qui aide les utilisateurs à suivre leur consommation d'eau avec une visualisation intelligente des progrès et des rappels doux.

Nous utiliserons Antigravity pour laisser les agents IA planifier, écrire, tester et montrer des vidéos de votre application. Ce style de “[vibe coding](https://www.freecodecamp.org/news/how-to-use-vibe-coding-effectively-as-a-dev/)“ signifie que vous décrivez ce que vous voulez, examinez les plans et approuvez les changements – tout en laissant les agents faire le travail difficile.

L'application présentera un design [glassmorphism](https://www.freecodecamp.org/news/glassmorphism-how-to-create-a-glass-card-in-figma/) : des cartes en verre givré, des arrière-plans floutés, des bordures subtiles et une translucidité douce. Cela donnera à l'application un aspect premium et moderne qui est à la fois élégant et apaisant.

## Voici ce que nous allons couvrir :

* [Voici ce que nous allons couvrir :](#heading-voici-ce-que-nous-allons-couvrir)
    
* [Prérequis](#heading-prerequis)
    
* [Comprendre le moteur Antigravity](#heading-comprendre-le-moteur-antigravity)
    
* [Invites : la clé du "Vibe Coding" réussi dans Antigravity](#heading-invites-la-cle-du-vibe-coding-reussi-dans-antigravity)
    
* [Étape 1 : Ouvrir Antigravity et créer un espace de travail](#heading-etape-1-ouvrir-antigravity-et-creer-un-espace-de-travail)
    
* [Étape 2 : Maîtriser l'art de l'invitation agentique](#heading-etape-2-maitriser-lart-de-linvitation-agentique)
    
    * [L'anatomie d'une invite parfaite](#heading-lanatomie-dune-invite-parfaite)
        
    * [Analyse de la stratégie d'invite](#heading-analyse-de-la-strategie-dinvite)
        
    * [Examen du plan de mise en œuvre](#heading-examen-du-plan-de-mise-en-oeuvre)
        
    * [Autorisation des commandes dans le gestionnaire d'agents](#heading-autorisation-des-commandes-dans-le-gestionnaire-dagents)
        
    * [Gestion des commandes et des dossiers](#heading-gestion-des-commandes-et-des-dossiers)
        
    * [Vérification du lancement de l'émulateur](#heading-verification-du-lancement-de-lemulateur)
        
* [Passage à l'éditeur pour vérification](#heading-passage-a-lediteur-pour-verification)
    
    * [Comprendre l'orchestration vs la vérification](#heading-comprendre-lorchestration-vs-la-verification)
        
    * [Résumé du flux de travail](#heading-resume-du-flux-de-travail)
        
* [Étape 3 : Implémenter l'écran principal Glassmorphic](#heading-etape-3-implementer-lecran-principal-glassmorphic)
    
* [Étape 4 : Ajouter la persistance et la logique quotidienne](#heading-etape-4-ajouter-la-persistance-et-la-logique-quotidienne)
    
* [Étape 5 : Ajouter des rappels intelligents sur l'appareil avec Gemma](#heading-etape-5-ajouter-des-rappels-intelligents-sur-lappareil-avec-gemma)
    
* [Étape 6 : Dernières retouches](#heading-etape-6-dernieres-retouches)
    
    * [Examen des dernières modifications](#heading-examen-des-dernieres-modifications)
        
* [Limite de quota Antigravity](#heading-limite-de-quota-antigravity)
    
* [Conclusion](#heading-conclusion)
    

Dans ce tutoriel, nous allons construire **Water Tracker** : une application Flutter moderne avec un design attrayant en glassmorphisme. Nous utiliserons le flux de travail agentique d'Antigravity pour gérer les tâches difficiles, y compris une visualisation circulaire des progrès et des rappels intelligents sur l'appareil alimentés par Gemma.

## Prérequis

Pour suivre ce tutoriel, vous aurez besoin de :

* Le SDK Flutter installé (Flutter doctor doit être propre)
    
* Un émulateur Android ou un appareil physique
    
* Google Antigravity installé (vous pouvez utiliser l'aperçu public gratuit depuis [antigravity.google](https://antigravity.google/))
    

## Comprendre le moteur Antigravity

Avant de plonger dans le code, il est important de comprendre ce qui se passe sous le capot. Contrairement aux interfaces de chat LLM standard qui fournissent simplement des extraits de code à copier-coller, Google Antigravity est une plateforme de développement agentique.

Bien que le cœur soit une expérience d'IDE alimentée par IA qui utilise le meilleur des modèles de Google, Antigravity fait évoluer l'IDE vers un avenir axé sur les agents avec des capacités de contrôle du navigateur, des modèles d'interaction asynchrones et un facteur de forme de produit axé sur les agents. Ensemble, tout cela permet aux agents de planifier et d'exécuter de manière autonome des tâches logicielles complexes, de bout en bout.

Il se connecte à des modèles de langage puissants, mais il dispose également d'"outils" ou de "compétences" qui lui permettent d'interagir avec votre système de fichiers, d'exécuter des commandes de terminal comme `flutter create`, et même d'exécuter l'application dans un émulateur.

Lorsque vous envoyez une invite, le système ne se contente pas de deviner le mot suivant. Il utilise une boucle de raisonnement pour planifier des actions, les exécuter et vérifier la sortie.

Mais parce que ces agents peuvent prendre des décisions autonomes, votre rôle passe de "rédacteur" à "éditeur et superviseur". Vous devez vérifier les plans des agents pour vous assurer qu'ils suivent les meilleures pratiques et n'introduisent pas de régressions de sécurité ou de performance.

## **Invites : la clé du "Vibe Coding" réussi dans Antigravity**

En construisant ma plateforme, j'ai appris que les invites pour Google Antigravity sont complètement différentes des chats IA réguliers ou des compléteurs de code.

Antigravity est **agentique**. Cela signifie que les agents IA peuvent exécuter des commandes, créer des fichiers, lancer des applications et tout tester de manière autonome. Cette puissance signifie que les invites doivent être structurées comme des instructions détaillées à un développeur junior très capable, et non comme de courtes demandes.

C'est pourquoi chaque invite dans ce tutoriel suit le même modèle :

* **Objectif de haut niveau + ambiance** : Je décris la fonctionnalité et le sentiment souhaité (par exemple, glassmorphisme avec des bleus doux, premium et apaisant).
    
* **Exigences détaillées en puces** : Fonctionnalité, UX, design, performance, accessibilité – tout ce dont l'agent a besoin pour livrer une qualité dès la première tentative.
    
* **Sécurité d'abord** : Incluez toujours quelque chose comme : "Avant toute commande/code : générez un artefact de plan détaillé (arbre de dossiers, dépendances, étapes) et demandez une approbation." Cela force l'agent à réfléchir d'abord et me permet de réviser/corriger avant que quoi que ce soit ne change.
    
* **Demande de vérification** : Demandez des captures d'écran et des artefacts de vidéo pour que je puisse vérifier visuellement le résultat.
    
* **Pas de rôles ou de fluff** : Utilisez un langage direct et naturel. Les agents n'ont pas besoin de "Vous êtes un expert..." pour bien travailler.
    

Ce style aide à prévenir les erreurs (pour que les agents ne puissent pas s'emballer), assure une qualité premium constante (glassmorphisme bien fait) et crée le flux "vibe coding" détendu : vous pouvez vous concentrer sur la vision, approuver les plans et obtenir des fonctionnalités polies rapidement.

Sans cette structure, les agents pourraient sauter des étapes ou produire des résultats basiques. Avec elle, vous obtenez la belle application fonctionnelle que nous avons construite ensemble. Dans ce tutoriel, je partagerai les invites que j'utilise.

## Étape 1 : Ouvrir Antigravity et créer un espace de travail

Pour commencer, vous devrez télécharger et installer l'IDE Antigravity. Il est important de noter qu'Antigravity est une application autonome, et non un plugin ou une extension pour votre éditeur existant.

Il est construit comme un **fork de Visual Studio Code**, ce qui signifie que la configuration est incroyablement simple. Si vous avez déjà utilisé VS Code, l'interface vous sera instantanément familière, et vous pouvez même apporter vos raccourcis et thèmes préférés. Il fonctionne comme un environnement de développement autonome qui intègre l'éditeur, le terminal et les agents IA dans une seule fenêtre.

Ensuite, ouvrez le gestionnaire d'agents en cliquant sur "Open Agent Manager" (soit le bouton en haut ou au centre de l'écran, comme vous pouvez le voir ci-dessous) :

![Ouvrir le gestionnaire d'agents dans Antigravity](https://cdn.hashnode.com/res/hashnode/image/upload/v1766772585000/860da5bb-99f5-4e57-a3ef-18f93d4b6a54.png align="center")

Le panneau de gauche a un bouton "+ Open Workspace" – cliquez simplement dessus pour créer un nouvel espace de travail :

![Cliquez sur "Open Workspace" pour créer un nouvel espace de travail dans Antigravity](https://cdn.hashnode.com/res/hashnode/image/upload/v1766432535748/016d64c0-3869-48f7-860d-0a6b087db01e.png align="center")

Ensuite, cliquez sur "Open New Workspace" :

![Ouvrez l'espace de travail en cliquant sur "Open New Workspace"](https://cdn.hashnode.com/res/hashnode/image/upload/v1766432590892/24504fd9-e621-4ecd-b6d5-7d99ac0fd14a.png align="center")

Ensuite, nommez-le `water_tracker` et créez-le :

![Nommez et créez l'espace de travail](https://cdn.hashnode.com/res/hashnode/image/upload/v1766432640664/3d9a3522-6199-4659-a62d-ec199c87be2e.png align="center")

Vous avez maintenant un espace de travail propre prêt pour les invites :

![L'espace de travail est maintenant prêt](https://cdn.hashnode.com/res/hashnode/image/upload/v1766432668236/e0df1845-6012-4732-97da-f45135d41680.png align="center")

Cela crée un environnement en bac à sable où l'agent IA peut gérer vos fichiers en toute sécurité sans affecter vos autres projets. Et maintenant, vos agents IA ont la permission de construire et de tester votre code Flutter !

## Étape 2 : Maîtriser l'art de l'invitation agentique

Dans Antigravity, votre succès dépend de la manière dont vous communiquez avec vos agents. Les bonnes invites sont détaillées et nécessitent toujours un plan d'abord. Pour créer une invite efficace, vous devez penser comme un chef de projet : définir la portée, établir des contraintes techniques et créer un "point de contrôle" avant que l'agent n'exécute un code.

### L'anatomie d'une invite parfaite

Comme nous en avons brièvement discuté ci-dessus, une invite solide suit une structure claire : **Contexte + Objectif + Contraintes + Vérification**. En demandant explicitement un plan, vous empêchez l'agent de faire des suppositions sur votre architecture ou votre style d'UI qui pourraient être difficiles à annuler plus tard.

Copiez et collez l'invite suivante dans le gestionnaire d'agents :

```markdown
Créez un nouveau projet Flutter nommé `water_tracker`.

Exigences de design :
- Style glassmorphism partout : cartes en verre givré, arrière-plans floutés, bordures subtiles, translucidité
- Palette de couleurs douces : bleus clairs, blancs, dégradés doux
- Aspect moderne et premium avec profondeur et élégance

Avant toute commande :
1. Générez un artefact de plan de projet détaillé incluant :
   - Arbre de structure de dossiers complet
   - Dépendances recommandées (par exemple, shared_preferences, package glassmorphism si disponible)
   - Architecture de haut niveau (gestion d'état simple pour commencer)
2. Demandez mon approbation explicite.

Après approbation :
- Exécutez `flutter create water_tracker`
- Ajoutez les dépendances
- Lancez l'application vide
- Fournissez des captures d'écran et un artefact de vidéo.
```

![Collez l'invite dans le chat du gestionnaire d'agents et cliquez sur le bouton bleu "+"](https://cdn.hashnode.com/res/hashnode/image/upload/v1766433166692/2e0ba4b8-dbb0-4101-a2c6-a250ec318dbf.png align="center")

### Analyse de la stratégie d'invite

J'ai conçu cette invite avec des "hooks" spécifiques pour garantir une sortie de haute qualité :

1. Tout d'abord, le bloc **Exigences de design** utilise un langage sensoriel ("givré", "doux", "profondeur") pour guider le choix esthétique de l'agent.
    
2. Ensuite, la section **"Avant toute commande"** est l'élément le plus important car elle crée une porte de sécurité. Cela force l'agent à passer en mode "Plan d'abord", où il doit présenter sa logique sous forme de document lisible (un artefact) avant de toucher votre système de fichiers.
    
3. Enfin, les demandes de **vérification** (captures d'écran/vidéo) garantissent que l'agent est responsable de prouver que la configuration a réussi.
    

### Examen du plan de mise en œuvre

Après avoir exécuté cette invite, l'agent vous donnera un plan à examiner. Faites défiler vers le bas et lisez tout attentivement, en vous assurant que le plan semble solide. Si c'est le cas, répondez en cliquant sur le bouton **"Proceed"** :

![Examinez la réponse/le plan et cliquez sur proceed si vous êtes satisfait des résultats](https://cdn.hashnode.com/res/hashnode/image/upload/v1766777527328/cceff62d-9cf3-4794-b8e6-65565598b4d8.png align="center")

### Autorisation des commandes dans le gestionnaire d'agents

Après avoir procédé avec le plan, l'agent commencera la phase **Initialisation du projet**. Dans Antigravity, les agents n'exécutent pas les commandes de terminal en arrière-plan sans votre connaissance. Au lieu de cela, ils présentent la commande spécifique pour votre autorisation.

!["L'agent exécute des commandes de terminal" - pour que vous puissiez les examiner](https://cdn.hashnode.com/res/hashnode/image/upload/v1766778411176/0ea3013b-e7b9-486f-ab3b-c65f2ef1b628.png align="center")

Comme montré dans la capture d'écran ci-dessus, l'agent demandera à exécuter : `flutter pub add provider shared_preferences intl flutter_animate google_fonts`.

Cliquer sur **"Accept"** ici est l'action spécifique qui donne à l'agent la permission d'exécuter réellement la commande dans votre espace de travail. C'est le moment où le projet commence réellement à exister, les dépendances sont ajoutées et la structure de dossiers initiale est générée.

![Acceptez le travail de l'agent](https://cdn.hashnode.com/res/hashnode/image/upload/v1766436979535/d5b65713-761a-4b3d-ad6e-ebea5be343d9.png align="center")

### Gestion des commandes et des dossiers

La porte "Step Requires Input" garantit que vous conservez le contrôle total sur ce qui est installé sur votre machine.
Avant que des répertoires ne soient réellement créés, l'agent affiche la commande exacte `mkdir` qu'il prévoit d'exécuter. Vous devrez examiner cette structure de dossiers proposée et cliquer sur le bouton bleu **"Accepter"** pour autoriser l'agent à créer physiquement ces chemins dans votre espace de travail.

![Accepter que l'agent crée des chemins spécifiques dans votre espace de travail](https://cdn.hashnode.com/res/hashnode/image/upload/v1766778588513/d348cab7-147a-4733-8a31-cf66010a2449.png align="center")

### Vérification du lancement de l'émulateur

Avant de lancer sur l'émulateur, l'agent demandera la permission de le lancer :

![Agent demandant la permission de lancer l'émulateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1766779040373/7cfcaf88-ba61-40d2-8eda-f100a65c0151.png align="center")

L'agent initialisera ensuite le projet et vous montrera l'application en cours d'exécution dans l'émulateur intégré :

![Agent montrant l'application en cours d'exécution](https://cdn.hashnode.com/res/hashnode/image/upload/v1766833166339/bab74ad2-d15a-4870-b767-1f8a08ca8836.png align="center")

De plus, l'agent teste l'application et enregistre une vidéo de quelques secondes pour démontrer que tous les boutons fonctionnent :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1766833182488/dad906af-b0a4-450d-9fcd-68b914c54c85.png align="center")

## Passage à l'éditeur pour vérification

Une fois que l'agent a terminé l'initialisation du projet et la construction de la structure de répertoires, vous voudrez voir les résultats de son travail.

Comme Antigravity est un IDE agentique, il garde souvent le focus sur le **Gestionnaire d'agents** pendant qu'il exécute des commandes de terminal et génère du code en arrière-plan. Pour passer du journal de l'agent au code source réel, cliquez sur le bouton "Ouvrir l'éditeur" (l'icône `< >`) situé en haut à droite de l'interface.

![Vérification des dossiers/fichiers du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1767653383038/5f84773b-0b04-4417-9c1b-c992f1a9e9c1.png align="center")

En cliquant sur ce bouton, vous révélerez la vue **Explorer** à gauche, où vous pourrez maintenant voir le projet `water_tracker` nouvellement créé. Vous devriez explorer le répertoire `lib/` pour vérifier que l'agent a bien créé `main.dart` et organisé vos fichiers dans les dossiers `core`, `data` et `ui` comme proposé dans son plan précédent.

C'est votre chance de faire une vérification de cohérence du code lui-même. Ouvrez `main.dart` pour vous assurer que l'agent a correctement configuré `WaterTrackerApp` et initialisé votre thème avant de passer à l'étape suivante du développement.

![Effectuez votre vérification de cohérence](https://cdn.hashnode.com/res/hashnode/image/upload/v1766783330487/83adf159-a017-40e6-9c93-299c243735ca.png align="center")

### Comprendre l'orchestration vs la vérification

Pour clarifier, dans Antigravity, la transition entre le Gestionnaire d'agents et le bouton Ouvrir l'éditeur (l'icône `< >`) représente un passage de l'**orchestration** à la **vérification** :

* **Vue du Gestionnaire d'agents (Orchestration)** : Lorsque vous cliquez sur **Ouvrir le Gestionnaire d'agents**, vous regardez le "centre de commande" pour les agents IA. Dans cette vue, vous voyez une interface de type terminal où l'agent propose des actions. Par exemple, comme vu dans votre capture d'écran, l'agent montre un "Step Requires Input" et attend que vous cliquiez sur Accepter pour une commande de terminal comme `flutter pub add`. Vous ne pouvez pas éditer de code ici – vous ne pouvez qu'approuver ou rejeter les opérations de terminal prévues par l'agent.

* **Vue de l'Éditeur (Vérification)** : Lorsque vous cliquez sur le bouton **'Ouvrir l'éditeur'** (l'icône `< >`) en haut à droite, l'IDE révèle l'espace de travail standard de style VS Code. C'est ici que les fichiers physiques (comme `main.dart` et la structure de dossiers que vous venez d'autoriser) apparaissent réellement. Alors que le Gestionnaire d'agents vous montre le *journal* de ce que l'agent a fait, la Vue de l'Éditeur vous permet d'ouvrir ces fichiers pour vérifier que le code suit vos normes et est prêt pour la production.

### Résumé du flux de travail

En bref : vous utilisez le Gestionnaire d'agents pour autoriser l'agent à exécuter des commandes de terminal et créer des dossiers, et vous cliquez sur le bouton 'Ouvrir l'éditeur' pour voir, explorer et éditer les fichiers résultants.

## Étape 3 : Implémenter l'écran principal Glassmorphic

Il est maintenant temps de créer la belle interface utilisateur. Le Glassmorphism repose sur le widget `BackdropFilter` et `ClipRRect` pour créer cet effet de "verre givré". Nous voulons un anneau de progression central qui montre la quantité d'eau que nous avons bue et qui semble physique et tactile.

Collez la demande suivante :

```markdown
Implémenter l'écran principal de suivi de l'eau avec un design glassmorphic.

Exigences détaillées :
- Grand anneau de progression circulaire central (style verre givré, arrière-plan flou visible à travers)
- Gros bouton "+" flottant avec effet de verre et lueur subtile au toucher
- Texte de consommation actuelle en grande police élégante
- Carte glassmorphic en dessous montrant "X verres · Y ml sur 2000 ml"
- Liste d'historique déroulante dans des cartes givrées
- État vide avec illustration/textes apaisants
- Animation de remplissage fluide sur l'anneau de progression lors de l'ajout d'eau

Avant de coder :
1. Planifier l'artefact avec :
   - Approche d'implémentation du Glassmorphism (BackdropFilter, ClipRRect, etc.)
   - Hiérarchie des widgets
   - Détails de l'animation
2. Demander l'approbation.

Après approbation :
- Générer le code
- Recharger à chaud
- Fournir une visite vidéo montrant :
   - Ajout d'eau plusieurs fois
   - Remplissage de l'anneau de progression avec effet de verre
   - Apparition des cartes d'historique
```

Si tout semble bon, approuvez le plan. L'agent devrait construire une interface glassmorphic époustouflante. Appuyez sur "+" et regardez l'anneau se remplir avec une animation soyeuse à travers le verre givré.

![Démonstration de l'animation](https://cdn.hashnode.com/res/hashnode/image/upload/v1766835614486/1930f868-07a9-4264-95cc-af48f163549f.png align="center")

## Étape 4 : Ajouter la persistance et la logique quotidienne

Une application n'est utile que si elle se souvient de vos données. Nous utiliserons `shared_preferences` pour un stockage local simple. Nous avons également besoin d'une logique qui vérifie la date actuelle et réinitialise le compteur à zéro à minuit.

Nous allons maintenant demander à l'agent d'ajouter la persistance et la logique de réinitialisation quotidienne en utilisant shared_preferences.

L'application doit sauvegarder la consommation et la date de la dernière réinitialisation. Avant de mettre en œuvre, expliquez comment la vérification de la réinitialisation à minuit sera déclenchée.

Utilisez cette demande :

```markdown
Ajouter la persistance et la réinitialisation quotidienne.

Exigences :
- Utiliser shared_preferences pour sauvegarder la consommation et la date de la dernière réinitialisation
- Réinitialisation automatique à 0 ml à minuit
- Conserver l'historique de la journée jusqu'à la réinitialisation
- Boîte de dialogue de paramètres simple pour changer l'objectif quotidien

Avant les modifications :
1. Planifier avec la logique de stockage et de réinitialisation
Demander l'approbation.

Après :
- Mettre en œuvre
- Tester la fermeture/réouverture de l'application
- Vidéo : ajouter de l'eau → fermer → rouvrir → les données persistent
```

Examinez la logique de l'agent pour la réinitialisation. Un piège courant est de ne vérifier la date que lorsque l'application est ouverte pour la première fois – assurez-vous donc que l'agent tient compte du fait que l'application reste ouverte en arrière-plan pendant la nuit.

Vos progrès survivent maintenant :

![Progrès sauvegardé](https://cdn.hashnode.com/res/hashnode/image/upload/v1766837605166/93c57ff2-c279-4897-b8b3-e2697b76064b.png align="center")

## Étape 5 : Ajouter des rappels intelligents sur l'appareil avec Gemma

La fonctionnalité la plus avancée de notre Water Tracker est le système de rappels intelligents alimenté par **Gemma 3n**. Contrairement aux rappels traditionnels qui utilisent un texte statique et répétitif, ces rappels sont générés dynamiquement pour garder l'utilisateur engagé et motivé. L'objectif principal de ces rappels est de suivre les progrès de l'utilisateur par rapport à son objectif d'hydratation quotidien et de fournir des encouragements personnalisés pour s'assurer qu'il reste sur la bonne voie tout au long de la journée.

Pour y parvenir, nous utiliserons Gemma 3n, qui est une variante spécialisée de la famille de modèles à poids ouverts de Google, conçue spécifiquement pour les performances sur l'appareil. Gemma 3n agit comme notre coach d'hydratation IA en analysant l'état actuel de la consommation de l'utilisateur. Par exemple, il remarque si un utilisateur n'a consommé que 500 ml sur son objectif de 2000 ml en milieu d'après-midi. Il utilise ensuite ce contexte pour générer un message amical et unique.

Nous utilisons Gemma 3n ici pour plusieurs raisons critiques :

* **Confidentialité et souveraineté des données** : Comme Gemma 3n fonctionne entièrement localement sur le téléphone de l'utilisateur, aucune donnée de santé personnelle ou habitudes quotidiennes ne quitte jamais l'appareil, offrant une expérience "privacy-first" où aucune donnée ne fuit vers le cloud.

* **Architecture de nouvelle génération** : Gemma 3n utilise la même architecture que le dernier Gemini Nano, ce qui lui permet d'offrir une vitesse et une efficacité incroyables tout en maintenant une empreinte minimale sur la batterie et la mémoire de l'appareil.

* **Support multimodal natif** : Ce modèle est unique car il dispose d'un support audio natif pour la première fois, ce qui signifie que, bien que nous l'utilisions actuellement pour les notifications textuelles, l'application est prête pour l'avenir pour la journalisation et l'interaction vocales.

Copiez et collez cette demande :

```markdown
Ajouter des rappels d'hydratation sur l'appareil en utilisant Gemma.

Exigences :
- Utiliser flutter_gemma ou un package similaire pour Gemma 3n
- Toutes les 2 heures, vérifier les progrès
- Si en retard sur le planning, afficher une notification locale : message amical et motivant comme "Il est temps pour un verre rafraîchissant ! Vous avez bu X sur Y ml aujourd'hui."
- Utiliser une invite simple sur l'appareil pour la variété
- Basculer dans les paramètres
- Badge de confidentialité : "Rappels alimentés localement"

Avant la mise en œuvre :
1. Planifier avec le package, la configuration des notifications et la logique de timing
Demander l'approbation.

Après :
- Mettre en œuvre
- Tester (simuler le temps ou attendre)
- Vidéo montrant l'apparition de la notification.
```

Vous devriez vérifier que l'agent ne fait pas d'appels fréquents et épuisant la batterie au modèle. Les rappels doivent être planifiés efficacement en utilisant des tâches en arrière-plan.

![Rappels avec Gemma](https://cdn.hashnode.com/res/hashnode/image/upload/v1766838947780/f051ad6e-383d-4965-ae41-dd939cb181c9.png align="center")

Pour tester le coach d'hydratation IA :

1. Allez dans Paramètres (icône d'engrenage).

2. Activez le bascule "Coach d'hydratation IA".

3. Vous devriez recevoir une notification simulée immédiatement avec un message motivant comme : *"Hydration Buddy 💦 : Restez hydraté ! Vous êtes à X% de votre objectif quotidien."*

## Étape 6 : Dernières retouches

Pour finaliser l'application, nous allons ajouter des micro-interactions – les petits détails qui donnent à une application un sentiment premium. Cela inclut une célébration avec des confettis lorsque l'objectif quotidien est atteint et une animation de vague pour l'état vide.

Utilisez cette demande :

```markdown
Ajouter les dernières retouches :
- Explosion de confettis lors de l'atteinte de 100% de l'objectif
- Écran de paramètres glassmorphic
- Meilleur état vide avec une animation de vague subtile
- Optimiser les performances

Mettre en œuvre une à la fois avec des mises à jour vidéo rapides.
```

Exécutez l'application sur votre téléphone. Ajoutez de l'eau tout au long de la journée et profitez de la beauté glassmorphic, des rappels doux et de la célébration lorsque vous atteignez votre objectif.

![Capture d'écran montrant diverses fonctionnalités de l'application comme la définition d'objectifs et la sauvegarde](https://cdn.hashnode.com/res/hashnode/image/upload/v1766840697130/8227c083-76af-4ab3-9b59-fd645e429dad.png align="center")

Ensuite, retournez à votre application et cliquez sur le bouton '+' pour obtenir les résultats. Après avoir obtenu un score de 100%, les confettis seront visibles :

![Montrant les confettis lorsque vous atteignez votre objectif](https://cdn.hashnode.com/res/hashnode/image/upload/v1766839488270/7e9f12ce-0d68-45e5-a01d-1634f367e311.png align="center")

### Examen des dernières modifications

Alors que l'agent travaille, utilisez le bouton **'Ouvrir l'éditeur'** (l'icône `< >`) pour inspecter les nouvelles animations. Lors de la vérification de l'optimisation des performances, recherchez l'utilisation par l'agent de `RepaintBoundary` autour des couches glassmorphic. C'est un indicateur clé que l'agent suit les normes de performance élevées de Flutter plutôt que d'écrire simplement du code basique.

Une fois que chaque micro-interaction est vérifiée, votre Water Tracker est prêt pour le grand public. Exécutez-le sur votre appareil, enregistrez votre consommation d'eau tout au long de la journée et profitez de la combinaison de la beauté glassmorphic, des rappels respectueux de la vie privée et de la célébration de vos objectifs de santé.

## **Limite de quota Antigravity**

Si votre modèle préféré vous notifie qu'il a atteint sa limite de quota, vous pouvez passer à un autre modèle avant que la limite ne se réinitialise. Comme vous pouvez le voir dans ma capture d'écran, mon Gemini 3 Pro préféré ne sera pas disponible avant 20h26, je vais donc sélectionner un autre modèle dans le menu déroulant pour l'utiliser avant cela.

![Sélection d'un autre modèle à utiliser](https://cdn.hashnode.com/res/hashnode/image/upload/v1766831055155/c04b71e6-2949-4294-aa9b-3c8df8511c19.png align="center")

## Conclusion

Dans ce tutoriel, vous avez construit une application utile de suivi des habitudes en utilisant le **développement agentique**.

Vous avez appris :

* La gestion des espaces de travail dans Antigravity

* L'écriture de demandes détaillées, planifiées en premier

* La création de designs glassmorphic

* L'intégration de l'IA sur l'appareil avec Gemma

* Le prototypage rapide et de haute qualité