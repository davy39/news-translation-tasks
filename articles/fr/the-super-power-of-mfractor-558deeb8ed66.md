---
title: Les (super) pouvoirs de MFractor et comment ils peuvent faciliter votre vie
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-30T14:31:00.000Z'
originalURL: https://freecodecamp.org/news/the-super-power-of-mfractor-558deeb8ed66
coverImage: https://cdn-media-1.freecodecamp.org/images/1*m8FRApkjXvrgg3OowObeEw.jpeg
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: visual studio
  slug: visual-studio
- name: Xamarin
  slug: xamarin
seo_title: Les (super) pouvoirs de MFractor et comment ils peuvent faciliter votre
  vie
seo_desc: 'By Łukasz Ławicki

  If you ask a Xamarin developer what could be changed in Xamarin development, they
  would for sure mention one of the following:


  build time

  performance

  app start time

  previewers

  removing bin/obj from IDE

  lack of Image wizard in Visua...'
---

Par 1ukasz 1awicki

Si vous demandez à un développeur Xamarin ce qui pourrait être changé dans le développement Xamarin, il mentionnerait sûrement l'un des éléments suivants :

* temps de construction
* performance
* temps de démarrage de l'application
* aperçus
* suppression de bin/obj depuis l'IDE
* manque d'assistant d'images dans Visual Studio pour Mac
* pas d'IntelliSense XAML,

et ainsi de suite... et si je suis honnête, les réponses ci-dessus sont justes. Mais hé, nous sommes les développeurs ! Si Microsoft ne nous donne pas ces fonctionnalités, essayons de trouver des solutions de contournement ou inventons quelque chose par nous-mêmes.

Il existe plusieurs bibliothèques et extensions d'IDE qui facilitent notre vie. L'une d'entre elles est certainement MFractor, une extension super puissante pour Visual Studio pour Mac.

### Alors, qu'est-ce que MFractor ?

MFractor est une extension pour Visual Studio pour Mac. Elle a été fondée en 2015 en Australie. Après 3,5 ans sur le marché, elle a gagné la confiance et l'amour des gens. « Comment a-t-elle fait cela ? » pourriez-vous demander. C'est parce qu'elle étend Visual Studio pour Mac avec des fonctionnalités qui manquent au quotidien.

