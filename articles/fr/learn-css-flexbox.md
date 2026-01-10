---
title: Apprenez le CSS Flexbox dans ce cours accéléré
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-07-22T13:58:50.000Z'
originalURL: https://freecodecamp.org/news/learn-css-flexbox
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/cssflexbox.png
tags:
- name: flexbox
  slug: flexbox
- name: youtube
  slug: youtube
seo_title: Apprenez le CSS Flexbox dans ce cours accéléré
seo_desc: 'Understanding CSS Flexbox is super helpful if you want to make your websites
  responsive.

  Flexbox is a powerful responsive web design tool that''s built right into CSS itself.

  And we just published a CSS Flexbox crash course on the freeCodeCamp.org You...'
---

Comprendre le CSS Flexbox est extrêmement utile si vous souhaitez rendre vos sites web responsives.

Flexbox est un outil puissant de conception web responsive intégré directement dans le CSS.

Et nous venons de publier un cours accéléré sur le CSS Flexbox sur la chaîne YouTube de freeCodeCamp.org.

James Maxwell a créé ce cours. Non seulement il a créé le cours, mais il a également créé des fiches de révision PDF incroyables pour l'accompagner.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-70.png)
_Fiches de révision Flexbox_

Le modèle de mise en page flex permet aux éléments responsives à l'intérieur d'un conteneur d'être automatiquement disposés en fonction de la taille de l'écran.

Vous apprendrez des propriétés telles que display, flex-direction, flex-wrap, flex-flow, justify-content, align-items, align-content, et bien plus encore.

