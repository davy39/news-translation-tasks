---
title: Qu'est-ce que le Firmware ? Définition et Exemples
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2022-04-21T18:40:08.000Z'
originalURL: https://freecodecamp.org/news/what-is-firmware
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/postimage.png
tags:
- name: firmware
  slug: firmware
- name: hardware
  slug: hardware
- name: software
  slug: software
seo_title: Qu'est-ce que le Firmware ? Définition et Exemples
seo_desc: 'Did you know that firmware is literally everywhere? It might be strange
  to think about – but it''s just as common as hardware and software.

  In fact, it is thanks to firmware that:


  Printers work

  Defibrillators work

  Car radios works

  and more …


  Based o...'
---

Saviez-vous que le firmware est littéralement partout ? Cela peut sembler étrange à penser – mais il est tout aussi courant que le hardware et le software.

En fait, c'est grâce au firmware que :

* Les imprimantes fonctionnent
* Les défibrillateurs fonctionnent
* Les radios de voiture fonctionnent
* et plus encore…

D'après les exemples ci-dessus, vous avez probablement déjà une idée de ce qu'est le firmware. Mais vous n'avez pas de définition claire.

Pour vraiment comprendre ce qu'est le firmware, nous devons d'abord comprendre le software, puis le hardware, et enfin nous pouvons nous pencher sur le firmware.

Dans ce tutoriel, j'expliquerai chaque sujet avec une analogie. De cette façon, tout le monde peut comprendre.

Peu importe si vous débutez dans la technologie !

Avec cela, je souhaite m'assurer que tout le monde comprend ce qu'est le software, le hardware et le firmware. Je ne m'attarderai pas sur les termes techniques.

### Dans cet article, nous explorerons :

* Qu'est-ce que le software exactement ?
* Qu'est-ce que le hardware exactement ?
* Qu'est-ce que le firmware exactement ?

## Qu'est-ce que le Software ?

