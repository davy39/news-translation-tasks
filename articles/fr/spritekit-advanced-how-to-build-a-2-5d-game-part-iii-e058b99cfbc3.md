---
title: SpriteKit Avancé — Comment construire un jeu 2,5D (Partie III)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-01T20:09:42.000Z'
originalURL: https://freecodecamp.org/news/spritekit-advanced-how-to-build-a-2-5d-game-part-iii-e058b99cfbc3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AcTkWr0OAaQmXWb0uJ_wbA.png
tags:
- name: Game Development
  slug: game-development
- name: indie game
  slug: indie-game
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: SpriteKit Avancé — Comment construire un jeu 2,5D (Partie III)
seo_desc: 'By Luke Konior

  Intro

  This article is about improving visuals of Raft Challenge by applying GPU’s shaders
  to the still scenery. It explains the algorithms and potential pitfalls when using
  GLSL in SpriteKit.

  The reader should have basic experience in ...'
---

Par Luke Konior

### Introduction

Cet article traite de l'amélioration des visuels de [Raft Challenge](https://itunes.apple.com/app/apple-store/id1073887270?pt=117756562&ct=Develop%20Articles&mt=8) en appliquant les shaders du GPU au décor immobile. Il explique les algorithmes et les pièges potentiels lors de l'utilisation de GLSL dans SpriteKit.

Le lecteur doit avoir une expérience de base dans l'écriture de fragment shaders. Nous en avons discuté dans la [partie 1](https://medium.freecodecamp.org/spritekit-advanced-how-to-build-a-2-5d-game-part-i-2dc76c7c65e2) et la [partie 2](https://medium.freecodecamp.org/spritekit-advanced-how-to-build-a-2-5d-game-part-ii-30ddb613b568) de cette série.

### Le problème

![Image](https://cdn-media-1.freecodecamp.org/images/oDaivdEqUg2e5rQhlqXi78c5MC603SYztUGx)

Après que le jeu soit entré en phase bêta, nous avons reçu des retours de diverses personnes. Nous avons souvent entendu dire que les graphismes étaient bons, mais aussi statiques, ce qui, à long terme, menait à l'ennui.

Ma réaction instantanée a été : « Ils ont dit que c'était statique ? Alors nous allons ajouter un peu de vent pour bouger le tout ! » Après cela, nous avons réfléchi davantage au problème.

De si grands objets comme les arbres ne peuvent pas être animés image par image, car cela entraînerait des problèmes de mémoire. Nous envisagions d'ajouter de petits objets animés comme des animaux. Mais cela compliquerait encore plus le graphe de scène. Et cela aurait un impact inconnu sur les performances.

La solution à laquelle j'ai pensé était d'animer toute la forêt en utilisant les fragment shaders. Je voulais créer l'effet de vent.

L'idée était d'appliquer une distorsion horizontale à la texture du sprite avec une intensité proportionnelle à la distance par rapport à la base des troncs. Cette intensité changeait également avec le temps et était influencée par la « profondeur » de la scène.

Autres avantages de cette solution :

* intégration facile
C'est aussi simple que de remplir les propriétés d'un objet existant
* performance
* grande flexibilité

Voici le code source (GLSL) :

```
void main( void ){    float horizonAbsoluteOffset = 0.64; // 1    float distanceFromTrunksBase = abs(v_tex_coord[1] - horizonAbsoluteOffset); // 2    float maxDivergence = mix(0.0,1.0,distanceFromTrunksBase)*0.038; // 3    float factor = sin(u_time*2+(attrDepth * 1.3)); // 4    vec2 deltaUV = vec2(maxDivergence * factor, 0); // 5        gl_FragColor = texture2D(u_texture, v_tex_coord + deltaUV); //6}
```

1. Ce `float` contient la position verticale de la base de tous les troncs
— Cette valeur est spécifique à notre texture
2. Nous calculons la distance entre le point d'échantillonnage actuel et la valeur ci-dessus
— Cette valeur est inférieure à 1.0 et peut être négative
3. Nous calculons la divergence maximale
— Le nombre magique à la fin a été ajusté par essais et erreurs
4. Nous calculons la force changeante et la direction du vent
— La fonction sin est une bonne base car elle retourne des valeurs prévisibles (-1 à 1)
— C'est aussi une fonction continue
— Cela signifie que nous pouvons mettre n'importe quoi comme argument et cela fonctionnera toujours
— Dans ce cas, « l'argument » est le temps actuel plus la « profondeur » du sprite actuel
— Des nombres magiques sont ajoutés pour façonner l'animation
5. Le vecteur delta est créé
— La divergence maximale multipliée par le facteur va dans la position X tandis que Y reste à 0.
6. Cette ligne prend la couleur d'un point spécifique dans la texture et la sort à l'écran
— En ajoutant delta à notre position actuelle avec `vtexcoord`, nous modifions le point à partir duquel l'échantillonneur extrait la valeur de couleur

Résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/Y3nIvwFwhV7kkuep3Ukrsv1MCtU0uVdfZdO7)

