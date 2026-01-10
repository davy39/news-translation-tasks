---
title: Comment j'ai lancé une application iOS avec un adolescent
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-01T23:58:44.000Z'
originalURL: https://freecodecamp.org/news/how-i-launched-an-ios-app-with-a-teenager-926b5a65a991
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0eG3vNBbMh7an5R3CY6Gmw.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: education
  slug: education
- name: General Programming
  slug: programming
- name: teaching
  slug: teaching
- name: 'tech '
  slug: tech
seo_title: Comment j'ai lancé une application iOS avec un adolescent
seo_desc: 'By Sean Choi

  How to go from Scratch to an iPhone app in the App store

  As a follow up to two of my prior articles, (How to teach programming to teenagers
  and Beginner’s Guide to Raspberry Pi), I want to share my experiences in helping
  a teenager go fr...'
---

Par Sean Choi

#### Comment passer de Scratch à une application iPhone dans l'App Store

En complément de deux de mes articles précédents ([Comment enseigner la programmation aux adolescents](https://medium.freecodecamp.org/how-to-teach-programming-to-teenagers-2ecd43846f0d) et [Guide du débutant pour Raspberry Pi](https://medium.freecodecamp.org/beginners-guide-to-raspberry-pi-6e55080fdaaf)), je souhaite partager mes expériences en aidant un adolescent à passer de la programmation en Scratch à la création et au déploiement d'une application iOS.

Comme mentionné dans [un de mes articles précédents](https://medium.freecodecamp.org/how-to-teach-programming-to-teenagers-2ecd43846f0d), j'ai remarqué que les adolescents ont un fort désir de faire quelque chose qui semble plus réel. Ainsi, la question naturelle qui revenait souvent dans mes cours était : _"Pouvons-nous créer une application iPhone ?"_. J'ai senti que le moment était venu pour les étudiants de créer une application, et je leur ai demandé à chacun de proposer une idée.

Une semaine plus tard, l'un des étudiants est revenu avec une idée qui semblait vraiment intéressante, alors nous avons décidé de prendre du temps en dehors des heures de cours régulières pour la construire ensemble. Et nous avons abouti à une application cool appelée [SwimGrader](https://itunes.apple.com/us/app/swimgrader/id1364739414?mt=8).

![Image](https://cdn-media-1.freecodecamp.org/images/SqaTFid-0S7n7JVHpIEGmz8spT13QTPUByVZ)
_Natation aux Jeux Asiatiques de [Wikipedia Commons](https://commons.wikimedia.org/wiki/File:Incheon_AsianGames_Swimming_19_(15178565298).jpg" rel="noopener" target="_blank" title=")_

#### Comment SwimGrader est-il né ?

Mon étudiant est un nageur passionné et a toujours été curieux de savoir à quel point il était bon en natation. Évaluer sa propre capacité de nage n'est pas vraiment évident, et il faut souvent un expert pour vous dire à quel point vous êtes bon.

Nous savons tous que réduire le temps au tour est l'objectif que la plupart des athlètes visent, donc beaucoup de gens essaient de le faire. Cependant, il est assez difficile de savoir en détail sur quoi vous devez travailler pour atteindre des temps au tour plus bas. Bien sûr, vous pouvez simplement essayer de battre des pieds plus vite et de pratiquer davantage pour gagner plus de muscles de nage, mais ce n'est généralement pas la meilleure façon d'améliorer votre natation.

Partant de ce constat, mon étudiant a pensé que les gens avaient besoin de quelque chose qui pourrait pointer du doigt un domaine de la natation sur lequel ils devraient travailler ensuite. Ainsi, son idée brillante était de créer une application qui pourrait évaluer divers aspects de votre natation et vous dire sur quel domaine vous devriez travailler pour vous améliorer.

Sachant par expérience à quel point il est difficile d'améliorer ma natation, j'ai été **vraiment** impressionné par son idée. C'était quelque chose que je n'avais jamais entendu auparavant et qui avait un cas d'utilisation spécifique pouvant potentiellement bénéficier à beaucoup de gens. Cependant, comme mon étudiant n'avait jamais créé d'application iPhone auparavant, nous avons décidé de travailler ensemble à partir de zéro.

#### Commencer

N'étant pas moi-même un nageur compétitif et pensant que ce serait un bon exercice de réflexion, j'ai demandé à mon étudiant de concevoir l'application et les métriques que nous pourrions utiliser pour évaluer le nageur dans l'application.

Ce processus s'est avéré être une expérience d'apprentissage vraiment enrichissante. Non seulement cet exercice a aidé l'étudiant à peaufiner les détails du projet, mais il a également permis de garder mes attentes et celles de mon étudiant alignées. Comme mentionné dans mes articles sur l'enseignement aux adolescents, les adolescents ont des attentes élevées concernant tout ce qui touche à la programmation. Ainsi, après avoir discuté de chaque détail, des données à collecter, des pages à créer, du fonctionnement des transitions entre les pages et des métriques à afficher, nous avons pu définir clairement nos objectifs et nos attentes.

Et connaître le produit final exact que nous prévoyions de réaliser a aidé l'étudiant à rester constamment engagé.

S'éloignant un peu du sujet principal, nous apprenons souvent des choses dont nous ne savons pas quand nous les appliquerons dans notre vie. Cela peut nous donner l'impression de marcher dans un long tunnel sombre sans lumière au bout.

Cela est particulièrement vrai lorsque vous êtes plus jeune, car il est probable que l'on vous dise d'apprendre certaines choses. Je crois que cela fait que de nombreux étudiants ne s'enthousiasment pas pour ce qu'ils apprennent. J'ai appris que fixer les bonnes attentes en montrant la fin du parcours d'un exercice d'apprentissage aide vraiment à motiver les étudiants et augmente l'efficacité de l'exercice d'apprentissage lui-même.

Donc, revenons à la conception et aux métriques de l'application suggérées par l'étudiant : mon étudiant a d'abord suggéré que l'application, en général, ne devrait pas ajouter de surcharge pour le nageur. Il voulait créer une application capable de collecter des statistiques sans entraver les performances du nageur.

L'étudiant avait déjà en tête un appareil de mesure pour servir exactement à cet usage, que je partagerai dans la section suivante. Après quelques discussions pour aboutir à un produit viable minimal, nous avons décidé de nous concentrer sur la collecte de deux métriques spécifiques : les **mouvements de tête** et la **vitesse de virage**.

Étant donné que les mouvements de tête sont principalement des mouvements superflus qui peuvent réduire l'efficacité de la natation, si nous pouvons simplement compter le nombre de mouvements de tête dans un intervalle de temps donné, nous avons pensé que nous pourrions suggérer une réduction des mouvements de tête superflus.

Nous avons également convenu que des virages rapides sont nécessaires pour réduire les temps au tour. Ainsi, si nous pouvions mesurer le temps qu'il faut au nageur pour effectuer un virage à la fin de la ligne, nous pourrions évaluer le nageur en fonction du temps.

Étant donné cette conception et cette idée, nous avions seulement besoin de commencer à l'implémenter avec le bon capteur.

#### Alors, quel matériel a rendu SwimGrader possible ?

![Image](https://cdn-media-1.freecodecamp.org/images/9aLWiVhSZZeCfqgwKTSqVAaddclmgStXu9tb)
_Kit de recherche de capteurs de mbientlab_

Bien que les derniers [iPhones](https://amzn.to/2RZbPH1) soient étanches, les nageurs ne veulent probablement pas risquer d'emmener leurs [iPhones super chers](https://amzn.to/2RZbPH1) dans la piscine. Ainsi, mon étudiant a suggéré que nous utilisions un [capteur](https://amzn.to/2CpAnUi) de [mbientlab](https://mbientlab.com/product/mountable-sensor-research-kit/) et que nous l'enfermions dans un boîtier étanche.

Ce capteur vous permet de collecter diverses données provenant de l'environnement et de vos mouvements, car il abrite un accéléromètre, un gyroscope, un baromètre, un thermomètre, etc. De plus, ils ont un [code exemple](https://github.com/mbientlab/MetaWear-SDK-iOS-macOS-tvOS) que vous pouvez utiliser pour démarrer votre application afin de collecter immédiatement les données d'intérêt.

Ainsi, notre idée était de placer le capteur à l'intérieur de son bonnet de bain. Il a estimé que cela aurait un impact minimal sur la capacité des nageurs à nager, ce à quoi j'ai souscrit. Nous avons immédiatement acheté deux de ces capteurs et avons commencé à construire notre application. Je ne vais pas passer en revue les détails de la construction d'une application iOS multi-pages simple en utilisant Swift, car ils ont été couverts dans des milliers d'autres articles ([ici](https://hackernoon.com/the-ultimate-list-of-resources-to-mastering-swift-and-ios-development-2018-edition-3bd2a87ff400) se trouve un bon article medium qui en présente beaucoup).

![Image](https://cdn-media-1.freecodecamp.org/images/ktN8sHcvZNgzVcV4mval6VErSN3sHmepTzuS)
_Fenêtre de l'application SwimGrader_

#### Présentation de SwimGrader

Ainsi, après des heures de programmation et de passage par Apple pour obtenir l'approbation de notre application pour l'App Store, nous avons enfin pu lancer [SwimGrader](https://appadvice.com/app/swimgrader/1364739414). Ce fut vraiment surprenant de voir cela, car je n'ai aidé que pour la configuration initiale du projet, qui consistait à mettre en place un projet d'application Swift à page unique et à aider à ajouter des boutons et des champs de texte, ainsi qu'une intégration matérielle simple pour récupérer les données du capteur.

Pour donner une idée de la facilité de l'intégration matérielle, voici un extrait de code pour faire clignoter la LED du capteur en vert. La récupération des données était tout aussi simple, comme on peut le voir dans l'exemple ci-dessous.

```
import MetaWear
import MetaWearCpp
```

```
MetaWearScanner.shared.startScan(allowDuplicates: true) { (dev) in
    // Nous avons trouvé une carte MetaWear, voyons si elle est à proximité
    if dev.rssi.intValue > -50 {
        // Nous avons trouvé une carte MetaWear !
        MetaWearScanner.shared.stopScan()
        // Connectons-nous à la carte que nous avons trouvée
        dev.connectAndSetup().continueWith { t in
            if let error = t.error {
                // Désolé, nous n'avons pas pu nous connecter
                print(error)
            } else {
                // Nous sommes connectés ! Faisons clignoter sa LED !
                var pattern = MblMwLedPattern()
                mbl_mw_led_load_preset_pattern(
                    &pattern, MBL_MW_LED_PRESET_PULSE)
                mbl_mw_led_stop_and_clear(device.board)
                mbl_mw_led_write_pattern(
                    device.board, &pattern, MBL_MW_LED_COLOR_GREEN)
                mbl_mw_led_play(device.board)
            }
        }
    }
}
```

Avec seulement une aide limitée, mon étudiant a dépassé mes attentes en construisant un algorithme de notation et une interface graphique. Il a récupéré les données X, Y, Z du capteur et a donné une note sur la quantité de mouvements de la tête dans chaque direction. Il a recherché en ligne une bibliothèque de graphiques sur iOS et a affiché ce que son capteur rapportait. Et, après avoir terminé son application, il est allé tester son application dans la piscine !

C'est un effort d'un étudiant de collège, donc ce ne sera pas aussi sophistiqué que Clash of Clans. Cependant, je pense que c'est vraiment impressionnant, venant d'un jeune étudiant qui n'a jamais construit d'application iPhone auparavant ! Après avoir terminé cela, l'étudiant m'a demandé,

> Pouvons-nous créer une application Apple Watch pour cela ?

Je lui ai dit qu'il pouvait définitivement créer une version Apple Watch de l'application à l'avenir, mais qu'il pourrait probablement la construire sans mon aide :).

#### Réflexions finales

En tant qu'adultes, je pense qu'il est vraiment difficile de garder nos idées fraîches, sauvages et à jour. Ainsi, je pense qu'il est vraiment éducatif d'écouter ce que ces jeunes étudiants ont à dire et de soutenir ce qu'ils veulent faire de toutes les manières possibles.

Non seulement ces opportunités ouvrent la porte à la construction de nouveaux produits passionnants, mais soutenir les étudiants pour qu'ils proposent et construisent leurs propres idées leur offre les meilleures expériences éducatives. Voir mon étudiant demander aux gens de télécharger son application me fait sourire. J'espère pouvoir peut-être construire une application cool un jour et la présenter à mes amis. Bien que mon étudiant vienne de me devancer :)

Pour conclure, j'ai appris que la construction d'une application iOS cool est plus facile que jamais. Il existe de nombreux articles pour vous aider à construire des applications pour tous les usages possibles : jeux, applications à vue unique, applications de réseaux sociaux et bien plus encore. De plus, il existe plus de matériel que jamais que vous pouvez facilement connecter à votre téléphone et étendre les capacités de votre téléphone.

J'espère pouvoir bientôt partager des expériences de construction de ma propre application. Je m'inquiète simplement de savoir si mes étudiants trouveront mon application cool...

Merci d'avoir lu cet article ! J'espère pouvoir vous convaincre de travailler avec vos étudiants ou vos enfants et de commencer à construire une application simple ! Je suis également ouvert à entendre parler de vos idées d'applications cool.