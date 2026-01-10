---
title: Comment pirater votre Mac et lui offrir les magnifiques fonds d'écran qu'il
  mérite vraiment
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-11T23:33:33.000Z'
originalURL: https://freecodecamp.org/news/this-is-the-wallpaper-your-mac-truly-deserves-with-a-bit-of-coding-f3149bbeb51
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kEVDB5B2KX5_O69b0ccLPQ.jpeg
tags:
- name: Apple
  slug: apple
- name: Photography
  slug: photography
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment pirater votre Mac et lui offrir les magnifiques fonds d'écran qu'il
  mérite vraiment
seo_desc: 'By Aakaash Jois

  Let’s face it. The default wallpapers on the Mac gets boring after a few weeks.
  And setting new wallpaper manually is tiresome. Well, what if I told you that I
  got my Mac greet me with a brand new, high resolution wallpaper every time...'
---

Par Aakaash Jois

Admettons-le. Les fonds d'écran par défaut sur le Mac deviennent ennuyeux après quelques semaines. Et définir manuellement un nouveau fond d'écran est fastidieux. Eh bien, que diriez-vous si je vous disais que j'ai réussi à faire en sorte que mon Mac m'accueille avec un tout nouveau fond d'écran haute résolution chaque fois que je l'ouvre ?

