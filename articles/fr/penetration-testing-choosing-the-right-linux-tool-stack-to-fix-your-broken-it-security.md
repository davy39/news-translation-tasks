---
title: 'Tests d''intrusion : choisir la bonne pile d''outils (Linux) pour réparer
  votre sécurité IT défaillante'
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-07-29T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/penetration-testing-choosing-the-right-linux-tool-stack-to-fix-your-broken-it-security
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/security.jpeg
tags:
- name: Linux
  slug: linux
- name: penetration testing
  slug: penetration-testing
- name: Security
  slug: security
seo_title: 'Tests d''intrusion : choisir la bonne pile d''outils (Linux) pour réparer
  votre sécurité IT défaillante'
seo_desc: 'Got IT infrastructure? Do you know how secure it is? The answer will probably
  hurt, but this is the kind of bad news you’re better off getting sooner rather than
  later.

  The only reasonably sure way to find out what’s going on with your servers is to
  ...'
---

Vous avez une infrastructure IT ? Savez-vous à quel point elle est sécurisée ? La réponse risque de faire mal, mais c'est le genre de mauvaise nouvelle qu'il vaut mieux recevoir tôt plutôt que tard.

La seule façon raisonnablement sûre de savoir ce qui se passe avec vos serveurs est d'appliquer une série solide de tests d'intrusion. Votre objectif ultime est de découvrir toute vulnérabilité dangereuse afin de pouvoir les verrouiller.

Par "vulnérabilité dangereuse", j'entends des choses évidentes comme des ports ouverts non protégés et des logiciels non corrigés. Mais je veux aussi dire l'existence d'informations librement disponibles sur votre organisation qui flottent probablement sur Internet, attendant d'être collectées et utilisées contre vous.

Les tests d'intrusion se composent de trois parties très différentes, chacune avec ses propres outils et protocoles uniques.

* **Collecte passive d'informations**, où les testeurs fouillent l'Internet public à la recherche d'indices subtils ou de données privées révélées négligemment qui peuvent être utilisées contre l'organisation.
* **Collecte active d'informations**, où les réseaux et serveurs de l'organisation sont scannés pour détecter les vulnérabilités potentielles.
* **Identification des exploits** qui pourraient éventuellement être exécutés contre l'infrastructure de l'organisation.

Examinons chacune de ces parties une par une.

## Collecte passive d'informations (OSINT)

Disons que votre entreprise compte environ 50 employés et une poignée de contractants externes, chacun étant probablement actif sur les réseaux sociaux professionnels et personnels. Et disons que vous avez la gamme habituelle de sites Web corporatifs et de produits, ainsi que des comptes de médias sociaux (comme LinkedIn).

Prenez un moment pour imaginer que vous êtes un hacker à la recherche d'informations exploitables sur votre entreprise qu'il peut utiliser pour lancer une attaque. En supposant qu'il se limite exclusivement à l'Internet public et ne viole aucune loi, combien pensez-vous qu'il trouvera ?

Pas trop ? Après tout, personne n'est assez stupide pour publier des mots de passe et des informations de compte sur Internet, n'est-ce pas ?

Peut-être. Mais vous ne croirez pas à quel point il peut être facile d'utiliser ce qui **est** là pour découvrir tous les mots de passe et les informations d'administration dont les hackers auront besoin pour obtenir ce qu'ils veulent. Vous ne me croyez pas ? Faites vous-même une collecte passive d'informations.

Parmi les outils fantastiques/terrifiants de collecte d'informations disponibles pour vous aider (qui incluent également Maltego et Shodan), il y a un excellent package open source basé sur Linux nommé Recon-ng — à propos duquel j'ai créé un [cours vidéo sur Pluralsight](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton).

Vous commencez par fournir à Recon-ng quelques informations sur votre entreprise et en choisissant les scans particuliers qui vous intéressent. Tout le travail difficile sera ensuite effectué par des outils qu'ils appellent _modules_. Chacun des 90+ modules disponibles est un script qui lit les données de la base de données Recon-ng et lance une opération de scan contre une ressource de données distante.

En fonction de vos choix, Recon-ng parcourra intelligemment d'énormes volumes de résultats DNS, de médias sociaux et de moteurs de recherche, ainsi que des offres d'emploi riches en informations pour de nouveaux développeurs et des indices sur les adresses e-mail internes liées à votre cible. Une fois terminé, le logiciel préparera un rapport qui vous fera peur.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-57.png)
_Un rapport textuel basé sur quelques scans Recon-ng_

Avec ces informations, un hacker n'aurait qu'à parcourir les données et fixer la date de lancement de votre attaque. Avec ces informations, **vous** n'aurez qu'à renforcer vos défenses et parler à votre équipe pour être **beaucoup** plus prudent lors de la communication en ligne.

Cet acronyme OSINT que j'ai utilisé ci-dessus ? Il signifie Open Source Intelligence. Des choses que n'importe qui peut obtenir.

## Collecte active d'informations (évaluation des vulnérabilités)

Outre toutes les choses que vous laissez traîner sans réfléchir sur Internet, il y a probablement beaucoup plus qu'un hacker peut apprendre sur votre infrastructure à partir de l'infrastructure elle-même. Si vos serveurs sont sur un réseau, c'est parce que, dans une certaine mesure, vous voulez qu'ils soient exposés aux utilisateurs du réseau. Mais cela pourrait également exposer des choses que vous préféreriez garder secrètes, y compris le fait que vous pourriez exécuter un logiciel bogué et ouvert aux exploits.

