---
title: 'Le meilleur format d''image pour le Web : JPEG, WEBP, HEIC ou AVIF ?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-13T15:08:57.000Z'
originalURL: https://freecodecamp.org/news/best-image-format-for-web-in-2019-jpeg-webp-heic-avif-41ba0c1b2789
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Z3SfTvHOfvZiz1mr7uOODA.jpeg
tags:
- name: Design
  slug: design
- name: image
  slug: image
- name: performance
  slug: performance
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Le meilleur format d''image pour le Web : JPEG, WEBP, HEIC ou AVIF ?'
seo_desc: 'By Anton Garcia Diaz

  After decades of the unrivaled dominance of JPEG, recent years have witnessed the
  appearance of new formats — WebP and HEIC — that challenge this position.

  These have only partial, but significant, support by major players among ...'
---

Par Anton Garcia Diaz

Après des décennies de domination sans rival du JPEG, les années récentes ont vu l'apparition de nouveaux formats — WebP et HEIC — qui remettent en question cette position.

Ces formats bénéficient d'un soutien partiel, mais significatif, de la part des principaux acteurs parmi les navigateurs web et les systèmes d'exploitation mobiles.

Un autre nouveau format d'image — AVIF — devrait faire son entrée en 2019 avec la promesse de balayer l'ensemble du web.

Dans cet article, nous commencerons par une brève révision des formats classiques, suivie d'une description de WebP et HEIC/HEIF. Nous explorerons ensuite AVIF, et terminerons par un résumé mettant ensemble tous les points principaux.

Les commentaires sur les avantages et les inconvénients s'appuient à la fois sur l'examen de rapports autorisés disponibles et sur des observations de première main lors du développement et du déploiement d'[outils pour les pipelines d'optimisation d'images dans les flux de travail ecommerce](https://abraia.me/).

### Formats d'image classiques pour le web avec un support universel

Rappelons-nous, dans l'ordre chronologique, les trois formats classiques les plus importants pour les images web.

#### **GIF**

GIF supporte la compression sans perte LZW et plusieurs frames qui nous permettent de produire des animations simples.

La limitation majeure de ce format est qu'il est limité à 256 couleurs. Cela était raisonnable à l'époque de sa création à la fin des années 80, puisque la même limitation s'appliquait aux écrans existants. Cependant, avec l'amélioration de la technologie d'affichage, il est devenu évident qu'il n'était pas adapté pour reproduire des dégradés de couleurs fluides, comme ceux que l'on trouve dans les images photographiques. Nous pouvons facilement repérer le banding de couleurs qu'il produit.

Cependant, GIF permet des animations légères avec un support universel. Cette caractéristique a maintenu le format en vie jusqu'à aujourd'hui dans des cas d'utilisation peu sensibles aux problèmes de qualité, les plus typiques étant les petites images animées avec peu ou pas de couleurs.

#### **JPEG**

Le roi des formats d'image pour le web a été développé pour supporter les flux de travail de la photographie numérique.

Avec une profondeur habituelle de 24 bits, il offre une résolution de couleur bien supérieure (à ne pas confondre avec la gamme ou le gamut) à ce que l'œil humain peut discerner. Il supporte la compression avec perte en exploitant des mécanismes connus de la vision humaine.

Nos yeux sont plus sensibles aux échelles moyennes qu'aux détails fins. Par conséquent, JPEG nous permet de discarder les détails fins (hautes fréquences spatiales), selon un facteur de qualité contrôlé. Moins de qualité signifie moins de détails préservés. De plus, nous sommes beaucoup plus sensibles aux détails avec un fort contraste de luminance qu'aux détails avec seulement un contraste chromatique.

Ainsi, JPEG recodifie internement les images RGB (Rouge, Vert et Bleu) en un canal de luminance et deux canaux de chrominance. Cela nous permet d'utiliser le sous-échantillonnage de chrominance pour discarder plus de détails uniquement dans les canaux de chrominance. Il est intéressant de noter que JPEG code les images en blocs de 8x8 pixels.