Notez que les reflets sur l'eau bougent également. C'est parce que les arbres et les reflets font partie du même sprite et de la même texture. Pas de sorcellerie ici.

### Améliorer le brouillard

Y a-t-il autre chose que nous pouvons faire ? Eh bien, si nous ne pouvons pas inventer quelque chose de nouveau, nous pouvons toujours améliorer quelque chose qui existe. Notre designer a dit un jour que les arbres plus éloignés devraient avoir une couleur solide pour mieux se fondre dans le brouillard.

![Image](https://cdn-media-1.freecodecamp.org/images/7RcgTWOFptqBltzlww4HqWlpnjzbGp-1Baz2)

L'image ci-dessus est presque auto-explicative. Plus tôt, j'ai mentionné la « profondeur ». Chaque couche de la forêt a un attribut `attrDepth`. Il représente la distance entre les montagnes (0.0) et le spectateur (6.0).

Améliorons ce brouillard !

```
__constant vec3 colorLightMountains = vec3(0.847, 0.91, 0.8);__constant vec3 colorDarkMountains = vec3(0.729, 0.808, 0.643);
```

```
void main( void ){       //obtenir la couleur    vec4 color = texture2D(u_texture, v_tex_coord);    float alpha = color.a; // 1
```

```
    //brouillard    vec3 outputColor = vec3(color.rgb);    if (attrDepth < 1.0) {					// 2        outputColor = colorLightMountains;        alpha = min(attrDepth,alpha);    } else if (attrDepth < 2.0) {			// 3        outputColor = mix(colorLightMountains, colorDarkMountains, attrDepth - 1.0);    } else if (attrDepth <= 3.0) {		// 4        outputColor = mix(colorDarkMountains, color.rgb, attrDepth - 2.0);    }        gl_FragColor = vec4(outputColor, 1.0) * alpha; // 5}
```

Le code ci-dessus est assez simple, donc je vais me concentrer uniquement sur les points les plus importants :

1. Extraire `alpha` de la texture.
2. La phase éloignée
Lorsque la forêt est aussi éloignée que possible, elle a la couleur `Light Mountains` et `0 alpha`
En s'approchant, elle apparaît en augmentant `alpha` jusqu'à `depth == 1.0`
3. La distance moyenne
La couleur passe à `Dark Mountains` à mesure que les sprites se rapprochent du spectateur.
4. La distance proche
La couleur est un mélange entre `Dark Mountains` et la couleur de texture native
Naturellement, plus elle est proche, plus elle semble normale
5. Passer la couleur finale à la sortie en utilisant l'alpha extrait au début

Encore une fois, le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/wIO03dNsvPG8f9GbcFYWLRZngMMvWVBx5AJA)

### Combiner les deux effets

