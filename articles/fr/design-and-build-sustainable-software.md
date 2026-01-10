---
title: Comment concevoir et construire des logiciels durables
subtitle: ''
author: Jayant Chowdhary
co_authors: []
series: null
date: '2024-01-18T01:28:38.000Z'
originalURL: https://freecodecamp.org/news/design-and-build-sustainable-software
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Cover-4.jpg
tags:
- name: MathJax
  slug: mathjax
- name: software architecture
  slug: software-architecture
- name: sustainability
  slug: sustainability
seo_title: Comment concevoir et construire des logiciels durables
seo_desc: 'Electronic devices that run software are all around us. Your mobile phone,
  your car, your microwave, and virtually anything around you – there’s a very good
  chance that they have electronic components running some form of software.

  These devices inev...'
---

Les appareils électroniques qui exécutent des logiciels sont partout autour de nous. Votre téléphone mobile, votre voiture, votre micro-ondes et pratiquement tout ce qui vous entoure – il y a de très grandes chances qu'ils aient des composants électroniques exécutant une forme de logiciel.

Ces appareils utilisent inévitablement de l'énergie et ont des batteries et des circuits, qui se dégradent avec le temps. Avec le temps, ces appareils sont remplacés par des modèles plus récents et améliorés. Mais cela signifie également que de plus en plus de déchets électroniques s'accumulent sur notre planète. 

De plus, puisque nous avons de plus en plus d'appareils électroniques entrant dans notre écosystème chaque jour, nous utilisons également plus d'énergie, ce qui entraîne plus d'émissions de carbone. 

Cela signifie que nous devons concevoir à la fois le matériel et les logiciels de manière à reconnaître que les ressources de la Terre sont limitées. Cet article vous donnera une introduction sur la manière dont vous pouvez architecturer votre logiciel pour la durabilité. 

### Voici ce que nous allons couvrir :

<ul>
    <li><a href="#prerequis">Prérequis</a> </li>
    <li><a href="#pourquoipensonsnousacelamaintenant">Pourquoi pensons-nous à cela maintenant ?</a> </li>
    <li><a href="#quimpliquetildanslarchitectureetlaprogrammationpourladurabilite">Qu'implique l'architecture et la programmation pour la durabilité ?</a></li>
    <li><a href="#profilezvotrelogicielpourlapuissanceetlaconsommationdenergie">Profilez votre logiciel pour la puissance et la consommation d'énergie</a>
    <ul><li><a href="#produitdelenergieretard">Produit de l'énergie retard</a></ul>
    <ul><li><a href="#greenuppowerupetspeedup">Greenup, Powerup et Speedup</a></li></ul>
    <ul><li><a href="#outilsdeprofilage">Outils de profilage</a></ul></li>
    <li><a href="#techniqueslogiciellesetmodesdeconceptionpourladurabilite">Techniques logicielles et modes de conception pour la durabilité</a>
  
   <ul><li><a href="#considerezquelangagedeprogrammationutiliser"> Considérer quel langage de programmation utiliser </a></ul>
   <ul><li><a href="#rendezlelogicielsensiblealapuissanceagissezauxevenementsthermiques">Rendez le logiciel sensible à la puissance : réagissez aux événements thermiques </a></ul>
  
    <ul><li><a href="#lorsquilestapproprioutilisezdesetatsdebassepuissancesurlemateriel"> Lorsque c'est approprié, utilisez des états de basse puissance sur le matériel </a></ul>
    <ul><li><a href="#etudiezlescompromisentrelentreesortiepiloteesparinterruptionetlepolling"> Étudiez les compromis entre les E/S pilotées par interruption et le polling </a></ul>
     <ul><li><a href="#examinezlamiseencache"> Examinez la mise en cache </a></ul>
     <ul><li><a href="#concevezlelogicielendurantetmodifiableamind"> Concevez le logiciel en pensant à la durée de vie et à la modifiabilité</a></ul></li>
     <li><a href="#conclusion">Conclusion</a>
    </li>
</ul>

##Prérequis

J'ai écrit cet article en me concentrant sur des idées générales en informatique. Cette [conférence](http://wla.berkeley.edu/~ee42/sp01/LectNotes/Lect6.PDF) vous aidera avec quelques notions de base sur la puissance et l'énergie dans les circuits électriques. 

