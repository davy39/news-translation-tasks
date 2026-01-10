---
title: J'avais besoin d'un professeur de guitare. Alors j'ai transformé mon Alexa
  en un professeur.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-03T21:18:41.000Z'
originalURL: https://freecodecamp.org/news/who-can-teach-you-the-guitar-better-youtube-or-alexa-96e8cef77470
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-vVeRVJfQZb2IgpH2RBJyQ.jpeg
tags:
- name: amazon echo
  slug: amazon-echo
- name: music
  slug: music
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: J'avais besoin d'un professeur de guitare. Alors j'ai transformé mon Alexa
  en un professeur.
seo_desc: 'By Terren Peterson

  Learning how to play guitar takes practice. A lot of practice. One of my self-improvement
  goals is to get better playing the guitar.

  An area I’m working on now is finger positioning on the fretboard. This requires
  memorization of d...'
---

Par Terren Peterson

Apprendre à jouer de la guitare demande de la pratique. Beaucoup de pratique. L'un de mes objectifs d'amélioration personnelle est de mieux jouer de la guitare.

Un domaine sur lequel je travaille actuellement est le positionnement des doigts sur le manche. Cela nécessite la mémorisation de différents motifs de placement des doigts sur les cordes. L'amélioration demande une pratique fréquente et un coaching, mais c'est très gratifiant.

En recherchant ce qui est disponible sur Internet, j'ai découvert de nombreux musiciens qui donnent un coup de main. Un média populaire où ils partagent est YouTube. La vidéo ci-dessous a plus de cinq millions de vues, démontrant son utilisation généralisée. L'instructeur explique les bases du positionnement des doigts et des notes.

Ces vidéos sont excellentes pour commencer, mais ce qui se perd, c'est comment se concentrer complètement sur la musique. Concentrer mon attention sur le placement des doigts et la reconnaissance des notes est ainsi que je progresse.

J'ai essayé différents artistes YouTube dans une tentative de trouver le coach parfait. La limitation à laquelle je continue de me heurter n'est pas l'artiste ou la qualité audio de l'appareil. Plutôt, la limitation est le média lui-même d'une vidéo jouant sur mon téléphone ou mon ordinateur portable. Lorsque je pratique, je ne réussis jamais un exercice correctement dès la première tentative. Étant donné l'interface de YouTube, il est difficile de rejouer des sections étant donné que mes mains sont sur ma guitare.

### **Alors j'ai créé la compétence Alexa Guitar Teacher**

Cela met en lumière les applications vocales interactives qui sont meilleures que les plateformes mobiles traditionnelles. Une application vocale n'a pas besoin de l'utilisation de vos mains. La lecture d'une section nécessite ma voix, et mes mains restent sur la guitare. Pour les apprenants comme moi qui doivent répéter les leçons pour les maîtriser, être sans les mains est un énorme atout.

J'ai essayé ce qui était disponible dans le magasin de compétences, mais j'ai trouvé des compétences très simplistes. Certaines ne comportaient même pas le son d'une guitare, mais plutôt une voix monotone donnant des instructions. Alors j'ai fait ce que tout ingénieur logiciel ferait, et j'ai créé la mienne appelée « [Guitar Teacher](https://www.amazon.com/Drawrz-com-Guitar-Teacher/dp/B01N805N3E/ref=sr_1_1?s=digital-skills&ie=UTF8&qid=1489286872&sr=1-1&keywords=guitar+teacher) ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZjxeaGi4Js4i5UqxCh6KTQ.png)

La plateforme Alexa a la capacité d'interagir avec quelqu'un en utilisant uniquement sa voix. Cela libère les doigts pour se concentrer sur le jeu des cordes. Voici une rapide démonstration de la compétence avec certaines des fonctionnalités principales.

### Comment cela fonctionne-t-il ?