Vous pouvez regarder le cours complet ci-dessous ou sur [la chaîne YouTube de freeCodeCamp.org](https://youtu.be/tXIhdp5R7sc) (35 minutes de visionnage).

%[https://youtu.be/tXIhdp5R7sc]

## Transcription

(générée automatiquement)

Comprendre le CSS Flexbox est important si vous souhaitez créer des sites web responsives. James Maxwell a créé ce cours, ainsi que des fiches de révision PDF incroyables pour l'accompagner.

Flexbox va changer votre perspective sur la conception web.

Et encore une fois, pour la puissance du cours, j'ai créé deux belles fiches de révision PDF, que vous pouvez télécharger.

Ces fiches de révision contiennent chaque propriété que nous allons apprendre maintenant.

L'une est exclusive pour les propriétés du conteneur parent, et l'autre est exclusive pour les propriétés des enfants.

Vous pouvez utiliser cette fiche de révision pour vos références futures. Je vous encourage vivement à suivre la vidéo maintenant, puis à utiliser les fiches de révision plus tard.

Alors, plongeons dans le concept de Flexbox.

Sans plus tarder, nous allons créer un fichier séparé à des fins d'apprentissage afin que vous puissiez vous référer au fichier ainsi qu'aux fiches de révision à l'avenir.

Créons rapidement un fichier head Sumo en utilisant la fonction Emmet.

Maintenant, je vais vous apprendre une autre fonction Emmet pour créer un conteneur et les enfants à l'intérieur.

Nous avons donc besoin d'une balise div avec une classe conteneur.

Puis, à l'intérieur, un symbole supérieur pour créer quelques enfants à l'intérieur du conteneur.

Donnons à l'élément enfant une classe appelée items.

Donc, encore une fois, nous devrons entrer une fléchette et simplement taper items.

Et nous voulons également que chaque élément enfant ait un numéro unique.

Donc, insérez un tiret, puis insérez le symbole $1 fois cinq.

Cette fonction Emmet créera un conteneur avec cinq éléments numérotés à l'intérieur.

Nous voulons également que les éléments aient un nom d'alias unifié.

Et nous allons l'appeler item.

Donc, encore une fois, insérez une fléchette et tapez simplement item.

Maintenant, appuyez sur Entrée.

N'était-ce pas simple ? Cela peut sembler un peu intimidant au début.

Mais une fois que vous vous y serez habitué avec la pratique, vous ne pourrez plus créer de conteneurs head Sumo sans ces belles fonctions d'image.

Pour en savoir plus sur ces fonctions mn, vous pouvez visiter Doc's dot me.io.

Maintenant, avant de passer à notre fichier CSS, nous devons remplir les numéros à l'intérieur d'une balise div.

Créons rapidement un fichier CSS et le lier au fichier HTML.

Commençons par la réinitialisation de base en utilisant le sélecteur universel.

Nous allons donc définir la marge à zéro, le remplissage à zéro et le box sizing border box.

Ensuite, nous allons styliser le conteneur et les éléments enfants pour implémenter les propriétés Flexbox.

Nous allons donc cibler le conteneur maintenant.

Et lui donner une couleur de fond de hash Ca Ca NCAA, qui est une couleur gris clair.

Puis lui donner un remplissage de 10 pixels.

Ensuite, une marge de 50 pixels.

Ensuite, nous allons parler du sélecteur d'élément.

Et nous allons leur donner une couleur de fond de hash, ff 0037, qui est une belle couleur rouge.

Puis pour la police et ainsi de suite pour l'élément, nous allons leur donner une couleur blanche.

Taille de police de 35 pixels, remplissage de 20 pixels et une marge de 10 pixels.

Si vous voyez ici, nous n'avons pas encore implémenté Flexbox, mais nous avons un conteneur de couleur grise et des éléments de couleur rouge à l'intérieur du conteneur.

Les éléments peuvent être n'importe quoi dans un site web réel.

Cela pourrait être la barre de navigation du site web, ou quelques paragraphes majeurs ou autre chose.

Cette vidéo est entièrement consacrée aux propriétés du conteneur Flexbox.

Pour activer Flexbox, nous devons définir la propriété display sur flex à l'intérieur du conteneur.

Définissons donc la propriété display sur flex à l'intérieur d'un conteneur.

Vous pouvez déjà voir la magie que Flexbox a produite, comme vous pouvez le voir, pour créer ce type de mise en page en utilisant la propriété float, la propriété position et les propriétés de marge, cela aurait été un processus fastidieux, je ne prendrais jamais ce risque personnellement, simplement en définissant la propriété display sur flex dans le conteneur parent, les éléments enfants sont devenus les éléments flex.

Maintenant, parlons de la propriété flex direction.

La propriété flex direction est utilisée pour trouver la direction des éléments flex à l'intérieur du conteneur.

Par défaut, la flex direction est définie sur row.

Lorsque la flex direction est définie sur row, vous ne voyez rien se passer.

Outre row, il existe quelques autres valeurs de direction qui changeront la direction des enfants à l'intérieur du conteneur.

Voyons-les une par une.

Lorsque nous changeons la flex direction en colonne, vous pouvez voir que les éléments enfants sont disposés verticalement dans une colonne.

C'est le superpouvoir de Flexbox.

En définissant la direction sur colonne, nous avons changé l'axe lui-même.

Il existe deux axes différents selon Flexbox, l'axe principal et l'axe transversal, l'axe diffère pour différentes directions.

Pour la flex direction définie sur row, l'axe principal serait l'axe x.

Pour la flex direction définie sur colonne, l'axe principal serait l'axe y.

Ce concept n'a rien à voir avec Flexbox, notre développement web, ce sont les bases des mathématiques, pour inverser la direction des éléments flex en colonne ou en ligne, nous pouvons utiliser les valeurs column reverse ou row reverse.

Lorsque la direction est définie sur column reverse.

Vous pouvez voir que la direction des éléments est inversée sur l'axe y.

Donc, l'axe principal ici va de bas en haut, alors qu'avant il allait de haut en bas.

Et bien sûr, les numéros sont dans l'ordre inverse, le feu est en haut et le un est en bas.

La même règle s'applique pour reverse, vous pouvez choisir le bon mot qui conviendrait.

Donc, lorsque j'ai dit la flex direction sur reverse ? Exactement, cela empile les éléments dans l'ordre inverse.

Ici, l'axe principal va de droite à gauche.

Et les numéros sont également dans l'ordre inverse, vous devez toujours être conscient de l'axe principal.

C'est vraiment important.

Puisque nous avons expérimenté toutes les valeurs possibles pour la propriété flex direction, revenons à row qui est la valeur par défaut.

Nous n'avons pas encore exploré beaucoup de choses sur Flexbox, mais je suis sûr que vous pourriez comprendre à quel point Flexbox va nous aider dans la création d'un design responsive.

Probablement, lors de la conception pour un écran plus petit, nous pouvons simplement définir la flex direction sur colonne, ce qui empilera les éléments les uns sur les autres.

Donc, c'est tout ce qu'il y a à savoir sur la flex direction.

Ensuite, je veux discuter de la propriété justify content.

Donc, rappelez-vous que la propriété justify content définit comment les éléments flex doivent être empilés le long de l'axe principal.

Commençons par la valeur center ici.

Maintenant, automatiquement, tous les éléments flex sont empilés au centre ici.

Permettez-moi de zoomer un peu pour que vous puissiez voir les choses clairement.

Bien, vous pouvez toujours utiliser les outils de développement pour inspecter les éléments.

Le navigateur a compris que cette balise div utilise Flexbox.

Lorsque vous survolez la propriété justify content, vous pouvez voir à quel point Flexbox a calculé les distances et aligné les éléments au centre.

Imaginez simplement si nous n'avions pas Flexbox.

Pour créer cette mise en page très simple.

Eh bien, nous aurions dû utiliser une propriété float, ce qui aurait été un vrai cauchemar pour nous.

Donc, la valeur center aligne les éléments flex exactement au centre du conteneur.

Mais elle ne fait rien avec l'espace entre les éléments.

L'espace entre les éléments est dû à la valeur de marge que nous donnons pour le sélecteur d'élément.

Donc, si la valeur de marge est commentée, vous pouvez voir que les éléments flex sont étroitement regroupés.

Désactivons rapidement cette marge et expérimentons la valeur suivante qui est space between. Changeons donc justify content en space between. Vous pouvez voir que l'espace entre nos éléments flex est uniformément distribué.

Nous n'avons pas eu à spécifier de nombre ici, mais Flexbox calcule automatiquement la distance et distribue les éléments en fonction de l'espace disponible.

Le meilleur aspect ici est l'autre côté.

Avoir un navigateur, l'espace entre les éléments s'ajuste également.

Cela le rend vraiment pratique pour créer une mise en page responsive.

Maintenant, revenons à la propriété de marge à l'intérieur du sélecteur d'élément, car nous allons explorer une autre valeur qui est similaire à space between appelée space around. En changeant justify content en space around, vous pouvez voir que la valeur space around a créé une quantité égale d'espace des deux côtés gauche et droit des éléments flex.

L'espace entre ces deux éléments est deux fois la quantité d'espace du côté gauche de cet élément.

Ensuite, nous allons voir la valeur space evenly.

Donc, en changeant justify content en space evenly.

Lorsque j'ai commencé à utiliser Flexbox, je n'ai pas compris la différence entre ces valeurs au début, c'est tout à fait normal.

Vous allez commencer à comprendre ces valeurs une fois que vous allez les utiliser dans vos projets.

Donc, en définissant la valeur sur space evenly, vous pouvez voir que l'espace entre les éléments flex est uniformément distribué des deux côtés.

L'espace entre le premier et le deuxième élément flex est le même que le reste.

Donc, tandis que space evenly garantira que l'espace entre les éléments est toujours le même des deux côtés, space around garantit que l'espace autour de chaque élément est le même du côté gauche et droit.

Definitely not a big difference, but the usages differ completely.

Il y a deux autres valeurs pour la propriété justify content, les valeurs flex start et flex end, et justify content, elles servent flex start.

Eh bien, c'est la valeur par défaut.

Désactivons la valeur de marge pour nous assurer que oui, c'est la valeur par défaut.

Maintenant, si nous définissons justify content sur flex end.

Ici, une attention très complète.

Les gens confondent souvent row reverse et les valeurs flex end.

Reverse inversera l'ordre des éléments flex.

Mais la valeur flex end, lorsque vous déplacez les éléments flex à la fin du conteneur, en maintenant la marge si elle est fournie.

D'accord, la dernière propriété que nous allons discuter dans cette vidéo est Align items.

La propriété justify content aligne les éléments flex le long de l'axe principal, mais la propriété Align items aligne les éléments flex le long de l'axe transversal.

Afin de faire fonctionner la propriété Align items, nous allons maintenant rendre l'un des éléments flex plus grand que les autres.

Parce que chaque élément flex a une hauteur unifiée.

Donc, il sera difficile de démontrer la propriété Align items, choisissons le troisième élément et définissons sa hauteur à 150 pixels.

Changeons également justify content en center.

Et voici.

Je viens de remarquer une erreur dans ma nomenclature.

J'ai inclus des numéros pour les éléments, qui auraient dû être pour l'élément, c'est totalement correct.

Ici, vous pouvez voir que tous les éléments flex ont maintenant une hauteur de 150 pixels et pas seulement le troisième élément flex.

Ce n'est pas un bug, mais cela se produit parce que la valeur par défaut pour nos éléments en ligne est stretch.

Lorsque l'élément en ligne est stretch, c'est ce qui se passe.

Donc, ajoutons également Align items à center.

Très bien, nous pouvons visualiser comment la propriété align items aligne nos éléments flex le long de l'axe transversal.

Ici, nous avons un élément flex qui est plus grand que les autres.

Et avec la propriété Align items définie sur center, nous centrons les éléments flex plus petits par rapport au plus grand de manière verticale.

Si nous définissons maintenant Align items sur flex start, tous les éléments commenceront en haut le long du haut de l'élément flex le plus grand.

L'inverse se produira si nous définissons Align items sur flex end.

Donc, les éléments flex s'alignent également en bas.

Jusqu'à présent, nous avons vu les valeurs center, flex start, flex end et stretch pour la propriété Align items.

La valeur stretch étire la hauteur de tous les éléments flex pour correspondre à la hauteur de l'élément flex le plus grand.

Il y a une dernière valeur pour la propriété Align items, elle s'appelle baseline.

Pour utiliser la valeur baseline, nous devons d'abord augmenter la taille de la police de l'un des éléments.

Donc, sélectionnons l'élément numéro quatre et augmentons sa taille de police à 50 pixels.

Si nous définissons maintenant Align items sur baseline, vous pouvez voir qu'il aligne tous les éléments flex le long du texte à l'intérieur de l'élément numéro quatre sur une ligne imaginaire.

Je ne vais pas réinitialiser align items sur center et supprimer les sélecteurs des éléments numéro quatre et numéro trois.

Très bien, nous arrivons à la fin de cette vidéo.

Donc, flex direction, justify content et Align items sont les propriétés les plus importantes et les plus fréquemment utilisées.

Bien sûr, il y a quelques autres propriétés, mais nous les verrons dans une autre vidéo.

Avant de terminer cette vidéo, je veux répondre à l'une des questions les plus notées, que se passera-t-il avec justify content et la propriété Align items et la flex direction définie sur colonne ? Eh bien, vérifions cela.

Super.

Si vous remarquez, l'axe principal a changé maintenant.

Il ne va plus de gauche à droite.

Mais il va de haut en bas.

Tout est bien.

Mais pourquoi les éléments sont-ils alignés au centre ? Eh bien, c'est dû à align items, ils ont dit le centre et la flex direction définie sur colonne.

Lorsque la flex direction est définie sur colonne, l'axe principal serait l'axe y et l'axe transversal serait l'axe x.

Nous savons que la propriété Align items affecte l'axe transversal.

Et c'est pourquoi nos éléments sont alignés au centre verticalement.

Donc, si nous définissons maintenant Align items sur flex end, et vous pouvez voir que les éléments sont alignés à la fin du conteneur verticalement.

L'inverse de cela se produira si nous définissons Align items sur flex start.

Et oui, les éléments sont empilés au début du conteneur.

Donc, je vais à nouveau insister pour que vous gardiez toujours une trace de l'axe principal et de l'axe transversal afin d'utiliser justify content et align items de la bonne manière.

Maintenant, pour votre meilleure compréhension.

Je vais également expérimenter avec justify content lorsque la flex direction est définie sur colonne.

Pour cela, nous devons d'abord définir une valeur de hauteur pour le conteneur.

Donc, peut-être définissons-la à 1400 pixels.

Puis je vais diminuer la taille de ma fenêtre d'affichage.

Maintenant, si je définis justify content sur space between, si je survole justify content dans mes outils de développement, vous pouvez voir que l'espace entre les éléments est distribué comme nous l'avons vu précédemment, mais dans la direction verticale.

Très bien, terminons cette vidéo ici.

Je sais que je laisse la plupart d'entre vous avec un esprit sceptique.

Mais c'est tout à fait normal pour tout débutant.

J'ai ressenti la même chose lorsque j'ai appris Flexbox pour la première fois.

Et c'est pourquoi j'ai fait ces belles fiches de révision à des fins de référence.

Je pense que cela aurait été mieux si quelqu'un m'avait donné ces fiches de révision lorsque j'ai commencé à apprendre Flexbox, vous pouvez maintenant re-regarder cette vidéo avec la fiche de révision pour avoir une meilleure clarté sur ces concepts.

Définissons rapidement la flex direction sur row, supprimons la hauteur et définissons justify content et align items sur center et terminons cette vidéo.

Super.

Retrouvons-nous dans la prochaine leçon pour en apprendre davantage sur les concepts de Flexbox.

Dans la dernière leçon, nous avons appris trois propriétés importantes du conteneur Flexbox.

Il y en a quelques autres, mais nous les verrons plus tard.

Maintenant, dans cette vidéo, apprenons les propriétés des enfants Flexbox.

Donc, c'est là où nous en étions restés dans notre dernière vidéo.

La première propriété que nous allons apprendre dans cette leçon est la propriété Align self.

La propriété align self est similaire à la propriété Align items.

Avec l'aide de la propriété align items, nous avons pu changer collectivement l'alignement d'un élément flex le long de l'axe transversal, mais la propriété align self alignera un seul élément flex le long de l'axe transversal.

Et elle peut également remplacer la propriété Align items.

Je sais que cela semble être du charabia, voyons-les en action pour comprendre comment cela fonctionne.

Pour expérimenter la propriété align self, créons à nouveau le sélecteur item trois et donnons-lui une hauteur de 150 pixels.

Vous allez utiliser l'item trois comme point de référence.

Donc, essayons d'appliquer align self à l'item numéro quatre.

Juste après l'item numéro trois, vous allez créer le sélecteur item numéro quatre et créer une propriété align self ici.

Définissons cela sur flex start.

Eh bien, vous pouvez voir que lorsque l'item numéro quatre est aligné au début du conteneur flex, et tous les éléments flex sont alignés au centre de l'item trois le long de l'axe transversal, la propriété align self accepte chaque valeur que la propriété align items accepte.

Mais comme je vous l'ai dit plus tôt, nous utilisons la propriété align self uniquement pour aligner un élément individuel.

Maintenant, changeons cela en flex end et voyons ce qui se passe.

Donc, l'item s'est déplacé en bas du conteneur flex.

Maintenant, lorsque align self est défini sur stretch.

Eh bien, l'item s'étire pour correspondre à la hauteur de l'item le plus grand, qui est l'item trois dans notre cas.

Maintenant, je vous laisse cela à vous.

Allez-y et expérimentez les autres valeurs possibles comme center, space between, space evenly, space around et essayez d'analyser les cas d'utilisation.

Ensuite, nous allons jouer avec l'ordre des éléments flex.

La propriété order est utilisée pour changer la portion des éléments flex à l'intérieur du conteneur pour expérimenter cette propriété, nous allons créer des sélecteurs pour tous les éléments flex et changer l'ordre. La valeur initiale de order est zéro.

Donc, selon Flexbox, l'élément flex un est dans la portion zéro.

Définissons la propriété order pour chaque élément flex et changeons les portions.

Donc, nous allons déplacer l'item un à la position trois.

Puis l'item deux, à la position quatre, l'item trois, à la position zéro, l'item quatre à la position un.

l'item cinq à la position deux.

Donc, après avoir enregistré le fichier, vous pouvez voir que nos éléments ont été relocalisés.

Je veux que vous compreniez que les valeurs données ici sont simplement des valeurs expérimentales.

Vous pouvez aller de l'avant et organiser les éléments comme vous le souhaitez.

Mais encore une fois, je vous encouragerais tous à suivre l'ordre que je donne ici afin que nous continuions sur la même voie.

Si vous voyez ici, un est à la troisième position, deux est à la quatrième position, trois est à la position zéro, quatre est à la première position et cinq est à la deuxième position.

La propriété order sera pratique pour nous pour relocaliser la portion des éléments lorsqu'il s'agit de design responsive.

Vous pouvez voir certaines personnes utiliser des valeurs négatives pour changer l'ordre.

Mais je n'encourage jamais personne à utiliser des valeurs négatives, cela nous confondra lorsque nous regarderons notre code à l'avenir.

C'est tout ce qu'il y a à savoir sur la propriété order.

Nous allons maintenant voir les trois dernières propriétés associées aux éléments enfants de la flex box.

Flex grow, flex shrink et flex basis, et supprimer les propriétés order de tous les éléments flex.

La première chose que nous allons voir est la propriété flex grow.

La propriété flex grow permet à un élément flex de croître.

Pour faire croître un élément flex.

Tout ce que nous faisons est de spécifier un entier, juste un nombre comme nous l'avons assigné à la propriété order.

Pour expérimenter cette propriété.

Appliquons généralement dans le sélecteur d'élément.

Donc, je vais créer une propriété flex grow et la définir à un.

Eh bien, tous les éléments flex sont devenus plus grands en taille.

Donc, ici, tous les éléments flex occupent l'espace vide qu'ils peuvent remplir dans le conteneur.

En d'autres termes, ils occupent l'espace maximum disponible à l'intérieur du conteneur, nous pouvons mieux le visualiser si nous revenons à la propriété de marge.

Vous pouvez voir qu'ils se touchent maintenant et occupent tout l'espace qu'ils peuvent, c'est tout ce qu'il y a à savoir sur la propriété flex grow que nous avons découverte, cette propriété de marge maintenant.

Donc, même si vous changez cela en 200, ils ne vont pas devenir plus grands que cela.

C'est parce que la valeur n'a d'importance que par rapport aux autres.

Réinitialisons cette valeur à un et essayons de comprendre comment la valeur compte.

En relation avec les autres valeurs de flex grow.

Ajoutons une propriété flex grow à l'item quatre et donnons-lui trois.

Donc, ici, l'item numéro quatre est trois fois plus grand que le reste des éléments flex.

Par cela, je suis sûr que vous pouvez comprendre comment la propriété flex grow fonctionne relativement.

Lorsque je change ce trois en cinq, il va devenir cinq fois plus grand que les autres éléments flex.

C'est tout ce qu'il y a à savoir sur la propriété flex grow.

Supprimons la propriété flex grow de l'item numéro quatre et discutons d'une propriété abrégée.

Donc, les quelques propriétés que nous apprenons ont une propriété abrégée, nous pouvons les appeler directement en utilisant le mot-clé flex.

Donc, avec le mot-clé flex, nous pouvons déclarer trois valeurs différentes.

La première valeur sera pour une propriété flex grow, la deuxième sera pour flex shrink.

Et la dernière sera pour flex basis, puis nous donnons simplement un comme première valeur, il comprendra automatiquement que nous déclarons la valeur flex grow.

Donc, si vous vous souvenez du mot-clé grow d'ici, chaque élément flex occupe toujours l'espace maximum.

Cette méthode va être extrêmement pratique lorsqu'il s'agit de projets du monde réel.

Et dans la plupart des cas, nous utiliserons la propriété abrégée dans un projet.

Peut-être voulons-nous que l'un de nos éléments flex croisse plus que les autres.

Par exemple, essayons de faire croître le dernier élément.

Maintenant, en définissant flex à cinq pour l'item numéro cinq, vous pouvez voir qu'il occupe l'espace maximum et les autres occupent relativement l'espace disponible.

C'est tout ce qu'il y a à savoir sur la propriété flex grow.

Ensuite, nous allons voir la propriété flex basis.

La propriété flex basis définira la largeur d'un élément flex.

Au lieu d'utiliser la propriété width, nous pouvons utiliser flex basis en utilisant la propriété flex basis ou la propriété width signifierait la même chose.

C'est toujours un choix personnel.

Mais à mon avis, je dirais qu'il est toujours bon de pratiquer l'utilisation de la propriété flex basis afin que nous soyons en mesure de différencier l'élément flex et l'élément nominal.

Maintenant, pour notre exemple, je vais changer cela en flex basis et définir cela à 75 pour cent.

Lorsque nous utilisons la propriété flex basis, nous devons déclarer une valeur basée sur un pourcentage ou une valeur basée sur des pixels.

Maintenant, l'item numéro cinq occupe 75 pour cent du conteneur et le reste est altéré pour occuper les 25 pour cent restants de l'espace en définissant flex basis sur auto en arrière-plan.

Ne vous inquiétez pas si vous n'êtes pas en mesure de comprendre la différence entre ces propriétés.

Vous allez les utiliser beaucoup dans notre cours.

Donc, vous allez finalement les comprendre avec la pratique.

La toute dernière propriété que nous allons voir dans cette vidéo est flex shrink.

Donc, pour vous montrer ce que fait la propriété flex shrink, laissez-moi changer cette valeur de pourcentage en une valeur basée sur les pixels.

Peut-être laissez-moi changer cela en 700 pixels.

D'accord.

Laissez-moi également minimiser la fenêtre de mon navigateur pour démontrer cette propriété.

Maintenant, si j'augmente la largeur de la fenêtre d'affichage, regardez simplement ce qui se passe.

Donc, vous pouvez voir que notre item numéro cinq se rétrécit à un certain point de rupture.

Malgré avoir défini son flex basis à 700 pixels, il se rétrécit à un certain point.

Pour éviter cela, nous déclarons la propriété flex shrink et la définissons à zéro.

Les deux seules valeurs pour la propriété flex shrink sont un et zéro.

Donc, elle fonctionne comme une propriété binaire.

Par défaut, elle est définie à un, ce qui signifie qu'elle rétrécira l'élément flex à un certain point.

Essayons de définir la propriété flex shrink à zéro et voyons ce qui se passe.

Mais avant cela, laissez-moi agrandir la taille de la fenêtre de mon navigateur. Allant à mon éditeur de texte.

Je vais définir une propriété flex shrink à l'item numéro cinq et la définir à zéro.

Maintenant, si j'essaie de diminuer la taille de la fenêtre de mon navigateur, eh bien, vous pouvez voir qu'après avoir défini flex shrink à zéro, peu importe la taille que nous prenons de la fenêtre d'affichage, l'item numéro cinq ne se rétrécit pas.

Mais le reste des éléments débordent de la fenêtre d'affichage.

Dans la plupart des cas, les gens ignorent de comprendre qu'ils utilisent la propriété flex shrink.

En temps réel, nous utilisons un mot-clé flex où nous pouvons déclarer consécutivement les trois propriétés flex grow, flex shrink et flex basis que nous voulons cibler la propriété flex basis, alias la propriété width pour définir les éléments flex avec.

Et c'est ainsi que nous allons l'implémenter dans notre cours également.

Après avoir regardé cette vidéo, j'encourage vivement tout le monde à ouvrir la fiche de révision et à pratiquer jusqu'à ce point.

Dans la vidéo suivante, nous allons apprendre le reste des propriétés du conteneur flex et dans cette section.

Avant de terminer cette section, j'aimerais vous apprendre à gérer beaucoup d'éléments flex dans le conteneur flex.

Donc, pour l'instant, nous avons cinq éléments flex.

Ajoutons simplement cinq autres éléments flex à notre conteneur et recevons les noms de classe.

Donc, vous pouvez voir que tous ces éléments flex sont étroitement regroupés pour s'adapter au conteneur, et certains débordent du conteneur flex, zoomez un navigateur à 150 pour cent pour des raisons de démonstration.

Si vous ne trouvez pas ces éléments qui débordent, zoomez simplement la fenêtre de votre navigateur comme je l'ai dit.

Maintenant, en revenant au point, nous avons cette dernière vidéo pour cette section.

Parce qu'ils ont une solution si vous trouvez des éléments flex qui se serrent comme ceci.

Donc, nous pouvons utiliser la propriété flex wrap pour surmonter ce problème.

La valeur par défaut pour flex wrap est no wrap.

Et c'est pourquoi nos éléments flex débordent du conteneur.

Mais si nous créons une propriété flex wrap dans le sélecteur de conteneur et la définissons sur wrap.

Alors cela créera une nouvelle ligne comme ceci pour faire tenir tous les éléments flex à l'intérieur du conteneur.

Au cas où nous serions un sélecteur pour l'élément numéro 10 et avons dit flex à un.

Vous pouvez voir que l'élément numéro 10 occupe son espace maximum dans la ligne.

Maintenant, si vous réduisez la taille du navigateur, alors la propriété flex wrap enveloppera les éléments flex de plus en plus pour s'assurer que tous les éléments flex tiennent dans le conteneur.

Et une fois de plus, cela va être extrêmement utile pour le design responsive, puis nous avons moins d'espace à l'écran.

Maintenant, laissez-moi augmenter la hauteur du conteneur ici et vous montrer ce qui va se passer.

Et nous définissons cela à 600 pixels et voyons ce qui se passe.

Donc, ici, nous avons toujours deux lignes.

Mais pourquoi avons-nous cet espace vide entre les deux.

C'est à cause de la propriété Align content que nous n'avons pas encore discutée.

C'est encore une propriété du conteneur flex.

Donc, créons la propriété align content dans le sélecteur de conteneur et définissons-la sur flex start.

Maintenant, comme vous pouvez le voir, chaque ligne dans un conteneur flex est en haut du conteneur.

Par conséquent, la propriété Align content aligne la ligne dans l'axe transversal dans le conteneur.

Encore une fois, nous pouvons utiliser les mêmes valeurs pour la propriété align content que celles que nous utilisons pour les propriétés align items et align self.

Ici, je veux que vous mettez la vidéo en pause et analysiez la différence entre les propriétés Align items, align self et align content.

Maintenant, définissons align content sur center.

Donc, comme vous pouvez le voir, les lignes sont alignées au centre du conteneur.

Nous pouvons également changer flex end.

Et oui, les lignes sont à la fin du conteneur.

Puis voyons space around, space between et enfin space evenly.

Donc, la marche suit la même logique, comme vous le voyez, ces propriétés prendront un certain temps pour que vous les mémorisiez.

Mais vous n'avez pas à vous en soucier vraiment, car à partir de maintenant, nous allons seulement utiliser Flexbox dans notre projet principal.

Félicitations à tous.

Nous avons maîtrisé le concept de Flexbox.

Ne perdons plus de temps.

Nous avons une belle application à construire à l'intérieur de notre site web.

Donc, retrouvons-nous dans la prochaine section, où nous allons reconstruire une barre de navigation et la section héro, puis nous passerons à notre application.