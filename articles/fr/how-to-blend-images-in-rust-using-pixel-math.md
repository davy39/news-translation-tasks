---
title: Comment fusionner des images en Rust à l'aide de l'arithmétique de pixels
subtitle: ''
author: Anshul Sanghi
co_authors: []
series: null
date: '2024-08-27T10:25:56.499Z'
originalURL: https://freecodecamp.org/news/how-to-blend-images-in-rust-using-pixel-math
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1724689572465/f03e4b74-1091-4673-af5b-c8827e74caf0.png
tags:
- name: Rust
  slug: rust
- name: image processing
  slug: image-processing
- name: Mathematics
  slug: mathematics
seo_title: Comment fusionner des images en Rust à l'aide de l'arithmétique de pixels
seo_desc: 'For anyone looking to learn about image processing as a programming niche,
  blending images is a very good place to start. It''s one of the simplest yet most
  rewarding techniques when it comes to image processing.

  To help your intuition, it''s best to i...'
---

Pour quiconque souhaite découvrir le traitement d'image en tant que niche de programmation, la fusion d'images est un excellent point de départ. C'est l'une des techniques les plus simples et pourtant les plus gratifiantes en matière de traitement d'image.

Pour aider votre intuition, il est préférable d'imaginer une image comme un graphique mathématique de valeurs de pixels tracées le long des coordonnées x et y. Le pixel en haut à gauche d'une image est votre origine, ce qui correspond à une valeur x de 0 et une valeur y de 0.

Une fois que vous avez imaginé cela, n'importe quel pixel d'une image peut être lu ou modifié à l'aide de ses coordonnées dans ce graphique x-y. Par exemple, pour une image carrée de taille 5px x 5px, la coordonnée du pixel central est 2, 2. Vous vous attendiez peut-être à ce que ce soit 3, 3, mais les coordonnées d'image dans ce contexte fonctionnent de la même manière que les indices de tableau et commencent à 0 pour les deux axes.

