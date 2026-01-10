---
title: Comment hacher des mots de passe avec bcrypt dans Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-04-03T22:01:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-hash-passwords-with-bcrypt-in-nodejs
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/How-to-Hash-Password-With-Bcrypt-In-Nodejs.png
tags:
- name: information security
  slug: information-security
- name: node js
  slug: node-js
- name: Security
  slug: security
seo_title: Comment hacher des mots de passe avec bcrypt dans Node.js
seo_desc: "By Dennis Temoye Charity\nSecurity is critical in the field of web development,\
  \ particularly when dealing with user credentials such as passwords. One security\
  \ procedure that's critical in web development is password hashing. \nPassword hashing\
  \ guarant..."
---

Par Dennis Temoye Charity

La sécurité est cruciale dans le domaine du développement web, en particulier lorsqu'il s'agit des informations d'identification des utilisateurs telles que les mots de passe. Une procédure de sécurité qui est cruciale dans le développement web est le hachage des mots de passe. 

Le hachage des mots de passe garantit que les mots de passe en texte clair sont difficiles à trouver pour les attaquants, même dans une situation où une base de données est compromise. Mais toutes les méthodes de hachage ne se valent pas, et c'est là que bcrypt se distingue.

Node.js, un framework populaire pour le développement d'applications web, fournit un écosystème robuste pour construire des systèmes d'authentification sécurisés. Dans cet article, nous allons examiner l'utilisation de bcrypt dans Node.js pour hacher les mots de passe. Nous verrons comment bcrypt peut être intégrée de manière fluide dans les applications Node.js pour améliorer la sécurité et protéger efficacement les informations d'identification des utilisateurs.

Que vous soyez un développeur Node.js expérimenté cherchant à renforcer vos pratiques d'authentification ou un débutant cherchant à apprendre les meilleures techniques pour une gestion sécurisée des mots de passe, cet article vous sera utile. Examinons comment vous pouvez utiliser bcrypt pour hacher des mots de passe dans Node.js.

### Voici ce que nous allons couvrir :

