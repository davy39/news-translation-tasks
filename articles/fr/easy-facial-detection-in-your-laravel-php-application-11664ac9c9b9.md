---
title: Détection faciale facile dans votre application Laravel PHP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-06T07:54:52.000Z'
originalURL: https://freecodecamp.org/news/easy-facial-detection-in-your-laravel-php-application-11664ac9c9b9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6uFn3v0cRY3xlzbGxUyt0g.jpeg
tags:
- name: Laravel
  slug: laravel
- name: Machine Learning
  slug: machine-learning
- name: PHP
  slug: php
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Détection faciale facile dans votre application Laravel PHP
seo_desc: 'By Darren Chowles

  Detect faces in images using the Google Cloud Vision API


  You’ve probably seen facial detection before. As soon as you upload that family
  photo to Facebook, you’ll notice the boxes around all detected faces. And with facial
  recognit...'
---

Par Darren Chowles

#### Détecter les visages dans les images en utilisant l'API Google Cloud Vision

![Image](https://cdn-media-1.freecodecamp.org/images/VnPML50ueenYtoyQkR3ysp29B8sCZWkEcjVw)

Vous avez probablement déjà vu la détection faciale. Dès que vous téléchargez cette photo de famille sur Facebook, vous remarquerez les cadres autour de tous les visages détectés. Et avec la **reconnaissance** faciale, elle peut même auto-étiqueter le bon ami. Ce n'est pas toujours précis à 100 %, mais c'est toujours une grande ingénierie !

### Applications pour la détection faciale

Dans cet article, nous allons utiliser l'API Google Cloud Vision pour détecter les visages. Nous allons utiliser une image existante et nous allons dessiner un cadre autour de chaque visage détecté.

Il existe plusieurs cas d'utilisation réels pour la détection faciale. Certains d'entre eux incluent :

* détecter si une image téléchargée contient des visages. Cela pourrait être une étape de filtrage dans le cadre d'un processus d'identification "connaître votre client".
* modération d'images pour les applications qui permettent le contenu généré par les utilisateurs.
* la capacité de fournir des étiquettes, de la même manière que les réseaux sociaux.

### Autres fonctionnalités disponibles dans l'API Cloud Vision

La détection faciale n'est qu'une des nombreuses fonctions disponibles dans cette API. Elle prend en charge les fonctionnalités supplémentaires suivantes :

* détection de logos populaires.
* la capacité de détecter toutes les catégories applicables à une image. Par exemple, une photo d'un chat pourrait produire les catégories : chat, mammifère, vertébré et persan.
* détecter des monuments naturels et artificiels populaires.
* extraire du texte à partir d'images.
* exécuter la détection Safe Search pour signaler les images qui contiennent du contenu pour adultes ou de la violence.

### Configuration de la plateforme Google Cloud

La première étape consiste à créer un nouveau projet dans la console Google Cloud Platform.

![Image](https://cdn-media-1.freecodecamp.org/images/kQJQiuCqrMNADYCOMlkELdp3GeTAlQDSklSa)

Rendez-vous sur le tableau de bord et [créez un nouveau projet](https://console.cloud.google.com/projectcreate).

![Image](https://cdn-media-1.freecodecamp.org/images/PHON06KcoAaQASLSaAKClQgTtT7Nc71bplbQ)

Une fois votre projet créé, gardez l'ID du projet à portée de main.

![Image](https://cdn-media-1.freecodecamp.org/images/Jc5LfR6-jxcRwOmVt5nvWURCQVvQYnJ2yNu-)

Suivez ces étapes :

* une fois que vous avez votre projet, allez sur la page [Créer une clé de compte de service](https://console.cloud.google.com/apis/credentials/serviceaccountkey).
* assurez-vous que votre projet de détection faciale est sélectionné en haut.
* sous "Compte de service", sélectionnez "Nouveau compte de service".
* entrez un nom dans "Nom du compte de service".
* sous "Rôle", sélectionnez "Projet" > "Propriétaire".
* Enfin, cliquez sur "Créer" pour télécharger automatiquement le fichier d'identifiants JSON.

![Image](https://cdn-media-1.freecodecamp.org/images/Ty1vbdKD5bpsIwJ1wqTD6mBq13htpDsmYHkj)

Vous devrez peut-être également activer l'API Cloud Vision via la section [Bibliothèque d'API](https://console.developers.google.com/apis/library/vision.googleapis.com).

### Configuration du projet Laravel

L'étape suivante consiste à configurer un nouveau projet Laravel. Si vous avez déjà un projet Laravel, vous pouvez sauter cette étape.

J'utilise Laravel 5.5 LTS pour cet article. Dans la ligne de commande, exécutez la commande Composer suivante pour créer un nouveau projet (vous pouvez également utiliser l'[installeur Laravel](https://laravel.com/docs/5.5#installing-laravel)) :

```
composer create-project --prefer-dist laravel/laravel sample "5.5.*"
```

Si vous avez utilisé Composer, renommez le fichier **.env.example** en **.env** et exécutez la commande suivante pour définir la clé de l'application :

```
php artisan key:generate
```

### Ajouter le package Google cloud-vision

Exécutez la commande suivante pour ajouter le package `google/cloud-vision` à votre projet :

```
composer require google/cloud-vision
```

Vous pouvez placer le fichier d'identifiants JSON téléchargé à la racine de votre application. **Ne** le placez pas dans votre répertoire public. Vous pouvez le renommer. **Ne** commitez pas ce fichier dans votre dépôt de code. Une option consiste à l'ajouter manuellement au serveur.

### Enfin, commençons à coder !

Tout d'abord, assurez-vous d'avoir la bibliothèque [GD](http://php.net/manual/en/image.setup.php) installée et active. La plupart des plateformes ont cela activé par défaut.

J'ajouterai la route suivante à mon fichier "routes/web.php" :

```
Route::get('/', 'SampleController@detectFaces');
```

J'ai créé un contrôleur simple pour héberger le code. J'ajouterai tout le code dans le contrôleur. Dans une application de production, je **recommande fortement** d'utiliser des classes de service séparées pour toute logique métier. Ainsi, les contrôleurs sont légers et respectent leur intention originale : contrôler l'entrée/sortie.

Nous commencerons par un contrôleur simple, en ajoutant une instruction `use` pour inclure la classe `ServiceBuilder` de Google Cloud :

```
<?php
```

```
namespace App\Http\Controllers;
```

```
use Google\Cloud\Core\ServiceBuilder;
```

```
class SampleController extends Controller{    public function detectFaces()    {        // Le code sera ajouté ici    }}
```

La première chose que nous ferons est de créer une instance de la classe `ServiceBuilder` afin que nous puissions spécifier notre ID de projet et nos identifiants JSON.

```
$cloud = new ServiceBuilder([     'keyFilePath' => base_path('fda.json'),     'projectId' => 'facial-detection-app' ]);
```

Vous spécifiez l'emplacement du fichier JSON en utilisant la clé `keyFilePath`. J'ai utilisé l'assistant Laravel [base_path()](https://laravel.com/docs/5.5/helpers#method-base-path) pour faire référence au chemin racine de l'application entièrement qualifié.

L'option suivante est `projectId`. Il s'agit de la valeur que vous avez récupérée lorsque vous avez créé le projet dans la console GCP.

Ensuite, nous créerons une instance de la classe `VisionClient`. La classe `ServiceBuilder` facilite cela en exposant diverses méthodes de fabrique qui accordent l'accès aux services de l'API.

```
$vision = $cloud->vision();
```

Maintenant que nous avons une instance de la classe, nous pouvons commencer à utiliser l'API Vision. Nous utiliserons l'image suivante comme exemple. N'hésitez pas à télécharger cette image, à la nommer "friends.jpg" et à la placer dans votre dossier "public".

![Image](https://cdn-media-1.freecodecamp.org/images/HU1KqsFMeLTJcMXm2sFaV4qiRJGfSNanuQ24)
_Deux filles regardant joyeusement la caméra. par [Unsplash](https://unsplash.com/@matheusferrero?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Matheus Ferrero</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Nous allons d'abord créer une nouvelle image en utilisant la fonction GD `imagecreatefromjpeg()`. Nous utiliserons l'assistant Laravel [public_path()](https://laravel.com/docs/5.5/helpers#method-public-path) pour faire référence à notre image placée dans le dossier "public".

```
$output = imagecreatefromjpeg(public_path('friends.jpg'));
```

Ensuite, nous créerons un objet `Image` Cloud Vision avec cette même image et spécifierons que nous voulons exécuter la détection faciale :

```
$image = $vision->image(file_get_contents(public_path('friends.jpg')), ['FACE_DETECTION']);
```

Vous remarquerez un léger changement ici. Au lieu de fournir le chemin de l'image, nous fournissons l'image réelle sous forme de chaîne en utilisant `file_get_contents()`.

Ensuite, nous exécutons la méthode `annote()` sur l'image :

```
$results = $vision->annotate($image);
```

Maintenant que nous avons les résultats, nous devons simplement parcourir les visages trouvés et dessiner des cadres autour d'eux en utilisant les sommets fournis dans le résultat :

```
foreach ($results->faces() as $face) {    $vertices = $face->boundingPoly()['vertices'];
```

```
    $x1 = $vertices[0]['x'];    $y1 = $vertices[0]['y'];    $x2 = $vertices[2]['x'];    $y2 = $vertices[2]['y'];
```

```
    imagerectangle($output, $x1, $y1, $x2, $y2, 0x00ff00);}
```

Une fois cela fait, nous pouvons sortir l'image et la détruire pour libérer la mémoire :

```
header('Content-Type: image/jpeg'); imagejpeg($output); imagedestroy($output);
```

Et voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/8dLhhJCpCUsq8c6rsXjBNRfvOKvVUkir7d0A)

Voici le code final de la classe contrôleur :

```
<?php
```

```
namespace App\Http\Controllers;
```

```
use Google\Cloud\Core\ServiceBuilder;
```

```
class SampleController extends Controller{    public function detectFaces()    {        $cloud = new ServiceBuilder([            'keyFilePath' => base_path('fda.json'),            'projectId' => 'facial-detection-app'        ]);
```

```
        $vision = $cloud->vision();
```

```
        $output = imagecreatefromjpeg(public_path('friends.jpg'));        $image = $vision->image(file_get_contents(public_path('friends.jpg')), ['FACE_DETECTION']);        $results = $vision->annotate($image);
```

```
        foreach ($results->faces() as $face) {            $vertices = $face->boundingPoly()['vertices'];
```

```
            $x1 = $vertices[0]['x'];            $y1 = $vertices[0]['y'];            $x2 = $vertices[2]['x'];            $y2 = $vertices[2]['y'];
```

```
            imagerectangle($output, $x1, $y1, $x2, $y2, 0x00ff00);        }
```

```
        header('Content-Type: image/jpeg');
```

```
        imagejpeg($output);        imagedestroy($output);    }}
```

### Fonctionnalités supplémentaires

En plus de récupérer les sommets, la réponse inclut également une mine d'informations utiles. Cela inclut les emplacements des bouches, des yeux, des sourcils, des nez, etc. Il suffit d'utiliser `print_r()` sur la variable `$face` pour un aperçu rapide des données disponibles.

Une autre grande fonctionnalité est la vérification si le visage détecté est heureux, triste, en colère ou surpris. Vous pouvez même détecter si le visage est flou ou sous-exposé, et s'ils portent une coiffure.

Si vous utilisez cela et finissez par faire quelque chose de cool, faites-le moi savoir !

### Améliorez vos compétences en développement web !

[Inscrivez-vous à ma newsletter](https://webdev.chowles.com/) où je partagerai des articles perspicaces sur le développement web pour dynamiser vos compétences.

Publié à l'origine sur [www.chowles.com](https://www.chowles.com/easy-facial-detection-in-your-laravel-php-application/) le 6 juillet 2018.