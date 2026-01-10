---
title: À l'intérieur de Wannacry — la pire épidémie de ransomware de l'histoire —
  et comment vous protéger
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2017-05-15T22:14:57.000Z'
originalURL: https://freecodecamp.org/news/inside-the-worst-ransomware-outbreak-in-history-and-how-to-protect-yourself-168e7028a236
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wCZfBwbHBn5KItwrx_FiZQ.jpeg
tags:
- name: News
  slug: news-tag
- name: politics
  slug: politics
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: À l'intérieur de Wannacry — la pire épidémie de ransomware de l'histoire
  — et comment vous protéger
seo_desc: 'Over the weekend, hundreds of thousands of computers were infected with
  the “WannaCry” ransomware, in what Interpol is calling the largest ransomware outbreak
  in history.

  People who are unlucky enough to get infected will see a threat on their comput...'
---

Au cours du week-end, des centaines de milliers d'ordinateurs ont été infectés par le ransomware « WannaCry », ce qu'Interpol qualifie de plus grande épidémie de ransomware de l'histoire.

Les personnes suffisamment malchanceuses pour être infectées verront une menace sur leur ordinateur qui ressemble à l'image ci-dessus.

Voici comment fonctionne un ransomware :

1. Quelqu'un exécute accidentellement un code malveillant sur son ordinateur (peut-être à partir d'une pièce jointe à un e-mail)
2. Ce code (appelé « ransomware ») chiffrera de nombreux fichiers sur leur disque dur (ou fera autre chose de malveillant).
3. Le code exige alors une rançon. Il notifie à la personne que si elle ne fait pas quelque chose (dans le cas de WannaCry, envoyer aux attaquants 300 $ en Bitcoin), le logiciel ne déchiffrera pas ces fichiers.

Dans le cas de WannaCry, après 3 jours, la demande passe à 600 $. Ensuite, après une semaine, il affirme que les données seront perdues à jamais. Cela dit, 7 jours ne se sont pas encore écoulés, nous ne savons donc pas encore si les attaquants mettront cette menace à exécution.

Pour autant que nous le sachions, seuls les ordinateurs exécutant Windows sont vulnérables à WannaCry. Mais c'est un ransomware particulièrement vicieux, car une seule personne sur un réseau doit le télécharger. À partir de là, il peut se propager automatiquement à travers les réseaux locaux, en utilisant des ports normalement réservés au partage de fichiers en réseau.

WannaCry est capable de faire cela grâce à une faille appelée EternalBlue qui aurait été développée par la propre Agence de sécurité nationale (NSA) de l'Amérique, puis divulguée le mois dernier par le groupe de pirates The Shadow Brokers ([lecture de 2 minutes](https://fcc.im/2r9XEUR)).

En raison de sa nature particulièrement virulente, WannaCry a fermé plusieurs organisations au cours du week-end, y compris une grande partie du Service national de santé britannique — empêchant les médecins d'utiliser les machines IRM, et même éteignant les réfrigérateurs de stockage qui gardaient le sang donné au frais.

Ce matin, je suis passé à Good Morning America d'ABC. Ils m'ont interviewé sur les ransomwares et m'ont demandé ce que les gens ordinaires peuvent faire pour se protéger.

Voici mes conseils de base :

1. Si vous êtes préoccupé par vos fichiers, sauvegardez-les. Windows et MacOS disposent tous deux d'outils de sauvegarde intégrés.
2. Gardez votre logiciel à jour. Ne désactivez pas la mise à jour automatique. Les développeurs corrigent constamment les vulnérabilités de sécurité. Même si cela semble fastidieux, installez leurs mises à jour recommandées.
3. N'ouvrez pas les pièces jointes suspectes des e-mails.
4. Ne comptez pas uniquement sur des outils comme les antivirus pour vous protéger contre ces types d'attaques. Vous devez personnellement être vigilant. La sécurité n'est pas un produit — c'est un processus.

Si votre ordinateur est infecté par un ransomware et que vous n'avez pas de sauvegardes de vos fichiers, vous pourriez vouloir payer la rançon. Bien que cela récompense les criminels, c'est un petit prix à payer pour sauver des fichiers irremplaçables, comme des photos de famille.

Rappelez-vous que sans la clé cryptographique, même les gouvernements les plus puissants du monde n'ont aucun moyen de vous aider à déverrouiller vos fichiers.

Microsoft a découvert la vulnérabilité exploitée par WannaCry en mars, et ils ont publié des correctifs pour tous les systèmes d'exploitation récents. Dans le cas de WannaCry, si vous avez une version de Windows des cinq dernières années et que la mise à jour automatique est activée, votre ordinateur ne devrait pas être à risque.

Mais si vous utilisez toujours des versions plus anciennes de Windows, comme le Windows XP vieux de 16 ans, vous devriez absolument télécharger le correctif. Voici les instructions pour cela : ([lecture de 2 minutes](https://fcc.im/2rjW7IX))

WannaCry a frappé la Russie le plus durement. La société de conseil en cybersécurité [Comae](https://fcc.im/2pPXNYR) estime que près de la moitié des infections se sont produites là-bas.

![Image](https://cdn-media-1.freecodecamp.org/images/QirJUiEgI6tnG7kfpFmdTTMih4G-Oi1ohfBG)

Hier, de nouvelles variantes de WannaCry ont commencé à apparaître : ([lecture de 4 minutes](https://blog.comae.io/wannacry-new-variants-detected-b8908fefea7e)).

La NSA, la CIA et d'autres agences gouvernementales consacrent actuellement environ 90 % de leurs ressources en cybersécurité aux cyberattaques offensives : ([lecture de 4 minutes](https://fcc.im/2rjJSfN)).

De nombreux développeurs sont indignés que les agences gouvernementales aient accumulé ces vulnérabilités, au lieu d'alerter les éditeurs de logiciels à leur sujet, afin qu'ils puissent rapidement corriger ces bugs.

Comme le dit le proverbe, parfois la meilleure offense est une bonne défense. Et c'est précisément la stratégie que de nombreux développeurs espèrent voir les gouvernements adopter.

Dans tous les cas, la situation des ransomwares va empirer avant de s'améliorer. Alors, restez en sécurité !

### Voici trois autres liens qui valent votre temps (également sur les ransomwares) :

1. Lisez l'histoire de la façon dont un développeur a découvert une porte dérobée dans le code de WannaCry et a pu arrêter temporairement sa propagation : ([lecture de 7 minutes](https://fcc.im/2qKleYn))
2. Le chercheur en sécurité Troy Hunt a écrit une analyse approfondie de l'épidémie de WannaCry : ([lecture de 12 minutes](https://fcc.im/2qkTsRh))
3. Regardez comment ces portefeuilles bitcoin reçoivent des paiements de ransomware de la cyberattaque mondiale en cours, via un bot Twitter ([lecture de 2 minutes](https://fcc.im/2qpd8Bv))

**Je n'écris que sur la programmation et la technologie. Si vous [me suivez sur Twitter](https://twitter.com/ossia), je ne perdrai pas votre temps. ?**