À mesure que nous réduisons le facteur de qualité et/ou appliquons un sous-échantillonnage de chrominance plus agressif, nous commençons à obtenir des artefacts croissants de ringing, de halos, de blocage ou de flou. Un problème avec JPEG est que, selon le contenu de l'image, les artefacts peuvent apparaître à différentes valeurs de facteur de qualité. La différence la plus marquée apparaît lorsque l'on compare les effets sur la photographie naturelle avec les effets sur les œuvres d'art. Puisque les œuvres d'art (formes, polices) reposent généralement sur des bords nets, elles commencent à produire des artefacts même pour de petites quantités de détails discards.

Pour les photos, JPEG offre facilement une réduction du poids du fichier d'un facteur de 10 avec des artefacts à peine perceptibles, par rapport à la compression sans perte.

#### **PNG**

Ce format graphique sans perte a été développé pour remplacer GIF, en abordant ses problèmes de banding de couleurs (et de licence). Il était nécessaire pour les images avec une quantité considérable d'œuvres d'art, pour lesquelles JPEG produisait de grands artefacts même avec des taux de compression minimaux.

Il supporte la transparence et une compression améliorée par rapport à GIF. Puisque PNG ne discarde pas d'informations, il ne produit pas d'artefacts. Bien sûr, cela se fait au détriment d'un poids d'image plus lourd en présence de nombreux dégradés de couleurs différents, par rapport à la compression avec perte.

Il réussit à exploiter une caractéristique fréquente des œuvres d'art : Contrairement à la photographie — qui présente un continuum de couleurs avec des variations subtiles — les images d'œuvres d'art présentent généralement peu de couleurs bien définies.

Ainsi, PNG compresse les images en mappant de grandes quantités de pixels à une palette discrète simple et économise beaucoup de bits en conséquence. Comparé à GIF, il offre une qualité beaucoup plus élevée avec généralement bien moins d'octets.

### Nouveaux formats avec un support partiel : WEBP et HEIC basés sur HEVC

Les mécanismes utilisés par les codecs vidéo pour compresser les flux peuvent être classés en deux types principaux : inter-frame et intra-frame. Alors que le premier exploite les redondances le long du temps, les mécanismes intra-frame se concentrent sur la réduction de la redondance à l'intérieur d'une frame donnée, sans aucune dépendance au reste. Ce mécanisme de compression peut être appliqué aux images fixes.

L'explosion du partage vidéo — avec les réseaux mobiles au cœur — et l'augmentation constante de la résolution d'affichage ont poussé les efforts sur les nouvelles normes de codage pour atteindre la plus haute efficacité possible en compression.

Ainsi, de nouveaux formats d'image émergent en tant que dérivés des nouvelles normes de codage vidéo. Ces nouveaux formats d'image offrent des ensembles de fonctionnalités plus larges que JPEG et promettent des économies pertinentes en poids de fichier avec une qualité visuelle améliorée.

#### **WEBP**

Google a développé ce format dans le but de fournir un seul format d'image capable pour le web pour traiter tous les cas d'utilisation typiques.

Importamment, il cherche à obtenir des images plus légères que JPEG, sans pénalités sur la qualité visuelle. Il utilise des opérations plus complexes — comme la prédiction de blocs — et est un dérivé du codec vidéo VP8. Il supporte la compression sans perte et, contrairement à JPEG, il permet la transparence et les animations qui peuvent combiner des images codées avec compression sans perte et avec perte.

En principe, il devrait servir de remplacement pour JPEG, PNG et GIF. Un inconvénient important a été le manque de support universel. Jusqu'à récemment, WebP avait été restreint aux logiciels soutenus par Google comme le navigateur Chrome et les applications natives Android.

Cependant, avec l'[annonce](https://www.zdnet.com/article/firefox-and-edge-add-support-for-googles-webp-image-format/) que Edge et Firefox (à l'exclusion de Firefox iOS) doivent introduire le support WebP en 2019, il gagne clairement en traction. Il est également intéressant de noter qu'Apple — Safari et iOS — ne supporte pas encore WebP.

#### **HEIC/HEIF**

Ce format apporte une évolution significative dans deux domaines différents.

