---
title: Comment simplifier votre processus de téléchargement de fichiers dans Express.js
  avec Multer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-12T21:05:14.000Z'
originalURL: https://freecodecamp.org/news/simplify-your-file-upload-process-in-express-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/file-stream.png
tags:
- name: Express JS
  slug: express-js
seo_title: Comment simplifier votre processus de téléchargement de fichiers dans Express.js
  avec Multer
seo_desc: "By Kelvin Moses\nFile uploading is a common requirement in web development\
  \ projects. But handling file uploads in Node.js can be complex and time-consuming.\
  \ That's where Multer comes in. \nMulter is a powerful middleware for Node.js that\
  \ simplifies the..."
---

Par Kelvin Moses

Le téléchargement de fichiers est une exigence courante dans les projets de développement web. Mais la gestion des téléchargements de fichiers dans Node.js peut être complexe et chronophage. C'est là que Multer intervient. 

Multer est un middleware puissant pour Node.js qui simplifie le processus de téléchargement de fichiers en gérant les requêtes multipart/form-data. Dans ce tutoriel, vous apprendrez à tirer parti de la puissance de Multer pour simplifier votre processus de téléchargement de fichiers.

### Prérequis

Pour suivre ce tutoriel et implémenter le processus de téléchargement de fichiers en utilisant Multer, vous devez avoir les prérequis suivants :

1. Connaissances de base en JavaScript et Node.js : La familiarité avec JavaScript et Node.js est essentielle pour comprendre les concepts et les exemples de code dans ce tutoriel.
2. Node.js et npm : Assurez-vous d'avoir Node.js et npm (Node Package Manager) installés sur votre machine. Vous pouvez les télécharger et les installer depuis le site officiel de Node.js : [https://nodejs.org](https://nodejs.org).
3. Un éditeur de texte ou un environnement de développement intégré (IDE) : Vous aurez besoin d'un éditeur de texte ou d'un IDE pour écrire et modifier votre code. Les choix populaires incluent Visual Studio Code, Sublime Text, Atom ou WebStorm.
4. Interface de ligne de commande (CLI) : Vous devez être à l'aise avec l'utilisation de la ligne de commande ou du terminal pour exécuter des commandes et naviguer dans la structure de répertoires de votre projet.
5. Compréhension de base du HTML : Ce tutoriel suppose une compréhension de base du HTML pour créer un formulaire HTML pour les téléchargements de fichiers.

En vous assurant que vous avez ces prérequis en place, vous serez prêt à suivre et à implémenter le processus de téléchargement de fichiers en utilisant Multer.

Commençons par la première étape : la configuration de votre projet.

## Étape 1 : Configurer le projet

Commencez par créer un nouveau projet Node.js et initialisez-le avec un fichier package.json :

 ``` bash
$ mkdir multer-tutorial
$ cd multer-tutorial
$ npm init -y
 ```

Ensuite, installez les dépendances nécessaires, y compris Express et Multer :

``` bash
$ npm install express multer
```

## Étape 2 : Créer un serveur Express

Créez un nouveau fichier nommé server.js et configurez un serveur Express de base :

``` javascript
const express = require('express');
const app = express();
const port = 3000;

app.listen(port, () => {
  console.log(`Le serveur est en cours d'exécution sur le port ${port}`);
});
``


## Étape 3 : Configurer le middleware Multer

Dans cette étape, vous allez créer un fichier séparé nommé upload.js pour configurer le middleware Multer. Multer est un middleware pour gérer les requêtes multipart/form-data, spécifiquement conçu pour les téléchargements de fichiers dans Node.js.

Tout d'abord, importez le module **multer** en utilisant **require('multer')**. Cela garantit que vous avez accès à la fonctionnalité de Multer. 

Ensuite, définissez la configuration de stockage pour les fichiers téléchargés en utilisant **multer.diskStorage()**. Cette configuration détermine où les fichiers téléchargés seront stockés sur le serveur. Elle prend un objet avec deux fonctions : **destination** et **filename**.

La fonction destination spécifie le répertoire où les fichiers téléchargés seront enregistrés. Dans cet exemple, nous le définissons sur **'uploads/'**, ce qui signifie que les fichiers seront stockés dans un dossier nommé "uploads" dans le répertoire racine de votre projet. Vous pouvez personnaliser le chemin de destination en fonction de vos besoins.

La fonction filename détermine le nom du fichier téléchargé. Dans cet exemple, nous utilisons **Date.now()** pour générer un timestamp unique pour chaque fichier téléchargé, ce qui aide à prévenir les conflits de noms de fichiers. 

Nous ajoutons le nom original du fichier en utilisant **file.originalname** pour maintenir un certain contexte sur le fichier téléchargé. Vous pouvez modifier cette fonction pour générer des noms de fichiers en fonction de vos besoins spécifiques.

Après avoir configuré la configuration de stockage, vous créez une instance de Multer en appelant **multer({ storage })**, en passant l'objet de configuration **storage**. Cela crée le middleware Multer que vous pouvez utiliser dans votre application Express pour gérer les téléchargements de fichiers.

Enfin, vous exportez l'instance Multer en utilisant **module.exports** afin qu'elle puisse être importée et utilisée dans d'autres parties de votre application, comme dans la route Express pour gérer les téléchargements de fichiers.