1. [Qu'est-ce que le hachage ?](#heading-quest-ce-que-le-hachage)
2. [Qu'est-ce que Bcrypt ?](#heading-quest-ce-que-bcrypt)
3. [Comment installer Bcrypt dans Node.js](#heading-comment-installer-bcrypt-dans-nodejs)
4. [Comment configurer Bcrypt dans Node.js](#heading-comment-configurer-bcrypt-dans-nodejs)
5. [Comment hacher des mots de passe avec Bcrypt](#heading-comment-hacher-des-mots-de-passe-avec-bcrypt)
6. [Comment vérifier des mots de passe avec Bcrypt](#heading-comment-verifier-des-mots-de-passe-avec-bcrypt)
7. [Bonnes pratiques de sécurité avec Bcrypt](#heading-bonnes-pratiques-de-securite-avec-bcrypt)
8. [Conclusion](#heading-conclusion)

## Qu'est-ce que le hachage ?

Le hachage consiste à convertir une clé donnée ou une chaîne de caractères en une autre valeur. Cela est généralement représenté par une valeur ou une clé de longueur fixe plus courte qui représente la valeur originale et facilite la récupération.

### Qu'est-ce que le hachage de mot de passe ?

Le hachage de mot de passe est un processus de conversion d'un mot de passe d'entrée en une chaîne de caractères de longueur fixe, généralement dans le but de stocker et de transmettre le mot de passe de manière sécurisée. 

Les fonctions de hachage de mot de passe sont conçues pour être des fonctions à sens unique. Cela signifie qu'il ne devrait pas être possible de calculer l'inverse du processus et d'obtenir le mot de passe d'entrée original à partir de la valeur hachée.

Par exemple, supposons que nous voulons hacher un mot de passe comme "password123". Le mot de passe sera transformé en une chaîne de caractères de longueur fixe en utilisant un algorithme de hachage comme bcrypt. Et nous obtiendrons un résultat haché une fois que la fonction de hachage aura traité notre mot de passe. 

La sortie hachée de "password123" en utilisant bcrypt, par exemple, ressemblerait à ceci :

```
e234dsdom3k2kmdl3l43iwes9vjro44223m3n32kn5n2ksdo4   

```

Maintenant que vous comprenez les bases du fonctionnement du hachage de mot de passe, il est temps de plonger plus profondément dans l'application pratique du hachage d'un mot de passe en utilisant l'algorithme bcrypt. 

Mais avant de procéder à cela, apprenons un peu plus sur bcrypt afin que vous compreniez son fonctionnement et son processus d'installation, ainsi que la manière de l'intégrer dans un projet Node.js.

Tout d'abord, acquérons une compréhension de bcrypt – ce qu'il est, comment il fonctionne et son importance dans la sécurité des mots de passe. Ensuite, nous discuterons de la manière d'installer bcrypt et de l'intégrer de manière transparente dans un environnement Node.js. Cela inclura un guide détaillé sur la configuration de bcrypt dans votre projet et l'utilisation efficace de ses fonctionnalités.

À la fin de cet article, vous aurez une compréhension complète de bcrypt, équipé des connaissances pour hacher des mots de passe de manière sécurisée dans vos applications Node.js. Alors, embarquons dans ce voyage pour améliorer la sécurité de nos projets grâce à l'intégration de bcrypt.

## Qu'est-ce que bcrypt ?

Bcrypt est un type d'algorithme cryptographique utilisé pour stocker des mots de passe de manière sécurisée. Il brouille le mot de passe d'un utilisateur en un code unique. De cette manière, même si un voleur prend la base de données, il ne pourra pas récupérer les mots de passe originaux facilement.

### Comment fonctionne bcrypt ?

Bcrypt fonctionne en combinant le hachage et une technique connue sous le nom de salage, qui est spécifiquement développée pour rendre les mots de passe stockés plus sûrs. 

Voici une décomposition de la procédure :

1. **Hachage :** Bcrypt traite le mot de passe d'un utilisateur en utilisant une fonction mathématique sophistiquée. Cette fonction convertit le mot de passe en une chaîne de caractères de longueur fixe qui semble aléatoire et sans signification. La valeur hachée est ce qui est conservé dans la base de données, et non le mot de passe original. Parce que la fonction de hachage est à sens unique, inverser le hachage ne produira pas le mot de passe original.
2. **Salage :** Pour améliorer la sécurité, bcrypt incorpore un nombre aléatoire appelé sel. Ce sel est unique pour chaque mot de passe et est attaché à celui-ci avant le hachage. La valeur combinée (mot de passe + sel) est ensuite transmise à la fonction de hachage.

## Comment installer Bcrypt dans Node.js

Avant d'installer bcrypt, vous devrez avoir un projet Node.js déjà configuré. Si vous n'en avez pas encore créé un, suivez ces étapes pour créer un nouveau projet Node.js :

### Créer un répertoire :

Cette commande crée un nouveau répertoire (dossier) où votre projet Node.js résidera. Il est nommé `bcrypt-password-hash`.

```
mkdir bcrypt-password-hash

```

* `mkdir` : Cette commande signifie "make directory". Elle est utilisée pour créer un nouveau répertoire.
* `bcrypt-password-hash` : C'est le nom du répertoire que vous créez. Vous pouvez choisir n'importe quel nom que vous préférez pour votre répertoire de projet.

### Changer dans le répertoire nouvellement créé : 

Cette commande vous naviguera dans le répertoire nouvellement créé afin que vous puissiez commencer à travailler sur votre projet à l'intérieur.

```
cd bcrypt-password-hash

```

* `cd` : Cette commande signifie "change directory". Elle est utilisée pour passer d'un répertoire à un autre.
* `bcrypt-password-hash` : C'est le nom du répertoire dans lequel vous souhaitez naviguer.

### Initialiser un nouveau projet Node.js : 

Cette commande initialise un nouveau projet Node.js dans le répertoire que vous avez créé. Elle crée un fichier `package.json`, qui est utilisé pour gérer les dépendances et la configuration de votre projet Node.js.

```
npm init -y

```

* `npm init` : Cette commande initialise un nouveau projet Node.js en utilisant npm (Node Package Manager).
* `-y` : Ce flag accepte automatiquement toutes les valeurs par défaut pour le fichier `package.json`, donc vous n'avez pas à fournir manuellement d'entrée pour chaque champ.

Après avoir exécuté ces commandes, vous devriez avoir un nouveau répertoire (bcrypt-password-hash) avec un fichier package.json, indiquant que vous avez réussi à créer un nouveau projet Node.js. Vous pouvez maintenant installer des dépendances et écrire du code.

### Créer un fichier nommé `index.js` où vous écrirez votre code :

Pour créer un fichier nommé `index.js` où vous écrirez votre code, vous pouvez utiliser la commande `touch` dans votre terminal. Voici comment faire :

```
touch index.js

```

* `touch` : Cette commande est utilisée pour créer un nouveau fichier. (Notez que vous devez avoir déjà installé `touch` sur votre machine pour l'utiliser. Si vous ne l'avez pas, vous pouvez exécuter cette commande dans votre terminal pour installer touch : `npm install touch-cli -g`.)
* `index.js` : C'est le nom du fichier que vous souhaitez créer. Dans ce cas, vous créez un fichier JavaScript nommé `index.js`.

Après avoir exécuté cette commande, vous aurez un nouveau fichier nommé `index.js` dans votre répertoire de projet où vous pourrez écrire votre code Node.js comme vous pouvez le voir dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/Bcrypt.jpg)

Maintenant que nous avons correctement construit un projet Node.js, nous pouvons installer bcrypt dans notre projet.

### Installer les dépendances requises (bcrypt) :

Pour installer bcrypt, vous utiliserez npm, le gestionnaire de paquets Node.js. Voici la commande pour installer bcrypt :

```
npm install bcrypt

```

* `npm install` : Cette commande est utilisée pour installer des paquets depuis le registre npm.
* `bcrypt` : C'est le nom du paquet que vous souhaitez installer. bcrypt est un paquet populaire pour hacher des mots de passe de manière sécurisée dans Node.js.

Lorsque vous exécutez cette commande, npm téléchargera et installera le paquet bcrypt et ses dépendances dans le répertoire `node_modules` de votre projet. Ce répertoire contiendra toutes les dépendances requises pour votre projet, y compris bcrypt.

## Comment configurer Bcrypt dans Node.js

Une fois que Bcrypt est installé dans votre projet Node.js, vous pouvez intégrer ses fonctionnalités de manière transparente dans votre application. Voici comment procéder :

Tout d'abord, après avoir installé le paquet bcrypt en utilisant npm, assurez-vous de l'importer dans votre fichier d'application Node.js `index.js` pour utiliser ses fonctionnalités efficacement. 

Voici comment faire :

```javascript
const bcrypt = require('bcrypt');

```

Cette ligne de code garantit que le paquet bcrypt est accessible dans votre application, vous permettant de tirer parti de ses puissantes capacités pour le hachage sécurisé des mots de passe et la vérification. 

Avec bcrypt intégré dans votre projet, vous pouvez améliorer la sécurité de l'authentification des utilisateurs et de la protection des données.

bcrypt fournit deux fonctions principales pour le hachage et la comparaison des mots de passe :

1. `bcrypt.hash()` : Cette fonction est utilisée pour générer un hachage d'un mot de passe en texte clair. Elle prend le mot de passe en texte clair et un facteur de sel (facultatif) comme paramètres d'entrée et retourne le mot de passe haché de manière asynchrone.
2. `bcrypt.compare()` : Cette fonction est utilisée pour comparer un mot de passe en texte clair avec son équivalent haché. Elle prend le mot de passe en texte clair et le mot de passe haché comme paramètres d'entrée et retourne une valeur booléenne indiquant si les mots de passe correspondent.

## Comment hacher des mots de passe avec Bcrypt

Ayant approfondi l'importance du hachage des mots de passe, ainsi que les concepts de hachage et de sel, mettons la théorie en pratique dans notre fichier `index.js`.

### Comment générer un sel et hacher le mot de passe

Comme nous l'avons appris, un aspect clé du hachage sécurisé des mots de passe implique l'incorporation d'un sel unique dans le processus de hachage. bcrypt simplifie cela en gérant la génération de sel et le hachage des mots de passe de manière transparente.

Pour commencer, nous nécessitons le module bcrypt dans notre application Node.js :

```javascript
const bcrypt = require('bcrypt');

```

Pour garantir la robustesse de nos hachages de mots de passe, nous déterminons le nombre de tours de sel. Cette valeur dicte le coût computationnel du hachage et, par conséquent, le niveau de sécurité :

```javascript
const saltRounds = 10; // Typiquement une valeur entre 10 et 12

```

Avec notre configuration établie, nous pouvons générer un sel de manière asynchrone en utilisant la fonction `bcrypt.genSalt()`. Ce sel sera unique pour chaque hachage de mot de passe, améliorant la sécurité :

```javascript
bcrypt.genSalt(saltRounds, (err, salt) => {
if (err) {
    // Gérer l'erreur
    return;
}

// Génération de sel réussie, procéder au hachage du mot de passe
});
```

Une fois le sel généré, nous le combinons avec le mot de passe de l'utilisateur pour calculer le hachage en utilisant la fonction `bcrypt.hash()`. Cela donne un mot de passe haché de manière sécurisée prêt pour le stockage :

```javascript
const userPassword = 'user_password'; // Remplacer par le mot de passe réel
bcrypt.hash(userPassword, salt, (err, hash) => {
    if (err) {
        // Gérer l'erreur
        return;
    }

// Hachage réussi, 'hash' contient le mot de passe haché
console.log('Mot de passe haché :', hash);
});
```

En utilisant bcrypt pour le hachage des mots de passe dans notre application Node.js, nous garantissons la sécurité robuste des informations d'identification des utilisateurs. L'incorporation de sels uniques pour chaque hachage de mot de passe, couplée à la complexité computationnelle de bcrypt, renforce notre défense contre l'accès non autorisé et les attaques malveillantes.

Dans la section suivante, nous explorerons comment vérifier les mots de passe et discuterons des meilleures pratiques pour gérer de manière sécurisée les mots de passe hachés.

## Comment vérifier des mots de passe avec Bcrypt

Maintenant que nous avons couvert le processus de hachage des mots de passe en utilisant bcrypt dans notre application Node.js, concentrons-nous sur la vérification des mots de passe lors de l'authentification des utilisateurs. 

Dans cette section, nous explorerons comment bcrypt facilite la vérification des mots de passe, garantissant un processus d'authentification sécurisé et fluide.

### Comment récupérer un mot de passe haché de la base de données

Avant de pouvoir vérifier le mot de passe d'un utilisateur, nous devons récupérer le mot de passe haché associé au compte de l'utilisateur dans la base de données. 

En supposant que vous avez un système d'authentification des utilisateurs en place, vous interrogerez généralement la base de données pour récupérer le mot de passe haché en fonction du nom d'utilisateur ou de l'email de l'utilisateur.

Une fois que vous avez récupéré le mot de passe haché de la base de données, vous êtes prêt à procéder au processus de vérification du mot de passe.

### Comment vérifier des mots de passe

Pour vérifier un mot de passe en utilisant bcrypt, utilisez la fonction `bcrypt.compare()`. Cette fonction compare un mot de passe en texte clair fourni par l'utilisateur lors de la connexion avec le mot de passe haché stocké dans la base de données.

Voici comment vous pouvez implémenter la vérification des mots de passe en utilisant bcrypt dans votre application Node.js :

```javascript
const storedHashedPassword = 'hashed_password_from_database';
const userInputPassword = 'password_attempt_from_user';

bcrypt.compare(userInputPassword, storedHashedPassword, (err, result) => {
    if (err) {
        // Gérer l'erreur
        console.error('Erreur lors de la comparaison des mots de passe :', err);
        return;
    }

if (result) {
    // Les mots de passe correspondent, authentification réussie
    console.log('Les mots de passe correspondent ! Utilisateur authentifié.');
} else {
    // Les mots de passe ne correspondent pas, authentification échouée
    console.log('Les mots de passe ne correspondent pas ! Authentification échouée.');
}
});

```

Dans cet extrait de code, `storedHashedPassword` représente le mot de passe haché récupéré de la base de données, tandis que `userInputPassword` est le mot de passe en texte clair fourni par l'utilisateur lors de la connexion. La fonction `bcrypt.compare()` compare ces deux mots de passe et retourne une valeur booléenne indiquant s'ils correspondent.

Dans la section suivante, nous discuterons des meilleures pratiques pour gérer de manière sécurisée les mots de passe hachés, y compris les considérations pour le stockage et la manipulation des mots de passe.

## Bonnes pratiques de sécurité avec bcrypt

Maintenant que nous avons discuté des principes du hachage et de la vérification des mots de passe avec bcrypt, examinons quelques bonnes pratiques de sécurité importantes pour garantir l'intégrité de notre système d'authentification.

### Directives pour des mots de passe robustes

Encouragez les utilisateurs à créer des mots de passe forts et complexes qui résistent aux attaques par dictionnaire. Fournissez des directives sur la longueur des mots de passe, l'inclusion de caractères alphanumériques, de symboles et l'évitement des motifs courants.

### Salage

Utilisez toujours un sel unique pour chaque hachage de mot de passe. Cela empêche les attaquants d'utiliser des tables arc-en-ciel précalculées pour craquer les mots de passe. bcrypt gère automatiquement la génération de sel, garantissant que chaque hachage est unique.

### Hachage adaptatif

Bcrypt utilise le hachage adaptatif, permettant aux développeurs d'ajuster le coût computationnel du hachage au fil du temps. Augmentez périodiquement le nombre de tours de hachage pour suivre les avancées du matériel et de la puissance de calcul.

### Stockage sécurisé

Stockez les mots de passe hachés de manière sécurisée dans votre base de données. Assurez-vous que des contrôles d'accès sont en place pour prévenir l'accès non autorisé aux informations d'identification des utilisateurs. Évitez de stocker des mots de passe en texte clair ou d'utiliser des algorithmes de chiffrement réversibles.

### Gestion des erreurs

Implémentez des mécanismes de gestion des erreurs appropriés lors de l'utilisation des fonctions bcrypt. Gérez les erreurs de manière élégante et évitez de divulguer des informations sensibles qui pourraient aider les attaquants à exploiter des vulnérabilités.

## Conclusion

En conclusion, nous avons exploré les aspects essentiels de la sécurité des mots de passe et le rôle de bcrypt dans la protection des informations d'identification des utilisateurs au sein des applications Node.js. De la compréhension des principes fondamentaux du hachage des mots de passe et du salage à la mise en œuvre de mécanismes d'authentification sécurisés, nous avons couvert un large éventail de sujets visant à améliorer la posture de sécurité de nos applications.

En utilisant bcrypt pour le hachage et la vérification des mots de passe, nous garantissons que les données sensibles des utilisateurs restent protégées contre l'accès non autorisé et les attaques malveillantes. L'algorithme robuste de bcrypt, combiné au hachage adaptatif et à la génération de sel, fournit un mécanisme de défense fiable contre les vulnérabilités courantes basées sur les mots de passe.

Nous avons également discuté des bonnes pratiques de sécurité, y compris les politiques de mots de passe forts, les pratiques de stockage sécurisé et la gestion des erreurs. En adhérant à ces bonnes pratiques et en restant vigilants contre les menaces évolutives, nous pouvons créer un système d'authentification sécurisé qui inspire confiance à nos utilisateurs et maintient l'intégrité de nos applications.

Continuons à prioriser la sécurité et à nous efforcer d'exceller dans notre quête de construction d'applications robustes et dignes de confiance.

Merci de vous être joint à moi dans cette exploration de la sécurité des mots de passe avec bcrypt. Ensemble, nous pouvons créer un environnement numérique plus sûr pour tous les utilisateurs.

Bon codage !