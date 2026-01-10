---
title: Comment créer une IA adaptative de Morpion avec l'apprentissage par renforcement
  en JavaScript
subtitle: ''
author: Mayur Vekariya
co_authors: []
series: null
date: '2025-10-07T20:49:27.122Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-adaptive-tic-tac-toe-ai-with-reinforcement-learning-in-javascript
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1759870150966/f65a07a6-123b-45e2-a3f2-bc099638825a.png
tags:
- name: JavaScript
  slug: javascript
- name: AI
  slug: ai
- name: Reinforcement Learning
  slug: reinforcement-learning
- name: Artificial Intelligence
  slug: artificial-intelligence
seo_title: Comment créer une IA adaptative de Morpion avec l'apprentissage par renforcement
  en JavaScript
seo_desc: Reinforcement learning (RL) is one of the most powerful paradigms in artificial
  intelligence. Unlike supervised learning where you train models on labeled datasets,
  RL agents learn through direct interaction with their environment, receiving rewards
  ...
---

L'apprentissage par renforcement (Reinforcement Learning - RL) est l'un des paradigmes les plus puissants de l'intelligence artificielle. Contrairement à l'apprentissage supervisé où vous entraînez des modèles sur des ensembles de données étiquetés, les agents RL apprennent par interaction directe avec leur environnement, recevant des récompenses ou des pénalités pour leurs actions.

Dans ce tutoriel, vous allez construire une IA de Morpion (Tic-Tac-Toe) qui apprend des stratégies optimales grâce au Q-learning, un algorithme fondamental du RL. Vous implémenterez des niveaux de difficulté adaptatifs, visualiserez le processus d'apprentissage en temps réel et explorerez des techniques d'optimisation avancées.

À la fin de ce tutoriel, vous disposerez d'une application web prête pour la production qui démontre des concepts pratiques de RL – le tout s'exécutant directement dans le navigateur avec du JavaScript pur (vanilla).

## Ce que vous allez apprendre

Dans ce tutoriel, vous apprendrez :

* Les concepts de base de l'apprentissage par renforcement, notamment le Q-learning, l'exploration vs exploitation et le façonnement des récompenses (reward shaping).
    
* Comment implémenter un algorithme de Q-learning complet avec gestion d'état.
    
* Des techniques avancées comme la décroissance d'epsilon (epsilon decay) et le rejeu d'expérience (experience replay).
    
* Comment construire un jeu interactif avec l'API Canvas HTML5 et des contrôles réactifs.
    
* L'optimisation des performances pour la prise de décision de l'IA en temps réel.
    
* Des techniques de visualisation pour comprendre le processus d'apprentissage de l'IA.
    

## Prérequis

Pour tirer le meilleur parti de ce tutoriel, vous devriez avoir :

* Une solide compréhension de JavaScript (syntaxe ES6+, classes, méthodes de tableau).
    
* Une familiarité avec l'API Canvas HTML5 pour le rendu graphique.
    
* Des connaissances de base en algorithmes et structures de données.
    
* Une compréhension du JavaScript asynchrone (Promises, async/await).
    

Vous n'avez besoin d'aucune expérience préalable en machine learning, car j'expliquerai tous les concepts de RL à partir de zéro.

## Table des matières