La bonne nouvelle est que les acteurs gouvernementaux et industriels — comme le gouvernement américain et leur [National Vulnerability Database](https://nvd.nist.gov/) — suivent activement les vulnérabilités logicielles depuis des décennies et rendent leurs informations librement disponibles. La mauvaise nouvelle est que leurs bases de données contiennent des centaines de milliers de ces vulnérabilités et cela fait une lecture vraiment ennuyeuse.

Vous aimeriez pouvoir scanner rapidement et régulièrement votre réseau et les appareils qui y sont connectés pour vous assurer qu'il n'y a rien à corriger, mais il est tout simplement impossible de le faire manuellement. Alors oubliez les humains. Vous allez avoir besoin de logiciels.

Les scanners de vulnérabilités sont des outils logiciels qui scannent automatiquement votre réseau et vos serveurs pour détecter les logiciels non corrigés, les ports ouverts, les services mal configurés et les vecteurs d'exploits potentiels (comme l'injection SQL ou le cross-site scripting). Généralement, le logiciel gère les données de vulnérabilité et recherche toute correspondance avec ce que vous avez en cours d'exécution. C'est à vous de définir la cible, de définir les types de scan que vous souhaitez exécuter, de lire les rapports qui sortent de l'autre côté et — surtout — de corriger ce qui est cassé.

Les packages de scan commerciaux avec des niveaux gratuits incluent Nessus, Nexpose et Burp Suite. OpenVAS est un outil mature, entièrement open source qui peut gérer presque tout ce que vous lui lancez. Et, de manière très pratique, il se trouve que ma collection Pluralsight comprend également un [guide vidéo pour utiliser OpenVAS](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton).

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-58.png)
_La page des résultats d'un scan OpenVAS — utilisant leur interface navigateur Greenbone_

Une plateforme exceptionnelle pour exécuter tous types de scans et de tests est la distribution Kali Linux. Kali, qui est elle-même très sécurisée par défaut, vient avec des dizaines de packages logiciels de réseau et de sécurité préconfigurés. OpenVAS, bien que facilement installable sur Kali, a été exclu du profil par défaut en raison de sa taille.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-59.png)
_Quelques packages logiciels adaptés aux tests d'intrusion disponibles dans Kali Linux dès la sortie de la boîte_

Il est courant d'exécuter Kali dans un environnement virtuel comme [VirtualBox](https://hackernoon.com/virtualbox-are-you-getting-your-moneys-worth-4d7f98f3d7d2) plutôt que de lui faire occuper une machine physique entière. Ainsi, vous pouvez isoler en toute sécurité vos tests de vos activités informatiques régulières... sans parler de vous faire économiser du temps et de l'argent significatifs.

## Tests d'exploits (tests de pénétration)

Ici (**_après_** avoir obtenu une autorisation explicite de la direction de l'organisation) est l'endroit où vos testeurs d'intrusion tentent réellement de pénétrer vos défenses pour voir jusqu'où ils peuvent aller. Les testeurs utiliseront des outils comme le Metasploit Framework (souvent également exécuté à partir de Kali Linux), qui exécute des exploits en direct contre l'infrastructure cible. Ma mauvaise chance : je n'ai pas de cours sur Metasploit, mais [d'autres auteurs de Pluralsight](http://pluralsight.pxf.io/c/1191769/424552/7490?u=pluralsight.com) en ont certainement.

L'objectif immédiat est de tirer parti de l'une des vulnérabilités du réseau ou du système d'exploitation découvertes lors des premières étapes du processus de scan. Mais l'idée ultime, bien sûr, est de corriger les failles de sécurité que votre testeur d'intrusion découvre. Tous les tests du monde ne vous seront d'aucune utilité si vous ne les utilisez pas pour vous améliorer.

Outre les outils de piratage purement techniques que vous utiliserez, la phase d'exploitation des tests d'intrusion peut également incorporer une bonne vieille ingénierie sociale. C'est là que (lorsque cela est autorisé) vous pouvez utiliser des e-mails, des appels téléphoniques et des contacts personnels pour essayer de tromper les employés afin qu'ils divulguent des informations sensibles.

C'est beaucoup de travail et cela nécessite une grande formation et préparation pour bien le faire. Mais si vous êtes responsable des ressources IT de votre entreprise, vous ne pouvez pas laisser les tests d'intrusion pour plus tard.

Alors, quelle est votre prochaine étape ? Si vous êtes du genre à tout faire vous-même, alors par tous les moyens, travaillez soigneusement à travers certaines ressources en ligne ou des cours et plongez-vous dedans. Sinon, trouvez un professionnel en qui vous avez confiance et voyez ce qu'ils recommandent.

Bonne chance !

_Ne pensez pas que je suis juste une sorte de geek unidimensionnel. En plus de mes [cours Pluralsight](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton), j'écris également des [cours de livres sur Linux et AWS](https://bootstrap-it.com/) et même un cours hybride appelé [Linux in Motion](https://www.manning.com/livevideo/linux-in-motion?a_aid=bootstrap-it&a_bid=0c56986f&chan=motion1) qui est composé de plus de deux heures de vidéos et d'environ 40 % du contenu de mon livre [Linux in Action](https://www.manning.com/books/linux-in-action?a_aid=bootstrap-it&a_bid=4ca15fc9). D'accord. Donc je suppose que je suis une sorte de geek unidimensionnel._