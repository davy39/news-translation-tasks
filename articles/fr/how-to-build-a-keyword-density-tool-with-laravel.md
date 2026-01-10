---
title: Tutoriel PHP Laravel – Comment créer un outil de densité de mots-clés à partir
  de zéro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-28T18:50:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-keyword-density-tool-with-laravel
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/keyword-density-app-with-laravel-banner.jpg
tags:
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
- name: SEO
  slug: seo
seo_title: Tutoriel PHP Laravel – Comment créer un outil de densité de mots-clés à
  partir de zéro
seo_desc: "By Dan Englishby\nHello, freeCodeCamp readers. I hope I can bring you some\
  \ great coding content for inspiration, education and of course, fun! \nIn this\
  \ tutorial, we will learn about keyword density and how to build a tool that can\
  \ calculate keyword de..."
---

Par Dan Englishby

Bonjour, lecteurs de freeCodeCamp. J'espère pouvoir vous apporter du contenu de codage génial pour l'inspiration, l'éducation et bien sûr, le plaisir ! 

Dans ce tutoriel, nous allons apprendre la densité des mots-clés et comment construire un outil qui peut calculer la densité des mots-clés avec Laravel. 

L'outil web nous permettra de coller une page complète de HTML. Ensuite, la magie sera exécutée pour nous donner un score de densité de mots-clés précis.

En résumé rapide, voici quelques compétences de base que nous aborderons lors de la construction de l'outil.

1. Routes, contrôleurs et vues Laravel
2. Mises en page Laravel
3. HTML et formulaires
4. JQuery et Ajax
5. Un peu de PHP natif
6. Un peu de SEO !

## Qu'est-ce que la densité des mots-clés ?

Si vous avez votre propre site web ou blog, vous savez probablement déjà ce qu'est la densité des mots-clés. Pour ceux qui ne savent pas ce que cela signifie, je vais donner une explication courte et simple ci-dessous.

La densité des mots-clés est un calcul des occurrences de mots ou de mots-clés, généralement dans un grand texte. La densité est rapportée en pourcentage, qui est simplement calculé avec la formule suivante.

DensitéMotsClés = (Nombre de mots-clés / Nombre total de mots) * 100

### Pourquoi est-ce important ?

La densité des mots-clés est un facteur clé dans l'algorithme du moteur de recherche Google. Il est largement admis qu'une bonne densité de mots-clés pour optimiser les pages web pour les classements Google est d'environ 3,5 %. Si le pourcentage est plus élevé, par exemple 20 %, cela pourrait être considéré comme du "bourrage de mots-clés" et pourrait donc affecter négativement vos classements dans les recherches Google.

Donc, voici une leçon minuscule sur le SEO et pour vous donner un peu de contexte sur ce que nous essayons de construire. 

## Construire un outil de densité de mots-clés avec Laravel

Ce tutoriel supposera que nous commençons tous avec une nouvelle installation Laravel, permettant à chacun de suivre à partir de n'importe quel point particulier. (Désolé si les premières sections vous disent de sucer des œufs !) 

Aussi, juste pour plus de contexte, je construis cela sur MacOS avec XAMPP en local.

### Prérequis

1. Un environnement PHP installé et accès au répertoire racine
2. Composer installé
3. Votre éditeur de code préféré qui interprète PHP, HTML, CSS et JS.

Avec tous ces prérequis vérifiés, nous pouvons maintenant nous mettre au travail.

## Créer notre application Laravel

Tout d'abord, nous devons télécharger et installer une nouvelle version de Laravel. Suivez les étapes ci-dessous pour y parvenir.

1. Ouvrez votre interface de ligne de commande à la racine de votre serveur web, par exemple XAMPP	/xamppfiles/	htdocs/
2. Exécutez la commande suivante et laissez composer faire sa magie

```
composer create-project --prefer-dist laravel/laravel KeywordDensityApp
```

**Astuce :** Si vous travaillez sur MacOS, consultez les étapes suivantes pour activer les permissions sur le dossier de stockage Laravel.

1. Naviguez vers votre CLI dans le dossier du projet ('KeywordDensityApp') 
2. Exécutez la commande suivante

```
sudo chmod -R 777 storage/*
```

## Ajout d'un contrôleur et d'une vue

Maintenant que nous avons les bases en place, nous pouvons commencer à construire notre contrôleur et notre page web qui permettra à un utilisateur de coller et d'analyser du HTML.

Nous pouvons créer un nouveau contrôleur de deux manières : via l'assistant de ligne de commande PHP artisan ou simplement en le créant avec votre éditeur de code. N'hésitez pas à utiliser l'une des méthodes ci-dessous, assurez-vous simplement que le contrôleur correspond.

