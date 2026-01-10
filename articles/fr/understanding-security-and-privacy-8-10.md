---
title: Sécurité et confidentialité – Ce que vous devez savoir pour protéger vos données
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-03-01T18:36:46.000Z'
originalURL: https://freecodecamp.org/news/understanding-security-and-privacy-8-10
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-photomix-company-96612.jpg
tags:
- name: information security
  slug: information-security
- name: privacy
  slug: privacy
- name: Security
  slug: security
seo_title: Sécurité et confidentialité – Ce que vous devez savoir pour protéger vos
  données
seo_desc: 'I''ve talked a lot about security and privacy in my "A Beginners Guide
  to Digital Security" and "What Is Digital Privacy" articles. So why are we flogging
  this certifiably dead horse now?

  Because it''s not dead. Security and privacy are as or more impo...'
---

J'ai beaucoup parlé de sécurité et de confidentialité dans mes articles "[Un guide du débutant pour la sécurité numérique](https://www.freecodecamp.org/news/understanding-digital-security/)" et "[Qu'est-ce que la confidentialité numérique](https://www.freecodecamp.org/news/beginners-guide-to-digital-privacy/)". Alors pourquoi ressasser ce cheval mort certifié maintenant ?

Parce qu'il n'est pas mort. La sécurité et la confidentialité sont aussi importantes, sinon plus, que tout autre aspect des technologies de l'information. La plupart d'entre nous n'y pensent pas assez, mais c'est quelque chose que vous ne pouvez vraiment pas trop faire. 

Comme le dirait un professionnel de l'informatique exceptionnel avec qui j'ai travaillé : "Paranoïaque n'est qu'un début." Et en plus, il reste encore quelques sujets urgents et fascinants que nous n'avons pas abordés.

Nous allons donc passer un peu de temps à explorer comment les outils de sécurité de base (comme les contrôles d'authentification et le chiffrement) peuvent être appliqués pour résoudre un éventail beaucoup plus large de problèmes de sécurité et de confidentialité. Et nous allons également affronter directement quelques menaces significatives qui existent grâce aux appareils que nous avons appris à aimer.

Ce chapitre a été tiré du livre, [Rester à jour : Des informations de base sur toutes les grandes tendances technologiques que vous ne pouvez pas vous permettre d'ignorer](https://amzn.to/3FXXAfb). Si vous préférez regarder ce chapitre sous forme de vidéo, n'hésitez pas à suivre ici :

%[https://www.youtube.com/watch?v=FOlJEp4UEiA&list=PLSiZCpRYoTZ6UWl4xialvwLOKyHYYJUiC&index=8]

# Blockchains et sécurité

La machine à hype des nouvelles technologies a adoré les blockchains lorsqu'elles sont arrivées à l'attention du public. Il y avait fréquemment des articles élogieux dans les médias sur la façon dont c'était _ça_ : les blockchains étaient sur le point de changer le monde, inaugurant un âge d'or de joie sans fin et de licornes féeriques duveteuses. Réjouissez-vous ! Le salut est arrivé.

Mais malgré tout cela, les technologies de blockchain sont, en fait, une grande affaire. Avant d'aller là-bas, cependant, de quoi s'agit-il exactement ?

Une blockchain est une chaîne distribuée de enregistrements numériques utilisée pour enregistrer et valider des transactions. L'objectif est de maintenir un "grand livre" public fiable et incorruptible des transactions pour sécuriser et améliorer la manière dont les opérations financières et de marchandises sont enregistrées.

Les _blocs_ dans les _blockchains_ sont en fait des paquets de données contenant certaines méta-informations d'identification (y compris un horodatage) et un hachage cryptographique. 

Le hachage – qui est produit par un logiciel exécuté sur l'ordinateur qui génère le bloc – est dérivé du contenu unique du bloc précédent dans la chaîne qui, à son tour, était basé sur le bloc qui l'a précédé.

Parce que le contenu d'un bloc dépend de l'état des autres, aucun bloc unique ne peut être modifié sans laisser derrière lui des preuves évidentes et facilement traçables. 

Cela explique pourquoi on l'appelle une _chaîne_, car si un seul maillon (bloc) est altéré, toute la chaîne se brisera. En effet, une chaîne ne sera jamais fiable à moins qu'elle ne maintienne le consensus clair des créateurs de tous ses blocs.

La génération des hachages pour les blockchains est intensive en calcul et peut entraîner des coûts significatifs en puissance de calcul et en électricité. 

C'est par conception, car cela force presque les blockchains dans les mains de communautés distribuées, plutôt que dans celles d'individus ou de petits groupes. Cette décentralisation rend les chaînes moins vulnérables aux attaques et ajoute une robustesse à la fiabilité des données qui sont gérées.

## Blockchains et cryptomonnaie

Comme la plupart des gens, j'ai d'abord entendu parler des blockchains dans le contexte des cryptomonnaies comme Bitcoin et Ethereum. Les cryptomonnaies sont des actifs numériques qui peuvent être utilisés comme alternatives à la monnaie fiduciaire (c'est-à-dire le type de représentations virtuelles et mutuellement acceptées de valeur trouvées dans des instruments d'échange comme les monnaies nationales).

En utilisant les fonds d'un compte en cryptomonnaie, je pourrais payer des biens ou des services tout en conservant, dans de nombreux cas, l'anonymat. Bien sûr, cet anonymat même comporte des risques significatifs.

Les cryptomonnaies ont, par exemple, été utilisées pour soutenir des activités criminelles. Les personnes derrière les attaques de ransomware demanderont souvent des paiements en cryptomonnaie en échange des clés de déchiffrement qui, vous l'espérez, restaureront l'accès à vos données perdues. 

Et le contenu de grands comptes de cryptomonnaie a été effectivement perdu lorsque les serveurs de contrôle ont planté (ou ont été forcés de s'arrêter) ou, dans au moins un cas, lorsque l'administrateur d'une monnaie valant des millions de dollars est mort sans partager ses informations d'authentification.

Il est utile de noter que la valeur relative des fonds dans le compte lui-même – lorsqu'elle est mesurée par rapport à la capacité de les échanger contre de la monnaie fiduciaire – a historiquement été volatile, souffrant de manière imprévisible de fluctuations violentes du marché.

## Blockchains et comptabilité

Les blockchains peuvent résoudre de nombreux problèmes anciens adressés par les pratiques comptables traditionnelles. Plus précisément, l'intégration de la vérification par blockchain dans les processus financiers d'une entreprise peut fournir des transactions sécurisées et un accès à la demande à des enregistrements immuables et transparents. 

L'existence continue et en temps réel de tels enregistrements pourrait éventuellement éliminer le besoin d'audits périodiques et de réconciliations mensuelles.

De nombreuses caractéristiques de ces blockchains pourraient profondément changer la nature et la valeur des contrats – un changement qui pourrait se répandre au-delà de la comptabilité, dans la pratique du droit.

## Blockchains et assurance

Les caractéristiques potentielles de sécurité et de confidentialité des blockchains bien conçues peuvent également créer des efficacités et de la valeur dans l'industrie de l'assurance. 

Pour un exemple, avoir une seule blockchain où tous les assureurs d'un marché particulier peuvent partager de manière fiable les informations de compte de leurs clients peut aider à réduire la fraude aux réclamations. Les comportements suspects et les multiples réclamations pour un seul événement seront plus facilement visibles dans un système transparent et hautement accessible qui inclut les données de toutes les parties participantes.

Pouvoir réduire la duplication administrative peut également grandement rationaliser le traitement des réclamations légitimes. 

Vous apprécierez cela lorsque vous considérerez comment l'assureur d'une victime traitera souvent la réclamation de son client en utilisant des étapes similaires à celles utilisées par l'assureur auprès duquel vous faites une réclamation. Mais si les deux entreprises sont capables de partager ouvertement leurs données, le processus peut être unifié et, encore mieux, automatisé.

Peut-être, et c'est le plus significatif, la prestation des soins de santé peut être améliorée et rendue plus efficace si les dossiers personnels critiques peuvent être consultés de manière sûre et instantanée. Et – vous l'avez deviné – les blockchains peuvent être utiles ici aussi.

De quels types d'automatisation parlons-nous ? Eh bien, en revenant aux réclamations d'accidents, un "contrat intelligent" est un logiciel qui vérifie régulièrement les changements de statut des objets associés. Le simple clic de souris d'approbation d'un expert en sinistres, par exemple, pourrait déclencher tous les événements nécessaires pour payer une réclamation, notifier toutes les parties concernées et mettre à jour les dossiers existants.

Peut-être – juste peut-être – que l'assurance n'est pas aussi ennuyeuse que les gens le pensent.

# Qu'est-ce que l'authentification multifacteur ?

Les mots de passe sont des choses terribles. Bien sûr, nous ne pouvons pas simplement laisser nos appareils et comptes en ligne ouverts à tous. Mais qui a décidé que demander aux gens de mémoriser de longues chaînes de texte sans signification (comme _sIIkdm^&sv234LKi_) était la solution ? 

Bien sûr, vous pourriez choisir des mots de passe faciles à retenir comme _mysecret_ ou cette variation astucieuse : _mysecret22_. Mais tout ce qui est facile à retenir est tout aussi facile à deviner. Et doublez cela si vous utilisez le même mot de passe pour plusieurs comptes. En d'autres termes, ce type de protection ne vaut pas l'effort.

Il existe, soit dit en passant, deux façons d'améliorer vos mots de passe :

* Utilisez un coffre-fort de mots de passe pour générer et stocker en toute sécurité des mots de passe extrêmement complexes que vous n'aurez pas besoin de mémoriser : vous pouvez simplement les copier et les coller dans les pages de connexion que vous visitez.
* Utilisez des mots de passe longs (15-20 caractères) qui incorporent des mots mémorables, mais non connectés. Quelque chose comme : _house-seventy-warfare-calf_.

Mathématiquement parlant, il est hautement improbable que quelqu'un ait la puissance de calcul et le temps nécessaires pour craquer celui-ci. Et ce n'est pas si difficile à mémoriser.

Mais lorsqu'il s'agit de sites particulièrement sensibles – comme ceux où vous faites vos opérations bancaires – même de bons mots de passe ne suffisent pas. Pour cette raison, de plus en plus d'organisations intègrent l'authentification multifacteur (MFA) dans leurs profils de sécurité.

Un site web ou une application configurée avec MFA vous demande de présenter plus d'un type de preuve que vous êtes bien celui que vous prétendez être. 

L'un pourrait être basé sur quelque chose que vous savez, et un autre pourrait être une preuve basée sur quelque chose que vous avez. "Quelque chose que vous savez" pourrait être un mot de passe, tandis que "quelque chose que vous avez" pourrait être un appareil MFA autonome ou une application exécutée sur votre smartphone. 

Cela fonctionne souvent en ayant l'application envoyer un code de courte durée via un message instantané à un numéro de téléphone prédéfini. Vous devrez entrer le code sur la page de connexion d'authentification.

# Qu'est-ce que les identités fédérées ?

Une fois que vous avez maîtrisé les bases de l'authentification, grâce à des mots de passe robustes et/ou à la MFA, il y a la question de l'autorisation. En d'autres termes, quelles ressources votre compte connecté pourra accéder. 

Les systèmes individuels contrôleront les utilisateurs grâce à un type de contrôles d'accès. Microsoft Windows, par exemple, utilise Active Directory, Linux a des permissions d'objet, et les fournisseurs de cloud comme Amazon Web Services peuvent appliquer des rôles et des politiques.

Mais si vous voulez que vos utilisateurs puissent passer _entre_ les services sans avoir à se connecter à chaque service individuellement, ou si vous préférez simplement ne pas avoir à gérer l'authentification du tout, vous pouvez implémenter une identité fédérée.

Vous avez probablement déjà expérimenté la fédération sans même le savoir. Se connecter à un service web tiers en utilisant votre compte Google est une forme de fédération. 

Le service intègre son système d'authentification avec un fournisseur de fédération en utilisant une technologie d'identité comme Security Assertion Markup Language (SAML) ou OAuth. 

Lorsque vous acceptez les termes et vous connectez, le fournisseur partagera juste assez d'informations d'identité avec le service tiers pour permettre la création d'un compte.

# Surveillance numérique

Parce qu'elle peut à la fois vous protéger du danger et aussi envahir votre vie privée, la surveillance est une épée à double tranchant. Mais la surveillance _numérique_ est une épée à double tranchant qui est beaucoup plus tranchante. Laissez-moi expliquer pourquoi.

Les caméras vidéo en circuit fermé sont utilisées dans les systèmes de sécurité depuis au moins les années 1930, mais elles ne faisaient vraiment qu'une seule chose : enregistrer des images qui étaient généralement stockées localement et ensuite, après quelques jours, écrasées par de nouveaux enregistrements. 

C'était utile mais, pour être efficace, vous deviez physiquement accéder à la bande et ensuite rechercher laborieusement, trouver et visionner les images d'intérêt.

Les caméras de surveillance numériques sont certainement moins chères que leurs équivalents analogiques, beaucoup plus faciles à cacher physiquement et faciles à accéder via les réseaux. 

Mais il y a aussi beaucoup plus de choses que vous pouvez faire avec des flux vidéo numériques. Vous pouvez, par exemple, configurer des alertes par e-mail chaque fois que la caméra détecte un mouvement. Ou vous pouvez rediriger un flux vidéo vers des services cloud (comme Kinesis d'Amazon) où il peut être intégré à vos opérations d'analyse de données et d'apprentissage automatique ou interprété en temps quasi réel par un service de reconnaissance d'objets et de visages (comme Rekognition d'Amazon).

Tous ces outils peuvent être utilisés au service de buts à la fois positifs et nuisibles. Le fait est qu'il existe désormais des millions de ces caméras déployées dans le monde qui sont, dans de nombreux cas, connectées à des opérations de surveillance à grande échelle. À tout le moins, vous devriez être conscient du potentiel ainsi que du risque que présentent ces technologies.

# Qu'est-ce qu'une porte dérobée ?

Une _porte dérobée_ est une vulnérabilité matérielle ou logicielle qui a été intentionnellement intégrée dans un appareil ou le système d'exploitation qui l'exécute.

Dans certains cas, la porte dérobée existe avec la pleine connaissance du client, car elle était destinée à permettre un support à distance ou l'installation automatisée de correctifs et de mises à jour. Mais ce n'est pas toujours le cas.

Les gouvernements, les entreprises associées aux gouvernements et les organisations criminelles ont été pris en train de livrer des appareils informatiques et de réseau sensibles avec des portes dérobées dangereuses. De telles vulnérabilités ont été utilisées pour contourner la protection par chiffrement afin de surveiller les communications, voler des données de recherche et récolter des informations d'authentification.

Les portes dérobées peuvent prendre la forme de logiciels malveillants actifs qui collectent des données locales et les envoient ensuite à des serveurs d'attaque distants, ou permettent passivement des connexions à distance via des environnements réseau non sécurisés.

Se protéger contre les portes dérobées nécessite une défense à plusieurs niveaux, y compris :

* Une vérification minutieuse des fournisseurs potentiels de matériel (en tenant compte de leurs pays d'origine et de leurs associations)
* Une surveillance régulière des sources d'information technologique fiables pour les nouvelles découvertes de vulnérabilités
* Une surveillance minutieuse des activités réseau de vos appareils
* Une mise à jour régulière de vos systèmes de réseau et d'informatique
* Une chance aveugle et stupide en grandes doses

Merci d'avoir lu ! Espérons que vous avez maintenant une meilleure idée de l'importance de la sécurité et de la confidentialité et de la manière de protéger les vôtres.

_Les vidéos YouTube des dix chapitres de ce livre [sont disponibles ici](https://www.youtube.com/playlist?list=PLSiZCpRYoTZ6UWl4xialvwLOKyHYYJUiC). Beaucoup plus de bonnes choses technologiques - sous forme de livres, de cours et d'articles - [peuvent être trouvées ici](https://bootstrap-it.com). Et envisagez de suivre mes [cours sur AWS, la sécurité et la technologie des conteneurs ici](https://www.udemy.com/user/david-clinton-12/).