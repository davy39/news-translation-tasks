---
title: Qu'est-ce que le modèle à cinq couches ? Le cadre d'Internet expliqué
subtitle: ''
author: Omer Rosenbaum
co_authors: []
series: null
date: '2022-10-17T13:37:19.000Z'
originalURL: https://freecodecamp.org/news/the-five-layers-model-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/d.png
tags:
- name: computer network
  slug: computer-network
- name: computer networking
  slug: computer-networking
seo_title: Qu'est-ce que le modèle à cinq couches ? Le cadre d'Internet expliqué
seo_desc: "Computer Networks are a beautiful, amazing topic. Networks involve so much\
  \ knowledge from different fields, from physics to algorithms. \nWhen dealing with\
  \ Computer Networks, there is one framework that puts everything into place – and\
  \ that is the lay..."
---

Les réseaux informatiques sont un sujet magnifique et fascinant. Les réseaux impliquent tant de connaissances issues de différents domaines, de la physique aux algorithmes. 

Lorsqu'on traite des réseaux informatiques, il existe un cadre qui met tout en place – et c'est le modèle en couches. 

Dans cet article, vous apprendrez _pourquoi_ nous avons besoin de couches, ainsi que _ce qu'est_ le modèle à cinq couches. Vous comprendrez également le rôle de chaque couche dans ce modèle. 

# Pourquoi des couches ?

Imaginez que vous avez pour tâche de concevoir et d'implémenter l'Internet ! Par où commencez-vous ? Que voulons-nous réellement d'un réseau, et d'un réseau important comme l'Internet ? 

Eh bien, nous voulons en réalité beaucoup de choses. Pour en citer quelques-unes :

* Nous voulons qu'il soit **rapide** – c'est-à-dire, permettre une communication rapide. Nous ne voulons pas attendre longtemps pour qu'un message passe d'un hôte à un autre.
* Il doit également être **fiable** – lorsque nous envoyons un message, nous voulons que le destinataire le reçoive réellement.
* Le réseau doit être **extensible** – c'est-à-dire, permettre à plus d'appareils de se joindre. Nous ne voudrions pas commencer avec deux ordinateurs, puis ne pas pouvoir en ajouter un troisième.
* Le réseau doit supporter **différents appareils et connexions** – il doit être capable de connecter un PC filaire, un ordinateur portable sans fil et un téléphone portable, par exemple.

Et ce n'est qu'une liste partielle.

