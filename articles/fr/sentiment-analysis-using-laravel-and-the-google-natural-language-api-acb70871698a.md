---
title: Analyse de sentiment avec Laravel et l'API Google Natural Language
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-13T11:02:55.000Z'
originalURL: https://freecodecamp.org/news/sentiment-analysis-using-laravel-and-the-google-natural-language-api-acb70871698a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TdiVdPnYkvgl3qWnLGgOcg.jpeg
tags:
- name: Laravel
  slug: laravel
- name: nlp
  slug: nlp
- name: PHP
  slug: php
- name: Sentiment analysis
  slug: sentiment-analysis
- name: 'tech '
  slug: tech
seo_title: Analyse de sentiment avec Laravel et l'API Google Natural Language
seo_desc: 'By Darren Chowles

  Write your own sentiment checker in 5 minutes.


  Sentiment Analysis is the process of determining whether a piece of text is positive,
  negative, or neutral.

  Real world applications for Sentiment Analysis

  The goal of this article is t...'
---

Par Darren Chowles

#### Créez votre propre vérificateur de sentiment en 5 minutes.

![Image](https://cdn-media-1.freecodecamp.org/images/W-RZSezYMfrCrFNASW1qeHGAc8tHm8epzb9F)

L'analyse de sentiment est le processus qui consiste à déterminer si un texte est positif, négatif ou neutre.

### Applications réelles de l'analyse de sentiment

Le but de cet article est de vous faire démarrer avec l'API Google Natural Language et Laravel. Vous utiliserez cette API pour effectuer une analyse de sentiment sur du texte.

En utilisant ces techniques, vous pouvez intégrer des fonctionnalités intéressantes dans des applications existantes. Voici quelques idées :

* détecter le sentiment dans les commentaires ou les avis
* prévoir les mouvements du marché en fonction de l'activité sur les réseaux sociaux
* évaluer l'efficacité d'une campagne marketing en observant le sentiment avant et après

### Interprétation des valeurs d'analyse de sentiment

L'API Google prend le texte fourni, l'analyse et détermine l'opinion émotionnelle dominante. Elle détermine si l'écriture est positive, négative ou neutre.

Le sentiment est représenté par des valeurs numériques de **score** et de **magnitude**.

* Le **score** varie entre -1,0 (négatif) et 1,0 (positif).
* La **magnitude** indique la force de l'émotion (à la fois positive et négative). La plage s'étend de 0,0 à l'infini. La **magnitude** n'est pas normalisée, donc les passages de texte plus longs auront toujours une **magnitude** plus grande.

![Image](https://cdn-media-1.freecodecamp.org/images/okN8PYIoQbHRpiBvsV2A1QCDW3rlkUJMyk6H)
_Les valeurs ci-dessus sont des guides uniquement, et vous devrez les ajuster selon votre environnement spécifique._

### Configuration de la plateforme Google Cloud

La première étape consiste à créer un nouveau projet dans la console Google Cloud Platform.

Rendez-vous sur le tableau de bord et [créez un nouveau projet](https://console.cloud.google.com/projectcreate).

![Image](https://cdn-media-1.freecodecamp.org/images/z6371dAtV-MSOkaUJgZaEJvCvlB5pykD3OUq)

Une fois votre projet créé, gardez l'**ID de projet** à portée de main.

![Image](https://cdn-media-1.freecodecamp.org/images/ssGnt0a3bKIaNyCRIwJcbaSD7iaAuKrMUSGP)

* Une fois que vous avez votre projet, allez sur la page [Créer une clé de compte de service](https://console.cloud.google.com/apis/credentials/serviceaccountkey).
* Assurez-vous que votre projet d'exemple est sélectionné en haut.
* Sous **Compte de service**, sélectionnez **Nouveau compte de service**.
* Entrez un nom dans le champ **Nom du compte de service**.
* Sous **Rôle**, sélectionnez **Projet** > **Propriétaire**.
* Enfin, cliquez sur **Créer** pour télécharger automatiquement le fichier d'identifiants JSON.

![Image](https://cdn-media-1.freecodecamp.org/images/IbX4pzWkQIl9XCtFFizscV2S4zRXvQCohCRP)

Vous devrez peut-être également activer l'API Cloud Natural Language via la section [Bibliothèque d'API](https://console.developers.google.com/apis/library/language.googleapis.com).

![Image](https://cdn-media-1.freecodecamp.org/images/ZSc4dpY-9xCA4MM7q7WrYcQV-mFqndbkFEiA)

### Configuration du projet Laravel

L'étape suivante consiste à configurer un nouveau projet Laravel. Si vous avez déjà un projet Laravel existant, vous pouvez sauter cette étape.

J'utilise Laravel 5.5 LTS pour cet article. Dans la ligne de commande, exécutez la commande Composer suivante pour créer un nouveau projet (vous pouvez également utiliser l'[installeur Laravel](https://laravel.com/docs/5.5#installing-laravel)) :

```
composer create-project --prefer-dist laravel/laravel sample "5.5.*"
```

Si vous avez utilisé Composer, renommez le fichier **.env.example** en **.env** et exécutez la commande suivante pour définir la clé de l'application :

```
php artisan key:generate
```

### Ajout du package Google "cloud-language"

Exécutez la commande suivante pour ajouter le package Google Cloud Natural Language à votre projet :

```
composer require google/cloud-language
```

Vous pouvez placer le fichier d'identifiants JSON téléchargé à la racine de votre application (PAS dans votre répertoire public). Vous pouvez le renommer. Ne commitez jamais ce fichier dans votre dépôt de code — cela vaut également pour tout paramètre sensible. Une option consiste à l'ajouter manuellement au serveur après le déploiement initial.

### L'événement principal : ajout du code réel à votre projet

J'ajouterai la route suivante à mon fichier **routes/web.php** :

```
<?php 
```

```
Route::get('/', 'SampleController@sentiment');
```

J'ai créé un contrôleur simple pour héberger le code. J'ajouterai tout le code dans le contrôleur. Dans une application de production, je suggère fortement d'utiliser des classes de service séparées pour toute logique métier. Ainsi, les contrôleurs restent légers et respectent leur intention originale : contrôler l'entrée/sortie.

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
class SampleController extends Controller{    public function sentiment()    {        // Le code sera ajouté ici    }}
```

La première chose que nous ferons est de créer une instance de la classe `ServiceBuilder` afin de pouvoir spécifier notre ID de projet et nos identifiants JSON.

```
$cloud = new ServiceBuilder([    'keyFilePath' => base_path('gc.json'),    'projectId' => 'sample-207012']);
```

Vous spécifiez l'emplacement du fichier JSON en utilisant l'option `keyFilePath`. J'ai utilisé l'aide [base_path()](https://laravel.com/docs/5.5/helpers#method-base-path) de Laravel pour faire référence au chemin racine complet de l'application.

L'option suivante est `projectId`. Il s'agit de la valeur que vous avez récupérée lors de la création du projet dans la console GCP.

Ensuite, nous créerons une instance de la classe `LanguageClient`. La classe `ServiceBuilder` facilite cela en exposant diverses méthodes de fabrique qui donnent accès aux services de l'API.

```
$language = $cloud->language();
```

Maintenant que nous avons une instance de la classe, nous pouvons commencer à utiliser l'API Natural Language. Nous déclarerons une variable avec du texte, analyserons le sentiment et afficherons les résultats :

```
// Le texte à analyser$text = 'I hate this - why did they not make provisions?';
```

```
// Détecter le sentiment du texte$annotation = $language->analyzeSentiment($text);$sentiment = $annotation->sentiment();
```

```
echo 'Score de sentiment : ' . $sentiment['score'] . ', Magnitude : ' . $sentiment['magnitude'];
```

Et c'est tout !

![Image](https://cdn-media-1.freecodecamp.org/images/savaV9K6VqBmJIvC8kMz97tdvMFa4NpX7jRs)
_Sortie pour le code ci-dessus._

Voici le code final de la classe du contrôleur :

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
class SampleController extends Controller{    public function sentiment()    {        $cloud = new ServiceBuilder([            'keyFilePath' => base_path('gc.json'),            'projectId' => 'sample-207012'        ]);
```

```
        $language = $cloud->language();
```

```
        // Le texte à analyser        $text = 'I hate this - why did they not make provisions?';
```

```
        // Détecter le sentiment du texte        $annotation = $language->analyzeSentiment($text);        $sentiment = $annotation->sentiment();
```

```
        echo 'Score de sentiment : ' . $sentiment['score'] . ', Magnitude : ' . $sentiment['magnitude'];    }}
```

### Conclusion

Nous n'avons fait qu'effleurer la surface de ce que l'API Google Natural Language a à offrir. Une fois que vous aurez maîtrisé cela, je vous suggère de consulter les services supplémentaires suivants disponibles dans cette API :

* **Analyse d'entités** : analyser des entités comme des monuments et des figures publiques.
* **Classification de contenu** : analyser du texte et retourner une liste de catégories qui s'appliquent au contenu.

Si vous avez des questions, n'hésitez pas à me contacter !

_Publié à l'origine sur [www.chowles.com](https://www.chowles.com/sentiment-analysis-using-laravel-and-google-natural-language-api/) le 13 juin 2018._