---
title: Frameworks Computer Vision.js que vous devez connaître
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-18T16:05:59.000Z'
originalURL: https://freecodecamp.org/news/computer-vision-js-frameworks-you-need-to-know-b233996103ce
coverImage: https://cdn-media-1.freecodecamp.org/images/0*uXRPu25xSI_86KUw
tags:
- name: Computer Vision
  slug: computer-vision
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: Machine Learning
  slug: machine-learning
- name: technology
  slug: technology
seo_title: Frameworks Computer Vision.js que vous devez connaître
seo_desc: 'By Shen Huang

  Computer vision has been a hot topic in recent years, enabling countless great applications.
  With the effort from some dedicated developers in the world, creating an application
  utilizing computer vision is no longer rocket science. In ...'
---

Par Shen Huang

La vision par ordinateur a été un sujet brulant ces dernières années, permettant d'innombrables applications formidables. Grâce aux efforts de certains développeurs dévoués dans le monde, créer une application utilisant la vision par ordinateur n'est plus une science complexe. En fait, vous pouvez construire de nombreuses applications en quelques lignes de code JavaScript. Dans cet article, je vais vous présenter certains de ces frameworks.

### 1. TensorFlow.js

Étant l'un des plus grands frameworks de machine learning, TensorFlow permet également la création d'applications Node.js et front-end JavaScript avec [**Tensorflow.js**](https://www.tensorflow.org/js). Ci-dessous se trouve l'une de leurs démonstrations qui fait correspondre des poses avec une collection d'images. TensorFlow dispose également d'un [**playground**](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.27185&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false) qui nous permet de mieux visualiser les réseaux de neurones artificiels, ce qui peut être excellent à des fins éducatives.

![Image](https://cdn-media-1.freecodecamp.org/images/fzXRDjBio2OIxVNIHI2Njxb9sg6x9rVQRAph)
_Une démonstration de Move Mirror de [Tensorflow.js](https://experiments.withgoogle.com/move-mirror" rel="noopener" target="_blank" title=")_

### 2. Amazon Rekognition

[**Amazon Rekognition**](https://aws.amazon.com/rekognition/?sc_channel=PS&sc_campaign=acquisition_US&sc_publisher=google&sc_medium=ACQ-P%7CPS-GO%7CBrand%7CDesktop%7CSU%7CMachine%20Learning%7CRekognition%7CUS%7CEN%7CText&sc_content=aws_recognition_software_e&sc_detail=amazon%20rekognition&sc_category=Machine%20Learning&sc_segment=293645376368&sc_matchtype=e&sc_country=US&s_kwcid=AL!4422!3!293645376368!e!!g!!amazon%20rekognition&ef_id=EAIaIQobChMIwLzV1obx4AIVEK6WCh3MZAPREAAYASAAEgJlv_D_BwE:G:s) est un outil puissant basé sur le cloud. Mais ils fournissent également des SDK pour JavaScript dans les navigateurs que vous pouvez trouver [**ici**](https://aws.amazon.com/sdk-for-browser/). Ci-dessous se trouve une image illustrant à quel point leur détection de visage peut être détaillée.

![Image](https://cdn-media-1.freecodecamp.org/images/0pIcn86SNFaM5cbA5CXboENRyfMtX0ayQ3rb)
_Détection des caractéristiques faciales avec [Amazon Rekognition API](https://docs.aws.amazon.com/rekognition/latest/dg/faces-detect-images.html" rel="noopener" target="_blank" title=")_

### 3. OpenCV.js

Étant l'un des plus anciens frameworks de vision par ordinateur, [**OpenCV**](https://opencv.org/) a servi les développeurs en vision par ordinateur depuis très longtemps. Ils disposent également d'une [**version JavaScript**](https://docs.opencv.org/3.4/d5/d10/tutorial_js_root.html) permettant aux développeurs d'implémenter ces fonctionnalités sur un site web.

![Image](https://cdn-media-1.freecodecamp.org/images/axCPVu-3ItA12kmt4OLraf0WgqxzZ-BmmUfr)
_Exemple de détection de visage avec OpenCV, Image de [DZone](https://dzone.com/articles/face-detection-using-html5" rel="noopener" target="_blank" title=")_

### 4. tracking.js

Si vous cherchez uniquement à créer une application de détection de visage rapide, comme une version web des filtres snapchat, vous devriez jeter un coup d'œil à [**tracking.js**](https://trackingjs.com/). Ce framework permet l'intégration de la reconnaissance faciale avec JavaScript avec une configuration assez simple. J'ai également écrit un [**guide**](https://medium.freecodecamp.org/how-to-drop-leprechaun-hats-into-your-website-with-computer-vision-b0d115a0f1ad) sur ce framework pour ajouter un chapeau de leprechaun sur les visages pour la Saint-Patrick.

![Image](https://cdn-media-1.freecodecamp.org/images/ntEODKKA39CkXs9Q8Fcb8uMBEaVC0OZZZpot)
_Exemple de détection de visage avec [tracking.js](https://trackingjs.com/examples/face_hello_world.html" rel="noopener" target="_blank" title=")_

### 5. WebGazer.js

Que vous cherchiez à effectuer des études d'expérience utilisateur ou à créer de nouveaux systèmes interactifs pour vos jeux ou sites web, [**WebGazer.js**](https://webgazer.cs.brown.edu/) peut être un excellent point de départ. Ce framework puissant permet à nos applications de savoir où la personne regarde avec les entrées de la caméra.

![Image](https://cdn-media-1.freecodecamp.org/images/ofDdoti6XYIdLDUNfnDA4X54j8AHvNXeOpJY)
_Exemple de suivi du regard avec [WebGazer.js](https://webgazer.cs.brown.edu/#examples" rel="noopener" target="_blank" title=")_

### 6. three.ar.js

Un autre framework de Google, [**three.ar.js**](https://github.com/google-ar/three.ar.js?files=1) étend les fonctionnalités de [**ARCore**](https://developers.google.com/ar/) au JavaScript front-end. Il nous permet d'intégrer la détection de surface et d'objets dans les navigateurs, ce qui est l'outil parfait pour un jeu en réalité augmentée.

![Image](https://cdn-media-1.freecodecamp.org/images/2jPTttH19OZg9eeSQ7YXiFsQ-Xq8E2bqmk96)
_Démonstration de [three.ar.js](https://github.com/google-ar/three.ar.js?files=1" rel="noopener" target="_blank" title=")_

### En conclusion

Je suis passionné par l'apprentissage de nouvelles technologies et le partage avec la communauté. Si vous souhaitez lire quelque chose en particulier, n'hésitez pas à me le faire savoir. Voici mes articles précédents liés à ce sujet. Restez à l'écoute et amusez-vous en ingénierie !

* [**Comment la vision par ordinateur révolutionne le eCommerce**](https://medium.com/swlh/how-computer-vision-is-revolutionizing-ecommerce-d05e0ca11765)
* [**Comment ajouter des CHAPEAUX DE LEPRECHAUN à votre site web avec la VISION PAR ORDINATEUR**](https://medium.freecodecamp.org/how-to-drop-leprechaun-hats-into-your-website-with-computer-vision-b0d115a0f1ad)