D'autres parties de cet article fournissent des références chaque fois que vous pourriez avoir besoin de quelques notions de base.

## Pourquoi pensons-nous à cela maintenant ?

Le [changement climatique causé par l'homme](https://climate.nasa.gov/scientific-consensus/) s'est accéléré de manière constante pendant des décennies. Les émissions de carbone ont augmenté. En tant que partie de la communauté technologique, nous pouvons aider à réduire certains facteurs qui ont contribué à la dégradation de l'environnement terrestre. 

Dans cet article, je vais présenter quelques idées et techniques sur la manière dont vous, en tant que programmeur et architecte logiciel, pouvez faire des choix qui mèneront à une technologie plus durable.

## Qu'implique l'architecture et la programmation pour la durabilité ? 

Dans le contexte de cet article, lorsque je décris l'architecture de logiciels et la programmation pour la durabilité, je fais référence aux objectifs suivants : 

Concevoir des logiciels de manière à ce qu'ils :

1. Consomment la plus petite quantité d'énergie possible, pour accomplir la tâche à accomplir.
2. Résultent en la plus faible dégradation de la batterie possible, tout en maintenant la quantité minimale de performance nécessaire pour la tâche.
3. Nécessitent une quantité minimale de refroidissement pour le matériel sur lequel ils fonctionnent.
4. Résultent en des appareils durables plus longtemps.

Vous verrez que les techniques que nous allons discuter ici ont toutes le même thème derrière elles : faire en sorte que le matériel électronique effectue le minimum de travail possible pour accomplir la tâche à accomplir. 

Commençons par quelques techniques que vous pouvez utiliser pour accomplir cela tout en architecturant et en écrivant des logiciels.

##Profilez votre logiciel pour la puissance et la consommation d'énergie

Un problème qui ne peut pas être mesuré, ne peut pas être résolu. Par conséquent, mesurer la consommation d'énergie et de puissance des logiciels est l'une des tâches les plus importantes que nous devons faire lors de la conception avec la durabilité à l'esprit. 

Faisons un pas en arrière et couvrons quelques bases de la puissance et de l'énergie. 

Comme vous le savez peut-être, la puissance est le taux auquel l'énergie est consommée. C'est-à-dire :

$$P = dE/dt$$

Dans le domaine du temps continu, nous pourrions également dire que :

$$Énergie = \int_{0}^{t} P \,dt$$

En pratique, nous n'obtenons jamais vraiment des mesures de puissance dans le domaine du temps continu. Nous avons généralement des mesures de puissance discrètes sur un intervalle de temps. Ainsi, notre graphique Puissance vs temps pourrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-94.png)
_Figure 1 : Puissance vs temps et calcul de la consommation d'énergie_

Puisque nous avons `n` mesures de puissance discrètes sur le temps, la consommation d'énergie peut être estimée comme l'aire sous la courbe. Cela peut être modélisé comme la somme de `n-1` trapèzes.

 \(Énergie = \sum_{i=1}^{n-1} A^{i}\) où  \(A^{i}\) est l'aire du ième trapèze.

Le profilage de logiciels pour la consommation d'énergie fait référence au processus de mesure de l'énergie consommée par le logiciel en cours d'exécution.

Alors, devriez-vous profiler la puissance ou l'énergie ? La réponse est – cela dépend. Dans certains scénarios qui impliquent une interaction utilisateur intensive (où l'utilisateur contrôle la quantité de temps passée), il est plus judicieux de mesurer la puissance. 

Par exemple : Lorsqu'un utilisateur regarde une vidéo sur un ordinateur portable ou un téléphone mobile, il contrôle de nombreuses choses telles que la durée de la vidéo regardée, la luminosité de l'écran, le volume du haut-parleur, et ainsi de suite. 

Dans d'autres scénarios où l'utilisateur n'a pas autant de contrôle sur le travail effectué par l'appareil électronique, il est judicieux de profiler l'énergie. Un exemple d'un tel cas pourrait être l'énergie nécessaire pour envoyer un message via un service de messagerie SMS/IP (sans compter l'énergie nécessaire pour taper le message).

Examinons quelques métriques courantes pour le profilage de la consommation d'énergie ensuite.