* Vous voulez XAML IntelliSense ? C'est fait. Il suffit d'installer MFractor.
* Vous voulez supprimer les dossiers bin/obj dans votre IDE ? MFractor peut le faire. (Au fait, à mon avis, il semble ridicule que nous ayons besoin d'extensions pour cela ou que nous devions les supprimer de temps en temps. Quelque chose ne fonctionne définitivement pas...)
* **Et voici la bombe :** Vous voulez avoir un assistant d'images dans Visual Studio pour Mac, afin de pouvoir gérer les ressources ?

Je savais que vous voudriez cela ! Je vous ai déjà parlé de MFractor ? Och, je l'ai fait !

Soyons clairs : **MFractor est un outil super puissant lorsque vous développez des applications avec Visual Studio sur votre Mac.**

Vous ne croyez peut-être pas mes mots, alors vérifions comment cela fonctionne dans la vie réelle.

### Installation

C'est très facile. Dans VS4Mac, ouvrez simplement **Extensions...** sous le menu Visual Studio, cliquez sur **Gallery** et recherchez **MFractor**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3KaeayISJSUFKXa3YA4wrg.png)

Voilà. Une chose à noter : vous aurez installer au lieu de **Disable/ Uninstall...** Installez-le simplement et suivez les étapes requises et une fenêtre contextuelle s'ouvrira. Après l'avoir installé, passons à la partie intéressante.

### Gestionnaire d'images

Commençons par cette fonctionnalité totalement géniale. Elle est sortie assez récemment, donc elle est encore assez fraîche.

Supposons que vous souhaitez gérer les ressources d'images dans votre projet, mais que vous détestez vraiment le faire manuellement.

Découvrez ce dont MFractor est capable :

![Image](https://cdn-media-1.freecodecamp.org/images/1*q_4qD5gd8jDy-9B5gnSjQg.png)

Comme vous pouvez le voir, vous avez une liste de toutes les icônes incluses dans le projet avec des miniatures. Lorsque vous cliquez sur l'élément, vous pouvez voir l'image en plus grande taille. De plus, vous pouvez remarquer qu'il y a une liste déroulante où vous pouvez sélectionner votre projet et vérifier quelles icônes sont incluses dans le projet (SPYROtalks est le nom de mon projet).

#### Que pouvez-vous faire dans le gestionnaire d'images ?

**Importer une nouvelle ressource d'image**

![Image](https://cdn-media-1.freecodecamp.org/images/1*Cwqa92AX-6dubJH-BPFkig.png)

L'ajout de la ressource est vraiment facile.

1. Vous sélectionnez simplement l'image depuis votre ordinateur. MFractor devrait détecter automatiquement la densité de l'image. Si vous n'êtes pas d'accord, vous pouvez la changer.
2. Après cela, vous devez fournir le **Nom de la ressource**. Juste, non ?
3. Maintenant, vous devez décider à quels projets vous souhaitez ajouter la ressource.

En gros, c'est tout ce que vous devez fournir. Si vous le souhaitez, vous pouvez redimensionner une image ou l'optimiser. En écrivant cet article, j'ai décidé de vérifier à quel point l'optimisation des images est bonne. Pour cela, j'ai pris 10 photos et optimisé chacune d'entre elles. Voici les résultats :

![Image](https://cdn-media-1.freecodecamp.org/images/1*7pOZo3uGONbRbwqAvxf5Og.png)
_Résultats de l'optimisation_

Comme vous pouvez le voir dans le tableau ci-dessus, en général, les résultats étaient assez bons. Une moyenne de 54 % en fait un bon résultat. Ce qui est intéressant, cependant, c'est le fait qu'une image était plus grande après optimisation que les autres. Pourquoi ? Je ne sais pas.

#### Supprimer une image

Dans le gestionnaire d'images, vous pouvez également supprimer des ressources. Ce qui est génial et fait gagner du temps, c'est le fait qu'il supprimera toutes les densités de ressources en une seule fois. Pas besoin de la supprimer 6 (ou même plus) fois. Vraiment un gain de temps.

#### Optimiser toutes les images

Au cas où vous auriez oublié d'optimiser votre ressource lors de son ajout, vous pouvez optimiser toutes les images plus tard. Bon à savoir.

Si vous souhaitez en savoir plus sur les ressources d'images, allez-y et lisez l'article de Matthew disponible sur le blog de MFractor [ici](https://www.mfractor.com/blogs/news/simplified-image-asset-management-for-xamarin-apps).

### XAML IntelliSense

Si vous n'êtes pas très expérimenté dans le développement avec Xamarin.Forms, vous pourriez trouver le développement d'interfaces utilisateur XAML un cauchemar. D'un autre côté, même si vous êtes un développeur expérimenté de Xamarin.Forms, vous pourriez vous frustrer en utilisant XAML.

Tout d'abord, en raison du manque d'aperçu (il y en a un, mais soyons honnêtes : il ne fonctionne pas pour les vues complexes), vous créez des interfaces utilisateur presque à l'aveugle. Vous devez utiliser votre imagination. Ne serait-il pas mieux si nous avions un LiveXAML intégré ou quelque chose de similaire ? Malheureusement, il ne semble pas que Microsoft ait l'intention de nous fournir quelque chose pour le moment. Dommage.

Deuxièmement, en raison du manque d'IntelliSense XAML. Ce serait bien de l'avoir, afin que lorsque vous créez des liaisons vers votre ViewModel, vous puissiez sélectionner la propriété dans la liste déroulante au lieu de la taper vous-même. Qui n'a jamais fait une faute de frappe dans le nom de la propriété, compilé le code et s'est ensuite demandé pourquoi cela ne fonctionnait pas ?

#### MFractor à la rescousse !

Une autre grande fonctionnalité de MFractor est XAML IntelliSense. Il peut vous suggérer les noms des propriétés dans ViewModel, afin que vous puissiez vous y lier. De plus, il peut suggérer les noms des images que vous avez dans les ressources et bien plus encore. Vous ne me croyez pas ? Allez-y et vérifiez ces gifs :

![Image](https://cdn-media-1.freecodecamp.org/images/1*SMz2x4MgrEzklBpRU9gfEw.gif)

Juste pour expliquer : dans mon projet, j'ai trois icônes : _Icon.png, Launcher_Foreground.png,_ et _logo_spyrotalks.png._ Comme vous pouvez le voir, MFractor me donne la possibilité d'en choisir une. Sympa !

Passons aux liaisons. Comme vous pouvez le supposer, MFractor suggère les propriétés de la même manière qu'il suggère les images.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ny7GBRA2lTcVx_eBSZ7z4g.gif)

Comme vous pouvez le voir dans mon ViewModel, j'ai 5 propriétés liables. Ce que j'aime vraiment, c'est le fait qu'avec MFractor, il est presque impossible de faire une faute de frappe dans le nom de la propriété.

#### **Générer une propriété de ViewModel**

Êtes-vous une personne qui préfère écrire les vues en premier ? Si oui, j'ai une bonne nouvelle pour vous : avec MFractor, vous pouvez générer des propriétés de ViewModel à partir de votre vue.

Lors de la création de la vue, vous pourriez constater que vous avez oublié de créer une propriété ou une autre. Avec MFractor, vous pouvez les créer sans changer de fichier. Sympa, non ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*tiv0sQZIqsED0P3sSsdRkA.gif)

#### **Aller à une utilisation de la propriété de ViewModel**

De temps en temps, vous pourriez vouloir vérifier où la propriété est utilisée. Malheureusement, lorsque vous recherchez des références dans Visual Studio, il ne trouvera pas celles que vous avez dans XAML. Bien sûr, comme vous pouvez le supposer, MFractor peut trouver ces références pour vous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DKF1i0jXygiG5PfqTU1Cwg.gif)

### Assistant MVVM

Ceci est quelque chose qui n'a pas été mentionné au début de ce blog car il n'était pas encore sorti. Selon l'annonce marketing dans la version 3.7.3, l'**Assistant MVVM** sera disponible.

Selon le tweet de Matthew Robbins (le fondateur de MFractor), vous pourrez créer à la fois des vues et des ViewModels avec (presque) un seul clic.

Ce qui est bien avec cette fonctionnalité, c'est qu'elle vous donne le contrôle sur l'endroit où vous placez les fichiers et quelles sont les classes de base. Cela semble prometteur, mais j'avais quelques questions : supportera-t-il également Xamarin.Native ? Si nous ajoutons XAML avec BaseContentPage, fonctionnera-t-il dès la sortie de la boîte ?

J'ai donc installé la version 3.7.3, et il y a un **Gestionnaire MVVM**. Il ressemble à celui de l'image ci-dessus. Il y a trois façons d'y accéder : depuis le menu MFractor, depuis les options de la solution, et avec le raccourci **Cmd + Shift + M**. Pour l'instant, le gestionnaire fonctionne uniquement pour les projets Xamarin.Forms.

Si vous voulez que ViewModel dérive de BaseClass, vous devrez peut-être écrire la classe avec un espace de noms avant. Sinon, vous devrez importer la classe lorsque le VM est créé.

#### MISE À JOUR 31.01

Ce que vous lirez ci-dessous n'est plus valable (problème XAML). J'ai soulevé le problème ci-dessus, et après 33h, il a été résolu. La version 3.7.5 devrait avoir corrigé cela. Comme je l'ai écrit dans mon tweet, c'est ainsi que les bugs devraient être résolus ! Fin de la mise à jour ;-)

Le problème est avec le fichier XAML. Comme je l'avais supposé, dériver de, par exemple, BaseContentPage ne serait pas si facile. Lorsque vous voulez que la vue dérive de votre BaseContentPage, vous devez alimenter le gestionnaire MVVM avec ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*1yGsBw8qPVqFUxilS1WTEQ.png)

Le code visible est-il celui dont nous avons besoin ? Pas complètement. Il est similaire à celui que nous voulons mais pas exactement le même. Nous avons besoin d'un code comme celui-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*edLNzudQii71JenMrW0eSg.png)

Ce n'est pas un grand changement, mais nous devons le gérer nous-mêmes. Je peux tout à fait comprendre que ce n'est pas une tâche facile à accomplir. Je crois qu'il est toujours préférable d'ajuster légèrement les fichiers créés plutôt que de les créer à partir de zéro.

Si vous êtes intéressé, sur le blog de MFractor [blog](https://www.mfractor.com/blogs/news/generating-viewmodels-in-xamarin-forms-with-the-mvvm-wizard), vous pouvez en savoir plus sur le gestionnaire MVVM.

### bin/obj

Comme je l'ai mentionné au début de cet article, je ne suis pas sûr de ce que je pense des dossiers bin/obj. Tout d'abord, vous devez les supprimer assez souvent lors du développement d'une application Xamarin. Je pense que c'est un problème.

Pourquoi devons-nous le faire ? Si c'est un problème connu (et d'après mes conversations avec mes collègues, je crois que c'est le cas), ne devrions-nous pas avoir une option pour supprimer ces dossiers dans notre IDE ? Le faire manuellement prend tellement de temps. Bien sûr, vous pouvez avoir un script pour le faire, mais est-ce quelque chose que nous devons implémenter nous-mêmes ?

Heureusement, MFractor a une fonctionnalité qui peut supprimer ces dossiers pour vous. Comment ? Très simple. Vérifiez cela :

![Image](https://cdn-media-1.freecodecamp.org/images/1*egwuFt435DqROt58nB6sJg.gif)

Ici, vous avez des options : soit supprimer les dossiers de sortie (supprime bin/obj et les packages NuGet), soit vous pouvez uniquement effacer les packages NuGet.

### Conclusion

Alors, quels sont les inconvénients de l'utilisation de MFractor ? Certains pourraient dire que le prix de **MFractor Professional** (200 AUD par an) peut être un problème. Mais hé ! Est-ce vraiment beaucoup pour une licence à vie ? Je ne le pense pas. Surtout lorsque vous prenez en considération le nombre d'heures perdues à cause, par exemple, d'une faute de frappe dans votre XAML ou de l'ajout de ressources d'images.

Publié à l'origine sur mon [blog](http://lukaszlawicki.pl/mfractor/) ?