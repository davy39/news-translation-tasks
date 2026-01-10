---
title: Comment rester conforme au RGPD avec les journaux d'accès
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-08T16:24:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-stay-gdpr-compliant-with-access-logs
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/privacy.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: '#gdpr'
  slug: gdpr
- name: privacy
  slug: privacy
seo_title: Comment rester conforme au RGPD avec les journaux d'accès
seo_desc: 'By Yuli Stremovsky

  Privacy is a complicated topic. A well-known method used to save application logs
  turned out to be tricky with the new privacy regulations. In fact, new regulations
  define an IP address as a personal identifier. Like other user ide...'
---

Par Yuli Stremovsky

La confidentialité est un sujet compliqué. Une méthode bien connue utilisée pour sauvegarder les journaux d'application s'est avérée délicate avec les nouvelles réglementations sur la confidentialité. En fait, les nouvelles réglementations définissent une adresse IP comme un identifiant personnel. Comme les autres identifiants utilisateur, elle doit être traitée avec prudence.

Dans cet article, je vais aborder quelques méthodes pour rendre vos journaux respectueux de la confidentialité. 

Tout d'abord, je vais vous enseigner les termes de base du **RGPD** : **PII** et **droit de l'utilisateur à l'oubli**. Ensuite, nous aborderons les méthodes pour rendre les journaux des serveurs web ou d'applications conformes au RGPD. 

Ensuite, je parlerai d'un produit open-source que je développe appelé **[Databunker](http://databunker.org/)** et comment il aide. **Databunker** est un outil multifonction pour stocker des enregistrements personnels.

## Quelques termes liés au RGPD

### Qu'est-ce que l'information personnellement identifiable ?

Le RGPD définit le concept de **PII** ou **Information Personnellement Identifiable**. Cela peut être toute information qui aide à identifier une personne. 

Par exemple, cela peut être un nom d'utilisateur, une adresse, un numéro de téléphone, une adresse e-mail ou un numéro de sécurité sociale. Cela peut aussi être une identité faible, comme les informations du navigateur, l'adresse IP, le nom du cookie de session. 

Comme dans la triangulation, une combinaison d'identités faibles peut nous mener à un utilisateur. Les identités fortes et faibles des utilisateurs sont toutes considérées comme des **PII**.

Le **RGPD** introduit le droit pour les individus de faire effacer leurs données personnelles. Votre utilisateur ou client peut vous envoyer un e-mail vous demandant de supprimer ses enregistrements. Vous avez un mois pour répondre à cette demande.

### Que signifie une demande d'oubli pour les fichiers journaux ?

Supprimer les données utilisateur de la base de données est facile. Vous avez SQL pour cela. Supprimer les PII de l'utilisateur du fichier journal est la partie délicate. 

Vous pouvez avoir différents serveurs générant des journaux et vous pouvez alimenter des journaux vers différents services cloud. Cela peut compliquer la manière dont vous effectuez la suppression des enregistrements. 

Dans cet article, je vais aborder des méthodes plus intelligentes pour rendre vos journaux conformes à la confidentialité.

### Introduction à Databunker

Mais d'abord, laissez-moi vous donner un peu plus d'informations sur ce qu'est **Databunker** et comment il fonctionne puisque nous allons en discuter dans certaines de ces méthodes ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/databunker-solution.png)

**Databunker** est un service de stockage d'utilisateurs conforme au RGPD pour les applications Web et mobiles. Il fonctionne comme un service d'application backend. Ce produit est une combinaison de plusieurs concepts logiciels fusionnés ensemble. Il fournit un stockage sécurisé des PII et une confidentialité par conception dès la sortie de la boîte :

* Un stockage et un coffre-fort d'informations personnellement identifiables (PII)
* Un stockage sécurisé de session pour les applications web
* Un portail de confidentialité pour les clients
* Un serveur backend d'application
* Un outil de gestion du DPO
* Un service de tokenisation
* Une sauce secrète

