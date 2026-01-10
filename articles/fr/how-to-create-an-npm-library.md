---
title: Comment créer une bibliothèque npm
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2025-02-07T15:33:19.302Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-npm-library
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738941301640/7189d889-387d-4bd2-bf5c-2cbcbd17faad.png
tags:
- name: npm
  slug: npm
- name: Yarn
  slug: yarn
- name: software development
  slug: software-development
seo_title: Comment créer une bibliothèque npm
seo_desc: In the world of JavaScript development, npm (Node Package Manager) has become
  an essential tool for managing dependencies and sharing reusable code. Whether you're
  building a simple website or a complex web application, npm libraries help streamline
  ...
---

Dans le monde du développement JavaScript, **npm** (Node Package Manager) est devenu un outil essentiel pour gérer les dépendances et partager du code réutilisable. Que vous construisiez un simple site web ou une application web complexe, les bibliothèques npm aident à rationaliser le développement en fournissant des solutions pré-construites à des problèmes courants.

Un autre gestionnaire de paquets populaire est **Yarn**, qui offre une gestion des dépendances plus rapide et plus fiable tout en maintenant la compatibilité avec l'écosystème npm.

Dans cet article, nous allons explorer ce que sont les bibliothèques npm, leurs avantages et comment elles améliorent l'écosystème JavaScript et React. Nous allons également passer par un guide pratique étape par étape sur la création, la publication et l'utilisation de votre propre bibliothèque npm dans un projet React. Nous comparerons également npm et Yarn, montrant comment vous pouvez utiliser l'un ou l'autre efficacement dans votre flux de travail.

À la fin de ce tutoriel, vous aurez une compréhension claire de la manière d'empaqueter et de distribuer votre propre code, le rendant réutilisable dans plusieurs projets et même disponible pour la communauté des développeurs.

## **Table des matières**

