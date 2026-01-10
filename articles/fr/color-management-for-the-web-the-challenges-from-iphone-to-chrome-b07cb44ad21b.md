---
title: 'Comment gérer les couleurs dans vos images et vidéos : dernières tendances
  et meilleures pratiques'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-25T18:15:07.000Z'
originalURL: https://freecodecamp.org/news/color-management-for-the-web-the-challenges-from-iphone-to-chrome-b07cb44ad21b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UQygvO5FoRqMZuzlPO_4yg.jpeg
tags:
- name: Design
  slug: design
- name: Photography
  slug: photography
- name: technology
  slug: technology
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: 'Comment gérer les couleurs dans vos images et vidéos : dernières tendances
  et meilleures pratiques'
seo_desc: 'By Anton Garcia Diaz

  During the last world football cup, few people knew that only the flags of Argentina
  and France out of the top 10 teams could be accurately displayed on a standard HDTV.
  All the remaining flags colors were clearly out of gamut. T...'
---

Par Anton Garcia Diaz

Lors de la dernière Coupe du monde de football, peu de gens savaient que seuls les drapeaux de l'Argentine et de la France parmi les 10 meilleures équipes pouvaient être affichés avec précision sur un téléviseur HD standard. Toutes les autres couleurs des drapeaux étaient clairement [hors gamme](https://dot-color.com/2018/06/14/2018-world-cup-watching-in-4k-hdr-makes-a-difference/). C'est-à-dire que les écrans standards n'étaient pas capables de reproduire correctement les couleurs. Seuls les fans utilisant des écrans à large gamme pouvaient voir leurs couleurs dans une diffusion 4K HDR.

En ce qui concerne un flux de travail web, cela est beaucoup plus complexe que les propriétés d'affichage. Les textures, la saturation, la teinte ou la luminosité peuvent être bien plus importantes dans d'autres industries que dans le football — pensez simplement à la mode ou à l'imagerie artistique dans le commerce électronique. Dans de tels cas, une gestion propre des couleurs est essentielle pour déployer des pipelines de traitement et d'optimisation d'images et de vidéos sains et fiables.

