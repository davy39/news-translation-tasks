---
title: HTTP vs HTTPS – Quelle est la différence ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-16T17:47:14.000Z'
originalURL: https://freecodecamp.org/news/http-vs-https
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/HTTP-VS-HTTPS.png
tags:
- name: http
  slug: http
- name: https
  slug: https
- name: information security
  slug: information-security
- name: Web Security
  slug: web-security
seo_title: HTTP vs HTTPS – Quelle est la différence ?
seo_desc: "By Karlgusta Annoh\nWe interact with HTTP and HTTPS a lot in our day-to-day\
  \ lives, but many people don't know the difference. \nMost computer users just see\
  \ that the browser is telling them their application is not safe and that a hacker\
  \ might want to ..."
---

Par Karlgusta Annoh

Nous interagissons beaucoup avec HTTP et HTTPS dans notre vie quotidienne, mais beaucoup de gens ne connaissent pas la différence.

La plupart des utilisateurs d'ordinateurs voient simplement que le navigateur leur indique que leur application n'est pas sécurisée et qu'un pirate pourrait vouloir voler leurs informations importantes. Cela pousse les utilisateurs à fuir plus vite que le record actuel d'Usain Bolt.

Mais cela est évitable. C'est là qu'intervient HTTPS pour remplacer HTTP. Et nous allons en discuter aujourd'hui. :)

## Voici ce que nous allons couvrir :
1. Qu'est-ce que HTTP ?
2. Comment fonctionne HTTP
3. Caractéristiques de HTTP
4. Comment savoir si un site n'est pas sécurisé
5. Tous les sites HTTP sont-ils non sécurisés ?
6. Qu'est-ce que HTTPS ?
7. Comment fonctionne HTTPS
8. Caractéristiques de HTTPS
9. Comment fonctionne le chiffrement
10. Comment savoir si un site est sécurisé
11. Qu'est-ce qu'un certificat SSL ?
12. Comment fonctionne SSL ?
13. Comment puis-je obtenir SSL pour mon site web ?
14. Où puis-je obtenir un certificat SSL ?
15. Puis-je obtenir un certificat SSL gratuitement ?
16. Les principales différences entre HTTPS et HTTP
18. Conclusion

## Qu'est-ce que HTTP ?
Hyper Text Transfer Protocol, ou HTTP, est une méthode de communication entre votre navigateur et le site que vous souhaitez visiter (serveur web).

Cela vous permet d'obtenir les informations dont vous avez besoin depuis le serveur sur votre navigateur.

Une bonne façon de comprendre HTTP et HTTPS est d'utiliser une analogie. Nous savons que les navigateurs et les serveurs communiquent en utilisant HTTP. HTTP est généralement en texte brut. Beaucoup de gens dans le monde parlent anglais. Si un pirate qui connaît l'anglais pirate votre ordinateur, il peut facilement voir tout mot de passe que vous entrez.

Ici au Kenya, dans ma langue maternelle, nous parlons le Turkana. Si vous ne parlez pas la langue et que vous venez au Kenya et trouvez deux Turkanas en train de parler, vous ne comprendrez peut-être pas ce qu'ils disent.

C'est la beauté de HTTPS. Il est chiffré de sorte que le pirate ne comprenne pas la communication entre le navigateur et le serveur.

