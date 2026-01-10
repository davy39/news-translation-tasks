---
title: Comment devenir un expert du codage assisté par IA – Un guide pour les développeurs
date: '2025-09-02T20:34:51.054Z'
author: Mrugesh Mohapatra
authorURL: https://www.freecodecamp.org/news/author/mrugesh/
originalURL: https://freecodecamp.org/news/how-to-become-an-expert-in-ai-assisted-coding-a-handbook-for-developers
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1756139431600/1d0cf8b5-ba1b-4c06-ab2d-45ad5e4b4d3b.png
tags:
- name: AI
  slug: ai
- name: coding
  slug: coding
- name: agentic AI
  slug: agentic-ai
seo_desc: I’ve been running freeCodeCamp’s infrastructure for the past seven years,
  and I’m now convinced that experienced developers can write code 3-4x faster while
  maintaining quality. That's what AI-assisted development can offer. In simple terms,
  you can ...
---


Je gère l'infrastructure de freeCodeCamp depuis sept ans et je suis désormais convaincu que les développeurs expérimentés peuvent écrire du code 3 à 4 fois plus vite tout en maintenant la qualité. C'est ce que propose le développement assisté par IA. En termes simples, vous pouvez être plus productif avec des outils d'IA comme GitHub Copilot comme partenaire de codage. Ils suggèrent du code, vous aident au débogage et accélèrent les tâches répétitives.

<!-- more -->

### Pourquoi c'est important

Lors du codage traditionnel, vous tapez chaque ligne vous-même, recherchez dans la documentation et déterminez la syntaxe. Avec l'IA, vous pouvez :

-   Vous concentrer sur la résolution de problèmes au lieu de mémoriser la syntaxe
    
-   Apprendre plus vite en voyant de bons exemples de code en temps réel
    
-   Construire des projets rapidement sans sacrifier la qualité
    

Les développeurs expérimentés peuvent accomplir des tâches plus rapidement avec l'assistance de l'IA. Mais voici la clé : **vous devez savoir comment utiliser ces outils efficacement**. Et vous avez besoin d'une base en programmation pour le faire.

Intéressé ? Plongeons dans le monde des outils de codage basés sur l'IA qui ont pris le monde d'assaut.

## Table des matières

