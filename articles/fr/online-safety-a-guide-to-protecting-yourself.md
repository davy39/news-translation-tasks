---
title: Sécurité en ligne – Un guide pour vous protéger
subtitle: ''
author: Rohit Jacob Mathew
co_authors: []
series: null
date: '2024-05-20T15:13:00.000Z'
originalURL: https://freecodecamp.org/news/online-safety-a-guide-to-protecting-yourself
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/rohit-2400-x-1260.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Security
  slug: security
seo_title: Sécurité en ligne – Un guide pour vous protéger
seo_desc: "Navigating digital accounts safely is a concern for many in the modern\
  \ age. \nDigital accounts have become an integral part of our daily lives. From\
  \ email and online banking to accounts on ride-sharing platforms like Uber and e-commerce\
  \ platforms like..."
---

Naviguer en toute sécurité dans les comptes numériques est une préoccupation pour beaucoup à l'ère moderne.

Les comptes numériques sont devenus une partie intégrante de notre vie quotidienne. Des emails et de la banque en ligne aux comptes sur des plateformes de covoiturage comme Uber et des plateformes de commerce électronique comme Amazon, protéger notre vie numérique en ligne devient impératif.

Lorsque l'informatique a commencé, nous utilisions des ordinateurs pour des calculs complexes sur des machines individuelles.

Progressivement, nous avons commencé à connecter ces machines via l'internet, ce qui a conduit au boom des dot-com. Ce boom a abouti à la création de nombreux sites web comme des salons de discussion et des forums.

Pour y accéder, vous deviez vous identifier, ce qui a conduit à l'utilisation du système courant de nom d'utilisateur et de mot de passe que nous utilisons aujourd'hui pour créer des comptes.

Ce nom d'utilisateur et ce mot de passe sont devenus un moyen d'identifier de manière unique une personne et son compte sur ces sites, formant un type d'identité numérique.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-47.png)
_Vecteurs courants d'attaques cybernétiques ([Source](https://www.balbix.com/insights/attack-vectors-and-breach-methods/))_

De nos jours, certains des incidents les plus courants que nous voyons sont les escroqueries par hameçonnage, le vol d'identité, les [attaques par ingénierie sociale](https://www.cisco.com/c/en/us/products/security/what-is-social-engineering.html), les ransomwares, et les identifiants compromis ou faibles. La plupart, sinon tous, de ces incidents sont directement ou indirectement liés à notre identité numérique et à la manière dont nous y accédons. Par conséquent, nous devons nous assurer de nous sécuriser en ligne.

## Comment se sécuriser en ligne ? 👋

Je vais discuter d'un aspect de la sécurisation en ligne, qui concerne les comptes numériques et la manière dont nous y accédons. La stratégie la plus recommandée pour cela est :

