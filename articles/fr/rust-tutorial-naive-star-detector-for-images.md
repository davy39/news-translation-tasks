---
title: Tutoriel Rust – Comment construire un détecteur d'étoiles naïf pour les images
subtitle: ''
author: Anshul Sanghi
co_authors: []
series: null
date: '2024-04-16T19:34:07.000Z'
originalURL: https://freecodecamp.org/news/rust-tutorial-naive-star-detector-for-images
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/cover.jpg
tags:
- name: image processing
  slug: image-processing
- name: Rust
  slug: rust
seo_title: Tutoriel Rust – Comment construire un détecteur d'étoiles naïf pour les
  images
seo_desc: Star detection is a crucial step in many of the processing and analysis
  routines that we perform on astronomical images. It is extremely important for a
  process called plate-solving, which is the process of figuring out which part of
  the sky an image...
---

La détection d'étoiles est une étape cruciale dans de nombreuses routines de traitement et d'analyse que nous effectuons sur les images astronomiques. Elle est extrêmement importante pour un processus appelé "plate-solving", qui consiste à déterminer quelle partie du ciel une image montre, ou vers quelle partie du ciel votre télescope est pointé.

Tous les montages de télescopes modernes peuvent utiliser des logiciels de plate-solving pour déterminer automatiquement où ils sont pointés, et dans quelle direction ils doivent se déplacer pour pointer vers l'emplacement correct.

La détection d'étoiles est parfois également utilisée pour corriger l'effet de l'atmosphère sur la netteté des cibles telles que les galaxies. Elle est également cruciale pour combiner des images astronomiques de plusieurs nuits, télescopes, emplacements, etc., en une seule image de sortie qui a un rapport signal/bruit très élevé.

Avec ce tutoriel, j'aimerais introduire une technique très naïve pour détecter les étoiles dans une image.

### Une note rapide :

La détection d'étoiles est un sujet très complexe, et je n'ai fait qu'effleurer la surface à la fois dans ma propre compréhension et dans cet article.

