---
title: Framework UI Astro [Livre Complet]
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-12T20:58:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-astro-ui-framework
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/large-heading.png
tags:
- name: book
  slug: book
- name: TypeScript
  slug: typescript
- name: User Interface
  slug: user-interface
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "Par Emmanuel Ohans\nAstro est un nouveau framework UI conçu pour la vitesse.\
  \ Et si vous voulez apprendre à l'utiliser, vous êtes au bon endroit. \nTable\
  \ des Matières\n\nIntroduction \nChapitre 1 : Construisez votre première application Astro \n\
  Chapitre 2 : Les composants Astro en profondeur \nChapitre 3 : Construisez votre propre îlot de composants..."
---

Par Emmanuel Ohans

Astro est un nouveau framework UI conçu pour la vitesse. Et si vous voulez apprendre à l'utiliser, vous êtes au bon endroit.

## Table des Matières

1. [Introduction](#heading-introduction)
2. [Chapitre 1 : Construisez votre première application Astro](#heading-chapitre-1-construisez-votre-premiere-application-astro)
3. [Chapitre 2 : Les composants Astro en profondeur](#heading-chapitre-2-les-composants-astro-en-profondeur)
4. [Chapitre 3 : Construisez votre propre îlot de composants](#heading-chapitre-3-construisez-votre-propre-ilot-de-composants)
5. [Chapitre 4 : La vie secrète des îlots de composants Astro](#heading-chapitre-4-la-vie-secrete-des-ilots-de-composants-astro)
6. [Chapitre 5 : Oh mon React ! (Comment construire un clone du site de documentation React)](#heading-chapitre-5-oh-mon-react-comment-construire-un-clone-du-site-de-documentation-react)
7. [Chapitre 6 : Rendu côté serveur (SSR) dans Astro](#heading-chapitre-6-rendu-cote-serveur-ssr-dans-astro)
8. [Chapitre 7 : Soyez Audible ! (Comment construire un projet Astro Fullstack)](#heading-chapitre-7-soyez-audible-comment-construire-un-projet-astro-fullstack)
9. [Chapitre 8 : Construisez vos propres intégrations Astro](#heading-chapitre-8-construisez-vos-propres-integrations-astro)
10. [Conclusion](#conclusion-6)

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-132.png)

# Introduction

Je ne fais pas partie de ces gens qui sautent sur chaque nouvelle bibliothèque ou framework brillant qui arrive sur la scène juste parce que c'est tendance. Je suis plutôt du genre "attendre et voir".

Vous vous demandez donc probablement pourquoi j'ai écrit un livre sur Astro, un framework UI relativement nouveau.

Eh bien, laissez-moi vous dire.

Je suis dans ce jeu depuis près d'une décennie maintenant, et j'ai vu des frameworks aller et venir comme une mauvaise indigestion. Et Astro ne vivra peut-être pas éternellement non plus.

Mais voilà le truc : lorsque vous utilisez un nouveau framework UI, il ne s'agit pas seulement de faire fonctionner les choses et d'assembler quelques applications à la va-vite. Non, non, non. La vraie magie réside dans la compréhension des principes et des concepts derrière la création du framework. Et c'est exactement l'état d'esprit que j'avais quand j'ai écrit ce livre.

Vous devez vous demander : qu'est-ce qui rend ce framework si unique ? En quoi est-il différent de tout le reste ? Comment pouvez-vous appliquer son modèle mental à la vision globale du développement d'applications pour le web ? De plus, quels principes agnostiques au framework pouvez-vous apprendre en cours de route ?

La bonne nouvelle est que j'ai des réponses à toutes ces questions brûlantes, parsemées tout au long du livre comme des confettis.

Maintenant, parlons performance, voulez-vous ? Bien sûr, c'est une toute autre histoire selon le type d'application auquel vous avez affaire. Mais pour des applications spécifiques, par exemple les applications axées sur le contenu, Astro change totalement la donne. Ses performances par défaut sont hors normes.

Plus je faisais de recherches sur Astro, plus j'étais fasciné à l'idée d'écrire ce livre.

Et voici le meilleur : ce livre va au-delà d'Astro. Dans des chapitres spécifiques, nous discuterons de concepts que vous pouvez appliquer à n'importe quel framework avec lequel vous travaillez. Et ce n'est pas seulement cool – c'est carrément pratique.

Astro ouvre la voie à une nouvelle architecture sur le web : l'architecture des îlots de composants (component island architecture). Et mon objectif est de vous aider à la comprendre suffisamment bien pour construire des applications de production sérieusement robustes.

Alors, ne vous contentez pas d'effleurer la surface. Plongeons plutôt en profondeur et apprenons à connaître ce framework.

C'est pourquoi j'écris ce livre. Et hé, six mois plus tard, j'aime toujours autant ça.

Alors, qu'attendez-vous ? Prenez votre boisson préférée (thé plutôt que café, ici), installez-vous, et commençons à construire !

Santé 🥂

## Une note à propos de ce livre

D'accord, si vous ne l'avez pas déjà remarqué, j'écris comme je parle. J'utilise un langage simple et des analogies que même ma grand-mère pourrait (potentiellement) comprendre — quand je le fais bien.

Ce livre ne se lit pas comme une documentation technique typique — désolé, amis nerds.

À mon avis, les livres techniques devraient être agréables à regarder et faciles à lire. Et pourquoi ne pas rire un peu pendant qu'on y est ?

Si vous êtes partant pour passer un bon moment tout en apprenant une chose ou deux (enfin, beaucoup plus), alors allons-y !

## Ce livre vs la documentation officielle

Certaines ressources ne font que répéter la documentation officielle. Mais je ne trouve pas cela très utile.

Ainsi, ce livre diffère de la documentation officielle de plusieurs manières :

*   **Le ton de l'écriture** : ce livre adopte un style d'écriture de documentation non technique pour faciliter la compréhension. Que vous appréciiez cela ou non est laissé à votre goût.
*   **Ne suit pas le framework Diataxis** : la documentation technique d'Astro est écrite en suivant le framework [Diataxis](https://diataxis.fr/). Le framework suggère de structurer le contenu autour de four types distincts : tutoriel, guide pratique (how-to), explication et référence.
    Ce livre sort de cette structure stricte pour mettre l'accent sur la compréhension et l'apprentissage pratique. Ce livre n'est pas une référence et ne vise pas à remplacer les références officielles d'Astro. Dans le jargon Diataxis, comprendre Astro pourrait être défini comme un mélange de guides pratiques et un mélange soigneux de tutoriels avec des explications élaborées entrelacées.
*   **Utilisation avancée** : certaines utilisations avancées d'Astro sont cachées dans les références officielles – sans explications ni exemples pratiques. C'est parfaitement bien pour un site de documentation. Les ingénieurs expérimentés peuvent passer du temps à creuser cela. Cependant, ce livre comble le fossé.
    Par exemple, considérez la construction d'intégrations Astro personnalisées. Vous ne trouverez pas de meilleure ressource (pratique) que ce livre.
*   **Applications du monde réel** : parfois, pour assembler un puzzle, il est essentiel de le voir en action dans des exemples proches du monde réel. Ce livre explique des concepts importants et va au-delà pour les mettre en pratique dans des exemples comparatifs du monde réel.
*   **Gain de temps** : Ce livre vous fera économiser d'innombrables heures à bricoler avec des références et des exemples de code en tant que sous-produit des distinctions ci-dessus. Oui, vous pouvez passer des heures à creuser profondément dans la documentation ou le code source d'Astro, mais j'ai passé des heures (des mois, en fait) à le faire ! Je peux donc présenter les apprentissages sans que vous ayez à faire autant de travail. Mais ne vous y trompez pas – vous devez toujours faire le travail de lire le livre.

Envisagez de lire (ou de parcourir) la documentation officielle après avoir lu ce livre ou de l'utiliser comme référence. Ce livre complète la documentation officielle, il ne la remplace pas.

## Comment le livre est structuré

Chaque chapitre de ce livre est l'un des suivants :

1.  Un chapitre conceptuel
2.  Un chapitre projet
3.  Un chapitre projet et concept

Le mélange de ces différents types de chapitres vous gardera engagé et rendra votre apprentissage efficace. Rappelez-vous, l'objectif est une bonne compréhension.

### Chapitres conceptuels

![Les chapitres conceptuels sont les chapitres fondateurs pour le reste du livre.](https://blog.ohansemmanuel.com/content/images/2023/05/concept@2x.png)
_Les chapitres conceptuels sont les chapitres fondateurs pour le reste du livre._

Dans les chapitres conceptuels, nous apprendrons les concepts fondamentaux d'Astro. Ces chapitres incluront des exemples de code et des applications jetables. Nous ne construirons pas de projets du monde réel dans ces chapitres.

### Chapitres projets

![C'est l'heure du spectacle ! Rassemblez ce que nous avons appris pour construire un projet du monde réel.](https://blog.ohansemmanuel.com/content/images/2023/05/build.png)
_C'est l'heure du spectacle ! Rassemblez ce que nous avons appris pour construire un projet du monde réel._

Dans les chapitres projets, nous appliquerons les concepts précédents que nous avons appris pour construire un projet proche du monde réel.

### Chapitres concept et projet

![Rassemblez le meilleur des deux mondes. Construisez et apprenez de nouveaux concepts en cours de route.](https://blog.ohansemmanuel.com/content/images/2023/05/concept-and-build.png)
_Rassemblez le meilleur des deux mondes. Construisez et apprenez de nouveaux concepts en cours de route._

Un chapitre projet et concept se concentre sur la construction d'une application du monde réel tout en introduisant de nouveaux concepts.

## Aperçu des chapitres

Voici un résumé des chapitres du livre :

### Chapitre 1 : Construisez votre première application avec Astro

Le livre commence de manière pratique avec un chapitre projet et concept.

Dans ce chapitre, nous apprendrons les bases d'Astro tout en construisant un site web personnel riche en fonctionnalités.

### Chapitre 2 : Les composants Astro en profondeur

Ceci est un chapitre conceptuel qui va en profondeur dans les composants Astro. Nous irons au-delà des bases et maîtriserons (sans doute) l'entité essentielle d'Astro.

Nous commencerons par explorer un argument pour abandonner la surcharge d'exécution JavaScript (runtime overhead) lorsque cela est approprié. Nous étudierons ensuite le comportement du balisage des composants Astro, des styles et des scripts, ainsi que la puissante syntaxe de template.

### Chapitre 3 : Construisez votre propre îlot de composants

Ce chapitre projet s'éloigne d'Astro et considère l'architecture des îlots de composants de manière isolée.

Nous examinerons une vue d'ensemble du rendu d'application, comprendrons l'architecture des îlots depuis la base, et construirons notre propre implémentation à partir de zéro.

Ce chapitre consolidera vos connaissances fondamentales du nouveau modèle d'architecture web axé sur la performance.

### Chapitre 4 : La vie secrète des îlots de composants Astro

Ceci est un chapitre conceptuel où nous acquerrons une expérience pratique en travaillant avec des composants de framework dans Astro. Je vous présenterai l'hydratation responsable et pourquoi elle est importante.

Nous construirons de nombreuses applications jetables pour explorer comment les îlots de composants fonctionnent dans Astro et pourquoi ils sont significatifs.

### Chapitre 5 : Oh mon React ! (Le clone du site de documentation React)

Dans ce chapitre projet et concept, nous explorerons des techniques pour gérer de grandes quantités de contenu au sein d'une application Astro. De plus, nous examinerons des cas d'utilisation du monde réel pour fournir des exemples pratiques.

Ce chapitre consolidera les concepts précédents appris et en introduira de nouveaux pendant que nous construirons un clone du site de documentation React avec les meilleures pratiques de production.

### Chapitre 6 : Rendu côté serveur (SSR) dans Astro

Ce chapitre conceptuel explorera le rendu côté serveur et les nouvelles fonctionnalités débloquées dans une application Astro rendue côté serveur. Nous explorerons le routage dynamique, les points de terminaison API, le streaming serveur, et bien plus encore.

### Chapitre 7 : Soyez Audible ! (Projet Astro Fullstack)

Ce chapitre projet vous emmènera au-delà des sites statiques vers la construction d'applications full stack avec Astro. Dans ce chapitre, je soutiendrai que si vous pouvez construire l'application comme une MPA (Multi-Page Application) et tirer parti des îlots de composants, vous pouvez la construire avec Astro.

### Chapitre 8 : Construisez vos propres intégrations Astro

Ceci est un chapitre projet et concept où nous répondrons à la question : que se passe-t-il lorsque vous voulez une fonctionnalité en dehors de ce qu'Astro fournit par défaut ?

Nous exploiterons les hooks dans le processus de build d'Astro pour construire des fonctionnalités personnalisées. Celles-ci sont appelées intégrations Astro.

### Chapitre 9 : Conclusion

Ici, nous prendrons du recul et apprécierons le chemin parcouru. Ensuite, nous réitérerons les fonctionnalités qui font qu'Astro se démarque. Des fonctionnalités que vous avez déjà vues en pratique !

C'est là que notre voyage se termine probablement, et que votre voyage dans le monde d'Astro commence.

## Prérequis

J'ai essayé de faire en sorte que ce livre "fonctionne pour tout le monde", mais c'est incroyablement difficile.

Donc, pour tirer le meilleur parti de ce livre :

*   Vous devriez déjà connaître un peu de HTML, CSS et JS : ce n'est pas un guide pour débutant en développement web.
*   Vous devriez déjà connaître les bases de TypeScript : je ne m'attends pas à ce que vous soyez un champion de TypeScript, mais une compréhension superficielle vous préparera pour tout le TypeScript dans ce livre.

J'ai écrit ce livre spécifiquement pour les ingénieurs intermédiaires, seniors et seniors+, et le livre contient des chapitres de difficulté technique variable. Mais j'ai fait de mon mieux pour les expliquer clairement et visuellement afin de satisfaire différents niveaux de compétence.

## Conventions typographiques

Lorsque le texte est écrit dans une police à chasse fixe (monospaced), cela représente généralement des exemples de code. Ces exemples peuvent être des fragments autonomes ou faire référence à une section spécifique du code d'une application.

Voici un exemple :

```js
---
const { author } = Astro.props;
const book = "Understanding Astro.js";
---

<h1 data-name={book}>A new book</h1>

```

Parfois, pour montrer la source du code, j'ai ajouté un commentaire avec le chemin du fichier en haut du bloc de code, comme indiqué ci-dessous :

```js
{/** 📂 src/pages/index.astro **/}
---
const { author } = Astro.props;
const book = "Understanding Astro.js";
---

<h1 data-name={book}>A new book</h1>

```

Avec des fragments de code faisant référence à des changements dans le code d'une application voisine, vous trouverez des points de suspension pour signifier qu'il n'y a pas de changements de code dans le code précédent, comme ceci :

```js
// ...
<h1 data-name={book}>A changed book name</h1>

```

Le code ci-dessus suggère que le bloc de code précédent reste le même, à l'exception du nouveau `<h1>` avec `A changed book name`.

Enfin, le livre utilise le gestionnaire de paquets `npm`. Par exemple, le code pour installer un paquet sera décrit comme indiqué ci-dessous :

```bash
npm install some-package

```

Vous pouvez utiliser les commandes associées pour d'autres gestionnaires de paquets, tels que `yarn` ou `pnpm`.

Ouf ! Assez de tâches ménagères. Maintenant, plongeons dans Astro !

## Vous voulez obtenir l'eBook ?

![Image](https://www.freecodecamp.org/news/content/images/2023/06/book-cover-transparent-1.png)
_[Télécharger l'ebook sur Github](https://github.com/understanding-astro/understanding-astro-book)_

*   500+ pages de valeur
*   4+ chapitres de projets pratiques
*   100+ illustrations et images soigneusement conçues
*   Apprenez des techniques pour construire des applications plus rapides
*   **Intégrez React, Svelte, Vue, Tailwind** et plus encore dans un projet Astro
*   Apprenez à construire votre propre **implémentation d'îlots de composants** à partir de zéro
*   Apprenez à **construire des applications full stack avec Astro** (sans sacrifier la performance)
*   Allez **au-delà des bases** et analysez le code Astro en ASTs et construisez des fonctionnalités de projet personnalisées

[Téléchargez l'ebook gratuit sur GitHub.](https://ohans.me/ua-github)

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-133.png)
_Chapitre un._

## Chapitre 1 : Construisez votre première application Astro

> "Longue est la route de l'apprentissage par les préceptes, mais courte et fructueuse par les exemples." – Sénèque le Jeune.

Cet essai commencera par les bases d'Astro en construisant une application pratique : un site web personnel. Pour voir l'application complète, consultez le [dépôt GitHub](https://github.com/understanding-astro/astro-beginner-project).

## Ce que vous apprendrez

*   Construire un site web personnel avec Astro.
*   Configurer un environnement de développement local pour Astro.
*   Familiarité avec les composants Astro, les mises en page (layouts) et les pages.
*   Une connaissance pratique des styles et des scripts dans Astro.
*   Thématisation des sites Astro via des variables CSS.
*   Exploiter les pages markdown pour la facilité.
*   Déploiement d'une application Astro statique.

## Aperçu du projet

Je me souviens de mon premier projet de développement web commercial. Rétrospectivement, c'était un désastre. Un projet construit par un ingénieur autodidacte passionné, mais un désastre quand même.

Faisons de votre premier projet Astro un projet dont vous vous souviendrez en bien.

%[

## Pour commencer

**Astro est un framework web conçu pour la vitesse**. Avant d'arriver aux bonnes choses, assurons-nous que nous sommes tous les deux sur la même longueur d'onde.

### Installer Node.js

Tout d'abord, assurez-vous d'avoir Node.js installé.

Si vous n'êtes pas sûr, exécutez `node --version` dans votre terminal. Vous obtiendrez une version de Node si Node.js est installé.

![Obtenir la version de NodeJS depuis la CLI.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-29-at-11.11.18@2x.png)
_Obtenir la version de NodeJS depuis la CLI._

Vous n'avez pas Node installé ? Alors, visitez la page officielle de [téléchargement](https://nodejs.org/en/download) et installez le paquet nécessaire pour votre système d'exploitation. C'est aussi simple que d'installer n'importe quel autre programme informatique. Clic, clic, clic !

![La page de téléchargement de NodeJS.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-28-at-10.44.30@2x.png)
_La page de téléchargement de NodeJS._

### Comment configurer votre éditeur de code

J'éviterai tout débat houleux sur l'éditeur de code avec lequel vous devriez écrire des logiciels. Très franchement, cela m'est égal.

Cependant, j'utilise Visual Studio Code (VSCode).

Vous pouvez développer des applications Astro avec n'importe quel éditeur de code, mais VSCode est également l'éditeur officiellement recommandé pour Astro.

Si vous construisez avec VSCode, installez l'[extension Astro](https://marketplace.visualstudio.com/items?itemName=astro-build.astro-vscode) officielle. Cela aide avec la coloration syntaxique et sémantique, les messages de diagnostic, IntelliSense, et plus encore.

![L'extension VSCode officielle d'Astro.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-28-at-11.03.36@2x.png)
_L'extension VSCode officielle d'Astro._

Commençons maintenant à configurer notre premier projet Astro. Pour ce faire, nous devons installer Astro. Le moyen le plus rapide de le faire est d'utiliser la CLI automatique d'Astro.

Pour lancer l'assistant d'installation, exécutez la commande suivante :

```bash
npm create astro@latest

```

Si vous êtes sur `pnpm` ou `yarn`, la commande ressemble à ceci :

```bash
# en utilisant pnpm
pnpm create astro@latest


# en utilisant yarn
yarn create astro

```

![Démarrer un nouveau projet avec l'assistant CLI Astro.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-28-at-11.15.44@2x.png)
_Démarrer un nouveau projet avec l'assistant CLI Astro._

Cela lancera l'assistant, qui nous guidera à travers des invites utiles. Il est important de mentionner que nous pouvons exécuter cela de n'importe où sur notre machine et choisir plus tard où exactement nous voulons que le projet soit créé.

Lorsqu'on vous demande, "Where should we create your new project?" (Où devrions-nous créer votre nouveau projet ?), allez-y et passez un chemin de fichier. Dans mon cas, c'est `documents/dev/books/understanding-astro/astro-beginner-project`.

Alternativement, nous aurions pu exécuter la commande `npm create astro@latest` dans notre répertoire souhaité et simplement entrer un chemin de fichier plus court, par exemple, `./astro-beginner-project`.

Lorsqu'on vous demande, "How would you like to start your new project?" (Comment souhaitez-vous démarrer votre nouveau projet ?), allez-y et choisissez "Empty" (Vide).

![Répondre à l'invite de modèle CLI.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-28-at-11.20.54@2x.png)
_Répondre à l'invite de modèle CLI._

Nous voulons un nouveau départ pour explorer Astro depuis la base.

Maintenant, on nous demandera d'installer les dépendances ou non. Sélectionnez oui et appuyez sur entrée pour continuer l'installation.

![Installer les dépendances dans l'invite CLI.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-28-at-11.22.21@2x.png)
_Installer les dépendances dans l'invite CLI._

Une fois les dépendances installées, répondez à l'invite "Do you plan to write TypeScript?" (Prévoyez-vous d'écrire du TypeScript ?) par un oui et choisissez l'option "strictest" (la plus stricte).

Nous voulons une sécurité de type forte.

![Choisir Typescript dans l'invite CLI.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-28-at-11.24.22@2x.png)
_Choisir Typescript dans l'invite CLI._

Ensuite, répondez à la question "Initialise a new Git repository?" (Initialiser un nouveau dépôt Git ?) avec ce qui vous convient. Je vais répondre oui ici et appuyer sur entrée.

![Initialiser git dans l'invite CLI.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-28-at-11.25.33@2x.png)
_Initialiser git dans l'invite CLI._

Et voilà ! Croyez-le ou non, notre nouveau projet est déjà créé et prêt à partir !

Changez de répertoire pour aller là où vous avez configuré le projet. Dans mon cas, cela ressemble à ceci :

```html
cd ./documents/dev/books/understanding-astro/astro-beginner-project

```

Et ensuite exécutez l'application via ce qui suit :

```html
npm run start

```

Cela démarrera l'application en direct sur un port local disponible 🚀

![Le projet Astro de base fonctionnant sur localhost:3000](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-28-at-11.29.57@2x.png)
_Le projet Astro de base fonctionnant sur localhost:3000_

## Structure du projet

Ouvrez le projet nouvellement créé dans votre éditeur de code, et vous remarquerez que l'assistant CLI `create astro` a inclus quelques fichiers et dossiers.

Astro a une structure de dossiers arrêtée. Nous pouvons voir une partie de cela dans notre nouveau projet. Par conception, chaque projet Astro inclura ce qui suit dans le répertoire racine :

<table>
	<thead>
		<tr>
			<th>
				Fichier / Répertoire
			</th>
			<th>
				Quoi ?
			</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<br>astro.config.mjs
			</td>
			<td>
				<br>Le fichier de configuration Astro. C'est là que nous fournissons <br>les options de configuration pour notre projet Astro.<br>
			</td>
		</tr>
		<tr>
			<td>
				<br>tsconfig.json
			</td>
			<td>
				<br>Un fichier de configuration Typescript. Cela spécifie les fichiers racines et les options du compilateur Typescript.<br>
			</td>
		</tr>
		<tr>
			<td>
				<br>package.json
			</td>
			<td>
				<br>Un fichier JSON qui contient les métadonnées du projet. <br>On le trouve généralement à la racine de la plupart des projets Node.js. <br>
			</td>
		</tr>
		<tr>
			<td>
				<br>public/<em></em>
			</td>
			<td>
				<br>Ce répertoire contient des fichiers et des actifs qui seront copiés <br>dans le répertoire de build Astro sans modification, par exemple, des polices, des images et <br>des fichiers tels que <code>robots.txt</code><br>
			</td>
		</tr>
		<tr>
			<td>
				<br>src/<em></em>
			</td>
			<td>
				<br>Le code source de notre projet réside ici.<br>
			</td>
		</tr>
	</tbody>
</table>

Regardons maintenant les fichiers dans notre projet nouvellement généré.

### Fichier `tsconfig.json`

Le contenu de notre fichier `tsconfig.json` est le suivant :

```js
{
  "extends": "astro/tsconfigs/strictest"
}

```

La propriété `extends` pointe vers le chemin du fichier de configuration de base dont il faut hériter, c'est-à-dire hériter la configuration typescript du fichier dans `astro/tsconfigs/strictest`.

En utilisant votre éditeur, naviguez vers le chemin référencé – par exemple dans `vscode` en cliquant sur le lien tout en maintenant `CMD`. Cela nous mènera à `node_modules/astro/tsconfigs/strictest.json`, où nous trouverons un fichier bien annoté :

```js
{
  ...
  "compilerOptions": {
    // Report errors for fallthrough cases in switch statements
    "noFallthroughCasesInSwitch": true,

    // Force functions designed to override their parent class to be specified as `override`.
    "noImplicitOverride": true,

    // Force functions to specify that they can return `undefined` if a possible code path does not return a value.
    "noImplicitReturns": true,
	 ...
  }
}

```

C'est très bien annoté, donc nous ne passerons pas de temps là-dessus. Mais les `compilerOptions` pour TypeScript sont définies dans ce fichier. Le point à retenir ici est qu'Astro conserve une liste de configurations TypeScript (`base`, `strict` et `strictest`) que notre projet exploite lorsque nous l'initialisons via l'assistant CLI.

Dans cet exemple, nous laisserons le fichier `tsconfig.json` tel quel. TypeScript (et par conséquent le fichier `tsconfig.json`) est optionnel dans les projets Astro. Mais je vous recommande fortement d'utiliser TypeScript. Nous le ferons tout au long du livre.

### Fichier `package.json`

Le fichier `package.json` est facile à comprendre. Il contient des métadonnées sur notre projet et inclut des scripts pour gérer notre projet Astro, comme `npm start`, `npm run build`, et `npm preview`.

### Fichier `package-lock.json`

Le fichier `package-lock.json` est un fichier généré automatiquement qui contient des informations sur les dépendances/paquets de notre projet. Nous ne toucherons pas à ce fichier manuellement. Au lieu de cela, il est généré (et mis à jour) automatiquement par npm.

Notez que le fichier de verrouillage d'un projet peut différer selon le gestionnaire de paquets, par exemple yarn ou pnpm.

### Fichier `astro.config.mjs`

La plupart des frameworks définissent un moyen pour nous de spécifier nos configurations spécifiques au projet. Par exemple, Astro réalise cela via le fichier `astro.config`.

```js
import { defineConfig } from 'astro/config';

export default defineConfig({});

```

Pour le moment, il définit une configuration vide. Nous allons donc le laisser tel quel. Mais c'est le bon endroit pour spécifier différentes options de build et de serveur, par exemple.

### Fichier `src/env.d.ts`

Les fichiers `d.ts` sont appelés fichiers de déclaration de type. Oui, c'est pour TypeScript uniquement, et ils existent dans un seul but : décrire la forme d'un module existant. Les informations contenues dans ce fichier sont utilisées pour la vérification de type par TypeScript.

```js
/// <reference types="astro/client" />

```

Le contenu du fichier pointe vers `astro/client`. C'est essentiellement une référence à un autre fichier de déclaration à `astro/client.d.ts`

### Fichier `src/pages/index.astro`

Comme mentionné précédemment, le dossier `src` est l'endroit où réside le code source de notre projet. Mais qu'est-ce que le répertoire `pages`, et pourquoi y a-t-il un fichier `index.astro` ?

Tout d'abord, considérez le contenu du fichier `index.astro` :

```js
---
---

<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width" />
    <meta name="generator" content={Astro.generator} />
    <title>Astro</title>
  </head>
  <body>
    <h1>Astro</h1>
  </body>
</html>

```

Vous remarquerez qu'il ressemble remarquablement au HTML standard, à quelques exceptions près.

Aussi, remarquez ce qui est écrit à l'intérieur de la balise `<body>` : un élément `<h1>` avec le texte `Astro`.

Si nous visitons l'application en cours d'exécution dans le navigateur, nous avons le `<h1>` rendu.

![L'en-tête de page rendu.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-11-at-14.18.20@2x.png)
_L'en-tête de page rendu._

Maintenant, changez le texte pour lire `<h1>Hello world</h1>` et remarquez comment la page est mise à jour dans le navigateur :

![L'en-tête de page mis à jour.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-11-at-14.19.41@2x.png)
_L'en-tête de page mis à jour._

Cela nous amène gentiment à discuter des pages dans Astro — ce que je considère comme le point d'entrée de notre application.

## Introduction aux pages Astro

Astro exploite un système de routage basé sur les fichiers. Il réalise cela en utilisant les fichiers dans le répertoire `src/pages`.

Par exemple, le fichier `src/pages/index.astro` correspond à la page `index` servie dans le navigateur.

![La page d'index du projet.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-29-at-09.49.26@2x.png)
_La page d'index du projet._

Allons-y et créons une page `src/pages/about.astro` avec un contenu similaire à `index.astro` comme indiqué ci-dessous :

```js
// 📂 src/pages/about.astro
---
---

<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width" />
    <meta name="generator" content={Astro.generator} />
    <title>About us</title>
  </head>
  <body>
    <h1>About us</h1>
  </body>
</html>

```

*   Copiez et collez le contenu exact de `index.astro` dans `about.astro`.
*   Changez le `<h1>` pour avoir le texte `About us`.

Maintenant, si nous naviguons vers `/about` dans le navigateur, nous devrions avoir la nouvelle page rendue.

![La page "About us".](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-29-at-09.50.13@2x.png)
_La page "About us"._

### Qu'est-ce qui fait une page Astro valide ?

Nous avons défini les pages Astro comme des fichiers dans le répertoire `src/pages/`. Malheureusement, ce n'est que partiellement correct.

Par exemple, si nous dupliquons le fichier `favicon.svg` dans `public/favicon.svg` vers le répertoire `pages`, cela représente-t-il une page `favicon` ?

![Dupliquer le favicon dans le répertoire pages.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-29-at-09.55.21.png)
_Dupliquer le favicon dans le répertoire pages._

Même si `index.astro` et `about.astro` correspondent aux pages index et about de notre site web, `/favicon` renverra une erreur `404: Not found`.

![La route /favicon.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-29-at-09.56.51@2x.png)
_La route /favicon._

C'est parce que seuls des fichiers spécifiques font une page Astro valide. Par exemple, si nous considérons les fichiers `index` et `about` dans le répertoire `pages`, vous remarquez peut-être quelque chose : ils ont tous les deux la terminaison de fichier `.astro` !

En termes simples, ce sont des fichiers Astro, mais une terminologie plus technique pour ceux-ci est composants Astro.

Alors, petit quiz : qu'est-ce qu'un composant Astro ?

C'est facile — un fichier avec la terminaison `.astro`.

10 points pour vous ! Bien joué.

## Anatomie d'un composant Astro

Nous avons établi que `index.astro` et `about.astro` représentent des composants Astro et sont des pages Astro valides.

Maintenant, creusons dans le contenu de ces fichiers.

Considérez le contenu de la page `index.astro` :

```js
// 📂 src/pages/index.astro
---
---

<html lang="en">
  <!-- removed for brevity -->

</html>

```

Remarquez la distinction entre les deux parties du contenu de ce fichier.

La section en bas contient le balisage de la page :

```js
// 📂 src/pages/index.astro
// ...
<html lang="en">
  <!-- removed for brevity -->
</html>

```

Cette partie est appelée la section **template de composant**.

Tandis que la section supérieure contient une syntaxe plutôt étrange ressemblant à un diviseur :

```js
---
---

```

Cette partie est appelée la section **script de composant**, et le `---` est appelé une barrière (fence).

Ensemble, ils constituent un composant Astro.

Essayons la section script de composant.

Le nom de la section laisse entendre ce que fait cette section du composant. À l'intérieur de la barrière de code du script de composant, nous pouvons déclarer des variables, importer des paquets et profiter pleinement de JavaScript ou TypeScript.

Oh oui, TypeScript !

Commençons par créer une variable pour contenir la photo de profil de notre utilisateur, comme indiqué ci-dessous :

```js
// 📂 src/pages/index.astro
---
const profilePicture = "https://i.imgur.com/JPGFE75.jpg";
---

```

Nous pouvons ensuite profiter de la section template de composant pour référencer cette image comme indiqué ci-dessous :

```js
// 📂 src/pages/index.astro
---
const profilePicture = "https://i.imgur.com/JPGFE75.jpg";
---

<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width" />
    <meta name="generator" content={Astro.generator} />
    <title>Astro</title>
  </head>
  <body>
    <!-- 👀 Look here  -->
    <img
      src={profilePicture}
      alt="Frau Katerina's headshot."
      width="100px"
      height="100px"
    />
  </body>
</html>


```

Notez que la variable `profilePicture` est référencée en utilisant des accolades `{ }`. C'est ainsi que l'on référence des variables du script de composant dans le balisage du composant.

Maintenant, nous devrions avoir l'image rendue sur la page d'accueil :

![Rendre la photo de profil de l'utilisateur.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-29-at-10.30.54@2x.png)
_Rendre la photo de profil de l'utilisateur._

Ce n'est pas grand-chose, mais c'est du travail honnête, hein ?

Allons-y et étoffons la page pour avoir le balisage du profil de l'utilisateur :

```js
// 📂 src/pages/index.astro
// ...
  <body>
    <!-- Look here 👀 -->
    <div>
      <img
        src={profilePicture}
        alt="Frau Katerina's headshot."
        width="100px"
        height="100px"
      />
      <div>
        <h1>Frau Katerina</h1>
        <h2>VP of Engineering at Goooogle</h2>
        <p>
          Helping developers be excellent and succeed at building scalable
          products
        </p>
      </div>
    </div>
  </body>
// ...

```

Comme vous l'avez peut-être remarqué, nous écrivons une syntaxe ressemblant à du `HTML` dans la section balisage du composant !

Maintenant, nous devrions avoir la photo de l'utilisateur et sa bio rendues dans le navigateur comme suit :

![La photo de profil de l'utilisateur et sa bio.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-10-at-14.07.31@2x.png)
_La photo de profil de l'utilisateur et sa bio._

## Styles de composants

Le style dans Astro est relativement facile à comprendre. Ajoutez une balise `<style>` à un composant, et Astro gérera automatiquement son style.

Bien qu'il soit possible de sélectionner des éléments directement, allons-y et ajoutons des classes au balisage du composant pour faciliter cela :

```js
// 📂 src/pages/index.astro
// ...
<div class="profile">
    <img
      src={profilePicture}
      class="profile__picture"
      {/** ... **/}
    />
    <div class="profile__details">
      <h1>Frau Katerina</h1>
      {/** ... **/}
    </div>
</div>
// ...

```

Ajoutez une balise `<style>`, et écrivez du CSS comme d'habitude :

```js
// ...
<style>
  .profile {
    display: flex;
    align-items: flex-start;
    flex-wrap: wrap;
    padding: 1rem 0 3rem 0;
  }

  .profile__details {
    flex: 1 0 300px;
  }

  .profile__details > h1 {
    margin-top: 0;
  }

  .profile__picture {
    border-radius: 50%;
    margin: 0 2rem 1rem 0;
  }
</style>


```

Les détails de l'utilisateur devraient maintenant être stylisés comme prévu.

![Appliquer des styles au composant de page index.astro.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-01-at-08.42.27@2x.png)
_Appliquer des styles au composant de page index.astro._

Si nous inspectons les styles finaux appliqués à nos éléments UI via les outils de développement du navigateur, nous remarquerons que les sélecteurs de style semblent différents.

Par exemple, pour styliser le nom de l'utilisateur, nous avons écrit le CSS suivant :

```js
.profile__details > h1 {
  margin-top: 0;
}

```

Cependant, ce qui est appliqué dans le navigateur ressemble à quelque chose comme ceci :

```js
.profile__details:where(.astro-J7PV25F6) > h1:where(.astro-J7PV25F6) {
  margin-top: 0;
}

```

Pourquoi cela ?

Les déclarations de style réelles pour l'élément `h1` restent inchangées. La seule différence ici est le sélecteur.

L'élément `h1` a maintenant des noms de classe générés automatiquement, et le sélecteur est maintenant scopé via le sélecteur CSS `:where`.

Cela est fait en interne par Astro. Cela garantit que les styles que nous écrivons ne fuient pas au-delà de notre composant. Par exemple, si nous stylisions chaque `h1` dans notre composant comme suit :

```css
h1 {
  color: red
}

```

Le style final appliqué dans le navigateur sera similaire à ce qui suit :

```css
h1:where(.astro-some-unique-id) {
  color: red
}

```

Cela garantira que tous les autres `h1` dans notre projet restent les mêmes, et ce style s'applique uniquement au `h1` de notre composant spécifique.

## Mises en page (Layouts)

Regardez les pages de notre application terminée. Vous remarquerez peut-être qu'elles ont toutes des formes identiques.

![Une décomposition de la structure des pages de l'application.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-01-at-09.10.55.png)
_Une décomposition de la structure des pages de l'application._

Il y a une barre de navigation, un pied de page, et un conteneur qui contient le contenu principal de la page.

Devrions-nous répéter ces structures UI similaires sur toutes les pages ?

La plupart des gens répondront "Non". Alors, y a-t-il un moyen de partager des structures UI réutilisables entre les pages ?

Oui, oui, oui ! C'est là que les mises en page (layouts) entrent en jeu.

Les mises en page sont des composants Astro avec une particularité. Ils sont utilisés pour fournir des structures UI réutilisables à travers les pages, par exemple des barres de navigation et des pieds de page.

Conventionnellement, les mises en page sont placées dans le répertoire `src/layouts`. Ce n'est pas obligatoire mais c'est un modèle très répandu.

Allons-y et créons notre première mise en page dans `src/layouts/Main`. Nous ferons cela en déplaçant toutes les structures UI réutilisables actuellement dans `index.astro` comme suit :

```js
// 📂 src/layouts/Main.astro
---
---

<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width" />
    <meta name="generator" content={Astro.generator} />
    {/* Add a new meta description tag */}
    <meta name="description" content="Frau Katarina's website" />
    {/* Title is hardcoded as Astro, for now. */}
    <title>Astro</title>
  </head>
  <body>
    <main>
      {/* We want the content of each page to go here */}
    </main>
  </body>
</html>

```

*   Nous avons déplacé les éléments `<html>`, `<head>` et `<body>` vers la mise en page `Main.astro`.
*   Nous avons également introduit une nouvelle balise `<meta name=description />` pour le SEO.
*   Nous avons également introduit un élément `<main>` où nous voulons que le reste de notre page aille.
*   Notez que le nom de fichier de la mise en page commence par une majuscule, c'est-à-dire `Main.astro`, pas `main.astro`.

D'une part, les mises en page sont uniques parce qu'elles font principalement une chose : fournir des structures réutilisables. Mais, d'autre part, elles ne sont pas uniques. Elles sont comme les autres composants Astro et peuvent faire tout ce qu'un composant peut faire.

## Comment rendre des composants et des slots

Rendre un composant Astro est similaire à la façon dont vous tenteriez de rendre un élément HTML. Par exemple, nous rendrions un div en écrivant ce qui suit :

```js
<div>
 render something within the div
</div>

```

Il en va de même pour les composants Astro.

Pour rendre le composant `Main.astro`, nous ferions quelque chose de similaire :

```js
<Main>
  render something within the Main component
</Main>

```

Mettons cela en pratique. Nous pouvons maintenant utiliser la mise en page `Main` dans la page `index.astro`. Pour ce faire, nous ferons ce qui suit :

*   Importer la mise en page `Main` depuis `"../layouts/Main.astro"`
*   Substituer les éléments `<html>`, `<head>` et `<body>` par la mise en page `<Main>` dans `index.astro`.

```js
---
import Main from "../layouts/Main.astro";

const profilePicture = "https://i.imgur.com/JPGFE75.jpg";
---

<Main>
  <div class="profile">
    <img
      src={profilePicture}
      class="profile__picture"
      alt="Frau Katerina's headshot."
      width="100px"
      height="100px"
    />
    <div class="profile__details">
      <h1>Frau Katerina</h1>
      <h2>VP of Engineering at Goooogle</h2>
      <p>
        Helping developers be excellent and succeed at building scalable
        products
      </p>
    </div>
  </div>
</Main>

```

Si nous vérifions notre application, nous aurions une page `index` blanche.

![Page d'application blanche.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-10-at-17.18.07.png)
_Page d'application blanche._

Pourquoi cela ?

Contrairement aux éléments HTML, les éléments enfants dans la balise `<Main>` ne sont pas automatiquement rendus.

```js
{/** Child div will not be automatically rendered */}
<Main>
  <div>Hello from child</div>
<Main>

```

Le composant de mise en page `<Main>` est rendu, et rien d'autre. Les composants enfants ne le sont pas. D'où la page vide.

Pour rendre les éléments enfants d'un composant Astro, nous devons spécifier où rendre ceux-ci en utilisant un élément `<slot />`.

![Injecter des éléments enfants dans un slot.](https://blog.ohansemmanuel.com/content/images/2023/06/a.png)
_Injecter des éléments enfants dans un slot._

Ajoutons un `<slot>` à l'intérieur de `Main.astro` :

```js
//...
  <body>
    <main>
      {/* We want the content of each page to go here */}
       <slot />
    </main>
  </body>

```

![Page refactorisée pour utiliser un composant de mise en page réutilisable.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-10-at-17.19.59.png)
_Page refactorisée pour utiliser un composant de mise en page réutilisable._

Nous devrions maintenant avoir notre page rendue avec la mise en page réutilisable en place.

## Capitalisation des noms de composants

Nous avons mis une majuscule au nom de fichier du composant de mise en page `Main.astro`, mais est-ce important ?

Théoriquement, la réponse est non.

Nous pourrions créer un fichier avec un nom en minuscules, par exemple `mainLayout.astro` et importer le composant comme suit :

```js
import Main from "../layouts/mainLayout.astro";

```

C'est parfaitement correct.

Mais là où nous rencontrons des problèmes, c'est si nous nommons le composant importé avec une minuscule :

```js
// main NOT Main
import main from "../layouts/mainLayout.astro";

```

Dans ce cas, nous rencontrerons des problèmes lorsque nous tenterons de rendre le composant, car le nom entre en conflit avec l'élément HTML standard `main`.

Pour cette raison, c'est une pratique courante de mettre une majuscule aux noms de fichiers des composants et au nom de la variable importée.

## La directive de style global

La mise en page `Main` est en place mais n'ajoute pas grand-chose à notre page. Commençons par ajouter quelques styles pour les en-têtes et centrons également le contenu de la page :

```html
<!-- 📂 src/layouts/Main.astro -->
<style>
  h1 {
    font-size: 3rem;
    line-height: 1;
  }

  h1 + h2 {
    font-size: 1.1rem;
    margin-top: -1.4rem;
    opacity: 0.9;
    font-weight: 400;
  }

  main {
    max-width: 40rem;
    margin: auto;
  }
</style>

```

Avec cela, nous aurons l'élément `main` centré, mais les en-têtes, `h1` et `h2` restent non stylisés.

![Une comparaison des changements avant et après le style du composant de mise en page.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-10-at-17.21.33.png)
_Une comparaison des changements avant et après le style du composant de mise en page._

C'est parce que les styles appliqués via la balise `<style>` sont scopés localement par défaut.

Pouvez-vous me dire pourquoi ?

L'élément `main` réside dans la mise en page `Main`. Mais les en-têtes `h1` et `h2` existent dans un composant `index.astro` différent.

Pour notre cas d'utilisation, nous avons besoin de styles globaux.

Nous devons sortir des styles scopés localement par défaut que le composant Astro fournit, mais comment faisons-nous cela ?

Les styles globaux peuvent être un cauchemar — sauf quand ils sont vraiment nécessaires. Pour de tels cas, Astro fournit plusieurs solutions. La première est d'utiliser ce qu'on appelle une directive de template de style global.

Je sais que ça a l'air compliqué ! Mais en termes simples, les directives de template dans Astro sont différents types d'attributs HTML qui peuvent être utilisés dans les templates de composants Astro.

Par exemple, pour sortir du comportement par défaut de `<style>` scopé localement, nous pouvons ajouter un attribut `is:global` comme indiqué ci-dessous :

```html
<style is:global>
 ...
</style>

```

Cela supprimera le scoping CSS local et rendra les styles disponibles globalement.

![Styles globaux maintenant intégrés dans la page via <style>.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-01-at-11.06.50.png)
_Styles globaux maintenant intégrés dans la page via &lt;style&gt;._

## Polices personnalisées et CSS global

Les composants de mise en page de base comme `Main.astro` sont un excellent endroit pour avoir des propriétés globales telles que des styles globaux et des polices personnalisées.

Nous avons ajouté des styles globaux via la directive de template `is:global`. Mais alternativement, nous pourrions avoir tous les styles globaux importés dans `Main.astro` depuis un fichier `global.css`.

Dans les cas où un projet nécessite l'importation d'un fichier css global existant, c'est l'approche la plus simple.

Par exemple, refactorisons notre projet pour utiliser `global.css`. Pour ce faire, déplacez tout le contenu CSS à l'intérieur de l'élément `<style is:global>` vers `src/styles/global.css`. Ensuite, importez les styles dans le frontmatter du composant `Main.astro` :

```js
// 📂 src/layouts/Main.astro
---
import "../styles/global.css";
---

```

Cela chargera et injectera le style sur la page.

Maintenant, tournons notre attention vers les polices globales.

Nous utiliserons la police Google [Inter](https://fonts.google.com/specimen/Inter) pour le projet, mais comment faisons-nous cela ?

Techniquement parlant, pour ajouter Inter à notre projet, nous devons ajouter les `<link>`s vers Inter sur chaque page requise.

Mais au lieu de nous répéter sur chaque page, nous pouvons tirer parti du composant de mise en page partagé `Main.astro`.

Allez-y et ajoutez les `<link>`s vers la police Inter comme indiqué ci-dessous :

```js
// 📂 src/layouts/Main.astro
<html lang="en">
  <head>
    {/** 👀 Look here ... */}
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap"
      rel="stylesheet"
    />
  </head>
  {/** ... */}
</html>

```

Nous pouvons maintenant mettre à jour le fichier `global.css` pour utiliser la nouvelle famille de polices :

```css
body {
  font-family: "Inter", sans-serif;
  padding: 0 0.5rem; /* Additional body style */
}

```

Et boum ! Nous avons réglé les polices globales.

![La page avec des polices et des styles globaux.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-10-at-17.41.13.png)
_La page avec des polices et des styles globaux._

## Composants Astro indépendants

Nous avons discuté de deux types spéciaux de composants Astro : les mises en page et les pages.

Mais un site fonctionnel est composé de plus que de simples mises en page et pages. Par exemple, différents blocs d'interfaces utilisateur sont généralement intégrés dans une page. Ces blocs d'interfaces utilisateur indépendants et réutilisables peuvent également être représentés à l'aide de composants Astro.

Mettons cela en pratique en créant des composants `NavigationBar` et `Footer` à utiliser dans la mise en page `Main.astro`.

Lors de la création de composants, une convention standard est de les avoir dans le répertoire `src/components`. Allons-y et créons-en un.

```js
// 📂 src/components/Footer.astro
<footer>&copy; Frau Katerina</footer>

<style>
  footer {
    /* Applies top and bottom paddings */
    padding: 3rem 0;
    /* Centers the text content */
    text-align: center;
    /* Makes the font smaller */
    font-size: 0.9rem;
  }
</style>

```

Créons également un composant `NavigationBar` :

```js
// 📂 src/components/NavigationBar.astro
---
---

<nav>
  <ul>
    <li>
      <a href="/">Home</a>
    </li>

    <li>
      {/** Link points nowhere for now*/}
      <a href="#">Philosophies</a>
    </li>

    <li>
      {/** Link points nowhere for now*/}
      <a href="#">Beyond technology</a>
    </li>
  </ul>
</nav>

<style>
  nav {
    display: flex;
    align-items: flex-start;
    padding: 2rem 0;
  }

  ul {
    display: flex;
    flex-wrap: wrap;
    padding: 0;
    margin: 0 auto 0 0;
  }

  nav li {
    opacity: 0.8;
    list-style: none;
    font-size: 0.95rem;
  }

  a {
    padding: 0.5rem 1rem;
    border-radius: 10px;
    text-decoration: none;
  }
</style>

```

Maintenant, rendez le `NavigationBar` et le `Footer` comme indiqué ci-dessous :

```js
// 📂 src/layouts/Main.astro
---
//...
import Footer from "../components/Footer.astro";
import NavigationBar from "../components/NavigationBar.astro";
---

{/** ... **/}
<main>
  <NavigationBar />

  <slot />

  <Footer />
</main>

```

![Barre de navigation et pied de page rendus.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-01-at-15.17.48@2x.png)
_Barre de navigation et pied de page rendus._

## Comment ajouter des scripts interactifs

Une partie intégrante de la philosophie d'Astro est de ne livrer aucun JavaScript par défaut au navigateur.

Cela signifie que nos pages sont compilées en pages `HTML` avec tout le JavaScript supprimé par défaut.

Vous pourriez demander, qu'en est-il de tout le JavaScript écrit dans la section script de composant d'un composant Astro ?

Le script de composant et le balisage seront utilisés pour générer la ou les pages `HTML` finales envoyées au navigateur.

Par exemple, allez-y et ajoutez un simple `console.log` au frontmatter de la page `index.astro` :

```js
// 📂 src/pages/index.astro
---
console.log("Hello world!");
---

```

Inspectez la console du navigateur et remarquez comment le journal n'arrive jamais au navigateur !

Alors, où est le journal ?

Astro s'exécute sur le serveur. Dans notre cas, cela représente notre serveur de développement local. Donc, le `console.log` apparaîtra dans le terminal où Astro sert notre application locale.

![Journaux du serveur Astro.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-01-at-17.55.33.png)
_Journaux du serveur Astro._

Lorsque nous construirons finalement notre application pour la production avec `npm run build`, Astro produira des fichiers `HTML` correspondant à nos pages dans `src/pages`.

Dans cet exemple, le message `Hello world!` sera journalisé mais n'entrera pas dans les pages `HTML` compilées.

![Journaux pendant la construction de l'application de production.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-01-at-18.02.53.png)
_Journaux pendant la construction de l'application de production._

Pour ajouter des scripts interactifs, c'est-à-dire des scripts qui entrent dans la sortie de build `HTML` finale, ajoutez un élément `<script>` dans la section balisage du composant.

Par exemple, déplaçons le `console.log` du frontmatter vers le balisage via un élément `<script>` :

```js
// 📂 src/pages/index.astro
---
---
// ...

<script>
  console.log("Hello world!");
</script>

```

Nous devrions avoir `Hello world!` journalisé dans la console du navigateur :

![Le journal "Hello world" du navigateur.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-01-at-18.07.13@2x.png)
_Le journal "Hello world" du navigateur._

## Bascule de thème interactive

Mettons nos connaissances nouvellement acquises sur les scripts côté client à bon escient.

Créez un nouveau composant `ThemeToggler.astro` dans le répertoire `src/components`.

Ajoutez le balisage suivant :

```js
// 📂 src/components/ThemeToggler.astro
<button aria-label="Theme toggler">
  <svg width="25px" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
    <path
      class="sun"
      fill-rule="evenodd"
      d="M12 17.5a5.5 5.5 0 1 0 0-11 5.5 5.5 0 0 0 0 11zm0 1.5a7 7 0 1 0 0-14 7 7 0 0 0 0 14zm12-7a.8.8 0 0 1-.8.8h-2.4a.8.8 0 0 1 0-1.6h2.4a.8.8 0 0 1 .8.8zM4 12a.8.8 0 0 1-.8.8H.8a.8.8 0 0 1 0-1.6h2.5a.8.8 0 0 1 .8.8zm16.5-8.5a.8.8 0 0 1 0 1l-1.8 1.8a.8.8 0 0 1-1-1l1.7-1.8a.8.8 0 0 1 1 0zM6.3 17.7a.8.8 0 0 1 0 1l-1.7 1.8a.8.8 0 1 1-1-1l1.7-1.8a.8.8 0 0 1 1 0zM12 0a.8.8 0 0 1 .8.8v2.5a.8.8 0 0 1-1.6 0V.8A.8.8 0 0 1 12 0zm0 20a.8.8 0 0 1 .8.8v2.4a.8.8 0 0 1-1.6 0v-2.4a.8.8 0 0 1 .8-.8zM3.5 3.5a.8.8 0 0 1 1 0l1.8 1.8a.8.8 0 1 1-1 1L3.5 4.6a.8.8 0 0 1 0-1zm14.2 14.2a.8.8 0 0 1 1 0l1.8 1.7a.8.8 0 0 1-1 1l-1.8-1.7a.8.8 0 0 1 0-1z"
    ></path>
    <path
      class="moon"
      fill-rule="evenodd"
      d="M16.5 6A10.5 10.5 0 0 1 4.7 16.4 8.5 8.5 0 1 0 16.4 4.7l.1 1.3zm-1.7-2a9 9 0 0 1 .2 2 9 9 0 0 1-11 8.8 9.4 9.4 0 0 1-.8-.3c-.4 0-.8.3-.7.7a10 10 0 0 0 .3.8 10 10 0 0 0 9.2 6 10 10 0 0 0 4-19.2 9.7 9.7 0 0 0-.9-.3c-.3-.1-.7.3-.6.7a9 9 0 0 1 .3.8z"
    ></path>
  </svg>
</button>

```

*   Pour l'accessibilité, le bouton a un `aria-label` de `Theme toggler`.
*   Le `SVG` a une largeur fixe de `25px`, rendant deux éléments `<path>`.
*   Le premier `<path>` représente visuellement une icône de soleil. Le second est une icône de lune.
*   Par défaut, les deux icônes (soleil et lune) sont rendues. Notre objectif est de basculer l'icône affichée en fonction du thème actif.

Ensuite, importez le composant et rendez-le dans le `NavigationBar` :

```js
// 📂 src/components/NavigationBar
---
import ThemeToggler from "./ThemeToggler.astro";
---

<nav>
  <ul>
    {/** ... **/}
  </ul>
  {/** 👀 Look here **/}
  <ThemeToggler />
</nav>

```

![Les icônes soleil et lune rendues dans le bouton de bascule.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-02-at-06.43.28.png)
_Les icônes soleil et lune rendues dans le bouton de bascule._

Ajoutons un peu de `<style>` à `ThemeToggler` :

```js
// 📂 src/components/ThemeToggler.astro
// ...
<style>
  button {
    cursor: pointer;
    border-radius: 10px;
    border: 0;
    padding: 5px 10px;
    transition: all 0.2s ease-in-out;
  }

  button:hover {
    /* Make the button smaller (scale down) when hovered */
    transform: scale(0.9);
  }

  button:active {
    /** Return the button to its standard size when active */
    transform: scale(1);
  }

  .sun {
    /* Hide the sun icon by default. This assumes a light theme by default */
    fill: transparent;
  }
</style>

```

Maintenant, nous devrions avoir un bouton de bascule de thème décent.

![Un bouton de bascule de thème stylisé.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-02-at-06.50.49.png)
_Un bouton de bascule de thème stylisé._

## Le sélecteur `:global()`

Prenons un moment pour considérer la stratégie que nous utiliserons pour basculer le thème.

Nous basculerons une classe CSS sur l'élément racine chaque fois qu'un utilisateur clique sur le bouton.

![Ajouter une nouvelle classe "dark" lors de la bascule.](https://blog.ohansemmanuel.com/content/images/2023/06/embed.png)
_Ajouter une nouvelle classe "dark" lors de la bascule._

Par exemple, si l'utilisateur consultait le site en mode clair et cliquait pour basculer, nous ajouterons une classe `.dark` à l'élément racine et, sur cette base, appliquerons des styles de thème sombre.

Si l'utilisateur est en mode sombre, cliquer sur le bouton supprimera la classe `.dark`. Nous appellerons cela une stratégie de classe pour basculer le mode sombre.

Sur la base de cette stratégie, nous devons mettre à jour notre style local `ThemeToggler` pour afficher l'icône pertinente en fonction de la classe globale `.dark`.

Pour ce faire, nous exploiterons le sélecteur `:global`.

Voici comment nous y parviendrions :

```html
<!-- 📂 src/components/ThemeToggler.astro -->
<style>
 /**...**/

 /** If a parent element has a .dark class, target the .sun icon and make the path black (shows the icon) */
 :global(.dark) .sun {
   fill: black;
 }

 /** If a parent element has a .dark class, target the .moon icon and make the path transparent (hides the icon) */
 :global(.dark) .moon {
   fill: transparent;
 }
</style>

```

Pour voir cela à l'œuvre, inspectez la page via les outils de développement, et ajoutez une classe `dark` à l'élément racine. L'icône de bascule sera modifiée de manière appropriée.

![Inspecter le changement d'icône avec une classe racine dark.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-02-at-07.03.08.png)
_Inspecter le changement d'icône avec une classe racine dark._

En pratique, limitez `:global` uniquement aux cas d'utilisation appropriés, car mélanger des styles globaux et des styles de composants scopés localement deviendra difficile à déboguer. Mais cela est admissible, étant donné notre cas d'utilisation.

## Gestion des événements

Nous avons géré les styles pour notre bascule, en supposant une classe racine `.dark`. Maintenant, allons-y et gérons l'événement de clic de bascule avec un élément `<script>`.

```html
<!-- 📂 src/components/ThemeToggler.astro -->
<script>
  /** Represent the toggle theme class with a variable */
  const DARK_THEME_CLASS = "dark";

  /** Grab the toggle */
  const toggle = document.querySelector("button");
  /** Grab the document root element. In this case <html>  */
  const rootEl = document.documentElement;

  if (toggle) {
    toggle.addEventListener("click", () => {
      /** toggle the "dark" class on the root element */
      rootEl.classList.toggle(DARK_THEME_CLASS);
    });
  }
</script>

```

Remarquez que c'est du JavaScript standard. Rien d'extraordinaire ici.

*   Le bouton est sélectionné via `document.querySelector("button")`.
*   Pour configurer un écouteur d'événements, nous utilisons la méthode `.addEventListener` sur le bouton.
*   En cliquant sur le bouton, nous basculons la liste de classes sur l'élément racine : ajoutant ou supprimant la classe "dark".

Avec cela en place, l'icône de bascule change lorsqu'on clique dessus pour devenir soit celle du soleil, soit celle de la lune.

Excellent !

## Thématisation via les variables CSS

Les variables CSS sont exceptionnelles, et nous les exploiterons pour thématiser notre application.

Tout d'abord, allons-y et définissons les variables de couleur que nous utiliserons dans le projet.

```js
// 📂 styles/global.css
html {
  --background: white;
  --grey-200: #222222;
  --grey-400: #444444;
  --grey-600: #333333;
  --grey-900: #111111;
}

html.dark {
  --background: black;
  --grey-200: #eaeaea;
  --grey-400: #acacac;
  --grey-600: #ffffff;
  --grey-900: #fafafa;
}

```

*   Définissez les variables sur l'élément racine `HTML` pour qu'elles soient scopées globalement.
*   Une variable CSS est une propriété qui commence par deux tirets, `--` – par exemple `--background`.
*   Pour simplifier, nous nous en tiendrons à la palette grise minimale ci-dessus.

Le premier changement visuel que nous ferons est d'ajouter les déclarations de style `color` et `background` suivantes à l'élément `body` :

```js
// 📂 styles/global.css
body {
  color: var(--grey-600);
  background: var(--background);
}

```

Avec ce changement apparemment simple, nous devrions maintenant avoir la couleur du texte et de l'arrière-plan du `body` qui réagissent au clic sur le bouton.

![Mode sombre activé.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-02-at-07.51.51.png)
_Mode sombre activé._

Enfin, mettez à jour les liens de navigation dans `NavigationBar` pour refléter les préférences de thème :

```css
/* 📂 src/components/NavigationBar.astro */
<style>
  /* ... */
  a {
    color: var(--grey-400);
    padding: 0.5rem 1rem;
    border-radius: 10px;
    text-decoration: none;
  }

  a:hover {
    color: var(--grey-900);
  }
</style>

```

![Liens de navigation stylisés pour le mode sombre.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-02-at-07.55.56.png)
_Liens de navigation stylisés pour le mode sombre._

## Comment accéder aux objets clients globaux

Question ! 🙋🏼

Où devrions-nous accéder aux objets globaux tels que `window.localStorage` ? Dans le frontmatter d'un composant Astro ou dans un `<script>` interactif ?

À ce stade, j'espère que la réponse à la question est claire d'après les exemples précédents.

Puisque Astro s'exécute sur le serveur, tenter d'accéder à une propriété `window` dans le frontmatter d'un composant entraînera une erreur.

```css
---
{/** ❌ this will fail with the error: window is undefined **/}
 const value = window.localStorage.getItem("value")
---

```

Pour accéder aux propriétés `window`, nous avons besoin que le script s'exécute sur le client – c'est-à-dire dans le navigateur. Nous devons donc exploiter un ou plusieurs scripts côté client.

Un bon cas d'utilisation pour cela est de se souvenir du choix de thème de l'utilisateur.

Si les utilisateurs basculent leur thème de clair à sombre et rafraîchissent le navigateur, ils perdent l'état du thème sélectionné.

Que diriez-vous de sauvegarder cet état dans le stockage local du navigateur et de restaurer le thème sélectionné lors du rafraîchissement ?

Eh bien, faisons cela !

Voici les premières étapes que nous prendrons :

*   Saisir l'état actuel du thème, c'est-à-dire sombre ou clair, lorsque le bouton de thème est cliqué.
*   Sauvegarder la valeur du thème dans le stockage local du navigateur sous la forme :

```
{
  COLOUR_MODE: "LIGHT" | "DARK"
}
```

Voici cela traduit en code :

```html
<!-- 📂 src/components/ThemeToggler.astro -->
<script>
  const DARK_THEME_CLASS = "dark";
  /** Represent the local storage key by a variable */
  const COLOUR_MODE = "COLOUR_MODE";
  /** Represent the local storage values by variables */
  const LIGHT_THEME = "LIGHT";
  const DARK_THEME = "DARK";
  /** ... **/
  toggle.addEventListener("click", () => {
    /** ... */
    /**Get the current theme mode, i.e., light or dark */
    const colourMode = rootEl.classList.contains(DARK_THEME_CLASS)
      ? DARK_THEME
      : LIGHT_THEME;

    /** Save the current theme to local storage   */
    window.localStorage.setItem(COLOUR_MODE, colourMode);
  });
</script>

```

Nous avons sauvegardé le thème dans le stockage local mais nous devons maintenant définir le thème actif dès que la page est chargée et que le `script` est exécuté.

Voici le code annoté requis pour y parvenir :

```html
<!-- 📂 src/components/ThemeToggler.astro -->
<script>
  {/**... **/}
  const getInitialColourMode = () => {
    /** Get colour mode from local storage **/
    const previouslySavedColourMode = window.localStorage.getItem(COLOUR_MODE);
    if (previouslySavedColourMode) {
      return previouslySavedColourMode;
    }
    /** Does the user prefer dark mode, e.g., through an operating system or user agent setting? */
    if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
      return DARK_THEME;
    }
    /** Default to the light theme */
    return LIGHT_THEME;
  };
  /**Get initial colour mode */
  const initialColourMode = getInitialColourMode();
  const setInitialColourMode = (mode: string) => {
    if (mode === LIGHT_THEME) {
      rootEl.classList.remove(DARK_THEME_CLASS);
    } else {
      rootEl.classList.add(DARK_THEME_CLASS);
    }
  };
  /** Set the initial colour mode as soon as the script is executed */
  setInitialColourMode(initialColourMode);
{/**... **/}
</script>

```

Maintenant, essayez cela. Tout d'abord, basculez le thème et rafraîchissez pour voir le choix de thème préservé.

## La magie des scripts

Les scripts côté client ajoutés via un `<script>` peuvent sembler être votre JavaScript vanilla typique, mais ils sont plus capables de manières spécifiques.

Le point le plus crucial est qu'Astro les traite. Cela signifie qu'à l'intérieur d'un `<script>`, nous pouvons importer d'autres scripts ou importer des paquets npm, et Astro résoudra et empaquetera le script pour une utilisation dans le navigateur.

```html
<script>
 /** ✅ valid package import **/
 import { titleCase } from "title-case";

 const title = titleCase("string")

 alert(title)
</script>

```

```html
/** ✅ valid script reference **/
<script src="path-to-script.js"/>

```

Un autre point critique est que le `<script>` supporte pleinement TypeScript. Par exemple, dans notre solution, nous avons typé le paramètre pour la fonction `setInitialColourMode` :

```ts
// mode is of type string
const setInitialColourMode = (mode: string) => {
  ...
};

```

Nous n'avons pas à sacrifier la sécurité de type dans les éléments `<script>` clients et pouvons continuer à écrire du code TypeScript standard. Astro supprimera les types au moment de la construction et ne servira que le JavaScript traité au navigateur.

Voici un résumé de ce qu'Astro fait :

*   Les paquets `NPM` et les fichiers locaux peuvent être importés et seront regroupés.
*   TypeScript est entièrement pris en charge dans le `<script>`.
*   Si un seul composant `Astro` avec un `<script>` est utilisé plusieurs fois sur une page, le `<script>` est traité et inclus une seule fois.
*   Astro traitera et insérera le script dans le `<head>` de la page avec un attribut `type=module`.
*   ❗️L'implication de `type=module` est que le navigateur différera le script, c'est-à-dire le chargera en parallèle et **l'exécutera seulement après** que la page soit analysée.

## Comment exploiter les scripts en ligne

Par défaut, Astro traite les `<script>`s. Cependant, pour désactiver le traitement de script par défaut d'Astro, nous pouvons passer une directive `is:inline` comme indiqué ci-dessous :

```ts
<script is:inline>
 // Imports will not be processed
 // Typescript not supported by default
 // Script will be added as is, e.g., multiple times if the component is used more than once on a page.
</script>

```

Dans le monde réel, nous réalisons rapidement que les valeurs par défaut ne satisfont pas toujours toutes les exigences du projet.

Par exemple, considérez le flash non stylisé du thème incorrect lorsque nous rafraîchissons notre page d'accueil. Pour un utilisateur qui a choisi le thème sombre précédemment, rafraîchir la page montre le contenu rendu avec le thème clair avant de passer au sombre après que le script soit analysé.

![Transition du contenu à thème clair vu avec un throttling 3G régulier.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-03-at-03.24.42.png)
_Transition du contenu à thème clair vu avec un throttling 3G régulier._

Cela se produit parce que nous restaurons le thème choisi par l'utilisateur seulement après que le HTML de la page a été analysé, ce qui est le comportement par défaut des scripts Astro traités.

Pour éviter cela, nous utiliserons la directive `is:inline`, qui rendra le script bloquant, c'est-à-dire qu'il sera exécuté immédiatement et arrêtera l'analyse jusqu'à ce qu'il soit terminé.

Puisque les scripts avec l'attribut `is:inline` ne sont pas traités, ils seront ajoutés plusieurs fois s'ils sont utilisés dans des composants réutilisables qui apparaissent plus d'une fois sur la page.

Alors, allons-y et déplaçons le morceau de code de restauration de thème dans `Main.astro` — parce que la mise en page `Main` n'est incluse qu'une seule fois par page.

Nous nous assurerons également d'ajouter cela dans le `<head>` de la mise en page, comme indiqué ci-dessous :

```html
<!-- 📂 src/layouts/Main.astro -->
<head>
   <!-- ... -->
    <!-- 👀 add is:inline -->
    <script is:inline>
      const DARK_THEME_CLASS = "dark";
      const COLOUR_MODE = "COLOUR_MODE";
      const LIGHT_THEME = "LIGHT";
      const DARK_THEME = "DARK";
      const rootEl = document.documentElement;
      const getInitialColourMode = () => {
        /** ... */
      }
      const initialColourMode = getInitialColourMode();
      // 👀 remove string type on mode
      const setInitialColourMode = (mode) => {
         /** ... */
      };
      /** Set the initial colour mode as soon as the script is executed */
      setInitialColourMode(initialColourMode);
    </script>
  </head>

```

Nous ajoutons explicitement cela au `<head>` parce qu'Astro ne traitera pas le script `is:inline`. En tant que tel, il ne sera pas déplacé vers le `head` par Astro.

Soyez prudent avec `is:inline` car il supprime la nature non bloquante par défaut des scripts. Mais c'est idéal pour ce cas d'utilisation.

Ouvrez vos outils de développement et limitez le réseau. Ensuite, allez-y et rafraîchissez après avoir basculé le mode sombre. Nous devrions avoir éradiqué le flash de thème incorrect :

![Limitation du réseau via les outils de développement chrome.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-11-at-07.30.21@2x.png)
_Limitation du réseau via les outils de développement chrome._

## Sélecteurs globaux dans les scripts

Comprendre comment Astro traite le `<script>` dans nos composants nous aide à prendre des décisions éclairées.

Nous savons que le `<script>` sera finalement regroupé et injecté dans le `<head>` de notre page.

Mais considérez notre sélecteur pour enregistrer les clics de bascule de thème :

```ts
// 📂 src/components/ThemeToggler.astro
const toggle = document.querySelector("button");

```

Le problème avec ce code apparemment inoffensif est que `document.querySelector` renverra le premier élément qui correspond au sélecteur — un élément bouton.

Cela sera sélectionné si nous ajoutons un bouton aléatoire quelque part sur la page avant notre bouton de bascule de thème.

```js
// 📂 src/layouts/Main.astro
<button> Donate to charity </button>
<Nav />

//...

```

![Le bouton faire un don à une œuvre caritative.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-03-at-03.38.21.png)
_Le bouton faire un don à une œuvre caritative._

Ce bouton, qui n'a rien à voir avec la bascule de thème, sera désormais responsable de la bascule du thème de l'utilisateur.

Cliquer sur "faire un don à une œuvre caritative" bascule maintenant le thème. C'est inacceptable.

La leçon ici est d'être attentif à vos sélecteurs DOM et d'être spécifique lorsque c'est possible, par exemple via des identifiants ou des classes :

```js
document.querySelector("#some-unique-id")

```

Refactorisons notre solution pour utiliser un attribut de données.

```html
<!-- 📂 src/components/ThemeToggler.astro -->
<button aria-label="Theme toggler" data-theme-toggle>
  <!-- ... -->
</button>

<script>
  /** 👀 Look here */
  const toggle = document.querySelector("[data-theme-toggle]");
  // ...
</script>

```

Avec le sélecteur plus spécifique, seul un élément avec l'attribut de données `theme-toggle` sera sélectionné, laissant `<button> Donate to charity </button>` en dehors de nos affaires de bascule de thème.

## Pages Markdown

Nous avons établi que tous les types de fichiers ne sont pas des pages valides dans Astro. Nous avons vu les composants Astro comme des pages, mais permettez-moi de vous présenter les pages markdown.

Markdown est un langage de balisage populaire et facile à utiliser pour créer du texte formaté. Je suis sûr que ma grand-mère ne connaît pas le markdown, donc il est plus sûr de dire que c'est un format de texte célèbre parmi les développeurs.

Il n'est pas surprenant qu'Astro prenne en charge la création de pages via markdown. Alors, mettons cela à l'épreuve.

Nous allons créer deux nouvelles pages pour remplacer nos liens de navigation morts `Philosophies` et `Beyond technology`.

![Les liens de navigation morts.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-02-at-10.50.19@2x.png)
_Les liens de navigation morts._

Créez la première page dans `src/pages/philosophies.md` avec le contenu suivant :

```md
- Be present and enjoy the now
- Be driven by values
- Health is wealth
- Be deliberate
- Laugh out loud

```

Créez la deuxième page dans `src/pages/beyond-tech.md` avec le contenu suivant :

```md
- 5X Marathoner
- Olympic gold medalist
- Fashion model
- Michellin star restaurant owner
- Adviser to the vice president

```

Ces fichiers sont écrits en syntaxe markdown.

Comme pour les pages de composants Astro, les pages markdown sont finalement compilées en pages `HTML` standard rendues dans le navigateur. Le même routage basé sur les fichiers est également utilisé. Par exemple, pour accéder aux pages `philosophies` et `beyond-tech`, visitez respectivement les routes `/philosophies` et `/beyond-tech`.

![La page philosophies](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-03-at-02.42.23.png)
_La page philosophies_

## Comment naviguer entre les pages

Naviguer entre les pages dans Astro ne nécessite pas de baguette magique. Surprise !

Astro utilise l'élément standard `<a>` pour naviguer entre les pages. Cela a du sens car chaque page est une page `HTML` séparée.

Mettons à jour les liens de navigation pour pointer vers les nouvelles pages markdown comme indiqué ci-dessous :

```html
<!-- 📂 NavigationBar.astro -->

<li>
  <a href="/">Home</a>
</li>

<li>
  <a href="/philosophies">Philosophies</a>
</li>

<li>
  <a href="/beyond-tech">Beyond technology</a>
</li>

```

Cliquer sur l'un de ces liens devrait maintenant nous mener à leurs pages appropriées.

## Mises en page Markdown

Soyons honnêtes – nous ne gagnerons aucun prix de design pour nos pages markdown actuelles. C'est parce qu'elles semblent décalées et ne partagent pas la même mise en page que notre page existante. Pouvons-nous réparer cela ?

Vous avez probablement réalisé que je pose des questions et que je fournis ensuite des réponses. D'accord, vous m'avez eu. C'est donc mon astuce pour vous faire réfléchir à un problème — aussi bref soit-il — avant d'expliquer la solution.

Croyez-le ou non, le frontmatter des composants Astro a été inspiré par le markdown. La syntaxe markdown originale prend en charge le frontmatter pour fournir des métadonnées sur le document. Par exemple, nous pourrions ajouter une métadonnée `title` comme indiqué ci-dessous :

```ts
---
title: Understanding Astro
---

```

C'est une excellente nouvelle car Astro exploite cela pour fournir des mises en page pour les pages markdown.

Au lieu de la page _si ennuyeuse que je ne peux pas la supporter_, nous pouvons utiliser une mise en page pour apporter une structure réutilisable à toutes nos pages markdown.

Commençons.

Avec les pages markdown Astro, nous pouvons fournir des mises en page pour une page markdown en fournissant une métadonnée de frontmatter layout comme indiqué ci-dessous :

```ts
---
layout: path-to-layout
---

```

Tout d'abord, réutilisons la même mise en page `Main` en ajoutant ce qui suit aux deux pages markdown :

```ts
// add at the top of the Markdown pages.
---
layout: ../layouts/Main.astro
---

```

Les pages markdown devraient maintenant réutiliser notre mise en page existante avec la thématisation, la navigation et le pied de page tous en place.

![Utiliser la mise en page Main dans les pages markdown.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-03-at-04.40.15.png)
_Utiliser la mise en page Main dans les pages markdown._

Puisque `Main.astro` inclut nos fichiers `global.css`, allons-y et fournissons quelques styles globaux par défaut pour les paragraphes et les listes :

```css
{/** 📂 src/styles/global.css **/}
p,
li {
  font-size: 1rem;
  color: var(--gray-400);
  opacity: 0.8;
}

li {
  margin: 1rem 0;
}

```

![Les styles de liste globaux sont maintenant appliqués aux pages Markdown.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-11-at-07.51.10@2x.png)
_Les styles de liste globaux sont maintenant appliqués aux pages Markdown._

Nous devrions maintenant avoir ces styles qui prennent effet sur nos pages markdown ! La vie n'est-elle pas meilleure avec des composants de mise en page partagés ? 😉

## Comment composer des mises en page

Les mises en page sont des composants Astro, ce qui signifie que nous pouvons les composer – c'est-à-dire rendre une mise en page dans une autre.

Par exemple, créons une mise en page `Blog.astro` séparée qui compose notre mise en page de base `Main.astro`.

```js
// 📂 src/layouts/Blog.astro
---
import Main from "./Main.astro";
---

<Main>
  <slot />
</Main>

```

Composer les mises en page de cette manière signifie que nous pouvons réutiliser toutes les bonnes choses dans `Main.astro` tout en étendant `Blog.astro` pour inclure uniquement des éléments spécifiques au blog.

La séparation des préoccupations améliore considérablement la lisibilité et force chaque mise en page à avoir une seule responsabilité.

Maintenant, à ce stade, les pages markdown ont le même balisage de mise en page et les mêmes styles que `Main.astro`. Nous n'avons fait aucune personnalisation. Mais nous pouvons déjà changer les pages `beyond-tech` et `philosophies` pour utiliser la nouvelle mise en page `Blog.astro` comme indiqué ci-dessous :

```md
---
layout: ../layouts/Blog.astro
---

```

## Props de composants

Lorsque nous construisons des composants réutilisables, nous trouvons souvent des situations où nous devons personnaliser certaines valeurs au sein d'un composant. Par exemple, considérez le `<title>` dans notre composant de mise en page `Main.astro` :

```js
// 📂 src/layouts/Main.astro
<title>Astro</title>

```

Un `title` codé en dur sur chaque page où la mise en page `Main` est utilisée est ridicule.

Pour favoriser la réutilisabilité, les composants peuvent accepter des propriétés. Celles-ci sont communément appelées **props**.

Les props sont passées aux composants comme des attributs.

```js
<Main title="Some title" />

```

Les valeurs des props sont ensuite accessibles via `Astro.props`. Cela est mieux expliqué avec un exemple.

Allez-y et mettez à jour `Main` pour accepter une prop `title` comme indiqué ci-dessous :

```js
// 📂 src/layouts/Main.astro
---
// ...
const { title } = Astro.props;
---

<html lang="en">
  <head>
    {/** ... **/}
    {/** 👀 look here **/}
    <title>{title}</title>
  </head>
     {/** ... **/}
</html>

```

Pour appliquer les vérifications TypeScript, définissez l'alias de type ou l'interface `Props`.

```js
// Either of these is valid
type Props = {
  title: string
}

interface Props {
  title: string
}

```

Pour simplifier, je m'en tiendrai à un alias de type pour la mise en page `Main` :

```js
// 📂 src/layouts/Main.astro
---
type Props = {
  title: string
}

const { title } = Astro.props;
---
// ...

```

Avec le type déclaré, nous aurons des erreurs TypeScript dans les fichiers où nous avons utilisé `<Main>` sans la prop `title` requise.

![Erreur de props title invalide.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-03-at-06.01.52.png)
_Erreur de props title invalide._

Mettez à jour les pages `index.astro` et `Blog.astro` pour passer une prop `title` à `Main` :

```js
// 📂 src/layouts/index.astro
<Main title="Frau Katarina">
{/* ... */}

```

```js
// 📂 src/layouts/Blog.astro
<Main title="Frau Katarina | Blog">
{/* ... */}

```

## Comment exploiter les propriétés de frontmatter Markdown

Toutes les pages markdown de notre application auront un titre, un sous-titre et une affiche. Heureusement, un excellent moyen de les représenter est via les propriétés de frontmatter.

Mettez à jour les pages markdown pour inclure maintenant ces propriétés, comme indiqué ci-dessous.

`📂 src/pages/beyond-tech.md`:

```md
---
layout: ../layouts/Blog.astro
poster: "/images/road-trip.jpg"
title: "Beyond Technology"
subtitle: "Humans are multi-faceted. Beyond tech, I indulge in the following:"
---
...

```

`📂 src/pages/philosophies.md`:

```md
---
layout: ../layouts/Blog.astro
poster: "/images/philosophies.jpg"
title: "My Guiding Philosophies"
subtitle: "These are the philosophies that guide every decision and action I make."
---
...

```

Notez que `poster` pointe vers des chemins d'image. Ces chemins référencent le répertoire `public`. Donc `/images/philosophies.jpg` pointe vers une image dans `public/images/philosophies.jpg`.

Si vous codez en même temps, n'hésitez pas à télécharger n'importe quelle image depuis Unsplash et à les déplacer vers le répertoire `public`.

Ajouter des métadonnées à nos pages markdown ne nous sert à rien si nous ne pouvons pas les utiliser.

Heureusement, les mises en page markdown ont un super pouvoir unique — elles peuvent accéder au frontmatter markdown via `Astro.props.frontmatter`.

Allons-y et gérons cela globalement dans notre composant de mise en page `Blog.astro`. Voici la section script de composant :

```ts
// 📂 src/layouts/Blog.astro
---
// import the type utility for the markdown layout props
import type { MarkdownLayoutProps } from "astro";
// import the base layout: Main.astro
import Main from "./Main.astro";

// defined the Props type
type Props = MarkdownLayoutProps<{
  // Define the expected frontmatter props here
  title: string;
  poster: string;
  subtitle: string;
}>;

// get properties from the markdown frontmatter
const { poster, title, subtitle } = Astro.props.frontmatter;
---

```

*   Le type utilitaire `MarkdownLayoutProps` accepte un générique et renvoie le type pour toutes les propriétés disponibles pour une mise en page markdown. N'hésitez donc pas à inspecter la forme entière.
*   `MarkdownLayoutProps` accepte notre définition de type de propriété frontmatter comme générique, c'est-à-dire `title`, `poster` et `subtitle`. Ce sont des propriétés que nous avons ajoutées dans le frontmatter de nos pages Markdown.
*   `type Props = ...` ou `interface Props {}` est la façon dont nous fournissons des types pour un composant Astro.
*   La ligne finale déconstruit les propriétés de `Astro.props.frontmatter` avec un support TypeScript complet.

![Support Typescript dans la mise en page Markdown.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-03-at-05.16.20.png)
_Support Typescript dans la mise en page Markdown._

Mettez également à jour le balisage de la mise en page pour rendre l'image, le titre et le sous-titre :

```html
<!-- 📂 src/layouts/Blog.astro -->
<Main>
  <figure class="figure">
    <img
      src={poster}
      alt=""
      width="100%"
      height="480px"
      class="figure__image"
    />
    <figcaption class="figure__caption">
      Poster image for {title.toLowerCase()}
    </figcaption>
  </figure>

  <h1>{title}</h1>
  <h2>{subtitle}</h2>

  <slot />
</Main>

<style>
  h1 + h2 {
    margin-bottom: 3rem;
  }

  .figure {
    margin: 0;
  }

  .figure__image {
    max-width: 100%;
    border-radius: 10px;
  }

  .figure__caption {
    font-size: 0.9rem;
  }
</style>

```

La plupart du balisage est sans doute standard. Cependant, notez l'appel `title.toLowerCase()` pour la légende de l'image de l'affiche. Cela est possible car toute expression JavaScript valide peut être évaluée entre accolades `{ }` dans le balisage du composant.

Nos pages markdown auront désormais des titres, des sous-titres et des images d'affiche stylisés. Avec tout cela géré en un seul endroit — la mise en page markdown.

![La page Markdown entièrement formée.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-03-at-05.19.26.png)
_La page Markdown entièrement formée._

## État de navigation interactif

Maintenant que nous sommes des pros de la gestion des scripts interactifs dans Astro, allons-y et assurons-nous de styliser nos liens de navigation actifs différemment.

Comme pour tout ce qui concerne la programmation, il existe différentes façons d'y parvenir, mais nous allons scripter cela.

```html
<!-- 📂 src/components/NavigationBar.astro -->
<script>
  const { pathname } = window.location;
  const activeNavigationElement = document.querySelector(
    `nav a[href="${pathname}"]`
  );

  if (activeNavigationElement) {
    activeNavigationElement.classList.add("active");
  }
</script>

```

*   Obtenez le `pathname` de l'objet `location`. Ce sera sous la forme `"/beyond-tech"`, `"/philosophies` ou `"/"`.
*   Puisque le `pathname` correspond au `href` sur la balise d'ancrage, nous pouvons sélectionner la balise d'ancrage active via : `document.querySelector(`nav a[href="${pathname}"]`).`
*   Enfin, nous ajoutons la classe `active` à la balise d'ancrage active.

Enfin, ajoutez le style pertinent pour la balise active :

```css
/* 📂 src/components/NavigationBar.astro */
<style>
  /* ... */
 a.active {
  background: var(--grey-900);
  color: var(--background);
 }
</style>

```

Violà ! Nous devrions maintenant avoir la balise d'ancrage active stylisée différemment.

![Styles de balise d'ancrage active.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-03-at-09.44.02.png)
_Styles de balise d'ancrage active._

## Composition de composants

Notre premier regard sur la composition de composants était avec les mises en page `Main` et `Blog`. Allons plus loin.

Notre objectif est de créer un ensemble de cartes différentes mais identiques. Chaque carte agit comme un lien vers un blog et aura un titre et un dégradé d'arrière-plan.

![La mise en page de carte éventuelle que nous construirons.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-04-at-09.44.58.png)
_La mise en page de carte éventuelle que nous construirons._

Pour y parvenir, nous aurons un composant `Cards.astro` qui rend plusieurs composants `Card.astro`.

![La composition de carte visualisée.](https://blog.ohansemmanuel.com/content/images/2023/06/b.png)
_La composition de carte visualisée._

Commençons par créer `Card.astro`.

Définissez les props de composant pertinentes et le balisage pertinent comme indiqué ci-dessous :

```js
// 📂 src/components/Card.astro
---
{/** Export the Props type alias **/}
export type Props = {
  to: string;
  title: string;
  gradientFrom: string;
  gradientTo: string;
};

// Get component props from Astro.props
const { title, to } = Astro.props;
---

```

```html
<a href={to} class="card">
  <div class="card__inner">
    <div class="card__title">{title}</div>
    <!-- Render the arrow via HTML entity name: → = &rarr;-->
    <div class="card__footer">&rarr;</div>
  </div>
</a>

<style>
  .card {
   /** local CSS variable reused below */
    --radius: 10px;

    padding: 4px;
    border-radius: var(--radius);
    text-decoration: none;
    transition: all 0.2s ease-in-out;
  }

  .card:hover {
    transform: scale(0.95);
  }

  .card__inner {
    background: var(--background);
    padding: 1.5rem;
    border-radius: var(--radius);
    display: flex;
    flex-direction: column;
  }

  .card__title {
    font-size: 1.2rem;
    color: var(--grey-900);
    font-weight: 500;
    line-height: 1.75rem;
  }

  .card__footer {
    padding-top: 2rem;
    font-size: 1.2rem;
	color: var(--grey-900);
    margin: auto 0 0 auto;
  }
</style>

```

Maintenant, allez-y et créez le composant `Cards.astro` comme suit :

```js
// 📂 src/components/Cards.astro
---
// Import the Card component
import Card from "./Card.astro";
// Import the Card Props type
import type { Props as CardProp } from "./Card.astro";

// Define the Props for this component
type Props = {
  cards: CardProp[]; // accepts an array of CardProps
};

// Retrieve the cards prop
const { cards } = Astro.props;
---

```

```html
<div class="cards">
  <!-- Dynamically render multiple Card components and spread the required card props -->
   {cards.map((card) => <Card {...card} />)}
</div>

<style>
  .cards {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  /* Since this is standard CSS, we can have media queries here */
  @media screen and (min-width: 768px) {
    .cards {
      flex-direction: row;
    }
  }
</style>

```

Pour voir les fruits de notre travail, nous devons maintenant importer et rendre `Cards` dans le composant de page `index.astro`.

```js
// 📂 src/pages/index.astro
---
// ...
import Cards from "../components/Cards.astro";
---
<Main>
  <div class="profile">
   {/** ... **/}
  </div>
  {/** 👀 look here **/}
  <Cards
    cards={[
      {
        title: "Here are my guiding philosophies for life",
        gradientFrom: "#818cf8",
        gradientTo: "#d8b4fe",
        to: "/philosophies",
      },
      {
        title: "A summary of my work history",
        gradientFrom: "#fde68a",
        gradientTo: "#fca5a5",
        to: "/work-summary",
      },
      {
        title: "What I do beyond technology",
        gradientFrom: "#6ee7b7",
        gradientTo: "#9333ea",
        to: "/beyond-tech",
      },
    ]}
  />
</Main>

```

![Les cartes rendues.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-04-at-10.18.23.png)
_Les cartes rendues._

Cliquer sur l'un des liens pointera vers la page de blog respective.

N'oublions pas d'ajouter la nouvelle page `work-summary.md` :

```js
// 📂 src/pages/work-summary.md
---
layout: ../layouts/Blog.astro
poster: "/images/work-summary.jpg"
title: "Work summary"
subtitle: "A summary of my work:"
---

- VP Engineering at Google
- VP Engineering at Facebook
- VP Engineering at Tesla
- VP Engineering at Amazon
- VP Engineering at Netflix

```

Et voilà !

## Le flux de données du template

Comme nous en avons discuté, les données dans le frontmatter s'exécutent sur le serveur et ne sont pas disponibles dans le navigateur.

Au fur et à mesure que nous avons construit notre application, nous avons fréquemment exploité les données du frontmatter dans la section template, comme indiqué ci-dessous :

```js
---
 const data = "Understanding Astro"
---

//Use data in the template
<h1>{data}</h1>

```

C'est facile à comprendre pour notre site web statique. Nous savons que cela sera finalement compilé en HTML.

Mais considérez un balisage plus robuste qui inclut des éléments `<style>` et `<script>`. Comment référençons-nous les données du frontmatter dans ces sections de balisage ?

```js
---
 const data = "Understanding Astro"
---

// ✅ Use data in the template
<h1>{data}</h1>

// styles
<style>
 {/** ❌referencing data here will fail */}
</style>

// scripts
<script>
{/** ❌referencing data here will fail */}
 console.log(data)
</script>

```

Une réponse est via la directive de template `define:vars`.

`define:vars` passera nos variables du frontmatter dans le `<script>` ou `<style>` client. Il est important de noter que seules les valeurs sérialisables JSON fonctionnent ici.

Essayons cela.

Nous devons référencer les variables `gradientFrom` et `gradientTo` passées comme props dans notre `<style>`.

Tout d'abord, pour rendre les variables disponibles dans `<style>`, nous allons utiliser `define:vars` comme suit :

```js
// 📂 src/components/Card.astro
---
const { title, to, gradientFrom, gradientTo } = Astro.props;
// ...
---

<style define:vars={{gradientFrom, gradientTo }}>
  {/** ... **/}
</style>

```

`define:vars` accepte un objet de variables que nous voulons rendre disponibles dans `<style>`.

Les variables sont définies mais pas encore utilisées.

Maintenant, nous pouvons référencer les variables via des propriétés personnalisées (alias variables css) comme indiqué ci-dessous :

```css
/** 📂 src/components/Card.astro **/
<style define:vars={{gradientFrom, gradientTo }}>
  /** 👀 look here **/
  .card {
    background-image: linear-gradient(
      to right,
      var(--gradientFrom),
      var(--gradientTo)
    );
  }
 /** ... **/
</style>

```

Et voilà !

Nos cartes sont maintenant plus belles que jamais.

![Appliquer des dégradés dynamiques aux cartes.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-04-at-10.45.36.png)
_Appliquer des dégradés dynamiques aux cartes._

## Le côté obscur de `define:vars`

Nous avons vu que `define:vars` est pratique pour utiliser des variables du frontmatter d'un composant Astro. Mais soyez prudent lorsque vous utilisez `define:vars` avec des scripts.

Utiliser `define:vars` avec un `<script>` est similaire à l'utilisation de la directive `is:inline`.

Astro ne regroupera pas le script et il sera ajouté plusieurs fois si le même composant est rendu plus d'une fois sur une page.

Voici un exemple pour clarifier cela.

Dans `Card.astro`, allez-y et ajoutez un `<script>` avec la directive `define:vars` comme suit :

```js
/** 📂 src/components/Card.astro **/
<script define:vars={{ gradientFrom }}>
  console.log(gradientFrom);
</script>

```

Inspectez les éléments via les outils de développement. Vous remarquerez que le `<script>` est intégré et non traité, c'est-à-dire tel que nous l'avons écrit, à part être enveloppé dans une exécution de fonction immédiatement invoquée (IIFE).

![Les scripts intégrés.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-04-at-12.07.32.png)
_Les scripts intégrés._

Le script est également ajouté trois fois — avec une valeur différente de `gradientFrom` pour chaque carte rendue.

Avec les scripts, une meilleure solution (sauf si le comportement en ligne est idéal pour votre cas d'utilisation) est de passer les données du frontmatter du composant à l'élément rendu via des attributs `data-` et d'y accéder ensuite via JavaScript.

Par exemple, nous pouvons réécrire la solution précédente comme indiqué ci-dessous :

```html
---

---
<a href={to} class="card" data-gradientfrom={gradientFrom}>
 ...
</a>
...
<script>
  const card = document.querySelector(".card");

  // narrow the type of card to HTMLElement to access ".dataset"
  if (card instanceof HTMLElement) {
    // access data in dataset.gradientfrom
    console.log(card.dataset.gradientfrom);
  }
</script>

```

Notez que ceci est un exemple artificiel et ne récupère que le premier élément de carte avec ses données `gradientfrom` associées. Néanmoins, cela démontre comment prévenir les comportements indésirables avec `define:vars` dans les `<script>`s.

## Comment charger plusieurs fichiers locaux

Allons-y et créons un nouveau répertoire `blog` pour contenir quelques pages markdown supplémentaires. Les pages et leur contenu sont indiqués ci-dessous :

`📂 pages/blogs/rust-javascript-tooling.md` :

```md
---
layout: "../../layouts/Blog.astro"
poster: "/images/adventure.jpg"
title: "Why Rust is the Future of Javascript Tooling"
subtitle: "How to create fast, speedy developer experiences."
---

- Rust is fast
- Yes, it is fast
- Touted as the new C++
- Did I mention it's pretty fast?

```

`📂 pages/blogs/sleep-more.md` :

```md
---
layout: "../../layouts/Blog.astro"
poster: "/images/sleeping-cat.jpg"
title: "Why you should sleep more"
subtitle: "Sleep is great for you. Here's why:"
---

- Sleep
- Sleep more
- Sleep a little more

```

`📂 pages/blogs/typescript-new-javascript.md` :

```md
---
layout: "../../layouts/Blog.astro"
poster: "/images/coding.jpg"
title: "Typescript is the new Javascript"
subtitle: "Typescript is becoming a standard for web development these days:"
---

- Type safety
- Type safety!
- Even more type safety!

```

Nous visons à lister ces titres de blog sur notre page d'accueil. Une façon de faire serait de rendre tous les éléments de lien dans `index.astro` manuellement :

```html
<!-- 📂 src/pages/index.astro -->
...
<Main>
 ...
 <div class="featured-blogs">
    <h3 class="featured-blogs__title">Featured Blogs</h3>
    <p class="featured-blogs__description">
      Opinion pieces that will change everything you know about web development.
    </p>
 </div>

 <ol class="blogs">
    <li class="blogs__list">
      <a href="blogs/typescript-new-javascript" class="blog__link"
        >Typescript is the new Javascript</a
      >
    </li>

    <li class="blogs__list">
      <a href="/blogs/rust-javascript-tooling" class="blog__link"
        >Why Rust is the future of Javascript tooling</a
      >
    </li>

    <li class="blogs__list">
      <a href="/blogs/sleep-more" class="blog__link"
        >Why you should sleep more</a
      >
    </li>
 </ol>
</Main>

```

Ensuite, mettez à jour nos styles de composants :

```html
<!-- 📂 src/pages/index.astro -->
...
<style>
  ...
  .featured-blogs {
    margin: 0;
    padding: 3rem 0 0 0;
  }
  .featured-blogs__title {
    font-size: 2rem;
    color: var(--gray-900);
  }

  .featured-blogs__description {
    margin-top: -1.2rem;
  }

  .blogs {
    font-size: 1rem;
    font-weight: 500;
  }

  .blogs__list {
    border-bottom: 1px solid;
    border-color: var(--gray-200);
  }

  .blog__link {
    opacity: 1;
    height: 100%;
    display: block;
    padding: 1rem 0;
    color: var(--gray-200);
    text-decoration: none;
    transition: opacity 0.2s ease-in-out;
  }

  .blog__link:hover {
    opacity: 0.7;
  }
</style>

```

Ce n'est pas nécessairement une mauvaise approche pour y parvenir. Nous aurons maintenant une liste des blogs, comme prévu.

![La liste de blogs rendue.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-11-at-12.52.18@2x.png)
_La liste de blogs rendue._

Une meilleure solution est d'utiliser `Astro.glob()` pour charger plusieurs fichiers.

`Astro.glob()` accepte un seul paramètre glob `URL` des fichiers que nous aimerions importer. `glob()` renverra alors un tableau des exportations du fichier correspondant.

Parler ne coûte rien, alors mettons cela en action.

Au lieu d'écrire manuellement la liste des articles de blog, nous utiliserons `Astro.glob()` pour récupérer tous les articles de blog :

```js
// 📂 src/pages/index.astro
---
const blogs = await Astro.glob<{
  poster: string;
  title: string;
  subtitle: string;
}>("../pages/blogs/*.md");
...
---
...

```

*   Notez l'argument passé à `.glob`, c'est-à-dire `../pages/blogs/*.md`. Ce chemin glob relatif représente tous les fichiers markdown dans le répertoire `/blogs`.
*   Notez également le typage fourni. `.glob` implémente un générique, qui, dans ce cas, représente le type d'objet frontmatter markdown.

```js
{
    poster: string;
    title: string;
    subtitle: string;
}
```

Maintenant, nous pouvons remplacer la liste manuelle par une liste rendue dynamiquement, comme indiqué ci-dessous :

```js
// 📂 src/pages/index.astro
...
  <ol>
    {
      blogs.map((blog) => (
        <li class="blogs__list">
          <a href={blog.url} class="blog__link">
            {blog.frontmatter.title}
          </a>
        </li>
      ))
    }
  </ol>

```

*   Rendre dynamiquement la liste de blogs en utilisant la fonction de tableau `.map`.
*   `Astro.glob()` renvoie des propriétés markdown, y compris le frontmatter et `url` où `blog.url` fait référence au chemin url du navigateur pour le fichier markdown.

Et voilà ! Même résultat avec une implémentation beaucoup plus propre.

## Comment déployer un site Astro statique

Nous avons parcouru un long chemin ! Maintenant, déployons ce bébé dans la nature.

Déployer un site web statique est relativement la même chose quelle que soit la technologie utilisée pour créer le site.

À la fin de votre build de déploiement, nous aurons des actifs statiques à déployer sur n'importe quel service de notre choix.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/generate-prod-build-1.png)
_Générer des builds de production._

Une fois cela fait, nous devons connecter un serveur web statique pour servir ce contenu lorsque vos utilisateurs visitent le site déployé.

NB : un serveur web statique est un serveur web qui sert du contenu statique. Il sert essentiellement tous les fichiers (par exemple, HTML, CSS, JS) que le client demande.

Cela décompose le processus de déploiement d'un site web statique en deux parties :

1.  Créer les actifs de production statiques
2.  Servir les actifs statiques via un serveur web statique

Passons en revue ces étapes.

### 1. Créer des actifs de production statiques

Pour construire notre application pour la production, exécutez la commande :

```bash
npm run build

```

Cela exécutera en interne la commande `astro build` et construira les actifs statiques de production de notre application.

Par défaut, ces actifs existeront dans le dossier `dist`.

### 2. Servir les actifs statiques via un serveur web statique

Le choix d'un serveur web dépendra de votre choix. Je vais expliquer comment utiliser Netlify. Mais les étapes que vous suivrez avec votre fournisseur de serveur web seront similaires.

Allez sur Netlify et créez un compte.

![La page d'accueil de Netlify.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-01-25-at-04.51.46@2x.png)
_La page d'accueil de Netlify._

Une fois que vous avez créé un compte et que vous vous êtes connecté, vous trouverez une section manuelle pour déployer un site.

![Le tableau de bord Netlify.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-01-25-at-04.56.37@2x.png)
_Le tableau de bord Netlify._

Maintenant, cliquez sur `browse to upload` et téléchargez le dossier `dist` contenant nos actifs de production statiques.

Une fois le téléchargement terminé, vous aurez votre site déployé avec une URL publique aléatoire, comme indiqué ci-dessous :

![URL du site Netlify déployé.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-01-25-at-04.57.57@2x.png)
_URL du site Netlify déployé._

Visitez l'URL pour voir votre site web nouvellement déployé !

## Le problème avec les déploiements manuels

Les déploiements manuels sont excellents pour décomposer conceptuellement le processus de déploiement d'un site web statique.

Mais dans le monde réel, vous trouverez cela moins optimal.

Le principal défi ici est que chaque changement apporté à votre site web vous oblige à construire l'application et à la re-télécharger manuellement sur votre serveur.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/manual-redeployment.png)
_Redéploiement manuel après de nouveaux changements._

C'est un problème bien connu avec une solution standardisée. La solution consiste à automatiser l'ensemble du processus de déploiement de sites web statiques en connectant votre site web à un fournisseur Git.

## Comment automatiser le déploiement d'un site web statique

Automatiser le déploiement d'un site web statique ressemble à ceci :

**Étape 1** : Écrivez et poussez votre code vers un fournisseur Git comme GitHub.

**Étape 2** : Connectez le projet GitHub à votre fournisseur de serveur web statique, par exemple Netlify.

**Étape 3** : Vous fournissez la commande `build` de votre site web et l'emplacement des actifs construits à votre fournisseur de serveur web, par exemple Netlify.

**Étape 4** : Votre fournisseur de serveur web exécute automatiquement la commande de build et sert vos actifs statiques.

**Étape 5** : Chaque fois que vous apportez des modifications au projet GitHub, votre fournisseur de serveur web récupère les modifications et réexécute l'étape 4, c'est-à-dire déploie automatiquement les modifications de votre site web.

Pour voir ce processus en pratique avec Netlify, allez [sur votre tableau de bord](https://app.netlify.com/start) et connectez un fournisseur Git (étape 1).

![Netlify : connecter un fournisseur Git.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-01-25-at-05.46.08@2x.png)
_Netlify : connecter un fournisseur Git._

Je vais sélectionner GitHub, autoriser Netlify et sélectionner le projet GitHub (étape 2).

![Netlify : sélectionner le projet Github.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-01-25-at-05.47.23@2x.png)
_Netlify : sélectionner le projet Github._

Une fois cela sélectionné, fournissez les paramètres pour le déploiement de votre application (Étape 3). Par défaut, Netlify suggérera le `build` et le `publish directory`. Vérifiez-les pour vous assurer qu'il n'y a pas d'erreurs.

![Netlify : commande de build suggérée et répertoire de publication.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-01-25-at-05.49.46@2x.png)
_Netlify : commande de build suggérée et répertoire de publication._

Appuyez sur déployer, et votre site sera en ligne en quelques secondes (étape 4).

Pour voir le redéploiement après un nouveau changement, poussez un nouveau changement vers le dépôt git connecté.

## À quelle vitesse est notre site web Astro ?

Astro se vante de sites web incroyablement rapides par rapport à des frameworks comme React ou Vue.

Mettons cela à l'épreuve en suivant les étapes ci-dessous :

*   Visitez le site web nouvellement déployé sur Chrome.
*   Ouvrez les outils de développement Chrome.
*   Allez à l'onglet Lighthouse.
*   Analysez le chargement de la page.

![Analyser le chargement de la page via lighthouse.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-11-at-13.42.45@2x.png)
_Analyser le chargement de la page via lighthouse._

Voici mon résultat en exécutant le test :

![Scores Lighthouse 100%.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-11-at-13.44.24@2x.png)
_Scores Lighthouse 100%._

Si c'était un examen scolaire, nous aurions juste obtenu un A+ en performance sans essayer.

C'est un site web rapide !

N'hésitez pas à exécuter le test sur d'autres pages.

## Conclusion de ce chapitre

Cela a été une longue introduction à Astro ! Nous avons plongé dans la construction d'un projet et appris une poignée de capacités d'Astro, de l'installation à la structure du projet en passant par les nuances des scripts en ligne et, finalement, le déploiement du projet.

Pourquoi s'arrêter ici ? Nous n'avons fait qu'effleurer la surface.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-134.png)
_Chapitre deux._

# Chapitre 2 : Les composants Astro en profondeur

Dans cette section, vous irez au-delà des bases et maîtriserez l'entité essentielle d'Astro.

## Ce que vous apprendrez

*   Ce que signifie zéro JavaScript en termes pratiques.
*   Pourquoi nous devrions envisager d'abandonner la surcharge d'exécution JavaScript.
*   Comprendre vraiment ce qu'est un composant Astro.
*   Comprendre le comportement du balisage des composants Astro, des styles et des scripts.
*   Apprendre la puissante syntaxe de template Astro et comment elle diffère de `JSX`.

## Introduction

Considérez le principe de Pareto :

> Le principe de Pareto, également connu sous le nom de règle des 80/20, stipule que 20 % des intrants peuvent avoir un impact significatif sur 80 % des résultats dans une situation ou un système particulier.

![Le principe de Pareto illustré](https://blog.ohansemmanuel.com/content/images/2023/06/pareto.png)
_Le principe de Pareto illustré_

Maintenant, faites attention car c'est là que les choses deviennent épicées. Lorsqu'il s'agit de travailler avec des composants Astro, j'ai le soupçon sournois que ces 20 % magiques génèrent une productivité énorme de 80 %.

Alors, craquons et maîtrisons ces composants Astro, voulez-vous ?

## La colonne vertébrale d'Astro

Au moment de la rédaction, considérez la définition des composants Astro de la documentation officielle :

> Les composants Astro sont les blocs de construction de base de tout projet Astro. Ce sont des composants de templating HTML uniquement sans exécution côté client.

La première partie de la phrase est claire comme de l'eau de roche : _Les composants Astro sont les blocs de construction de base de tout projet Astro._

![Comme un jeu amusant de Tetris, les composants Astro sont la façon dont nous construisons des applications Astro.](https://blog.ohansemmanuel.com/content/images/2023/06/building-blocks.png)
_Comme un jeu amusant de Tetris, les composants Astro sont la façon dont nous construisons des applications Astro._

La deuxième partie de la phrase laisse place à l'interprétation ou à l'ambiguïté : _ce sont des composants de templating HTML uniquement sans exécution côté client._

Mais dans cette phrase réside le cœur des composants Astro.

Explorons cela en termes pratiques.

### La fatigue de l'exécution JavaScript

Pour vraiment apprécier les composants Astro, nous devons nous tourner vers nos composants de framework d'interface utilisateur "standard", par exemple ceux fournis par `React` ou `Vue`.

Votre niveau de familiarité avec ces frameworks n'a pas d'importance. J'expliquerai les étapes suivantes aussi clairement que possible. Alors faites-moi confiance et suivez.

Tout d'abord, créez un nouveau projet React appelé `test-react-app` avec la commande terminal suivante :

```bash
npx create-react-app test-react-app

```

Cela utilise l'utilitaire [create-react-app](https://create-react-app.dev/).

![Créer un nouveau projet React depuis le terminal.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-28-at-12.28.51@2x.png)
_Créer un nouveau projet React depuis le terminal._

Cela créera une nouvelle application React dans le répertoire `test-react-app`.

Maintenant, changez le répertoire actuel, installez les dépendances et démarrez l'application React avec la commande suivante :

```bash
cd test-react-app && npm install && npm run start

```

![Démarrer l'application de test React.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-28-at-12.30.17@2x.png)
_Démarrer l'application de test React._

Cela démarrera une application React triviale sur `http://localhost:3000/` ou tout autre port local disponible.

![L'application de test React fonctionnant dans le navigateur.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-28-at-12.31.38@2x.png)
_L'application de test React fonctionnant dans le navigateur._

Ceci est une application React artificielle. Elle rend des paragraphes de texte, et le logo React, et l'application n'a pas de changements d'état UI significatifs ou de logique complexe.

Maintenant, regroupons cette application pour la production.

Arrêtez le serveur local en cours d'exécution et construisez l'application avec la commande suivante :

```js
npm run build

```

![Construire l'application de test React pour la production.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-28-at-12.34.26@2x.png)
_Construire l'application de test React pour la production._

Jetons un coup d'œil à la sortie de build.

Ouvrez le répertoire `test-react-app` dans votre éditeur de code de choix et observez le fichier `build/index.html`. Ce fichier racine sera servi au navigateur lorsque l'application React sera visitée.

Déballez le fichier minifié :

```html
<!-- 📂 build/index.html -->

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="/favicon.ico" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="Web site created using create-react-app"
    />
    <link rel="apple-touch-icon" href="/logo192.png" />
    <link rel="manifest" href="/manifest.json" />
    <title>React App</title>
    <script defer="defer" src="/static/js/main.3b5961bb.js"></script>
    <link href="/static/css/main.073c9b0a.css" rel="stylesheet" />
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>

```

Ceci est un fichier HTML standard. Mais ce qui est à noter dans son contenu est ce qui suit :

```html
<!-- 📂 build/index.html -->
...
<script defer="defer" src="/static/js/main.3b5961bb.js"></script>
<link href="/static/css/main.073c9b0a.css" rel="stylesheet" />
...

<div id="root"></div>
...

```

Le document rend un nœud `<div id="root"></div>`, et les actifs `JS` et `CSS` regroupés sont liés dans le `<head>`.

Voyez-vous l'attribut `defer` sur le `<script>` ?

Avec l'attribut `defer`, le script sera téléchargé en parallèle pendant que la page est analysée et sera exécuté après que la page soit analysée.

Par implication, cette page rend un `<div>` vide au début jusqu'à ce que le JavaScript soit analysé.

Eh bien, ne paniquons pas. Explorons plutôt le JavaScript référencé ici. Tout d'abord, regardez l'actif JavaScript regroupé dans `build/static/js/main...js`.

Si nous déballons le fichier minifié, nous devrions avoir un fichier qui est un peu court de `9500` lignes de JavaScript !

![Déballer l'actif Javascript minifié pour l'application React triviale.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-28-at-12.46.05@2x.png)
_Déballer l'actif Javascript minifié pour l'application React triviale._

Attendez… quoi ?! Pour une application aussi triviale ?! 😱

Oh oui.

J'ai envisagé d'ajouter un mème drôle ici, mais ne nous éloignons pas de l'importance du point.

Expliquer ce qui se passe dans ces `9000+` lignes de JavaScript dépasse le cadre de ce livre. Mais ce que nous avons dans le fichier est une fonction immédiatement invoquée (IIFE) avec tout son contenu exécuté.

```js
// 📂 build/static/js/main...js
!(function () {
  // ... lines of code go here
})();

```

Nous n'avons certainement pas écrit les `9000+` lignes de code dans le bundle `main`. Non ! La plupart de cela est le runtime React nécessaire pour faire fonctionner notre application React de la manière dont React est construit : état, props, hooks, DOM virtuel, et toutes les belles abstractions que React fournit.

### Abandonner le runtime

Contrairement à la plupart des frameworks JavaScript, Astro préconise zéro JavaScript par défaut. Cela signifie pas de surcharge d'exécution JavaScript, comme dans l'application React précédente.

J'ai donc fait ce que tout enquêteur compétent ferait — reconstitué la scène du crime.

Pour ce faire, j'ai construit la même application de démarrage React en utilisant Astro.

Utilisez la commande suivante pour créer le projet :

```js
npm create astro@latest -- --template ohansemmanuel/astrojs-ditch-the-runtime-react --yes

```

Nous utilisons la même commande `create astro` pour créer un nouveau projet. La différence ici est l'argument `--template` qui pointe vers `ohansemmanuel/astrojs-ditch-the-runtime-react` et l'argument `--yes` pour sauter toutes les invites et accepter les valeurs par défaut.

![Créer un nouveau projet Astro avec un modèle.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-09-at-07.40.44.png)
_Créer un nouveau projet Astro avec un modèle._

Choisissez le répertoire du projet, puis démarrez l'application via :

```js
npm run start

```

![Le nouveau projet Astro fonctionnant sur localhost](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-01-14-at-09.31.23@2x.png)
_Le nouveau projet Astro fonctionnant sur localhost_

Notez que l'application est similaire à l'application de démarrage React que nous avons explorée plus tôt.

Maintenant, allons-y et construisons cette application pour la production avec la commande suivante :

```js
npm run build

```

Cela construira l'application Astro et générera des fichiers statiques dans le répertoire `dist/`.

Explorez la sortie de build et trouvez les principaux fichiers `HTML`, `CSS` et image dans `dist/assets`.

![La sortie de build du projet Astro.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-28-at-13.04.29@2x.png)
_La sortie de build du projet Astro._

Regardez attentivement, et vous réaliserez qu'il n'y a pas de sortie de build JavaScript ! Au lieu de cela, nous avons le fichier `index.html`, le `CSS` associé et les actifs image.

Pour le même résultat, nous avons éliminé les 9000+ lignes de JavaScript que l'exemple React nécessitait.

C'est exactement ce que l'on entend par **zéro JavaScript par défaut.** C'est la prémisse d'Astro.

Je ne préconise pas que vous n'utilisiez pas React ou votre framework préféré. Mais cet exemple vous aide à comprendre la prémisse d'Astro, c'est-à-dire éliminer le besoin d'avoir une telle exécution côté client **si vous n'en avez pas besoin.**

La vérité passionnante est que nous n'avons pas besoin de la surcharge d'exécution JavaScript pour de nombreuses applications, telles que les sites web axés sur le contenu. Vous pouvez donc l'abandonner en faveur d'Astro.

## Qu'est-ce qu'un composant Astro ?

Avant de définir les composants Astro, considérons une question plus générique. En termes simples, qu'est-ce qu'un site web ?

Ma réponse simple serait : un site web est un ensemble de pages `HTML` liées sous un seul domaine.

![Un site web multi-pages](https://blog.ohansemmanuel.com/content/images/2023/06/2.png)
_Un site web multi-pages_

Maintenant, avec une application à page unique (SPA), ma définition devrait être mise à jour. C'est parce qu'un site web à page unique consiste maintenant en une seule page `HTML` avec un routage géré via JavaScript côté client.

Quel que soit le type de site web, il y a un dénominateur commun : le navigateur rend une ou plusieurs pages `HTML`.

Nous commencerons donc notre discussion en explorant la page `HTML` de base ci-dessous :

```js
<!DOCTYPE html>
<html lang="en-GB">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width" />
    <title>HTML 101</title>

    <style>
      p {
        color: red;
      }
    </style>

    <script>
      console.log('Hello world');
    </script>
  </head>
  <body>
    <p>Hello World</p>
  </body>
</html>

```

Nous ne gagnerons aucun prix de design avec cette page, mais elle suffit pour nos besoins d'apprentissage.

Dans le `HTML` ci-dessus, remarquez comment nous avons produit un paragraphe avec le texte `Hello world`, l'avons stylisé avec du `CSS` et avons journalisé un message dans la console en utilisant `JavaScript`.

![La page HTML de base](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-02-02-at-06.19.40.png)
_La page HTML de base_

Dans ce fichier apparemment simple, nous avons combiné `style`, `script` et `markup` (balisage) — les trois composants principaux de toute application web.

Les composants Astro sont identiques aux fichiers HTML, ce qui nous amène à notre première définition d'un composant Astro.

### Un composant Astro est un fichier `.astro` capable de rendre n'importe quel HTML valide

Un composant Astro est un document avec une terminaison de fichier `.astro`, c'est-à-dire `file.astro` ou `anotherFile.astro` capable de rendre un contenu HTML valide.

Commençons un projet `hello-astro` minimal pour explorer cette déclaration. Cette fois, nous n'utiliserons pas l'utilitaire `create astro`. Au lieu de cela, nous installerons Astro manuellement.

Créez un répertoire vide et naviguez dedans :

```bash
mkdir hello-astro
cd hello-astro

```

Exécutez la commande suivante pour démarrer le nouveau projet :

```js
npm init --yes

```

Le drapeau `--yes` utilisera toutes les valeurs par défaut, sautant les invites.

Maintenant installez `astro` :

```js
npm install astro

```

Créez une page Astro vide dans le projet dans `src/pages/index.astro`.

Ce fichier doit être dans le répertoire `src/pages` car les `pages` sont le point d'entrée d'un projet Astro.

Maintenant, nous devrions avoir une structure de projet similaire à la suivante :

![La structure du projet hello-astro.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-02-02-at-07.30.52.png)
_La structure du projet hello-astro._

À ce stade, allez-y et collez l'extrait `HTML` de départ dans le composant `index.astro` comme suit :

```html
<!-- 📂 src/pages/index.astro -->
<!DOCTYPE html>
<html lang="en-GB">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width" />
    <title>HTML 101</title>

    <style>
      p {
        color: red;
      }
    </style>

    <script>
      console.log('Hello world');
    </script>
  </head>
  <body>
    <p>Hello World</p>
  </body>
</html>

```

Ensuite, démarrez l'application avec la commande :

```html
npx astro dev

```

![L'application hello astro](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-02-04-at-07.09.03.png)
_L'application hello astro_

Nous avons `Hello World` en rouge ! `index.astro` rend avec succès le contenu `HTML` sur la page `index` de notre application web.

Un HTML valide est donc un Astro valide.

Si vous connaissez le HTML, vous connaissez déjà un peu d'Astro.

La familiarité avec le HTML rend Astro accessible. Mais les composants Astro seraient inutiles s'ils étaient équivalents aux pages `HTML`. Construire une nouvelle bibliothèque (Astro) identique au HTML serait un gaspillage de ressources. Enfin, à part le logo Astro fantaisie, c'est une victoire.

Heureusement, la syntaxe des composants Astro fournit des fonctionnalités attendues d'une bibliothèque frontend moderne, ce qui en fait **un sur-ensemble de HTML**.

Cela mène à notre deuxième définition.

### Les composants Astro peuvent être composés pour créer des pages complexes

Les fichiers HTML standard ne peuvent pas être composés. Nous ne pouvons pas importer des fichiers HTML dans un autre fichier HTML. Ce serait invalide.

Mais la composabilité est vitale pour structurer des interfaces utilisateur complexes.

Les composants Astro sont composables, ce qui les rend hautement flexibles et réutilisables.

![La relation composant parent enfant](https://blog.ohansemmanuel.com/content/images/2023/06/c.png)
_La relation composant parent enfant_

Le pseudocode suivant serait une représentation valide de composants parents-enfants :

```html
<AstroComponent>
	<!-- render children components in here -->
	<ChildAstroComponent />
	<ChildAstroComponent />
	<ChildAstroComponent />
</AstroComponent>

```

Le modèle mental simplifié pour construire des sites web classiques implique d'enchaîner un tas de pages HTML pour constituer un site web.

Astro s'appuie sur le même modèle mental.

Donc, essentiellement, un site web Astro comprend des pages qui sont finalement compilées en `HTML`.

![Un site web fait de pages Astro.](https://blog.ohansemmanuel.com/content/images/2023/06/c-1.png)
_Un site web fait de pages Astro._

Puisque les pages Astro sont juste des composants Astro trouvés dans le répertoire `src/pages` de notre projet Astro, elles peuvent également composer d'autres composants Astro.

Essayons cela.

Considérez la page `index.astro` de départ ci-dessous :

```html
<!-- 📂src/pages/index.astro -->

<!DOCTYPE html>
<html lang="en-GB">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width" />
    <title>HTML 101</title>

    <style>
      p {
        color: red;
      }
    </style>

    <script>
      console.log('Hello world');
    </script>
  </head>
  <body>
    <p>Hello World</p>
  </body>
</html>

```

Conceptuellement, nous pourrions composer le composant `index.astro` à partir de deux composants plus petits : `Head` et `Body`.

![Composer la page d'index à partir des composants Head et Body](https://blog.ohansemmanuel.com/content/images/2023/06/c-2.png)
_Composer la page d'index à partir des composants Head et Body_

Voici comment :

```js
<!-- 📂 src/pages/index.astro -->
---
import Body from "../components/Body.astro";
import Head from "../components/Head.astro";
---

<!DOCTYPE html>
<html lang="en-GB">
  <Head />
  <Body />
</html>


```

*   Les composants enfants sont importés à l'intérieur d'une barrière de code `---`
*   Les composants enfants sont rendus dans le template du composant, c'est-à-dire `<Head />` et `<Body />` — similaire aux balises `HTML` auto-fermantes.

Où `Body` et `Head` sont comme suit :

```js
// 📂 src/components/Body.astro
<body>
  <p>Hello World</p>
</body>

```

```js
// 📂 src/components/Head.astro
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width" />
  <title>HTML 101</title>

  <style>
    p {
      color: red;
    }
  </style>

  <script>
    console.log("Hello world");
  </script>
</head>

```

Notez comment `Head` et `Body` représentent des blocs de construction `HTML` "partiels".

Le niveau de composition à partir duquel nous construisons nos pages dépend entièrement de nous. Par exemple, nous pourrions décomposer davantage le composant `Head` en morceaux plus petits.

Envisageons d'introduire des composants isolés pour les éléments `meta`, `title`, `style` et script.

![Composer le composant Head à partir d'autres composants plus petits](https://blog.ohansemmanuel.com/content/images/2023/06/c-3.png)
_Composer le composant Head à partir d'autres composants plus petits_

```js
// 📂 src/components/Head.astro
---
import Meta from "./Meta.astro";
import Title from "./Title.astro";
import Style from "./Style.astro";
import Script from "./Script.astro";
---

<head>
  <Meta />
  <Title />
  <Style />
  <Script />
</head>

```

La page `index` compose toujours les mêmes composants de haut niveau, c'est-à-dire `Head` et `Body`. Cependant, `Head` contient maintenant encore plus de composants.

C'est le niveau de composition disponible pour nous avec de nombreuses bibliothèques frontend modernes. Mais pour éviter les bugs indésirables, il y a quelques comportements essentiels à connaître lors de la composition de composants dans Astro.

#### 1. Les styles sont locaux par défaut

Il est vital de distinguer comment Astro se comporte lors de la composition de composants avec des styles.

Par exemple, nous avions un paragraphe rouge lorsque nous avons commencé avec tout le contenu `HTML` dans `index.astro`.

Maintenant, nous avons perdu le style de paragraphe après notre composition.

![Le style de paragraphe rouge perdu après la composition](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-02-04-at-13.04.36.png)
_Le style de paragraphe rouge perdu après la composition_

Qu'est-ce qui a mal tourné ?

Pour comprendre cela, nous devons déterminer où le style siège dans la composition du composant.

![Les styles dans les composants Astro sont locaux par défaut et ne fuient pas.](https://blog.ohansemmanuel.com/content/images/2023/06/c-4.png)
_Les styles dans les composants Astro sont locaux par défaut et ne fuient pas._

Nous avons le `style` défini dans le composant `Head.astro` et nous nous attendons à ce qu'il affecte le `<p>` dans le composant `Body.astro`.

Cela ne fonctionne pas.

C'est parce que, avec les composants Astro, les styles sont locaux par défaut. Cela signifie que le `<style>` dans `Head.astro` n'affecte que les éléments définis dans le composant `Head.astro`.

Puisque le `<p>Hello world</p>` vit dans un composant séparé, les styles ne fuient jamais.

#### 2. L'élément HTML sera toujours présent

L'élément `<html>` représente l'élément de niveau supérieur d'un document HTML. Il est souvent appelé l'élément racine. Les autres éléments doivent être des descendants.

Notre composition de page `index.astro` actuelle ressemble à ceci :

```js
// 📂 src/components/index.astro
---
import Body from "../components/Body.astro";
import Head from "../components/Head.astro";
---

<!DOCTYPE html>
<html lang="en-GB">
  <Head />
  <Body />
</html>

```

Chaque composant enfant est logé dans `Head` et `Body` et rendu dans l'élément racine `html`.

Mais que se passe-t-il si nous supprimons cet élément (et le `DOCTYPE` associé) comme vu ci-dessous :

```js
// src/components/index.astro
---
import Body from "../components/Body.astro";
import Head from "../components/Head.astro";
---

<Head />
<Body />

```

La page `HTML` sera rendue avec une valeur par défaut raisonnable :

```html
<!-- Default HTML wrapper provided -->
<!DOCTYPE html>
<html>
  <!-- Every other component rendered here -->
</html>

```

![La page rendue avec une valeur par défaut raisonnable.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-01-17-at-06.40.58@2x.png)
_La page rendue avec une valeur par défaut raisonnable._

Saviez-vous que selon les normes HTML, l'utilisation de `<html>` est optionnelle ? Cela signifie que même sans lui, le navigateur peut toujours rendre la page avec une valeur par défaut appropriée. Les navigateurs peuvent même rendre des pages HTML invalides !

Cela étant dit, le paramètre par défaut d'Astro vous permet de créer des modèles même avec un balisage HTML invalide. Donc, soyez prudent.

Pour des raisons d'accessibilité, incluez un élément `<html>`. Ceci est pertinent pour fournir l'attribut `lang` pour la page web. Encore une fois, cela est utile pour les technologies de lecture d'écran.

#### 3. Les styles et les scripts sont hissés (hoisted)

Les éléments `<script>` et `<style>` de notre page existent dans les composants associés `Script` et `Style`.

![Les composants enfants Style et Script](https://blog.ohansemmanuel.com/content/images/2023/06/c-5.png)
_Les composants enfants Style et Script_

Ces composants enfants sont également rendus précisément dans le composant `Head`, et finalement, nous avons un balisage avec `<style>` et `<script>` dans `<head>`.

```html
<head>
  <style> ... </style>
  <script> ... </script>
</head/>

```

Comme mentionné précédemment, le `HTML` est assez indulgent et tentera même de rendre un balisage HTML invalide. Mais l'élément `<style>` doit être inclus dans le `<head>` d'un document `HTML`.

Tentons de briser cette règle.

Changez `index.astro` pour avoir `Style` et `Script` comme composants frères adjacents à `Head` :

```js
---
import Body from "../components/Body.astro";
import Head from "../components/Head.astro";
import Style from "../components/Style.astro";
import Script from "../components/Script.astro";
---

<Head />
<Body />
<Style />
<Script />

```

Au lieu de rendre `Style` et `Script` dans le `<head>` du document, nous les avons placés adjacents aux éléments `<head>` et `<body>`.

D'après la composition ci-dessus, vous pourriez vous attendre à un balisage de rendu similaire à ce qui suit :

```js
<head> ... <head>
<body> .... </body>
<style> ... </style>
<script> ... </script>

```

Mais inspectez la page Astro rendue, et vous trouverez les éléments `style` et `script` toujours placés dans le `<head>` du document.

![Les éléments script et style hissés](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-02-04-at-13.50.39.png)
_Les éléments script et style hissés_

C'est parce que dans Astro, nous pouvons utiliser librement les éléments `<style>` et `<script>` dans nos composants, et ils seront hissés (hoisted) vers le `<head>` du document rendu. Ceci est indépendant de la composition du composant.

![<style> et <script> sont hissés vers le <head> de notre page](https://blog.ohansemmanuel.com/content/images/2023/06/c-6.png)
_&lt;style&gt; et &lt;script&gt; sont hissés vers le &lt;head&gt; de notre page_

Comme nous l'apprendrons plus tard, il y a une exception à ce comportement avec les scripts en ligne.

#### 4. L'élément <head> et ses enfants ne seront pas hissés

Voir comment les éléments `<style>` et `<script>` sont hissés peut vous tenter d'utiliser un élément `<head>` de manière incorrecte dans la composition de votre composant.

Mais notez que l'élément `<head>` et ses enfants ne seront pas hissés, c'est-à-dire qu'il n'est pas déplacé vers le haut de la page ou fusionné avec un `<head>` existant.

Ajoutons un nouvel élément `<head>` adjacent :

```js
// 📂 src/components/index.astro
---
import Body from "../components/Body.astro";
import Head from "../components/Head.astro";
import Style from "../components/Style.astro";
import Script from "../components/Script.astro";
---

<Head />
<Body />
<Style />
<Script />
<head>
  <meta property="og:type" content="article" />
</head>

```

Ajouter un nouvel élément `<head>` au bas de la page est une composition idiote. Mais les navigateurs pardonnent le mauvais balisage `HTML`, donc dans ce cas, l'élément `<head>` supplémentaire est ignoré, et son contenu est rendu dans l'élément `<body>` de la page.

![Le navigateur essayant de donner un sens à la mauvaise composition](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-01-17-at-07.50.01@2x.png)
_Le navigateur essayant de donner un sens à la mauvaise composition_

Ayez toujours les éléments de page `<head>` dans un composant de mise en page pour éviter les comportements indésirables. C'est une meilleure pratique recommandée.

### Les composants Astro peuvent exploiter une syntaxe de templating puissante

Le templating est au cœur de la plupart des bibliothèques frontend bien-aimées. Pensez à React et JSX ou Vue et les templates Vue.

Astro n'est pas différent.

Astro fournit un templating puissant en divisant un composant en deux parties principales : le script de composant et les sections de template de composant.

![La constitution d'un composant Astro](https://blog.ohansemmanuel.com/content/images/2023/06/c-7.png)
_La constitution d'un composant Astro_

Il est important de noter que techniquement, un composant Astro est toujours valide avec une ou aucune des sections présentes, c'est-à-dire qu'un composant Astro vide (mais valide) n'aura aucune de ces sections.

#### Script de composant

La section script de composant est identifiée par une barrière de code `(---)`.

```js
---
  // This is the component script section
---

```

Généralement, la section script de composant est l'endroit où nous écrivons le code JavaScript que nous devons référencer dans notre template.

![Exploiter les valeurs de la section script de composant dans le template de composant](https://blog.ohansemmanuel.com/content/images/2023/06/c-8.png)
_Exploiter les valeurs de la section script de composant dans le template de composant_

Rappelez-vous que lorsque notre composant Astro est finalement compilé, les expressions JavaScript dans la section script sont évaluées au moment de la construction. Par conséquent, les valeurs JavaScript sont utilisées pour générer les pages `HTML` finales une fois.

La section script de composant n'est pas l'endroit pour le code JavaScript interactif dynamique.

Cela étant dit, il y a trois actions principales que nous effectuerons dans la section script de composant.

Jetons un coup d'œil à celles-ci.

##### 1. Créer ou référencer des variables

Nous pouvons avoir besoin de créer des variables pour diverses raisons, par exemple pour garder notre balisage DRY (don't repeat yourself). De plus, la section script de composant prend en charge le code JavaScript et TypeScript standard. Donc, créer ou référencer des variables fonctionne comme nous nous y attendrions.

```js
---
// Javascript
const newVariable = "This is a new variable"
// Typescript
let newVar: string = "This is a new var";
newVar = 9;
---

```

Si l'IDE est configuré pour TypeScript, nous obtiendrons un avertissement dans l'éditeur lorsque nous essaierons de réassigner la variable `newVar` à un nombre :

```js
Type 'number' is not assignable to type 'string'.

```

TypeScript est pris en charge dans la section script de composant par défaut.

Les composants sont également capables de recevoir des props. Les props sont des attributs de type HTML passés lorsque nous rendons un composant. Par exemple, voici une prop name passée à un composant `MyAstroComponent` :

```js
<MyAstroComponent name="Emmanuel"/>

```

Dans la section script de composant, les props passées à un composant peuvent être référencées sur le global `Astro.props` comme indiqué ci-dessous :

```js
<!-- 📂 MyAstroComponent.astro -->
---
const { name } = Astro.props
---

```

Puisque TypeScript est valide dans la section script de composant, nous pouvons également typer la prop d'un composant.

Pour fournir des types de props, allez-y et définissez une interface `Props` ou un alias de type dans la section script de composant :

```js
---
// ✅ This is valid
type Props = {
  name: string
}
---

```

```js
---
// ✅ This is equally valid
interface Props {
  name: string
}
---

```

Astro détectera automatiquement le type `Props` défini et donnera des avertissements/erreurs de type pertinents liés à une mauvaise utilisation des props de composant.

##### 2. Gestion des imports

Au début de la plupart des modules JavaScript se trouvent les imports. Les composants Astro ne sont pas différents.

Composer plusieurs composants Astro pour construire des pages complexes signifie généralement importer d'autres composants ou exploiter des modules nécessaires pour faire fonctionner notre page comme prévu.

Prêt à l'emploi, Astro prend en charge un large éventail de types de fichiers, à savoir :

*   Composants Astro (`.astro`)
*   Markdown (`.md`, `.markdown`, et ainsi de suite)
*   JavaScript (`.js`, `.mjs`)
*   TypeScript (`.ts`, `.tsx`)
*   Paquets NPM
*   JSON (`.json`)
*   JSX (`.jsx`, `.tsx`)
*   CSS (`.css`)
*   Modules CSS (`.module.css`)
*   Images & Actifs (`.svg`, `.jpg`, `.png`, et ainsi de suite)

Cela fait beaucoup de types de fichiers pris en charge nativement ! Voici quelques exemples d'instructions d'importation :

```js
// Astro
import Book from './book.astro'

// Javascript
import { getUnderstandingAstro } from './book.js';

// Typescript
import { getUser } from './book';
import type { UserType } from './book';

// NPM package
import { v4 as uuidv4 } from 'uuid';

// load JSON via default export
import json from './data.json';

// load and inject style onto the page
import './style.css';

// css modules
import styles from './style.module.css';

// other assets
import imgReference from './image.png';
import svgReference from './image.svg';
import txtReference from './words.txt';


```

Le point important à noter ici est qu'à part les fichiers TypeScript et les paquets NPM, nous devons généralement ajouter la terminaison de fichier à l'instruction d'importation Astro, par exemple :

```js
// ✅ do this
import Book from './book.astro'

// ❌ not this
import Book from './book'

```

Astro prend également en charge l'importation de composants d'autres frameworks UI tels que React, Vue, Svelte, et ainsi de suite. Un exemple d'importation pour un composant React ressemblerait à ceci :

```js
import { Header } from './Header.jsx'
// if file ending is .tsx
import { Header } from './Header'

```

Nous explorerons cela dans un chapitre ultérieur.

Il est également important de noter que nous pouvons importer n'importe quel actif du répertoire `public`. Mais notez que les actifs dans le répertoire `public` resteront intacts par Astro, c'est-à-dire qu'ils seront copiés tels quels dans le build final sans traitement (par exemple, minification).

```js
// image in public/img-public.png
import imageRef from "/img-public.png";

```

En tant que meilleure pratique, privilégiez le placement des images dans le répertoire `src` afin qu'Astro puisse les transformer, les optimiser et les regrouper si possible. L'exception concerne les images dans les fichiers markdown (`.md`).

Les images dans `src` ne fonctionneront pas dans les fichiers markdown, utilisez donc le répertoire `public` ou une URL `src` distante comme indiqué ci-dessous :

```md
// my-nice-blog.md

![A wonderful photo of a cat](/photo-in-public-dir.png)
![Another cat photo](https://www.photos.com/this-is-a-cat.png)

```

##### 3. Récupération de données

Les composants Astro peuvent utiliser la fonction globale `fetch` pour établir des requêtes HTTP vers des API distantes depuis la section script de composant. Les données récupérées peuvent ensuite être accessibles dans le template de composant.

```js
---
{/** Random user generator **/}
const URL = "https://random-data-api.com/api/users/random_user?size=1"
const response = await fetch(URL)
const data = await response.json()
---

// Use data in the template
<pre>{JSON.stringify(data, null, 2)}</pre>


```

L'appel API ne sera effectué qu'une seule fois pour les sites Astro générés statiquement pour construire la page `HTML`.

Mais lors du développement local, les requêtes API dans la section script de composant sont récupérées à chaque rafraîchissement de page. C'est seulement un comportement de développement. Dans notre exemple, nous obtiendrons un nouvel utilisateur aléatoire à chaque rafraîchissement de page.

Exécutez le build de production avec `npm run build` et prévisualisez l'application de production avec `npm run preview` pour voir le comportement standard en action. Nous aurons un seul utilisateur à chaque rafraîchissement de page, c'est-à-dire l'utilisateur récupéré au moment de la construction.

#### Template de composant

Les variables créées, les imports effectués et les données récupérées dans la section script de composant existent principalement pour une raison : être consommés dans la section template de composant du composant.

![Consommer des variables dans la section template de composant](https://blog.ohansemmanuel.com/content/images/2023/06/d.png)
_Consommer des variables dans la section template de composant_

Si les composants Astro sont finalement construits en `HTML`, la section template définit le balisage de ladite page `HTML`. Mais la section template de composant nous permet de le faire dynamiquement, c'est-à-dire en exploitant la puissance des expressions JavaScript.

Explorons certaines des actions que nous sommes susceptibles d'effectuer dans le template de composant d'un composant Astro.

##### Consommer des variables

Pour consommer une variable, enveloppez le nom de la variable dans des accolades comme indiqué ci-dessous :

```js
---
const book = "Understanding AstroJS";
---

<h1>{book}</h1> // Outputs <h1>Understanding AstroJS</h1>

```

##### Créer des attributs dynamiques

Créer un attribut dynamique est similaire à la consommation d'une variable. Utilisez la variable entre accolades pour passer des attributs aux éléments HTML et aux composants :

```js
---
const { author } = Astro.props;
const book = "Understanding AstroJS";
---

<h1 data-name={book}>A new book</h1>
// Outputs <h1 data-name="Understanding AstroJS">A new book</h1>

```

##### HTML dynamique

Le HTML dynamique est un véritable sauveur car nous ne voudrons parfois pas nous répéter. Par exemple, considérez comment nous pouvons créer des listes dynamiques comme indiqué ci-dessous :

```js
---
const technologies = ['Javascript', 'Typescript', 'NodeJS']
---
// Dynamically create a list of elements from technologies
<ul>
  {items.map((item) => <li>{item}</li>)}
</ul>

```

Ou nous pouvons nous trouver dans le besoin d'un rendu conditionnel. Pour ce faire, exploitez les opérateurs logiques et les expressions ternaires comme indiqué ci-dessous :

```js
---
const showCallToAction = true;
---

// This will render <button>Buy now</button>
{showCallToAction && <button>Buy now</button>}

// Alternatively, represent this with a ternary to provide a fallback
{showCallToAction ?  <button>Buy now</button> : <p>Continue
 shopping</p>}

```

Cela rendra `<button>Buy now</button>` lorsque `showCallToAction` est vrai et `<p>Continue shopping</p>` sinon.

##### Balises dynamiques

Moins couramment utilisées, les balises dynamiques peuvent toujours être utiles dans certaines situations, comme la construction de composants polymorphes.

Selon l'entrée de prop du consommateur, ces composants peuvent rendre divers nœuds d'éléments. Un exemple est le composant `Text.astro` qui peut rendre n'importe quel élément qui lui est passé :

```js
// usage
<Text as="h1" />
<Text as="div" />

```

Dans les deux cas, nous voulons rendre le même composant avec différents nœuds d'éléments HTML sous-jacents, c'est-à-dire des nœuds de texte `h1` et `div`.

Nous pouvons gérer cela dynamiquement, comme indiqué ci-dessous :

```js
<!-- 📂 Text.astro -->
---
const { as: As = "h1" } = Astro.props;
---

<As>Text content</As>

```

Dans la section script de composant, nous déconstruisons la prop `as` et la renommons en une variable capitalisée `As`. Ceci est important car les noms de variables pour un composant rendu dynamiquement doivent être capitalisés, c'est-à-dire :

```js
// ✅ Do this
<As>Text content</As>

// ❌ not this
<as>Text content</as>

```

Si nous passons une variable en minuscules, Astro essaiera de rendre le nom de la variable comme une balise `HTML` littérale. Dans notre exemple, `<as>Text content</as>` et non l'élément dynamique `<h1>Text content</h1>` ou `<div>Text content</div>`.

##### Revisiter les Slots

Si vous voulez facilement ajouter du contenu HTML externe à votre template de composant, l'élément `<slot />` est votre ami ! Tous les éléments enfants que vous incluez seront automatiquement rendus dans le `<slot />` d'un composant.

![Utiliser l'élément <slot/>.](https://blog.ohansemmanuel.com/content/images/2023/06/slot.png)
_Utiliser l'élément &lt;slot/&gt;._

Si nous avions un composant `Main` de base avec un slot comme indiqué ci-dessous :

```js
// 📂 src/components/main.astro
---
---

<main>
  <slot />
</main>

```

Les éléments enfants de `Main` seront rendus dans le `<slot />` comme indiqué ci-dessous :

```js
// 📂 src/pages/index.astro
---
---
<Main>
  <p>This will be rendered in the slot </p>
</Main>

```

Nous pouvons également fournir un contenu de repli `<slot>` lorsqu'aucun élément enfant n'est passé au composant. Pour ce faire, fournissez au `<slot />` ses propres enfants comme indiqué ci-dessous :

```js
// 📂 src/components/main.astro
---
---

<main>
  <slot>
    <p>This paragraph will be rendered if no child elements are passed to Main</p>
  </slot>
</main>

```

Il est possible de fournir plus d'un slot via des slots nommés. Considérez l'exemple suivant :

```js
// 📂 src/components/main.astro
---
---

<main>
  <h1> This is header </h1>
  <slot />
  <p>This is an INTRO paragraph </p>
  <slot name="after-intro" />
  <footer> &copy; 2023 </footer>
  <slot name="after-footer" />
</main>

```

Dans ce cas, nous pouvons rendre des éléments enfants spécifiques aux slots spécifiques `after-intro` et `after-footer` comme indiqué ci-dessous :

```js
// 📂 src/pages/index.astro
---
---
<Main>
  <p slot="after-intro">Hello after Intro</p>
  <p>This will be rendered in the default (nameless) slot </p>
  {/** This will be rendered in the after-footer slot **/}
  <p slot="after-footer">Download my new book </>
</Main>

```

##### Pas tout à fait JSX

La syntaxe d'Astro semblera très familière aux développeurs React car elle est conçue pour ressembler à HTML et JSX. Mais il y a des différences significatives à connaître pour ne pas se tirer une balle dans le pied.

Tous les attributs `HTML` dans `JSX` utilisent des formats `camelCase`. Dans Astro, tenez-vous-en au format standard `kebab-case` :

```js

<!-- JSX -->
<div className="foo" dataValue="bar" />

<!-- Astro -->
<div class="foo" data-value="bar" />

```

Contrairement à `JSX`, utilisez `class`, pas `className`.

Dans Astro, nous pouvons également utiliser des commentaires JavaScript ou HTML standard :

```js
---
//This is a comment
---
<!-- HTML-style comment -->
{/* JS style comment also valid */}

```

Les deux sont valides dans les composants Astro. Mais dans JSX, seuls les commentaires de style JavaScript sont pris en charge.

Avec Astro, il est essentiel de noter que les commentaires de style HTML seront inclus dans le DOM du navigateur lors de la construction de la page. Mais les commentaires de style JavaScript seront ignorés. En tant que tel, pour les commentaires de développement uniquement, préférez l'utilisation de commentaires de style JavaScript.

Ma différence préférée est que nous pouvons utiliser le raccourci d'attribut pour des variables nommées de manière identique dans Astro, par exemple :

```js
---
const name = "Understanding astro"
---

<MyComponent {name} />

// This is identical to writing <MyComponent name={name}>

```

Ce raccourci n'est pas pris en charge dans JSX.

Astro et JSX diffèrent également dans la façon dont les espaces blancs sont traités. Astro suit les règles HTML aussi étroitement que possible. Mais contrairement à JSX, les espaces blancs ne sont pas échappés.

```js
// ❌ will render span (string) with extra whitespace(s)
<span>
  <slot />
</span>

// ✅ will add no extra character spaces
<span><slot /></span>

```

Dans la plupart des cas, ce n'est pas très important sauf quand vous ne voulez pas cet espace là ! Par exemple, avec des arrière-plans de texte colorés.

Considérez le composant `Code.astro` indiqué ci-dessous :

```js
// 📂 src/components/Code.astro
---
---

<code>
  <slot />
</code>

<style>
  code {
    background-color: red;
    color: wheat;
  }
</style>

```

Inclure le composant `Code` dans un paragraphe entraînera des espaces blancs mis en évidence.

![Espaces blancs supplémentaires dans les arrière-plans de texte colorés.](https://blog.ohansemmanuel.com/content/images/2023/06/white-space.png)
_Espaces blancs supplémentaires dans les arrière-plans de texte colorés._

```js
// 📂 src/pages/index.astro
---
import Code from "../components/Code.astro";
---

<p>Use an <Code>if</Code> statement. Displaying a list? Try array <Code>map()</Code>.</p>

```

Pour éviter cela, changez le rendu du composant `Code` pour ignorer les espaces blancs :

```js
// ✅ will add no extra character spaces
<span><slot /></span>

```

Et c'est tout !

## Conclusion de ce chapitre

Mettez tout cela ensemble, et nous avons maintenant une définition solide pour un composant Astro : un document avec une terminaison de fichier .`astro` représentant un sur-ensemble composable de HTML. Il fournit également une syntaxe de templating puissante et rend en HTML sans surcharge d'exécution Javascript.

Wow, si je devais demander à un candidat une définition de composant Astro lors d'un entretien et qu'il me donnait cette réponse, je le ferais chevalier sur-le-champ ! Le poste est à lui.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-135.png)
_Chapitre trois._

# Chapitre 3 : Construisez votre propre îlot de composants

> "Longue est la route de l'apprentissage par les préceptes, mais courte et fructueuse par les exemples." — Sénèque le Jeune

Le récit rapide d'Astro repose sur les îlots de composants, qui vous permettent d'utiliser d'autres composants de framework comme React, Vue ou Svelte dans vos applications Astro. Ce chapitre nous guidera dans la création de notre propre îlot de composants à partir de zéro.

Pour voir l'application complète, consultez le [dépôt GitHub](https://github.com/understanding-astro/build-your-own-component-island).

## Ce que vous apprendrez

*   Un aperçu des différentes techniques de rendu d'application web.
*   Construire votre propre implémentation d'îlots de composants à partir de zéro.
*   Comprendre l'architecture des îlots.

## Une brève histoire de comment nous en sommes arrivés là

Pour nous assurer que l'implémentation technique à venir est construite sur une compréhension solide, jetons un coup d'œil dans le passé et explorons les différentes techniques de rendu d'application que nous pouvons employer sur une application frontend.

Il est essentiel de noter que ce n'est pas un guide exhaustif du rendu d'application front-end. Mais vous en apprendrez assez pour comprendre et apprécier l'architecture des îlots de composants.

### Où tout commence

En termes simples, il y a deux acteurs principaux dans le service d'une application à un utilisateur :

1.  Le client utilisateur, par exemple un navigateur web
2.  Le serveur d'application

Pour afficher un site web, un utilisateur demande une ressource à un serveur d'application.

![Le navigateur web demandant article.html à un serveur d'application](https://blog.ohansemmanuel.com/content/images/2023/06/a-5.png)
_Le navigateur web demandant article.html à un serveur d'application_

Avec ces deux acteurs en jeu, une décision architecturale importante que vous prendrez lors de la construction de toute application frontend décente est de savoir s'il faut rendre une application sur le client ou le serveur.

Explorons brièvement les deux options.

### Rendu côté client (CSR)

![Choisir le rendu côté client.](https://blog.ohansemmanuel.com/content/images/2023/06/1.png)
_Choisir le rendu côté client._

Par définition, une application rendue côté client rend les pages directement dans le navigateur en utilisant JavaScript. Toute la logique, la récupération de données, le templating et le routage sont gérés sur le client (le navigateur de l'utilisateur).

![Un aperçu d'une application rendue côté client.](https://blog.ohansemmanuel.com/content/images/2023/06/a-1.png)
_Un aperçu d'une application rendue côté client._

Les années passées ont vu la montée du rendu côté client, en particulier parmi les applications à page unique. Vous avez probablement vu cela en action si vous avez travaillé avec des bibliothèques comme React ou Vue.

Pour un aperçu pratique, considérez la page web d'un article de blog avec un compteur de likes et une section de commentaires sous la fenêtre d'affichage initiale.

![Un article de blog avec une barre latérale dynamique et une section de commentaires sous l'article.](https://blog.ohansemmanuel.com/content/images/2023/06/a-2.png)
_Un article de blog avec une barre latérale dynamique et une section de commentaires sous l'article._

Si cette application était entièrement rendue côté client, le flux de rendu simplifié ressemblerait à ceci :

1.  L'utilisateur visite votre site web.
2.  Votre serveur statique renvoie une page `HTML` presque vide au navigateur.
3.  Le navigateur récupère le fichier script lié dans la page `HTML`.
4.  Le JavaScript est chargé et analysé.
5.  Les données pour l'article, le nombre de commentaires et les commentaires sont récupérés.
6.  Une page entièrement interactive est montrée à l'utilisateur.

![Visualiser le processus de rendu du point de vue d'un utilisateur.](https://blog.ohansemmanuel.com/content/images/2023/06/a-3.png)
_Visualiser le processus de rendu du point de vue d'un utilisateur._

#### Les avantages du rendu côté client (CSR)

*   L'utilisateur reçoit rapidement la ressource du serveur. Dans notre cas, une page `HTML` presque vide, mais du bon côté, l'utilisateur reçoit cela rapidement ! En termes techniques, le rendu côté client donne un temps élevé jusqu'au premier octet (**TTFB**).
*   Sans doute accessible à comprendre. Toute la logique, la récupération de données, le templating et le routage sont gérés en un seul endroit – le client.

#### Les inconvénients du rendu côté client

*   Il faut potentiellement beaucoup de temps à l'utilisateur pour voir quelque chose de tangible sur notre page, c'est-à-dire qu'il est initialement confronté à un écran vide. Même si nous changeons la page `HTML` initiale envoyée au navigateur pour être une coquille d'application vide, cela prend toujours potentiellement du temps pour que l'utilisateur voie les données éventuelles, c'est-à-dire après que le Javascript soit analysé et les données récupérées du serveur.
*   À mesure que l'application grandit, la quantité de JavaScript analysée et exécutée avant d'afficher les données augmente. Cela peut avoir un impact négatif sur les performances mobiles.
*   Le temps jusqu'à l'interactivité (**TTI**) de la page souffre, par exemple cela prend beaucoup de temps avant que nos utilisateurs puissent interagir avec les commentaires. Tout le JavaScript doit être analysé, et toutes les données associées doivent être récupérées d'abord.
*   SEO préjudiciable s'il n'est pas implémenté correctement.

### Rendu côté serveur

![Choisir le rendu côté serveur.](https://blog.ohansemmanuel.com/content/images/2023/06/choosing-ssr.png)
_Choisir le rendu côté serveur._

Supposons que nous soyons mécontents du rendu côté client et décidions de faire le contraire.

À l'extrémité opposée du pôle de rendu se trouve le rendu côté serveur.

Dans une application rendue côté serveur, un utilisateur navigue vers notre site, et le serveur génère le `HTML` complet pour la page et le renvoie à l'utilisateur.

Dans notre exemple, voici à quoi ressemblerait un flux simplifié :

1.  L'utilisateur visite notre site web.
2.  Les données pour l'article, le profil utilisateur et les commentaires sont récupérés sur le serveur.
3.  Le serveur rend la page `HTML` avec l'article, le nombre de commentaires et d'autres actifs requis.
4.  Le serveur envoie au client une page `HTML` entièrement formée.

![Visualiser le processus de rendu du point de vue d'un utilisateur.](https://blog.ohansemmanuel.com/content/images/2023/06/aa.png)
_Visualiser le processus de rendu du point de vue d'un utilisateur._

NB : il est supposé que le serveur envoie une page `HTML` principalement statique avec un minimum de JavaScript nécessaire pour l'interactivité.

#### Les avantages du rendu côté serveur

*   Dès que le navigateur de l'utilisateur reçoit notre page `HTML` entièrement formée, il peut presque immédiatement interagir avec elle, par exemple les commentaires rendus. Il n'est pas nécessaire d'attendre que plus de JavaScript soit chargé et analysé. Dans le jargon de la performance, le temps jusqu'à l'interactivité (**TTI**) est égal au premier contenu peint (**FCP**).
*   Grands avantages SEO car les moteurs de recherche peuvent indexer vos pages et les explorer très bien.

#### Les inconvénients du rendu côté serveur

*   Générer des pages sur le serveur prend du temps. Dans notre cas, nous devons attendre que toutes les données pertinentes soient récupérées sur le serveur. En tant que tel, le temps jusqu'au premier octet (**TTFB**) est lent.
*   Gourmand en ressources : le serveur assume la charge de rendre le contenu pour les utilisateurs et les bots. En conséquence, les coûts de serveur associés augmentent car le rendu doit être fait sur le serveur.
*   Rechargements complets de la page pour chaque ressource serveur demandée.

### Rendu côté serveur avec hydratation côté client

Nous avons exploré le rendu des deux côtés du pôle de rendu d'application. Mais et s'il y avait un moyen d'utiliser le rendu côté serveur et côté client ? Une stratégie juste au milieu du pôle de rendu hypothétique ?

![Choisir le SSR avec hydratation côté client.](https://blog.ohansemmanuel.com/content/images/2023/06/ssr-with-client-rehydration.png)
_Choisir le SSR avec hydratation côté client._

Si nous construisions une application interactive et travaillions avec un framework comme React ou Vue, une approche largement courante est de rendre sur le serveur et d'hydrater sur le client.

L'hydratation, en termes simples, signifie re-rendre l'application entière à nouveau sur le client pour attacher des gestionnaires d'événements au DOM et prendre en charge l'interactivité.

En théorie, cela est censé nous donner les avantages du rendu côté serveur plus l'interactivité que nous obtenons avec des applications riches rendues côté client.

Dans notre exemple, voici à quoi ressemblerait un flux simplifié :

1.  L'utilisateur visite notre site web.
2.  Les données pour l'article, le profil utilisateur et les commentaires sont récupérés sur le serveur.
3.  Le serveur rend la page `HTML` avec l'article, le nombre de commentaires et d'autres actifs requis.
4.  Le serveur envoie au client une page `HTML` entièrement formée aux côtés de l'exécution client JavaScript.
5.  Le client "démarre" ensuite JavaScript pour rendre la page interactive.

Rendre une page autrement statique interactive (par exemple, attacher des écouteurs d'événements) est appelé hydratation.

![Visualiser le processus de rendu du point de vue d'un utilisateur.](https://blog.ohansemmanuel.com/content/images/2023/06/ssr-csr-hydrate-flow.png)
_Visualiser le processus de rendu du point de vue d'un utilisateur._

#### Les avantages du rendu côté serveur avec hydratation côté client

*   Avantages du SSR, par exemple FP et FMP rapides
*   Peut alimenter des applications hautement interactives.
*   Style de rendu pris en charge dans la plupart des frameworks frontend tels que React et Vue.

#### Les inconvénients du rendu côté serveur avec hydratation côté client

*   Temps lent jusqu'au premier octet — similaire au SSR standard.
*   Cela peut retarder le temps jusqu'à l'interactivité (TTI) en faisant paraître l'interface utilisateur prête avant de terminer le traitement côté client. La période où l'interface utilisateur semble prête mais est insensible (non hydratée) est ce qui a été — assez hilarant — surnommé la vallée de l'étrange (uncanny valley).

NB : cela suppose que certaines parties de notre application, telles que les likes et les commentaires, peuvent être interagies, par exemple cliquées pour effectuer une action supplémentaire.

### Hydratation partielle pour la victoire

Combiner le rendu côté serveur avec l'hydratation côté client a le potentiel d'offrir le meilleur des deux mondes. Mais ce n'est pas sans ses démérites.

Une façon de s'attaquer au lourd retard dans le temps jusqu'à l'interactivité (TTI) semble claire. Au lieu d'hydrater l'application entière, pourquoi ne pas hydrater uniquement les morceaux interactifs ?

![Hydratation partielle vs hydratation pleine page.](https://blog.ohansemmanuel.com/content/images/2023/06/p-hydration.png)
_Hydratation partielle vs hydratation pleine page._

Contrairement à l'hydratation de l'application entière côté client, l'hydratation partielle fait référence à l'hydratation de parties spécifiques d'une application tout en laissant le reste statique.

Par exemple, dans notre application, nous laisserions le reste de la page statique tout en hydratant juste le bouton like et la section commentaire.

Nous pouvons également pousser l'hydratation partielle plus loin et implémenter ce qu'on appelle l'hydratation paresseuse (lazy hydration). Par exemple, notre application a une section de commentaires sous la fenêtre d'affichage initiale.

Dans ce cas, nous pouvons hydrater le bouton like lorsque la page est chargée et hydrater la section commentaire uniquement lorsque l'utilisateur fait défiler sous la fenêtre d'affichage initiale.

![Hydrater la section commentaire plus tard.](https://blog.ohansemmanuel.com/content/images/2023/06/a-4.png)
_Hydrater la section commentaire plus tard._

Parlez de flexibilité !

#### Les avantages de l'hydratation partielle

*   Les mêmes avantages du rendu côté serveur avec hydratation côté client.
*   Temps plus rapide jusqu'à l'interactivité car l'application entière n'est pas hydratée.

#### Les inconvénients de l'hydratation partielle

*   Si la plupart des parties de l'application sont interactives et ont une priorité élevée, l'avantage de l'hydratation partielle pourrait être sans doute minime, c'est-à-dire que l'application entière prendrait tout autant de temps à être hydratée.

### D'où vient l'architecture des îlots ?

L'architecture des îlots est construite sur la base de l'hydratation partielle. Essentiellement, l'architecture des îlots fait référence au fait d'avoir des "îlots d'interactivité" sur une page `HTML` autrement statique.

![Îlots d'interactivité sur une page web autrement statique.](https://blog.ohansemmanuel.com/content/images/2023/06/independent-islands.png)
_Îlots d'interactivité sur une page web autrement statique._

Pour donner un sens à cela, pensez à ces îlots comme des composants partiellement hydratés. Donc notre page entière n'est pas hydratée, mais plutôt ces îlots.

## Comment implémenter une architecture d'îlots à hydratation partielle

C'est l'heure du jeu, mon pote.

Cette section peut sembler difficile, mais je suggère de prendre votre temps et de coder en même temps si possible. Mais, bien sûr, vous vous en sortirez probablement bien si vous êtes un ingénieur plus expérimenté.

Nous commencerons à construire notre propre implémentation d'architecture d'îlots à partir de zéro. En termes plus techniques, nous implémenterons une architecture d'îlots à hydratation partielle indépendante du framework.

Ouf ! C'est une bouchée.

Décomposons cela.

### Objectifs

Le but de cet exercice n'est pas de construire une bibliothèque à part entière ou de créer un clone exact de l'implémentation Astro Island. Non !

Notre objectif est de retirer la couche perçue de complexité et de dépouiller les îlots de composants jusqu'à une unité fondamentale digestible.

Voici les exigences fonctionnelles pour notre implémentation d'îlots :

1.  Indépendant du framework : notre solution doit fonctionner sur plusieurs frameworks, par exemple, `Preact`, `Vue`, `Petite-Vue` et `React`.
2.  Une implémentation d'architecture d'îlots à hydratation partielle : nous supprimerons JavaScript par défaut et n'hydraterons que sur une base nécessaire.
3.  Pas d'étape de build frontend : pour simplifier, notre implémentation ignorera une étape de build frontend, par exemple en utilisant `babel.`
4.  Prendre en charge l'hydratation paresseuse : c'est une forme d'hydratation partielle où nous pouvons déclencher l'hydratation plus tard et non immédiatement après le chargement du site. Par exemple, si un îlot est hors écran (pas dans la fenêtre d'affichage), nous ne chargerons pas le JavaScript pour l'îlot. Nous ne le ferons que lorsque l'îlot sera visible.

### Installation

Appelons notre module d'îlot `mini-island`.

Pour installer `mini-island`, un développeur importera notre module _bientôt construit_ comme indiqué ci-dessous :

```js
<script type="module">
    {/** import a mini-island.js module **/}
	import "/mini-island.js"
</script>

```

Pour profiter des avantages de l'hydratation partielle, les développeurs ajouteront `mini-island.js` à leur page avec la promesse d'avoir une petite empreinte JS — un petit prix à payer pour obtenir des îlots d'interactivité partiellement hydratés.

### Conception de l'API

Notre premier objectif est de nous assurer que notre solution est agnostique au framework. Une excellente solution native pour les implémentations agnostiques au framework est les **composants web** (web components).

Par définition, les composants web sont une suite de technologies qui nous permet de créer des éléments personnalisés réutilisables.

Si vous êtes nouveau aux composants web, au lieu de rendre un élément HTML standard, par exemple un `div`, nous créerons notre élément HTML personnalisé, `mini-island`.

`mini-island.js` exposera un élément personnalisé avec l'utilisation de base suivante :

```js
<mini-island>
 This is an island
</mini-island>

```

À l'intérieur de `<mini-island>`, un développeur pourra exploiter un îlot d'interactivité sur une page autrement statique.

Nous prendrons en charge trois attributs `<mini-island>` différents pour gérer l'hydratation partielle et paresseuse : `client:idle`, `client:visible` et `client:media={QUERY}`.

Voici un exemple de la façon dont ils seraient utilisés sur `<mini-island>` :

```js
<mini-island client:idle />
<mini-island client:visible />
<mini-island client:media="(max-width: 400px)" />

```

Ces attributs affecteront la façon dont l'îlot est hydraté.

*   `client:idle` : charger et hydrater JavaScript lorsque la page entière est chargée et que le navigateur est inactif.
*   `client:visible` : nous chargerons et hydraterons le JavaScript de l'îlot une fois que l'îlot sera visible, par exemple, lorsqu'il entrera dans la fenêtre d'affichage de l'utilisateur.
*   `client:media` : nous chargerons et hydraterons l'îlot une fois que la requête sera satisfaite, par exemple `client:media="(max-width: 400px)"`.

Il y a une dernière pièce à notre conception d'API. Comment les développeurs définiront-ils les scripts ou le balisage à hydrater ?

Nous utiliserons l'élément HTML `<template>`, l'élément de modèle de contenu.

```html
<!-- ❌ incorrect usage: -->
<mini-island client:idle>
    <script>
      console.log("this should be partially hydrated")
    </script>
</mini-island>

<!-- ✅ correct usage: -->
<mini-island client:idle>
  <!-- use the <template> element -->
  <template>
    <script>
      console.log("this should be partially hydrated")
    </script>
  </template>
</mini-island>

```

`<template>` est généralement utilisé pour contenir du `HTML` qui ne devrait pas être rendu immédiatement au chargement de la page. Mais le `HTML` peut être instancié via JavaScript.

Par exemple, en supposant qu'un utilisateur veuille enregistrer un avertissement dans la console mais veuille utiliser notre implémentation d'îlot, il ferait ce qui suit :

```js
<mini-island>
  <h2> Warning, something may be wrong </h2>
  <template data-island>
     <script type="module">
		console.error("something has gone wrong")
     </script>
  </template>
<mini-island>

```

Lorsque ce qui précède est rendu, le message `<h2> Warning, something may be wrong </h2>` sera affiché. Mais les éléments enfants du `template` ne seront pas rendus par défaut, c'est-à-dire que le `script` ne sera jamais exécuté.

Notre implémentation `mini-island` saisira le contenu du `template` et initialisera le `<script>` lorsque souhaité.

Par exemple, si l'utilisateur passe un attribut `client:visible`, nous nous assurerons que le script ne s'exécute que lorsque l'îlot est visible.

```js
<mini-island client:visible>
  <h2> Warning, something may be wrong </h2>
  <template data-island>
     <script type="module">
		console.error("something has gone wrong")
     </script>
  </template>
<mini-island>

```

Il est important de noter que nous attendons du développeur qu'il passe un attribut `data-island` au `template`. Nous n'hydraterons que les modèles avec l'attribut `data-island` pour éviter d'interférer avec d'autres modèles potentiels définis par l'utilisateur.

Ne vous inquiétez pas si cela semble flou pour le moment. Nous implémenterons et testerons cela avec des exemples qui consolideront votre compréhension.

### Pour commencer

Prêt ?

Commencez par créer un fichier `mini-island.js` dans le répertoire de votre choix.

Dans `mini-island`, créez un composant personnalisé minimal comme annoté ci-dessous :

```js
// 📂 mini-island.js

/**
 * Define a MiniIsland class to encapsulate the behaviour of
our custom element, <mini-island>
 * This class extends HTMLElement where the HTMLElement
interface represents any HTML element.
 */
class MiniIsland extends HTMLElement {
  /**
   * Define the name for the custom element as a static class
property.
   * Custom element names require a dash to be used in them
(kebab-case).
   * The name can't be a single word. ✅ mini-island ❌
miniIsland
   */
  static tagName = 'mini-island';
  /**
   * Define the island element attributes
   *, e.g., <mini-island data-island>
   */
  static attributes = {
    dataIsland: "data-island",
  };
}

/**
 * Our solution relies heavily on web components. Check that the
 * browser supports web components via the 'customElements' property
 */

if ('customElements' in window) {
  /**
   * Register our custom element on the CustomElementRegistry object using the define method.
   *
   * NB: The CustomElementRegistry interface provides methods for registering custom elements and querying registered elements.
   *
   * NB: The arguments to the define method are the name of the custom element (mini-island)
   * and the class (MiniIsland) that defines the behaviour of the custom element.
   *
   * NB: "MiniIsland.tagName" below represents the static class property, i.e., "static tagName".
   */
  window.customElements.define(MiniIsland.tagName, MiniIsland);
} else {
  /**
   * custom elements not supported, log an error to the console
   */
  console.error(
    'Island cannot be initiated because Window.customElements is unavailable.'
  );
}

```

Faisons quelques tests manuels de base pour nous pousser dans la bonne direction.

Créez un nouveau fichier `demos/initial.html` avec le contenu suivant :

```js
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Initial island demo</title>

    <script type="module">
      import "../mini-island.js";
    </script>
  </head>
  <body>
    <h1>Initial island demo</h1>
  </body>
</html>


```

Pour voir cela via un serveur web local, exécutez la commande suivante depuis le répertoire du projet :

```bash
 npx local-web-server

```

Par défaut, cela devrait démarrer un serveur web statique local sur le port `8000`. Nous pouvons maintenant voir la page de démonstration initiale sur `http://localhost:8000/demos/initial.html`

![La page de démonstration initiale.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-14-at-07.29.14.png)
_La page de démonstration initiale._

Confirmons que notre élément personnalisé `mini-island` est enregistré en rendant l'élément personnalisé avec un simple élément enfant paragraphe :

```html
<!-- 📂 demos/initial.html -->
...
<body>
    <h1>Initial island demo</h1>
    <mini-island>
       <p>Hello future island</p>
    </mini-island>
</body>

```

Cela rendra l'élément personnalisé et le paragraphe `Hello future island` comme prévu :

![Rendre l'élément personnalisé avec un élément enfant.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-14-at-07.27.26.png)
_Rendre l'élément personnalisé avec un élément enfant._

Maintenant, allons-y et ajoutons du JavaScript à l'intérieur de `<mini-island>` comme indiqué ci-dessous :

```html
<!-- 📂 demos/initial.html -->
...
<mini-island>
  <p>Hello future island</p>
  <script type="module">
    console.warn("THIS IS A WARNING FROM AN ISLAND");
  </script>
</mini-island>

```

Si vous rafraîchissez la page et vérifiez la console du navigateur, vous devriez voir l'avertissement journalisé.

![Avertissement de console de l'îlot.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-14-at-07.32.44.png)
_Avertissement de console de l'îlot._

Cela signifie que le script a été déclenché presque immédiatement. Pas notre solution idéale.

Alors que les images et la vidéo représentent plus de 70 % des octets téléchargés pour le site web moyen, octet par octet, JavaScript a un impact négatif plus important sur les performances.

Donc, notre objectif est de nous assurer que JavaScript ne s'exécute pas par défaut. Nous rendrons tout balisage pertinent dans l'îlot (HTML et CSS) mais différerons le chargement de JavaScript.

### Comment exploiter l'élément de modèle de contenu

`<template>` est un élément HTML natif qui est presque parfait pour notre cas d'utilisation.

Le contenu à l'intérieur d'un élément `<template>` est analysé pour sa correction par le navigateur mais n'est pas rendu.

Par exemple, allons-y et enveloppons le script de l'exemple précédent dans un élément `<template>` comme indiqué ci-dessous :

```html
<!-- 📂 demos/initial.html -->
...
<mini-island>
  <p>Hello future island</p>
  <template>
    <script type="module">
      console.warn("THIS IS A WARNING FROM AN ISLAND");
    </script>
  </template>
</mini-island>

```

Si vous rafraîchissez la page, vous remarquerez que le paragraphe `Hello future island` est rendu, mais le `script` à l'intérieur de `<template>` ne l'est pas, c'est-à-dire pas de journal dans la console.

C'est l'étape un : isoler JavaScript pour qu'il ne soit pas chargé tout de suite.

Cependant, l'objectif final ici est de s'assurer que le développeur peut décider quand exécuter le `script` à l'intérieur de notre `template` d'îlot.

Comme discuté dans l'implémentation d'API proposée, considérez ce qui suit :

```html
<mini-island client:visible>
  <p>Hello future island</p>
  <template>
    <script type="module">
      console.warn("THIS IS A WARNING FROM AN ISLAND");
    </script>
  </template>
</mini-island>

```

Avec l'attribut `client:visible`, nous n'initialiserons le script que lorsque l'îlot sera visible (dans la fenêtre d'affichage de l'utilisateur).

Sans prendre en compte les attributs `client:`, allons-y et initialisons tout contenu de modèle dès que l'élément `<mini-island>` est attaché au DOM.

Considérez le code annoté ci-dessous :

```js
// 📂 mini-island.js
class MiniIsland extends HTMLElement {
  // ...

  /**
   * The connectedCallback is a part of the custom elements lifecycle callback.
   * It is invoked anytime the custom element is attached to the DOM
   */
  async connectedCallback() {
    /**
     * As soon as the island is connected, we will go ahead and hydrate the island
     */
    await this.hydrate();
  }

  hydrate() {
    /**
     * Retrieve the relevant <template> child elements of the island
     */
    const relevantChildTemplates = this.getTemplates();
  }
}

```

Maintenant, nous allons tourner notre attention vers `getTemplates()`.

Puisque `<mini-island>` est un élément personnalisé étendant un `HTMLElement` standard, nous pouvons accéder aux méthodes de requête DOM traditionnelles telles que `querySelectorAll`.

Alors, utilisons `querySelectorAll` pour récupérer une liste de tous les éléments de modèle enfants avec un attribut `data-island`.

```js
// 📂 mini-island.js
// ...

getTemplates() {
  /**
   * querySelectorAll() returns a list of the document's elements that match the specified group of selectors.
   * The selector, in this case, is of the form "template[data-island]."
   *, i.e., this.querySelectorAll("template[data-island]")
  */
  return this.querySelectorAll(
    `template[${MiniIsland.attributes.dataIsland}]`
  );
}

```

Notez que l'attribut `data-island` est récupéré dans le code ci-dessus via `MiniIsland.attributes.dataIsland`.

Aussi, vous rappelez-vous pourquoi nous utilisons l'attribut `data-island` ?

C'est parce que nous voulons donner aux développeurs la flexibilité d'utiliser des éléments `<template>` standard à l'intérieur de notre îlot. Donc, notre îlot ne se préoccupera que des éléments `<template data-island>`.

Maintenant que nous avons récupéré le nœud de modèle via `getTemplates()`, nous allons saisir son contenu et l'hydrater.

Mettons à jour la méthode `hydrate` comme indiqué ci-dessous :

```js
// 📂 mini-island.js
// ...
hydrate() {
    /**
     * Retrieve the relevant <template> child elements of the island
     */
    const relevantChildTemplates = this.getTemplates();
    /**
     * Grab the DOM subtree within the template and replace the template with live content
     */
    this.replaceTemplates(relevantChildTemplates);
}

```

La méthode `replaceTemplates` est comme indiqué ci-dessous :

```js
// 📂 mini-island.js
// ...
 replaceTemplates(templates) {
    /**
     * Iterate over all nodes in the template list.
     * templates refer to a NodeList of templates
     * node refers to a single <template>
     */
    for (const node of templates) {
      /**
       * replace the <template> with its HTML content
       * e.g., <template><p>Hello</p></template> becomes <p>Hello</p>
       */
      node.replaceWith(node.content);
    }
  }

```

Voyez-vous ce que nous faisons ici ?

Nous saisissons le sous-arbre DOM du modèle, accédons à son contenu et supprimons l'élément `<template>`.

```html
<!-- 👀 before -->
<mini-island>
  <template>
    <p>Hello</p>
  </template>
<mini-island>

<!-- ✅ after -->
<mini-island>
  <p>Hello</p>
<mini-island>

```

Cela attachera le contenu au DOM et lancera le rendu et le chargement du script.

Avec les modèles maintenant remplacés, allons-y et changeons le fichier de démonstration initial pour contenir un exemple plus tangible, comme indiqué ci-dessous :

```js
<!-- 📂 demos/initial.html -->
<mini-island>
  <p>Hello future island</p>
  <template data-island>
    <script type="module">
      console.warn("THIS IS A WARNING FROM AN ISLAND");
    </script>
  </template>
</mini-island>

```

Notez que l'élément `<template>` a l'attribut `data-island`. C'est ainsi que nous signalons à l'îlot d'hydrater le contenu du modèle.

Maintenant, rafraîchissez votre navigateur et remarquez comment le `console.warn` est déclenché.

![Script d'îlot hydraté.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-15-at-07.10.42.png)
_Script d'îlot hydraté._

Si vous inspectez également les éléments, vous remarquerez que le `<template>` a été remplacé par son contenu enfant vivant.

![Élément <template> d'îlot remplacé.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-15-at-07.11.54.png)
_Élément &lt;template&gt; d'îlot remplacé._

Nous hydratons officiellement notre îlot !

### Comment gérer l'hydratation paresseuse via les attributs "client:"

Notre solution actuelle ne va pas nous faire gagner de prix. Dès que l'îlot est attaché au DOM, nous hydratons l'îlot. Améliorons-le en introduisant l'hydratation paresseuse.

L'hydratation paresseuse est une forme d'hydratation partielle où nous hydratons plus tard — pas immédiatement après le chargement de la page.

L'hydratation paresseuse est puissante car nous pouvons déterminer ce qui est essentiel ou prioritaire pour notre site, c'est-à-dire que nous pouvons choisir de retarder l'exécution de JavaScript sans importance.

Mettez à jour le document `initial.html` pour considérer notre premier cas d'utilisation. Voici le code mis à jour :

```html
<!-- 📂 demos/initial.html -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Initial island demo</title>

    <script type="module">
      import "../mini-island.js";
    </script>
  </head>
  <body>
    <h1>Initial island demo</h1>
	<!-- 👀 look here  -->
    <p style="padding-bottom: 100vh">Scroll down</p>
	<!-- 👀 look here  -->
    <mini-island client:visible>
      <p>Hello island</p>

      <template data-island>
        <script type="module">
          console.warn("THIS IS A WARNING FROM AN ISLAND");
        </script>
      </template>
    </mini-island>
  </body>
</html>

```

![La démo client:visible](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-15-at-07.18.38.png)
_La démo client:visible_

Nous avons maintenant un paragraphe qui lit `scroll down`, qui a un remplissage inférieur suffisamment grand pour pousser l'îlot hors de la fenêtre d'affichage.

Avec l'attribut `client:visible` sur le `<mini-island>`, nous ne devrions pas hydrater l'îlot sauf lorsqu'il est visible, c'est-à-dire lorsque l'utilisateur fait défiler pour voir l'îlot.

Cependant, testez cela dans votre navigateur.

![L'îlot est hydraté avant d'être visible.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-15-at-07.20.43.png)
_L'îlot est hydraté avant d'être visible._

Le script est hydraté avant que nous fassions défiler (dès que la page se charge), et le message `THIS IS A WARNING FROM AN ISLAND` est journalisé.

Empêchons cela de se produire.

Pour y parvenir, jetez un second coup d'œil à la méthode d'hydratation de l'îlot :

```js
  hydrate() {
    const relevantChildTemplates = this.getTemplates();
    this.replaceTemplates(relevantChildTemplates);
  }

```

Conceptuellement, nous visons à attendre que des conditions de chargement spécifiques soient remplies avant de remplacer les modèles d'îlot. Dans ce cas, nous voulons attendre que l'îlot soit visible.

En pseudo-code :

```js
  hydrate() {
     // Get island conditions, e.g., client:visible, client:idle
    // If these exist, wait for the conditions to be met before the next steps
    const relevantChildTemplates = this.getTemplates();
    this.replaceTemplates(relevantChildTemplates);
  }

```

Pour gérer nos conditions de chargement d'îlot, introduisons une nouvelle classe `Conditions` comme indiqué ci-dessous :

```js
// 📂 mini-island.js

// ...
class Conditions {

}

// same existing code ...
if ("customElements" in window) {
  window.customElements.define(MiniIsland.tagName, MiniIsland);
} else {
  console.error(
    "Island cannot be initiated because Window.customElements is unavailable."
  );
}

```

À l'intérieur de `Conditions`, nous introduirons une propriété statique qui est une représentation clé-valeur de l'attribut `client:` et des méthodes asynchrones.

![Un objet avec clé-valeur correspondant à l'attribut et à la condition de promesse.](https://blog.ohansemmanuel.com/content/images/2023/06/attr-promise.png)
_Un objet avec clé-valeur correspondant à l'attribut et à la condition de promesse._

Nos conditions seront remplies à un moment inconnu ultérieur. Nous représenterons donc celles-ci avec des fonctions asynchrones. Ces fonctions asynchrones renverront des promesses qui sont résolues lorsque la condition associée est remplie.

Voici la représentation de cela en code :

```js
// // 📂 mini-island.js
// ...
class Conditions {
  /**
   * A map of loading conditions and their respective async methods
   */
  static map = {
    idle: Conditions.waitForIdle,
    visible: Conditions.waitForVisible,
    media: Conditions.waitForMedia,
  };

  static waitForIdle() {
    return new Promise((resolve) => resolve());
  }

  static waitForVisible() {
    return new Promise((resolve) => resolve());
  }

  static waitForMedia() {
    return new Promise((resolve) => resolve());
  }
}

```

Pour le moment, les promesses se résolvent immédiatement. Mais allons-y et étoffons notre cas d'utilisation pour `client:visible`.

Tout d'abord, nous exposerons une méthode `getConditions` sur la classe `Conditions`. La méthode vérifiera si un certain nœud DOM (dans notre cas, notre `mini-island`) a un attribut sous la forme de `client:${condition}`.

Voici l'implémentation annotée :

```js
// 📂 mini-island.js

class Conditions {
 // ...
  static getConditions(node) {
    /**
     * The result variable will hold the
     * key:value representing condition:attribute.
     * e.g., For <mini-island client:visible>
     * result should be { visible: "" }
     * and for <mini-island client:media="(max-width: 400px)" />
     * result should be { media: "(max-width: 400px)" }
     */
    let result = {};

    /**
     * Loop over all keys of the static map,
     *, i.e., ["idle", "visible", "media"]
     */
    for (const condition of Object.keys(Conditions.map)) {
      /**
       * Check if the node has the attribute
       * of the form "client:${key}".
       */
      if (node.hasAttribute(`client:${condition}`)) {
        /**
         * If the node has the attribute...
         * save the condition (key) - attribute (value)
         * to the result object
         */
        result[condition] = node.getAttribute(`client:${condition}`);
      }
    }
	/** return the result */
	return result
  }
}

```

Ensuite, nous exposerons une méthode `hasConditions` responsable de vérifier si un îlot a une ou plusieurs conditions :

```js
// 📂 mini-island.js
// ...
class Conditions {
 // ...
  static hasConditions(node) {
    /**
     * Using the "getConditions" static class method, retrieve
     * a conditions attributes map
     */
    const conditionAttributesMap = Conditions.getConditions(node);

    /**
     * Check the length of the result keys to determine if there are
     * any loading conditions on the node
     */
    return Object.keys(conditionAttributesMap).length > 0;
  }
}

```

Avec `hasConditions` et `getConditions` prêts, allons-y et utilisons-les dans la méthode `hydrate` de `MiniIsland`.

Tout d'abord, voici l'état actuel de la méthode `hydrate`.

```js
// 📂 mini-island.js

class MiniIsland extends HTMLElement {
 // ...
  hydrate() {
    const relevantChildTemplates = this.getTemplates();
    this.replaceTemplates(relevantChildTemplates);
  }
 // ...
}

```

Maintenant, mettez à jour la méthode avec ce qui suit. J'ai fourni des annotations pour faciliter la compréhension.

```js
// 📂 mini-island.js

class MiniIsland extends HTMLElement {
 // ...
  async hydrate() {
    /**
     * conditions will hold an array of potential
     * promises to be resolved before hydration
     */
    const conditions = [];

    /**
     * Get the condition - attribute value map
     * NB: the argument passed to
     * `Conditions.getConditions` is the island node
     */
    let conditionAttributesMap = Conditions.getConditions(this);

    /**
     * Loop over the conditionAttributesMap variable
     */
    for (const condition in conditionAttributesMap) {
      /**
       * Grab the condition async function from the static map
       * Remember that the function that returns a promise when invoked
       */
      const conditionFn = Conditions.map[condition];

      /**
       * Check if the condition function exists
       */
      if (conditionFn) {
        /**
         * Invoke the condition function with two arguments:
         * (1) The value of the condition attribute set on the node
         * For example:
         * for <mini-island client:visible /> this is an empty string ""
         * for <mini-island client:media="(max-width: 400px)" />
         * This is the string "(max-width: 400px)"
         *
         * (2) The node, i.e., the island DOM node
         */
        const conditionPromise = conditionFn(
          conditionAttributesMap[condition],
          this
        );

        /**
         * append the promise to the conditions array
         */

        conditions.push(conditionPromise);
      }

      /**
       * Await all promise conditions to be
       * resolved before replacing the template nodes
       */
      await Promise.all(conditions);
      /**
       * Retrieve the relevant <template> child elements of the island
       */
      const relevantChildTemplates = this.getTemplates();
      /**
       * Grab the DOM subtree in the template
       * and replace the template with live content
       */
      this.replaceTemplates(relevantChildTemplates);
    }
  }
}

```

Pour le moment, rappelez-vous que nos promesses de condition dans `Conditions` se résolvent immédiatement.

Avant de tester notre solution, nous devons satisfaire la condition pour l'attribut `client:visible`.

Comment nous assurons-nous que l'îlot est visible ?

La meilleure solution ici est d'utiliser l'API `IntersectionObserver`. Profitons-en comme indiqué ci-dessous :

```js
// 📂 mini-island.js

class Conditions {
 // ...
   /**
   *
   * @param noop - the value of the condition attribute.
   * This is named "noop" as it is not relevant in this condition, i.e.,
   * as per our API, client:visible always has a falsy attribute value, e.g.,
   * ✅ <mini-island client:visible />
   * ❌ <mini-island client:visible={some-value} />
   * @param el - the node element.
   * This represents our island DOM node passed during hydration
   * @returns - a Promise that resolves when "el" is visible
   * NB: relies on the Intersection Observer API
   */
  static waitForVisible(noop, el) {
    /**
     * If the Intersection Observer API is not available,
     * go ahead and exit immediately.
     */
    if (!("IntersectionObserver" in window)) {
      return;
    }

    /**
     * Otherwise, set up a new Promise that is resolved when the
     * node parameter (our island DOM node) is visible
     */
    return new Promise((resolve) => {
      let observer = new IntersectionObserver((entries) => {
        let [entry] = entries;

        /**
         * is it visible?
         */
        if (entry.isIntersecting) {
          /**
           * remove observer
           */
          observer.unobserve(entry.target);
          /**
           * resolve promise
           */
          resolve();
        }
      });

      /**
       * set up the observer on the "el" argument
       */
      observer.observe(el);
    });
  }
}

```

C'est un excellent travail !

Revenez à l'application de démonstration `initial.html` en cours d'exécution dans votre navigateur, rafraîchissez, et remarquez comment l'îlot se comporte.

L'îlot n'est plus hydraté jusqu'à ce que nous fassions défiler vers le bas et que l'îlot soit visible 🎉

Bien joué, mon pote ! Applaudissez-vous et prenez une tasse de thé. Nous avons tout déchiré. Faites une pause si vous en avez besoin, et passons à la prochaine série d'exigences quand vous serez prêt.

### Comment prendre en charge les conditions `client:idle` et `client:media`

Nous avons une solution assez robuste dans la méthode `hydrate`. Donc, pour prendre en charge plus de conditions de chargement, nous devons étoffer les autres promesses de condition.

#### waitForIdle

Faites une pause et réfléchissez à la façon dont nous devrions faire cela. Par exemple, sur quelle heuristique nous appuyons-nous pour déterminer quand le navigateur est "inactif" (idle) ?

Cela soulève la question, qu'est-ce qui est "inactif" dans ce cas ?

Eh bien, pour notre implémentation, la définition d'inactif est lorsque le navigateur ne charge activement aucune ressource, et qu'aucun événement critique pour la latence, tel que l'animation et les réponses d'entrée, n'est en cours.

Pour y parvenir, nous nous appuierons sur deux propriétés :

(i) L'événement `document.readyState`

Si la valeur de cet événement est `complete`, le document et toutes les sous-ressources ont fini de charger. Cela inclut toutes les ressources dépendantes telles que les feuilles de style, les scripts, les iframes et les images.

Écouter cet événement garantit que nous hydratons l'îlot lorsque tous les autres actifs essentiels ont été téléchargés.

(ii) La méthode `window.requestIdleCallback()`

Par définition, la méthode `window.requestIdleCallback()` mettra en file d'attente une fonction à appeler lorsqu'un navigateur est inactif. Cela garantit que la fonction n'est exécutée que lorsque le navigateur ne gère aucun événement critique pour la latence.

Mettons cela ensemble et créons une promesse qui se résout lorsque l'événement `document.readyState` est `complete`, et qu'aucun événement critique pour la latence n'est géré.

Voici l'implémentation ci-dessous :

```js
// 📂 mini-island.js
// ...
class Conditions {
 // ...
 static waitForIdle() {
    const onLoad = new Promise((resolve) => {
      /**
       * The document.readyState property
       * describes the loading state of the document.
       */
      if (document.readyState !== "complete") {
        /**
         * Set up an event listener for the "load" event.
         * The load event is fired when the whole page
		 * has loaded, including all dependent resources
		 * such as stylesheets, scripts, iframes, and
		 * images.
         */
        window.addEventListener(
          "load",
          () => {
            /**
             * resolve this promise once the "load" event is fired.
             */
            resolve();
          },
          /**
           * Remove the listener after the first
		   * invocation of the "load" event.
           */
          { once: true }
        );
      } else {
        resolve();
      }
    });

    /**
     * The window.requestIdleCallback() method queues a
     * function to be called during a browser's idle periods.
     * This enables developers to perform background
     * and low-priority work on the main event loop
     */

    const onIdle = new Promise((resolve) => {
      /**
       * Check for "requestIdleCallback" support
       */
      if ("requestIdleCallback" in window) {
        requestIdleCallback(() => {
          /**
           * pass the promise resolve function
		   * as the operation to be queued
           */
          resolve();
        });
      } else {
        /**
         * resolve the promise immediately
         * if requestIdleCallback isn't supported
         */
        resolve();
      }
    });

    /**
     * waitForIdle will wait for both
     * promises to be resolved, i.e., onIdle and onLoad
     */
    return Promise.all([onIdle, onLoad]);
  }
}

```

Maintenant, allez au fichier de démonstration `initial.html` et mettez à jour le fichier comme indiqué ci-dessous :

```html
<!-- 📂 demos/initial.html -->
<!DOCTYPE html>
<html lang="en">
  <!-- ... -->
  <!-- content unchanged -->
  <body>
    <h1>Initial island demo</h1>
    <img
      src="https://raw.githubusercontent.com/ohansemmanuel/larder/main/large_image.jpeg"
      alt="34MB large satellite image from Effigis."
    />

    <mini-island client:idle>
      <p>Hello island</p>

      <template data-island>
        <script type="module">
          console.warn("THIS IS A WARNING FROM AN ISLAND");
        </script>
      </template>
    </mini-island>
  </body>
</html>

```

Notez que nous avons introduit une grande image de `34MB` de [Effigis](https://effigis.com/en/solutions/satellite-images/satellite-image-samples/) et passé un attribut `client:idle` à `<mini-island>`.

Astuce : envisagez de télécharger la grande image et de la référencer localement au lieu de frapper les serveurs GitHub à plusieurs reprises.

La grande image occupera le navigateur pendant un certain temps. Avant de tester cela dans le navigateur, je suggère de désactiver le cache du navigateur via les outils de développement.

![La propriété de désactivation du cache dans Firefox.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-15-at-11.43.31.png)
_La propriété de désactivation du cache dans Firefox._

Ouvrez la page dans le navigateur et remarquez comment le script n'est pas invoqué tant que le navigateur n'a pas fini de charger la grande image et n'est pas dans un état inactif.

C'est génial !

Au lieu de permettre potentiellement au code JavaScript non prioritaire de rivaliser pour les ressources du navigateur, nous avons mis cela de côté pour être initialisé plus tard pendant la période d'inactivité du navigateur.

#### waitForMedia

La condition média est fascinante. L'îlot n'est hydraté que lorsqu'une requête média CSS est remplie. Ceci est utile pour les bascules mobiles ou d'autres éléments uniquement visibles sur des tailles d'écran spécifiques.

Nous exploiterons `window.matchMedia()` pour déterminer si le document correspond à la chaîne de requête média.

Voici l'implémentation annotée :

```js
// 📂 mini-island.js
// ...
class Conditions {
/**
   *
   * @param {*} query - the query string
   * passed to the client:media attribute
   * @returns Promise that resolves when
   * the document matches the passed CSS media query
   */
  static waitForMedia(query) {
    /**
     * window.matchMedia(query) returns A MediaQueryList object.
     * This object stores information on a media query
     * applied to a document and one of the properties
     * on this object is "matches" - a boolean for
     * whether the document matches the media query or not.
     * Create a new simple object of similar form, i.e.,
     * with a "matches" property
     */
    let queryList = {
      matches: true,
    };

    if (query && "matchMedia" in window) {
     /**
       Override our stub with the actual query list
     */
      queryList = window.matchMedia(query);
    }

    /**
     * If matchMedia isn't supported or the
     * query is truthy, return immediately
     * e.g., truthy if matchMedia isn't in the window object
     */
    if (queryList.matches) {
      return;
    }

    return new Promise((resolve) => {
      /**
       * Set a new listener on the queryList object
       * and resolve the promise when there's a match
       */
      queryList.addListener((e) => {
        if (e.matches) {
          resolve();
        }
      });
    });
  }
}

```

Avec cela en place, nous pouvons mettre à jour le fichier de démonstration `initial.html` comme suit :

```html
<!DOCTYPE html>
<html lang="en">
  <!-- content remains the same -->
  <body>
    <h1>Initial island demo</h1>

    <mini-island client:media="(max-width: 400px)">
      <p>Hello island</p>

      <template data-island>
        <script type="module">
          console.warn("THIS IS A WARNING FROM AN ISLAND");
        </script>
      </template>
    </mini-island>
  </body>
</html>

```

Maintenant, rafraîchissez la page dans votre navigateur et remarquez comment le script n'est jamais initialisé jusqu'à ce que vous redimensionniez la fenêtre de votre navigateur pour correspondre à la requête CSS, c'est-à-dire une largeur maximale de `400px`.

### Comment prendre en charge les frameworks : Vue, Petite-vue et Preact

Notre implémentation `<mini-island>` est simple mais efficace. Mais vous ne l'apprécierez peut-être pas tant que vous ne l'aurez pas vue utilisée avec d'autres frameworks. Par coïncidence, cela fait également partie de nos objectifs – développer une solution agnostique au framework.

Les sections suivantes montrent des exemples de frameworks utilisant `<mini-island>`. Pour ce faire, nous construirons la même interface utilisateur de framework sous la forme d'un simple compteur.

#### Vue

Vue est un framework JavaScript pour construire des interfaces utilisateur. Le modèle mental de Vue s'appuie sur le HTML, CSS et JavaScript standard, ce qui le rend facile à comprendre pour la plupart des gens.

Comme on peut s'y attendre d'un framework UI moderne, Vue est déclaratif et réactif.

Allons-y et construisons une application de compteur exploitant Vue et `<mini-island>` comme indiqué ci-dessous :

```html
<!-- 📂 demos/vue.html -->

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vue mini-island demo</title>

    <script type="module">
      import "../mini-island.js";
    </script>
  </head>
  <body>
    <h1>Vue</h1>
    <mark>This is a vue counter </mark>

    <p>
      By default, this button does not load any Javascript and isn't hydrated.
    </p>

    <p>
      Resize your browser to match the media query:
      <code>(max-width: 400px)</code> to hydrate the island
    </p>

    <mini-island client:media="(max-width: 400px)">
      <div id="vue-app">
        <button @click="count++">
          <span>⬆️</span>

          <div>
            <strong>Vue</strong>
            <div>
              <span v-html="count">0</span>
              <span>-</span>
              <span>clicks</span>
            </div>
          </div>
        </button>
      </div>

      <template data-island>
        <script type="module">
          import { createApp } from "https://unpkg.com/vue@3.2.36/dist/vue.esm-browser.prod.js";

          createApp({
            data: () => ({ count: 0 }),
          }).mount("#vue-app");
        </script>
      </template>
    </mini-island>
  </body>
</html>

```

Ce n'est pas grave si vous ne comprenez pas les extraits de code Vue. Ce qui est important est ce qui suit :

*   Le balisage HTML est rendu dès que la page HTML est chargée et analysée.
*   Cela inclut le balisage de compteur statique à l'intérieur de `mini-island`, c'est-à-dire :
    `<div id="vue-app">`
    `<button @click="count++">`
    `<span>⬆️</span>`
    ``
    `<div>`
    `<strong>Vue</strong>`
    `<div>`
    `<span v-html="count">0</span>`
    `<span>-</span>`
    `<span>clicks</span>`
    `</div>`
    `</div>`
    `</button>`
    `</div>`
*   Mais le compteur n'est pas hydraté à ce stade. Donc, cliquer sur le compteur n'augmentera pas le compte. C'est parce que Vue n'a pas été chargé, et le bouton de compteur n'est pas encore hydraté.
*   Considérez la condition de chargement définie sur l'îlot, c'est-à-dire `client:media="(max-width: 400px)"`.
*   Maintenant, redimensionnez votre navigateur (profitez des outils de développement) à une largeur inférieure à `400px` pour hydrater l'îlot.
*   Cela importera Vue et hydratera le compteur. Voici le code responsable à l'intérieur du `template` de l'îlot :
    `<template data-island>`
    `<script type="module">`
    `import { createApp } from "https://unpkg.com/vue@3.2.36/dist/vue.esm-browser.prod.js";`
    ``
    `createApp({`
    `data: () => ({ count: 0 }),`
    `}).mount("#vue-app");`
    `</script>`
    `</template>`
*   Le compteur devrait maintenant être hydraté. Nous pouvons maintenant cliquer à notre guise.

#### Petite-vue

D'après la [documentation](https://vuejs.org/guide/extras/ways-of-using-vue.html#standalone-script) officielle de Vue, Vue fournit également une distribution alternative appelée petite-vue qui est optimisée pour améliorer progressivement le HTML existant.

C'est parfait pour notre cas d'utilisation.

Allons-y et créons une démo similaire en utilisant `petite-vue` comme indiqué ci-dessous :

```html
<!-- 📂 demos/petite-vue.html -->

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vue mini-island demo</title>

    <script type="module">
      import "../mini-island.js";
    </script>
  </head>
  <body>
    <h1>Petite-vue</h1>
    <mark>This is a petite-vue counter </mark>

    <p>
      By default, this button does not load any Javascript and isn't hydrated.
    </p>

    <p>
      Resize your browser to match the media query:
      <code>(max-width: 400px)</code> to hydrate the island
    </p>

    <mini-island client:media="(max-width: 400px)">
      <div id="vue-app" v-scope="{ count: 0 }">
        <button @click="count++">
          <span>⬆️</span>

          <div>
            <strong>Petite-vue</strong>
            <div>
              <span v-html="count">0</span>
              <span>-</span>
              <span>clicks</span>
            </div>
          </div>
        </button>
      </div>

      <template data-island>
        <script type="module">
          import { createApp } from "https://unpkg.com/petite-vue@0.4.1/dist/petite-vue.es.js";

          createApp().mount("#vue-app");
        </script>
      </template>
    </mini-island>
  </body>
</html>


```

À part quelques changements, le code ci-dessus est identique à l'API Vue standard.

Voici comment cela fonctionne :

*   Le balisage HTML est rendu dès que la page HTML est chargée et analysée.
*   Cela inclut le balisage de compteur statique à l'intérieur de `mini-island`, c'est-à-dire :
    `<div id="vue-app" v-scope="{ count: 0 }">`
    `<button @click="count++">`
    `<span>⬆️</span>`
    ``
    `<div>`
    `<strong>Vue</strong>`
    `<div>`
    `<span v-html="count">0</span>`
    `<span>-</span>`
    `<span>clicks</span>`
    `</div>`
    `</div>`
    `</button>`
    `</div>`
*   NB : la différence significative dans le code ci-dessus est l'introduction de l'attribut `v-scope` pour contenir notre variable de données de comptage.
*   Le compteur, cependant, n'est pas hydraté à ce stade. Donc, cliquer sur le compteur n'augmentera pas le compte. C'est parce que petite-vue n'a pas été chargé, et le bouton de compteur n'est pas encore hydraté.
*   Considérez la condition de chargement définie sur l'îlot, c'est-à-dire `client:media="(max-width: 400px)"`
*   Maintenant, redimensionnez votre navigateur (utilisez les outils de développement) à une largeur inférieure à `400px` pour hydrater l'îlot.
*   Cela importera Petite-vue et hydratera le compteur. Voici le code responsable à l'intérieur du `template` de l'îlot :
    `<template data-island>`
    `<script type="module">`
    `import { createApp } from "https://unpkg.com/petite-vue@0.4.1/dist/petite-vue.es.js";`
    ``
    `createApp().mount("#vue-app");`
    `</script>`
    `</template>`
*   Le compteur devrait maintenant être hydraté. Nous pouvons maintenant cliquer à notre guise.

#### Preact

Preact est une alternative rapide de 3 Ko à React avec la même API moderne, et il peut être utilisé dans le navigateur sans aucune étape de transpiration.

Allons-y et créons une démo similaire en utilisant Preact, comme indiqué ci-dessous :

```html
<!-- 📂 demos/preact.html -->

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Preact mini-island demo</title>

    <script type="module">
      import "../mini-island.js";
    </script>
  </head>

  <body>
    <h1>Preact</h1>
    <p>This is a preact counter</p>

    <p>By default, this button is not rendered or hydrated</p>

    <mini-island client:idle>
      <div id="preact-app">
        <mark
          >The counter island will be rendered and hydrated just above this mark
          when the browser is idle</mark
        >
      </div>

      <template data-island>
        <script type="module">
          import { h, Component, render } from "https://esm.sh/preact";
          import { useState } from "https://esm.sh/preact/hooks";
          import htm from "https://esm.sh/htm";

          // Initialize htm with Preact
          const html = htm.bind(h);

          function App(props) {
            const [count, setCount] = useState(0);

            const increment = () =>
              setCount((currentCount) => currentCount + 1);

            return html`<div>
              <button onClick=${() => increment()}>
                <span>⬆️ </span>

                <div>
                  <strong>Preact</strong>
                  <div>
                    <span>${count}</span>
                    <span>-</span>
                    <span>clicks</span>
                  </div>
                </div>
              </button>
            </div>`;
          }

          render(html`<${App} />`, document.getElementById("preact-app"));
        </script>
      </template>
    </mini-island>

    <ul>
      <li>The document must be completely loaded</li>
      <li>The large image below must complete loading</li>
    </ul>

    <img
      src="https://raw.githubusercontent.com/ohansemmanuel/larder/main/large_image.jpeg"
      alt="34MB large satellite image from Effigis."
    />
  </body>
</html>

```

Le code ci-dessus se comporte différemment des exemples de framework précédents.

Voici comment cela fonctionne :

*   Le balisage HTML est rendu après le chargement et l'analyse du HTML.
*   Le compteur, cependant, n'est pas rendu ni hydraté. C'est parce que `mini-island` a une condition de chargement `client: idle`.
*   Le compteur sera rendu et hydraté lorsque le navigateur sera inactif. Pour que ce soit le cas, la grande image dans le document doit finir de charger.
*   Une fois que cela est chargé (y compris d'autres ressources documentaires associées), Preact rend et hydrate le compteur lorsque le navigateur est inactif.
*   Le compteur devrait maintenant être hydraté ; nous pouvons maintenant cliquer à notre guise.

## Conclusion de ce chapitre

Lorsqu'il s'agit de performance et de décider quelle solution de rendu fonctionne pour votre application, aucune solution unique ne convient à toutes les applications.

Selon l'application, nous devons toujours faire des compromis. Mais l'architecture des îlots fournit des applications clientes très performantes sans sacrifier une riche interactivité.

L'objectif principal de ce chapitre était de retirer la couche perçue de complexité et de dépouiller les îlots de composants jusqu'à une unité fondamentale digestible avec `<mini-island>`.

Maintenant, nous allons emporter ces connaissances pour explorer les îlots de composants dans Astro, et (presque) rien ne vous surprendra. C'est la définition d'une bonne compréhension.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-136.png)
_Chapitre quatre._

# Chapitre 4 : La vie secrète des îlots de composants Astro

Les îlots de composants sont le secret du récit super rapide d'Astro. Il est temps de tout apprendre à leur sujet.

## Ce que vous apprendrez

*   Expérience pratique de travail avec des composants de framework dans Astro.
*   L'hydratation responsable et pourquoi elle est importante.
*   Comment les îlots de composants fonctionnent dans Astro.
*   Pourquoi les îlots sont essentiels.

## Comment fonctionnent les îlots dans Astro

Supposons que nous ayons une application Astro avec du contenu statique : une barre de navigation, du contenu principal, un pied de page et un volet latéral.

![Une structure de page astro statique](https://blog.ohansemmanuel.com/content/images/2023/06/a-6.png)
_Une structure de page astro statique_

Si nous devons introduire du contenu interactif dans le volet latéral de l'application, comment pourrions-nous y parvenir ?

![Ajouter du contenu interactif à la page statique](https://blog.ohansemmanuel.com/content/images/2023/06/b-1.png)
_Ajouter du contenu interactif à la page statique_

Astro fournit les moyens suivants pour ce faire :

*   Nous avons vu comment cela fonctionne : introduisez un élément `<script>` pour gérer l'interactivité au sein de votre composant Astro.
*   Utilisez un composant de framework pris en charge, et tirez parti d'un îlot de composants.

La deuxième option est le sujet de ce chapitre.

Au moment de la rédaction, Astro vous permet d'utiliser des composants construits avec `React`, `Preact`, `Svelte`, `Vue`, `SolidJS`, `AlpineJS` ou `Lit` dans vos composants Astro. À l'avenir, je ferai référence à ceux-ci comme **composants de framework**.

![Exploiter les composants de framework dans Astro.](https://blog.ohansemmanuel.com/content/images/2023/06/framework-components.png)
_Exploiter les composants de framework dans Astro._

Alors, pourquoi utiliserions-nous des composants de framework et ne fournirions-nous pas simplement un support natif via un élément `<script>` ?

Il serait préférable de s'en tenir à un élément `<script>` dans les cas où vous pouvez vous en sortir avec du JavaScript ou TypeScript vanilla. Mais il y a des cas où nous pouvons privilégier un composant de framework. Par exemple :

*   **Systèmes de design** : utiliser un système de design préexistant dans un projet Astro peut faire gagner du temps, selon le cas d'utilisation. Cela aide également à garder toutes vos applications avec la même apparence et la même sensation.
*   **Open-source** : nous pourrions envisager d'utiliser un composant de framework open-source riche en fonctionnalités existant déjà au lieu de construire un composant hautement interactif à partir de zéro. De cette façon, nous pouvons facilement utiliser un composant de framework open-source dans Astro.
*   **Facilité de développement** : nous pouvons trouver la construction d'interfaces utilisateur avec état plus riches plus facile, plus gérable et plus rapide à implémenter via des composants de framework que le JavaScript / TypeScript vanilla fourni dans `<script>`.

Pour utiliser un composant de framework dans Astro, nous exploitons les îlots de composants.

Revenons à notre exemple d'application.

En supposant que nous ayons pesé le pour et le contre et décidé d'introduire un composant de framework, la section suivante met en évidence les étapes à suivre.

### Étape 1 : Construire un site Astro

Nous ne pouvons pas utiliser de composants de framework sans avoir un site Astro dans lequel les utiliser.

Nous avons déjà vu comment construire des sites statiques avec Astro, donc créer un nouveau projet statique n'est pas nécessaire. Au lieu de cela, commençons un nouveau projet Astro avec un projet que j'ai préparé.

Clonez le projet :

```bash
git clone https://github.com/understanding-astro/astro-islands-visual-example.git

```

Ensuite, installez les dépendances et démarrez l'application via ce qui suit :

```bash
npm install
npm run start

```

Cela exécutera le projet sur l'un de vos ports locaux.

![Le projet d'exemple visuel des îlots astro](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-03-11-at-14.06.52@2x.png)
_Le projet d'exemple visuel des îlots astro_

Le projet prend la même forme que notre exemple hypothétique — il a une navigation, un contenu principal, un pied de page et un volet latéral.

![Une structure de page astro statique](https://blog.ohansemmanuel.com/content/images/2023/06/a-1-1.png)
_Une structure de page astro statique_

Dans le volet latéral, il y a un `slot` pour rendre notre contenu interactif via un composant de framework.

Dans `src/pages/index.astro`, vous trouverez le code responsable du rendu de la page comme indiqué ci-dessous :

```js
// 📂 src/pages/index.astro
---
import DefaultIslandLayout from "../layouts/DefaultIslandLayout.astro";
---

<DefaultIslandLayout />

```

`DefaultIslandLayout` fournit la mise en page pour toute la page et inclut un `slot` pour rendre tous les éléments enfants qui lui sont passés. Initialisez le projet localement et jetez un coup d'œil.

### Étape 2 : Installer l'intégration du framework

Astro fournit des intégrations officielles pour les composants de framework pris en charge. Dans cet exemple, nous utiliserons le framework `react`.

Il est important de noter que les étapes décrites ici sont les mêmes quel que soit le composant de framework de votre choix. Par conséquent, je m'en tiens à `react` car beaucoup plus de développeurs l'utilisent sans doute.

Le moyen le plus pratique d'ajouter votre intégration de framework est d'utiliser la commande `astro add`, par exemple pour ajouter `react`, exécutez les commandes suivantes :

```bash
# using NPM
npx astro add react
# Using Yarn
yarn astro add react
# Using PNPM
pnpm astro add react

```

Cela ajoutera automatiquement les dépendances de framework pertinentes à notre projet.

![Exécuter astro add react.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-03-11-at-14.56.20@2x.png)
_Exécuter astro add react._

La commande mettra également automatiquement à jour notre configuration de projet, `astro.config.mjs`, pour inclure l'intégration du framework.

![Mettre à jour le fichier de configuration du projet.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-03-11-at-14.57.00@2x.png)
_Mettre à jour le fichier de configuration du projet._

Essentiellement, cela décompose l'installation d'un framework dans notre projet Astro en deux processus distincts :

1.  Installer les dépendances du framework.
2.  Ajouter l'intégration du framework pertinente dans le fichier de configuration du projet.

Si nous n'utilisions pas la commande `Astro add`, nous pourrions obtenir les mêmes résultats manuellement en installant les dépendances du framework et en ajoutant l'intégration du framework dans notre fichier de configuration de projet.

### Étape 3 : Écrire le composant de framework

Notre composant de framework sera un compteur glorifié. En supposant que la page consiste en un article qu'un lecteur peut voter positivement, nous construirons un bouton de vote positif.

![Le compteur de vote positif illustré.](https://blog.ohansemmanuel.com/content/images/2023/06/upvote-counter.png)
_Le compteur de vote positif illustré._

Voici le composant React `UpvoteContent` annoté :

```js
<!-- 📂 src/components/UpvoteContent.tsx -->

import { useState } from "react";

// The maximum number of upvotes available
const MAX_COUNT = 50;

export const UpvoteContent = () => {
  // the initial state of the upvote counter
  const [upvoteCount, setUpvoteCount] = useState(0);

  return (
    <div>
      <button
       // update state when a user clicks the counter. check if
       //The maximum count value was reached first.
        onClick={() => {
          setUpvoteCount((prevCount) =>
            prevCount < MAX_COUNT ? prevCount + 1 : prevCount
          );
        }}
      >
       { /** Upvote counter SVG icon. shortened for brevity **/}
        <svg />
        Upvote
      </button>

      <div>
        <div>{`${upvoteCount} upvotes`}</div>

		{/** show a growing visual bar based on the upvote count **/}
        <div
          style={{
            width: `${upvoteCount}%`,
          }}
        />

		{/** show a warning if the maximum count has been reached**/}
        {upvoteCount === MAX_COUNT && (
          <div>
            Max upvote reached
          </div>
        )}
      </div>
    </div>
  );
};


```

Ne vous inquiétez pas si vous ne comprenez pas `react`. L'objectif ici est de savoir comment travailler avec des composants de framework dans Astro. Nous pourrions construire le même composant en utilisant n'importe quel autre framework de notre choix, comme Vue ou Svelte.

### Étape 4 : Rendre le composant de framework

Allons-y et rendons le composant de framework comme indiqué ci-dessous :

```js
<!-- 📂 src/pages/none.astro -->
---
import { UpvoteContent } from "../components/UpvoteContent.jsx";
import DefaultIslandLayout from "../layouts/DefaultIslandLayout.astro";
---

<DefaultIslandLayout>
  <UpvoteContent />
</DefaultIslandLayout>

```

*   Créez une nouvelle page dans `src/pages/none.astro`
*   Rendez le composant `UpvoteContent` comme un enfant de `DefaultIslandLayout`, c'est-à-dire :
    `<DefaultIslandLayout>`
    `<UpvoteContent />`
    `</DefaultIslandLayout>`
*   `DefaultIslandLayout` prend le composant enfant `UpvoteContent` et le rend dans son slot de mise en page.

Maintenant, ouvrez la page `/none` dans le navigateur, et nous devrions avoir le composant `UpvoteContent` rendu.

![Rendre le composant de framework.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-03-13-at-12.59.52@2x.png)
_Rendre le composant de framework._

Le compteur de vote positif est rendu avec succès, mais cliquer sur le bouton n'augmente pas le compte !

Que se passe-t-il ? 🥹

#### Ce n'est pas un bug. C'est une fonctionnalité.

Par défaut, lorsque vous rendez un composant de framework, Astro le rend automatiquement en HTML à l'avance, c'est-à-dire qu'Astro supprime tout le JavaScript du composant.

Essentiellement, vous n'obtenez aucune interactivité des composants de framework par défaut.

![Si Astro lançait une campagne Twitter, #NoJavscriptByDefault ferait un excellent hashtag.](https://blog.ohansemmanuel.com/content/images/2023/06/no-js-by-default.png)
_Si Astro lançait une campagne Twitter, #NoJavscriptByDefault ferait un excellent hashtag._

En l'état, ce que nous avons actuellement n'est techniquement pas un îlot. Nous avons le balisage du composant rendu sans interactivité.

## Hydratation responsable

Astro vous aide à minimiser le gonflement JavaScript lors de l'utilisation de composants de framework en tirant parti de l'hydratation responsable.

Si Astro rend votre composant de framework à `100%` HTML, comment hydratez-vous (rendez interactif) le composant de framework ?

Dans le contexte du développement Astro, l'hydratation responsable fait référence au fait qu'Astro ne prend aucune décision sur le moment d'hydrater votre composant de framework et laisse cette décision entièrement au développeur.

C'est puissant mais cela vient avec le fardeau de la décision reposant sur nous — les développeurs.

Lorsque des décisions techniques comme celle-ci doivent être prises, elles doivent être prises en fonction d'exigences spécifiques. Dans ce cas, la décision réside dans l'évaluation de deux critères, à savoir la **priorité** et l'**interactivité**.

*   Priorité : est-ce un élément d'interface utilisateur à haute ou basse priorité ?
*   Interactivité : cet élément doit-il être interactif dès que possible ?

Nous pouvons représenter cela sur un plan 2d comme suit :

![Représenter la priorité et l'interactivité sur un plan 2d.](https://blog.ohansemmanuel.com/content/images/2023/06/hydration-plane.png)
_Représenter la priorité et l'interactivité sur un plan 2d._

Il y a quatre attributs que vous pouvez passer à votre composant de framework rendu, par exemple :

```js
<ReactComponent attribute />

```

Ces attributs sont appelés directives client (ou, plus génériquement, directives de template). Voici les cinq directives client qui contrôlent l'hydratation de votre composant de framework :

*   `client:load`
*   `client:only`
*   `client:visible`
*   `client:media`
*   `client:idle`

![Représenter les directives de template client sur un plan priorité - interactivité.](https://blog.ohansemmanuel.com/content/images/2023/06/responsible-hydration-astro-plane.png)
_Représenter les directives de template client sur un plan priorité - interactivité._

### `client:load`

`client:load` doit être utilisé pour les éléments d'interface à haute priorité qui doivent être interactifs dès que possible.

*   Priorité : haute
*   Interactivité : haute

Nous pouvons aller de l'avant et rendre notre composant `UpvoteContent` comme indiqué ci-dessous :

```js
// 📂 src/pages/index.astro
---
import { UpvoteContent } from "../components/UpvoteContent.jsx";
import DefaultIslandLayout from "../layouts/DefaultIslandLayout.astro";
---

<DefaultIslandLayout>
  <UpvoteContent client:load />
</DefaultIslandLayout>

```

Voici les étapes d'hydratation :

1.  Rendre le HTML du composant (non hydraté).
2.  Attendre que la page se charge.
3.  Charger le JavaScript du composant.
4.  Hydrater le composant.

L'événement load est déclenché lorsque la page a chargé, y compris toutes les ressources dépendantes telles que les feuilles de style, les scripts, les iframes et les images.

Il est important de noter que cliquer sur le bouton de vote positif ne déclenchera aucun vote positif avant l'hydratation.

### `client:only`

`client:only` se comporte de manière similaire à `client:load`. Il doit être utilisé pour les éléments où vous voulez sauter le rendu côté serveur (le composant ne sera pas initialement rendu en HTML) mais le rendre interactif dès qu'il est montré à l'utilisateur sur le client.

*   Priorité : moyenne (nous sommes d'accord pour ne pas montrer le HTML initial du composant)
*   Interactivité : haute (dès qu'il est montré à l'utilisateur)

Nous pouvons aller de l'avant et rendre notre composant `UpvoteContent` comme indiqué ci-dessous :

```js
// 📂 src/pages/index.astro
---
import { UpvoteContent } from "../components/UpvoteContent.jsx";
import DefaultIslandLayout from "../layouts/DefaultIslandLayout.astro";
---

<DefaultIslandLayout>
  <UpvoteContent client:only="react" />
</DefaultIslandLayout>

```

Il est essentiel de passer le nom du framework comme indiqué ci-dessus. Sinon, Astro ne sait pas quel JavaScript de framework charger. C'est parce que cela n'est pas déterminé sur le serveur.

```js
<ReactComponent client:only="react" />
<PreactComponent client:only="preact" />
<SvelteComponent client:only="svelte" />
<VueComponent client:only="vue" />
<SolidComponent client:only="solid-js" />

```

Voici les étapes d'hydratation :

1.  Ne pas rendre le HTML du composant.
2.  Attendre que la page se charge.
3.  Charger le JavaScript du composant.
4.  Hydrater le composant.

La différence entre `client:only` et `client:load` est de savoir s'il faut rendre un HTML de composant statique avant que l'élément ne soit interactif. `client:only` est particulièrement pratique lors du rendu de composants nécessitant des API client (navigateur).

### `client:visible`

`client:visible` doit être utilisé pour les éléments d'interface à basse priorité sous la ligne de flottaison (loin en bas de la page) ou gourmands en ressources. Vous ne voulez pas les charger si l'utilisateur ne voit jamais le composant.

*   Priorité : basse
*   Interactivité : basse

Nous pouvons aller de l'avant et rendre notre composant `UpvoteContent` comme indiqué ci-dessous :

```js
// 📂 src/pages/index.astro
---
import LargeMainContentLayout from "../layouts/LargeMainContentLayout.astro";
import { UpvoteContent } from "../components/UpvoteContent.jsx";
---

<LargeMainContentLayout>
  <UpvoteContent client:visible />
</LargeMainContentLayout>

```

Notez que j'importe une mise en page `LargeMainContentLayout` différente dans le bloc de code ci-dessus. La mise en page est responsable de pousser l'îlot hors de la fenêtre d'affichage initiale.

Voici les étapes d'hydratation :

1.  Rendre le HTML du composant.
2.  Attendre que l'élément soit visible (utilise `IntersectionObserver`).
3.  Charger le JavaScript du composant.
4.  Hydrater le composant.

### `client:media`

`client:media` doit être utilisé pour les éléments d'interface à basse priorité uniquement visibles sur des tailles d'écran spécifiques, par exemple les bascules de barre latérale.

*   Priorité : basse
*   Interactivité : basse

Nous pouvons aller de l'avant et rendre notre composant `UpvoteContent` comme indiqué ci-dessous :

```js
// 📂 src/pages/index.astro
---
import { UpvoteContent } from "../components/UpvoteContent.jsx";
import DefaultIslandLayout from "../layouts/DefaultIslandLayout.astro";
---

<DefaultIslandLayout>
  <UpvoteContent client:media="(max-width: 30em)" />
</DefaultIslandLayout>

```

Voici les étapes d'hydratation :

1.  Rendre le HTML du composant
2.  Vérifier si la requête média correspond
3.  Charger le JavaScript du composant
4.  Hydrater le composant

### `client:idle`

`client:idle` doit être utilisé pour les éléments d'interface à basse priorité qui n'ont pas besoin d'être immédiatement interactifs.

*   Priorité : moyenne
*   Interactivité : moyenne

Nous pouvons aller de l'avant et rendre notre composant `UpvoteContent` comme indiqué ci-dessous :

```js
// 📂 src/pages/index.astro
---
import { UpvoteContent } from "../components/UpvoteContent.jsx";
import DefaultIslandLayout from "../layouts/DefaultIslandLayout.astro";
---

<DefaultIslandLayout>
  <UpvoteContent client:idle />
</DefaultIslandLayout>

```

Voici l'étape d'hydratation visualisée :

1.  Rendre le HTML du composant.
2.  Attendre que la page se charge.
3.  Attendre que l'événement `requestIdleCallback` soit déclenché. Si `requestIdleCallback` n'est pas pris en charge, utilisez uniquement l'événement `load` du document.
4.  Charger le JavaScript du composant.
5.  Hydrater le composant.

## Comment utiliser plusieurs frameworks

Théoriquement, nous pouvons utiliser plusieurs composants de framework dans une application Astro. C'est une fonctionnalité puissante, mais elle ne doit pas être abusée.

Cela permet de faire des démos puissantes de ce qui est possible avec Astro. Mais il n'y a que quelques cas réels où nous pourrions vouloir faire cela, comme composer des micro-frontends autonomes sur une page Astro.

Dans un composant Astro, ce qui suit est valide :

```js
---
 // import different framework components
 import SpecialReactComponent from '../components/
SpecialReactComponent.jsx'

 import SpecialVueComponent from '../components/
SpecialVueComponent.jsx'


import SpecialSvelteComponent from '../components/
SpecialSvelteComponent.jsx'
---

<!-- render the components -->
<SpecialReactComponent client:load/>
<SpecialVueComponent client:idle/>
<SpecialSvelteComponent client:load/>

```

Voyons un exemple réel en pratique.

### Un compteur de vote positif en Vue

Rappelez-vous que nous avons construit le composant `UpvoteContent` initial en utilisant React. Nous allons maintenant créer le composant `UpvoteContent` en utilisant Vue et rendre les deux composants dans notre projet Astro.

Voici l'implémentation annotée :

```js
<!-- 📂 src/components/UpvoteContent.vue -->
<script>
export default {
  data() {
   // data properties used in the UI template
    return {
      upvoteCount: 0,
      maxUpvoteCount: 50,
    };
  },
  methods: {
	// method called when you click the upvote button
    upvote() {
      if (this.upvoteCount < this.maxUpvoteCount) {
        this.upvoteCount++;
      }
    },
  },
};
</script>

<template>
  <div>
    <button
	  // Attach a click event handler and invoke "upvote."
      @click="upvote"
    >
	 {/** Collapsed svg for brevity **/}
      <svg ../>
      Upvote
    </button>

    <div>
      <div>
        Vue
      </div>
      <div>{{ `${upvoteCount} upvotes` }}</div>

	   {/** Increase the width of the div by "count percentage"**/}
      <div :style="{ width: `${upvoteCount}%` }" />

		{/** Render this section only if
		  the count is equal to the max count  **/}
      <div
        v-if="upvoteCount === maxUpvoteCount"
      >
        Max upvote reached
      </div>
    </div>
  </div>
</template>

```

Et c'est tout !

### Comment rendre différents composants de framework

Le processus de rendu pour les composants de framework est essentiellement le même. Allons-y et rendons les composants React et Vue `UpvoteContent` sur une nouvelle page, comme indiqué ci-dessous :

```js
<!-- 📂 src/pages/multiple-frameworks.astro -->
---
import { UpvoteContent } from "../components/UpvoteContent.jsx";
import UpvoteContentVue from "../components/UpvoteContent.vue";
import DefaultIslandLayout from "../layouts/DefaultIslandLayout.astro";
---

<DefaultIslandLayout>
  <UpvoteContent client:load />
  <UpvoteContentVue client:load />
</DefaultIslandLayout>

```

*   Nous créons une nouvelle page dans `pages/multiple-frameworks.astro`.
*   Nous importons les composants React et Vue.
*   Nous rendons les deux composants selon un modèle identique et avec la même directive client, `client:load`.

Il est également essentiel d'ajouter le support Vue au projet en exécutant ce qui suit :

```js
npx astro add vue

```

Cela installera les dépendances Vue pertinentes et ajoutera le support d'intégration dans le fichier de configuration Astro.

Une fois cela fait, nous pouvons voir l'application en cours d'exécution sur la route `/multiple-frameworks`.

![Le composant React et Vue rendu dans une seule route de page Astro.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-03-13-at-15.39.40@2x.png)
_Le composant React et Vue rendu dans une seule route de page Astro._

Comme prévu, les deux composants sont rendus et fonctionnent exactement comme prévu.

## Comment partager l'état entre les îlots de composants

Lorsque nous travaillons avec des îlots de composants dans Astro, vous aurez inévitablement besoin de partager certains états d'application entre les îlots de composants.

![Partager l'état entre deux îlots de vote positif.](https://blog.ohansemmanuel.com/content/images/2023/06/islands-share-state.png)
_Partager l'état entre deux îlots de vote positif._

Par exemple, supposons que nous voulions que nos composants `UpvoteContent` partagent les mêmes valeurs de compteur.

Quel que soit le framework de composant, chaque framework a sa construction pour partager l'état UI entre les composants, par exemple entre les composants React ou Vue.

Mais lorsque nous travaillons au sein de composants Astro, nous avons besoin d'une solution qui fonctionne de manière agnostique au framework, c'est-à-dire qu'elle n'est pas liée à un seul framework.

Voici quelques solutions agnostiques au framework formidables parmi lesquelles nous pouvons choisir :

*   **Signaux** : Ils sont excellents pour exprimer l'état basé sur des principes réactifs. Nous pouvons utiliser [signals de Preact](https://github.com/preactjs/signals), [signia de tldraw](https://github.com/tldraw/signia) ou [Solid signals](https://www.solidjs.com/docs/latest) en dehors d'un contexte de composant.
*   **[API de réactivité de Vue](https://vuejs.org/guide/scaling-up/state-management.html#simple-state-management-with-reactivity-api)** : Cela peut être une excellente solution prête à l'emploi si vous utilisez déjà des composants Vue dans votre projet Astro.
*   **[Stores de Svelte](https://svelte.dev/tutorial/writable-stores)** : Cela peut également être une excellente solution prête à l'emploi si vous utilisez déjà des composants Svelte dans votre projet Astro.
*   **[Nano stores](https://github.com/nanostores/nanostores)** : C'est une minuscule bibliothèque agnostique au framework pour la gestion d'état.

Dans cet exemple, nous utiliserons Nano stores principalement parce qu'ils sont légers (moins de 1 Ko) et n'ajoutent pas beaucoup d'empreinte JavaScript à notre application.

### Comment fonctionne nano store

À un niveau élevé, ce que nous essayons d'atteindre est de supprimer les valeurs d'état de l'intérieur de nos composants de framework et de les gérer via `nanastores`.

Nous créerons une nouvelle variable d'état `upvoteCounter` dans nanostore. Nous propagerons ensuite les modifications de cette variable d'état à nos composants de framework.

![Propager les variables d'état depuis nanostore.](https://blog.ohansemmanuel.com/content/images/2023/06/nanostore-share-variable.png)
_Propager les variables d'état depuis nanostore._

### Installer nano store

Pour utiliser nano store, nous devons installer la bibliothèque dans notre projet. Exécutez la commande d'installation suivante :

```bash
npm install nanostores @nanostores/vue @nanostores/react

```

*   `nanostores` représente la bibliothèque de base pour créer et gérer nos valeurs d'état.
*   Pour garantir que le composant de framework est re-rendu chaque fois qu'une valeur d'état change, nous utiliserons les intégrations React et Vue pour nano stores via `@nanostores/react` et `@nanostores/vue`, respectivement.

### Créer la valeur d'état

Notre exemple inclut le partage de la valeur du compteur de votes positifs entre plusieurs composants de framework.

Pour créer une valeur d'état, nano stores utilise des atomes pour stocker des chaînes, des nombres et des tableaux.

Créons un atome pour contenir la variable d'état du compteur :

```js
<!-- 📂 src/stores/upvote.ts -->
import { atom } from "nanostores";

export const upvoteCountStore = atom(0);

```

*   Nous créons un nouveau fichier dans `src/stores/upvote.ts`.
*   Nous importons `atom` depuis `nanostore`.
*   Nous créons une nouvelle valeur d'état numérique appelée `upvoteCountStore`.

Nous pouvons penser aux atomes comme de petits morceaux d'état à partager entre les composants de notre application.

### Comment utiliser la valeur d'état dans les composants de framework

Dans le composant React, nous exploiterons le hook `useStore` fourni dans `@nanostores/react` pour récupérer la valeur d'état depuis le `upvoteCountStore` :

```js
// 📂 src/components/UpvoteContent.tsx

import { useStore } from "@nanostores/react";
import { upvoteCountStore } from "../stores/upvote";

const MAX_COUNT = 50;

export const UpvoteContent = () => {
  // Obtenir la valeur d'état depuis le store créé
  const upvoteCount = useStore(upvoteCountStore);

  return (
    <div>
      <button
        onClick={() => {
          if (upvoteCount < MAX_COUNT) {
            //Mettre à jour le store via la méthode set
            upvoteCountStore.set(upvoteCount + 1);
          }
        }}
      >
      { /** Le reste du code reste le même **/}
        Upvote
      </button>
	  { /** Le reste du code reste le même **/}
     </div>
  );
};


```

J'ai annoté le code pour le rendre plus facile à comprendre. Jetez un œil.

Avec le composant Vue, nous pouvons exploiter les `props` pour la réactivité comme indiqué ci-dessous :

```html
<script>
import { useStore } from "@nanostores/vue";
import { upvoteCountStore } from "../stores/upvote";

export default {
  // configurer les props à utiliser dans le template UI
  setup(props) {
    return {
	  // Définir la valeur de upvoteCount depuis le store
      upvoteCount: useStore(upvoteCountStore),
      maxUpvoteCount: 50,
    };
  },

  methods: {
    upvote() {
      if (this.upvoteCount < this.maxUpvoteCount) {
        // Mettre à jour le store via la méthode set
        upvoteCountStore.set(this.upvoteCount + 1);
      }
    },
  },
};
</script>

<template>
  { /** Le reste du code reste le même **/}
</template>


```

Adorable !

Maintenant, si nous essayons l'application, les deux composants de framework devraient avoir des valeurs de vote synchronisées :

![Valeurs d'état de vote synchronisées via nanostores.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-03-15-at-07.20.20.png)
_Valeurs d'état de vote synchronisées via nanostores._

## Comment passer des props et des enfants aux composants de framework

La plupart des composants de framework prennent en charge la réception de données via des props et des enfants (children). Ceux-ci sont également pris en charge lors du rendu de composants de framework dans Astro.

Par exemple, nous avons actuellement l'étiquette du bouton de vote codée en dur.

![L'étiquette de vote positif.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-19-at-18.06.54@2x.png)
_L'étiquette de vote positif._

Nous pourrions rendre cela dynamique via des props comme indiqué ci-dessous :

```html
// 📂 src/pages/load.astro
---
import { UpvoteContent } from "../components/UpvoteContent.jsx";
import DefaultIslandLayout from "../layouts/DefaultIslandLayout.astro";
---

<DefaultIslandLayout>
  <UpvoteContent client:load label="Click" />
</DefaultIslandLayout>

```

Nous gérerions ensuite la prop dans le composant React `UpvoteContent` comme d'habitude :

```ts
// 📂 src/components/UpvoteContent.tsx
export const UpvoteContent = (props: { label: string }) => {
   // ... render props.label
}

```

Il est important de noter que nous pouvons passer n'importe quelle primitive comme props, et elles fonctionneront comme prévu.

Mais attention aux props de fonction. Les props de fonction ne fonctionneront que pendant le rendu côté serveur et échoueront lorsqu'elles seront utilisées dans un composant client hydraté, par exemple comme gestionnaire d'événements. C'est parce que les fonctions ne peuvent pas être sérialisées (transférées du serveur au client).

Les enfants sont souvent traités comme un type de prop – selon le composant de framework utilisé. Par exemple, React, Preact et Solid utilisent la prop spéciale `children`, tandis que Svelte et Vue utilisent l'élément `<slot />`. Les deux sont pris en charge lorsque l'on travaille avec des composants de framework dans Astro.

Par exemple, avec notre composant React `<UpvoteContent />`, nous pourrions aller de l'avant et recevoir une description de composant comme `children` :

```js
<UpvoteContent client:load>
	<em>An upvote counter created using React</em>
</UpvoteContent>

```

Cela ne changera rien jusqu'à ce que nous gérions explicitement la prop `children` à l'intérieur du composant `<UpvoteContent>`, comme indiqué ci-dessous :

```js
// The component accepts props as an argument
export const UpvoteContent = (props: PropsWithChildren<{}>) => {
  const upvoteCount = useStore(upvoteCountStore);

  return (
    <>
     {/** Render the content of the children prop**/}
      <div>{props.children}</div>

      <div>
        {/** The rest of the component goes here**/}
      </div>
    </>
  );
};


```

![Rendre l'élément enfant du composant React.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-03-15-at-12.50.27.png)
_Rendre l'élément enfant du composant React._

Avec notre composant Vue `<UpvoteContent />`, nous pourrions également recevoir une description de composant comme enfants :

```js
 <UpvoteContentVue client:load>
    <em>An upvote counter created using Vue</em>
  </UpvoteContentVue>

```

Mais nous devons référencer cela via un élément `<slot>`. C'est une différence fondamentale dans la façon dont les bibliothèques comme React / Preact et Vue / Svelte traitent les références à la prop children.

Voici comment référencer l'élément enfants dans `UpvoteContentVue` :

```js
// 📂 src/components/UpvoteContent.vue
<template>
 <div>
  <div>
    <!-- the slot element renders the children element -->
    <slot />
  </div>

  <div>
   <!-- The rest of the template goes here -->
  </div>
 </div>
</template>

```

Aussi, nous pouvons utiliser plusieurs slots pour grouper et référencer des enfants au sein de nos composants de framework.

Considérez l'exemple suivant avec plusieurs éléments enfants :

```js
---
 import { UpvoteContent } from "../components/UpvoteContent.jsx"
---


<UpvoteContent>
  <ul slot="social-links">
	<li><a href="https://twitter.com/understanding-astro">Twitter</a></li>
    <li><a href="https://github.com/understanding-astro">GitHub</a></li>
  </ul>

  <em slot="description">An upvote counter created using React</em>
</UpvoteContent>

```

Notez que nous avons deux nœuds enfants référencés par les noms de slot `social-links` et `description`, respectivement.

À l'intérieur de `<UpvoteContent />`, nous pouvons référencer ceux-ci séparément comme indiqué ci-dessous :

```js
export const UpvoteContent = ({props}) => {
  return (
    <>
	  <div>{props.description}</div>
      <div>{props.socialLinks}</div>
      {/** ... **/}
    </>
  );
};

```

Il est important de noter que les noms de slot en `kebab-case` dans le composant Astro sont référencés comme des valeurs `camelCase` sur l'objet `props`.

![Référencer les noms de slot en kebab-case comme camelCase dans React ou Preact.](https://blog.ohansemmanuel.com/content/images/2023/06/kebab_to_camel_case.png)
_Référencer les noms de slot en kebab-case comme camelCase dans React ou Preact._

Dans Svelte et Vue, les slots seront référencés en utilisant un élément `<slot>` avec un attribut `name`. Voici l'implémentation dans `<UpvoteContentVue />` :

```js
<template>
	<slot name="description" />
    <slot name="social-links" />
</template>

```

Notez comment les noms de slot en `kebab-case` sont préservés.

![Rendre les éléments enfants des composants React et Vue.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-03-16-at-08.07.52.png)
_Rendre les éléments enfants des composants React et Vue._

## Composants de framework imbriqués

Dans un fichier Astro, nous pouvons également imbriquer des composants de framework, c'est-à-dire passer des composants de framework comme enfants. Par exemple, ce qui suit est valide :

```js
<DefaultIslandLayout>
  <UpvoteContent client:load>
    <div slot="description">
     <!-- This is a nested <UpvoteContent /> component -->
      <UpvoteContent client:load>
        <em slot="description">This is the nested component</em>
      </UpvoteContent>
    </div>
  </UpvoteContent>
</DefaultIslandLayout>


```

Comme prévu, cela rend le composant `UpvoteContent` imbriqué :

![Rendre des composants de framework imbriqués.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-03-16-at-09.00.38.png)
_Rendre des composants de framework imbriqués._

Rendre récursivement le même composant est rarement l'objectif que nous voulons atteindre. Mais rendre des composants de framework imbriqués est puissant car nous pouvons composer une application de composants de framework entière comme bon nous semble.

![Imbriquer plusieurs composants enfants pour créer une application plus importante.](https://blog.ohansemmanuel.com/content/images/2023/06/nesting-framework-component.png)
_Imbriquer plusieurs composants enfants pour créer une application plus importante._

## Pièges des îlots Astro

En tant que développeurs, nous sommes souvent responsables de casser des choses par inadvertance. Bien que le débogage puisse être un défi agréable, considérez les limites suivantes avec les îlots Astro.

### 1. Ne pas utiliser un composant Astro dans un composant de framework

Considérez l'exemple suivant d'importation d'un composant `.astro` et de son rendu à l'intérieur d'un composant React :

```js
import { OurAstroComponent } from "../components/OurAstroComponent"

const OurReactComponent = () => {
  return <div>
	<OurAstroComponent />
  </div>
}

```

```js
<OurReactComponent client:load />

```

Ceci est une utilisation invalide. La raison est que le composant React est rendu comme un "îlot" React. Par conséquent, l'îlot ne doit contenir que du code React valide. C'est la même chose pour les autres îlots de composants de framework.

![Ne pas rendre un composant Astro comme enfant d'un composant de framework sans <slot>.](https://blog.ohansemmanuel.com/content/images/2023/06/wrong-astro-island-composition.png)
_Ne pas rendre un composant Astro comme enfant d'un composant de framework sans &lt;slot&gt;._

Pour surmonter cela, envisagez d'utiliser le modèle de slot discuté précédemment pour passer du contenu statique depuis un composant Astro :

```js
---
 import { OurReactComponent } from "../components/OurReactComponent"
import { OurAstroComponent } from "../components/OurAstroComponent"
---

<OurReactComponent client:load>
 <!-- pass Astro component as a child via a named slot -->
 <OurAstroComponent slot="description" />
</OurReactComponent>

```

### 2. Ne pas hydrater un composant Astro

Considérez l'exemple naïf suivant pour hydrater un composant Astro en utilisant une directive client :

```js
---
 import { OurAstroComponent } from "../components/OurAstroComponent"
---

<OurAstroComponent client:load />

```

Ceci est invalide. Les composants Astro n'ont pas d'exécution côté client. Utilisez donc une balise `<script>` si vous avez besoin d'interactivité.

## Pourquoi utiliser des îlots ?

Généralement, la plupart des ressources placeraient cette section au début du chapitre. Mais il y a certains cas où il est plus bénéfique de présenter des cas d'utilisation pratiques avant de plonger dans les raisons qui les sous-tendent. De plus, cette approche pourrait favoriser une compréhension intuitive, ce que j'ai adopté ici.

Alors, pourquoi se concentrer sur les îlots ? Quels avantages offrent-ils ?

### 1. Performance

L'un des principaux avantages est l'amélioration des performances. Nous pouvons améliorer considérablement la vitesse de notre site en convertissant la majeure partie de notre site web en HTML statique et en chargeant sélectivement JavaScript via des îlots uniquement lorsque cela est nécessaire. C'est parce que JavaScript est l'un des actifs les plus lents à charger par octet.

### 2. Hydratation responsable

Si JavaScript est coûteux à analyser et à exécuter, la décision de le charger doit être prise avec soin (d'un point de vue performance). De plus, aucune solution unique ne convient à tous les types d'applications et cas d'utilisation. En tant que tel, contrôler quand un îlot de composants est hydraté vous met aux commandes de la performance de votre site web.

### 3. Chargement parallèle

Enfin, il est essentiel d'utiliser le chargement parallèle. Cela signifie que lorsque nous chargeons plusieurs îlots, ils n'auront pas à s'attendre les uns les autres pour devenir hydratés. Au lieu de cela, chaque îlot est considéré comme une unité distincte qui se charge et devient hydratée indépendamment, de manière isolée.

## Conclusion de ce chapitre

Dans ce chapitre, nous avons appris sur les îlots de composants dans Astro et comment ils fonctionnent. Nous avons également exploré pourquoi les composants de framework sont parfois préférés au JavaScript ou TypeScript vanilla via un élément `<script>`.

Nous avons également parcouru les étapes pour utiliser un composant de framework dans une application Astro, y compris la construction d'un site statique, l'installation du framework et l'écriture du composant.

Enfin, nous avons expérimenté l'utilisation d'un composant React et Vue pour démontrer l'utilisation des composants de framework. Rendez-vous au prochain chapitre !

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-137.png)
_Chapitre cinq_

# Chapitre 5 : Oh mon React ! (Comment construire un clone du site de documentation React)

Dans ce chapitre, nous couvrirons tout ce que vous devez savoir pour développer des sites web riches en contenu avec les meilleures pratiques du monde réel.

Ceci est une section pratique mieux servie avec vous codant en même temps. Pour voir l'application complète, consultez le [dépôt GitHub](https://github.com/understanding-astro/react.dev-astro).

## Ce que vous apprendrez

*   Comment styliser des projets Astro avec Tailwind.
*   Plusieurs solutions de coloration syntaxique pour Astro.
*   Comment exploiter les collections de contenu pour un développement évolutif et sécurisé par type.
*   Comprendre le routage dynamique dans Astro.

## Configurer le projet de démarrage

Nous avons passé beaucoup de temps à apprendre les tenants et les aboutissants de la construction de sites web statiques avec Astro. Donc, dans ce chapitre, nous ne partirons pas de zéro.

Au lieu de cela, nous commencerons avec un projet statique de base sur lequel nous construirons tout au long du chapitre.

![Construire à partir d'un projet de démarrage](https://blog.ohansemmanuel.com/content/images/2023/07/project-shell.png)
_Construire à partir d'un projet de démarrage_

Dans ce chapitre, nous adopterons une approche orientée solution similaire à celle utilisée par les détectives. Nous visons à résoudre divers `TODOs` dispersés dans le projet de démarrage.

![Résoudre de petits problèmes isolés](https://blog.ohansemmanuel.com/content/images/2023/07/todos.png)
_Résoudre de petits problèmes isolés_

La raison de cela est d'ignorer les concepts que vous avez déjà appris et de se concentrer sur l'apprentissage de nouveaux concepts ou la consolidation des concepts plus anciens par la pratique — résoudre des problèmes isolés.

Pour commencer, allez-y et clonez le projet :

```bash
git clone https://github.com/understanding-astro/react.dev-astro.git

```

Ensuite, changez de répertoire :

```bash
cd react.dev-astro

```

Enfin, passez à la branche `clean-slate` que j'ai préparée afin que nous puissions construire systématiquement sur l'application de base.

```bash
git checkout clean-slate

```

## Installer les dépendances

Allez-y et installez les dépendances du projet via ce qui suit :

```bash
npm install

```

Ensuite, installez l'intégration Astro `react` :

```bash
npx astro add react

```

Lorsque vous y êtes invité, tapez "y" pour accepter chaque invite. "y" signifie "yes" (oui) !

L'installation complète ajoutera toutes les dépendances React pertinentes et mettra à jour le fichier de configuration du projet `astro.config.mjs`.

![Image](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-06-23-at-08.11.48.png)
_Installer l'intégration React et les dépendances_

Enfin, allez-y et installez l'intégration `mdx`. Je décrirai le quoi et le pourquoi plus tard dans le chapitre. Pour l'instant, allez-y et installez l'intégration en exécutant ce qui suit :

```bash
npx astro add mdx

```

Cela installera l'intégration `@astrojs/mdx` et mettra également à jour le fichier de configuration du projet `astro.config.mjs`.

![Image](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-06-23-at-08.13.42.png)
_Installer l'intégration MDX_

Maintenant, exécutez l'application :

```bash
npm start

```

Cela exécutera l'application sur un port local disponible – le défaut `localhost:3000`.

Visitez le serveur local et vous trouverez l'application de base non stylisée fonctionnant dans le navigateur comme indiqué ci-dessous :

![La page d'accueil non stylisée](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-06-23-at-08.16.14.png)
_La page d'accueil non stylisée_

Je dois dire que c'est une page assez moche.

Nous allons réparer cela ensuite.

## Comment styliser des projets Astro avec Tailwind

Qu'on l'aime ou qu'on le déteste, le CSS est la façon dont nous créons de belles applications web.

Au chapitre un, nous avons écrit les styles pour le site web personnel à la main, c'est-à-dire en écrivant chaque déclaration CSS. Mais dans ce chapitre, nous utiliserons un framework CSS appelé Tailwind.

Alors, qu'est-ce que Tailwind ?

Une définition trop simple serait : Tailwind est le [bootstrap](https://getbootstrap.com/) moderne. Jamais utilisé Bootstrap ? Alors pensez à Tailwind comme un framework CSS orienté utilitaire qui fournit des noms de classe comme `flex`, `text-lg`, `items-center` et bien d'autres que vous pouvez appliquer à votre balisage pour les styles.

Tailwind nous permettra de construire des sites web modernes — rapidement.

### Comment installer Tailwind

Gardez le projet en cours d'exécution dans votre terminal et ouvrez un autre onglet de terminal. Exécutez la commande d'installation suivante :

```bash
npx astro add tailwind

```

Cela installera l'intégration Astro tailwind dans le projet et mettra à jour la configuration du projet.

![Image](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-06-24-at-08.16.12.png)
_Installer l'intégration Astro Tailwind_

Une fois l'installation terminée, les styles d'application existants prendront effet. Visitez l'application sur votre port local pour voir l'application stylisée.

![Image](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-06-24-at-08.17.17.png)
_L'application stylisée_

Quelle différence le style fait !

Prenez votre temps et parcourez les différentes pages de l'application stylisée.

### Comment fonctionne Tailwind ?

Utiliser Tailwind dans Astro est simple. Installez l'intégration Tailwind et fournissez un attribut `class` avec des classes utilitaires Tailwind dans le balisage de votre composant.

Par exemple, considérez le texte stylisé "The library for web and native user interfaces" sur la page d'accueil du projet :

![Image](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-07-03-at-06.50.11@2x.png)
_Le sous-titre de la page d'accueil_

Maintenant, considérez le code responsable des styles :

```js
// pages/index.astro
// ...
<p
   class="max-w-lg py-1 text-center font-display text-4xl leading-snug text-secondary dark:text-primary-dark md:max-w-full"
 >
   The library for web and native user interfaces
</p>


```

Dans l'exemple ci-dessus, les classes appliquées sont comme indiqué ci-dessous :

```html
"max-w-lg py-1 text-center font-display text-4xl leading-snug text-secondary dark:text-primary-dark md:max-w-full"

```

Bien que ce ne soit pas un livre sur Tailwind, il est juste de donner une explication générale de ce qui se passe ici.

Tout d'abord, la plupart des classes utilitaires Tailwind sont bien nommées et vous pouvez déduire ce qu'elles font. D'autres ne sont pas si bien nommées.

Si vous codez en même temps dans VSCode, je recommande d'installer l'intégration officielle Tailwind :

![Installer le plugin VSCode Tailwind officiel](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-07-03-at-06.55.50@2x.png)
_Installer le plugin VSCode Tailwind officiel_

Si vous n'utilisez pas VSCode, envisagez de trouver votre [configuration d'éditeur](https://tailwindcss.com/docs/editor-setup) dans la documentation officielle de Tailwind.

Installer l'intégration apporte de nombreux avantages. L'avantage important que je veux souligner ici est que vous pouvez survoler n'importe laquelle des classes utilitaires Tailwind pour voir la valeur exacte de la propriété CSS à laquelle la classe correspond.

Par exemple, survoler `max-w-lg` affiche la valeur de la propriété CSS pour la classe utilitaire comme indiqué ci-dessous :

```css
.max-w-lg {
    max-width: 32rem/* 512px */;
}

```

![Image](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-07-03-at-06.58.37@2x.png)
_Survoler les classes Tailwind_

C'est très utile car vous pouvez maintenant inspecter toutes les classes ajoutées à n'importe quel balisage dans le projet.

### Configuration de Tailwind

Lors de l'installation de Tailwind, il est livré avec son thème par défaut.

Ce n'est pas un mauvais thème, mais lorsque vous construisez des projets, vous voulez probablement contrôler le thème du projet.

Dans notre exemple, nous voulons un thème modelé sur le thème officiel de la documentation React.

Pour personnaliser Tailwind, nous pouvons fournir un fichier `tailwind.config.js` où nous pouvons définir les polices, la palette de couleurs, l'échelle de type, les valeurs de rayon de bordure, les points d'arrêt et bien plus encore de notre projet.

Regardez le fichier `tailwind.config.cjs` à la racine du projet. C'est là que la magie de la configuration Tailwind du projet se produit.

Pour plus de détails sur la personnalisation de Tailwind, vous pouvez consulter la [documentation officielle](https://tailwindcss.com/docs/theme).

## Alias d'importation Typescript

Soyons honnêtes, personne n'aime ces importations relatives moches, hein ?

```js
import MyComponent from '../../components/MyComponent.astro

```

Beurk !!

Allez, on peut faire mieux.

C'est là que les alias d'importation entrent en jeu. Le moyen le plus simple de configurer cela dans un projet Astro est de définir les alias dans le fichier `tsconfig.json`.

Par exemple, nous pouvons faire ce qui suit :

```js
// 📂 tsconfig.json

{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@components/*": ["src/components/*"],
    }
  }
}

```

Nous mappons essentiellement tous les répertoires dans le chemin d'importation `src/components` vers `@components`.

Maintenant, attendez la suite.

Le résultat de cela est que nous pouvons prendre notre précédent chemin d'importation moche et le transformer en une œuvre d'art comme indiqué ci-dessous :

```js
// Before
import MyComponent from '../../components/MyComponent.astro

// After
import MyComponent from '@components/MyComponent.astro'

```

Beau et propre, n'est-ce pas ?

La raison pour laquelle je mentionne cela est que le projet de démarrage a été configuré pour utiliser des alias d'importation. Alors, ne soyez pas confus.

Allez-y et regardez dans le fichier `tsconfig.json` où vous trouverez les alias d'importation suivants :

```js
"paths": {
   "@components/*": ["src/components/*"],
   "@layouts/*": ["src/layouts/*"],
   "@utils/*": ["src/utils/*"]
}

```

De rien 😉

## Îlots et colocation de composants de page

Nous avons appris que les types de fichiers appropriés dans le répertoire `src/pages` sont transformés en pages HTML.

Mais que faire si nous avons besoin d'avoir certains fichiers colocalisés dans le répertoire `src/pages` sans être transformés en pages `HTML` associées ?

![Colocaliser des fichiers dans le répertoire pages](https://blog.ohansemmanuel.com/content/images/2023/07/exclude_page_intro.png)
_Colocaliser des fichiers dans le répertoire pages_

Cela peut être utile pour colocaliser des tests, des utilitaires et des composants le long des pages associées.

Eh bien, il y a une solution pour cela.

Pour exclure un type de fichier de page valide dans le répertoire `src/pages` d'être compilé en une page `HTML` associée, préfixez le nom du fichier avec un trait de soulignement `_`.

![Préfixer le nom de fichier avec un trait de soulignement pour ne pas transformer en pages HTML](https://blog.ohansemmanuel.com/content/images/2023/07/prefix_exclude_page.png)
_Préfixer le nom de fichier avec un trait de soulignement pour ne pas transformer en pages HTML_

Par exemple, jetez un coup d'œil au répertoire `pages/_components/Home` dans le projet.

Ce répertoire contient une poignée de composants qui ne sont pas destinés à être réutilisables dans tout le projet. Ils n'existent que pour être utilisés sur la page d'accueil du projet.

Pour les exclure d'être des pages de navigateur séparées, notez comment le répertoire `_components` est nommé.

À titre d'exemple, si vous visitiez `/_components/Home/Code` dans le navigateur, cela renverrait une `404`. Même si les composants `Code` existent, ce n'est pas une page.

Maintenant, rassemblons nos connaissances sur les composants colocalisés et les îlots Astro pour résoudre notre premier TODO dans le projet.

Jetez un coup d'œil à `index.astro` et considérez le `TODO` pour rendre le composant React `Video` comme indiqué ci-dessous :

```js
// 📂 src/pages/index.astro
❗️ <Code class="text-white">TODO:</Code> (Astro Island): Render the ...

```

![TODO : Rendre l'îlot de composant React Video](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-07-05-at-08.40.18@2x.png)
_TODO : Rendre l'îlot de composant React Video_

Maintenant, considérez la solution annotée ci-dessous :

```js
// 📂 src/pages/index.astro
===
// Import the Video component from "_components ..."
import { Video } from "./_components/home/Video";
// ...
---
<ExampleResultPanel slot="right-content">
  {/** Render the Video component. NB: this is a React component **/}
   <Video
     client:visible {/** 👈 Add the client directive **/}
     video={{ title: "My video", description: "Video description" }}
    />
</ExampleResultPanel>

```

*   Rendre le composant React `Video`
*   Passer un attribut `client:visible` pour hydrater l'îlot dès que le composant est visible
*   Enfin, passer les props d'objet `video` requises au composant `Video` : `{title: "my video", description: "Video description"}`.

![L'îlot vidéo rendu](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-07-05-at-08.39.19@2x.png)
_L'îlot vidéo rendu_

De même, résolvons le deuxième TODO. Cette fois-ci, nous rendrons plusieurs composants `Video`.

```js
// 📂 src/pages/index.astro
❗️ <Code class="text-white">TODO:</Code> (Astro Island): Render two ...

```

![TODO : Rendre deux îlots de composants React](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-07-05-at-08.43.18@2x.png)
_TODO : Rendre deux îlots de composants React_

Considérez la solution ci-dessous :

```js
<ExampleResultPanel slot="right-content">
  <div class="flex w-full flex-col gap-4">
    {/** ... **/}
    {/** Render both islands **/}
    <Video
      client:visible
      video={{ title: "My video", description: "Video description" }}
    />
    <Video
      client:visible
      video={{ title: "My video", description: "Video description" }}
    />
  </div>
</ExampleResultPanel>

```

![Les îlots Astro rendus](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-07-05-at-08.45.15@2x.png)
_Les îlots Astro rendus_

## Coloration syntaxique

Je n'ai jamais compris les subtilités de la coloration syntaxique jusqu'à ce que je commence à faire des recherches pour cette section du livre. C'est génial de voir combien de choses sont abstraites dans les bibliothèques.

Quoi qu'il en soit, je vais sauter les nuances et fournir ce que je crois être les éléments les plus importants.

Alors, comment abordons-nous la coloration syntaxique dans une application Astro ?

Par défaut, Astro utilise [Shiki](https://github.com/shikijs/shiki) – une bibliothèque de coloration syntaxique sous le capot. De manière générale, il existe deux façons de procéder à la coloration syntaxique de vos blocs de code dans un composant Astro.

Jetons un coup d'œil à celles-ci.

### Le composant Code par défaut

Astro est livré avec un composant `<Code />` qui fournit des colorations syntaxiques au moment de la construction.

![Le composant Code rend en HTML et styles en ligne sans aucun Javascript](https://blog.ohansemmanuel.com/content/images/2023/07/code_component.png)
_Le composant Code rend en HTML et styles en ligne sans aucun Javascript_

Par implication, il n'y a pas de surcharge d'exécution pour cette méthode de coloration syntaxique car aucun calcul n'est effectué au moment de l'exécution et le résultat final est un tas d'éléments avec des styles en ligne.

Ceci est propulsé par Shiki.

![Exemple de sortie DOM avec coloration syntaxique](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-06-25-at-08.35.52.png)
_Exemple de sortie DOM avec coloration syntaxique_

Revenons à notre projet de démarrage et résolvons un autre TODO.

```js
📂 src/pages/index.astro

// ...
❗️ <Code class="text-white">TODO:</Code> Replace with Syntax highlighted code

```

![TODO : Ajouter un bloc de code avec coloration syntaxique](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-07-05-at-16.06.25@2x.png)
_TODO : Ajouter un bloc de code avec coloration syntaxique_

L'objectif ici est de fournir du code avec coloration syntaxique dans le balisage du composant.

Pour résoudre cela, nous exploiterons le composant `Code` d'Astro comme indiqué dans le bloc de code annoté ci-dessous :

```js
// 📂 src/pages/index.astro
---
// import Code from "astro/components"
import { Code as AstroCode } from "astro/components";
//... other imports
---

// ...Render the component and pass the code and lang string props
<div slot="left-content">
  <AstroCode
            code={`function Video({ video }) {
  return (
    <div>
      <Thumbnail video={video} />
      <a href={video.url}>
        <h3>{video.title}</h3>
        <p>{video.description}</p>
      </a>
      <LikeButton video={video} />
    </div>
  );
}`}
    lang="jsx" {/** 👈 code language for syntax highlighting **/}
   />
</div>

```

![Le bloc de code avec coloration syntaxique](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-06-25-at-13.04.02@2x.png)
_Le bloc de code avec coloration syntaxique_

Puisque les extraits de code ne sont que de bons vieux nœuds DOM HTML, nous pouvons appliquer quelques styles sur le `div` parent pour les styliser davantage comme indiqué ci-dessous :

```js
// 📂 src/pages/index.astro
<div
   slot="left-content"
   class="[&_pre]:!bg-transparent [&_pre]:!text-sm [&_pre]:!leading-6">
	<AstroCode ... />
</div>

```

Cela réduira la taille de la police, réduira l'interlignage et rendra l'arrière-plan du code transparent. Notez que les crochets sont la façon dont nous écrivons des [styles personnalisés](https://tailwindcss.com/docs/adding-custom-styles#using-arbitrary-values) arbitraires dans Tailwind.

Voir les résultats ci-dessous :

![Bloc de code avec coloration syntaxique mieux stylisé](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-06-25-at-13.03.25@2x.png)
_Bloc de code avec coloration syntaxique mieux stylisé_

Bien mieux, hein ?

Nous pouvons aller de l'avant et faire de même pour l'autre `TODO` :

```js
// 📂 src/pages/index.astro
❗️ <Code class="text-white">TODO:</Code> Replace with Syntax highlighted code

```

Considérez la solution identique ci-dessous :

```js
<div
   slot="left-content"
   {/** Similar style as before. Leverages Tailwind **/}
   class="[&_pre]:!bg-transparent [&_pre]:!text-sm [&_pre]:!leading-6"
        >
          <AstroCode
            code={`function VideoList({ videos, emptyHeading }) {
  const count = videos.length;
  let heading = emptyHeading;
  if (count > 0) {
    const noun = count > 1 ? 'Videos' : 'Video';
    heading = count + ' ' + noun;
  }
  return (
    <section>
      <h2>{heading}</h2>
      {videos.map(video =>
        <Video key={video.id} video={video} />
      )}
    </section>
  );
}`}
   lang="jsx"
 />

```

![Le bloc de code avec coloration syntaxique](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-06-25-at-13.05.02@2x.png)
_Le bloc de code avec coloration syntaxique_

Le composant `Code` par défaut prend également en charge tous les [thèmes](https://github.com/shikijs/shiki/blob/main/docs/themes.md#all-themes) officiels de Shiki. Par exemple, nous pouvons changer le thème du composant en `poimandres` comme indiqué ci-dessous :

```js
<AstroCode
    // ...
   lang="jsx"
   theme="poimandres"
 />

```

![Le thème poimandres](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-06-25-at-13.15.33@2x.png)
_Le thème poimandres_

Considérons les avantages et les inconvénients de l'utilisation du composant `Code` par défaut fourni par Astro.

#### Avantages

*   Facile à utiliser
*   Excellents résultats pour peu d'effort
*   Beaucoup de thèmes disponibles par défaut

#### Inconvénients

*   Plus de travail est nécessaire pour personnaliser vos thèmes, par exemple notre clone de www.react.dev nécessite son thème personnalisé
*   Pas de support par défaut pour les thèmes sombre et clair

### Apportez votre thème

Utiliser vos thèmes de syntaxe spécifiques n'est probablement pas en haut de votre liste.

Mais Shiki prend en charge la même syntaxe pour les thèmes VSCode. Par exemple, nous pourrions charger un thème VSCode open-source personnalisé (ou construire par-dessus) pour nos blocs de code.

Jetons un coup d'œil à [Nightowl](https://github.com/sdras/night-owl-vscode-theme), un thème sombre VS Code pour le contraste pour le codage nocturne.

Allez-y et copiez le [thème d'extrait](https://raw.githubusercontent.com/sdras/night-owl-vscode-theme/main/themes/Night%20Owl-color-theme.json) de code dans un fichier `src/snippet-theme.json`.

Ensuite, nous écrirons un composant simple pour charger notre thème personnalisé comme indiqué ci-dessous :

```js
// 📂 src/components/Shiki.astro

---
import type { Lang } from "shiki";

// Similar to Astro's Code component, this is built on shiki
import shiki, { getHighlighter } from "shiki";

// Similar to Astro's Code component, receive lang and code as props
type Props = {
  lang: Lang;
  code: string;
};

const { code = "", lang = "jsx" } = Astro.props;

// 👀 Load the custom theme
const theme = await shiki.loadTheme("../../snippet-theme.json");

const highlighter = await getHighlighter({
  theme,
  langs: [lang],
});
---

{/**
  A fragment is an available Astro component. Use Fragment to prevent unnecessary markup.
The set:html directive is used to inject an HTML string into an element e.g., similar to el.innerHTML.
**/}
<Fragment
  set:html={highlighter.codeToHtml(code, {
    lang,
  })}
/>

```

Importez et utilisez le nouveau composant :

```js
// 📂 src/pages/index.astro
---
import Shiki from "@components/Shiki.astro";
// ...
---

// Change AstroCode to Shiki (new component)

<Shiki
 code={`function Video({ video }) {
  return (
    <div>
      <Thumbnail video={video} />
      <a href={video.url}>
        <h3>{video.title}</h3>
        <p>{video.description}</p>
      </a>
      <LikeButton video={video} />
    </div>
  );
}`}
  lang="jsx"
/>

```

Et voilà ! Nous avons chargé avec succès un thème personnalisé.

![Comparer le code surligné précédent avec le nouveau thème Night Owl](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-06-25-at-13.55.54@2x.png)
_Comparer le code surligné précédent avec le nouveau thème Night Owl_

Pour plus de personnalisations, nous pourrions passer du temps à ajuster les différents jetons de thème dans le fichier `snippet-theme.json`.

#### Avantages

*   Flexibilité : nous pouvons personnaliser les jetons de thème aussi finement que nécessaire

#### Inconvénients

*   Nécessite plus de travail
*   Support pour les thèmes sombre et clair

### Gérer les thèmes clair et sombre

Prendre en charge les thèmes clair et sombre dans Shiki (le surligneur de syntaxe sous-jacent d'Astro) est délicat car Shiki génère des thèmes au moment de la construction.

Au moment où un utilisateur bascule le thème du site, aucun changement ne sera apporté à la coloration syntaxique puisqu'elle a été générée au moment de la construction.

Lorsque l'on travaille avec des composants Astro, une solution simple consiste à exploiter les variables CSS.

```js
---
import { Code as AstroCode } from "astro/components";
---

// Among, other properties, pass a "css-variables" theme prop to the Code component
 <AstroCode theme="css-variables" />

```

Ensuite, fournissez des jetons de style pour les thèmes sombre et clair. Rappelez-vous que cela doit être global. Par exemple, nous pouvons le faire dans le composant de mise en page `Baselayout.astro` comme indiqué ci-dessous :

```js
// 📂 src/layouts/BaseLayout.astro
<style is:global>
  @media (prefers-color-scheme: dark) {
    :root {
      --astro-code-color-text: #ffffff;
      --astro-code-color-background: black;
      --astro-code-token-constant: #86d9ca;
      --astro-code-token-string: #977cdc;
      --astro-code-token-comment: #757575;
      --astro-code-token-keyword: #77b7d7;
      --astro-code-token-parameter: #ffffff;
      --astro-code-token-function: #86d9ca;
      --astro-code-token-string-expression: #c64640;
      --astro-code-token-punctuation: #ffffff;
      --astro-code-token-link: #977cdc;
    }
  }

  :root {
    --astro-code-color-text: #24292e;
    --astro-code-color-background: #ffffff;
    --astro-code-token-constant: #032f62;
    --astro-code-token-string: #032f62;
    --astro-code-token-comment: #6a737d;
    --astro-code-token-keyword: #d73a49;
    --astro-code-token-parameter: #24292e;
    --astro-code-token-function: #6f42c1;
    --astro-code-token-string-expression: #c64640;
    --astro-code-token-punctuation: #ffffff;
    --astro-code-token-link: #977cdc;
  }
</style>

```

Si la coloration syntaxique des thèmes sombre et clair est critique pour votre application, jetez un coup d'œil à la [documentation officielle](https://github.com/shikijs/shiki/blob/main/docs/themes.md#theming-with-css-variables) pour plus d'informations.

## Comment démarrer avec les collections de contenu

Imaginez construire une grande application pilotée par beaucoup de contenu – que ce soit des fichiers Markdown (`/md`), MDX (`.mdx`), JSON (`.json`) ou YAML (`.yaml`).

Une solution pour organiser au mieux le contenu du projet pourrait être de sauvegarder les données de contenu dans une base de données où nous pouvons valider le schéma du document et nous assurer que le contenu requis correspond au modèle de données que nous désirons.

Nous pouvons modéliser visuellement cela comme des collections de données enregistrées dans une base de données avec un schéma de données prédéfini.

![Modéliser des données avec un schéma prédéfini dans une base de données](https://blog.ohansemmanuel.com/content/images/2023/07/predefined_schema_db.png)
_Modéliser des données avec un schéma prédéfini dans une base de données_

Avec les projets Astro, nous n'avons pas particulièrement besoin d'une base de données pour stocker et appliquer nos modèles de données de contenu.

Entrez les collections de contenu.

Quelle que soit la taille du projet Astro, les collections de contenu sont le meilleur moyen d'organiser notre document de contenu, de valider la structure du document et de profiter également d'un support TypeScript prêt à l'emploi lors de l'interrogation ou de la manipulation de la collection de contenu.

Alors, qu'est-ce qu'une collection de contenu ?

Une collection de contenu est tout répertoire de niveau supérieur dans le dossier `src/content` d'un projet Astro.

![Collections de contenu - répertoires de niveau supérieur dans src/content](https://blog.ohansemmanuel.com/content/images/2023/07/content_collections.png)
_Collections de contenu - répertoires de niveau supérieur dans src/content_

Notez que le répertoire `src/content` est strictement réservé aux collections de contenu. N'utilisez pas ce répertoire pour autre chose.

Maintenant que nous savons ce qu'est une collection de contenu, les documents individuels ou entrées au sein d'une collection sont appelés entrées de collection.

![Entrées de collection au sein d'une seule collection](https://blog.ohansemmanuel.com/content/images/2023/07/collection_entries.png)
_Entrées de collection au sein d'une seule collection_

Les entrées de collection sont des documents dans des formats tels que Markdown ou MDX. Elles peuvent également être dans des formats de données tels que JSON ou YAML. Pour la cohérence, vous trouverez la plupart des entrées de collection avec un modèle de nommage cohérent, par exemple kebab-case.

### Quels problèmes les collections de contenu résolvent-elles ?

Encombrer un projet avec différents documents de contenu et aucune structure claire est un moyen sûr de créer un désordre.

La meilleure solution : utiliser des collections de contenu.

Maintenant, les collections de contenu visent à résoudre trois problèmes principaux :

1.  Organiser les documents.
2.  Valider la structure du document (par exemple valider les propriétés de frontmatter d'un fichier markdown).
3.  Fournir une forte sécurité de type lors de l'interrogation et du travail avec les collections de contenu.

### Comment organiser les collections de contenu

Lorsque vous travaillez avec des collections de contenu, notez que seuls les répertoires de niveau supérieur dans `src/content` comptent comme des collections.

Par exemple, avec plusieurs collections telles que `blogs`, `authors` et `comments`, nous pourrions représenter avec précision ces types de contenu distincts avec trois répertoires de niveau supérieur dans `src/content`.

![Organiser différentes collections de contenu](https://blog.ohansemmanuel.com/content/images/2023/07/content_collection_example.png)
_Organiser différentes collections de contenu_

S'il est nécessaire d'organiser davantage le contenu via des sous-répertoires au sein d'une collection, c'est tout à fait acceptable ! Par exemple, la collection de contenu `blogs` peut avoir des sous-répertoires pour organiser le contenu via des langues par exemple `en`, `fr`, et ainsi de suite.

![Sous-répertoires au sein des collections de contenu](https://blog.ohansemmanuel.com/content/images/2023/07/collection_subdirectories.png)
_Sous-répertoires au sein des collections de contenu_

### Comment autoriser le contenu avec MDX

Jetez un coup d'œil à la collection de contenu existante dans le projet.

Que voyez-vous ?

Vous devriez trouver une collection `blog` dans `src/content/blog` avec une poignée de fichiers `.mdx`.

![Entrées dans la collection blog](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-07-11-at-06.44.39.png)
_Entrées dans la collection blog_

Chaque fichier `mdx` fait référence à l'entrée de collection pour la collection blog. Mais qu'est-ce qu'un fichier `mdx` ?

MDX se présente comme le markdown pour l'ère des composants. Pensez, et si nous pouvions utiliser des composants dans le markdown ? Eh bien, avec `MDX`, nous le pouvons.

Dans ces fichiers, nous pouvons importer des composants et les intégrer dans notre contenu markdown standard.

Dans la section d'installation de ce chapitre, nous avons installé le plugin Astro MDX en exécutant `npx astro add mdx`.

Il est grand temps que nous commencions à utiliser MDX.

### Comment configurer les collections de contenu

Une grande partie des collections de contenu consiste à assurer un format d'entrée de collection cohérent pour chaque collection de contenu.

Par exemple, en supposant un certain nombre d'entrées de collection markdown ou MDX, nous pouvons aller de l'avant et nous assurer que chaque entrée de collection a les mêmes propriétés de frontmatter. Comme vous pouvez l'imaginer, cela protège l'intégrité de chaque entrée de collection et donne confiance qu'aucun bug surprenant ne nous sautera dessus lorsque nous travaillerons avec les entrées.

Alors, comment assurons-nous une telle cohérence ?

La façon dont nous faisons cela est en créant des schémas de collection.

Un schéma applique des données d'entrée de collection cohérentes au sein d'une collection. C'est aussi ce qui alimente le support TypeScript que nous obtiendrons lorsque nous travaillerons avec les entrées de collection.

Pour créer notre schéma de collection, allez-y et créez un fichier `src/content/config.ts` avec le contenu suivant :

```js
// Import utilities from astro:content
import { z, defineCollection } from "astro:content";

// Define the type and schema for one or more collections
const blogCollection = defineCollection({
  type: 'content',
  // an object of strings - title, year, month, day, and intro
  schema: z.object({
    title: z.string(),
    year: z.string(),
    month: z.string(),
    day: z.string(),
    intro: z.string(),
  }),
});

// Export a single collections object to register the collections
// The key should match the collection directory name in "src/content"
export const collections = {
  blog: blogCollection, // add the blog collection
};

```

Jetez un coup d'œil au code annoté ci-dessus.

Vous n'avez pas besoin de mémoriser comment faire cela, car vous pouvez toujours vous référer à la documentation officielle. Mais rappelez-vous que le schéma pour les collections de contenu d'un projet est défini dans un fichier `src/content/config.ts` (ou `.js` et `.mjs`).

Si nous décomposons ce qui se passe dans un fichier de configuration de collection, nous avons trois actions principales :

1.  Importer des utilitaires depuis `astro:content`.
2.  Définir le(s) schéma(s) de collection de contenu via l'utilitaire `z`.
3.  Exporter un seul objet de clé de nom de collection et de valeur de schéma.

Le schéma est le cerveau derrière la garantie que notre contenu contient les bonnes données et fournit également un support TypeScript — autocomplétion et vérification de type lors de l'interrogation de la collection.

Je connais la question que vous vous posez probablement.

Qu'est-ce que l'utilitaire `z` exporté depuis `astro:content` ?

L'utilitaire `z` réexporte la bibliothèque très populaire [zod](https://github.com/colinhacks/zod) — une bibliothèque de validation de schéma TypeScript-first avec inférence de type statique. La variable `z` dans la `config` est une exportation pratique de `zod`.

#### Introduction rapide à Zod

Bien que ce ne soit pas un livre sur Zod, la vérité reste que si nous allons définir des schémas avec Zod, il vaut la peine de comprendre les bases.

Alors, voici une introduction rapide.

Tout d'abord, considérez le schéma pour notre collection `blog` :

```js
z.object({
  title: z.string(),
  year: z.string(),
  month: z.string(),
  day: z.string(),
  intro: z.string(),
})

```

Déconstruisons cela.

Créer un schéma commence par importer Zod. Avec Astro, cela se fait via l'importation depuis `astro:content`

```js
import {z} from 'astro:content'

```

Pour créer un schéma pour une propriété de chaîne, utilisez la méthode `string` comme indiqué ci-dessous :

```js
const stringSchema = z.string()

```

Pour créer un schéma d'objet, vous l'avez deviné. Nous utilisons la méthode `object` comme indiqué ci-dessous :

```js
const myObjectSchema = z.object({

})

```

Maintenant, à l'intérieur de cet objet, nous pouvons définir des propriétés comme indiqué ci-dessous :

```js
const myObjectSchema = z.object({
	someString: z.string()
})

```

Dans notre schéma de collection de blog, nous disons essentiellement que les fichiers markdown (et MDX) au sein de la collection `blog` doivent avoir des propriétés de frontmatter de chaîne `title`, `year`, `month`, `day` et `intro`.

Le frontmatter est représenté par le schéma d'objet et ses propriétés, les clés d'objet.

Maintenant, allez-y et visualisez toutes les entrées de collection dans la collection `blog` et notez comment elles ont toutes des propriétés définies.

#### Le dossier `.astro`

Au fur et à mesure que vous créez et travaillez avec des collections de contenu, Astro crée un répertoire `.astro` à la racine de notre projet pour garder une trace des métadonnées importantes pour nos collections de contenu — principalement des informations de type générées.

Il est sûr d'ignorer ce répertoire.

Le répertoire `.astro` est mis à jour automatiquement lorsque nous exécutons les commandes `astro dev` ou `astro build`. Mais si nous trouvons que les informations de type ne sont pas synchronisées, nous pouvons exécuter manuellement `astro sync` à tout moment pour mettre à jour le répertoire `.astro` manuellement.

## Comment interroger et rendre des collections de contenu

Donc, nous savons comment créer des collections de contenu et définir leurs schémas. Et ensuite ?

Les collections de contenu existent pour être consommées d'une manière ou d'une autre — généralement en interrogeant et en rendant les collections.

Alors, comment commençons-nous avec cela ?

Une collection se compose d'une ou plusieurs entrées de collection. Donc, pour interroger une collection entière, Astro fournit la méthode `getCollection()`.

Considérez comment nous pouvons récupérer tous les articles de blog dans notre projet :

```js
---
import { getCollection } from 'astro:content'

// Get all entries from the blog collection
const allBlogPosts = await getCollection('blog')
---

```

Pour filtrer les entrées de collection, nous pouvons passer un deuxième argument de fonction à `getCollection` comme indiqué ci-dessous :

```js
---
import { getCollection } from 'astro:content'

// Get all entries from the blog collection
const allBlogPosts = await getCollection('blog', ({data}) => {
  // return only blogs from a certain year
  return data.year === '2023'
})
---

```

Notez que dans notre cas, les `data` ci-dessus font référence aux propriétés de frontmatter de nos entrées de blog `MDX`.

Qu'en est-il de l'obtention d'une seule entrée de collection ?

Votre première inclination pourrait être de filtrer comme indiqué ci-dessous :

```js
---
import { getCollection } from 'astro:content'

// Get all entries from the blog collection
const allBlogPosts = await getCollection('blog', ({data}) => {
  // return only a specific title
  return data.title === 'my-single-blog-title"
})
---

```

Ce qui précède est techniquement valide. Mais Astro fournit une méthode `getEntry()` spécifiquement pour ce cas.

Considérez l'utilisation ci-dessous :

```js
import {getEntry} from 'astro:content'

// Get a single blog entry with the entry slug
const blog = await getEntry('blog', 'introduction-to-react')

```

L'exemple ci-dessus récupérera l'entrée dans la route `src/content/blog/introduction-to-react.mdx`.

Notez que `getCollection` et `getEntry` renvoient tous deux un type [CollectionEntry](https://docs.astro.build/en/reference/api-reference/#collection-entry-type).

Assez de théorie, revenons à la construction de notre projet.

Trouvez le prochain TODO sur la page `blog/index.astro` :

```js
📂 src/pages/blog/index.astro

<!-- ❗️TODO: List and render (all) blog post cards -->

```

L'objectif est de récupérer tous les blogs dans la collection de contenu de blog et de rendre des cartes visuelles pour chaque entrée. Notez également que cliquer sur chaque carte devrait pointer vers le blog réel.

![Rendre des cartes d'articles de blog.](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-07-10-at-05.49.23.png)
_Rendre des cartes d'articles de blog._

Considérez la solution ci-dessous :

```js
📂 src/pages/blog/index.astro

---
// Import getCollection from astro:content
import { getCollection } from "astro:content";
// Import the BlogCard visual component
import BlogCard from "@components/BlogCard.astro";
// Import the getMonthName utility
import { getMonthName } from "@utils/getMonthName";

// Fetch all the blog posts
const allBlogPosts = await getCollection("blog");
---

{/** render all blog posts **/}
  <div class="mt-12 flex flex-col gap-5 px-5 sm:-mx-5 lg:px-4">
    {
      allBlogPosts.map(({ data, slug }) => {
        const url = `/blog/${data.year}/${data.month}/${data.day}/${slug}`;

        return (
          <BlogCard
            url={url}
            date={`${getMonthName(+data.month)} ${data.day}, ${data.year}`}
            title={data.title}
          >
            {data.intro}
          </BlogCard>
        );
      })
    }
  </div>

```

Notez l'URL de chaque blog construite dans la solution ci-dessus :

```js
const url = `/blog/${data.year}/${data.month}/${data.day}/${slug}`;

```

Par exemple, l'entrée de collection de blog `data-fetching-with-react-server-components.mdx` aura le chemin : `/blog/2020/12/21/data-fetching-with-react-server-components`.

Allez-y et cliquez sur n'importe laquelle des cartes de blog. Pour le moment, elles devraient mener à une page vide.

Résolvons cela.

## Routage dynamique

Les routes statiques sont sans doute faciles à comprendre. Par exemple, les fichiers `.astro`, `.md` et `.mdx` dans `src/pages` deviendront automatiquement des pages sur notre site web.

Mais parfois, nous avons besoin de routes dynamiques pour éviter la répétition. Cela se produit généralement lorsque nous avons différentes routes avec des changements d'interface utilisateur minimes entre elles.

Par exemple, considérez notre projet actuel. Les blogs auront des routes différentes, mais l'apparence et la convivialité de chaque blog sont identiques.

```ts
// example routes for different blogs
/blog/2020/12/21/data-fetching-with-react-server-components
/blog/2023/04/24/some-other-blog-title
/blog/2023/07/12/getting-started-with-react

```

```ts
// 👀 Manually creating multiple pages for each blog
/pages/2020/12/21/data-fetching-with-react-server-components.astro
/pages/2023/04/24/some-other-blog-title.astro
/pages/2023/07/12/getting-started-with-react.astro

```

Fournir manuellement plusieurs pages pour chaque blog est sans doute fastidieux.

Au lieu de créer manuellement différentes pages pour représenter chaque blog, nous pouvons gérer dynamiquement le routage de l'une des deux manières suivantes.

### 1. Paramètres nommés

La structure URL des blogs pourrait être représentée par `/${year}/${month}/${day}/${title}` où `title` représente le titre du blog et `year`, `month` et `day`, décrivent quand le blog a été publié.

Nous pourrions représenter les variables dans le chemin de la route avec des paramètres nommés entourés de crochets.

Par exemple, nous pouvons créer un fichier dans le répertoire `pages/blog` avec le nom de fichier suivant :

```md
/[year]/[month]/[day]/[title].astro

```

Puisque nos pages sont construites statiquement, par exemple lorsque nous exécutons le script de build, toutes les routes doivent être déterminées au moment de la construction.

Pour y parvenir, nous devons exporter une fonction `getStaticPaths` qui renvoie un tableau d'objets correspondant à chaque route. Voici comment :

```js
// 📂 pages/blog/[year]/[month]/[day]/[title].astro
---
import BlogLayout from "@layouts/BlogLayout.astro";

export function getStaticPaths() {
    return [
        {
            params: {
                title: "data-fetching-with-react-server-components",
                year: "2020",
                month: "12",
                day: "21",
            },
        },
    ];
}
---

```

Notez que `getStaticPaths` renvoie spécifiquement un objet avec un champ `params` qui définit toutes les variables dans le chemin de la route, c'est-à-dire `title`, `year`, `month` et `day`

Pour ajouter une autre route de blog, ajoutez simplement un autre objet avec sa propriété `params` :

```js
// 📂 pages/blog/[year]/[month]/[day]/[title].astro
---
export function getStaticPaths() {
    return [
        {
            params: {
                title: "data-fetching-with-react-server-components",
                year: "2020",
                month: "12",
                day: "21",
            },
        },
        {
            params: {
                title: "introducing-react-dev",
                year: "2023",
                month: "03",
                day: "16",
            },
        },
    ];
}
---

```

Avec les `params` de route définis, nous saisissons ensuite les variables et rendons chaque blog comme indiqué ci-dessous :

```js
// 📂 pages/blog/[year]/[month]/[day]/[title].astro
---
import BlogLayout from "@layouts/BlogLayout.astro";

export function getStaticPaths() {
    return [
        {
            params: {
                title: "data-fetching-with-react-server-components",
                year: "2020",
                month: "12",
                day: "21",
            },
        },
        {
            params: {
                title: "introducing-react-dev",
                year: "2023",
                month: "03",
                day: "16",
            },
        },
    ];
}

// Get the path variables from Astro.params
const { title, year, month, day } = Astro.params;
---

// Provide markup for each matched page
<BlogLayout title="React Blog - React" header="React Blog">
    <h1>{title}</h1>
    <p>{year}</p>
    <p>{month}</p>
    <p>{day}</p>
</BlogLayout>


```

Cliquer sur les cartes _data fetching with react server components_ et _introducing react dev blog_ devrait maintenant rendre leur page associée.

![Balisage de blog rendu](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-07-02-at-07.41.17.png)
_Balisage de blog rendu_

### 2. Paramètres rest

Les paramètres rest offrent une flexibilité ultime dans notre routage URL. Par exemple, nous pouvons utiliser `[...path]` pour faire correspondre des chemins de fichiers **de n'importe quelle profondeur**. Où `path` pourrait être représenté par n'importe quelle chaîne, par exemple `[...file]` ou `[...somestring]`.

En suivant notre exemple existant, comment pouvons-nous réduire le chemin `pages/blog/[year]/[month]/[day]/[title].astro` à simplement `pages/blog/[...path].astro`.

Supprimez les répertoires et fichiers précédents qui constituaient `[year]/[month]/[day]/[title].astro` et créez un seul `blog/[...path].astro`.

Ce nouveau fichier correspondra à la route du blog.

De même, nous devons fournir une fonction `getStaticPaths`, mais la variable à fournir ici est `path` comme indiqué ci-dessous :

```js
---
import BlogLayout from "@layouts/BlogLayout.astro";

export function getStaticPaths() {
    return [
        {
            params: {
                path: "2020/12/21/data-fetching-with-react-server-components",
            },
        },
        {
            params: {
                path: "2023/03/16/introducing-react-dev",
            },
        },
    ];
}

const { path } = Astro.params;
---

<BlogLayout title="React Blog - React" header="React Blog">
    <h1>{path}</h1>
</BlogLayout>

```

Cliquer sur les cartes _data fetching with react server components_ et _introducing react dev blog_ devrait maintenant rendre leur page associée.

![Balisage de blog rendu](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-07-02-at-07.40.03.png)
_Balisage de blog rendu_

### Ordre de priorité

Comme nous en avons discuté, les chemins URL peuvent être mis en correspondance de différentes manières. Alors que se passe-t-il lorsque différents chemins de fichiers correspondent au même chemin URL dans notre projet ?

Eh bien, Astro doit prendre une décision, et c'est en suivant la liste de priorité ci-dessous :

1.  Les routes statiques, c'est-à-dire celles sans paramètres de chemin, ont la priorité la plus élevée, par exemple `/pages/products/this-is-a-product`.
2.  Les routes dynamiques avec des paramètres nommés ont la priorité suivante, par exemple `/pages/products/[id]`.
3.  Les routes dynamiques avec des paramètres rest ont la priorité la plus basse, par exemple `/pages/products/[...path]`.
4.  En suivant ce qui précède, toute égalité sera résolue par ordre alphabétique.

![Ordre de priorité des routes du premier au dernier.](https://blog.ohansemmanuel.com/content/images/2023/07/route_priority.png)
_Ordre de priorité des routes du premier au dernier._

Un exemple décent est de noter que même si le chemin dynamique `[...path.astro]` correspond au chemin racine `/blog`, la route statique `blog/index.astro` prend toujours la priorité tandis que la route dynamique `[...path.astro]` intervient pour chaque page de blog.

## Comment générer des routes avec des collections de contenu

En ce moment, nous ajoutons manuellement des objets à la fonction exportée `getStaticPaths` pour définir nos chemins de blog.

Mais notre solution souhaitée est de générer ceux-ci à partir de la collection de contenu de blog.

![Générer automatiquement des routes pour chaque entrée de collection](https://blog.ohansemmanuel.com/content/images/2023/07/auto_entry_route.png)
_Générer automatiquement des routes pour chaque entrée de collection_

Pour y parvenir, nous devons retravailler l'implémentation de `getStaticPaths` pour récupérer tous les articles de blog de la collection de contenu et générer les chemins requis.

Considérez la solution ci-dessous :

```js
---
import { getCollection } from "astro:content";
import BlogLayout from "@layouts/BlogLayout.astro";

// Make the function async
export async function getStaticPaths() {
    // Fetch all blog posts
    const allBlogPosts = await getCollection("blog");
    // Dynamically construct the blog paths
    const paths = allBlogPosts.map((blogEntry) => ({
        // construct params
        params: {
            path: `${blogEntry.data.year}/${blogEntry.data.month}/${blogEntry.data.day}/${blogEntry.slug}`,
        },
    }));

    // Eventually return the constructed paths
    return paths;
}

const { path } = Astro.params;
---

<BlogLayout title="React Blog - React" header="React Blog">
    <h1>{path}</h1>
</BlogLayout>

```

Maintenant, chaque entrée de blog a désormais un chemin associé défini. Essayez cela en cliquant sur n'importe quel lien de blog depuis la page d'accueil.

![Tous les chemins de blog sont maintenant gérés automatiquement](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-07-02-at-07.51.47.png)
_Tous les chemins de blog sont maintenant gérés automatiquement_

### Comment rendre le contenu de chaque blog

Rendre simplement le chemin du blog était excellent pour simplifier les concepts précédents, mais ce n'est pas tout à fait notre résultat.

Rendons correctement le contenu de chaque blog. D'abord, voici la solution :

```js
---
import { getCollection } from "astro:content";
import BlogLayout from "@layouts/BlogLayout.astro";

// Make the function async
export async function getStaticPaths() {
    const allBlogPosts = await getCollection("blog");
    // dynamically construct the blog paths
    const paths = allBlogPosts.map((blogEntry) => ({
        // construct params
        params: {
            path: `${blogEntry.data.year}/${blogEntry.data.month}/${blogEntry.data.day}/${blogEntry.slug}`,
        },
        // 👀 Pass blogEntry as props to be later accessed in the markup via Astro.props
        props: {
            blogEntry,
        },
    }));

    //Eventually return the constructed paths
    return paths;
}

// Get the blog entry from the props
const { blogEntry } = Astro.props;

// get blog content via entry.render()
const { Content } = await blogEntry.render();
---

<BlogLayout title="React Blog - React" header="React Blog">
    <!-- Render the Content -->
    <Content />
</BlogLayout>

```

Déconstruisons cette solution.

La pièce la plus importante du puzzle de la solution est de passer chaque entrée de blog comme une `prop` dans la fonction `getStaticPath`.

Faire cela nous permet de référencer chaque entrée dans la section balisage du composant via `Astro.props`.

Deuxièmement, chaque entrée de collection interrogée a une méthode `render()` qui rend l'entrée en `HTML`. La solution utilise cela pour rendre chaque blog.

```js
const { Content } = await blogEntry.render();
//...
<Content />

```

![Le contenu du blog rendu](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-07-02-at-08.48.36.png)
_Le contenu du blog rendu_

## Composants MDX

Revenons à MDX.

La fonctionnalité la plus impressionnante de MDX est la capacité d'utiliser des composants avec du contenu markdown standard.

Considérons des exemples pratiques.

### Éléments HTML personnalisés

Lorsque le contenu MDX est rendu en HTML, la sortie finale utilise des éléments HTML standard.

Par exemple, si nous avions le contenu MDX suivant :

```js
# Title

This is a paragraph

```

Cela donnera un résultat HTML similaire à ce qui suit :

```js
<h1>Title</h1>
<p>This is a paragraph</p>

```

La bonne nouvelle est que, au lieu de s'appuyer sur des éléments HTML standard, nous pouvons spécifier des composants à utiliser à la place des éléments HTML.

Par exemple, nous pouvons fournir nos propres composants d'en-tête et de paragraphe stylisés à la place des éléments HTML standard `h1` et `p`.

Pour ce faire, créez un objet de mappage d'élément HTML vers composant personnalisé.

```js
// sample MDX component map

// Provide custom header and paragraph
import H1 from "./H1.astro"; // custom Astro component
import P from "./P.astro" // custom paragraph component

// map of HTML element to custom component
export const mdxComponents = {
  h1: H1,
  p: P,
}

```

Maintenant, lorsque le contenu MDX est rendu en HTML, passez la carte de composants comme indiqué ci-dessous :

```js
---
import {getEntry} from 'astro:content'
// import the component map
import { mdxComponents } from '../mdxComponents'

// Get a collection entry
const blogCollection = await getEntry('blog', 'some-title')
// Get the entry Content
const { Content } = await blogEntry.render();
---

{/** Render to HTML and pass the components map**/}
<Content components={mdxComponents} />

```

Mettons cela en action.

Jetez un coup d'œil au fichier `src/components/mdxComponents.ts` dans le projet. Il contient une liste d'éléments HTML et de composants Astro personnalisés associés.

Nous importerons cet objet et le passerons à l'entrée de blog `<Content />` comme indiqué ci-dessous :

```js
// 📂 pages/blog/[...path].astro
---
import { mdxComponents } from "@components/mdxComponents";
// ... other imports
---

<BlogLayout title="React Blog - React" header="React Blog">
    {/** 👀 pass the components down to Content **/}
    <Content components={mdxComponents} />
</BlogLayout>

```

Avec cela, nous devrions maintenant avoir des composants correctement stylisés à la place des éléments HTML fades.

![Exploiter des composants personnalisés pour la sortie HTML MDX](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-07-10-at-06.39.24.png)
_Exploiter des composants personnalisés pour la sortie HTML MDX_

Considérez la liste complète des éléments HTML disponibles qui peuvent être écrasés avec des composants personnalisés dans la [documentation officielle MDX](https://mdxjs.com/table-of-components/).

### Composants internes

Les composants peuvent également être importés et directement rendus dans MDX. Cela fait partie du plaisir !

Allez-y et ouvrez la première route de blog dans `/blog/2020/12/21/data-fetching-with-react-server-components` et trouvez le premier `TODO` sur la page.

![TODO : ajouter le composant Intro](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-07-10-at-06.42.47.png)
_TODO : ajouter le composant Intro_

Pour résoudre ce TODO, nous devons importer et rendre le composant `Intro` dans `src/components/Intro.astro`.

Considérez la solution ci-dessous :

```js
// 📂 src/content/blog/data-fetching-with-react-server-components.mdx
---

import Intro from "@components/Intro.astro";

{/** First content after the frontmatter and other imports**/}
<Intro>
  2020 has been a long year. As it comes to an end we wanted to share a special
  Holiday Update on our research into zero-bundle-size **React Server
  Components**.
</Intro>
---

```

![Le composant Intro rendu](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-07-02-at-09.07.29.png)
_Le composant Intro rendu_

Nous avons importé et rendu un composant Astro directement dans le fichier MDX. C'est incroyable !

Notez que la syntaxe `---` représente des diviseurs (comme vu en 1 et 2 ci-dessus) et non des barrières de code utilisées pour définir le frontmatter markdown.

Il n'y a pas de limite au nombre de composants que nous pouvons importer et rendre dans un fichier MDX. Nous pouvons donc aller plus loin et rendre un autre composant comme indiqué ci-dessous :

```js
{/** Import the Note component **/}
import Note from "@components/Note.astro";

{/** Render at the bottom of the file **/}
<Note>React Server Components are still in research and development.</Note>

```

![Le composant Note rendu](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-07-02-at-10.43.07.png)
_Le composant Note rendu_

Notez que, contrairement aux importations JavaScript qui doivent être en haut du fichier, nous pouvons importer des composants dans un fichier MDX n'importe où en dehors de la section frontmatter.

Je préfère généralement garder les importations en haut du document juste après le frontmatter, mais vous pouvez également colocaliser les importations près de l'endroit où elles sont rendues. Les deux options fonctionnent !

### Importations externes

Nous avons vu différents composants importés dans nos documents MDX. Heureusement, cela devient encore plus amusant.

Nous pouvons également importer et rendre des composants externes, par exemple depuis NPM dans MDX.

Allez-y et installez `astro-embed`

```
npm install astro-embed

```

`astro-embed` nous permet d'intégrer des composants tels que des Tweets et des vidéos Youtube dans un projet Astro.

Dans le même blog dans `/blog/2020/12/21/data-fetching-with-react-server-components` considérez le prochain TODO :

```md
## Reference

To introduce React Server Components, we have prepared a talk
and a demo. If you want, you can check them out during the.
holidays, or later when work picks back up in the new year.

❗️TODO: Add Youtube video embed here


```

Pour résoudre cela, allez-y et importez le composant `YouTube` depuis `astro-embed` et rendez le composant avec une prop `id` comme indiqué ci-dessous :

```md
## Reference

To introduce React Server Components, we have prepared a talk and a demo. If you want, you can check them out during the holidays, or later when work picks back up in the new year.

import { YouTube } from "astro-embed";

<YouTube id=" />

```

![Le composant Youtube rendu](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-07-10-at-07.05.09.png)
_Le composant Youtube rendu_

Notez que nous colocalisons l'instruction d'importation près du rendu du composant. Mais nous pouvons également déplacer l'importation plus haut dans le fichier.

```md
{/** ✅ This is correct **/}

import { YouTube } from "astro-embed";

<YouTube id=" />

```

```md
{/** ✅ This is equally correct **/}

{/** Keep all imports on top, right after the frontmatter **/}

import Intro from "@components/Intro.astro";
import { YouTube } from "astro-embed";

{/** Render other content ... and component much later **/}

<YouTube id=" />

```

### AutoImport

Les composants `Youtube`, `Intro` et `Note` sont utilisés dans tous les blogs. Pour l'instant, importer les composants à chaque fois semble répétitif.

Avec des composants que nous voulons réutiliser dans tous nos fichiers MDX, que diriez-vous de les importer automatiquement – c'est-à-dire sans dupliquer manuellement l'importation dans chaque document MDX ?

Pour y parvenir, nous exploiterons le paquet `astro-auto-import`.

Avec `astro-auto-import`, nous pouvons facilement importer des composants ou des modules automatiquement et les utiliser dans des fichiers MDX sans avoir besoin d'importation manuelle.

Tout d'abord, installez `astro-auto-import` :

```md
npm install astro-auto-import

```

`astro-auto-import` fonctionne comme une intégration Astro. Pour l'utiliser, nous devons mettre à jour le fichier `astro.config.mjs` du projet comme indiqué ci-dessous :

```js
// other imports ...
// import AutoImport
import AutoImport from "astro-auto-import";

export default defineConfig({
  integrations: [
   // Pass AutoImport in the integrations array
    AutoImport({
      imports: [
        /**
         * Generates:
         * import Intro from './src/components/Intro.astro';
         */
        "./src/components/Intro.astro",
        "./src/components/Note.astro",
        /**
         * Generates:
         * import { YouTube } from 'astro-embed';
         */
        { "astro-embed": ["YouTube"] },
      ],
    }),
    react(),
    tailwind(),
    mdx(),
  ],
});

```

Pour utiliser `AutoImport`, nous le passons dans le tableau `integrations` et invoquons `AutoImport` avec une liste d'importations :

```js
AutoImport({
   imports: [
     "./src/components/Intro.astro",
     "./src/components/Note.astro",
     { "astro-embed": ["YouTube"] },
   ],
})

```

Les `imports` représentent une liste d'importations à ajouter automatiquement à nos fichiers MDX.

Une chaîne avec le chemin de l'importation telle que `"./src/components/Intro.astro"` générera une importation par défaut telle que `import Intro from './src/components/Intro.astro'`.

Un objet tel que `{ "astro-embed": ["YouTube"] }` génère une importation nommée telle que `import { Tweet, YouTube } from 'astro-embed'`.

Avec ceux-ci en place, nous devons maintenant supprimer les importations manuelles dans les fichiers MDX et compter sur la magie `AutoImport` ✨

Propre !

## Focus sur l'intégration : Astro SEO

Vous avez déjà vu beaucoup d'intégrations Astro. Pensez à `@astrojs/react` pour avoir des îlots React dans un projet Astro, ou l'intégration officielle `@astrojs/tailwind` pour utiliser tailwind dans Astro.

De manière générale, les intégrations ajoutent de nouvelles fonctionnalités et comportements à un projet Astro, généralement avec juste quelques lignes de code.

Cela semble être une victoire !

Dans cette section, discutons de `astro-seo`, une intégration qui rend simple l'ajout d'informations pertinentes pour le SEO à n'importe quelle application Astro.

Vous connaissez la chanson.

Tout d'abord, installez l'intégration :

```js
npm install astro-seo

```

Pour utiliser `astro-seo`, nous importons le composant `SEO` et lui passons les props pertinentes comme vu ci-dessous :

```js
// 📂 src/layouts/BaseLayout.astro
---
import { SEO } from "astro-seo";
// ...
---
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width" />
    <meta name="generator" content={Astro.generator} />

    <SEO
      title={title}
      description={description}
      openGraph={{
        basic: {
          title,
          type: "website",
          image: "https://react.dev/images/og-home.png",
        },
      }}
      twitter={{
        creator: "@reactjs",
      }}
      extend={{
        meta: [
          {
            name: "twitter:image",
            content: "https://react.dev/images/og-home.png",
          },
          { name: "twitter:title", content: "@reactjs" },
          {
            name: "twitter:description",
            content: description,
          },
        ],
      }}
    />
  {/** ... **/}
</head>
{/** ... **/}
</html>

```

Cela générera des balises méta pertinentes, y compris des balises méta open-graph pour une application plus conforme au SEO.

## Comment créer des pages 404 personnalisées dans Astro

Les pages 404 personnalisées sont faciles à comprendre dans Astro. Créez un fichier `404.astro` ou toute autre terminaison de fichier de page pertinente dans `src/pages`. Cela construira une page `404.html` que la plupart des services de déploiement utiliseront si une page invalide est demandée et non trouvée.

Faisons cela pour notre projet.

Créez une page `404.astro` dans `src/pages` avec le contenu suivant :

```js
// 📂 src/pages/404.astro
---
import BaseLayout from "@layouts/BaseLayout.astro";
---

<BaseLayout title="Redirecting ..." page="index" />

<script is:inline>
// lazy redirect. This is better done server-side: discussed in the next book's chapter
const { pathname } = window.location;

window.location.replace(`https://www.react.dev${pathname}`);
</script>

```

Notre page `404` vient avec une particularité.

Elle rend une page blanche via `<BaseLayout />` et redirige automatiquement l'utilisateur vers le chemin correspondant sur `www.react.dev`. Violà !

Essayez cela en visitant le lien de référence API sur la page d'accueil.

![Le lien de référence API](https://blog.ohansemmanuel.com/content/images/2023/07/CleanShot-2023-07-10-at-07.28.40.png)
_Le lien de référence API_

## Conclusion de ce chapitre

Construire des applications de contenu riches est tout à fait dans les cordes d'Astro. Avec les collections de contenu, nous pouvons construire de grandes applications axées sur le contenu avec organisation et confiance.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-138.png)
_Chapitre six._

# Chapitre 6 : Rendu côté serveur (SSR) dans Astro

Ce chapitre vous montrera comment activer le SSR dans un projet Astro. Nous discuterons également d'un aperçu détaillé des fonctionnalités étendues qu'offre un projet Astro rendu côté serveur.

## Ce que vous apprendrez

*   Activer le SSR dans un projet Astro.
*   Exploiter les variables d'environnement pour stocker des secrets.
*   Fournir un routage serveur flexible via des routes dynamiques.
*   Comprendre le cycle requête-réponse et ses propriétés pertinentes.
*   Tirer parti des routes API Astro pour alimenter des applications robustes.

## Quand avez-vous besoin du SSR ?

Dans un chapitre précédent, nous avons discuté de plusieurs techniques de rendu pour une application frontend. La raison était que nous puissions prendre des décisions efficaces pour choisir une technique de rendu plutôt qu'une autre.

Je résumerai brièvement pourquoi nous pouvons avoir besoin du SSR dans un projet Astro. Rappelez-vous que votre kilométrage peut varier – référez-vous donc toujours aux bases discutées dans le Chapitre 3 : Construisez votre propre îlot de composants.

Maintenant, voici des indicateurs de quand nous pouvons avoir besoin d'activer le SSR dans un projet Astro :

*   **Contenu sujet à des changements fréquents.** : Nous pouvons avoir besoin du SSR si le contenu d'une page change fréquemment, plutôt que d'utiliser une page générée statiquement qui nécessiterait une reconstruction pour chaque nouveau changement.
*   **Le besoin de points de terminaison API** : Le SSR nous permet de créer des points de terminaison API tout en gardant les données sensibles cachées des clients. Nous verrons comment faire cela plus tard dans le chapitre.
*   **Créer des pages avec un accès restreint** : Pour limiter l'accès à une page, activez le rendu serveur pour la gestion côté serveur des privilèges utilisateur.

## Comment activer le SSR dans Astro

D'accord, voici comment tout commence. Pour activer le SSR dans un projet Astro, définissez l'option de configuration `output` sur `server` dans le fichier `astro.config.mjs`.

```ts
// 📂 astro.config.mjs

import { defineConfig } from 'astro/config'


export default defineConfig({
  //This will enable SSR
  output: 'server'
})

```

Et c'est tout !

Voyons cela en action en démarrant un nouveau projet avec la commande suivante :

```ts
npm create astro@latest --  --template=minimal --yes --skip-houston ssr

```

Cela utilisera le modèle `minimal`, `--skip-houston` sautera l'animation Houston, et l'option `--yes` sautera toutes les invites et acceptera les valeurs par défaut.

Maintenant, changez de répertoire vers `ssr` et démarrez le projet :

```bash
cd ssr && npm start

```

L'application devrait s'exécuter sur un serveur local avec une seule page `index.astro`.

Si nous construisons l'application pour la production via `npm build`, nous devrions avoir la seule page `index.astro` pré-rendue, c'est-à-dire construite statiquement.

![Rendre statiquement la page index.astro.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-22-at-07.13.56.png)
_Rendre statiquement la page index.astro._

Pour réitérer, une application pré-rendue est essentiellement un site statique, c'est-à-dire – non rendu côté serveur.

Pour initier le rendu côté serveur, changeons la configuration pour inclure la propriété `output` comme indiqué ci-dessous :

```js
// 📂 src/astro.config.mjs
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  output: 'server'
});


```

Si nous réexécutons le build de production, nous aurons une erreur dans la console.

```she
[error] Cannot use `output: 'server'` without an adapter. Please install and configure the appropriate server adapter for your final deployment.

```

## Comment déployer un projet SSR

La cause profonde de l'erreur ci-dessus est que pour construire votre application pour le rendu côté serveur, la commande de build Astro doit savoir sur quel serveur vous allez finalement déployer.

Le SSR nécessite un runtime serveur, c'est-à-dire le code s'exécutant au sein du serveur qui rend nos pages Astro. Pour y parvenir, Astro fournit des adaptateurs qui correspondent à notre runtime de déploiement.

Un adaptateur permet à Astro de faire deux choses. Premièrement, déterminer l'environnement d'exécution du serveur. Deuxièmement, produire un script qui exécute le code SSR sur le runtime spécifié.

![Les besoins de l'adaptateur Astro.](https://blog.ohansemmanuel.com/content/images/2023/06/astro_adapter_needs.png)
_Les besoins de l'adaptateur Astro._

Au moment de la rédaction, les adaptateurs Astro disponibles sont Cloudfare, Deno, Netlify, NodeJS et Vercel.

Nous pouvons déployer notre projet SSR sur n'importe lequel de ces runtimes avec des adaptateurs pris en charge nativement.

Pour installer l'un de ces adaptateurs, utilisez la commande :

```bash
npx astro add [name-of-adapter]

```

`[name-of-adapter]` pourrait être `cloudfare`, `deno`, `netlify`, `node` ou `vercel`.

Je recommande de consulter la [référence officielle](https://docs.astro.build/en/guides/deploy/) pour tous les adaptateurs dont vous avez besoin dans votre projet, car il serait déraisonnable de tous les couvrir dans le livre. Ici, nous nous en tiendrons à `netlify`.

Pour ajouter l'adaptateur `netlify`, allez-y et entrez la commande suivante dans le terminal :

```bash
npx astro add netlify

```

Cela ira de l'avant et installera l'adaptateur et mettra à jour notre fichier de configuration comme suit :

```js
import { defineConfig } from "astro/config";
// 👀 look here
import netlify from "@astrojs/netlify/functions";

// https://astro.build/config
export default defineConfig({
  output: "server",
  // 👀 look here
  adapter: netlify()
});

```

Essentiellement, l'adaptateur est importé à la deuxième ligne de la config et ajouté à la propriété `adapter`.

Maintenant réexécutez la commande de build :

```js
npm run build

```

Cela construira avec succès notre projet SSR pour la production en produisant des extraits de code spécifiques à `netlify` dans le répertoire `dist` et `.netlify`.

Maintenant, nous sommes en affaires 🚀

## Utilisez le bon adaptateur

Il va sans dire que, après avoir ajouté un adaptateur, le projet doit être déployé sur l'adaptateur spécifié (ici, `netlify`) et non sur un autre fournisseur (comme `vercel`).

Utilisez le bon adaptateur pour votre runtime de déploiement.

![Déployer un adaptateur Vercel sur Netlify est incorrect.](https://blog.ohansemmanuel.com/content/images/2023/06/adapter_deploy.png)
_Déployer un adaptateur Vercel sur Netlify est incorrect._

Nos étapes de déploiement réelles varieront en fonction du runtime serveur déployé. Par exemple, pour Netlify, nous pouvons suivre les étapes décrites dans le déploiement d'un site statique au Chapitre 1. Ces étapes seront identiques pour des runtimes similaires comme Vercel.

Pour les autres runtimes, les [guides de déploiement](https://docs.astro.build/en/guides/deploy/) officiels d'Astro font un excellent travail pour expliquer les étapes de déploiement requises.

## SSR avec des pages statiques

Avec la propriété de configuration `output` définie sur `server`, chaque page de notre projet Astro sera rendue côté serveur. Mais il y a de grandes chances que nous voulions qu'une ou plusieurs pages soient générées statiquement au moment de la construction, c'est-à-dire certaines pages rendues côté serveur et d'autres pré-rendues.

![Avoir un mélange de pages rendues par le serveur et statiquement.](https://blog.ohansemmanuel.com/content/images/2023/06/hybrid_rendering.png)
_Avoir un mélange de pages rendues par le serveur et statiquement._

Dans de tels cas, nous pouvons opter pour le pré-rendu en ajoutant `export const prerender = true` à toute page qui prend en charge l'exportation de variables, par exemple `.astro`, `.mdx` `, .ts` et `.js`.

Essayons cela en créant une nouvelle page `about.astro` avec le contenu suivant :

```js
// 📂 src/pages/about.astro

---
// 👀 note the prerender export
export const prerender = true;
---

<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width" />
    <meta name="generator" content={Astro.generator} />
    <title>Astro</title>
  </head>
  <body>
    <h1>About us</h1>
  </body>
</html>


```

Avec l'exportation `prerender`, la page `about` sera rendue statiquement au moment de la construction, tandis que la page `index` reste rendue côté serveur.

Exécutez `npm run build` pour voir cela en action.

![Pages statiques et générées côté serveur dans le même projet.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-22-at-08.33.08.png)
_Pages statiques et générées côté serveur dans le même projet._

## De la requête à la réponse

L'interaction entre un client et un serveur peut être simplifiée en deux étapes :

*   le client fait une **requête**.
*   le serveur envoie une **réponse**.

Les deux entités principales dans cette interaction simplifiée sont la requête client et la réponse serveur. Heureusement, avec le rendu côté serveur, nous pouvons accéder aux détails de l'objet requête et réponse.

### L'objet Request

L'objet `Request` peut être accédé sur le global `Astro` comme indiqué ci-dessous :

```js
---
 const request = Astro.request
---

```

L'objet contient des informations sur la requête actuelle et est représenté par l'interface standard [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) de l'API fetch.

```js
interface Request extends Body {
    readonly cache: RequestCache
    readonly credentials: RequestCredentials;
    readonly destination: RequestDestination;
    readonly headers: Headers;
    readonly integrity: string;
    readonly keepalive: boolean;
    readonly method: string;
    readonly mode: RequestMode;
    readonly redirect: RequestRedirect;
    readonly referrer: string;
    readonly referrerPolicy: ReferrerPolicy;
    readonly signal: AbortSignal;
    readonly url: string;
    clone(): Request;
}

```

Par exemple, nous pouvons accéder aux en-têtes de la requête via `Astro.request.headers` et à l'URL de la requête actuelle sous forme de chaîne via `Astro.request.url`.

### L'objet Response

L'objet `Response` est l'interface correspondante représentant la réponse à une requête. Ceci est également représenté par l'interface standard [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) de l'API Fetch.

Contrairement à l'accès à l'objet sur le global `Astro`, l'objet `Response` est créé en utilisant le constructeur `Response()`.

Le constructeur `Response()` a la signature suivante :

```js
new Response(body, options)

```

Où `body` définit le corps de la réponse et `options` est un objet contenant des paramètres personnalisés à appliquer à la réponse, c'est-à-dire `status`, `statusText` et `headers`.

Par exemple, nous pourrions mettre à jour notre page `index` pour renvoyer une nouvelle réponse si nous étions vraisemblablement en bêta – représenté par une simple variable.

```js
---
const isBeta = true;

if (isBeta) {
  return new Response("app not available - check back", {
    status: 200,
    statusText: "OK!",
  });
}
---

<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width" />
    <meta name="generator" content={Astro.generator} />
    <title>Astro</title>
  </head>
  <body>
    <h1>We're live!</h1>
  </body>
</html>

```

Au lieu de renvoyer la page `HTML`, nous devrions maintenant avoir une simple réponse texte envoyée au client.

![Renvoyer une simple réponse texte au client.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-22-at-10.43.19.png)
_Renvoyer une simple réponse texte au client._

Il y a aussi un objet `response` sur le global `Astro`. Bon sang !

Mais il est important de noter que ce n'est pas la même chose que le constructeur d'objet `Response`. Donc, réécrire notre exemple pour utiliser `Astro.response` échouera.

```js
---
const isBeta = true;

if (isBeta) {
  // ❌ This is wrong and will fail
  return new Astro.response("app not available - check back", {
    status: 200,
    statusText: "Excellent!",
  });
}
---

```

![Erreur : Astro.response n'est pas un constructeur.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-22-at-11.28.52.png)
_Erreur : Astro.response n'est pas un constructeur._

C'est parce que `Astro.response` représente l'initialiseur d'objet de réponse. Il est utilisé pour définir les `options` sur la réponse du serveur, c'est-à-dire `status`, `statusText` et `headers`.

Par exemple, pour définir un en-tête personnalisé sur la réponse du serveur, nous pourrions faire ce qui suit :

```js
// 📂 src/pages/index.astro
---
Astro.response.headers.set("beta_id", "some_header_value");
---

<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width" />
    <meta name="generator" content={Astro.generator} />
    <title>Astro</title>
  </head>
  <body>
    <h1>We're live!</h1>
  </body>
</html>


```

Le serveur renverra la page `HTML` et notre en-tête personnalisé `beta_id`.

![Définir un en-tête personnalisé sur la réponse du serveur.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-22-at-11.31.50.png)
_Définir un en-tête personnalisé sur la réponse du serveur._

### Réponse de redirection

Il est assez courant de recevoir une requête client et d'effectuer une redirection sur le serveur.

Il existe deux façons d'y parvenir dans Astro.

La première consiste à exploiter l'objet `Response` standard via `Response.redirect`.

Considérez un cas où nous voulons rediriger un utilisateur vers une autre page s'il n'est pas connecté, comme indiqué ci-dessous :

```js
{/** 📂 src/index.astro **/}
---
const getIsLoggedOut = () => true;
const isLoggedOut = getIsLoggedOut();

if (isLoggedOut) {
  return Response.redirect(`${Astro.request.url}about`, 307);
}
---

```

Dans cet exemple, nous appelons `Response.redirect` tout en lui passant une URL de redirection et un code d'état, c'est-à-dire :

```js
Response.redirect(URL, status)

```

Il est important de noter que l'`URL` dans ce cas est un chemin absolu. Donc construire à partir de `Astro.request.url` qui pointe vers le chemin de base absolu, par exemple `http://localhost:3001/`.

Lorsqu'il est déconnecté, l'utilisateur sera redirigé vers la page `about` et le code d'état optionnel `307` indique une redirection temporaire.

Comme nous l'avons vu ci-dessus, construire l'URL absolue pourrait devenir inutilement complexe. Heureusement, il existe un moyen alternatif d'effectuer une redirection.

Nous pouvons également exploiter la méthode `Astro.redirect` pour rediriger vers une autre page. Par exemple, nous pourrions réécrire notre solution pour utiliser `Astro.redirect` comme indiqué ci-dessous :

```js
---
const getIsLoggedOut = () => true;
const isLoggedOut = getIsLoggedOut();

if (isLoggedOut) {
  return Astro.redirect("/about", 307);
}
---

```

Nous avons une API beaucoup plus simple ici. Nous pouvons rediriger en passant simplement le chemin relatif vers lequel rediriger. Le code d'état est également optionnel ici.

Il est important de noter que les redirections doivent être effectuées dans les composants de page, c'est-à-dire pas à l'intérieur d'autres composants comme les mises en page ou les composants de base.

### Utilitaires pour manipuler les cookies

En mode SSR, nous pouvons avoir besoin de lire ou de manipuler des cookies. Eh bien, Astro nous couvre avec `Astro.cookies`. Cela contient des utilitaires pour lire et utiliser des cookies en mode SSR.

Considérez les exemples de récupération d'un cookie :

```js
//Get an AstroCookie object
const cookieObject = Astro.cookies.get("coooookiee")

// Get the string value of the cookie
const cookieValue = cookieObject.value

// Parse the cookie value via JSON.parse. Returns an object if the cookie is a valid JSON. It throws an error otherwise.

const cookieJSON = cookieObject.json()

// Parse the cookie value as a Number
const cookieNumber = cookieObject.number()

// Parse the cookie as a boolean
const cookieBoolean = cookieObject.boolean()

```

C'est beaucoup de flexibilité !

Nous pouvons également vérifier si un cookie existe avec la méthode `has`, comme indiqué ci-dessous :

```js
// check if the "cooooookies" cookie exists. returns a boolean
const hasCookie = Astro.cookies.has('cooooookies')

```

Il est également possible de définir un cookie comme indiqué ci-dessous :

```js
// Set a cookie
Astro.cookies.set("cooookiees", "the-cookie-value")

```

La signature pour `Astro.cookies.set` est indiquée ci-dessous :

```js
// Astro.set(key, value, options)
key: string,
value: string | number | boolean | object,
options?: CookieOptions) => void

```

Notez comment différents types de valeurs de cookie peuvent être définis et des [options](https://www.npmjs.com/package/cookie#options-1) de cookie supplémentaires passées si nécessaire, par exemple `domain`, `encode`, `expires`, `maxAge` ou `httpOnly`.

### L'adresse IP de la requête

Comprendre les [adresses IP](https://www.freecodecamp.org/news/ipv4-vs-ipv6-what-is-the-difference-between-ip-addressing-schemes/) dépasse le cadre de ce livre. Mais, nous pouvons accéder à l'adresse IP de la requête sur le serveur via la propriété `Astro.clientAddress`.

Voici un exemple simple :

```js
---
const ip = Astro.clientAddress;
---

<div>Your IP address is: {ip}</div>

```

## Variables d'environnement

Si vous êtes complètement nouveau aux variables d'environnement, vous pourriez penser, _"Hé, que sont les variables d'environnement, et pourquoi devrais-je m'en soucier ?"_

De manière générale, les variables d'environnement nous aident à stocker des informations importantes comme des clés API ou des données sensibles sans jamais avoir à les révéler aux clients accédant à votre application.

Comme tout secret, les variables d'environnement peuvent être sans doute un peu délicates à gérer. Vous devez savoir exactement où les trouver, comment les utiliser, et surtout, comment les garder à l'abri des regards indiscrets.

### Comment obtenir des variables d'environnement

Dans Astro, les variables d'environnement sont accessibles sur l'objet `import.meta.env`.

Donc, par exemple, si nous avions une valeur `CAT_API_TOKEN`, nous y accéderions comme suit :

```js
---
import.meta.env.CAT_API_TOKEN
---

```

Si vous êtes familier avec les variables d'environnement dans les environnements node, vous remarquerez que cela diffère de l'objet classique `process.env`. Astro exploite Vite, qui utilise la fonctionnalité JavaScript [import.meta](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta).

### Variables d'environnement par défaut

Nous avons tous des secrets.

Eh bien, je n'en suis pas tout à fait sûr. Laissez-moi reformuler : la plupart des gens ont des secrets.

De même, chaque projet Astro a quelques secrets par défaut, alias variables d'environnement, prêts à l'emploi. Considérez les valeurs par défaut ci-dessous :

```js
// Get the mode the Astro site is running in: "development" | "production"
import.meta.env.MODE

// Is the site running in production? returns true or false
import.meta.env.PROD

// Is the site running in development? returns true or false
import.meta.env.DEV

// The base URL of the Astro site
import.meta.env.BASE_URL

// Get the final deployed URL of the Astro site
import.meta.env.SITE

// Get prefix for Astro-generated asset links
import.meta.env.ASSETS_PREFIX

```

Pour `import.meta.env.BASE_URL`, il est important de noter que cela sera par défaut `/` sauf si explicitement indiqué dans la configuration du projet. Par exemple :

```js
import { defineConfig } from 'astro/config'

export default defineConfig({
   base: '/docs'
})

```

Astro utilisera désormais `/docs` comme racine pour nos pages et actifs dans le développement et le build de production.

De même, `import.meta.env.SITE` s'appuie sur la propriété `site` définie dans la config astro, par exemple :

```js
import { defineConfig } from 'astro/config'

export default defineConfig({
   site: 'https://www.ohansemmanuel.com'
})

```

Astro utilisera cette URL complète pour générer le sitemap du site et les URL canoniques le cas échéant.

`import.meta.env.ASSETS_PREFIX` s'appuie également sur l'option `build.assetsPrefix` définie dans la config du projet, par exemple :

```js
import  defineConfig  from 'astro/config'

export default defineConfig({
  build: {
    assetsPrefix: 'https://cdn.example.com'
  }
})

```

Cela peut être utilisé si les actifs sont servis depuis un domaine différent du site actuel. Par exemple avec le préfixe `https://cdn.example.com`, les actifs seront récupérés depuis `https://cdn.example.com/_astro/...`. Cela implique que les fichiers dans le répertoire de build astro par défaut `./dist/astro` doivent être téléchargés dans le répertoire CDN pour servir les actifs.

Ouf ! Finis les secrets.

### Comment créer des variables d'environnement

Cela ne sert pas à grand-chose si nous ne pouvons pas créer nos propres secrets. Bon sang, ça aide avec le mystique.

Le moyen le plus courant de créer des variables d'environnement est d'utiliser des fichiers `.env`.

Par exemple, allons-y et créons un fichier `.env` dans le répertoire racine de notre répertoire de projet avec le contenu suivant :

```js
// 📂 src/.env
CAT_API_TOKEN="this-is-the-cat-production-token"

```

Nous pouvons ensuite accéder au secret côté serveur via `import.meta.env.CAT_API_TOKEN`.

Je dois mentionner qu'il est possible d'exposer certaines variables d'environnement au client (navigateur). Pour ce faire, préfixez la variable d'environnement avec un `PUBLIC_`, par exemple :

```js
PUBLIC_INSENSITIVE_TOKEN="this-is-public"

```

`PUBLIC_INSENSITIVE_TOKEN` sera désormais accessible à la fois sur le serveur et le client. C'est un secret de polichinelle. N'importe qui, et je dis bien n'importe qui, peut voir votre linge sale ici. N'utilisez cela que pour des variables d'environnement non sensibles.

Rappelez-vous que les variables d'environnement ne sont disponibles que dans le code côté serveur par défaut. Préfixez les variables d'environnement avec `PUBLIC_` pour les exposer au client.

Il est également possible d'exécuter votre projet et de fournir des variables d'environnement depuis la CLI, comme indiqué ci-dessous :

```bash
CAT_API_TOKEN="this-is-the-cat-production-token npm run dev"

```

Dans ce cas, `CAT_API_TOKEN` sera disponible à la fois côté serveur et côté client. À utiliser avec prudence. Nous ne confions des secrets qu'aux personnes en qui nous avons confiance et ne faisons jamais confiance aveuglément à un client, comme un navigateur utilisateur.

### IntelliSense TypeScript

Nous n'obtenons pas le support IntelliSense TypeScript si nous tentons d'accéder à `CAT_API_TOKEN` dans `pages/index.astro` après avoir créé le fichier `.env`.

![Pas d'IntelliSense Typescript pour notre variable d'environnement personnalisée.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-23-at-09.44.07.png)
_Pas d'IntelliSense Typescript pour notre variable d'environnement personnalisée._

Nous sommes des développeurs pro, alors allez – réparons cela.

Nous trouverons un fichier `src/env.d.ts` avec les projets démarrés avec un modèle Astro. Sinon, allez-y et créez-en un.

Voici le contenu initial du fichier s'il existe déjà :

```ts
/// <reference types="astro/client" />

```

Étendons l'interface par défaut `ImportMeta` qui fournit des définitions de type pour `import.meta.env` en ajoutant ce qui suit :

```ts
interface ImportMetaEnv {
  readonly CAT_API_TOKEN: string;
  // add other custom env variables...
}

```

Et voilà ! TypeScript connaît nos secrets – pour le meilleur.

![IntelliSense Typescript activé.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-23-at-09.50.10.png)
_IntelliSense Typescript activé._

## Routes dynamiques

Les routes statiques sont sans doute faciles à comprendre. Par exemple, les fichiers `.astro`, `.md` et `.mdx` dans `src/pages` deviendront automatiquement des pages sur notre site web.

Mais parfois, nous avons besoin de routes dynamiques pour éviter la répétition. Cela se produit généralement lorsque nous avons différentes routes avec des changements d'interface utilisateur minimes entre elles.

Par exemple, si nous vendions des produits sur notre site web, nous aurions une route différente pour chaque produit.

```ts
// example routes for different products
www.example.com/product/understanding-astro
www.example.com/product/astro-a-to-z
www.example.com/product/astro-for-beginners
www.example.com/product/fullstack-astro

```

```ts
// ❌ Providing multiple pages for each product
/pages/understanding-astro.astro
/pages/astro-a-to-z
/pages/astro-for-beginners
/pages/fullstack-astro

```

La structure URL des pages de produits pourrait être représentée par `www.example.com/product/${name}` où `name` signifie le nom du produit.

Au lieu de créer différentes pages pour représenter chaque produit, nous pouvons gérer dynamiquement le routage des produits de l'une des deux manières suivantes.

### 1. Paramètres nommés

Nous pourrions représenter les variables dans le chemin de la route avec un paramètre nommé entouré de crochets. Par exemple, créer un fichier dans le répertoire `pages` comme suit :

```js
/pages/products/[product].astro

```

Nous pouvons ensuite saisir la valeur du chemin `product` sur la page comme suit :

```js
{/** 📂 src/pages/[product].astro **/}
<h1>{Astro.params.product}</h1>

```

Alternativement :

```js
---
 const {product} = Astro.params
---

<h1>{product}</h1>

```

Maintenant, si nous visitons la page `/products/understanding-astro`, nous devrions avoir le titre du produit affiché.

![Saisir les valeurs de chemin de route dynamique.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-24-at-10.25.23.png)
_Saisir les valeurs de chemin de route dynamique._

Dans la plupart des cas, notre paramètre de chemin variable inclura un identifiant unique, par exemple `/pages/products/[id].astro`.

Le même routage fonctionne.

Il est également possible d'exploiter plusieurs paramètres nommés dans le chemin de la route, comme indiqué ci-dessous :

```js
{/** /products/[product]_[id].astro **/}
<h1>Product name: {Astro.params.product}</h1>
<h1>Product id: {Astro.params.id}</h1>

```

Cela correspondra à une URL similaire à `/products/understanding-astro_09u34359534530903453450`.

![Correspondance de plusieurs paramètres nommés de route.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-24-at-10.31.22.png)
_Correspondance de plusieurs paramètres nommés de route._

### 2. Paramètres rest

Les paramètres rest offrent une flexibilité ultime dans notre routage URL. Par exemple, nous pouvons utiliser `[...path]` pour faire correspondre des chemins de fichiers de n'importe quelle profondeur. Où `path` pourrait être représenté par n'importe quelle chaîne, comme `[...file]` ou `[...somestring]`.

Considérez les pages de produits suivantes :

```js
/products/product-id
/products/category/product-id/
/products/types/category/product-id

```

Les routes ci-dessus correspondront toutes à la page `pages/product/[...path].astro`, et nous pouvons accéder au chemin de chaîne dynamique complet dans notre code.

Par exemple, créez un fichier dans `/pages/product/[...path].astro` avec le contenu suivant :

```js
---
const { path } = Astro.params;
console.log({ path });
---

<h1>Hello there</h1>

```

Pour les chemins ci-dessus, la variable `path` correspond à `product-id`, `category/product-id` et `types/category/product-id`.

Avec beaucoup de pouvoir vient beaucoup de responsabilité.

Avec la flexibilité accrue que fournissent les paramètres de chemin rest vient la responsabilité de gérer les chemins dans notre code. Par exemple, considérez comment nous pouvons gérer les multiples chemins de produits ci-dessous :

```js
---
// Get the dynamic route path
const { path } = Astro.params;

// Hold a list of all expected paths and corresponding data, e.g., title.
const page = [
  {
    path: undefined,
    title: "View all products"
  },
  {
    path: "product-id",
    title: "Some Product",
  },
  {
    path: "category/product-id",
    title: "Some Product Category Item",
  },
  {
    path: "types/category/product-id",
    title: "Some Product Type Category Item",
  },
];

//Is this a valid path? i.e., exists in our list?
const relevantPageDetails = page.find((v) => v.path === path);

if (!relevantPageDetails) {
  // redirect if the dynamic page isn't valid.
  return Astro.redirect("/404");
}
---

// render the title of the page
<h1>{relevantPageDetails.title}</h1>

```

![Rendre les routes de paramètres rest.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-24-at-12.42.28@2x.png)
_Rendre les routes de paramètres rest._

Il est important de noter que si le `path` est indéfini, le chemin racine sera mis en correspondance, c'est-à-dire qu'il correspond à `pages/product`.

Bien que cela démontre l'utilisation de chemins rest dans des pages rendues côté serveur, c'est un exemple artificiel où nous avons supposé la chaîne littérale "product-id".

Dans le monde réel, la chaîne littérale sera représentée par différentes chaînes d'identifiants de produits plutôt que `product-id` – et nous pourrions ne pas savoir ce qu'elles sont à l'avance.

Comme nous l'avons fait dans la solution précédente, conserver une liste massive de tous les identifiants de produits dans notre application devient impossible à maintenir.

Pour ce cas d'utilisation, une façon d'y parvenir serait de mettre à jour notre solution pour avoir une logique de correspondance suffisamment complexe, par exemple via des expressions régulières, car nous ne connaissons pas les identifiants de produits à l'avance.

```js
---
const { path = "index" } = Astro.params;

const page = [
  {
    match: /some-regex/,
    title: "View all products",
  },
  {
    match: /some-regex/,
    title: "Some Product",
  },
  {
    match: /some-regex/,
    title: "Some Product Category Item",
  },
  {
    match: /some-regex/,
    title: "Some Product Type Category Item",
  },
];

const relevantPageDetails = page.find((v) => path.match(v.match));

if (!relevantPageDetails) {
  return Astro.redirect("/404");
}
---

<h1>{relevantPageDetails.title}</h1>

```

En tant que préférence personnelle, j'ai prêté serment de sang d'éviter les paramètres rest de chemin pour plusieurs chemins de page SSR lorsque je ne peux pas déterminer de manière déterministe les variables de chemin à l'avance.

Simple est parfois mieux.

Dans ce cas, je suggère de séparer les pages, c'est-à-dire de créer plusieurs répertoires et de laisser le routage automatique par défaut d'Astro intervenir.

Par exemple, faites correspondre le chemin `category/product-id` en créant une page dans `category/[id]` et `types/category/[id]` pour correspondre à la route `types/category/product-id`.

Elles peuvent également être composées avec une mise en page commune ou des composants partagés si elles ont des interfaces utilisateur identiques.

### Ordre de priorité

Comme nous en avons discuté ci-dessus, les chemins URL peuvent être mis en correspondance de différentes manières, alors que se passe-t-il lorsque différents chemins de fichiers correspondent au même chemin URL dans notre projet ?

Eh bien, Astro doit prendre une décision, alors passons en revue la liste de priorité ci-dessous :

1.  Les routes statiques, c'est-à-dire celles sans paramètres de chemin, ont la priorité la plus élevée, par exemple `/pages/products/this-is-a-product`.
2.  Les routes dynamiques avec des paramètres nommés ont la priorité suivante, par exemple `/pages/products/[id]`.
3.  Les routes dynamiques avec des paramètres rest ont la priorité la plus basse, par exemple `/pages/products/[...path]`.
4.  En suivant ce qui précède, toute égalité sera résolue par ordre alphabétique.

![Ordre de priorité des routes du premier au dernier.](https://blog.ohansemmanuel.com/content/images/2023/06/route_priority.png)
_Ordre de priorité des routes du premier au dernier._

## Points de terminaison serveur

Les points de terminaison serveur sont comme les armes secrètes de notre arsenal lors de l'exécution de fonctions côté serveur.

Ils peuvent être utilisés comme points de terminaison API REST pour exécuter des fonctions telles que l'accès à la base de données, les authentifications et les vérifications sans exposer de données sensibles au client, c'est-à-dire que nous pouvons exécuter en toute sécurité du code sur le serveur au moment de l'exécution dans ces fonctions.

Considérez l'état actuel de notre projet avec un répertoire `page/products`. Et si nous voulions créer une route API pour gérer certaines requêtes clients ? Comment ferions-nous cela ?

### Comment créer des points de terminaison serveur

Pour créer une route API dans le mode de sortie `server`, créez un fichier `.ts` ou `.js` dans le répertoire `pages`. En option, vous pouvez voir des points de terminaison créés avec le type de données que le point de terminaison renvoie dans le nom du fichier, par exemple `.json.ts`.

Je préfère garder les points de terminaison serveur simples et omettre les noms de fichiers supplémentaires. Allons-y et créons un fichier `api.ts` et gérons les requêtes `GET` entrantes comme indiqué ci-dessous :

```js
// 📂 pages/products/api
import type { APIRoute } from "astro";

export const get: APIRoute = (ctx) => {
  return {
    body: JSON.stringify({
      message: "Hello world",
    }),
  };
};

```

*   Notez le type `APIRoute` utilisé sur la fonction `get`. Cela représente la définition de type de fonction de route API.
*   Chaque fonction de route API reçoit un objet de contexte, par exemple représenté par `ctx`. L'[objet de contexte](https://docs.astro.build/en/reference/api-reference/#endpoint-context) contient des propriétés pertinentes que nous examinerons sous peu.
*   Comme indiqué ci-dessus, une fonction de route API peut renvoyer une réponse avec un `body`. La forme complète de la réponse est indiquée ci-dessous :
    `{`
    `body: string`
    `encoding?: 'ascii' | 'utf8' | 'utf-8' | 'utf16le' |`
    `'ucs2' | 'ucs-2' | 'base64' | 'base64url' |`
    `'latin1' | 'binary' | 'hex'`
    `}`
    Nous pouvons également renvoyer une réponse standard via l'objet Response comme indiqué ci-dessous :
    `import type { APIRoute } from "astro";`
    ``
    `export const get: APIRoute = (ctx) => {`
    `return new Response(JSON.stringify({`
    `message: "Hello world"`
    `}), {`
    `status: 200,`
    `});`
    `};`

### Détails de la requête

Accéder aux détails de l'objet requête est un jeu d'enfant avec les routes API. Par exemple, nous pouvons accéder à l'objet requête sur l'objet de contexte pour vérifier ses en-têtes, comme indiqué ci-dessous :

```js
import type { APIRoute } from "astro";

export const get: APIRoute = (ctx) => {
  // check for an Authorization header on the request
  const auth = ctx.request.headers.get("Authorization");

  // The user is unauthorised to get this resource
  if (!auth) {
    return new Response(JSON.stringify({ message: "Unauthorized" }), {
      status: 401,
    });
  }

  return new Response(JSON.stringify({ message: "Hello world" }), {
    status: 200,
  });
};

```

Nous pourrions également déstructurer les propriétés de l'objet de contexte, par exemple l'objet requête, comme indiqué ci-dessous :

```js
export const get: APIRoute = ({ request }) => {
  // ...
}

```

Bien que l'obtention de l'objet `request` soit excellente, considérez la liste complète des propriétés disponibles sur l'objet de contexte de point de terminaison :

```js
export const get: APIRoute = ({
  url,
  site,
  params,
  request,
  cookies,
  generator,
  redirect,
  clientAddress,
}) => {
  return new Response(JSON.stringify({ message: "Hello world" }), {
    status: 200,
  });
};

```

Certaines de ces propriétés devraient être familières après avoir discuté des objets requête et réponse sur le global `Astro` ; cependant, voici une brève description :

<table>
	<thead>
		<tr>
			<th>
				Propriété
			</th>
			<th>
				 Quoi ?
			</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<br>url
			</td>
			<td>
				<br>Une interface <a href="https://developer.mozilla.org/en-US/docs/Web/API/URL">URL</a> standard. <br>
			</td>
		</tr>
		<tr>
			<td>
				<br>site
			</td>
			<td>
				<br>La propriété site du fichier de configuration astro.<br>
			</td>
		</tr>
		<tr>
			<td>
				<br>params
			</td>
			<td>
				<p><br>Un objet contenant les valeurs des segments de chemin </p>

				<p>dynamiques correspondant à la requête.</p>
			</td>
		</tr>
		<tr>
			<td>
				<br>request
			</td>
			<td>
				<br>Une interface <a href="https://developer.mozilla.org/en-US/docs/Web/API/Request">Request</a> standard de l'API Fetch.<br>
			</td>
		</tr>
		<tr>
			<td>
				<br>cookies
			</td>
			<td>
				<br>Similaire à Astro.cookies. Il contient des utilitaires <br>pour lire et manipuler les cookies.
			</td>
		</tr>
		<tr>
			<td>
				<br>generator
			</td>
			<td>
				<br>Indique la version d'Astro que notre projet exécute.<br>
			</td>
		</tr>
		<tr>
			<td>
				<br>redirect
			</td>
			<td>
				<br>Similaire à Astro.redirect. <br>
			</td>
		</tr>
		<tr>
			<td>
				<br>clientAddress
			</td>
			<td>
				<br>Spécifie l'adresse IP de la requête. <br>Similaire à Astro.clientAddress
			</td>
		</tr>
	</tbody>
</table>

Les propriétés étrangères ici sont `generator`, `url` et `params`.

`generator` est facile à comprendre, tandis que `url` représente un objet [URL](https://developer.mozilla.org/en-US/docs/Web/API/URL) construit à partir de `request.url`, c'est-à-dire identique à `new URL(request.url)`.

Il convient de mentionner qu'un objet similaire peut être accédé sur le global `Astro` via `Astro.url`. Cela pourrait être utile dans les pages statiques.

Qu'en est-il de `params` ? Eh bien, cela nécessite une section séparée lorsque nous discutons des routes dynamiques.

### Routes API dynamiques

Le tissu de route dynamique sur les pages opère la même magie sur les points de terminaison API.

Par exemple, notre point de terminaison API est dans le fichier `pages/products/api`. Et si nous voulions que les requêtes clients soient faites au format : `GET /api/products/${id}` ?

Avez-vous remarqué la variable `id` ?

Dans ce cas, nous pouvons exploiter les routes dynamiques comme indiqué ci-dessous :

```js
// 📂 pages/api/products/[id]

import type { APIRoute } from "astro";

export const get: APIRoute = async (ctx) => {
  // Get the product ID
  const productId = ctx.params.id;

  try {
    const response = await fetch("https://fakestoreapi.com/products/1");
    const data = await response.json();

    return new Response(JSON.stringify({
     ...data,
     // Add the ID in the response body
     id: productId
    }), {
      status: 200,
    });
  } catch (error) {
    return new Response(JSON.stringify({
        message: "An error occurred."
      }), {
      status: 500,
    });
  }
};

```

Je vous ai peut-être surpris dans le bloc de code ci-dessus. Mais la principale différence ici est que nous contactons une API externe (pensez à récupérer des données d'une base de données) et envoyons la réponse au client.

Un autre point critique est de remarquer comment l'id spécifique est récupéré depuis `ctx.params.id`, où `ctx` représente l'objet de contexte.

Si nous faisons une requête GET à `api/products/astro-book-001`, nous devrions avoir des données renvoyées au client.

![Tester l'API produit sur hopscotch.io](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-25-at-08.57.00@2x.png)
_Tester l'API produit sur hopscotch.io_

Notez comment tout "id" passé dans le chemin de la requête est correctement récupéré, par exemple `astro-book-001`.

![L'ID produit renvoyé dans la réponse JSON.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-25-at-08.49.31@2x.png)
_L'ID produit renvoyé dans la réponse JSON._

Pour réitérer, nous pouvons obtenir les segments de chemin dans le modèle de route dynamique via `context.params` et voilà ! Nous avons notre cas d'utilisation résolu.

Passer des paramètres de requête aux requêtes `GET` n'est pas rare dans le monde réel. Bon sang, c'est même un cas d'utilisation assez courant en fait.

En supposant la requête client suivante `GET api/products/astro-book-001?version=2&publishedDate=2023-06-12`, comment gérerions-nous cela ?

Il est important de noter que `version` et `publishedDate` ne seront pas présents dans `context.params`. Mais nous pouvons les saisir depuis l'objet `URL` comme indiqué ci-dessous :

```js
// 📂 pages/api/products/[id]
export const get: APIRoute = async (ctx) => {
  const productId = ctx.params.id;

  // retrieve relevant search parameters, aka URL query parameters
  const searchParams = ctx.url.searchParams;
  const version = searchParams.get("version");
  const publishedDate = searchParams.get("publishedDate");

  try {
    const response = await fetch("https://fakestoreapi.com/products/1");
    const data = await response.json();

    // Return a new response with the retrieved
    // "version" and "publishedDate"
    return new Response(
      JSON.stringify({
        ...data,
        version,
        publishedDate,
        id: productId
       }),
      {
        status: 200,
      }
    );
  } catch (error) {
    return new Response(JSON.stringify({
	  message: "An error occurred" }), {
      status: 500,
    });
  }
};

```

Le cœur de la solution est le suivant :

```js
 // retrieve relevant search parameters, aka URL query parameters
  const searchParams = ctx.url.searchParams;
  const version = searchParams.get("version");
  const publishedDate = searchParams.get("publishedDate");

```

![Récupérer les paramètres de requête dans un point de terminaison serveur.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-25-at-09.13.04@2x.png)
_Récupérer les paramètres de requête dans un point de terminaison serveur._

### Répertoire API dédié

Au moment de la rédaction, les routes API doivent vivre dans le répertoire `pages` avec des terminaisons de fichier appropriées, par exemple `.ts` ou `.js`.

Par exemple, vous pouvez avoir `pages/anyFileName.js` agissant comme un point de terminaison serveur.

Mais je trouve plus facile (et meilleur) d'avoir mes routes API serveur dans un répertoire `pages/api` dédié au lieu de mélanger celles-ci dans d'autres routes de page.

Un avantage à cela est de rendre potentiellement plus facile la redirection d'un sous-domaine vers un chemin unique pour toutes les routes API, par exemple rediriger `api.my-website.com/...` vers `my-website.com/api/...`.

D'un autre côté, un inconvénient discutable est que nous brisons la colocation d'autres routes, par exemple les pages standard telles que `pages/products/...` auront leur route API associée dans `api/products/...`. C'est un inconvénient et un compromis que je fais volontiers dans les applications de production.

### Comment prendre en charge d'autres méthodes HTTP

Tous nos exemples jusqu'à présent ont utilisé la méthode get dans nos routes API. Mais Astro prend en charge toutes les autres méthodes HTTP, telles que post ou delete.

Considérez l'exemple suivant qui étend notre point de terminaison `api/products/${id}` pour inclure plus de méthodes :

```js
import type { APIRoute } from "astro";

// Handle client GET requests
export const get: APIRoute = async (ctx) => {
  const productId = ctx.params.id;
  try {
    // fetch remote resource
    const response = await fetch("https://fakestoreapi.com/products/1");
    const data = await response.json();

    // return data, and the id param
    return new Response(JSON.stringify({
	  ...data,
	  id: productId
    }), {
      status: 200,
    });
  } catch (error) {
    return new Response(JSON.stringify({
	  message: "An error occurred" }), {
      status: 500,
    });
  }
};

/**
 * Handle "DELETE" requests
 * "delete" is a reserved word in Javascript. Hence, the function name "del"
 */
export const del: APIRoute = async (ctx) => {
  const productId = ctx.params.id;
  try {
    const response = await fetch("https://fakestoreapi.com/products/1", {
      method: "DELETE",
    });
    const data = await response.json();

    return new Response(
      JSON.stringify({
		id: productId,
		message: "deleted",
        title: data.title }),
      {
        status: 202,
      }
    );
  } catch (error) {
    return new Response(JSON.stringify({
	  message: "An error occurred" }), {
      status: 500,
    });
  }
};

/**
 * Handle "POST" requests
 */
export const post: APIRoute = async (ctx) => {
  // Get the POST body data
  const data = await ctx.request.json();

  return new Response(JSON.stringify({
	message: "Created", data
  }));
};

```

Allez-y et essayez-les !

![Faire une requête POST à notre point de terminaison serveur.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-25-at-08.53.33@2x.png)
_Faire une requête POST à notre point de terminaison serveur._

Comme solution de repli pour gérer d'autres méthodes HTTP, nous pouvons fournir une fonction `all` pour correspondre aux méthodes qui n'ont pas de fonction exportée correspondante. Considérez l'exemple ci-dessous :

```js
...
export const all: APIRoute = async (ctx) => {
  // Get the request method
  const method = ctx.request.method;

  // Return a response
  return new Response(
    JSON.stringify({
      method,
      message: "Unsupported HTTP method",
    }),
    {
      status: 501, // unsupported
    }
  );
};

```

Cela correspondra aux méthodes non gérées dans notre implémentation, telles que les requêtes `PATCH`.

![Gérer les méthodes non prises en charge dans un point de terminaison serveur.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-25-at-08.56.25@2x.png)
_Gérer les méthodes non prises en charge dans un point de terminaison serveur._

## Streams, Oh Streams

J'ai choisi un titre ludique pour cette section car elle implique une fonctionnalité relativement moins connue d'Astro : le streaming serveur.

### Qu'est-ce que le streaming serveur ?

De manière générale, le SSR fait référence à la génération de HTML sur le serveur et à l'envoi de celui-ci à un navigateur en réponse à une requête.

En théorie, nous pouvons décomposer cela en étapes distinctes :

*   Le navigateur demande une page
*   Le serveur rend la page (et toutes les données associées)
*   Le serveur renvoie la **page entièrement formée** au navigateur
*   Le navigateur rend la page

![Serveur envoyant une page entièrement formée au client.](https://blog.ohansemmanuel.com/content/images/2023/06/send_full_page.png)
_Serveur envoyant une page entièrement formée au client._

Ce qui est important ici est de noter que le serveur génère le HTML complet de la page, et seulement alors il envoie le HTML au navigateur.

Maintenant, considérez une approche différente.

Dans la plupart des cas, certaines parties de la page HTML sont statiques et pourraient être envoyées depuis le serveur immédiatement, c'est-à-dire sans dépendre de la récupération de toutes les données pertinentes.

Et si le serveur pouvait transmettre le `HTML` au navigateur au fur et à mesure qu'il crée la page côté serveur ?

![Le serveur envoie des morceaux partiels au navigateur.](https://blog.ohansemmanuel.com/content/images/2023/06/server_send_chunks.png)
_Le serveur envoie des morceaux partiels au navigateur._

C'est le cœur du streaming : diffuser le HTML vers un navigateur au fur et à mesure que le serveur génère le HTML.

### Pourquoi devrions-nous nous en soucier ?

En théorie, les navigateurs peuvent rendre du HTML partiel et prendre en charge la réception et le rendu de données HTML par morceaux. Les utilisateurs peuvent voir et interagir avec une page au fur et à mesure qu'elle est diffusée plutôt que d'attendre que la page complète soit envoyée en un gros morceau.

Différentes applications auront besoin de diverses solutions de contournement. Mais le streaming améliore la surcharge du serveur. Le serveur n'a pas besoin d'autant de mémoire pour mettre en mémoire tampon des pages entières. Il enverra progressivement les données de page au navigateur, libérant de la mémoire pour gérer plus de requêtes et par conséquent économiser des coûts de surcharge.

C'est un excellent argument pour convaincre votre patron que le streaming est bon pour le portefeuille de l'entreprise (sauf si votre entreprise joue au jeu idiot de _brûler autant d'argent que possible_).

### Le streaming est facile mais difficile

J'ai chanté les louanges du streaming. C'est conceptuellement facile à comprendre. Mais en pratique, vous pouvez rencontrer des cas d'utilisation difficiles.

Un excellent exemple est de considérer le `<title>` d'une page qui va dans le `<head>` de notre HTML. Typiquement, le `<head>` est l'un des premiers éléments que nous diffusons au navigateur. Mais certains éléments à l'intérieur du `<head>` pourraient très bien être dynamiques, par exemple nous pouvons avoir un `<title>` sous la forme `<title>{product name} fetched from the server<title>`.

Ce qui est susceptible de se produire, c'est que nous diffusons un `<title>` obsolète avant d'obtenir finalement le nom du produit de la base de données (en supposant que la base de données est la source externe de données ici).

Ce streaming hors ordre représente certains des problèmes les plus courants auxquels nous pouvons être confrontés dans la pratique. Dans cet exemple, nous pouvons fournir un espace réservé `<title>` générique et continuer le streaming.

Une fois les données disponibles côté serveur, nous pouvons diffuser un petit `<script>` qui met à jour le titre de la page à la valeur souhaitée.

D'accord, c'est assez d'histoire. Ensuite, creusons dans le streaming dans Astro.

### Streaming serveur dans Astro

Maintenant que vous êtes convaincu (pas confus) de l'importance du streaming serveur, explorons comment fonctionne le streaming dans Astro.

Peut-être la chose la plus importante à savoir est qu'Astro prend en charge le streaming par défaut. Oui, vous avez bien entendu. Les navigateurs prennent également en charge nativement le streaming HTML.

Essentiellement, dans le template Astro, Astro diffusera le HTML qui se produit avant de frapper une limite asynchrone.

Par exemple, considérez la page de base avec un composant `<LoadPets/>` responsable de la récupération et du rendu de certaines données d'animaux de compagnie depuis une base de données.

```js
---
import LoadPets from '../components/LoadPets.astro'
---

<html>
 <head>
   <title> Petsssss! </title>
 </head>
 <body>
   <h1>This is a pet site</h1>
   <p> Consider how pets are awesome ... </p>
   <LoadPets />
 </body>
</html>

```

Dans cet exemple artificiel, Astro diffusera les sections `<head>`, `<h1>` et `<p>` au navigateur avant de s'arrêter pour récupérer les données dans `<LoadPets />` et ensuite diffuser son résultat au navigateur lorsqu'il sera prêt.

Explorons un exemple visuel.

Mettez à jour le projet `ssr` pour avoir une nouvelle page `streaming.astro` avec le contenu suivant :

```js
---
import Block from "../components/Block.astro";
---

<html>
  <head>
    <title>Streaming</title>
  </head>
  <body>
    <Block text="Block #1" delay={1000} />
    <Block text="Block #2" delay={2000} />
    <Block text="Block #3" delay={3000} />
    <Block text="Block #4" delay={4000} />
    <Block text="Block #5" delay={5000} />
  </body>
</html>


```

Le composant `<Block/>` reçoit une prop `text` et une prop `delay`. `delay` représente combien de temps attendre avant de rendre son template, c'est-à-dire simuler un appel de requête réseau.

Voici le composant `<Block/>` :

```js
{/** 📂 src/components/Block.astro **/}
---
import { sleep } from "../sleep";

interface Props {
  text: string;
  delay: number;
}

const { text, delay } = Astro.props;

await sleep(delay);
---

<div>
  {text}
</div>

<style>
  div {
    margin: 1rem 0;
    padding: 2rem 6rem;
    border-radius: 10px;
    background-color: blanchedalmond;
  }
</style>

```

Où `sleep` est un utilitaire comme suit :

```js
// 📂 src/sleep.ts
export const sleep = (delay: number) =>
  new Promise((r) => setTimeout(r, delay));

```

Maintenant, allez sur le navigateur Chrome et visitez la route `/streaming` pour voir les merveilles du streaming.

![Bloc initial diffusé en attendant le Bloc #2](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-26-at-11.47.56.png)
_Bloc initial diffusé en attendant le Bloc #2_

Chaque bloc de contenu arrive un par un.

Il est important de noter que nous n'avons pas à abstraire les morceaux asynchrones dans des composants. Le streaming fonctionne également avec des promesses standard dans le template Astro :

```js
// 📂 src/pages/streaming_blocks
---
import Block from "../components/Block.astro";
import { sleep } from "../sleep";

const block5Promise = async () => {
  await sleep(1000);
  return "Block #5";
};
---

<html>
  <head>
    <title>Streaming</title>
  </head>
  <body>
    <Block text="Block #1" delay={1000} />
    <Block text="Block #2" delay={2000} />
    <Block text="Block #3" delay={3000} />
    <Block text="Block #4" delay={4000} />
    <p>{block5Promise}</p>
  </body>
</html>

```

Un fait important à noter ici est qu'Astro initie les récupérations asynchrones en parallèle lorsque des composants asynchrones frères sont dans l'arbre des composants.

Donc dans notre exemple, `Block #1` à `Block #5` commencent à récupérer des données en parallèle et ne se bloquent pas les uns les autres.

Lorsque `Block #4` est rendu, `block5Promise` est déjà récupéré car cela prend une seconde par rapport aux quatre secondes de `Block #4`. Donc le résultat de `block5` est diffusé aux côtés de `Block #4`.

Cela peut être difficile à saisir via des descriptions textuelles, alors voici un visuel :

![Décrire le rendu parallélisé de chaque bloc.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-25-at-13.44.47@2x.png)
_Décrire le rendu parallélisé de chaque bloc._

Jetez un coup d'œil dans votre navigateur Chrome.

### Comment tirer parti du streaming

Puisque Astro prend en charge le streaming par défaut, le comprendre et l'appliquer est la première étape pour tirer parti du streaming.

Considérez l'exemple suivant :

```js
---
import { sleep } from "../sleep";

const getSomeData = async () => {
  await sleep(1000);
  return "some data ";
};

const getSomeOtherData = async () => {
  await sleep(200);
  return "another data";
};

const data = await getSomeData();
const otherData = await getSomeOtherData();
---

<html>
  <head>
    <title>Product</title>
  </head>
  <body>
    <h2>A name</h2>
    <p>{data}</p>
    <h2>A fact</h2>
    <p>{otherData}</p>
  </body>
</html>

```

Dans l'exemple ci-dessus, nous avons vraisemblablement besoin de récupérer deux ressources, `data` et `otherData`. Mais notre solution bloque le streaming. Nous attendons `await getSomeData()` et `await getSomeOtherData()` avant d'envoyer la page complète au navigateur.

Si nous voulions tirer parti du streaming serveur, nous pourrions soit rendre les promesses directement dans le balisage :

```js
---
import { sleep } from "../sleep";

const getSomeData = async () => {
  await sleep(1000);
  return "some data ";
};

const getSomeOtherData = async () => {
  await sleep(200);
  return "another data";
};
---

<html>
  <head>
    <title>Product</title>
  </head>
  <body>
    <h2>A name</h2>
    <p>{getSomeData}</p>
    <h2>A fact</h2>
    <p>{getSomeOtherData}</p>
  </body>
</html>

```

Ou extraire la récupération de données vers des composants enfants :

```js
---
import Data from '../components/Data.astro'
import OtherData from '../components/OtherData.astro'
---

<html>
  <head>
    <title>Product</title>
  </head>
  <body>
    <h2>A name</h2>
    <!-- Handle fetch of data in <Data /> -->
    <Data />
    <h2>A fact</h2>
    <!-- Handle other data fetch in <OtherData /> -->
    <OtherData />
  </body>
</html>

```

Excellent !

## Conclusion de ce chapitre

Le rendu côté serveur est puissant et ouvre de nombreuses opportunités dans notre application. Mais avec beaucoup de pouvoir vient la responsabilité.

Donc, avant d'envisager de rendre chaque page de votre application rendue par le serveur, considérez les avantages et les inconvénients (comme discuté au Chapitre 3). Ensuite, prenez la bonne décision pour votre application — c'est là que réside la vraie responsabilité. Et n'oubliez pas de tirer parti du rendu hybride lorsque c'est possible.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-139.png)
_Chapitre sept._

# Chapitre 7 : Soyez Audible ! (Comment construire un projet Astro Fullstack)

> … Les gens croiront ce qu'ils voient. Laissez-les voir. ― Henry David Thoreau

Dans ce chapitre, je vous demanderai de voir au-delà des applications statiques et de construire une application full stack avec Astro. Pour voir l'application complète, consultez le [dépôt GitHub](https://github.com/understanding-astro/react.dev-astrohttps://github.com/understanding-astro/fullstack-astro).

## Ce que vous apprendrez

*   La capacité d'ajouter l'authentification à une application Astro.
*   Une compréhension de la configuration d'un backend pour une application Astro.
*   Une connaissance pratique de la gestion des soumissions de formulaires sans routes API dédiées.
*   Une expérience pratique du téléchargement et de la récupération de données dans une application Astro.
*   Une compréhension du type d'applications que vous pouvez construire avec Astro.

## Configuration du projet

Nous avons vu comment construire des sites statiques avec Astro. Donc, pour rendre cette section focalisée sur le scripting et les fonctionnalités Astro, j'ai configuré un site statique pour que nous travaillions dessus ici.

Le site a été dépouillé de toute fonctionnalité pertinente. Nous les construirons étape par étape ensemble.

Commencez par cloner le projet :

```bash
git clone https://github.com/understanding-astro/fullstack-astro

```

Changez de répertoire :

```bash
cd fullstack-astro

```

Vous devriez être sur la branche `clean-slate` par défaut. Sinon, passez à `clean-slate`.

Ensuite, installez les dépendances et démarrez l'application :

```bash
npm install && npm run start

```

L'application devrait s'exécuter avec succès sur l'un des ports du serveur local.

![L'application BeAudible initialisée.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-29-at-11.59.17@2x.png)
_L'application BeAudible initialisée._

## Aperçu du projet

Notre application est pour une startup hypothétique, BeAudible. Sa mission est de découvrir les voix du monde.

En termes techniques, BeAudible permet aux utilisateurs autorisés de créer des enregistrements audio, de les télécharger sur leurs serveurs et d'avoir une chronologie où les gens peuvent écouter les enregistrements de tout le monde.

![Un aperçu de l'application BeAudible.](https://blog.ohansemmanuel.com/content/images/2023/06/beaudible-overview.png)
_Un aperçu de l'application BeAudible._

Le projet que nous venons de cloner recevra et téléchargera l'enregistrement d'un utilisateur et affichera finalement chaque enregistrement sur une chronologie partagée.

Explorons les pages du projet.

### La page d'accueil

Tout d'abord, considérez la page d'accueil, c'est-à-dire la route de base `/`.

![Les sections de l'application BeAudible.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-29-at-11.59.17@2x-1.png)
_Les sections de l'application BeAudible._

1.  La barre de navigation contient un formulaire de commentaires pour que les utilisateurs envoient leurs pensées.
2.  La barre de navigation inclut un lien d'enregistrement pour naviguer vers une page dédiée à l'enregistrement de l'audio d'un utilisateur.
3.  La barre de navigation contient un bouton de déconnexion. Par implication, la page d'accueil devrait être protégée, c'est-à-dire que seuls les utilisateurs authentifiés devraient atterrir ici.
4.  Enfin, au centre de la page se trouve la chronologie qui devrait lister tous les enregistrements des utilisateurs.

### La page d'enregistrement

Si vous cliquez sur "Record" depuis la barre de navigation, vous serez dirigé vers la route `/record` où un utilisateur peut enregistrer son audio.

![La page d'enregistrement.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-29-at-12.24.30.png)
_La page d'enregistrement._

Un composant React hydraté dans l'application Astro alimente l'élément d'interface utilisateur d'enregistrement.

### La page d'inscription

Maintenant, allez à la route `/signup`.

![La page d'inscription.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-29-at-12.22.45.png)
_La page d'inscription._

C'est la page pour inscrire les utilisateurs à BeAudible.

### La page de connexion

Enfin, visitez la route `/signin`.

![La page de connexion.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-29-at-12.21.59.png)
_La page de connexion._

C'est la page pour que les utilisateurs précédemment authentifiés se connectent à l'application.

Allez-y et tuez l'application en cours d'exécution depuis le terminal. Ensuite, nous continuerons avec une certaine configuration.

### Composants d'aide et utilitaires

Pour nous assurer que notre attention reste sur Astro, j'ai créé des composants UI et les ai stockés dans le dossier `src/components`.

Nous importerons et utiliserons ces composants pour développer notre solution au fur et à mesure.

De même, les constantes ont été stockées dans `src/constants` et les scripts utilitaires dans `src/scripts`. Nous visons à nous concentrer sur l'objectif critique de ce chapitre, qui est de construire une application full stack avec Astro.

## Choix technologiques

1.  **Firebase** comme service backend : nous pouvons choisir n'importe quel service backend avec Astro, mais nous utiliserons Firebase pour la simplicité. Les principes dont nous discuterons fonctionnent avec tout autre service préféré. Nous exploiterons les services d'authentification et de stockage cloud de Firebase.
2.  **Tailwind** pour le style : Tailwind est célèbre pour le style des applications. Au lieu d'écrire les styles manuellement, le projet utilise Tailwind.
3.  **Astro** comme framework web principal : Bien sûr, le framework web de choix pour notre application est Astro. Pas de questions posées ! Mais nous exploiterons également des composants React pour des îlots d'interactivité.

## Configuration du backend

Tournons notre attention vers la configuration de notre serveur backend. Rappelez-vous, nous utiliserons Firebase comme service backend.

Allez sur la [page d'accueil de Firebase](https://firebase.google.com/) et visitez la console Firebase.

![La page d'accueil de Firebase.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-26-at-12.35.06@2x.png)
_La page d'accueil de Firebase._

Le processus est beaucoup plus fluide si vous avez (et êtes connecté à) un compte Google (par exemple, Gmail).

Ensuite, créez un nouveau projet Firebase.

![Créer un nouveau projet Firebase.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-26-at-12.36.54@2x.png)
_Créer un nouveau projet Firebase._

Nommez le projet `BeAudible` et choisissez d'utiliser Google Analytics dans le projet.

![Choisir Google analytics et créer le projet.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-26-at-12.41.10@2x.png)
_Choisir Google analytics et créer le projet._

Après avoir créé le projet avec succès, ajoutez une application web au projet Firebase.

![Ajouter une application web au projet Firebase.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-26-at-12.51.18@2x.png)
_Ajouter une application web au projet Firebase._

Maintenant, continuez le processus de configuration de l'application web en choisissant un nom (de préférence le même qu'avant), en configurant l'hébergement Firebase et en enregistrant l'application web.

![Continuer la configuration de l'application.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-26-at-12.53.46@2x.png)
_Continuer la configuration de l'application._

L'étape suivante est critique.

**Copiez la configuration Firebase de votre application web**. Nous utiliserons cela pour initialiser l'application Firebase côté client.

![Copier la configuration Firebase pour le SDK client.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-26-at-12.59.41@2x.png)
_Copier la configuration Firebase pour le SDK client._

Les étapes suivantes sont optionnelles. Suivez l'invite guidée de Firebase et continuez vers la console Firebase.

![Suivre l'invite guidée de Firebase.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-26-at-13.02.36@2x.png)
_Suivre l'invite guidée de Firebase._

Une fois terminé, nous serons redirigés vers le tableau de bord de l'application Firebase.

Allez dans les paramètres du projet, trouvez la section compte de service et générez une nouvelle clé privée que nous exploiterons dans notre serveur d'application.

![Aperçu du projet > Paramètres du projet](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-27-at-11.26.30.png)
_Aperçu du projet &gt; Paramètres du projet_

![Générer une nouvelle clé privée.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-27-at-11.28.49.png)
_Générer une nouvelle clé privée._

Cela téléchargera un fichier JSON sur votre machine. Gardez-le en sécurité car il donne accès au service de Firebase. Nous exploiterons cela pour accéder aux ressources serveur de Firebase depuis notre serveur d'application.

## Comment gérer l'authentification

De manière générale, l'authentification est une affaire sérieuse et peut prendre différentes formes.

Firebase fournit un service d'authentification, nous exploiterons donc ses bibliothèques clientes pour authentifier l'utilisateur côté client.

![Processus d'authentification simplifié.](https://blog.ohansemmanuel.com/content/images/2023/06/simple-auth-flow.png)
_Processus d'authentification simplifié._

L'authentification client communiquera avec les serveurs de Firebase, mais plus tard, nous examinerons la vérification du jeton d'authentification d'un utilisateur (JWT) sur notre serveur.

Tout d'abord, configurez l'application Firebase pour recevoir les demandes d'authentification client.

Revenez à la console Firebase et configurez l'authentification.

![Sélectionner l'authentification dans la liste des services fournis.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-26-at-15.13.50@2x.png)
_Sélectionner l'authentification dans la liste des services fournis._

Firebase fournit différentes méthodes de connexion. Gardons cela simple. Activez la méthode Email et mot de passe depuis la console Firebase.

![Sélectionner la méthode de connexion par email / mot de passe.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-26-at-15.15.36@2x.png)
_Sélectionner la méthode de connexion par email / mot de passe._

Assurez-vous d'activer l'option et d'appuyer sur enregistrer.

![Activer et enregistrer la méthode de connexion par Email / Mot de passe.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-26-at-15.16.33@2x.png)
_Activer et enregistrer la méthode de connexion par Email / Mot de passe._

### Comment initialiser Firebase sur le client

`src/scripts/firebase/init.ts` contient le script d'initialisation pour notre application client.

Le code responsable de l'initialisation de l'application est indiqué ci-dessous :

```js
// ...
// 📂 src/scripts/firebase/init.ts
export const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);

```

Le script exporte l'application initialisée via `app` et le module client d'authentification via `auth` où `initializeApp` et `getAuth` sont des méthodes importées du SDK Firebase.

Nous devons maintenant remplacer la variable `firebaseConfig` par l'objet copié lors de l'initialisation de l'application Firebase.

![La configuration client firebase.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-26-at-12.59.41@2x-1.png)
_La configuration client firebase._

Une fois cela fait, nous devrions avoir le client Firebase correctement initialisé.

### Comment utiliser les émulateurs Firebase

Parler aux services de production firebase tout en testant et en développant localement est plutôt idiot.

![Envoyer des requêtes aux serveurs de production Firebase tout en développant localement.](https://blog.ohansemmanuel.com/content/images/2023/06/talk-to-prod-firebase.png)
_Envoyer des requêtes aux serveurs de production Firebase tout en développant localement._

Au lieu de cela, nous pouvons utiliser la suite d'émulateurs Firebase tout en développant localement. La suite d'émulateurs interceptera nos demandes de service Firebase et fournira un terrain d'essai localement sans frapper les services de production.

J'ai configuré le projet pour utiliser les émulateurs Firebase. Alors faisons-le fonctionner.

Assurez-vous d'avoir les outils CLI Firebase installés. Si vous ne les avez pas, installez la CLI via la commande suivante :

```bash
npm install -g firebase-tools

```

En supposant que vous avez l'application en cours d'exécution dans un onglet de votre terminal, ouvrez un autre onglet et exécutez le script firebase `emulators` pour démarrer les émulateurs firebase :

```bash
npm run emulators

```

Cela démarrera les émulateurs d'authentification et de stockage avec une interface utilisateur fonctionnant sur `localhost:4001`. Nous pouvons voir les données de développement dans l'interface utilisateur de l'émulateur, par exemple les inscriptions d'utilisateurs d'application et les enregistrements téléchargés.

![Démarrer les émulateurs Firebase.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-29-at-15.06.19.png)
_Démarrer les émulateurs Firebase._

### Comment gérer les inscriptions d'utilisateurs

Alors, comment allons-nous gérer les inscriptions d'utilisateurs ?

Veuillez considérer le diagramme de flux global ci-dessous :

![Le flux d'inscription.](https://blog.ohansemmanuel.com/content/images/2023/06/sign-up-flow.png)
_Le flux d'inscription._

*   Le flux démarre avec l'utilisateur soumettant le formulaire d'inscription.
*   Ensuite, vérifiez si l'email et le mot de passe soumis sont valides.
*   Si les valeurs du formulaire sont invalides, affichez une erreur.
*   Créez un nouvel utilisateur via la méthode `createUserWithEmailAndPassword` du module d'authentification Firebase.
*   Si la création du nouvel utilisateur échoue, affichez une erreur.
*   Sinon, notre nouvel utilisateur est maintenant dans un état connecté.
*   Saisissez le jeton d'authentification utilisateur (c'est appelé jeton ID dans le jargon Firebase et représente un JSON Web Token (JWT)).
*   Redirigez l'utilisateur vers la page d'accueil avec le jeton comme paramètre URL, c'est-à-dire `/?token=${USER_AUTH_TOKEN}`.

Avant de plonger dans le code pour savoir comment faire cela, je voudrais souligner que le projet a un alias de module configuré pour éviter les importations relatives embêtantes, par exemple :

```js
// This ...
import { auth } from "../../firebase/init"

// Becomes this ...
import { auth } from "@scripts/firebase/init";

```

Cela est réalisé en mettant à jour le fichier `tsconfig.json` pour inclure l'alias :

```js
// 📂 tsconfig.json
{
   // ...
    "baseUrl": ".",
    "paths": {
      "@components/*": ["src/components/*"],
      "@layouts/*": ["src/layouts/*"],
      "@scripts/*": ["src/scripts/*"],
      "@stores/*": ["src/stores/*"],
      "@constants/*": ["src/constants/*"]
    }
  }
}

```

Nous référencerons les modules existants dans le projet via l'alias de module pertinent.

Maintenant, voici le code annoté pour gérer l'inscription de l'utilisateur :

```html
<!-- 📂 src/pages/signup.astro -->
<script>
  // import the Validator from the tiny "validator.tool" library
  import Validator from "validator.tool";
  import { createUserWithEmailAndPassword } from "firebase/auth";
  // Import the auth module from `src/scripts`
  import { auth } from "@scripts/firebase/init";
  // Import basic form validation rules
  import { authClientValidationRules } from "@scripts/authClientValidationRules";

 // Type alias for the form values
  type FormValues = {
    email?: string;
    password?: string;
  };

  // Grab the submit button element
  const submitButton = document.getElementById(
    "submit-signup-form"
  ) as HTMLButtonElement | null;

  // Grab the form element
  const form = document.getElementById("signup-form") as HTMLFormElement | null;

   // Initialise the validator
  const validator = new Validator({
    form,
    // Pass in basic rules already existing in the project
    rules: authClientValidationRules,
  });


  if (validator.form) {
    // Attach a submit event handler on the form
    validator.form.onsubmit = async (evt) => {
      evt.preventDefault();

      const errors = validator.errorMessages;
      const values = validator.getValues() as FormValues;

      //Check for errors
      if (Object.keys(errors).length > 0) {
        const errorMessages = Object.values(errors).join("...and...");
        return alert(errorMessages);
      }

      const { email, password } = values as Required<FormValues>;

      if (!submitButton) {
        return alert("Missing form button");
      }

      try {
        // Show submitting state
        submitButton.innerText = "Submitting";
        submitButton.disabled = true;

        // Create the new user
        const { user } = await createUserWithEmailAndPassword(
          auth,
          email,
          password
        );

 		// redirect the user to the homepage with their token
        const token = await user.getIdToken();
        window.location.href = `/?token=${token}`;
      } catch (error) {
        submitButton.innerText = "Signup";
        submitButton.disabled = false;

        alert(error);
      }
    };
  }
</script>

```

Dans la solution ci-dessus, nous gérons la validation du formulaire via [validator.js](https://github.com/jaywcjlove/validator.js) mais nous aurions pu utiliser n'importe quelle autre bibliothèque. Une autre bibliothèque agnostique au framework minimale qui fait un bon choix est [Felte](https://github.com/pablo-abc/felte).

### Comment gérer la connexion utilisateur

Avec l'inscription utilisateur gérée, le processus de connexion utilisateur est le même à l'exception d'un changement. Au lieu d'appeler la méthode `createUserWithEmailAndPassword`, nous utiliserons la méthode d'authentification Firebase `signInWithEmailAndPassword`.

Remarquez comment le flux est identique dans le code ci-dessous :

```html
<!-- 📂 src/pages/signin.astro -->
<!-- ... -->

<script>
  import { signInWithEmailAndPassword } from "firebase/auth";
  import Validator from "validator.tool";
  import { auth } from "@scripts/firebase/init";
  import { authClientValidationRules } from "@scripts/authClientValidationRules";

  type FormValues = {
    email?: string;
    password?: string;
  };

  const form = document.getElementById("signin-form") as HTMLFormElement | null;
  const submitButton = document.querySelector(
    "#signin-form button[type='submit']"
  ) as HTMLButtonElement | null;

  const validator = new Validator({
    form,
    rules: authClientValidationRules,
  });

  if (validator.form) {
    validator.form.onsubmit = async (evt) => {
      evt.preventDefault();

      const errors = validator.errorMessages;
      const values = validator.getValues() as FormValues;

      if (Object.keys(errors).length > 0) {
        const errorMessages = Object.values(errors).join("...and...");
        return alert(errorMessages);
      }

      const { email, password } = values as Required<FormValues>;

      if (!submitButton) {
        return alert("Missing form button");
      }

      try {
        submitButton.innerText = "Submitting";
        submitButton.disabled = true;

        const { user } = await signInWithEmailAndPassword(
          auth,
          email,
          password
        );

        const token = await user.getIdToken();
        window.location.href = `/?token=${token}`;
      } catch (error) {
        submitButton.innerText = "Signin";
        submitButton.disabled = false;

        alert(error);
      }
    };
  }
</script>

```

Avec ceux-ci en place, nous avons l'authentification gérée !

Mais une question qui peut rester dans votre cœur est, pourquoi exactement envoyons-nous le jeton utilisateur dans l'URL de redirection de la page d'accueil ?

## Comment implémenter des pages protégées

Chaque page de notre application est générée statiquement à l'exception de `index.astro`, c'est-à-dire la page d'accueil.

La page d'accueil est rendue côté serveur car nous voulons nous assurer qu'elle est protégée, et que seuls les utilisateurs authentifiés atterrissent ici.

Nous discuterons de la façon dont nous y parviendrons, mais d'abord nous devons écrire du code qui s'exécute sur le serveur ici.

### Comment initialiser Firebase sur le serveur

Pendant l'initialisation du projet, nous avons téléchargé une clé privée pour l'accès au serveur. C'est un fichier JSON sous la forme :

```js
{
  type: "...",
  project_id: "..."
   // more properties
}

```

Nous avons besoin de ces valeurs pour initialiser notre application serveur. Alors, créez un fichier `.env` pour stocker ces secrets. Ensuite, nous décomposerons les clés JSON en variables d'environnement individuelles comme indiqué ci-dessous :

```js

FIREBASE_PRIVATE_KEY_ID="..."
FIREBASE_PRIVATE_KEY="..."
FIREBASE_PROJECT_ID="..."
FIREBASE_CLIENT_EMAIL="..."
FIREBASE_CLIENT_ID="..."
FIREBASE_AUTH_URI="..."
FIREBASE_TOKEN_URI="..."
FIREBASE_AUTH_PROVIDER_CERT_URL="..."
FIREBASE_CLIENT_CERT_URL="..."

```

Enregistrez le fichier `env`. Sans cela, nous ne pourrons pas accéder aux ressources de l'application depuis notre serveur.

✨ Fait amusant : Comme discuté au Chapitre 5, nous fournissons un support TypeScript pour ces valeurs d'environnement dans `.env.d.ts`.

### Comment protéger la route de la page d'accueil

Une fois qu'un utilisateur s'est connecté avec succès, Firebase génère un jeton ID unique qui sert d'identifiant unique et donne accès à diverses ressources, telles que le stockage cloud Firebase.

J'ai vaguement appelé cela des jetons d'authentification. Nous utiliserons ce jeton ID pour reconnaître l'utilisateur sur notre serveur.

✨ Fait amusant : Les jetons ID Firebase sont de courte durée et durent une heure.

Considérez le flux ci-dessous :

![Le flux de route protégée.](https://blog.ohansemmanuel.com/content/images/2023/06/protected-route-flow.png)
_Le flux de route protégée._

*   Le flux démarre avec l'utilisateur atterrissant sur la page d'accueil.

Notez que les étapes suivantes sont effectuées sur le serveur, c'est-à-dire dans la section frontmatter de notre page rendue côté serveur.

*   Ensuite, récupérez le jeton ID utilisateur depuis l'URL (premier utilisateur) ou les cookies de requête (utilisateur de retour).
*   Vérifiez la validité du jeton. Nous utiliserons le SDK serveur Firebase (Firebase admin) pour vérifier cela.
*   Si le jeton est invalide ou n'existe pas, l'utilisateur n'est pas autorisé. Redirigez-le vers la page `/signin`.
*   Si le jeton est valide, définissez le `token` comme un cookie.

✨Fait amusant : en définissant le jeton via des cookies, nous pouvons supprimer le jeton de l'URL et rafraîchir sans perdre l'état connecté de l'utilisateur. Chaque requête renverra le cookie au serveur, où nous pourrons revérifier sa validité.

Maintenant, voici l'implémentation :

```js
// 📂 src/pages/index.astro
---
// ...
import { serverApp } from "@scripts/firebase/initServer";
import { getAuth } from "firebase-admin/auth";
import { TOKEN } from "@constants/cookies";

// Get client token from the URL param
const url = new URL(Astro.request.url);
const urlTokenParam = url.searchParams.get("token");

// Get token from cookies
const cookieToken = Astro.cookies.get(TOKEN);
const token = urlTokenParam || cookieToken.value;

if (!token) {
  // Unauthorised user. Redirect to sign in
  return Astro.redirect("/signin");
}

const auth = getAuth(serverApp);

try {
  // verify the auth token
  await auth.verifyIdToken(token);

  // set token cookie
  // Note that the "TOKEN" constant refers to the string "X-Token."
  Astro.cookies.set(TOKEN, token, {
    path: "/",
    httpOnly: true,
    secure: true,
  });
} catch (error) {
  console.error("Could not decode token", {
    fromCookie: !!cookieToken.value,
    fromUrl: !!urlTokenParam,
  });

  // Error occurred, e.g., invalid token. Redirect to sign in
  return Astro.redirect("/signin");
}
---

```

![Le cookie de jeton défini dans la réponse du navigateur.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-29-at-15.41.52.png)
_Le cookie de jeton défini dans la réponse du navigateur._

### Comment mettre à jour l'URL de redirection

Lorsqu'un utilisateur se connecte avec succès, l'utilisateur ressemble à quelque chose comme `localhost:3000/?token=${some-long-string}`.

Après avoir effectué notre validation de jeton sur le serveur et renvoyé la page `HTML` protégée, nous pouvons mettre à jour l'URL pour supprimer le paramètre `token`.

```js
// Before
localhost:3000/?token=${some-long-string}

// After
localhost:3000

```

Ce n'est pas nécessaire, mais une belle touche UX.

Puisque nous voulons faire cela sur le client, notre solution de prédilection est d'ajouter un `<script>` client à la page.

Considérez la solution ci-dessous :

```html
<!-- 📂 src/pages/index.astro -->
<!-- ... -->

<script>
  // Enhancement: remove the token from the URL after the page's parsed.
  const url = new URL(window.location.href);
  const urlTokenParam = url.searchParams.get("token");

  if (urlTokenParam) {
    // delete the token param from the URL
    url.searchParams.delete("token");

   // update history without a refresh with the new URL
    window.history.pushState({}, "", url.href);
  }
</script>

```

La solution est sans doute facile à comprendre, le point crucial après avoir obtenu le paramètre de recherche étant `window.history.pushState(...).`

### Comment déconnecter un utilisateur de la page protégée

La section supérieure gauche de la barre de navigation de l'application comprend un bouton de déconnexion. Lorsqu'un utilisateur clique dessus, nous le déconnecterons de l'application.

Pour déconnecter un utilisateur, nous utiliserons le SDK client Firebase pour déconnecter un utilisateur de l'appareil.

Mais rappelez-vous que la page d'index protégée vérifie la valeur du cookie de requête `token`.

Lorsque nous déconnectons un utilisateur en utilisant le SDK client Firebase, le `token` client émis reste valide jusqu'à une heure (selon le moment où il a été émis).

Alors, considérez le flux pour notre solution ci-dessous :

![Le flux de déconnexion utilisateur.](https://blog.ohansemmanuel.com/content/images/2023/06/sign-out-flow.png)
_Le flux de déconnexion utilisateur (Cliquer sur le bouton de déconnexion, faire une requête au point de terminaison API, déconnecter l'utilisateur, rediriger l'utilisateur vers la page de connexion)_

Commençons notre implémentation en mettant à jour l'application client pour gérer l'événement de clic sur le bouton de déconnexion et initier notre flux comme indiqué ci-dessous :

```html
<!-- 📂 src/pages/layouts/BaseLayout.astro -->
<!-- ... -->
<script>
  import { auth } from "@scripts/firebase/init";

   // Grab the sign-out button
  const signoutButton = document.getElementById("sign-out-button") as
    | HTMLButtonElement
    | undefined;

  if (signoutButton) {
    // Add a click event listener on the button
    signoutButton.addEventListener("click", async () => {
      try {
        // Disable the button while we log the user out
        signoutButton.disabled = true;
        // Change button text to read "Signing out ..."
        signoutButton.innerText = "Signing out ...";
        // Invalidate server http cookie
        const response = await fetch("/api/auth/signout", {
          method: "POST",
        });

        if (!response.ok) {
          throw new Error("server signout failed");
        }
		/**
 		* sign the user out via the signOut method
		* on the Firebase auth module
		*/
        await auth.signOut ();
		// Redirect to the signin page
        window.location.href = "/signin";
      } catch (error) {
        signoutButton.disabled = false;
        alert(error);
      }
    });
  }
</script>

```

Nous faisons une requête à `/api/auth/signout`, mais la route API n'existe pas.

Changeons cela avec le code suivant :

```js
// 📂 src/pages/api/auth/signout.ts
// ...

import { TOKEN } from "@constants/cookies";

export const post: APIRoute = (ctx) => {
  ctx.cookies.delete(TOKEN, {
    path: "/",
  });

  return {
    body: JSON.stringify({ message: "successfully signed out" }),
  };
};

```

Après une déconnexion réussie, tentez de visiter la page protégée `localhost:3000`, et vous serez automatiquement redirigé vers `/sign`.

Nous cuisinons maintenant au gaz ! 🔥

## Configuration du stockage cloud

Nous avons une grande partie de notre application fonctionnelle — en grande partie l'authentification et la protection de la page d'index. Mais nous protégeons une page vide pour le moment. Les utilisateurs ne peuvent donc pas enregistrer ou voir les enregistrements des autres utilisateurs.

Réparons cela en configurant le stockage cloud pour sauvegarder les enregistrements des utilisateurs sur le serveur.

Allez sur la console Firebase et cliquez sur "See all build features" (Voir toutes les fonctionnalités de build) pour trouver le service de stockage cloud.

![Voir toutes les fonctionnalités de build sur la console Firebase.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-26-at-15.33.40@2x.png)
_Voir toutes les fonctionnalités de build sur la console Firebase._

Ensuite, sélectionnez le service Storage.

![Sélectionner le service de stockage.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-26-at-15.33.58@2x.png)
_Sélectionner le service de stockage._

Ensuite, commencez la configuration.

![Cliquer sur commencer sur la page du service de stockage.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-26-at-15.34.29@2x.png)
_Cliquer sur commencer sur la page du service de stockage._

Gardez les règles de stockage telles quelles :

![Les règles de stockage par défaut.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-26-at-15.34.40@2x.png)
_Les règles de stockage par défaut._

Ensuite, sélectionnez un emplacement de serveur.

BeAudible est une startup américaine hypothétique, je choisirai donc un emplacement américain ici.

![Sélectionner un emplacement de stockage.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-26-at-15.35.33@2x.png)
_Sélectionner un emplacement de stockage._

Une fois la configuration terminée, visitez la page Storage et copiez le nom du bucket sous la forme `gs://{name-of-project}.appspot.com.`

![Le nom du bucket de stockage.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-27-at-16.43.07.png)
_Le nom du bucket de stockage._

Excellent !

Lorsque nous téléchargerons et obtiendrons les enregistrements des utilisateurs, nous en aurons besoin pour nous connecter aux serveurs de stockage.

## Comment télécharger des enregistrements audio

L'interface utilisateur de l'enregistreur est alimentée par un composant React Recorder hydraté via la directive `client:load`.

```js
<Recorder client:load>
   ...
</Recorder>

```

Ouvrez le composant `Recorder` et considérez le rappel `onAudioDownload`.

```js
// src/components/AudioRecorder.tsx
// ...
<VoiceRecorder
   onAudioDownload={(blob: Blob) => {
   // 👀 upload recording
   }}
/>

```

Après qu'un utilisateur a terminé l'enregistrement, ce rappel sera invoqué. Notre première tâche est d'aller de l'avant et de télécharger le blob audio sur le serveur.

![Envoyer le blob audio à un point de terminaison serveur.](https://blog.ohansemmanuel.com/content/images/2023/06/upload-flow.png)
_Envoyer le blob audio à un point de terminaison serveur._

### Comment gérer les téléchargements via une route API

Allons-y et créons le point de terminaison API qui recevra le blob audio du client.

Considérez le flux pour notre solution ci-dessous :

![Le diagramme de flux du point de terminaison de sauvegarde d'enregistrement.](https://blog.ohansemmanuel.com/content/images/2023/06/save-audio-recording-flow.png)
_Le diagramme de flux du point de terminaison de sauvegarde d'enregistrement (Le point de terminaison reçoit une requête post. Le jeton est-il valide ? Si oui, convertir le blob audio en tampon, sauvegarder le fichier dans le stockage avec un nom unique, et renvoyer une réponse de succès. Sinon, renvoyer une réponse d'erreur._

Maintenant, voici le code annoté :

```js
// 📂 src/pages/api/recording.ts
// ...
import type { APIRoute } from "astro";

// nanoid will be used to generate unique IDs
import { nanoid } from "nanoid";
import { TOKEN } from "@constants/cookies";
import { getAuth } from "firebase-admin/auth";
import { BUCKET_NAME } from "@constants/firebase";
import { getStorage } from "firebase-admin/storage";
import { serverApp } from "@scripts/firebase/initServer";

// get firebase server auth module
const auth = getAuth(serverApp);

export const post: APIRoute = async (ctx) => {
  // Create an error response
  const authUserError = new Response("Unauthenticated user", { status: 401 });

  try {
    // Get token cookie
    const authToken = ctx.cookies.get(TOKEN).value;

    // not present, return error response
    if (!authToken) {
      return authUserError;
    }

    // verify the user token
    await auth.verifyIdToken(authToken);
  } catch (error) {
   /**
     * Return error response, e.g.,
 	 * if the token verification fails
     */
    return authUserError;
  }

  try {
    // Get the audio blob from the client request
    const blob = await ctx.request.blob();

    // Get access to the firebase storage
    const storage = getStorage(serverApp);
    const bucket = storage.bucket(BUCKET_NAME);

    // convert Blob to native Node Buffer for server storage
    const buffer = Buffer.from(await blob.arrayBuffer());
    const file = bucket.file(`recording-${nanoid()}.wav`);

    // save to firebase storage
    await file.save(buffer);

    // return a successful response
    return {
      body: JSON.stringify({
        message: "Recording uploaded",
      }),
    };
  } catch (error) {
    console.error(error);
    return new Response("Something went horribly wrong", { status: 500 });
  }
};
// ...

```

### Comment télécharger des enregistrements depuis le client

Maintenant que nous avons le point de terminaison API prêt à recevoir les requêtes clients, allons-y et téléchargeons les enregistrements des utilisateurs depuis le client.

Au lieu d'encombrer nos composants d'interface utilisateur avec la logique de téléchargement, je trouve plus maintenable de déplacer une telle logique métier loin des composants UI et, dans notre cas, de l'avoir colocalisée avec l'état de l'application géré via `nanastores`.

Vous vous souvenez de `nanastores` ?

Nous utiliserons [nano stores](https://github.com/nanostores/nanostores) pour la gestion d'état. La bibliothèque `~1kb` est simple et efficace pour notre cas d'utilisation.

Créez un nouveau fichier `audioRecording.ts` pour gérer notre état d'enregistrement et être également responsable d'exposer une méthode `uploadRecording`.

Considérez l'implémentation ci-dessous :

```js
// 📂 src/stores/audioRecording.ts
import { atom } from "nanostores";

/**
 * Deterministic state representation
 */
type Store =
  | {
      blob: null;
      status: "idle";
    }
  | {
      blob: Blob;
      status: "uploading" | "completed" | "failed";
    };

/**
 * Optional naming convention: $[name_of_store]
 * instead of [name_of_store]Store
 *, i.e., $audioRecording instead of audioRecordingStore
 */
export const $audioRecording = atom<Store>({
  // Initialise the atom with the default state
  blob: null,
  status: "idle",
});

/**
 * upload audio recording action
 */
export const uploadRecording = async (blob: Blob) => {
  // Update $audioRecording state to "uploading."
  $audioRecording.set({
    status: "uploading",
    blob,
  });

  try {
   // POST request to our recording endpoint
    const response = await fetch("/api/recording", {
      method: "POST",
      body: blob, // pass blob as the request body
    });

    if (response.ok) {
     // Successful? Update state to "completed."
      $audioRecording.set({
        status: "completed",
        blob,
      });
    } else {
     // Request failed. Update state to "failed."
      $audioRecording.set({
        status: "failed",
        blob,
      });
    }
  } catch (error) {
    $audioRecording.set({
      status: "failed",
      blob,
    });
  } finally {
    // after 't' revert state to idle again
    const timeout = 3000;
    setTimeout(() => {
      $audioRecording.set({
        status: "idle",
        blob: null,
      });
    }, timeout);
  }
};

```

Notre état UI est bien représenté, et l'action de téléchargement est définie. Mais cela ne prendra effet que lorsqu'il sera utilisé dans le composant UI.

### Comment réagir aux changements d'interface utilisateur dans les composants de framework

Nous allons maintenant mettre à jour le composant UI `AudioRecorder` pour réagir à l'état dans le magasin `$audioRecording` comme indiqué ci-dessous :

```js
// 📂 src/components/AudioRecorder.tsx

/**
* The useStore hook will help with the React
* component rerenders. In simple terms, it'll hook into the
* store and react upon any change.
*/
import { useStore } from "@nanostores/react";
import { VoiceRecorder } from "react-voice-recorder-player";
// Import the store and the upload recording action
import { $audioRecording, uploadRecording } from "@stores/audioRecording";

type Props = {
  cta?: string;
};

export const Recorder = (props: Props) => {
  // Get the current application state from the store
  const state = useStore($audioRecording);

  // React deterministically based on the status of the store
  switch (state.status) {
    case "idle":
      return (
        <div>
          <VoiceRecorder
   	        // 👀 Invoke uploadRecording after a user completes the recording
            onAudioDownload={(blob: Blob) => uploadRecording(blob)}
          />

          {props.cta}
        </div>
      );
/**
 Show relevant UI during the uploading state.
**/
    case "uploading":
      return (
        <div className="flex items-center justify-center w-56 h-56 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-800 dark:border-gray-700">
          <div className="px-3 py-1 text-xs font-medium leading-none text-center text-blue-800 bg-blue-200 rounded-full animate-pulse dark:bg-blue-900 dark:text-blue-200">
            Uploading ...
          </div>
        </div>
      );
/**
 Show relevant UI during the failed state.
**/
    case "failed":
      return (
        <div className="bg-red-400 rounded-md py-6 px-3 text-slate-100 motion-safe:animate-bounce">
          An error occurred uploading your recording
        </div>
      );
/**
 Show relevant UI during the completed state.
**/
    case "completed":
      return (
        <div className="bg-green-400 rounded-md py-6 px-3 text-slate-100 motion-safe:animate-bounce">
          Successfully published your recording!
        </div>
      );
/**
 Typescript exhaustive checking
 @see https://www.typescriptlang.org/docs/handbook/2/narrowing.html#exhaustiveness-checking
**/

    default:
      const _exhaustiveCheck: never = state;
      return _exhaustiveCheck;
  }
};

```

Maintenant, un utilisateur devrait pouvoir enregistrer dans le navigateur, et nous irons de l'avant et sauvegarderons l'enregistrement sur notre backend.

![Voir les enregistrements sauvegardés dans l'émulateur Firebase.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-29-at-19.15.22@2x.png)
_Voir les enregistrements sauvegardés dans l'émulateur Firebase._

## Comment récupérer des données depuis le serveur

Nous sauvegardons correctement les enregistrements des utilisateurs, mais pour le moment ils ne peuvent pas être vus sur la page d'accueil.

Résolvons cela.

Notre solution est de récupérer les enregistrements sur le serveur et d'envoyer la page HTML rendue au client.

Voici la solution de code :

```js
// 📂 src/pages/index.astro

---
import { BUCKET_NAME } from "@constants/firebase";
import LinkCTA from "@components/LinkCTA.astro";
import AudioPlayer from "@components/AudioPlayer.astro";
// ...

// Represent the recordings with the "Audible" type alias
type Audible = { url: string; timeCreated: string };

// audibles will hold the list of "Audibles."
let audibles: Audible[] = [];
const storage = getStorage(serverApp);


try {
   /**
	 *  After verifying the user auth token
  	 * and setting the token cookie ...
	*/
    try {
    // get all recordings in the storage bucket
    const bucket = storage.bucket(BUCKET_NAME);
    const [files] = await bucket.getFiles();

    audibles = await Promise.all(
      files.map(async (file) => {
        const [metadata] = await file.getMetadata();

        // return the url and timeCreated metadata
        return {
          url: file.publicUrl(),
          timeCreated: metadata.timeCreated,
        };
      })
    );
  } catch (error) {
    console.error(error);
    console.error("Error fetching audibles");
    return Astro.redirect("/signin");
  }
}

//...
---

```

Maintenant, mettez à jour la section template de composant pour rendre les "audibles". Nous exploiterons le composant `AudioPlayer`, en lui passant l'`url` audible et les métadonnées `timeCreated`.

```html
<div class="flex flex-col items-center">
    {
      audibles.length === 0 ? (
        <>
          <Empty />
          <LinkCTA href="/record">Record</LinkCTA>
        </>
      ) : (
        audibles
          .sort((a, b) =>
            new Date(a.timeCreated) < new Date(b.timeCreated) ? 1 : -1
          )
          .map((audible) => (
            <AudioPlayer url={audible.url} timeCreated={audible.timeCreated} />
          ))
      )
    }
</div>

```

Dans le code ci-dessus, nous affichons une interface utilisateur `Empty` vide s'il n'y a pas d'audibles. Sinon, nous rendons une liste triée d'audibles.

![Rendre la liste triée des enregistrements audio.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-29-at-19.06.31@2x.png)
_Rendre la liste triée des enregistrements audio._

## Comment soumettre des formulaires HTML

Le dernier puzzle de notre application est la gestion de la soumission du formulaire de commentaires.

J'ai inclus cette fonctionnalité pour montrer un exemple de gestion d'un formulaire au sein de la même page rendue côté serveur, c'est-à-dire sans créer de point de terminaison API pour gérer la requête de formulaire.

Jetez un coup d'œil à l'élément formulaire et remarquez comment son attribut method est défini sur `POST` :

```js
// 📂 src/layouts/BaseLayout.astro
// ...
<form class="mx-auto flex" method="POST">
...
</form>

```

Par défaut, le navigateur enverra une requête POST au serveur lorsque ce formulaire sera soumis, que nous pouvons capturer et sur laquelle nous pouvons réagir.

Dans la section frontmatter de la page `index.astro`, nous pouvons ajouter une condition pour gérer les requêtes de formulaire de commentaires comme indiqué ci-dessous :

```js
// ...
if (Astro.request.method === "POST") {
  try {
	// Get the form data
    const data = await Astro.request.formData();
    /**
	* Get the feedback value.
	* Corresponds to the form input element value of the name, "feedback".
	*/
    const feedback = data.get("feedback");

    // Do something with the data
    console.log({ feedback });

    // Do something with the data
  } catch (error) {
    if (error instanceof Error) {
      console.error(error.message);
    }
  }
}
// ...

```

Je garde cela simple en journalisant simplement les commentaires sur le serveur. Mais nous pourrions sauvegarder cette valeur dans une base de données dans le monde réel. Le point crucial ici est de recevoir les valeurs du formulaire, comme indiqué ci-dessus.

![Les données de commentaires journalisées.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-05-29-at-19.14.07@2x.png)
_Les données de commentaires journalisées._

## Conclusion de ce chapitre

Astro est excellent pour construire des sites web axés sur le contenu tels que des blogs, des pages de destination, et ainsi de suite. Mais, nous pouvons faire beaucoup plus avec.

Supposons que vous puissiez construire l'application comme une application multi-pages (MPA), c'est-à-dire pas une application à page unique, et que vous puissiez tirer parti des îlots d'interactivité (îlots de composants). Dans ce cas, vous pouvez la construire avec Astro.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-140.png)
_Chapitre huit._

# Chapitre 8 : Construisez vos propres intégrations Astro

À la fin de ce chapitre, vous rejoindrez l'ordre des mages qui manient un grand pouvoir pour plier Astro à leur volonté avec de nouvelles fonctionnalités et comportements.

## Ce que vous apprendrez

*   La relation entre Astro et le bundler de modules Vite
*   Les différents types d'intégrations disponibles dans Astro
*   Construire votre première intégration Astro
*   Comprendre le cycle de vie des hooks Astro
*   Approfondir vos connaissances sur la construction d'intégrations de fonctionnalités Astro personnalisées

## Astro et Vite

Avant de plonger dans le monde magnifique des intégrations Astro, nous devons savoir qui alimente le navire de build Astro - et c'est [Vite](https://vitejs.dev/), l'outil de build tout en vitesse, efficacité et flexibilité.

Pensez à Vite comme notre fidèle copilote, nous aidant à regrouper nos pages web et créant un environnement de développement ultra-rapide.

![La relation Astro Vite.](https://blog.ohansemmanuel.com/content/images/2023/06/astro-vite-relationship.png)
_La relation Astro Vite._

Pour construire les intégrations personnalisées dont nous rêvons, nous devrons peut-être aller au-delà d'Astro et nous aventurer profondément dans le territoire de Vite, par exemple en personnalisant l'étape de build avec des plugins Vite.

Maintenant, je sais que cela pourrait ne pas être très clair, surtout quand nous commencerons à parler de Vite dans les sections à venir de ce chapitre. Mais ne craignez rien - vous savez maintenant pourquoi Vite est essentiel au processus de build, et j'expliquerai avec des exemples dans les sections à venir de ce chapitre.

## Que sont les intégrations Astro ?

Par définition, les intégrations Astro étendent Astro avec de nouvelles fonctionnalités et comportements au sein de votre projet.

Nous nous retrouverons à construire trois types d'intégrations Astro, à savoir :

1.  **Renderers** : ces intégrations permettent le rendu d'un composant de framework (généralement le rendu côté serveur et l'hydratation côté client). Des exemples de cela incluent les intégrations officielles Astro React, Preact et Vue.
2.  **Bibliothèques** : ces intégrations permettent le support de bibliothèques externes au sein d'Astro. Des exemples de cela incluent les intégrations officielles Tailwind et Partytown.
3.  **Fonctionnalités** : ce sont des intégrations qui étendent le comportement d'Astro d'une manière spécifique, généralement pour prendre en charge un ensemble de fonctionnalités défini par l'utilisateur. Des exemples incluent l'intégration officielle [sitemap](https://docs.astro.build/en/guides/integrations-guide/sitemap/) qui génère un sitemap lorsque vous construisez votre projet Astro.

Pour la plupart des gens, la majorité des intégrations que vous construirez seront pour prendre en charge une fonctionnalité particulière, c'est-à-dire des intégrations de fonctionnalités. Ce sera le seul objectif de ce chapitre. Une fois que vous aurez une connaissance suffisante de la construction d'intégrations de fonctionnalités, vous pourrez transférer les connaissances aux intégrations de bibliothèque ou de renderer.

Commençons avec une intégration Astro artificielle.

## Hello World. Désolé – Hello, Integration

Faisons connaissance avec une intégration Astro hello world de base. Même si nous manierons bientôt des épées et tuerons des dragons, avant cela, vous devez être présenté aux outils du métier.

### Objectif du projet

L'objectif de notre première intégration Astro est sans doute simple : nous écrirons une intégration Astro personnalisée qui enregistre automatiquement un message hello world dans la console du navigateur sur chaque page de l'application.

Vous avez compris ?

J'ai entendu un oui !

### Votre première intégration personnalisée

Nous aborderons cette solution en injectant un script sur chaque page de l'application.

Comment ?

Où ?

Quand ?

Retenez vos chevaux, mon pote !

Commencez par démarrer un nouveau projet Astro avec la commande familière :

```js
npm create astro@latest hello-astro-integration

```

Maintenant que vous êtes un pro à ce sujet, nommez le projet comme vous le souhaitez, par exemple `hello-astro-integration`, et utilisez un modèle minimal (vide).

Ouvrez le répertoire de l'application et dirigez-vous vers le fichier `astro.config.mjs`.

Le fichier `astro.config.mjs` comprend des options de configuration pour notre projet Astro. C'est là que nous définissons les intégrations pour notre projet, c'est-à-dire c'est là que la magie opère.

Pour le moment, notre fichier `astro.config.mjs` devrait être dans l'état vide par défaut, comme indiqué ci-dessous :

```js
// 📂 astro.config.mjs
import { defineConfig } from "astro/config";

export default defineConfig({});

```

Changeons cela en ajoutant une liste `integrations` vide à la configuration :

```js
// 📂 astro.config.mjs
import { defineConfig } from "astro/config";

export default defineConfig({
  integrations: [], // 👀 look here
});

```

En bref, une intégration Astro est représentée par un objet avec des propriétés `name` et `hooks`, comme indiqué ci-dessous :

```js
// 📂 astro.config.mjs
import { defineConfig } from "astro/config";

// https://astro.build/config
export default defineConfig({
  // 👀 look here
  integrations: [
    {
      name: "astro-hello",
      hooks: {},
    },
  ],
});

```

Dans le bloc de code ci-dessus, nous avons décrit l'objet dans le tableau `integrations`.

Le nom de l'intégration est `astro-hello`. Nous discuterons des hooks dans la section à venir, mais cela représente des points d'accroche extensibles au sein du processus de cycle de vie de build d'Astro.

Par exemple, exploitons le premier hook dans le processus de cycle de vie appelé `astro:config:setup`.

Ce hook est le point de départ de tout le cycle de vie de build. Il est déclenché à l'initialisation avant qu'Astro n'ait résolu la configuration du projet. C'est l'endroit idéal pour injecter des scripts sur une nouvelle page ou étendre la configuration du projet avant qu'elle ne soit résolue.

Profitons-en en le passant dans l'objet hooks et en le pointant vers une fonction invoquée lorsque le hook est déclenché.

```js
// 📂 astro.config.mjs
import { defineConfig } from "astro/config";

export default defineConfig({
  integrations: [
    {
      name: "astro-hello",
      hooks: {
        // 👀 hook: callbackFn
        "astro:config:setup": (options) => {},
      },
    },
  ],
});

```

Notez le paramètre `options` dans le rappel du hook. C'est un objet avec la définition de type suivante :

```js
{
  config: AstroConfig;
  command: 'dev' | 'build';
  isRestart: boolean;
  updateConfig: (newConfig: Record<string, any>) => void;
  addRenderer: (renderer: AstroRenderer) => void;
  addWatchFile: (path: URL | string) => void;
  injectScript: (stage: InjectedScriptStage, content: string) => void;
  injectRoute: ({ pattern: string, entryPoint: string }) => void;
}

```

Heureusement, il contient la méthode `injectScript` qui nous intéresse :

```js
  injectScript: (stage: InjectedScriptStage, content: string) => void;

```

`stage` indique comment le `content` du script doit être injecté dans la page, et il y a quatre valeurs possibles : `head-inline`, `before-hydration`, `page`, et `page-ssr`.

L'option `page` regroupera et injectera le script avec d'autres balises `<script>` définies dans n'importe quel composant Astro sur la page. La sortie finale chargera finalement cela avec un `<script type="module>`.

Quand j'ai commencé à bricoler avec l'API d'intégrations, j'ai essayé des choses stupides pour faire fonctionner `injectScript`. Je peux vous dire en toute confiance que celles-ci ne fonctionneront pas :

```js
// 👀 Error: Failed to parse source for import analysis
// because the content contains invalid JS syntax.
injectScript("page", "console.log('Hello World')")

const log = () => console.log("me");
// 👀 Uncaught ReferenceError: log is not defined
options.injectScript("page", "log()");

```

Cela vous évite la futilité que j'ai vécue jusqu'à ce que je regarde dans le code source d'Astro.

Le paramètre de chaîne `content` dans `injectScript` fait référence à un chemin d'importation. C'est comme indiqué ci-dessous :

```js
import { defineConfig } from "astro/config";

// https://astro.build/config
export default defineConfig({
  integrations: [
    {
      name: "astro-hello",
      hooks: {
        "astro:config:setup": (options) => {
		  //  👀 "page" option with an import path
          options.injectScript("page", `import '/src/scripts/
  globalLog.js'`);
        },
      },
    },
  ],
});

```

Puisque nous passons un chemin d'importation au script, assurons-nous que le script existe.

Créez un nouveau script avec le contenu suivant dans `src/scripts/globalLog.js` :

```js
// 📂 src/scripts/globalLog.js
const logger = () => {
  const msg = "Hello Integrations"
  console.log(`%c ${msg}`, "background: black;  color: yellow");
};

logger();

```

La méthode `logger` appelle la méthode `console.log` avec une chaîne `Hello integrations` tout en ajoutant de la couleur au message.

Et voilà !

Nous avons notre première intégration fonctionnant comme prévu.

![Journal d'intégration fonctionnel imprimé dans la console du navigateur](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-06-at-05.29.53.png)
_Journal d'intégration fonctionnel imprimé dans la console du navigateur_

Nous pouvons créer plus de pages, et le message de la console sera journalisé sur chaque page de l'application.

### Comment imprimer un message dans la console du serveur

Puisque nous avons des points d'accroche dans le processus de build d'Astro, il est également possible de sortir des journaux vers la console du serveur.

Cela peut être utile pour l'utilisabilité ou pour s'assurer que notre intégration personnalisée fonctionne comme prévu.

Pour le moment, voici le désordre à quoi ressemblent mes journaux de serveur :

![Les journaux (désordonnés) du serveur Astro](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-06-at-05.33.46.png)
_Les journaux (désordonnés) du serveur Astro_

Les vôtres devraient sembler familiers. Cela vient du processus incrémentiel de construction de notre première intégration.

Allons-y et imprimons quelque chose dans les journaux une fois que nous avons injecté avec succès notre script sur la page.

```js
// ...

hooks: {
    "astro:config:setup": (options) => {
      options.injectScript("page", `import '/src/scripts/
    globalLog.js'`);

     // 👀 add a new log
     console.log("Injected hello integration script");
    },
},

```

Redémarrez le serveur pour une ardoise propre, et nous devrions avoir le journal imprimé comme indiqué ci-dessous :

![Le journal du serveur de notre intégration hello world](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-06-at-05.38.59.png)
_Le journal du serveur de notre intégration hello world_

Puisque nous sommes des développeurs sophistiqués qui se soucient de l'utilisabilité, allons-y et faisons en sorte que le journal semble natif aux autres journaux Astro en ajoutant un peu de formatage de texte et de couleur via `kleur`.

Installez le paquet `kelur` :

```js
npm install kleur

```

Une fois l'installation terminée, nous devrions maintenant avoir un nouveau journal dans le serveur de développement qui lit :

```js
05:41:02 AM [astro] update /package-lock.json

```

![Exemple de journal de serveur astro natif](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-06-at-05.41.12.png)
_Exemple de journal de serveur astro natif_

`05:41:02` représente mon heure actuelle.

S'il vous plaît, ne me demandez pas pourquoi j'écris ce chapitre si tôt le matin.

Allons-y et faisons en sorte que notre journal ressemble à cela. Au lieu d'utiliser simplement `console.log`, introduisons un `logServerMessage` qui fait notre belle enchère comme indiqué ci-dessous :

```js
// 📂 astro.config.mjs

import kleur from "kleur";
import { defineConfig } from "astro/config";

// 👀 The Intl.DateTimeFormat object enables language-sensitive
// date and time formatting.
const dateTimeFormat = new Intl.DateTimeFormat([], {
  hour: "2-digit",
  minute: "2-digit",
  second: "2-digit",
});

const logServerMessage = (message) => {
  // 👀 Get a new date string using the dateTimeFormat object
  const date = dateTimeFormat.format(new Date());

  // log to console with kleur colours and formatting
  console.log(`${kleur.gray(date)} ${kleur
    .bold()
    .cyan("[astro-hello-integration]")} ${message}
  `);
};

export default defineConfig({
  // ... same content as before
});

```

Maintenant, nous devrions avoir un beau message de journal qui semble natif à Astro, comme les autres journaux de console du serveur.

![Le journal de serveur "sensation native" de l'intégration personnalisée](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-06-at-05.47.14.png)
_Le journal de serveur "sensation native" de l'intégration personnalisée_

### Intégrations personnalisées comme fonctions d'usine

Notre implémentation actuelle commence à encombrer le fichier de configuration Astro.

En pratique, au lieu d'intégrer notre intégration Astro personnalisée, elle est susceptible de vivre dans un fichier séparé en tant que fonction d'usine, c'est-à-dire une fonction qui crée et renvoie l'objet d'intégration Astro.

Faisons cela – ce sera quelque chose comme un refactoring.

Déplacez tout le contenu de l'intégration dans un nouveau fichier `src/integrations/astro-hello.ts`.

```js
// 📂 src/integrations/astro-hello.ts
import kleur from "kleur";

const dateTimeFormat = new Intl.DateTimeFormat([], {
  hour: "2-digit",
  minute: "2-digit",
  second: "2-digit",
});

const logServerMessage = (message) => {
  const date = dateTimeFormat.format(new Date());
  console.log(`${kleur.gray(date)} ${kleur
    .bold()
    .cyan("[astro-hello-integration]")} ${message}
    `);
};

// 👀 Introduce a default export function that returns the Astro
// integration object.
export default function helloIntegration() {
  return {
    name: "astro-hello",
    hooks: {
      "astro:config:setup": (options) => {
        options.injectScript("page", `import '/src/scripts/
    globalLog.js'`);

        logServerMessage("Injected script");
      },
    },
  };
}

```

Maintenant, ajoutez les types TypeScript :

```js
// 📂 src/integrations/astro-hello.ts

import type { AstroIntegration } from "astro";

const logServerMessage = (message: string) => {
  // ...
};

export default function helloIntegration(): AstroIntegration {
  // ...
}


```

Oh ouais !

Notre implémentation prend forme joliment.

Maintenant, nettoyons `astro.config.mjs` en important notre intégration comme indiqué ci-dessous :

```js
// 📂 astro.config.mjs
import { defineConfig } from "astro/config";
import astroHello from "./src/integrations/astro-hello";

export default defineConfig({
  // 👀 invoke the imported astroHello function in the list
  integrations: [astroHello()],
});

```

Et voilà ! Une intégration Astro personnalisée étincelante de propreté.

Vous pouvez voir le code source complet sur [GitHub](https://github.com/understanding-astro/hello-astro-integration).

## Le cycle de vie des hooks Astro

Par définition, le cycle de vie fait référence à la série de changements dans la vie d'un organisme. Par exemple, un papillon commence comme un œuf, une larve, une pupe, et devient ensuite un adulte à part entière.

Jusqu'à ce que le clonage humain devienne disponible, il y a de fortes chances que vous ayez également commencé comme un nourrisson, puis grandi en un tout-petit, finalement la puberté, et ensuite trouvé votre chemin vers l'âge adulte. Du moins, je l'espère !

En logiciel, le terme cycle de vie représente les différentes étapes d'un processus.

Avec les hooks Astro, nous faisons explicitement référence aux étapes par lesquelles Astro passe lors de la construction de vos pages d'application. C'est le processus depuis la résolution de la configuration du projet Astro jusqu'au lancement d'un serveur local pour regrouper vos pages statiquement ou rendues côté serveur en production.

L'ensemble du processus est ce que j'appelle le cycle de vie des hooks Astro.

Pour devenir productif dans le développement d'intégrations personnalisées, nous devrons savoir où dans le cycle de vie nous devons effectuer un changement ou réagir.

Les hooks sont des fonctions qui sont appelées à diverses étapes de la construction. Pour interagir avec le processus de build, nous exploiterons les dix hooks suivants :

*   `astro:config:setup`
*   `astro:config:done`
*   `astro:server:setup`
*   `astro:server:start`
*   `astro:server:done`
*   `astro:build:start`
*   `astro:build:setup`
*   `astro:build:generated`
*   `astro:build:ssr`
*   `astro:build:done`

Dix semble beaucoup à retenir. Heureusement que ce n'est pas une douzaine de hooks (douze). Et vous n'avez pas à les mémoriser. Au lieu de cela, comprenez comment ils fonctionnent. Vous pouvez toujours vous référer à la référence officielle en cas de besoin.

### Le quand et le pourquoi des hooks

L'une des premières questions que je me suis posées lorsque j'ai commencé à bricoler avec les intégrations Astro était quand exactement celles-ci sont déclenchées, et y a-t-il un ordre d'exécution pour elles ?

Eh bien, la réponse à celles-ci se trouve ci-dessous, mais d'abord, considérez le diagramme suivant qui dépeint l'ordre dans lequel les hooks sont exécutés :

![Ordre d'exécution des hooks Astro](https://blog.ohansemmanuel.com/content/images/2023/06/hooks-lifecycle.png)
_Ordre d'exécution des hooks Astro_

Le processus démarre avec deux hooks :

1.  `astro:config:setup`
2.  `astro:config:done`

Ces hooks sont toujours exécutés quel que soit le processus de build Astro.

Voici une ventilation de quand ceux-ci sont exécutés et comment nous pourrions les exploiter dans nos intégrations personnalisées :

<table>
	<thead>
		<tr>
			<th>
				Hook
			</th>
			<th>
				Exécuté quand …
			</th>
			<th>
				 Pourquoi utiliser ceci …
			</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<br><br><code>astro:config:<br>setup</code><br>
			</td>
			<td>
				<br><br>Astro est initialisé. <br><br>Cela se produit <br>avant que la configuration du projet Astro (ou la config Vite) <br>ne soient résolues.
			</td>
			<td>
				<br><br>Considérez être le premier au pub avant qu'il n'ouvre. Vous pouvez causer du chahut avant même que quelqu'un d'autre ne se présente ! <br><br>De même, c'est là que vous intervenez pour étendre la configuration du projet, par exemple mettre à jour la config Astro, appliquer des plugins Vite, ajouter des renderers de composants et injecter des scripts avant qu'Astro ne sache ce qui l'a frappé.
			</td>
		</tr>
		<tr>
			<td>
				<br><br><code>astro:config:done</code>
			</td>
			<td>
				<br><br>La config Astro a été résolue. À ce stade, chaque hook <code>astro:config:setup</code> a été invoqué pour chaque intégration dans le projet. <br><br><br>
			</td>
			<td>
				<br><br>Comme une pinte de bière parfaite, nous attendons patiemment de saisir le verre seulement après qu'il a été versé. <br><br>De même, après que la config Astro a finalement mis de l'ordre dans ses affaires et que toutes les autres intégrations ont fait leur truc, c'est là que nous récupérons la config finale pour une utilisation dans notre intégration. <br>
			</td>
		</tr>
	</tbody>
</table>

Une fois que `astro:config:done` est déclenché, il y a deux branches à considérer : le mode développement et le mode production.

Lors du développement de vos applications localement, sans initier un build de production généralement via `npm run build` ou `astro build`, le côté gauche du graphique dépeint l'ordre d'exécution des hooks en mode développeur. Ensuite, les hooks suivants sont invoqués :

1.  `astro:server:setup`
2.  `astro:server:start`
3.  `astro:server:done`

Ces hooks sont exécutés lors de la construction de votre application pour le développement local.

Voici une ventilation de quand ceux-ci sont exécutés et comment nous pourrions les exploiter dans nos intégrations personnalisées :

<table>
	<thead>
		<tr>
			<th>
				Hook
			</th>
			<th>
				Exécuté quand …
			</th>
			<th>
				 Pourquoi utiliser ceci …
			</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<br><br><code>astro:server:<br>setup</code><br>
			</td>
			<td>
				<br><br>Le serveur Vite vient d'être créé en mode développement.<br><br>C'est avant que l'événement serveur <code>listen()</code> ne soit déclenché, c'est-à-dire avant de démarrer le serveur.
			</td>
			<td>
				<br><br>C'est là que nous pouvons mettre à jour les options du serveur Vite et le middleware.<br><br>L'objet serveur de développement Vite est passé en argument à notre hook.
			</td>
		</tr>
		<tr>
			<td>
				<br><br><code>astro:server:start</code>
			</td>
			<td>
				<br><br>La méthode Vite <code>listen()</code> vient d'être déclenchée, c'est-à-dire que le serveur est en cours d'exécution. <br><br><br>
			</td>
			<td>
				<br><br>Comme des super-héros férus de technologie, nous pouvons intervenir ici pour sauver la situation à la dernière minute - enfin, si cela implique d'intercepter des requêtes réseau. <br><br>C'est là que nous pouvons intervenir pour intercepter les requêtes réseau à l'adresse du serveur de développement spécifiée (passée en argument à notre hook)
			</td>
		</tr>
		<tr>
			<td>
				<br><br><code>astro:server:done</code>
			</td>
			<td>
				<br><br>Le serveur de développement vient d'être fermé.
			</td>
			<td>
				<br><br>Comme des nettoyeurs venant après la fête pour balayer le désordre, c'est là que nous exécutons les nettoyages. <br><br>Si vous souhaitez nettoyer les effets secondaires déclenchés pendant <code>astro:server:setup</code> ou <code>astro:server:start</code>, c'est ici que vous le faites !
			</td>
		</tr>
	</tbody>
</table>

Lorsque nous exécutons un build de production, deux hooks seront toujours déclenchés. Ce sont

1.  `astro:build:start`
2.  `astro:build:setup`

Et voici une ventilation de quand ceux-ci sont exécutés et comment nous pourrions les exploiter dans nos intégrations personnalisées :

<table>
	<thead>
		<tr>
			<th>
				Hook
			</th>
			<th>
				Exécuté quand …
			</th>
			<th>
				 Pourquoi utiliser ceci …
			</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<br><br><code>astro:build:<br>start</code><br>
			</td>
			<td>
				<br><br>La config Astro est complètement résolue mais avant que le build de production ne commence.
			</td>
			<td>
				<br><br>Le build de production est sur le point de commencer mais peut-être voulez-vous configurer des objets globaux ou des clients nécessaires pendant le build ? <br>C'est ici que nous le faisons.
			</td>
		</tr>
		<tr>
			<td>
				<br><br><code>astro:build:setup</code>
			</td>
			<td>
				<br><br>Le build est sur le point de commencer. À ce stade, la config de build est entièrement construite. <br><br><br>
			</td>
			<td>
				<br><br>Pour voler la phrase parfaite de la documentation officielle d'Astro : c'est notre dernière chance de modifier le build. <br><br>C'est comme se préparer pour une soirée - nous avons mis notre meilleure tenue et avons l'air élégant, mais nous avons juste besoin d'ajouter ce dernier accessoire pour compléter le look. C'est notre chance de faire exactement cela - d'écraser certaines valeurs par défaut et de s'assurer que tout est parfait. <br><br>Je dois mentionner que si vous n'êtes pas sûr d'utiliser ce hook ou <code>astro:build:start</code>, optez pour <code>astro:build:start</code> à la place.
			</td>
		</tr>
	</tbody>
</table>

Maintenant, selon que la page en cours de construction est générée statiquement ou doit être rendue côté serveur, soit `astro:build:generated` soit `astro:build:ssr` sera invoqué, et enfin, `astro:build:done`.

Oui, vous l'avez deviné. Voici la ventilation finale de quand ceux-ci sont exécutés et comment nous pourrions les exploiter dans nos intégrations personnalisées :

<table>
	<thead>
		<tr>
			<th>
				Hook
			</th>
			<th>
				Exécuté quand …
			</th>
			<th>
				 Pourquoi utiliser ceci …
			</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<br><br><code>astro:build:<br>generated</code><br>
			</td>
			<td>
				<br><br>Le build de production statique a complètement généré les routes et les actifs.
			</td>
			<td>
				<br><br>Accéder aux routes et actifs générés avant que les artefacts de build ne soient nettoyés. Selon la documentation officielle, c'est un cas peu courant et nous pourrions être mieux avisés d'utiliser <code>astro:build:done</code> dans de nombreux cas, sauf si nous avons vraiment besoin d'accéder à ces fichiers avant le nettoyage.
			</td>
		</tr>
		<tr>
			<td>
				<br><br><code>astro:build:ssr</code>
			</td>
			<td>
				<br><br>Un build de production SSR est terminé.<br><br><br>
			</td>
			<td>
				<br><br>Pour obtenir l'accès au manifeste SSR. Ceci est utile lors de la création de builds SSR personnalisés.
			</td>
		</tr>
		<tr>
			<td>
				<br><br><code>astro:build:done</code>
			</td>
			<td>
				<br><br>Le build de production est terminé !
			</td>
			<td>
				<br><br>C'est là que nous pouvons accéder aux routes et actifs générés, par exemple pour être copiés quelque part. Pour transformer les actifs générés, envisagez d'utiliser un plugin Vite et de configurer <code>astro:config:setup</code>.
			</td>
		</tr>
	</tbody>
</table>

### Examiner l'ordre d'évaluation des hooks

Même si nous avons pris le temps d'explorer quand les hooks Astro sont invoqués, il n'y a pas de meilleur professeur que la pratique.

Allons-y et écrivons une intégration simple qui crache un journal dans la console du serveur lorsqu'elle est invoquée. Ensuite, vous pouvez bricoler avec la construction de plusieurs pages pour la production et inspecter les journaux.

Notre objectif final est d'avoir une intégration personnalisée qui ressemble à quelque chose comme ceci :

```js
{
  name: "some-identifier",
  hooks: {
   "hook-name": () => {
     // log hook name so we know it's been invoked
   }
  }
}

```

Ça a du sens ?

Allons-y et construisons cela.

Si vous construisez en même temps, étendez l'application hello world ou créez une nouvelle application Astro avec l'intégration personnalisée suivante :

```js
// 📂 src/integrations/lifecycle-logs.ts

import kleur from "kleur";
import type { AstroIntegration } from "astro";

//Create a new dateTimeFormat object
const dateTimeFormat = new Intl.DateTimeFormat([], {
  hour: "2-digit",
  minute: "2-digit",
  second: "2-digit",
});

export const lifecycleLogs = () => {
  const hooks = [
    `astro:config:setup`,
    `astro:config:done`,
    `astro:server:setup`,
    `astro:server:start`,
    `astro:server:done`,
    `astro:build:start`,
    `astro:build:setup`,
    `astro:build:generated`,
    `astro:build:ssr`,
    `astro:build:done`,
  ] as const;

  // base integration structure. "hooks" will be updated
  let integration: AstroIntegration = {
    name: "astro-lifecycle-logs",
    hooks: {},
  };

  // loop over the hooks list and add the name and log
  for (const hook of hooks) {
    integration.hooks[hook] = () => {
      // 👀 Get a new date string
      const date = dateTimeFormat.format(new Date());

      // log with kleur colours and formatting
      console.log(`${kleur.gray(date)} ${kleur
        .bold()
        .yellow("[lifecycle-log]")} ${kleur.green(hook)}
        `);
    };
  }

  return integration;
};


export default lifecycleLogs;

```

Importez `lifecycleLogs` et ajoutez-le à la liste d'intégration de votre projet, puis (re)démarrez votre application pour voir les journaux dans la console comme indiqué ci-dessous :

![Les hooks de cycle de vie de développement](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-08-at-17.13.02.png)
_Les hooks de cycle de vie de développement_

En guise d'exercice, je vous suggère d'ajouter une nouvelle page SSR et d'exécuter un build de production pour voir l'ordre d'exécution des hooks journalisé.

Voici un exemple avec deux pages :

*   une page statique `index.astro`
*   une page rendue côté serveur `ssr.astro`

![Le cycle de vie complet des hooks journalisé](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-08-at-18.16.15.png)
_Le cycle de vie complet des hooks journalisé_

## Comment construire une intégration de pré-rendu par défaut

Lorsque nous activons le SSR dans notre projet, nous pouvons également opter pour le pré-rendu, c'est-à-dire rendre statiquement certains fichiers au moment de la construction.

La façon de faire cela est d'ajouter un `export const prerender = true` à la ou aux pages statiques souhaitées.

Il fut un temps où Astro ne prenait pas en charge le rendu hybride, donc c'est une excellente fonctionnalité.

Mais en pratique, nous pouvons avoir plusieurs pages statiques et seulement quelques-unes rendues côté serveur. Ajouter `export const prerender = true` à toutes les pages statiques devient péniblement ennuyeux.

L'autre jour, j'ai commencé à construire une application Astro qui était principalement rendue statiquement. Puis j'ai réalisé que j'avais besoin d'une route rendue côté serveur.

À ce stade, je change mon fichier `astro.config.mjs` pour inclure `output: server`. Par conséquent, j'ai dû aller sur toutes les pages statiques existantes pour ajouter `export const prerender = true`. Ce n'était pas agréable.

Vous pouvez voir le code source complet sur [GitHub](https://github.com/understanding-astro/astro-integration-prerender-by-default).

### Objectif du projet

L'objectif de notre intégration personnalisée est d'inverser le comportement de rendu hybride par défaut d'Astro.

Par défaut, avec un `output: server` dans notre configuration, toutes les pages sont supposées être rendues par le serveur, et nous devons explicitement ajouter `export const prerender = true` à nos pages statiques.

Nous voulons obtenir un comportement différent pour les cas où nous avons plus de pages statiques, c'est-à-dire :

*   Par défaut, avec `output: server` dans notre configuration, rendre toutes les pages statiquement au moment de la construction – pré-rendre par défaut.
*   Ajouter `export const prerender = false` pour rendre explicitement une page côté serveur.

Vous voyez ce que nous avons fait là ?

Maintenant, réfléchissez-y. Comment y parvenons-nous ?

Au moment de la rédaction, il existe une feuille de route publique pour qu'Astro [prenne en charge le pré-rendu par défaut](https://github.com/withastro/roadmap/issues/539) en interne. Jusque-là, plions Astro à notre volonté.

### API d'intégration

Nous concevrons notre intégration comme une fonction d'usine nommée `prerenderByDefault`.

Nos utilisateurs iront de l'avant et invoqueront cette fonction dans leur liste `integrations`, comme indiqué ci-dessous :

```js
export default defineConfig({
  integrations: [prerenderByDefault()],
});

```

Par défaut, nous enregistrerons des messages dans la console du serveur mais exposerons un paramètre `silent` pour empêcher les journaux de la console du serveur.

Les intégrations Astro prennent généralement en charge les configurations en passant des arguments à la fonction d'usine. Voici notre API proposée :

```js
export default defineConfig({
  integrations: [prerenderByDefault({
     silent: true // or false (boolean)
  })],
});

```

Enfin, nous ajouterons une validation de base au sein de notre intégration. Si l'utilisateur n'a pas d'option `output: server` ou `adapter` dans sa configuration, nous sauterons le pré-rendu par défaut. C'est parce que nous voulons seulement que notre intégration prenne effet pendant le rendu hybride, qui n'est activé qu'avec `output: server` dans la configuration de projet de l'utilisateur.

### Aperçu de la solution technique

À la base, notre intégration tirera parti de deux hooks de cycle de vie : `astro:config:setup` et `astro:config:done` comme indiqué ci-dessous :

```js
export default function prerenderByDefault() {
  return {
    name: "astro-prerender-by-default",
    hooks: {
      "astro:config:setup"() {

      },
      "astro:config:done"(options) {

      },
    },
  };
}

```

Dans `astro:config:done`, nous récupérerons la configuration résolue du projet et effectuerons notre validation.

```js
"astro:config:done"(options) {

   // 1. Get resolved config from options.config
   // 2. Validate that the config object has the right
    //   output and adapter values

}

```

Dans `astro:config:setup`, nous interviendrons et étendrons la configuration du projet Astro de l'utilisateur en appliquant un plugin Vite personnalisé.

```js
"astro:config:setup"(options) {
    // Apply a custom Vite plugin here
}

```

Lorsque Astro construit notre projet, il le fait en utilisant Vite. Les intégrations sont à Astro ce que les plugins sont à Vite. Pour étendre Vite, nous utilisons des plugins.

Nous pouvons puiser dans le cycle de vie de build de Vite pour accéder au code Astro de l'utilisateur (en particulier ses `pages`) pendant le processus de build.

Maintenant, voici la partie amusante.

Tout d'abord, nous analyserons le code Astro en Arbres de Syntaxe Abstraite (ASTs).

Essentiellement, un AST sert de moyen de représenter la structure du code dans un langage de programmation. Tout comme une phrase peut être décomposée en noms, verbes et adjectifs, un AST dissèque le code en ses composants essentiels – variables, fonctions et opérations – et reflète leurs relations dans une structure arborescente.

Un composant Astro valide peut prendre différentes formes. Mais le `frontmatter` doit toujours être le premier nœud enfant du nœud racine.

Par exemple, ce qui suit est correct :

```js
---
 // frontmatter
---
// markup goes here
<h1> Hello world </h1>

```

Ce qui suit est invalide :

```js
<h1> Hello world </h1>

---
 // frontmatter
---

```

Avec cette heuristique, nous saisirons le premier nœud enfant dans la racine de notre AST analysé et prendrons quelques décisions :

*   Si le fichier a déjà une exportation `prerender`, ne rien faire, c'est-à-dire laisser le fichier tel quel.
*   Sinon, mettre à jour le code pour inclure `export const prerender = true` – nous mettrons donc à jour le code au sein de notre intégration. Il est important de noter que cela ne transforme que le code de la page à construire. Cela ne met pas à jour le fichier local.
*   Enfin, si une page n'a pas de frontmatter, nous en créerons un et inclurons l'extrait de code `export const prerender = true`.

### Comment initialiser des projets via des drapeaux CLI

La commande `create astro` est robuste. Mais parfois, vous n'avez pas la patience de sélectionner chaque option via des invites.

Dans de tels cas, utilisez les drapeaux CLI comme indiqué ci-dessous.

Initialisez un nouveau projet avec la commande suivante :

```bash
npm create astro@latest -- --template=minimal
--typescript=strictest --git --install
astro-integration-prerender-by-default

```

Cela configurera un nouveau projet Astro dans le répertoire `prerenderbyDefault` avec des drapeaux CLI passés au lieu de via des invites, c'est-à-dire `--template=minimal` utilisera le modèle minimal, `--template=strictest` utilisera la config typescript `strictest`, `--git` initialisera un dépôt Git et `--install` installera les dépendances.

Voici un tableau rapide des drapeaux CLI disponibles :

<table>
	<thead>
		<tr>
			<th>
				Nom
			</th>
			<th>
				Description
			</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<code>--template &lt;name&gt;</code>
			</td>
			<td>
				Spécifier le modèle. Où <code>name</code> pourrait être <br>n'importe lequel des répertoires dans <br><a href="https://github.com/withastro/astro/tree/main/examples/">https://github.com/withastro/astro/tree/main/examples/</a>.
			</td>
		</tr>
		<tr>
			<td>
				<br><br><code>--install</code> / <code>--no-install</code>
			</td>
			<td>
				<br><br>Installer les dépendances (ou non).
			</td>
		</tr>
		<tr>
			<td>
				<br><br><code>--git</code> / <code>--no-git</code>
			</td>
			<td>
				<br><br>Initialiser le dépôt git (ou non).
			</td>
		</tr>
		<tr>
			<td>
				<br><br><code>--yes</code> (<code>-y</code>)
			</td>
			<td>
				<br><br>Sauter toutes les invites et accepter les valeurs par défaut.
			</td>
		</tr>
		<tr>
			<td>
				<br><br><code>--no</code> (<code>-n</code>)
			</td>
			<td>
				<br><br>Sauter toutes les invites et refuser les valeurs par défaut.
			</td>
		</tr>
		<tr>
			<td>
				<br><br><code>--dry-run</code>
			</td>
			<td>
				<br><br>Parcourir les étapes de création de projet <br>sans aucune exécution réelle. Utile pour une "répétition générale"
			</td>
		</tr>
		<tr>
			<td>
				<br><br><code>--skip-houston</code>
			</td>
			<td>
				<br><br>Sauter l'animation Houston. Si vous êtes pressé, cela fait gagner du temps et démarre l'invite directement.
			</td>
		</tr>
		<tr>
			<td>
				<br><br> <code>--typescript &lt;option&gt;</code>
			</td>
			<td>
				<br><br>Où <code>option</code> est <code>strict</code> , <code>strictest</code> ou <code>relaxed</code>
			</td>
		</tr>
	</tbody>
</table>

Maintenant, changez de répertoire et exécutez la nouvelle application Astro :

```bash
cd ./astro-integration-prerender-by-default && npm run start

```

Par défaut, cela devrait démarrer l'application sur un port disponible, par exemple `localhost:3000`.

### Comment configurer l'intégration

Créez un nouveau fichier `index` dans `integrations/prerenderByDefault` et créez la fonction d'usine d'intégration comme indiqué ci-dessous :

```bash
export default function prerenderByDefault() {
  return {
    name: "astro-prerender-by-default",
    hooks: {
      "astro:config:setup"() {},
      "astro:config:done"() {},
    },
  };
}


```

Ajoutons le support pour la configuration de l'intégration en acceptant un objet de configuration.

Allez-y et créez un fichier `types.ts` dans `integrations/prerenderByDefault` comme indiqué ci-dessous :

```js
export type Config =
  | {
      silent?: boolean;
    }
  | undefined;

```

Maintenant, ajoutons un paramètre `config` à la fonction d'usine `prerenderByDefault` et typons sa valeur de retour comme indiqué ci-dessous :

```js
import type { AstroIntegration } from "astro";
import type { Config } from "./types";

export default function prerenderByDefault(config: Config): AstroIntegration {
    // ...
}


```

Maintenant, allez-y et ajoutez l'intégration dans le fichier de configuration du projet :

```js
import { defineConfig } from "astro/config";
import prerenderByDefault from "./integrations/prerenderByDefault";

export default defineConfig({
  integrations: [prerenderByDefault()],
});


```

### Comment valider une configuration Astro résolue

Allons de l'avant pour gérer notre validation d'intégration. Tout d'abord, nous créerons une méthode `isValidAstroConfig` pour recevoir une configuration Astro et un résultat de validation.

Voici l'implémentation ci-dessous :

```js
// 📂 prerenderByDefault/isValidAstroConfig.ts

import type { AstroConfig } from "astro";

/**
 * @param config: the fully resolved astro project config
 * @returns validation result
 */
export const isValidAstroConfig = (config: AstroConfig) => {
  if (config.output !== "server") {
    return { type: "invalid_output_config", value: false } as const;
  }

  if (!config.adapter) {
    return { type: "invalid_adapter_config", value: false } as const;
  }

  /**
   * configuration is valid
   */
  return { type: "success", value: true } as const;
};

```

J'ai décidé de renvoyer un objet au lieu de simples valeurs booléennes pour utiliser la [vérification d'exhaustivité](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#exhaustiveness-checking) de typescript.

Maintenant, exploitons `isValidAstroConfig` dans le hook `astro:config:done` en faisant ce qui suit :

*   Récupérer la configuration finale du projet Astro
*   Valider la configuration
*   Enregistrer des messages dans la console du serveur en fonction du résultat de la validation

Voici comment :

```js
export default function prerenderByDefault(config: Config): AstroIntegration {
  return {
    name: "astro-prerender-by-default",
    hooks: {
      "astro:config:setup"() {},
      // 👀 look below
      "astro:config:done"(options) {
        // get the 'silent' integration config property, default to false.
        const silent = config?.silent ?? false;

        // validate the resolved project configuration
        const validationResult = isValidAstroConfig(options.config);

        /**
         * Leverage Typescript exhaustive check to handle all
         * validation types and log messages where appropriate
         */
        switch (validationResult.type) {
          case "invalid_adapter_config":
            log({
              silent,
              message: `Adapter not set for hybrid rendering. Skipping`,
            });
            return;

          case "invalid_output_config":
            log({
              silent,
              message: `Config output not set to "server". Skipping`,
            });
            return;

          case "success":
            return;

          default:
            const _exhaustiveCheck: never = validationResult;
            return _exhaustiveCheck;
        }
      },
    },
  };
}

```

Nous appelons une fonction `log` pour écrire des messages dans la console du serveur en fonction du résultat de la validation, mais cette fonction n'existe pas.

Nous avons écrit des fonctions de journalisation similaires, alors voici le code pour celle-ci :

```js
// 📂 prerenderByDefault/log.ts

import kleur from "kleur";

type LogOptions = {
  silent: boolean;
  message: string;
};

const dateTimeFormat = new Intl.DateTimeFormat([], {
  hour: "2-digit",
  minute: "2-digit",
  second: "2-digit",
});

export const log = (options: LogOptions) => {
  // do not log if the "silent" argument is passed
  if (options.silent) {
    return;
  }

  // get new date
  const date = dateTimeFormat.format(new Date());

  // log to the console with colours and text formatting
  console.log(`${kleur.gray(date)} ${kleur
    .bold()
    .magenta("[astro-prerender-by-default]")} ${options.message}
  `);
};

```

Maintenant, assurez-vous d'importer la fonction `log` dans `prerenderByDefault/index.ts` :

```js
import { log } from "./log";
...

```

Maintenant, si nous allons de l'avant et construisons le projet avec `npm run build`, nous devrions avoir notre journal de validation d'intégration affiché comme indiqué ci-dessous :

![Journal de serveur de validation](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-12-at-07.01.41.png)
_Journal de serveur de validation_

Ceci est attendu car le projet n'a pas de sortie `server` configurée. Dans ce cas, le rendu hybride ne peut pas être utilisé.

### Comment appliquer des plugins Vite dans des intégrations personnalisées

Astro utilise Vite sous le capot. En tant que tel, il est possible de passer des configurations supplémentaires à Vite dans le fichier `astro.config.mjs`, par exemple :

```js
{
  vite: {
    //This adds a custom plugin directly to the Astro config
    plugins: [myPlugin()]
  }
}

```

Par conséquent, nous pouvons en profiter dans notre intégration.

Rappelez-vous de la section des hooks de cycle de vie que `astro:config:setup` est l'endroit où nous pouvons intervenir pour étendre la configuration du projet. Faisons-le maintenant :

```js
import { injectVitePlugin } from "./injectVitePlugin";
// ...

  return {
    name: "astro-prerender-by-default",
    hooks: {
      // 👀 look here
      "astro:config:setup"(options) {
        options.updateConfig({
          vite: {
            plugins: [injectVitePlugin()],
          },
        });
      },
}
// ...

```

Dans le tableau des plugins, nous invoquons `injectVitePlugin()`, qui devrait renvoyer un plugin Vite valide.

Oh, mais qu'est-ce qu'un plugin Vite valide, pourriez-vous demander ?

Similaire aux intégrations Astro, un plugin Vite est représenté par un objet avec une propriété name et des hooks spécifiques, qui sont des méthodes sur l'objet, par exemple :

```js
{
  name: "vite-plugin-${name},
  configResolved() {
   // Called after the Vite config is resolved
  }
}

```

Allons-y et écrivons une version de base de `injectVitePlugin` :

```js
import type { Plugin } from "vite";

export const injectVitePlugin = (): Plugin => {
  //Our prerender plugin to be fleshed out
  const prerenderByDefaultPlugin = { name: "" };

  return {
    // name follows the pattern vite-plugin-${framework}-${feature}
    name: "vite-plugin-astro-inject-default-prerender",
    configResolved: (options) => {
      //Grab the Vite plugins in the resolved config
	 // and add our plugin as the first in the list
      (options.plugins as Plugin[]).unshift(prerenderByDefaultPlugin);
    },
  };
};

```

Nous allons étoffer cette structure de base, mais considérez d'abord que dans le cycle de vie des hooks astro, `astro:config:setup` s'exécute avant `astro:config:done`.

Nous mettons à jour les plugins Vite dans `astro:config:setup`. Mais nous validons la config du projet dans `astro:config:done`.

Nous allons probablement rencontrer une condition de concurrence ici, c'est-à-dire mettre à jour la liste des plugins Vite dans `astro:config:setup` avant que `astro:config:done` n'ait entièrement validé la config du projet.

Comment pouvons-nous résoudre cela ?

Exploitons une promesse.

Nous initialiserons une promesse qui n'est résolue qu'après la fin de la validation, et nous attendrons la résolution de la promesse dans `injectVitePlugin`. Heureusement, `astro:config:setup` peut prendre des fonctions asynchrones. Particulièrement dans la ou les fonctions de plugin Vite.

Passons en revue les changements requis pour y parvenir.

Tout d'abord, introduisons un type `ValidationResult` dans notre fichier `types.ts` :

```js
// 📂 prerenderByDefault/types.ts

import type { isValidAstroConfig } from "./isValidAstroConfig";

export type ValidationResult = ReturnType<typeof isValidAstroConfig>;

// ...

```

Maintenant, créez une nouvelle promesse dans le fichier `index` principal :

```js
// ...
import type { Config, ValidationResult } from "./types";

let resolveValidationResult: (value: ValidationResult) => void;

let validationResultPromise = new Promise<ValidationResult>((resolve) => {
  resolveValidationResult = resolve;
});

// ...

```

Juste après que la validation est faite dans `astro:config:done`, allons-y et résolvons la promesse avec le résultat de la validation :

```js
// ...
"astro:config:done"(options) {
   const silent = config?.silent ?? false;
   const validationResult = isValidAstroConfig(options.config);

   // resolve the validation promise
   resolveValidationResult(validationResult);

   // ...
}

```

Ensuite, passez à la fois la configuration de l'intégration et la promesse de résultat de validation à `injectVitePlugin` :

```js
// ...
plugins: [injectVitePlugin(config, validationResultPromise)],

```

Nous devons maintenant mettre à jour `injectVitePlugin` pour attendre la promesse de résultat de validation comme indiqué ci-dessous :

```js
import type { Plugin } from "vite";
import type { Config, ValidationResult } from "./types";

export const injectVitePlugin = async (
  config: Config,
  validationResultPromise: Promise<ValidationResult>
): Promise<Plugin | null> => {

  // await the validation result promise before continuing
  const validationResult = await validationResultPromise;

  // exit if the validation result value is false
  if (!validationResult.value) {
    return null;
  }

  // TBD ..
  const prerenderByDefaultPlugin = { name: "" };

  return {
    name: "vite-plugin-astro-inject-default-prerender",
    configResolved: (options) => {
      (options.plugins as Plugin[]).unshift(prerenderByDefaultPlugin);
    },
  };
};

```

Ouf ! Nous avons éradiqué la condition de concurrence embêtante. Notre solution prend donc forme joliment, hein ?

### Comment écrire des plugins Vite pour Astro

Nous savons à quoi ressemble un plugin Vite maintenant. Mais la fonctionnalité principale de notre intégration n'a pas encore été écrite. Ceci est actuellement représenté par la variable `prerenderByDefaultPlugin`, c'est-à-dire :

```js
// TBD...
  const prerenderByDefaultPlugin = { name: "" };

```

Changeons cela pour être renvoyé par une fonction `getVitePlugin` séparée :

```js
// ...
import { getVitePlugin } from "./getVitePlugin";

export const injectVitePlugin = async (
  config: Config,
  validationResultPromise: Promise<ValidationResult>
): Promise<Plugin | null> => {
  // ...

  const prerenderByDefaultPlugin = getVitePlugin(config);

  // ...
};


```

Où `getVitePlugin` est ce qui suit :

```js
import type { Config } from "./types";

export const getVitePlugin = (config: Config) => ({
  name: "vite-plugin-astro-prerender-by-default",
});

```

### Comment analyser et transformer les ASTs

Nous voulons transformer le code Astro d'un utilisateur et effectuer des mises à jour avant qu'il ne soit finalement construit.

Heureusement, Vite a un hook `transform` que nous pouvons exploiter juste pour cela. Jouons un peu avec cela dans notre fonction `getVitePlugin` :

```js
import type { Plugin } from "vite";
import type { Config } from "./types";
import { log } from "./log";

export const getVitePlugin = (config: Config): Plugin => {
  const silent = config?.silent ?? false;

  return {
    name: "vite-plugin-astro-prerender-by-default",
    async transform(code, id) {
      // 👀 log the value of the id
      log({
        silent,
        message: id,
      });
    },
  };
};

```

Le hook `transform` est idéal pour transformer des modules individuels dans le processus de build, et nous recevons le `code` dans le fichier sous forme de `string` et un `id` représentant le chemin `string` vers le nom du fichier.

Pour tester comment cela fonctionne, mettez à jour la config du projet Astro pour inclure une sortie `server`.

```js
export default defineConfig({
  output: "server",
  integrations: [prerenderByDefault()],
});

```

Ensuite, ajoutez un adaptateur pour gérer le rendu côté serveur avec :

```bash
npx astro add netlify

```

Nous pouvons maintenant explorer le journal de `getVitePlugin` en exécutant `npm run build` depuis le terminal.

Remarquez combien de fichiers supplémentaires sont transformés par rapport aux seules pages `.astro` de l'utilisateur.

![Explorer la liste des fichiers transformés.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-12-at-09.18.14.png)
_Explorer la liste des fichiers transformés._

La plupart des fichiers ici sont liés aux rouages internes d'Astro. Nous ne devons donc nous préoccuper que des pages `.astro` de l'utilisateur. Nous voulons transformer ces fichiers tout en laissant tout le reste tel quel.

Ajoutons une condition simple :

```js
// ...
  return {
    name: "vite-plugin-astro-prerender-by-default",
    async transform(code, id) {
      // 👀 filtrer les autres types de fichiers
      if (!id.endsWith(".astro")) {
        return;
      }

      // journaliser la valeur de l'id
      log({
        silent,
        message: id,
      });
    },
  };

```

Maintenant, relancez le build, et nous ne devrions avoir que les fichiers de page `.astro` de l'utilisateur.

![Journalisation des fichiers de page du projet.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-12-at-09.22.30.png)
_Journalisation des fichiers de page du projet._

C'est excellent.

Juste après la condition, nous pouvons passer à l'analyse du code. Pour ce faire, nous exploiterons l'utilitaire `parse` exporté du compilateur d'Astro comme indiqué ci-dessous :

```js
    // ...
    async transform(code, id) {
      if (!id.endsWith(".astro")) {
        return;
      }

	  // 👀
      const { ast } = await parse(code);

      // 👀 journaux pour le débogage
      log({
        silent,
        message: "Parsed AST",
      });

      console.log(ast);
    }

```

Ce projet n'a qu'une seule page dans `src/index.astro`. Donc, essentiellement, seule cette page sera transformée.

Voici le contenu de la page :

```js
---
---

<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width" />
    <meta name="generator" content={Astro.generator} />
    <title>Astro</title>
  </head>
  <body>
    <h1>Astro</h1>
  </body>
</html>

```

Voici l'AST correspondant journalisé dans la console :

```js
{
  type: 'root',
  children: [
    { type: 'frontmatter', value: '\n', position: [Object] },
    {
      type: 'element',
      name: 'html',
      attributes: [Array],
      children: [Array]
    },
    { type: 'text', value: '\n', position: [Object] }
  ]
}

```

Chaque AST analysé aura un élément `root`. Un fichier vide aura la forme :

```js
{ type: 'root' }

```

Sachant cela, nous pouvons construire notre logique d'analyse. Mais nous avons besoin d'un moyen de parcourir l'AST entier.

Nous pourrions écrire une fonction sophistiquée pour boucler sur chaque élément de l'arbre. Mais nous pouvons exploiter l'utilitaire `walk` du compilateur Astro, qui traversera chaque nœud de l'arbre, et nous pourrions effectuer n'importe quelle action sur un nœud spécifié via un rappel (callback).

Essayons cela en ajoutant ce qui suit :

```js
const { ast } = await parse(code);

// 👀
walk(ast, (node) => {
  console.log("=========== \n", node);
});

```

Inspectez les journaux, et nous devrions avoir les différents nœuds journalisés dans la console, par exemple :

```js
===========
 {
  type: 'root',
  children: [
    { type: 'frontmatter', value: '\n', position: [Object] },
    {
      type: 'element',
      name: 'html',
      attributes: [Array],
      children: [Array]
    },
    { type: 'text', value: '\n', position: [Object] }
  ]
}
===========
 {
  type: 'frontmatter',
  value: '\n',
  position: {
    start: { line: 1, column: 1, offset: 0 },
    end: { line: 2, column: 4, offset: 7 }
  }
}
===========
// ... see logs

```

C'est l'heure du jeu. Allons-y et écrivons le code complet, ce qui implique :

*   Parcourir l'AST
*   Vérifier si le fichier a un frontmatter
*   Vérifier si le fichier a déjà une exportation `prerender` dans son frontmatter. Pour cela, nous utiliserons [es-module-lexer](https://github.com/guybedford/es-module-lexer#readme) , qui sort la liste des exportations des spécificateurs d'importation
*   Ajouter `export const prerender = true` au code là où c'est nécessaire
*   Après avoir transformé l'AST, c'est-à-dire ajouté `export const prerender = true` là où c'est nécessaire, nous renverrons l'AST en code via l'utilitaire `serialize` du compilateur Astro.

C'est parti :

```js
import type { Plugin } from "vite";
import type { Config } from "./types";
import { parse } from "@astrojs/compiler";
import { walk, is, serialize } from "@astrojs/compiler/utils";
import { parse as parseESModuleLexer } from "es-module-lexer";

import { log } from "./log";

export const getVitePlugin = (config: Config): Plugin => {
  const silent = config?.silent ?? false;

  return {
    name: "vite-plugin-astro-prerender-by-default",
    async transform(code, id) {
      if (!id.endsWith(".astro")) {
        return;
      }

      const { ast } = await parse(code);

      walk(ast, (node) => {
        if (is.root(node)) {
          const firstChildNode = node.children?.[0];

          //Vérifier qu'un frontmatter existe comme premier nœud enfant
          if (firstChildNode?.type === "frontmatter") {
            //En utilisant es-module-lexer, obtenir la liste des exportations
            const [, exports] = parseESModuleLexer(firstChildNode.value);

            //Vérifier si une exportation est nommée "prerender". "n" signifie "name" (nom).
            if (exports.some((e) => e.n === "prerender")) {
              log({
                silent,
                message: "'prerender' export found. Skipping",
              });

              // sortir - laisser la valeur prerender exportée prendre effet
              return;
            }

            // ajouter l'exportation prerender pour le build statique, c'est-à-dire "export const prerender = true."
            // notez que nous concaténons cela à la valeur de chaîne actuelle du nœud
            firstChildNode.value = `\nexport const prerender = true; \n ${firstChildNode.value}`;

            log({
              silent,
              message: "Added 'prerender' export to frontmatter",
            });
          } else {
            // Pas de frontmatter dans ce composant astro. Ajouter un nœud frontmatter et l'exportation par défaut
            log({
              silent,
              message: "No frontmatter, going ahead to add one",
            });

            // "unshift" pour ajouter cela au début de la liste, c'est-à-dire le premier enfant
            node.children.unshift({
              type: "frontmatter",
              value: "\nexport const prerender = true\n",
            });
          }
        }
      });

      //sérialiser l'AST et renvoyer le résultat
      const result = serialize(ast);

      // ajouté pour le débogage du lecteur
      console.log(result);
      return result;
    },
  };
};

```

Le bloc de code ci-dessus est annoté. Veuillez le regarder de près. Si quelque chose n'est pas clair, ajoutez quelques `console.log`. Avec l'annotation, je suis sûr que vous comprendrez encore mieux les explications.

### Tests manuels

Nous avons notre solution complète. Maintenant, testons-la. Tout d'abord, construisez le projet avec `npm run build`, et même si nous avons une sortie `server` dans la config Astro, nous avons maintenant la page `index.astro` construite statiquement par défaut.

![Pré-rendu de la route statique index.astro.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-12-at-16.10.58@2x.png)
_Pré-rendu de la route statique index.astro._

Pour rendre une page côté serveur, nous devons ajouter manuellement `export const prerender = false`.

Créez une nouvelle page avec un contenu identique à `index.astro` et ayez l'exportation `prerender`.

```js
---
export const prerender = false;
---

<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width" />
    <meta name="generator" content={Astro.generator} />
    <title>SSR</title>
  </head>
  <body>
    <h1>SSR</h1>
  </body>
</html>

```

Maintenant, relancez le build et remarquez comment seule la page `index.astro` est pré-rendue.

![Sauter le pré-rendu lorsque l'exportation est trouvée.](https://blog.ohansemmanuel.com/content/images/2023/06/CleanShot-2023-04-12-at-16.17.15@2x.png)
_Sauter le pré-rendu lorsque l'exportation est trouvée._

## Comment construire des Renderers et des Intégrations de Bibliothèque

Comme indiqué plus tôt dans le chapitre, l'accent est mis ici sur les intégrations de fonctionnalités. Pour construire des renderers et des intégrations de bibliothèque, je recommande fortement de jeter un coup d'œil au code source des intégrations populaires telles que :

*   Les intégrations de renderer [React](https://github.com/withastro/astro/tree/main/packages/integrations/react) , [Preact](https://github.com/withastro/astro/tree/main/packages/integrations/preact) ou [Vue](https://github.com/withastro/astro/tree/main/packages/integrations/vue).
*   Les intégrations de bibliothèque [Tailwind](https://github.com/withastro/astro/tree/main/packages/integrations/tailwind) ou [partytown](https://github.com/withastro/astro/tree/main/packages/integrations/partytown).

La plupart de ces intégrations font à peine 100 lignes de code à la base. Creusez dedans !

## Conclusion de ce chapitre

Construire des intégrations personnalisées est définitivement quelque chose que vous pouvez faire. Bon sang ! Écrire des compilateurs n'est pas un prérequis.

En s'appuyant sur les explications et les exemples discutés ici, nous avons vu comment de simples mortels comme nous peuvent atteindre les rouages internes d'Astro et le plier à notre volonté. Maintenant, mettez ces connaissances en pratique.

![La fin.](https://www.freecodecamp.org/news/content/images/2023/06/image-141.png)
_La fin._

# Conclusion

Regardez qui est arrivé jusqu'au bout ! 🚀

Oui, vous !

J'ai mis tout mon cœur dans ces chapitres, et je suis sûr que vous avez appris une chose ou deux.

Alors, où allez-vous ensuite ?

Premièrement, je recommande fortement de visiter la [documentation](https://astro.build/) officielle d'Astro. C'est une excellente ressource qui vous sera bénéfique à long terme lorsque vous développerez des applications Astro.

Deuxièmement, réfléchissez aux fonctionnalités qui font qu'Astro se démarque :

*   **Exploitez les îlots de composants** : Une nouvelle architecture web pour construire des sites web plus rapides.
*   **Zéro JS, par défaut** : Gardez les applications rapides sans surcharge d'exécution JS.
*   **Prêt pour l'Edge** : Déployez n'importe où, même sur des runtimes edge mondiaux comme Deno ou Cloudflare.
*   **Incroyablement personnalisable** : Utilisez Tailwind, MDX et plus de 100 autres [intégrations](https://astro.build/integrations/).
*   **Apportez votre propre framework** : Prend en charge React, Preact, Vue, Svelte, Solid, Lit et plus encore.

## Liens et ressources utiles

*   ⚠️ [Restez en contact avec mon travail](https://www.ohansemmanuel.com/newsletter) et soyez le premier informé des mises à jour de ce livre (et de mes autres écrits). [Faites-le ici](https://www.ohansemmanuel.com/newsletter).
*   [Intégrations Astro](https://astro.build/integrations/) : explorez-les pour ajouter plus de fonctionnalités à vos applications Astro.
*   [Thèmes Astro](https://astro.build/themes) : explorez les thèmes avec lesquels vous pouvez démarrer votre nouveau projet.

À la prochaine,

[Ohans E.](https://www.ohansemmanuel.com/)🥂

## Vous voulez obtenir l'ebook ?

![Image](https://www.freecodecamp.org/news/content/images/2023/06/book-cover-transparent-1.png)
_[Télécharger les ebooks sur Github](https://github.com/understanding-astro/understanding-astro-book)_

*   500+ pages de valeur
*   4+ chapitres de projets pratiques
*   100+ illustrations et images soigneusement conçues
*   Apprenez des techniques pour construire des applications plus rapides
*   **Intégrez React, Svelte, Vue, Tailwind** et plus encore dans un projet Astro
*   Apprenez à construire votre propre **implémentation d'îlots de composants** à partir de zéro
*   Apprenez à **construire des applications fullstack avec Astro** (sans sacrifier la performance)
*   Allez **au-delà des bases** et analysez le code Astro en ASTs et construisez des fonctionnalités de projet personnalisées

_[Téléchargez l'ebook gratuit sur Github.](https://ohans.me/ua-github)_