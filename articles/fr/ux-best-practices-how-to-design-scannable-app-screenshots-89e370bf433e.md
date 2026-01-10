---
title: 'Meilleures pratiques UX : Comment concevoir des captures d''écran d''application
  scannables'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-22T15:53:04.000Z'
originalURL: https://freecodecamp.org/news/ux-best-practices-how-to-design-scannable-app-screenshots-89e370bf433e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*B8O1AJC2mA9Oa5hEGjqbGg.png
tags:
- name: Design
  slug: design
- name: mobile app development
  slug: mobile-app-development
- name: technology
  slug: technology
- name: user experience
  slug: user-experience
- name: UX
  slug: ux
seo_title: 'Meilleures pratiques UX : Comment concevoir des captures d''écran d''application
  scannables'
seo_desc: 'By Girish Rawat

  Redesigning HeyDoctor’s App Store Screenshots


  Let’s play a game. Pick an app on your phone that you really like. You are the creator
  of this app and are looking to raise money from investors. You have a minute to
  pitch your app to VC...'
---

Par Girish Rawat

#### Redesigning HeyDoctors App Store Screenshots

![Image](https://cdn-media-1.freecodecamp.org/images/1*jQQ2k7-ZTuvm_fBsGOig2A.png)

Jouons à un jeu. Choisissez une application sur votre téléphone que vous aimez vraiment. Vous êtes le créateur de cette application et vous cherchez à lever des fonds auprès d'investisseurs. Vous avez une minute pour présenter votre application aux capital-risqueurs. L'argent est à portée de main, mais seulement si vous pouvez les convaincre en 60 secondes. Comment faites-vous ? Décrivez-vous ce que fait l'application ? Expliquez-vous comment l'application est unique par rapport à ses concurrents ? Montrez-vous à quel point l'expérience utilisateur est bonne ?

Il faut en moyenne 7 secondes à un utilisateur sur l'App Store pour décider s'il veut télécharger votre application ou non. Une [étude de recherche](https://incipia.co/post/app-marketing/app-store-screenshots-study-of-the-top-100-apps/) sur les décisions de téléchargement impliquant 25 000 visiteurs et 10 000 installations a classé les captures d'écran comme la deuxième raison la plus importante d'installation, le classement prenant la première place.

> Nous avons découvert que le temps moyen que les gens passent sur une fiche de magasin est de 7 secondes. Le fait est que la grande majorité des gens quittent la page encore plus tôt. Les utilisateurs engagés restent un peu plus longtemps, mais ils suivent tous le même processus : vérifier l'icône, voir les deux premières captures d'écran et scanner la première ligne de la description de l'application  Peter Fodor, [Pourquoi 7 secondes pourraient faire ou défaire votre application mobile](https://asostack.com/why-7-seconds-could-make-or-break-your-mobile-app-f41000fb2a17)

Les captures d'écran sont un miroir des histoires utilisateur de votre application et reflètent son expérience utilisateur. J'ai étudié les 100 meilleures applications et leurs captures d'écran en utilisant les données recueillies par les bonnes gens d'Incipia. Je vais référencer ici les principales conclusions de plusieurs études.

### Application en focus : HeyDoctor

![Image](https://cdn-media-1.freecodecamp.org/images/1*b_vKDZBlMOkgYTckLdaGwg.png)

[HeyDoctor](https://www.heydoctor.co/) est une application qui permet aux utilisateurs d'obtenir des ordonnances médicales en ligne sans avoir besoin de consulter un médecin généraliste. HeyDoctor peut prescrire et renouveler des ordonnances pour des médicaments allant des contraceptifs, des traitements pour la croissance des cheveux aux traitements contre les infections urinaires, les rapports de laboratoire et plus encore. Vous pouvez également obtenir un traitement pour des cas de soins primaires comme le traitement de l'acné, les infections urinaires, le traitement des boutons de fièvre et plus encore. L'application mobile de HeyDoctor a été bien accueillie dans l'App Store avec 122 avis lui attribuant 4,7 étoiles.

Nous allons redessiner les captures d'écran de HeyDoctor et apprendre à concevoir des captures d'écran scannables.

#### Avertissement

Veuillez noter que je ne travaille pas chez HeyDoctor et que les opinions exprimées dans cette étude de cas sont strictement les miennes. Contrairement aux designers, aux chefs de produit et à tous ceux qui sont responsables de la prise de décisions clés impliquant la conception travaillant chez HeyDoctor, je n'ai pas accès aux analyses de sa base d'utilisateurs et je ne peux pas voir l'ensemble du tableau. Les décisions de conception peuvent être basées sur des objectifs commerciaux, la priorisation des ressources ou des contraintes techniques. Par conséquent, toute étude de cas non sollicitée n'est pas exhaustive, et je ne suggère certainement pas que HeyDoctor abandonne leurs captures d'écran actuelles et adopte mon redessin.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wmaVEQdPEskC4HXYnfNCeg.png)
_Rendez votre application plate  un gars. Crédits du mème : [**@**parasmael](https://twitter.com/parasmael" rel="noopener" target="_blank" title=")_

#### Le Design Actuel

Nous allons travailler sur l'application iOS de HeyDoctor. Voici à quoi ressemblent les captures d'écran existantes :

![Image](https://cdn-media-1.freecodecamp.org/images/1*K_JNBDrKErv4JsWeQcRyFg.png)

Il suit la configuration standard de titre et de sous-titre qui fait un bon travail d'explication des histoires utilisateur de l'application. Nous ne sommes pas intéressés par la refonte de la marque ou de l'UI, donc nous allons essayer de les garder cohérents dans notre redessin.

#### Histoires Utilisateur

Avant de nous lancer et de commencer à faire des changements visuels, nous devons apprendre pourquoi les utilisateurs installent HeyDoctor et ce qu'ils recherchent lorsqu'ils découvrent cette application.

1. **Obtenir des ordonnances et des renouvellements.** Les utilisateurs cherchent un moyen facile d'obtenir leurs ordonnances et renouvellements en ligne sans avoir besoin de consulter un médecin.
2. **Obtenir un traitement pour une maladie.** Les utilisateurs recherchent comment obtenir un traitement pour leur maladie en ligne.
3. **Parler à un médecin généraliste.** Les utilisateurs veulent parler à un médecin mais ils ne peuvent probablement pas en consulter un pour le moment en raison de contraintes de temps, financières ou de déplacement.
4. **Faire tout cela sans impliquer de paperasserie d'assurance.** Les utilisateurs ne veulent pas impliquer leur assurance médicale parce qu'ils n'en ont pas ou que leur copay est trop élevé.

### Captures d'écran ou Miniatures ?

Les tailles d'écran ont augmenté de 72 % depuis le lancement de l'iPhone original avec son écran de 3,5 pouces. La taille moyenne des écrans des smartphones vendus aux États-Unis en 2018 est de 5,5 pouces. Les écrans sont plus grands que jamais et les designers de produits évoluent constamment pour utiliser cet espace supplémentaire disponible. On pourrait penser que les écrans plus grands inciteraient les designers à mettre plus de légendes textuelles sur les captures d'écran. Mais ce que nous observons est tout le contraire.

> Nous avons constamment observé que moins de 4 % des utilisateurs recherchant une application agrandissent les captures d'écran en portrait, et seulement 2 % agrandissent les captures d'écran en paysage. Pour les joueurs, c'est encore moins, seulement 0,5 %. Cela est probablement dû au fait que le gameplay est généralement suffisamment clair même à partir des miniatures  [Peter Fodor](https://asostack.com/why-7-seconds-could-make-or-break-your-mobile-app-f41000fb2a17)

Moins de 4 % des personnes venant sur votre page d'application cliquent sur vos captures d'écran.

Les designers ont commencé à prêter attention à cette métrique avec de nombreuses applications traitant leurs captures d'écran comme des miniatures à consulter plutôt que comme quelque chose à cliquer. Les utilisateurs en 2016 pouvaient être amenés à cliquer sur la capture d'écran pour lire le texte. Mais avec la nouvelle disposition de l'app store et les écrans plus grands, les utilisateurs ne cliquent plus sur vos captures d'écran.

Examinons quelques redessins de captures d'écran de 2016 à 2018. Remarquez comment presque toutes ont moins de mots et des polices plus grandes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AacKwwec2tzyqNOr75UrBw.png)

### Le Nombre Magique 2

78 des 100 meilleures applications ont cinq captures d'écran, 13 applications en ont quatre, 6 applications en ont trois et 3 n'en ont que deux. En tant que développeur, vous pourriez penser opter pour cinq captures d'écran parce que plus de contenu est mieux, n'est-ce pas ? Faux.

Seulement 9 % des utilisateurs font défiler les deux premières captures d'écran. Les captures d'écran en paysage performent moins bien à 5 %. Cela rend impératif d'attirer l'utilisateur dans les deux premières captures d'écran elles-mêmes. Dites à vos utilisateurs ce que fait votre application dans la première capture et développez cela dans les captures correspondantes.

> Les résultats de notre recherche montrent clairement que vous DEVEZ expliquer le principal avantage de votre application dans les deux premières (iOS10, Google Play), ou trois (iOS11) captures d'écran si vous utilisez des images en portrait. Si vous voulez vraiment utiliser une image en paysage, vous n'en avez qu'une  [Peter Fodor](https://asostack.com/why-7-seconds-could-make-or-break-your-mobile-app-f41000fb2a17)

Examinons les deux premières captures d'écran de quelques applications populaires.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OL3200-Ug5bBh-faKQetJg.png)

### Éléments UI Mise en Évidence

Les utilisateurs qui regardent vos captures d'écran essaient d'évaluer les fonctionnalités de votre application. Les légendes textuelles les aident à comprendre le contexte derrière les écrans. Les designers facilitent encore plus la tâche des utilisateurs en mettant en évidence les éléments UI que la légende textuelle essaie d'expliquer.

Regardons quelques exemples.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gPvYkFQOCnT73ESDdBs-uQ.png)

### Apprentissages

1. **Expliquez l'histoire utilisateur la plus importante de votre application dans les deux premières captures d'écran.** Seulement 9 % des utilisateurs venant sur votre fiche d'application feront défiler les deux premières captures d'écran.
2. **Augmentez la taille de la police et réduisez le texte.** Avec des écrans plus grands, les utilisateurs sont conditionnés à scanner et à regarder la capture d'écran au lieu de cliquer dessus et de la lire. Moins de 4 % des utilisateurs cliqueront sur vos captures d'écran pour les lire.
3. **Mettez en évidence les éléments UI qui représentent les légendes textuelles.** Cela facilite le scan des captures d'écran et améliore la capacité de glance de votre capture d'écran.

Maintenant que nous savons un peu comment rendre les captures d'écran plus lisibles, commençons à appliquer nos principales conclusions aux captures d'écran de HeyDoctor.

### Étape 1 : Mettre à jour l'iPhone vers les nouvelles générations

Les captures d'écran de HeyDoctor utilisent l'ancienne génération d'iPhones. Bien que ce ne soit pas un critère de rejet, j'aime mes iPhones comme mes applications. Mis à jour et [on fleek](https://www.merriam-webster.com/words-at-play/fleek-meaning-and-history) (désolé).

![Image](https://cdn-media-1.freecodecamp.org/images/1*DCJJjHTMleDNz4msxdOp3g.png)

### Étape 2 : Réduire le texte et le rendre plus lisible

Nous allons essayer de rendre les légendes un peu plus lisibles en énonçant les histoires utilisateur dans un format concis. Nous allons également supprimer le sous-titre et les descriptions pour accommoder les titres plus grands.

![Image](https://cdn-media-1.freecodecamp.org/images/1*L4ibILF69FpckRyqJ_y0Sw.png)

La troisième capture d'écran montre la page des paramètres de l'application tandis que sa légende parle de la façon dont l'application ne nécessite pas de police d'assurance. Remplaçons-la par un écran plus pertinent. Je vais la remplacer par le premier écran que vous voyez lorsque vous essayez d'obtenir une ordonnance dans l'application, impliquant indirectement que vous n'avez pas besoin d'une assurance pour commencer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*e--yMKYb4Twomc5PBK0m4g.png)

### Étape 3 : Mettre en évidence les éléments UI pertinents

Comme nous l'avons appris ci-dessus, la mise en évidence des éléments UI pertinents qui référencent les légendes les rend plus scannables et lisibles. Cela aide également l'utilisateur à scanner la capture d'écran plus facilement.

#### **UI de Chat**

Voyons comment Tinder met en évidence leur UI de chat :

![Image](https://cdn-media-1.freecodecamp.org/images/1*X1XFH0_nF0ODsU4wlAiVLg.png)

Il utilise intelligemment des photos de profil et des bulles de chat avec des éléments de marque comme des couleurs pour imiter son véritable UI de chat.

Essayons de faire quelque chose de similaire :

![Image](https://cdn-media-1.freecodecamp.org/images/1*OA58UMljLeGyB73wx5XZKA.png)

Insérons cet élément dans la capture d'écran :

![Image](https://cdn-media-1.freecodecamp.org/images/1*HzkAcWMNMr_-Gmbp6tEzdA.png)

J'ai essayé d'intégrer la marque de HeyDoctor dans les bulles de chat. Je n'ai pas ressenti le besoin d'inclure des photos de profil car les médecins auxquels vous parlez dans l'application n'ont pas de photo de profil.

#### Cartes et Ombre Portée

Regardons comment Uber met en évidence leurs éléments UI.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9VrQw5k2aMJK3SwtHALxCw.png)

J'adore cette façon minimale de mettre en évidence les éléments UI avec des cartes et des ombres portées. Nous allons utiliser ce style pour souligner certains éléments dans nos captures d'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qZN-kTTkoJNtZcI1_V0KuQ.png)

J'ai décidé de déplacer les légendes sous le téléphone afin que l'utilisateur voie l'élément UI mis en évidence avant de lire la légende.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1G225-9KlBR4PcdXfiCS7w.png)

### Étape 4 : Changements Cosmétiques

Nous avons apporté plusieurs modifications à nos captures d'écran pour optimiser la scannabilité. Maintenant, faisons en sorte qu'elles aient meilleure apparence. Un bon design visuel peut être un leurre incroyable pour les utilisateurs et il ne doit pas être ignoré lors de la refonte des captures d'écran.

#### Ajouter des Écrans en Perspective

Les écrans isométriques ont l'air modernes et polis. Vous pouvez voir des téléphones isométriques presque partout, des publicités de produits parfaitement rendues d'Apple aux maquettes hautement polies sur Dribble (crazy de penser que Dribble a été initialement lancé comme un site pour partager des prototypes de design WIP de bas niveau !)

J'ai fait quelques perspectives à partir des écrans disponibles pour nous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iwn33HPFpys14STxNuyIlw.png)

Je vais choisir la première maquette de perspective et la diviser en deux captures d'écran car nous n'avons que 3 captures d'écran pour le moment et nous pouvons en ajouter jusqu'à 5 dans l'App Store.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QSDm10p_QyaRel0YdhRfFA.png)

J'ai ajouté une légende à la première page  Votre médecin personnel. Facile à lire, résume ce que fait l'application, et concis.

#### Changer le Dégradé de Fond

Le contraste entre le fond et le premier plan est un peu trop dur pour moi en ce moment. Changeons-le pour une teinte plus claire de bleu.

![Image](https://cdn-media-1.freecodecamp.org/images/1*s1dgtAZrQB3hN4wPi7ykHg.png)

Nous allons faire un dégradé avec les nouvelles couleurs que nous choisissons.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1nwKzgiuCStEfD_qgdPn1w.png)

Voyons comment cela se présente dans nos captures d'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pdMgBD9nrj3rphapjhmmhg.png)
_Parfait !_

Je vais ajouter quelques crêtes juste en dessous du texte pour qu'elles servent de différenciateur entre le texte et le téléphone.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7NBTNuqTtvEw2JeeJfrMaQ.png)

J'ai réussi à obtenir un vecteur isométrique cool sur le [web](https://www.freepik.com/). Utilisons-le pour faire la dernière capture d'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aZgKxVOipjmgdEO6iSBnZQ.png)

### Designs Finaux

#### Avant

![Image](https://cdn-media-1.freecodecamp.org/images/1*QgBVdYeuC-vXfMdvl7571Q.png)

#### Après

![Image](https://cdn-media-1.freecodecamp.org/images/1*B8O1AJC2mA9Oa5hEGjqbGg.png)

### Conclusion

Dans l'ensemble, nous avons apporté juste plus de quatre petites modifications itératives. Mais le résultat final est des captures d'écran faciles à scanner et qui ont l'air modernes. De plus, aucune de ces modifications n'a nécessité une compétence artistique innée. L'étude d'une poignée d'applications dans l'App Store nous a aidé à savoir quels problèmes rechercher.

**Merci d'avoir lu !** Ce fut un projet de week-end amusant pour moi et j'ai apprécié en écrire ici. Espérons que cet article vous a donné un aperçu de l'état des captures d'écran dans l'app store. N'hésitez pas à fournir des commentaires ou à poser des questions que vous avez dans la section des commentaires ci-dessous.