![graphique mathématique avec axes x et y](https://cdn.hashnode.com/res/hashnode/image/upload/v1724421916445/8d27ec1d-43f5-4cc3-b706-b9bd2efb05a4.png align="center")

Aborder le traitement d'image de cette manière vous aide également à traiter chaque pixel individuellement, ce qui rend le processus beaucoup plus simple.

## Prérequis

L'objectif de cet article est de vous faire comprendre et apprendre comment fusionner des images en utilisant le langage de programmation Rust, sans entrer dans les détails du langage ou de sa syntaxe. Il est donc nécessaire d'être à l'aise avec l'écriture de programmes en Rust.

Si vous ne connaissez pas Rust, je vous encourage vivement à en apprendre les bases. [Voici un cours interactif sur Rust qui peut vous aider à démarrer.](https://www.freecodecamp.org/news/rust-in-replit/)

## Table des matières

1. [Introduction](#heading-introduction)
    
2. [Comment fonctionne la fusion d'images](#heading-comment-fonctionne-la-fusion-dimages)
    
3. [Configuration du projet](#heading-configuration-du-projet)
    
4. [Comment lire les valeurs des pixels](#heading-comment-lire-les-valeurs-des-pixels)
    
5. [Comment utiliser les fonctions de fusion](#heading-comment-utiliser-les-fonctions-de-fusion)
    
    1. [Fusion Moyenne](#heading-fusion-moyenne)
        
    2. [Fusion Produit](#heading-fusion-produit)
        
    3. [Fusion Éclaircir](#heading-fusion-eclaircir)
        
    4. [Fusion Obscurcir](#heading-fusion-obscurcir)
        
    5. [Fusion Superposition](#heading-fusion-superposition)
        
    6. [Fusion Addition](#heading-fusion-addition)
        
    7. [Fusion Soustraction](#heading-fusion-soustraction)
        
6. [Comment appliquer les fonctions de fusion aux images](#heading-comment-appliquer-les-fonctions-de-fusion-aux-images)
    
7. [Assemblage final](#heading-assemblage-final)
    
8. [Glossaire](#heading-glossaire)
    

## Introduction

La fusion d'images fait référence à la technique consistant à fusionner les pixels de plusieurs images pour créer une image de sortie unique dérivée de toutes ses entrées. Selon l'opération de fusion utilisée, le résultat de l'image peut varier considérablement pour les mêmes entrées.

Cette technique sert de base à de nombreux outils de traitement d'image complexes, dont certains vous sont peut-être déjà familiers. Des choses comme supprimer des personnes en mouvement des images si vous avez plusieurs clichés, fusionner des images du ciel nocturne pour créer des traînées d'étoiles, et fusionner plusieurs images fortement bruitées pour créer une image à bruit réduit sont tous des exemples de cette technique en action.

Pour réaliser la fusion d'images dans ce tutoriel, nous utiliserons l'"arithmétique de pixels", qui, bien que n'étant pas un terme véritablement standard, fait référence à la technique consistant à effectuer des opérations mathématiques sur un pixel ou un ensemble de pixels pour générer un pixel de sortie.

Par exemple, pour fusionner deux images à l'aide du mode de fusion "moyenne", vous effectuerez l'opération mathématique de moyenne sur tous les pixels d'entrée à un emplacement donné, pour générer la sortie au même emplacement.

L'arithmétique des pixels ne se limite pas aux opérations ponctuelles, qui sont essentiellement des opérations effectuées lors du traitement d'image qui génèrent un pixel de sortie donné basé sur le pixel d'entrée d'une ou plusieurs images au même emplacement dans le système de coordonnées x-y.

D'après mon expérience jusqu'à présent, l'ensemble du domaine du traitement d'image est composé à 99 % de mathématiques et à 1 % de magie noire. Les opérations mathématiques sur les pixels et leurs pixels environnants sont la base des techniques de manipulation d'image telles que la compression, le redimensionnement, le flou et la netteté, la réduction du bruit, et ainsi de suite.

## **Comment fonctionne la fusion d'images**

La technique est techniquement simple à mettre en œuvre. Prenons l'exemple d'une simple fusion moyenne. Voici comment cela fonctionne :

1. Lire les données de pixels des deux images en mémoire, généralement dans un tableau pour chaque image.
    
    * Le tableau est généralement à 2 dimensions. Chaque entrée du tableau est un autre tableau pour les images en couleur, le tableau secondaire contenant les 3 valeurs de pixels correspondant aux canaux de couleur Rouge, Vert et Bleu.
        
2. Pour chaque emplacement de pixel :
    
    1. Pour chaque canal :  
        a. Prendre la valeur du canal de la 2ème image, considérons-la comme `y`.  
        b. Effectuer l'opération de moyenne `x/2 + y/2`.  
        c. Enregistrer la valeur de sortie de cette opération comme valeur du canal de sortie.
        
    2. Enregistrer le résultat de l'opération précédente comme valeur du pixel de sortie.
        
3. Construire l'image de sortie avec les mêmes dimensions à partir des données calculées.
    

Vous remarquerez que l'arithmétique des pixels est effectuée par canal. C'est toujours vrai pour les modes de fusion que nous couvrons dans ce tutoriel, mais de nombreuses techniques impliquent l'application de fusions entre les canaux eux-mêmes et souvent au sein de la même image.

## **Configuration du projet**

Commençons par configurer un projet qui nous donne une bonne base de travail.

```bash
cargo new --bin image-blender
cd image-blender
```

Vous aurez également besoin d'une seule dépendance pour vous aider à effectuer ces opérations :

```bash
cargo add image
```

`image` est une bibliothèque Rust que nous utiliserons pour travailler avec des images de tous les formats et encodages standards. Elle nous aide également à convertir entre différents formats et offre un accès facile aux données de pixels sous forme de tampons (buffers).

Pour plus d'informations sur la caisse (crate) `image`, vous pouvez vous référer à la [documentation officielle](https://docs.rs/image/).

Pour suivre, vous pouvez utiliser deux images de votre choix, la seule exigence étant qu'elles soient de la même taille et dans le même format. Vous pouvez également trouver les images utilisées dans ce tutoriel, ainsi que le code complet, [dans le dépôt GitHub ici](https://github.com/anshulsanghi-blog/blend-images).

## **Comment lire les valeurs des pixels**

La première étape consiste à charger les images et à lire leurs valeurs de pixels dans une structure de données qui facilite notre opération. Pour ce tutoriel, nous allons utiliser un `Vec` de tableaux (`Vec<[u8; 3]>`). Chaque entrée dans le `Vec` externe représente un pixel, et les valeurs par canal de chaque pixel sont stockées dans un tableau `[u8; 3]`.

Commençons par créer un nouveau fichier pour contenir ce code appelé **io.rs**.

```rust
// src/io.rs

use image::GenericImageView;

pub struct SourceData {
    pub width: usize,
    pub height: usize,
    pub image1: Vec<[u8; 3]>,
    pub image2: Vec<[u8; 3]>,
}

pub fn read_pixel_data(image1_path: String, image2_path: String) -> SourceData {
    // Ouvrir les images
    let image1 = image::open(image1_path).unwrap();
    let image2 = image::open(image2_path).unwrap();

    // Calculer les dimensions de l'image
    let (width, height) = image1.dimensions();
    let (width, height) = (width as usize, height as usize);

    // Créer des tableaux pour stocker les données de pixels d'entrée
    let mut image1_data: Vec<[u8; 3]> = vec![[0, 0, 0]; width * height];
    let mut image2_data: Vec<[u8; 3]> = vec![[0, 0, 0]; width * height];

    // Itérer sur tous les pixels de l'image d'entrée, ainsi que leurs positions dans les
    // coordonnées x et y.
    for (x, y, pixel) in image1.to_rgb8().enumerate_pixels() {
        // Calculer les valeurs brutes de chaque canal dans le pixel RGB.
        let [r, g, b] = pixel.0;

        // Calculer l'index linéaire basé sur l'index 2D. Il s'agit essentiellement de calculer l'index dans un
        // tableau 1D basé sur l'index de ligne et de colonne du pixel dans l'image 2D.
        let index = (y * (width as u32) + x) as usize;

        // Sauvegarder les valeurs par canal dans l'index correct des tableaux de données.
        image1_data[index] = [r, g, b];
    }

    // Itérer sur tous les pixels de l'image d'entrée, ainsi que leurs positions dans les
    // coordonnées x et y.
    for (x, y, pixel) in image2.to_rgb8().enumerate_pixels() {
        // Calculer les valeurs brutes de chaque canal dans le pixel RGB.
        let [r, g, b] = pixel.0;

        // Calculer l'index linéaire basé sur l'index 2D. Il s'agit essentiellement de calculer l'index dans un
        // tableau 1D basé sur l'index de ligne et de colonne du pixel dans l'image 2D.
        let index = (y * (width as u32) + x) as usize;

        // Sauvegarder les valeurs par canal dans l'index correct des tableaux de données.
        image2_data[index] = [r, g, b];
    }

    SourceData {
        width,
        height,
        image1: image1_data,
        image2: image2_data,
    }
}
```

## Comment utiliser les fonctions de fusion

L'étape suivante consiste à implémenter les fonctions de fusion, qui sont des fonctions pures prenant deux valeurs de pixels en entrée et renvoyant la valeur de sortie. Ceci est implémenté via le trait `BlendOperation` défini ci-dessous. Créons un nouveau fichier pour héberger toutes les opérations appelé **operations.rs**.

```rust
// src/operations.rs

pub trait BlendOperation {
    fn perform_operation(&self, pixel1: [u8; 3], pixel2: [u8; 3]) -> [u8; 3];
}
```

Ensuite, nous devons implémenter ce trait pour toutes les méthodes de fusion que nous voulons supporter.

Pour illustrer le résultat de chacun des modes de fusion, les deux images d'entrée suivantes sont fusionnées ensemble :

![Image source 1 : Lucioles dans une zone de forêt sombre](https://cdn.hashnode.com/res/hashnode/image/upload/v1724236939605/77d32c76-abf6-4d24-bba7-df40729863b8.jpeg align="center")

![Image source 2 : Lucioles dans une zone de forêt lumineuse](https://cdn.hashnode.com/res/hashnode/image/upload/v1724428339241/3cc70fd2-f6da-4704-8606-97c094a2ff35.jpeg align="center")

### Fusion Moyenne

Une fusion moyenne implique de faire la moyenne par canal des valeurs de pixels d'entrée pour obtenir le pixel de sortie.

```rust
// src/operations.rs

pub struct AverageBlend;

impl BlendOperation for AverageBlend {
    fn perform_operation(&self, pixel1: [u8; 3], pixel2: [u8; 3]) -> [u8; 3] {
        [
            pixel1[0] / 2 + pixel2[0] / 2,
            pixel1[1] / 2 + pixel2[1] / 2,
            pixel1[2] / 2 + pixel2[2] / 2,
        ]
    }
}
```

![Résultat de la fusion moyenne des images sources](https://cdn.hashnode.com/res/hashnode/image/upload/v1724236691772/291f14f4-2019-4771-8cd2-b9f9b3cf3f86.jpeg align="center")

### Fusion Produit

Une fusion produit (multiply) implique une multiplication par canal des valeurs de pixels d'entrée après qu'elles ont été normalisées[\[¹\]](#heading-glossaire) pour obtenir le pixel de sortie. Le pixel de sortie est ensuite remis à l'échelle vers la plage d'origine en le multipliant par 255.

```rust
// src/operations.rs

pub struct MultiplyBlend;

impl BlendOperation for MultiplyBlend {
    fn perform_operation(&self, pixel1: [u8; 3], pixel2: [u8; 3]) -> [u8; 3] {
        [
            ((pixel1[0] as f32 / 255. * pixel2[0] as f32 / 255.) * 255.) as u8,
            ((pixel1[1] as f32 / 255. * pixel2[1] as f32 / 255.) * 255.) as u8,
            ((pixel1[2] as f32 / 255. * pixel2[2] as f32 / 255.) * 255.) as u8,
        ]
    }
}
```

![Résultat de la fusion produit des images sources](https://cdn.hashnode.com/res/hashnode/image/upload/v1724236703622/9aff3ffd-9a63-4b76-9675-d7db4ccee89b.jpeg align="center")

### Fusion Éclaircir

La fusion Éclaircir (Lighten) implique une comparaison par canal des valeurs de pixels d'entrée, en sélectionnant le pixel ayant la valeur la plus élevée (intensité) comme pixel de sortie.

```rust
// src/operations.rs

pub struct LightenBlend;

impl BlendOperation for LightenBlend {
    fn perform_operation(&self, pixel1: [u8; 3], pixel2: [u8; 3]) -> [u8; 3] {
        [
            pixel1[0].max(pixel2[0]),
            pixel1[1].max(pixel2[1]),
            pixel1[2].max(pixel2[2]),
        ]
    }
}
```

![Résultat de la fusion éclaircir des images sources](https://cdn.hashnode.com/res/hashnode/image/upload/v1724236726111/5d1607fb-2740-46b8-906d-1ffb482a0561.jpeg align="center")

### Fusion Obscurcir

La fusion Obscurcir (Darken) est l'opération inverse de la fusion éclaircir. Elle implique une comparaison par canal des valeurs de pixels d'entrée, en sélectionnant le pixel ayant la valeur la plus faible (intensité) comme pixel de sortie.

```rust
// src/operations.rs

pub struct DarkenBlend;

impl BlendOperation for DarkenBlend {
    fn perform_operation(&self, pixel1: [u8; 3], pixel2: [u8; 3]) -> [u8; 3] {
        [
            pixel1[0].min(pixel2[0]),
            pixel1[1].min(pixel2[1]),
            pixel1[2].min(pixel2[2]),
        ]
    }
}
```

![Résultat de la fusion obscurcir des images sources](https://cdn.hashnode.com/res/hashnode/image/upload/v1724236746972/18307fa1-1a77-4d39-b233-a7a6d87233d0.jpeg align="center")

### Fusion Superposition

La fusion Superposition (Screen) consiste à multiplier l'inverse de deux images, puis à inverser le résultat. Dans notre implémentation, les pixels doivent d'abord être normalisés[\[¹\]](#heading-glossaire). Les valeurs normalisées[\[¹\]](#heading-glossaire) sont ensuite inversées en les soustrayant de 1, puis multipliées et inversées à nouveau.

Enfin, le résultat est multiplié par 255 pour dé-normaliser la valeur du pixel de sortie.

```rust
// src/operations.rs

pub struct ScreenBlend;

impl BlendOperation for ScreenBlend {
    fn perform_operation(&self, pixel1: [u8; 3], pixel2: [u8; 3]) -> [u8; 3] {
        [
            ((1. - ((1. - (pixel1[0] as f32 / 255.)) * (1. - (pixel2[0] as f32 / 255.)))) * u8::MAX as f32) as u8,
            ((1. - ((1. - (pixel1[1] as f32 / 255.)) * (1. - (pixel2[1] as f32 / 255.)))) * u8::MAX as f32) as u8,
            ((1. - ((1. - (pixel1[2] as f32 / 255.)) * (1. - (pixel2[2] as f32 / 255.)))) * u8::MAX as f32) as u8,
        ]
    }
}
```

![Résultat de la fusion superposition des images sources](https://cdn.hashnode.com/res/hashnode/image/upload/v1724236758380/fd531b6e-729c-4db4-987e-f503478ff950.jpeg align="center")

### Fusion Addition

La fusion Addition consiste à additionner les valeurs d'entrée, puis à limiter (clamper) le résultat à la plage maximale de la profondeur de couleur ciblée. Dans ce cas, ce serait 0-255 car nous ciblons une profondeur de couleur de 8 bits.

Nous devons également convertir les valeurs en u16 afin d'éviter toute perte de valeur due à un dépassement de capacité (overflow). Nous pouvons également utiliser des valeurs normalisées[\[¹\]](#heading-glossaire) ici pour obtenir le même résultat.

```rust
// src/operations.rs

pub struct AdditionBlend;

impl BlendOperation for AdditionBlend {
    fn perform_operation(&self, pixel1: [u8; 3], pixel2: [u8; 3]) -> [u8; 3] {
        [
            (pixel1[0] as u16 + pixel2[0] as u16).clamp(0, u8::MAX as u16) as u8,
            (pixel1[1] as u16 + pixel2[1] as u16).clamp(0, u8::MAX as u16) as u8,
            (pixel1[2] as u16 + pixel2[2] as u16).clamp(0, u8::MAX as u16) as u8,
        ]
    }
}
```

![Résultat de la fusion addition des images sources](https://cdn.hashnode.com/res/hashnode/image/upload/v1724236766684/05f01177-024d-4196-a9fa-5274bb56a0f4.jpeg align="center")

### Fusion Soustraction

La fusion Soustraction consiste à soustraire les valeurs d'entrée, puis à limiter (clamper) le résultat à la plage maximale de la profondeur de couleur ciblée. Dans ce cas, ce serait 0-255 car nous ciblons une profondeur de couleur de 8 bits.

Nous convertissons également les valeurs en i16 afin d'éviter toute perte de valeur due à un dépassement de capacité ou à l'absence de signe. Nous pouvons également utiliser des valeurs normalisées[\[¹\]](#heading-glossaire) ici pour obtenir le même résultat.

```rust
// src/operations.rs

pub struct SubtractionBlend;

impl BlendOperation for SubtractionBlend {
    fn perform_operation(&self, pixel1: [u8; 3], pixel2: [u8; 3]) -> [u8; 3] {
        [
            (pixel1[0] as i16 - pixel2[0] as i16).clamp(0, u8::MAX as i16) as u8,
            (pixel1[1] as i16 - pixel2[1] as i16).clamp(0, u8::MAX as i16) as u8,
            (pixel1[2] as i16 - pixel2[2] as i16).clamp(0, u8::MAX as i16) as u8,
        ]
    }
}
```

![Résultat de la fusion soustraction des images sources](https://cdn.hashnode.com/res/hashnode/image/upload/v1724236775603/507ba176-579d-494f-bb56-25a27ed2317f.jpeg align="center")

## Comment appliquer les fonctions de fusion aux images

La dernière étape consiste à utiliser réellement les opérations de fusion que nous avons créées précédemment et à les appliquer à des paires d'images.

Pour y parvenir, nous avons besoin d'une fonction capable de prendre le type `SourceData` que nous avons défini précédemment en entrée, ainsi qu'une opération de fusion comme arguments, et de nous donner le tampon de sortie final. Commençons par créer un nouveau fichier pour cela appelé **blend.rs**.

```rust
// src/blend.rs

use image::{ImageBuffer, Rgb};
use crate::{operations::BlendOperation, SourceData};

impl SourceData {
    pub fn blend_images(&self, operation: impl BlendOperation)  -> ImageBuffer<Rgb<u8>, Vec<u8>> {
        let SourceData {
            width,
            height,
            image1,
            image2,
        } = self;

        // Créer un nouveau tampon de la même taille que les images d'entrée, qui servira de données de sortie
        let mut buffer = ImageBuffer::new(*width as u32, *height as u32);

        // Itérer sur tous les pixels du tampon de sortie, ainsi que leurs coordonnées
        for (x, y, output_pixel) in buffer.enumerate_pixels_mut() {
            // Calculer l'index linéaire à partir des coordonnées x et y. En d'autres termes, vous avez ici les
            // index de ligne et de colonne, et vous voulez calculer l'index du tableau basé sur ces deux positions.
            let index = (y * *width as u32 + x) as usize;

            // Stocker les valeurs de pixels à la position donnée dans des variables
            let pixel1 = image1[index];
            let pixel2 = image2[index];

            // Calculer le pixel fusionné et le convertir en type `Rgb`, qui est ensuite
            // assigné au pixel de sortie dans le tampon.
            *output_pixel = Rgb::from(operation.perform_operation(pixel1, pixel2));
        }

        buffer
    }
}
```

### Assemblage final

Il est maintenant temps d'utiliser tout ce que vous avez appris jusqu'à présent et de tout rassembler dans le fichier **main.rs**.

```rust
// src/main.rs

mod blend;
mod io;
mod operations;

use io::*;
use operations::{
    AdditionBlend, AverageBlend, DarkenBlend, LightenBlend, MultiplyBlend, ScreenBlend,
    SubtractionBlend,
};

fn main() {
    let source_data = read_pixel_data("image1.jpg".to_string(), "image2.jpg".to_string());

    let output_buffer = source_data.blend_images(AdditionBlend);
    output_buffer.save("addition.jpg").unwrap();

    let output_buffer = source_data.blend_images(AverageBlend);
    output_buffer.save("average.jpg").unwrap();

    let output_buffer = source_data.blend_images(DarkenBlend);
    output_buffer.save("darken.jpg").unwrap();

    let output_buffer = source_data.blend_images(LightenBlend);
    output_buffer.save("lighten.jpg").unwrap();

    let output_buffer = source_data.blend_images(MultiplyBlend);
    output_buffer.save("multiply.jpg").unwrap();

    let output_buffer = source_data.blend_images(ScreenBlend);
    output_buffer.save("screen.jpg").unwrap();

    let output_buffer = source_data.blend_images(SubtractionBlend);
    output_buffer.save("subtraction.jpg").unwrap();
}
```

Vous pouvez maintenant exécuter le programme à l'aide de la commande suivante, et toutes les images devraient être générées et enregistrées dans le dossier du projet :

```bash
cargo run --release
```

Comme vous l'avez peut-être déjà deviné, cette implémentation ne fonctionne que pour les images RGB 8 bits. Ce code peut toutefois être étendu très facilement pour prendre en charge d'autres formats de couleur tels que le Luma 8 bits (Monochrome), le RGB 16 bits (nombreuses images d'appareils photo RAW), et ainsi de suite.

Je vous encourage vivement à essayer cela. Vous pouvez également me contacter pour obtenir de l'aide sur n'importe quel point de ce tutoriel ou pour étendre le code. Je serais ravi de répondre à toutes vos questions. L'e-mail est le meilleur moyen de me joindre, vous pouvez m'écrire à [anshul@anshulsanghi.tech](mailto:anshul@anshulsanghi.tech).

### Glossaire

La normalisation fait référence au processus de remise à l'échelle des valeurs de pixels afin que les valeurs soient au format virgule flottante et comprises entre 0 et 1. Par exemple, pour une image 8 bits, la couleur noire est représentée par 0 (0 en valeur dé-normalisée) et la couleur blanche est représentée par 1 (255 en valeur dé-normalisée). Les valeurs décimales intermédiaires entre 0 et 1 représentent différentes intensités du pixel entre le noir et le blanc. La normalisation est effectuée pour de nombreuses raisons différentes, telles que :

* Prévenir les dépassements de capacité lors des calculs.
    
* Remettre les images à la même échelle quelle que soit leur profondeur de couleur individuelle.
    
* Étendre la plage dynamique possible de l'image.
    

### **Vous appréciez mon travail ?**

Pensez à m'offrir un café pour soutenir mon travail !

[![](https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&emoji=%E2%98%95&slug=anshulsanghi&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff align="left")](https://www.buymeacoffee.com/anshulsanghi)

À la prochaine, bon codage et je vous souhaite un ciel dégagé !