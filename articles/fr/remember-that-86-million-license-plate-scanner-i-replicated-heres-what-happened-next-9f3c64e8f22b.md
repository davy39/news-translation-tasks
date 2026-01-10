---
title: Vous vous souvenez du scanner de plaques d'immatriculation à 86 millions de
  dollars que j'ai reproduit ? J'ai coincé quelqu'un avec.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-24T05:14:14.000Z'
originalURL: https://freecodecamp.org/news/remember-that-86-million-license-plate-scanner-i-replicated-heres-what-happened-next-9f3c64e8f22b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HwbifravoUSXmONi7UUemg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Machine Learning
  slug: machine-learning
- name: politics
  slug: politics
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Vous vous souvenez du scanner de plaques d'immatriculation à 86 millions
  de dollars que j'ai reproduit ? J'ai coincé quelqu'un avec.
seo_desc: 'By Tait Brown

  A few weeks ago, I published what I thought at the time was a fairly innocuous article:
  How I replicated an $86 million project in 57 lines of code.

  I’ll admit — it was a rather click-bait claim. I was essentially saying that I’d
  reprod...'
---

Par Tait Brown

Il y a quelques semaines, j'ai publié ce que je pensais être à l'époque un article assez anodin : [Comment j'ai reproduit un projet de 86 millions de dollars en 57 lignes de code](https://medium.freecodecamp.org/how-i-replicated-an-86-million-project-in-57-lines-of-code-277031330ee9).

Je l'admets — c'était une affirmation plutôt racoleuse. Je disais essentiellement que j'avais reproduit la même technologie de balayage et de validation de plaques d'immatriculation pour laquelle la police de Victoria, en Australie, venait de payer 86 millions de dollars.

Depuis lors, les réactions ont été écrasantes. Mon article a reçu plus de 100 000 visites le premier jour et, au dernier pointage, se situe aux alentours de 450 000. J'ai été invité à m'exprimer sur des stations de radio locales et lors d'une conférence en Californie. Je pense que quelqu'un a dû confondre Victoria, AU avec Victoria, C.-B.

Bien que j'aie poliment décliné ces offres, j'ai rencontré divers développeurs locaux et de grandes entreprises autour d'un café. C'était incroyablement excitant.

La plupart des lecteurs l'ont vu pour ce qu'il était : une preuve de concept pour susciter une discussion sur l'utilisation de la technologie open source, les dépenses gouvernementales et le désir d'un homme de construire des trucs cool depuis son canapé.

Les puristes ont souligné le manque de formation, de support et les habituels surcoûts de l'informatique d'entreprise, mais cela ne vaut pas la peine de s'y attarder. Je préfère consacrer ce post à l'examen de mes résultats et à la manière dont d'autres peuvent s'y prendre pour améliorer leur propre précision.

Avant d'entrer trop profondément dans les résultats, j'aimerais revenir sur un point qui, selon moi, a été perdu dans le [post original](https://medium.freecodecamp.org/how-i-replicated-an-86-million-project-in-57-lines-of-code-277031330ee9). Le concept de ce projet a débuté de manière totalement distincte du projet BlueNet à 86 millions de dollars. Ce n'était en aucun cas une tentative de contrefaçon.

Tout a commencé par l'idée persistante que, puisque [OpenCV](https://opencv.org/) existe et que le site web de VicRoads propose des vérifications de plaques d'immatriculation, il devait y avoir un moyen de combiner les deux ou d'utiliser quelque chose de mieux.

Ce n'est qu'au moment de commencer ma rédaction que je suis tombé sur BlueNet. Bien que la découverte de BlueNet et de son prix m'ait donné un excellent angle éditorial, le code était déjà écrit. Il y avait forcément des incohérences entre les deux projets.

Je pense également qu'une partie de la raison pour laquelle cela a explosé est le timing opportun d'un rapport sur les [dépenses informatiques gouvernementales excessives en Australie](http://www.abc.net.au/news/2017-08-28/federal-governments-$10bn-bill-rivals-newstart-cost/8849562). La facture informatique du gouvernement fédéral est passée de 5,9 milliards de dollars à 10 milliards de dollars, et elle a offert une valeur douteuse pour ce dépassement. Les chercheurs en médias qui m'ont contacté n'ont pas tardé à lier les deux, mais ce n'est pas quelque chose que je m'empresse d'encourager.

#### **Un avertissement**

Dans un esprit de transparence, je dois déclarer quelque chose qui manquait également dans le post original. Mon ancien employeur a réalisé de petits projets informatiques (moins d'un million de dollars) pour la police de Victoria et d'autres organismes d'État. En conséquence, j'ai subi des contrôles de police et rempli les formulaires requis pour devenir un contractant de VicPol.

Cela pourrait impliquer que j'ai un compte à régler ou des connaissances d'initié spécifiques, mais au contraire, je suis fier des projets que nous avons livrés. Ils ont été réalisés à la fois dans les délais et dans le budget.

### Visualisation des résultats

Ce qui suit est une représentation vidéo de mes résultats, composée dans After Effects pour s'amuser un peu. J'ai enregistré diverses séquences de test, et celle-ci était le clip le plus réussi.

J'entrerai dans les détails sur les configurations de caméra idéales, les régions de détection et plus encore après la vidéo. Cela vous aidera à mieux comprendre pourquoi cette vidéo iPhone que j'ai prise à travers le pare-brise était une meilleure vidéo qu'une Contour HD orientée sur le côté.

### Un dilemme éthique

Si vous avez vu l'image d'en-tête de cet article ou regardé la vidéo ci-dessus, vous avez peut-être remarqué un développement très intéressant : **j'ai coincé quelqu'un**.

Plus précisément, j'ai surpris quelqu'un conduisant un véhicule dont l'immatriculation avait été annulée en 2016. Cela a pu arriver pour de nombreuses raisons, la plus innocente étant une pratique de revente douteuse.

Parfois, lorsqu'une vente privée de véhicule n'est pas faite dans les règles de l'art, l'acheteur et le vendeur peuvent ne pas effectuer le transfert officiel de l'immatriculation. Cela permet à l'acheteur d'économiser des centaines de dollars, mais le véhicule reste immatriculé au nom du vendeur. Il n'est pas rare qu'un vendeur annule ensuite l'immatriculation et reçoive un remboursement ad hoc des mois restants, valant également des centaines de dollars.

Alternativement, le conducteur du véhicule pourrait très bien être le criminel que nous soupçonnons.

Ainsi, bien que j'aie plaisamment nommé le projet plate-snitch (le mouchard de plaques) lors de sa configuration sur mon ordinateur, je suis maintenant confronté au dilemme de savoir s'il faut signaler ce que j'ai vu.

En fin de compte, le conducteur a été détecté à l'aide d'un prototype d'un appareil réservé à la police. Mais conduire avec une immatriculation de 2016 (annulée, pas expirée) est un acte très délibéré. Hmm.

### Retour aux résultats

Parmi les nombreuses réactions à mon article, un nombre important était assez littéral et dubitatif. Puisque j'ai dit que j'avais *reproduit* le logiciel, ils ont affirmé que je devais avoir un centre de support, des garanties et des manuels de formation. L'un d'eux a même tenté de reproduire mes résultats et a rencontré les inévitables obstacles de la qualité d'image et du matériel source.

À cause de cela, certains ont insinué que j'avais trié mes images sources sur le volet. À cela, je ne peux que répondre : « Eh bien, évidemment. »

Lorsque j'ai construit ma preuve de concept initiale (encore une fois, en me concentrant sur la validation d'une idée, pas sur la reproduction de BlueNet), j'ai utilisé un petit échantillon de moins de dix images. Étant donné que la configuration de la caméra est l'un des facteurs les plus importants, sinon *le* plus important, en [ALPR,](http://www.theiacp.org/ALPR) je les ai sélectionnées pour leurs caractéristiques idéales qui améliorent la reconnaissance.

Au bout du compte, il est très simple de prendre une preuve de concept fragile et de la briser. La véritable innovation et le défi consistent à prendre une preuve de concept et à *la faire fonctionner*. Tout au long de ma carrière professionnelle, de nombreux développeurs seniors m'ont dit que certaines choses ne pouvaient pas être faites ou du moins pas dans des délais raisonnables. Parfois, ils avaient raison. Souvent, ils étaient simplement réticents à prendre des risques.

> « Rien n'est impossible jusqu'à ce que ce soit prouvé. »

Beaucoup de gens déforment cette citation, et vous en avez peut-être déjà vu ou entendu l'une des incarnations. Pour moi, elle résume parfaitement un état d'esprit de développement sain, dans lequel tester et valider des idées est presque obligatoire pour les comprendre.

### Configurations de caméras ALPR optimales

Ce projet est si excitant et différent pour moi car il possède une mesure de succès claire — si le logiciel reconnaît la plaque ou non. Cela ne peut se produire qu'avec une combinaison de solutions matérielles, logicielles et réseau. Après avoir publié mon article original, des personnes vendant des caméras ALPR m'ont rapidement proposé des conseils.

#### Zoom optique

La solution la plus évidente avec le recul est l'utilisation d'un [zoom optique](https://www.digitaltrends.com/photography/digital-cameras-digital-zoom-vs-optical-zoom/). Bien que j'explore d'autres facteurs importants ci-dessous, aucun n'entraîne une augmentation aussi nette de la reconnaissance que celui-ci. En général, les solutions ALPR professionnelles sont décalées d'un certain angle, orientées vers l'endroit où se trouvera la plaque d'immatriculation et zoomées sur la zone pour maximiser la clarté.

Cela signifie que **plus il y a de zoom, plus il y a de pixels avec lesquels travailler**.

Toutes les caméras que j'avais à ma disposition étaient à focale fixe. Elles comprenaient :

* Une caméra d'action Contour HD. Elles sont sorties en 2009, et j'utilise la mienne pour enregistrer mon trajet à vélo et pour revoir l'expérience de mort imminente de chaque semaine.
* Un Fujifilm X100S (célèbre pour son objectif fixe à focale fixe)
* Mon iPhone 6+

Le test présenté a été enregistré sur mon téléphone. Ma seule méthode pour reproduire un zoom optique a été d'utiliser une application pour enregistrer en 3K au lieu de 1080p, puis de zoomer et de recadrer numériquement. Encore une fois, plus de pixels avec lesquels travailler.

#### Angle et positionnement

L'angle de vue de 30**°** est souvent cité comme la norme pour une reconnaissance idéale des plaques. C'est incroyablement important quand on apprend que BlueNet utilise un réseau de caméras. Cela prend également tout son sens quand on considère ce qu'une caméra frontale verrait généralement — pas grand-chose.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tVk-4iB99Y65ILWrsxbWmw.gif)
_Ce qu'une caméra ALPR frontale voit — pas grand-chose._

Si je devais deviner, je dirais qu'un réseau principalement orienté vers l'avant serait la configuration idéale. Il consisterait en une seule caméra pointée droit devant comme ci-dessus, deux décentrées à 30**°** de chaque côté, et une seule caméra orientée vers l'arrière. L'intérêt d'avoir la plupart des caméras pointées vers l'avant viendrait de l'augmentation du temps de réaction si le véhicule circule dans la direction opposée. Cela permettrait un balayage, un traitement et un demi-tour plus rapides que si les caméras orientées vers l'arrière repéraient un véhicule suspect déjà dix mètres après le véhicule de police.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sQ2gt2ChTKJExl8spIpo6w.png)
_Un réseau de quatre caméras devrait être incliné de manière similaire à ceci. Icônes de [Freepik](http://www.freepik.com/" rel="noopener" target="_blank" title=")._

#### Un stabilisateur (Gimbal)

Lors du montage de la vidéo, j'ai pensé à stabiliser la séquence. Au lieu de cela, j'ai choisi de montrer le trajet cahoteux tel qu'il était. Ce que vous avez vu, c'est moi tenant mon téléphone près du pare-brise pendant que ma femme conduisait. Admirez cette méthode scientifique rigoureuse.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VSdNQ8RAcaH6Yy2boa5Xqw.gif)
_Toute version prête pour la production d'un ALPR monté sur véhicule a besoin d'une forme de stabilisation. Pas d'une main._

### D'autres facteurs importants

#### Fréquence d'images

La tentative de reproduction de mi-projet et mes enregistrements depuis lors ont exploré la même idée fausse selon laquelle la fréquence d'échantillonnage des images ALPR pourrait être liée au succès. D'après mon expérience, cela n'a fait que gaspiller des cycles. Au contraire, ce qui est incroyablement important, c'est la vitesse d'obturation créant des séquences nettes et précises qui alimentent bien l'algorithme.

Mais je testais aussi des séquences à vitesse assez basse. Au maximum, deux véhicules se croisant dans une zone à 60 km/h créaient un [différentiel](http://www.mathwords.com/d/differential.htm) de 120 km/h. BlueNet, en revanche, peut fonctionner jusqu'à un prétendu 200 km/h.

Comme moyen de résoudre ce problème, un collègue a suggéré la détection d'objets et le traitement hors bande. Identifier un véhicule et dessiner un cadre de délimitation (bounding box). Attendre qu'il entre dans l'angle de reconnaissance et le zoom idéaux. Puis prendre une rafale de photos pour un traitement asynchrone.

J'ai cherché à utiliser OpenCV (node-opencv) pour la reconnaissance d'objets, mais j'ai trouvé que quelque chose de plus simple comme la détection de visage prenait entre 600 et 800 ms. Non seulement ce n'est pas idéal pour mon utilisation, mais c'est assez médiocre en général.

Le train de la hype [TensorFlow](https://www.tensorflow.org/) vient à la rescousse. Capable de s'exécuter sur l'appareil, il existe des exemples de [projets](https://github.com/MarvinTeichmann/KittiBox) identifiant plusieurs véhicules par image à un rythme étonnant de 27,7 fps. [Cette version](https://github.com/balancap/SDC-Vehicle-Detection) pourrait même exposer des estimations de vitesse. Légalement sans valeur, mais peut-être utile dans le maintien de l'ordre quotidien (pas de benchmark fps dans le readme).

Pour mieux expliquer comment la reconnaissance de véhicules haute performance pourrait se coupler avec des techniques ALPR plus lentes, j'ai créé une autre vidéo dans After Effects. J'imagine que les deux travaillant main dans la main ressembleraient à quelque chose comme ceci :

#### Fréquence d'images vs vitesse d'obturation

Une manifestation différente de la *fréquence d'images* est largement influencée par la vitesse d'obturation, et plus spécifiquement, les problèmes d'obturateur roulant (*rolling shutter*) qui affligent les enregistreurs vidéo numériques anciens ou bas de gamme. Ce qui suit est un instantané d'une séquence Contour HD. Vous pouvez voir qu'à seulement 60 km/h, le problème de rolling shutter rend la séquence plus ou moins inutilisable d'un point de vue ALPR.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uCdnYdomqAQBZYMJjZEI_A.png)
_Problèmes de rolling shutter sur une Contour HD à 60 km/h._

L'ajustement de la fréquence d'images sur la Contour HD et sur mon iPhone n'a pas entraîné de réduction notable de la distorsion. En théorie, une vitesse d'obturation plus élevée devrait produire des images plus claires et plus nettes. Elles deviendraient de plus en plus importantes si vous deviez poursuivre le benchmark de 200 km/h de BlueNet. Moins de flou et moins de distorsion due au rolling shutter mèneraient idéalement à une meilleure lecture.

#### Version Open ALPR

L'une des découvertes les plus intéressantes a été que la version node-[openalpr](https://github.com/openalpr/openalpr) que j'utilisais est à la fois obsolète et loin d'être aussi puissante que leur solution propriétaire. Bien qu'une exigence d'open source ait certainement été un facteur, il était étonnant de voir avec quelle précision la version cloud pouvait lire avec succès des images sur lesquelles je ne pouvais même pas identifier de plaque.

#### Données d'entraînement ALPR par pays

J'ai également découvert que le package node-openalpr principal utilise par défaut le traitement pour les États-Unis sans aucun moyen de le modifier. Vous devez récupérer le fork de quelqu'un d'autre qui vous permet ensuite de fournir un paramètre de pays supplémentaire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*I0t_Xoyayj3sMwLs-px3Pg.png)
_Les plaques australiennes fines ont-elles besoin de leur propre détection de pays séparée des plaques australiennes régulières ?_

Mais cela n'aide pas toujours. En utilisant l'algorithme américain par défaut, j'ai pu produire le plus grand nombre de résultats. Spécifier le jeu de données australien a en fait réduit de moitié le nombre de lectures de plaques réussies, et il n'a réussi à en trouver qu'une ou deux que l'algorithme américain ne pouvait pas. Fournir le jeu séparé « Australian Wide Plate » a encore réduit de moitié le compte et n'a introduit qu'une seule plaque supplémentaire.

Il y a clairement beaucoup à désirer en ce qui concerne les jeux de données basés sur l'Australie pour l'ALPR, et je pense que le nombre impressionnant de styles de plaques disponibles à Victoria est un facteur contributif.

![Image](https://cdn-media-1.freecodecamp.org/images/1*K0v8vubrzykpVRk9rpx0qQ.png)
_Bonne chance avec ça._

#### Déformations planaires

Open ALPR est livré avec un outil particulier pour réduire l'impact de la distorsion provenant à la fois de l'angle de la caméra et des problèmes de rolling shutter. La déformation planaire (*planar warp*) fait référence à une méthode dans laquelle des coordonnées sont transmises à la bibliothèque pour incliner, translater et faire pivoter une image jusqu'à ce qu'elle ressemble de près à une plaque vue de face.

Dans mon expérience de test limitée, je n'ai pas pu trouver de déformation planaire qui fonctionnait à toutes les vitesses. Quand on considère le rolling shutter, il est logique que la distorsion augmente proportionnellement à la vitesse du véhicule. J'imagine que fournir des données de vitesse d'accéléromètre ou de GPS comme coefficient pourrait fonctionner. Ou, vous savez, se procurer une caméra qui n'est pas complètement médiocre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kpJTyMZdn4tjoTDMHEqsuA.png)
_L'outil de déformation planaire fourni avec Open ALPR_

### Ce que font les autres dans l'industrie

De nombreux lecteurs m'ont contacté après le dernier post pour partager leurs propres expériences et idées. L'une des solutions les plus intéressantes qui m'a été partagée est celle d'[Auror](https://www.auror.co/) en Nouvelle-Zélande.

Ils utilisent des caméras ALPR fixes dans les stations-service pour signaler les personnes qui volent de l'essence. En soi, ce n'est pas particulièrement nouveau ou révolutionnaire. Mais lorsqu'elles sont couplées à leur réseau, elles peuvent automatiquement déclencher une alerte lorsque des délinquants connus sont revenus ou ciblent des stations-service dans la zone.

Des développeurs indépendants en Israël, en Afrique du Sud et en Argentine ont montré un intérêt pour la construction de leurs propres versions bricolées de BlueNet. Certains s'en sortiront probablement mieux que d'autres, car des endroits comme Israël utilisent des plaques d'immatriculation à sept chiffres sans caractères alphabétiques.

### Points clés à retenir

Il y a tout simplement trop de choses que j'ai apprises au cours des dernières semaines de tâtonnements pour tout faire tenir dans un seul post. Bien qu'il y ait eu de nombreux détracteurs, j'apprécie vraiment le soutien et les connaissances qui m'ont été envoyés.

Il y a beaucoup de défis auxquels vous ferez face en essayant de construire votre propre solution ALPR, mais heureusement, beaucoup d'entre eux sont des problèmes déjà résolus.

Pour mettre les choses en perspective, je suis un designer et un développeur front-end. J'ai passé environ dix heures sur les séquences et le code, huit autres sur la production vidéo, et au moins dix autres sur les seuls articles. J'ai accompli ce que j'ai fait en montant sur les épaules de géants. J'installe des bibliothèques construites par des gens intelligents et j'ai profité des conseils de personnes qui vendent ces caméras pour gagner leur vie.

La question à 86 millions de dollars demeure — si l'on peut construire une solution bricolée qui fait un travail correct en montant sur les épaules de géants, combien d'argent supplémentaire faut-il investir pour faire un travail vraiment, *vraiment* excellent ?

Ma solution n'est même pas dans le même système solaire que le scanner précis à 99,999 % que certains commentateurs sur Internet semblent attendre. Mais d'un autre côté, BlueNet n'a qu'à atteindre un objectif de précision de 95 %.

Donc, si 1 million de dollars vous permet d'atteindre 80 % de précision, et peut-être 10 millions de dollars vous amènent à 90 % — quand arrêtez-vous de dépenser ? De plus, étant donné que la technologie a des applications commerciales prouvées ici en Océanie, combien d'argent des contribuables devrait encore être versé dans une solution propriétaire et fermée alors que des startups locales pourraient en bénéficier ? L'Australie est censée être une « nation de l'innovation » après tout.