Si vous êtes utilisateur de Chromecast, vous êtes peut-être familier avec [Chromecast Backdrop](https://www.google.com/chromecast/backdrop/). Backdrop permet au Chromecast d'afficher un diaporama de belles photos lorsqu'il est en veille.

Bien que la plupart des utilisateurs utilisent Facebook pour publier des photos, de nombreux photographes utilisent Google+ pour publier leur travail. Google sélectionne certaines de ces meilleures photos pour créer des diaporamas brillants.

Pendant longtemps, cela était exclusif aux utilisateurs de ChromeCast. Mais il y a quelques mois, Google a publié une application pratique pour Mac appelée [Google Featured Photos](https://plus.google.com/featuredphotos).

Vous vous demandez peut-être pourquoi mon titre dit « fond d'écran » mais renvoie ensuite à une application « Économiseur d'écran ». Eh bien, il y a un petit truc. Sur un Mac, n'importe quel économiseur d'écran peut être transformé en fond d'écran avec une seule ligne de code.

Tout d'abord, vous devez télécharger et installer l'[Économiseur d'écran Google Featured Photos](https://plus.google.com/featuredphotos). Ensuite, allez dans _Préférences Système_ → _Bureau et Économiseur d'écran_ et définissez _Google Featured Photos_ comme économiseur d'écran actif. Il est maintenant temps d'exécuter le code magique.

![Image](https://cdn-media-1.freecodecamp.org/images/6uI-dPJ4HxwPs-zEr6X2tOaLgd4cVCxJisDG)
_Définir Google Featured Photos comme économiseur d'écran_

#### C'est l'heure de coder !

Ouvrez le Terminal et collez la ligne de code ci-dessous. Elle définira votre économiseur d'écran comme fond d'écran.

```
/System/Library/Frameworks/ScreenSaver.framework/Resources/ScreenSaverEngine.app/Contents/MacOS/ScreenSaverEngine -background &
```

#### MODIFICATION : Apple a décidé de restructurer un peu dans High Sierra.

![Image](https://cdn-media-1.freecodecamp.org/images/PIf9ZPG2dnz2LDhSVwH8wkXipDvVITqT1J4K)

Si vous utilisez High Sierra (ou une version ultérieure), l'application `ScreenSaverEngine.app` a été déplacée vers un autre emplacement. Utilisez le code ci-dessous à la place de celui ci-dessus.

```
/System/Library/CoreServices/ScreenSaverEngine.app/Contents/MacOS/ScreenSaverEngine -background &
```

Il suffit de remplacer toutes les occurrences de `Frameworks/ScreenSaver.framework/Resources` par `CoreServices` et vous serez prêt à partir !

Cool, non ?

Le problème avec l'exécution de cette seule ligne de code est que si vous fermez la fenêtre du Terminal — ou si votre Mac s'endort — l'économiseur d'écran se ferme et votre fond d'écran revient à ce qu'il était par défaut. Pour gérer cela, nous devons aller un peu plus loin.

Pour détecter lorsque le Mac s'endort et se réveille, nous avons besoin d'un petit logiciel appelé « Sleepwatcher ». Vous pouvez le télécharger [ici](http://www.bernhard-baehr.de/sleepwatcher_2.2.tgz). Il suffit d'ouvrir le fichier et votre Mac extraira le fichier téléchargé (parfois il peut être nécessaire de l'extraire deux fois). Après l'extraction, vous obtiendrez un dossier « sleepwatcher_2.2 ». Déplacez simplement ce dossier sur le Bureau et exécutez les lignes de code suivantes dans le Terminal.

```
sudo mkdir -p /usr/local/sbin /usr/local/share/man/man8
```

Vous devrez peut-être entrer votre mot de passe après avoir collé cette ligne. Ensuite, exécutez :

```
sudo cp ~/Desktop/sleepwatcher_2.2/sleepwatcher /usr/local/sbin
```

Puis exécutez :

```
sudo cp ~/Desktop/sleepwatcher_2.2/sleepwatcher.8 /usr/local/share/man/man8
```

Super ! Vous avez installé Sleepwatcher avec succès.

Maintenant, ajoutons les lignes de code nécessaires pour que Sleepwatcher exécute l'économiseur d'écran lorsque votre Mac se réveille, et ferme l'économiseur d'écran lorsque votre Mac s'endort.

Sleepwatcher recherche et exécute deux fichiers, `.sleep` lorsque le Mac s'endort, et `.wakeup` lorsque le Mac se réveille. Nous devons simplement créer ces 2 fichiers dans le répertoire personnel de l'utilisateur.

Dans le Terminal, tapez `nano ~/.wakeup` puis collez le code ci-dessous.

```
#!/bin/bashosascript -e 'do shell script "/System/Library/Frameworks/ScreenSaver.framework/Resources/ScreenSaverEngine.app/Contents/MacOS/ScreenSaverEngine -background & EOF"'
```

Appuyez maintenant sur **Control + X** pour quitter. Lorsque le système demande si vous souhaitez enregistrer le fichier, appuyez sur **Y** puis sur la touche Entrée pour confirmer le nom du fichier. Cela créera le fichier `.wakeup`. Maintenant, pour créer le fichier `.sleep`.

![Image](https://cdn-media-1.freecodecamp.org/images/bAhqA6gKmCsnH2MBP7bdHc4yEox2raRLTATj)
_Le fichier .wakeup_

Comme ci-dessus, tapez `nano ~/.sleep` et collez le code ci-dessous.

```
#!/bin/bash
```

```
osascript -e 'do shell script "kill `ps -ax | grep [S]creenSaver | cut -c1-6` EOF"'
```

Encore une fois, appuyez sur **Control + X** pour quitter, **Y** pour enregistrer, puis sur la touche Entrée pour confirmer le nom du fichier. Le fichier `.sleep` sera maintenant créé.

![Image](https://cdn-media-1.freecodecamp.org/images/oGnweS4gcVcIWtmisaePYhRDrlTgahBL3U6h)
_Le fichier .sleep_

Dans le Terminal, exécutez la ligne de code ci-dessous.

```
chmod 700 ~/.sleep ~/.wakeup
```

Cela modifie les permissions des nouveaux fichiers afin qu'ils puissent être exécutés par Sleepwatcher.

Maintenant que vous avez créé les scripts, vous devez simplement ajouter Sleepwatcher à `launchd` afin qu'il puisse démarrer lorsque le système démarre, puis continuer à s'exécuter en arrière-plan. Collez le code suivant dans votre Terminal.

```
cp ~/Desktop/sleepwatcher_2.2/config/de.bernhard-baehr.sleepwatcher-20compatibility-localuser.plist ~/Library/LaunchAgents
```

Cela copiera le fichier de liste de propriétés Sleepwatcher afin qu'il puisse être ajouté à `launchd`. Il suffit maintenant de coller le code ci-dessous dans le Terminal pour ajouter Sleepwatcher à `launchd`.

```
launchctl load ~/Library/LaunchAgents/de.bernhard-baehr.sleepwatcher-20compatibility-localuser.plist
```

Super ! Vous pouvez maintenant redémarrer votre Mac et `launchd` exécutera les scripts Sleepwatcher au démarrage. Il suffit de mettre votre Mac en veille et de le réveiller. Vous serez alors accueilli avec un magnifique fond d'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/SdQIhifPuCV8vx-vSgqLlgLHmNDTpM59Weqa)
_Exemple du nouveau fond d'écran installé_

Si vous souhaitez tout désinstaller et revenir aux paramètres par défaut, suivez le lien ci-dessous.

[**Pour désinstaller, exécutez les lignes suivantes dans le Terminal une par une.**](https://medium.com/@aakaashjois/to-uninstall-run-the-following-lines-in-terminal-one-by-one-299916c8ff3b)  
[_Après avoir exécuté ces commandes, vous pouvez désinstaller l'économiseur d'écran Google et redémarrer votre Mac. Il devrait être supprimé. Faites-moi savoir..._medium.com](https://medium.com/@aakaashjois/to-uninstall-run-the-following-lines-in-terminal-one-by-one-299916c8ff3b)

J'espère que vous avez apprécié ce court tutoriel et que vous profiterez de ces magnifiques photos de fonds d'écran. Si vous avez aimé cela, cliquez sur le ❤️ et restez à l'écoute pour plus de contenu.