### Créer un contrôleur avec PHP artisan

```
php artisan make:controller ToolController
```

### Créer un contrôleur avec l'éditeur de code

1. Localisez le dossier suivant - ProjectFolder/App/Http/Controllers
2. Créez un nouveau fichier .php nommé ToolController

Assurez-vous que ce fichier nouvellement créé contient les éléments suivants :

```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ToolController extends Controller
{
    //
}

```

Maintenant, créons la vue.

### Créer une vue avec l'éditeur de code

1. Localisez le dossier des vues sous ProjectFolder/resources/views
2. Créez un nouveau dossier nommé tool
3. Créez un nouveau fichier PHP de vue nommé index.blade.php

### Créons maintenant un fichier de mise en page

Avec la plupart des applications Laravel, vous voudrez construire un fichier de mise en page afin de ne pas avoir à répéter beaucoup de HTML pour obtenir le même design. 

Cette mise en page est assez basique, utilisant un modèle Bootstrap simple et a un appel @yield à la zone 'content' que nous utiliserons dans nos vues. De plus, il y a un appel @yield à 'scripts' que nous utiliserons plus tard.

1. Localisez le dossier des vues sous ProjectFolder/resources/views
2. Créez un nouveau dossier ici nommé layouts
3. Créez un nouveau fichier nommé master.blade.php
4. Ajoutez le code suivant au fichier

```php
<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Outil de densité de mots-clés</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <!-- Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Nunito:200,600" rel="stylesheet">
    <meta name="csrf-token" content="{{ csrf_token() }}">
<style>
    body {padding-top: 5em;}
</style>
</head>
<body>

<nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
    <a class="navbar-brand" href="#">Application de densité de mots-clés</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarsExampleDefault">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item">
                <a class="nav-link" href="/">Accueil <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item active">
                <a class="nav-link" href="{{route('KDTool')}}">Outil</a>
            </li>
        </ul>

    </div>
</nav>

<main role="main" class="container mt-3">

    @yield('content')

</main><!-- /.container -->

<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
@yield('scripts')
</body>
</html>
```

### Étendre nos vues pour utiliser le fichier de mise en page

Utilisons maintenant le fichier de mise en page nouvellement créé dans notre vue d'accueil et notre vue d'index d'outil. Suivez ces étapes pour étendre la mise en page.

1. Ajoutez le code suivant à la fois dans ProjectFolder/resources/views/welcome.blade.php et ProjectFolder/resources/views/tool/index.blade.php

```php
@extends('layouts.master')

@section('content')
    

@endsection
```

Essayez de rendre la page d'index du répertoire de l'outil, par exemple localhost/tool. Cela devrait ressembler à quelque chose comme ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-221.png)
_Mise en page de la vue de base_

## Relier le contrôleur, la route et la vue

Maintenant que nous avons un contrôleur et une vue, nous devons d'abord définir une route et ensuite ajouter une méthode de retour de vue au contrôleur.

### Définir la route

1. Localisez le fichier des routes web sous ProjectFolder/routes/web.php
2. Ajoutez le code suivant à la fin du fichier :

```php
Route::get('/tool', 'ToolController@index')->name('KDTool');
```

### Créer la nouvelle méthode du contrôleur

Maintenant, retournez à votre ToolController et ajoutez la fonction suivante :

```php
public function index()
{
   return view('tool.index');
}
```

N'hésitez pas à changer les noms des vues, les URLs des routes ou les fonctions des contrôleurs selon vos préférences personnelles. Assurez-vous simplement qu'ils correspondent tous et que la page s'affiche.

## Construire notre vue d'outil

Maintenant, avec notre configuration précédente des vues et des fichiers de mise en page, nous pouvons commencer à ajouter le contenu sous forme de HTML dont nous allons avoir besoin. Il ne consistera en rien de plus que du texte, un formulaire de zone de texte et un bouton de soumission. 

Ajoutez le HTML suivant à la section de contenu du fichier ProjectFolder/resources/views/tool/index.blade.php.

```html
    <form id="keywordDensityInputForm">
        <div class="form-group">
            <label for="keywordDensityInput">HTML ou Texte</label>
            <textarea class="form-control" id="keywordDensityInput" rows="12"></textarea>
        </div>
        <button type="submit" class="btn btn-primary mb-2">Obtenir les densités de mots-clés</button>
    </form>
```

La vue devrait maintenant s'afficher comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-226.png)
_Vue de l'outil de densité de mots-clés avec zone de texte d'entrée_

## Créer le pont entre le front-end et le back-end

