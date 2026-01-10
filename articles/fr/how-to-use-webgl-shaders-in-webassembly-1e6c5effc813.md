---
title: Comment utiliser les shaders WebGL dans WebAssembly
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-28T18:26:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-webgl-shaders-in-webassembly-1e6c5effc813
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wJXxr-2-89FQ2O1wVXBD8w.jpeg
tags:
- name: General Programming
  slug: programming
- name: Shaders
  slug: shaders
- name: Tutorial
  slug: tutorial
- name: WebAssembly
  slug: webassembly
- name: WebGL
  slug: webgl
seo_title: Comment utiliser les shaders WebGL dans WebAssembly
seo_desc: 'By Dan Ruta

  WebAssembly is blazing fast for number crunching, game engines, and many other things,
  but nothing can quite compare to the extreme parallelization of shaders, running
  on the GPU.

  This is especially so if you’re looking to do some image p...'
---

Par Dan Ruta

WebAssembly est extrêmement rapide pour le [traitement de données](https://ai.danruta.co.uk/webassembly), les [moteurs de jeu](http://webassembly.org/demo/), et bien d'autres choses, mais rien ne peut égaler le parallélisme extrême des shaders, exécutés sur le GPU.

Cela est particulièrement vrai si vous souhaitez faire du traitement d'image. Habituellement, sur le web, cela est fait via WebGL, mais comment accéder à ses APIs lorsque vous utilisez WebAssembly ?

### Installation

Nous allons très brièvement passer en revue la configuration d'un projet exemple, puis nous verrons comment une image peut être chargée en tant que texture. Ensuite, dans un contexte séparé, nous appliquerons un shader GLSL de détection de contours à l'image.

Tout le code est dans un dépôt [ici](https://github.com/DanRuta/webassembly-webgl-shaders), si vous préférez passer directement à cela. Notez que vous devez servir vos fichiers via un serveur pour que WebAssembly fonctionne.

En tant que prérequis, je vais supposer que vous avez déjà configuré votre projet WebAssembly. Si ce n'est pas le cas, vous pouvez consulter l'article [ici](https://medium.com/statuscode/setting-up-the-ultimate-webassembly-c-workflow-6484efa3e162) sur la façon de le faire, ou simplement forker le dépôt lié ci-dessus.

Pour démontrer le code ci-dessous, j'utilise un fichier HTML de base qui sert uniquement à charger une image, obtenir ses données d'image, et les passer au code WebAssembly en utilisant [la fonction _ccallArrays_](https://becominghuman.ai/passing-and-returning-webassembly-array-parameters-a0f572c65d97).

![Image](https://cdn-media-1.freecodecamp.org/images/1*zJIvrPP5Q_-JqJSSAH738g.png)
_Le fichier HTML avec l'image d'entrée de prévisualisation_

En ce qui concerne le code C++, il y a un fichier emscripten.cpp qui gère et achemine les appels de méthode vers des instances de contexte créées dans le fichier Context.cpp. Le fichier Context.cpp est structuré comme suit :

### Compilation

WebGL est basé sur et suit la spécification OpenGL ES (Embedded Systems), qui est un sous-ensemble de OpenGL. Lors de la compilation, emscripten mappera notre code à l'API WebGL.

Il existe plusieurs versions différentes que nous pouvons cibler. OpenGL ES 2 correspond à WebGL 1, tandis que OpenGL ES 3 correspond à WebGL 2. Par défaut, vous devriez cibler WebGL 2, car il vient avec [certaines optimisations et améliorations gratuites](https://github.com/kripken/emscripten/blob/incoming/site/source/docs/optimizing/Optimizing-WebGL.rst#which-gl-mode-to-target).

Pour ce faire, nous devons ajouter [le flag `USE_WEBGL2=1`](https://kripken.github.io/emscripten-site/docs/porting/multimedia_and_graphics/OpenGL-support.html#webgl-friendly-subset-of-opengl-es-2-0-3-0) à la compilation.

Si vous prévoyez d'utiliser certaines fonctionnalités OpenGL ES non présentes dans la spécification WebGL, vous pouvez utiliser [les flags `FULL_ES2=1` et/ou `FULL_ES3=1`](https://kripken.github.io/emscripten-site/docs/porting/multimedia_and_graphics/OpenGL-support.html#opengl-es-2-0-3-0-emulation).

Pour pouvoir gérer de grandes textures/images, nous pouvons également ajouter [le flag `ALLLOW_MEMORY_GROWTH=1`](https://kripken.github.io/emscripten-site/docs/optimizing/Optimizing-Code.html#memory-growth). Cela supprime la limite de mémoire du programme WebAssembly, au détriment de certaines optimisations.

Si vous savez à l'avance combien de mémoire vous aurez besoin, vous pouvez utiliser le flag `TOTAL_MEMORY=X`, où X est la taille de la mémoire.

Nous allons donc finir avec quelque chose comme ceci :

`emcc -o ./dist/appWASM.js ./dev/cpp/emscripten.cpp -O3 -s ALLOW_MEMORY_GROWTH=1 -s USE_WEBGL2=1 -s FULL_ES3=1 -s WASM=1 -s NO_EXIT_RUNTIME=1 -std=c++1z`

Enfin, nous avons besoin des imports suivants, dans notre code :

```
#include <emscripten.h>
#include <string>
#include <GLES2/gl2.h>
#include <EGL/egl.h>
extern "C" {
    #include "html5.h" // module emscripten
}
```

### Implémentation

Si vous avez déjà de l'expérience avec WebGL ou OpenGL, cette partie peut vous sembler familière.

Lors de l'écriture de code OpenGL, l'API ne fonctionnera pas tant que vous n'aurez pas créé un contexte. Cela est normalement fait en utilisant des APIs spécifiques à la plateforme. Cependant, le web n'est pas lié à une plateforme, et nous pouvons utiliser une API intégrée dans OpenGL ES.

La majorité du travail, cependant, peut être plus facilement implémentée en utilisant les APIs d'emscripten dans [le fichier html5.h](http://kripken.github.io/emscripten-site/docs/api_reference/html5.h). Les fonctions qui nous intéressent sont :

* _emscripten_webgl_create_context_ — Cela instanciera un contexte pour le canvas et les attributs donnés
* _emscripten_webgl_destroy_context_ — Cela est nécessaire pour nettoyer la mémoire lors de la destruction des instances de contexte
* _emscripten_webgl_make_context_current_ — Cela assignera et changera le contexte auquel WebGL rendra

#### Créer le contexte

Pour commencer l'implémentation, vous devez d'abord créer les éléments canvas dans votre code JavaScript. Ensuite, lorsque vous utilisez la fonction `emscripten_webgl_create_context`, vous passez l'id du canvas comme premier paramètre, avec toute configuration comme second. La fonction `emscripten_webgl_make_context_current` est utilisée pour définir le nouveau contexte comme celui actuellement en cours d'utilisation.

Ensuite, le vertex shader (pour spécifier les coordonnées) et le fragment shader (pour calculer la couleur à chaque pixel) sont compilés, et le programme est construit.

Enfin, les shaders sont attachés au programme, qui est ensuite lié et validé.

Bien que cela semble beaucoup, le code pour cela est le suivant :

La compilation du shader est effectuée dans la fonction auxiliaire `CompileShader` qui effectue la compilation, imprimant toute erreur :

#### Créer le shader

Le code du shader pour cet exemple est minimal, et il mappe simplement chaque pixel à lui-même, pour afficher l'image en tant que texture :

Vous pouvez accéder au contexte du canvas en JavaScript en plus du contexte dans le code C++, mais il doit être du même type, 'webgl2'. Bien que définir plusieurs types de contexte ne fasse rien lorsque vous utilisez uniquement JavaScript, si vous le faites avant de créer le contexte webgl2 dans WebAssembly, cela générera une erreur lorsque l'exécution du code atteindra ce point.

#### Charger la texture

La première chose à faire lors de l'application du shader est d'appeler la fonction `emscripten_webgl_make_context_current` pour s'assurer que nous utilisons toujours le bon contexte, et `glUseProgram` pour s'assurer que nous utilisons le bon programme.

Ensuite, nous obtenons les indices des variables GLSL (similaire à l'obtention d'un pointeur) via les fonctions `glGetAttribLocation` et `glGetUniformLocation`, afin que nous puissions assigner nos propres valeurs à ces emplacements. La fonction utilisée pour cela dépend du type de valeur.

Par exemple, un entier, tel que l'emplacement de la texture, nécessite `glUniform1i`, tandis qu'un float nécessiterait `glUniform1f`. [Ceci est une bonne ressource](https://www.khronos.org/registry/OpenGL-Refpages/es3.0/html/glUniform.xhtml) pour voir quelle fonction vous devez utiliser.

Ensuite, nous obtenons l'objet de texture via `glGenTextures`, nous l'assignons comme texture active, et nous chargeons le tampon imageData. Les tampons de sommets et d'indices sont ensuite liés, pour définir les limites de la texture afin de remplir le canvas.

Enfin, nous effaçons le contenu existant, définissons nos variables restantes avec des données, et dessinons sur le canvas.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lICDL2HxpbsJ2RjvjfzCbg.png)
_La texture en cours de chargement_

#### Détecter les contours à l'aide d'un shader

Pour ajouter un autre contexte, où la détection de contours est effectuée, nous chargeons un fragment shader différent (qui applique le [filtre Sobel](https://en.wikipedia.org/wiki/Sobel_operator)), et nous lions la largeur et la hauteur comme variables supplémentaires, dans le code.

Pour choisir entre différents fragment shaders, pour les différents contextes, nous ajoutons simplement une instruction if-else dans le constructeur, comme ceci :

Et pour charger les variables de largeur et de hauteur, nous ajoutons ce qui suit à la fonction run :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kfvsG8s4vRLbxPxZot8isg.png)

Si vous rencontrez une erreur similaire à `ERROR: GL_INVALID_OPERATION : glUniform1i: wrong uniform function for type`, alors il y a une fonction d'assignation incorrecte pour la variable donnée.

Une chose à surveiller lors de l'envoi des imageData, est d'utiliser le bon tas, unsigned integer (le tableau typé Uint8Array). Vous pouvez en apprendre plus sur ceux-ci [ici](https://becominghuman.ai/passing-and-returning-webassembly-array-parameters-a0f572c65d97), mais si vous utilisez la fonction ccallArray, définissez la configuration 'heapIn' sur "HEAPU8", comme vu ci-dessus.

Si le type n'est pas correct, la texture se chargera toujours, mais vous allez voir des rendus étranges, comme ceux-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*0_EmLybuEaLJnnd_JfobFg.png)

### Conclusion

Nous avons passé en revue un mini projet de style "Hello World !" pour montrer comment charger des textures et appliquer des shaders GLSL à celles-ci dans WebAssembly. Le code complet est hébergé sur GitHub [ici](https://github.com/DanRuta/webassembly-webgl-shaders), pour référence supplémentaire.

Pour un projet réel, vous pourriez vouloir ajouter une gestion d'erreurs supplémentaire. Je l'ai omise ici, pour plus de clarté.

Il pourrait également être plus efficace (dans l'exemple ci-dessus) de partager des données telles que la texture imageData entre les contextes. Vous pouvez en lire plus sur cela et plus [ici](https://blog.gvnott.com/some-usefull-facts-about-multipul-opengl-contexts/).

Pour quelques lectures supplémentaires, vous pouvez consulter [ce lien](https://www.khronos.org/opengl/wiki/Common_Mistakes) pour les erreurs courantes, ou vous pouvez parcourir quelques projets de démonstration dans le dossier [glbook](https://github.com/kripken/emscripten/tree/incoming/tests/glbook) d'emscripten, sur GitHub.

Pour voir WebGL utilisé dans un projet WebAssembly, vous pouvez consulter la [branche dev sur jsNet](https://github.com/DanRuta/jsNet/tree/dev), un framework d'apprentissage profond basé sur le web, où je travaillerai sur le déplacement de calculs plus lourds vers les shaders, au cours des prochaines semaines (le support des shaders de calcul WebGL via OpenGL ES 3.1 [ne peut pas arriver assez tôt](https://www.khronos.org/webgl/public-mailing-list/public_webgl/1706/msg00034.php) ? ).

**Mise à jour**

Pour voir à quoi ressemblerait le calcul GPU utilisant des shaders dans WebAssembly, vous pouvez consulter [le dépôt pour GPGPU](https://github.com/DanRuta/GPGPU), une petite bibliothèque sur laquelle je travaille, avec des versions JavaScript et WebAssembly.