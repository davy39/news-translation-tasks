---
title: SpriteKit Avancé — Comment créer un jeu 2,5D (Partie II)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-01T20:06:08.000Z'
originalURL: https://freecodecamp.org/news/spritekit-advanced-how-to-build-a-2-5d-game-part-ii-30ddb613b568
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MYgdND4CCLf9eONh2LfRSg.png
tags:
- name: Game Development
  slug: game-development
- name: indie game
  slug: indie-game
- name: iOS
  slug: ios
- name: SpriteKit
  slug: spritekit
- name: 'tech '
  slug: tech
seo_title: SpriteKit Avancé — Comment créer un jeu 2,5D (Partie II)
seo_desc: 'By Luke Konior

  Intro

  This article shows how to write basic shaders in the SpriteKit. It’s split into
  two parts: first we play, then we learn.

  It also contains information how to use SKAttribute and SKAttributeValue classes
  that were added in iOS SDK ...'
---

Par Luke Konior

### Introduction

Cet article montre comment écrire des shaders de base dans SpriteKit. Il est divisé en deux parties : d'abord nous jouons, puis nous apprenons.

Il contient également des informations sur l'utilisation des classes `SKAttribute` et `SKAttributeValue` qui ont été ajoutées dans le SDK iOS 10.0.

Si vous n'avez pas encore lu la première partie, [la voici](https://medium.freecodecamp.org/spritekit-advanced-how-to-build-a-2-5d-game-part-i-2dc76c7c65e2).

### Préparer le projet

Allons-y rapidement.

* Ouvrez XCode 8 et créez un nouveau projet à partir du modèle : iOS > Game.
* Ouvrez le fichier `GameScene.sks` et supprimez le label au centre de l'écran.
* Téléchargez [cette image](http://cosmicteapotgames.com/wp-content/uploads/2017/06/trees.png) et placez-la dans `Assets.xcassets`

![Image](https://cdn-media-1.freecodecamp.org/images/MxZmGjoG9xkRbOf3TFew3ePoayMqXZd8qsQa)

* Nommez-la « Trees »
* Ouvrez le fichier `GameScene.m`
* supprimez toutes les variables d'instance
* supprimez toutes les méthodes

### Le Fragment Shader

Maintenant, nous créons un **fragment shader** vide dans XCode :

* Dans le Project Navigator, sélectionnez Supporting Files
* Choisissez : File > New > File…
* Sélectionnez : Other > Empty
* Nommez-le « `myShader.fsh` » et appuyez sur Create.
* Placez ceci à l'intérieur :

```
// actuellement un shader pass-thru ennuyeux
void main( void ) {
    vec4 color = texture2D(u_texture, v_tex_coord);
    // ici émergera quelque chose de digne
    gl_FragColor = color;
}
```

Le fragment shader ci-dessus ne fait rien de perceptible. Explication rapide :

* `void main()`
  cette fonction est appelée pour chaque pixel du sprite et sort la couleur pour ce pixel
  Reçoit les données d'entrée des globales environnantes et doit définir la variable `gl_FragColor`
* `vec2`, `vec3` et `vec4` sont des types similaires au C : `float array[2]`, `float array[3]` et `float array[4]`
* _u_texture_ est un ID de texture
  Laissez-le tranquille :-)
* `v_tex_coord` est un `vec2` qui contient notre position actuelle dans la texture
* `texture2D(tex , p)` est une fonction qui retourne la couleur de la texture `tex` au `point p` sous forme de `vec4`
  qui contient rgba
* `gl_FragColor` est une couleur de sortie
  Nous devons lui assigner un `vec4`

### Code de chargement

Il reste le code de chargement.

* Ouvrez le fichier `GameScene.m`
* ajoutez la méthode `-didMoveToView:`

```
- (void)didMoveToView:(SKView *)view {
    // 1. charge le source du shader depuis myShaderFile.fsh
    NSString *file = [[NSBundle mainBundle] pathForResource:@"myShader" ofType:@"fsh"];
    NSString *sourceString = [NSString stringWithContentsOfFile:file encoding:NSUTF8StringEncoding error:nil];
    
    // 2. crée le shader
    SKShader *shader = [SKShader shaderWithSource:sourceString];
    
    // 3. assigne le shader à un nouveau nœud sprite
    SKSpriteNode *spriteNode = [SKSpriteNode spriteNodeWithImageNamed:@"Trees"];
    spriteNode.shader = shader;
    
    // 4. enfin ajoute le sprite à la scène
    [self addChild:spriteNode];
}
```

Assurez-vous que `myShader.fsh` figure dans ProjectFile > Target > Build Phases > Copy Bundle Resources !

Vous pouvez maintenant exécuter le projet sur un appareil iOS. Il ne devrait y avoir aucune erreur dans la console de XCode et vous devriez voir un écran similaire à celui-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/4TnLiWjcn9mTO94Y-lcdZ3L9Y46zJe7iKZUN)

