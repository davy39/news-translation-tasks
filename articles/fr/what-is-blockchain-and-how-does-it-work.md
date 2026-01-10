---
title: Qu'est-ce que la Blockchain et comment fonctionne-t-elle ?
subtitle: ''
author: Zubin Pratap
co_authors: []
series: null
date: '2020-02-10T23:48:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-blockchain-and-how-does-it-work
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ca4740569d1a4ca335e.jpg
tags:
- name: Blockchain
  slug: blockchain
- name: Developer
  slug: developer
seo_title: Qu'est-ce que la Blockchain et comment fonctionne-t-elle ?
seo_desc: 'If you''re interested in technology, there''s a good chance you’ve probably
  heard the terms Bitcoin, Crypto, Ethereum, or even "distributed, decentralized ledgers."

  You’ve probably heard people talk about cryptocurrency and encryption algorithms,
  about...'
---

Si vous vous intéressez à la technologie, il y a de fortes chances que vous ayez probablement entendu les termes Bitcoin, Crypto, Ethereum, ou même « registres distribués et décentralisés ».

Vous avez probablement entendu des gens parler de cryptomonnaie et d'algorithmes de chiffrement, de la fin des « intermédiaires » et ainsi de suite.

Il est facile de supposer que les cryptomonnaies (par exemple : Bitcoin, Ripple, Ethereum, Litecoin, etc.) sont identiques à la blockchain. Ce n'est pas le cas.

Les [cryptomonnaies](https://en.wikipedia.org/wiki/Cryptocurrency) sont une application ingénieuse d'une technologie bien plus ingénieuse – [la Blockchain](http://en.wikipedia.org/wiki/Blockchain_(database)).

Dans cet article, je vais aborder certains des concepts de base de la blockchain afin que vous compreniez ce qu'elle est, comment elle doit être conceptualisée et ce qui peut être construit par-dessus.

Mais comme pour toutes choses, elles ont plus de sens si vous comprenez *pourquoi* elles ont été inventées, avant de vous pencher sur ce qu'elles font. Ce contexte vous aidera à saisir quel problème la blockchain était censée résoudre.

## Pourquoi utiliser la blockchain ?

Excellente question. Je suis ravi que vous l'ayez posée. Asseyez-vous et faisons une petite expérience de pensée.

Que se passe-t-il si vous et votre meilleur ami menez *indépendamment* et séparément la même campagne de pétition ? Disons que c'est pour la cause « Libérez les Hamsters ».

Disons que vous la menez dans une séquence identique à travers le même quartier, mais que vous obtenez des ensembles de signatures différents sur la pétition. Quelle version de la pétition signée est la « source de vérité » ?

Vous devriez retracer vos parcours séparés, une signature à la fois, pour localiser la *dernière* divergence. Ensuite, vous devriez travailler plus en amont pour identifier le premier résultat qui a divergé entre vos feuilles de signatures. Avant cette divergence racine, toutes les autres signatures sur les deux listes devraient correspondre.

Vous savez alors qu'avant cette divergence, les deux listes sont en accord, donc ces signatures représentent le nombre minimum de personnes qui ont signé pour soutenir la libération des hamsters.

Bien que cela puisse bien fonctionner pour les hamsters et les petites enquêtes de quartier, cela ne fonctionne pas aussi bien dans le monde numérique. Ou pour le vote, la banque, les transactions financières, le transfert de titres de propriété, la décharge d'obligations contractuelles, etc. Vous avez besoin d'intermédiaires indépendants et « de confiance » pour vérifier une chaîne d'événements et vous rassurer solennellement que la « chaîne de garde » n'a pas été rompue.

Une « chaîne de garde » peut parfois aussi être appelée « provenance » – les deux termes signifient la même chose : la séquence des événements historiques concernant les données en question.

C'est pourquoi les gouvernements ont le dernier mot sur votre identité, et les votes doivent être comptés et recomptés physiquement par des centaines de bénévoles, et des greffiers dans des bureaux sombres maintiennent des registres et des certificats pour confirmer si vous possédez ou non votre ferme/bungalow à la clôture blanche.

C'est pourquoi vous avez besoin d'intermédiaires financiers pour vous assurer que lorsque vous achetez votre figurine de collection Darth Vader avec une carte de crédit, l'argent (la valeur) est « retiré » de votre compte et « mis » sur le compte du vendeur.

Cela s'appelle techniquement le problème de la « [double dépense](https://en.wikipedia.org/wiki/Double-spending) » – comment vous assurez-vous que vous ne dépensez pas le même argent deux fois ? Sans quelqu'un pour faire cela, vous pourriez dépenser de l'argent et en même temps continuer à le garder.

Donc, c'est un gros problème – la vie moderne exige que nous nous fiions à, fassions confiance et payions des intermédiaires « de confiance » pour nous assurer que la valeur (l'argent) change bien numériquement de mains. C'est pourquoi Visa et MasterCard existent, et pourquoi PayPal et autres se lient à vos comptes bancaires.

