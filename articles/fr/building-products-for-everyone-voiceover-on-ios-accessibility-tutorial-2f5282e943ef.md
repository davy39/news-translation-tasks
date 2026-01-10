---
title: Comment créer des applications pour tous en utilisant VoiceOver sur iOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-19T17:04:02.000Z'
originalURL: https://freecodecamp.org/news/building-products-for-everyone-voiceover-on-ios-accessibility-tutorial-2f5282e943ef
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ClYE1SfHWy4XYzSDrlK3ug.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: Design
  slug: design
- name: iOS
  slug: ios
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment créer des applications pour tous en utilisant VoiceOver sur iOS
seo_desc: 'By Jayven N

  Getting started with accessibility


  There’s always those topics that people don’t talk about enough. Sometimes, those
  topics happen to be the most important ones. Accessibility is one of those topics.

  Goal

  This article talks about why acc...'
---

Par Jayven N

#### Commencer avec l'accessibilité

![Image](https://cdn-media-1.freecodecamp.org/images/Vv7jyJkcf6i4lRZs6UMtuVokbfLXWg-hNoZs)

Il y a toujours ces sujets dont les gens ne parlent pas assez. Parfois, ces sujets se trouvent être les plus importants. L'accessibilité est l'un de ces sujets.

### Objectif

Cet article parle de l'importance de l'accessibilité et de la manière dont vous pouvez vous mettre à la place d'un utilisateur de VoiceOver.

### Introduction

Les gens ont des handicaps.

Beaucoup de gens ont des handicaps.

Le handicap est normal.

Le handicap n'a pas besoin d'être quelque chose de dramatique comme une fracture. Cela peut être une douleur à l'épaule droite qui m'empêche de faire l'exercice A. Par conséquent, je suis handicapé pour faire l'exercice A. L'exercice B, en revanche, est tout aussi efficace comme exercice pour l'épaule que l'exercice A. Et il est possible pour les personnes avec ou sans douleur à l'épaule droite.

Une personne sur six aux États-Unis a un ou plusieurs handicaps.

Oui, une sur six. Regardez autour de vous. Comptez de un à six. Statistiquement, l'un de vous a un handicap.

**Les handicaps sont réels et pertinents.**

Tout le monde finit par se détériorer naturellement avec le temps. Le cerveau, les muscles, les yeux et les oreilles fonctionnent différemment avec le temps. Tout change avec le temps. Les humains ne font pas exception.

Parlons de l'importance de l'accessibilité et de la manière de commencer à créer des applications en gardant l'accessibilité à l'esprit.

### Pourquoi créer une application accessible ?

#### Avantage #1 : cela fait du bien

Cela fait du bien de faire de grandes choses. Vous pouvez laisser le monde un peu meilleur que vous ne l'avez trouvé. Rien ne vaut dormir comme un bébé en sachant que vous avez donné tout ce que vous pouviez au monde aujourd'hui pour un lendemain plus inclusif. Faire un impact positif selon vos idéologies fait toujours du bien.

#### Avantage #2 : taille de l'audience

Et si vous pouviez augmenter vos revenus de 16,7 % simplement en soutenant les utilisateurs d'accessibilité ? Cela semble être une très bonne affaire.

Si une entreprise réalise 100 000 000 USD par an, elle pourrait réaliser 117 000 000 USD en implémentant des fonctionnalités d'accessibilité. Cela en rendant l'application disponible pour une gamme plus large d'utilisateurs.

Voici le problème, personne ne veut être exclu d'une grande fête. Si vous avez une grande fête, vous voulez probablement inviter beaucoup de gens formidables. Si vous avez une grande application, vous voulez probablement que beaucoup de gens expérimentent votre chef-d'œuvre également.

Disons que les lettres d'invitation sont envoyées. Les lettres d'invitation atteignent les boîtes aux lettres. Les invités ouvrent joyeusement les lettres d'invitation et crient OUI ! dans le ciel.

Maintenant, parlons de venir à votre fête : tout le monde a une forme de transport préférée. Les gens peuvent voyager en voiture, en moto, en hélicoptère, en jet privé ou en jetpack.

Imaginez maintenant à quel point votre fête serait tragique si vous oubliiez les utilisateurs de jetpack. Alors, vous décidez d'enregistrer les voies aériennes de jetpack vers votre maison. Par conséquent, les utilisateurs de jetpack peuvent maintenant passer à votre fête.

N'est-ce pas formidable ? Votre fête devient plus amusante et les utilisateurs de jetpack peuvent également profiter de la fête. Tout le monde est gagnant.

Si votre application ne supporte pas certaines façons de l'utiliser, alors les gens peuvent trouver difficile de naviguer dans votre application. Ils décideront de ne pas utiliser votre application du tout. Nous pouvons atténuer cela et amener les utilisateurs de jetpack à bord.

#### Avantage #3 : créer une application accessible est difficile

Plaintes courantes concernant le développement de fonctionnalités d'accessibilité :

* Vitesse de développement lente
* Ressources insuffisantes
* La pensée "Je n'ai aucune idée par où commencer"

Ce sont des points valables.

Cela demande des efforts pour convaincre les gens autour de vous de vous donner du temps et de l'espace pour implémenter des fonctionnalités d'accessibilité dans votre application.

Cela demande du courage pour risquer votre nom et votre capital afin de convaincre le PDG que les fonctionnalités d'accessibilité en valent la peine.

Même si vous convainquez tout le monde de prêter attention à l'accessibilité, vous pouvez encore vous retrouver avec une page de questions sur ce qu'il faut faire ensuite. Étant donné que l'accessibilité est si peu discutée, vos recherches peuvent ne pas être aussi utiles que vous l'espériez.

Et la vérité est :

> Oui.

> C'est difficile.

> Mais, difficile est bon.

Voici le problème. Ajouter des fonctionnalités d'accessibilité à votre application est la bonne chose à faire. Au-delà d'être la bonne chose à faire, ajouter des fonctionnalités d'accessibilité peut aider votre application et votre entreprise à faire des bonds en avant et à se différencier.

Nommez cinq entreprises qui vous viennent à l'esprit et qui se soucient de créer des applications accessibles.

Je vais attendre...

C'est ça. Probablement moins de cinq.

Si la création d'applications accessibles était facile, alors tout le monde le ferait car cela atteint un public plus large.

Mais parce que la création d'applications accessibles est difficile, vous pouvez vous différencier. Vous faites quelque chose que la plupart des gens préféreraient ne pas faire. Pourtant, l'impact que vous pouvez avoir peut être transformateur pour certains utilisateurs.

#### Avantage #4 : découvrir les défauts de conception de votre application

Chaque appareil iOS dispose d'une fonctionnalité VoiceOver intégrée. VoiceOver est le lecteur d'écran d'iOS. Les lecteurs d'écran permettent aux personnes d'écouter les mots sur un écran. Pour les personnes qui trouvent difficile de lire avec leurs yeux, elles peuvent également absorber des informations avec leurs oreilles.

VoiceOver vous aide à découvrir les défauts de conception de l'application. Plus tard dans l'article, vous apprendrez à utiliser VoiceOver.

Pour découvrir les défauts de conception de l'application, vous devez simplement naviguer dans une application avec VoiceOver activé. La fonctionnalité VoiceOver activée signifie généralement qu'un utilisateur peut difficilement voir ce qui se trouve sur l'écran. Cela signifie que vous devriez pouvoir naviguer sans dépendance visuelle.

Ensuite, répondez aux questions suivantes :

* L'application semble-t-elle correcte ?
* L'application prend-elle trop de temps pour passer du point A au point B ?
* L'application présente-t-elle l'UI et les mises en page dans l'ordre chronologique basé uniquement sur le son ?

Ces problèmes peuvent être explicitement exposés par VoiceOver et peuvent vous donner de nouvelles perspectives de conception. Vous pouvez utiliser VoiceOver pour aider à améliorer la navigation, la simplicité et l'organisation de votre application.

#### Avantage #5 : diffusez votre application par le bouche-à-oreille

Le bouche-à-oreille est l'un des plus grands mécanismes de diffusion de messages. Vous avez déjà voulu attirer l'attention de quelqu'un ? L'une des meilleures façons de le faire est d'avoir une introduction. Cela est dû au fait que le bouche-à-oreille peut contenir beaucoup de confiance.

Imaginez un homme nommé Jon Mack. Il se trouve qu'il a une mauvaise vue. Il utilise l'application Non Accessible A, l'application Non Accessible B et l'application Non Accessible C. Toutes les applications sont mal conçues pour les personnes ayant une déficience visuelle.

Jon est une personne capable. Jon a des amis. Jon et ses amis avancent vers l'âge avancé.

Un soir, l'application Accessible arrive. L'application est conçue en pensant à un large public. Jon utilise l'application Accessible. Il l'adore.

Jon partage l'application Accessible avec des amis, des membres de la famille et des collègues.

Jon parle dans le mégaphone. L'application Accessible se diffuse et le fait par le bouche-à-oreille. L'application Accessible gagne. Jon et ses proches gagnent également. C'est une situation gagnant-gagnant.

Lorsque votre application est exceptionnelle, les gens veulent la partager. Les gens partagent votre application parce que cela en dit long sur eux.

Vos utilisateurs sont importants, alors faisons-les se sentir importants.

Il est temps de passer à l'action.

### Par où commencer

Comprenons comment l'un de vos utilisateurs de VoiceOver peut utiliser votre application.

Nous allons configurer VoiceOver sur iOS.

#### Configuration de VoiceOver sur iOS

Déverrouillez votre appareil iOS.

Ouvrez l'application **Réglages**.

Appuyez sur **Général**.

![Image](https://cdn-media-1.freecodecamp.org/images/UChK9z2ihhlmezfUvgIGvq58A2QDNeo4tKu7)

Appuyez sur **Accessibilité**.

![Image](https://cdn-media-1.freecodecamp.org/images/16s7CAfLWVpS2FKtTjK4I26KWkBoNJ5WkOXy)

Appuyez sur **Raccourci d'accessibilité**.

![Image](https://cdn-media-1.freecodecamp.org/images/pjJje2y1bBOAgITTNhER4aS8GV76mUlkWbXc)

Vous devriez voir une liste de fonctionnalités d'accessibilité intégrées.

Appuyez sur **VoiceOver**.

![Image](https://cdn-media-1.freecodecamp.org/images/n27lI17e86JnlSs9TSLv7yw3Ic1-3kdXkGvQ)

Super.

Maintenant, balayez vers le haut depuis l'application **Réglages** pour entrer dans la disposition de l'écran d'accueil.

![Image](https://cdn-media-1.freecodecamp.org/images/LkoSRm8TtlmW-VunZrXz5jipNdUA9SG-o31V)

### Navigation sur iOS avec VoiceOver

Il est temps d'essayer VoiceOver. Voici quatre gestes utiles pour utiliser VoiceOver :

1. Balayez vers la gauche ou la droite — naviguez dans l'UI

2. Double-tap — sélectionnez

3. Balayez vers le haut ou vers le bas — choisissez parmi les options disponibles si elles existent

4. Balayez vers le haut depuis le bas avec une seule vibration — retour à l'écran d'accueil

Mettons le chapeau d'action. Commençons à utiliser VoiceOver.

**Triple-cliquez** sur le bouton d'alimentation.

![Image](https://cdn-media-1.freecodecamp.org/images/n2QwR1f1jWA207JQoQ0rbktOwETXb69EgCFC)

VoiceOver est activé.

Maintenant, balayez vers la droite jusqu'à ce que l'application **Réglages** soit sélectionnée.

Double-tap pour ouvrir l'application **Réglages**.

![Image](https://cdn-media-1.freecodecamp.org/images/w0jx7AkFhsP1ylY5CtqQGUKmxXeyx3QZr8Mi)

Super.

Maintenant, balayez vers la droite jusqu'à ce que **Général** soit sélectionné.

Double-tap pour sélectionner **Général**.

![Image](https://cdn-media-1.freecodecamp.org/images/b1LxT1-4u4yKf1kcH37jopImpV-gNcNV1j6H)

Balayez vers la droite jusqu'à ce que **Accessibilité** soit sélectionné.

Double-tap pour sélectionner **Accessibilité**.

![Image](https://cdn-media-1.freecodecamp.org/images/lJc8iXIM6rjPnP9PyUtCmfTEc8uGhJMUn3Sa)

Balayez vers la droite jusqu'à ce que **VoiceOver** soit sélectionné.

Double-tap pour sélectionner **VoiceOver**.

![Image](https://cdn-media-1.freecodecamp.org/images/CnUEPCNVCjvXZSQNFrNI0xCXp2UPboCM2dgD)

Balayez vers la droite jusqu'à ce que le curseur **Vitesse de parole** soit sélectionné.

Balayez vers le haut ou vers le bas avec un doigt rapidement pour ajuster la vitesse de parole.

![Image](https://cdn-media-1.freecodecamp.org/images/WUOlj4RvRtCzundoZPWqcu8TqXV147qS0Axs)

Une fois que vous avez la vitesse de parole souhaitée, balayez vers le haut depuis le bas avec une seule vibration pour revenir à l'écran d'accueil.

![Image](https://cdn-media-1.freecodecamp.org/images/ICXsddJBrgdzkMWkhLPZLmsipCtjGY4EFsb7)

Il s'avère que VoiceOver est assez pratique. Vous pouvez transformer presque n'importe quoi sur iOS en un livre audio.

Je me suis définitivement surpris à utiliser VoiceOver aussi souvent que tous les jours pour lire du texte sur iOS. Cela réduit la charge cognitive. En même temps, cela peut augmenter la compréhension grâce à la combinaison de lecture et d'écoute.

Vous êtes formidable. Vous venez de franchir l'étape la plus difficile. L'étape que peu de gens ont franchie. La première étape. Félicitations, vous avez augmenté votre capacité à vous mettre à la place de beaucoup plus de gens. Vous êtes sur la bonne voie pour créer des applications encore plus exceptionnelles.

### DÉFI : Utilisez votre application les yeux bandés

Voici une méthode pour évaluer l'accessibilité de votre application.

Activez VoiceOver.

Triple-tap à trois doigts.

![Image](https://cdn-media-1.freecodecamp.org/images/yamurZqDKLCOF7oBqWrMS9Yfgv5nuIpDmDYJ)

Cela active le mode rideau et votre écran devient complètement noir.

Maintenant, naviguez dans votre application avec VoiceOver en mode rideau activé.

Lorsque la navigation de votre application est sans effort avec le mode rideau, vous êtes sur le point de créer une application exceptionnellement accessible.

### Remarques finales

Je crois que rendre les applications accessibles pousse l'humanité dans la bonne direction. Créer une expérience d'application exceptionnelle pour tous les utilisateurs est une victoire pour les créateurs d'applications et les utilisateurs.

J'espère voir plus de nos applications préférées supporter pleinement les fonctionnalités d'accessibilité.

Veuillez partager cet article si vous l'avez trouvé utile.

### Remerciements spéciaux

Cet article est possible grâce à Daud A., Kane C., Esther H., Todd K., Tim C., Tim I., Lilit B., Cliff W., et Shawn.

### Solutions pour entreprises

Pour les entreprises intéressées, je vous recommande de [contacter 2359 Media pour des solutions d'entreprise](http://2359media.com/contacts/).