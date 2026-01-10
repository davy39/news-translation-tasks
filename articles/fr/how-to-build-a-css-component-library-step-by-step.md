---
title: Comment construire une bibliothèque de composants CSS et améliorer vos compétences
  en développement web
subtitle: ''
author: Prankur Pandey
co_authors: []
series: null
date: '2024-10-11T19:16:44.726Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-css-component-library-step-by-step
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1728400677433/de06f432-0861-4ba4-ad7c-6e10157e2822.jpeg
tags:
- name: CSS
  slug: css
- name: components
  slug: components
- name: Web Development
  slug: web-development
seo_title: Comment construire une bibliothèque de composants CSS et améliorer vos
  compétences en développement web
seo_desc: 'Application development is a complex, multi-stage process, and it all begins
  with UI/UX design.

  Once the design phase is complete, the focus shifts to UI development, where tools
  like HTML, CSS, and JavaScript come into play. At a higher level, libra...'
---

Le développement d'applications est un processus complexe et multi-étapes, et tout commence par la conception UI/UX.

Une fois la phase de conception terminée, l'accent est mis sur le **développement UI**, où des outils comme **HTML**, **CSS** et **JavaScript** entrent en jeu. À un niveau supérieur, des bibliothèques comme **React** et **Vue** simplifient le processus de développement.

Quelle que soit le type d'application, votre code peut presque toujours être décomposé en **composants**.

*Les composants répétés sont un cauchemar à gérer.*  Chaque développeur UI frustré

Imaginez avoir une bibliothèque de composants où tous les éléments couramment utilisés sont pré-construits et réactifsà quel point cela rendrait le développement plus facile et plus rapide ?

Dans cet article, je vais vous montrer comment construire votre propre bibliothèque de composants, en utilisant une pile technologique minimale, puis l'utiliser pour construire une application.

### Ce que nous allons couvrir