Les étapes que j'utilise et décris dans cet article sont dérivées de la documentation publique sur des applications réelles existantes (à la fois pour la détection d'étoiles et pour la détection de contours), ainsi que de certains articles de blog de personnes incroyablement compétentes (que je lie à la fin de l'article, assurez-vous de les consulter).

Ainsi, cette implémentation est destinée à des fins d'apprentissage uniquement.

## **Avant de lire**

### **Prérequis pour la première partie du tutoriel**

Le processus décrit s'appuie sur le concept de [traitement multi-échelle des images utilisant une transformation en ondelettes à trous](https://www.freecodecamp.org/news/multi-scale-analysis-of-images-in-rust/). Si vous ne savez pas ce que c'est, je vous encourage à en apprendre davantage à ce sujet en utilisant mon article précédent que je viens de lier, puis à revenir à celui-ci.

Cet article suppose également que vous avez une compréhension de base des [Centroids](https://en.wikipedia.org/wiki/Centroid). Il suffit de savoir ce qu'ils signifient, car vous n'avez pas à les calculer vous-même. Puisque l'article se concentre sur le traitement et l'analyse d'images, une compréhension de base du fonctionnement des pixels en format numérique est utile, mais pas obligatoire.

### **Prérequis pour la deuxième partie de ce tutoriel**

Ici, nous nous concentrons sur l'implémentation de l'algorithme en utilisant le langage de programmation Rust, sans entrer dans les détails du langage lui-même. Il est donc nécessaire d'être à l'aise avec l'écriture de programmes Rust et la lecture de documentations de crates.

Si ce n'est pas votre cas, vous pouvez toujours lire la partie 1 et apprendre la technique, puis peut-être voudrez-vous l'essayer dans un langage de votre choix.

Si vous n'êtes pas familier avec Rust, je vous encourage fortement à apprendre les bases. [Voici un cours interactif sur Rust](https://www.freecodecamp.org/news/rust-in-replit/) qui peut vous aider à commencer.

## Table des matières

1. [Comment fonctionne la détection d'étoiles](#heading-comment-fonctionne-la-detection-detoiles-1)
    1. [Qu'est-ce que la détection d'étoiles ?](#heading-quest-ce-que-la-detection-detoiles)
    2. [Comment fonctionne la détection d'étoiles](#heading-comment-fonctionne-la-detection-detoiles-1)
    3. [Un regard intermédiaire sur le processus](#heading-un-regard-intermediaire-sur-le-processus)
    4. [Décortiquer le processus](#heading-decortiquer-le-processus)
2. [Comment l'implémenter en Rust](#heading-comment-limplementer-en-rust)
    1. [Prérequis](#heading-prerequis)
    2. [Comment lire et décomposer l'image d'entrée](#heading-comment-lire-et-decomposer-limage-dentree)
    3. [Réduction du bruit](#heading-reduction-du-bruit)
    4. [Comment optimiser le seuil et la binarisation](#heading-comment-optimiser-le-seuil-et-la-binarisation)
    5. [Comment construire des polygones autour des étoiles](#heading-comment-construire-des-polygones-autour-des-etoiles)
    6. [Comment détecter la taille et l'emplacement des étoiles en utilisant les contours](#heading-comment-detecter-la-taille-et-lemplacement-des-etoiles-en-utilisant-les-contours)
    7. [Comment encapsuler le processus](#heading-comment-encapsuler-le-processus)
    8. [Comment tester l'implémentation sur des images astronomiques](#heading-comment-tester-limplementation-sur-des-images-astronomiques)
    9. [Comment optimiser le nombre minimum d'étoiles](#heading-comment-optimiser-le-nombre-minimum-detoiles)
    10. [Mais il y a une autre chose...](#heading-mais-il-y-a-une-autre-chose)
3. [Lectures complémentaires](#heading-lectures-complementaires)
4. [Conclusion](#heading-conclusion)

## Comment fonctionne la détection d'étoiles

Puisque ce processus implique de nombreuses étapes, voyons comment il fonctionne, avec un niveau de détail croissant sur ce qui se passe réellement au fur et à mesure. Avec chaque niveau croissant, nous allons déballer la boîte noire bit par bit.

### Qu'est-ce que la détection d'étoiles ?

La détection d'étoiles, dans sa forme la plus simple, implique d'isoler les étoiles du reste de l'image, puis d'effectuer une détection de contours sur celle-ci.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/m42-star-detection-1.jpg)
_1. Image d'entrée_

![Image](https://www.freecodecamp.org/news/content/images/2024/08/level-1-1.jpg)
_2. Étoiles détectées visualisées à l'aide de cercles verts_

### Comment fonctionne la détection d'étoiles

Tout d'abord, vous essayez d'extraire les pixels que vous pensez être des étoiles du reste des pixels de l'image. Cette nouvelle image, qui ne contient que les pixels extraits, est ensuite analysée à l'aide de techniques de détection de contours pour trouver les positions des étoiles dans l'espace 2D.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/m42-star-detection-2.jpg)
_1. Image d'entrée_

![Image](https://www.freecodecamp.org/news/content/images/2024/08/level-1-2-1.jpg)
_2. Pixels extraits qui sont potentiellement des étoiles_

![Image](https://www.freecodecamp.org/news/content/images/2024/08/level-1-1-1.jpg)
_3. Étoiles détectées visualisées à l'aide de cercles verts_

### Un regard intermédiaire sur le processus

Ensuite, vous décomposez votre image d'entrée en plusieurs couches, chaque couche contenant une partie des données originales de sorte que l'addition de toutes les couches vous donne les données originales.

Vous isolez ensuite les couches qui ne contiennent que des structures de petite taille, telles que le bruit et les étoiles, et vous jetez le reste des données.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/layers-of-structure.jpg)
_Différentes couches de structure dans l'image que l'entrée est décomposée. Nous jetons la couche finale et conservons le reste dans cet exemple_

Avec ces données filtrées, vous trouvez les contours dans l'image en utilisant la technique de contouring (qui est expliquée dans la section suivante). Chaque contour vous donne plusieurs "points" dans l'espace 2D. Vous essayez ensuite de dessiner une forme fermée en utilisant les points que vous avez.

Une fois que vous avez fait cela, tout ce dont vous avez besoin est de trouver le centre de cette forme et vous avez l'emplacement des étoiles.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/m42-star-detection-5.jpg)
_1. Image d'entrée_

![Image](https://www.freecodecamp.org/news/content/images/2024/08/level-3-1.jpg)
_2. Image après décomposition en couches et rejet des données à grande échelle_

![Image](https://www.freecodecamp.org/news/content/images/2024/08/level-1-2-2.jpg)
_3. Image après binarisation_

![Image](https://www.freecodecamp.org/news/content/images/2024/08/polygon.jpg)
_4. Contours détectés visualisés à l'aide de contours verts_

![Image](https://www.freecodecamp.org/news/content/images/2024/08/level-1-1-2.jpg)
_5. Étoiles détectées visualisées à l'aide de cercles verts_

### Décortiquer le processus

En utilisant une technique d'analyse multi-échelle facilitée par l'algorithme de transformation en ondelettes à trous, vous décomposez l'image en plusieurs couches, chacune contenant différentes structures mises à l'échelle de l'image originale. Vous prenez les couches contenant des structures de plus petite échelle et vous jetez le reste.

À ces couches, vous appliquez un filtre de débroitage bilatéral pour réduire le bruit afin de vous assurer que vous ne conservez que les étoiles et non le bruit que l'algorithme pourrait prendre pour des étoiles plus tard.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/decomposed-image.jpg)
_Différentes couches de structure dans l'image que l'entrée est décomposée. Nous jetons la couche finale et conservons le reste dans cet exemple._

![Image](https://www.freecodecamp.org/news/content/images/2024/08/m42-star-detection-5-1.jpg)
_1. Image d'entrée_

![Image](https://www.freecodecamp.org/news/content/images/2024/08/level-3-1-1.jpg)
_2. Image après décomposition en couches et rejet des données à grande échelle_

![Image](https://www.freecodecamp.org/news/content/images/2024/08/level-4-1.jpg)
_3. Image avec réduction de bruit_

Une fois que vous avez filtré le bruit, vous binarisez votre image en utilisant un seuil. La binarisation et le seuil consistent à convertir tous les pixels en noir pur ou blanc pur, afin qu'ils soient plus faciles à manipuler. Vous pouvez le faire en sélectionnant une certaine valeur d'intensité, et tous les pixels avec une intensité inférieure à celle-ci deviennent noirs et tous les pixels avec une intensité supérieure à celle-ci deviennent blancs.

Pour trouver la valeur d'intensité optimale pour binariser l'image, vous définissez un nombre minimum d'étoiles que vous vous attendez à trouver dans l'image, ce qui est généralement déterminé en fonction de ce que vous devez réellement faire avec les positions de vos étoiles.

Dans notre exemple, nous commencerons avec un minimum de 500 et nous le pousserons lentement à la limite de l'image échantillon pour voir ce qui se passe.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/level-1-2-3.jpg)
_Binarisation de l'image filtrée par ondelettes et réduite en bruit_

Cela rend le processus de détection de contours (qui est l'étape suivante de notre processus) en utilisant le contouring beaucoup plus fiable.

Le contouring est un terme qui décrit le processus de détermination de l'emplacement des structures dans votre image, et de dessin d'une bordure le long de ces structures – celles-ci sont connues sous le nom de contours.

C'est similaire à la détection de contours, mais la détection de contours vous aide à différencier les pixels voisins individuels, tandis que les contours sont conçus pour travailler avec une frontière complète de toute structure dans une image.

La bibliothèque que nous allons utiliser trouve les contours dans une image en utilisant l'algorithme proposé par Suzuki et Abe : [Analyse structurelle topologique des images binaires numérisées par suivi de bordure](https://www.sciencedirect.com/science/article/abs/pii/0734189X85900167). Le contouring de cette manière vous donnera une collection de points qui se trouvent sur la bordure de chaque contour.

Pour chaque contour qu'il trouve, vous créez un polygone en reliant tous les points de bordure dans ce contour. Si cette forme est une forme ouverte, alors vous extrapolez simplement la bordure finale pour créer un polygone, qui doit être une forme fermée. Vous utilisez ensuite les formules de centroïde sur ce polygone pour trouver le centre de masse de votre forme, ce qui vous donne le centre de votre étoile (dans la plupart des cas).

Vous devez également trouver les distances euclidiennes entre le centre de masse et chaque point de bordure, la plus longue devenant la taille de l'étoile.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/polygon-1.jpg)
_Contouring de l'image binarisée pour trouver des polygones fermés autour des étoiles visualisés ici à l'aide de contours verts_

Une fois que vous avez la taille de votre étoile, vous rejetez toutes les étoiles qui sont soit plus petites qu'1 pixel, soit plus grandes que 24 pixels. Ce sont des suppositions éclairées que j'utilise, et elles semblent me donner les meilleurs résultats pour les images échantillons (mais c'est définitivement un point potentiel d'amélioration).

Après tout cela, vous devriez avoir les coordonnées x et y de l'étoile, ainsi que sa taille en pixels.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/level-1-1-3.jpg)
_Étoiles détectées visualisées à l'aide de cercles verts autour d'elles_

Nous allons nous arrêter là, mais il y a beaucoup plus que vous pouvez faire après cette étape pour supprimer les faux-positifs et corriger le centroïde/taille des étoiles.

## Comment l'implémenter en Rust

Créons un nouveau projet de bibliothèque :

```shell
cargo new --lib stardetect-rs && cd stardetect-rs 
```

### Prérequis

Vous avez besoin de quelques dépendances pour commencer. Ajoutons-les et je vais expliquer pourquoi vous en avez besoin :

```shell
cargo add image imageproc image-dwt geo
```

* `image` est une bibliothèque Rust que nous utiliserons pour travailler avec des images de tous les formats et encodages standard. Elle nous aide également à convertir entre divers formats et fournit un accès facile aux données de pixels sous forme de tampons.
* `imageproc` est une autre bibliothèque des personnes qui ont créé la bibliothèque `image`. C'est une extension pour celle-ci car elle implémente des fonctions et algorithmes de traitement d'images pour la bibliothèque `image`.
* `image-dwt` est ma propre bibliothèque (plug sans vergogne) qui implémente l'algorithme de [décomposition en ondelettes à trous](https://www.freecodecamp.org/news/multi-scale-analysis-of-images-in-rust/) pour le crate `image`. Cela est nécessaire pour décomposer notre image en plusieurs échelles dont j'ai parlé précédemment.
* `geo` est une bibliothèque Rust qui nous permet de travailler facilement avec des types géométriques (comme des points dans l'espace 2D), des formes (telles que des polygones) et des algorithmes implémentés pour eux. Nous utilisons cette bibliothèque pour construire notre polygone basé sur les données de contour, et également pour trouver le centroïde du polygone que j'ai décrit ci-dessus. Elle nous aide également à calculer les distances euclidiennes entre les points, que nous utilisons pour déterminer la taille des étoiles.

### Comment lire et décomposer l'image d'entrée

Vous commencez par lire l'image d'entrée et la décomposer afin de ne conserver que les étoiles (et le bruit).

Vous devez définir une nouvelle structure qui servira d'enveloppe pour votre image d'entrée, et ajouter un constructeur pour créer une instance de cette structure basée sur l'entrée :

```rust
// lib.rs
use image::{DynamicImage, GrayImage};

pub struct StarDetect {
    source: GrayImage,
}

impl From<DynamicImage> for StarDetect {
    fn from(source: DynamicImage) -> Self {
        Self {
            source: source.to_luma8(),
        }
    }
}
```

Vous devez ensuite ajouter la capacité d'extraire les premières couches `n` de la décomposition en ondelettes de votre image :

```rust
// lib.rs

use image_dwt::kernels::LinearInterpolationKernel;
use image_dwt::recompose::{OutputLayer, RecomposableWaveletLayers};
use image_dwt::transform::ATrousTransform;

impl StarDetect {
    fn extract_small_scale_structures(&mut self) {
        let (width, height) = self.source.dimensions();

        // Décomposer l'image en 8 couches
        let filtered_image = ATrousTransform::new(
            &DynamicImage::ImageLuma8(self.source.clone()),
            8,
            LinearInterpolationKernel,
        )
        // Filtrer l'image résiduelle et conserver le reste
        .filter(|item| item.pixel_scale.is_some())
        // Recomposer les 3 premières couches en une image en niveaux de gris.
        .recompose_into_image(width as usize, height as usize, OutputLayer::Grayscale);

        // Mettre à jour l'image source avec laquelle nous allons travailler
        // par la suite.
        self.source = filtered_image.to_luma8();
    }
}
```

### Réduction du bruit

Maintenant que vous avez l'image d'entrée (qui ne devrait contenir que du bruit et des étoiles), débarrassons-nous du bruit :

```rust
// lib.rs

impl StarDetect {
    fn apply_noise_reduction(&mut self) {
        self.source = imageproc::filter::bilateral_filter(&self.source, 10, 10., 3.);
    }
}
```

Ensuite, vous devez déterminer la valeur de seuil optimale pour un nombre minimum donné d'étoiles. Vous la trouvez en choisissant une valeur et en l'optimisant de manière itérative jusqu'à atteindre un nombre d'étoiles supérieur au minimum.

### Comment optimiser le seuil et la binarisation

Commencez par créer un nouveau fichier `threshold.rs` et définissez un trait avec les méthodes nécessaires. Vous avez besoin d'une méthode pour optimiser votre valeur de seuil et d'une autre pour effectuer l'opération de binarisation :

```rust
// threshold.rs

pub(crate) trait ThresholdingExtensions {
    fn optimize_threshold_for_star_count(&self, min_star_count: usize) -> u8;
    fn binarize(&mut self, threshold: u8);
}

```

Implémentons les deux :

```rust
// threshold.rs

use crate::centroid::find_star_centres_and_size;
use crate::StarDetect;

impl ThresholdingExtensions for StarDetect {
    fn optimize_threshold_for_star_count(&self, min_star_count: usize) -> u8 {
        // Nombre actuel d'étoiles
        let mut star_count = 0;

        // Valeur de seuil initiale
        let mut threshold = u8::MAX;

        // Itérer jusqu'à ce que vous ayez trouvé le meilleur seuil
        while star_count < min_star_count {
            // Panique si nous atteignons la valeur d'intensité 0 lors de l'itération.
            // Cela signifie qu'il y a moins d'étoiles que nous l'espérions.
            if threshold == 0 {
                panic!("Nombre maximum d'itérations atteint");
            }

            // Réduire le seuil à 95 % de sa valeur précédente.
            // En utilisant cela, nous vérifions des différences de plus en plus fines
            // de seuil pour chaque itération.
            threshold = (0.95 * threshold as f32) as u8;

            // Cloner les données sources puisque nous devons les modifier
            // sans affecter les données originales.
            let mut source = self.clone();

            // Binariser l'image des données sources en utilisant le seuil actuel
            ThresholdingExtensions::binarize(&mut source, threshold);

            // Trouver le nombre d'étoiles détectées avec le seuil actuel
            star_count = find_star_centres_and_size(&source.source).len();
        }

        threshold
    }

    fn binarize(&mut self, threshold: u8) {
        // Itérer sur chaque pixel dans l'image source
        for pixel in self.source.iter_mut() {
            if *pixel > threshold {
                // Si l'intensité du pixel est supérieure au seuil
                // définissez-la à l'intensité maximale à la place.
                *pixel = u8::MAX;
            } else {
                // Sinon, définissez-la à une intensité de 0.
                *pixel = 0;
            }
        }
    }
}
```

Vous avez peut-être remarqué que nous utilisons la fonction `find_star_centres_and_size` lorsque nous essayons de trouver la valeur de seuil optimisée. Nous y viendrons bientôt, car nous devons déclarer certains types qui conserveront l'état de notre calcul avant d'implémenter la fonction.

Créez un nouveau fichier `centroid.rs`.

Définissez une nouvelle structure qui conservera les coordonnées et la taille de l'étoile :

```rust
// centroid.rs

use imageproc::point::Point;

#[derive(Eq, PartialEq, Copy, Clone, Debug)]
pub struct StarCenter {
    coord: Point<u32>,
    radius: u32,
}

impl StarCenter {
    pub fn coord(&self) -> &Point<u32> {
        &self.coord
    }
    pub fn radius(&self) -> u32 {
        self.radius
    }
}
```

Nous avons également défini des méthodes pour récupérer ces champs. `Point` est un type fourni par le crate `imageproc` pour stocker les coordonnées dans une image.

### Comment construire des polygones autour des étoiles

Nous allons implémenter cette fonction de l'intérieur vers l'extérieur. Nous avons d'abord besoin d'un moyen de construire notre polygone à partir de contours. Implémentons cela :

```rust
// centroid.rs

use geo::LineString;
use imageproc::contours::Contour;

pub(crate) fn construct_closed_polygon(contour: &Contour<u32>) -> LineString<f32> {
    // Créer une nouvelle chaîne de lignes qui relie tous les points
    // dans le contour. Cela peut créer soit une forme ouverte
    // soit une forme fermée.
    let mut line_string = LineString::from_iter(contour.points.iter().map(|point| Coord {
        x: point.x as f32,
        y: point.y as f32,
    }));

    // Si c'est une forme ouverte, fermer la forme pour créer un
    // polygone. Cela ne fait rien sinon.
    line_string.close();

    line_string
}
```

`Contour` est un type fourni par le crate `imageproc`, qui est ce qu'il retourne comme résultat de l'opération de contouring sur une image. Il contient une liste de points qui se trouvent sur la bordure du contour.

`LineString` est un type fourni par `geo` et est défini par eux comme "Une collection ordonnée de deux ou plusieurs [`Coord`](https://docs.rs/geo/latest/geo/geometry/struct.Coord.html)s, représentant un chemin entre des emplacements.". Dans ce cas, nous utilisons ce type pour construire la forme du polygone.

### Comment détecter la taille et l'emplacement des étoiles en utilisant les contours

Ensuite, vous avez besoin d'un moyen de calculer le type `StarCenter` que nous avons déclaré précédemment à partir des données de contour :

```rust
// centroid.rs

use geo::{Centroid, Coord, EuclideanDistance};

pub(crate) fn filter_map_contour_to_star_centers(contour: &Contour<u32>) -> Option<StarCenter> {
    // S'il n'y a pas de points dans le contour
    // ce n'est pas une étoile.
    if contour.points.is_empty() {
        return None;
    }

    if contour.points.len() == 1 {
        // S'il n'y a qu'un seul point dans le contour
        // considérez-le comme étant le centre de l'étoile
        // de taille 1px.
        let center = contour.points.first().unwrap();
        let radius = 1_u32;

        return Some(StarCenter {
            coord: *center,
            radius,
        });
    }

    // Sinon, construisez un polygone autour de l'étoile basé sur
    // les informations de contour.
    let polygon = construct_closed_polygon(contour);

    // Trouvez le centre de gravité de ce polygone (centroïde)
    let center = polygon.centroid().unwrap();

    // Trouvez le rayon de l'étoile basé sur la distance maximale entre
    // le centroïde et l'un des points du contour.
    let radius = polygon.points().fold(0., |distance, point| {
        point.euclidean_distance(&center).max(distance)
    });

    // Si le rayon est inférieur à 1px ou supérieur à 24px
    // nous le rejetons comme non-étoile.
    if !(1. ..=24.).contains(&radius) {
        return None;
    }

    // Construisez le centre de l'étoile basé sur les informations précédemment calculées
    Some(StarCenter {
        coord: Point {
            x: center.x() as u32,
            y: center.y() as u32,
        },
        radius: radius as u32,
    })
}
```

Cette fonction utilise la fonction `construct_closed_polygon` que vous avez définie précédemment pour calculer les centres et tailles finaux des étoiles. Maintenant, la partie facile : implémentons la fonction manquante `find_star_centres_and_size` :

```rust
// centroid.rs

use image::GrayImage;

pub(crate) fn find_star_centres_and_size(image: &GrayImage) -> Vec<StarCenter> {
    // Calculer les contours dans l'image source
    let contours = imageproc::contours::find_contours::<u32>(image);

    contours
        .iter()
        // Itérer sur tous les contours et créer une liste
        // de données de centre et de taille d'étoile.
        .filter_map(filter_map_contour_to_star_centers)
        .collect()
}
```

### Comment encapsuler le processus

Tout ce dont vous avez besoin maintenant est d'implémenter une dernière méthode sur la structure `StarDetect` qui encapsule tout le processus :

```rust
// lib.rs

use crate::centroid::{find_star_centres_and_size, StarCenter};
use crate::threshold::ThresholdingExtensions;

impl StarDetect {
	pub fn find_stars(&mut self, min_stars: usize) -> Vec<StarCenter> {
        self.extract_small_scale_structures();
        self.apply_noise_reduction();

        let threshold = self.optimize_threshold_for_star_count(min_stars);
        self.binarize(threshold);

        find_star_centres_and_size(&self.source)
    }
}
```

Cette méthode n'appelle que les fonctions que nous avons écrites jusqu'à présent. L'utilisateur de votre bibliothèque n'aura besoin d'appeler que cette fonction et rien d'autre.

Vous pouvez maintenant utiliser ce que vous avez créé pour trouver des étoiles dans une image. Pour la suite de cet article, l'image que j'utiliserai pour démontrer est montrée ci-dessous. Si vous souhaitez suivre, vous pouvez télécharger l'image que j'utiliserai à partir d'[ici](https://anshulsanghi-assets.s3.ap-south-1.amazonaws.com/m42-star-detection.jpg).

![Image](https://www.freecodecamp.org/news/content/images/2024/04/m42-star-detection.jpg)
_Nébuleuse d'Orion M42, La Nébuleuse du Cheval Noir, La Nébuleuse de l'Étoile Flamme et le Gaz H-Alpha Environnant_

Comme vous pouvez le remarquer, nous avons une large gamme de formes, tailles et couleurs d'étoiles dans cette image, mais il en va de même pour le bruit et d'autres structures de nébuleuses à grande échelle.

### Comment tester l'implémentation sur des images astronomiques

Créez un nouveau fichier `main.rs` et déclarez-le comme une cible binaire dans le fichier `Cargo.toml`. Il devrait ressembler à ceci :

```toml
[package]
name = "stardetector"
version = "0.1.0"
edition = "2021"

[[bin]]
name = "stardetector"
path = "src/main.rs"

# Voir plus de clés et leurs définitions à https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
geo = "0.28.0"
image = "0.25.1"
image-dwt = "0.3.2"
imageproc = "0.24.0"
```

Vous pouvez enfin utiliser la bibliothèque que nous avons créée pour traiter l'image échantillon. Le code final dans `main.rs` devrait ressembler à ceci :

```rust
use image::Rgba;
use stardetector::StarDetect;

fn main() {
    // Charger l'image en tant que mutable. Vous avez besoin de mutabilité pour que
    // vous puissiez dessiner sur cette image.
    let mut image = image::open("m42-star-detection.jpg").unwrap();

    // Créer une nouvelle instance de détecteur d'étoiles. Vous clonez l'image
    // ici car vous devez également dessiner sur l'image pour
    // des fins de visualisation dans cet exemple.
    let mut star_detector = StarDetect::from(image.clone());

    // Exécuter la fonction de recherche d'étoiles avec un nombre minimum d'étoiles de
    // 500
    let stars = star_detector.find_stars(500);

    // Itérer sur toutes les étoiles que vous avez trouvées
    for star in stars {
        // Dessiner un cercle creux sur l'image pour que vous
        // puissiez voir ce que l'algorithme a trouvé
        imageproc::drawing::draw_hollow_circle_mut(
            &mut image,
            (star.coord().x as i32, star.coord().y as i32),
            // Étendre le rayon de 4px pour qu'il soit plus facile à voir
            // dans la visualisation.
            star.radius() as i32 + 4,
            // Dessiner le cercle avec une couleur verte pure
            Rgba([0, u8::MAX, 0, 1]),
        );
    }

    // Enregistrer l'image avec les positions des étoiles annotées avec
    // des cercles verts.
    image.save("annotated.jpg").unwrap();
}
```

Assurez-vous que l'image téléchargée est présente à la racine de ce dossier de projet.

Nous pouvons enfin exécuter le programme et voir ce qu'il nous donne :

```shell
cargo run --release
```

![Image](https://www.freecodecamp.org/news/content/images/2024/04/annotated.jpg)
_Une partie de la région d'Orion avec les étoiles détectées annotées avec des cercles verts_

Cela semble assez bien ! Si nous zoomons sur une petite partie de l'image :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/annotated-zoomed.jpg)
_Une partie de la région d'Orion avec les étoiles détectées annotées avec des cercles verts_

Nous pouvons voir qu'il y a quelques problèmes mineurs avec l'algorithme, comme des étoiles qui sont très proches les unes des autres et dont les halos se chevauchent sont considérées comme une seule étoile. Le problème est assez intéressant.

Il existe diverses techniques pour résoudre ce problème, mais elles sont hors du cadre de cet article.

### Comment optimiser le nombre minimum d'étoiles

Augmentons le nombre minimum d'étoiles à **1000** et voyons ce qui se passe :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/annotated1.jpg)
_Une partie de la région d'Orion avec les étoiles détectées annotées avec des cercles verts_

![Image](https://www.freecodecamp.org/news/content/images/2024/04/annotated1-zoomed.jpg)
_Une partie de la région d'Orion avec les étoiles détectées annotées avec des cercles verts_

Cette fois, il a détecté beaucoup des étoiles les plus faibles puisque le seuil devait être plus bas pour accommoder le nombre minimum d'étoiles plus élevé.

Il est temps de l'augmenter encore ! Essayons **2000**.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/annotated2.jpg)
_Une partie de la région d'Orion avec les étoiles détectées annotées avec des cercles verts_

![Image](https://www.freecodecamp.org/news/content/images/2024/04/annotated2-zoomed.jpg)
_Une partie de la région d'Orion avec les étoiles détectées annotées avec des cercles verts_

Il a détecté encore plus d'étoiles cette fois, mais il a également commencé à halluciner certaines étoiles là où il n'y en a pas. Cela est causé par un seuil plus bas retenant plus de bruit dans l'image, qui est ensuite détecté comme une étoile. Mais le bruit n'est pas aussi visible dans l'image finale à moins que vous ne regardiez vraiment les pixels, ce qui explique pourquoi il semble que l'algorithme hallucine des étoiles.

**Bruit**, dans cette situation particulière, ne fait pas seulement référence au bruit au sens traditionnel – mais aussi à tout pixel qui n'appartient pas à une étoile pour ce but particulier.

### Mais il y a une autre chose...

Augmentons le nombre minimum d'étoiles au maximum absolu pour cette image particulière, que j'ai trouvé être **3500**.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/annotated3.jpg)
_Une partie de la région d'Orion avec les étoiles détectées annotées avec des cercles verts_

![Image](https://www.freecodecamp.org/news/content/images/2024/04/annotated3-zoomed.jpg)
_Une partie de la région d'Orion avec les étoiles détectées annotées avec des cercles verts_

L'algorithme semble maintenant nous avoir lamentablement échoué, ce qui est attendu lorsque le bruit est trop élevé. Il y a trop de faux-positifs pour que ces données soient utiles.

Je voulais vous montrer cela de toute façon car cela vous montre les défauts de l'algorithme. Cela vous montre également à quoi ressemble la détection d'étoiles sur un signal bruité et pourquoi nous devons pré-traiter une image pour supprimer tout ce qui n'est pas une étoile avant d'exécuter la détection d'étoiles.

Nous allons nous arrêter ici pour l'implémentation, mais il y a de nombreuses ressources que vous pouvez trouver ci-dessous si vous êtes intéressé à en apprendre davantage sur le sujet.

Le code complet pour tout ce dont j'ai parlé aujourd'hui peut être trouvé ici : [https://github.com/anshulsanghi-blog/stardetector](https://github.com/anshulsanghi-blog/stardetector)

## **Lectures complémentaires**

Voici quelques-unes des ressources qui m'ont été très utiles lorsque j'essayais de comprendre comment fonctionne la détection d'étoiles. Les ressources concernent davantage le plate-solving (le processus de détermination des coordonnées exactes dans le ciel nocturne des objets dans une image), mais la détection d'étoiles est une partie cruciale de ce processus.

* [Comment fonctionne le plate-solving astronomique](https://olegignat.com/how-plate-solving-works/) par Oleg Ignat
* [Détection d'étoiles pendant le processus d'alignement d'étoiles dans PixInsight](https://pixinsight.com/doc/tools/StarAlignment/StarAlignment.html#description_002)

Les étoiles ont des caractéristiques assez intéressantes, certaines étant uniques telles que leurs estimations de [fonction d'étalement de point](https://en.wikipedia.org/wiki/Point_spread_function). Ces caractéristiques peuvent être implémentées pour améliorer davantage la détection d'étoiles et le filtrage des faux-positifs.

De plus, j'ai créé une bibliothèque Rust qui implémente cet algorithme, mais avec certaines fonctionnalités supplémentaires déjà, et des processus plus robustes sont en cours.

Des choses comme la gestion correcte des images RVB au lieu de les convertir en niveaux de gris sont déjà implémentées. Elle a également la capacité de travailler avec des images RAW.

Je vais également bientôt travailler sur des améliorations de performance pour celle-ci.

Si vous souhaitez en savoir plus ou contribuer à la bibliothèque, n'hésitez pas à le faire. Le dépôt peut être trouvé ici : [https://github.com/anshap1719/stardetect](https://github.com/anshap1719/stardetect)

## **Conclusion**

J'espère que vous avez apprécié le voyage jusqu'à présent. Si le traitement et l'analyse d'images ou leur implémentation en Rust est quelque chose qui vous intéresse, alors restez à l'écoute pour plus d'articles car ce sont les sujets que j'adore écrire.

De plus, n'hésitez pas à [me contacter](mailto:contact@anshulsanghi.tech) si vous avez des questions ou des opinions sur ce sujet.

### **Appréciez mon travail ?**

Envisagez de m'offrir un café pour soutenir mon travail !

<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="anshulsanghi" data-color="#FFDD00" data-emoji="☕"  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>

Jusqu'à la prochaine fois, bon codage et vous souhaitant des cieux dégagés !