1. Utilisez une méthode de connexion sans mot de passe comme Face ID, la connexion par empreinte digitale ou les clés d'accès.
2. Utilisez un gestionnaire de mots de passe, comme BitWarden ou 1Password, pour les sites qui nécessitent encore un nom d'utilisateur et un mot de passe.
3. Implémentez l'authentification multifacteur (MFA) pour vérifier votre identité. Cela peut inclure un OTP basé sur le temps (TOTP) ou une vérification par lien profond via email.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-48.png)
_Tableau de mauvais à bon pour protéger votre compte ([Source](https://www.microsoft.com/en-us/security/business/solutions/passwordless-authentication))_

Permettez-moi également de partager la stratégie que j'utilise :

* J'utilise actuellement 1Password comme gestionnaire de mots de passe.
* J'ai implémenté TOTP ou MFA sans mot de passe sur la plupart des sites.
* J'ai supprimé la plupart des connexions sociales et des connexions uniques.
* Je réalise régulièrement un audit de sécurité pour voir qui a accès à mes données.
* En cas de fuite de données ou de piratage, je change immédiatement mes mots de passe.
* La création de compte sans mot de passe utilisant des clés d'accès est une amélioration récente, et je commencerai probablement à les adopter bientôt.

## Mais ... 🤔 Je suis toujours confus. Pourquoi devrions-nous faire tout cela ?

Bonne question. Explorons pourquoi nous trouvons les connexions basées sur les mots de passe inefficaces, peu pratiques et frustrantes.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-49.png)
_Page de connexion et d'inscription_

Commençons par un écran de connexion. Vous voyez ci-dessus la page de connexion ou d'inscription traditionnelle par nom d'utilisateur/mot de passe et quelques [connexions sociales](https://blog.rohitjmathew.space/why-is-a-social-login-more-secure). Ce sont actuellement les méthodes les plus courantes pour accéder à un compte.

Examinons comment ces méthodes contribuent à des sentiments d'inefficacité, de désagrément et de frustration.

### Inefficace

* **Nous créons des mots de passe terribles -** Voici quelques-uns des mots de passe les plus courants au monde. Il existe des listes open-source de ces mots de passe que les pirates utilisent. Des mots de passe simples comme ceux-ci ou ceux qui vous concernent ne sont pas du tout sécurisés. Ils peuvent facilement être devinés à partir de la liste ou avec un peu d'ingénierie sociale.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-50.png)
_Mots de passe courants dans le monde ([Source](https://www.quora.com/Is-using-password-as-a-password-really-common))_

* **Nous réutilisons les mêmes mots de passe -** Pour simplifier les choses, nous utilisons souvent les mêmes mots de passe pour plusieurs comptes. Cela est très peu sécurisé car si un compte est compromis, un pirate peut facilement accéder à d'autres comptes.
* **Connexions sociales compromises -** Bien que les connexions sociales soient plus faciles à utiliser, elles présentent également un point de défaillance unique. Si une connexion sociale est compromise, cela peut entraîner la compromission d'autres comptes également.
* **L'authentification multifacteur (MFA) basée sur SMS et voix peut être piratée -** Bien que la MFA ait amélioré la sécurité, les pirates se sont adaptés et ont trouvé des moyens d'intercepter la MFA basée sur SMS ou voix. Par conséquent, ces méthodes ne sont plus les plus sécurisées.

**_Note:_** _Si vous visitez le site_ [_haveibeenpwned_](https://haveibeenpwned.com), _vous pouvez voir quelles données ont été compromises._

### Peu pratique

* **La réinitialisation des mots de passe n'est pas facile -** Lorsque nous oublions nos mots de passe, nous devons souvent passer par plusieurs étapes pour retrouver l'accès à nos comptes.
* **Les exigences en matière de mots de passe sont parfois difficiles à retenir -** Créer un nouveau mot de passe qui répond à toutes les exigences de sécurité, telles que l'inclusion de lettres majuscules, de chiffres et de caractères spéciaux, peut être difficile à retenir.
* **Les connexions sociales peuvent ne pas fonctionner parfois -** Avec les récents temps d'arrêt des sites de médias sociaux, vos connexions peuvent également subir des interruptions.
* **L'authentification multifacteur (MFA) peut ajouter de la friction -** La MFA nécessite souvent une étape supplémentaire et est liée à un appareil, ce qui peut compliquer le processus. De plus, la sauvegarde et la récupération des méthodes MFA ne sont pas simples.

### Frustrant

* **Se souvenir de différents mots de passe -** Les mots de passe mémorables sont faciles à deviner ou à craquer pour les pirates. Il est frustrant d'avoir différents mots de passe pour divers comptes et de se souvenir de chacun.
* **Fournisseurs de connexion sociale et confidentialité des données -** Certains fournisseurs de connexion sociale ou sites web peuvent partager ou vendre les données de leurs utilisateurs à des entités tierces. Cela signifie que lorsque vous utilisez des connexions sociales, vos informations personnelles, vos habitudes de navigation et d'autres données peuvent être accessibles par des entreprises auxquelles vous n'aviez pas l'intention de les partager.
* **L'authentification multifacteur (MFA) ne fonctionne pas -** Le SMS ou l'appel vocal contenant le code d'authentification n'est pas reçu, les retards dans la réception des notifications push, ou les mots de passe à usage unique basés sur le temps (TOTP) peuvent expirer sont quelques exemples. Ces problèmes peuvent causer une frustration significative et entraver le processus de connexion.
* **Abus de l'authentification multifacteur (MFA) -** Il y a eu une augmentation des pirates abusant de la MFA pour accéder aux comptes. Ils exploitent les solutions MFA qui envoient des notifications d'approbation de connexion après des tentatives d'accès au compte, sachant que les gens sont souvent frustrés par un flux de messages. Les pirates ont compromis [Uber](https://www.wired.com/story/uber-hack-mfa-phishing/), [Microsoft et Cisco](https://tech.co/news/mfa-fatigue-hackers) en utilisant cette méthode.

## D'accord, alors pourquoi la stratégie recommandée est-elle meilleure ? 😅

Décomposons la stratégie recommandée :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-48.png)
_Tableau de mauvais à bon pour protéger votre compte ([Source](https://www.microsoft.com/en-us/security/business/solutions/passwordless-authentication))_

### Utilisez une méthode de connexion sans mot de passe

Les méthodes sans mot de passe sont plus sécurisées que les connexions basées sur les mots de passe. Si vous voulez savoir pourquoi, vous pouvez lire mon article sur [Comment fonctionne Face ID ou Touch ID](https://blog.rohitjmathew.space/intro-to-webauthn).

En termes simples, les méthodes sans mot de passe, comme Passkey, utilisent l'authentification biométrique ainsi que les identifiants de l'appareil pour activer l'authentification multifacteur (quelque chose que vous êtes et quelque chose que vous avez) au lieu d'un mot de passe (quelque chose que vous savez).

Cette approche n'est pas seulement plus facile et plus sécurisée, mais aussi résistante à de nombreux problèmes que nous avons discutés précédemment. Bien que encore nouvelle, il y a eu une poussée significative de l'industrie pour adopter cela, surtout avec la montée des authentificateurs biométriques dans nos appareils.

_**Note:** Vous pouvez trouver une liste de sites web et d'applications qui prennent en charge la connexion sans mot de passe ou la MFA, ainsi que des instructions sur la manière de la configurer, sur [passkeys.directory](https://passkeys.directory/)._

### Utilisez un gestionnaire de mots de passe pour les sites qui nécessitent encore un nom d'utilisateur et un mot de passe

Bien que tous les sites n'aient pas adopté les connexions sans mot de passe, une meilleure façon de sécuriser vos comptes qui utilisent encore des mots de passe est d'utiliser un gestionnaire de mots de passe comme [Bitwarden](https://bitwarden.com/) ou [1Password](https://1password.com/).

Ils vous aident à créer des mots de passe forts et uniques et à les retenir facilement. La plupart des gestionnaires de mots de passe sont dotés de fonctions de remplissage automatique qui facilitent leur utilisation sur différents appareils.

Bien qu'ils puissent représenter un point de défaillance unique et être un peu fastidieux à configurer initialement, les avantages l'emportent largement sur les inconvénients.

Se souvenir d'un seul mot de passe principal pour gérer vos comptes de manière sécurisée est bien mieux que de devoir faire face aux problèmes mentionnés précédemment.

**_Note:_** _1Password (le gestionnaire de mots de passe que j'utilise) a fourni plus de_ [_détails_](https://blog.1password.com/what-if-1password-gets-hacked/) _sur ce qui se passe s'ils sont piratés. Bien qu'il y ait eu des incidents de piratage récents, je ne suis pas au courant de données compromises._

### Implémentez l'authentification multifacteur pour vérifier votre identité

L'authentification multifacteur (MFA) est une mesure de sécurité qui exige des utilisateurs qu'ils fournissent plus d'une forme d'identification pour accéder à leurs comptes.

Cela implique généralement une combinaison de quelque chose que vous savez, comme un mot de passe traditionnel, et de quelque chose que vous avez, comme un mot de passe à usage unique (OTP) envoyé par SMS ou email.

En ajoutant cette couche supplémentaire de sécurité, la MFA réduit considérablement le risque d'accès non autorisé, même si votre mot de passe est compromis.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-51.png)
_Qu'est-ce que l'authentification multifacteur ([Source](https://www.hsph.harvard.edu/information-technology/2022/10/03/october-is-cybersecurity-month-week-1/))_

L'implémentation de la MFA est une étape cruciale pour protéger vos comptes en ligne et vos informations personnelles. Cela peut prendre un peu de temps supplémentaire lors du processus de connexion, mais la sécurité ajoutée en vaut bien l'effort.

**_Note:_** _La plupart des sites web et services que nous utilisons fournissent la 2FA. Vous pouvez vérifier en fonction de votre cas d'utilisation sur_ [_2fa.directory_](https://2fa.directory/)_.

## Conclusion

Cet article explore les menaces de sécurité courantes et propose des stratégies pour vous protéger en ligne.

Certaines recommandations incluent l'utilisation de méthodes de connexion sans mot de passe comme Face ID ou Passkeys, l'utilisation de gestionnaires de mots de passe comme 1Password, et l'implémentation de l'authentification multifacteur (MFA).

Ces mesures peuvent grandement améliorer votre sécurité en ligne et réduire le risque d'accès non autorisé à vos comptes.

Espérons que cet article vous aide à comprendre pourquoi la sécurité en ligne est importante et vous permet de rester en sécurité sur internet.

Merci d'avoir lu ! J'espère vraiment que vous trouvez cet article utile. Si vous pensez que cet article était utile, veuillez partager l'article pour aider à promouvoir ce contenu auprès des autres.

Si vous souhaitez lire plus de mes articles, visitez mon [**blog**](https://blog.rohitjmathew.space/).

Merci encore d'avoir lu ! :)

P.S N'hésitez pas à me contacter sur [**LinkedIn**](https://www.linkedin.com/in/rohitjmathew) ou [**Twitter**](https://twitter.com/iamrohitjmathew).