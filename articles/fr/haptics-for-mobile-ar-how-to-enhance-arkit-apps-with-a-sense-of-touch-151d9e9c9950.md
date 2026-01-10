---
title: 'Haptique pour la RA mobile : comment améliorer les applications ARKit avec
  un sens du « toucher »'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-23T17:51:48.000Z'
originalURL: https://freecodecamp.org/news/haptics-for-mobile-ar-how-to-enhance-arkit-apps-with-a-sense-of-touch-151d9e9c9950
coverImage: https://cdn-media-1.freecodecamp.org/images/1*t8zy_q2Ynm3QowFPo8w6MQ.png
tags:
- name: Augmented Reality
  slug: augmented-reality
- name: Design
  slug: design
- name: 'tech '
  slug: tech
- name: unity
  slug: unity
- name: user experience
  slug: user-experience
seo_title: 'Haptique pour la RA mobile : comment améliorer les applications ARKit
  avec un sens du « toucher »'
seo_desc: 'By Neil Mathew

  I’m really excited about the future of haptics for AR and VR. It feels like the
  missing link between my HTC Vive and jumping into the OASIS with Parzival and Art3mis.
  So it’s not surprising that haptics is perhaps the most hotly antici...'
---

Par Neil Mathew

Je suis vraiment enthousiaste quant à l'avenir de l'haptique pour la RA et la RV. Cela semble être le chaînon manquant entre mon HTC Vive et [le fait de plonger dans l'OASIS avec Parzival et Art3mis](https://en.wikipedia.org/wiki/Ready_Player_One_(film)). Il n'est donc pas surprenant que l'haptique soit peut-être la technologie la plus attendue dans la communauté XR en ce moment. Plusieurs entreprises comme Microsoft et HTC, ainsi que des startups comme [SenseGlove](https://www.senseglove.com/) et [HaptX](https://haptx.com/), ont montré des démonstrations d'itérations de plus en plus prometteuses de gants haptiques que j'ai hâte d'essayer.

Malheureusement, comme la plupart des développeurs RA aujourd'hui, notre travail chez [**Placenote**](https://placenote.com) est presque entièrement axé sur les plateformes RA mobiles comme **ARKit** et **ARCore**. Naturellement, cela nous a amenés à nous demander, **« L'haptique peut-elle faire quelque chose pour la RA mobile ? »**

L'haptique a été un ajout formidable aux écrans tactiles, allant de la simulation de clics tactiles sur les boutons aux notifications silencieuses. Mais, après quelques recherches frénétiques sur Google, nous nous sommes rendu compte qu'il n'y avait en fait aucune discussion réelle sur l'haptique pour les **applications RA mobiles** jusqu'à présent... DÉFI ACCEPTÉ ??

### **Le défi de la RA mobile**

Nous avons décidé d'approfondir pourquoi l'haptique n'a pas encore fait son chemin dans la RA mobile et il n'a pas été difficile de voir pourquoi. La RA mobile est de loin le média RA le moins immersif. Le consensus dans la communauté est qu'il ne s'agit que d'une solution temporaire en attendant la plateforme RA ultime — les lunettes intelligentes.

Mais l'état d'esprit n'est pas le seul obstacle ici. Nous avons constaté que le format mobile présente certains défis uniques pour le concepteur d'expériences RA :

* contrairement aux casques, l'écran du téléphone est à la fois l'affichage et le contrôleur
* il est impossible d'intégrer vos mains dans l'expérience puisque vous tenez le téléphone.
* nous dépendons toujours des interactions tactiles qui sont ambiguës en termes de dimensionnalité — tactile 2D ou 3D ?

Néanmoins, la réalité est que, pour les prochaines années et peut-être plus, la RA mobile est là pour rester. Il y a un milliard d'appareils mobiles dans les poches des consommateurs en ce moment et seulement une poignée de casques RA sur leurs têtes. En tant que développeur, la distribution de vos applications prime sur la plupart des autres facteurs. En fait, dans des applications comme la navigation intérieure et les jeux, le mobile s'est déjà révélé comme un média viable pour déployer des expériences RA.

Cela nous amène au sujet de l'haptique pour la RA mobile. À première vue, il peut sembler qu'il n'y ait aucun réel espoir pour que l'haptique améliore les expériences RA mobiles, mais des études récentes ont en fait montré le contraire.

### **En haptique, moins c'est plus**

Il existe une myriade de méthodes conçues pour obtenir un retour haptique. En général, elles se divisent en deux grandes catégories — **l'haptique kinesthésique** (retour de force) et **l'haptique cutanée** (sensations cutanées).

L'haptique kinesthésique a largement été considérée comme la technologie haptique la plus réaliste. Elle implique des actionneurs physiques, soit ancrés, soit non ancrés. Ceux-ci poussent et tirent nos doigts et autres appendices en réponse aux interactions avec des objets virtuels. Intuitivement, un retour de force réaliste devrait fonctionner bien mieux que de simples vibrations. Mais une étude publiée dans [Science Robotics cette année intitulée « The Uncanny Valley of Haptics »](http://robotics.sciencemag.org/content/3/17/eaar7010) a remis en question ces hypothèses.

Les chercheurs ont découvert que l'augmentation du réalisme de la sensation haptique n'augmente pas nécessairement la qualité de l'expérience RA. Cela a souvent un impact négatif en raison de la vallée dérangeante du réalisme dans les simulations. Ils ont découvert que l'haptique cutanée, qui est essentiellement une combinaison de légers contacts et de vibrations, faisait beaucoup mieux pour tromper le cerveau plus profondément dans l'illusion. Des résultats étranges, mais ils ont essentiellement réalisé que nous avions sous-estimé à quel point notre cerveau est bon pour combler les lacunes dans notre sensation de réalité.

> Les situations où notre cerveau intervient pour combler les lacunes sont ce que je trouve le plus intéressant dans notre perception de la sensation du toucher. — Justin Brad, PDG de Osso VR

### **Apporter l'haptique à la RA mobile**

Étant donné ces résultats, pourquoi ne pas tester ce que l'haptique cutanée peut faire pour la RA mobile ? Après tout, l'haptique sur mobile ne se limite plus aux simples vibrations des sonneries.

Les systèmes micro-électro-mécaniques (MEMS) sur les appareils mobiles sont devenus beaucoup plus sophistiqués et capables de comportements assez nuancés. Depuis l'iPhone 7, Apple a mis à niveau les anciennes vibrations de base pour ce qu'ils appellent maintenant le **Taptic Engine**. Cela est beaucoup plus subtil et se compose de **sept différents types de retour haptique** avec des motifs et des intensités variés.

Les modes de retour haptique disponibles sont :

* Changement de sélection
* Impact léger
* Impact moyen
* Impact lourd
* Notification de succès
* Notification d'avertissement
* Notification d'échec

![Image](https://cdn-media-1.freecodecamp.org/images/EKykqXsyuWpCeEGMquFljyCCzN6ug26uPhCm)
_Le nouveau Taptic Engine d'iOS (iPhone 7 et versions ultérieures) dispose de 7 types différents de retour haptique_

Pour en savoir plus sur le générateur de retour d'iOS, [consultez cette documentation Apple](https://developer.apple.com/documentation/uikit/uifeedbackgenerator). À la fin de cet article, je partagerai quelques codes que vous pouvez utiliser pour ajouter rapidement ces types de retour à vos applications ARKit.

Nous **avons décidé d'expérimenter** avec un certain nombre de ces modes de retour haptique dans nos applications RA et je suis vraiment enthousiaste de dire que les résultats ont été une agréable surprise pour notre équipe. Voici quelques exemples d'implémentations haptiques dans nos applications RA mobiles.

### **Exemples d'utilisation de l'haptique dans la RA mobile**

Dans nos expériences jusqu'à présent, nous avons constaté que le retour haptique pour la RA mobile fonctionne bien dans cinq scénarios distincts. Voici une description de chacun.

#### 1. Pointeurs magnétiques (c'est-à-dire, alignement sur la grille)

Un pointeur verrouillé le long d'une surface plane est une fonctionnalité couramment utilisée dans de nombreuses applications ARKit, en particulier dans les outils de mesure comme [Air Measure](http://armeasure.com/) et [Magic Plan](https://www.magic-plan.com/). Puisque votre téléphone se comporte comme un contrôleur dans la RA mobile, l'UX standard dans les applications de mesure implique de faire glisser un pointeur le long d'une surface pour dessiner des lignes ou des polygones afin de mesurer des choses dans le monde réel. Bien sûr, lorsqu'il s'agit de dessiner des lignes, les pointeurs magnétiques qui s'alignent sur les points de fin et les bords des lignes sont vus partout — de PowerPoint à Photoshop.

Nous avons constaté qu'un retour haptique subtil indiquant un « alignement » de la position du pointeur est une grande amélioration. Cela donne presque l'impression que votre téléphone, c'est-à-dire votre contrôleur, se déplace physiquement pour s'aligner en place.

J'étais vraiment heureux de voir que **la nouvelle application d'Apple « Mesure »** utilise en fait le retour haptique dans leur UX. C'est une implémentation incroyablement subtile et vous pouvez voir un GIF de celle-ci en action ci-dessous. Un « Impact Moyen » est déclenché lorsque le pointeur s'aligne sur le bord du plan.

![Image](https://cdn-media-1.freecodecamp.org/images/5h7tXFoybj35qprzl6G1EJIOrljyh-G6o2T-)
_Application Mesure d'Apple_

#### 2. Test de collision (ressentir les surfaces du monde réel)

Une autre fonctionnalité courante dans les applications ARKit est le test de collision. Cela est implémenté comme un lancer de rayon à partir d'un point sur l'écran — soit un point de contact, soit le centre — vers une surface dans le monde réel. Il est généralement utilisé pour ajouter un objet 3D au point de contact. Une légère sensation haptique peut aider l'utilisateur à comprendre qu'une surface a été « touchée ». Nous avons trouvé deux méthodes qui fonctionnent bien ici :

**Épinglage**  
Dans cet exemple, un marqueur est ajouté à la scène au point de contact. Un « Impact Léger » aide les utilisateurs à ressentir l'« épinglage » du marqueur dans l'espace 3D. Bien sûr, l'inconvénient est que vous ne pouvez pas vraiment ressentir la « profondeur » du point de contact — en d'autres termes, à quelle distance le marqueur est de l'utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/5RQoGLCzDtV5l8bEtaqGmVs7ObuPGxdGGC98)

**Effleurement**  
Une alternative à l'épinglage est la méthode d'effleurement du test de collision. Dans ce cas, un marqueur en constante mise à jour prévisualise où un marqueur pourrait être ajouté à une scène. Nous avons constaté qu'une série d'impulsions haptiques, basées sur l'ampleur du déplacement du marqueur de prévisualisation à chaque image, donne la sensation de gratter un pointeur le long d'une surface 3D et permet de « ressentir » une surface 3D.

![Image](https://cdn-media-1.freecodecamp.org/images/l7GMZUOcwkxV8lsIvnS1xRLPwOOQhNGWl08K)

Voici un exemple de code d'effleurement dans Unity :

```
if (distanceChange >= 0.1 && distanceChange < 0.2) 
{
    iOSHapticFeedback.Instance.Trigger(Impact_Light);
}
else if (distanceChange >= 0.2 && distanceChange < 0.4) 
{
    iOSHapticFeedback.Instance.Trigger(Impact_Medium);
}
else if (distanceChange >= 0.4)
{
    iOSHapticFeedback.Instance.Trigger(Impact_Heavy);
}
```

#### 3. Recul de l'arme FPS ou explosions

C'est de loin l'exemple le plus amusant de retour haptique. Lorsque vous construisez un jeu de tir à la première personne en RA, votre téléphone est à la fois l'affichage et l'arme. Un excellent moyen de simuler un tir d'arme est un simple « Impact Lourd », qui produit une seule secousse, ou une « Notification d'Échec », qui crée une double secousse qui ressemble beaucoup au recul d'une arme. Bien sûr, l'exemple ci-dessous est une arme laser, mais, hé, cela n'est pas censé être trop réaliste, n'est-ce pas ?

![Image](https://cdn-media-1.freecodecamp.org/images/6AOfjrGjmc9pSjmaTVQ-88VW7h92isqHEnfz)

#### 4. Collision avec la pointe du contrôleur

Dans les applications RV comme [Oculus Medium](https://www.oculus.com/medium/) ou [Tilt Brush](https://www.tiltbrush.com/), l'un des contrôleurs portables sert de pointe de pinceau que l'utilisateur déplace pour dessiner dans l'espace 3D. J'ai passé des heures à peindre dans Tilt Brush et j'ai donc naturellement essayé très fort de reproduire cette expérience avec ARKit.

Le problème est que la création d'une expérience de dessin précise sur mobile devient vraiment difficile. Vous perdez le sens de la profondeur lorsque votre téléphone est à la fois l'affichage et le contrôleur. L'une des choses les plus difficiles dans les applications de dessin 3D sur mobile est de savoir où se trouve la pointe de votre pinceau par rapport aux autres objets 3D de la scène.

**Et, encore une fois, l'haptique était la réponse.** Nous avons découvert qu'une façon de donner aux utilisateurs un sens de la profondeur est d'imaginer que le pinceau est en fait une canne que vous pouvez utiliser pour frapper des objets 3D qui sont déjà dans la scène. Fournir un retour haptique pour informer les utilisateurs si la pointe du pinceau est en contact avec des objets existants dans la scène permet aux utilisateurs de positionner précisément leur pinceau dans l'espace 3D.

![Image](https://cdn-media-1.freecodecamp.org/images/BN9Hp8CqQrX7jHi0jXsy36SRCjSQJqbC4rU-)
_Détection des collisions de la pointe du pinceau_

#### 5. Alignement de la re-localisation dans les applications RA persistantes.

Chez [Placenote](https://placenote.com), nous construisons principalement des applications RA persistantes, ou RA Cloud. La fonctionnalité principale de ces applications est la capacité à sauvegarder le contenu RA **de manière permanente** dans un lieu physique. Les utilisateurs peuvent le charger au même endroit à chaque fois.

Ce comportement est appelé la **re-localisation d'une scène.**

![Image](https://cdn-media-1.freecodecamp.org/images/8z3xdAIYFaaEPXbpVxXGAhov8pHtYZOaEPdN)
_Alignement de la localisation en place_

Pour re-localiser une scène RA, un utilisateur doit d'abord pointer la caméra de son téléphone vers le monde réel, puis attendre que la caméra détecte sa position.

Avec Placenote, la re-localisation se produit presque instantanément, mais tout se passe en interne. Par conséquent, nous devons concevoir un moyen de notifier l'utilisateur d'une re-localisation réussie. Les indices visuels peuvent suffire, comme le montre le GIF ci-dessus. Mais une indication plus subtile consiste à fournir un retour haptique « Impact Léger » pour suggérer que vous vous êtes aligné en place dans le monde réel.

### **Comment ajouter l'haptique à votre projet ARKit**

Si vous travaillez avec **Swift** pour le développement natif d'ARKit sur iOS, [consultez ce tutoriel](https://www.appcoda.com/haptic-feedback/) sur la mise en œuvre du retour haptique dans les applications natives.

Si vous travaillez avec **Unity**, mon package préféré jusqu'à présent est le [**iOS Haptic Feedback Package**](https://assetstore.unity.com/packages/tools/integration/ios-haptic-feedback-73225) sur le **Unity Asset Store**. Il coûte 5 $, mais cela en vaut la peine car la fonction intégrée de Unity [Handheld.Vibrate()](https://docs.unity3d.com/ScriptReference/Handheld.Vibrate.html) n'expose pas en réalité les nouvelles fonctions du Taptic Engine d'iOS !

Le package iOS Haptic Feedback fournit un Prefab simple et des scripts pour ajouter les 7 types de retour haptique à votre application. Vous pouvez l'obtenir à partir du lien Asset Store ici :

### **Points à surveiller**

Comme pour tout outil de conception, voici quelques points à surveiller lors de l'incorporation de l'haptique dans votre application RA mobile.

#### **Utiliser trop l'haptique peut perturber le suivi ARKit**

Testez l'impact de l'haptique sur votre session AR. Puisque ARKit repose sur la détection inertielle pour suivre le mouvement du téléphone, l'ajout de trop de vibrations pendant une session ARKit peut perturber légèrement le suivi.

#### **Utiliser trop l'haptique peut surchauffer l'appareil**

L'haptique est, après tout, un mouvement physique de votre appareil mobile et tend naturellement à utiliser plus d'énergie. Utilisez cela avec parcimonie pour éviter que votre téléphone ne surchauffe ou ne manque de batterie trop rapidement.

#### **Trop de retour haptique peut confondre et désensibiliser votre utilisateur**

Cela est vrai pour tout mécanisme haptique. Ne faites pas trop. Plus précisément, ne l'utilisez pas sans une compréhension claire de pourquoi le retour haptique est nécessaire pour l'action que votre utilisateur effectue. Le danger de l'utilisation excessive est que votre utilisateur soit confus et donc désensibilisé à votre retour.

Et c'est tout ! J'espère que cet article vous a donné une dose utile d'idées de conception et vous a convaincu de vous aventurer dans le monde de l'haptique pour la RA mobile. Nous avons vraiment apprécié explorer les différentes façons dont nous pourrions simuler des sensations tactiles dans la RA mobile et si vous avez d'autres idées, nous serions ravis d'en discuter avec vous. Si vous êtes intéressé à essayer l'un de nos exemples de code pour l'haptique RA mobile, envoyez-moi un email à **neil [at] placenote.com**.

Si vous êtes intéressé par les applications RA persistantes ou par ce que nous faisons chez Placenote, envoyez-nous un message sur Twitter, ou consultez [**Placenote.com**](https://placenote.com)

![Image](https://cdn-media-1.freecodecamp.org/images/Gn8g8nxE5b5L2zv-C-1aDXCRS1RuigcRudig)