Ce que j'aime le plus avec les shaders, c'est leur flexibilité. Il n'est pas seulement possible de fusionner les deux effets sans sacrifier quoi que ce soit. C'est même recommandé de le faire.

Fusionner les shaders diminue les appels de dessin et cela augmente le taux de rafraîchissement.

```
__constant vec3 colorLightMountains = vec3(0.847, 0.91, 0.8);__constant vec3 colorDarkMountains = vec3(0.729, 0.808, 0.643);
```

```
void main( void ){    //vent    float horizonAbsoluteOffset = 0.64;    float distanceFromTrunksBase = abs(v_tex_coord[1] - horizonAbsoluteOffset);    float maxDivergence = mix(0.0,1.0,distanceFromTrunksBase)*0.038;    float factor = sin(u_time*2+(attrDepth * 1.3));    vec2 deltaUV = vec2(maxDivergence * factor, 0);        //obtenir la couleur    vec4 color = texture2D(u_texture, v_tex_coord + deltaUV);    float alpha = color.a;
```

```
    //brouillard    vec3 outputColor = vec3(color.rgb);    if (attrDepth < 1.0) {        outputColor = colorLightMountains;        alpha = min(attrDepth,alpha);    } else if (attrDepth < 2.0) {        outputColor = mix(colorLightMountains, colorDarkMountains, attrDepth - 1.0);    } else if (attrDepth <= 3.0) {        outputColor = mix(colorDarkMountains, color.rgb, attrDepth - 2.0);    }        //sortie    gl_FragColor = vec4(outputColor, 1.0) * alpha;}
```

Le résultat final :

![Image](https://cdn-media-1.freecodecamp.org/images/cltludNI-9wXKzt4KYKH2j4bUU6euwYIpXaD)

### Pièges

Il n'y a pas de rose sans épine.

* L'utilisation de shaders sur plusieurs grands sprites avec un canal `alpha` peut provoquer une baisse visible du taux de rafraîchissement.
* Le même GPU peut donner 60fps sur l'iPhone mais seulement 20fps sur l'iPad avec plus de pixels
Testez votre code fréquemment sur différents appareils, surtout les iPads avec écrans rétina
* Il n'y a pas de moyen fiable d'estimer les performances de l'appareil à partir du code
Exécutez votre jeu sur plusieurs appareils physiques et listez ceux qui sont capables d'exécuter des shaders avec des performances décents
Pour distinguer les appareils, vous pouvez utiliser [UIDevice-Hardware.m](https://github.com/erica/uidevice-extension/blob/master/UIDevice-Hardware.m)
* Votre texture partiellement transparente perd-elle de la couleur et devient grise ? Googlez **premultiplied alpha** !
* Méfiez-vous de l'utilisation de `SKTextureAtlases` si vous modifiez les coordonnées comme dans l'exemple du vent
Lors de la génération de l'atlas, XCode peut faire pivoter et déplacer certaines textures.
Il est impossible de détecter une telle anomalie à partir du code, ou du moins je ne sais pas comment
* Pour certains sprites, vous pouvez recevoir une texture avec les coordonnées X et Y échangées !
* Vous pouvez accidentellement vous retrouver sur une sous-texture complètement différente !

![Image](https://cdn-media-1.freecodecamp.org/images/rJPStNu5vGDYqBx3i97bg2tuJ5VjyROFDw0n)

### Résumé

Nous avons appris comment utiliser les fragment shaders pour créer du vent et du brouillard. En écrivant votre propre code GLSL, vous produirez sûrement de nombreux artefacts d'affichage. Certains d'entre eux sont ennuyeux, et d'autres sont hilarants. Gardez à l'esprit que certains d'entre eux peuvent avoir le potentiel de devenir une fonctionnalité !

À propos de l'auteur : Kamil Zi9tek est un développeur iOS chez [www.allinmobile.co](http://www.allinmobile.co)