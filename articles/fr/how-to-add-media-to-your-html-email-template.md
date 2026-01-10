---
title: Comment ajouter des médias à votre modèle d'email HTML
subtitle: ''
author: Fanny Nyayic
co_authors: []
series: null
date: '2024-04-23T17:40:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-media-to-your-html-email-template
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/Add-Media-to-Your-HTML-Email-Template.png
tags:
- name: email
  slug: email
- name: HTML
  slug: html
seo_title: Comment ajouter des médias à votre modèle d'email HTML
seo_desc: "In my previous article, \"How to Create a Responsive HTML Email Template,\"\
  \ we explored the fundamentals of designing and coding a simple HTML email template\
  \ that adapts beautifully across different devices and email clients. \nI got a\
  \ couple of questio..."
---

Dans mon article précédent, "[How to Create a Responsive HTML Email Template](https://www.freecodecamp.org/news/how-to-create-a-responsive-html-email-template/)", nous avons exploré les bases de la conception et du codage d'un modèle d'email HTML simple qui s'adapte parfaitement à différents appareils et clients de messagerie. 

J'ai reçu quelques questions sur l'ajout de médias au modèle d'email HTML.

En partant de cette base, je vais vous guider à travers différentes façons d'ajouter des médias à votre modèle d'email HTML. L'ajout de médias tels que des images, des vidéos et de l'audio peut augmenter significativement l'engagement et l'efficacité de vos communications. 

### Exigences

* Un modèle d'email HTML simple. Vous pouvez en créer un en suivant [ce guide](https://www.freecodecamp.org/news/how-to-create-a-responsive-html-email-template/). 

## Comment ajouter des images à votre modèle d'email

Les images sont le type de média le plus courant ajouté aux emails. Voici comment les inclure dans vos modèles d'email HTML :

* Avant d'ajouter une image, assurez-vous qu'elle est correctement dimensionnée et optimisée pour une utilisation sur le web. Une pratique courante consiste à garder la largeur de l'image inférieure à 600 pixels pour s'adapter à la plupart des clients de messagerie sans mise à l'échelle. Pour cet exemple particulier, nous avons une image de stock et nous l'avons redimensionnée à 600 x 750 pixels comme montré ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/600x750.jpg)
_ceci est l'image que nous allons télécharger_

* Téléchargez votre image sur un serveur web fiable ou un réseau de diffusion de contenu (CDN). Vous aurez besoin d'une URL stable pour la référencer dans votre email.  

