---
title: Serverless n'a pas à être une boîte noire exaspérante
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-26T09:46:17.000Z'
originalURL: https://freecodecamp.org/news/serverless-doesnt-have-to-be-an-infuriating-black-box-b23cca2b2ba2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DNIVlOppPmMFB91A3vhzow.png
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: technology
  slug: technology
seo_title: Serverless n'a pas à être une boîte noire exaspérante
seo_desc: 'By Burke Holland


  “In science, computing, and engineering, a black box is a device, system or object
  which can be viewed in terms of its inputs and outputs (or transfer characteristics),
  without any knowledge of its internal workings. Its implementat...'
---

Par Burke Holland

> « En science, en informatique et en ingénierie, une **boîte noire** est un dispositif, un système ou un objet qui peut être considéré en termes d'entrées et de sorties (ou de [caractéristiques de transfert](https://en.wikipedia.org/wiki/Transfer_function)), **sans aucune connaissance de son fonctionnement interne.** Sa mise en œuvre est « opaque » (noire). Presque tout peut être appelé une boîte noire : un [transistor](https://en.wikipedia.org/wiki/Transistor), un [algorithme](https://en.wikipedia.org/wiki/Algorithm), ou le [cerveau humain](https://en.wikipedia.org/wiki/Human_brain). »

> — Sans vergogne copié de Wikipedia par moi

Il y a quelques semaines, j'ai regardé un documentaire HBO (parce que je suis vieux et c'est ce que font les vieux — nous regardons des documentaires) sur les traumatismes crâniens.