Premièrement, le [conteneur de fichier supporte le plus grand ensemble de fonctionnalités parmi les formats d'image](http://nokiatech.github.io/heif/technical.html) disponibles. Il supporte, par exemple, les images multi-frames avec compression multi-frames — une fonctionnalité clé pour les images HDR, multi-focus ou multi-vues efficaces.

Deuxièmement, il supporte de nombreux types de données non-image avec une flexibilité remarquable. Actuellement, la plupart des images utilisant ce conteneur sont compressées avec un dérivé pour les images du codec vidéo H265/HEVC, développé pour gérer efficacement les résolutions 4k et 8k des écrans de dernière génération. Le codage HEVC implique des opérations plus complexes avec moins de restrictions que JPEG. Il atteint une efficacité de compression beaucoup plus élevée au coût de temps de codage légèrement plus longs — ce qui n'est pas un problème du tout dans les flux de travail web.

Comme H265, HEIC basé sur HEVC est soutenu par Apple. Il bénéficie d'un support natif dans iOS et macOS, mais — principalement en raison de problèmes de brevets et de licences — il n'est pas soutenu par les autres plateformes (Android, Windows). Même dans macOS, Safari ne le supporte pas. Les applications iOS semblent être le seul cas d'utilisation viable pour HEIC sur le web.

Une grande question se pose donc : devons-nous offrir des alternatives WEBP/HEIC et JPEG, avec des versions PNG comme solution de repli ?

Examinons chaque cas...

### Dois-je servir des dérivés WEBP ?

Google affirme que ce format produit des images beaucoup plus légères que JPEG avec une qualité comparable. Cependant, des tests indépendants ont montré que ce résultat [n'est pas cohérent selon les différentes mesures de qualité](https://research.mozilla.org/2013/10/17/studying-lossy-image-compression-efficiency/), et la réduction de poids est, dans la plupart des cas, équilibrée par une augmentation du flou.

Dans nos propres tests avec des images ecommerce, nous avons vu des économies de fichier pour WebP, mais au prix d'un flou plus important et de moins de détails. Cependant, nous avons également vu moins de risques d'artefacts de ringing et de blocage, que nous considérerions comme plus visuellement gênants que le flou.

Comme WebP manque de support de la part des navigateurs et systèmes d'exploitation Apple, nous ne recommandons généralement pas de servir des dérivés WebP en concurrence avec JPEG. De telles actions augmenteraient la complexité de la gestion des médias avec des bénéfices limités.

Cette situation changerait si Apple commençait à supporter WebP.

Si c'était le cas, alors l'ensemble de fonctionnalités étendu de WebP et les images plus légères produites pourraient valoir son utilisation, simplifiant effectivement les flux de travail de gestion des images.

Pour essayer WebP vous-même, un outil classique comme [ImageMagick](https://www.imagemagick.org/script/index.php) est une bonne option. Il permet de créer facilement des versions d'images comparables avec différents paramètres de qualité et de résolution pour WebP et JPEG. Les résultats peuvent être visualisés avec Chrome.

```
# Convertir en WEBP qualité 60
convert input.jpg -quality 60 output_60.webp
# Convertir en JPEG qualité 60
convert input.jpg -quality 60 output_60.jpg
# Convertir en WEBP qualité 60 et largeur 450px
convert input.jpg -resize 450 -quality 60 output_450_60.webp
```

Différentes combinaisons de qualité et de résolution auront des effets différents dans chaque cas, car les algorithmes de compression fonctionnent différemment. Donc, vérifiez vos tailles de fichier pertinentes sur plusieurs images pour avoir une idée des économies potentielles et des meilleurs paramètres pour un cas d'utilisation donné.

### Dois-je servir des dérivés HEIC ?

L'avantage de HEIC (par rapport à JPEG) est clair. La réduction de poids est systématiquement significative — environ 50 % — sans perte de qualité visuelle. L'ensemble de fonctionnalités supporté est simplement impressionnant.

Le problème est à nouveau le support des navigateurs et des systèmes d'exploitation.

Étant donné les problèmes de brevets de HEVC et les royalties importantes associées, nous pouvons nous attendre à ce que le support reste restreint à ceux du monde Apple. Puisque JPEG est déjà efficace pour compresser les images, les 50 % de quelque chose de petit pourraient ne pas valoir assez pour ajouter de la complexité à notre flux de travail de traitement d'images.

Certains cas utilisant de grandes images, avec un intérêt majeur pour la qualité visuelle ET avec un grand pourcentage d'appareils Apple dans leur base d'utilisateurs devraient envisager de servir ce format.

Effectuer des tests avec HEIC est très facile avec un Mac. Preview nous permet d'exporter une image en HEIC et JPEG avec différentes valeurs de qualité et différentes résolutions. Vous n'aurez pas besoin de faire beaucoup de tests pour voir la différence claire et systématique entre eux.

![Image](https://cdn-media-1.freecodecamp.org/images/XRTmUucDfTZm0iiTDvreSpEauY-ymS3dP1Bb)
_Exporter en HEIC dans Preview_

Si vous voulez essayer quelque chose de plus flexible qui peut être intégré dans un flux de travail de traitement d'images web, [GPAC](https://gpac.wp.imt.fr/2017/06/09/gpac-support-for-heif/) vaut le coup d'œil.

### **Et AVIF ?**

AVIF est le dernier de nos concurrents.

Comme WebP et HEIC basé sur HEVC, AVIF est un dérivé des derniers efforts en matière de normes vidéo. Il utilise également des conteneurs HEIF et supporte donc un ensemble de fonctionnalités complet, englobant tous les principaux formats disponibles. Il apporte une efficacité de compression beaucoup plus élevée, héritée de l'utilisation des mécanismes de codage intra-frame AV1. Ces avantages rendent ce format convaincant.

Un autre avantage significatif vient de l'[Alliance for Open Media](https://aomedia.org/), le grand consortium derrière son développement en tant qu'approche entièrement ouverte, avec une licence ouverte, exemptée de royalties. Des acteurs majeurs comme Google, Netflix, Adobe, Mozilla, Microsoft, Facebook et Amazon — principaux acteurs de la scène graphique et vidéo web — soutiennent ce nouveau format et font un cas pour une adoption rapide et large, tant dans les logiciels que dans les matériels. Alors que le format de flux a été figé en mars 2018 [avec un code de référence disponible](https://aomedia.googlesource.com/aom/+/master/av1), les premiers appareils avec support matériel pour AV1 sont attendus pour la fin de 2019.

Au moment de la rédaction de cet article, l'implémentation open source de AV1 disponible peut encore être considérée comme expérimentale et non adaptée à la production.

### **Résumé**

JPEG restera le format roi pour les images générales sur le web en 2019, et PNG restera l'option par défaut pour les images avec une quantité significative d'œuvres d'art.

La raison ? Le support universel.

Tout ce qui ouvre une image ouvrira JPEG ou PNG en 2019, tout comme les années et décennies précédentes ! Il ne fait donc aucun doute que ces formats universels resteront en place encore quelque temps.

Les avantages de WebP restent controversés. Un avantage clair de WebP est sa capacité à remplacer également PNG, simplifiant potentiellement les flux de travail de traitement d'images. Cependant, sans support universel, cet avantage disparaît. Cela pourrait changer uniquement si Apple change d'avis et que WebP obtient enfin une adoption universelle, alors il pourrait être utilisé comme remplacement pour toutes les images JPEG, PNG et GIF.

En revanche, les images HEIC basées sur HEVC offrent des avantages clairs, en particulier pour les grandes résolutions. Si le trafic des utilisateurs iOS est pertinent pour un site web avec de grandes images lourdes, il peut être intéressant d'envisager de servir des alternatives HEIC pour eux, avec des améliorations potentielles de l'UX, en particulier pour les connexions mobiles lentes. En plus d'accélérer, HEIC assure la qualité, presque exempt des artefacts de blocage et de ringing gênants qui affligent les politiques JPEG agressives.

Bien qu'AVIF soit attendu pour 2019, le support et l'adoption prendront du temps. Mais sans aucun doute, c'est un format d'image à garder sous votre radar pour un avenir proche.

Bien sûr, l'utilisation d'un service cloud — via une [API d'optimisation d'images](https://abraia.me/docs/api/) ou un [plugin d'optimisation d'images](https://medium.com/abraia/best-image-optimization-plugins-for-wordpress-benchmarked-20508f9a0a57) — restera toujours une alternative facile et directe pour accomplir le travail.