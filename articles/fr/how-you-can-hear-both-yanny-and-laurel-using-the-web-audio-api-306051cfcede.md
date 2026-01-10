---
title: Comment entendre à la fois « Yanny » et « Laurel » en utilisant l'API Web Audio
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T16:11:04.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-hear-both-yanny-and-laurel-using-the-web-audio-api-306051cfcede
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mXeOkNmfZwMkcgUcv8_yhw.jpeg
tags:
- name: audio
  slug: audio
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment entendre à la fois « Yanny » et « Laurel » en utilisant l'API Web
  Audio
seo_desc: 'By _haochuan

  Recently an audio clip asking listeners whether they hear the word “Yanny” or “Laurel”
  has been completely puzzling the world and pitting friend against friend in the
  online debate.

  The clip and the “Yanny or Laurel” poll were posted on ...'
---

Par _haochuan

Récemment, un extrait audio demandant aux auditeurs s'ils entendent le mot « Yanny » ou « Laurel » a complètement déconcerté le monde et opposé les amis dans un débat en ligne.

L'extrait et le sondage « Yanny ou Laurel » ont été publiés sur Instagram, Reddit et d'autres sites par des lycéens qui ont déclaré l'avoir enregistré à partir d'un site web de vocabulaire diffusé par les haut-parleurs d'un ordinateur. Maintenant, des centaines de milliers de personnes sont engagées dans un débat sur ce qu'elles entendent. Cela rend les gens fous et conduit à des défenses passionnées des deux côtés.

Cependant, la magie derrière ce débat est assez simple. **Différentes oreilles ont des zones de fréquences sensibles différentes pour le même extrait audio.** De plus, différents haut-parleurs ont des réponses différentes aux différentes fréquences audio.

Ce tutoriel expliquera en détail comment utiliser l'API Web Audio et un simple JavaScript pour créer un outil qui vous aidera à entendre à la fois « Yanny » **et** « Laurel ». Ensuite, vous pourrez gagner n'importe lequel de ces débats. :)

Si vous voulez simplement essayer l'outil, il est disponible [ICI](https://haochuan.github.io/yanny-vs-laurel/static/). Ouvrez simplement votre navigateur, jouez l'audio et essayez de trouver les points idéaux pour « Yanny » et « Laurel » tout en déplaçant le curseur de fréquence.

### Comment cela fonctionne

Parlons d'abord de la partie clé. Pour entendre le mot différent, vous devez somehow augmenter le volume pour une plage de fréquences spécifique qui dépend de vos oreilles. Heureusement, l'API Web Audio a déjà quelque chose de prêt pour nous : `BiquadFilterNode`.

Il existe différents types de `[BiquadFilterNode](https://developer.mozilla.org/en-US/docs/Web/API/BiquadFilterNode)` que vous pouvez utiliser. Pour ce cas, nous utiliserons simplement le filtre `bandpass`.

> _Un filtre passe-bande est un dispositif ou circuit électronique qui permet aux signaux entre deux fréquences spécifiques de passer, mais qui discrimine les signaux à d'autres fréquences. ([source](https://whatis.techtarget.com/definition/bandpass-filter))_