Alors, comment procéder pour implémenter l'Internet lorsque nous voulons atteindre autant de choses différentes ?

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-58.png)
_Les réseaux informatiques sont complexes (Source : [XKCD](https://xkcd.com/2259/))_

Afin de simplifier les choses et de rendre les réseaux flexibles, la communication est divisée en **couches**. 

Chaque couche a sa propre responsabilité. Elle fournit des services à une couche supérieure et utilise les services fournis par une couche inférieure.

Considérons un exemple de réseau composé de trois appareils :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-51.png)
_Un exemple de réseau avec trois appareils (Source : [Brief](https://www.youtube.com/watch?v=iHp5J_f_ToQ&ab_channel=Brief))_

Nous avons deux couches :

**La couche Alpha** est responsable de la transmission de données entre des hôtes directement connectés les uns aux autres. Dans le diagramme ci-dessus, c'est entre les hôtes A et B, ou entre les hôtes B et C.

**La couche Bêta** est responsable de la transmission de données entre des hôtes distants. Dans le diagramme, c'est entre les hôtes A et C.

Qu'avons-nous gagné avec cette division ? Nous avons gagné beaucoup de **flexibilité**. 

Chaque couche peut être développée et implémentée par différentes personnes. La couche supérieure ne se soucie pas de l'implémentation de la couche inférieure, et vice versa.

Par exemple, la connexion entre les hôtes A et B pourrait être une connexion WiFi, tandis que la connexion entre B et C pourrait consister en un pigeon voyageur. Ce sont des implémentations (complètement) différentes de la couche Alpha. 

Remarquez que cette méthode permet également d'avoir différentes spécialisations et expertises – un expert dans le dressage de pigeons voyageurs n'a pas nécessairement à être qualifié pour construire des cartes réseau WiFi solides, ou vice versa.  


![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-52.png)
_La couche Alpha peut avoir différentes implémentations sur le même réseau (Source : [Brief](https://www.youtube.com/watch?v=iHp5J_f_ToQ&ab_channel=Brief))_

Les développeurs de la couche Bêta n'ont pas besoin de se soucier de cette différence. À ce niveau, l'hôte A doit savoir que pour atteindre l'hôte C, il doit d'abord envoyer son message à l'hôte B, plutôt qu'à, par exemple, l'hôte D. Ensuite, l'hôte B le transmettra à l'hôte C.

Ainsi, la couche Bêta est uniquement responsable de la recherche de l'itinéraire pour envoyer le message. Elle utilise le service fourni par la couche Alpha – transmettre des données entre des hôtes directement connectés.

En général, les réseaux sont très compliqués et ont diverses exigences. Diviser la communication en couches nous permettra de simplifier les choses et de rendre la communication plus flexible.

Maintenant que vous comprenez _pourquoi_ nous avons besoin de couches, nous pouvons passer à l'apprentissage des couches qui sont réellement utilisées dans les réseaux. 

# Qu'est-ce que le modèle à cinq couches ?

Il y a eu plusieurs modèles de couches proposés au fil des ans – notamment, le modèle à cinq couches, le modèle à 7 couches (aka modèle OSI), ou le modèle à 4 couches (aka le modèle TCP/IP). 

Ils sont bien plus similaires que différents, et je choisis de me concentrer sur le modèle à cinq couches car il est le plus pratique de tous – et décrit le mieux le fonctionnement réel de l'Internet.

## La première couche – La couche physique

La première couche est responsable de la **transmission d'un seul bit** – 0 ou 1 – sur le réseau.

Pour avoir une intuition de ce dont cette couche est responsable, considérons le temps de transmission. Supposons que nous avons un type de câble pour transmettre nos données, et que nous utilisons une tension de `+5` Volt pour transmettre `1`, et une tension de `-5` Volt pour transmettre `0`. Quels bits représente le diagramme suivant ?

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-53.png)
_Une implémentation de la couche physique encodant 1 comme +5 Volt et 0 comme -5 Volt (Source : [Brief](https://www.youtube.com/watch?v=Q3qqd6Y2FbQ&ab_channel=Brief))_

  
Eh bien, cela pourrait être `1001`. C'est le cas si cela prend _ce_ temps pour transmettre un seul bit (démontré par la ligne orange en pointillés dans le diagramme ci-dessous) :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-54.png)
_Un exemple de flux de bits encodé par ce signal (Source : [Brief](https://www.youtube.com/watch?v=Q3qqd6Y2FbQ&ab_channel=Brief))_

Cependant, cela pourrait également représenter d'autres flux de bits. Par exemple, si cela ne prend que la moitié du temps pour transmettre un seul bit (démontré par la ligne verte en pointillés ci-dessous), alors le flux de bits pourrait être `11000011` :  


![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-55.png)
_Un autre flux de bits possible encodé par le même signal (Source : [Brief](https://www.youtube.com/watch?v=Q3qqd6Y2FbQ&ab_channel=Brief))_

La différence réside dans le temps dédié à la transmission d'un seul bit. Cela s'appelle le **débit binaire** – c'est-à-dire, le nombre de bits qui sont transmis par unité de temps.

Bien sûr, atteindre un débit binaire élevé est préférable, car cela signifie que nous pouvons envoyer de nombreux bits en un court laps de temps. Mais il est difficile d'atteindre des débits binaires élevés sans obtenir de nombreuses erreurs.

Ce n'est qu'une des choses que la première couche doit prendre en considération. L'important pour l'instant est l'objectif de cette couche : transmettre et recevoir un seul bit.

## La deuxième couche – La couche de liaison de données

La deuxième couche est responsable de la transmission de données entre **deux hôtes directement liés**, malgré les erreurs possibles.

Que voulons-nous dire par "directement liés" ? Pour l'instant, imaginez qu'il n'y a aucun appareil entre les deux appareils. Donc, si nous avons deux ordinateurs ici – l'ordinateur A et l'ordinateur B, et qu'ils sont connectés via l'ordinateur M – alors l'ordinateur A et l'ordinateur B ne sont PAS directement liés. Mais l'ordinateur A et l'ordinateur M **sont** directement liés, et il en va de même pour l'ordinateur M et l'ordinateur B.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-56.png)
_Deux hôtes distants connectés via un autre appareil (Source : [Brief](https://www.youtube.com/watch?v=Q3qqd6Y2FbQ&ab_channel=Brief))_

Une autre façon de le dire est que l'ordinateur A et l'ordinateur M sont à **un saut** l'un de l'autre, tandis que l'ordinateur A et l'ordinateur B sont à **deux sauts**. 

C'est-à-dire, pour aller de l'ordinateur A à l'ordinateur B, nous avons besoin de deux "sauts" – un saut de A à M, et un autre saut de M à B.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-57.png)
_Chaque connexion directe est appelée un saut (Source : [Brief](https://www.youtube.com/watch?v=Q3qqd6Y2FbQ&ab_channel=Brief))_

Revenons à la responsabilité de la deuxième couche – nous avons mentionné qu'elle est responsable de la transmission de données entre deux hôtes directement liés, **malgré les erreurs possibles**.

Que voulons-nous dire par **erreurs** ? La couche physique peut fournir des données erronées. Par exemple, `1` au lieu de `0`. Ainsi, un flux de bits tel que `000110` pourrait être reçu comme `001110`. 

De nombreuses raisons peuvent causer ce type d'erreurs. Par exemple, nous pouvons imaginer un camion passant littéralement sur le fil où les bits sont transmis, causant un problème. Peu importe la raison, la deuxième couche doit gérer la communication malgré ces erreurs.

La deuxième couche envoie des données en _datagrammes_, c'est-à-dire en morceaux. Les datagrammes dans cette couche sont appelés **trames**. Les trames contiendront généralement des **adresses MAC**, qui sont des adresses physiques, une identifiant l'expéditeur, et une autre identifiant le destinataire.  
  
Pourquoi aurions-nous besoin d'une adresse MAC ?

Premièrement, les appareils récepteurs aimeraient savoir si la trame leur est destinée. Le récepteur ne voudrait pas perdre de temps précieux à lire des données destinées à quelqu'un d'autre. Si la trame contient une adresse MAC qui n'appartient pas à un appareil récepteur, cet appareil peut simplement ignorer cette trame.

Deuxièmement, pour des raisons de confidentialité - nous aimerions que les messages arrivent uniquement aux destinataires prévus, afin qu'ils soient les seuls à pouvoir lire les données.

Troisièmement, l'expéditeur aimerait que le destinataire sache qui a envoyé la trame. De cette façon, le destinataire pourra envoyer sa réponse à l'expéditeur, et non à quelqu'un d'autre.

Notez que nous aimerions que ces adresses soient uniques. C'est-à-dire, nous voulons qu'une adresse identifie un seul appareil. De cette façon, nous savons que si nous envoyons un message à une adresse spécifique, il sera envoyé uniquement à l'appareil prévu.

## La troisième couche – La couche réseau

La troisième couche est responsable du **routage** – c'est-à-dire, déterminer le chemin que les données emprunteront.

Vous pouvez penser à cette couche comme une application de routage réussie, Google Maps. Lorsque vous montez dans la voiture et utilisez Google Maps, vous indiquez à l'application votre destination, et Google Maps trouve le meilleur itinéraire pour vous. 

Remarquez que Google Maps est dynamique – il ne choisira pas nécessairement le même itinéraire à chaque fois. Parfois, un chemin aura un embouteillage, donc Google Maps préférera un autre itinéraire.

Nous avons dit que la deuxième couche a des adresses physiques, appelées adresses MAC. La troisième couche est responsable des **adresses logiques**, telles que les **adresses IP**. 

Dans cette couche, les datagrammes sont appelés **paquets**. 

Considérons le diagramme de réseau suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-59.png)
_Un diagramme de réseau avec l'ordinateur A en France, l'ordinateur B aux États-Unis, et 10 routeurs entre eux (Source : [Brief](https://www.youtube.com/watch?v=Q3qqd6Y2FbQ&ab_channel=Brief))_

Nous avons ici deux ordinateurs – un en France, et un aux États-Unis. Bien sûr, ils ne sont pas directement liés. Plutôt, ils sont liés via des appareils de la troisième couche appelés **routeurs**. 

Quelle couche est responsable de chaque connexion ?

Considérons la connexion entre l'ordinateur A et le routeur 1. La deuxième couche est responsable de cette connexion. Et la connexion entre le routeur 2 et le routeur 5 ? Exact, encore une fois, c'est la deuxième couche. Il en va de même pour chaque connexion entre deux appareils directement liés.

La troisième couche est responsable de la définition de l'itinéraire – c'est-à-dire que le message envoyé de l'ordinateur A à l'ordinateur B passera par les routeurs 1, 2, 5, 8 et 10, et non d'une autre manière.

Notez qu'il peut y avoir différentes implémentations pour chaque couche. Par exemple, nous pouvons avoir différentes implémentations de la deuxième couche. Ainsi, tandis que la connexion entre l'ordinateur A et le routeur 1 pourrait être via un câble Ethernet, la connexion entre le routeur 1 et 2 pourrait être sans fil et utiliser le WiFi. La connexion entre le routeur 2 et le routeur 5 pourrait utiliser un pigeon voyageur, tandis que la connexion entre le routeur 5 et 9 utilisera également le WiFi.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-61.png)
_La deuxième couche peut être implémentée différemment sur chaque lien (Source : [Brief](https://www.youtube.com/watch?v=Q3qqd6Y2FbQ&ab_channel=Brief))_

La troisième couche ne se soucie pas de ces changements, mais la deuxième couche le fait définitivement. Si le pigeon voyageur qui transmet les données du routeur 2 au routeur 5 est malade, la deuxième couche devra le gérer. La couche de liaison de données devra également s'assurer que les données transmises par les airs entre les routeurs 1 et 5 sont valides et sans erreurs. 

## Résumé intermédiaire

Jusqu'à présent, nous avons couvert trois des cinq couches. Pour récapituler :

* La couche physique est responsable de la transmission d'un seul bit, `1` ou `0`, sur le réseau. 
* La couche de liaison de données est responsable de la transmission de données entre des appareils directement liés, c'est-à-dire des appareils connectés via un seul saut. 
* La troisième couche est responsable du transfert de données entre des hôtes connectés via plusieurs sauts. Elle détermine l'itinéraire, le chemin que les paquets emprunteront.

## La quatrième couche – La couche de transport

La quatrième couche est une couche de bout en bout. C'est-à-dire, elle est responsable de la communication de la source jusqu'à la destination finale.

Elle permet le **multiplexage** de plusieurs services. Par exemple, un serveur peut servir de serveur Web ainsi que de serveur de messagerie. Lorsqu'un client se tourne vers ce serveur, le client doit être en mesure de spécifier quel service il souhaite accéder. Alors que la troisième couche spécifie l'adresse du serveur, la couche de transport identifie quel **service** est pertinent pour la communication actuelle.

De plus, la couche de transport _peut_ assurer la fiabilité. Ainsi, lorsque cette couche reçoit des données de la couche supérieure, elle les divise en morceaux, les envoie et s'assure que tous ces morceaux arrivent correctement à l'autre extrémité. 

Remarquez que la couche réseau n'est généralement _pas_ fiable. Les paquets peuvent arriver dans le mauvais ordre, ils peuvent arriver avec des données incorrectes, ou même ne pas arriver du tout. Une couche de transport fiable s'assure que les données sont correctement reçues.

Dans cette couche, les datagrammes sont appelés **segments**. 

Considérons à nouveau le diagramme de réseau suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-59.png)
_Le diagramme de réseau à nouveau (Source : [Brief](https://www.youtube.com/watch?v=Q3qqd6Y2FbQ&ab_channel=Brief))_

Quelle couche est responsable de quoi ?

Nous avons déjà dit que la couche réseau est responsable de l'itinéraire, c'est-à-dire le chemin que les paquets emprunteront. Nous avons également mentionné que la deuxième couche est responsable de la transmission des données entre deux appareils directement connectés. Par exemple, le lien entre le routeur 1 et le routeur 2.

La quatrième couche voit tout ce diagramme de réseau comme un nuage abstrait. Elle ne connaît pas les routeurs et ne se soucie pas de la structure du réseau, ni du routage. Elle suppose que le réseau peut envoyer un paquet d'une extrémité à l'autre :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-62.png)
_La quatrième couche voit le réseau comme un nuage abstrait (Source : [Brief](https://www.youtube.com/watch?v=LYH4DwydVAM&ab_channel=Brief))_

La couche de transport s'assure que les points d'extrémité peuvent communiquer via différents services – par exemple, le web et le courrier électronique. De plus, elle peut s'assurer que la connexion est fiable. 

Un exemple serait d'accuser réception de chaque segment reçu. Par exemple, lorsque l'ordinateur A envoie un segment à l'ordinateur B, l'ordinateur B enverra un segment d'accusé de réception spécial, annonçant qu'il a reçu le paquet. 

## La cinquième couche – La couche application

Dernière mais non des moindres, nous avons la cinquième couche, ou **couche application**. Cette couche fournit le service à l'application de l'utilisateur – service web, voix sur IP (VoIP), jeux en réseau, streaming, et ainsi de suite. 

Selon le modèle des couches, la cinquième couche ne se soucie pas du tout du réseau. Elle s'appuie sur la quatrième couche, ainsi que sur les couches inférieures, pour transmettre les données d'un point d'extrémité à un autre. La cinquième couche utilisera ce service pour les divers besoins de l'application. 

Différents protocoles seront utilisés pour différentes applications. Par exemple, le protocole HTTP est couramment utilisé pour servir des pages web sur le World Wide Web. SMTP est un protocole utilisé pour les emails, FTP pour échanger des fichiers, et il y en a beaucoup, beaucoup d'autres.

# Qu'est-ce que l'encapsulation ?

Le but des réseaux est de transmettre des données d'un hôte à un autre.

Pour atteindre cet objectif, chaque couche ajoute son propre **en-tête** aux données. Un en-tête contient des informations spécifiques à cette couche, et il précède les données elles-mêmes. 

Considérons un cas où nous avons un service de recherche, utilisé pour trouver le numéro de téléphone d'une personne, étant donné le nom de la personne. Les données consistent en le prénom et le nom de la personne. 

Avant que le paquet ne soit envoyé, la cinquième couche peut ajouter son propre **en-tête**, décrivant qu'il s'agit d'un paquet de REQUÊTE. L'en-tête peut également spécifier qu'il s'agit d'une demande de mappage du nom d'une personne à un numéro de téléphone, et non l'inverse.  


![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-64.png)
_En-tête de la 5ème couche, avec les données (Source : [Brief](https://www.youtube.com/watch?v=DBLtFjrTvD0&ab_channel=Brief))_

Ensuite, la cinquième couche transmet les données à la quatrième couche. Notez que la quatrième couche considère tout comme des données – des uns et des zéros. Elle ne se soucie pas si la cinquième couche a ajouté un en-tête, ou de ce qui est écrit dans cet en-tête. 

La quatrième couche ajoute ensuite son propre en-tête. Par exemple, elle peut spécifier que le service demandé est le service des noms et téléphones. Elle peut également inclure un numéro séquentiel pour le paquet, afin qu'il puisse être identifié plus tard.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-65.png)
_En-tête de la 4ème couche, avec les données qui incluent l'en-tête de la 5ème couche (Source : [Brief](https://www.youtube.com/watch?v=DBLtFjrTvD0&ab_channel=Brief))_

Par la suite, la quatrième couche transmettra le paquet à la troisième couche. Encore une fois, la troisième couche considérera tout ce qu'elle a reçu – y compris les données elles-mêmes, l'en-tête ajouté par la cinquième couche et l'en-tête ajouté par la quatrième couche – simplement comme un morceau de données. 

Ensuite, la troisième couche ajoutera son propre en-tête. Par exemple, elle peut inclure l'adresse source et l'adresse de destination du paquet.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-66.png)
_En-tête de la 4ème couche, avec les données qui incluent l'en-tête de la 4ème couche et les données (Source : [Brief](https://www.youtube.com/watch?v=DBLtFjrTvD0&ab_channel=Brief))_

Ce processus continue. Ainsi, chaque couche ajoute son propre en-tête au paquet*. Ce processus est appelé **encapsulation**. 

À l'autre extrémité, le récepteur reçoit le paquet et doit lire et supprimer les en-têtes. 

* La deuxième couche peut également inclure un _trailer_ – un morceau supplémentaire de bits suivant les données, avec certaines informations. 

# Mettre tout ensemble

Maintenant que nous avons couvert les cinq couches, prenons un exemple utilisant toutes ensemble. 

Disons que nous souhaitons envoyer un fichier vidéo à notre ami qui vit en France, tandis que nous profitons d'un voyage en Argentine. Pour cela, nous utilisons un service de messagerie. 

La cinquième couche définit comment l'email sera transmis. Par exemple, il inclut l'adresse email de l'expéditeur ainsi que celle du destinataire. Il contient un titre et le corps du message. Il exige que nous suivions un modèle spécifique d'adresse email, qui sera inclus dans l'en-tête de cette couche. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-63.png)
_Le modèle à cinq couches, avec un exemple d'envoi d'un email (Source : [Brief](https://www.youtube.com/watch?v=LYH4DwydVAM&ab_channel=Brief))_

Ensuite, la cinquième couche utilise la quatrième couche afin de diviser l'email en morceaux. Bien sûr, chaque morceau portera également l'en-tête de la quatrième couche. Elle est également utilisée afin de spécifier que nous utilisons actuellement un service de messagerie. 

Dans ce cas, nous voulons définitivement que la connexion soit fiable – afin que le destinataire puisse lire correctement notre fichier vidéo. Ainsi, la quatrième couche gérera également la fiabilité. À l'extrémité du récepteur, elle pourrait envoyer un paquet d'accusé de réception pour chaque paquet qu'elle reçoit. 

La troisième couche définira le meilleur itinéraire pour chaque paquet à envoyer. Elle pourrait choisir différents itinéraires pour différents paquets. Parmi d'autres choses, son en-tête contiendra les adresses source et de destination pour le paquet. 

La deuxième couche sera responsable de chaque lien entre deux appareils directement connectés. Son en-tête inclura les adresses MAC pour chaque appareil. 

La première couche est responsable de l'encodage de tous les uns et zéros, et de les transmettre sur la ligne. Ensuite, de les décoder et de les lire à l'autre extrémité. À ce niveau, nous n'avons pas vraiment d'en-tête, car il se compose uniquement de bits simples. 

De cette manière, chaque couche utilise les services fournis par les couches inférieures, et le énorme problème de transmission de données sur le réseau devient réalisable. N'est-ce pas incroyable ? 

# Résumé

Dans cet article, vous avez appris ce qu'est le modèle à cinq couches et pourquoi nous avons besoin de couches. Vous devriez maintenant comprendre ce dont chaque couche est responsable, et vous pouvez intégrer chaque sujet que vous rencontrez dans les réseaux informatiques dans ce modèle. 

## À propos de l'auteur

[Omer Rosenbaum](https://www.linkedin.com/in/omer-rosenbaum-034a08b9/) est le Chief Technology Officer de [Swimm](https://swimm.io/). Il est l'auteur de la chaîne YouTube [Brief](https://youtube.com/@BriefVid). Il est également un expert en formation cybernétique et fondateur de Checkpoint Security Academy. Il est l'auteur de [Computer Networks (en hébreu)](https://data.cyber.org.il/networks/networks.pdf). Vous pouvez le trouver sur [Twitter](https://twitter.com/Omer_Ros). 

### Références supplémentaires

* [Liste de lecture sur les réseaux informatiques - sur ma chaîne Brief](https://www.youtube.com/playlist?list=PL9lx0DXCC4BMS7dB7vsrKI5wzFyVIk2Kg).
* [Le modèle à sept couches expliqué en anglais simple](https://www.freecodecamp.org/news/osi-model-networking-layers-explained-in-plain-english/)
* [Le modèle TCP/IP – couches et protocole expliqués](https://www.freecodecamp.org/news/what-is-tcp-ip-layers-and-protocols-explained/)