1. [Qu'est-ce que npm ?](#heading-quest-ce-que-npm)
    
    * [Comment npm fonctionne](#heading-comment-npm-fonctionne)
        
    * [Le rôle du fichier `package.json`](#heading-le-role-du-fichier-packagejson)
        
    * [Commandes npm clés](#heading-commandes-npm-cles)
        
2. [Pourquoi utiliser les bibliothèques npm ?](#heading-pourquoi-utiliser-les-bibliotheques-npm)
    
    * [Réutilisation et modularisation du code](#heading-reutilisation-et-modularisation-du-code)
        
    * [Gestion simplifiée des dépendances](#heading-gestion-simplifiee-des-dependances)
        
    * [Écosystème piloté par la communauté](#heading-ecosysteme-pilote-par-la-communaute)
        
3. [Présentation de Yarn : une alternative à npm](#heading-presentation-de-yarn-une-alternative-a-npm)
    
    * [Qu'est-ce que Yarn ?](#heading-quest-ce-que-yarn)
        
    * [Différences entre npm et Yarn](#heading-differences-entre-npm-et-yarn)
        
    * [Quand utiliser Yarn au lieu de npm](#heading-quand-utiliser-yarn-au-lieu-de-npm)
        
4. [Comment créer votre propre bibliothèque npm](#heading-comment-creer-votre-propre-bibliotheque-npm)
    
    * [Configuration d'un nouveau package](#heading-installation-dun-nouveau-package)
        
    * [Écriture de code modulaire et réutilisable](#heading-ecriture-de-code-modulaire-et-reutilisable)
        
    * [Ajout de dépendances et de dépendances peer](#heading-ajout-de-dependances-et-de-dependances-peer)
        
5. [Comment publier votre bibliothèque sur npm](#heading-comment-publier-votre-bibliotheque-sur-npm)
    
    * [Création d'un compte npm](#heading-creation-dun-compte-npm)
        
    * [Configuration de package.json pour la publication](#heading-configuration-de-packagejson-pour-la-publication)
        
    * [Publication du package](#heading-publication-du-package)
        
6. [Comment utiliser votre bibliothèque npm dans un projet React](#heading-comment-utiliser-votre-bibliotheque-npm-dans-un-projet-react)
    
    * [Installation de votre package](#heading-installation-de-votre-package)
        
    * [Importation et utilisation du package dans un composant React](#heading-importation-et-utilisation-de-la-bibliotheque-dans-un-composant-react)
        
    * [Gestion des mises à jour et du versionnage du package](#heading-gestion-des-mises-a-jour-et-du-versionnage-du-package)
        
7. [Bonnes pratiques pour les bibliothèques npm et Yarn](#heading-bonnes-pratiques-pour-les-bibliotheques-npm-et-yarn)
    
    * [Écrire une documentation significative](#heading-ecrire-une-documentation-significative)
        
    * [Suivre le versionnage sémantique (SemVer)](#heading-suivre-le-versionnage-semantique-semver)
        
    * [Maintenir les dépendances à jour](#heading-maintenir-les-dependances-a-jour)
        
    * [Écrire des tests unitaires pour votre bibliothèque](#heading-ecrire-des-tests-unitaires-pour-votre-bibliotheque)
        
    * [Assurer la compatibilité multiplateforme](#heading-assurer-la-compatibilite-multiplateforme)
        
8. [Conclusion & Prochaines étapes](#heading-conclusion)
    
    * [Récapitulatif des points clés](#heading-recapitulatif-des-points-cles)
        
    * [Ressources supplémentaires pour le développement de bibliothèques npm et Yarn](#heading-ressources-supplementaires)
        
    * [Encouragement à contribuer à l'open-source](#heading-encouragement-a-contribuer-a-lopen-source)
        

## **Qu'est-ce que npm ?**

npm (Node Package Manager) est le gestionnaire de paquets par défaut pour JavaScript et Node.js. Il permet aux développeurs d'installer, de partager et de gérer des bibliothèques ou des dépendances qui rendent la construction d'applications plus facile et plus efficace.

npm fournit un accès à un vaste écosystème de paquets open-source hébergés sur le **registre npm**, ce qui en fait l'un des plus grands dépôts de logiciels au monde.

npm est fourni avec **Node.js**, ce qui signifie que dès que vous installez Node.js, vous avez automatiquement accès à npm. Vous pouvez vérifier si npm est installé en exécutant la commande suivante dans votre terminal :

```python
npm -v
```

Cette commande doit retourner la version de npm installée sur votre système.

### **Comment npm fonctionne**

npm fonctionne à travers trois composants clés :

1. **Le registre npm** – Un dépôt public qui héberge des paquets JavaScript open-source.
    
2. **L'interface en ligne de commande npm (CLI)** – Un outil qui permet aux développeurs d'installer, de mettre à jour et de gérer des paquets à partir de la ligne de commande.
    
3. **Le fichier package.json** – Un fichier de métadonnées qui garde une trace des dépendances, des scripts et des configurations de projet.
    

Lorsque vous installez un paquet en utilisant npm, il récupère le paquet depuis le registre et l'enregistre dans le dossier `node_modules` au sein de votre projet.

Par exemple, pour installer **Lodash**, une bibliothèque d'utilitaires populaire, vous exécuteriez :

```python
npm install lodash
```

Cela va :

* Télécharger la dernière version de `lodash` depuis le registre npm
    
* L'ajouter à votre dossier `node_modules`
    
* Mettre à jour les fichiers `package.json` et `package-lock.json` pour refléter la nouvelle dépendance
    

### **Le rôle du fichier** `package.json`

Le fichier `package.json` est le cœur de tout projet npm. Il sert de plan, contenant des informations sur le projet, y compris :

* **Métadonnées du projet** (nom, version, description)
    
* **Dépendances** (paquets externes requis pour le projet)
    
* **Scripts** (commandes pour automatiser des tâches comme démarrer un serveur ou exécuter des tests)
    
* **Informations de versionnage** (assurant la compatibilité entre différentes versions de dépendances)
    

Un fichier `package.json` typique ressemble à ceci :

```json
{
  "name": "my-awesome-project",
  "version": "1.0.0",
  "description": "Un projet d'exemple démontrant l'utilisation de npm",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "test": "echo \"No tests specified\" && exit 0"
  },
  "dependencies": {
    "lodash": "^4.17.21"
  },
  "devDependencies": {
    "eslint": "^8.0.0"
  },
  "author": "Votre Nom",
  "license": "MIT"
}
```

* `dependencies` – Liste les paquets essentiels requis pour que l'application fonctionne.
    
* `devDependencies` – Inclut les dépendances uniquement pour le développement (par exemple, outils de test et de linting).
    
* `scripts` – Définit les commandes CLI pour automatiser les tâches.
    

Pour installer toutes les dépendances listées dans `package.json`, exécutez simplement :

```python
npm install
```

Cela garantit que tous les paquets requis sont téléchargés et prêts à être utilisés.

### **Commandes npm clés**

Voici quelques commandes npm essentielles que vous utiliserez fréquemment :

| Commande | Description |
| --- | --- |
| `npm init -y` | Crée un fichier `package.json` par défaut |
| `npm install <nom-du-package>` | Installe un package et l'ajoute à `dependencies` |
| `npm install <nom-du-package> --save-dev` | Installe un package et l'ajoute à `devDependencies` |
| `npm uninstall <nom-du-package>` | Supprime un package du projet |
| `npm update` | Met à jour toutes les dépendances installées |
| `npm outdated` | Vérifie les dépendances obsolètes |
| `npm run <nom-du-script>` | Exécute un script défini dans `package.json` |

## **Pourquoi utiliser les bibliothèques npm ?**

Alors que le développement web moderne devient de plus en plus complexe, l'utilisation de bibliothèques npm est devenue essentielle pour construire des applications évolutives et maintenables. Au lieu d'écrire tout à partir de zéro, vous pouvez tirer parti de bibliothèques pré-construites, testées et optimisées pour accélérer le développement et garantir la fiabilité.

Dans cette section, nous allons explorer les principaux avantages de l'utilisation des bibliothèques npm et pourquoi elles sont cruciales dans le développement JavaScript et React.

### **Réutilisation et modularisation du code**

L'un des plus grands avantages des bibliothèques npm est la **réutilisation du code**. Au lieu d'écrire à plusieurs reprises les mêmes fonctions ou utilitaires dans différents projets, les développeurs peuvent :

* ✅ Utiliser des paquets open-source existants pour des fonctionnalités courantes (par exemple, formatage de dates, requêtes HTTP, composants UI).
    
* ✅ Créer et publier leurs propres bibliothèques réutilisables pour les partager dans plusieurs projets.
    

Par exemple, au lieu d'implémenter manuellement une fonction pour formater des dates, vous pouvez installer un paquet bien maintenu comme date-fns :

```python
npm install date-fns
```

Ensuite, vous pouvez l'utiliser dans votre projet :

```javascript
import { format } from "date-fns";

const formattedDate = format(new Date(), "yyyy-MM-dd");
console.log(formattedDate); // Affiche : 2024-02-04 (ou la date actuelle)
```

Cette approche modulaire économise du temps et assure la cohérence entre les projets.

### **Gestion simplifiée des dépendances**

npm facilite la gestion des dépendances dans un projet. Au lieu de télécharger et de maintenir manuellement différentes versions de bibliothèques externes, npm automatise ce processus grâce aux fichiers package.json et package-lock.json.

Quelques fonctionnalités clés incluent :

🔹 **Installation automatique** – Exécutez `npm install`, et toutes les dépendances sont configurées.  
🔹 **Contrôle de version** – Spécifiez les versions des paquets pour éviter les changements cassants.  
🔹 **Dépendances peer** – Assurez la compatibilité entre différentes bibliothèques.

Par exemple, voici comment npm aide à gérer les versions des dépendances dans `package.json` :

```json
"dependencies": {
  "react": "^18.0.0",
  "axios": "^1.5.0"
}
```

* `^18.0.0` – Permet les mises à jour mineures mais empêche les changements majeurs cassants.
    
* `axios` – Assure que les requêtes HTTP sont gérées de manière cohérente dans différents projets.
    

Pour mettre à jour toutes les dépendances en toute sécurité, exécutez :

```python
npm update
```

Cela garantit que votre projet fonctionne toujours avec les dernières versions stables.

### **Écosystème piloté par la communauté**

npm dispose d'une communauté active et en croissance, ce qui signifie que des développeurs du monde entier contribuent et maintiennent des milliers de bibliothèques utiles. Cela se traduit par :

🌏 **Développement plus rapide** – Pas besoin de réinventer la roue.  
🏢 **Solutions bien testées** – De nombreuses bibliothèques sont testées en production.  
📚 **Documentation riche** – La plupart des paquets npm sont livrés avec des instructions claires et des exemples d'utilisation.

Les bibliothèques npm populaires incluent :

| Bibliothèque | Objectif |
| --- | --- |
| **React** (`react`) | Bibliothèque UI pour construire des applications web |
| **Axios** (`axios`) | Client HTTP pour faire des requêtes API |
| **Lodash** (`lodash`) | Fonctions utilitaires pour travailler avec des tableaux, objets et chaînes |
| **Express** (`express`) | Framework web pour construire des services backend |
| **Jest** (`jest`) | Framework de test JavaScript |

Par exemple, utiliser **Axios** pour faire une requête API :

```javascript
import axios from "axios";

axios.get("https://jsonplaceholder.typicode.com/posts/1")
  .then(response => console.log(response.data))
  .catch(error => console.error(error));
```

Cela remplace le besoin d'écrire des requêtes `fetch` complexes avec une gestion d'erreurs manuelle.

## **Présentation de Yarn : une alternative à npm**

Alors que **npm** est le gestionnaire de paquets par défaut pour Node.js, une autre alternative puissante existe : **Yarn**. Développé par Facebook en 2016, Yarn a été créé pour améliorer la vitesse, la sécurité et la fiabilité dans la gestion des dépendances.

Dans cette section, nous allons explorer ce qu'est Yarn, comment il diffère de npm, et quand vous pourriez préférer utiliser Yarn plutôt que npm.

### **Qu'est-ce que Yarn ?**

Yarn (**Yet Another Resource Negotiator**) est un gestionnaire de paquets qui fonctionne de manière similaire à npm mais avec un accent sur la performance, la sécurité et la cohérence. Il offre :

🚀 **Installation des dépendances plus rapide** grâce aux téléchargements parallèles  
🔐 **Gestion des paquets plus sécurisée** en utilisant la vérification des sommes de contrôle  
📦 **Résolution des dépendances fiable** avec un cache hors ligne

Pour vérifier si vous avez Yarn installé, exécutez :

```python
yarn -v
```

Si vous ne l'avez pas encore, vous pouvez l'installer globalement en utilisant npm :

```python
npm install --global yarn
```

Une fois installé, vous pouvez l'utiliser comme npm pour gérer les dépendances.

### **Différences entre npm et Yarn**

Bien que npm et Yarn servent le même but, ils ont quelques différences clés :

| Fonctionnalité | npm | Yarn |
| --- | --- | --- |
| **Vitesse** | Installe les paquets un par un | Installe plusieurs paquets en parallèle (plus rapide) |
| **Fichier de verrouillage** | `package-lock.json` | `yarn.lock` |
| **Cache hors ligne** | Non disponible (par défaut) | Peut installer des paquets depuis le cache local |
| **Sécurité** | Vérifie l'intégrité des paquets mais manque de vérification des sommes de contrôle | Utilise la vérification des sommes de contrôle pour la sécurité |
| **Support Monorepo** | Supporte les workspaces mais pas optimisé | Support intégré pour les monorepos avec `workspaces` |

#### **Comparaison de performance**

Lors de l'installation des dépendances, Yarn est souvent plus rapide car il télécharge les paquets en parallèle, tandis que npm les installe séquentiellement.

Par exemple, pour installer toutes les dépendances dans un projet :

```python
# Avec npm
npm install

# Avec Yarn
yarn install
```

Yarn peut également installer des paquets à partir d'un cache local, ce qui signifie qu'il n'a pas toujours besoin de récupérer les dépendances depuis Internet.

#### **Commandes Yarn courantes vs. npm**

De nombreuses commandes npm ont un équivalent dans Yarn :

| Action | Commande npm | Commande Yarn |
| --- | --- | --- |
| Initialiser un nouveau projet | `npm init` | `yarn init` |
| Installer toutes les dépendances | `npm install` | `yarn install` |
| Installer un paquet | `npm install nom-du-paquet` | `yarn add nom-du-paquet` |
| Installer une dépendance de développement | `npm install nom-du-paquet --save-dev` | `yarn add nom-du-paquet --dev` |
| Supprimer un paquet | `npm uninstall nom-du-paquet` | `yarn remove nom-du-paquet` |
| Mettre à jour tous les paquets | `npm update` | `yarn upgrade` |
| Exécuter un script | `npm run nom-du-script` | `yarn nom-du-script` |

Par exemple, installer `axios` en utilisant Yarn :

```python
yarn add axios
```

### **Quand utiliser Yarn au lieu de npm**

Yarn est un excellent choix lorsque :

* **Vous voulez des installations plus rapides** – Yarn installe plusieurs paquets en parallèle, ce qui le rend plus rapide que npm.
    
* **Vous avez besoin d'une meilleure cohérence des dépendances** – Le fichier `yarn.lock` garantit que tous les développeurs utilisent les mêmes versions de dépendances.
    
* **Vous travaillez avec des monorepos** – Les **workspaces** intégrés de Yarn facilitent la gestion de plusieurs projets au sein du même dépôt.
    
* **Vous voulez une sécurité améliorée** – La vérification des sommes de contrôle de Yarn empêche l'installation de paquets corrompus.
    

Néanmoins, npm s'est considérablement amélioré ces dernières années, surtout avec npm v7+, ce qui en fait un choix viable pour la plupart des projets.

#### **Passer de npm à Yarn**

Si votre projet a été initialement configuré en utilisant npm mais que vous souhaitez passer à Yarn, vous pouvez :

1️⃣ **Supprimer** `node_modules` et `package-lock.json`

```python
rm -rf node_modules package-lock.json
```

2️⃣ **Exécuter Yarn pour installer les dépendances**

```python
yarn install
```

Cela générera un fichier yarn.lock, garantissant que toutes les dépendances sont gérées par Yarn à l'avenir.

npm et Yarn sont tous deux des outils puissants pour la gestion des paquets. Le choix entre eux dépend des besoins de votre projet :

✅ Utilisez **npm** si vous voulez le gestionnaire de paquets par défaut, largement utilisé, qui fonctionne bien avec la plupart des projets.  
✅ Utilisez **Yarn** si vous avez besoin d'installations plus rapides, d'une meilleure sécurité et d'un support pour les monorepos.

En fin de compte, les deux outils vous permettent d'**installer, gérer et publier** des paquets JavaScript efficacement.

## **Comment créer votre propre bibliothèque npm**

Créer votre propre bibliothèque npm est un excellent moyen de **partager du code réutilisable**, de contribuer à la communauté open-source, ou même de rationaliser le développement dans plusieurs projets. Dans cette section, nous allons passer par le processus étape par étape de configuration, de codage et de préparation d'une bibliothèque pour la publication sur npm.

### **Configuration d'un nouveau package**

Avant d'écrire du code, vous devez configurer un package npm. Suivez ces étapes :

#### **Étape 1 : Créer un nouveau dossier de projet**

```python
mkdir ma-bibliotheque-geniale
cd ma-bibliotheque-geniale
```

#### **Étape 2 : Initialiser npm**

Exécutez la commande suivante pour créer un fichier `package.json` :

```python
npm init
```

Vous serez invité à entrer des détails tels que :

* Nom du package
    
* Version
    
* Description
    
* Point d'entrée (par défaut : `index.js`)
    
* Auteur
    
* Licence
    

💡 Pour sauter les invites et créer un `package.json` par défaut, utilisez :

```python
npm init -y
```

### **Écriture de code modulaire et réutilisable**

Maintenant, créons une simple bibliothèque d'utilitaires qui fournit une fonction pour formater des dates.

#### **Étape 3 : Créer un fichier** `index.js`

À l'intérieur du dossier du projet, créez un fichier nommé `index.js` et ajoutez le code suivant :

```javascript
function formatDate(date) {
  if (!(date instanceof Date)) {
    throw new Error("Date invalide");
  }
  return date.toISOString().split("T")[0];
}

module.exports = { formatDate };
```

### **Ajout de dépendances et de dépendances peer**

Votre bibliothèque peut dépendre de paquets externes. Par exemple, utilisons date-fns pour un meilleur formatage de dates.

Pour l'installer comme dépendance, exécutez :

```python
npm install date-fns
```

Ensuite, modifiez `index.js` pour utiliser `date-fns` :

```javascript
const { format } = require("date-fns");

function formatDate(date) {
  if (!(date instanceof Date)) {
    throw new Error("Date invalide");
  }
  return format(date, "yyyy-MM-dd");
}

module.exports = { formatDate };
```

Si vous créez une bibliothèque spécifique à React, vous devriez ajouter React comme dépendance peer :

```python
npm install react --save-peer
```

Cela garantit que les utilisateurs de votre bibliothèque installent React séparément, évitant les conflits de version.

Avant de publier, vous devriez tester comment votre package fonctionne lorsqu'il est installé comme dépendance.

#### **Étape 4 : Lier le package localement**

Exécutez la commande suivante dans votre dossier de package :

```python
npm link
```

Ensuite, dans un autre projet où vous voulez utiliser votre package, naviguez vers ce projet et exécutez :

```python
npm link ma-bibliotheque-geniale
```

Maintenant, vous pouvez importer et utiliser votre fonction :

```javascript
const { formatDate } = require("ma-bibliotheque-geniale");

console.log(formatDate(new Date())); // Affiche : 2025-02-04 (ou la date actuelle)
```

Une fois que vous êtes satisfait de votre package, il est temps de le **publier sur npm**.

## **Comment publier votre bibliothèque sur npm**

Maintenant que nous avons créé notre package npm, l'étape suivante est de le **publier sur le registre npm** afin que d'autres puissent l'installer et l'utiliser. Dans cette section, nous allons couvrir comment publier le package étape par étape.

### **Création d'un compte npm**

Avant de publier, vous avez besoin d'un compte npm.

#### **Étape 1 : Inscription sur npm**

1. Allez sur [https://www.npmjs.com/signup](https://www.npmjs.com/signup) et créez un compte.
    
2. Vérifiez votre adresse e-mail.
    

#### **Étape 2 : Connexion à npm depuis le terminal**

Exécutez la commande suivante dans votre terminal :

```python
npm login
```

Vous serez invité à entrer :

* Votre nom d'utilisateur npm
    
* Votre mot de passe
    
* Votre e-mail (associé à votre compte npm)
    

Si la connexion est réussie, vous verrez un message :

```python
Connecté en tant que votre-nom-dutilisateur sur https://registry.npmjs.org/
```

### **Configuration de package.json pour la publication**

#### **Étape 3 : Assurez-vous que le nom de votre package est unique**

Chaque package npm a besoin d'un nom unique. Exécutez la commande suivante pour vérifier si le nom souhaité est disponible :

```python
npm search ma-bibliotheque-geniale
```

Si le nom est déjà pris, vous devrez modifier `package.json` et changer le champ `"name"`.

#### **Étape 4 : Ajoutez des métadonnées et des mots-clés**

Ouvrez `package.json` et assurez-vous qu'il inclut des métadonnées utiles :

```json
{
  "name": "ma-bibliotheque-geniale",
  "version": "1.0.0",
  "description": "Un simple package npm pour formater des dates",
  "main": "index.js",
  "repository": {
    "type": "git",
    "url": "https://github.com/votre-nom-dutilisateur/ma-bibliotheque-geniale.git"
  },
  "keywords": ["date", "formatter", "utility", "npm package"],
  "author": "Votre Nom <votre-email@example.com>",
  "license": "MIT"
}
```

🔹 **repository** – Utile si vous prévoyez d'héberger le projet sur GitHub.  
🔹 **keywords** – Aide les gens à découvrir votre package sur npm.  
🔹 **license** – Spécifie comment les autres peuvent utiliser votre package (par exemple, MIT, GPL, etc.).

### **Publication du package**

#### **Étape 5 : Publiez votre package sur npm**

Exécutez la commande suivante à l'intérieur de votre dossier de projet :

```python
npm publish
```

Si la publication est réussie, vous verrez une sortie similaire à :

```python
+ ma-bibliotheque-geniale@1.0.0
```

Votre package est maintenant disponible à l'adresse :

📍 [**https://www.npmjs.com/package/ma-bibliotheque-geniale**](https://www.npmjs.com/package/ma-bibliotheque-geniale)

#### **Étape 6 : Apporter des modifications et mettre à jour le package**

Si vous souhaitez publier une nouvelle version, mettez à jour le champ `version` dans `package.json`. npm suit le versionnage sémantique (SemVer) :

* **Patch** : Corrections de bugs (1.0.0 → 1.0.1)
    
* **Minor** : Nouvelles fonctionnalités, compatibles ascendantes (1.0.0 → 1.1.0)
    
* **Major** : Changements cassants (1.0.0 → 2.0.0)
    

Au lieu de mettre à jour manuellement `package.json`, utilisez :

```python
npm version patch   # 1.0.0 → 1.0.1
npm version minor   # 1.0.0 → 1.1.0
npm version major   # 1.0.0 → 2.0.0
```

Ensuite, publiez la nouvelle version :

```python
npm publish
```

Si vous avez accidentellement publié un package et que vous devez le supprimer :

```python
npm unpublish ma-bibliotheque-geniale --force
```

⚠️ **Note** : Vous ne pouvez supprimer des packages que **dans les 72 heures** suivant la publication.

🎉 **Vous avez publié avec succès votre propre bibliothèque npm !** Maintenant, d'autres développeurs peuvent l'installer en utilisant :

```python
npm install ma-bibliotheque-geniale
```

En suivant le versionnage sémantique, en écrivant une documentation claire et en maintenant votre package, vous contribuez à l'écosystème open-source et rendez votre code réutilisable.

## **Comment utiliser votre bibliothèque npm dans un projet React**

Maintenant que nous avons publié notre package npm, voyons comment l'installer, l'importer et l'utiliser dans un projet React créé avec **Vite**. Cette section vous guidera à travers le processus en utilisant à la fois npm et Yarn.

### **Installation de votre package**

#### **Étape 1 : Créer un nouveau projet React avec Vite (si nécessaire)**

Si vous n'avez pas de projet React existant, créez-en un en utilisant Vite :

#### **En utilisant npm**

```python
npm create vite@latest mon-app-react --template react
cd mon-app-react
npm install
```

#### **En utilisant Yarn**

```python
yarn create vite@latest mon-app-react --template react
cd mon-app-react
yarn install
```

Une fois l'installation terminée, vous pouvez démarrer le serveur de développement :

```python
npm run dev
```

ou

```python
yarn dev
```

#### **Étape 2 : Installer votre package npm**

Maintenant, installez la bibliothèque npm que nous avons créée précédemment (`ma-bibliotheque-geniale`).

#### **En utilisant npm**

```python
npm install ma-bibliotheque-geniale
```

#### **En utilisant Yarn**

```python
yarn add ma-bibliotheque-geniale
```

### **Importation et utilisation de la bibliothèque dans un composant React**

Une fois installé, vous pouvez utiliser la bibliothèque à l'intérieur d'un composant React.

Ouvrez `src/App.jsx` et modifiez-le comme suit :

```javascript
import React from "react";
import { formatDate } from "ma-bibliotheque-geniale";

function App() {
  const today = new Date();
  return (
    <div>
      <h1>Date formatée</h1>
      <p>{formatDate(today)}</p>
    </div>
  );
}

export default App;
```

Maintenant, exécutez votre application React Vite :

```python
npm run dev
```

Ou avec Yarn :

```python
yarn dev
```

Cela affichera une date formatée sur la page web, confirmant que notre bibliothèque fonctionne !

### **Gestion des mises à jour et du versionnage du package**

Pour mettre à jour votre package npm dans votre projet :

#### **En utilisant npm**

```python
npm update ma-bibliotheque-geniale
```

#### **En utilisant Yarn**

```python
yarn upgrade ma-bibliotheque-geniale
```

Si vous voulez vérifier les dépendances obsolètes :

```python
npm outdated
```

ou

```python
yarn outdated
```

### **Utilisation d'une version locale de votre package en développement**

Si vous apportez encore des modifications à votre package npm et que vous souhaitez le tester dans votre projet React **avant de le publier**, vous pouvez utiliser `npm link` ou `yarn link`.

#### **Étape 1 : Lier votre package localement**

Allez dans le dossier de votre package :

```python
cd ~/chemin-vers-ma-bibliotheque-geniale
npm link
```

ou

```python
yarn link
```

#### **Étape 2 : Utilisez-le dans votre projet React**

Naviguez vers votre application React et liez le package :

```python
cd ~/chemin-vers-mon-app-react
npm link ma-bibliotheque-geniale
```

ou

```python
yarn link ma-bibliotheque-geniale
```

Maintenant, lorsque vous importez et utilisez `ma-bibliotheque-geniale`, il utilisera la version locale au lieu de la version publiée.

### **Publication d'une mise à jour de votre package**

Si vous avez apporté des modifications à votre package et que vous souhaitez publier une nouvelle version :

1️⃣ **Mettez à jour le numéro de version** dans `package.json` (utilisez `npm version patch` pour les petites mises à jour).  
2️⃣ **Exécutez** `npm publish` pour télécharger la nouvelle version.  
3️⃣ **Exécutez** `npm update ma-bibliotheque-geniale` dans votre projet React pour obtenir la dernière version.

### **Réflexions finales sur l'utilisation des bibliothèques npm dans React (Édition Vite)**

À ce stade, vous devriez avoir un package npm entièrement fonctionnel et savoir comment l'installer, l'utiliser et le mettre à jour dans un projet React en utilisant Vite.

✅ Vite est plus rapide que Create React App et offre de meilleures performances pour le développement.  
✅ npm et Yarn facilitent la gestion des dépendances.  
✅ `npm link` permet des tests locaux avant la publication.  
✅ Maintenir les dépendances à jour assure la stabilité.

Ce flux de travail est essentiel pour les développeurs qui cherchent à créer, maintenir et distribuer des composants React réutilisables ou des utilitaires JavaScript.

## **Bonnes pratiques pour les bibliothèques npm et Yarn**

Maintenant que vous avez créé, publié et utilisé votre propre package npm, il est essentiel de suivre les meilleures pratiques pour garantir que votre package est fiable, maintenable et facile à utiliser. Cette section couvrira les principes et techniques clés pour rendre votre bibliothèque npm aussi professionnelle que possible.

### **Écrire une documentation significative**

Une bibliothèque bien documentée aide les autres développeurs à comprendre comment l'utiliser efficacement.

#### **Ce qu'il faut inclure dans votre documentation**

📍 Instructions d'installation  
📍 Exemples d'utilisation  
📍 Référence API (fonctions, paramètres, valeurs de retour)  
📍 Historique des versions et mises à jour  
📍 Guide de contribution (si open-source)

Par exemple, un simple fichier [`README.md`](http://README.md) pour ma-bibliotheque-geniale :

````python
# ma-bibliotheque-geniale

Un simple package npm pour formater des dates.

## Installation

### En utilisant npm
```sh
npm install ma-bibliotheque-geniale
````

#### En utilisant Yarn

```python
yarn add ma-bibliotheque-geniale
```

#### Utilisation

```javascript
import { formatDate } from "ma-bibliotheque-geniale";

console.log(formatDate(new Date())); // Affiche : 2025-02-04
```

### **Suivre le versionnage sémantique (SemVer)**

Le versionnage aide à maintenir la compatibilité et informe les utilisateurs des changements. npm suit le versionnage sémantique (SemVer) :

MAJOR.MINOR.PATCH

| Type de changement | Exemple | Signification |
| --- | --- | --- |
| **Patch** | `1.0.0 → 1.0.1` | Corrections de bugs, pas de changements cassants |
| **Minor** | `1.0.0 → 1.1.0` | Nouvelles fonctionnalités, compatibles ascendantes |
| **Major** | `1.0.0 → 2.0.0` | Changements cassants |

💡 Pour incrémenter les versions automatiquement, utilisez :

````javascript
```sh
npm version patch   # Petite correction de bug
npm version minor   # Nouvelle fonctionnalité ajoutée
npm version major   # Changements cassants
````

Ensuite, publiez la nouvelle version :

```javascript
npm publish
```

👉 Utilisez un versionnage approprié pour éviter de casser les projets qui dépendent de votre bibliothèque.

### **Maintenir les dépendances à jour**

Mettre régulièrement à jour les dépendances améliore la sécurité, les performances et la compatibilité.

#### **Vérifier les dépendances obsolètes :**

```javascript
npm outdated
```

ou

```javascript
yarn outdated
```

#### **Mettre à jour les dépendances :**

```javascript
npm update
```

ou

```javascript
yarn upgrade
```

### **Écrire des tests unitaires pour votre bibliothèque**

Les tests garantissent que votre package fonctionne correctement avant de publier des mises à jour.

#### **Installer un framework de test (Jest)**

```javascript
npm install --save-dev jest
```

#### **Créer un fichier de test (**`index.test.js`)

```javascript
const { formatDate } = require("./index");

test("formate une date correctement", () => {
  expect(formatDate(new Date("2025-02-04"))).toBe("2025-02-04");
});

test("lance une erreur si l'entrée n'est pas une date", () => {
  expect(() => formatDate("not a date")).toThrow("Date invalide");
});
```

#### **Exécuter les tests**

```javascript
shCopyEditnpm test
```

👉 Vous pouvez utiliser CI/CD (par exemple, GitHub Actions) pour exécuter les tests automatiquement à chaque push.

### **Utilisation de CI/CD pour la publication automatisée**

#### **Automatiser la publication avec GitHub Actions**

Créez un fichier `.github/workflows/publish.yml` :

```javascript
ymlCopyEditname: Publier sur npm
on:
  push:
    branches:
      - main

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: 18
          registry-url: "https://registry.npmjs.org/"
      - run: npm install
      - run: npm test
      - run: npm publish
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
```

1️⃣ **Créez un token npm** :  
Exécutez :

```javascript
shCopyEditnpm token create
```

Copiez le token et ajoutez-le aux secrets GitHub (`NPM_TOKEN`).

2️⃣ **Poussez le code sur GitHub** → Publication automatique sur npm !

👉 Automatiser la publication évite les erreurs humaines et assure le contrôle de la qualité.

### **Assurer la compatibilité multiplateforme**

* Utilisez **les modules ES** (`import/export`) pour une compatibilité moderne.
    
* Incluez le **support CommonJS** (`require/module.exports`) pour les environnements plus anciens.
    
* Test avec différentes **versions de Node.js** en utilisant CI/CD.
    

Exemple `package.json` pour une double compatibilité :

```javascript
jsonCopyEdit"type": "module",
"main": "index.cjs",
"exports": {
  "import": "./index.mjs",
  "require": "./index.cjs"
}
```

👉 Cela garantit que votre package fonctionne partout (Node.js, React, Next.js, etc.).

## **Conclusion**

Félicitations ! 🎉 Vous avez réussi à apprendre comment créer, publier et utiliser votre propre package npm, tout en comprenant les avantages de **npm** et **Yarn** pour la gestion des paquets.

Tout au long de ce guide, nous avons couvert :

✅ Ce qu'est npm et pourquoi c'est important  
✅ Comment utiliser npm et Yarn pour gérer les dépendances  
✅ Comment créer un package npm réutilisable  
✅ Comment publier et mettre à jour votre package sur npm  
✅ Comment intégrer votre package dans un projet React avec Vite  
✅ Les bonnes pratiques pour écrire, tester et maintenir votre bibliothèque

En suivant ces étapes, vous avez fait un pas important vers le développement open-source et la programmation modulaire, rendant votre code réutilisable pour vous-même et la communauté des développeurs.