Et pour un filtre passe-bande, la plupart du temps, nous devons simplement définir la valeur de la fréquence centrale que nous voulons amplifier ou couper, au lieu du début et de la fin de la plage de fréquences. Nous utilisons une valeur `Q` pour contrôler la largeur de la plage de fréquences. Plus la valeur `Q` est grande, plus la plage de fréquences sera étroite. [Consultez Wikipedia](https://en.wikipedia.org/wiki/Q_factor) pour plus de détails.

C'est tout ce que nous devons savoir pour l'instant. Maintenant, écrivons le code.

### Initialisation de l'API Web Audio

```
const AudioContext = window.AudioContext || window.webkitAudioContext;
```

```
const audioContext = new AudioContext();
```

#### Créer des nœuds audio avec la configuration et la chaîne de signal

```
// la balise audio en HTML, où se trouve l'extrait audio originalconst audioTag = document.getElementById('audioTag');
```

```
// créer une source audio dans l'API Web Audioconst sourceNode = 
```

```
audioContext.createMediaElementSource(audioTag);
```

```
const filterNode = audioContext.createBiquadFilter();
```

```
filterNode.type = 'bandpass'; // filtre passe-bande
filterNode.frequency.value = 1000 // définir la fréquence centrale
```

```
// définir le gain pour la plage de fréquences
filterNode.gain.value = 100;
```

```
// définir la valeur Q, 5 créera une largeur de bande équitable pour ce cas
filterNode.Q.value = 5;
```

```
// connecter les nœudssourceNode.connect(filterNode);
filterNode.connect(gainNode);
gainNode.connect(audioContext.destination);
```

#### Exemple de fichier HTML

```
<!DOCTYPE html><html lang="en"><head>  <meta charset="UTF-8">  <title>Yanny vs Laurel Web Audio API</title></head><body>  <div id="container">    <audio id='audioTag' crossorigin="anonymous" src="yanny-laurel.wav" controls loop></audio>    <hr>    <input type="range" min="20" max="10000" value="20" step="1" class="slider" id="freqSlider">  </div>  <script src='script.js'></script></body></html>
```

#### Ajout de l'interface utilisateur du curseur de fréquence

Pour faciliter l'ajustement de la fréquence centrale de notre filtre passe-bande, nous devons ajouter un curseur pour contrôler la valeur.

```
<!DOCTYPE html><html lang="en"><head>  <meta charset="UTF-8">  <title>Yanny vs Laurel Web Audio API</title></head><body>  <div id="container">    <audio id='audioTag' src="yanny-laurel.wav" controls loop></audio>    <hr>    <input type="range" min="50" max="4000" value="1000" step="1" class="slider" id="freqSlider">    <br>    <p id="freqLabel" >Fréquence : 1000 Hz</p>  </div>  <script>;    // ajouter un écouteur d'événement pour le curseur afin de changer la valeur de la fréquence    slider.addEventListener('input', e => {
```

```
      filterNode.frequency.value = e.target.value;      label.innerHTML = `Fréquence : ${e.target.value}Hz`;
```

```
    }, false);  <script src='script.js'></script><;/body></html>
```

### Bug createMediaElementSource dans iOS Safari

J'ai constaté que `createMediaElementSource` ne fonctionne pas dans iOS Safari et Chrome. Pour résoudre ce problème, vous devez utiliser `createBufferSource` pour créer un AudioBufferNode afin de stocker et de lire l'audio au lieu de la balise audio HTML. 
Veuillez consulter [le code ici](https://github.com/haochuan/yanny-vs-laurel/blob/master/static/script.js) pour plus de détails.

Maintenant, vous avez créé un outil pour pouvoir entendre à la fois « Yanny » et « Laurel ». Ouvrez simplement votre navigateur, jouez l'audio et essayez de trouver le point idéal tout en déplaçant le curseur de fréquence.

Si vous voulez simplement essayer l'outil, il est disponible [ICI](https://haochuan.github.io/yanny-vs-laurel/static/).

J'écris du code pour l'audio et le web, et je joue de la guitare sur YouTube. Si vous voulez voir plus de choses de ma part ou en savoir plus sur moi, vous pouvez toujours me trouver sur :

Site web : 
[https://haochuan.io/](https://haochuan.io/)

GitHub : 
[https://github.com/haochuan](https://github.com/haochuan)

Medium : 
[https://medium.com/@haochuan](https://medium.com/@haochuan)

YouTube : [https://www.youtube.com/channel/UCNESazgvF_NtDAOJrJMNw0g](https://www.youtube.com/channel/UCNESazgvF_NtDAOJrJMNw0g)