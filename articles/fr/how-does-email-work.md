---
title: Comment fonctionne l'email ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-30T18:56:00.000Z'
originalURL: https://freecodecamp.org/news/how-does-email-work
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99f2740569d1a4ca229b.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: email
  slug: email
- name: information security
  slug: information-security
- name: technology
  slug: technology
- name: Web Security
  slug: web-security
seo_title: Comment fonctionne l'email ?
seo_desc: "By Megan Kaczanowski\nFirst, you use a mail user agent, or MUA to read\
  \ and send email from your device (such as gmail, or the mail app on Apple devices).\
  \ These programs are only active when you're using them. \nGenerally, they communicate\
  \ with a mail t..."
---

Par Megan Kaczanowski

Tout d'abord, vous utilisez un agent utilisateur de messagerie, ou MUA, pour lire et envoyer des emails depuis votre appareil (comme Gmail, ou l'application de messagerie sur les appareils Apple). Ces programmes ne sont actifs que lorsque vous les utilisez. 

Généralement, ils communiquent avec un agent de transfert de messagerie, ou MTA (également connu sous le nom de serveur de messagerie, hôte MX et échangeur de messagerie), qui sert à recevoir et à stocker vos emails. 

Les emails sont stockés à distance jusqu'à ce que vous ouvriez votre MUA pour vérifier vos emails. Les emails sont livrés par des agents de distribution de messagerie (MDA), qui sont généralement inclus avec le MTA.

Les emails étaient autrefois envoyés à un serveur de messagerie en utilisant SMTP, ou Simple Mail Transfer Protocol. SMTP est un protocole de communication pour l'email. 

Même aujourd'hui, alors que de nombreux systèmes propriétaires comme Microsoft Exchange et des programmes de webmail comme Gmail utilisent leurs propres protocoles en interne, ils utilisent SMTP pour transférer des messages en dehors de leurs systèmes (par exemple, si un utilisateur Gmail souhaite envoyer un email à un client Outlook).

Les emails étaient ensuite téléchargés depuis le serveur en utilisant le protocole Post Office Protocol (POP3). POP3 est un protocole de couche application qui fournit un accès via un réseau de protocole internet (IP) pour qu'une application utilisateur contacte une boîte aux lettres sur un serveur de messagerie. Il peut se connecter, récupérer des messages, les stocker sur l'ordinateur du client, et les supprimer ou les conserver sur le serveur. 