1. [Prérequis](#heading-prerequis)
    
2. [Pourquoi construire une bibliothèque de composants](#heading-pourquoi-construire-une-bibliothèque-de-composants) ?
    
3. [Comment construire la bibliothèque de composants](#heading-comment-construire-la-bibliothèque-de-composants)
    
4. [Construisons la bibliothèque](#heading-construisons-la-bibliothèque)
    
    * [Étape 1 : Concevoir la mise en page à l'aide de papier et de stylo](#heading-etape-1-concevoir-la-mise-en-page-à-laide-de-papier-et-de-stylo)
        
    * [Étape 2 : Concevoir les composants en HTML et CSS](#heading-etape-2-concevoir-les-composants-en-html-et-css)
        
    * [Étape 3 : Héberger le fichier CSS du projet](#heading-etape-3-héberger-le-fichier-css-du-projet)
        
5. [FAQ](#heading-faq)
    
6. [Conclusion](#heading-conclusion)
    

## Prérequis

* **Maîtrise de HTML, CSS et JavaScript** : Une compréhension solide des fondamentaux du développement front-end est essentielle.
    
* **Compétences de base en déploiement** : Familiarité avec le déploiement d'applications sur des plateformes comme **Netlify** ou **Vercel** est requise.
    
* **Connaissance de Git/GitHub** : Vous devez être à l'aise avec le contrôle de version, y compris les commandes Git de base et la gestion des dépôts sur GitHub.
    

## Pourquoi construire une bibliothèque de composants ?

Chaque site web est construit à partir de composants, qui sont structurés avec **HTML** et stylisés à l'aide de **CSS**.

**HTML** et **CSS** sont des technologies fondamentales pour créer des pages web visuellement attrayantes. Cependant, les maîtriser peut être difficile en raison de la grande variété de balises HTML et de propriétés CSS.

Pour simplifier le processus, les développeurs utilisent souvent des **bibliothèques de composants**, qui offrent divers avantages :

1. **Développement plus rapide** : Les composants pré-construits et les fonctionnalités de conception réactive accélèrent le processus de développement.
    
2. **Uniformité** : Assure une uniformité de style et une compatibilité multi-navigateurs dans toute l'application.
    
3. **Maintenabilité** : Encourage un code structuré et modulaire, facilitant la maintenance et l'évolutivité.
    
4. **Support communautaire** : Une documentation extensive, des plugins et une communauté forte fournissent des ressources précieuses.
    
5. **Personnalisation et accessibilité** : Offre une personnalisation facile et des composants axés sur l'accessibilité pour des conceptions inclusives.
    

## Comment construire la bibliothèque de composants

La construction d'une bibliothèque de composants implique plusieurs étapes clés. Tout d'abord, je vais vous donner un aperçu de chaque étape que nous allons suivre pour créer la bibliothèque de composants. Ensuite, nous la construirons ensemble.

### 1. Concevoir la mise en page des composants

Avant d'écrire du code, il est crucial d'avoir une vision claire de ce que vous voulez construire. Commencez par esquisser la mise en page de vos composants sur papier, ou utilisez des outils de conception comme **Figma** ou **Canva** pour créer une représentation visuelle.

Avoir un guide visuel simplifiera votre processus de codage et vous aidera à rester concentré lorsque vous traduisez les conceptions en code.

### 2. Écrire la structure des composants en HTML

Une fois la conception prête, l'étape suivante consiste à structurer vos composants en **HTML**. Cela crée la base de votre page web, car HTML est l'épine dorsale de tout projet web.

**Astuce professionnelle** : Utilisez **HTML sémantique** pour améliorer l'accessibilité des utilisateurs et le référencement. Par exemple, utilisez les balises `<article>`, `<section>`, ou `<header>` au lieu d'éléments `<div>` génériques lorsque cela est approprié.

### 3. Styliser les composants avec CSS

Avec la structure HTML en place, vous pouvez commencer à styliser les composants à l'aide de **CSS**. Appliquez des styles comme les **couleurs de fond**, les **tailles de police**, les **décorations de liens** et les **styles de boutons** en utilisant des **classes CSS** et des **ID**.

CSS est un outil puissantvous pouvez même ajouter de belles animations. Mais dans ce tutoriel, nous nous concentrerons sur l'utilisation des propriétés essentielles de CSS pour créer des conceptions propres et fonctionnelles.

### 4. Héberger le fichier CSS du projet

Une fois votre bibliothèque de composants prête, vous voudrez la rendre accessible pour les projets futurs. Héberger votre **fichier CSS** sur des plateformes comme **Netlify**, **GitHub Pages**, ou **Vercel** vous permet d'utiliser les composants dans différents projets en liant simplement le fichier CSS global.

En suivant ces quatre étapes, vous créerez une bibliothèque de composants réutilisables qui vous aidera à construire de beaux sites web de manière efficace et efficace.

## Construisons la bibliothèque

J'ai commencé mon parcours en tant que développeur logiciel en plongeant dans **HTML** et **CSS** pour concevoir des pages web. Ces technologies fondamentales sont essentielles pour tout développeur web, mais les maîtriser peut être difficileHTML compte 152 balises, tandis que CSS a plus de 200 propriétés.

Bien que vous n'ayez pas besoin d'utiliser chaque balise HTML ou propriété CSS, la connaissance des concepts de base nécessite un temps et un effort significatifs.

Maintenant, imaginons un scénario : si je vous demandais de créer un petit site web ou une page de destination sans utiliser de bibliothèque de composants, comment vous y prendriez-vous ? Mon objectif est de minimiser le temps passé sur la conception.

Imaginez s'il existait un moyen d'automatiser le processus de conception, vous permettant d'obtenir de beaux résultats sans sacrifier la flexibilité. C'est là qu'intervient une **bibliothèque de composants**. En écrivant vos composants en CSS vanilla pur une fois, vous pouvez les réutiliser dans n'importe quel projet.

Je vous encourage à poursuivre cette approche car elle vous fournira une expérience en temps réel avec HTML et CSS tout en vous aidant à apprendre une multitude de concepts simultanément.

J'ai développé une petite bibliothèque composée de 10+ beaux composants, que vous pouvez explorer ici : [**SlateUi**](#). Cette bibliothèque m'a aidé à approfondir ma compréhension des technologies web.

Mon objectif était de comprendre HTML et CSS en profondeur. Après avoir terminé un projet, je voulais me sentir confiant dans tous les aspects critiques de la conception web, de l'UI au code.

En concevant et en développant ces composants, j'ai gagné un plus grand contrôle et des options de personnalisation adaptées à des exigences spécifiques.

Le processus d'apprentissage a également été incroyablement gratifiant. La création de chaque composant a pris un temps considérable, mais l'exposition que j'ai acquise à ces deux technologies a considérablement renforcé ma confiance.

De plus, cette approche aide à éviter la redondance de l'écriture de code CSS répétitif pour des éléments similaires.

### Étape 1 : Concevoir la mise en page à l'aide de papier et de stylo

Tout d'abord, vous voudrez créer une mise en page de base pour la page web. Ce n'est qu'une esquisse initiale pour que vous sachiez ce que vous devez construire dans votre projet.

La mise en page se compose de trois éléments clés :

a) **En-tête**  
b) **Carte(s)**  
c) **Pied de page**

Chaque composant comprend des couleurs distinctes, du texte et des éléments supplémentaires. Voici à quoi cela ressemble dans notre exemple :

[![Illustration des principaux composants de la mise en page : en-tête, carte, pied de page](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fzrcqxm4mrnyx778sedui.png align="left")](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fzrcqxm4mrnyx778sedui.png)

Dans un projet réel, vous commencez généralement avec des modèles de conception préparés créés dans des outils comme **Figma** ou d'autres logiciels de conception UI.

Pour ce projet, j'ai utilisé **Canva** pour concevoir la mise en page. Cette phase de conception initiale est cruciale car elle pose les bases du développement des fonctionnalités principales.

Ensuite, vous écrivrez la structure du composant en HTML. À ce niveau, je vais simplement placer nos éléments HTML de manière à préparer un squelette de base de la page web tel que nous l'avons conçu. Dans l'en-tête, j'ai un logo et quelques liens de navigation, dans les cartes j'ai un bouton et une image ; et dans le pied de page, j'ai quelques liens supplémentaires.

### Étape 2 : Concevoir les composants en HTML et CSS

À ce stade, nous allons améliorer les composants que nous avons créés avec HTML en appliquant des propriétés CSS pour les embellir. Cette étape implique l'utilisation de CSS pour définir les couleurs de fond, les couleurs principales, les décorations de liens, les styles de boutons, et plus encore. Nous allons faire cela en utilisant des classes et des ID CSS.

Jusqu'à présent, nous avons construit trois composants :

a) **En-tête** avec des liens de navigation  
b) **Pied de page**  
c) **Cartes horizontales** avec des boutons d'action

Maintenant, commençons par construire le premier composant : l'**En-tête**.

#### Le composant d'en-tête :

L'en-tête se trouve en haut d'une page ou d'une section. Il contient généralement un logo, une barre de recherche, des liens de navigation, etc.

<iframe height="300" style="width:100%" src="https://codepen.io/iprankurpandey/embed/eYVzNPR?default-tab=html">
  See the Pen <a href="https://codepen.io/iprankurpandey/pen/eYVzNPR">
  Header</a> by PRANKUR PANDEY (<a href="https://codepen.io/iprankurpandey">@iprankurpandey</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

#### Le composant de pied de page :

Le pied de page définit le bas d'une page web ou d'une section. Habituellement, il contient des informations de copyright, des détails de contact, des liens de navigation, etc.

<iframe height="300" style="width:100%" src="https://codepen.io/iprankurpandey/embed/poabJqN?default-tab=html">
  See the Pen <a href="https://codepen.io/iprankurpandey/pen/poabJqN">
  Footer</a> by PRANKUR PANDEY (<a href="https://codepen.io/iprankurpandey">@iprankurpandey</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

#### Le composant de carte :

Le **composant de carte** peut contenir divers types de contenu, y compris un titre, une image, un contenu principal et un pied de page qui présente un bouton d'appel à l'action.

Les cartes sont conçues pour servir des objectifs spécifiques, tels que la présentation de produits de commerce électronique, l'affichage d'articles d'actualité, ou servant de multiples autres fonctions dans différents contextes.

<iframe height="300" style="width:100%" src="https://codepen.io/iprankurpandey/embed/KKQMpvd?default-tab=html">
  See the Pen <a href="https://codepen.io/iprankurpandey/pen/KKQMpvd">
  Horizontal-Cards</a> by PRANKUR PANDEY (<a href="https://codepen.io/iprankurpandey">@iprankurpandey</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

#### Combiner le tout :

<iframe height="300" style="width:100%" src="https://codepen.io/iprankurpandey/embed/NWyrjGm?default-tab=html">
  See the Pen <a href="https://codepen.io/iprankurpandey/pen/NWyrjGm">
  Demo-API</a> by PRANKUR PANDEY (<a href="https://codepen.io/iprankurpandey">@iprankurpandey</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

En cliquant sur le bouton, les données de la carte seront mises à jour avec des faits aléatoires sur les chats, ainsi que la longueur de chaque fait.

**Note** : J'ai utilisé une API open-source pour ce projet. Si le contenu ne se met pas à jour sur la carte, cela peut être dû à une panne de l'API.

Maintenant, avez-vous vérifié le code CSS ?

Vous vous demandez peut-être pourquoi j'ai importé une seule ligne de code dans mon fichier CSS. Eh bien, j'ai combiné les fichiers CSS des trois parties de la mise en page (**en-tête, pied de page et cartes**) en un seul fichier CSS et hébergé le fichier sur Netlify. Voici l'URL qui contient les trois fichiers CSS :

`@import url("https://hashnodeblogchallenge.netlify.app/index.css");`

Il sert le CSS dans les trois composants et maintient les styles pour les trois composants.

### Étape 3 : Héberger le fichier CSS du projet

Enfin, je suis arrivé à la partie la plus cruciale de ce projet, où toute la magie opère.

Actuellement, j'ai trois fichiers CSS pour chacun des composants web : **en-tête**, **cartes** et **pied de page**.

Étant donné que notre projet est petit, je vais combiner tout le code des fichiers CSS en un seul fichier CSS pour obtenir un fichier CSS universel.

Le processus d'hébergement du fichier CSS est simple. Voici une décomposition détaillée de ce que vous devez faire :

#### 1. **Poussez votre code vers GitHub**

Vous devez pousser (télécharger) vos fichiers de projet, y compris le HTML, le CSS et d'autres actifs, vers un dépôt GitHub. Voici comment vous pouvez faire cela :

1. Initialisez un dépôt Git dans votre répertoire de projet en utilisant `git init`.
    
2. Ajoutez tous vos fichiers en utilisant `git add .`.
    
3. Validez les fichiers avec `git commit -m "Initial commit"`.
    
4. Liez à un dépôt GitHub que vous avez créé en utilisant `git remote add origin <repo-url>`.
    
5. Enfin, poussez votre code en utilisant `git push -u origin main`.
    
6. **Résultat** : Vos fichiers de projet seront maintenant hébergés dans votre dépôt GitHub.
    

#### 2. **Ouvrez Netlify et connectez-vous ou inscrivez-vous**

Ensuite, visitez [Netlify](https://www.netlify.com) et connectez-vous si vous avez déjà un compte ou créez-en un nouveau.

Vous pouvez vous inscrire en utilisant vos identifiants GitHub ou un email séparé. Cette étape vous donne accès aux services d'hébergement web de Netlify, qui vous permettront de déployer votre projet directement depuis GitHub.

#### 3. **Connectez votre dépôt GitHub contenant votre code**

Une fois connecté, vous allez connecter votre dépôt GitHub à Netlify.

1. Sur Netlify, cliquez sur "New site from Git".
    
2. Choisissez **GitHub** comme source.
    
3. Autorisez Netlify à accéder à votre compte GitHub.
    
4. Sélectionnez le dépôt contenant votre projet dans la liste.
    
5. Configurez les paramètres de construction si nécessaire (bien que pour les sites statiques simples, Netlify les détecte automatiquement).
    

#### 4. **Cliquez sur "Deploy"**

Après avoir connecté votre dépôt, Netlify affichera un bouton "Deploy".

1. Cliquez sur "Deploy" pour déclencher le processus de construction et de déploiement.
    
2. Netlify tirera votre code depuis GitHub, construira le site (si nécessaire) et le déployera sur une URL en direct.
    

Votre projet est maintenant en ligne sur le web, et vous recevrez une URL où vous pourrez accéder au site déployé.

#### 5. **Accédez à l'URL déployée et ajoutez l'URL du fichier CSS**

Vous accéderez au site déployé en visitant l'URL fournie par Netlify et en référençant directement le fichier CSS que vous avez téléchargé.

1. Une fois votre site déployé, notez l'URL fournie (par exemple, [`https://example.netlify.app`](https://example.netlify.app)).
    
2. Pour accéder à un fichier CSS spécifique, ajoutez le nom du fichier à l'URL, par exemple : [`https://example.netlify.app/styles.css`](https://example.netlify.app/styles.css).
    
3. Ici, `styles.css` est le nom de votre fichier CSS que vous avez téléchargé sur GitHub et déployé via Netlify.
    

Cela vous permettra de visualiser ou de référencer le fichier CSS directement via une URL publique.

Ce processus vous aide essentiellement à héberger votre projet et ses actifs sur Netlify, permettant un accès facile à tout fichier (comme `filename.css`) que vous avez téléchargé sur GitHub. Vous pouvez utiliser ces liens publics dans vos projets ou les partager.

**Et c'est tout ! Liez cette URL au fichier CSS de votre projet.**

J'ai hébergé le fichier CSS principal sur l'application Netlify afin qu'il puisse être accessible n'importe où simplement en l'important dans votre projet. Voici l'URL de mon fichier CSS hébergé : `https://hashnodeblogchallenge.netlify.app/index.css`.

La beauté des bibliothèques de composants est qu'elles vous permettent de vous concentrer sur le développement plutôt que sur la conception.

## FAQ

### Quels avantages avons-nous tirés de cela ?

Maintenant, vous devez simplement copier le code HTML et importer le fichier CSS dans votre projet. Voici les principaux avantages :

* **Réduit le temps** passé sur le codage CSS répétitif.
    
* Offre un **meilleur contrôle** sur les composants, permettant une personnalisation basée sur vos besoins.
    
* Fournit une **expérience en temps réel** avec HTML et CSS, vous permettant d'apprendre les concepts de base efficacement.
    

### Que faire si je veux changer quelque chose ?

C'est simple. Il suffit de modifier votre fichier CSS et de mettre à jour la couleur de l'en-tête de noir à bleu où vous avez déclaré cette classe ou cet ID d'en-tête.

### Que faire si je veux créer plus de composants ?

Vous pouvez créer autant de composants que vous le souhaitez ! Il suffit de stocker le code de style dans le même fichier CSS hébergé, et tout fonctionnera de manière transparente.

### Comment cela me fait-il gagner du temps ?

Imaginez que vous devez créer 5 sites web, chacun avec 5 pages (soit un total de 25 pages). Si vous identifiez des éléments communs, tels que des en-têtes et des pieds de page, qui seront utilisés sur les 25 pages, vous pouvez éviter d'écrire 25 composants séparés. Au lieu de cela, vous pouvez simplement utiliser les composants de votre bibliothèqueil suffit de copier et coller le HTML et d'ajouter le fichier CSS.

### Qu'est-ce qui permet à l'ensemble de l'application de fonctionner avec une seule ligne de CSS ?

Le concept est assez simple et peut être décomposé en les étapes suivantes :

1. **Créer des composants** en fonction de vos exigences.
    
2. **Contrôler leur conception** avec CSS et appliquer les propriétés nécessaires.
    
3. **Héberger votre fichier CSS principal** quelque part pour obtenir une nouvelle URL, que vous pouvez utiliser pour importer vos styles CSS en HTML.
    

**Maintenant, vous pouvez calculer combien de temps vous avez économisé.**

## Conclusion

Créer une bibliothèque de composants en utilisant **HTML** et **CSS** vous permet de construire de belles pages web rapidement et efficacement.

Cela vous donne également une compréhension approfondie de HTML et CSS, qui sont des compétences essentielles pour une carrière réussie en développement logiciel. Avec ces compétences, vous serez en mesure de créer des mises en page engageantes sans passer un temps excessif à coder à partir de zéro.

Pour vous aider à commencer, voici un exemple de bibliothèque de composants que j'ai développée, qui comprend 10+ beaux composants : [SlateUI](https://slateui.netlify.app).

Maintenant, vous devez simplement copier le code HTML et le coller où vous voulez afficher vos composants, ainsi qu'importer l'URL de votre fichier CSS dans ce fichier HTML.

Alors, c'est la fin de mon côté. Si vous trouvez cet article utile, alors partagez-le et connectez-vous avec moi  je suis ouvert aux opportunités :

* Suivez-moi sur X : [Twitter de Prankur](https://x.com/prankurpandeyy)
    
* Suivez-moi sur LinkedIn : [LinkedIn de Prankur](https://linkedin.com/in/prankurpandeyy)
    
* Consultez mon portfolio ici : [Portfolio de Prankur](https://prankurpandeyy.netlify.app/)