Cependant, la gestion des couleurs dans le commerce électronique et en général dans les flux de travail web peut se révéler être un problème délicat. Mon expérience récente avec des équipes complexes de commerce électronique impliquant des photographes, des retoucheurs et des devops pour déboguer et déployer des solutions d'[optimisation d'images et de vidéos](https://abraia.me) ne fait que renforcer cette idée.

Dans cet article, je passe brièvement en revue les concepts de base impliqués dans la gestion des couleurs, les meilleures pratiques et les défis posés par les dernières tendances en matière de technologie d'affichage.

### La couleur dans l'œil humain

Les humains ayant une vision des couleurs saine disposent de trois types de détecteurs de couleur dans la rétine. Chacun de ces types de détecteurs répond avec des intensités différentes aux couleurs spectrales, du rouge au violet. Par conséquent, toute couleur physique que nous percevons peut être représentée comme la combinaison de trois primaires chromatiques.

Ce fait nous a permis — il y a près de 90 ans — de définir la première norme de [colorimétrie](https://medium.com/hipster-color-science/a-beginners-guide-to-colorimetry-401f1830b65a) pour convertir les grandeurs physiques de la lumière en une représentation numérique uniquement liée aux couleurs. Elle a posé les bases pour représenter avec précision toute couleur (de la lumière atteignant l'œil) par un simple tableau de trois nombres.

### Appareils photo et écrans

Les appareils photo numériques et les écrans ont été conçus pour transmettre des images de scènes qu'un œil humain est capable de voir comme s'il était là, en les regardant. Ainsi, les appareils photo capturent une représentation trichromatique de la scène et la codent dans un fichier numérique.

Pour ce faire, les appareils photo ont _simplement_ :) trois types de détecteurs de lumière (R, G et B) comme notre rétine. De même, les écrans transforment les valeurs numériques en signaux trichromatiques qui pilotent la génération de lumière pour recréer l'image stockée dans un fichier numérique. Pour ce faire, les écrans ont _simplement_ :) trois types d'émetteurs de lumière (R, G et B).

Cela semble facile : l'appareil photo imite l'œil et l'écran projette de la lumière pour imiter la scène, la transmettant finalement à l'œil, n'importe quand, n'importe où.

Mais il y a...

### Quelques problèmes fondamentaux

Certains liés à la physique et d'autres à la perception.

#### Nécessité de calibrer

Pour commencer, les sensibilités spectrales des trois détecteurs d'un capteur d'appareil photo sont différentes — très différentes en effet — de celles des détecteurs de lumière de notre œil (les détecteurs de notre œil ne sont pas R, G et B). De plus, différents capteurs d'appareils photo présentent des comportements assez différents (leurs R, G et B sont différents). La perception des couleurs est clairement non linéaire avec des grandeurs physiques comme l'intensité de la lumière. Mais les capteurs sont généralement linéaires avec l'intensité de la lumière.

En fin de compte, cela signifie que pour fournir des représentations de couleurs précises, les appareils photo doivent être calibrés. Le calibrage est effectué en prenant une image d'un motif de couleurs. Un profil de couleur est ensuite créé pour transformer la réponse du capteur en une représentation standard de la couleur. Mais cela doit être fait pour différents éclairages.

En termes simples, si nous cherchons une fidélité véritable des couleurs, nous devrions calibrer pour corriger la couleur pour chaque nouvelle scène ! Et tout léger changement d'éclairage signifie que la scène a également changé. Heureusement, selon le besoin spécifique de précision et la flexibilité du flux de travail, [les exigences de calibrage peuvent être assouplies](https://www.dpreview.com/articles/6497352654/get-more-accurate-color-with-camera-calibration-).

Quelque chose de similaire se produit avec les écrans, mais dans l'autre sens. Ils traduisent les couleurs codées dans les fichiers d'image en lumière émise. De légères variations dans la quantité de lumière émise ont un impact sur la couleur effectivement affichée.

C'est pourquoi les écrans professionnels doivent être calibrés de temps en temps. La lumière émise pour certaines primaires est vérifiée et un profil de couleur d'écran est créé. Ce profil est utilisé pour transformer les valeurs de pixels stockées en lumière réelle avec la couleur souhaitée. Il va sans dire que les écrans des utilisateurs ne sont pas calibrés, mais ils ont généralement un profil de couleur d'usine à la place.

Nous devons reconnaître que la technologie LED actuelle a grandement limité la variation des propriétés de couleur entre différentes unités du même modèle d'écran et également dans le même écran au fil du temps.

#### Toujours... des tours de perception

Si tout cela ne suffisait pas, notre cerveau excelle dans l'assurance de la constance des couleurs sous différents éclairages. Pour ce faire, une variété de mécanismes ajustent constamment la perception afin de correspondre à la couleur attendue en fonction du contexte de la scène. Cela est fait indépendamment des vraies valeurs de la couleur physique. Vous pouvez sélectionner les valeurs RGB numériques en A et B dans cette illusion classique (vérifiez [l'original ici](https://upload.wikimedia.org/wikipedia/commons/b/be/Checker_shadow_illusion.svg), puisque Medium altère l'image).

![Image](https://cdn-media-1.freecodecamp.org/images/XO28ZzoXDgz4FUWSHEBWssaOUkvX8GyGqbeO)
_[constance des couleurs](http://illusionoftheyear.com/cat/top-10-finalists/2018/" rel="noopener" target="_blank" title="">Notre cerveau trompe notre perception</a> pour assurer <a href="https://en.wikipedia.org/wiki/Color_constancy" rel="noopener" target="_blank" title=") sous des conditions d'éclairage variables_

Ils sont exactement les mêmes : l'écran envoie la même lumière depuis chacun d'eux. Même après avoir su cela, vous verrez A plus sombre que B. Je le vois alors que j'écris ceci. Une telle perception trompeuse est une raison puissante pour de nombreux photographes d'ajuster les couleurs à la main plutôt que d'utiliser une référence de scène calibrée.

### Gestion des couleurs

Cependant, les choses peuvent encore empirer, bien pire. À ce stade, nous devrions avoir remarqué que parler de couleur avec le même langage est important si nous voulons rester cohérents. Pour accomplir ce besoin, nous devons gérer la couleur. En d'autres termes, notre logiciel doit être géré en couleur. Un échec à gérer la couleur dans un flux de travail web compromettra la cohérence de l'expérience utilisateur.

Dans cet objectif, différents espaces colorimétriques ont été développés. Chaque espace colorimétrique vise à supporter un cas d'utilisation de la meilleure manière possible. Trois exemples de cas d'utilisation sont :

* technologie d'affichage moyenne
* impression de photos
* vidéo et cinéma 4K HDR

Chaque espace colorimétrique a un profil de couleur associé pour interpréter les valeurs RVB stockées dans un fichier. Il existe de nombreux outils pratiques pour vérifier l'espace colorimétrique d'une image. Par exemple, l'outil inspecteur de Preview sur Mac.

![Image](https://cdn-media-1.freecodecamp.org/images/WnGZ7G3v-sUnTyioaxdeNRrOvAIVlZgL7taJ)

![Image](https://cdn-media-1.freecodecamp.org/images/JroDDhekpFIYRUbaredfEjut6AGSFsz24TC4)

![Image](https://cdn-media-1.freecodecamp.org/images/uh48YMtViR-W8UyPEFWC9GNsM8M8PYBewim4)
_Trois exemples de profils de couleur affichés dans Preview : un avec un profil de couleur non défini, un autre avec le profil de couleur d'un écran iMac, et un autre avec un profil de couleur sRGB_

Pour vérifier tous les détails d'une image, je trouve très pratique d'utiliser _exiftool_. Il révèle le profil de couleur, parmi de nombreuses autres métadonnées.

```
exiftool test.jpg
```

Vous devriez voir quelque chose comme ceci

![Image](https://cdn-media-1.freecodecamp.org/images/3jYcqsOx82Z31YuOaoa10s68L7kKUwYYBnqI)
_Fragment des données exif d'une image codée dans l'espace colorimétrique sRGB_

Avec les vidéos, Mediainfo est un outil pratique avec une interface graphique simple et utilisable. En plaçant le pointeur sur la zone _Vidéo_, des métadonnées détaillées de la vidéo apparaissent, y compris l'espace colorimétrique en bas.

![Image](https://cdn-media-1.freecodecamp.org/images/2YEAbslcKDEP4MmjjGrPSxKsuvwjFDt9s9hX)
_Capture de la fenêtre Mediainfo avec les informations sur le profil de couleur mises en évidence en rouge_

#### Profils de couleur classiques

**sRGB : basé sur Rec. 709**

Créé par HP et Microsoft, cet espace colorimétrique était spécialement destiné à l'Internet. Il est basé sur la norme BT.709 (ou Rec 709) pour la vidéo, ajoutant un gamma adapté aux écrans CRT. Mais il est également adapté à la perception humaine moyenne. Cela signifie qu'il fait un usage efficace de la plage dynamique.

C'est l'espace colorimétrique [universellement supporté](https://www.w3.org/Graphics/Color/sRGB.html) sur le web. Toute image (ou élément web) sans profil de couleur explicite (c'est-à-dire un espace colorimétrique non défini) sera interprétée par tout navigateur web comme étant sRGB. De plus, tout écran décent est capable de sRGB : il peut reproduire toute la gamme de couleurs sRGB. Au moment de la rédaction de cet article, c'est l'espace colorimétrique le plus sûr dans un contexte web.

Si vous assurez que TOUT votre flux de travail, du studio à la livraison web, est (bien) fait en sRGB, alors les couleurs des images sur votre web seront cohérentes pour tout le monde. Vous pouvez être confiant à ce sujet.

Au cas où vous trouvez une image non sRGB et que vous avez besoin d'une correction rapide, [Little CMS](http://www.littlecms.com/) est un outil pratique pour faire le travail. Quel que soit le profil de couleur de l'image, vous pouvez le convertir en sRGB en utilisant simplement

```
jpegicc -q100 input.jpg output.jpg
```

Cependant, rappelez-vous que la meilleure pratique est de travailler dès le début en sRGB. Lors de la transformation depuis un espace plus large, les couleurs hors gamme peuvent être traitées différemment — et dans certains cas, les couleurs peuvent être coupées tandis que dans d'autres cas, elles peuvent être lavées. Cela dépend de l'[intention de rendu](http://www.johnpaulcaponigro.com/blog/6088/rendering-intents-compared/).

L'inconvénient du sRGB est que votre gamme sera plus limitée qu'un bon pourcentage de la technologie d'affichage actuelle, ce pourcentage augmentant régulièrement. Rappelez-vous le début de cet article. À moins que vous ne soyez Français ou Argentin, il est probable que vous ne verrez pas les couleurs de votre pays correctement sur un moniteur sRGB standard. Ou dans d'autres contextes, tout le monde achetant des vêtements en ligne décide des achats en fonction de couleurs non vraies (affichées sur des écrans non calibrés !). Mais si le web reste fidèle au sRGB, le décalage vécu par chaque utilisateur sera au moins cohérent, limitant les chances de mauvaises surprises.

**Adobe RGB**

C'est l'espace colorimétrique classique utilisé dans l'industrie graphique. Il a une gamme plus large que le sRGB et couvre assez bien la gamme pertinente dans la production d'impressions. Pour travailler avec lui, vous aurez besoin d'un écran professionnel calibré à large gamme capable d'Adobe RGB.

À moins que les images ne soient destinées à être imprimées plutôt que vues sur un écran, ce profil de couleur n'a pas de sens dans un flux de travail web. Je l'inclus ici parce que je l'ai trouvé plusieurs fois dans un tel contexte.

Puisqu'il s'agit de l'espace colorimétrique préféré des photographes et des retoucheurs qui impriment leur travail, certaines personnes le considèrent comme impliquant une qualité supérieure au sRGB. Ajuster la couleur dans un espace colorimétrique et enregistrer l'image dans un autre peut finir par être une perte de temps et apporter des résultats inattendus, surtout en présence de tons fortement saturés.

Si vous êtes invité à optimiser des images vierges avec ce profil de couleur, vous êtes probablement confronté à des problèmes en amont provenant des équipes de retouche ou de studio. Les problèmes peuvent être encore pires si vous trouvez Adobe ProPhoto, avec une gamme encore plus large.

#### Nouveaux espaces colorimétriques à large gamme

**DCI-P3 (ou simplement P3).**

Cet espace colorimétrique a été adopté par Apple dans leurs écrans à large gamme depuis 2016. D'autres marques ayant récemment adopté la large gamme ont [également adopté P3](https://gizmodo.com/why-every-smartphone-screen-looks-different-1820748943). Bien que de taille similaire à Adobe RGB, il couvre une gamme différente, mieux adaptée aux écrans — technologie de projection de lumière — plutôt qu'aux impressions. C'est une étape intermédiaire vers l'UHDTV, visant les TV 8k et l'industrie cinématographique. Il est bon pour le streaming de haute qualité qui peut s'adresser aux écrans capables de 4K HDR.

L'utilisation de P3 donne des couleurs beaucoup plus riches et plus profondes, avec un vrai impact sur l'expérience utilisateur et la fidélité des couleurs. Revenons à l'exemple de la coupe du monde, P3 améliorerait grandement la fidélité des couleurs et livrerait de vraies couleurs pour la plupart des fans. Il est facile de penser à un avantage similaire pour l'imagerie dans des sites de mode, de cuisine ou de voyage.

**UHDTV /Rec. 2020**

Cet espace colorimétrique a été conçu pour les TV 4k et 8k HDR. Il apporte une gamme plus large par rapport à P3. Il contient également P3. Même pour les TV HDR, cette norme est [toujours l'avenir](https://www.rtings.com/tv/tests/picture-quality/color-volume-hdr-dci-p3-and-rec-2020). Cela n'a pas beaucoup de sens dans un flux de travail web actuel.

#### **Comparaison des gammes**

Si vous possédez un écran à large gamme et jouissez d'une vision des couleurs saine, une vérification visuelle de première main est le meilleur et le plus rapide moyen de comprendre et d'évaluer les différences entre les profils de couleur. Un bon point de départ est d'utiliser des images à large gamme spécialement préparées pour [comparer les espaces colorimétriques](https://webkit.org/blog-files/color-gamut/comparison.html).

### Bonnes pratiques avec la couleur

À moins que vous ne soyez déterminé à être un pionnier de la large gamme, la gestion des couleurs sera synonyme d'imposition de l'espace colorimétrique sRGB tout au long du pipeline de traitement d'image.

Une bonne pratique est de calibrer l'appareil photo au moins avec un [calibrage à double illuminant](http://blog.xritephoto.com/2010/05/x-rite-colorchecker-passport-dual-illuminant-profiles-part-1/). Bien sûr, l'utilisation de calibrages spécifiques pour des éclairages spécifiques sera toujours meilleure. En studio, plus vos réglages d'éclairage sont fixes (donc vous n'avez pas besoin de recalibrer), mieux c'est. Si vous prenez directement des jpegs en sRGB au lieu de RAW, votre calibrage doit être fait en sRGB.

Lorsque des iPhones sont utilisés pour prendre des photos, l'espace colorimétrique peut être un problème puisque [les appareils photo iPhone sont réglés sur DCI-P3 par défaut](https://photo.stackexchange.com/questions/98792/which-color-space-is-used-by-my-iphone-8-photos).

Juste après la prise de vue, toute correction de couleur dans un logiciel de chambre noire doit déjà être faite en sRGB. La retouche doit être faite en sRGB. Vous éviterez les problèmes liés au choix de l'intention de rendu. Il en va de même pour les œuvres d'art et les créations visuelles.

Le logiciel utilisé doit être géré en couleur. C'est le cas de la plupart des packages d'édition d'images et de graphiques. Dans le cas de la vidéo, il y avait une exception notable : les versions d'Adobe Premiere Pro antérieures à octobre 2018 [ne géraient pas la couleur](https://premierepro.net/color-management-premiere-pro/).

Si Premiere est utilisé en post-production pour le web, la meilleure pratique est d'utiliser un écran sRGB calibré. Sinon, vous pourriez finir avec des couleurs de vidéo qui changeront (généralement lavées) lorsqu'elles seront vues sur le web. C'est pourquoi tant d'utilisateurs de Premiere sur des écrans iMAC ont tendance à oversaturer leurs vidéos, afin d'éviter des résultats exportés lavés.

Si la règle sRGB est observée, les seuls risques pour la couleur dus à la génération et à l'optimisation des dérivés seront les [artéfacts de compression](https://abraia.me/docs/image-optimization/#jpeg-compression) liés à des valeurs q faibles ou à un sous-échantillonnage chromatique excessif.

Ne vous laissez pas tromper par d'anciennes publications disant que les navigateurs ne sont pas gérés en couleur. Ce n'est que la preuve que le fait d'être bien classé dans la recherche Google n'est pas une garantie d'informations précises et à jour. Tous les principaux navigateurs web (de Safari à Firefox, Edge ou Chrome) sont actuellement gérés en couleur et capables d'interpréter les profils ICC.

Si vous avez de nombreux utilisateurs iOS et macOS, vous pourriez être tenté par l'espace colorimétrique P3. Vous leur offrirez une expérience beaucoup plus réaliste, avec des couleurs bien plus vibrantes.

Mais en 2019, c'est encore un mouvement risqué. Tous les autres utilisateurs avec des écrans sRGB moyens peuvent voir des images soit lavées, soit oversaturées. L'impact dépendra toujours de l'image spécifique et du navigateur, puisque les navigateurs peuvent utiliser différentes [intentions de rendu](http://www.johnpaulcaponigro.com/blog/6088/rendering-intents-compared/). Par exemple, dans macOS — en janvier 2019 — Chrome (version 71) et Safari (version 12) utilisent l'intention perceptuelle, tandis que Firefox (version 64) utilise l'intention colorimétrique.

Servir deux versions ajustées manuellement pour tirer parti de la large gamme sur les utilisateurs iOS tout en servant toujours des images sRGB optimales... vous obligerait à ajuster les couleurs dans les deux espaces. Les avantages sont peu susceptibles de compenser le fardeau pour les équipes de photographie et de retouche.

### Résumé

Une bonne pratique du studio au web est de rester fidèle de bout en bout au même espace colorimétrique. Dans la plupart des cas (pratiquement tous), cela signifie rester fidèle au sRGB.

Lorsque différentes sources d'images et de vidéos alimentent le flux de travail, cela nécessite une sensibilisation de toutes les personnes impliquées dans la chaîne de création et de traitement d'images.

Cependant, la technologie d'affichage a récemment évolué de la course à la résolution à la course à la gamme de couleurs. Nous devons donc garder un œil sur l'espace colorimétrique P3 et la technologie utilisée par nos utilisateurs. À mesure que de plus en plus d'entre eux achètent des écrans à large gamme, le passage à des images avec un profil de couleur P3 peut commencer à avoir du sens.