Malgré ce que vous voyez avec la plupart des compétences sur la plateforme, Alexa peut faire plus que parler. Les applications vocales plus complexes utilisent une syntaxe connue sous le nom de SSML. Cela mélange la voix de la machine avec des sons enregistrés dans un fichier MP3.

Voici la syntaxe requise qui utilise Alexa pour expliquer comment positionner vos doigts pour jouer un accord standard. Cette section du code joue le son de l'accord pour renforcer ce qui sort d'une vraie guitare.

```
{"outputSpeech": {"type": "SSML","ssml":"<speak>D'accord, commençons à apprendre à jouer l'accord Do Majeur.<audio src=\"https://s3.amazonaws.com/.../Chordcmajor.mp3\" /><break time=\"1s\"/>Voici les positions des doigts. Votre index sera sur la corde 2 en appuyant sur la case 1.<break time=\"2s\"/>Votre majeur sera sur la corde 4 en appuyant sur la case 2.<break time=\"2s\"/>Enfin, votre annulaire sera sur la corde 5 en appuyant sur la case 3.<break time=\"2s\"/>Maintenant, allez-y et jouez l'accord Do Majeur.<break time=\"1s\"/><audio src=\"https://s3.amazonaws.com/.../Chordcmajor.mp3\"/>Une fois de plus.<break time=\"1s\"/><audio src=\"https://s3.amazonaws.com/.../Chordcmajor.mp3\"/><break time=\"2s\"/>Si vous êtes prêt à apprendre un autre accord, demandez-le maintenant. Par exemple, dites "Apprends-moi à jouer La Majeur".</speak>"}}
```

### Utiliser des visuels pour compléter l'expérience audio

Une compétence bien écrite partage des visuels en envoyant des cartes à l'application compagnon sur le téléphone ou la tablette de l'utilisateur. Ces visuels renforcent l'audio diffusé et complètent le contenu.

Ci-dessous est un exemple de carte qui montre comment positionner chaque doigt sur la guitare lors du jeu d'un accord. L'audio fournit des détails explicites en utilisant des instructions vocales à l'utilisateur. Le visuel renforce le message en utilisant un autre média. Le diagramme inclus est une notation standard utilisée par les guitaristes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XczNUsPCWSQHtJzPARL9zA.png)

Il y a aussi des cartes montrant l'emplacement sur le manche de différentes notes. Une fois de plus, cela renforce ce qui est décrit à travers l'audio de la compétence.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uG-tfMa6PvjSrDwT0yo6zQ.png)

Ces cartes contiennent un contenu similaire aux graphiques intégrés dans les vidéos YouTube.

Un avantage est que ces cartes affichent des informations pertinentes sans utiliser vos mains. Remettre la compétence pour rejouer une session précédente rejoue également les cartes. Votre voix dirige complètement la narration. Aucun bouton, geste de la main ou clic de souris n'appuie sur le bouton de retour ou actions similaires. Les doigts se concentrent sur le pincement et l'appui des cordes pour créer de la musique.

### Quelle fonctionnalité manque à Alexa ?

Il est encore tôt dans l'adoption des plateformes vocales. Je m'attends à voir plus d'applications comme la mienne qui tirent parti de l'interface vocale. Des lacunes existent où les applications exclusives à un appareil mobile sont supérieures.

Une fonctionnalité pour Alexa est de permettre les données sonores brutes des microphones à l'application. Aujourd'hui, Alexa traduit chaque son directement en texte. Cela limite la capacité de la plateforme à écouter les tons lorsque je joue de l'instrument. Les applications mobiles utiles valident les sons joués et informent l'utilisateur des tons corrects.

### Feedback Bienvenu

Si vous êtes un musicien en herbe comme moi et que vous avez un appareil Alexa, veuillez essayer la compétence. Comme toutes les compétences Alexa, elle est gratuite à activer. Ce serait génial d'avoir des retours sur ce qui est utile et d'autres fonctionnalités à ajouter. J'apprends toujours l'instrument, donc j'accueille également tout conseil sur ce qui manque à la compétence.