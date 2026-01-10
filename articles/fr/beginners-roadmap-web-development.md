---
title: Feuille de route pour débutants en développement web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-23T16:32:52.000Z'
originalURL: https://freecodecamp.org/news/beginners-roadmap-web-development
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/roadmap-web-development.jpg
tags:
- name: learn to code
  slug: learn-to-code
- name: Web Development
  slug: web-development
seo_title: Feuille de route pour débutants en développement web
seo_desc: 'By Jessica Chan

  This beginner''s roadmap lays out all the basics for web development. We’re going
  to go through each step–from figuring out what code editor to use, to what JavaScript
  framework or back-end language you can pick up. And we’ll also incl...'
---

Par Jessica Chan

Cette feuille de route pour débutants expose toutes les bases du développement web. Nous allons passer en revue chaque étape, depuis le choix de l'éditeur de code à utiliser, jusqu'au choix du framework JavaScript ou du langage back-end que vous pouvez apprendre. Et nous inclurons également des liens vers des ressources où vous pouvez apprendre ces compétences.

En fait, si vous débutez, tout ce dont vous avez besoin de savoir pour l'instant, ce sont les bases. Vous n'avez vraiment pas besoin de connaître chaque technologie, outil ou langage existant dès le départ. (Vous traverserez ce pont quand vous y arriverez, croyez-moi !)

**À la fin de ce guide, vous aurez une compréhension des bases du développement web, des compétences dont vous avez besoin et où les trouver !**

**1 : Qu'est-ce que le développement web** : Comment fonctionnent les sites web, front-end vs back-end, éditeur de code

**2 : Bases du front-end** : HTML, CSS et JavaScript

**3 : Outils** : Gestionnaires de paquets, outils de build, contrôle de version

**4a : Front-end supplémentaire** : Sass, design responsive, frameworks JavaScript

**4b : Bases du back-end** : Gestion du serveur et de la base de données, langage de programmation

Dans cette feuille de route, je recommande de faire les étapes 1, 2 et 3 dans l'ordre. Ensuite, selon que vous souhaitiez vous concentrer davantage sur le front-end ou le back-end, vous pouvez faire les étapes 4a ou 4b dans n'importe quel ordre.

Je pense personnellement qu'il est bon pour les développeurs web front-end de connaître au moins un peu de back-end, et vice versa. À tout le moins, connaître les bases des deux vous aidera à déterminer si vous préférez le front-end ou le back-end ?