Il a été conçu pour pouvoir gérer des connexions internet temporaires, comme le dial-up (il se connectait et récupérait les emails lorsqu'il était connecté, et vous permettait de consulter les messages lorsque vous étiez hors ligne). Cela était plus populaire lorsque l'accès dial-up était plus répandu.

Aujourd'hui, IMAP, Internet Message Access Protocol, a principalement remplacé POP3. IMAP permet à plusieurs clients de gérer la même boîte aux lettres (vous pouvez donc lire vos emails depuis votre ordinateur de bureau, votre ordinateur portable et votre téléphone, etc., et tous vos messages y seront, organisés de la même manière). 

Enfin, le webmail a remplacé les deux. Le webmail vous permet de vous connecter à un site web et de recevoir des messages de n'importe où ou sur n'importe quel appareil (youpi !), mais vous devez être connecté à internet pour l'utiliser. Si le site web (comme Gmail) est votre MUA, vous n'avez pas besoin de connaître les paramètres du serveur SMTP ou IMAP.

## Comment l'email est-il sécurisé ?

Malheureusement, la sécurité n'a pas vraiment été intégrée aux protocoles de messagerie dès le début (comme la plupart des protocoles internet initiaux). Les serveurs s'attendaient simplement à prendre n'importe quel message de n'importe qui et à le transmettre à n'importe quel autre serveur qui pourrait aider à acheminer le message vers sa destination finale (le destinataire dans le champ to:). 

Sans surprise, cela est devenu un problème lorsque l'internet s'est étendu d'un petit groupe de gouvernements et de groupes de recherche à quelque chose que la plupart du monde utilise pour faire essentiellement tout. Très vite, les emails de spam et de phishing sont devenus (et restent) un énorme problème pour tout le monde. 

En réponse, nous avons collectivement essayé de mettre en place plusieurs mesures qui empêchent les gens de lire les messages des autres (chiffrement) et valident que les messages proviennent réellement de l'expéditeur prétendu (authentification).  

La plupart des endroits utilisent TLS (transport layer security, le remplacement de SSL, secure sockets layer), un protocole cryptographique qui fournit un chiffrement en transit. Il offre une protection lorsque le message est transmis, mais pas lorsque les données sont au repos (par exemple, stockées sur votre ordinateur). 

Cela garantit qu'un message n'est pas altéré ou espionné pendant qu'il voyage de MTA à MTA. Cependant, cela ne vérifie pas que le message n'a pas été modifié pendant le trajet. 

Par exemple, si l'email passe par plusieurs serveurs de messagerie avant d'atteindre sa destination finale, l'utilisation de TLS garantira qu'il est chiffré entre les serveurs, mais chaque serveur pourrait altérer le contenu du message. Pour remédier à cela, nous avons créé SPF, DKIM et DMARC.

## SPF (Sender Policy Framework) 

SPF permet au propriétaire d'un domaine (comme google.com) de définir un enregistrement TXT dans son DNS qui indique quels serveurs sont autorisés à envoyer des emails depuis ce domaine (pour des instructions sur la façon de faire cela pour une variété de fournisseurs d'hébergement, consultez [ce site](https://support.knowbe4.com/hc/en-us/articles/115015835387-How-Can-I-Add-a-TXT-Record-to-My-DNS-Records-)).

### Comment cela fonctionne-t-il ?

Cet enregistrement liste les appareils (généralement par IP) qui sont autorisés et peut se terminer par l'une des options suivantes : 

-all = Si la vérification échoue (la source de l'email n'est pas l'un des appareils listés), le résultat est un HardFail. La plupart des systèmes de messagerie marqueront ces messages comme spam.

?all = Si la vérification échoue (la source de l'email n'est pas l'un des appareils listés), le résultat est neutre. Cela est généralement utilisé pour les tests, pas pour les domaines de production.

~all = Si la vérification échoue (la source de l'email n'est pas l'un des appareils listés), le résultat est un SoftFail. Cela signifie que ce message est suspect, mais n'est pas nécessairement un mauvais connu. Certains systèmes de messagerie marqueront ces messages comme spam, mais la plupart ne le feront pas.

Les en-têtes SPF peuvent être utiles aux serveurs eux-mêmes, lorsqu'ils traitent les messages. Par exemple, si un serveur est à la périphérie d'un réseau, il sait que les messages qu'il reçoit doivent provenir de serveurs dans l'enregistrement SPF de l'expéditeur. Cela aide les serveurs à se débarrasser du spam plus rapidement. Bien que cela semble génial, malheureusement, il y a quelques problèmes majeurs avec SPF. 

1. SPF ne dit pas à un serveur de messagerie quoi faire avec le message - ce qui signifie qu'un message peut échouer à une vérification SPF et être tout de même livré. 
2. Un enregistrement SPF ne regarde pas l'adresse 'from' que l'utilisateur voit, il regarde le 'return-path'. Cela équivaut essentiellement à l'adresse de retour que vous écrivez sur une lettre. Il indique aux serveurs de messagerie qui traitent la lettre où retourner le message (et il est stocké dans les en-têtes de l'email - essentiellement des informations techniques que les serveurs utilisent pour traiter les emails).   
Cela signifie que je peux mettre ce que je veux dans l'adresse from: et cela n'affectera pas la vérification SPF. En fait, les deux adresses email peuvent être relativement usurpées par un pirate. Parce qu'il n'y a pas de chiffrement impliqué, les en-têtes SPF ne peuvent pas être entièrement fiables. 
3. Les enregistrements SPF doivent être constamment mis à jour, ce qui peut être difficile dans les grandes organisations en constante évolution.
4. La redirection brise SPF. Cela est dû au fait que si un email de, par exemple google.com, est redirigé par bob@bobsburgers.com, l'expéditeur de l'enveloppe reste inchangé (l'adresse from indique toujours google.com). Le serveur de messagerie récepteur pense qu'il prétend provenir de google.com, mais provient de bobsburgers.com, donc il échoue à la vérification SPF (même si le message provient réellement de google.com). 

Pour plus de lectures sur SPF, consultez ces [articles](https://postmarkapp.com/guides/spf) et [articles](http://knowledge.ondmarc.com/en/articles/1148885-spf-hard-fail-vs-spf-soft-fail). Vous pouvez vérifier si un domaine spécifique dispose d'enregistrements SPF et DMARC configurés [ici.](https://domain-checker.valimail.com/google.com)

## DKIM (DomainKeys Identified Mail)

DKIM est similaire à SPF. Il utilise également des enregistrements TXT dans le DNS du domaine expéditeur et fournit une certaine authentification du message lui-même. Il tente de fournir une vérification que les messages n'ont pas été altérés en transit. 

### Comment cela fonctionne-t-il ?

Le domaine expéditeur génère une paire de clés publique/privée et place la clé publique dans l'enregistrement TXT DNS du domaine (si vous ne savez pas ce qu'est une paire de clés publique/privée, consultez [cet article](https://www.freecodecamp.org/news/how-to-send-secret-messages/) sur la cryptographie). 

Ensuite, les serveurs de messagerie du domaine (sur la frontière extérieure - les serveurs qui envoient des emails en dehors du domaine (ex. de gmail.com à outlook.com)) utilisent la clé privée pour générer une signature de l'ensemble du corps du message, y compris les en-têtes. 

La génération d'une signature nécessite généralement que le texte soit haché et chiffré (pour plus de détails sur ce processus, consultez [cet article](https://www.freecodecamp.org/news/understanding-encryption-algorithms/)). 

Les serveurs de messagerie récepteurs utilisent la clé publique dans l'enregistrement TXT DNS pour déchiffrer la signature, puis hachent le message et les en-têtes pertinents (tous les en-têtes qui ont été créés alors que le message était à l'intérieur de l'infrastructure de l'expéditeur - par exemple, si plusieurs serveurs Gmail ont traité l'email avant qu'il ne soit envoyé en externe à outlook.com). 

Le serveur vérifiera ensuite que les deux hachages correspondent. Si c'est le cas, le message est probablement non altéré (sauf si quelqu'un a compromis la clé privée de l'expéditeur) et provient légitimement de l'expéditeur prétendu. Si les hachages ne correspondent pas, le message n'était soit pas de l'expéditeur prétendu, soit il a été altéré par un autre serveur en transit, soit les deux.

DKIM fait un très bon travail pour une tâche très spécifique - répondre à la question 'cet email a-t-il été altéré en transit ou n'est-il pas de l'expéditeur prétendu ?'. Cependant, c'est tout ce qu'il fait. Il ne vous dit pas comment traiter les emails qui échouent à ce test, quel serveur a pu altérer le message, ou quelles altérations ont été faites.  

DKIM est également utilisé par certains FAI, ou Fournisseurs d'Accès à Internet, pour déterminer la réputation de votre domaine (envoyez-vous beaucoup de spam ? Avez-vous un faible engagement ? À quelle fréquence vos emails rebondissent-ils ?).

Pour plus de lectures sur DKIM, consultez cet [article](https://postmarkapp.com/guides/dkim). Vous pouvez valider un enregistrement DKIM [ici](https://www.dmarcanalyzer.com/how-to-validate-a-domainkey-dkim-record/).

## DMARC (Domain-Based Message Authentication, Reporting, and Conformance)

DMARC est essentiellement des instructions pour les serveurs de messagerie sur la façon de gérer les enregistrements SPF et DKIM. Il ne effectue aucun test lui-même, mais il indique aux serveurs de messagerie comment gérer les vérifications effectuées par SPF et DKIM.

Les FAI participants examineront les enregistrements DMARC publiés et les utiliseront pour déterminer comment traiter les échecs DKIM ou SPF. Par exemple, une marque souvent usurpée pourrait publier un enregistrement DMARC qui indique que si DKIM ou SPF échouent, le message doit être rejeté. 

Souvent, les FAI enverront également des rapports sur l'activité de votre domaine avec la source de l'email et s'il a réussi/échoué DKIM/SPF. Cela signifie que vous pourrez voir lorsque des personnes usurpent (prétendent envoyer depuis) votre domaine ou altèrent vos messages.

Pour mettre en œuvre DMARC, vous devez créer un enregistrement DMARC, en fonction de vos besoins (de la surveillance de votre trafic email pour déterminer toutes vos sources d'email à la demande d'actions, comme le rejet de tout email qui échoue à DKIM ou SPF). Vous pouvez en apprendre plus sur la façon de faire cela [ici](https://blog.returnpath.com/build-your-dmarc-record-in-15-minutes-v2/) et [ici](https://blog.returnpath.com/demystifying-the-dmarc-record/).

Pour plus de lectures sur DMARC, consultez [cet article](https://postmarkapp.com/guides/dmarc). Vous pouvez vérifier si un domaine spécifique dispose d'enregistrements SPF et DMARC configurés [ici.](https://domain-checker.valimail.com/google.com)

## Conclusion

Aucune de ces mesures de sécurité n'est parfaite, mais ensemble, elles font un travail décent pour nous aider à améliorer la sécurité des systèmes de messagerie dans le monde entier. 

Plus les organisations adoptent ces mesures (soit en utilisant des implémentations open source, soit en payant pour un produit), mieux tout le monde se portera. La sécurité ajoutée après qu'un protocole ou un produit a été développé est généralement plus coûteuse, moins efficace et plus difficile à mettre en œuvre que la sécurité intégrée au produit. 

Cependant, la plupart des protocoles sur lesquels l'internet actuel repose ont été conçus pour le début de l'internet - pour un petit groupe d'enthousiastes, de scientifiques et de représentants du gouvernement - et non pour un réseau mondial sur lequel nous gérons des bâtiments, des appareils intelligents, les transports publics, les centrales nucléaires (!), et bien plus encore. 

Ainsi, à mesure que l'internet continue de s'étendre, nous devons continuer à nous adapter et à développer de nouvelles façons de sécuriser les systèmes dont nous dépendons.