![Client vers serveur](https://user-images.githubusercontent.com/33565767/178446926-d904cc04-57cd-4427-bdcc-e76c35f8b51b.png "client/navigateur communiquant avec le serveur")

Si je devais aller sur http://www.google.com, je m'attendrais à voir la page par défaut de Google.

![Page par défaut de Google](https://user-images.githubusercontent.com/33565767/178450768-e1fed4a5-993d-4d49-a47f-83cce6473085.png "Page par défaut de Google")

Le client, qui dans la plupart des cas est le navigateur web, envoie un message qui, en termes informatiques, est une requête. Ensuite, le serveur renvoie une réponse.

HTTP est très utile pour envoyer des documents HTML ainsi que des images et des vidéos au navigateur web pour que l'utilisateur puisse les voir. Il est également utilisé pour envoyer des données au serveur dans des formulaires HTML.

![Où se situe le protocole HTTP](https://user-images.githubusercontent.com/33565767/178460366-d0568e2d-d107-4afe-a778-0ce1d224b176.png "Le protocole HTTP est entre le navigateur web (client) et le serveur web, qui est en communication constante avec le script côté serveur et la base de données.")


## Comment fonctionne HTTP
HTTP envoie des données en texte brut. Par exemple, si vous accédez à la page web de votre banque et qu'ils utilisent HTTP, un pirate pourrait être en mesure d'y accéder et de lire toute information que vous envoyez.

C'est là qu'intervient HTTPS. De nombreuses entreprises ont mis en place HTTPS pour permettre à leurs utilisateurs d'envoyer des données de manière sécurisée. Nous en discuterons plus en détail ci-dessous.

## Caractéristiques de HTTP
- Texte brut. Initialement, lorsque HTTP a été développé, les développeurs avaient une chose en tête : servir uniquement des documents texte. Aujourd'hui, HTTP est utilisé de manière plus étendue que prévu initialement.
- Protocole de couche 7. HTTP est un protocole de couche 7 dans le modèle OSI de réseau. La couche 7 est la couche application. Cette couche est la couche la plus haute dans le modèle OSI. Les autres couches incluent les couches physique, liaison de données, réseau, transport, session et présentation. Pour en savoir plus sur le modèle OSI, vous pouvez regarder cette vidéo gratuite sur la chaîne YouTube de freeCodeCamp par Brian Ferrill sur le fonctionnement d'Internet. Il y a plus de cookies dans le bocal que le modèle OSI. [Cours de réseaux informatiques - Ingénierie réseau [Préparation à l'examen CompTIA Network+]](https://www.youtube.com/watch?v=qiQR5rTSshw&t=27s&ab_channel=freeCodeCamp.org)

- Non sécurisé. Lorsque vous envoyez des requêtes HTTP, elles sont envoyées en texte brut. De plus, lorsque vous recevez une réponse, vous la recevez en texte brut. Cela signifie que toute personne pouvant accéder aux requêtes et aux réponses peut les lire.
![Connexion non sécurisée](https://user-images.githubusercontent.com/33565767/179723161-3ec27c27-df79-4749-b810-974583cf1687.png "Connexion non sécurisée lors d'une connexion HTTP normale par l'utilisateur")
- Léger. L'avantage de HTTP est qu'il est très léger. Il est donc très rapide car il ne fait pas le chiffrement pour sécuriser les données, comme le fait HTTPS.
- HTTP écoute généralement sur le port 80.

## Comment savoir si un site n'est pas sécurisé

Lorsque un site n'est pas sécurisé, Chrome envoie généralement un avertissement qui dit `Votre connexion n'est pas privée`.
![HTTP Non sécurisé](https://user-images.githubusercontent.com/33565767/182329336-d405d5b4-f5bb-45df-b936-aa1d04b9dffd.png "Votre connexion n'est pas sécurisée lorsque vous accédez à un site non sécurisé")

Sur Chrome, la barre d'URL montre généralement `Non sécurisé` en rouge si un site n'est pas sécurisé.
![Image d'URL non sécurisée](https://user-images.githubusercontent.com/33565767/182329466-d2db68a8-7033-4f64-bb66-0665e8fc0c62.png "URL d'un site web non sécurisé")


## Tous les sites HTTP sont-ils non sécurisés ?
Eh bien, prenons un exemple. Imaginez que vous naviguez sur un site de memes, en riant à chaque meme que vous voyez. Si le site utilise HTTP, alors vous êtes hors de danger. Ce n'est pas grave.

Vous vous ennuyez et décidez d'aller sur le site de votre banque pour accéder à votre compte sur votre navigateur. Si le site n'utilise pas HTTPS, vous pourriez aussi bien servir vos détails de compte à un pirate sur un plateau d'argent.

Donc, en résumé, si vous naviguez sur des informations sans conséquence, HTTP est acceptable. Mais si vous traitez des informations sensibles, HTTP n'est pas suffisant.

## Qu'est-ce que HTTPS ?
Hyper Text Transfer Protocol Secure, ou HTTPS, est un moyen par lequel la communication peut se faire de manière SÉCURISÉE entre votre navigateur et le site que vous souhaitez visiter (serveur web).

## Comment fonctionne HTTPS
HTTPS établit une connexion sécurisée en utilisant un protocole sécurisé qui chiffre vos données.

Pour la plupart des sites web, la meilleure façon d'avoir HTTPS est d'obtenir un certificat SSL (Secure Sockets Layer) ou un certificat TLS (Transport Layer Security).

À l'heure actuelle, SSL est devenu suffisamment avancé pour supporter TLS. Vous n'avez donc pas besoin d'obtenir un certificat TLS.

## Caractéristiques de HTTPS
- Chiffre les données. Le chiffrement des données se fait via le protocole TLS/SSL.
- C'est un protocole de couche 4 (couche Transport).
- Les échanges de clés publiques et privées se font en HTTPS pour chiffrer et déchiffrer les données.
- Comparé à HTTP, il est plus lourd. Lorsque le chiffrement et le déchiffrement se font en HTTPS, il devient plus lourd.
- HTTPS écoute sur le port 443.
## Comment fonctionne le chiffrement

![Comment fonctionne le chiffrement](https://user-images.githubusercontent.com/33565767/180215739-5e731309-eda1-4993-927c-c9daa400c3c5.png "Je suis un dev du texte client passant par un chiffrement")

Supposons que je tape "Je suis un dev". Ce texte est chiffré lorsque je clique sur envoyer, puis il est déchiffré côté serveur.

La même chose est également vraie côté serveur. Si je reçois une réponse du serveur, elle sera d'abord chiffrée, puis déchiffrée côté client.

## Comment savoir si un site est sécurisé
Pour savoir qu'un site est sécurisé, vous regardez généralement la barre d'URL où vous pouvez voir un cadenas. Si il y a un cadenas, la connexion du client au serveur est sécurisée.

![Montrant que le site est sécurisé](https://user-images.githubusercontent.com/33565767/178449484-738fb908-901d-4a61-9f8f-fa5a39029012.png "Un cadenas qui montre que le site est sécurisé sur l'URL")

Lorsque vous cliquez sur l'icône de cadenas, il vous donne plus d'informations sur la connexion sécurisée.

![Montre que le site est sécurisé](https://user-images.githubusercontent.com/33565767/180213859-21460cfa-6a8c-484e-81e5-5dba4fc31f2a.png "La section URL avec plus de détails d'un site sécurisé")


## Qu'est-ce qu'un certificat SSL ?
Un certificat SSL est un petit fichier qui indique aux navigateurs que votre site web – par exemple, freecodecamp.org – est bien celui qu'il prétend être, et qu'il est fiable.

Afin de s'authentifier, le certificat est capable de confirmer au client (utilisateur) que le serveur auquel il se connecte est bien celui qui gère ce domaine. Tout cela est fait pour protéger l'utilisateur contre les problèmes de sécurité tels que l'usurpation de domaine.

Il contient une clé publique et indique qui est le propriétaire du site web auquel vous essayez de vous connecter. Si un site web n'a pas de certificat SSL, il ne peut pas être chiffré avec TLS.

Vous pouvez personnellement créer votre propre certificat SSL (également appelé certificat auto-signé), si vous êtes le propriétaire du site web. Le problème avec cette approche est que les navigateurs comme Chrome ne font pas confiance à ces certificats. Ils préfèrent faire confiance aux certificats émis par une autorité de certification.

## Comment fonctionne le chiffrement SSL ?

Il existe deux types de chiffrement SSL, asymétrique et symétrique. La combinaison de l'asymétrique et du symétrique est ce qui rend le chiffrement SSL efficace. Examinons-les ci-dessous pour en savoir plus.

### Qu'est-ce que le chiffrement asymétrique ?

Dans le chiffrement asymétrique, vous avez deux clés. Ce sont :
1. Clé publique.
2. Clé privée.

![Chiffrement asymétrique](https://user-images.githubusercontent.com/33565767/181718454-847858dc-0df5-4bc5-bfaf-b6210c571d8f.png "Chiffrement asymétrique (clé publique)")

Le client/utilisateur/navigateur donne la clé publique au serveur avec lequel il communique. Ensuite, le chiffrement se fait à l'aide de la clé publique, et le déchiffrement se fait à l'aide de la clé privée du serveur.

La clé privée ne peut être trouvée que sur ce serveur particulier. Personne d'autre ne l'a. Cela montre pourquoi le chiffrement asymétrique est plus fort et plus difficile à pirater, car il a deux clés différentes, la clé privée et la clé publique. Les deux clés fonctionnent ensemble pour garantir que les données sont plus sécurisées.

Cela explique également pourquoi la taille de ce chiffrement est de 1024/2048 bits.

### Qu'est-ce que le chiffrement symétrique ?

Dans le chiffrement symétrique, c'est très simple. Vous avez une clé, et c'est tout. Le client utilise une clé pour le chiffrement, et le serveur utilise la même clé pour déchiffrer les données.

Le chiffrement symétrique est très léger. La taille est de 128/256 bits. Mais il est un peu plus facile à pirater par rapport à l'asymétrique. Cela ne signifie pas qu'il n'est pas utile. Lorsque nous utilisons SSL, nous combinons l'asymétrique et le symétrique pour pouvoir rendre la communication plus sûre et plus sécurisée.

![Chiffrement symétrique](https://user-images.githubusercontent.com/33565767/181720497-326e0dd9-5e0b-4bfb-b01a-2effec5ab9e0.png "Comment fonctionne le chiffrement symétrique en utilisant une clé côté client pour chiffrer et la même clé côté serveur pour déchiffrer")

### Comment fonctionnent le chiffrement asymétrique + symétrique

La combinaison des deux, asymétrique et symétrique, est maintenant le mur à double face.
![Asymétrique et Symétrique](https://user-images.githubusercontent.com/33565767/182565306-224f199a-da88-4a68-be81-707636cc1069.png "Comment fonctionnent le chiffrement asymétrique et symétrique par le client envoyant d'abord un Hello au serveur. Le serveur envoie ensuite au client sa clé publique et son certificat en réponse. Le client, à l'étape 3, envoie une clé de session qui est chiffrée à l'aide de la clé publique. À l'étape 4, le serveur déchiffrera la clé de session à l'aide de la clé privée du serveur. Enfin, à l'étape 5, la connexion est établie entre le client et le serveur.")

Dans la première étape, le serveur envoie au navigateur la clé publique asymétrique. Comme nous le savons maintenant, la clé asymétrique a à la fois la clé publique et la clé privée. Par conséquent, le navigateur recevra la clé publique.

Après cela, le navigateur génère une clé de session.

Le chiffrement symétrique utilise une seule clé pour le client et le serveur. Donc, ce qui se passera, c'est que le navigateur générera une clé de session locale. Il s'agit d'une clé de session de chiffrement symétrique. Elle sera ensuite chiffrée, à l'aide de la clé publique qui est asymétrique, donnée dans la première étape. La clé de session générée localement sera ensuite combinée avec la clé publique, et envoyée au serveur.

Le serveur utilisera ensuite une clé privée pour déchiffrer la clé de session chiffrée qu'il a reçue. Dans cette étape particulière, le serveur utilisera la clé privée asymétrique pour déchiffrer la clé de session qu'il a reçue.

Maintenant, une fois le déchiffrement effectué, le serveur et le navigateur utiliseront la clé de session pour la communication. La clé de session ne sera utilisée que pour cette session spécifique.

Supposons que vous fermiez votre navigateur, et peut-être que vous vous connectez le lendemain – tout recommence. Les clés de session sont recréées.

## Comment puis-je obtenir SSL pour mon site web ?
Si vous êtes propriétaire d'un site web, vous pouvez obtenir un certificat SSL auprès d'une autorité de certification.

Vous devrez ensuite installer le certificat sur votre serveur web où votre site est hébergé. La plupart du temps, l'entreprise d'hébergement où vous hébergez votre site web gère ce processus pour vous.

## Où puis-je obtenir un certificat SSL ?
Il existe des organisations qui délivrent des certificats de sécurité. Ces organisations sont appelées autorités de certification. Certaines de ces autorités de certification incluent : DigiCert, Comodo, et bien d'autres.

De nombreux développeurs obtiennent des certificats de ces organisations. Comme ce sont les émetteurs de certificats les plus largement utilisés, les navigateurs font généralement confiance aux certificats de ces organisations.

## Puis-je obtenir un certificat SSL gratuitement ?
Cloudflare offre des certificats SSL gratuitement. C'est l'une des premières entreprises de sécurité Internet à le faire.

Si vous souhaitez en obtenir un, vous pouvez [le vérifier ici](https://www.cloudflare.com/ssl/).

## À quoi sert HTTPS ?
HTTPS aide beaucoup avec la sécurité. Sans lui, la transmission d'informations sensibles devient un grand défi, surtout si votre entreprise nécessite une méthode de communication sécurisée.

Les sites qui acceptent les paiements en ligne comme les sites de commerce électronique nécessitent généralement HTTPS. Cela permet d'éviter que des informations telles que les détails de carte de crédit et les informations de connexion ne soient volées (Source : [Tony Messer](https://www.entrepreneur.com/article/281633)).

## Les principales différences entre HTTPS et HTTP
- La couche de chiffrement est activée dans HTTPS alors qu'il n'y a pas de couche de chiffrement dans HTTP.
- Vos données sont protégées dans HTTPS alors que dans HTTP, elles ne le sont pas.
- Votre classement est boosté dans Google lorsque vous utilisez HTTPS alors qu'avec HTTP, vous n'obtenez aucun boost de classement.
- Vous êtes protégé contre le phishing lorsque vous utilisez HTTPS alors qu'il n'y a pas de protection lorsque vous utilisez HTTP.
- Vous êtes conforme aux réglementations de l'industrie des paiements lorsque vous utilisez HTTPS alors que HTTP n'est pas conforme.
- Le chargement de HTTPS dans les premières secondes peut être plus lent que le chargement de HTTP.
- L'obtention de certificats SSL peut coûter de l'argent alors qu'il n'y a pas de coûts de certification avec HTTP.
- Lorsque vous utilisez HTTPS, vous devenez copain avec Google Chrome. Google Chrome n'aime pas HTTP et donc vous recevrez toujours des notifications de site non sécurisé.

## Conclusion
HTTP et HTTPS sont très importants dans notre vie quotidienne en tant que développeurs. La communication entre le navigateur et le serveur est ce qui alimente une grande partie du travail que nous faisons.

En protégeant les données de vos utilisateurs autant que possible pour que leurs informations ne soient pas volées, vous gagnerez leur confiance et offrirez une meilleure expérience utilisateur.

À bientôt.