![Image](https://www.freecodecamp.org/news/content/images/2022/03/book.jpeg)
_Photo par [**Pexels**](https://www.pexels.com/@kubra-dogu-80605500?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels" rel="noopener">**Kübra Doğu**</a> from <a href="https://www.pexels.com/photo/food-wood-dawn-coffee-9222655/?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels" rel="noopener)_

Imaginez, si vous le voulez, que vous n'avez aucune idée de ce que vous allez préparer pour le dîner aujourd'hui.

Heureusement, vous trouvez un vieux livre de cuisine et décidez de cuisiner une des recettes qu'il contient.

Le livre de cuisine contient de nombreuses recettes. Chacune de ces recettes a ses propres instructions.

Dans le **livre de cuisine**, une **recette** peut être vue comme un **ensemble d'étapes** (ou instructions) qui, ensemble, forment un **repas**.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/cooking-instruction.jpg)
_Photo par [Luis Quintero on Pexels](https://www.pexels.com/photo/open-bible-2294878/)_

Vous pouvez également créer vos propres repas en fonction de votre expérience dans la cuisine de nombreuses recettes différentes, n'est-ce pas ?

Le software n'est pas différent.

Les **programmes logiciels** peuvent être vus comme un **ensemble d'instructions** qui fonctionnent ensemble pour former un **programme**.

```assembly
 global  _main
    extern  _printf

    section .text
_main:
    push    message
    call    _printf
    add     esp, 4
    ret
message:
    db  'Hello, World', 10, 0
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/HelloWorld.asm.png)

Ensuite, les applications sont de grands ensembles d'instructions qui effectuent des tâches spécifiques.

Les systèmes d'exploitation sont de grands ensembles d'instructions qui coordonnent les ressources logicielles et matérielles.

* Livre de cuisine = software
* Livre de cuisine pour le dîner = type de software (application ou système d'exploitation)
* Recette = programme

Vous avez besoin d'une recette pour préparer le dîner. Vous devez suivre chaque étape du livre de cuisine pour créer une recette.

Une fois que vous avez terminé toutes les étapes, votre dîner est prêt.

Vous avez besoin de software pour accomplir une tâche particulière. Un ordinateur doit suivre toutes les instructions pour que le software fonctionne.

Par conséquent, le software s'exécute soit pendant que les instructions sont suivies, soit après qu'elles ont été complétées.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/recipie---cooking-instructions.png)

## Qu'est-ce que le Hardware ?

![Image](https://www.freecodecamp.org/news/content/images/2022/03/food.jpeg)
_Photo par [**Pexels**](https://www.pexels.com/@elevate?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels" rel="noopener">**ELEVATE**</a> from <a href="https://www.pexels.com/photo/chef-preparing-vegetable-dish-on-tree-slab-1267320/?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels" rel="noopener)_

Pour préparer le dîner, vous avez besoin d'une série d'étapes du livre de cuisine qui vous indiquent comment préparer un repas particulier.

Vous avez également besoin de divers outils pour cuisiner – comme des casseroles et des poêles, des couteaux et les aliments eux-mêmes. C'est comme le hardware.

Ainsi, un livre de cuisine vous donne des instructions qui vous permettent de cuisiner.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/cooking-process-1.png)

Pour que le hardware fonctionne, il a besoin de software (un ensemble d'instructions) pour lui dire quoi faire.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/CPU-process-2.png)

Le software donne alors des instructions au hardware qui lui permettent de fonctionner.

* Outils de préparation de repas = hardware
* Recette = software

Sans software, vous ne pouvez pas faire fonctionner le hardware.

Sans recette, vous ne saurez pas quoi faire avec vos divers outils et ingrédients pour préparer un repas.

Comme le hardware sans software, vous pouvez également manger un repas avec juste des aliments non cuits. Beurk.

De la même manière qu'il existe divers types de repas, il existe également divers types de hardware informatique.

Par exemple :

* CPU
* RAM
* GPU
* et bien plus encore…

![Image](https://www.freecodecamp.org/news/content/images/2022/04/comparason-of-processes.png)
_Comparaison des processus_

## Qu'est-ce que le Firmware ?

![Image](https://www.freecodecamp.org/news/content/images/2022/03/dessert.jpeg)
_Photo par [**Pexels**](https://www.pexels.com/@ella-olsson-572949?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels" rel="noopener">**Ella Olsson**</a> from <a href="https://www.pexels.com/photo/close-up-photo-of-chocolate-mousse-3026810/?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels" rel="noopener)_

Un programme est un ensemble d'instructions lues par un ordinateur.

Disons que vous voulez simplement préparer une collation ou un dessert. Vous n'avez probablement pas besoin d'autant d'ingrédients que lorsque vous préparez un dîner pour votre famille, n'est-ce pas ?

Disons que vous voulez un software qui fonctionne sur un micro-ondes. Vous n'avez pas besoin de tout le hardware de l'ordinateur pour faire fonctionner le micro-ondes, n'est-ce pas ? Vous avez juste besoin de ce qui est spécifique pour faire fonctionner le micro-ondes.

Ou disons que vous voulez un software qui fonctionne sur une imprimante. Vous n'avez pas besoin de tout le hardware de l'ordinateur pour faire fonctionner l'imprimante, n'est-ce pas ? Juste le software pour l'imprimante.

* Software de micro-ondes = firmware
* Software d'imprimantes = firmware

Ainsi, cela signifie que le firmware n'est rien de plus que du software, mais dans un appareil hardware. Pas dans un ordinateur.

Le firmware permet à un hardware très spécifique d'accomplir des tâches très spécifiques.

## Conclusion

Merci d'avoir lu ! Maintenant, vous en savez plus sur :

* Software
* Hardware
* Firmware

Photo de microprocesseur par **[Pok Rie](https://www.pexels.com/@pok-rie-33563?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)** from **[Pexels](https://www.pexels.com/photo/dell-motherboard-and-central-processing-unit-1432675/?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)**