Maintenant, nous avons presque tout ce dont nous avons besoin sur le front-end : une simple zone de texte d'entrée où les utilisateurs peuvent coller leur texte brut ou HTML. Ce qui manque, c'est la logique pour lorsque le bouton "Obtenir les densités de mots-clés" est pressé. 

Cette logique de pont fera essentiellement ce qui suit. 

1. Écouter les clics sur le bouton Obtenir la densité de mots-clés
2. Récupérer le contenu de la zone de texte d'entrée non vide
3. Utiliser JQuery Ajax pour envoyer les données au backend pour être traitées et attendre une réponse.
4. Lorsque la réponse est renvoyée, traiter les données et créer un tableau HTML avec les statistiques lisibles par l'homme (densité de mots-clés).

### Front-end

Pour cela, nous utiliserons un script dans la page que nous pouvons injecter en utilisant la balise @section.

Ajoutez ce qui suit à la vue tool/index.blade.php, après la section de contenu.

```php
@section ('scripts')
    <script>
        $('#keywordDensityInputForm').on('submit', function (e) { // Écouter le clic sur le bouton de soumission et la soumission du formulaire.
            e.preventDefault(); // Empêcher le formulaire de se soumettre
            let kdInput = $('#keywordDensityInput').val(); // Obtenir l'entrée
            if (kdInput !== "") { // Si l'entrée n'est pas vide.
			// Configurer le jeton CSRF avec ajax.
                $.ajaxSetup({
                    headers: {
                        'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
                    }
                });

                $.ajax({ // Transmettre les données au backend
                    type: "POST",
                    url: "/tool/calculate-and-get-density",
                    data: {'keywordInput': kdInput},
                    success: function (response) {
                        // En cas de succès, construire un tableau de données avec les mots-clés et les densités
                        if (response.length > 0) {
                            let html = "<table class='table'><tbody><thead>";
                            html += "<th>Mot-clé</th>";
                            html += "<th>Compte</th>";
                            html += "<th>Densité</th>";
                            html += "</thead><tbody>";

                            for (let i = 0; i < response.length; i++) {
                                html += "<tr><td>"+response[i].keyword+"</td>";
                                html += "<td>"+response[i].count+"</td>";
                                html += "<td>"+response[i].density+"%</td></tr>";
                            }

                            html += "</tbody></table>";

                            $('#keywordDensityInputForm').after(html); // Ajouter le tableau html après le formulaire.
                        }
                    },
                });
            }
        })
    </script>
@endsection
```

Ce script entier que nous injectons gérera tous les éléments de la liste numérotée ci-dessus.

Ce qu'il reste à faire, c'est gérer les données arrivant du côté back-end.

### Back-end

Tout d'abord, avant d'aller plus loin avec le codage, nous devons gérer le fait que du texte brut et du HTML peuvent être soumis. Pour cela, nous pouvons utiliser un outil astucieux pour nous aider.