Pour cet exemple, nous utiliserons [le site imgbb](https://imgbb.com/) et téléchargerons notre image. Cliquez sur "Start Uploading" et choisissez l'image.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/screely-1713853483929.png)
_imgbb est l'une des plateformes d'hébergement d'images gratuites_

Après avoir choisi l'image à utiliser, sélectionnez "Don't Autodelete" et cliquez sur Upload.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/screely-1713853781152.png)
_Choisissez Don't Autodelete dans le menu déroulant_

Après le téléchargement, une URL sera générée. Cliquez sur le menu déroulant et choisissez "HTML full linked"

![Image](https://www.freecodecamp.org/news/content/images/2024/04/screely-1713854879006-copy-code.png)
_Le code intégré généré_

* Copiez le code HTML généré et insérez-le dans une section souhaitée de votre modèle d'email comme montré.

```html
<a href="https://ibb.co/XpRp2N8">
    <img src="https://i.ibb.co/q9Q9yX5/600x750.jpg" alt="600x750" border="0"></a>
```

N'hésitez pas à essayer d'autres options de code intégré pour tester comment votre image apparaîtra dans le modèle d'email. 

Voici le résultat de l'image insérée :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/screely-1713854742721.png)
_image insérée avec succès dans notre modèle d'email_

**Note** : Incluez toujours l'attribut `alt` pour fournir un texte alternatif dans les scénarios où l'image ne peut pas être affichée.

## Comment intégrer des vidéos dans votre modèle d'email

La lecture directe de vidéos n'est pas prise en charge dans la plupart des clients de messagerie. Au lieu de cela, vous pouvez intégrer une miniature cliquable qui mène à une vidéo hébergée en ligne :

* **Créez une miniature** : Capturez une image de votre vidéo ou créez un graphique personnalisé qui représente le contenu de la vidéo. Cela servira de placeholder. Dans cet exemple, nous utiliserons la même image comme miniature.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/screely-1713855881423-thumbnail.png)

* Dans le menu déroulant, choisissez HTML thumbnail linked. Copiez le code et collez-le dans votre modèle d'email.

```html
<a href="https://ibb.co/XpRp2N8"><img src="https://i.ibb.co/XpRp2N8/600x750.jpg" alt="600x750" border="0"></a>
```

* **Lien vers la vidéo** : Modifiez le code ci-dessus pour utiliser la miniature comme image cliquable liée à l'URL de la vidéo. 
* Changez l'URL dans le `<a href ="">` pour le lien vidéo comme montré ci-dessous.

```html
<a href="https://youtu.be/UG8rjxYBfFg?si=xU2zqCtQW5-2z7nw">
    <img src="https://i.ibb.co/XpRp2N8/600x750.jpg" alt="600x750" border="0"</a>

```

Ce snippet HTML crée une image liée sans bordure. Et voici comment elle apparaîtra dans notre modèle d'email :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/screely-1713856590062-thumbnail.png)
_la miniature liée apparaîtra comme ceci_

## Comment intégrer des vidéos YouTube dans votre modèle d'email

Alternativement, vous pouvez directement intégrer une vidéo YouTube à votre modèle d'email. Voici comment :

* Allez sur YouTube et choisissez la vidéo que vous souhaitez intégrer.
* Cliquez sur **partager -> intégrer** et un `iframe` sera généré. Voici un exemple :

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/UG8rjxYBfFg?si=nYBBM032nvBn5tNZ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

* Copiez le `iframe` et collez-le dans une section `<td>` de votre code de modèle d'email HTML. Et vous aurez quelque chose qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/screely-1713857296270-youtube.png)
_ceci est un exemple de vidéo YouTube dans un modèle d'email_

## Comment ajouter de l'audio à votre modèle d'email

L'ajout de fichiers audio directement aux emails n'est également pas pris en charge par la plupart des clients de messagerie. Comme pour les vidéos, vous pouvez inclure un lien vers le fichier audio :

* **Hébergez le fichier audio** : Téléchargez votre fichier audio sur une plateforme ou un serveur approprié. Il existe un certain nombre de plateformes audio, comme Google Drive, votre propre site web, YouTube, SoundCloud, etc.
* Pour cet exemple, nous utiliserons une plateforme appelée [audio.com](https://audio.com/). Créez simplement un compte en cliquant sur "join now for free" ou connectez-vous si vous avez déjà un compte.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/screely-1713861900834.png)

Cliquez sur télécharger et choisissez votre fichier .mp3 qui sera stocké dans votre compte. Une fois l'audio terminé, cliquez sur l'icône de partage.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/screely-1713862121050.png)

* Cela vous mènera à quelques options où vous pouvez copier le lien ou simplement intégrer le lien :

Cliquez sur intégrer, et vous verrez un aperçu de la façon dont votre audio apparaîtra. Copiez le code et collez-le dans la section de votre modèle d'email.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/screely-1713862229377.png)
_code généré par audio.com qui peut être intégré dans le modèle d'email_

Vous pouvez également éliminer la `div` et utiliser simplement l'`iframe`. N'hésitez pas à supprimer les parties que vous ne souhaitez pas voir apparaître dans le modèle d'email et personnalisez-le selon vos préférences. 

Voici le code :

```html
<div style="height: 228px; width: 600px;">
<iframe src="https://audio.com/embed/audio/1797114509131910?theme=image"
                            style="display:block; border-radius: 6px; border: none; height: 204px; width: 600px;"></iframe><a href='https://audio.com/nyayic-fanny' style="text-align: center; display: block; color: #A4ABB6; font-size: 12px; font-family: sans-serif; line-height: 16px; margin-top: 8px; overflow: hidden; white-space: nowrap; text-overflow: ellipsis;">@nyayic-fanny</a>
</div>
                       
```

Voici le résultat final pour ce qui précède :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/screely-1713862296389.png)
_notre audio apparaîtra comme ceci dans notre modèle d'email_

### Utilisation de la balise `audio`

Outre l'intégration, nous pouvons utiliser la balise audio et simplement ajouter l'URL à notre source audio comme montré ci-dessous : 

```html
 <p>Audio ajouté via la balise audio</p> <br><br>
   <audio controls="controls">
   <source src="https://audio.com/nyayic-fanny/audio/past-life-jvna.mp3">
      <p>? Écouter : <a href="https://audio.com/nyayic-fanny/audio/past-life-jvna.mp3">Audio</a> (mp3)</p>
       </audio>
```

Changez simplement l'URL par votre `URL audio`. Et voici à quoi devrait ressembler notre modification complète.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/final-newsletter.png)
_notre modèle d'email HTML modifié_

**Note** : Hotmail et les clients qui ne supportent pas HTML5 ne fonctionneront pas !

## Bonnes pratiques pour les médias dans les emails HTML

Lors de l'intégration de médias dans les emails HTML, tenez compte des conseils suivants pour optimiser la compatibilité et l'expérience utilisateur :

* Utilisez toujours des URLs complètes et absolues pour les images, vidéos et audio afin de garantir leur chargement correct dans tous les clients de messagerie.
* Testez vos emails : Différents clients de messagerie affichent le contenu HTML de diverses manières. Utilisez des outils comme Litmus ou Email on Acid pour tester comment votre email est rendu sur différentes plateformes.
* Gardez les temps de chargement à l'esprit : Optimisez la taille des fichiers médias pour garantir que vos emails se chargent rapidement, ce qui est crucial pour retenir l'attention du destinataire et améliorer l'engagement.
* Pensez à l'accessibilité : Fournissez un texte alternatif descriptif pour les images et des légendes ou transcriptions pour les contenus audio et vidéo.

Bien qu'il existe des limitations à ce que les clients de messagerie peuvent supporter, l'utilisation d'images liées pour les vidéos et les fichiers audio fournit une solution conviviale qui fonctionne sur la plupart des plateformes. 

Assurez-vous toujours de tester vos emails de manière approfondie et suivez les bonnes pratiques pour garantir une expérience utilisateur fluide et engageante.

Bon codage !