-   [Terminologie essentielle de l'IA][1]
    
-   [Quand utiliser l'IA vs quand coder soi-même][2]
    
-   [Prérequis][3]
    
-   [Votre parcours d'apprentissage complet][4]
    
-   [Comment générer votre premier code assisté par IA (Démarrage rapide)][5]
    
-   [Étape 1 : Fondations – Débuter avec le codage par IA][6]
    
-   [Étape 2 : Fonctionnalités avancées de GitHub Copilot][7]
    
-   [Étape 3 : Agents IA basés sur le CLI (Claude Code & Gemini)][8]
    
-   [Étape 4 : Maîtrise – Combiner les outils et workflows avancés][9]
    
-   [Problèmes courants liés à l'IA][10]
    
-   [Et après avoir terminé toutes les étapes ?][11]
    
-   [Conclusion][12]
    

## Terminologie essentielle de l'IA

Avant de commencer, assurez-vous de comprendre ces termes clés :

-   **Tokens :** Considérez les tokens comme des "morceaux de mots" – la façon dont l'IA lit votre code et votre texte. Chaque caractère, mot ou symbole utilise des tokens. Les versions gratuites limitent le nombre de tokens que vous pouvez utiliser.
    
-   **Fenêtre de contexte (Context Window) :** La quantité de code/conversation que l'IA peut "mémoriser" à la fois. Comme la mémoire à court terme, des fenêtres plus larges signifient une meilleure compréhension de votre projet.
    
-   **Hallucinations :** Lorsque l'IA suggère avec assurance des informations erronées – comme inventer des fonctions qui n'existent pas. Vérifiez toujours les suggestions de l'IA !
    
-   **Prompt :** Vos instructions à l'IA – commentaires, questions ou requêtes qui guident le code qu'elle génère.
    

## Quand utiliser l'IA vs quand coder soi-même

**Utilisez l'IA pour :**

-   Écrire du code boilerplate (getters, setters, CRUD de base)
    
-   Apprendre de nouveaux frameworks ou une nouvelle syntaxe
    
-   Écrire des tests et de la documentation
    
-   Refactoriser des patterns répétitifs
    
-   Se débloquer sur des erreurs de syntaxe
    

**Codez vous-même quand vous :**

-   Concevez l'architecture du système
    
-   Prenez des décisions critiques pour la sécurité
    
-   Écrivez une logique métier complexe
    
-   Apprenez de nouveaux concepts (la première fois)
    
-   Travaillez sur des optimisations critiques pour la performance
    

**La règle d'or :** Utilisez l'IA pour accélérer l'implémentation, mais gardez les décisions architecturales pour vous-même. L'IA est excellente pour le "comment", mais vous décidez du "quoi" et du "pourquoi".

## Prérequis

Avant de commencer ce tutoriel, vous devriez avoir :

-   **Une expérience de base en programmation** – Vous pouvez écrire des programmes simples dans n'importe quel langage
    
-   **Un éditeur de code installé** – VS Code est recommandé (gratuit sur [code.visualstudio.com][13])
    
-   **Des connaissances de base sur Git** – Vous savez comment commit et push du code
    
-   **Gratuit pour commencer** – De nombreux outils ont désormais des paliers gratuits généreux, et les forfaits payants commencent autour de 10-20 $/mois
    

## Votre parcours d'apprentissage complet

Ce tutoriel complet est structuré comme un programme étape par étape pour vous transformer en expert du développement assisté par IA :

Note : Pour garder le tutoriel accessible, nous nous concentrerons sur une poignée d'outils essentiels. Mais vous devriez rechercher et explorer d'autres outils qui pourraient répondre à vos besoins spécifiques au-delà de ceux que nous utilisons ici.

### Votre parcours d'apprentissage :

Vous progresserez à travers 4 étapes : maîtriser les bases de GitHub Copilot, débloquer les fonctionnalités avancées comme les modes de chat et les agents, explorer les outils CLI (Claude Code & Gemini), et enfin combiner stratégiquement plusieurs outils pour des workflows de projet complets.

Tout d'abord, voyons rapidement comment générer votre premier extrait de code par IA.

## Comment générer votre premier code assisté par IA (Démarrage rapide)

Commençons par les bases absolues. Ne vous souciez pas de choisir l'outil "parfait" – vous pourrez toujours changer plus tard. Voici comment commencer :

### GitHub Copilot (Recommandé pour les débutants)

Vous pouvez installer GitHub Copilot en suivant ces étapes :

1.  Ouvrez VS Code
    
2.  Cliquez sur l'icône Extensions (ou appuyez sur Ctrl+Shift+X)
    
3.  Recherchez "GitHub Copilot"
    
4.  Cliquez sur "Installer"
    
5.  Connectez-vous avec votre compte GitHub
    

GitHub Copilot dispose d'un palier gratuit (2000 complétions de code + 50 requêtes de chat par mois), ce qui devrait suffire pour cette expérience.

**ASTUCE :** Les étudiants, enseignants et mainteneurs de projets OSS [peuvent obtenir le forfait Pro gratuitement][14], qui offre un usage illimité.

### Votre première suggestion d'IA

Une fois installé, créez un nouveau fichier nommé `test.js` et tapez :

```
// function to calculate the area of a circle
```

Appuyez sur Entrée et attendez. Vous verrez du texte gris apparaître – c'est votre suggestion d'IA ! Appuyez sur Tab pour l'accepter.

C'est tout ! Vous venez de recevoir votre première suggestion d'IA ! N'est-ce pas génial ?

## Étape 1 : Fondations – Débuter avec le codage par IA

### Étape 1 : Comprendre vos options

Considérez les assistants de codage par IA comme différents types d'amis et de collègues serviables. Couvrons-en quelques-uns :

**Basés sur l'IDE :** Certains outils sont conçus pour fonctionner avec des éditeurs de code familiers ou sont des forks autonomes d'éditeurs comme VS Code. Par exemple :

-   **GitHub Copilot (Extension VS Code)** – Un assistant de codage par IA de GitHub, fonctionne directement dans VS Code avec la complétion par tabulation et des fonctionnalités de chat.
    
-   **Cursor (Autonome)** – Un fork de VS Code avec des modes agents améliorés, un codage autonome plus rapide et une meilleure gestion de la refactorisation de grandes bases de code.
    
-   **Windsurf (Autonome ou Extension VS Code)** – Se concentre sur le développement collaboratif par IA avec des suggestions en temps réel et des fonctionnalités d'équipe.
    
-   **Zed** – Un éditeur haute performance avec assistance IA intégrée et rendu rapide.
    

**Basés sur le CLI :** Certains outils sont basés sur le CLI (interface en ligne de commande), que vous pouvez lancer dans votre terminal :

-   **Claude Code** – L'IA en terminal d'Anthropic pour des sessions de développement autonomes et un raisonnement complexe.
    
-   **Gemini** – L'outil CLI de Google avec de grandes fenêtres de contexte et des capacités multimodales (images, documents).
    
-   **OpenCode** – Alternative open-source avec des modèles personnalisables et des options de traitement local.
    
-   **Cursor CLI** – Version terminal de Cursor pour l'assistance IA en ligne de commande.
    

**Basés sur l'UI et agents d'arrière-plan :** En plus de ceux-ci, il existe également des agents d'arrière-plan et des outils qui peuvent fonctionner entièrement en arrière-plan, comme pour effectuer des revues de pull requests et plus encore.

Par exemple, l'application de bureau de ChatGPT et celle de Claude peuvent éditer des fichiers sur votre système de fichiers local si vous les configurez. De même, certains agents basés sur le cloud peuvent "tourner en arrière-plan" pour exécuter vos instructions. Nous les exclurons du cadre de ce guide.

### Étape 2 : Faire votre choix & apprendre les suggestions automatiques (Complétion par Tab)

Pour votre première étape, je recommande de commencer par GitHub Copilot. Vous pourrez toujours passer à l'outil qui correspond le mieux à vos besoins après avoir appris les bases.

### Étape 3 : Configuration étape par étape

#### Comment configurer GitHub Copilot (Vous pouvez sauter ceci si vous avez déjà suivi le démarrage rapide plus haut)

1.  **Ouvrez VS Code.** Si vous ne l'avez pas, téléchargez-le sur [code.visualstudio.com][15].
    
2.  **Installez l'extension**
    
    -   Appuyez sur `Ctrl+Shift+X` (Windows/Linux) ou `Cmd+Shift+X` (Mac)
        
    -   Tapez "GitHub Copilot" dans la barre de recherche
        
    -   Cliquez sur le bouton bleu "Installer"
        
    -   Vous verrez une fenêtre contextuelle vous demandant de vous connecter
        
3.  **Connectez-vous**
    
    -   Cliquez sur "Sign in to GitHub"
        
    -   Votre navigateur s'ouvrira
        
    -   Connectez-vous avec votre compte GitHub (créez-en un gratuitement sur [github.com][16] si nécessaire)
        
    -   Cliquez sur "Authorize GitHub Copilot"
        
4.  **Commencez à utiliser Copilot**
    
    -   De retour dans VS Code, vous verrez "GitHub Copilot is ready"

### Étape 4 : Maîtriser la complétion par tabulation

Vérifions que cela fonctionne. Créez un nouveau fichier : `hello.py`. Tapez ce commentaire et appuyez sur Entrée :

```
# function to greet a user by name
```

Attendez 1 à 2 secondes. Vous devriez voir du texte gris apparaître. Appuyez simplement sur `Tab` pour accepter la suggestion.

**Ce que vous devriez voir :**

```
# function to greet a user by name
def greet_user(name):
    return f"Hello, {name}!"
```

Si vous voyez cela, félicitations ! Vous utilisez maintenant l'IA pour vous aider à écrire du code.

Si vous rencontrez des problèmes de configuration, vous pouvez consulter la [Référence rapide de dépannage][17] pour des solutions.

### Étape 5 : Raccourcis clavier essentiels & première pratique

Voici les seuls raccourcis dont vous avez besoin pour votre première semaine :

**Les bases :**

-   `Tab` – Accepter la suggestion de l'IA (le plus utilisé !)
    
-   `Esc` – Ignorer la suggestion (quand vous n'en voulez pas)
    

Quand vous serez prêt pour plus, essayez ceux-là :

**Windows/Linux :**

-   `Alt+]` – Voir la suggestion suivante
    
-   `Alt+[` – Voir la suggestion précédente
    
-   `Ctrl+Enter` – Voir toutes les suggestions dans un panneau
    

**macOS :**

-   `Option+]` (ou `Alt+]`) – Voir la suggestion suivante
    
-   `Option+[` (ou `Alt+[`) – Voir la suggestion précédente
    
-   `Ctrl+Enter` – Voir toutes les suggestions dans un panneau
    

### Exercice pratique de l'étape 1

#### Exercice : Construire une application Todo simple

1.  Créez un nouveau fichier nommé `todo.js`
    
2.  Commencez par ce commentaire : `// TODO app with add, remove, and list functions`
    
3.  Ajoutez ce commentaire et attendez les suggestions de l'IA : `// function to add a new todo item`
    
4.  Acceptez la suggestion avec Tab si elle vous semble correcte
    
5.  Continuez d'ajouter des commentaires pour les fonctions de suppression et de liste
    
6.  Testez vos fonctions pour vous assurer qu'elles fonctionnent
    

**Objectif :** Apprendre à "converser" avec l'IA via des commentaires clairs et gagner en confiance pour accepter/rejeter des suggestions.

Besoin d'aide ? Consultez la [Référence rapide de dépannage][18] pour les problèmes courants et les solutions.

### Prêt pour l'étape suivante ? Avant de continuer, assurez-vous de pouvoir :

```
- [ ] Obtenir des suggestions d'IA en tapant des commentaires
- [ ] Accepter les suggestions avec Tab et les ignorer avec Esc
- [ ] Utiliser Alt+] et Alt+[ pour voir différentes suggestions
- [ ] Écrire des fonctions de base avec l'aide de l'IA
```

Si vous êtes à l'aise avec ces bases, vous êtes prêt à apprendre des fonctionnalités plus puissantes de Copilot.

## Étape 2 : Fonctionnalités avancées de GitHub Copilot

### Étape 6 : Obtenir de meilleures suggestions d'IA

Maintenant que vous connaissez les bases, apprenons comment obtenir de _bien meilleures_ suggestions de votre IA. Le secret est de comprendre ce que votre IA peut voir.

#### Ce que votre assistant IA voit

Considérez votre assistant IA comme un ami serviable qui regarde par-dessus votre épaule. Il peut voir :

1.  **Ce que vous tapez en ce moment** – Votre fichier actuel
    
2.  **Les autres onglets ouverts** – Les fichiers que vous avez ouverts (c'est important !)
    
3.  **La structure de votre projet** – Les noms de dossiers et de fichiers
    
4.  **Vos commentaires** – C'est ainsi que vous "parlez" à l'IA
    

#### L'astuce des "onglets voisins"

Voici un conseil de pro qui vous fera gagner des heures : **Gardez les fichiers liés ouverts dans des onglets**.

**Exemple :** Si vous écrivez un composant React :

-   Gardez votre fichier de composant ouvert (`Button.jsx`)
    
-   Ouvrez également votre fichier CSS (`Button.css`)
    
-   Gardez votre fichier de test visible aussi (`Button.test.js`)
    

Vous pouvez ensuite partager ces fichiers supplémentaires comme contexte avec l'IA de plusieurs manières :

-   **Mentionner des fichiers avec @ :** Tapez `@nomdufichier.js` dans le chat pour référencer des fichiers spécifiques
    
-   **Utiliser @workspace :** Ce participant au chat peut voir tous les fichiers de votre projet
    
-   **Glisser-déposer :** Faites simplement glisser des fichiers de l'explorateur vers la fenêtre de chat
    
-   **Sélectionner du code :** Surlignez du code et faites un clic droit sur "Ask Copilot" pour l'inclure dans le contexte
    

L'IA utilise ces fichiers ouverts pour comprendre la structure de votre projet et suggérer du code plus pertinent qui correspond à vos patterns existants.

### Étape 7 : Contrôle qualité & meilleures pratiques

#### Comprendre les limites de l'IA

L'IA est puissante mais elle n'est pas parfaite. Voici les points clés à surveiller :

**Erreurs courantes de l'IA :**

1.  Fonctions inventées : par exemple, `const result = array.superSort();` n'existe pas !
    
2.  Mauvais paramètres : par exemple, `greetUser("John", "Doe");` quand la fonction attend `greetUser(name)`
    
3.  Solutions sur-compliquées : par exemple, `const isEven = (num) => num.toString(2).slice(-1) === "0";` – utilisez simplement `num % 2 === 0`
    

Checklist rapide de qualité :

```
- [ ] Tester le code - fonctionne-t-il réellement ?
- [ ] Le lire - a-t-il un sens logique ?
- [ ] Vérifier les bases - toutes les fonctions/variables sont-elles définies ?
- [ ] Faire confiance à son instinct - si cela semble faux, enquêtez
```

#### Essentiels de sécurité

Avant d'accepter des suggestions d'IA, assurez-vous de vérifier ces problèmes de sécurité :

```
- [ ] Pas de mots de passe ou de clés API codés en dur
- [ ] Les entrées utilisateur sont validées
- [ ] Pas de eval() avec des données utilisateur
- [ ] Les messages d'erreur n'exposent pas d'informations sensibles
```

#### Meilleure rédaction de prompts

Voici une formule pour écrire des prompts solides : Quoi + Comment + Type de retour.

```
// ❌ Vague : "make function"
// ✅ Clair : "function to validate email format using regex, returns boolean"
```

#### Personnalisation au niveau du dépôt avec les instructions Copilot

GitHub Copilot prend désormais en charge la personnalisation au niveau du dépôt via les fichiers `.github/copilot-instructions.md`. Cette fonctionnalité aide Copilot à comprendre les patterns et conventions spécifiques de votre projet.

Voici comment configurer les instructions Copilot :

```
# Créer le répertoire GitHub s'il n'existe pas
mkdir -p .github
touch .github/copilot-instructions.md
```

Exemple de fichier [copilot-instructions.md][19] :

```
# Copilot Instructions

## Style de code

- Utiliser des composants fonctionnels React avec des hooks
- Préférer TypeScript à JavaScript pour les nouveaux fichiers
- Utiliser Tailwind CSS pour le style
- Suivre la structure de fichiers existante dans `/src/components`

## Tests

- Écrire des tests avec React Testing Library
- Placer les fichiers de test dans les répertoires `__tests__`
- Utiliser des noms de tests descriptifs qui expliquent le comportement

## Patterns API

- Utiliser des hooks personnalisés pour les appels API
- Gérer les états de chargement et d'erreur de manière cohérente
- Utiliser React Query pour la récupération de données

## Conventions de nommage

- Composants : PascalCase (ex: `UserProfile.tsx`)
- Hooks : camelCase commençant par 'use' (ex: `useUserData.ts`)
- Utilitaires : camelCase (ex: `formatDate.ts`)
```

**Ce que cela permet :**

-   Copilot suggère du code qui correspond aux patterns de votre projet
    
-   Suit automatiquement vos conventions de nommage
    
-   Suggère des approches de test appropriées
    
-   Comprend vos bibliothèques et frameworks préférés
    

**Meilleures pratiques :**

-   Gardez des instructions claires et spécifiques
    
-   Mettez-les à jour au fur et à mesure que les standards de votre projet évoluent
    
-   Incluez des exemples de patterns préférés
    
-   Mentionnez les bibliothèques et frameworks que vous utilisez
    

### Étape 8 : Débloquer les fonctionnalités avancées de Copilot

#### Comprendre vos options

GitHub Copilot offre plusieurs façons d'obtenir de l'aide par IA :

1.  **Complétion par tabulation** (ce que vous avez utilisé) – Suggestions pendant la frappe
    
2.  **Mode Chat** – Avoir des conversations avec l'IA sur votre code
    
3.  **Mode Édition** – Demander à l'IA de modifier du code existant
    
4.  **Mode Agent** – Laisser l'IA travailler de manière autonome sur de grosses tâches
    

Nous discuterons de ces modes plus en détail ci-dessous afin que vous sachiez comment ils fonctionnent et quand vous devriez les utiliser.

#### Sélection du modèle

Copilot propose désormais différents modèles d'IA pour différents besoins :

Gratuit avec abonnement :

-   **GPT-4.1** – Modèle par défaut avec de solides performances globales
    
-   **GPT-4** – Fiable pour la plupart des tâches de codage
    

Modèles Premium (usage mensuel limité) :

-   **Claude 3.5 Sonnet** – Excellent pour la logique complexe
    
-   **GPT-5** – Le plus récent et le plus performant
    
-   **Gemini 2.0 Flash** – Réponses très rapides
    

**Comment changer de modèle :** Cliquez sur le menu déroulant du modèle dans la vue Chat.

**Conseil :** Commencez avec les modèles gratuits (GPT-4.1) pour l'apprentissage, et réservez les modèles premium pour les problèmes complexes.

#### Limites de GitHub Copilot

Voici quelques points importants à considérer lorsque vous utilisez l'IA pour vous aider dans votre codage :

-   **Dépendance à Internet** – Nécessite une connexion stable pour les suggestions
    
-   **Limites de contexte** – Ne voit que les fichiers ouverts, pas toute la structure de votre projet
    
-   **Limites du palier gratuit** – 2 000 complétions et 50 requêtes de chat par mois
    
-   **Qualité de code variable** – Examinez toujours les suggestions, surtout pour le code sensible à la sécurité
    
-   **Courbe d'apprentissage** – Prend du temps pour écrire des prompts efficaces pour des tâches complexes
    
-   **Considérations de confidentialité** – Votre code est envoyé aux serveurs de GitHub (vérifiez les politiques de votre organisation)
    

#### Chat basique vs Suggestions

Vous vous demandez peut-être quand utiliser la complétion par tabulation et quand utiliser le chat ? Il est préférable d'utiliser la complétion pour écrire de nouvelles fonctions, obtenir une aide rapide sur la syntaxe et compléter des patterns. Utilisez le chat pour expliquer du code existant, obtenir de l'aide sur des erreurs et planifier votre approche des problèmes.

**Essayez :** Ouvrez le Chat (Ctrl+Shift+I) et demandez : "Que fait cette fonction ?" tout en sélectionnant du code.

### Étape 9 : Maîtriser les modes Chat et Agent

#### Les trois modes de Chat

1.  **Mode Ask (Défaut)** – pour les questions et explications :

```
"Que fait cette fonction ?"
"Comment puis-je optimiser ce code ?"
"Explique ce message d'erreur"
```

2.  **Mode Edit** – Pour apporter des modifications au code existant :

```
"Refactorise ceci pour utiliser async/await"
"Ajoute une gestion d'erreurs à tous les appels API"
"Convertis ceci en TypeScript"
```

-   Affiche les diffs inline avant d'appliquer les changements
    
-   Fonctionne sur plusieurs fichiers
    
-   Idéal pour les refactorisations systématiques
    

3.  **Mode Agent** – Pour le développement autonome :

```
"Crée une API REST avec authentification"
"Construis une application todo avec React et des tests"
"Migre cette base de code de Vue 2 vers Vue 3"
```

-   Appuyez sur `Shift+Cmd+I` (Mac) ou `Ctrl+Shift+I` (Windows/Linux)
    
-   Travaille indépendamment pendant des heures
    
-   Installe des packages, crée des fichiers, lance des tests automatiquement
    

#### Quand utiliser chaque mode

Chaque mode a ses cas d'utilisation particuliers. Utilisez le mode Ask quand vous apprenez de nouveaux concepts, que vous voulez comprendre du code existant, pour obtenir des explications et pour planifier des approches.

Utilisez le mode Edit quand vous refactorisez du code existant, appliquez des changements cohérents, ajoutez des fonctionnalités à des fonctions existantes, ou pour des mises à jour de style/pattern.

Le mode Agent est utile pour construire des fonctionnalités complètes (plus de 30 minutes de travail), configurer de nouveaux projets, effectuer des refactorisations à grande échelle, et quand vous voulez travailler sur d'autres choses pendant que l'IA code.

#### Exemples du mode Agent

Petite tâche d'agent (15 minutes) :

```
"Ajoute l'authentification utilisateur à mon application Express"
```

Ce que l'agent a généré :

```
// middleware/auth.js
const jwt = require('jsonwebtoken');

const authenticateToken = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) return res.sendStatus(401);

  jwt.verify(token, process.env.ACCESS_TOKEN_SECRET, (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
};

// routes/auth.js
router.post('/login', async (req, res) => {
  // Logique d'authentification avec bcrypt
  const accessToken = jwt.sign({username: user.username}, process.env.ACCESS_TOKEN_SECRET);
  res.json({accessToken: accessToken});
});
```

**Problèmes clés trouvés :** L'agent avait initialement oublié de hasher les mots de passe et n'avait pas inclus de tokens de rafraîchissement. Cela a nécessité une itération pour corriger les failles de sécurité et ajouter une gestion d'erreurs appropriée.

Grosse tâche d'agent (plus de 4 heures) :

```
"Modernise cette application React basée sur des classes vers des hooks avec TypeScript"
```

Ce que l'agent a généré :

```
// Avant (Composant de classe)
class UserProfile extends React.Component {
  constructor(props) {
    this.state = { user: null, loading: true };
  }
  // ... méthodes de cycle de vie
}

// Après (Hooks + TypeScript)
interface User {
  id: number;
  name: string;
  email: string;
}

const UserProfile: React.FC = () => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchUser().then(setUser).finally(() => setLoading(false));
  }, []);

  return <div>{loading ? 'Chargement...' : user?.name}</div>;
};
```

**Problèmes clés trouvés :** l'agent a réussi à mettre à jour 47 fichiers, mais a eu initialement des problèmes de typage avec les gestionnaires d'événements et a eu besoin d'affiner les types génériques. Les tests automatisés ont également nécessité une revue manuelle pour assurer une couverture TypeScript correcte.

#### Utiliser les participants au chat

Les participants au chat sont des assistants IA spécialisés qui ont accès à des parties spécifiques de votre environnement de développement. Considérez-les comme des experts dans différents domaines qui peuvent aider pour des tâches ciblées.

Ce sont essentiellement des aides IA préfixées par `@` qui possèdent des connaissances et des capacités spéciales :

-   **@workspace** a accès à toute la structure de votre projet, peut rechercher des fichiers et comprendre les relations entre les composants. Utilisez `@workspace` quand vous avez besoin d'une analyse à l'échelle du projet : "Trouve tous les points de terminaison API dans ce projet" ou "Montre-moi où l'authentification utilisateur est implémentée."
    
-   **@terminal** connaît les opérations en ligne de commande et peut suggérer des commandes shell et expliquer la sortie du terminal. Utilisez `@terminal` pour l'aide en ligne de commande : "Quelle commande lance les tests ?" ou "Comment construire ce projet pour la production ?"
    
-   **@vscode** est un expert des fonctionnalités de VS Code et peut aider pour les paramètres, le débogage et la configuration de l'éditeur. Utilisez `@vscode` pour l'assistance sur l'éditeur : "Configure le débogage pour Node.js" ou "Configure le formatage automatique pour ce projet."
    

**Exemple d'utilisation :**

```
@workspace Peux-tu trouver tous les modèles de base de données dans ce projet ?
@terminal Quelle est la commande pour installer les dépendances et démarrer le serveur de dev ?
@vscode Comment configurer des points d'arrêt pour déboguer cette application Express ?
```

### Étape 10 : Fonctionnalités pour utilisateurs avancés et workflows sophistiqués

Au-delà des fonctionnalités de base de Copilot que vous avez apprises, il existe des outils et des commandes spécialisés qui peuvent décupler votre productivité. Ces fonctionnalités vont au-delà des modes de chat basiques et de la sélection de modèles, en se concentrant sur des opérations multi-fichiers complexes et une automatisation avancée.

#### Commandes Slash avancées

```
/doc - Générer de la documentation
/explain - Explication détaillée du code
/fix - Corriger les erreurs dans le code sélectionné
/tests - Générer des tests unitaires
/new - Créer une nouvelle structure de projet
```

#### Opérations multi-fichiers

**Utiliser les références # :**

Le symbole `#` crée des références spécifiques qui indiquent à Copilot sur quoi se concentrer exactement. Ces références fonctionnent comme des pointeurs précis vers différentes parties de votre projet :

-   **#file:nomdufichier** : Référence un fichier spécifique : `#file:UserModel.js`
    
-   **#codebase** : Référence l'ensemble de la base de code de votre projet pour la recherche
    
-   **#selection** : Référence le code actuellement sélectionné
    
-   **#editor** : Référence le fichier actuellement actif
    

```
"Mets à jour #file:UserModel.js pour inclure des horodatages"
"Recherche dans #codebase toutes les requêtes de base de données"  
"Refactorise #selection pour utiliser la syntaxe JavaScript moderne"
"Ajoute une gestion d'erreurs à #editor pour tous les appels API"
```

Ces références aident Copilot à comprendre exactement où regarder et quoi changer, rendant les opérations multi-fichiers beaucoup plus précises.

**Glisser-déposer :**

Le glisser-déposer est l'un des moyens les plus intuitifs de fournir du contexte à Copilot. Vous pouvez simplement faire glisser des fichiers de l'explorateur VS Code directement dans la fenêtre de chat, et Copilot comprendra instantanément leur contenu et leur structure.

Cette fonctionnalité est particulièrement utile lorsque vous travaillez sur des composants liés et que vous avez besoin que l'IA comprenne comment les différents fichiers se connectent. Copilot mémorise ces relations de fichiers tout au long de votre conversation, vous n'avez donc pas besoin de re-télécharger les fichiers en continuant la même discussion.

Cette persistance du contexte fonctionne sur plusieurs sessions de chat, ce qui facilite la reprise là où vous vous étiez arrêté sur des projets multi-fichiers complexes.

### Exercices pratiques de l'étape 2

#### Exercice 1 : Pratique du mode Chat

1.  Utilisez le mode Ask pour comprendre une fonction complexe
    
2.  Passez au mode Edit pour la refactoriser
    
3.  Comparez les approches
    

#### Exercice 2 : Projet en mode Agent

1.  Démarrez le mode Agent (`Shift+Cmd+I`)
    
2.  Requête : "Crée une application todo simple avec des tests"
    
3.  Observez le processus de développement autonome
    
4.  Examinez le code généré
    

#### Exercice 3 : Fonctionnalités avancées

1.  Utilisez les participants @ pour des questions sur le projet
    
2.  Expérimentez avec les commandes slash
    
3.  Pratiquez les opérations multi-fichiers
    

### Prêt pour les outils CLI ?

Vous avez maintenant appris les bases de GitHub Copilot dans VS Code ! Les outils CLI comme Claude Code et Gemini offrent encore plus de puissance pour le développement basé sur le terminal.

Si vous êtes intéressé par l'IA en terminal, vous pouvez passer à l'étape 3 juste en dessous. Si vous préférez rester sur VS Code, passez directement à l'étape 4 pour les workflows avancés.

## Étape 3 : Agents IA basés sur le CLI (Claude Code & Gemini)

### Étape 11 : Rencontrez Claude Code – Votre assistant IA en terminal

#### Qu'est-ce que Claude Code ?

Vous vous souvenez comment GitHub Copilot vous aide dans VS Code ? Claude Code fait la même chose, mais dans votre terminal.

Au lieu de taper dans VS Code et d'obtenir des suggestions, vous tapez dans votre terminal et avez des conversations avec l'IA. C'est comme avoir un binôme de codage directement dans votre ligne de commande.

#### Exemple simple :

Dans VS Code avec Copilot :

```
// create a function to validate email
[L'IA suggère du code]
```

Dans le terminal avec Claude Code :

```
claude
> Crée une fonction pour valider les adresses email
[L'IA écrit le code pour vous]
```

Alors, quand devriez-vous utiliser VS Code/Copilot et quand devriez-vous utiliser Claude Code ?

**Claude Code est idéal si vous :**

-   Aimez travailler dans le terminal
    
-   Voulez avoir des conversations IA sur le code
    
-   Avez besoin d'aide pour des tâches en ligne de commande
    
-   Voulez plus de contrôle sur les interactions IA
    

**Restez avec VS Code Copilot si vous :**

-   Préférez les éditeurs visuels
    
-   Êtes satisfait de votre workflow actuel
    
-   Ne passez pas beaucoup de temps dans le terminal
    

#### Tarification

Claude Code nécessite un abonnement Claude Pro (20 $/mois), Claude Team (30 $/mois par utilisateur) ou Claude Enterprise, ou un paiement à l'usage avec des crédits API.

#### Limites de Claude Code

Voici quelques considérations importantes si vous prévoyez d'utiliser Claude Code :

-   **Payant uniquement** – Pas de palier gratuit, nécessite un abonnement Claude Pro ou des crédits API
    
-   **Basé sur le terminal** – Moins visuel que les outils intégrés à l'IDE
    
-   **Courbe d'apprentissage** – Nécessite d'être à l'aise avec les interfaces en ligne de commande
    
-   **Gestion du contexte** – Vous devez gérer manuellement le contexte de la conversation
    
-   **Dépendance à Internet** – Nécessite une connexion stable pour toutes les opérations
    
-   **Limites de session** – Les longues sessions autonomes consomment beaucoup de crédits API
    

#### Installation

Recommandé (toutes plateformes) :

```
npm install -g @anthropic-ai/claude-code
```

Installations alternatives :

-   **macOS/Linux** : `curl -fsSL https://claude.ai/install.sh | bash`
    
-   **Windows** : `irm https://claude.ai/install.ps1 | iex`
    

#### Utilisation de base

**Mode interactif (Recommandé) :**

Le mode interactif est l'interface principale de Claude Code où vous avez des conversations en temps réel avec l'IA. Contrairement aux commandes one-shot qui s'exécutent une fois et s'arrêtent, le mode interactif crée une session persistante où vous pouvez poser des questions de suivi, itérer sur des solutions et construire des projets complexes au fil du temps.

Le mode interactif est recommandé car :

-   **Persistance du contexte :** Claude mémorise toute la conversation et le contexte du projet
    
-   **Développement itératif :** Vous pouvez affiner les requêtes et construire sur les réponses précédentes
    
-   **Collaboration en temps réel :** Posez des questions, obtenez des explications et modifiez les approches au fur et à mesure que vous travaillez
    
-   **Reprise de session :** Continuez les conversations précédentes avec `claude --resume`
    

**Autres modes disponibles :**

-   **Mode one-shot :** Exécution d'une seule commande (expliqué ci-dessous)
    
-   **Mode agent :** Sessions de développement autonomes qui peuvent travailler pendant des heures indépendamment
    

1.  Naviguez vers votre projet :

```
cd votre-projet
claude
```

2.  Commencez à converser naturellement :

```
Claude Code > analyse cette base de code et suggère des améliorations

Claude Code > maintenant aide-moi à refactoriser l'authentification utilisateur

Claude Code > ajoute des tests unitaires pour le module de paiement
```

3.  Continuez la session précédente :

```
claude --resume
```

**Commandes One-shot (pour les tâches rapides) :**

Les commandes one-shot sont des commandes à exécution unique qui effectuent une tâche spécifique puis s'arrêtent. Contrairement au mode interactif, elles ne maintiennent pas le contexte de la conversation – elles sont parfaites pour des tâches rapides et autonomes.

**Que sont les commandes One-shot ?**

Ce sont des commandes que vous lancez avec une instruction spécifique directement depuis votre terminal, sans entrer dans une session interactive. Claude exécute la requête et fournit les résultats immédiatement.

**Quand utiliser les commandes One-shot :**

-   Analyse rapide ou revues de code
    
-   Modifications simples de fichiers
    
-   Scripts automatisés et intégration CI/CD
    
-   Lorsque vous avez besoin d'une réponse unique et spécifique
    

**Exemples :**

```
claude "analyse cette base de code et suggère des améliorations"
claude "corrige toutes les erreurs TypeScript dans src/"
claude "génère des tests unitaires pour utils.js"
claude "explique ce que fait cette fonction" --file src/auth.js
```

La différence clé est que les commandes one-shot ne mémorisent pas le contexte entre les exécutions, tandis que le mode interactif maintient l'historique complet de la conversation et la compréhension du projet.

**Sessions interactives vs autonomes :**

Au sein du mode interactif, vous pouvez choisir entre des approches collaboratives et autonomes :

**Session interactive (collaborative) :**

```
Claude Code > Je construis l'authentification utilisateur. Quelle approche devrions-nous adopter ?

Vous : Utilise des tokens JWT avec rotation des refresh tokens

Claude Code > implémente l'authentification JWT avec refresh tokens
[Vous montre l'implémentation étape par étape]

Claude Code > dois-je aussi ajouter la fonctionnalité de réinitialisation de mot de passe ?

Vous : Oui, utilise la réinitialisation par email
```

**Session autonome (développement sans intervention) :**

```
Claude Code > Construis un système complet de gestion des utilisateurs avec authentification, profils, préférences et fonctionnalités d'administration. Utilise les meilleures pratiques pour la sécurité et les tests.

[Claude travaille pendant des heures de manière autonome, fournissant des mises à jour périodiques]
[Résultat final : Système complet de gestion des utilisateurs prêt pour la production]
```

**Quand utiliser chacune :** Utilisez les sessions interactives lors de l'apprentissage ou quand vous voulez garder le contrôle sur les décisions. Utilisez les sessions autonomes pour des tâches bien définies où vous faites confiance à Claude pour faire de bons choix indépendamment.

#### Fonctionnalités clés

**Modes de réflexion (à utiliser en session interactive) :**

Les modes de réflexion sont des commandes spéciales qui indiquent à Claude la profondeur d'analyse souhaitée avant de répondre. Vous choisissez ces modes manuellement en fonction de la complexité de votre problème.

**Quand utiliser chaque mode :**

-   `think` – Analyse rapide pour des tâches simples : "think: revois cette fonction pour des bugs"
    
-   `think hard` – Raisonnement plus profond pour une logique complexe : "think hard: optimise cet algorithme"
    
-   `think harder` – Résolution de problèmes complexes avec de multiples considérations : "think harder: conçois un schéma de base de données évolutif"
    
-   `ultrathink` – Analyse de profondeur maximale pour les décisions architecturales : "ultrathink: évalue microservices vs monolithe pour ce projet"
    

**Comment ils fonctionnent :**

Claude vous montre son processus de raisonnement avec les modes de réflexion plus longs. Vous verrez une analyse étape par étape avant d'obtenir la réponse finale. Les modes de réflexion plus élevés prennent plus de temps mais fournissent des solutions plus approfondies.

**Choisir le bon mode :**

Utilisez `think` pour des revues de code rapides, `think hard` pour déboguer des problèmes complexes, `think harder` pour des problèmes de conception de système, et `ultrathink` pour les décisions architecturales majeures qui affectent tout votre projet.

#### Personnalisation au niveau du projet avec Claude.md

L'une des fonctionnalités les plus puissantes de Claude Code est la personnalisation au niveau du projet à l'aide des fichiers `.claude/CLAUDE.md`. Cela vous permet de donner à Claude le contexte de votre projet spécifique, de vos standards de codage et de vos préférences.

Configurez CLAUDE.md comme ceci :

```
# Créer la configuration au niveau du projet
mkdir -p .claude
touch .claude/CLAUDE.md
```

Voici un exemple de fichier CLAUDE.md :

```
# Contexte du projet

Ceci est une API REST Node.js utilisant Express et PostgreSQL.

## Standards de codage

- Utiliser async/await, jamais de callbacks
- Toutes les requêtes de base de données utilisent Prisma ORM
- Écrire des tests avec Jest pour toutes les nouvelles fonctions
- Suivre les conventions RESTful

## Structure du projet

- `/src/routes` - Points de terminaison API
- `/src/models` - Modèles de base de données
- `/src/middleware` - Middleware Express
- `/tests` - Tests unitaires et d'intégration

## Préférences

- Utiliser TypeScript pour tous les nouveaux fichiers
- Préférer les patterns de programmation fonctionnelle
- Inclure des commentaires JSDoc pour toutes les fonctions
```

Cela aide Claude à comprendre automatiquement la structure de votre projet. Cela aide également Claude à suivre vos standards de codage spécifiques, à suggérer des patterns appropriés pour votre stack technique et à mémoriser vos préférences d'une session à l'autre.

**Conseil de pro :** Mettez à jour votre CLAUDE.md au fur et à mesure que votre projet évolue pour que les suggestions de Claude restent pertinentes et précises.

#### Sessions de développement autonome Claude Code

Voici un exemple d'une session de développement autonome de plusieurs heures :

```
cd votre-projet
claude
```

**Votre prompt :** "Construis une API GraphQL évolutive avec des abonnements en temps réel, authentification, limitation de débit et tests complets"

Processus autonome de 6 heures de Claude :

```
Claude Code > ultrathink: analyse des exigences et conception de l'architecture

[Crée des spécifications techniques détaillées et un plan de développement]

Claude Code > implémentation du serveur GraphQL de base avec Apollo
[Exécute : npm install apollo-server-express graphql]
[Crée : server.js, schema/typeDefs.js, resolvers/index.js]

Claude Code > ajout du middleware d'authentification et d'autorisation
[Crée : middleware/auth.js, utils/jwt.js, models/User.js]
[Implémente la stratégie JWT avec une gestion d'erreurs appropriée]

Claude Code > configuration des abonnements en temps réel avec Redis
[Exécute : npm install graphql-redis-subscriptions]
[Configure les connexions WebSocket, crée les résolveurs d'abonnement]

Claude Code > implémentation de la limitation de débit et des mesures de sécurité
[Ajoute helmet, express-rate-limit, analyse de complexité de requête]

Claude Code > rédaction d'une suite de tests complète
[Crée des tests unitaires, tests d'intégration, tests de charge]
[Exécute : npm test - voit 8 tests échouer]

Claude Code > correction automatique des échecs de tests
[Identifie des problèmes de timing asynchrone, corrige la logique des résolveurs]
[Relance les tests à plusieurs reprises jusqu'à ce que 94/94 tests réussissent]

Claude Code > optimisation des performances et mise en cache
[Implémente la mise en cache Redis, optimise les requêtes de base de données]
[Ajoute la surveillance des performances et la journalisation]

Claude Code > génération d'une documentation complète
[Crée la doc API avec exemples, README, guide de déploiement]

Claude Code > validation finale et nettoyage
[Lance la suite complète de tests, vérifie la couverture de code : 96%]
[Crée le build de production et les scripts de déploiement]
```

Cela représente 6 heures de travail autonome (vous pouvez travailler sur d'autres projets pendant ce temps). Le résultat est une API GraphQL prête pour la production avec authentification, fonctionnalités en temps réel et tests complets.

Pourquoi cela fonctionne :

-   **Boucles de rétroaction autonomes :** Claude lance les tests, voit les échecs, les corrige automatiquement.
    
-   **Conscience du contexte :** Maintient la compréhension de toute la structure du projet.
    
-   **Auto-correction :** Itère sur les solutions jusqu'à ce qu'elles fonctionnent correctement.
    
-   **Intégration d'outils :** Utilise git, npm, les frameworks de test de manière transparente.
    

**Intégration de la recherche Web :**

Claude Code peut effectuer des recherches sur le Web pour obtenir des informations actuelles, ce qui est particulièrement utile puisque les données d'entraînement de l'IA ont des dates de coupure. Cette fonctionnalité vous aide à rester à jour avec les dernières documentations, meilleures pratiques et solutions.

```
Claude Code > recherche les dernières fonctionnalités de React 19 et mets à jour mes composants

[Claude cherche sur le web, puis continue la conversation avec ses découvertes]

Claude Code > maintenant applique ces nouvelles fonctionnalités au composant UserProfile
```

**Quand la recherche Web aide :**

-   Obtenir la documentation actuelle pour les nouvelles versions de bibliothèques.
    
-   Trouver des solutions à des messages d'erreur ou des bugs récents.
    
-   Rechercher les dernières meilleures pratiques et patterns.
    
-   Comparer les approches actuelles des problèmes.
    

La recherche Web se produit automatiquement lorsque Claude détecte qu'il a besoin d'informations actuelles, ou vous pouvez la demander explicitement en mentionnant "recherche" ou "dernier" dans vos prompts.

#### Raccourcis clavier Claude Code

Vous pouvez utiliser ces raccourcis clavier pour être encore plus productif :

**Contrôles essentiels :**

-   `Ctrl+C` – Annuler l'entrée ou la génération actuelle
    
-   `Ctrl+D` – Quitter la session Claude Code
    
-   `Ctrl+L` – Effacer l'écran du terminal
    
-   `Flèches Haut/Bas` – Naviguer dans l'historique des commandes
    
-   `Esc` + `Esc` – Modifier le message précédent
    

**Entrée multiligne :**

-   `\` + `Entrée` – Échap rapide pour créer une nouvelle ligne (fonctionne dans tous les terminaux)
    
-   `Option+Entrée` (Mac) / `Shift+Entrée` (si configuré) – Insérer une nouvelle ligne
    

### Étape 12 : Google Gemini CLI

#### Quand utiliser Gemini vs Claude Code :

Gemini est un autre outil IA basé sur le CLI qui complète Claude Code plutôt que de le concurrencer. Alors que Claude Code excelle dans le raisonnement profond et les tâches de développement complexes, Gemini offre des avantages uniques : des fenêtres de contexte massives (plus d'un million de tokens), des limites gratuites généreuses et de puissantes capacités multimodales.

**Utilisez Gemini quand vous :**

-   Avez besoin d'analyser d'entières bases de code volumineuses d'un coup.
    
-   Voulez traiter des images, des diagrammes ou des croquis.
    
-   Travaillez avec des contraintes budgétaires (palier gratuit généreux).
    
-   Avez besoin de fenêtres de contexte extrêmement larges pour des projets complexes.
    

**Utilisez Claude Code quand vous :**

-   Avez besoin d'un raisonnement et d'une résolution de problèmes sophistiqués.
    
-   Voulez des sessions de développement autonomes.
    
-   Préférez des modes de réflexion avancés pour une analyse complexe.
    
-   Construisez des systèmes de production nécessitant une planification détaillée.
    

**La meilleure approche :** De nombreux développeurs utilisent les deux outils de manière stratégique – Gemini pour l'analyse et les entrées visuelles, Claude Code pour les tâches de développement complexes.

Gemini apporte l'IA de Google dans votre terminal avec des limites gratuites généreuses.

#### Installation

Utilisation de npx (recommandé pour essayer) :

```
npx @google/gemini-cli
```

Installation globale :

```
npm install -g @google/gemini-cli
gemini  # Démarre une session interactive
```

#### Authentification

1.  Connectez-vous avec Google :

```
gemini auth login
```

2.  Vérifiez le statut :

```
gemini auth status
```

Limites gratuites :

-   60 requêtes/minute
    
-   1 000 requêtes/jour avec un compte Google
    

Outils intégrés :

-   `/memory` – Gérer la mémoire de la conversation
    
-   `/stats` – Voir les statistiques d'utilisation
    
-   `/tools` – Lister les outils disponibles
    
-   `/mcp` – Configurer les serveurs Model Context Protocol
    

#### Limites du CLI Gemini

Voici quelques considérations importantes si vous prévoyez d'utiliser Gemini :

-   **Limites de débit** – 60 requêtes/minute et 1 000/jour sur le palier gratuit.
    
-   **Dépendance à Google** – Nécessite un compte Google et une connexion Internet.
    
-   **Outil plus récent** – Communauté plus petite et moins de ressources par rapport à GitHub Copilot.
    
-   **Axé sur le terminal** – Moins d'intégration avec les IDE populaires.
    
-   **Traitement multimodal** – Les téléchargements d'images ont des limites de taille (20 Mo).
    
-   **Fonctionnalités bêta** – Certaines fonctionnalités avancées peuvent être instables.
    

#### Fonctionnalités uniques de Gemini

**Fenêtre de contexte massive :**  
Gemini peut gérer plus d'un million de tokens dans une seule session, ce qui signifie qu'il peut analyser simultanément d'entières bases de code volumineuses. C'est particulièrement utile pour comprendre les architectures système complexes et les relations entre de nombreux fichiers.

**Capacités multimodales :**  
Gemini peut traiter et comprendre divers types de contenu visuel à côté du code, ce qui le rend unique pour les workflows du design au code et le débogage visuel.

#### Transformez vos croquis en code

C'est vraiment génial : vous pouvez littéralement dessiner quelque chose sur papier et Gemini le transformera en code fonctionnel !

Voici comment faire :

1.  **Créez votre croquis :** Dessinez votre idée sur papier, un tableau blanc ou une tablette numérique.
    
2.  **Prenez une photo ou une capture d'écran :** Utilisez votre téléphone ou faites une capture d'écran pour capturer le croquis numériquement.
    
3.  **Enregistrez l'image :** Enregistrez-la au format JPG, PNG ou WebP (moins de 20 Mo).
    
4.  **Montrez-la à Gemini via la ligne de commande :**
    

```
gemini -p "Transforme ce croquis en un composant React avec un joli style" sketch.jpg
```

**Méthodes alternatives :**

```
# Si vous êtes dans une session interactive, vous pouvez référencer le fichier :
gemini
> analyse ce croquis d'UI et crée le HTML/CSS : @sketch.jpg

# Ou glisser-déposer dans les terminaux supportés
gemini
> implémente ce design comme un composant Vue
[glissez sketch.jpg dans le terminal]
```

Gemini regarde alors votre dessin et crée :

-   Un composant React fonctionnel qui correspond à votre croquis.
    
-   Un joli style CSS pour le rendre attrayant.
    
-   La validation de formulaire si vous avez dessiné un formulaire.
    
-   Tout le code dont vous avez besoin pour le faire fonctionner.
    

C'est comme avoir un designer et un développeur qui peuvent lire dans vos pensées !

#### Corriger des bugs en montrant des images à Gemini

Vous avez un bug dans votre UI ? Vous pouvez montrer des informations visuelles à Gemini pour aider au débogage :

```
gemini -p "Cette UI semble cassée. Qu'est-ce qui ne va pas et comment puis-je corriger ?" image.png
```

Gemini peut analyser les informations visuelles et vous dire :

-   Ce qui cause le problème.
    
-   Exactement quel code changer.
    
-   Parfois même de meilleures façons de le faire.
    

#### Transformer des diagrammes d'architecture en code

Dessinez un diagramme système et Gemini peut le construire :

```
gemini -p "Construis cette architecture système avec Docker et des bases de données" diagram.jpg
```

Gemini va :

-   Comprendre votre diagramme.
    
-   Créer tous les fichiers Docker dont vous avez besoin.
    
-   Configurer les bases de données et les connexions.
    
-   Vous donner un système fonctionnel basé sur votre design.
    

#### Pourquoi ce codage visuel est incroyable

Au lieu de passer des heures à traduire un design en code, vous pouvez :

1.  Montrer à Gemini votre croquis ou design.
    
2.  Demander à Gemini de le construire.
    
3.  Obtenir du code fonctionnel en quelques minutes au lieu de plusieurs heures et simplement l'affiner si nécessaire.
    

La plupart du temps, Gemini se rapproche assez de ce que vous vouliez dès le premier essai. Même quand ce n'est pas parfait, cela vous donne un excellent point de départ qui vous fait gagner énormément de temps.

### Étape 13 : Comparaison des outils CLI

Voici un tableau rapide pour vous aider à comparer les fonctionnalités de Claude Code et du CLI Gemini :

| **Fonctionnalité** | **Claude Code** | **CLI Gemini** |
| --- | --- | --- |
| **Fenêtre de contexte** | Large | 1M+ tokens |
| **Recherche Web** | Intégrée | Intégration Google Search |
| **Édition de fichiers** | Modifications directes | Basée sur les diffs |
| **Modes de réflexion** | 4 niveaux | Boucle ReAct |
| **Intégration IDE** | Raccourcis VS Code | Terminal d'abord |
| **Palier gratuit** | Limité | Généreux (1000/jour) |
| **Open Source** | Non | Oui |
| **Multimodal** | Non | Oui (images, PDFs) |

### Étape 14 : Workflows CLI avancés

#### Workflow 1 : Revue de code interactive avec Claude Code

```
Claude Code > revois mes changements git récents

[Claude analyse le diff]

Claude Code > corrige le problème de sécurité que tu as trouvé dans la fonction login

Claude Code > maintenant crée une pull request avec une bonne description
```

#### Workflow 2 : Analyse d'architecture conversationnelle avec Gemini

```
Gemini > analyse l'architecture de cette base de code et identifie la dette technique

[Gemini fournit une analyse complète]

Gemini > crée un plan de migration pour les problèmes de base de données que tu as trouvés

Gemini > génère la documentation API pour les points de terminaison
```

#### Workflow 3 : Développement piloté par les tests (TDD) interactif

```
Claude Code > Je dois ajouter le traitement des paiements. Commence par écrire des tests complets

[Claude crée la suite de tests]

Claude Code > maintenant implémente le service de paiement pour passer ces tests

Claude Code > ajoute la gestion d'erreurs et les cas limites
```

### Combiner VS Code avec les outils CLI

#### La puissance des workflows hybrides :

Les développeurs les plus productifs ne choisissent généralement pas un seul outil d'IA – ils combinent stratégiquement les extensions VS Code avec les outils CLI pour maximiser leur efficacité. Chaque outil a des forces uniques, et les combiner crée un workflow supérieur à la somme de ses parties.

**Avantages de la combinaison d'outils :**

-   **Changement de contexte fluide :** Commencez avec Copilot pour un développement rapide, puis passez sans effort à Claude Code pour une analyse complexe sans perdre votre élan.
    
-   **Forces complémentaires :** Utilisez les meilleures fonctionnalités de chaque outil, comme les suggestions en temps réel de Copilot + le raisonnement profond de Claude + le traitement visuel de Gemini.
    
-   **Workflow continu :** Pas besoin de copier/coller du code entre les outils - travaillez directement dans votre projet avec différentes assistances IA selon les besoins.
    
-   **Charge mentale réduite :** Les outils gèrent différentes tâches cognitives, vous permettant de vous concentrer sur la résolution créative de problèmes.
    

#### Comment combiner pratiquement les outils :

Exemple de workflow – construire un tableau de bord utilisateur :

1.  **Commencez dans VS Code avec Copilot :** Utilisez la complétion par tabulation pour construire rapidement la structure de base du composant.
    
2.  **Gardez VS Code ouvert, lancez Claude Code :** Obtenez des conseils architecturaux et des suggestions de refactorisation tout en conservant le contexte de votre éditeur.
    
3.  **Passez à Gemini pour les éléments visuels :** Téléchargez des maquettes d'UI pour générer les styles correspondants.
    
4.  **Revenez à VS Code :** Appliquez toutes les suggestions avec l'aide de Copilot pour les détails d'implémentation.
    

**Points d'intégration clés :**

-   **Contexte de projet partagé :** Tous les outils travaillent dans le même répertoire, comprenant la structure de votre projet.
    
-   **Coordination du système de fichiers :** Les modifications apportées par les outils CLI sont immédiatement visibles dans VS Code.
    
-   **Intégration du contrôle de version :** Utilisez les outils CLI pour les opérations git tandis que VS Code affiche les diffs visuels.
    

### Configuration du changement rapide

#### Qu'est-ce que le changement rapide ?

Une configuration de changement rapide consiste à configurer votre environnement de développement pour pouvoir passer rapidement d'un outil d'IA à l'autre sans friction. Au lieu de taper de longues commandes ou de naviguer dans plusieurs étapes de configuration, vous créez des raccourcis qui vous permettent d'accéder instantanément au bon outil d'IA pour votre tâche actuelle.

Ajoutez à la configuration de votre shell (`.zshrc` ou `.bashrc`) :

```
# Commandes IA rapides pour le mode interactif
alias cc="claude"
alias gc="gemini"

# Pour les commandes one-shot rapides si besoin
alias think="claude 'think hard:'"
alias analyze="gemini -p 'analyze:'"
```

### Exercices pratiques de l'étape 3

#### Exercice 1 : Configuration de projet interactive avec Claude Code

1.  Créez un nouveau répertoire de projet.
    
2.  Lancez : `claude`
    
3.  Commencez la conversation : "configure une API Node.js Express avec PostgreSQL"
    
4.  Continuez à discuter : "ajoute un middleware d'authentification"
    
5.  Poursuivez : "maintenant ajoute une gestion d'erreurs complète"
    
6.  Examinez le code généré et posez des questions.
    

#### Exercice 2 : Analyse de base de code interactive avec Gemini

1.  Naviguez vers un projet existant.
    
2.  Lancez : `gemini`
    
3.  Commencez par : "analyse cette base de code et identifie les vulnérabilités de sécurité potentielles"
    
4.  Suivez avec : "explique le problème le plus critique en détail"
    
5.  Continuez : "crée un correctif pour la vulnérabilité d'authentification"
    
6.  Demandez : "quelles autres améliorations devrais-je prioriser ?"
    

#### Exercice 3 : Workflow combiné interactif

1.  Commencez avec Copilot dans VS Code pour le développement initial.
    
2.  Passez à une session interactive Claude Code pour une refactorisation complexe.
    
3.  Utilisez une session interactive Gemini pour l'analyse de la base de code et la documentation.
    
4.  Entraînez-vous à passer fluidement d'un outil à l'autre.
    

Besoin d'aide avec les outils CLI ? Consultez la [Référence rapide de dépannage][20] pour la configuration et les problèmes courants.

## Étape 4 : Maîtrise – Combiner les outils et workflows avancés

### Étape 15 : Stratégie de sélection d'outils

#### Quand utiliser chaque outil

Très bien, alors quand devriez-vous utiliser chaque outil dans vos workflows ?

Vous pouvez utiliser GitHub Copilot comme un binôme programmeur inline quand la vitesse est primordiale. Il vous aide à produire de nouvelles fonctions, à obtenir des suggestions en temps réel pendant que vous tapez, et à appréhender des API ou des frameworks inconnus à la volée. Il est aussi pratique pour des recherches rapides de docs sans casser votre flux.

Ensuite, vous pouvez passer à Claude Code pour les travaux plus gros et plus complexes : refactorisations multi-fichiers complexes, rédaction de tests complets, et "réflexion à voix haute" sur l'architecture et les compromis. Ici, il aide aussi pour les tâches Git comme vous guider à travers les opérations et assembler des pull requests.

Enfin, vous pouvez solliciter le CLI Gemini depuis le terminal quand vous avez besoin d'analyser de grandes bases de code de bout en bout ou d'incorporer des entrées visuelles (comme des captures d'écran/diagrammes) dans votre workflow. Il est utile pour de nombreuses exécutions grâce à son palier gratuit, et il s'adapte aux scénarios où vous pourriez vouloir une configuration personnalisable et scriptable.

### Étape 16 : Comprendre le MCP – Faire travailler les outils d'IA ensemble

#### Qu'est-ce que le MCP ?

Le MCP (Model Context Protocol) est un moyen simple de donner des pouvoirs supplémentaires à vos outils d'IA. Considérez cela comme l'ajout d'applications à votre téléphone – chaque serveur MCP ajoute une nouvelle capacité à votre IA.

#### Pourquoi les débutants devraient-ils s'intéresser au MCP ?

Voici le problème sans MCP : votre IA ne peut travailler qu'avec ce qu'elle sait et ce que vous lui dites. Elle ne peut pas :

-   Chercher sur le Web des informations actuelles.
    
-   Tester votre site Web automatiquement.
    
-   Se souvenir des détails de votre projet entre les sessions.
    
-   Se connecter à vos bases de données ou API.
    

Mais avec les serveurs MCP, votre IA peut soudainement :

-   **Obtenir des informations actuelles** – Chercher sur Google les dernières docs et solutions.
    
-   **Tester votre code** – Vérifier automatiquement si votre site fonctionne.
    
-   **Se souvenir de votre projet** – Garder une trace de votre architecture et de vos décisions.
    
-   **Se connecter aux outils** – Travailler avec GitHub, les bases de données, et plus encore.
    

Ainsi, au lieu de faire manuellement des tâches répétitives, votre IA peut les gérer automatiquement. Cela signifie que vous passerez moins de temps à googler des messages d'erreur, à tester manuellement votre code et à expliquer votre projet à l'IA à chaque session. Et vous passerez plus de temps à construire réellement des choses.

#### Exemples simples de MCP pour débutants

Voici des exemples accessibles de ce que le MCP peut faire pour vous :

**Exemple 1 : Obtenir de l'aide sans googler**

```
Vous : "Ce CSS ne fonctionne pas. Trouve pourquoi et corrige-le"

Sans MCP : Vous googleriez l'erreur, liriez les docs, essayeriez des solutions.
Avec MCP : L'IA cherche les docs CSS actuelles, trouve le problème, le corrige automatiquement.
```

**Exemple 2 : Tester votre site Web automatiquement**

```
Vous : "Vérifie si mon formulaire de contact fonctionne réellement"

Sans MCP : Vous rempliriez manuellement le formulaire, vérifieriez l'email, testeriez les cas limites.
Avec MCP : L'IA remplit le formulaire, vérifie que l'email est envoyé, teste différentes entrées.
```

**Exemple 3 : L'IA se souvient de votre projet**

```
Vous : "Ajoute une nouvelle fonctionnalité à mon application todo"

Sans MCP : Vous expliquez votre structure de base de données, vos routes API, votre framework frontend.
Avec MCP : L'IA se souvient déjà de tout et construit simplement la fonctionnalité.
```

#### Prêt à essayer le MCP ?

Ne vous inquiétez pas si cela semble intimidant ! Vous pouvez commencer avec un seul serveur MCP simple et en ajouter d'autres au fur et à mesure que vous vous sentez à l'aise.

#### Configuration MCP facile pour débutants

Nous commencerons par VS Code (car c'est l'option la plus simple) :

1.  Ouvrez VS Code.
    
2.  Allez dans Extensions (Ctrl+Shift+X).
    
3.  Recherchez "GitHub Copilot MCP" ou des extensions MCP similaires.
    
4.  Cliquez sur "Installer".
    

Et c'est fini ! L'extension gère tout automatiquement.

Avec cela, vous obtenez une capacité de recherche Web pour votre IA, une mémoire de projet de base et des fonctionnalités d'automatisation simples.

Pour tester, demandez à votre IA : "Recherche les dernières meilleures pratiques React et montre-moi un exemple". Si elle peut chercher et ramener des informations actuelles, le MCP fonctionne !

#### Vous voulez plus de puissance MCP ?

Une fois que vous êtes à l'aise avec le MCP de base, vous pouvez explorer une configuration plus avancée ci-dessous :

-   Installation de serveur MCP personnalisé.
    
-   Options de configuration avancées.
    
-   Construction de vos propres intégrations MCP.
    

Pour l'instant, l'approche de l'extension VS Code ci-dessus vous donnera plein de super-pouvoirs IA pour commencer !

**C'est le MCP en résumé !** Commencez par l'approche simple de l'extension VS Code ci-dessus, et vous verrez rapidement à quel point votre IA devient plus puissante.

#### Prochaines étapes

-   Essayez l'extension MCP de base pour VS Code.
    
-   Testez-la avec des requêtes simples comme "recherche X et implémente-le".
    
-   Une fois à l'aise, explorez plus de serveurs MCP à l'étape 4.
    

Le MCP transforme votre IA d'un simple suggesteur de code en un véritable partenaire de développement. La meilleure partie ? Une fois configuré avec un outil, cela fonctionne avec tous les autres !

#### Le MCP ne fonctionne pas ?

Si l'IA dit qu'elle ne peut pas chercher sur le Web, il y a quelques choses que vous pouvez essayer.

D'abord, vérifiez si l'extension MCP est réellement installée dans VS Code. Ensuite, essayez de redémarrer VS Code. Enfin, assurez-vous de poser la question d'une manière que l'IA comprend : "Recherche X et montre-moi Y".

Si l'extension VS Code ne s'installe pas, essayez de vérifier votre connexion Internet ou de mettre à jour VS Code vers la dernière version. Vous pouvez aussi chercher des extensions "MCP" ou "Model Context Protocol" sous d'autres noms.

Si vous avez toujours des problèmes, nous couvrirons le dépannage avancé ci-dessous. Ou vous pouvez aussi demander à votre IA : "Aide-moi à dépanner la configuration MCP".

### Configuration et intégration MCP avancées

#### Installation manuelle de serveur MCP

Pour les utilisateurs avancés qui veulent un contrôle total sur leur configuration MCP :

**Étape 1 : Installer les serveurs MCP**

La plupart des serveurs MCP peuvent être installés via npm :

```
# Pour l'automatisation web et les tests
npm install -g @modelcontextprotocol/server-puppeteer

# Pour la recherche web sans clés API
npm install -g @mcp-servers/duckduckgo

# Pour l'accès aux bases de données
npm install -g @modelcontextprotocol/server-postgres
```

Certains serveurs (comme GitHub) utilisent Docker à la place :

```
docker pull ghcr.io/github/github-mcp-server
```

**Étape 2 : Configurer votre outil**

**Comprendre la configuration hiérarchique :**

Chaque outil d'IA vérifie les configurations MCP à plusieurs endroits, privilégiant les paramètres plus spécifiques aux paramètres généraux. Cela signifie que vous pouvez avoir des valeurs par défaut globales mais les écraser pour des projets spécifiques. Considérez cela comme du CSS – les règles plus spécifiques écrasent les générales.

**Claude Code a la configuration la plus flexible :**

Hiérarchie de configuration de Claude Code (vérifiée dans l'ordre) :

1.  **Niveau projet** : `.claude/mcp.json` (priorité la plus haute)
    
2.  **Paramètres locaux** : `.claude/settings.local.json`
    
3.  **Config globale** : `~/.claude/mcp.json` (repli)
    

Autres outils :

-   **VS Code** : `.vscode/mcp.json` (niveau projet uniquement)
    
-   **Cursor** : `.cursor/mcp.json` (niveau projet uniquement)
    
-   **Windsurf** : Utilise le format de configuration de VS Code
    

Voici un exemple de configuration (fonctionne dans n'importe quel outil, ajustez juste l'emplacement du fichier) :

```
{
  "mcpServers": {
    "puppeteer": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-puppeteer"]
    },
    "duckduckgo": {
      "command": "npx",
      "args": ["@mcp-servers/duckduckgo"]
    },
    "github": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "GITHUB_PERSONAL_ACCESS_TOKEN",
        "ghcr.io/github/github-mcp-server"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "votre_token_ici"
      }
    }
  }
}
```

#### Serveurs MCP de production

**1. Outils cognitifs révolutionnaires :**

**Serveur de pensée séquentielle (Sequential Thinking) :**  
Ce serveur transforme la façon dont l'IA aborde les problèmes complexes en les décomposant en étapes logiques. Lorsque vous demandez l'implémentation d'une grosse fonctionnalité, au lieu de sauter directement au code, l'IA crée d'abord un plan détaillé avec des phases, des dépendances et des points de décision.

C'est inestimable pour refactoriser des systèmes hérités ou construire de nouvelles fonctionnalités où l'ordre des opérations compte. Le serveur maintient ce contexte de planification tout au long de la session de développement, assurant une prise de décision cohérente.

**Serveur de banque de mémoire (Memory Bank) :**  
Élimine le besoin frustrant de ré-expliquer la structure de votre projet à chaque session. Ce serveur crée une mémoire persistante de vos choix d'architecture, standards de codage, préférences d'équipe et objectifs de projet. Quand vous revenez travailler quelques jours plus tard, l'IA connaît immédiatement votre schéma de base de données, vos patterns API, et même pourquoi certaines décisions ont été prises. C'est comme avoir un système de documentation de projet qui reste parfaitement synchronisé avec votre travail de développement.

**Serveur de graphe de connaissances (Knowledge Graph) :**  
Crée une carte vivante des relations de votre base de code – pas seulement les dépendances de fichiers, mais les connexions conceptuelles entre les fonctionnalités, les utilitaires partagés et les patterns architecturaux. Lorsque vous modifiez un composant, l'IA peut instantanément identifier toutes les zones liées qui pourraient nécessiter des mises à jour. Cela prévient les bugs causés par l'oubli de changements liés et aide à l'analyse d'impact lors de la refactorisation.

**2. Serveurs d'automatisation Web & de tests :**

**Serveur Puppeteer :**  
Fournit le contrôle du navigateur Chrome headless pour des workflows de tests complets. L'IA peut naviguer automatiquement dans votre application web, remplir des formulaires, cliquer sur des boutons et vérifier les comportements attendus.

C'est particulièrement puissant pour les tests de régression – l'IA peut rejouer les workflows utilisateurs et détecter les changements cassants avant le déploiement. Cela permet aussi l'automatisation des tests basés sur des captures d'écran et la surveillance des performances.

**Serveur Playwright :**  
Étend l'automatisation du navigateur à Chrome, Firefox et Safari simultanément. Ce serveur est essentiel pour les tests de compatibilité multi-navigateurs et permet à l'IA de détecter les problèmes spécifiques à certains navigateurs tôt dans le développement.

Contrairement aux tests manuels, l'IA peut exécuter des scénarios de test identiques sur tous les navigateurs en parallèle, générant des rapports comparatifs sur les différences de fonctionnalité et de performance.

**3. Serveurs d'intégration de développement :**

**Serveur GitHub :**  
Transforme votre terminal en une interface GitHub complète avec l'intelligence de l'IA. L'IA peut créer automatiquement des branches, gérer des pull requests, analyser les commentaires de revue de code, et même générer des descriptions de PR basées sur les changements de code. Elle peut aussi trier les issues, assigner des labels basés sur l'analyse du contenu, et maintenir les tableaux de projet en comprenant la relation entre les issues et les changements de code réels.

**Serveur de recherche DuckDuckGo :**  
Fournit un accès en temps réel à la documentation et aux solutions actuelles sans coûts d'API. Lorsque l'IA rencontre des erreurs ou a besoin de vérifier les meilleures pratiques, elle peut instantanément chercher les informations les plus récentes. C'est crucial pour les technologies qui évoluent rapidement où les données d'entraînement deviennent vite obsolètes. Le serveur aide aussi au dépannage en trouvant des solutions à des messages d'erreur que vous n'avez jamais vus.

**Serveur PostgreSQL :**  
Permet l'analyse et l'optimisation directe de la base de données. L'IA peut examiner les performances des requêtes, suggérer des optimisations d'index, analyser les patterns de données, et même générer des scripts de migration. Ce serveur est particulièrement précieux pour déboguer des problèmes de production où l'IA a besoin de comprendre la distribution réelle des données et les patterns d'exécution des requêtes plutôt que juste la conception théorique de la base de données.

**4. Outils d'aide :**

**MCP Compass**  
Vous aide à trouver le bon serveur MCP pour n'importe quelle tâche.

Ces serveurs transforment votre IA d'un suggesteur de code en un véritable partenaire de développement qui peut tester, chercher, se souvenir et automatiser !

### Étape 17 : Prompt Engineering avancé

#### Prompting contextuel

Fournissez des exemples :

```
// Au lieu de : "crée une fonction de validation"
// Utilisez : "crée une fonction de validation comme celle-ci mais pour l'email :
// function validatePhone(phone) { return /^\d{10}$/.test(phone); }"
```

Spécifiez les contraintes :

```
claude "refactorise ce code pour utiliser la programmation fonctionnelle, pas de boucles, utilise map/filter/reduce"
```

Incluez les cas limites :

```
gemini -p "implémente l'authentification utilisateur qui gère : les tokens expirés, les connexions simultanées, la limitation de débit"
```

### Étape 18 : Construire des pipelines de développement assistés par IA

#### Pipeline de revue de code automatisé

1.  Pre-commit avec Copilot :

```
// .copilot-instructions
"Revoir tous les changements pour : problèmes de sécurité, problèmes de performance, style de code";
```

2.  Revue de PR avec Claude :

```
claude "revois cette PR : git diff main..feature-branch"
```

3.  Documentation avec Gemini :

```
gemini -p "génère le changelog et mets à jour le README pour ces changements"
```

#### Développement IA piloté par les tests

1.  Écrire les spécifications de test :

```
claude "écris des specs de test complètes pour un système de traitement de paiement"
```

2.  Générer le code de test :

```
gemini -p "implémente ces spécifications de test en utilisant Jest"
```

3.  Implémenter avec Copilot :
    
    -   Utilisez le mode Agent pour implémenter les fonctionnalités.
        
    -   Les tests guident l'implémentation.
        

### Étape 19 : Créer votre workflow IA personnel

#### Configuration de votre environnement

1. Paramètres VS Code (`settings.json`) :

```
{
  "github.copilot.enable": {
    "*": true
  },
  "github.copilot.advanced": {
    "inlineCompletions.enable": true,
    "chat.enabled": true
  }
}
```

2. Configuration Claude Code (`~/.claude/settings.json`) :

```
{
  "cleanupPeriodDays": 7,
  "permissions": {
    "allow": [
      "Bash(fd:*)",
      "Bash(rg:*)",
      "Bash(ls:*)",
      "WebFetch(domain:github.com)",
      "WebFetch(domain:stackoverflow.com)"
    ],
    "deny": ["WebFetch(domain:medium.com)"]
  }
}
```

3. Configuration Gemini (`~/.gemini/config.json`) :

```
{
  "defaultModel": "gemini-2.5-pro",
  "contextWindow": "large",
  "safetyMode": "interactive"
}
```

#### Commandes personnalisées et alias

Alias de shell pour les tâches courantes :

```
# Lancer des sessions interactives
alias cc='claude'
alias gc='gemini'

# Commandes one-shot rapides (quand vous en avez besoin)
alias aicommit='claude "crée un commit git avec un message descriptif"'
alias aireview='claude "revois mes changements non commités"'
alias complexity='gemini -p "analyse la complexité du code et suggère des simplifications"'
alias security='claude "think harder: vérifie les vulnérabilités de sécurité"'
alias aidocs='gemini -p "génère une documentation complète"'
```

### Projet final : Construire une application complète avec l'IA

#### Exigences du projet

Construire une API de gestion de tâches avec :

-   Authentification utilisateur
    
-   Opérations CRUD
    
-   Mises à jour en temps réel
    
-   Suite de tests
    
-   Documentation
    

#### Workflow suggéré

Phase 1 : Planification interactive

```
# Démarrer la session Claude Code
claude

Claude Code > ultrathink: conçois une architecture d'API de gestion de tâches évolutive

[Claude fournit une analyse détaillée]

Claude Code > maintenant décompose cela en phases d'implémentation

# Passer à Gemini pour les spécifications
gemini

Gemini > crée des spécifications techniques détaillées pour cette API de gestion de tâches

Gemini > inclus le schéma de base de données et les spécifications des points de terminaison API
```

Phase 2 : Implémentation interactive

1.  Utilisez le mode Agent de Copilot pour la configuration initiale.
    
2.  Implémentez les fonctionnalités avec Copilot inline.
    
3.  Passez à une session interactive Claude Code pour la logique complexe :
    

```
Claude Code > implémente le système d'authentification utilisateur que nous avons planifié

Claude Code > maintenant ajoute les opérations CRUD de tâches

Claude Code > intègre les mises à jour en temps réel avec WebSockets
```

Phase 3 : Tests & Documentation interactifs

```
# Session Claude Code pour les tests
claude

Claude Code > écris des tests complets pour tous les points de terminaison API

Claude Code > ajoute des tests d'intégration pour le flux d'authentification

Claude Code > crée des tests de performance pour des scénarios de charge élevée

# Session Gemini pour la documentation
gemini

Gemini > génère une documentation API complète avec des exemples

Gemini > crée un guide d'intégration pour les développeurs
```

Phase 4 : Optimisation interactive

```
# Claude Code pour l'optimisation des performances
claude

Claude Code > analyse et optimise nos requêtes de base de données

Claude Code > implémente la mise en cache pour les données fréquemment consultées

Claude Code > ajoute la surveillance et la journalisation

# Gemini pour la revue finale
gemini

Gemini > revois toute la base de code pour des améliorations

Gemini > identifie les vulnérabilités de sécurité potentielles

Gemini > suggère des optimisations de déploiement
```

### Mesurer votre progression

#### Jalons de l'étape 1

-   À l'aise avec la complétion par tabulation.
    
-   Peut écrire des prompts efficaces.
    
-   Comprend les limites de l'IA.
    

#### Jalons de l'étape 2

-   Utilise plusieurs modèles efficacement.
    
-   Maîtrise les modes de chat et les agents.
    
-   Utilise les fonctionnalités de chat avancées.
    

#### Jalons de l'étape 3

-   Fluide avec les outils CLI.
    
-   Peut combiner les workflows VS Code et terminal.
    
-   Comprend les forces de chaque outil.
    

#### Jalons de l'étape 4

-   A créé un workflow IA personnalisé.
    
-   A construit une application complète avec l'IA.
    
-   Peut enseigner le développement assisté par IA à d'autres.
    

### Exercices pratiques de l'étape 4

#### Exercice 1 : Maîtrise de la sélection d'outils

1.  Choisissez une tâche de codage de complexité moyenne (par exemple, "Construire une API de réduction d'URL").
    
2.  Planifiez quel outil utiliser pour chaque phase (conception, codage, tests, déploiement).
    
3.  Exécutez en utilisant votre workflow choisi.
    
4.  Documentez ce qui a bien fonctionné et ce que vous changeriez.
    

#### Exercice 2 : Création de workflow personnalisé

1.  Identifiez une tâche de développement répétitive dans votre travail.
    
2.  Concevez un workflow assisté par IA utilisant plusieurs outils.
    
3.  Testez et affinez le workflow.
    
4.  Créez une documentation pour vos coéquipiers.
    

#### Exercice 3 : Construction de projet complet

1.  Construisez une petite application complète en utilisant uniquement l'assistance IA.
    
2.  Utilisez au moins 2 outils d'IA différents de manière stratégique.
    
3.  Incluez les tests, la documentation et le déploiement.
    
4.  Réfléchissez aux gains de productivité par rapport au développement traditionnel.
    

### Continuer votre voyage

#### Rester à jour

-   Suivez les notes de version des outils.
    
-   Rejoignez des communautés de codage IA.
    
-   Expérimentez les nouvelles fonctionnalités.
    

#### Sujets avancés à explorer

-   Développement de serveur MCP personnalisé.
    
-   Fine-tuning de modèles d'IA.
    
-   Stratégies de déploiement en entreprise.
    
-   Patterns de collaboration en équipe.
    

#### Ressources pour l'apprentissage continu

-   Documentation officielle pour chaque outil.
    
-   Forums communautaires et serveurs Discord.
    
-   Projets de codage IA open-source.
    
-   Conférences et tutoriels.
    

## Problèmes courants liés à l'IA

Même avec les meilleurs outils d'IA, vous rencontrerez des défis. Ces problèmes sont normaux et gérables une fois que vous comprenez leurs patterns. Voici les problèmes les plus courants auxquels les développeurs font face et des solutions pratiques qui fonctionnent réellement.

### "Mes suggestions d'IA sont terribles !"

**Problème :** L'IA donne des suggestions non pertinentes ou erronées.

**Solution :**

-   Écrivez des commentaires plus clairs.
    
-   Ouvrez les fichiers liés pour le contexte.
    
-   Commencez par des tâches plus simples.
    
-   Assurez-vous d'être dans le bon type de fichier.
    

**Exemple de correction :**

```
// Au lieu de : "make function"
// Essayez : "create function to validate US phone number format (xxx) xxx-xxxx"
```

### "L'IA est trop lente"

**Problème :** Attente trop longue pour les suggestions.

**Solution :**

-   Vérifiez votre connexion Internet.
    
-   Fermez les programmes inutiles.
    
-   Essayez un outil d'IA plus léger.
    
-   Soyez patient – les suggestions complexes prennent du temps.
    

### "J'ai peur de devenir dépendant de l'IA"

**Problème :** Inquiétude de perdre ses compétences en codage.

**Solution :**

-   Utilisez l'IA comme un outil d'apprentissage, pas comme une béquille.
    
-   Comprenez toujours le code avant de l'accepter.
    
-   Pratiquez régulièrement le codage sans IA.
    
-   Concentrez-vous sur la résolution de problèmes, pas sur la syntaxe.
    

### "Elle suggère du code obsolète"

**Problème :** L'IA suggère de vieux patterns ou des méthodes dépréciées.

**Solution :**

-   Spécifiez les versions dans vos commentaires.
    
-   Gardez vos outils à jour.
    
-   Apprenez à reconnaître les patterns obsolètes.
    

**Exemple :**

```
// create React functional component using hooks (not class component)
```

### Référence rapide de dépannage

#### Problèmes courants (Tous outils)

| **Problème** | **Correction rapide** |
| --- | --- |
| Pas de suggestions IA | Vérifier la connexion, redémarrer l'éditeur, vérifier la connexion au compte |
| Message "Besoin de payer" | Vérifier les limites du palier gratuit, vérifier le statut du compte |
| Suggestions médiocres | Utiliser des commentaires plus clairs, ouvrir les fichiers liés pour le contexte |
| L'outil ne s'installe pas | Mettre à jour l'éditeur, vérifier Internet, essayer une autre méthode d'installation |

#### Problèmes GitHub Copilot

| **Problème** | **Solution** |
| --- | --- |
| Pas de suggestions dans VS Code | Vérifier le statut "GitHub Copilot" en bas à droite |
| Palier gratuit expiré | Vérifier l'[accès gratuit pour étudiants/mainteneurs][21] |
| Mode Agent ne fonctionne pas | Essayer `Shift+Cmd+I` (Mac) ou `Ctrl+Shift+I` (Windows/Linux) |
| Le Chat ne répond pas | Essayer de redémarrer VS Code, vérifier la connexion Internet |

#### Problèmes Claude Code

| **Problème** | **Solution** |
| --- | --- |
| "Command not found" | Réinstaller : `npm uninstall -g @anthropic-ai/claude-code && npm install -g @anthropic-ai/claude-code` |
| Échec d'authentification | Lancer `claude auth login`, vérifier les crédits API restants |
| Réponses lentes | Vérifier le réseau : `ping api.anthropic.com`, essayer un modèle plus léger avec `--model claude-3-haiku` |
| Serveurs MCP ne fonctionnent pas | Vérifier la syntaxe de `~/.claude/mcp.json`, tester le serveur : `npx @mcp/server-github --help` |
| Commandes bloquées/gelées | Appuyer sur `Ctrl+C` pour annuler, redémarrer le terminal, vérifier les processus en arrière-plan |

#### Problèmes CLI Gemini

| **Problème** | **Solution** |
| --- | --- |
| Authentification requise | Lancer `gemini auth login`, vérifier les permissions du compte Google |
| Limite de débit dépassée | Vérifier l'usage : `gemini /stats`, attendre 1 minute ou monter de forfait |
| Ne s'installe pas | Essayer `npx @google/gemini-cli` à la place, vérifier Node.js 16+ |
| Échec téléchargement image | Vérifier le format (JPG/PNG/WebP), taille < 20 Mo, vérifier le chemin du fichier |
| Erreurs de fenêtre de contexte | Diviser les grosses requêtes en morceaux plus petits, effacer l'historique |

### Checklist d'urgence

Quand rien ne fonctionne, essayez ceci dans l'ordre :

1.  Redémarrez votre éditeur/terminal.
    
2.  Vérifiez la connexion Internet.
    
3.  Vérifiez que vous êtes connecté au bon compte.
    
4.  Mettez à jour vers la dernière version de l'outil.
    
5.  Essayez un autre outil (si l'un échoue, les autres fonctionnent généralement).
    
6.  Demandez à l'IA elle-même : "Aide-moi à dépanner la configuration de l'outil [nom de l'outil]".
    

## Et après avoir terminé toutes les étapes ?

Une fois que vous maîtrisez les bases, voici quelques étapes simples pour la suite :

### Travailler avec votre équipe

#### Bases du workflow IA en équipe

**Bibliothèques de prompts partagées :**

Construire une bibliothèque de prompts d'équipe transforme la façon dont toute votre équipe utilise l'IA. Commencez par créer un dépôt partagé où les développeurs documentent les prompts qui fonctionnent bien pour votre domaine et votre base de code spécifiques.

Par exemple, si vous construisez un logiciel d'e-commerce, créez des prompts standardisés pour des tâches courantes comme "générer des points de terminaison API de catalogue de produits suivant nos conventions REST" ou "créer une gestion d'erreurs de traitement de paiement utilisant nos patterns standards."

Documentez les workflows réussis du mode Agent que les membres de l'équipe peuvent réutiliser. Un développeur pourrait découvrir que Claude Code fonctionne particulièrement bien pour les migrations de base de données lorsqu'on lui donne un contexte spécifique sur vos pratiques d'évolution de schéma. En partageant ces workflows, vous évitez à chaque membre de l'équipe de devoir découvrir des approches efficaces indépendamment.

**Standardisation des outils :**

La productivité de l'équipe se multiplie quand tout le monde utilise des outils d'IA compatibles. Mettez-vous d'accord sur les outils principaux basés sur les besoins de votre équipe – par exemple, GitHub Copilot pour tous les développeurs pour assurer une assistance inline cohérente, plus Claude Code pour les tâches architecturales complexes qui bénéficient d'un raisonnement profond. Établissez des directives claires sur quand utiliser le mode Agent autonome par rapport aux sessions collaboratives pour prévenir les conflits et assurer la qualité du code.

Configurez des serveurs MCP partagés qui donnent à tous les membres de l'équipe accès aux mêmes capacités d'IA améliorées. Cela pourrait inclure des serveurs spécifiques à l'équipe pour vos API internes, un accès partagé aux bases de données, ou des outils personnalisés qui comprennent votre pipeline de déploiement. Quand tout le monde a les mêmes capacités d'IA, la collaboration devient fluide.

**Revues de code généré par IA :**

Transformez votre processus de revue de code pour travailler efficacement avec le code généré par IA. Établissez des conventions pour taguer les sections générées par IA dans les pull requests – cela aide les relecteurs à concentrer leur attention de manière appropriée. Au lieu de pinailler sur la syntaxe que l'IA gère généralement bien, les relecteurs peuvent se concentrer sur les décisions architecturales, la justesse de la logique métier et les patterns d'intégration qui nécessitent un jugement humain.

Implémentez des tests rigoureux pour le code généré par IA, car les tests automatisés détectent les erreurs d'IA plus fiablement que la revue manuelle. Créez des standards d'équipe pour tester la sortie de l'IA, incluant les cas limites et les scénarios d'intégration que l'IA pourrait manquer. Cela vous permet de bénéficier de la vitesse de l'IA tout en maintenant la qualité grâce à une vérification systématique.

**Documentez les décisions relatives aux outils d'IA** dans les messages de commit.

#### Configuration d'équipe simple

Commencez petit et progressez :

-   Faites en sorte que tout le monde utilise les mêmes outils d'IA d'abord.
    
-   Créez un document partagé de prompts qui fonctionnent bien pour vos projets.
    
-   Déterminez quand votre équipe devrait utiliser le mode Agent par rapport à l'assistance régulière.
    
-   Configurez des serveurs MCP pour vos outils d'équipe les plus importants.
    

### Pour les plus gros projets

Au fur et à mesure que vos projets grandissent, vous pourriez vouloir :

-   Essayer différents modèles d'IA pour différentes tâches (des rapides pour le code simple, des puissants pour les problèmes complexes).
    
-   Créer des raccourcis pour les tâches que vous faites souvent.
    
-   Connecter les outils d'IA avec votre workflow de développement existant.
    

### Continuer d'apprendre

Les outils de codage IA s'améliorent chaque mois ! Restez à jour en :

-   Suivant les notes de version des outils (ils envoient des mises à jour par email).
    
-   Rejoignant des communautés Discord pour le codage IA.
    
-   Essayant les nouvelles fonctionnalités dès qu'elles sortent.
    

## Conclusion

Félicitations ! Vous avez maintenant tout ce dont vous avez besoin pour commencer votre voyage dans le codage assisté par IA. Rappelez-vous, chaque expert a été un jour un débutant, et avec l'IA comme partenaire de codage, vous pouvez apprendre et grandir plus vite que jamais.

**Rappelez-vous :**

-   L'IA ne remplace pas votre créativité – elle l'amplifie.
    
-   Chaque suggestion est une opportunité d'apprentissage.
    
-   Les erreurs font partie du voyage.
    
-   La communauté est là pour aider.
    

Vous n'apprenez pas seulement à coder avec l'IA – vous apprenez le futur du développement logiciel. Dans quelques mois, vous vous demanderez comment vous avez pu coder sans elle. Les développeurs qui adoptent l'assistance de l'IA aujourd'hui seront les leaders de demain.

Bon codage ! 🚀

[1]: #heading-terminologie-essentielle-de-l-ia
[2]: #heading-quand-utiliser-l-ia-vs-quand-coder-soi-meme
[3]: #heading-prerequis
[4]: #heading-votre-parcours-d-apprentissage-complet
[5]: #heading-comment-generer-votre-premier-code-assiste-par-ia-demarrage-rapide
[6]: #heading-etape-1-fondations-debuter-avec-le-codage-par-ia
[7]: #heading-etape-2-fonctionnalites-avancees-de-github-copilot
[8]: #heading-etape-3-agents-ia-bases-sur-le-cli-claude-code-amp-gemini
[9]: #heading-etape-4-maitrise-combiner-les-outils-et-workflows-avances
[10]: #heading-problemes-courants-lies-a-l-ia
[11]: #heading-et-apres-avoir-termine-toutes-les-etapes
[12]: #heading-conclusion
[13]: http://code.visualstudio.com/
[14]: https://docs.github.com/en/copilot/how-tos/manage-your-account/getting-free-access-to-copilot-pro-as-a-student-teacher-or-maintainer
[15]: https://code.visualstudio.com/
[16]: http://github.com/
[17]: http://localhost:3333/#troubleshooting-quick-reference
[18]: http://localhost:3333/#troubleshooting-quick-reference
[19]: http://copilot-instructions.md/
[20]: http://localhost:3333/#troubleshooting-quick-reference
[21]: https://docs.github.com/en/copilot/how-tos/manage-your-account/getting-free-access-to-copilot-pro-as-a-student-teacher-or-maintainer