* [Pourquoi utiliser l'apprentissage par renforcement pour l'IA de jeu ?](#heading-pourquoi-utiliser-l-apprentissage-par-renforcement-pour-l-ia-de-jeu)
    
* [Comprendre le Q-Learning : Les bases](#heading-comprendre-le-q-learning-les-bases)
    
* [Aperçu de l'architecture du projet](#heading-apercu-de-l-architecture-du-projet)
    
* [Comment construire l'interface HTML avec Tailwind CSS](#heading-comment-construire-l-interface-html-avec-tailwind-css)
    
* [Comment implémenter l'algorithme de Q-Learning](#heading-comment-implementer-l-algorithme-de-q-learning)
    
* [Comprendre les fonctionnalités améliorées](#heading-comprendre-les-fonctionnalites-ameliorees)
    
* [Comment tester votre implémentation](#heading-comment-tester-votre-implementation)
    
* [Optimisations avancées et extensions](#heading-optimisations-avancees-et-extensions)
    
* [Pièges courants et solutions](#heading-pieges-courants-et-solutions)
    
* [Comment étendre ceci à d'autres jeux](#heading-comment-etendre-ceci-a-d-autres-jeux)
    
* [Conclusion](#heading-conclusion)
    

## Pourquoi utiliser l'apprentissage par renforcement pour l'IA de jeu ?

Les jeux constituent un environnement idéal pour l'apprentissage du RL car ils possèdent :

1. **Des représentations d'état claires** – Le plateau de jeu à n'importe quel moment.
    
2. **Des espaces d'action discrets** – Un ensemble fini de coups valides.
    
3. **Un retour immédiat** – Résultats de victoire, défaite ou match nul.
    
4. **Des règles déterministes** – Comportement cohérent d'une partie à l'autre.
    

L'IA de jeu traditionnelle utilise des techniques comme le minimax avec élagage alpha-bêta. Bien qu'efficaces, ces approches nécessitent de programmer explicitement les stratégies de jeu. Les agents RL, en revanche, découvrent les stratégies optimales par l'expérience – tout comme les humains apprennent par la pratique.

Le Morpion est un excellent point de départ car :

* L'espace d'état est gérable (5 478 positions uniques).
    
* Les parties sont courtes, permettant une itération rapide.
    
* Un jeu parfait est réalisable, offrant une métrique de succès claire.
    
* Les concepts sont transposables à des jeux plus complexes.
    

## Comprendre le Q-Learning : Les bases

Le [Q-learning](https://www.freecodecamp.org/news/an-introduction-to-q-learning-reinforcement-learning-14ac0b4493cc/) est un algorithme de RL basé sur la valeur et sans modèle (model-free). Voici ce que cela signifie :

* **Sans modèle** signifie que l'agent n'a pas besoin de comprendre les règles du jeu. Il apprend purement par l'expérience.
    
* **Basé sur la valeur** signifie que l'agent apprend la « valeur » de chaque action dans chaque état, puis choisit l'action ayant la valeur la plus élevée.
    

### Composants clés

Il y a quelques composants clés que vous devrez comprendre avant de construire ce jeu.

Tout d'abord, nous avons l'**état (s)**, qui est ici la configuration actuelle du plateau de jeu. Nous le représentons par une chaîne de 9 caractères (par exemple, `"XO-X-----"` où `-` représente les cellules vides).

Ensuite, nous avons l'**action (a)**, qui est un coup que l'IA peut jouer. Nous le représentons par un index de 0 à 8 correspondant aux positions sur le plateau.

Puis il y a la **récompense (r)**, le retour numérique de l'environnement :

* `+1` pour une victoire
    
* `-1` pour une défaite
    
* `0` pour les matchs nuls ou les parties en cours
    

Nous avons également la **Table Q (Q-Table)**, une table de correspondance stockant Q(s,a) – la récompense cumulative attendue pour l'action `a` dans l'état `s`.

Et enfin, il y a la **politique (policy)**, la stratégie de choix des actions. Nous utilisons une politique epsilon-greedy qui équilibre l'exploration et l'exploitation.

### La règle de mise à jour du Q-Learning

Le cœur du Q-learning est cette formule de mise à jour :

```bash
Q(s,a) ← Q(s,a) + α[r + γ max Q(s',a') - Q(s,a)]
```

Où :

* `α` (alpha) = Taux d'apprentissage (0 à 1) – de combien mettre à jour la valeur Q.
    
* `γ` (gamma) = Facteur de remise (0 à 1) – quelle valeur accorder aux récompenses futures.
    
* `s'` = État suivant après avoir effectué l'action `a`.
    
* `max Q(s',a')` = Valeur Q la plus élevée disponible dans l'état suivant.
    

Cette formule implémente l'**apprentissage par différence temporelle (temporal difference learning)**. Cela signifie qu'elle met à jour notre estimation de Q(s,a) en fonction de la différence entre notre estimation actuelle et une meilleure estimation utilisant la récompense réelle reçue plus la meilleure récompense future possible.

### Comment fonctionne l'Exploration vs Exploitation

Un défi critique dans l'apprentissage par renforcement est le compromis « exploration vs exploitation ». Pour comprendre pourquoi c'est difficile, imaginez que vous choisissiez un endroit pour dîner.

* **Exploitation :** Vous pourriez aller à votre restaurant préféré. Vous savez que la nourriture est bonne et vous êtes presque assuré d'un repas satisfaisant. C'est un choix sûr et fiable qui maximise votre récompense immédiate basée sur l'expérience passée.
    
* **Exploration :** Vous pourriez essayer un nouveau restaurant inconnu. Cela pourrait être un désastre, ou vous pourriez découvrir un nouveau favori encore meilleur que l'ancien. C'est un choix risqué qui n'offre aucune garantie immédiate, mais c'est le seul moyen de recueillir de nouvelles informations et de trouver potentiellement une meilleure stratégie à long terme.
    

Le même dilemme s'applique à notre IA. Si elle n'exploite que ses connaissances actuelles, elle pourrait rester bloquée sur une stratégie médiocre, sans jamais découvrir les coups brillants qui mènent à une victoire garantie. Si elle ne fait qu'explorer en effectuant des mouvements aléatoires, elle n'apprendra jamais à utiliser les bonnes stratégies qu'elle trouve et jouera mal.

La clé est d'équilibrer les deux : explorer suffisamment pour trouver des stratégies optimales, mais exploiter ces connaissances pour gagner des parties.

Pour atteindre cet équilibre, nous utilisons une **stratégie epsilon-greedy (ϵ)**. C'est un moyen simple mais puissant de gérer ce compromis :

1. Nous choisissons une petite valeur pour epsilon (ϵ), par exemple 0,1 (ce qui représente une probabilité de 10 %).
    
2. Avant que l'IA ne joue, elle génère un nombre aléatoire entre 0 et 1.
    
3. **Si le nombre aléatoire est inférieur à ϵ (la chance de 10 %) :** L'IA ignore sa stratégie et choisit un coup aléatoire parmi ceux disponibles. C'est l'**exploration**.
    
4. **Si le nombre aléatoire est supérieur ou égal à ϵ (la chance de 90 %) :** L'IA choisit le meilleur coup connu dans sa table Q. C'est l'**exploitation**.
    

Cela garantit que l'IA joue principalement pour gagner, tout en consacrant une petite fraction de ses coups à essayer de nouvelles choses. Nous implémenterons également la **décroissance d'epsilon (epsilon decay)** – en commençant par une valeur ϵ plus élevée pour encourager l'exploration lorsque l'IA est inexpérimentée, et en la diminuant progressivement à mesure que l'IA apprend et devient plus confiante dans sa stratégie.

## Aperçu de l'architecture du projet

Avant de commencer à coder, voici la structure de l'application que vous allez construire :

```bash
tic-tac-toe-ai/
├── index.html          # Interface du jeu avec Tailwind CSS
└── game.js            # Logique complète du jeu et de l'IA
```

Vous organiserez votre code en deux classes principales dans game.js :

1. **QLearning** : Implémente l'algorithme de Q-learning.
    
2. **TicTacToe** : Gère l'état du jeu et le rendu.
    

## Comment construire l'interface HTML avec Tailwind CSS

Créez un fichier `index.html` avec le CDN Tailwind CSS :

```xml
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IA de Morpion avec Q-Learning</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-br from-purple-600 to-purple-900 min-h-screen flex items-center justify-center p-4">
  
  <div class="bg-white rounded-3xl shadow-2xl p-8 max-w-5xl w-full">
    <!-- Header -->
    <div class="text-center mb-8">
      <h1 class="text-4xl font-bold text-gray-800 mb-2">🎮 IA de Morpion</h1>
      <p class="text-gray-600 text-lg">Regardez l'IA apprendre via l'apprentissage par renforcement</p>
    </div>

    <!-- Training Indicator -->
    <div id="trainingIndicator" class="hidden bg-yellow-100 border-l-4 border-yellow-500 text-yellow-700 p-4 mb-6 rounded">
      <p class="font-semibold">🤖 L'IA s'entraîne... <span id="trainingProgress"></span></p>
    </div>

    <!-- Main Game Area -->
    <div class="grid md:grid-cols-2 gap-8">
      
      <!-- Canvas Section -->
      <div class="flex flex-col items-center">
        <canvas id="gameCanvas" width="400" height="400" 
                class="border-4 border-purple-500 rounded-xl shadow-lg cursor-pointer hover:scale-[1.02] transition-transform">
        </canvas>
        <div id="gameStatus" class="mt-4 text-xl font-bold text-gray-700 min-h-[30px]">
          À vous de jouer ! (X)
        </div>
      </div>

      <!-- Controls Section -->
      <div class="space-y-6">
        
        <!-- Game Controls -->
        <div class="bg-gray-50 rounded-xl p-6">
          <h3 class="text-xl font-bold text-gray-800 mb-4">Contrôles du jeu</h3>
          <div class="space-y-3">
            <button onclick="game.reset()" 
                    class="w-full bg-purple-600 hover:bg-purple-700 text-white font-semibold py-3 px-6 rounded-lg transition-all hover:-translate-y-0.5 shadow-md hover:shadow-lg">
              Nouvelle partie
            </button>
            <button onclick="game.startTraining()" 
                    class="w-full bg-green-600 hover:bg-green-700 text-white font-semibold py-3 px-6 rounded-lg transition-all hover:-translate-y-0.5 shadow-md hover:shadow-lg">
              Entraîner l'IA (1000 parties)
            </button>
            <button onclick="game.resetAI()" 
                    class="w-full bg-red-600 hover:bg-red-700 text-white font-semibold py-3 px-6 rounded-lg transition-all hover:-translate-y-0.5 shadow-md hover:shadow-lg">
              Réinitialiser la mémoire de l'IA
            </button>
          </div>
        </div>

        <!-- Difficulty Selector -->
        <div class="bg-gray-50 rounded-xl p-6">
          <h3 class="text-xl font-bold text-gray-800 mb-4">Niveau de difficulté</h3>
          <div class="grid grid-cols-3 gap-2">
            <button onclick="game.setDifficulty('beginner')" id="diffBeginner"
                    class="py-2 px-4 rounded-lg font-semibold text-sm transition-all bg-green-100 text-green-700 hover:bg-green-200">
              🌱 Débutant
            </button>
            <button onclick="game.setDifficulty('intermediate')" id="diffIntermediate"
                    class="py-2 px-4 rounded-lg font-semibold text-sm transition-all bg-white text-gray-700 hover:bg-gray-100 border-2 border-purple-500">
              🎯 Moyen
            </button>
            <button onclick="game.setDifficulty('expert')" id="diffExpert"
                    class="py-2 px-4 rounded-lg font-semibold text-sm transition-all bg-white text-gray-700 hover:bg-gray-100">
              🔥 Expert
            </button>
          </div>
        </div>

        <!-- AI Parameters -->
        <div class="bg-gray-50 rounded-xl p-6">
          <h3 class="text-xl font-bold text-gray-800 mb-4">Paramètres de l'IA</h3>
          
          <div class="space-y-4">
            <!-- Learning Rate -->
            <div>
              <div class="flex justify-between items-center mb-2">
                <label class="text-sm font-medium text-gray-700 flex items-center gap-1">
                  Taux d'apprentissage (α)
                  <span class="group relative">
                    <span class="cursor-help text-purple-500">ⓘ</span>
                    <span class="invisible group-hover:visible absolute left-0 top-6 w-64 bg-gray-900 text-white text-xs rounded-lg p-3 z-10 shadow-xl">
                      Contrôle la rapidité avec laquelle l'IA met à jour ses connaissances. Valeurs élevées = apprentissage plus rapide mais moins de stabilité. Recommandé : 0.1-0.3
                    </span>
                  </span>
                </label>
                <span id="learningRateValue" class="text-sm font-bold text-purple-600">0.1</span>
              </div>
              <input type="range" id="learningRate" min="0.01" max="0.5" step="0.01" value="0.1"
                     class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer">
            </div>

            <!-- Discount Factor -->
            <div>
              <div class="flex justify-between items-center mb-2">
                <label class="text-sm font-medium text-gray-700 flex items-center gap-1">
                  Facteur de remise (γ)
                  <span class="group relative">
                    <span class="cursor-help text-purple-500">ⓘ</span>
                    <span class="invisible group-hover:visible absolute left-0 top-6 w-64 bg-gray-900 text-white text-xs rounded-lg p-3 z-10 shadow-xl">
                      Détermine l'importance que l'IA accorde aux récompenses futures par rapport aux récompenses immédiates. Élevé = vision à plus long terme. Recommandé : 0.85-0.95
                    </span>
                  </span>
                </label>
                <span id="discountFactorValue" class="text-sm font-bold text-purple-600">0.9</span>
              </div>
              <input type="range" id="discountFactor" min="0.5" max="0.99" step="0.01" value="0.9"
                     class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer">
            </div>

            <!-- Exploration Rate -->
            <div>
              <div class="flex justify-between items-center mb-2">
                <label class="text-sm font-medium text-gray-700 flex items-center gap-1">
                  Taux d'exploration (ε)
                  <span class="group relative">
                    <span class="cursor-help text-purple-500">ⓘ</span>
                    <span class="invisible group-hover:visible absolute left-0 top-6 w-64 bg-gray-900 text-white text-xs rounded-lg p-3 z-10 shadow-xl">
                      Probabilité que l'IA tente des coups aléatoires plutôt que d'utiliser sa stratégie apprise. Élevé = plus d'expérimentation. Réglez sur 0.01 pour un jeu optimal après l'entraînement.
                    </span>
                  </span>
                </label>
                <span id="explorationRateValue" class="text-sm font-bold text-purple-600">0.1</span>
              </div>
              <input type="range" id="explorationRate" min="0" max="0.5" step="0.01" value="0.1"
                     class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer">
            </div>
          </div>
        </div>

        <!-- Statistics -->
        <div class="bg-gray-50 rounded-xl p-6">
          <h3 class="text-xl font-bold text-gray-800 mb-4">Statistiques</h3>
          <div class="grid grid-cols-3 gap-3">
            <div class="bg-white rounded-lg p-3 text-center shadow-sm">
              <div class="text-xs text-gray-600 mb-1">Parties</div>
              <div id="gamesPlayed" class="text-2xl font-bold text-gray-800">0</div>
            </div>
            <div class="bg-white rounded-lg p-3 text-center shadow-sm">
              <div class="text-xs text-gray-600 mb-1">IA Gagne</div>
              <div id="aiWins" class="text-2xl font-bold text-green-600">0</div>
            </div>
            <div class="bg-white rounded-lg p-3 text-center shadow-sm">
              <div class="text-xs text-gray-600 mb-1">Vous Gagnez</div>
              <div id="playerWins" class="text-2xl font-bold text-red-600">0</div>
            </div>
            <div class="bg-white rounded-lg p-3 text-center shadow-sm">
              <div class="text-xs text-gray-600 mb-1">Nuls</div>
              <div id="draws" class="text-2xl font-bold text-gray-600">0</div>
            </div>
            <div class="bg-white rounded-lg p-3 text-center shadow-sm">
              <div class="text-xs text-gray-600 mb-1">États appris</div>
              <div id="statesLearned" class="text-2xl font-bold text-purple-600">0</div>
            </div>
            <div class="bg-white rounded-lg p-3 text-center shadow-sm">
              <div class="text-xs text-gray-600 mb-1">Taux de vict.</div>
              <div id="winRate" class="text-2xl font-bold text-blue-600">0%</div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>

  <script src="game.js"></script>
</body>
</html>
```

Cette structure HTML crée une interface moderne et réactive en utilisant les classes utilitaires de Tailwind CSS. La mise en page utilise une grille à deux colonnes sur les écrans moyens et plus grands, avec le canvas du jeu à gauche et tous les contrôles à droite. L'indicateur d'entraînement est initialement masqué et n'apparaît que pendant les sessions d'entraînement de l'IA.

Tous les éléments interactifs (boutons, curseurs) utilisent des gestionnaires `onclick` et des événements `oninput` pour communiquer avec la logique du jeu en JavaScript. Le système d'infobulles utilise les états de survol de groupe CSS pour afficher du texte explicatif lorsque les utilisateurs survolent les icônes d'information, les aidant à comprendre chaque paramètre sans encombrer l'interface.

Parlons un peu plus en détail de certaines parties clés du code :

* **Section d'en-tête** : Affiche le titre et le sous-titre du jeu pour présenter l'application aux utilisateurs.
    
* **Indicateur d'entraînement** : Une bannière jaune qui n'apparaît que pendant les sessions d'entraînement de l'IA, affichant les mises à jour de progression toutes les 50 parties. Cela fournit un retour visuel pour que les utilisateurs sachent que l'entraînement est en cours.
    
* **Section Canvas** : Contient l'élément Canvas HTML5 où le plateau de jeu est dessiné. Le canvas fait 400x400 pixels et est stylisé avec des classes Tailwind pour les bordures et les effets de survol. En dessous se trouve un message d'état qui se met à jour en fonction de l'état du jeu.
    
* **Contrôles du jeu** : Trois boutons principaux qui permettent aux utilisateurs de commencer une nouvelle partie, d'entraîner l'IA via 1000 parties en auto-jeu, ou de réinitialiser complètement la mémoire de l'IA (effacement de la table Q).
    
* **Sélecteur de difficulté** : Trois boutons pour choisir la difficulté de l'IA. Le mode Débutant fait jouer l'IA de manière aléatoire 70 % du temps, le mode Moyen utilise le Q-learning, et le mode Expert implémente un jeu minimax parfait.
    
* **Paramètres de l'IA** : Trois curseurs de plage avec des infobulles qui permettent aux utilisateurs d'ajuster les hyperparamètres de base de l'apprentissage par renforcement en temps réel.
    
* **Panneau de statistiques** : Une grille de six cartes affichant des métriques en temps réel, notamment les parties jouées, les victoires/défaites/nuls, les états appris et le pourcentage de victoires de l'IA.

## Comment implémenter l'algorithme de Q-Learning

Maintenant, donnons vie à la théorie. Créez un fichier `game.js`. Nous allons construire ce fichier étape par étape, mais si vous êtes bloqué à un moment donné ou si vous voulez voir le code complet pour référence, vous pouvez trouver la version finale [sur **GitHub** ici](https://github.com/mayur9210/tic-tac-toe-ai/blob/main/game.js).

Notre code sera structuré en deux classes principales : `QLearning`, qui gérera le « cerveau » de l'IA et la logique d'apprentissage, et `TicTacToe`, qui gérera l'état du jeu, le rendu et l'interaction avec l'utilisateur.

### La classe `QLearning` : Le cerveau de l'IA

Cette classe contiendra toute la logique de l'[agent d'apprentissage par renforcement](https://github.com/mayur9210/tic-tac-toe-ai/blob/main/game.js). Construisons-la morceau par morceau.

#### 1. Constructeur et gestion de la Table Q

Tout d'abord, configurons le `constructor` et une méthode pour accéder à notre table Q. La table Q sera un `Map` JavaScript, ce qui est très efficace pour stocker et récupérer des paires clé-valeur où la clé (l'état du plateau) est une chaîne de caractères.

```javascript
// Dans game.js

// Agent Q-Learning avec support localStorage
class QLearning {
  constructor(lr = 0.1, gamma = 0.9, epsilon = 0.1) {
    this.q = new Map(); // Stocke les valeurs Q : { état => [q_action_0, q_action_1, ...] }
    this.lr = lr; // Taux d'apprentissage (α)
    this.gamma = gamma; // Facteur de remise (γ)
    this.epsilon = epsilon; // Taux d'exploration (ε)
    this.difficulty = 'intermediate';
  }

  getQ(state) {
    if (!this.q.has(state)) {
      this.q.set(state, Array(9).fill(0));
    }
    return this.q.get(state);
  }
```

* Le `constructor` initialise nos trois hyperparamètres clés (α, γ, ε) et la table Q elle-même.
    
* `getQ(state)` est une fonction utilitaire cruciale. Elle récupère en toute sécurité le tableau des valeurs Q pour un état de plateau donné. Si l'IA n'a jamais vu cet état auparavant, elle crée une nouvelle entrée dans la map avec un tableau de neuf zéros, représentant une valeur Q initiale de 0 pour chaque coup possible.
    

#### 2. Choisir une action (La stratégie Epsilon-Greedy)

Ensuite, nous allons implémenter la méthode `getAction`. C'est ici que l'IA décide quel coup jouer, en intégrant nos niveaux de difficulté et la stratégie epsilon-greedy.

```javascript
  getAction(state, available) {
    // Comportement basé sur la difficulté
    if (this.difficulty === 'beginner') {
      // 70% de coups aléatoires pour le débutant
      if (Math.random() < 0.7) {
        return available[~~(Math.random() * available.length)];
      }
    } else if (this.difficulty === 'expert') {
      // Utilise minimax pour un jeu parfait
      return this.getMinimaxAction(state, available);
    }

    // Intermédiaire : epsilon-greedy
    if (Math.random() < this.epsilon) {
      return available[~~(Math.random() * available.length)];
    }
    const q = this.getQ(state);
    return available.reduce((best, a) => q[a] > q[best] ? a : best, available[0]);
  }
```

* La logique vérifie d'abord la difficulté. 'Beginner' est principalement aléatoire, tandis qu' 'Expert' s'en remet à un algorithme de jeu parfait séparé.
    
* Pour le niveau 'Intermediate', elle implémente la logique epsilon-greedy. Avec une probabilité ε, elle explore (choisit un coup aléatoire). Sinon, elle exploite (choisit le meilleur coup connu dans la table Q).
    

#### 3. La règle d'apprentissage

La méthode `update` est le cœur de l'algorithme. C'est l'implémentation directe de la formule de Q-learning dont nous avons discuté plus tôt.

*Q(s, a) ← Q(s, a) + α [r + γ max(a') Q(s', a') − Q(s, a)]*

```javascript
  update(s, a, r, s2, available2) {
    const q = this.getQ(s);
    const maxQ2 = available2.length ? Math.max(...available2.map(a_prime => this.getQ(s2)[a_prime])) : 0;
    q[a] += this.lr * (r + this.gamma * maxQ2 - q[a]);
  }
```

* `maxQ2` calcule la partie `max Q(s',a')` de la formule – la meilleure valeur Q possible que l'IA peut obtenir lors de son prochain coup.
    
* La dernière ligne est une traduction directe de la formule, mettant à jour la valeur de l'action qui vient d'être effectuée en fonction de la récompense et du potentiel futur.
    

#### 4. Minimax pour le mode Expert

Pour notre niveau 'Expert', nous allons implémenter l'algorithme minimax, un algorithme récursif classique de la théorie des jeux qui garantit un jeu parfait.

```javascript
  getMinimaxAction(state, available) {
    let bestScore = -Infinity;
    let bestMove = available[0];

    for (const move of available) {
      const newState = state.substring(0, move) + 'O' + state.substring(move + 1);
      const score = this.minimax(newState, 0, false);
      if (score > bestScore) {
        bestScore = score;
        bestMove = move;
      }
    }
    return bestMove;
  }

  minimax(state, depth, isMaximizing) {
    const winner = this.checkWinnerStatic(state);
    if (winner === 'O') return 10 - depth;
    if (winner === 'X') return depth - 10;
    if (winner === 'draw') return 0;

    const available = [...state].map((c, i) => c === '-' ? i : null).filter(x => x !== null);
    
    if (isMaximizing) {
      let best = -Infinity;
      for (const move of available) {
        const newState = state.substring(0, move) + 'O' + state.substring(move + 1);
        best = Math.max(best, this.minimax(newState, depth + 1, false));
      }
      return best;
    } else {
      let best = Infinity;
      for (const move of available) {
        const newState = state.substring(0, move) + 'X' + state.substring(move + 1);
        best = Math.min(best, this.minimax(newState, depth + 1, true));
      }
      return best;
    }
  }

  checkWinnerStatic(state) {
    const patterns = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
    for (const p of patterns) {
      if (state[p[0]] !== '-' && state[p[0]] === state[p[1]] && state[p[1]] === state[p[2]]) {
        return state[p[0]];
      }
    }
    return state.includes('-') ? null : 'draw';
  }
```

#### 5. Méthodes utilitaires et de persistance

Enfin, ajoutons des méthodes pour la décroissance d'epsilon, la réinitialisation de la mémoire de l'IA et la sauvegarde/chargement de la table Q dans le `localStorage`.

```javascript
  decay() {
    this.epsilon = Math.max(0.01, this.epsilon * 0.995);
  }

  reset() {
    this.q.clear();
    this.epsilon = 0.1;
  }

  save() {
    const data = {
      q: Array.from(this.q.entries()),
      lr: this.lr,
      gamma: this.gamma,
      epsilon: this.epsilon,
      difficulty: this.difficulty
    };
    localStorage.setItem('tictactoe_ai', JSON.stringify(data));
  }

  load() {
    const saved = localStorage.getItem('tictactoe_ai');
    if (!saved) return false;
    
    try {
      const data = JSON.parse(saved);
      this.q = new Map(data.q);
      this.lr = data.lr;
      this.gamma = data.gamma;
      this.epsilon = data.epsilon;
      this.difficulty = data.difficulty || 'intermediate';
      return true;
    } catch (e) {
      console.error('Échec du chargement de l\'état de l\'IA :', e);
      return false;
    }
  }

  clearStorage() {
    localStorage.removeItem('tictactoe_ai');
  }
}
```

### La classe `TicTacToe` : Gérer le jeu

Maintenant que nous avons notre « cerveau » d'IA, nous devons construire le jeu autour. Cette classe gérera le rendu du plateau, le traitement des clics de l'utilisateur, le flux du jeu et l'appel de l'IA quand c'est son tour.

#### 1. Constructeur et initialisation des contrôles

Le constructeur configure l'état initial du jeu, obtient une référence au canvas HTML et connecte les écouteurs d'événements pour les entrées utilisateur.

```javascript
class TicTacToe {
  constructor() {
    this.board = '---------';
    this.ai = new QLearning();
    this.stats = { played: 0, aiWins: 0, playerWins: 0, draws: 0 };
    this.training = false;
    this.gameOver = false;

    this.canvas = document.getElementById('gameCanvas');
    this.ctx = this.canvas.getContext('2d');
    this.cellSize = 133.33;

    this.canvas.onclick = e => this.handleClick(e);
    this.initControls();
    this.loadState();
    this.draw();
  }

  initControls() {
    ['learningRate', 'discountFactor', 'explorationRate'].forEach(id => {
      const el = document.getElementById(id);
      el.oninput = e => {
        const val = parseFloat(e.target.value);
        document.getElementById(id + 'Value').textContent = val.toFixed(2);
        if (id === 'learningRate') this.ai.lr = val;
        if (id === 'discountFactor') this.ai.gamma = val;
        if (id === 'explorationRate') this.ai.epsilon = val;
        this.saveState();
      };
    });
  }
```

`initControls` connecte nos curseurs HTML aux paramètres de l'IA, permettant des ajustements en temps réel.

#### 2. Méthodes de difficulté et d'interface utilisateur

Ces méthodes gèrent le réglage de la difficulté et mettent à jour l'interface utilisateur en conséquence.

```javascript
  setDifficulty(level) {
    this.ai.difficulty = level;
    
    // Mise à jour des styles de boutons
    ['beginner', 'intermediate', 'expert'].forEach(diff => {
      const btn = document.getElementById(`diff${diff.charAt(0).toUpperCase() + diff.slice(1)}`);
      if (diff === level) {
        btn.className = 'py-2 px-4 rounded-lg font-semibold text-sm transition-all bg-purple-600 text-white border-2 border-purple-600';
      } else {
        btn.className = 'py-2 px-4 rounded-lg font-semibold text-sm transition-all bg-white text-gray-700 hover:bg-gray-100';
      }
    });

    if (level === 'beginner') this.setStatus('🌱 Mode Débutant : l\'IA fait plus d\'erreurs');
    else if (level === 'intermediate') this.setStatus('🎯 Mode Moyen : IA équilibrée utilisant le Q-learning');
    else this.setStatus('🔥 Mode Expert : IA parfaite utilisant l\'algorithme minimax');

    this.saveState();
  }
```

#### 3. Dessin et rendu

Ces méthodes utilisent l'API Canvas HTML5 pour représenter visuellement l'état du jeu.

```javascript
  draw() {
    const { ctx, canvas, cellSize } = this;
    ctx.fillStyle = '#fff';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.strokeStyle = '#8b5cf6';
    ctx.lineWidth = 4;
    for (let i = 1; i < 3; i++) {
      ctx.beginPath();
      ctx.moveTo(i * cellSize, 0);
      ctx.lineTo(i * cellSize, canvas.height);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(0, i * cellSize);
      ctx.lineTo(canvas.width, i * cellSize);
      ctx.stroke();
    }

    for (let i = 0; i < 9; i++) {
      const symbol = this.board[i];
      if (symbol === '-') continue;
      
      const x = (i % 3) * cellSize + cellSize / 2;
      const y = ~~(i / 3) * cellSize + cellSize / 2;
      
      ctx.strokeStyle = symbol === 'X' ? '#ef4444' : '#10b981';
      ctx.lineWidth = 8;
      ctx.lineCap = 'round';

      if (symbol === 'X') {
        const s = cellSize * 0.3;
        ctx.beginPath();
        ctx.moveTo(x - s, y - s);
        ctx.lineTo(x + s, y + s);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(x + s, y - s);
        ctx.lineTo(x - s, y + s);
        ctx.stroke();
      } else {
        ctx.beginPath();
        ctx.arc(x, y, cellSize * 0.3, 0, Math.PI * 2);
        ctx.stroke();
      }
    }

    const winner = this.checkWinner();
    if (winner?.line) this.drawWinLine(winner.line);
  }

  drawWinLine(line) {
    const [a, , c] = line;
    const startX = (a % 3) * this.cellSize + this.cellSize / 2;
    const startY = ~~(a / 3) * this.cellSize + this.cellSize / 2;
    const endX = (c % 3) * this.cellSize + this.cellSize / 2;
    const endY = ~~(c / 3) * this.cellSize + this.cellSize / 2;

    this.ctx.strokeStyle = '#fbbf24';
    this.ctx.lineWidth = 6;
    this.ctx.beginPath();
    this.ctx.moveTo(startX, startY);
    this.ctx.lineTo(endX, endY);
    this.ctx.stroke();
  }
```

#### 4. Interaction du joueur et boucle de jeu

C'est la logique interactive centrale. `handleClick` traduit un clic en une position sur le plateau, `move` met à jour l'état, et `aiMove` obtient une action de la classe `QLearning` et l'exécute.

```javascript
  handleClick(e) {
    if (this.gameOver || this.training) return;
    
    const rect = this.canvas.getBoundingClientRect();
    const col = ~~((e.clientX - rect.left) / this.cellSize);
    const row = ~~((e.clientY - rect.top) / this.cellSize);
    const idx = row * 3 + col;

    if (this.board[idx] === '-') {
      this.move(idx, 'X');
      if (!this.gameOver) setTimeout(() => this.aiMove(), 300);
    }
  }

  move(idx, player) {
    if (this.board[idx] !== '-' || this.gameOver) return false;
    this.board = this.board.substring(0, idx) + player + this.board.substring(idx + 1);
    this.draw();
    this.checkGameOver();
    return true;
  }

  aiMove() {
    if (this.gameOver) return;
    
    const state = this.board;
    const available = this.getAvailable();
    const action = this.ai.getAction(state, available);
    
    this.move(action, 'O');
    
    const winner = this.checkWinner();
    const reward = winner?.winner === 'O' ? 1 : winner?.winner === 'X' ? -1 : 0;
    this.ai.update(state, action, reward, this.board, this.getAvailable());
  }
```

Après le mouvement de l'IA, elle appelle immédiatement `this.ai.update()` pour apprendre du résultat de son action.

#### 5. Le moteur de règles

Ces utilitaires déterminent l'état du jeu : coups disponibles, gagnant et conditions de fin de partie.

```javascript
  getAvailable() {
    return [...this.board].map((c, i) => c === '-' ? i : null).filter(x => x !== null);
  }

  checkWinner() {
    const patterns = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
    for (const p of patterns) {
      if (this.board[p[0]] !== '-' && 
          this.board[p[0]] === this.board[p[1]] && 
          this.board[p[1]] === this.board[p[2]]) {
        return { winner: this.board[p[0]], line: p };
      }
    }
    return this.board.includes('-') ? null : { winner: 'draw', line: null };
  }

  checkGameOver() {
    const result = this.checkWinner();
    if (!result) return;

    this.gameOver = true;
    this.stats.played++;

    if (result.winner === 'X') {
      this.stats.playerWins++;
      if (!this.training) this.setStatus('🎉 Vous avez gagné !');
    } else if (result.winner === 'O') {
      this.stats.aiWins++;
      if (!this.training) this.setStatus('🤖 L\'IA a gagné !');
    } else {
      this.stats.draws++;
      if (!this.training) this.setStatus('🤝 Match nul !');
    }

    if (!this.training) {
      this.updateStats();
      this.saveState();
    }
  }
```

#### 6. Mises à jour de l'interface utilisateur et des statistiques

Ces méthodes connectent l'état interne du jeu aux éléments HTML, affichant les messages d'état et les statistiques.

```javascript
  setStatus(msg) {
    document.getElementById('gameStatus').textContent = msg;
  }

  updateStats() {
    document.getElementById('gamesPlayed').textContent = this.stats.played;
    document.getElementById('aiWins').textContent = this.stats.aiWins;
    document.getElementById('playerWins').textContent = this.stats.playerWins;
    document.getElementById('draws').textContent = this.stats.draws;
    document.getElementById('statesLearned').textContent = this.ai.q.size;
    
    const winRate = this.stats.played ? (this.stats.aiWins / this.stats.played * 100).toFixed(1) : 0;
    document.getElementById('winRate').textContent = `${winRate}%`;
  }
```

#### 7. Gestion du jeu et de l'IA

Ces méthodes sont reliées aux boutons de contrôle pour réinitialiser le jeu ou la mémoire de l'IA.

```javascript
  reset() {
    this.board = '---------';
    this.gameOver = false;
    this.draw();
    this.setStatus('À vous de jouer ! (X)');
  }

  resetAI() {
    if (confirm('Réinitialiser la mémoire de l\'IA ? Tous les progrès seront perdus.')) {
      this.ai.reset();
      this.ai.clearStorage();
      this.stats = { played: 0, aiWins: 0, playerWins: 0, draws: 0 };
      this.updateStats();
      this.reset();
      this.setStatus('Mémoire de l\'IA réinitialisée !');
      localStorage.removeItem('tictactoe_stats');
    }
  }
```

#### 8. La boucle d'entraînement en auto-jeu

C'est la logique du bouton « Entraîner l'IA », permettant à l'IA d'apprendre rapidement en jouant contre elle-même.

```javascript
  async startTraining() {
    this.training = true;
    document.getElementById('trainingIndicator').classList.remove('hidden');
    
    const originalEpsilon = this.ai.epsilon;
    this.ai.epsilon = 0.3; // Plus d'exploration pendant l'entraînement

    for (let i = 0; i < 1000; i++) {
      await this.trainGame();
      this.ai.decay();
      if (i % 50 === 0) {
        document.getElementById('trainingProgress').textContent = `${i + 1}/1000`;
        await new Promise(r => setTimeout(r, 0)); // Permet à l'UI de se mettre à jour
      }
    }

    this.ai.epsilon = originalEpsilon;
    this.training = false;
    document.getElementById('trainingIndicator').classList.add('hidden');
    this.updateStats();
    this.reset();
    this.setStatus('Entraînement terminé !');
    this.saveState();
  }

  async trainGame() {
    this.board = '---------';
    this.gameOver = false;
    const moves = [];

    while (!this.gameOver && this.getAvailable().length > 0) {
      const state = this.board;
      const available = this.getAvailable();
      // Les joueurs alternés (X et O) sont tous deux l'IA
      const player = moves.length % 2 === 0 ? 'X' : 'O'; 
      const action = this.ai.getAction(state, available);
      
      moves.push({ state, action, player });
      this.move(action, player);
    }

    const winner = this.checkWinner();
    // Assigner les récompenses après la fin de la partie
    moves.forEach(m => {
      const reward = winner?.winner === m.player ? 1 : (winner?.winner && winner.winner !== m.player) ? -1 : 0;
      this.ai.update(m.state, m.action, reward, this.board, []);
    });
  }
```

#### 9. Persistance de l'état

Ces méthodes orchestrent la sauvegarde et le chargement de l'état du jeu et de la mémoire de l'IA dans le `localStorage`.

```javascript
  saveState() {
    this.ai.save();
    localStorage.setItem('tictactoe_stats', JSON.stringify(this.stats));
  }

  loadState() {
    if (this.ai.load()) {
      const savedStats = localStorage.getItem('tictactoe_stats');
      if (savedStats) {
        this.stats = JSON.parse(savedStats);
      }
      this.updateStats();
      this.setDifficulty(this.ai.difficulty);
      
      // Mettre à jour les curseurs pour refléter l'état chargé de l'IA
      document.getElementById('learningRate').value = this.ai.lr;
      document.getElementById('learningRateValue').textContent = this.ai.lr.toFixed(2);
      document.getElementById('discountFactor').value = this.ai.gamma;
      document.getElementById('discountFactorValue').textContent = this.ai.gamma.toFixed(2);
      document.getElementById('explorationRate').value = this.ai.epsilon;
      document.getElementById('explorationRateValue').textContent = this.ai.epsilon.toFixed(2);
      
      console.log('✓ État de l\'IA chargé depuis le localStorage');
    }
  }
}
```

#### 10. Initialisation du jeu

Enfin, ajoutez cet extrait à la fin de `game.js` pour créer une instance du jeu une fois le document HTML chargé.

```javascript
let game;
window.addEventListener('DOMContentLoaded', () => {
  game = new TicTacToe();
});
```

Ceci complète notre implémentation ! Vous avez maintenant un fichier `game.js` entièrement fonctionnel. Si vous avez rencontré des problèmes ou si vous voulez vérifier votre travail, vous pouvez comparer votre code avec le fichier source complet disponible sur GitHub : [https://github.com/mayur9210/tic-tac-toe-ai/blob/main/game.js](https://github.com/mayur9210/tic-tac-toe-ai/blob/main/game.js).

## Comprendre les fonctionnalités améliorées

Au-delà de la logique de base du Q-learning, cette implémentation inclut plusieurs fonctionnalités améliorées pour créer une application complète, conviviale et éducative. Explorons ce qu'elles sont et comment elles fonctionnent.

### 1. Niveaux de difficulté adaptatifs

Le jeu prend en charge trois modes de difficulté distincts pour s'adapter aux différents joueurs :

* **Débutant (🌱) :** Ce mode est conçu pour les nouveaux joueurs. L'IA effectue des coups aléatoires 70 % du temps, offrant une grande chance au joueur de gagner et d'apprendre les règles du jeu.
    
* **Moyen (🎯) :** C'est le mode standard où l'IA utilise l'algorithme de Q-learning avec une stratégie epsilon-greedy. Elle présente un adversaire stimulant mais équitable qui s'améliore avec le temps.
    
* **Expert (🔥) :** Ce mode passe de l'apprentissage par renforcement à l'algorithme classique **minimax**. Cet algorithme joue une partie parfaite, ce qui signifie qu'il est impossible à battre (le mieux qu'un joueur puisse obtenir est un match nul). Cela sert de référence pour un jeu optimal.
    

### 2. Autres fonctionnalités améliorées

En plus des niveaux de difficulté, l'application comprend :

* **Réglage des paramètres de l'IA en temps réel :** Les curseurs de l'interface utilisateur vous permettent d'ajuster le taux d'apprentissage (α), le facteur de remise (γ) et le taux d'exploration (ε) à la volée. Cela vous permet d'observer directement comment différents hyperparamètres affectent la vitesse d'apprentissage et les performances de l'IA.
    
* **Persistance avec localStorage :** L'IA sauvegarde automatiquement sa table Q et vos statistiques de jeu dans le stockage local du navigateur. Lorsque vous fermez l'onglet et revenez plus tard, l'IA se souviendra de tout ce qu'elle a appris.
    
* **Mode d'entraînement dédié en auto-jeu :** Le bouton « Entraîner l'IA » permet à l'IA de jouer 1 000 parties contre elle-même en quelques secondes. Cela remplit rapidement la table Q et est bien plus efficace que d'apprendre uniquement à partir de parties jouées par des humains.
    

## Mise en pratique : Un test guidé

Une fois que vous avez les fichiers HTML (`index.html`) et JavaScript (`game.js`) dans le même répertoire, ouvrez le fichier HTML dans un navigateur web pour tester toutes les fonctionnalités. Lorsque vous ouvrez le fichier HTML, il devrait ressembler à l'image ci-dessous.

J'ai également [hébergé ce fichier sur GitHub Pages](https://mayur9210.github.io/tic-tac-toe-ai/) si vous voulez voir comment il fonctionne.

Maintenant que l'application est lancée, voyons comment tester les fonctionnalités et observer de visu le processus d'apprentissage de l'IA. Ce test interactif est la partie la plus gratifiante, car vous verrez les concepts abstraits prendre vie.

### Étape 1 : Défier l'IA non entraînée

Lorsque vous chargez le jeu pour la première fois, l'IA est une page blanche. Sa table Q est vide. Assurez-vous que la difficulté est réglée sur **🌱 Débutant** et jouez une partie contre elle. Vous la trouverez probablement très facile à battre. Elle fait des coups aléatoires et insensés car elle n'a aucune expérience. Notez que le nombre d'« États appris » dans le panneau de statistiques est très bas.

### Étape 2 : Entraîner l'IA

Passons maintenant à la magie. Cliquez sur le bouton **« Entraîner l'IA (1000 parties) »**. Vous verrez l'indicateur d'entraînement jaune apparaître avec un compteur de progression. En ces quelques secondes, l'IA joue 1 000 parties contre elle-même, apprenant rapidement de ses victoires, défaites et nuls. Pour chaque coup de chaque partie, elle met à jour sa table Q, renforçant les bonnes stratégies et pénalisant les mauvaises.

### Étape 3 : Défier l'IA entraînée

Une fois l'entraînement terminé, jouez une autre partie en difficulté **🎯 Moyen**. La différence devrait être spectaculaire. L'IA jouera désormais de manière stratégique, bloquant vos victoires et préparant les siennes. Ce n'est plus une proie facile. Vérifiez à nouveau le panneau de statistiques : vous verrez que le nombre d'« États appris » a considérablement augmenté, représentant toutes les nouvelles positions de plateau qu'elle comprend désormais.

### Étape 4 : Expérimenter avec les contrôles

Maintenant que vous avez une IA entraînée, expérimentez les autres fonctionnalités :

* **Passer en 🔥 Expert :** Jouez contre l'algorithme minimax. Remarquez que vous ne pouvez pas gagner. Cela démontre la puissance d'un algorithme de jeu parfait.
    
* **Ajuster les paramètres :** Réglez le curseur du taux d'exploration (ε) sur 0. L'IA deviendra complètement déterministe, choisissant toujours le coup ayant la valeur Q la plus élevée. Réglez-le sur 0,5 et regardez-la redevenir plus erratique et expérimentale.
    
* **Réinitialiser l'IA :** Cliquez sur le bouton « Réinitialiser la mémoire de l'IA ». Cela effacera sa table Q. Si vous jouez contre elle maintenant, vous constaterez qu'elle est revenue à son état initial non entraîné. Cela confirme que son « intelligence » était stockée dans la table Q que vous venez d'effacer.
    

### Vérification de l'implémentation avec des tests automatisés

Bien que jouer au jeu vous donne une bonne idée du comportement de l'IA, les tests automatisés sont cruciaux pour confirmer par programmation que le code sous-jacent est correct. C'est différent du test manuel que vous venez d'effectuer. Ici, nous écrivons du code pour vérifier notre code.

La suite de tests suivante valide les trois fonctionnalités les plus critiques : le changement de difficulté, la persistance des données avec `localStorage` et l'infaillibilité de l'IA experte minimax. Vous pouvez exécuter ces tests en copiant et collant le code dans la console de développement de votre navigateur pendant que le jeu est ouvert.

```javascript
function runTests() {
  console.log('🧪 Exécution des tests améliorés...');
  
  // Test 1 : Changement de difficulté
  const g1 = new TicTacToe();
  g1.setDifficulty('beginner');
  console.assert(g1.ai.difficulty === 'beginner', '✓ Le changement de difficulté fonctionne');
  
  // Test 2 : Persistance localStorage
  const g2 = new TicTacToe();
  g2.ai.q.set('test-state', [1, 2, 3, 4, 5, 6, 7, 8, 9]);
  g2.saveState();
  const g3 = new TicTacToe();
  console.assert(g3.ai.q.has('test-state'), '✓ La persistance localStorage fonctionne');
  
  // Test 3 : Minimax ne perd jamais
  const g4 = new TicTacToe();
  g4.setDifficulty('expert');
  let expertLosses = 0;
  for (let i = 0; i < 100; i++) {
    g4.reset();
    while (!g4.gameOver) {
      const available = g4.getAvailable();
      const move = available[~~(Math.random() * available.length)];
      g4.move(move, 'X');
      if (!g4.gameOver) g4.aiMove();
    }
    const winner = g4.checkWinner();
    if (winner?.winner === 'X') expertLosses++;
  }
  console.assert(expertLosses === 0, '✓ L\'IA experte ne perd jamais');
  
  console.log('✅ Tous les tests ont réussi !');
}
```

Comment fonctionnent ces tests :

1. **Changement de difficulté :** Le premier test crée une instance de jeu, définit la difficulté et vérifie que la propriété interne de l'IA a été mise à jour correctement.
    
2. **Persistance :** Le deuxième test simule la sauvegarde de l'état de l'IA. Il ajoute une entrée factice à la table Q, la sauvegarde, crée une *nouvelle* instance de jeu (simulant un rechargement de page) et vérifie que la nouvelle instance a chargé avec succès les données sauvegardées.
    
3. **Correction du mode expert :** Le troisième test, le plus rigoureux, joue 100 parties contre l'IA experte en utilisant des coups aléatoires pour le joueur. Il vérifie ensuite que l'IA experte n'a pas perdu une seule partie, prouvant que l'implémentation du minimax est correcte.
    

Vous pouvez exécuter ces tests dans la console de votre navigateur après avoir chargé le jeu, comme le montre la capture d'écran ci-dessous.

![Exécution des tests](https://cdn.hashnode.com/res/hashnode/image/upload/v1759790825366/aedc84b7-5399-4067-bf2c-b0b488192c62.png align="center")

## Optimisations avancées et extensions

Maintenant que vous avez l'implémentation complète, voici des moyens de l'étendre davantage :

### Comment implémenter la réduction de symétrie

Vous pouvez réduire l'espace d'état en reconnaissant les positions de plateau équivalentes :

```javascript
getCanonicalState(s) {
  const transforms = [
    s, this.rot90(s), this.rot180(s), this.rot270(s),
    this.flip(s), this.flip(this.rot90(s)), 
    this.flip(this.rot180(s)), this.flip(this.rot270(s))
  ];
  return transforms.sort()[0];
}

rot90(s) {
  const b = s.split('');
  return [b[6],b[3],b[0],b[7],b[4],b[1],b[8],b[5],b[2]].join('');
}

rot180(s) {
  return s.split('').reverse().join('');
}

rot270(s) {
  const b = s.split('');
  return [b[2],b[5],b[8],b[1],b[4],b[7],b[0],b[3],b[6]].join('');
}

flip(s) {
  const b = s.split('');
  return [b[2],b[1],b[0],b[5],b[4],b[3],b[8],b[7],b[6]].join('');
}
```

Cette technique de réduction de symétrie accélère l'apprentissage de l'IA en reconnaissant les positions de plateau équivalentes.

**Comment ça marche :**

* **getCanonicalState()** : Génère les 8 versions symétriques d'un état de plateau (4 rotations + 4 versions retournées) et renvoie la première par ordre alphabétique comme représentation standard.
    
* **rot90()** : Fait pivoter le plateau de 90° dans le sens des aiguilles d'une montre en remappant les indices de position.
    
* **rot180()** : Rotation de 180° en inversant le tableau du plateau.
    
* **rot270()** : Rotation de 270° dans le sens des aiguilles d'une montre (ou 90° dans le sens inverse).
    
* **flip()** : Miroir horizontal du plateau.
    

**Pourquoi c'est important :** En ne stockant que les états canoniques dans la table Q, l'IA réduit les positions uniques d'environ 5 500 à environ 700, ce qui rend l'apprentissage **8 fois plus rapide**.

**Exemple :** Ces plateaux sont considérés comme identiques :

```bash
X-- --- --X
--- = --- = ---
--- --- ---
(original) (rotation 180°) (miroir horizontal)
```

Tous trois correspondent au même état canonique, l'IA n'a donc besoin d'en apprendre qu'un seul au lieu de trois.

Modifiez `getQ()` pour utiliser les états canoniques. Cela réduit le temps d'apprentissage par 8 puisque l'IA reconnaît les positions pivotées et retournées comme équivalentes.

### Comment ajouter une fonctionnalité d'exportation et d'importation

Vous pouvez également permettre aux utilisateurs de partager des modèles d'IA entraînés :

```javascript
exportAI() {
  const data = {
    q: Array.from(this.ai.q.entries()),
    stats: this.stats,
    difficulty: this.ai.difficulty,
    timestamp: Date.now()
  };
  
  const blob = new Blob([JSON.stringify(data)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `tictactoe-ai-${Date.now()}.json`;
  a.click();
  URL.revokeObjectURL(url);
}

importAI(file) {
  const reader = new FileReader();
  reader.onload = (e) => {
    try {
      const data = JSON.parse(e.target.result);
      this.ai.q = new Map(data.q);
      this.stats = data.stats;
      this.ai.difficulty = data.difficulty;
      this.updateStats();
      this.setStatus('✓ IA importée avec succès !');
    } catch (err) {
      this.setStatus('✗ Échec de l\'importation : fichier invalide');
    }
  };
  reader.readAsText(file);
}
```

Ces méthodes permettent de partager des modèles d'IA entraînés entre utilisateurs. La méthode `exportAI()` regroupe l'état complet de l'IA (table Q, statistiques, difficulté et horodatage) dans un objet JSON, crée un Blob à partir de la chaîne JSON, génère une URL de téléchargement temporaire, crée et clique par programmation sur un lien de téléchargement, puis nettoie l'URL. Le nom du fichier inclut un horodatage pour le suivi des versions.

La méthode `importAI()` utilise FileReader pour lire de manière asynchrone un fichier JSON téléchargé, l'analyse, reconstruit la Map à partir du tableau d'entrées, restaure tout l'état du jeu et met à jour l'affichage. La gestion des erreurs capture les fichiers JSON invalides ou corrompus.

### Comment ajouter une visualisation par carte de chaleur (Heatmap) des valeurs Q

Voici comment vous pouvez visualiser la prise de décision de l'IA :

```javascript
drawQValueHeatmap() {
  const state = this.board;
  const qValues = this.ai.getQ(state);
  const available = this.getAvailable();
  
  if (available.length === 0) return;
  
  const maxQ = Math.max(...available.map(i => qValues[i]));
  const minQ = Math.min(...available.map(i => qValues[i]));
  const range = maxQ - minQ || 1;

  this.ctx.globalAlpha = 0.3;
  for (const i of available) {
    const normalized = (qValues[i] - minQ) / range;
    const row = ~~(i / 3);
    const col = i % 3;
    
    // Vert pour les valeurs Q élevées, rouge pour les basses
    const hue = normalized * 120;
    this.ctx.fillStyle = `hsl(${hue}, 70%, 50%)`;
    this.ctx.fillRect(
      col * this.cellSize + 5,
      row * this.cellSize + 5,
      this.cellSize - 10,
      this.cellSize - 10
    );
    
    // Dessiner la valeur Q
    this.ctx.globalAlpha = 1;
    this.ctx.fillStyle = '#000';
    this.ctx.font = '14px monospace';
    this.ctx.fillText(
      qValues[i].toFixed(2),
      col * this.cellSize + 10,
      row * this.cellSize + 25
    );
  }
  this.ctx.globalAlpha = 1;
}
```

Cette méthode de visualisation crée une carte de chaleur codée par couleur montrant la confiance de l'IA dans chaque coup disponible.

Elle récupère d'abord les valeurs Q pour l'état actuel et trouve les valeurs min/max parmi les positions disponibles pour normaliser les données. Pour chaque cellule vide, elle calcule un score normalisé (0 à 1), le convertit en une valeur de teinte (0° rouge pour les valeurs basses, 120° vert pour les valeurs hautes) en utilisant l'espace colorimétrique HSL, et remplit la cellule avec un rectangle coloré semi-transparent. Elle superpose ensuite la valeur Q réelle sous forme de texte pour une inspection précise.

Cela vous donne un retour visuel instantané sur les coups que l'IA considère comme les plus prometteurs. Les cellules vertes sont de bons coups, les cellules rouges sont de mauvais coups.

## Pièges courants et solutions

### Problème 1 : L'IA ne s'améliore pas

* **Cause** : Le taux d'apprentissage est trop bas ou il n'y a pas eu assez d'entraînement.
    
* **Solution** : Augmentez le taux d'apprentissage entre 0,2 et 0,3, et entraînez sur plus de 2 000 parties.
    

### Problème 2 : L'IA fait des coups aléatoires

* **Cause** : Le taux d'exploration est trop élevé après l'entraînement.
    
* **Solution** : Réduisez le taux d'exploration à 0,01 une fois l'entraînement terminé.
    

### Problème 3 : Performances lentes

* **Cause** : La représentation de l'état ou la recherche dans la table Q est inefficace.
    
* **Solution** : Utilisez un Map au lieu d'objets et implémentez la mise en cache d'état.
    

### Problème 4 : L'IA sur-apprend (overfitting) une seule stratégie

* **Cause** : Il n'y a pas assez d'exploration pendant l'entraînement.
    
* **Solution** : Commencez par un taux d'exploration élevé (ε=0,5) et diminuez-le progressivement.
    

## Comment étendre ceci à d'autres jeux

Ce framework s'adapte à d'autres jeux :

* **Puissance 4** : État de 42 caractères, 7 actions (colonnes).
    
* **Blackjack** : L'état inclut les valeurs des mains et la carte du croupier.
    
* **Snake** : Les états continus nécessitent une approximation de fonction.
    

## Conclusion

Vous avez construit un système complet d'apprentissage par renforcement en JavaScript. Ce projet démontre :

* Les concepts de base du RL avec une implémentation pratique.
    
* Une architecture de code propre et maintenable.
    
* L'entraînement et la visualisation en temps réel.
    
* Des techniques avancées comme la décroissance d'epsilon et l'auto-jeu.
    
* Trois niveaux de difficulté, de débutant à expert.
    
* La persistance des données avec localStorage.
    
* Des infobulles interactives pour l'apprentissage.
    

La base de Q-learning que vous avez implémentée alimente des techniques plus avancées comme les réseaux de neurones Q profonds (Deep Q-Networks - DQN) utilisés dans l'IA de jeu moderne.

## Prochaines étapes

Voici quelques pistes pour continuer à apprendre :

1. Ajoutez plus de niveaux de difficulté avec des paramètres personnalisés.
    
2. Implémentez la persistance d'état avec IndexedDB pour des tables Q plus grandes.
    
3. Créez un mode multijoueur avec observation par l'IA.
    
4. Construisez une version avec réseau de neurones en utilisant TensorFlow.js.
    
5. Étendez le projet au Puissance 4 ou aux fins de parties d'échecs.
    

### Ressources pour aller plus loin

* [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book.html) par Sutton et Barto (manuel en ligne gratuit).
    
* [OpenAI Spinning Up](https://spinningup.openai.com/) – ressource complète sur le RL.
    
* [Deep RL Bootcamp](https://sites.google.com/view/deep-rl-bootcamp/) – conférences vidéo de Berkeley.
    
* [Documentation Stable-Baselines3](https://stable-baselines3.readthedocs.io/) – implémentations de RL pour la production.