### Amusons-nous un peu !

Maintenant vient la partie amusante. Nous allons remplacer la fonction principale du shader.

### Colorier en rouge avec préservation de l'alpha

![Image](https://cdn-media-1.freecodecamp.org/images/sGVOlBZaNhox2S1oXJutpLyAHMAKc-luelcG)

```
void main( void ){
    vec4 color = texture2D(u_texture, v_tex_coord);
    float alpha = color.a;
    gl_FragColor = vec4(1,0,0, 1.0) * alpha; // googlez "premultiplied alpha"
}
```

### Réduire de 2x

![Image](https://cdn-media-1.freecodecamp.org/images/L18M4oDhBB4a09tcqOz7LQk12QRaI45BzHEr)

```
void main( void ){
    vec4 color = texture2D(u_texture, v_tex_coord * 2.0);
    gl_FragColor = color;
}
```

### Échanger les couleurs après 1 seconde

![Image](https://cdn-media-1.freecodecamp.org/images/szn2VF1e3TpEyod6Vvc2kPXaqP5P9AqBt1sb)

```
void main( void ){
    vec4 color = texture2D(u_texture, v_tex_coord);
    float alpha = color.a;
    float phase = mod(u_time, 3);
    vec3 outputColor = color.rgb;
    if (phase < 1.0) {
        outputColor = color.bgr;
    } else if (phase < 2.0) {
        outputColor = color.brg;
    }
    gl_FragColor = vec4(outputColor, 1.0) * alpha;
}
```

### Colorier au fil du temps

![Image](https://cdn-media-1.freecodecamp.org/images/eOR06sIrv-Gja1ymP6RCgb-un73qHSOFuzgb)

```
void main( void ){
    vec4 color = texture2D(u_texture, v_tex_coord);
    float alpha = color.a;
    float r = (sin(u_time+ 3.14 * 0.00)+1.0)*0.5;
    float g = (sin(u_time+ 3.14 * 0.33)+1.0)*0.5;
    float b = (sin(u_time+ 3.14 * 0.66)+1.0)*0.5;
    gl_FragColor = vec4(r,g,b, 1.0) * alpha;
}
```

### Vagues

![Image](https://cdn-media-1.freecodecamp.org/images/nOcOdOxNc3mt-y8ZLgmJlFFLHYcLFLbarzbN)

```
void main( void ){
    float deltaX = sin(v_tex_coord.y*3.14*10 + u_time * 4)*0.01;
    vec2 coord = v_tex_coord;
    coord.x = coord.x + deltaX;
    vec4 color = texture2D(u_texture, coord);
    gl_FragColor = color;
}
```

### Nouveaux Attributs

Lors de la WWDC 2016, Apple a introduit une mise à jour importante pour SpriteKit — les classes `SKAttribute` et `SKAttributeValue`.

Avant cette mise à jour du SDK, si nous voulions passer des paramètres personnalisés dans le programme `shader`, nous devions passer les données via une valeur uniforme.

Cela avait deux sérieux inconvénients :

* chaque changement d'uniforme provoquait une recompilation du shader
* le programme shader traitait chaque sprite de la même manière exacte

Par exemple : si nous voulions teindre un groupe de sprites en rouge, et l'un d'eux en bleu, nous avions deux solutions. Premièrement, nous créions deux instances séparées de `SKShader` et changions notre uniforme personnalisé `myColor`.

Deuxièmement, nous faisions une instance de `shader` et changions son uniforme, ce qui provoquait une recompilation.

Les deux méthodes ne peuvent pas être dessinées dans le même passage. Et la seconde nécessite un code de gestion complexe.

Le SDK 10.0 a introduit les classes `SKAttribute` et `SKAttributeValue`. Ces deux classes permettent (enfin !) de passer des données aux programmes shader sans recompilation. L'algorithme d'utilisation est simple :

* La partie shader :

1. Créez un programme shader
   `SKShader`
2. Créez un tableau de `SKAttributes`
3. Assignez le tableau d'attributs au programme shader

* La partie `sprite` :

1. Assignez le programme shader à un sprite
2. Assignez un dictionnaire de `SKAttributeValues`

### Exemple avec attributs

Dans le dernier exemple, nous ajouterons deux sprites supplémentaires. Chacun d'eux aura le même programme shader et ne différera que par les attributs. Modifions le `_didMoveToView:` dans `GameScene.m` :

```
- (void)didMoveToView:(SKView *)view {
    NSString *file = [[NSBundle mainBundle] pathForResource:@"myShader" ofType:@"fsh"];
    NSString *sourceString = [NSString stringWithContentsOfFile:file encoding:NSUTF8StringEncoding error:nil];
    SKShader *shader = [SKShader shaderWithSource:sourceString];
    
    // 1. Ajoute un attribut personnalisé au shader
    SKAttribute *attrProgress = [SKAttribute attributeWithName:@"THE_MIGHTY_DARK_FACTOR" type:SKAttributeTypeFloat];
    shader.attributes = @[attrProgress];
    
    // 2. Crée des sprites d'arbres
    NSArray *trees = @[
                       [self createTreeWithShader:shader mightyFactor:0.3f zPosition:1],
                       [self createTreeWithShader:shader mightyFactor:0.6f zPosition:2],
                       [self createTreeWithShader:shader mightyFactor:0.9f zPosition:3],
                       ];
    for (SKSpriteNode *tree in trees) {
        [self addChild:tree];
    }
}

- (SKSpriteNode*)createTreeWithShader:(SKShader*)shader mightyFactor:(CGFloat)mightyFactor zPosition:(CGFloat)zPosition {
    SKSpriteNode *treeNode = [SKSpriteNode spriteNodeWithImageNamed:@"Trees"];
    treeNode.shader = shader;
    
    // 3. Remplit l'attribut personnalisé sur le sprite
    treeNode.attributeValues = @{@"THE_MIGHTY_DARK_FACTOR": [SKAttributeValue valueWithFloat:mightyFactor]};
    treeNode.zPosition = zPosition;
    return treeNode;
}
```

… et le programme shader :

```
void main( void ){
    vec4 color = texture2D(u_texture, v_tex_coord * (2.5 * THE_MIGHTY_DARK_FACTOR));
    float alpha = color.a;
    vec3 baseColor = color.rgb * THE_MIGHTY_DARK_FACTOR;
    gl_FragColor = vec4(baseColor, 1.0) * alpha;
}
```

… et voyez le résultat paramétré !

![Image](https://cdn-media-1.freecodecamp.org/images/BqTQUZBmVKfeJI4C97kqJR2gX3VyispHHaep)

### Avertissements

* Le code source du shader est généralement chargé depuis un fichier `.fsh` vers une `NSString` simple
  Ce code doit compiler sur l'appareil cible pendant l'exécution
  aucune vérification à la compilation !
* Les anciens appareils peuvent utiliser une version différente d'OpenGL ES, soyez donc prudent avec les différences de syntaxe GLSL !
  Dans le cas de Raft Challenge, il a été nécessaire de remplacer `__constant` (valide dans OpenGL ES 3.0) par `const` pour OpenGL ES 2.0.
* Il est bon de garder une référence à l'objet SKShader quelque part et de le réutiliser aussi souvent que nécessaire pour éviter une baisse visible du taux de rafraîchissement
  Bien que l'allocation et la compilation du shader prennent moins de 1/60 sec, cela peut devenir un fardeau énorme dans la boucle de rendu
* Lorsque vous utilisez les Texture Atlases de SpriteKit, soyez prudent avec `vtexcoord`
  XCode peut faire tourner certaines textures qui échangent les axes `X` et `Y`
  **La modification de couleur est sûre, la géométrie ne l'est pas**

![Image](https://cdn-media-1.freecodecamp.org/images/Nh9NYKX2tYvNvLca66dRsJAQTY7CmGd2EhqL)

### Résumé

Nous avons appris par des exemples comment utiliser les fragment shaders dans Sprite Kit. Nous avons ajouté des paramètres aux sprites afin que notre programme shader puisse rendre chaque instance de manière différente sans aucune perte de performance.

Le [projet complet](http://cosmicteapotgames.com/wp-content/uploads/2017/06/ShaderDemo.zip) est disponible pour téléchargement.

Vous pouvez [lire la partie 3 de cette série ici](https://medium.freecodecamp.org/spritekit-advanced-how-to-build-a-2-5d-game-part-iii-e058b99cfbc3).

À propos de l'auteur : Kamil Ziętek est un développeur iOS chez [www.allinmobile.co](http://www.allinmobile.co)