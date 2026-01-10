---
title: Comment rendre votre site web ultra-rapide avec des images WebP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-13T15:12:22.000Z'
originalURL: https://freecodecamp.org/news/make-your-website-load-lightning-fast-with-webp-images-cf55c98ac0a2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AvUpREMP85amQcVoNKntfw.jpeg
tags:
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment rendre votre site web ultra-rapide avec des images WebP
seo_desc: 'By Carmen Chung

  Ever felt like your website takes forever to load?

  The good news is that you’re not alone. A report published by Google found that
  70% of the pages they analysed took more than 10 seconds to load — for just one
  page.

  The bad news is…w...'
---

Par Carmen Chung

Vous êtes-vous déjà senti frustré parce que votre site web met une éternité à charger ?

La bonne nouvelle, c'est que vous n'êtes pas seul. Un [rapport](https://think.storage.googleapis.com/docs/mobile-page-speed-new-industry-benchmarks.pdf) publié par Google a révélé que 70 % des pages analysées mettaient plus de 10 secondes à charger — pour une seule page.

La mauvaise nouvelle, c'est... eh bien, c'est mauvais. Ce même rapport a montré que 53 % des visiteurs quittent une page web sur mobile si elle met plus de trois secondes à charger. Cela signifie que chaque seconde où votre site échoue à charger, un client potentiel ou un visiteur part.

Heureusement, il reste encore une bonne nouvelle : le format de fichier WebP peut compresser vos images à une taille encore plus petite qu'un fichier JPG, avec presque aucune réduction de qualité, rendant votre site plus de deux fois plus rapide. Et surtout, avec [moins de 0,1 %](https://w3techs.com/technologies/details/im-webp/all/all) des sites optimisant leurs images avec WebP (plus d'informations sur le pourquoi plus tard), vous pouvez prendre un réel avantage sur vos concurrents.