![Image](https://cdn-media-1.freecodecamp.org/images/tNhImYReknpw9o8VWV7cfZnuFWiCu8hb1but)

Dans le film, ils suivent quatre personnes qui se sont réveillées de comas causés par une blessure physique. Tous les patients sont à différents stades de récupération. Ils ont une capacité limitée à bouger, parler, ou même entendre. Tout ce dont vous avez besoin de votre cerveau peut ou peut ne pas fonctionner. C'est pourquoi j'ai été choqué lorsque les médecins ont demandé à l'un de ces patients si quelque chose avait changé depuis avant leur accident, et ils ont dit « **Non.** »

Ils sont incapables de marcher, incapables de tenir leur tête droite — deux choses qu'ils pouvaient faire il y a seulement quelques mois et pourtant leur cerveau était incapable de traiter que quelque chose avait changé.

C'est la définition d'une boîte noire — des données entrent, mais ce qui sort n'est pas ce à quoi nous nous attendons. Et il n'y a rien que nous puissions faire à ce sujet parce que vous ne pouvez pas « déboguer » un cerveau. Si vous le pouviez, je mettrais un point d'arrêt là et je découvrirais pourquoi la ligne « Beer And Chicken Wings » s'exécute TOUS LES SOIRS.

![Image](https://cdn-media-1.freecodecamp.org/images/eddAOXko7Lcef7-MWPvO2bHnH7RYghPEL2FK)
_debugger;_

C'est pourquoi il a fallu six mois pour comprendre pourquoi ce même patient ne pouvait pas entendre. **SIX MOIS**. Tout ce qu'ils peuvent faire, c'est essayer différentes choses jusqu'à ce que quelque chose fonctionne ou ne fonctionne pas et qu'ils puissent réduire les possibilités.

C'est tout un processus d'essais et d'erreurs. Pour les personnes ayant des lésions cérébrales, une grande partie du processus de récupération est exactement cela : essayer différentes entrées encore et encore jusqu'à ce que quelque chose fonctionne. Ce qui, malheureusement, est exactement comment se déroule actuellement une grande partie du développement Serverless.

#### Tristesse Serverless

L'état actuel de Serverless est très similaire au cerveau humain. C'est une technologie cool, mais ses mécanismes internes sont obscurcis pour les développeurs et nous sommes laissés à faire des suppositions éclairées sur ce qui se passe réellement.

C'est une manière incroyablement difficile de construire des applications, et c'est presque assez difficile pour éclipser tous les avantages de coût que Serverless pourrait offrir.

> « Ma fonction Serverless ne me coûte que 1 $ par mois ! Il m'a fallu 6 mois pour la construire, mais REGARDEZ COMBIEN C'EST PEU CHER ! »

J'ai fait ce graphique hautement scientifique et utile pour visualiser le rapport coût/bénéfice de Serverless sur le temps de développement.

![Image](https://cdn-media-1.freecodecamp.org/images/Gv5NsT0tviB6W3QaDYSSTjEhZU0CexMO8I5s)

Une partie de la raison pour laquelle c'est le cas est que le but même de Serverless est d'abstraire l'environnement d'exécution — c'est l'étape suivante dans cette merveilleuse pile d'abstractions. Et lorsque vous abstraitez, vous perdez une certaine quantité de contrôle.

Mais nous aimons les abstractions.

JavaScript est une abstraction qui finit par être exécutée en code machine. Cela signifie que nous perdons le contrôle sur des choses comme la gestion de la mémoire, mais HAHAHAHAHA personne ne s'en soucie parce que, JavaScript.

Dans le cas de Serverless, c'est génial que l'abstraction soit déplacée dans un cloud quelque part, mais nous avons besoin d'accès à cette abstraction au moment du développement. La plupart des fournisseurs Serverless offrent un éditeur en ligne comme interface principale pour le développement. C'est cool et tout, mais vous ne pouvez pas vraiment construire des applications serveur dans un éditeur en ligne parce que vous n'avez aucun accès à, vous savez, LE SERVEUR. Et c'est là que réside la boîte proverbialement (et littéralement).

Alors laissez-moi reformuler cela : Nous aimons les abstractions, jusqu'à ce que nous ne les aimions plus.

#### Quand Nous N'aimons Pas les Abstractions

Commençons par ce à quoi ressemble une expérience Serverless de base.

Si vous deviez créer un nouveau projet Serverless avec quelque chose comme Azure Functions, vous êtes plongé dans l'expérience de l'éditeur en ligne.

![Image](https://cdn-media-1.freecodecamp.org/images/FhIr-06GznTw8ualvzcdqxexJsg-URnJil3w)

C'est assez pratique. Il n'y a rien de tel que de pouvoir commencer à écrire du code directement. Ou si vous êtes comme moi, « copier et coller depuis Stack Overflow. »

![Image](https://cdn-media-1.freecodecamp.org/images/qCXbZRS6pfwd77lkDATsNUajh7HqwjW23Dx9)

Vous pouvez même tester la fonction en ligne. Dans l'ensemble, c'est une bonne première expérience.

Cela a des limitations sérieuses, cependant. Que faire si nous voulions installer un package Node ? Je ne sais pas lequel, mais probablement `left-pad`. Comment faites-vous cela ? Nous ne pouvons pas passer rapidement d'un fichier à l'autre. Nous ne pouvons pas vérifier le code et nous ne pouvons certainement pas ajouter de points d'arrêt.

Maintenant, toute personne qui est sérieuse à propos de Serverless (ou simplement construire quoi que ce soit, d'ailleurs) ne prend pas l'expérience de l'éditeur en ligne trop au sérieux. Pour construire quoi que ce soit de conséquent, nous devons développer localement.

#### Développement Serverless Local

La plupart des fournisseurs Serverless offrent une sorte d'expérience de développement local. Cela est généralement accompli en fournissant à l'utilisateur un émulateur. Ce n'est pas l'environnement d'exécution final, ce qui signifie que vous devez faire certaines suppositions sur des choses que vous ne connaissez tout simplement pas.

Par exemple, vous pouvez développer une fonction serverless localement avec un simple serveur web Node, mais il est très probable que ce n'est pas ainsi que votre code sera appelé en production. Cela signifie que les entrées et peut-être même tout le contexte de la fonction pourraient... SERONT différents lorsque vous déployez.

Azure Functions gère cela un peu différemment. Au lieu de vous donner un émulateur pour le développement local, ils vous donnent l'environnement d'exécution. C'est exact, vous obtenez **toute la boîte**.

### Développement Local Avec Azure Functions

Lorsque vous installez les [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?WT.mc_id=serverless-csstricks-buhollan), vous installez le même environnement d'exécution qu'Azure utilise. Parce que vous obtenez tout l'environnement d'exécution, vous pouvez construire n'importe quel type de fonction localement. Pas seulement des déclencheurs HTTP.

![Image](https://cdn-media-1.freecodecamp.org/images/tcGLRR9bf-3bW9XuKDK1UQjcTOOU6494hc-3)

Notez que vous pouvez également faire des déclencheurs Blob et File d'attente. Si vous déposez un fichier dans le stockage Blob Azure, votre fonction locale est déclenchée. Si vous mettez un message dans la file d'attente de messages Azure, votre fonction locale est déclenchée. C'est génial parce que sinon, comment diantre testeriez-vous les déclencheurs de blog ou de file d'attente ? Vous ne le feriez pas. Vous feriez simplement un Hail Mary dans le cloud et prieriez.

![Image](https://cdn-media-1.freecodecamp.org/images/OxGLltPvZ2C4vYCPBv3Xr0R1xxVLx3-VHi3A)

Les Hail Mary ne fonctionnent que pour [Aaron Rodgers](https://www.youtube.com/watch?v=r0vVqStvh_8). Ce sont deux références au football d'affilée et je suis désolé. Vous méritez mieux.

Avoir l'environnement d'exécution complet facilite également le débogage local si vous utilisez VS Code. Il aide un peu que Microsoft fasse ces deux choses.

#### Débogage des Fonctions Serverless Avec VS Code

Vous pouvez installer l'[extension Azure Functions](https://cda.ms/hx) pour VS Code qui active automatiquement le débogage local des fonctions.

Cela ajoute un nouveau panneau dans VS Code pour Azure Functions. Vous pouvez voir tous vos différents projets de fonctions dans cet espace.

![Image](https://cdn-media-1.freecodecamp.org/images/wN3F3-HxHQ968YKdTWQ1FxmKqQE7Qi8nHy-5)

Plus important encore, il ajoute une configuration de lancement intégrée pour le débogage. Si vous ouvriez un projet Azure Functions dans VS Code, l'extension le reconnaît et vous invite à configurer ce projet pour une utilisation avec l'extension.

![Image](https://cdn-media-1.freecodecamp.org/images/NLV411BjyWu6mSg-6ArGjpt1JUJhQ4vGH7AV)

Cela modifie votre projet de sorte que pour exécuter et déboguer cette fonction, placez un point d'arrêt dans la gouttière et appuyez sur le bouton vert dans le panneau de débogage.

![Image](https://cdn-media-1.freecodecamp.org/images/iWA16qHz6pUHfhzDoLLPuZg9wH2K09DKaRHu)

Dans le cas d'un déclencheur de minuterie, vous obtenez la minuterie qu'Azure Functions utilise, ainsi que les prochaines heures d'exécution planifiées.

![Image](https://cdn-media-1.freecodecamp.org/images/T0yky0ZV4CIjVbUnJrpSKGApKbMw6xuSjQLE)

J'ai déjà mentionné les déclencheurs blob et file d'attente, mais au cas où vous seriez comme moi et « des images ou cela n'est pas arrivé »...

![Image](https://cdn-media-1.freecodecamp.org/images/p56JERNxwFahTGaIrRJeJlrx2Hf-9WlxrOa8)

#### Les Boîtes Noires Sont Pour les Neurochirurgiens

En fait, il n'y a pas de métier appelé « Brain Surgeon ». C'est appelé Neurochirurgien, et en 2015, [le salaire moyen est de 609 639 $ par an](https://www.google.com/search?q=neurosurgeon+average+salary&stick=H4sIAAAAAAAAAOPgE-LQz9U3MM0wNdFSy0620s8uiM8p189ITcwpyYhPTixKTS2ySixLLUpMT40vTsxJLKoEAMCJ6NM0AAAA&sa=X&ved=0ahUKEwiL35So9-bZAhUO7lMKHXZLBIgQ6BMIngIoADAd&biw=1280&bih=1343). Oui. Sérieusement.

Eh bien, je ne suis pas neurochirurgien et je suis sûr que je ne suis pas payé assez pour m'occuper de boîtes noires toute la journée. Serverless a un avenir prometteur, mais seulement lorsqu'il offrira la même productivité que la valeur des coûts. Référez-vous au graphique dans cet article si vous avez des questions sur cette équation.