> Au cœur du « pourquoi » de la blockchain se trouve ce problème : comment savez-vous qu'une séquence d'événements n'a pas été falsifiée pour altérer l'état actuel ?

C'est là que la blockchain intervient. C'est clair pour l'instant ?

## Comment fonctionne la Blockchain

Pour simplifier la communication d'un concept, je peux prendre des libertés avec certains des aspects techniques sous le capot de cette technologie. Mon objectif est de vous faire comprendre ce qu'elle est et d'avoir un modèle mental de son fonctionnement. Pour cela, je peux avoir besoin d'être un peu imprécis pour améliorer les chances de compréhension, surtout pour les non-anglophones.

Il est essentiel de se rappeler que la blockchain est une technologie – un code logiciel mathématiquement complexe pour être précis. Et Bitcoin (ou Ethereum ou toute autre crypto disponible) sont simplement des applications de cette technologie.

Les principes clés sont donc :

* Les blockchains sont « minées » (produites par l'effort, comme dans l'extraction de l'or) par des ordinateurs puissants et gourmands en ressources – appelés nœuds, qui sont sur le même réseau.

* Les chaînes de registres de transactions chiffrées numériquement et horodatées sont regroupées en « blocs », qui sont maintenus sur un « registre » par chaque nœud. À mesure que les transactions sont ajoutées à un bloc, et que les blocs sont liés ensemble linéairement et chronologiquement en tant que « chaînes ». Ensuite, l'ensemble du registre est synchronisé à travers le réseau de nœuds de sorte que toutes les « chaînes » de blocs sur les nœuds racontent une histoire identique de l'historique de toute transaction donnée. Ainsi, nous obtenons « bloc + chaîne = blockchain ». C'est une longue liste liée et compliquée.

* Chaque bloc d'une chaîne a son propre identifiant - un hachage cryptographique unique et spécifique à chaque bloc. Ce hachage est également stocké dans le bloc *suivant* de la chaîne, créant un lien. Un bloc peut stocker des milliers de transactions et le plus petit changement dans les données de ce bloc entraînerait un nouveau hachage. Donc, si un hachage change mais que le bloc suivant a un hachage différent, alors nous savons que certaines données du bloc précédent ont été falsifiées.

* À mesure que des centaines deviennent des milliers de nœuds (et que d'autres sont ajoutés tout le temps), chaque nœud doit « s'accorder » sur l'historique des blocs/registres – cela s'appelle le « consensus critique ». L'une des façons d'atteindre le consensus est par le hachage cryptographique dont nous avons parlé plus tôt.

* En cas de divergences dans le registre (par exemple, le hachage d'un bloc ne correspond pas à la référence du bloc suivant au hachage du bloc précédent), le registre avec la plus longue chaîne de transactions valides intégrées sera le « correct » – la source de vérité. Tout nœud travaillant sur d'autres (versions plus courtes) de la chaîne bascule vers la plus longue. Cela maintient le consensus critique (cette partie est énormément simplifiée, mais suffisante pour l'instant).

* Toute interception ou modification malveillante d'un registre (par exemple, lorsque le hachage d'un bloc ne correspond pas) créerait immédiatement une divergence avec toutes les autres versions. Il aurait également un historique de blocs plus court pour le corroborer, ce qui rend cette version falsifiée suspecte dans le réseau blockchain où la longueur compte (hém).

* Répliquer cette divergence à travers *toutes* les versions du registre – l'ensemble du réseau blockchain – est une tâche si énorme qu'elle est computationnellement impraticable, et ne se produirait que si les méchants avaient soudainement le contrôle de la *majorité* des nœuds minant la blockchain et les changeaient tous assez rapidement. Ce type d'attaque coordonnée sur la majorité des nœuds du réseau est souvent appelé l'[attaque à 51 %](https://en.bitcoin.it/wiki/Majority_attack).

Intéressamment, Satoshi Nakamoto dit dans le [livre blanc original de Bitcoin](http://bitcoin.org/bitcoin.pdf),

> « *Ainsi, la vérification est fiable tant que les nœuds honnêtes contrôlent le réseau, mais est plus vulnérable si le réseau est submergé par un attaquant.* »

Cependant, ailleurs [lui/elle/l'organisation](http://en.wikipedia.org/wiki/Satoshi_Nakamoto) (nous ne savons pas qui est « Satoshi ») souligne calmement que pour modifier les transactions passées dans les blocs, à travers l'ensemble du réseau de nœuds, l'attaquant devrait refaire la chaîne de garde dans ces blocs, et tous les blocs ajoutés après cela. Ensuite, ils devraient courir comme des fous pour rattraper et surpasser le travail des nœuds qui ne sont pas sous le contrôle du méchant (afin qu'ils puissent réécrire le registre, pour ainsi dire).

Et à cause de cela, la « *probabilité qu'un attaquant plus lent rattrape diminue de manière exponentielle à mesure que des blocs ultérieurs sont ajoutés* ».

La complexité programmatique pure, le rythme et le volume des activités nodales rendent difficile pour les contrefacteurs/attaquants de rattraper, et encore moins de distancer, les nouveaux blocs minés constamment.

Cela a du sens. C'est comme le mensonge que vous dites à un membre de votre famille sur la raison pour laquelle vous n'avez pas pu assister au récital de flûte de leur enfant. Ensuite, vous devez courir comme un fou après tout le monde dans la famille et vous assurer que vous leur avez tous dit le même mensonge afin que lorsque la personne originale à qui vous avez menti en parle, tout le monde soit au courant de ce mensonge et joue le jeu. Cela semble épuisant.

Pour conclure, la caractéristique déterminante d'une blockchain est qu'elle est un registre distribué à travers de nombreux, nombreux nœuds et qu'il est extrêmement intensif en calcul (coûteux) d'ajouter des nœuds à ce réseau.

Ainsi, chaque registre doit être « conscient » de toutes les transactions et doit avoir une version convenue (qui aura la plus longue « chaîne de garde » derrière elle) à travers l'ensemble du réseau auquel la prochaine transaction sera ajoutée.

> *Comme* [*Satoshi Nakamoto le déclare*](http://bitcoin.org/bitcoin.pdf) *dans le livre blanc original de Bitcoin, « La seule façon de confirmer l'absence d'une transaction est d'être conscient de toutes les transactions. »*

Importamment, la blockchain « [désintermédie](https://en.wikipedia.org/wiki/Disintermediation) » la confiance – donc nous n'avons pas besoin de payer des frais de transaction aux « tiers de confiance » pour être dignes de confiance et nous maintenir, ainsi que les contreparties avec lesquelles nous traitons, honnêtes. La blockchain garantit programmatiquement la vérité (provenance) de l'historique des transactions qu'elle contient.

### Alors, pourquoi devrions-nous nous en soucier ?

Eh bien, en éliminant le besoin de « tiers de confiance », tout intermédiaire qui facture des frais modestes pour nous offrir le cadeau de la certitude doit trouver un nouvel emploi. Et cela impacte les banques qui offrent traditionnellement de tels services d'assurance.

Cela signifie également que nous pouvons programmer des « [contrats intelligents](https://en.wikipedia.org/wiki/Smart_contract) » entre le promettant et le bénéficiaire de la promesse qui reconnaissent automatiquement (numériquement) si cette promesse a été tenue ou non.

Cela a permis à une artiste vraiment techno comme [Imogen Heap de vendre sa musique directement](http://fortune.com/2016/09/22/blockchain-music-disruption/) à son public, et de collecter ses revenus directement auprès d'eux plutôt que de perdre la majeure partie de ses gains aux maisons de disques, managers et autres « tiers de confiance ».

Cela changera probablement la manière dont la propriété intellectuelle est protégée, accessible, partagée, distribuée et développée sur Internet.

Cela pourrait même signifier que la flotte de conducteurs d'Uber transige directement avec les personnes qui veulent un trajet plutôt que de dépendre d'Uber pour coordonner et contrôler le flux d'informations et d'argent.

Cela pourrait signifier que je pourrais vous envoyer de petites sommes d'argent pour des frais virtuellement nuls (micro-transactions). Cela pourrait signifier que les millions de personnes non bancarisées dans le monde qui possèdent des smartphones peuvent commencer à transiger bien au-delà de leurs frontières traditionnelles du monde physique.

Heureusement, les gouvernements regardent au-delà de la simple cryptomonnaie lorsqu'il s'agit de déployer cette technologie – pour [enregistrer la propriété foncière](http://www.redherring.com/startups/georgia-pilots-sweden-ponders-blockchain-future-europes-land-registries/), [par exemple](http://dci.mit.edu/assets/papers/spielman_thesis.pdf).

En effet, nous pourrions créer un monde de transactions numériques pair-à-pair pour le transfert de valeur qui est distribué, horizontal, élimine le besoin de se fier à la confiance, et surtout nécessite une puissance de calcul extraordinaire pour être falsifié. Ces transactions pourraient être entre personnes, machines et appareils.

Cela pourrait donc offrir un nouveau paradigme de sécurité pour la protection des données collectées et transférées par l'« internet des objets ».

Je crois personnellement que la complexité du monde moderne est obscurcie derrière des écrans tactiles intuitifs. La technologie de la blockchain deviendra rapidement intégrée dans notre univers technologique sans que nous en soyons pleinement conscients – tout comme nous utilisons l'ADN recombinant de levure pour la production d'insuline synthétique depuis les années 1970.

Les changements et les économies de coûts seront globalement référencés comme des changements technologiques, comme cette « chose interweby » ou une autre phrase vague et inclusive.

Un hic : cela fonctionnera tant que nous pourrons faire confiance à un « système sans confiance » qui est codé et conçu par des humains (en qui nous avons confiance ?) pour promouvoir la cause du « sans confiance » dans un monde méfiant et peu fiable. Vous devrez peut-être lire cette phrase plusieurs fois.

## Conclusion

D'accord – vous devriez maintenant être raisonnablement conscient des bases de la blockchain. Mais il y a beaucoup plus à apprendre si vous êtes intéressé.

Vous pouvez débattre si la blockchain est utile ou surévaluée, révolutionnaire ou ennuyeuse. Mais il est difficile d'ignorer qu'elle est assez cool en tant que concept.

Voici une vidéo vraiment fantastique d'Anders Brownworth qui explique tout cela avec une blockchain factice. Je vous recommande fortement de la regarder.

%[https://youtu.be/_160oMzblY8]

Et en tant qu'exercice d'apprentissage, vous pouvez construire votre propre blockchain directement dans votre navigateur ou votre ligne de commande. Voici un rapide [tutoriel pour construire votre propre blockchain](https://www.freecodecamp.org/news/how-does-blockchain-really-work-i-built-an-app-to-show-you-6b70cd4caf7d/).

Si vous avez des commentaires sur cet article ou pensez que j'aurais pu expliquer certaines parties mieux, tweetez-moi à [@ZubinPratap](https://twitter.com/zubinpratap)

Si vous souhaitez en savoir plus sur mon parcours dans le code, consultez l'[épisode 53](http://podcast.freecodecamp.org/53-zubin-pratap-from-lawyer-to-developer) du [podcast freeCodeCamp](http://podcast.freecodecamp.org/), où Quincy (fondateur de freeCodeCamp) et moi partageons nos expériences en tant que changeurs de carrière qui pourraient vous aider dans votre parcours. Vous pouvez également accéder au podcast sur [iTunes](https://itunes.apple.com/au/podcast/ep-53-zubin-pratap-from-lawyer-to-developer/id1313660749?i=1000431046274&mt=2), [Stitcher](https://www.stitcher.com/podcast/freecodecamp-podcast/e/59201373?autoplay=true), et [Spotify](https://open.spotify.com/episode/4lG0RGpzriG5vXRMgza05C).

Je vais également organiser quelques AMAs et webinaires dans les mois à venir. Si cela vous intéresse, faites-le moi savoir en allant [ici](http://www.matchfitmastery.com/). Et bien sûr, vous pouvez également me tweeter à [@ZubinPratap](https://twitter.com/zubinpratap).