![Image](https://cdn-media-1.freecodecamp.org/images/mvGhZR1OX-umYlZKZVFQ7zdwUL-XJCva4zev)

#### **Revenons en arrière : qu'est-ce que WebP ?**

WebP est un format d'image qui offre une compression avec et sans perte pour les images sur Internet en utilisant un codage prédictif pour encoder une image. Il a été introduit en 2010 et est actuellement développé et soutenu par Google. Mais ce n'est pas seulement Google qui utilise WebP : Pinterest, Facebook (sur les appareils Android) et les miniatures de YouTube utilisent toutes des images WebP, ainsi que d'autres grands acteurs.

[Google affirme](https://developers.google.com/speed/webp/) qu'une image WebP sans perte est 26 % plus petite que son équivalent PNG, et qu'une image WebP avec perte est 25–34 % plus petite que son équivalent JPG (en février 2019).

Testons les images WebP. Lorsque j'ai passé mon image JPG à travers le convertisseur WebP, j'ai obtenu les résultats suivants :

* Image JPG (déjà compressée) : **279 Ko**
* WebP à 100 % sans perte : **451 Ko** *(oui, c'est plus grand — plus d'informations sur le pourquoi ci-dessous !)*
* WebP à 80 % avec perte : **156 Ko** *(56 % de la taille originale)*

![Image](https://cdn-media-1.freecodecamp.org/images/hVwZLvxBCDlFyCY27Wr5PF84vXoE9vsKtwao)
_Gauche : JPG original à 279 Ko. Milieu : WebP 100 % sans perte à 451 Ko. Droite : WebP 80 % avec perte à 156 Ko._

*(Les photos ci-dessus sont trop petites pour voir la différence ? Si vous voulez voir l'image WebP 80 % avec perte en action, rendez-vous sur [mon site web](https://www.carmenhchung.com).)*

Vous vous demandez probablement pourquoi l'image WebP sans perte est en réalité _plus grande_ que le JPG original. Cela s'explique parce que mon image originale était en fait un fichier PNG sans perte, que j'ai ensuite converti et passé à travers un compresseur d'images pour produire un fichier JPG plus petit. Lors de ce processus de compression, le convertisseur ajoute ce que l'on appelle des _artéfacts_.

Lorsque vous inversez le processus et essayez de convertir le JPG avec perte en un format sans perte (comme WebP), l'algorithme supprimera les métadonnées inutiles (bien) — mais il encodera également chaque artéfact qu'il trouve pour le reproduire pixel par pixel (mal), ce qui entraîne souvent une augmentation de la taille du fichier, sans avantage visuel. Ainsi, le fichier final sera encore plus grand que si vous l'aviez converti directement à partir du fichier PNG original !

> Astuce pro : si votre image originale est dans un format sans perte (comme PNG, BMP ou Raw), convertissez-la directement en image WebP. Ne la convertissez pas d'abord en un format avec perte (comme JPG ou GIF).

La compression avec perte (celle de droite ci-dessus) crée des images approximativement identiques à l'original : mais en raison de la compression, la taille est plus petite (et la qualité en souffre parfois — bien que dans ce cas, cela soit à peine perceptible). De plus, les images avec perte perdent leur qualité de manière irréversible — une fois que vous les avez converties en un format avec perte, vous ne pouvez pas revenir en arrière, ce qui signifie que si vous compressez plusieurs fois la même image avec perte, la qualité se dégrade à chaque fois.

> Astuce pro : si vous compressez en formats avec perte, vous devez toujours compresser l'image originale. Ne compressez pas plusieurs fois des fichiers déjà compressés, sinon vous aggraverez la dégradation de la qualité.

#### **Je ne suis pas convaincu. Montrez-moi les résultats.**

J'ai placé les trois images ci-dessus sur des pages de test autonomes et j'ai soumis les trois pages simultanément à un test de charge (un outil de benchmarking que je détaillerai dans un autre article), en simulant environ 25 utilisateurs simultanés pour voir à quelle vitesse leurs temps de réponse seraient.

Sans surprise, le fichier WebP 80 % avec perte (c'est-à-dire le plus petit) a été le plus rapide, avec un temps de réponse moyen de **5,33 secondes** pour un chargement complet ; le JPG a ensuite pris en moyenne **8,34 secondes** ; et le fichier WebP 100 % sans perte a pris en moyenne **12,28 secondes**.

Ainsi, le fichier WebP 80 % avec perte était **2,3 fois plus rapide que le fichier WebP 100 % sans perte, et 1,56 fois plus rapide que le JPG**.

Pour les sites web encore plus riches en images (comme les sites de photographie, les blogs ou les portfolios visuels), je m'attendrais à ce que la différence de vitesse de chargement soit encore plus grande.

#### **Pourquoi tout le monde n'utilise-t-il pas le format WebP pour leurs images alors ?**

En février 2019, le [support des navigateurs](https://caniuse.com/#feat=webp) pour les fichiers WebP était proche de 72 %, avec Chrome, Firefox, Opera et la dernière version d'Edge le supportant. Malheureusement, Safari et IE ne supportent pas (encore) les fichiers WebP, vous avez donc toujours besoin d'une solution de repli pour ces navigateurs — plus d'informations à ce sujet ci-dessous.

#### **D'accord, je suis intéressé. Comment implémenter WebP ?**

Tout d'abord, vous devrez convertir vos images au format WebP. Il existe plusieurs façons de le faire, notamment des convertisseurs faciles à utiliser comme [celui-ci](https://image.online-convert.com/convert-to-webp) ou [celui-là](https://convertio.co/jpg-webp/). Pour ceux qui utilisent Photoshop, vous pouvez également convertir votre image en utilisant un [plugin WebP](https://www.filecluster.com/howto/open-save-webp-image-files-photoshop/).

Alternativement, vous pouvez télécharger le convertisseur WebP de Google [ici](https://storage.googleapis.com/downloads.webmproject.org/releases/webp/index.html), qui convertit les JPG et PNG en WebP, et les fichiers WebP en PNG ou PPM. Je préfère cette option, car je fais plus confiance à la qualité de la conversion logicielle de Google, et je peux spécifier des options précises pour chaque conversion.

Par exemple, pour convertir un fichier PNG en WebP 80 % avec perte, vous pouvez exécuter `cwebp -q 80 mypicture.png -o mypicture.webp` dans le Terminal/Ligne de commande. Des instructions simples sur la façon de convertir en utilisant cette option peuvent être trouvées [ici](https://developers.google.com/speed/webp/docs/cwebp).

N'oubliez pas que, une fois que vous avez converti votre image, vous devez conserver votre fichier JPG ou PNG original, car vous en aurez besoin comme fichier de repli au cas où le navigateur de l'utilisateur ne supporte pas WebP.

#### **J'ai mes images WebP. Et maintenant ?**

Supposons que vous souhaitiez afficher votre image de manière normale en HTML (plutôt que dans une classe CSS, dont je parlerai plus tard). Pour ce faire, utilisez le code suivant (remplacez évidemment les références à `mypicture` par le nom de votre fichier image) :

`HTML :`

```
<picture>
```

```
  <source srcset="images/mypicture.webp" type="image/webp">
```

```
  <source srcset="images/mypicture.jpg" type="image/jpeg">
```

```
  <img alt="C'est mon visage" src="images/mypicture.jpg">
```

```
</picture>
```

Ce qui se passe ici, c'est que nous vérifions d'abord si le navigateur supporte la balise `<picture>`. Si c'est le cas, nous servirons l'image WebP ; sinon, nous servirons l'image JPG. Si le navigateur ne supporte même pas la balise `<picture>`, alors nous aurons un repli final avec la balise `<img>` normale.

#### **Super. Mais que faire si j'ai une image dans une classe CSS, comme une URL d'image de fond ?**

Cela nécessite un peu plus de travail.

Tout d'abord, vous devez savoir quand le navigateur d'un utilisateur _ne peut pas_ gérer vos fichiers WebP, afin de charger les fichiers JPG ou PNG de repli (qui seront dans une autre classe CSS) à la place.

Pour ce faire, j'utilise Modernizr pour détecter le type de navigateur utilisé par l'utilisateur (et donc les fonctionnalités supportées par son navigateur). Vous pouvez vous rendre sur [leur site web](https://modernizr.com/download?webp-setclasses), cliquer sur « WebP » puis sur « Build ».

![Image](https://cdn-media-1.freecodecamp.org/images/9TCRqafaUI1UAOrW9ah91D6ZtOVJL0z9BOQU)

Une fenêtre contextuelle apparaîtra — cliquez sur « Download » à côté de la commande Build.

![Image](https://cdn-media-1.freecodecamp.org/images/sh9UDh4aTKk5JAlDpG-2nlbmzK0rHY65UQVp)

Après cela, un fichier nommé `modernizr-custom.js` sera téléchargé — déplacez ce fichier dans le répertoire de votre site web (disons, votre dossier racine). Pour appeler et déclencher Modernizr, placez ceci en bas de la page HTML où vous affichez vos fichiers WebP :

`HTML :`

```
// Tout d'abord, référencez l'emplacement de votre script Modernizr téléchargé. J'ai simplement laissé le mien dans le dossier racine.
```

```
<script src="modernizr-custom.js"></script>
```

```
// Ensuite, déclenchez Modernizr pour détecter la compatibilité WebP.
```

```
<script>
```

```
  Modernizr.on('webp', function (result) {
```

```
    if (result) {
```

```
      // supporté
```

```
    } else {
```

```
      // non supporté
```

```
    }
```

```
  });
```

```
</script>
```

Modernizr appliquera maintenant automatiquement une classe `webp` ou `no-webp` à l'élément HTML (dans mon exemple, le conteneur contenant l'image), selon qu'il détecte ou non le support du navigateur pour WebP. Cela signifie que vous pouvez spécifier quelles images vous souhaitez dans votre classe CSS, en ciblant l'une de ces classes comme ceci :

`CSS :`

```
.no-webp .container {     background-image: url("mypicture.jpg"); }  
```

```
.webp .container {     background-image: url("mypicture.webp"); }
```

#### **Que se passe-t-il si l'utilisateur n'a pas activé JavaScript ?**

Oh ! Pourquoi feraient-ils cela ? (Je vous regarde, Internet Explorer !)

Modernizr repose sur l'activation de JavaScript dans le navigateur de l'utilisateur, donc pour contourner cela, vous devrez ajouter une classe HTML en haut de la page, par exemple `<html class="no-js">`.

Ensuite, ajoutez un code JavaScript qui supprimera cette classe si JavaScript est activé :

`HTML :`

```
<script>     document.documentElement.classList.remove("no-js"); </script>
```

Si JavaScript n'est pas activé, alors la classe sera automatiquement appliquée à tous les éléments HTML de votre page — et vous pourrez créer une classe `no-js` avec l'image JPG comme image de fond :

`CSS :`

```
.no-js .container {     background-image: url("mypicture.jpg"); }
```

#### **Conclusion**

Les images WebP sont relativement faciles à implémenter lorsque vous affichez simplement des images dans votre code HTML (vous n'aurez pas besoin de Modernizr ou de la classe `no-js`), mais deviennent légèrement plus chronophages lorsque vous utilisez des images dans votre CSS (par exemple, comme images de fond).

Gardez à l'esprit que le temps que met votre site web à charger a un impact direct sur le temps que vos visiteurs passeront sur votre site — et donc, affecte votre taux de conversion de prospects — donc le temps que vous passez à passer aux images WebP en vaut la peine, pour le temps supplémentaire que vos utilisateurs passeront sur votre site web.

Si vous implémentez des images WebP, faites-le-moi savoir dans les commentaires — j'adorerais savoir à quel point votre site web est plus rapide !

#### _Merci d'avoir lu ! Si vous avez aimé cet article, n'hésitez pas à cliquer sur ce bouton d'applaudissements quelques fois ( ????) pour aider les autres à le trouver._

#### _De plus, consultez mes ressources gratuites [ici](https://www.carmenhchung.com/media.html) avec tout le code (et des commentaires de code utiles) que vous pouvez copier pour implémenter des images WebP sur votre site web. ?_