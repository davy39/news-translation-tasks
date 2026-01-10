---
title: Comment commiter des répertoires entiers sur GitHub directement depuis votre
  navigateur en utilisant GitHub.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-25T17:02:00.000Z'
originalURL: https://freecodecamp.org/news/pushing-a-list-of-files-to-the-github-with-javascript-b724c8c09b66
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ixeHa7nfJp7CPSZ2HjSywg.jpeg
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Comment commiter des répertoires entiers sur GitHub directement depuis
  votre navigateur en utilisant GitHub.js
seo_desc: 'By Illia Kolodiazhnyi

  Did you know you can parse a movie database website, then store its data in your
  own GitHub repository — without ever leaving your browser?

  You can also do things like change a webpage by using your browser’s developer tools,
  th...'
---

Par Illia Kolodiazhnyi

Saviez-vous que vous pouvez analyser un site web de base de données de films, puis stocker ses données dans votre propre dépôt GitHub — sans jamais quitter votre navigateur ?

Vous pouvez également faire des choses comme modifier une page web en utilisant les outils de développement de votre navigateur, puis pousser le code mis à jour sous forme de commit — avec toutes ses images et autres ressources.

[L'API HTTP de GitHub](https://developer.github.com/v3/) vous permet d'utiliser pratiquement toute l'infrastructure de GitHub. Dans la plupart des cas, elle est transparente et facile à comprendre. Mais il y a une chose qui n'est pas si facile à faire au premier abord — faire de beaux commits avec beaucoup de fichiers en même temps, comme le fait la commande `git push` depuis votre terminal.

Mais ne vous inquiétez pas. À la fin de cet article, vous serez en mesure d'utiliser un ensemble d'appels de bas niveau pour y parvenir.

### Installation

Vous allez implémenter une fonction qui prendra les données des fichiers et les poussera avec un commit sur GitHub, comme ceci :

```
pushFiles(    'Faire un commit avec mes fichiers adorables',    [        {content: 'Tu es un sorcier, Harry', path: 'harry.txt'},        {content: 'Que la Force soit avec toi', path: 'jedi.txt'}    ]);
```

Il y a cependant quelques points importants à noter :

* Je vais utiliser la bibliothèque [Github-JS](https://github.com/github-tools/github) pour simplifier les choses. C'est un wrapper pratique autour des appels à l'API.
* Bien qu'il n'y ait qu'une seule fonction pour faire le travail, elle effectuera de nombreuses requêtes en arrière-plan. Cela est dû à la manière dont l'API GitHub est construite — elle doit faire au moins une requête par fichier soumis, puis plusieurs requêtes supplémentaires.
* Le commit de fichiers binaires (comme les images) nécessitera un peu plus de configuration. J'ai une section spéciale ci-dessous qui couvre cela.

### Un algorithme pour réussir

Jetez un œil à la structure interne du dépôt GitHub :

![Image](https://cdn-media-1.freecodecamp.org/images/PnGrG5-SUYb1a9GuuXBSUzFq1jYjroFtZ6mO)
_Exemple de structure de dépôt ([source](https://developer.github.com/v3/git/" rel="noopener" target="_blank" title="))_

Voici une brève explication de son fonctionnement : le pointeur supérieur de chaque branche pointe vers un commit particulier, qui pointe vers un arbre, qui pointe vers une version d'un fichier. Ce sont essentiellement les types d'objets dont vous devez vous soucier : _Commit_, _Tree_ et _Blob_ (contenu d'un fichier).

Chacun contient une chaîne de hachage appelée SHA — il s'agit en fait d'un hachage de somme de contrôle de l'objet. Ainsi, les objets pointent les uns vers les autres en utilisant ces valeurs SHA.

Sur la [page Git Data](https://developer.github.com/v3/git/) de l'API, vous pouvez trouver la description de l'algorithme pour atteindre exactement votre objectif. Mais voici comment cela fonctionne en détail :

1. Récupère le _Commit_ actuel le plus récent et mémorise son SHA. Il sera nécessaire plus tard pour placer un nouveau _Commit_ au-dessus de l'ancien.
2. Récupère le _Tree_ du _Commit_ actuel et mémorise son SHA également. Il sera nécessaire pour créer le nouveau _Tree_ basé sur l'ancien.
3. Crée de nouveaux _Blobs_ pour chacun de vos fichiers, puis sauvegarde leurs SHAs.
4. Crée un nouveau _Tree_ et transmet les informations sur les _Blobs_ créés à l'étape 3 et le SHA de l'ancien _Tree_ récupéré à l'étape 2. Cela créera une relation entre l'ancien _Commit_ et le nouveau.
5. Crée un nouveau _Commit_ en utilisant : le SHA de l'ancien _Commit_ récupéré à l'étape 1, le SHA du _Tree_ créé à l'étape 4, et le message de commit pour le nouveau _Commit_.
6. Enfin, met à jour le pointeur de la branche pour qu'il pointe vers le _Commit_ nouvellement créé.

En dehors de cela, notez qu'il y a également une étape d'authentification, et une étape où GitHub configure le dépôt et la branche vers lesquels vous souhaitez pousser.

Maintenant que vous avez une compréhension conceptuelle de son fonctionnement, plongeons dans la partie amusante — faire les choses avec du code !

### Du code sacré !

Gardons les choses simples et utilisons une fonction wrapper pour stocker la fonctionnalité. Cela expose une référence à une instance de la [bibliothèque wrapper de l'API Github](https://github.com/github-tools/github), et avec elle plusieurs fonctions pour accomplir le travail :

```
function GithubAPI(auth) {    let repo;    let filesToCommit = [];    let currentBranch = {};    let newCommit = {};
```

```
    this.gh = new GitHub(auth);
```

```
    this.setRepo = function() {}    this.setBranch = function() {}    this.pushFiles = function() {}
```

```
    function getCurrentCommitSHA() {}    function getCurrentTreeSHA() {}    function createFiles() {}    function createFile() {}    function createTree() {}    function createCommit() {}    function updateHead() {}};
```

La méthode `setRepo()` transmet simplement les arguments à la bibliothèque sous-jacente et sauvegarde l'objet _Repository_ :

```
this.setRepo = function(userName, repoName) {    repo = this.gh.getRepo(userName, repoName);}
```

La méthode `setBranch()` est un peu plus compliquée en logique :

```
this.setBranch = function(branchName) {    return repo.listBranches()        .then((branches) => {            let branchExists = branches.data                .find( branch => branch.name === branchName );            if (!branchExists) {                return repo.createBranch('master', branchName)                    .then(() => {                        currentBranch.name = branchName;                    });            } else {                currentBranch.name = branchName;            }        });}
```

Ici, vous obtenez toutes les branches du _Repository_ et essayez de trouver celle à laquelle vous souhaitez commiter. Si elle n'est pas trouvée, la nouvelle branche est créée basée sur `master`.

Lorsque vous utilisez la fonction `pushFiles()`, elle passe par toutes les étapes dont nous avons discuté ci-dessus :

```
this.pushFiles = function(message, files) {    return getCurrentCommitSHA()        .then(getCurrentTreeSHA)        .then( () => createFiles(files) )        .then(createTree)        .then( () => createCommit(message) )        .then(updateHead)        .catch((e) => {            console.error(e);        });}
```

Elle utilise une chaîne de Promesses, car chaque étape effectuera une requête réelle à l'API GitHub.

Les étapes 1 et 2 de l'algorithme ne sont pas très intéressantes. Elles appellent simplement des méthodes API et sauvegardent les SHAs du _Commit_ et du _Tree_ actuels :

```
function getCurrentCommitSHA() {    return repo.getRef('heads/' + currentBranch.name)        .then((ref) => {            currentBranch.commitSHA = ref.data.object.sha;        });}
```

```
function getCurrentTreeSHA() {    return repo.getCommit(currentBranch.commitSHA)        .then((commit) => {            currentBranch.treeSHA = commit.data.tree.sha;        });}
```

Maintenant, à l'étape 3, vous devez créer des objets _Blob_ pour chaque fichier :

```
function createFiles(files) {    let promises = [];    let length = filesInfo.length;
```

```
    for (let i = 0; i < length; i++) {        promises.push(createFile(files[i]));    }
```

```
    return Promise.all(promises);}
```

```
function createFile(file) {    return repo.createBlob(file.content)        .then((blob) => {            filesToCommit.push({                sha: blob.data.sha,                path: fileInfo.path,                mode: '100644',                type: 'blob'            });        });}
```

Deux points à noter ici :

1. vous devez attendre que tous les _Blobs_ soient créés — d'où l'expression `Promise.all`
2. le mode de fichier doit être défini sur `100644` pour désigner un fichier simple. GitHub permet [d'autres types](https://developer.github.com/v3/git/trees/#create-a-tree), mais vous n'en avez pas vraiment besoin ici.

Les étapes 4 et 5 concernent la création d'un nouvel _Tree_ avec des fichiers (_Blobs_) et d'un _Commit_ avec ce _Tree_ :

```
function createTree() {    return repo.createTree(filesToCommit, currentBranch.treeSHA)        .then((tree) => {            newCommit.treeSHA = tree.data.sha;        });}
```

```
function createCommit(message) {    return repo.commit(currentBranch.commitSHA, newCommit.treeSHA, message)        .then((commit) => {            newCommit.sha = commit.data.sha;        });}
```

Et la seule chose qui reste est l'étape 6 — mettre à jour la branche pour qu'elle pointe vers le nouveau _Commit_ :

```
function updateHead() {    return repo.updateHead(        'heads/' + currentBranch.name,        newCommit.sha    );}
```

C'est tout ! Maintenant vous pouvez utiliser cette beauté pour pousser vos fichiers :

```
let api = new GithubAPI({token: 'API_TOKEN'});api.setRepo('GITHUB_USER', 'REPOSITORY');api.setBranch('AWESOME_BRANCH')    .then( () => api.pushFiles(        'Faire un commit avec mes fichiers adorables',        [            {content: 'Tu es un sorcier, Harry', path: 'harry.txt'},            {content: 'Que la Force soit avec toi', path: 'jedi.txt'}        ])    )    .then(function() {        console.log('Fichiers commités !');    });
```

Vous pouvez trouver l'implémentation prête à l'emploi résultante dans ce [Gist](https://gist.github.com/iktash/31ccc1d8582bd9dcb15ee468c7326f2d).

### **Et les fichiers binaires ?**

Malheureusement, au moment de la rédaction de cet article (janvier 2017), la bibliothèque utilisée ici en interne échoue à envoyer des données binaires à GitHub.

J'ai créé un [problème](https://github.com/github-tools/github/issues/417) avec eux pour essayer de résoudre le problème. Mais jusqu'à ce qu'il soit réglé, nous devrons trouver une solution de contournement.

Le problème réside dans la fonction `createBlob()`, qui devrait envoyer le contenu au format Base64 avec une structure de requête appropriée. Mais au lieu de cela, la bibliothèque le traite comme une simple chaîne.

La solution de contournement temporaire que j'ai trouvée inclut le fork de la bibliothèque et la modification de [cette ligne](https://github.com/github-tools/github/blob/master/lib/Repository.js#L253) comme suit :

```
if (typeof content === 'object') {    postBody = content;} else {    postBody = this._getContentObject(content);}
```

En gros, vous voulez que la bibliothèque vous permette de spécifier l'objet approprié vous-même.

En utilisant cette version modifiée de la bibliothèque, vous pouvez maintenant pousser des fichiers binaires avec :

```
createBlob({content: base64Content, encoding: 'base64'})
```

où le `base64Content` est généré comme ceci :

```
let fileReader = new FileReader();fileReader.onload = function(e) {    let content = e.target.result;    //supprimer l'en-tête et ne laisser que le contenu Base64 lui-même    base64Content = content.replace(/^(.+,)/, '');}fileReader.readAsDataURL(file);
```

J'admets que c'est un peu bidouillé, mais c'est probablement le moyen le plus facile d'obtenir le comportement nécessaire.

### Maintenant, allez de l'avant et commitez du code

GitHub vous donne la possibilité de travailler avec leur service de manière fluide, et depuis pratiquement n'importe quel environnement. J'espère que cet article a aidé à clarifier certains concepts cruciaux en relation avec l'utilisation de l'API GitHub dans le navigateur en utilisant JavaScript.

Bonne chance à vous tous ! Et faites-moi savoir ce que vous pensez de cela dans les commentaires.