Site web du projet : [https://databunker.org/](https://databunker.org/)

Un exemple complet fonctionnel avec Node.js et Passport.js est disponible ici : [https://github.com/securitybunker/databunker-nodejs-example](https://github.com/securitybunker/databunker-nodejs-example)

## Méthode 1 : Utiliser une période de conservation automatique des journaux

Vous avez **un mois** pour répondre à une **demande d'oubli de l'utilisateur**. Cela signifie en fait que vous avez un mois pour filtrer vos fichiers journaux de tous les enregistrements liés à l'utilisateur – par exemple, filtrer les adresses IP des utilisateurs. 

Ou vous pouvez limiter la période de conservation des journaux à un mois. Toutes les entrées de journal plus anciennes seront supprimées. Ainsi, vous n'avez rien à faire d'autre qu'une configuration unique de la période de conservation des journaux.

## Méthode 2 : Utiliser la pseudonymisation pour résoudre les problèmes de conformité des journaux

Le RGPD discute du concept de **pseudonymisation**. Cette méthode sera basée sur l'utilisation du terme pseudonymisation. Selon l'[Article 4(5) du RGPD](https://gdpr-info.eu/art-4-gdpr/) :

> _La « pseudonymisation » signifie le traitement de données personnelles de telle manière que les données personnelles ne puissent plus être attribuées à une personne concernée spécifique sans l'utilisation d'informations supplémentaires, à condition que ces informations supplémentaires soient conservées séparément et soient soumises à des mesures techniques et organisationnelles pour garantir que les données personnelles ne soient pas attribuées à une personne physique identifiée ou identifiable..._

Vous pouvez conserver les données personnelles dans une base de données séparée, par exemple dans **Databunker**. Lorsque vous recevez une **demande d'oubli de l'utilisateur**, vous supprimerez les données personnelles de l'utilisateur de **Databunker**, **en laissant les fichiers journaux inchangés**.

Pour faciliter encore plus notre vie, nous pouvons imprimer un token de session utilisateur et un token utilisateur dans chaque ligne de journal.

Vous pouvez consulter [cet exemple](https://github.com/securitybunker/databunker-nodejs-example) pour référence :

> ::ffff:141.226.198.55 - - [02/Jan/2021:18:42:54 +0000] "GET /user/me HTTP/1.1" 304 - "http://my-dev-site/user/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36" **"b994fdbf-694e-4289-b8db-04d8049da2e8" "1f587eb7-eaaa-1629-c108-b707d99798da"**

Cela diffère d'un journal de serveur web régulier par l'ajout de deux variables personnalisées à la fin de la ligne de journal.

**"b994fdbf-694e-4289-b8db-04d8049da2e8"** est le token de session généré par la bibliothèque de session Databunker.

**"1f587eb7-eaaa-1629-c108-b707d99798da"** est un token utilisateur de l'utilisateur connecté. Il s'agit du token utilisateur généré lors de la création de l'utilisateur dans Databunker.

## Méthode 3 : Solution pour les environnements à haute sécurité

Cette méthode inclut le chiffrement partiel des événements de journal. Les PII trouvées dans les événements de journal seront regroupées et chiffrées. La configuration initiale inclura une génération unique du mot de passe d'entrée de journal pour chaque utilisateur. Ce mot de passe peut, par exemple, être enregistré dans le profil utilisateur stocké dans **Databunker**.

Comme nous devons savoir qui est le propriétaire de l'enregistrement (pour déchiffrer l'enregistrement), nous devons enregistrer l'identifiant utilisateur avec les PII chiffrées. Ainsi, un autre niveau de chiffrement sera utilisé avec un mot de passe générique.

Pour les événements de journal identifiés par l'utilisateur, les PII seront chiffrées deux fois. La première fois, les données seront chiffrées à l'aide du mot de passe d'entrée de journal de l'utilisateur. La deuxième fois, elles seront chiffrées avec le mot de passe par défaut pour masquer l'identifiant utilisateur identifié.

Pour les utilisateurs identifiés :

```
const piiPayload = JSON.stringify({ClientIP, BrowserUserAgent, SessionID});
coast piiEncrypted = Encrypt(UserPassword, piiPayload);
const linePayload = JSON.stringify({UserToken, data: btoa(piiEncrypted)});
const encrypted = Encrypt(GenericPassword, linePayload);
```

Si l'utilisateur est inconnu, un seul niveau de chiffrement peut être utilisé :

```
const piiPayload = JSON.stringify({ClientIP, BrowserUserAgent, SessionID});
const encrypted = Encrypt(GenericPassword, piiPayload);
```

Lorsque vous recevez une demande d'oubli de l'utilisateur, vous pouvez supprimer le mot de passe d'entrée de journal de l'utilisateur et son profil stocké dans **[Databunker](http://databunker.org/)**. Cela rendra les entrées de journal de l'utilisateur irrécupérables. Cela est parfaitement acceptable et satisfait les exigences du RGPD. Ainsi, des actions supplémentaires pour supprimer quoi que ce soit des fichiers journaux ne sont pas requises.

## Résumé

Avec la bonne architecture, vous pouvez rendre vos journaux conformes à la confidentialité. Ce n'est pas compliqué. Vous pouvez utiliser **Databunker** ou développer votre propre solution. 

Quel que soit votre choix, c'est bien mieux que d'ignorer complètement ce problème et de supprimer manuellement les enregistrements utilisateur des fichiers journaux.

### À emporter gratuitement

Je dirige une formation sur la confidentialité pour les fondateurs de startups et les architectes. Elle est [disponible complètement GRATUITEMENT ici](https://basebunker.com/).

### À propos de l'auteur

Yuli Stremovsky est un architecte logiciel et de sécurité de classe mondiale. Fondateur des produits de confidentialité [PrivacyBunker.io](https://privacybunker.io/) et [DataBunker.org](http://databunker.org/). Ancien employé de Checkpoint et RSA Security. Expert dans le mariage des solutions technologiques avec la confidentialité.