%[https://www.youtube.com/watch?v=ysEN5RaKOlA]

Vous pouvez également consulter la [version mise à jour de cet article](https://coder-coder.com/learn-web-development) sur mon blog !

## **1 : Qu'est-ce que le développement web ?**

Avant de nous lancer dans le codage proprement dit, examinons d'abord quelques informations générales sur ce qu'est le développement web : comment fonctionnent les sites web, la différence entre front-end et back-end, et l'utilisation d'un éditeur de code.

### **Comment fonctionnent les sites web ?**

Tous les sites web, à leur niveau le plus basique, ne sont qu'un ensemble de fichiers stockés sur un ordinateur appelé **serveur**. Ce serveur est connecté à Internet. Vous pouvez ensuite charger ce site web via un navigateur (comme Chrome, Firefox ou Safari) sur votre ordinateur ou votre téléphone. Votre navigateur est également appelé le **client** dans cette situation.

Ainsi, chaque fois que vous êtes sur Internet, vous (le client) recevez et chargez des données (comme des photos de chats) depuis le serveur, ainsi que soumettez des données au serveur (_**chargez plus de photos de chats !**_). Cet échange entre le client et le serveur est la base d'Internet.

Tout ce à quoi vous pouvez accéder dans votre navigateur est quelque chose qu'un développeur web a construit. Certains exemples sont les sites web de petites entreprises et les blogs du côté le plus simple, jusqu'aux applications web très complexes comme AirBnb, Facebook et Twitter.

### **Quelle est la différence entre front-end et back-end ?**

Les termes « front-end », « back-end » et « full stack » décrivent quelle partie de la relation client/serveur vous travaillez.

« Front-end » signifie que vous traitez principalement avec le côté client. Il est appelé « front-end » parce que c'est ce que vous pouvez voir dans le navigateur. À l'inverse, le « back-end » est la partie du site web que vous ne pouvez pas vraiment voir, mais il gère beaucoup de la logique et de la fonctionnalité nécessaires pour que tout fonctionne.

Une façon de penser à cela est que le développement web front-end est comme la partie « devant de la maison » d'un restaurant. C'est la section où les clients viennent voir et vivre l'expérience du restaurant – la décoration intérieure, les sièges, et bien sûr, manger la nourriture.

D'un autre côté, le développement web back-end est comme la partie « derrière la maison » du restaurant. C'est là que les livraisons et les stocks sont gérés, et que le processus de création de la nourriture se déroule. Il y a beaucoup de choses en coulisses que les clients ne verront pas, mais ils vivront (et espérons-le, apprécieront) le produit final – un délicieux repas !

Mises à part les illustrations amusantes, le développement web front-end et back-end servent des fonctions différentes mais très importantes.

### **Utilisation d'un éditeur de code**

Lorsque vous construisez un site web, l'outil le plus essentiel que vous utiliserez est votre éditeur de code ou IDE (Environnement de Développement Intégré). Cet outil vous permet d'écrire le balisage et le code qui composeront le site web.

Il existe plusieurs bonnes options, mais actuellement l'éditeur de code le plus populaire est VS Code. [VS Code](https://code.visualstudio.com/) est une version plus légère de Visual Studio, l'IDE principal de Microsoft. Il est rapide, gratuit, facile à utiliser, et vous pouvez le personnaliser avec des thèmes et des extensions.

D'autres éditeurs de code sont [Sublime Text](https://www.sublimetext.com/), [Atom](https://atom.io/), et [Vim](https://www.vim.org/download.php).

Si vous débutez, cependant, je recommande de jeter un coup d'œil à VS Code, que vous pouvez [télécharger depuis leur site web](https://code.visualstudio.com/).

Maintenant que nous avons couvert certains des concepts plus larges de ce qu'est le développement web, plongeons dans plus de détails – en commençant par le front-end.

## **2 : Bases du front-end**

Le front-end d'un site web est composé de trois types de fichiers : HTML, CSS et JavaScript. Ces fichiers sont ce qui est chargé dans le navigateur, côté client.

Examinons chacun d'eux de plus près.

### **HTML**

HTML, ou HyperText Markup Language, est la base de tous les sites web. C'est le type de fichier principal qui est chargé dans votre navigateur lorsque vous regardez un site web. Le fichier HTML contient tout le contenu de la page, et il utilise des balises pour désigner différents types de contenu.

Par exemple, vous pouvez utiliser des balises pour créer des titres, des paragraphes, des listes à puces, des images, et ainsi de suite. Les balises HTML ont par défaut quelques styles attachés, mais ils sont assez basiques, comme ce que vous verriez dans un document Word.

### **CSS**

CSS, ou Cascading Style Sheets, vous permet de styliser ce contenu HTML pour qu'il ait l'air bien et élégant. Vous pouvez ajouter des couleurs, des polices personnalisées, et disposer les éléments de votre site web comme vous le souhaitez. Vous pouvez même créer des animations et des formes avec CSS !

Il y a beaucoup de profondeur dans CSS, et parfois les gens ont tendance à le survoler pour passer à des choses comme JavaScript. Cependant, je ne peux pas assez insister sur l'importance de comprendre comment convertir un design en une mise en page de site web en utilisant CSS. Si vous voulez vous spécialiser dans le front-end, il est essentiel d'avoir des compétences vraiment solides en CSS.

### **JavaScript**

JavaScript est un langage de programmation conçu pour s'exécuter dans le navigateur. En utilisant JavaScript, vous pouvez rendre votre site web dynamique, ce qui signifie qu'il répondra à différentes entrées de l'utilisateur ou d'autres sources.

Par exemple, vous pouvez construire un bouton « Retour en haut » qui, lorsque l'utilisateur clique dessus, le fait défiler vers le haut de la page. Ou vous pouvez construire un widget météo qui affichera la météo d'aujourd'hui en fonction de l'emplacement de l'utilisateur dans le monde.

Surtout si vous voulez développer vos compétences plus tard avec un framework JavaScript comme React, vous comprendrez mieux si vous prenez le temps d'apprendre d'abord le JavaScript vanilla. C'est un langage vraiment amusant à apprendre, et il y a tant de choses que vous pouvez faire avec !

### **Où apprendre HTML, CSS et JavaScript**

On me demande souvent quels sont les meilleurs endroits pour apprendre à coder, et je leur cite généralement certaines des ressources suivantes. De plus, j'ai une liste plus détaillée des [meilleurs cours pour apprendre le développement web](https://coder-coder.com/best-web-development-courses/) sur mon blog – vous pourriez la trouver utile !

_**Note** : Certains des liens ci-dessous (ceux vers des cours payants et des livres) sont des liens d'affiliation, ce qui signifie que je recevrai une commission si vous achetez via eux sans frais supplémentaires pour vous. C'est une façon de me soutenir dans la création de ressources utiles comme celle-ci !_

**freeCodeCamp**

L'un de mes endroits préférés à recommander est [freeCodeCamp](http://freecodecamp.org/). C'est un bootcamp de codage en ligne qui est à but non lucratif et complètement gratuit ! J'aime cette option car si vous êtes débutant et pas complètement sûr que le codage soit fait pour vous, c'est une façon sans pression et sans risque de voir si vous aimez ça.

Un inconvénient de freeCodeCamp est que bien qu'ils aient un programme incroyable avec un environnement de codage intégré, ils n'ont pas de vidéos structurées en tant que tel.

Donc, si vous aimez vraiment apprendre via des vidéos, voici quelques autres options :

**Team Treehouse**

[Team Treehouse](https://treehouse.7eer.net/c/1296848/228915/3944?subId1=fcc-roadmap) est une plateforme d'apprentissage en ligne premium basée sur des vidéos et propose plusieurs parcours que vous pouvez suivre. Ils ont même un programme de diplôme Tech en ligne qui est comme un bootcamp en ligne que vous pouvez compléter en 4-5 mois.

Malheureusement, Treehouse n'est pas gratuit, mais ils ont différents plans mensuels ou annuels selon votre budget. Ils ont un [essai gratuit de 7 jours](https://treehouse.7eer.net/c/1296848/517990/3944?subId1=fcc-roadmap) pour que vous puissiez voir si vous aimez ça, et je peux également vous offrir une réduction où vous pouvez obtenir [$100 de réduction sur 1 an de leur Plan Basique](https://treehouse.7eer.net/c/1296848/294479/3944?subId1=fcc-roadmap). Si vous êtes assez sûr de vouloir vous lancer dans le développement web, Team Treehouse est un excellent endroit pour apprendre.

Si vous êtes plus fan de cours vidéo ponctuels, il existe des options gratuites et payantes :

**Wes Bos**

Wes Bos propose des cours gratuits sur l'apprentissage de [Flexbox](https://flexbox.io/friend/CODERCODER), [CSS Grid](https://cssgrid.io/friend/CODERCODER) et [JavaScript](https://javascript30.com/friend/CODERCODER) qui sont excellents. Je viens de suivre son cours sur CSS Grid, et il était très complet et aussi amusant. Wes est un excellent professeur !

**Udemy**

Udemy est une plateforme d'apprentissage en ligne avec beaucoup de grands cours également. Un en particulier que vous pourriez aimer est [Le cours avancé CSS et Sass](https://click.linksynergy.com/deeplink?id=T4jMTDexBoM&mid=39197&murl=https%3A%2F%2Fwww.udemy.com%2Fadvanced-css-and-sass%2F) par Jonas Schmedtmann – ce cours payant couvre la grille CSS, flexbox, le design responsive, et d'autres sujets CSS !

**YouTube**

Il y a aussi une tonne de ressources vidéo gratuites sur YouTube :

Traversy Media, probablement la plus grande chaîne de développement web, a un [Cours accéléré HTML](https://www.youtube.com/watch?v=UB1O30fR-EE) et un [Cours accéléré CSS](https://www.youtube.com/watch?v=yfoY53QXEnI).

DesignCourse, une chaîne axée sur le design web et le front-end, a un [tutoriel HTML & CSS](https://www.youtube.com/watch?v=8gNrZ4lAnAw) également.

Et freeCodeCamp a sa propre chaîne YouTube, avec des vidéos comme un [cours Apprendre JavaScript](https://www.youtube.com/watch?v=PkZNo7MFNFg) et d'autres cours approfondis.

**Livres et articles sur le développement web**

Si vous êtes plus du genre à lire, je vous recommande vivement les éléments suivants :

Les livres incroyablement populaires de [Jon Duckett](https://amzn.to/2OYVKPG), sur HTML & CSS, et JavaScript & jQuery. Ces livres ne sont pas du tout vos manuels scolaires denses et ordinaires. Ils sont magnifiquement conçus, très bien écrits, et contiennent beaucoup de photos et d'images pour aider à enseigner le matériel.

Eloquent JavaScript est un autre livre que j'aime beaucoup. Vous pouvez le lire gratuitement sur [leur site web](https://eloquentjavascript.net/), ou acheter une [copie papier sur Amazon](https://amzn.to/2YwuZpZ) si vous aimez les livres physiques. J'ai celui-ci moi-même, et je l'aime vraiment !

Si vous souhaitez voir plus de recommandations de livres, consultez mon article sur [les livres recommandés pour apprendre le développement web](https://coder-coder.com/best-web-development-books/).

Et enfin, mais non des moindres, certains sites web qui ont de grands articles et d'autres ressources sont :

* [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Learn)
* [CSS Tricks](https://css-tricks.com/)
* [Smashing Magazine](https://www.smashingmagazine.com/)

## **3 : Outils**

Passons maintenant à quelques autres technologies front-end. Comme nous l'avons mentionné, HTML, CSS et JavaScript sont les blocs de construction de base du développement web front-end. En plus de ceux-ci, il y a quelques autres outils que vous voudrez apprendre.

### **Gestionnaires de paquets**

Les gestionnaires de paquets sont des collections en ligne de logiciels, dont beaucoup sont open source. Chaque logiciel, appelé package, est disponible pour que vous puissiez l'installer et l'utiliser dans vos propres projets.

Vous pouvez les considérer comme des plugins – au lieu d'écrire tout à partir de zéro, vous pouvez utiliser des utilitaires pratiques que d'autres personnes ont déjà écrits.

Le gestionnaire de paquets le plus populaire s'appelle [npm](https://www.npmjs.com/), ou Node Package Manager, mais vous pouvez également utiliser un autre gestionnaire appelé [Yarn](https://yarnpkg.com/en/). Les deux sont de bonnes options à connaître et à utiliser, bien qu'il soit probablement préférable de commencer avec npm.

Si vous êtes curieux d'en savoir plus, vous pouvez lire cet article sur [les bases de l'utilisation de npm](https://nodesource.com/blog/an-absolute-beginners-guide-to-using-npm/).

### **Outils de build**

Les bundlers de modules et les outils de build comme Webpack, Gulp ou Parcel sont une autre partie essentielle du workflow front-end.

À un niveau de base, ces outils exécutent des tâches et traitent des fichiers. Vous pouvez les utiliser pour compiler vos fichiers Sass en CSS, transpiler vos fichiers JavaScript ES6 en ES5 pour une meilleure compatibilité avec les navigateurs, exécuter un serveur web local, et bien d'autres tâches utiles.

[**Gulp**](https://gulpjs.com/), techniquement un runner de tâches, dispose d'une suite de packages npm que vous pouvez utiliser pour compiler et traiter vos fichiers.

[**Webpack**](https://webpack.js.org/) est un bundler super puissant qui peut faire tout ce que Gulp peut faire et plus encore. Il est largement utilisé dans les environnements JavaScript, en particulier avec les frameworks JavaScript (que nous aborderons un peu plus tard). Un inconvénient de Webpack est qu'il nécessite beaucoup de configuration pour démarrer, ce qui peut être frustrant.

[**Parcel**](https://parceljs.org/) est un bundler plus récent comme Webpack, mais il est pré-configuré dès le départ, donc vous pouvez littéralement le faire fonctionner en quelques minutes seulement. Et vous n'aurez pas à vous soucier autant de la configuration de tout.

Personnellement, j'aime utiliser Gulp pour mes propres workflows front-end où je veux simplement compiler mes fichiers Sass et JavaScript et ne pas faire trop d'autres choses.

**Liens utiles**

Si vous êtes intéressé par Gulp ou Parcel, j'ai des tutoriels pour les deux :

* [Utilisation de Gulp 4 dans votre workflow](https://coder-coder.com/gulp-4-walk-through/)
* [Guide de démarrage rapide pour Parcel](https://coder-coder.com/bundle-files-quickly-parcel/)

Si vous voulez en savoir plus sur Webpack, consultez les vidéos YouTube suivantes :

* [Cours accéléré sur Webpack par DesignCourse](https://www.youtube.com/watch?v=TzdEpgONurw)
* [Série en 10 parties sur Webpack par Colt Steele](https://www.youtube.com/watch?v=3On5Z0gjf4U)

### **Contrôle de version**

Le contrôle de version (également appelé contrôle de source) est un système qui suit chaque changement de code que vous apportez à vos fichiers de projet. Vous pouvez même revenir à un changement précédent si vous faites une erreur. C'est presque comme avoir des points de sauvegarde infinis pour votre projet, et laissez-moi vous dire, cela peut être un énorme sauveur.

Le système de contrôle de version le plus populaire est un système open source appelé [Git](https://git-scm.com/). En utilisant Git, vous pouvez stocker tous vos fichiers et leur historique de modifications dans des collections appelées dépôts.

Vous avez peut-être aussi entendu parler de [GitHub](https://github.com/), qui est une société d'hébergement en ligne appartenant à Microsoft où vous pouvez stocker tous vos dépôts Git.

Pour apprendre Git et GitHub, [GitHub.com](https://github.com/) dispose de certains [guides en ligne](https://guides.github.com) qui expliquent comment démarrer. Traversy Media propose également une [vidéo YouTube](https://www.youtube.com/watch?v=SWYqp7iY_Tc) expliquant comment fonctionne Git.

## **4a : Front-end supplémentaire**

Une fois que vous maîtrisez les bases du front-end, il y a quelques compétences intermédiaires supplémentaires que vous voudrez apprendre. Je recommande de regarder les éléments suivants : Sass, design responsive et un framework JavaScript.

### **Sass**

[Sass](https://sass-lang.com/) est une extension de CSS qui rend l'écriture des styles plus intuitive et modulaire. C'est un outil vraiment puissant. Avec Sass, vous pouvez diviser vos styles en plusieurs fichiers pour une meilleure organisation, créer des variables pour stocker des couleurs et des polices, et utiliser des mixins et des placeholders pour réutiliser facilement des styles.

Même si vous n'utilisez que certaines des fonctionnalités de base, comme l'imbrication, vous pourrez écrire vos styles plus rapidement et avec moins de maux de tête.

Vous pouvez en apprendre davantage sur Sass dans ce [tutoriel Scotch.io](https://scotch.io/tutorials/getting-started-with-sass), ainsi que dans une [vidéo YouTube de Dev Ed](https://www.youtube.com/watch?v=Zz6eOVaaelI).

### **Design responsive**

Le [design responsive](https://www.smashingmagazine.com/2011/01/guidelines-for-responsive-web-design/) garantit que vos styles auront une belle apparence sur tous les appareils – ordinateurs de bureau, tablettes et téléphones mobiles. Les pratiques de base du design responsive incluent l'utilisation de tailles flexibles pour les éléments, ainsi que l'utilisation de requêtes média pour cibler les styles pour des appareils et des largeurs spécifiques.

Par exemple, au lieu de définir votre contenu pour qu'il ait une largeur statique de 400px, vous pouvez utiliser une requête média et définir le contenu pour qu'il ait une largeur de 50% sur ordinateur et de 100% sur mobile.

Construire vos sites web avec du CSS responsive est un must de nos jours, car le trafic mobile dépasse le trafic desktop dans de nombreux cas.

Pour plus d'informations sur le design responsive et pour rendre vos sites web responsives, consultez [cet article](https://learn.shayhowe.com/advanced-html-css/responsive-web-design/). Je fais également des streams de codage en direct sur [ma chaîne YouTube](https://www.youtube.com/c/codercodertv) où je construis un site web à partir de zéro et les spectateurs peuvent me poser des questions en temps réel !

### **Frameworks JavaScript**

Une fois que vous maîtrisez les bases de JavaScript vanilla, vous pourriez vouloir apprendre l'un des frameworks JavaScript (surtout si vous voulez être un développeur full-stack JavaScript).

Ces frameworks viennent avec des structures et des composants pré-construits qui vous permettent de construire des applications plus rapidement que si vous partiez de zéro.

Actuellement, vous avez trois choix principaux : React, Angular et Vue.

**React** (techniquement une bibliothèque), a été créé par Facebook et est le framework le plus populaire en ce moment. Vous pouvez commencer à apprendre en allant sur le [site web de React.js](https://reactjs.org/docs/getting-started.html). Si vous êtes intéressé par un cours premium sur React, [Tyler McGinnins](https://tylermcginnis.com/courses/?affcode=36750_tycbdezb) et [Wes Bos](https://reactforbeginners.com/friend/CODERCODER) ont d'excellents cours.

**Angular** était le premier grand framework, et il a été créé par Google. Il est toujours très populaire, même s'il a été dépassé par React récemment. Vous pouvez commencer à apprendre Angular sur leur [site web](https://angular.io/start). Gary de DesignCourse a également un [cours accéléré sur Angular sur YouTube](https://www.youtube.com/watch?v=_TLhUCjY9iA).

**Vue** est un framework plus récent créé par Evan You, un ancien développeur Angular. Bien qu'il soit moins utilisé que React et Angular, il grandit rapidement et est également considéré comme facile et amusant à utiliser. Vous pouvez vous lancer avec sur le [site web de Vue](https://vuejs.org/v2/guide/).

**Quel framework devez-vous apprendre ?**

Vous vous demandez peut-être maintenant, « Ok, bien, quel framework est le meilleur ? »

La vérité est qu'ils sont tous bons. En développement web, il n'y a presque jamais un seul choix qui soit à 100% le meilleur choix pour chaque personne et chaque situation.

Votre choix sera probablement déterminé par votre travail, ou simplement par celui que vous préférez utiliser. Si votre objectif final est de décrocher un emploi, essayez de rechercher quel framework semble être le plus courant dans les offres d'emploi potentielles.

Ne vous inquiétez pas trop du choix du framework. Il est plus important que vous appreniez et compreniez les concepts qui les sous-tendent. De plus, une fois que vous avez appris un framework, il sera plus facile d'apprendre les autres (similaire aux langages de programmation).

Passons maintenant à notre dernière section : le développement web back-end !

## **4b : Bases du back-end**

Le back-end, ou le côté serveur du développement web, est composé de trois composants principaux : le serveur, un langage de programmation côté serveur et la base de données.

### **Serveur**

Comme nous l'avons mentionné au tout début, le serveur est l'ordinateur où tous les fichiers du site web, la base de données et d'autres composants sont stockés.

Les serveurs traditionnels fonctionnent sur des systèmes d'exploitation tels que Linux ou Windows. Ils sont considérés comme « centralisés » car tout – les fichiers du site web, le code back-end et les données sont stockés ensemble sur le serveur.

De nos jours, il existe également des architectures sans serveur, qui est un type de configuration plus décentralisé. Ce type d'application divise ces composants et utilise des fournisseurs tiers pour gérer chacun d'eux.

Malgré le nom, cependant, vous avez toujours besoin d'une sorte de serveur, au moins pour stocker vos fichiers de site web. Certains exemples de fournisseurs sans serveur sont [AWS](https://aws.amazon.com/) (Amazon Web Services) ou [Netlify](https://www.netlify.com/).

Les configurations sans serveur sont populaires car elles sont rapides, économiques et vous n'avez pas à vous soucier de la maintenance du serveur. Elles sont idéales pour les sites web statiques simples qui ne nécessitent pas un langage côté serveur traditionnel. Cependant, pour les applications très complexes, la configuration de serveur traditionnelle pourrait être une meilleure option.

Pour en savoir plus sur les configurations sans serveur, Netlify a un [article de blog informatif](https://www.netlify.com/blog/2016/09/29/a-step-by-step-guide-deploying-on-netlify/) qui vous guide à travers toutes les étapes pour configurer un site web statique avec déploiement.

### **Langage de programmation**

Sur le serveur, vous devez utiliser un langage de programmation pour écrire les fonctions et la logique de votre application. Le serveur compile ensuite votre code et transmet le résultat au client.

Les langages de programmation populaires pour le web incluent PHP, Python, Ruby, C# et Java. Il existe également une forme de JavaScript côté serveur – Node.js, qui est un environnement d'exécution capable d'exécuter du code JavaScript sur le serveur.

Il existe également des frameworks que vous pouvez utiliser avec chacun de ces langages côté serveur. Tout comme les frameworks JavaScript front-end, ces frameworks back-end sont des outils utiles qui rendent la construction d'applications web beaucoup plus rapide.

Examinons une liste des langages de programmation les plus couramment utilisés pour le développement web :

**C#**

C# a été développé comme le concurrent de Microsoft à Java. Il est utilisé pour créer des applications web avec le [framework .NET](https://docs.microsoft.com/en-us/dotnet/csharp/getting-started/introduction-to-the-csharp-language-and-the-net-framework), le développement de jeux, et peut même être utilisé pour créer des applications mobiles.

Endroits pour apprendre C# :[Livre jaune de programmation C# par Rob Miles](http://www.csharpcourse.com/)[Bases de C# sur Udemy](https://click.linksynergy.com/deeplink?id=T4jMTDexBoM&mid=39197&murl=https%3A%2F%2Fwww.udemy.com%2Fcsharp-tutorial-for-beginners)

**Java**

Java est l'un des langages de programmation les plus populaires, et est utilisé dans les applications web ainsi que pour construire des applications Android.

Endroits pour apprendre Java :[MOOC de l'Université d'Helsinki](https://mooc.fi/en/)[Le cours complet pour développeurs Java sur Udemy](https://click.linksynergy.com/deeplink?id=T4jMTDexBoM&mid=39197&murl=https%3A%2F%2Fwww.udemy.com%2Fjava-the-complete-java-developer-course)

**Node.js**

Node.js est une technologie très populaire (selon l'enquête des développeurs 2019 de Stack Overflow [enquête des développeurs](https://insights.stackoverflow.com/survey/2019#technology)). Une chose à noter : ce n'est pas techniquement un langage côté serveur – c'est une forme de JavaScript qui s'exécute sur le serveur en utilisant le framework [Express.js](https://expressjs.com/).

Endroits pour apprendre Node.js :[Tutoriel Node.js par Programming with Mosh](https://www.youtube.com/watch?v=TlB_eWDSMt4)[Apprendre Node par Wes Bos](https://learnnode.com/friend/CODERCODER)

**PHP**

PHP est le langage qui alimente [WordPress](https://wordpress.org/), donc ce pourrait être un bon choix si vous pensez que vous travaillerez avec des sites web de petites entreprises, car beaucoup d'entre eux utilisent WordPress. Vous pouvez également construire des applications web avec le framework [Laravel](https://laravel.com/).

Endroits pour apprendre PHP :[Introduction à PHP par mmtuts](https://www.youtube.com/watch?v=qVU3V0A05k8&list=PL0eyrZgxdwhwBToawjm9faF1ixePexft-)[PHP par Edwin Diaz sur Udemy](https://click.linksynergy.com/deeplink?id=T4jMTDexBoM&mid=39197&murl=https%3A%2F%2Fwww.udemy.com%2Fphp-for-complete-beginners-includes-msql-object-oriented)

**Python**

Python gagne en popularité, surtout car il est utilisé en science des données et en apprentissage automatique. Il est également considéré comme bon, car sa syntaxe est plus simple que certains autres langages. Si vous voulez construire des applications web, vous pouvez utiliser les frameworks [Django](https://www.djangoproject.com/) ou [Flask](https://www.fullstackpython.com/flask.html).

Endroits pour apprendre Python :[The Modern Python 3 Bootcamp par Colt Steele sur Udemy](https://click.linksynergy.com/deeplink?id=T4jMTDexBoM&mid=39197&murl=https%3A%2F%2Fwww.udemy.com%2Fthe-modern-python3-bootcamp)[LearnPython.org](https://learnpython.org/)

**Ruby**

Ruby est un autre langage qui a une syntaxe considérée comme facile à apprendre. Vous pouvez construire des applications web avec le framework [Ruby on Rails](https://rubyonrails.org/).

Endroits pour apprendre Ruby :[The Odin Project](https://www.theodinproject.com/courses)[Tutoriel Ruby on Rails par Michael Hartl](https://www.railstutorial.org/)

Tout comme avec les frameworks JavaScript, il n'y a pas de #1 meilleur langage de programmation. Votre choix doit être basé soit sur votre intérêt et préférence personnels, ainsi que sur les emplois potentiels – faites donc un peu de recherche sur celui qui pourrait être un bon choix _pour vous_.

### **Bases de données**

Les bases de données, comme leur nom l'indique, sont l'endroit où vous stockez les informations de votre site web. La plupart des bases de données utilisent un langage appelé [SQL](https://en.wikipedia.org/wiki/SQL) (prononcé « sequel ») qui signifie « Structured Query Language ».

Dans la base de données, les données sont stockées dans des tables, avec des lignes un peu comme des documents Excel complexes. Ensuite, vous pouvez écrire des requêtes en SQL afin de créer, lire, mettre à jour et supprimer des données.

La base de données est exécutée sur le serveur, en utilisant des serveurs comme [Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server) sur les serveurs Windows, et [MySQL](https://www.mysql.com/) pour Linux.

Il existe également des bases de données [NoSQL](https://www.mongodb.com/nosql-explained), qui stockent les données dans des fichiers JSON plutôt que dans les tables traditionnelles. Un type de base de données NoSQL est [MongoDB](https://www.mongodb.com/), qui est souvent utilisé avec les applications React, Angular et Vue.

Quelques exemples de la façon dont les données sont utilisées sur les sites web sont :

Si vous avez un formulaire de contact sur votre site web, vous pouvez construire le formulaire de sorte que chaque fois que quelqu'un soumet le formulaire, ses données soient sauvegardées dans votre base de données.

Vous pouvez également utiliser des connexions utilisateur dans la base de données, et écrire la logique dans le langage côté serveur pour gérer la vérification et l'authentification des connexions.

Quelques ressources pour apprendre les bases de SQL sont :

* [The Complete SQL Bootcamp par Jose Portilla sur Udemy](https://click.linksynergy.com/deeplink?id=T4jMTDexBoM&mid=39197&murl=https%3A%2F%2Fwww.udemy.com%2Fthe-complete-sql-bootcamp)
* [SQLBolt](https://sqlbolt.com)

### **Quelques conseils pour vous laisser...**

Merci d'avoir lu ! J'espère sincèrement que ce guide vous aide à commencer à apprendre le développement web.

Quelques conseils que j'ai si vous suivez la voie de l'auto-apprentissage :

1. **N'essayez pas d'apprendre tout à la fois.** Choisissez une compétence à apprendre à la fois.
2. **Ne sautez pas d'un tutoriel à l'autre.** Pendant que vous apprenez, il est acceptable de consulter différentes ressources pour voir celle que vous préférez. Mais encore une fois, choisissez-en une et essayez de la suivre jusqu'au bout.
3. **Sachez que l'apprentissage du développement web est un voyage à long terme.** Malgré les histoires que vous avez pu lire sur des personnes passant de zéro à un emploi de développeur web en 3 mois, je viserais plutôt 1 à 2 ans pour être prêt à travailler, si vous commencez depuis le début.
4. **Regarder une vidéo de cours ou lire un livre ne fera pas automatiquement de vous un expert.** Apprendre le matériel n'est que la première étape. Construire des sites web et des projets réels (même juste des démonstrations pour vous-même) vous aidera à vraiment ancrer votre apprentissage.

Bonne chance alors que vous commencez à apprendre le développement web ! Si vous êtes intéressé par plus, consultez cet article sur mon blog : [Apprendre le développement web en tant que débutant absolu.](https://coder-coder.com/learn-web-development/)

### **Voulez-vous me suivre ?**

Je poste des mini-conseils en développement web sur [Instagram](https://www.instagram.com/thecodercoder/) et [Twitter](https://twitter.com/thecodercoder), et je crée des vidéos de tutoriels de codage sur [YouTube](https://www.youtube.com/thecodercoder) !