[html2text](https://github.com/mtibben/html2text) est la bibliothèque PHP parfaite pour ce cas d'utilisation, il est donc temps de l'installer. html2text fait exactement ce qu'il dit sur l'étiquette, il convertit le balisage HTML en texte brut. 

Heureusement, ce package dispose d'une commande d'installation composer, alors entrez la commande suivante dans le CLI à la racine du projet.

```cli
composer require html2text/html2text
```

Maintenant, notre contrôleur backend va recevoir soit du HTML, soit du texte brut dans les requêtes provenant du formulaire HTML que nous avons créé dans notre vue. Nous devons maintenant créer la route pour gérer cet appel et router l'appel vers le contrôleur spécifique qui fera la magie.

Ajoutez le PHP suivant au fichier des routes web.php :

```php
Route::post('/tool/calculate-and-get-density', 'ToolController@CalculateAndGetDensity');
```

Deuxièmement, ajoutez ce qui suit au fichier ToolController.php :

```php
    public function CalculateAndGetDensity(Request $request) {
        if ($request->isMethod('GET')) {

          

        }
    }
```

OK, donc le décor est planté. Codons la magie qui calculera la densité des mots-clés et retournera les données.

Tout d'abord, l'instruction use est requise pour le package html2text nouvellement installé. Ajoutez ce qui suit en haut du ToolController.php, juste en dessous des autres instructions use :

```php
use Html2Text\Html2Text;
```

Ensuite, nous devons gérer le paramètre get qui doit être passé, en nous assurant qu'il n'est pas défini, puis en convertissant le paramètre de contenu en texte brut. Refactorisez la fonction CalculateAndGetDensity pour qu'elle ressemble à ce qui suit :

```php
public function CalculateAndGetDensity(Request $request) {
        if ($request->isMethod('GET')) {

            if (isset($request->keywordInput)) { // Tester si le paramètre est défini.
                $html = new Html2Text($request->keywordInput); // Configurer l'objet html2text.
                $text = $html->getText(); // Exécuter la fonction getText().


            }

        }
    }
```

Maintenant que nous avons une variable pour contenir tout le texte dépouillé du paramètre keywordInput, nous pouvons procéder au calcul de la densité.

Nous devons gérer ce qui suit :

1. Déterminer le nombre total de mots
2. Analyser la chaîne textuelle et la convertir en un tableau clé-valeur (la clé étant le mot-clé, la valeur étant l'occurrence du mot)
3. Trier par ordre décroissant avec la plus grande occurrence en premier dans le tableau
4. Parcourir le tableau clé et valeur, en poussant les valeurs vers un nouveau tableau avec un champ supplémentaire de 'densité' qui utilise la formule de densité de mots-clés que nous avons vue plus tôt dans l'article. Cette formule utilisera la valeur (occurrence) et le nombre total de mots.
5. Enfin, retourner les données

Refactorisez la fonction pour qu'elle ressemble à ce qui suit, en tenant compte des commentaires :

```php
public function CalculateAndGetDensity(Request $request) {
        if ($request->isMethod('GET')) {

            if (isset($request->keywordInput)) { // Tester si le paramètre est défini.
                $html = new Html2Text($request->keywordInput); // Configurer l'objet html2text.
                $text = strtolower($html->getText()); // Exécuter la fonction getText() et convertir tout le texte en minuscules pour éviter la duplication des mots
                $totalWordCount = str_word_count($text); // Obtenir le nombre total de mots dans la chaîne de texte
                $wordsAndOccurrence  = array_count_values(str_word_count($text, 1)); // Obtenir chaque mot et le nombre d'occurrences sous forme de tableau clé-valeur
                arsort($wordsAndOccurrence); // Trier par ordre décroissant de la valeur du tableau (occurrence)

                $keywordDensityArray = [];
                // Construire le tableau
                foreach ($wordsAndOccurrence as $key => $value) {
                    $keywordDensityArray[] = ["keyword" => $key, // mot-clé
                        "count" => $value, // occurrences de mots
                        "density" => round(($value / $totalWordCount) * 100,2)]; // Arrondir la densité à deux décimales.
                }

                return $keywordDensityArray;
            }
        }
    }
```

**Note :** La beauté de html2text est qu'il ne se soucie pas vraiment de convertir du HTML ou du texte brut en premier lieu, donc nous n'avons pas à nous soucier si un utilisateur soumet l'un ou l'autre. Il produira toujours du texte brut.

## Mettre à l'épreuve

Enfin, nous sommes prêts à tester l'outil, hourra ! Allez-y et rendez la vue d'index de l'outil (localhost/tool).

1. Maintenant, vous pouvez aller sur n'importe quel site web de votre choix sur le web, charger une page de ce site, faire un clic droit et cliquer sur afficher la source. 
2. Copiez l'intégralité du contenu et revenez à l'outil.
3. Collez le contenu dans la zone de texte et cliquez sur le bouton Obtenir les densités de mots-clés.
4. Attendez la réponse et consultez le tableau des densités de mots-clés !
5. Consultez mon exemple ci-dessous qui utilise le HTML de cette page.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-228.png)
_Outil de densité de mots-clés et tableau des mots-clés_

Et c'est tout !

## Résumé

Dans cet article, nous avons appris comment construire une application Laravel à partir de zéro. Il a abordé certaines des différentes parties de la pile complète en développement telles que JQuery, PHP, HTML, etc. Espérons qu'avec la compréhension de cette application, la même méthodologie pourra être utilisée pour construire autre chose, peut-être plus grand et meilleur. 

### Développements possibles

L'outil de densité de mots-clés prend actuellement en compte les mots "stop". Les mots "stop" sont connus pour être ignorés par les crawlers de Google. Des mots tels que "it", "the", "as", et "a". En regardant la capture d'écran de l'outil ci-dessus, vous pouvez voir qu'ils sont beaucoup utilisés ! 

Un développement supplémentaire pourrait être réalisé pour filtrer les mots "stop" et ne calculer la densité que sur les mots non-stop, ce qui est potentiellement une meilleure vue pour le score SEO.

J'espère que vous avez apprécié cet article ! Si c'est le cas, n'hésitez pas à consulter mon blog, [https://www.codewall.co.uk/](https://www.codewall.co.uk/)

À la prochaine fois !