---
title: Comment permettre aux utilisateurs de télécharger des images avec Node/Express,
  Mongoose et Cloudinary
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-23T14:36:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-allow-users-to-upload-images-with-node-express-mongoose-and-cloudinary-84cefbdff1d9
coverImage: https://cdn-media-1.freecodecamp.org/images/0*ETsmhAGOpiWfK06i
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: mongoose
  slug: mongoose
- name: Node.js
  slug: nodejs
- name: technology
  slug: technology
seo_title: Comment permettre aux utilisateurs de télécharger des images avec Node/Express,
  Mongoose et Cloudinary
seo_desc: 'By Glyn Lewington

  Are you building a full-stack app and want to let users upload an image but you’re
  not sure how? In my experience, this is always achieved by having users input a
  link and saving this string to your database. This works great and is...'
---

Par Glyn Lewington

Vous construisez une application full-stack et souhaitez permettre aux utilisateurs de télécharger une image, mais vous n'êtes pas sûr de la méthode à utiliser ? D'après mon expérience, cela est toujours réalisé en faisant entrer un lien par les utilisateurs et en sauvegardant cette chaîne de caractères dans votre base de données. Cela fonctionne très bien et est rapide et facile, mais c'est aussi un peu de la triche. Quelle sorte d'application vous fait d'abord aller sur un autre site et télécharger votre image, puis revenir et la lier ?

Alors, quelle est la solution ?

Permettre à l'utilisateur d'entrer un fichier, puis sur votre serveur, télécharger ce fichier vers un service cloud et sauvegarder cela dans votre base de données. Cloudinary est parfait pour cela. Il est dédié aux téléchargements de médias. Il a une excellente documentation. Il permet des transformations. **Et** il a un énorme plan gratuit (10 Go de stockage). Vous pouvez vous inscrire à [Cloudinary ici](https://cloudinary.com/invites/lpov9zyyucivvxsnalc5/yytj9stwvdsschwyccf8) (je n'obtiens rien pour cela).

### Commençons par le front-end

```html
<form action='/api/images' method="post" enctype="multipart/form-data">
  <input type='file' name='image' />
</form>
```

Cela devrait vous être familier. Tout ce dont vous avez besoin est un formulaire qui soumettra les informations au serveur. L'encodage est requis pour soumettre des fichiers au serveur.

C'est tout pour le front-end.

### Le back-end

Maintenant, le back-end est là où toute la magie opère. Vous aurez besoin de toutes les dépendances habituelles pour travailler avec **Express** et **Mongoose**. En outre, nous utiliserons **Multer**, **Cloudinary**, et **multer-storage-cloudinary**. Multer permettra l'accès aux fichiers soumis via le formulaire. Cloudinary est utilisé pour la configuration et le téléchargement. multer-storage-cloudinary facilitera le processus de combinaison de ces éléments.

```js
const multer = require("multer");
const cloudinary = require("cloudinary");
const cloudinaryStorage = require("multer-storage-cloudinary");
```

Une fois les dépendances requises, vous devez les configurer. Lorsque vous vous inscrivez à Cloudinary, vos identifiants API vous seront fournis. Je recommande de les stocker dans un fichier ".env" pour les garder sécurisés.

Ci-dessous, nous faisons également :

* définir un dossier pour garder toutes les images organisées sur Cloudinary pour ce projet
* garantir que seuls les fichiers "jpg" et "png" sont téléchargés
* ajouter une transformation pour garder la hauteur et la largeur cohérentes et pour gérer la taille du fichier.

Il y a beaucoup plus de choses que vous pouvez faire en matière de transformations — vous pouvez jeter un œil [ici](https://cloudinary.com/documentation/image_transformations) si vous êtes intéressé.

```js
cloudinary.config({
cloud_name: process.env.CLOUD_NAME,
api_key: process.env.API_KEY,
api_secret: process.env.API_SECRET
});
const storage = cloudinaryStorage({
cloudinary: cloudinary,
folder: "demo",
allowedFormats: ["jpg", "png"],
transformation: [{ width: 500, height: 500, crop: "limit" }]
});
const parser = multer({ storage: storage });
```

Maintenant que votre serveur est prêt à recevoir et traiter ces images, nous pouvons passer à la configuration de la route.

Dans votre route post, vous ajoutez simplement le parser que nous avons configuré auparavant comme middleware. Cela prendra le fichier, le téléchargera vers Cloudinary et retournera un objet avec les informations du fichier. Vous pouvez accéder à ces informations dans l'objet de requête.

J'aime extraire uniquement les informations que je veux de cela, pour garder ma base de données organisée. Au minimum, vous voudrez :

* l'URL qui peut être utilisée pour afficher l'image sur le front-end
* le public_id qui vous permettra d'accéder et de supprimer l'image de Cloudinary.

```js
app.post('/api/images', parser.single("image"), (req, res) => {
  console.log(req.file) // pour voir ce qui vous est retourné
  const image = {};
  image.url = req.file.url;
  image.id = req.file.public_id;
  Image.create(image) // sauvegarder les informations de l'image dans la base de données
    .then(newImage => res.json(newImage))
    .catch(err => console.log(err));
});
```

Votre image fera probablement partie d'un objet plus grand dans votre base de données. L'URL de l'image et l'ID peuvent être sauvegardés sous forme de chaînes de caractères dans le cadre de cet objet.

_*Image est un exemple de nom de collection pour votre base de données. Substituez-le par le vôtre._

### Afficher l'image

Lorsque vous souhaitez afficher l'image sur le front-end, effectuez une requête à la base de données, puis utilisez l'URL dans vos balises d'image `<img src=imageURL` />.

J'espère que cela vous aidera à ajouter ce petit extra à vos sites web. Ce n'est pas si difficile une fois que vous décomposez chaque étape du processus. Cela donnera à votre site web une touche professionnelle et le fera ressortir.

Si vous avez des questions, n'hésitez pas à demander dans les commentaires.