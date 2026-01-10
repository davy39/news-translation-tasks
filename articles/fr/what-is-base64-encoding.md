---
title: Qu'est-ce que le codage base64 et pourquoi est-il nécessaire ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-11-28T18:30:41.000Z'
originalURL: https://freecodecamp.org/news/what-is-base64-encoding
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/cover-base65.jpg
tags:
- name: Base64
  slug: base64
- name: encoding
  slug: encoding
seo_title: Qu'est-ce que le codage base64 et pourquoi est-il nécessaire ?
seo_desc: 'By Sergei Bachinin

  In this article, we''ll thoroughly explore base64 encoding. You''ll learn how it
  came into being and why it''s still so prevalent in modern systems.

  Here''s what we''ll cover:


  What is base64?

  Why use base64?

  When to use base64

  A Case o...'
---

Par Sergei Bachinin

Dans cet article, nous allons explorer en profondeur le codage base64. Vous apprendrez comment il est apparu et pourquoi il est encore si répandu dans les systèmes modernes.

Voici ce que nous allons couvrir :

1. [Qu'est-ce que le base64 ?](#heading-quest-ce-que-le-base64)
2. [Pourquoi utiliser le base64 ?](#heading-pourquoi-utiliser-le-base64)
3. [Quand utiliser le base64](#heading-quand-utiliser-le-base64)
4. [Un cas de SMTP](#heading-un-cas-de-smtp)
5. [Ces limitations sont-elles encore pertinentes aujourd'hui ?](#heading-ces-limitations-sont-elles-encore-pertinentes-aujourdhui)
6. [Comment le base64 aide avec ces limitations](#heading-comment-le-base64-aide-avec-ces-limitations)
7. [Pourquoi seulement 64 caractères ?](#heading-pourquoi-seulement-64-caracteres)
8. [Dois-je utiliser le base64 avec HTTP/1.1 ?](#heading-dois-je-utiliser-le-base64-avec-http11)
9. [Pourquoi le base64 est-il utilisé pour les URLs de données ?](#heading-pourquoi-le-base64-est-il-utilise-pour-les-urls-de-donnees-y-a-t-il-un-codage-plus-efficace-pour-cela)
10. [Conclusion](#heading-conclusion)

## Qu'est-ce que le base64 ?

Base64 est une méthode de transformation de toute donnée en un charabia de chiffres et de lettres. Aujourd'hui, il est largement utilisé et considéré comme acquis. La plupart du temps, vous l'utilisez parce que vous n'avez pas le choix : dans de nombreuses situations, seul un tel charabia de type texte est considéré comme **valide**.

En même temps, le base64 est un outil coûteux. Il augmente la taille des données d'environ 33 % en termes d'utilisation de la mémoire. Ainsi, le base64 est l'une de ces petites choses qui rendent les logiciels **lents**. C'est pourquoi vous ne devez l'utiliser que lorsque c'est absolument nécessaire.

Encore une fois, généralement, vous n'avez pas le choix. Mais parfois, vous en avez un, et c'est pourquoi il peut être utile de comprendre comment il fonctionne et quels problèmes il est censé résoudre.

Cet article s'adresse à ceux qui ont déjà rencontré le base64 dans leur pratique de la programmation et qui se demandent peut-être ce que c'est. Vous tirerez probablement plus de ce guide si vous avez au moins des connaissances de base sur les types de données et une certaine compréhension de la façon dont la mémoire de l'ordinateur est organisée au niveau binaire (bits, octets et tout cela).

L'algorithme de codage du base64 est simple. Il prend en entrée une séquence binaire et produit une autre séquence binaire. Il ne se soucie pas de ce que les octets originaux représentaient – qu'il s'agisse d'une image, d'un PDF ou autre chose. Il parcourt simplement les données binaires originales, les divise en morceaux de 6 bits et convertit chaque morceau en un caractère textuel sûr (ou, strictement parlant, une séquence binaire qui représente un tel caractère). Un caractère "sûr" fait référence à l'un d'un ensemble très limité, que nous discuterons plus tard.

![C'est approximativement comment le texte "Sun" est codé en base64](https://www.freecodecamp.org/news/content/images/2023/11/base64-diagram-smaller-1.png)
_Cette image montre approximativement comment le texte "Sun" est codé en base64_

Ensuite, à un moment donné, vous devez **décoder** ce pseudo-texte pour retrouver les données originales – car le charabia base64 en lui-même est inutile. Le décodage effectue des opérations binaires similaires mais à l'envers. Les données restaurées sont garanties d'être exactement les mêmes qu'avant le codage.

Je ne discuterai pas plus en profondeur de l'algorithme de codage/décodage ici. Wikipedia l'explique en [détail exhaustif](https://en.wikipedia.org/wiki/Base64) si vous souhaitez en savoir plus.

En pratique, vous (en tant que développeur) n'aurez presque jamais à traiter directement avec des données binaires lors du codage de vos données. Au lieu de cela, vous utiliserez des wrappers pratiques disponibles dans presque tous les langages, tels que les fonctions `btoa()` et `atob()` en JavaScript. Vous pouvez en savoir plus à leur sujet [ici](https://www.freecodecamp.org/news/encode-decode-html-base64-using-javascript/).

## Pourquoi utiliser le base64 ?

Quels problèmes le base64 est-il censé résoudre ? Nous avons ici 3 théories principales :

* Le base64 est utilisé parce que certains systèmes sont **limités aux caractères ASCII** mais sont en réalité utilisés pour tous types de données. Le base64 peut "camoufler" ces données en ASCII et ainsi aider ces données à passer la validation.
* Parce que certains systèmes anciens pensent que les données consistent en des morceaux de **7 bits** (octets), tandis que les systèmes modernes utilisent des octets de 8 bits. Cela peut entraîner des incompréhensions entre les systèmes. Et le base64 peut apparemment aider avec cela – mais ce n'est pas si évident.
* Parce que certains caractères peuvent avoir une **signification spéciale** et cela différera d'un système à l'autre. Le base64 résout ce problème en utilisant uniquement les caractères les plus "purement textuels" de l'ensemble ASCII.

De nombreux experts en base64 défendent une théorie et rejettent toutes les autres théories. Il peut sembler que nous devrions pouvoir (ou que nous devons) choisir la bonne dans la liste – mais en réalité, elles sont _toutes correctes_. Eh bien, le "problème des 7 bits" est beaucoup moins un problème aujourd'hui, mais les deux autres sont encore pertinents et le base64 les adresse tous les deux.

## Quand utiliser le base64

Quand devez-vous présenter des données sous forme de charabia base64 ? Dans de nombreuses situations, bien sûr. Mais comprenons le principe principal.

La spécification officielle (RFC4648) indique que le base64 "est utilisé pour **stocker** ou **transférer** des données dans des environnements qui, peut-être pour des raisons de compatibilité, sont limités aux données ASCII".

Ainsi, vous avez besoin de base64 lorsque :

* Des données incompatibles sont **transmises** via le réseau. Tout d'abord, c'est un problème d'e-mails – par exemple, le codage est nécessaire lorsque vous devez joindre une image à un message textuel. C'est la raison pour laquelle le base64 a été introduit.
* Des données incompatibles sont **stockées** dans des fichiers ou ailleurs. Souvent, vous devez intégrer des données non textuelles dans un fichier **textuel** comme JSON, XML ou HTML. Ou pour stocker quelque chose de sophistiqué dans un **cookie** de navigateur (et les cookies doivent être uniquement du texte).

La spécification officielle continue en disant que le base64 permet également :

* "de manipuler des objets avec des **éditeurs de texte**". Apparemment, cela signifie "éditeurs de texte riche" comme Microsoft Word où vous pouvez combiner du texte avec des images et d'autres choses. Ces programmes utilisent-ils le base64 pour le contenu intégré ? C'est possible, mais laissons cela à des chercheurs plus persévérants.

## Un cas de SMTP

SMTP est un ancien protocole d'e-mail encore répandu aujourd'hui et utilisé par Gmail, Outlook, et autres. Il définit comment les messages électroniques doivent être transmis entre les serveurs. Les règles SMTP originales étaient vraiment strictes, et à la fin des années 80, elles étaient déjà une grande nuisance.

Tout d'abord, SMTP n'autorisait que le texte brut en langue anglaise (qui se compose de seulement 128 caractères connus sous le nom d'ASCII). Ainsi, des solutions de contournement étaient nécessaires pour envoyer à la fois du texte non anglais et des pièces jointes non textuelles.

![Les serveurs de messagerie pouvaient communiquer uniquement en utilisant du texte anglais](https://www.freecodecamp.org/news/content/images/2023/11/email-sending.png)
_Diagramme montrant un e-mail passant entre deux personnes via des serveurs utilisant uniquement du texte anglais_

Base64 a résolu ce problème en convertissant toutes les données en "texte anglais sûr". Cette conversion n'est nécessaire que pour le moment, et lorsque le danger est passé, les données sont reconverties en format normal.

C'est essentiellement une pratique très laide qui ressemble quelque peu à de la contrebande. Les données sont obfusquées (bien, vraiment) afin de tromper un système qui n'autorise pas ce type de données.

Et d'ailleurs, les restrictions de SMTP étaient destinées à la **sécurité** en premier lieu. Mais c'était il y a longtemps et aujourd'hui personne n'a plus besoin de cette sécurité. Au lieu de cela, tout le monde a besoin d'un canal discret pour transporter n'importe quoi. Ainsi, les anciennes règles agissent comme une bureaucratie ennuyeuse. Mais c'est ce que sont les systèmes hérités et vous devez vivre avec eux.

## Ces limitations sont-elles encore pertinentes aujourd'hui ?

Oui, malgré toutes les extensions et astuces.

De nombreuses restrictions de SMTP sont assouplies grâce à diverses extensions. Par exemple, l'extension "8BIT MIME" vous permet d'envoyer des messages électroniques en octets de 8 bits et en caractères autres que l'ASCII. Ainsi, en théorie, aujourd'hui vous pouvez envoyer une lettre avec une pièce jointe sans codage.

Mais en pratique, il est encore impossible d'ignorer les anciennes restrictions. Parce qu'il existe des serveurs de messagerie obsolètes qui n'ont pas adopté les nouvelles extensions. Et vous devez être capable de communiquer avec eux même si votre propre serveur de messagerie prend en charge toutes les fonctionnalités modernes.

Avant d'envoyer un message à un certain serveur de messagerie, vous demandez d'abord quel type de règles SMTP il prend en charge. Implémente-t-il une extension 8BIT MIME ? Si ce n'est pas le cas, vous devrez convertir votre message au format ancien.

## Comment le base64 aide avec ces limitations

Il est évident que le base64 doit être une solution au problème "ASCII uniquement" car il transforme tout en caractères ASCII. Mais cela devient moins évident lorsque vous le combinez avec le problème des "**7 bits**". Parce que, peu importe le type de caractères que vous utilisez, ils doivent être d'une manière ou d'une autre transmissibles par des canaux de 7 bits et de 8 bits, selon la situation.

Les experts disent généralement quelque chose comme :

> "Base64 transforme la séquence binaire 01001101 01100001 01101110 _(quoi que cela signifie)_ en texte "TWFu".

De telles déclarations peuvent vous amener à penser que quelque chose de binaire devient non binaire. En fait, tous les caractères ASCII produits par base64 sont finalement des bits et des octets, tout comme les données originales. (Mais bien sûr, la quantité et l'ordre des bits changent).

Voici une commande bash pour obtenir une représentation binaire d'une chaîne :

```bash
echo -n "TWFu" | xxd -b
```

Elle vous dira que "TWFu" est en réalité "`01010100 01010111 01000110 01110101`". Mais si chaque caractère fait 8 bits de long, un canal de 7 bits peut ne pas reconnaître ce TWFu comme du texte. Apparemment, une manipulation binaire supplémentaire doit avoir lieu pour que cela fonctionne pour tous les canaux.

Heureusement, avec les caractères ASCII, cette manipulation binaire est facile. Parce que pour stocker un caractère ASCII en mémoire, vous avez en réalité besoin de seulement 7 bits. Ils peuvent être étendus à 8 bits uniquement si vous avez besoin d'un "octet" conventionnel. Cela se fait simplement en ajoutant un bit "0" devant les sept originaux. Par exemple, "T" peut être stocké à la fois comme `1010100` et `01010100`.

Ainsi, la conversion entre les caractères ASCII de 7 bits et de 8 bits est une question d'ajout/suppression du bit "0" le plus à gauche. Apparemment, les serveurs de messagerie doivent effectuer ce genre de choses lorsqu'ils communiquent entre eux.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/T-1.png)
_Cette image montre comment un caractère "T" produit par base64 peut être consommé par des canaux de 7 et 8 bits_

Ainsi, gardons à l'esprit que le base64 en lui-même ne résout pas le problème des "7 bits". Il produit simplement des caractères ASCII et cela permet une conversion rapide entre 7 et 8 bits. Mais cette conversion est de la responsabilité d'un système plus large, tel que MIME (extension de SMTP).

### Le coût de la mémoire dépend de la longueur des octets

D'ailleurs, si vous utilisez seulement 7 bits par caractère, alors le base64 doit être moins gaspilleur en termes d'utilisation de la mémoire.

La théorie principale est que le base64 provoque un surcoût de mémoire de 33 % (ou 37 % ou autre chose). Mais il semble être correct uniquement pour un scénario de 8 bits.

Parce que, comme je l'ai expliqué précédemment, le base64 convertit chaque morceau de 6 bits des données originales en un seul caractère ASCII. Si un tel caractère fait 8 bits de long, cela signifie que vous gaspillez 2 bits pour chaque morceau original, ce qui représente environ 33 %, comme promis par les experts. Mais avec des caractères de 7 bits, cette perte doit être environ deux fois moins importante.

## Pourquoi seulement 64 caractères ?

Le base64 serait excessif s'il était fait uniquement pour contourner la restriction ASCII.

L'ASCII compte 128 caractères, et si vous pouviez tous les utiliser, l'algorithme de codage serait plus efficace en termes de mémoire. C'est fastidieux à expliquer, mais en bref, avec un alphabet de 128 caractères, un seul caractère pourrait représenter 7 (au lieu de seulement 6) bits des données originales.

Mais les auteurs du base64 ont décidé d'utiliser seulement _la moitié_ des caractères ASCII, et sûrement ils avaient une très bonne raison pour cela.

Les caractères peuvent être incorrects (non sûrs) pour au moins deux raisons :

1. Ils peuvent être **invalides** (interdits par un système, comme SMTP interdit tout ce qui est au-delà de l'ASCII)
2. Ils peuvent être valides _mais_ reconnus par erreur comme un **caractère spécial**

Dans l'ASCII, il y a 30+ "caractères de contrôle". Ils ne sont **pas imprimables** et sont destinés à provoquer d'autres effets. Par exemple : "saut de ligne", "retour arrière", "supprimer", "échapper". Beaucoup de ces commandes sont un héritage de certains dispositifs préhistoriques comme les télétypes.

![Caractères ASCII non imprimables](https://www.freecodecamp.org/news/content/images/2023/11/ascii-control-chars.png)
_Tableau montrant 34 caractères non imprimables de l'ensemble ASCII_

Apparemment, vous devez exclure tous les caractères non imprimables de l'alphabet de codage. Vous êtes donc laissé avec environ 90+ caractères imprimables. Mais imprimable ne signifie pas sûr et fiable. Ils peuvent également avoir une **signification spéciale** dans différents systèmes. Et un certain nombre d'entre eux ont une signification spéciale dans SMTP, par exemple "@", "<", et ">". Ils produiront sûrement "d'autres effets" et cela ne vous rendra pas heureux.

Ainsi, cela s'est terminé avec 64 caractères – tout d'abord, parce que 64 est plus facile à gérer algorithmiquement. Et cela ressemble à un alphabet vraiment sûr qui peut être utilisé dans une large gamme de systèmes, pas seulement SMTP.

Malheureusement, ce n'est pas complètement sûr. Il n'y a que **62** caractères qui sont garantis de ne pas avoir de signification spéciale dans tous les systèmes. Ce sont les chiffres, les lettres minuscules anglaises et les lettres majuscules anglaises. Vous avez besoin de **2 caractères supplémentaires** pour le base64. Et leur choix diffère d'un système à l'autre.

Les candidats les plus populaires sont "+" et "/" mais dans certaines situations, ils casseront des choses. Par exemple, ils ont une signification spéciale dans les URLs. C'est pourquoi nous avons une variante "base64url" où les deux derniers caractères sont "_" et "-".

### Le base64 ne résout pas le problème des caractères spéciaux "ambigus"

Ici, j'aimerais brièvement expliquer une idée fausse qui apparaît souvent dans diverses discussions sur le base64.

Certains caractères spéciaux sont traités différemment par différents systèmes. Les plus notoires d'entre eux sont "saut de ligne" et "retour chariot". Tous deux concernent les sauts de ligne. Mais différents systèmes ont des opinions différentes sur la façon de combiner ces deux caractères pour produire un saut de ligne réel.

Il existe une croyance répandue que le base64 aide d'une manière ou d'une autre à réconcilier ces différences.

Mais le base64 n'a rien à voir avec la façon dont les données sont **interprétées** – par exemple, comment le texte est affiché à l'écran. Parce que pour afficher quelque chose, vous devez d'abord le **décoder** du base64 vers sa forme originale. Les données décodées seront exactement les mêmes qu'avant le codage. Ce sera la même séquence de bits avec les mêmes caractères ambigus qu'avant.

Ainsi, encore une fois, le base64 ne peut que **cacher** les caractères spéciaux pour le moment. Il ne nettoie pas magiquement les données des caractères dangereux.

## Dois-je utiliser le base64 avec HTTP/1.1 ?

HTTP/1.1 est un protocole basé sur du texte. Vous pouvez donc vous demander si les données non textuelles doivent être codées pour transmettre des choses sur Internet.

(Aussi, appelons-le simplement HTTP. Gardez à l'esprit que HTTP/2 et /3 sont des protocoles binaires, donc ils ne sont pas en question).

HTTP permet en réalité **tous** les types de données dans le **corps** d'un message. Le corps n'est pas limité aux caractères textuels. Ainsi, par exemple, une image peut être envoyée dans sa forme originale, sans mélanger ses bits et octets.

Ce qui est vraiment "basé sur du texte" dans HTTP, ce sont les **en-têtes**. En gros, ils sont limités à l'ASCII (ce n'est pas exactement vrai, mais c'est une bonne pratique d'utiliser uniquement l'ASCII).

Aujourd'hui, les en-têtes HTTP sont utilisés de nombreuses manières différentes – et parfois ils doivent également transporter des choses non ASCII.

Par exemple, un schéma d'authentification HTTP de base suggère que vous envoyez le nom d'utilisateur et le mot de passe dans le cadre de l'en-tête "Authentication". Le nom d'utilisateur et le mot de passe peuvent contenir beaucoup de choses incompatibles, vous devez donc les coder en caractères textuels sûrs. Le base64 est recommandé dans de tels cas. Pour cette raison, certains développeurs pensent que le base64 est une sorte de cryptage (protection des données) ce qui n'est pas vrai.

## Pourquoi le base64 est-il utilisé pour les URLs de données ? Y a-t-il un codage plus efficace pour cela ?

Les URLs de données sont probablement l'utilisation la plus connue du base64 aujourd'hui. C'est une façon d'inclure divers actifs comme des images (non pas des liens vers elles mais leur code réel) dans des fichiers HTML ou CSS.

Notez que les URLs de données n'ont rien à voir avec la transmission de données. Le base64 est utilisé ici non pas parce que le protocole HTTP interdit toute séquence binaire. Lorsque vous envoyez un fichier HTML ou CSS sur le réseau, HTTP ne se soucie pas de ce qu'il y a dans ces fichiers. Mais les fichiers HTML et CSS doivent être uniquement du texte pour être correctement interprétés (affichés) par les éditeurs de texte et les navigateurs.

Cela a du sens, mais c'est quand même dommage – car, encore une fois, le base64 est coûteux. Ce surcoût de mémoire notoire de 33 % ou 37 % est particulièrement ennuyeux avec les URLs de données. Dans la plupart des cas, cela défait entièrement leur objectif.

L'objectif est bien sûr d'améliorer les **performances**. Vous obtenez une image sans une requête HTTP supplémentaire et économisez ainsi quelques millisecondes. Mais ce gain de performance est faible et facilement annulé par les octets supplémentaires créés par le base64.

Alors pourquoi le base64 est-il utilisé pour les URLs de données ? Pourrions-nous utiliser un codage moins gaspilleur pour cela (c'est-à-dire un codage qui utilise un alphabet plus large et produit ainsi des chaînes de caractères plus courtes) ?

Actuellement, c'est très peu probable, car les navigateurs n'autorisent que les **caractères sûrs pour les URLs** dans les URLs de données. Et il n'y a pas trop de caractères sûrs pour les URLs – juste un peu plus que 64. Pourquoi sommes-nous limités aux caractères sûrs pour les URLs ? Parce que nous insérons les données codées dans des endroits où les navigateurs attendent une URL.

En théorie, les navigateurs pourraient être plus intelligents et assouplir cette limitation lorsque cela est nécessaire. Posons donc une question plus large ensuite.

### Existe-t-il un meilleur codage pour les données non textuelles en HTML ?

Sur le plan technique, les URLs de données ne sont **pas le seul moyen** d'intégrer des données non textuelles dans des fichiers HTML.

Vous pouvez créer vos propres solutions où les données non textuelles sont insérées ailleurs dans le balisage HTML (attributs, innerText, ou autre chose). Dans de tels cas, vous n'êtes pas limité à un alphabet sûr pour les URLs. Ainsi, en théorie, vous pouvez utiliser n'importe quels caractères autorisés en HTML.

La plupart des fichiers HTML utilisent l'ensemble de caractères UTF-8. Il contient **tous les caractères Unicode**, et il y en a plus d'un million. Il doit donc être possible de créer un codage baseNNN où au moins 256 caractères Unicode seront utilisés. Un tel codage n'aurait aucun (ou presque aucun) surcoût de mémoire.

En pratique, tout est beaucoup plus compliqué.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/chars-3.png)
_Diagramme montrant combien de caractères de l'UTF-8 sont "vraiment sûrs" et utilisables pour un codage baseNNN hypothétique_

Pourquoi ne pas coder des choses avec des caractères chinois, par exemple ? Parce qu'ils sont trop lourds. Ils prennent 3 ou même 4 octets de mémoire. C'est ainsi que fonctionne le codage UTF-8 – il utilise un nombre différent d'octets pour différents caractères. Et nous ne nous intéressons qu'à ceux qui prennent **1 octet**.

(Vous pouvez envisager d'utiliser des caractères multi-octets pour notre codage baseNNN, mais n'entrons pas dans cela. Vous n'avez besoin que de ceux à 1 octet – prenons cela comme un axiome.)

Combien y a-t-il de caractères à 1 octet dans l'UTF-8 ? Seulement 128, et c'est la **bonne vieille plage ASCII**. Pouvez-vous tous les prendre ? Non, car, encore une fois, vous n'avez besoin que de caractères imprimables. Vous devez vraiment les voir dans les éditeurs de texte et les outils de développement et ailleurs.

Ensuite, tout comme dans le cas de SMTP, vous devez exclure un certain nombre de caractères visibles parce qu'ils ont une signification spéciale en HTML. Par exemple, les guillemets doubles (") ne fonctionneront pas car ils peuvent terminer prématurément la chaîne de l'URL de données. Cela ne fonctionnera pas :

`<img src="data:image/png;base64,iVBOR"w0KAA" />`

Ainsi, un alphabet possible se réduit à nouveau à 80-90 caractères. Cela permet, en théorie, de créer un autre codage qui utilisera un peu moins de mémoire que le base64.

De tels codages existent en réalité, par exemple le **base85** créé par Adobe. Il est plus efficace en termes de mémoire car il code 4 octets de données originales en 5 caractères. Mais le base85 est également beaucoup plus lent à calculer, donc ses avantages globaux sont minimes, s'il y en a. Et d'ailleurs, il n'est pas destiné au développement web et contient des caractères qui peuvent casser des choses en HTML et CSS. (Bien qu'il doive être possible de construire un algorithme similaire mais compatible avec le web en échangeant certains caractères.)

Pouvons-nous trouver un meilleur baseNNN pour d'autres types de fichiers texte (JSON, XML, etc.) ? Cela semble peu probable, car ces formats sont principalement codés en UTF-8 et cela signifie à peu près les mêmes limitations que dans le cas de HTML. Seule la quantité de caractères imprimables spéciaux peut différer (elle est très petite en JSON par exemple) mais ce n'est pas un gros problème.

## Conclusion

Le base64 a été introduit pour la première fois comme un moyen de contourner un certain nombre de restrictions archaïques imposées aux messages électroniques par le protocole SMTP.

Le base64 nous a permis de camoufler toute donnée en texte afin de passer la validation lors de la transmission entre les serveurs de messagerie. Il a également garanti que ce pseudo-texte ne contenait que des caractères sûrs, c'est-à-dire 1) uniquement des caractères imprimables et 2) uniquement ceux qui n'ont pas de signification spéciale dans SMTP et (espérons-le) dans la plupart des autres systèmes.

L'alphabet final s'est avéré être vraiment étroit, et il nous a permis d'utiliser le base64 pratiquement partout (mais dans des variantes légèrement différentes). Il aide dans de nombreux cas où vous devez mélanger des données textuelles et non textuelles.

Les systèmes modernes utilisent également le base64 malgré son coût mémoire significatif. À première vue, cette pratique semble étrange, car les systèmes modernes n'ont pas ces restrictions archaïques que SMTP avait. Mais il s'avère que dans la plupart des cas, vous avez encore très peu de caractères bon marché et non spéciaux, et les alternatives potentielles au base64 offrent des avantages très faibles.