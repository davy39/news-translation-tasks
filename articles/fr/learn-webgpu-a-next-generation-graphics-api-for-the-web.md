---
title: Apprendre WebGPU – Une API graphique de nouvelle génération pour le web
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2022-03-17T21:33:19.000Z'
originalURL: https://freecodecamp.org/news/learn-webgpu-a-next-generation-graphics-api-for-the-web
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/webgpu.png
tags:
- name: webgpu
  slug: webgpu
- name: youtube
  slug: youtube
seo_title: Apprendre WebGPU – Une API graphique de nouvelle génération pour le web
seo_desc: 'WebGPU is the next-generation graphics API and future web standard for
  graphics and compute, aiming to provide modern 3D graphics and computation capabilities
  with the GPU acceleration.

  We just published a WebGPU course on the freeCodeCmap.org YouTub...'
---

WebGPU est l'API graphique de nouvelle génération et le futur standard web pour les graphismes et le calcul, visant à fournir des capacités modernes de graphismes 3D et de calcul avec l'accélération GPU.

Nous venons de publier un cours WebGPU sur la chaîne YouTube de freeCodeCamp.org.

Le Dr Jack Xu a développé ce cours. Le Dr Xu a plus de 25 ans d'expérience en programmation et a publié plusieurs livres sur WebGPU.

Dans ce cours, vous apprendrez les bases de WebGPU en construisant 10 projets WebGPU. Vous apprendrez comment créer chaque projet à partir de zéro et comment ajouter des graphismes 3D à vos applications web.