###Produit de l'énergie retard (EDT)

Utilisé dans l'article de recherche [Quelles sont les implications de l'énergie retard de votre langage de programmation ?](https://discovery.ucl.ac.uk/id/eprint/10074516/1/GKLS18_MSR18.pdf), le produit de l'énergie retard est une métrique pondérée qui est définie comme suit :

 $$EDT = E *  T^{w}$$

où E est la consommation d'énergie pour la tâche et T est le temps nécessaire pour accomplir la tâche.

Cette métrique vise à nous donner une mesure de la quantité d'énergie qu'une opération consomme, tout en pénalisant la métrique pour la quantité de temps nécessaire. C'est-à-dire, une opération consommant la même quantité d'énergie mais prenant plus de temps à être effectuée par un système, a un EDT plus élevé et est donc considérée comme moins économe en énergie.

Le poids `w` peut être choisi comme suit :

* 1 : Lorsque l'efficacité énergétique est une préoccupation majeure
* 2 : Lorsque l'énergie et la performance sont toutes deux importantes
* 3 : Lorsque la performance est plus importante que l'efficacité énergétique 

Ainsi, vous pouvez adapter `w` pour vous donner une idée de l'énergie et de la performance de votre système logiciel, en fonction des indicateurs adaptés à votre cas d'utilisation – que l'énergie soit plus importante ou la performance.

### Greenup, Powerup et SpeedUp

Dans la thèse [Utilisation des métriques Greenup, Powerup et Speedup pour évaluer l'efficacité énergétique des logiciels](https://digital.library.txst.edu/items/e8174fcc-4799-4612-88ad-5e3b7e3c3efb), AbdulSalam et al ont introduit de nouvelles métriques pour mesurer l'efficacité énergétique. 

Ils ont vu que l'EDT avait un inconvénient : puisque c'était un produit de deux quantités (Énergie et temps pondéré nécessaire pour accomplir la tâche à accomplir), il était possible que deux systèmes qui avaient le même EDT pour une tâche, différaient en réalité en termes d'efficacité énergétique et de performance - mais leur EDT était toujours le même. 

Par conséquent, il était difficile de conclure quel système était meilleur d'un point de vue énergie + performance, où l'énergie et la performance avaient une importance égale.

Ils ont introduit 3 métriques pour résoudre ce problème.

1. **Speedup**, qui est défini comme :

$$Speedup = T_{base} / T_{opt}$$

où \(T_{base}\) = Temps nécessaire pour accomplir la tâche pour le cas non optimisé, \(T_{opt}\) = Temps nécessaire pour accomplir la tâche pour le cas optimisé. 

Si le cas optimisé est plus performant que le cas non optimisé (puisque rappelez-vous, nous pourrions optimiser uniquement pour l'énergie, uniquement pour la performance, ou les deux), alors Speedup > 1.

2. **Greenup**, qui est défini comme :

 $$Greenup = Energy_{base} / Energy_{opt} = P_{base} * T_{base} / P_{opt} * T_{opt}$$. 

Ici, \(P_{base}\) est la puissance moyenne consommée par la tâche dans le cas non optimisé et de même, \(P_{opt}\) est la puissance moyenne consommée par la tâche dans le cas optimisé.

Si nous regardons différentes valeurs de Speedup et Powerup, elles peuvent tomber dans les catégories suivantes :

1. **Zone 1** : Powerup < 1 et Speedup < 1 et Speedup > Powerup – dans ce scénario, la solution optimisée a sacrifié une partie de la performance, mais il y a eu une plus grande réduction de la puissance. Par conséquent, Greenup > 1, donc il y a des économies d'énergie.
2. **Zone 2** : Powerup < 1, Speedup > 1 – dans ce scénario, la solution optimisée s'est améliorée en performance et en même temps, a réduit la consommation d'énergie. Par conséquent, la consommation d'énergie a diminué et la performance s'est améliorée. C'est le meilleur scénario pour toute optimisation.
3. **Zone 3** : Powerup > 1, Speedup > 1 et Speedup > Powerup – dans ce cas, la consommation moyenne d'énergie s'est améliorée, mais l'augmentation de la vitesse a plus que compensé l'augmentation de la consommation d'énergie. Par conséquent, l'énergie consommée a encore diminué entre les solutions optimisées et non optimisées.
4. **Zone 4** : Powerup > 1, Speedup > 1 et Powerup > Speedup – dans ce cas, la consommation d'énergie a diminué, mais la performance aussi. Pourtant, la consommation d'énergie dans son ensemble a augmenté puisque la perte de performance était plus grande que les économies d'énergie.
5. **Zone 5** : Powerup > 1, Speedup < 1 – dans ce cas, la consommation d'énergie a augmenté puisque la performance s'est dégradée et qu'il y a eu une augmentation de la consommation d'énergie.
6. **Zone 6** : Powerup < 1, Speedup < 1, Powerup > Speedup – dans ce cas, la performance s'est améliorée, mais la puissance a augmenté plus que la quantité de performance améliorée. Par conséquent, la consommation d'énergie a augmenté dans son ensemble.

La figure ci-dessous (inspirée de cette [thèse)](https://digital.library.txst.edu/items/e8174fcc-4799-4612-88ad-5e3b7e3c3efb) montre les zones où la consommation d'énergie augmente et où elle diminue. Les zones rouges (4, 5 et 6) et les zones vertes (1, 2 et 3) représentent ces zones.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-90.png)
_Figure 2 : Les différentes zones pour Speedup et Powerup_

Nous avons passé en revue quelques métriques qui ont toutes leurs forces et leurs faiblesses. La force de l'EDT est que vous pouvez donner plus de poids à la performance. Mais sa faiblesse est que, souvent, il peut ne pas vous dire si une solution est vraiment meilleure que l'autre. 

Bien que connaître la consommation d'énergie soit très important, vous ne devez pas ignorer la consommation de puissance. Une consommation de puissance élevée, parmi d'autres effets, peut avoir des impacts thermiques néfastes sur les appareils électroniques. C'est-à-dire que la température de la peau et des composants de votre appareil peut augmenter. Cela peut entraîner : 

1. **Dommage aux composants** : Les composants électroniques tels que la mémoire, les fils et les condensateurs de votre appareil peuvent être endommagés lorsque la température augmente.
2. **Dommage à la batterie** : Les batteries peuvent être endommagées à des températures plus élevées. Leur [durée de vie](https://www.intercel.eu/frequently-asked-questions/temperature-effects-on-batteries/#:~:text=Battery%20capacity%20is%20reduced%20by,%2C%20AGM%2C%20industrial%20or%20whatever.) peut diminuer et dans certains cas extrêmes, elles peuvent également [exploser](https://www.sciencedirect.com/science/article/pii/S2215098618310000).

Les appareils électroniques commerciaux sont généralement conçus pour fonctionner dans une plage de température de 0 à 70 degrés Celsius. Mais pour les téléphones mobiles, il est généralement recommandé que la température de fonctionnement ne dépasse pas 35 degrés Celsius. 

Avant de profiler l'énergie et la puissance consommées par une tâche spécifique sur vos appareils, il est important d'isoler la tâche autant que possible. 

Par cela, je veux dire qu'il est important que nous éliminions autant que possible d'autres tâches ou variables consommant de la puissance. Cela peut être d'autres services/daemons ou paramètres sur l'appareil qui peuvent affecter la puissance consommée de manière peu fiable. 

**Par exemple**, si l'appareil utilise Internet, des processus en arrière-plan peuvent effectuer certaines activités qui peuvent varier entre plusieurs exécutions de profilage, donc en général, il est bon de désactiver Internet (sauf si la tâche mesurée utilise Internet). Nous voulons faire cela puisque nous voulons des chiffres de profilage de puissance reproductibles d'une exécution à l'autre. 

Donc en général, il est bon de faire une liste de contrôle des conditions qui doivent être constantes pour que le profilage de puissance soit fiable et reproductible. Cela peut varier d'un système à l'autre.

##Outils de profilage

Maintenant, parlons de la manière dont la puissance peut être profilée. Différents systèmes peuvent offrir différentes façons de profiler l'énergie consommée. 

Selon le système d'exploitation et le matériel sous-jacent, il existe quelques options. Je ne vais pas entrer dans les détails de ces outils puisque il y a beaucoup d'options et il y a aussi une bonne documentation disponible sur leurs sites officiels. 

###Linux

1. [PowerStat](https://manpages.ubuntu.com/manpages/xenial/man8/powerstat.8.html) est un outil qui peut mesurer la consommation d'énergie sur le matériel Intel qui supporte l'interface [RAPL](https://sustainable-computing.io/design/kepler-energy-sources/#:~:text=Intel's%20Running%20Average%20Power%20Limit,versions%20of%20Intel's%20processing%20architecture.) (Running average power limit).
2. [Cpu-energy-meter](https://github.com/sosy-lab/cpu-energy-meter/blob/main/README.md) est un outil qui mesure l'énergie consommée par les CPU sur une période de temps donnée.
3. [Powertop](https://www.intel.com/content/www/us/en/developer/articles/tool/powertop-primer.html) est un outil écrit par Intel qui vous donne des informations sur de nombreuses choses d'intérêt telles que la consommation d'énergie, l'utilisation du CPU [C / P States](https://www.intel.com/content/www/us/en/docs/socwatch/user-guide/2020/c-state.html#:~:text=C%2DState%20residencies%20are%20collected,the%20processor%20is%20%22idle%22.), l'utilisation du CPU, et les opérations du système de fichiers par seconde (et ainsi de suite).

###macOS

1. [Intel power gadget](https://www.intel.com/content/www/us/en/developer/articles/tool/power-gadget.html) est un outil écrit par Intel qui donne aux utilisateurs la capacité de surveiller la consommation d'énergie, la fréquence du CPU, l'utilisation du CPU, et même la température sur les machines Mac basées sur Intel. Remarque : Selon le site web d'Intel, Power gadget ne recevra plus de mises à jour et il recommande d'utiliser [Intel Performance Counter](https://www.intel.com/content/www/us/en/developer/articles/tool/performance-counter-monitor.html) à la place.
2. [MxPower Gadget](https://www.seense.com/menubarstats/mxpg/) est un outil similaire à l'Intel power gadget, mais pour les Mac basés sur la puce Apple silicon.
3. [Powermetrics](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/MonitoringEnergyUsage.html) est un [outil en ligne de commande](https://firefox-source-docs.mozilla.org/performance/powermetrics.html) qui est préinstallé sur les machines Apple Silicon et basées sur Intel. Il vous aide à obtenir des mesures de puissance pour les opérations du CPU et du GPU.
4. [L'application Activity Monitor](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/MonitoringEnergyUsage.html) est préinstallée sur les Mac, et vous donne un aperçu de la performance de votre application. Elle vous donne également un aperçu de diverses métriques concernant votre Mac. Bien qu'elle ne vous donne pas de chiffres de puissance, c'est toujours un outil utile.

###Android

La documentation officielle de l'[AOSP](https://source.android.com/) (Android Open Source Project) fournit quelques directives sur la manière de mesurer la puissance des composants du système [ici](https://source.android.com/docs/core/power/component). Ce processus peut varier en fonction du fabricant de l'appareil.

Android Studio, l'IDE de développement officiel d'Android, propose également un [Power Profiler](https://developer.android.com/studio/profile/power-profiler) pour mesurer la puissance. Le On-Device Power Monitor (ODPM) rapporte la puissance consommée par tous les sous-systèmes profilables via leurs rails d'alimentation. Remarque : Ces mesures ne sont pas spécifiques à une application, car elles mesurent la puissance de l'appareil dans son ensemble.

###iOS


Pendant le développement d'applications iOS, les développeurs peuvent mesurer l'impact énergétique de leur application en utilisant le profileur [Instruments](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/MonitorEnergyWithInstruments.html) intégré à XCode.

Nous avons parlé de diverses façons de profiler la puissance et l'énergie dans cette section. Dans les sections à venir, je vais discuter de quelques techniques et considérations à garder à l'esprit pour rendre votre logiciel plus durable.

##Techniques logicielles et modes de conception pour la durabilité

###Considérer quel langage de programmation utiliser


Les langages de programmation ont plusieurs niveaux d'abstraction sur le matériel sur lequel ils fonctionnent. Certains ont un modèle de la machine présenté au programmeur qui est vraiment proche du matériel réel sur lequel ils fonctionnent.

Les langages qui sont directement compilés en code machine sont généralement plus économes en énergie. Ils sont également généralement plus performants, car il y a moins de surcharge par rapport aux langages qui sont interprétés ou exécutés sur une machine virtuelle, comme Java. 

L'article de recherche que j'ai mentionné précédemment ([Quelles sont les implications de l'énergie retard de votre langage de programmation](https://discovery.ucl.ac.uk/id/eprint/10074516/1/GKLS18_MSR18.pdf)) discute de cela en détail et est une excellente lecture. 

Bien que de nombreux systèmes d'exploitation populaires aient la majorité de leurs API dans des langages comme Java, Kotlin et Swift (qui ne sont pas natifs), ils ont généralement des API critiques pour la performance disponibles en code natif également – par exemple, la bibliothèque [NDK](https://developer.android.com/ndk) basée sur l'interface `C` d'Android. Celles-ci peuvent interfacer avec leurs homologues exécutés sur une machine virtuelle et en combinaison être utilisées pour écrire des applications efficaces.

###Rendez le logiciel sensible à la puissance : réagissez aux événements thermiques


Dans la section précédente, j'ai parlé de l'importance de maintenir une faible consommation d'énergie sur les appareils qui exécutent votre logiciel. Ce n'est pas seulement important pour réduire la consommation d'énergie, c'est aussi important pour que la température de fonctionnement de votre appareil n'atteigne pas un niveau qui peut endommager votre appareil. 

La température de fonctionnement de votre appareil ne dépend pas seulement du logiciel qui s'exécute dessus (ce qui inclut votre logiciel). Elle dépend également de la température ambiante. 

Par exemple : si un smartphone est utilisé dans une voiture par une journée chaude, il y a de bonnes chances que lorsqu'une application exigeante est exécutée dessus, elle stresse thermiquement l'appareil. Alors, que pouvez-vous faire en tant qu'architecte logiciel à ce sujet ? 

Vous ne pouvez pas contrôler la température ambiante, mais vous pouvez contrôler la manière dont votre logiciel réagit aux événements thermiques. De nombreux systèmes d'exploitation populaires offrent des API pour « écouter » les événements thermiques. Lorsque les applications reçoivent des notifications indiquant que la charge thermique de l'appareil a dépassé une certaine limite, elles doivent prendre des mesures appropriées. 

**Par exemple**, si un appareil diffuse une vidéo et qu'il reçoit une notification indiquant qu'il chauffe thermiquement, il peut réduire la résolution à laquelle il diffuse la vidéo afin de réduire la consommation d'énergie. 

Si une application de visioconférence reçoit une notification d'événement thermique préoccupante, elle peut vouloir réduire le taux de rafraîchissement auquel elle capture la vidéo / réduire la résolution.

Voici les API d'événements thermiques sur les systèmes d'exploitation populaires

**MacOS et iOS** : le `NSNotificationCenter` offre un [écouteur d'événements thermiques](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/RespondToThermalStateChanges.html) auquel les applications de l'espace utilisateur peuvent s'inscrire.

**Android** : PowerManager offre un [onThermalStatusChangedListener](https://developer.android.com/reference/android/os/PowerManager.OnThermalStatusChangedListener) auquel les applications peuvent s'inscrire, pour recevoir des notifications d'événements thermiques.

###Lorsque c'est approprié, utilisez des états de basse puissance sur le matériel


La plupart des processeurs modernes disposent de dispositions pour réduire la consommation d'énergie. Dans ces modes, le processeur consomme moins d'énergie en changeant la vitesse d'horloge du CPU, en mettant le CPU dans divers états de veille parmi diverses méthodes. Les systèmes d'exploitation donnent à l'utilisateur la capacité de tirer parti de ces états de basse puissance. 

**Par exemple**, Linux dispose de l'outil [`cpupower-frequency-set`](https://linux.die.net/man/1/cpupower-frequency-set) qui permet aux utilisateurs de modifier les paramètres de fréquence du CPU. 

Un autre exemple, les [microcontrôleurs Arduino](https://docs.arduino.cc/learn/electronics/low-power) donnent aux programmeurs la capacité de les mettre dans divers modes de veille lorsqu'il n'y a pas de tâches actives à exécuter. Ces microcontrôleurs sont généralement réveillés par une interruption lorsqu'une tâche à traiter est prête. 

###Étudiez les compromis entre les E/S pilotées par interruption et le polling

Souvent, un logiciel doit attendre qu'un autre composant matériel ou logiciel fournisse des données à traiter. Il y a généralement deux parties impliquées : le producteur des données et le consommateur des données 

Par exemple, une application mobile peut attendre un événement tactile sur l'écran. Ici, le consommateur est l'application mobile et le producteur est le matériel + logiciel de l'écran. 

Un autre exemple pourrait être un programme embarqué natif qui attend que l'état d'un registre CPU change afin d'effectuer une tâche. Ici, le consommateur est le programme embarqué natif et le producteur est le registre CPU (bien que le producteur puisse en fait produire d'autres données, mais pour simplifier, nous ne considérons ici qu'un registre CPU).  

Il existe généralement 2 façons de faire cela :

**Polling** : Le processus de vérification de l'état de la disponibilité des données à des intervalles de temps réguliers prédéterminés est appelé polling. Typiquement, cela ressemble à ceci en code :

```
// pseudo-code
while(poll) {
    bool data_available =  check_data();
    if (data_available) {
        process_data();
    }
    sleep(SLEEP_TIME); // pour éviter de gaspiller des cycles CPU
}
```

Le polling semble assez simple à implémenter. Mais à moins que vous ne soyez absolument sûr que les données ou la condition que vous attendez seront disponibles à une fréquence régulière, il présente certains inconvénients :

1. Le polling ne répond pas aux données disponibles dès qu'elles sont disponibles, car il vérifie la disponibilité après chaque SLEEP_TIME ms.
2. En vérifiant constamment chaque fois que le thread de polling se réveille, il gaspille toujours des cycles CPU et donc de l'énergie.

**E/S pilotées par interruption** : dans cette stratégie, il n'y a pas de vérifications explicites pour les données qui sont attendues pour être prêtes. Au lieu de cela, c'est la responsabilité du producteur d'informer le consommateur chaque fois que les données sont prêtes. Le consommateur ne vérifie pas explicitement auprès du producteur, même périodiquement. Par conséquent, cela économise des cycles CPU et aussi de l'énergie ! 

Il existe plusieurs façons d'implémenter les E/S pilotées par interruption. Il peut y avoir des interruptions matérielles ainsi que des interruptions logicielles. 

Par exemple, lorsqu'un utilisateur touche l'écran d'un téléphone mobile à un endroit particulier, le système d'exploitation pourrait envoyer un rappel à l'un des threads de l'application, l'informant qu'un événement d'entrée tactile est prêt à être traité. Jusqu'à ce que le thread reçoive la notification, il peut soit faire autre chose, soit simplement rester endormi ! 

En bref, les E/S pilotées par interruption sont généralement plus économes en énergie que le polling, et vous devriez les préférer, sauf s'il y a une très bonne raison d'utiliser le polling.

### Examinez la mise en cache

La mise en cache en informatique fait référence au processus de sauvegarde des données dans un emplacement de stockage qui est généralement plus rapide à accéder que le stockage à haute latence (qui sont généralement plus grands en capacité).

La mise en cache est utile lorsque le même ensemble de données doit être lu ou modifié à plusieurs reprises par un logiciel. Elle permet une récupération et une réutilisation efficaces des données. 

Vous pouvez voir la mise en cache en action sous de nombreuses formes telles que :

1. La mémoire vive (RAM) est un cache pour le disque sous-jacent
2. Le cache CPU – L(n) – où n est le niveau du cache. À mesure que n diminue, la taille du cache devient généralement plus petite et la latence de récupération des données devient également plus petite.
3. Les applications peuvent mettre en cache les données récupérées depuis Internet dans leur mémoire sur l'appareil pour un accès rapide.
4. Les serveurs locaux peuvent mettre en cache les données des serveurs distants pour un accès plus rapide également.

Et bien d'autres.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-98.png)
_Figure 3 : Flux de données du disque au CPU via la hiérarchie de cache_

  
En raison de son efficacité accrue avec l'accès aux données, la mise en cache réduit généralement la consommation d'énergie et économise également de l'énergie.

Avant que le logiciel puisse tirer parti de la mise en cache, il doit être architecturé de manière à ce que cela soit possible. En général, les étapes suivantes peuvent vous aider :

1. La toute première chose est de vous assurer que vous êtes à l'affût des opportunités de mise en cache des données.
2. Ensuite, implémentez la mise en cache. La manière dont vous l'implémentez dépendra du type de logiciel que vous construisez. Cela peut aller de l'opération de tuilage des matrices de données à la mise en cache des données récupérées depuis Internet pour une réutilisation ultérieure.
3. Surveillez les performances, l'énergie et l'utilisation de la puissance – et assurez-vous que ces métriques s'améliorent réellement. Il est possible, avec des implémentations sous-optimales, de provoquer un battement de cache – ce qui peut augmenter la consommation d'énergie et réduire les performances.

###Concevez le logiciel en pensant à la durée de vie et à la modifiabilité

Cet article a beaucoup parlé de la consommation d'énergie et de puissance de votre logiciel. Enfin, il y a autre chose qui est très important également : la capacité de votre logiciel à durer longtemps et à être modifiable. 

Il est très bénéfique pour un logiciel de durer longtemps, car cela signifie à son tour que les appareils fonctionneront bien plus longtemps. Le fait que le logiciel soit modifiable signifie que les anciens appareils reçoivent des mises à jour importantes de fonctionnalités et de sécurité, ce qui conduit les utilisateurs à ne pas nécessairement avoir besoin d'acheter de nouveaux appareils simplement pour obtenir un meilleur logiciel. Cela conduit à une réduction des déchets électroniques et de l'énergie dépensée pour le recyclage des composants électroniques. 

La modifiabilité des logiciels est un sujet vaste que je ne couvrirai pas en détail ici. Mais il y a quelques principes que vous devriez considérer et qui vous serviront bien lors de la conception pour la modifiabilité :

**Concevez votre logiciel en modules qui sont modifiables par eux-mêmes** : Cela peut impliquer d'avoir des interfaces strictes entre différents modules afin que, lors de la mise à jour d'un module, le package logiciel dans son ensemble fonctionne toujours correctement.

**Concentrez-vous sur l'utilisation de la mémoire aussi efficacement que possible** : Si tous les logiciels étaient conçus en gardant à l'esprit l'efficacité de la mémoire, les appareils électroniques dureraient plus longtemps, car la quantité de mémoire qu'ils avaient serait suffisante plus longtemps. 

Par exemple, considérons l'iPhone : la première génération en 2007 avait 128 Mo de RAM et 16 Go de stockage flash (maximum). Aujourd'hui, l'iPhone 15 a 6 Go de RAM et a une option de stockage maximum de 1 To (1024 Go). Cela représente une augmentation de près de 16 fois de la RAM et de 64 fois de la mémoire flash. Cela était nécessaire puisque la quantité de mémoire nécessaire par les applications et le système d'exploitation lui-même a augmenté en taille de manière énorme. 

Avec le temps, si la mémoire est utilisée de manière judicieuse, nous pouvons imaginer un avenir où les appareils électroniques durent plusieurs décennies au lieu d'être éliminés tous les 5-6 ans.

**Les tests doivent être infaillibles** : Lorsque le logiciel va être mis à jour fréquemment, il y aura plusieurs versions de logiciels fonctionnant sur des appareils qui interagissent avec d'autres morceaux de logiciels qui pourraient être plus anciens. Ces morceaux de logiciels doivent toujours fonctionner correctement. 

Pour que cela se produise, avant de déployer des mises à jour, le logiciel doit être testé de manière approfondie. Par exemple : lorsqu'un développeur d'applications publie une application, il doit tester avec plusieurs versions de systèmes d'exploitation pour s'assurer que leur application se comporte bien sur toutes.

##Conclusion

Cet article a introduit le concept d'ingénierie logicielle pour la durabilité et a discuté de la raison pour laquelle cela est nécessaire. 

Vous avez également appris diverses métriques ainsi que quelques techniques pour rendre votre logiciel durable et plus efficace. 

Enfin, j'espère qu'il vous a inspiré à réfléchir à un problème très sérieux auquel nous sommes confrontés en ce moment et à la manière dont nous, dans la communauté technologique, pouvons faire notre part.

J'espère que vous avez apprécié l'article !