En configurant le middleware Multer de cette manière, vous avez configuré la destination de stockage et le nom de fichier pour les fichiers téléchargés, permettant à Multer de gérer les téléchargements de fichiers de manière transparente dans votre application.


``` javascript 
const multer = require('multer');

// Configurer le stockage pour les fichiers téléchargés
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads/');
  },
  filename: (req, file, cb) => {
    cb(null, Date.now() + '-' + file.originalname);
  }
});

// Créer l'instance multer
const upload = multer({ storage: storage });

module.exports = upload;

```

## Étape 4 : Gérer les téléchargements de fichiers dans Express

Dans votre fichier server.js, requérez le fichier upload.js et configurez une route pour les téléchargements de fichiers :

``` javascript
const express = require('express');
const app = express();
const port = 3000;

// Requérez le middleware de téléchargement
const upload = require('./upload');

// Configurez une route pour les téléchargements de fichiers
app.post('/upload', upload.single('file'), (req, res) => {
  // Gérez le fichier téléchargé
  res.json({ message: 'Fichier téléchargé avec succès !' });
});

app.listen(port, () => {
  console.log(`Le serveur est en cours d'exécution sur le port ${port}`);
});
```

## Étape 5 : Créer un formulaire HTML

Dans cette étape, vous allez créer un formulaire HTML qui permet aux utilisateurs de sélectionner et de télécharger un fichier sur votre serveur. Le formulaire sera soumis en utilisant la méthode POST et aura un type d'encodage "multipart/form-data" pour gérer le téléchargement de fichiers :

Pour créer le formulaire HTML, vous utiliserez l'élément **< form >** avec les attributs suivants :

* **action** : Cet attribut spécifie l'URL ou la route où les données du formulaire seront envoyées lorsque le formulaire est soumis. Dans ce cas, vous définirez l'attribut action sur '**/upload**', qui est la route que vous avez créée dans l'étape 4 pour gérer les téléchargements de fichiers.
* **method** : Cet attribut spécifie la méthode HTTP à utiliser lors de la soumission du formulaire. Pour les téléchargements de fichiers, vous devez utiliser la méthode POST, car elle permet d'envoyer de plus grandes quantités de données. Donc, définissez l'attribut method sur "POST".
* **enctype** : Cet attribut spécifie le type de contenu utilisé pour soumettre les données du formulaire. Pour les téléchargements de fichiers, vous devez définir l'attribut enctype sur "multipart/form-data". Ce type d'encodage est nécessaire pour que les navigateurs gèrent correctement les téléchargements de fichiers.
    
À l'intérieur du formulaire, vous ajouterez un élément **< input >** de type "file". Cet élément permet aux utilisateurs de sélectionner un fichier depuis leur machine locale. Donnez à l'élément input un attribut **name** afin qu'il puisse être identifié lorsque le formulaire est soumis. Dans cet exemple, l'attribut name est défini sur "file". Vous pouvez ajuster la valeur de l'attribut name en fonction de vos besoins.
    
Enfin, vous pouvez ajouter d'autres champs de formulaire ou boutons de soumission si nécessaire. Lorsque le formulaire est soumis, le ou les fichiers sélectionnés seront envoyés à la route spécifiée pour le traitement.

En créant ce formulaire HTML, les utilisateurs pourront sélectionner et télécharger des fichiers sur votre serveur en utilisant le champ de saisie fourni.

``` html
<!DOCTYPE html>
<html>
<head>
  <title>Téléchargement de fichier</title>
</head>
<body>
  <h1>Téléchargement de fichier</h1>
  <form action="/upload" method="POST" enctype="multipart/form-data">
    <input type="file" name="file" required>
    <button type="submit">Télécharger</button>
  </form>
</body>
</html>
```

## Étape 6 : Tester votre téléchargement de fichier

Démarrez votre serveur en exécutant node server.js dans le répertoire racine du projet. Ouvrez votre navigateur et accédez à http://localhost:3000. Vous devriez voir un formulaire de téléchargement de fichier. Sélectionnez un fichier et cliquez sur le bouton "Télécharger". Si tout est configuré correctement, vous devriez recevoir une réponse JSON disant "Fichier téléchargé avec succès !".

C'est tout ! Vous avez simplifié avec succès votre processus de téléchargement de fichiers en utilisant Multer. 

Multer offre des fonctionnalités et options supplémentaires pour gérer divers scénarios, tels que le téléchargement de plusieurs fichiers ou la définition de limites de taille de fichiers. Consultez la documentation de Multer pour plus de détails et d'options de personnalisation.

## Conclusion

Dans ce tutoriel, vous avez appris à simplifier votre processus de téléchargement de fichiers en utilisant Multer, un middleware puissant pour Node.js. Avec Multer, vous pouvez gérer les téléchargements de fichiers sans effort en configurant les options de stockage, en gérant les téléchargements de fichiers uniques ou multiples, et en personnalisant divers aspects du processus.

En tirant parti de Multer, vous pouvez améliorer la fonctionnalité de votre application web et gagner du temps et des efforts dans la gestion des téléchargements de fichiers. 

N'oubliez pas d'explorer la documentation de Multer pour des options et fonctionnalités avancées, telles que la validation, la gestion des erreurs et l'intégration avec les services de stockage cloud.

Bon codage !

Restons en contact @ [iam_kelvinjnr](https://twitter.com/iam_kelvinjnr)
Vous pouvez télécharger le code source @ [GitHub](https://github.com/iamkelv/article-file-upload)