![sinc](https://github.com/jack1232/WebGPU-Step-By-Step/raw/main/assets/sinc.png)
_Surface Sinc 3D créée avec WebGPU_

À la fin de ce cours, vous comprendrez comment créer des graphismes 3D avancés en utilisant le calcul GPU sur le web avec l'API WebGPU. Voici les sections couvertes dans ce cours :

* Environnement de développement
* Créer un triangle coloré
* Créer un carré avec un tampon GPU (GPU Buffer)
* Cube avec des couleurs de face distinctes
* Animation et contrôle de la caméra
* Modèle de lumière
* Cube avec effets d'éclairage
* Carte de couleurs (Colormap)
* Surfaces 3D simples
* Surface Sinc 3D

Regardez le cours complet ci-dessous ou sur la chaîne YouTube de freeCodeCamp.org (2 heures de visionnage).

%[https://www.youtube.com/watch?v=KTFFdZSDiTU]

### Transcription

(générée automatiquement)

Le Dr Jack Xu est l'auteur de nombreux livres sur WebGPU. Dans ce cours, il vous enseignera les bases de WebGPU.

Bonjour, je suis Jack. Dans cette vidéo, vous apprendrez les bases de la programmation graphique WebGPU en construisant dix projets WebGPU distincts.

Chaque projet sera créé sur la base du précédent, des primitives simples aux graphismes 3D compliqués. Notre produit final sera une magnifique surface Sinc 3D, comme illustré ici.

Nous créerons ces projets WebGPU à partir de zéro et nous vous montrerons comment ajouter des graphismes 3D avec accélération GPU à vos applications web.

Ici, je tiens à remercier Beau et freeCodeCamp pour la publication de cette vidéo. freeCodeCamp est une excellente ressource pour la communauté de la programmation. Et merci pour tout ce que vous faites.

Avant d'entrer dans cette vidéo, j'aimerais vous parler rapidement de mon parcours. J'ai obtenu mon doctorat en physique théorique et j'ai plus de 25 ans d'expérience en programmation en C, C++, C# .NET et en développement web.

J'ai publié plus de 20 livres sur la programmation pratique sur divers sujets, notamment la programmation graphique, l'apprentissage automatique (machine learning), la finance quantitative, les méthodes de calcul numérique et les applications web.

Récemment, j'ai créé une chaîne YouTube : "Practical Programming" basée sur mes livres.

Sur cette chaîne, je présenterai plusieurs séries de vidéos étape par étape, dans lesquelles je mettrai l'accent sur l'utilité du code d'exemple pour les applications du monde réel.

La première série de vidéos concerne la programmation graphique WebGPU, basée sur mon livre récemment publié, "Practical WebGPU Graphics".

Les projets présentés ici sont également sélectionnés à partir de ce livre.

Ma chaîne : "Practical Programming with Dr. Xu" est nouvelle et je prévois de la mettre à jour chaque semaine.

J'apprécierais grandement que vous puissiez jeter un œil à ma chaîne et vous y abonner.

Passons maintenant à la programmation graphique WebGPU.

Commençons le projet un qui consistera à configurer un environnement de développement.

Le code source utilisé dans ce projet peut être téléchargé à partir du lien GitHub ici. Ce projet utilise cette version spécifique.

Alors, qu'est-ce que WebGPU ? WebGPU est l'API graphique de nouvelle génération.

C'est le futur standard web pour les graphismes et le calcul. WebGPU fournira des capacités modernes de graphismes 3D et de calcul avec accélération GPU.

Dans cette vidéo, nous utiliserons les outils de développement suivants pour construire nos applications WebGPU.

Tout d'abord, Visual Studio Code, Node.js.

Nous utilisons TypeScript comme langage de programmation, et nous utiliserons Webpack comme bundler modulaire.

Pour exécuter des applications WebGPU, nous avons actuellement trois options.

La première consiste à utiliser Chrome Canary pour tester nos applications WebGPU.

L'autre option consiste à exécuter des applications WebGPU sur un Chrome standard via un Origin Trial.

À partir de Chrome 94, WebGPU est disponible en tant qu'Origin Trial dans le Chrome standard.

Vous devrez vous inscrire aux Origin Trials et demander un jeton (token) pour votre origine.

La troisième option est que Chrome supportera officiellement WebGPU en mai de cette année.

Ainsi, après ce mois de mai, vous pourrez exécuter vos applications WebGPU sur le Chrome standard.

Dans cette série de vidéos, j'utiliserai Chrome Canary pour tester nos projets WebGPU.

Ici, je suppose que vous avez déjà installé Visual Studio Code, Node.js, et que vous avez également installé TypeScript globalement sur votre machine.

Commençons à programmer.

Ouvrons maintenant une fenêtre d'invite de commande et créons un dossier : `mkdir gpuapp` et entrons dedans avec `cd`.

Ensuite, nous allons exécuter cette commande : `npm init -y` pour créer un fichier `package.json`.

D'accord, ce fichier stockera nos dépendances utilisées dans ce projet.

Maintenant, nous allons installer Webpack et son interface en ligne de commande en utilisant cette commande : `npm install webpack webpack-cli`.

Webpack est un bundler modulaire qui regroupe les fichiers pertinents pour générer des actifs statiques pouvant être utilisés par les applications web.

Ici, nous utilisons Webpack principalement pour la transpilation des fichiers TypeScript, mais nous ne l'utilisons pas ici pour regrouper d'autres types de fichiers, tels que les fichiers HTML et les images.

Maintenant, l'installation est terminée.

À ce stade, nous allons lancer Visual Studio Code avec la commande : `code .`.

Voici l'interface de Visual Studio Code, vous pouvez voir que nous n'avons qu'un fichier `package.json`, mais il ne se passe pas grand-chose ici.

Ouvrez maintenant une fenêtre de terminal en appuyant sur la touche Ctrl+J.

Maintenant, installons quelques packages de dépendances.

Tout d'abord, nous allons installer jQuery et le package de types correspondant.

`npm install jquery`.

Nous utiliserons jQuery pour manipuler les éléments du DOM dans nos applications.

Ensuite, nous voulons installer les loaders CSS et TS.

Au cas où notre projet contiendrait un fichier de feuille de style, nous devons utiliser `style-loader` et `css-loader` pour le regrouper.

Afin de créer des modules TypeScript dans notre projet, nous devons également installer TypeScript localement.

`npm install typescript` localement.

Nous l'avions déjà installé globalement auparavant.

Maintenant, ouvrons le fichier `package.json`.

Vous pouvez voir que la section `scripts` ici ne contient que l'attribut `test`, ce qui n'est pas très utile.

Ici, nous allons remplacer cette section par le code approprié.

Ici, le code vous permet d'exécuter Webpack dans différents modes comme le développement, la production et le mode watch.

Maintenant, nous pouvons enregistrer ce fichier et le fermer.

Maintenant, tous les packages installés vont être stockés dans le dossier `node_modules`.

Ici, le fichier `package-lock.json` est automatiquement généré pour toutes les opérations npm.

Nous n'avons donc rien à faire avec.

L'étape suivante consiste à initialiser le fichier TypeScript avec la commande `tsc --init`.

Cette opération a créé un fichier de configuration pour TypeScript appelé `tsconfig.json` ici.

Maintenant, nous ouvrons ce fichier de configuration et nous devons remplacer son contenu. Vous pouvez voir ici que nous avons défini la cible sur `es6`. Notez également que nous définissons le répertoire racine comme `src` et le répertoire de sortie comme `dist`, le dossier de distribution.

Maintenant, enregistrez ce fichier et fermez-le.

Nous créons ensuite des structures de dossiers pour notre projet.

Tout d'abord, créons le dossier `src`.

Nous créons donc ici un dossier appelé `src`.

Nous stockerons tous les fichiers sources dans ce dossier.

Ensuite, nous créons un dossier `dist`, qui contiendra tous les fichiers qui seront téléchargés sur le serveur web pour exécuter nos applications.

Dans ce dossier, il y a au moins un fichier HTML.

Ajoutons un fichier `index.html` à ce dossier.

Ajoutez un autre fichier `index.html`, et ajoutez-y du code.

Vous pouvez voir ici que nous ajoutons le titre "WebGPU project".

Ici, le titre `h1` vérifie si votre navigateur supporte WebGPU ou non.

Nous avons également des éléments DOM `h2` ici et nous définissons son ID égal à `id_gpu_check`.

Cet élément `h2` sera utilisé pour afficher la chaîne de texte qui sera renvoyée par une fonction TypeScript qui sera créée plus tard.

Nous sommes sur le point de terminer la configuration de l'environnement de développement, mais nous avons manqué une étape clé, à savoir que nous devons installer le package WebGPU.

Le groupe de travail WebGPU a créé une définition de type pour le standard WebGPU.

Ce package correspond à l'API WebGPU en cours d'élaboration, qui n'est actuellement pas très stable.

Elle peut donc changer presque chaque semaine.

Soyez donc prudent en l'utilisant.

Quoi qu'il en soit, installons-le avec cette commande.

Ici, nous spécifions la version 0.1.12, c'est la version la plus récente, nous l'installons sous le nom `@webgpu/types`.

Comme WebGPU n'est pas rétrocompatible, il est préférable d'utiliser la même version pour exécuter notre projet.

Sinon, vous devrez apporter des modifications à votre code pour exécuter l'application.

Je vous suggère donc d'utiliser la même version ici, 0.1.12.

Après l'installation, nous devons le configurer.

Ouvrez le fichier de configuration TypeScript.

Vous pouvez voir ici que nous l'avons déjà configuré.

Nous ajoutons les types WebGPU et Node dans la section `types`. Vous pouvez voir ici que nous avons le type Node.

Nous devons donc l'installer en utilisant cette commande pour installer ce type Node.

D'accord, WebGPU est maintenant disponible pour notre projet.

Ajoutons maintenant un fichier TypeScript à notre projet.

Tout d'abord, ajoutez un nouveau fichier appelé `helper.ts` au dossier `src`.

Nous avons donc ajouté un nouveau fichier appelé `helper.ts` et y avons ajouté du code.

Vous pouvez voir ici que nous utilisons cette variable `navigator.gpu` pour vérifier la disponibilité du GPU.

Cette variable est définie dans l'API WebGPU.

Vous pouvez voir ici que nous utilisons la flèche (fat arrow) pour définir la fonction TypeScript.

Ensuite, nous devons créer un fichier de point d'entrée appelé `main.ts`.

D'accord, enregistrez d'abord ce fichier.

Et fermez-le.

Ajoutons un autre nouveau fichier au dossier `src` appelé `main.ts`.

Maintenant, ajoutez du code à ce fichier, nous importons simplement jQuery et importons également la fonction `checkWebGPU` du fichier `helper.ts` que nous venons d'implémenter.

Ici, nous définissons `id_gpu_check` pour afficher la chaîne renvoyée par la fonction `checkWebGPU`.

Ici, l'ID représente l'élément DOM `h2` défini dans le fichier `index.html`, assurez-vous que cet ID est le même que l'ID défini dans ce fichier.

Ensuite, nous devons également créer un fichier de configuration Webpack.

Ajoutez maintenant un nouveau fichier au répertoire racine `webpack.config.js`.

Vous pouvez voir ici que nous définissons un répertoire de sortie de bundle comme `dist` et un point d'entrée nommé `main` ici.

Le fichier `main`, `src/main.ts`.

Notez que le fichier de sortie a toujours l'extension `.bundle.js`.

Maintenant, nous pouvons enregistrer ce fichier et le fermer.

Maintenant, nous pouvons exécuter la commande suivante depuis la fenêtre du terminal pour regrouper notre fichier TypeScript : `npm run prod` en mode production. D'accord, c'est fini.

Vous pouvez vérifier le fichier bundle dans le dossier `dist`.

Vous pouvez voir ici que nous avons plusieurs fichiers `main.bundle.js`.

C'est notre fichier bundle, ceci est le fichier de licence, ceci est le fichier source map.

Ce fichier `main.bundle.js` a été référencé dans le fichier `index.html`.

Vous pouvez voir ici, c'est le `main.bundle.js`. Ce fichier bundle est généré par Webpack.

Afin de tester notre application, nous avons également besoin d'un serveur.

Ici, nous utiliserons l'extension Live Server.

Cliquez sur le lien des extensions et recherchez "Live Server".

Le premier est Live Server.

Ici, je l'ai déjà installé.

Sinon, nous avons un lien d'installation ici.

Si vous ne l'avez pas installé, cliquez simplement sur le bouton d'installation pour installer Live Server.

Je suppose donc que vous l'avez déjà installé.

Maintenant, nous pouvons ouvrir le fichier `index.html`, faire un clic droit n'importe où et choisir "Open with Live Server", cliquez sur ce lien.

Cela ouvrira notre navigateur par défaut pour afficher la page web.

Malheureusement, si votre navigateur par défaut est le Chrome standard, il affichera le message : "votre navigateur actuel ne supporte pas WebGPU".

Afin d'exécuter des applications WebGPU ici, nous allons installer Chrome Canary.

Recherchez donc Chrome Canary.

Cliquez dessus.

C'est la version nocturne (nightly build) pour les développeurs.

Téléchargez simplement Chrome Canary et installez-le.

J'ai déjà installé ce Chrome Canary sur ma machine.

N'oubliez pas l'emplacement où votre Chrome Canary est installé.

D'accord, je suppose que vous l'avez déjà installé.

Revenons à Visual Studio Code.

Nous voulons changer le navigateur par défaut pour Chrome Canary, ce qui facilitera le test de nos applications WebGPU.

Appuyez donc sur Ctrl+Shift+P et tapez "Preferences: Open Settings (JSON)" ici.

Ouvrez ce fichier.

Ici, vous devez ajouter ces trois lignes.

Le paramètre Live Server pour ne pas afficher de message d'information.

Je l'ai réglé sur `true`, cela n'a pas d'importance.

J'ai également défini le répertoire racine comme `dist` car notre fichier `index.html` se trouve dans ce répertoire.

Voici la ligne de commande du navigateur personnalisé qui définit le navigateur par défaut.

Vous devez donc remplacer ce code.

Vous devez copier l'emplacement de votre fichier `.exe` de Chrome Canary et le coller ici, vous devez le modifier pour qu'il corresponde à votre situation.

Maintenant, nous pouvons enregistrer ce fichier et le fermer.

Lancez maintenant Chrome Canary et tapez `chrome://flags` et recherchez "WebGPU".

Ici, activez-le, je l'ai déjà activé.

Si ce n'est pas le cas, vous devez simplement l'activer pour rendre WebGPU disponible pour notre Chrome Canary.

D'accord, nous pouvons le fermer.

Enfin, nous pouvons tester notre environnement de développement pour les applications WebGPU.

Ici, nous avons un lien dans la zone de la barre d'état, vous pouvez voir le lien "Go Live".

Cette fois, il lancera le navigateur Chrome Canary.

Cliquez sur ce lien.

Vous pouvez voir "Génial, votre navigateur actuel supporte WebGPU". Félicitations, nous avons configuré avec succès l'environnement de développement pour les applications WebGPU.

Nous avons maintenant terminé notre premier projet WebGPU qui montre comment configurer l'environnement de développement.

C'est le projet 2 de cette série de vidéos.

Ici, j'expliquerai comment créer un triangle coloré dans WebGPU comme illustré ici.

C'est un triangle coloré.

Ce projet est basé sur notre premier projet.

Vous pouvez ouvrir le projet un directement depuis Visual Studio Code ou cloner le code source depuis le dépôt GitHub.

`git clone`.

C'est le lien GitHub pour le code source du projet un.

J'ai également mis le code source de ce projet 2 dans le dépôt GitHub.

Voici le lien.

Vous pouvez donc télécharger le code source utilisé dans ce projet à partir de ce lien.

Maintenant, nous allons ouvrir le projet un directement depuis Visual Studio Code.

Ici, nous ajoutons d'abord un fichier CSS appelé `site.css` au dossier `src`, dossier `src`, ajoutez un nouveau fichier appelé `site.css`.

Tapez du code dans ce fichier, puis enregistrez et fermez-le.

Tout comme pour WebGL, la première chose que nous devons faire pour utiliser WebGPU pour le rendu graphique est de créer un élément canvas.

Depuis le dossier `dist`, ouvrez le fichier `index.html`.

Ici, nous devons changer les éléments `h2` à partir d'ici.

Ici, nous définissons l'élément canvas avec l'ID `canvas-webgpu`.

Plus tard, nous créerons des graphismes WebGPU sur ce canvas.

La programmation WebGPU se compose de deux parties : l'une est le code de contrôle écrit en TypeScript ou JavaScript, et l'autre partie est le code du shader exécuté sur le GPU.

Ici, nous utiliserons le langage de shader officiel pour WebGPU appelé WGSL, qui est l'abréviation de WebGPU Shading Language.

Pour profiter de la coloration syntaxique dans VS Code, nous convertirons le code du shader avec l'extension `.wgsl` en un module de type TypeScript.

Pour ce faire, nous devons installer un shader loader pour Webpack.

Ouvrez maintenant une nouvelle fenêtre de terminal.

Exécutez la commande suivante pour installer le shader loader appelé `npm install ts-shader-loader`. Ce loader a été créé à l'origine pour charger du code de shader GLSL.

Mais nous allons le faire fonctionner pour WGSL ici.

Ensuite, ouvrez le fichier de configuration Webpack et ajoutez-y le code suivant.

Ici, les fichiers avec `.wgsl`, `.glsl`, `.vs` (vertex shader), `.fs` (fragment shader).

Ainsi, les fichiers avec ces extensions seront traités comme du code de shader par ce shader loader.

Nous devons ensuite installer l'extension WGSL depuis VS Code.

Cliquez sur ce lien d'extension, recherchez "WGSL".

Voici la première : WGSL fournit la coloration syntaxique. J'ai déjà installé ce module.

Vous pouvez donc voir ici la coloration syntaxique du code.

Dans ce cas, il est facile d'écrire du code de shader en utilisant cette extension.

Si vous ne l'avez pas installée, cliquez sur ce bouton d'installation pour l'installer.

Ensuite, nous devons ajouter quelques déclarations de type pour notre shader.

Ajoutez un nouveau sous-dossier au dossier `src`.

Un nouveau dossier appelé `types`.

Ensuite, ajoutez un nouveau fichier appelé `shader.d.ts`.

À l'intérieur de ce fichier, nous ajoutons du contenu.

Ici, nous déclarons le module.

Les fichiers avec `.wgsl`, `.glsl`, `.vs` ou `.fs`, nous déclarons ces fichiers comme modules.

Maintenant, nous pouvons enregistrer ce fichier et le fermer.

Maintenant, nous pouvons écrire notre code de shader.

Dans le dossier `src`, ajoutez un nouveau fichier appelé `shader.wgsl`.

Ensuite, ajoutez du code. À partir de ce code, vous pouvez voir qu'il y a deux shaders ici.

L'un est le vertex shader (shader de sommets) et l'autre est le fragment shader (shader de fragments).

Nous avons une fonction de shader pour le vertex appelée fonction `vs_main`.

`vs` signifie fonction de vertex shader.

Ici, nous avons `fs_main` : fonction principale du fragment shader.

Le vertex shader prend les données des sommets, y compris la position dans le monde, la couleur et la texture comme entrée ; la sortie est la position dans les coordonnées de découpe (clip coordinates).

Tandis que les autres sorties telles que la couleur et la texture seront transmises au fragment shader.

Ces valeurs seront ensuite interpolées sur les fragments pour produire un dégradé de couleurs fluide.

Revenons maintenant à notre exemple.

Dans le vertex shader, nous définissons d'abord la structure de sortie ici, qui contient la position intégrée et la couleur de sortie appelée `vColor`.

À l'intérieur de la fonction `vs_main`, nous définissons d'abord trois sommets de notre triangle en utilisant le vecteur à virgule flottante `vec2`.

Nous avons donc trois sommets.

Nous spécifions également des couleurs pour chaque sommet en utilisant un vecteur à virgule flottante `vec3`.

Vous pouvez voir que la première est `1 0 0`.

Cela signifie rouge.

La deuxième couleur est `0, 1, 0` le vert, la dernière est `0, 0, 1`, qui est un bleu.

Nous définissons donc une couleur différente pour chaque sommet.

Ensuite, nous définissons la sortie en utilisant la structure de sortie ici, puis nous convertissons le vecteur 2D de la position en un `vec4`, le vecteur à quatre dimensions, nous mettons une composante Z à zéro et une composante W à un.

De même, nous convertissons le vecteur 3D pour la couleur en `vec4` ici.

Le un représente la transparence de la couleur. Dans le fragment shader, nous prenons la couleur de sortie du vertex shader comme entrée et la renvoyons comme couleur de fragment.

D'accord, c'est le shader que nous utiliserons lors de la création de notre triangle coloré dans WebGPU.

Maintenant, nous pouvons enregistrer ce fichier et le fermer.

Ensuite, nous utiliserons TypeScript pour écrire le code de contrôle WebGPU.

Ouvrez le fichier `main.ts`.

Et remplacez son contenu par le nouveau code suivant.

Ici, nous introduisons d'abord la fonction `checkWebGPU` du fichier `helper.ts`.

Ensuite, à partir du fichier `shader.wgsl`, nous introduisons notre shader. À partir de ce fichier, nous importons également le fichier `site.css`.

Ici, nous l'utiliserons pour configurer la mise en page de notre page web.

Ensuite, nous créons une nouvelle fonction appelée `CreateTriangle`.

Cette fonction doit être `async`, vous pouvez voir `async function` car l'API WebGPU elle-même est asynchrone.

À l'intérieur de cette fonction, nous vérifions d'abord si votre navigateur supporte WebGPU ou non.

Dans WebGPU, nous pouvons accéder au GPU en appelant `requestAdapter` ici.

Une fois que nous avons cet adaptateur, nous pouvons appeler la méthode `requestDevice` pour obtenir le périphérique GPU (GPU device).

Ce périphérique fournit un contexte pour travailler avec le matériel.

Et une interface pour créer des objets GPU, tels que des tampons (buffers) et des textures.

Nous pouvons également exécuter des commandes sur ce périphérique GPU. Comme avec WebGL, nous avons besoin d'un contexte pour notre élément canvas qui sera utilisé pour afficher les graphismes.

Ici, nous utilisons l'élément canvas pour demander le contexte WebGPU.

Vous pouvez voir ici `getContext` par le nom `webgpu`.

C'est un mot-clé utilisé par WebGPU pour créer le contexte.

Nous configurons ensuite ce contexte avec le périphérique et le format.

Ensuite, nous définissons le pipeline de rendu (render pipeline) en appelant la méthode `createRenderPipeline`.

À l'intérieur de ce pipeline, nous avons plusieurs attributs.

Le premier est `vertex`, où nous assignerons le shader au module.

Ici avec un point d'entrée comme fonction `vs_main`, cette fonction est créée dans notre fichier shader.

De même pour l'attribut `fragment`, nous assignons le shader au module et un point d'entrée comme fonction `fs_main`.

L'autre attribut requis est `primitive` ici, cet attribut contient un champ appelé `topology`.

Nous le définissons sur `triangle-list` car nous voulons créer un triangle dans ce projet.

Ensuite, nous créons l'encodeur de commandes (command encoder) et la passe de rendu (render pass) en appelant `beginRenderPass`.

Cette passe de rendu accepte un paramètre de type `GPURenderPassDescriptor` comme option de passe de rendu.

Ici, nous n'utilisons que des attachements de couleur (color attachments) qui sont utilisés pour stocker les informations d'image.

Dans notre exemple, il stocke la couleur d'arrière-plan dans la zone `clearValue`. Nous avons un autre champ appelé `loadValue`.

Ce champ sera supprimé de WebGPU dans la prochaine version, nous ne l'utilisons donc pas ici.

Ensuite, nous assignerons le pipeline à notre passe de rendu et dessinerons notre triangle en appelant la méthode `draw` ici.

Nous appelons la fonction `end` pour terminer la passe de rendu actuelle, ce qui signifie qu'aucune autre instruction n'est envoyée au GPU.

Enfin, nous soumettons toutes les instructions à la file d'attente (queue) du périphérique GPU pour exécution.

Après l'exécution de la commande, notre triangle sera écrit dans le contexte GPU et affiché sur notre élément canvas.

Nous avons maintenant terminé l'implémentation de notre méthode `createTriangle`.

Cette méthode fournit la procédure de base pour créer des applications WebGPU, à savoir : d'abord nous initialisons l'API WebGPU, créons le programme shader, configurons le pipeline de rendu et construisons la passe de rendu, appelons la fonction de dessin, soumettons les instructions au GPU pour exécution.

Enfin, nous appelons la fonction `CreateTriangle` pour générer notre triangle.

Jusqu'à présent, nous avons terminé notre programmation pour ce projet.

Nous pouvons maintenant exécuter la commande suivante sur la fenêtre du terminal : `npm run prod` pour regrouper notre code TypeScript en modèle de production.

D'accord, c'est fini.

Notre fichier bundle est créé avec succès.

Maintenant, nous pouvons cliquer sur le lien "Go Live" à partir d'ici pour ouvrir Chrome Canary et voir notre triangle.

Cliquez sur ce lien.

Voici notre triangle coloré.

Vous pouvez voir ici le rouge, le vert et le bleu.

D'un sommet à l'autre, vous pouvez voir que la couleur change en douceur car WebGPU interpelle la couleur en interne, ce qui donne un dégradé de couleurs fluide.

Nous avons maintenant terminé le projet 2.

C'est un projet trois : nous allons créer un carré coloré en utilisant un tampon GPU (GPU buffer).

Dans le dernier projet, nous avons créé un triangle coloré dans WebGPU en écrivant les données de sommets et de couleurs directement dans le code du shader.

Cette approche n'est possible que pour créer des formes très simples.

Il est presque impossible d'utiliser cette approche directe pour créer des graphismes 3D complexes avec différentes couleurs et textures.

Dans ce projet, j'introduirai le tampon GPU (GPU buffer) et je vous montrerai comment l'utiliser pour stocker les informations de sommets et de couleurs.

Dans cet exemple, nous créerons un carré coloré pour expliquer le concept du tampon GPU.

Ici, nous introduirons plusieurs nouveaux concepts qui seront la base pour créer des objets graphiques 3D complexes.

Le tampon GPU dans WebGPU représente un bloc de mémoire qui peut être utilisé pour stocker des données pour les opérations GPU.

Dans ce projet, je vous montrerai comment utiliser le tampon GPU pour stocker la position des sommets et les données de couleur.

Vous pouvez télécharger le code source utilisé dans ce projet à partir de ce lien de dépôt GitHub.

Vous pouvez voir que nous avons une version de commit spécifique, cette version est spécifique à notre projet actuel.

Maintenant, lançons Visual Studio Code et ouvrons le projet 2 que nous avons construit dans la dernière vidéo.

D'accord, voici le projet 2 que nous avons utilisé dans la dernière vidéo.

Maintenant, apportons d'abord quelques modifications au fichier `index.html`.

Depuis le dossier `dist`, ouvrez le fichier `index.html`.

Maintenant, nous devons changer ici le titre `h1` en "Create Square Using GPU Buffer".

Nous n'avons donc pas besoin de changer l'autre partie du code.

Nous pouvons donc enregistrer ce fichier.

Ensuite, à partir du dossier `src`, ouvrez le fichier `helper.ts`.

Maintenant, nous devons ajouter une nouvelle fonction appelée `InitGPU` à ce fichier helper.

Nous devons donc ajouter du code ici.

Vous pouvez voir que nous plaçons tout le code d'initialisation WebGPU dans cette fonction, `initGPU`.

Cela permet d'éviter la duplication de code car l'initialisation sera la même pour tous les projets WebGPU.

Cette fonction est une fonction asynchrone, et elle renvoie le périphérique (device), le canvas, le format et le contexte, qui seront utilisés lorsque nous créerons un pipeline de rendu et une passe de rendu.

Nous voulons également ajouter une autre fonction appelée `CreateGPUBuffer` à ce fichier helper.

Nous devons donc ajouter une autre fonction ici appelée `CreateGPUBuffer`.

Vous pouvez voir que cette fonction prend trois entrées : le périphérique, les données et le drapeau d'utilisation (usage flag).

Ici, nous définissons le drapeau d'utilisation par défaut sur `vertex` ou `copy-destination`.

Ici, vous pouvez voir que nous appelons la méthode `createBuffer` du périphérique pour créer un tampon GPU et définissons la taille comme la longueur en octets des données pour allouer l'espace pour les données du tampon.

L'autre attribut ici `mappedAtCreation`, nous le définissons sur `true`.

Cela signifie que le tampon GPU appartient au CPU, qui est accessible en lecture-écriture à partir du code TypeScript.

Une fois que le tampon GPU est mappé, l'application peut demander l'accès à une plage de contenu avec, par exemple, la méthode `getMappedRange` et y définir les données à stocker dans le tampon.

Veuillez noter que le tampon GPU mappé ne peut pas être directement utilisé par le GPU et il doit être démappé en appelant la méthode `unmap`.

Ici, notre méthode `createGPUBuffer` renvoie un tampon démappé, qui peut être utilisé par le GPU.

Soyez donc prudent ici concernant les états mappé et démappé du tampon GPU.

Maintenant, nous pouvons enregistrer ce fichier et le fermer.

Ensuite, nous devons apporter des modifications au fichier `main.ts` du dossier `src`, ouvrez le fichier `main.ts`.

Nous devons remplacer son contenu par le nouveau code.

Vous pouvez voir ici que nous introduisons d'abord `initGPU` et `createGPUBuffer` du fichier `helper.ts` puis nous introduisons le shader.

Le code du shader sera discuté dans un instant.

À l'intérieur de la méthode `CreateSquare`, nous appelons d'abord la méthode `initGPU` pour créer un objet GPU puis en obtenir le périphérique.

Ensuite, nous définissons les données de sommets et les données de couleur ici.

Vous pouvez voir que ce sont nos données de sommets, données de couleur.

Voici les coordonnées des sommets de notre carré a, b, c, d.

Ainsi, les coordonnées comme ici a moins point cinq moins un et ceci est a, b, d, nous avons divisé ce carré en deux triangles a, b, d et d, b, c, les sommets de chaque triangle doivent être disposés dans l'ordre inverse des aiguilles d'une montre.

Vous pouvez voir ici a-b-d, d-b-c.

Nous attribuons également une couleur à chaque sommet.

Vous pouvez voir a rouge, b vert, c bleu et d jaune.

Vous pouvez voir ici que pour a c'est rouge, pour b c'est vert, et ainsi de suite.

Ces données sont cohérentes avec les coordonnées illustrées dans cette figure.

Bien sûr, vous pouvez également diviser les deux triangles d'une autre manière.

Par exemple, a-b-c, c-d-a.

Vous tracez donc la diagonale dans ce sens.

Vous obtenez ainsi deux autres triangles.

Cela n'a pas d'importance.

Ensuite, nous créons deux tampons en appelant le `CreateGPUBuffer` : l'un est le tampon de sommets (vertex buffer) et l'autre est le tampon de couleurs (color buffer).

Ensuite, nous créons un pipeline en appelant la méthode `createRenderPipeline`.

Le nouveau code que nous ajoutons ici concerne l'attribut `buffers`.

Auparavant, nous n'avions pas cet attribut `buffers`.

Maintenant, c'est un tableau de deux éléments, le premier élément est pour la position des sommets.

Le second est pour la couleur.

Vous pouvez voir que pour la position des sommets, nous avons `arrayStride` que nous avons réglé sur huit puisque chaque sommet est représenté à l'aide de deux éléments `float32`.

Chaque nombre `float32` nécessite quatre octets tandis que pour la couleur, elle est représentée pour chaque sommet à l'aide de trois éléments `float32`.

Ainsi, son `arrayStride` est réglé sur 12.

L'autre paramètre important ici est `shaderLocation`.

Pour la position des sommets, nous définissons la `shaderLocation` sur zéro, et pour la couleur nous définissons la `shaderLocation` sur un. L'autre partie du code est très similaire à celle utilisée dans le projet précédent.

Ici, nous définissons la topologie primitive sur `triangle-list`.

Une chose nouvelle ici est qu'après avoir défini le pipeline pour la passe de rendu ici, nous devons également définir le tampon de sommets pour la passe de rendu en utilisant le tampon de sommets et le tampon de couleurs.

Vous pouvez voir ici que nous définissons le tampon de sommets comme slot zéro.

Et au slot un, nous définissons le tampon de couleurs.

Dans la fonction `draw` ici, nous définissons le nombre de sommets à six car nous avons maintenant deux triangles.

Nous avons maintenant terminé la modification de ce fichier.

Maintenant, nous pouvons enregistrer ce fichier.

Ensuite, nous devons apporter des modifications à notre code de shader.

Depuis le dossier `src`, ouvrez le fichier `shader.wgsl`.

Ici, nous devons remplacer son contenu par le nouveau code.

Ici, vous pouvez voir que nous n'avons défini aucun sommet ni aucune couleur dans ce code de shader car nous stockons ces données dans le tampon GPU.

Au lieu de cela, nous introduisons deux entrées : l'une est à la `location(0)` `pos`, et l'autre est la couleur à la `location(1)`, ce qui doit être cohérent avec la définition de la localisation du shader dans le pipeline de notre fichier `main.ts`, car nous avons défini la localisation du shader comme zéro pour la position et la localisation du shader est un pour la couleur.

Ici, la position est donc à zéro.

Et ici, la localisation de la couleur est à un.

C'est ainsi que nous établissons la relation entre le vertex shader et les tampons GPU.

Notez que nous les définissons ici comme un `vec4<f32>`.

Pour la couleur, la même chose `vec4<f32>`.

Ils semblent ne pas être très cohérents avec les données stockées dans les tampons de sommets et de couleurs où pour la position, c'est un tableau 2D et pour la couleur, c'est un tableau 3D.

C'est parce que le shader WGSL est assez intelligent pour les convertir automatiquement en types `vec4` en ajoutant zéro à la composante Z et un pour la composante W.

Vous pouvez voir ici que nous définissons également deux sorties : l'une est la position, l'autre est `vColor` en utilisant une structure.

À l'intérieur de cette fonction `vs_main`, nous traitons les données de position et de couleur en assignant `pos` à la position et `color` à `vColor`.

À l'intérieur du fragment shader, nous introduisons `vColor` du vertex shader et le renvoyons comme couleur de fragment.

D'accord, c'est le shader que nous utiliserons lors de la création de notre carré.

Nous pouvons maintenant enregistrer ce fichier et le fermer.

Maintenant, nous pouvons exécuter la commande suivante dans la fenêtre du terminal pour regrouper notre code TypeScript : `npm run prod` pour regrouper notre code en mode production.

D'accord, le fichier bundle est créé avec succès.

Maintenant, nous pouvons cliquer sur le lien "Go Live" pour ouvrir Chrome Canary et voir notre carré.

Cliquez donc sur ce lien "Go Live".

Voici notre carré coloré avec différentes couleurs de sommets.

Ici, c'est rouge, vert, bleu et jaune.

D'un sommet à l'autre, vous pouvez voir que la couleur change en douceur car WebGPU interpelle la couleur en interne, ce qui donne un dégradé de couleurs fluide.

D'accord, nous avons maintenant terminé le projet trois.

Dans les projets deux et trois, j'ai démontré comment créer un triangle et un carré dans les applications WebGPU.

En fait, ces deux objets sont plats et bidimensionnels.

Nous n'avons pas encore créé de véritables graphismes 3D.

Dans ce projet 4, j'expliquerai comment créer un cube 3D avec des couleurs de face distinctes.

C'est le premier véritable objet 3D que nous allons créer dans une application WebGPU.

Vous pouvez télécharger le code source utilisé dans ce projet à partir de ce lien de dépôt GitHub.

Ici, nous avons une version spécifique pour ce projet.

Cet exemple implique beaucoup de code et de mathématiques.

Préparez-vous donc à le digérer.

Afin de créer de véritables objets 3D dans WebGPU, vous devez avoir des bases mathématiques sur les matrices 3D et les transformations.

Comme notre écran d'ordinateur est bidimensionnel, il ne peut pas afficher directement des objets 3D.

Pour visualiser des objets 3D sur un écran 2D, vous devez projeter votre objet de la 3D vers la 2D, ce qui impliquera une série de transformations de coordonnées.

À partir d'ici, vous pouvez voir que nous définissons l'objet 3D dans le système de coordonnées de l'objet ici.

Nous effectuons ensuite diverses transformations sur l'objet, notamment la mise à l'échelle (scaling), la translation et la rotation.

Nous appelons cette transformation une transformation de modèle (model transform).

Après cette transformation, nous convertissons un objet des coordonnées de l'objet en l'objet dans l'espace mondial (world space).

Ensuite, la transformation de vue (view transformation) localise l'observateur dans l'espace mondial et transforme notre objet 3D dans l'espace de la caméra, également appelé coordonnées de l'œil (eye coordinates).

Le but de la transformation de projection ici est de définir un volume de vue appelé frustum de vue (view frustum), juste ici.

C'est un frustum de vue.

Ceci est utilisé de deux manières : cela détermine comment un objet est projeté sur l'écran.

Cela définit également quelles parties de l'objet sont découpées de l'image finale.

C'est-à-dire que seule la partie à l'intérieur de ce frustum sera conservée et tout ce qui se trouve à l'extérieur de ce frustum sera découpé.

Enfin, nous utilisons la transformation de viewport pour convertir les coordonnées de découpe en coordonnées de périphérique normalisées.

Dans WebGPU.

La transformation de viewport ici est automatiquement effectuée dans le code du shader.

Veuillez noter que, comme WebGL, l'API WebGPU ne fournit aucune fonction pour travailler avec les transformations.

Dans ce projet, nous utiliserons un package JavaScript appelé `gl-matrix` pour effectuer des opérations de matrices 3D et des transformations.

Comme les matrices 3D et les transformations sont communes à toute programmation graphique par ordinateur, je suppose ici que vous avez déjà ces bases mathématiques, je n'y passerai pas plus de temps.

Au lieu de cela, je me concentrerai sur la façon de créer des objets 3D dans les applications WebGPU.

À partir de ce projet, vous apprendrez des concepts importants dans WebGPU que sont le tampon uniforme (uniform buffer) et le groupe de liaison (binding group).

Nous utiliserons un tampon uniforme pour représenter les matrices de transformation et de projection, puis nous utiliserons le groupe de liaison pour passer les tampons uniformes au vertex shader.

Maintenant, nous commençons avec notre Visual Studio Code et ouvrons notre projet trois que nous avons construit dans la dernière section.

Voici le code que nous avons utilisé dans le projet trois.

Tout d'abord, nous devons installer un nouveau package NPM appelé `gl-matrix` : `npm install gl-matrix`.

Nous utiliserons ce package pour effectuer des opérations de matrices et des transformations 3D. Maintenant, apportons quelques modifications au fichier `index.html`.

Depuis le dossier `dist`, ouvrez le fichier `index.html`.

Ici, nous devons changer le titre `h1` en "Cube with Distinct Face Color".

Nous n'avons donc pas besoin de changer d'autres parties du code.

Enregistrez ce fichier.

Ici, nous allons créer notre cube 3D.

Ce sont les coordonnées de notre cube.

À partir de ce diagramme, vous pouvez voir qu'il y a huit sommets et six faces.

si chaque face a une couleur différente, chaque sommet aura alors trois couleurs différentes.

Pour ces sommets, par exemple, le sommet C, nous avons la face supérieure, la face avant et la face droite.

Parce que chaque face a une couleur différente.

Ainsi, le sommet C peut avoir trois couleurs différentes selon la face dont nous parlons. Voici la face avant A, B, C, D.

Vous pouvez voir A, B, C, D ici.

Comme nous l'avons fait auparavant, nous pouvons maintenant diviser cette face avant en deux triangles.

L'un est A-B-C, C-D-A, deux triangles que vous pouvez voir ici ABC et CBA.

De cette façon, vous pouvez effectuer la triangularisation pour les autres faces.

Ensuite, ajoutez un nouveau fichier TypeScript au dossier `src` et appelez-le `vertex_data.ts`.

Ajoutez le nouveau code à ce fichier. Voici les données de position pour notre cube : c'est la face avant, la face droite, et les six faces. Voici les données de couleur pour les différentes faces.

Vous pouvez voir que pour la face avant nous utilisons la couleur bleue, la face droite est rouge, la face arrière est jaune, et ainsi de suite.

Ainsi, chaque face a une couleur différente.

Toutes les coordonnées de position et la couleur sont cohérentes avec ce diagramme illustré ici.

Maintenant, nous pouvons enregistrer ce fichier et le fermer.

Ensuite, nous apporterons quelques modifications au code du shader.

Depuis le dossier `src`, ouvrez le fichier `shader.wgsl`.

Maintenant, nous devons remplacer ce contenu par le nouveau code. Vous pouvez voir que ce shader est différent de celui que nous avons utilisé dans le projet trois car nous devons incorporer les tampons uniformes qui stockent les matrices de transformation et de projection. Ici, nous définissons une structure uniforme puis utilisons le groupe de liaison pour passer la matrice modèle-vue-projection au shader.

Ici, la matrice `mvp` signifie matrice modèle-vue-projection. Vous pouvez voir ici que le type de variable est `uniform`.

Ensuite, nous définissons la structure de sortie comme nous l'avons fait dans le dernier projet.

Nous définissons la position et `vColor`.

C'est la même chose qu'avant.

Pour la fonction `vs_main`, nous définissons également les deux entrées : l'une est la position, l'autre est la couleur, comme dans le dernier projet.

Et à l'intérieur de cette fonction, la seule différence est que la position n'a pas seulement le `pos` ici, mais nous multiplions également par cette matrice modèle-vue-projection.

Nous effectuons donc la transformation sur cette position.

Pour le fragment shader, nous utilisons toujours `vColor` comme entrée et le renvoyons comme couleur de fragment.

C'est la même chose que dans le projet trois.

Maintenant, nous pouvons enregistrer ce fichier et le fermer. Maintenant, nous ouvrons le fichier `helper.ts` du dossier `src`.

Ici, nous devons d'abord importer depuis `gl-matrix`.

Nous devons introduire `vec3`, `mat4`, puis ajouter une nouvelle méthode appelée `CreateViewProjection` à ce fichier.

Cette méthode `CreateViewProjection` prend quatre arguments d'entrée : d'abord le rapport d'aspect (aspect ratio), la position de la caméra, la direction vers laquelle la caméra regarde, et la direction du haut de la caméra.

Ici, nous créons d'abord des matrices de vue, de projection et de vue-projection.

Nous utilisons ensuite `mat4.perspective` et `mat4.lookAt` pour créer les matrices de projection et de vue.

Ensuite, nous utilisons la méthode `mat4.multiply` pour combiner la matrice de projection avec la matrice de vue afin de former notre matrice de vue-projection.

Cette fonction renvoie la matrice de vue, la matrice de projection, la vue-projection et l'option de caméra.

L'option de caméra sera utilisée dans le prochain projet lorsque nous discuterons du contrôle de la caméra.

Maintenant, nous devons ajouter une autre fonction appelée `createTransformation`, qui est utilisée pour construire la matrice de modèle. Ici, nous créons d'abord trois matrices de rotation pour la rotation autour des axes X, Y et Z. Nous créons ensuite des matrices de translation et de mise à l'échelle.

Ensuite, nous effectuons une transformation individuelle pour les arguments d'entrée ici.

Enfin, nous combinons toutes les transformations ensemble pour former nos matrices de transformation finales qui sont nos matrices de modèle.

Maintenant, enregistrez ce fichier et fermez-le. Ensuite, nous devons apporter quelques modifications au fichier `main.ts`.

Depuis le dossier `src`, ouvrez le fichier `main.ts`.

Ici, nous devons remplacer son contenu par le nouveau code.

Ici, nous introduisons d'abord quelques méthodes d'un fichier `helper.ts`, y compris les nouvelles fonctions `createTransforms`, `createViewProjection`, nous introduisons également les données du cube du fichier `vertex_data.ts`, ainsi que `mat4` de la bibliothèque `gl-matrix`.

À l'intérieur de cette méthode `create3dObject`, le code est très similaire à celui que nous avons utilisé dans le projet trois.

Ici, nous créons le tampon de sommets, vous pouvez voir, et le tampon de couleurs en utilisant les positions et les couleurs des données du cube.

Voici le code du pipeline.

Également similaire au projet trois.

La différence ici est que l'enjambée du tableau (array stride) pour la position est de 12 au lieu de huit.

À l'heure actuelle pour notre cube, nous avons des coordonnées x, y, z.

Nous avons donc 12 ici. Pour notre couleur, toujours 12 car nous avons des éléments RVB.

Ici, nous définissons également la localisation du shader sur zéro pour la position et la localisation du shader est un pour la couleur.

La seule différence dans le pipeline ici est que nous ajoutons cet attribut `depth_stencil`.

Ici, nous définissons `depthWriteEnabled` sur `true` pour activer le test de profondeur (depth stencil testing).

Le test de profondeur détermine si un pixel donné doit être dessiné ou non.

Pour les graphismes 3D.

l'activation du test de profondeur est très importante.

Sinon, vous pourriez obtenir des résultats inattendus.

Le code suivant est nouveau et spécifique à notre cube 3D.

Ici, nous créons des matrices modèle-vue et modèle-vue-projection en appelant la méthode `CreateViewProjection`.

Nous créons ensuite un tampon uniforme pour nos matrices `mvp`.

Vous pouvez voir ici l'utilisation, nous le définissons comme un uniforme pour notre transformation.

La taille est de 64 puisque notre matrice est de quatre par quatre, nous avons donc 16 éléments.

Chaque élément est un nombre `float32`, donc sa taille est de 64.

Nous définissons ensuite le groupe de liaison en appelant `createBindGroup` pour ce tampon uniforme.

Ici, nous définissons la mise en page (layout) comme le pipeline par défaut `getBindGroupLayout(0)`.

Cela signifie que nous utilisons la mise en page du groupe de liaison zéro.

Dans l'attribut `entries`, nous définissons les liaisons (bindings) sur zéro et définissons le tampon ici sur le tampon uniforme que nous venons de définir ici.

Si nous avons plus de tampons uniformes, nous pouvons ajouter les éléments ici.

Placez-les dans ce tableau `entries`.

En plus de la vue de texture du contexte, nous introduisons également la texture de profondeur.

Ici, nous définissons la taille comme la largeur et la hauteur de notre canvas.

Et le format que nous utilisons ici est `depth24plus`, vous pouvez également utiliser un autre format.

L'utilisation ici, nous la définissons sur `render_attachment`.

Maintenant, notre description de passe de rendu comprend deux parties : l'une est les attachements de couleur et l'autre partie est l'attachement de profondeur (depth stencil attachment).

L'attachement de couleur est le même que celui que nous utilisons dans le projet trois.

L'attachement de profondeur est spécifique à notre cube 3D.

Ensuite, nous construisons la matrice de modèle en appelant la méthode `createTransforms` définie dans le fichier `helper.ts`.

Nous obtenons ensuite la matrice Model View MVP en multipliant la matrice de modèle par la matrice de vue-projection.

Ainsi, nous avons obtenu une matrice modèle-vue-projection finale, puis nous ajoutons cette matrice modèle-vue-projection à notre tampon uniforme en appelant la méthode `writeBuffer`.

Vous devriez déjà être familier avec le code suivant ici.

Nous définissons simplement la passe de rendu et définissons le tampon de couleur des sommets.

Mais nous devons également définir le groupe de liaison ici en utilisant le groupe de liaison uniforme qui est nécessaire pour passer le tampon uniforme au vertex shader.

Maintenant, nous avons terminé la modification du fichier `main.ts`.

Nous pouvons ensuite enregistrer ce fichier.

Jusqu'à présent, nous avons terminé toute la programmation pour ce projet.

Ensuite, nous pouvons exécuter la commande suivante dans la fenêtre du terminal pour regrouper notre code en mode production : `npm run prod`.

D'accord, le fichier bundle est créé avec succès.

Maintenant, nous pouvons cliquer sur le lien "Go Live" pour ouvrir Chrome Canary et voir notre cube 3D.

Cliquez sur ce lien.

Voici notre cube avec des couleurs de face distinctes affiché sur cette page.

D'accord, nous avons terminé ce projet.

C'est le projet 5, dans lequel nous discuterons de l'animation et du contrôle de la caméra.

Dans le dernier projet, j'ai expliqué comment utiliser le tampon uniforme pour créer un cube 3D.

Dans ce projet, j'illustre déjà comment animer ce cube et comment utiliser la souris pour interagir avec le cube, vous pouvez télécharger le code source utilisé dans ce projet à partir de ce lien de dépôt GitHub. Ici, la version de commit spécifique est utilisée pour ce projet.

Pour l'animation, nous utiliserons la fonction JavaScript `requestAnimationFrame`.

Cette fonction peut apporter des modifications à votre écran de manière efficace et optimisée.

Voici un exemple d'utilisation de `requestAnimationFrame`.

Vous pouvez voir ici que nous bouclons encore et encore en utilisant une récursion.

Ici, nous définissons d'abord l'élément DOM dans l'interface utilisateur et définissons un nombre de départ de zéro ici.

Ensuite, nous créons une fonction `count` qui augmente le nombre de un.

Et ensuite, nous le définissons comme contenu textuel pour l'élément compteur.

À l'intérieur de cette fonction de compteur, nous appelons `requestAnimationFrame` et passons la fonction de compteur elle-même comme fonction de rappel (callback).

Cela l'amène à s'exécuter à nouveau juste avant la image suivante.

Enfin, nous utilisons la fonction `requestAnimationFrame` pour démarrer l'animation.

C'est une utilisation basique de `requestAnimationFrame`.

Pour utiliser la souris pour interagir avec le cube, nous utiliserons le package npm appelé `3d-view-controls`.

Ce package peut être utilisé pour contrôler la caméra avec votre souris, vous pouvez ensuite interagir avec l'objet 3D en contrôlant la caméra.

Maintenant, lançons Visual Studio Code et ouvrons le projet quatre que nous avons construit dans la dernière section.

Voici le code utilisé dans le projet quatre.

Tout d'abord, nous devons installer le package JavaScript appelé `3d-view-controls`.

Ouvrez la fenêtre du terminal et exécutez `npm install 3d-view-controls`. Nous utiliserons ce package pour le contrôle de la caméra.

Le package est déjà installé.

Maintenant, apportons quelques modifications au fichier `index.html`.

Depuis le dossier `dist`, ouvrez ce fichier.

Tout d'abord, nous devons changer le titre `h1` en "Animation and Camera control".

Nous devons également ajouter deux boutons radio qui vous permettent de sélectionner si vous voulez l'animation ou le contrôle de la caméra ici. Vous pouvez voir le bouton radio.

D'accord, maintenant nous pouvons enregistrer ce fichier.

Le code du shader dans cet exemple est le même que celui utilisé dans le projet 4.

Nous n'avons donc pas besoin d'apporter de modification au code du shader.

Maintenant, à partir du dossier `src`, ouvrez le fichier `helper.ts`.

Ici, nous devons ajouter une nouvelle méthode appelée `CreateAnimation`.

Nous devons ajouter `create_animation` ici.

C'est le code pour la méthode `create_animation`.

Ici, l'argument `draw` est une fonction de rappel.

Ici, nous voulons animer la rotation autour des axes X, Y et Z en utilisant la fonction `step` ici, la fonction `step`.

`CreateAnimation` a un argument booléen ici `is_animation` qui contrôle si vous voulez animer l'objet ou non.

Maintenant, nous pouvons enregistrer ce fichier et le fermer.

Ensuite, nous devons apporter quelques modifications au fichier `main.ts`.

Ouvrez le fichier `main.ts`.

Nous devons remplacer le contenu par votre code.

Ce code est en fait très similaire au code utilisé dans le dernier projet.

Ici, en plus de l'autre fonction introduite à partir du fichier `helper.ts`, nous introduisons également la fonction `CreateAnimation` que nous venons de créer.

Notez que nous utilisons ici `require` pour introduire le module `3d-view-controls`, au lieu de `import`.

C'est parce que le package `3d-view-controls` a été créé en utilisant l'ancienne approche des modules.

Nous devons donc utiliser `require` au lieu de `import` ici.

Ici, nous définissons `createCamera` à partir de ce package.

Dans la méthode `create3dObject`, nous introduisons un argument d'entrée `is_animation`, et nous définissons sa valeur par défaut sur `true` ici.

Ici, le code d'initialisation et le code du pipeline sont les mêmes que ceux utilisés dans le dernier projet, nous n'avons pas besoin d'apporter de modification à ce code.

Dans la section de création des données uniformes, nous définissons `v-matrix`, c'est la matrice de vue, c'est une nouvelle matrice.

Ensuite, nous devons ajouter la rotation et la caméra.

La rotation, nous la définissons en utilisant `vec3` et la caméra, nous définissons `create-camera` ici.

nous avons les arguments `canvas` et l'option de caméra, nous n'avons pas besoin d'apporter de modifications au code pour créer un tampon uniforme ici et un groupe de liaison uniforme.

Cette description de passe de rendu est également la même que celle utilisée dans le dernier projet, ici, nous mettons ce code lié à la passe de rendu à l'intérieur de la nouvelle fonction appelée fonction `draw`.

Cette fonction `draw` est définie comme une fonction de rappel pour notre animation.

Vous pouvez voir ici que si `is_animation` n'est pas vrai, nous utilisons la caméra pour générer notre matrice de vue.

Et ensuite multiplions la matrice de projection par cette matrice de vue pour former notre matrice de vue-projection.

Le reste du code de la méthode `draw` est le même que celui que nous avons utilisé dans le dernier projet.

Ici, nous démarrons l'animation en appelant la fonction `CreateAnimation`.

Vous pouvez voir que nous avons une fonction de rappel, utilisant la fonction `draw` définie ici.

Enfin, nous devons ajouter une sélection de bouton radio ici, vous pouvez voir que si la valeur cochée de la radio est égale à animation, nous lançons l'animation.

Sinon, nous utilisons le contrôle de la caméra.

Maintenant, nous avons terminé la modification du fichier `main.ts`.

Nous pouvons donc enregistrer ce fichier maintenant.

Jusqu'à présent, nous avons terminé toute la programmation.

Maintenant, nous pouvons exécuter la commande suivante dans la fenêtre du terminal : `npm run prod` pour regrouper notre code TypeScript.

D'accord, le fichier bundle est créé avec succès.

Maintenant, nous pouvons cliquer sur le lien "Go Live" pour ouvrir Chrome Canary et voir notre cube 3D.

Cliquez sur ce lien "Go Live".

Vous pouvez voir le cube animé sur cette page.

Il tourne continuellement parce que nous avons appelé le mode animation.

Maintenant, vous pouvez cliquer sur ce bouton radio de contrôle de la caméra ici, puis vous pouvez utiliser le bouton gauche de la souris pour faire pivoter le cube et utiliser le bouton droit pour le déplacer.

Et vous pouvez également utiliser la molette de la souris pour zoomer et dézoomer sur le cube.

Vous pouvez donc utiliser la souris pour interagir avec le cube.

Nous avons donc maintenant terminé ce projet.

Dans les projets précédents, j'ai expliqué comment créer des objets 2D et 3D.

Cependant, lors du rendu de ces objets graphiques avec des couleurs unies, vous constaterez peut-être que l'image semble plate et qu'elle ne parvient pas à illustrer la nature 3D des objets.

C'est parce que nous négligeons l'interaction entre la lumière et la surface de nos objets.

L'éclairage aide à fournir un effet visuel à une scène afin qu'elle paraisse plus réaliste.

L'éclairage est l'un des facteurs les plus importants pour créer des objets graphiques 3D ombrés du monde réel.

Cependant, WebGPU ne fournit pas beaucoup de fonctionnalités intégrées sur l'éclairage.

Il exécute simplement deux fonctions : les shaders de sommets et de fragments.

Si vous voulez l'effet d'éclairage dans votre scène 3D, vous devez créer le modèle d'éclairage vous-même.

Dans ce projet, je vais construire un modèle d'éclairage simple dans WebGPU et l'utiliser pour simuler la source lumineuse.

Ici, vous pouvez télécharger le code source utilisé dans ce projet à partir de ce lien de dépôt GitHub.

Ici, la version de commit spécifique est utilisée pour ce projet.

Ici, je discuterai de trois types de sources lumineuses : la lumière ambiante, la lumière diffuse et la lumière spéculaire.

La lumière ambiante est la lumière qui éclaire tous les objets uniformément, quels que soient leur emplacement ou leur orientation.

C'est une illumination globale dans un environnement.

La réflexion de la lumière diffuse et de la lumière spéculaire dépend de l'angle de la lumière par rapport à une surface.

Lorsque la lumière frappe la surface, la réflexion diffuse se produit dans toutes les directions, comme illustré ici, tandis que la réflexion de la lumière spéculaire se produit dans une seule direction.

comme illustré ici.

Ici est montrée la réflexion de la lumière sur une surface de tore.

À gauche ici, la lumière provient uniquement de la lumière ambiante, vous pouvez voir que ce tore semble très plat.

Ici, au centre, la lumière provient à la fois de la lumière ambiante et de la lumière diffuse.

Vous pouvez voir que la caractéristique 3D apparaît déjà ici.

À droite ici, nous avons trois sources lumineuses : ambiante plus diffuse plus spéculaire.

Vous pouvez voir que ce tore semble plus réaliste.

Ainsi, c'est le modèle de lumière que nous voulons construire dans ce projet.

La réflexion de la lumière dépend de l'angle sous lequel la lumière frappe la surface.

L'angle est essentiel pour la lumière diffuse et la lumière spéculaire.

Cet angle est toujours associé à la normale de la surface qui est perpendiculaire à la surface.

Pour construire le modèle de lumière, nous devons calculer la normale de la surface en fonction de la direction dans laquelle la surface est orientée.

Comme la surface d'un objet 3D peut être courbe, elle peut être orientée dans différentes directions à différents sommets.

Ainsi, un vecteur normal est généralement différent pour différents sommets, c'est-à-dire que le vecteur normal est toujours associé à un point particulier sur la surface.

Ici est montré le vecteur normal pour un cube 3D.

Ici, la face avant est orientée vers l'écran.

Son vecteur normal est donc 001.

La face droite est orientée vers la droite.

Son vecteur normal est donc 1 00.

Et la face supérieure est orientée vers le haut.

Son vecteur normal est donc 010.

De même, vous pouvez spécifier les vecteurs normaux pour les faces arrière, gauche et inférieure.

Notez que la longueur des vecteurs normaux doit toujours être de un, c'est-à-dire que nous devons normaliser les vecteurs normaux.

Pour un quadrilatère général A B C, D, ses 4 sommets peuvent ne pas être dans le même plan, nous pouvons le diviser en deux triangles, A, B, C et C D A.

Nous pouvons calculer sa normale de surface en deux étapes.

Tout d'abord, nous calculons la normale pondérée pour chaque triangle, qui est pondérée par l'aire de ce triangle.

Le triangle ayant la plus grande aire recevra plus de poids.

Comme nous le savons, l'aire d'un triangle est proportionnelle au produit vectoriel (cross product) de deux de ses côtés.

Par exemple, ici, pour le triangle A, B, C, nous avons un produit vectoriel B, C et C-A, b c et a c.

De même pour le triangle C D A, we have a cross product D A and A C.

L'étape suivante consiste à calculer la normale de la surface à partir des normales de triangle pondérées, c'est-à-dire que la normale de la surface est égale à la somme de deux normales pondérées, et nous pouvons ensuite la normaliser.

Ainsi, nous obtenons cette normale de quadrilatère égale à la normalisation de ces deux produits vectoriels.

La somme de ce triangle plus un autre.

Ainsi, nous pouvons combiner ces deux termes pour former un seul terme égal au produit vectoriel de C A et D B.

Cela signifie que la normale de la surface pour ce quadrilatère général est simplement égale au produit vectoriel de C, A et d b.

Juste égal au produit vectoriel de ces deux vecteurs diagonaux.

Nous utiliserons cette formule pour calculer le modèle de lumière pour nos surfaces 3D.

Une fois que nous avons calculé le vecteur normal, nous pouvons l'utiliser pour calculer l'intensité lumineuse.

Pour la lumière diffuse, son intensité est proportionnelle au cosinus entre le vecteur de lumière ici et un vecteur normal N.

Vous pouvez voir ici que le cosinus alpha est égal à L normalisé dot N ici.

Si nous définissons Id, l'intensité diffuse, Kd la propriété du matériau diffuse, nous pouvons donc avoir cette formule : l'intensité diffuse est égale à Kd fois le maximum du cosinus alpha et de 0.

Ici, le maximum est utilisé pour éviter la valeur négative du cosinus alpha ici, nous ne prenons que la valeur positive.

Nous pouvons également ajouter la lumière ambiante à l'intensité de la lumière diffuse comme ceci.

Ici, Ia est l'intensité de la lumière ambiante.

Ainsi, l'intensité lumineuse totale est le maximum de Kd et ici est le Ia.

Nous ajoutons donc l'intensité ambiante à cette lumière diffuse comme ceci.

Pour la lumière spéculaire, nous avons deux modèles, l'un est le modèle de Phong, ce modèle est très simple.

Ainsi, Is, l'intensité de la lumière spéculaire, est égale à Ks, Ks est la propriété du matériau spéculaire, et s est la brillance (shininess) de la surface ou la rugosité, V est la direction de la vue, R est la direction de la réflexion.

Un problème avec le modèle de Phong est que l'angle entre la direction de la vue et la direction de la réflexion doit être inférieur à 90 degrés pour que le terme spéculaire de Phong contribue.

Nous pouvons utiliser le modèle de Blinn-Phong pour résoudre ce problème.

Le modèle de Blinn-Phong utilise un ensemble différent de vecteurs pour son calcul, basé sur le vecteur de demi-angle (half-angle vector).

Voici un vecteur de demi-angle, vous pouvez voir L est la direction de la lumière, N est le vecteur normal, V est la direction de la vue, H est le vecteur de demi-angle défini comme L la direction de la lumière plus la direction de la vue.

La direction de la vue plus la direction de la lumière donne H ici.

La formule dans le modèle de Blinn-Phong devient N dot H au lieu de V dot R ici.

Ainsi, l'angle entre ce N et H est toujours inférieur à 90 degrés.

Ainsi, ce N dot H donne toujours une valeur positive.

Nous utiliserons donc ce mode Blinn-Phong dans notre calcul pour la lumière spéculaire.

Passons maintenant à la partie programmation.

Nous avons commencé avec Visual Studio Code et ouvert le projet cinq que nous avons construit dans la dernière section.

Voici le code de notre fichier de projet.

Maintenant, implémentons le modèle de lumière dans le code du shader.

Depuis le dossier `src`, ouvrez le `shader.wgsl`.

Nous devons remplacer son contenu par le nouveau code.

Ici, nous définissons d'abord la structure uniforme ici qui contient la matrice de vue-projection, la matrice de modèle et la matrice normale.

Ici, la matrice normale est la matrice de transformation pour les données du vecteur normal.

Lors de l'application d'une transformation à une surface, nous devons dériver le vecteur normal pour la surface résultante à partir des vecteurs normaux originaux.

Afin de transformer correctement le vecteur normal, nous ne les multiplions pas simplement par la même matrice utilisée pour transformer notre objet, mais nous devons les multiplier par la transposée de l'inverse de cette matrice.

Comme la version actuelle de WGSL n'implémente pas encore la fonction d'inversion de matrice, nous devons donc fabriquer cette transposée de l'inverse de la matrice de transformation dans le code TypeScript, puis la passer comme une matrice uniforme comme illustré ici, `normalMatrix`.

Nous définissons ensuite la structure de sortie qui contient trois variables : la position intégrée, la `v-position` la position après une certaine transformation, nous l'appelons la `v-position` et la `v_normal`, qui est un vecteur normal après transformation.

Dans notre fonction `vs_main`, elle contient deux arguments d'entrée : l'un est la position du sommet appelée `pos` et l'autre est la donnée du vecteur normal.

À l'intérieur de cette fonction, nous effectuons uniquement la transformation de modèle sur la position.

Cela nous donne la `v-position` ici car elle est utilisée dans le calcul de la lumière.

La `v-normal` est le résultat des données du vecteur normal multipliées par la matrice de transformation normale ici.

Et la position par défaut ici est obtenue en effectuant la transformation modèle-vue et de projection sur les données des sommets.

Pour le fragment shader, nous introduisons d'abord la structure uniforme appelée `FragUniform` qui contient deux variables : l'une est la position de la lumière ou le vecteur de lumière, et l'autre est la position de l'œil.

Ou vecteur de vue.

Il possède également une autre structure appelée `LightUniform`.

Ici sont contenus les paramètres de notre modèle de lumière.

Voici une couleur de lumière et une couleur spéculaire.

La lumière spéculaire peut avoir sa propre couleur, et les autres paramètres contiennent l'intensité ambiante, l'intensité diffuse, l'intensité spéculaire et la brillance spéculaire.

Ici, la fonction `fs_main` prend `v_position` et `v_normal` comme entrées.

À l'intérieur de cette fonction, nous calculons le modèle de lumière.

Voici le diffus.

Utilisez simplement N dot L, le cosinus alpha.

Pour la lumière spéculaire, nous utilisons le modèle de Blinn-Phong.

C'est N dot H.

La couleur de sortie du fragment shader sera pondérée, vous pouvez le voir, par la lumière ambiante, diffuse et spéculaire.

Sa combinaison nous donne la couleur finale.

Ainsi, c'est le shader que nous allons utiliser pour calculer le modèle de lumière.

Maintenant, nous pouvons enregistrer ce fichier et le fermer.

Ensuite, dans le dossier `src`, nous ajouterons un nouveau fichier TypeScript appelé `light.ts`.

Ajoutez un nouveau fichier `light.ts`.

Voici le code de ce fichier.

Ici, nous créons d'abord une interface nommée `LightInputs` qui contient les paramètres utilisés pour calculer le modèle de lumière.

Ce code contient également une nouvelle fonction `createShapeWithLight` qui possède quatre arguments d'entrée : l'un est les données de sommets, les données normales, et l'entrée de lumière, et les paramètres d'animation.

Ici, nous définissons les paramètres de lumière par défaut si aucun paramètre n'a été passé, nous avons donc des valeurs par défaut pour les paramètres de lumière.

Ensuite, nous créons un tampon de sommets et un tampon de normales ici.

Vous pouvez voir que le pipeline contient un attribut `buffers` ici.

C'est un tableau qui contient deux éléments.

Le premier élément est la donnée de sommet avec la localisation du shader étant zéro.

Le second élément est pour la donnée du vecteur normal avec la localisation du shader étant un ici.

L'autre partie du pipeline est la même que celle que nous avons utilisée dans le Projet cinq.

Ensuite, nous créons des données uniformes.

Ici, nous définissons la matrice normale et une matrice de modèle, et les matrices de vue et de vue-projection ici.

Par souci de simplicité, nous définissons ici la position de l'œil que nous obtenons de la caméra égale à la position de la lumière.

Cela signifie que le vecteur de lumière est égal au vecteur de vue.

Ici, nous créons ensuite trois tampons uniformes : l'un est le tampon uniforme de sommets, un autre est un tampon uniforme de fragments, et enfin c'est le tampon uniforme de lumière.

Le tampon uniforme de sommets est utilisé pour stocker la matrice de modèle, la matrice de vue-projection et la matrice normale.

Le tampon uniforme de fragments est utilisé pour stocker la position de l'œil et la position de la lumière.

Et le tampon uniforme de lumière est utilisé pour stocker les paramètres de lumière qui seront utilisés dans le calcul du modèle de lumière dans le fragment shader. Veuillez noter ici, à l'intérieur de la fonction de rappel `draw`, nous écrivons une matrice de modèle et une matrice normale à l'intérieur de cette fonction `draw`, car nous voulons utiliser la matrice de modèle en temps réel pour effectuer diverses transformations.

Notez que nous construisons la matrice normale ici en inversant d'abord cette matrice de modèle puis en transposant cette matrice normale.

Et nous obtenons la matrice normale finale.

Cela signifie que nous faisons l'inverse et la transposée sur la matrice de modèle originale.

Et enfin, nous obtenons la matrice normale.

lorsque nous définissons les données dans le tampon, veuillez noter qu'ici 64 et 128 sont des décalages (offsets), nous devons donc également utiliser le décalage correct pour écrire ces données dans le tampon uniforme.

Enfin, nous définissons le tampon de sommets, le tampon de normales et un groupe de liaison uniforme pour la passe de rendu.

Maintenant, nous avons terminé le codage pour le fichier.

Nous pouvons enregistrer ce fichier et le fermer. D'accord, nous avons terminé la programmation pour le calcul du modèle de lumière.

Dans le prochain projet, nous utiliserons le modèle de lumière implémenté ici pour créer un cube 3D avec effet d'éclairage.

Dans le Projet 6, j'explique comment construire un modèle de lumière simple dans WebGPU.

Dans ce projet, je vous montrerai comment utiliser ce modèle de lumière pour ajouter un effet d'éclairage à un cube 3D, comme illustré ici. Vous pouvez télécharger le code source utilisé dans ce projet à partir de ce lien de dépôt GitHub.

Cette version de commit spécifique est utilisée pour ce projet.

Lancez maintenant Visual Studio Code et ouvrez notre projet 6 que nous avons construit dans la dernière section.

Voici le code utilisé dans le projet 6 comme nous l'avons discuté dans la dernière section.

Afin de calculer le modèle de lumière, nous devons connaître le vecteur normal à chaque sommet sur la surface de l'objet 3D.

Nous devons maintenant ajouter les données du vecteur normal aux `vertex_data` de notre cube.

Depuis le dossier `src`, ouvrez le fichier `vertex_data.ts`.

Ici, pour la méthode `CubeData`, nous devons ajouter les données du vecteur normal ici. Vous pouvez voir que les sommets sur la même face ont le même vecteur normal.

Par exemple, la face avant a tout à 001.

De même pour la droite c'est le 100, tout à 100 et ainsi de suite.

Une fois que nous avons ajouté les données du vecteur normal à cette fonction `CubeData`, nous devons renvoyer les données normales ici `normals`.

Nous devons également renvoyer `normals`.

D'accord, maintenant nous pouvons enregistrer ce fichier et le fermer.

Ensuite, nous devons apporter quelques modifications au fichier `index.html`.

Depuis le dossier `dist`, ouvrez le fichier `index.html`.

Maintenant, nous devons remplacer son contenu par le nouveau code.

Ici, nous ajoutons quelques paramètres d'entrée ici qui vous permettent de tester notre modèle de lumière.

Ces paramètres vous permettent également de spécifier la couleur de l'objet, les coefficients de lumière ambiante, diffuse et spéculaire.

Vous pouvez également spécifier la brillance de la surface et la couleur spéculaire pour le calcul de la lumière spéculaire.

Maintenant, nous pouvons enregistrer ce fichier.

Ensuite, nous devons apporter quelques modifications au fichier `main.ts`.

Depuis le dossier `src`, ouvrez le fichier `main.ts`.

Maintenant, remplacez son contenu par le nouveau code.

Comme la majeure partie du code pour le pipeline de rendu et la passe de rendu a déjà été incluse dans le fichier `light.ts`, ici le fichier `main.ts` devient très simple.

Tout d'abord, nous introduisons `createShapeWithLight` et l'interface `LightInputs` du fichier `light.ts`, puis nous introduisons les données du cube du fichier `vertex_data.ts`.

Ensuite, nous appelons la méthode `CubeData` pour obtenir les données de sommets et définissons le paramètre par défaut ici, les `LightInputs`, nous utilisons simplement les paramètres par défaut.

Et aussi `is_animation`, nous le réglons sur `true`.

Et ensuite nous appelons la fonction `createShapeWithLight` pour créer un cube 3D avec effet d'éclairage.

Cette partie du code permet à l'utilisateur de recréer le cube avec un effet d'éclairage différent en changeant les paramètres d'entrée.

Nous avons maintenant terminé les modifications du fichier `main.ts`.

Nous pouvons maintenant enregistrer ce fichier.

Maintenant, nous pouvons exécuter la commande suivante dans la fenêtre du terminal pour regrouper notre code TypeScript en mode production : `npm run prod`. D'accord, le fichier bundle est créé avec succès.

Maintenant, nous pouvons cliquer sur le lien "Go Live" pour ouvrir Chrome Canary et voir notre cube 3D avec effet de lumière.

Cliquez sur ce lien.

Voici un cube rouge avec l'effet d'éclairage affiché sur cette page.

Nous pouvons apporter quelques modifications aux paramètres d'entrée et cliquer sur le bouton de redessin (redraw) pour recréer le cube.

Maintenant, par exemple, nous pouvons régler les coefficients diffus et spéculaires sur zéro ici, sur zéro, et la lumière ambiante sur un.

Maintenant, cliquez sur redessiner, nous obtenons un cube avec seulement la lumière ambiante.

Vous pouvez voir que le cube semble plat et sans caractéristique 3D.

Ajoutons maintenant la lumière diffuse et la lumière spéculaire à nouveau.

point 2.

Nous pouvons ensuite changer la couleur de l'objet.

Par exemple, ce rouge nous le changeons en vert, 010.

Et changeons également la couleur spéculaire du blanc au jaune, puis cliquons sur le bouton de redessin.

Vous pouvez voir ici le jaune, vous pouvez augmenter la brillance, par exemple, 100.

Vous pouvez voir le point un peu jaune.

C'est la lumière spéculaire.

Maintenant, revenons à l'animation.

Ainsi, en changeant ce paramètre, vous pouvez obtenir un nouvel effet d'éclairage sur ce cube.

Vous pouvez utiliser ce modèle de lumière pour créer facilement votre propre objet 3D en suivant la procédure présentée ici.

D'accord, nous avons maintenant terminé le projet 7.

Les projets dont nous avons discuté jusqu'à présent appliquaient une couleur fixe en attribuant une valeur de couleur souhaitée à la variable de couleur de fragment dans le fragment shader.

Dans ce projet, j'expliquerai comment utiliser la carte de couleurs (colormap) pour rendre des surfaces 3D.

Les surfaces jouent un rôle important dans diverses applications, notamment les jeux informatiques graphiques et la visualisation de données 3D.

Dans certaines applications de graphiques et de diagrammes, nous avons besoin d'une carte de couleurs personnalisée pour obtenir des effets visuels spéciaux.

En fait, la carte de couleurs est juste un tableau ou une liste de couleurs qui sont organisées d'une manière souhaitée.

Nous pouvons créer une carte de couleurs personnalisée avec une matrice de couleurs mx3, chaque ligne représentant des valeurs RVB.

L'index de ligne peut représenter les données Y d'un graphique 2D ou la hauteur d'un tracé de surface 3D.

Pour une matrice de carte de couleurs donnée, les valeurs des données de couleur peuvent être mises à l'échelle linéairement par rapport à la carte de couleurs.

Ici sont montrées les bandes de couleurs pour les cartes de couleurs que nous créerons dans ce projet.

Vous pouvez voir que chaque carte de couleurs a un nom de carte de couleurs familier, tel que hsv, hot, cool, jet, et ainsi de suite.

Vous pouvez télécharger le code source utilisé dans ce projet à partir de ce lien de dépôt GitHub.

Cette version de commit spécifique est utilisée pour ce projet.

Maintenant, commencez avec Visual Studio Code et ouvrez notre projet 7 que nous venons de construire dans la dernière section. Ici se trouve le code source utilisé dans le dernier projet.

Nous pouvons facilement créer une carte de couleurs personnalisée en utilisant une formule mathématique simple.

Ici, je fournirai plusieurs cartes de couleurs couramment utilisées en utilisant un tableau de cartes de couleurs mx3.

Maintenant, ajoutez un nouveau fichier TypeScript appelé `colormap_data.ts` au dossier `src`, dossier `src`, ajoutez un nouveau fichier appelé `colormap_data.ts`.

Et ensuite ajoutez une nouvelle méthode à ce fichier.

Ici, la méthode `ColormapData` contient 11 données de cartes de couleurs différentes.

Vous pouvez voir hsv, hot, et jet par défaut.

À l'intérieur de cette fonction, vous pouvez voir que chaque carte de couleurs contient 11 tableaux de couleurs RVB, chaque tableau ici contient des valeurs RVB.

Ici sont montrées les bandes de couleurs générées à l'aide de ces données de carte de couleurs.

Ceci est hsv, correspondant à cette bande de couleur.

Voici donc le jet correspondant à cette bande de couleur.

Ainsi, ces bandes de couleurs sont générées à l'aide des données de carte de couleurs.

Dans la fonction `ColormapData`, nous supposons que ces 11 tableaux de couleurs sont uniformément répartis dans la plage de zéro et un.

Par exemple, la couleur zéro, le premier élément représente une couleur à l'emplacement zéro, tandis que la couleur 5 représente une couleur à 0,5, etc.

Cependant, nous devons utiliser une méthode d'interpolation pour obtenir une couleur à, par exemple, 0,55 ou tout autre emplacement arbitraire.

Ici, nous utiliserons donc un package npm appelé `interpolate-arrays` pour effectuer l'interpolation des couleurs.

Maintenant, dans la fenêtre du terminal, nous exécutons la commande : `npm install interpolate-arrays` pour installer ce package.

Maintenant, en haut de ce fichier de carte de couleurs, nous devons introduire ce package ici.

Ici, vous pouvez voir à nouveau que nous utilisons `require` pour introduire ce package.

parce qu'il a été créé à l'origine en utilisant l'ancienne méthode des modules.

Nous devons donc utiliser `require` au lieu de `import` pour obtenir ce package.

Ensuite, nous ajoutons une nouvelle fonction ici appelée `addColors`. Voici la méthode `addColors` pour ce fichier.

Cette fonction accepte l'argument `x` dont la valeur est comprise entre le minimum et le maximum.

Cette fonction vous permet d'interpoler la couleur pour n'importe quelle valeur `x` arbitraire.

À l'intérieur de cette fonction, nous obtenons d'abord le tableau de couleurs en appelant la méthode `ColormapData` avec un nom de carte de couleurs comme entrée.

Et ensuite nous nous assurons que le paramètre d'entrée `x` est dans la plage de minimum et de maximum.

Ensuite, nous normalisons `x` dans la plage de zéro et un.

Enfin, nous interpolons la couleur pour la variable `x` en appelant `interp` ici la couleur et le `x` normalisé ici.

Cet `interp` provient du package `interpolate-arrays`.

Maintenant, cette fonction renvoie un tableau RVB avec chaque composante étant dans la plage de zéro et un.

Nous pouvons donc maintenant enregistrer ce fichier et le fermer.

Ensuite, dans le dossier `src`, renommez le fichier `light.ts` en fichier `surface.ts`.

Nous renommons donc ce fichier en `surface`.

Ce fichier `surface.ts` sera utilisé pour créer différents tracés de surface.

Tout d'abord, nous devons apporter de petites modifications à l'interface `LightInputs`.

Ici, nous pouvons supprimer le champ de couleur ici, car nous n'avons pas besoin de spécifier la couleur unie pour notre objet, mais nous utiliserons la carte de couleurs pour la couleur de l'objet.

Ensuite, nous ajoutons un autre nouveau champ appelé `is_two_side_lighting`.

Comme les surfaces 3D sont généralement des surfaces ouvertes, nous devons implémenter le modèle de lumière pour les deux côtés, avant et arrière, afin de voir la surface clairement, mais ce paramètre contrôle si vous voulez l'éclairage d'un seul côté ou des deux côtés.

Ensuite, nous changeons le nom de la fonction ici en `createSurfaceWithColormap`.

Nous changeons donc `createColormap`, et ajoutons ensuite une donnée de couleur comme argument d'entrée.

Ici, nous avons des données normales, nous devons ajouter les données de couleur.

Ces données de couleur signifient les données de la carte de couleurs.

Ici, nous devons supprimer cette couleur, et ajouter une nouvelle valeur par défaut pour `is_two_side_lighting` ici.

Ici, nous définissons la valeur par défaut sur un. Cela signifie l'éclairage des deux côtés.

Si c'est zéro, c'est un seul côté.

Ici, nous créons un tampon de sommets, un tampon de normales, nous devons également créer le tampon de couleurs.

`Color` et utiliser les données de couleur.

Ensuite, voici un tableau de tampons : le premier est le tampon de sommets, ceci est le tampon de normales.

Nous devons également ajouter un autre tampon pour les données de la carte de couleurs.

Ainsi, ici, nous devons définir la localisation du shader sur 2.

nous n'avons pas besoin de changer l'autre partie du code pour le pipeline.

Ainsi, l'autre partie est la même que celle utilisée dans le dernier projet.

Le code pour les données uniformes, la caméra et la mise en page du tampon uniforme est le même que celui utilisé dans le dernier projet.

Nous n'avons donc pas besoin de changer quoi que ce soit ici.

Mais ici, les paramètres de lumière, nous devons apporter quelques modifications car nous avons déjà supprimé la couleur de la lumière.

Nous supprimons donc cette couleur de lumière, mais nous devons ajouter un autre paramètre appelé paramètre `is_two_side_lighting`.

Nous devons donc ajouter un paramètre ici, pousser le paramètre `is_two_side_lighting` par 0 0, 0.

Mais nous rendrons le paramètre cohérent avec le tableau `vec4`.

L'autre chose que nous devons modifier est que nous devrions ajouter le tampon de couleur à la passe de rendu.

Nous avons un tampon de sommets et un tampon de normales.

Nous devons également ajouter le tampon de couleur ici, appelé `colorBuffer` au slot 2.

D'accord, nous avons terminé la modification de ce fichier.

À l'heure actuelle, nous pouvons donc enregistrer ce fichier.

Ensuite, nous devons apporter une modification au code du shader car nous voulons incorporer l'éclairage et la carte de couleurs dans le shader.

Maintenant, depuis le dossier `src`, ouvrez le fichier `shader.wgsl` à partir de là, ouvrez ce fichier et nous devons remplacer son contenu par le nouveau code.

Ce shader est très similaire à celui utilisé dans le dernier projet.

À l'intérieur du vertex shader, en plus de la position du sommet, vous pouvez voir, et du vecteur normal, nous ajoutons également la couleur à la localisation 2 à cette entrée.

Dans la fonction `vs_main`, nous traitons la carte de couleurs et assignons cette carte de couleurs à `v_color`.

Dans le fragment shader ici, nous utilisons les données de carte de couleurs traitées comme couleur primaire de notre objet ici.

Vous pouvez voir `v_color`, ceci est traité à partir du vertex shader.

Nous l'utilisons comme couleur primaire pour obtenir la couleur finale.

À l'intérieur de la fonction principale du fragment shader, vous pouvez voir ici le paramètre `is_two_side_lighting` ici appelé le `parameter[0]`, contrôle si l'éclairage est appliqué à un côté ou aux deux côtés de notre surface.

Nous le réglons sur un pour l'éclairage des deux côtés, ce qui est également le réglage par défaut.

Pour l'éclairage des deux côtés, vous pouvez voir ceci pour un côté pour le côté avant le diffus nous utilisons le N dot L, la lumière spéculaire nous utilisons N dot H.

Si l'éclairage est des deux côtés, nous ajoutons un autre terme ici pour le diffus nous utilisons moins N dot L.

Pour le spéculaire, nous utilisons moins N dot H.

Cela signifie que pour la lumière de la face arrière, nous inversons simplement le vecteur normal pour obtenir la lumière pour la face arrière.

Maintenant, nous pouvons enregistrer ce fichier.

D'accord, nous avons maintenant terminé la programmation pour la carte de couleurs dans ce projet.

Dans le dernier projet, nous avons discuté du modèle de carte de couleurs.

Dans ce projet, j'expliquerai comment utiliser ce modèle pour construire des surfaces 3D simples.

Voici un exemple d'une surface 3D simple créée à l'aide d'une fonction de pics (peaks function).

Mathématiquement, une surface dessine une fonction Y sur la surface pour chaque coordonnée x et z dans une région d'intérêt.

Pour chaque paire de valeurs x et z, la surface 3D simple peut avoir au plus une valeur Y.

Nous pouvons définir une surface simple par les coordonnées y des points au-dessus d'une grille rectangulaire.

Dans le plan x-z, la surface est formée en joignant des points adjacents à l'aide de lignes droites.

Typiquement, la surface est formée à l'aide de maillages rectangulaires.

Cependant, WebGPU ne fournit que des triangles comme unités de base pour représenter n'importe quelle surface en 3D.

Afin de représenter une surface en utilisant des quadrilatères traditionnels, nous devons écrire nos propres fonctions.

Vous pouvez télécharger le code source utilisé dans ce projet à partir de ce lien de dépôt GitHub.

Cette version de commit spécifique est utilisée pour ce projet.

Maintenant, lancez Visual Studio Code et ouvrez le projet 8 que nous avons construit dans la dernière section.

Voici le code utilisé dans le projet 8.

Tout d'abord, nous devons ajouter un nouveau fichier TypeScript appelé `surface-data.ts` au dossier `src`, dossier `src`.

Ajoutez un nouveau fichier appelé `surface-data.ts`. Nous devons introduire `vec3`, importer `vec3` de la bibliothèque `gl-matrix`, et nous devons également importer du fichier `colormap-data.ts`, introduire la fonction `addColors`.

Tout d'abord, ajoutons une fonction utilitaire appelée `normalize-point` qui sera utilisée pour normaliser le point dans la plage de moins un et un.

Nous devons donc ajouter une fonction de normalisation.

Vous pouvez voir ici que cette fonction prend un `vec3` 3D ici les points.

Plage de données x : X minimum, X maximum, y minimum, y maximum, z minimum, z maximum, et introduisons également un paramètre d'échelle globale, qui vous permet de changer la plage de valeurs pour les coordonnées x, y et z.

Cela sera pratique pour définir la taille par défaut de notre surface.

Cette fonction renvoie le point 3D normalisé.

Pour notre surface 3D simple comme illustré ici, cette surface peut être formée par un maillage de quadrilatères. Voici l'un des quadrilatères.

Ceci, comme illustré ici, est une cellule de grille unitaire.

Cette grille unitaire est un quadrilatère avec 4 sommets P0, p1, p2 et p3.

Nous pouvons diviser ce quadrilatère en deux triangles P0-p1-p2, ce premier triangle, un autre triangle est p2-p3 et P0 comme illustré ici.

Nous créerons des données de sommets, des données de vecteurs normaux et des données de carte de couleurs pour ce quadrilatère.

Maintenant, nous pouvons ajouter une nouvelle fonction appelée `Create_Quad`.

Vous pouvez voir ici que cette fonction prend 4 points exactement comme illustré ici, points 0, 1, 2 et 3.

Elle prend ces 4 points comme arguments d'entrée.

Elle prend également la plage de données de sommets y minimum et y maximum, ainsi que le nom de la carte de couleurs comme paramètres d'entrée, car nous voulons ajouter la carte de couleurs aux valeurs y pour notre surface.

Bien sûr, vous pouvez mapper les données de couleur dans l'autre direction telle que la direction x et z.

Mais nous ajoutons généralement la carte de couleurs aux valeurs y.

ici, nous créons d'abord les données de position des sommets pour les six sommets. C'est le point zéro, le point un, le point deux.

C'est le premier triangle, c'est le deuxième triangle : point 2, point 3, et point zéro.

Voici donc les sommets pour cette cellule unitaire pour ces deux triangles.

Ensuite, nous définissons le vecteur normal pour ce quadrilatère.

Nous avons déjà discuté de la manière d'obtenir le vecteur normal pour ce quadrilatère dans le projet précédent.

Il est simplement égal au produit vectoriel de ces deux lignes diagonales de ce quadrilatère.

Ici, nous introduisons ces deux lignes : la première est p2-p0, p deux p zéro, nous l'appelons CA, une autre ligne est p3 et p1, p trois P un, nous l'appelons DB.

Ensuite, nous obtenons le produit vectoriel, nous l'appelons CP, de ces deux lignes, puis nous normalisons ce produit vectoriel CP, nous obtenons le vecteur normal pour ce quadrilatère.

Ainsi, tous les sommets de ce quadrilatère ont le même vecteur normal.

Ensuite, nous ajoutons les données de la carte de couleurs aux sommets de ce quadrilatère.

Vous pouvez voir les P zéro, p un, P deux et p trois, ce sont les données de la carte de couleurs pour ces 4 sommets.

Pour P zéro, vous pouvez voir que nous lui ajoutons les données de la carte de couleurs en appelant la fonction `addColors` avec sa composante y `p0[1]`, et en utilisant la plage de données y : y minimum et y maximum.

La fonction `addColors` a été implémentée dans le dernier projet.

Si vous voulez ajouter des données de carte de couleurs dans l'autre direction, par exemple la direction x, vous devriez utiliser la plage de données x et également `P zéro` ici à l'intérieur devrait être zéro, c'est la composante x.

De même, nous ajoutons les données de la carte de couleurs aux trois autres sommets.

Et enfin, nous ajoutons les données de la carte de couleurs à ces deux triangles.

Ceux-ci ont six sommets, ils ont une carte de couleurs différente sur différents sommets.

Enfin, la fonction `create-quad` renvoie le sommet, la normale et la couleur pour cette grille unitaire.

Cette fonction `create-quad` ici ne crée que les données pour une seule grille unitaire.

Maintenant, nous devons créer des données pour toute la surface.

Nous devons ajouter une nouvelle fonction appelée `simpleSurfaceData`.

C'est une fonction qui crée les données pour toute la surface.

Cette fonction prend `f` ici cet argument d'entrée.

`F` est une fonction mathématique qui décrit la surface 3D simple.

Nous définissons ensuite la plage de données dans le plan x-z en utilisant une valeur minimale et maximale pour le x et le z.

Ensuite, deux paramètres d'entrée `nx` et `nz` représentent les divisions de la grille le long des directions x et z.

Ici, l'échelle est un paramètre de mise à l'échelle globale utilisé dans la fonction `normalize-point`.

Le paramètre `scale-y` est utilisé pour contrôler la hauteur de la valeur y par rapport aux valeurs X et Z, c'est-à-dire que le paramètre `scale-y` ici contrôle le rapport d'aspect de notre tracé de surface.

À l'intérieur de cette méthode, nous définissons d'abord la taille d'une grille unitaire, vous pouvez voir `dx` et `dz`.

Nous calculons ensuite la position des sommets sur notre surface en appelant la fonction `f`.

Vous pouvez voir que nous utilisons cette boucle `for` à l'intérieur de laquelle nous appelons la fonction `F(X,Z)`.

Ceci décrit notre surface.

Ici, nous calculons également la plage de valeurs y : y minimum 1, y maximum 1.

Ensuite, nous réinitialisons la plage de valeurs y en utilisant le paramètre `scale-y` ici. Ensuite, nous normalisons la position des sommets en appelant le point normalisé en utilisant la plage de valeurs pour X, y et Z, ainsi que l'échelle.

À l'intérieur de cette double boucle `for`, nous définissons d'abord la cellule unitaire P zéro, p un, p deux et p trois.

C'est une cellule unitaire.

Ensuite, appelez la fonction `Create-Quad` pour obtenir la position des sommets, le vecteur normal et les données de carte de couleurs pour cette grille unitaire.

Ainsi, ce sont les sommets, normales et couleurs pour notre surface.

Enfin, cette fonction `simpleSurfaceData` renvoie les données de sommets, les données normales et les données de carte de couleurs.

Nous avons maintenant terminé la programmation pour les surfaces 3D simples dans ce projet.

Dans le prochain projet, nous utiliserons ce cadre pour créer une surface Sinc 3D avec à la fois l'effet d'éclairage et la carte de couleurs.

Dans les deux derniers projets, nous avons discuté du modèle de carte de couleurs et de la construction de surfaces 3D simples.

Dans ce projet, j'expliquerai comment utiliser le modèle de carte de couleurs et la fonction `simpleSurfaceData` pour créer une surface Sinc 3D comme illustré ici.

C'est une jolie surface Sinc que nous voulons créer dans ce projet.

Vous pouvez télécharger le code source utilisé dans ce projet à partir de ce lien de dépôt GitHub.

Cette version de commit spécifique est utilisée pour ce projet.

Maintenant, commencez avec Visual Studio Code et ouvrez notre projet 9 que nous avons construit dans la dernière section.

Voici le code utilisé dans le dernier projet.

Tout d'abord, nous devons apporter quelques modifications au fichier `index.html`. Depuis le dossier `dist`, ouvrez le fichier `index.html`.

Ici, nous devons changer ce titre `h1` en "Sinc surface" et ensuite nous devons changer le paramètre ici.

Vous pouvez voir ici que nous avons le paramètre `two_sided_light` qui contrôle si nous voulons appliquer l'effet d'éclairage à un côté ou aux deux côtés de la surface.

Voici un menu déroulant pour la carte de couleurs qui contient 11 noms de cartes de couleurs que nous avons définis dans le fichier `colormap-data.ts`, vous pouvez donc sélectionner une carte de couleurs différente pour notre surface à partir de ce menu déroulant.

Voici le paramètre d'échelle qui vous permet de définir la taille par défaut et le rapport d'aspect pour la surface Sinc.

Maintenant, nous pouvons enregistrer ce fichier. Maintenant, définissons notre fonction Sinc.

Ajoutez un nouveau fichier TypeScript appelé `math-func.ts` au dossier `src`.

Dossier `src`, ajoutez un nouveau fichier appelé `math-func.ts`.

Voici une définition de la fonction Sinc.

Ici, `r` est défini comme la racine carrée de x au carré plus z au carré.

Cette fonction est égale à `sin(r) / r` si `r` n'est pas égal à zéro.

Sinon, s'il est égal à zéro, cette fonction est égale à un.

En fait, cette fonction est la transformée de Fourier d'une fonction rectangulaire.

Maintenant, nous ajoutons du code ici pour définir cette fonction.

Vous pouvez voir que cette fonction est très simple : elle prend x et z et des paramètres de centre ici comme arguments d'entrée.

Le paramètre de centre ici vous permet de définir l'emplacement de notre surface Sinc.

À l'intérieur de cette fonction, nous définissons `r` en utilisant cette formule comme illustré ici.

Ainsi, ici, si `r` est égal à zéro, cette fonction est égale à un, sinon elle est égale à `sin(r) / r`.

Cette fonction renvoie un point `vec3` sur la surface Sinc ici.

Maintenant, nous pouvons enregistrer ce fichier et le fermer.

Ensuite, nous devons apporter quelques modifications au fichier `main.ts`.

Depuis le dossier `src`, ouvrez le fichier `main.ts` et maintenant nous devons remplacer le code par le nouveau code.

Comme la plupart du code pour le pipeline de rendu et la passe de rendu a déjà été inclus dans le fichier `surface.ts`.

Ainsi, le fichier `main.ts` ici devient très simple. Ici, nous introduisons d'abord `simpleSurfaceData` du fichier `surface-data.ts`, puis nous introduisons la fonction `sinc` du fichier `math-func.ts`.

Ensuite, du fichier `surface.ts`, nous introduisons `createSurfaceWithColormap` et introduisons également l'interface `LightInputs` du fichier `surface.ts`.

Ensuite, nous créons une nouvelle fonction appelée `CreateSurface`.

Cette fonction prend `LightInputs`, `is_animation`, le nom de la carte de couleurs, l'échelle et `scale-y` comme arguments d'entrée.

À l'intérieur de cette fonction, nous appelons `simpleSurfaceData` avec, vous voyez ici, la fonction `sinc` comme argument d'entrée.

À partir de cette méthode `simpleSurfaceData`, nous pouvons obtenir la position des sommets, le vecteur normal et les données de carte de couleurs, nous appelons ensuite la fonction `createSurfaceWithColormap` pour créer notre surface Sinc avec des effets d'éclairage et de carte de couleurs.

Ici, nous définissons les paramètres d'entrée par défaut et ensuite nous appelons la fonction `createSurface` pour créer une surface Sinc 3D avec des effets d'éclairage et de carte de couleurs par défaut.

Cette partie du code permet à l'utilisateur de recréer la surface Sinc avec différents paramètres d'entrée.

Ici, ce code permet à l'utilisateur de sélectionner la carte de couleurs différente dans le menu déroulant.

Maintenant, nous avons terminé la modification du fichier `main.ts`.

D'accord, enregistrez ce fichier.

Maintenant, nous pouvons exécuter la commande suivante dans la fenêtre du terminal pour regrouper notre code TypeScript.

Ouvrez une fenêtre de terminal et exécutez la commande : `npm run prod` pour regrouper notre code TypeScript en mode production, d'accord, le fichier bundle est créé avec succès.

Maintenant, nous pouvons cliquer sur ce lien "Go Live" pour ouvrir Chrome Canary et voir notre surface Sinc.

Cliquez sur ce lien.

D'accord, voici notre surface Sinc avec l'éclairage par défaut des deux côtés et la carte de couleurs jet affichée sur cette page.

Maintenant, vérifions ce qui se passe si nous utilisons l'éclairage d'un seul côté.

Nous utilisons donc le contrôle de la caméra.

C'est un côté et nous le réglons sur zéro.

Vous voyez, vous voyez qu'à l'arrière il n'y a pas de diffusion et de lumière spéculaire à l'arrière.

Mais il n'y a qu'une lumière ambiante très faible ici. Si nous le réglons sur un, vous pouvez voir à l'arrière la différence entre un côté et deux côtés.

Vous avez de la lumière à l'arrière.

Ici, l'échelle définit la taille par défaut de la surface.

Par exemple, nous la changeons en un, vous obtenez une surface plus petite, changez-la en 3, vous obtiendrez une surface plus grande.

Ainsi, ils peuvent contrôler la taille par défaut de la surface.

Nous revenons à 2.

Et ici, le `scale-y` vous permet de contrôler le rapport d'aspect.

Par exemple, nous le réglons sur zéro, vous obtenez une surface plus haute.

Et changez-le en 0,5 vous obtenez une surface plus courte et plus grasse.

Nous le changeons en 0,3, vous pouvez donc utiliser ce paramètre pour contrôler le rapport d'aspect.

Ensuite, nous pouvons changer la carte de couleurs à partir de ce menu déroulant.

Par exemple, autumn, bone, cool, copper, gray, hot, hsv, spring, summer et winter.

Vous pouvez donc obtenir une carte de couleurs différente pour notre surface.

Vous pouvez voir que dans WebGPU, nous pouvons facilement créer une magnifique surface 3D avec des effets d'éclairage et de carte de couleurs.

Vous pouvez créer vos propres surfaces en fournissant simplement vos propres fonctions mathématiques.

Ainsi, nous avons maintenant terminé notre projet 10.

Vous pouvez utiliser WebGPU pour créer des graphismes avancés dans vos applications web.

Voici quelques autres exemples de mon livre récemment publié "Practical WebGPU Graphics". Voici quelques exemples de surfaces 3D paramétriques.

Elles sont toutes magnifiques car elles ont à la fois des effets de carte de couleurs et d'éclairage comme nous l'avons fait pour la surface Sinc 3D simple dans nos projets.

Voici des exemples de mappage de texture sur des objets 3D.

La texture joue un rôle important dans les graphismes 3D.

Les GPU modernes supportent les textures d'image intégrées au niveau matériel.

Le mappage de texture sur un objet 3D offre un aspect plus intéressant et réaliste.

Ces exemples démontrent que vous pouvez effectuer un mappage de texture sur une sphère, un cylindre et une surface 3D.

Vous pouvez également utiliser plusieurs textures sur un objet 3D.

Vous pouvez voir ici : chaque face de notre cube 3D a une texture d'image différente.

Voici des exemples de coloration de domaine pour des fonctions avec des variables complexes.

Ces magnifiques images sont dessinées pixel par pixel sur la base d'un rendu bitmap, ce qui est un processus gourmand en calcul.

Ici, nous effectuons tous les calculs et le rendu directement dans le GPU, ce qui rend possible notre animation en temps réel ici.

C'est impossible en CPU.

Ce sont des exemples de fractales 3D.

Elles offrent plus de structures que les fractales 2D.

Encore une fois, ces jolies images ne peuvent être créées que dans le GPU.

En CPU, c'est trop lent et impossible d'avoir cette animation en temps réel.

Voici quelques exemples pour les grands systèmes de particules.

Ceci est un calcul de boids et nous essayons de simuler le comportement de groupe des oiseaux.

Cette image montre la cinématique des particules avec collision contre le mur.

Ceci montre trois centres de masse qui attirent les particules.

Ici, nous utilisons le Compute shader pour effectuer des calculs liés à la physique et mettre à jour les positions et les vitesses sur chaque image.

Ceci n'est possible que dans le GPU pour simuler ce grand système de particules en temps réel.

Si vous voulez apprendre à créer ces images et ces systèmes de particules, veuillez visiter mon site web à DrXudotnet.com et ma chaîne YouTube à Practical Programming with Dr. Xu. Merci d'avoir regardé."