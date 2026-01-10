---
title: Comment externaliser votre sécurité en ligne avec 1Password, Authy et Privacy.com
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-03-17T22:08:13.000Z'
originalURL: https://freecodecamp.org/news/outsourcing-security-with-1password-authy-and-privacy-com
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/cover-4.png
tags:
- name: authentication
  slug: authentication
- name: cybersecurity
  slug: cybersecurity
- name: life
  slug: life
- name: passwords
  slug: passwords
seo_title: Comment externaliser votre sécurité en ligne avec 1Password, Authy et Privacy.com
seo_desc: 'Take some work off your plate while beefing up security with three changes
  you can make today.

  Unstable times are insecure times, and we’ve already got enough going on to deal
  with. When humans are busy and under stress, we tend to get lax in less-ob...'
---

Allégez votre charge de travail tout en renforçant votre sécurité avec trois changements que vous pouvez apporter dès aujourd'hui.

Les périodes instables sont des périodes peu sûres, et nous avons déjà suffisamment à gérer. Lorsque les humains sont occupés et stressés, ils tendent à se relâcher dans des domaines moins évidemment pressants, comme la sécurité de nos comptes en ligne.

Ces domaines ne deviennent un problème évident que lorsqu'il est trop tard pour prévenir. Heureusement, la plupart du travail nécessaire pour maintenir nos mesures de cybersécurité peut être externalisé.

Mettre en place des mesures de cybersécurité appropriées peut être fastidieux, et je déteste particulièrement m'occuper de choses que je pourrais éviter. Ces choses fastidieuses incluent la réinitialisation des mots de passe oubliés, le transfert des codes d'authentification multifactorielle (MFA) lorsque je change de périphérique, et la gestion des conséquences des détails de paiement compromis en cas de violation de l'un de mes comptes.

Voici trois changements que j'ai apportés qui réduisent considérablement les chances de devoir m'occuper de ces choses à nouveau. Vous pouvez le faire aussi.

## 1Password

J'ai historiquement évité les gestionnaires de mots de passe en raison d'une réaction irrationnelle à mettre tous mes œufs dans le même panier.

Savez-vous ce qui est bon pour les réactions irrationnelles ? L'éducation. Pour déterminer si mettre tous mes mots de passe dans un gestionnaire de mots de passe est plus sécurisé que de ne pas en utiliser, je me suis mis en quête de voir ce que certaines personnes intelligentes en disaient.

Tout d'abord, nous devons savoir une ou deux choses sur les mots de passe. Troy Hunt a découvert il y a presque une décennie que [essayer de se souvenir de mots de passe forts ne fonctionne pas](https://www.troyhunt.com/only-secure-password-is-one-you-cant/). Plus récemment, Alex Weinert a développé ce point dans [Your Pa$$word doesnt matter](https://techcommunity.microsoft.com/t5/azure-active-directory-identity/your-pa-word-doesn-t-matter/ba-p/731984).

TL;DR : nos cerveaux ne sont pas meilleurs que les ordinateurs pour les mots de passe, et veuillez utiliser MFA.

Donc, les mots de passe n'ont pas d'importance, mais les mots de passe compliqués sont toujours meilleurs que ceux qui sont mémorables et devinables.

Puisque j'ai peu d'espoir de me souvenir d'une douzaine de variations de `p/q2-q4!` (je ne suis pas un [joueur d'échecs](https://inbox.vuxu.org/tuhs/CAG=a+rj8VcXjS-ftaj8P2_duLFSUpmNgB4-dYwnTsY_8g5WdEA@mail.gmail.com/)), c'est une tâche que je peux externaliser à [1Password](https://1password.com/). Je devrai toujours me souvenir d'un long mot de passe principal compliqué - 1Password l'utilise pour chiffrer mes données, donc je ne peux vraiment pas le perdre - mais je peux gérer un seul.

L'utilisation spécifique de 1Password présente un autre avantage, décidément évident. J'ai choisi 1Password en raison de leur fonctionnalité [Watchtower](https://support.1password.com/watchtower/). [Grâce à Have I Been Pwned de Troy Hunt](https://www.troyhunt.com/have-i-been-pwned-is-now-partnering-with-1password/), Watchtower vous alertera si l'un de vos mots de passe apparaît dans une violation afin que vous puissiez les changer. Les mots de passe ne fonctionnent toujours pas complètement, mais c'est probablement le meilleur pansement qui existe.

Un dernier bonus est que l'utilisation d'un gestionnaire de mots de passe est beaucoup plus pratique. Les mots de passe compliqués n'ont pas besoin de prendre deux tentatives pour être saisis.

En ce qui concerne les sites que j'utilise rarement et que je ne considère pas comme importants, je suis généralement beaucoup plus susceptible de finir par (ré)initialiser ces mots de passe à quelque chose de mémorable, et donc de facilement piratable. Même - peut-être surtout - les sites sans importance peuvent ouvrir des portes à vos sites plus importants.

En utilisant 1Password et des mots de passe générés, ces sites sont désormais également des citoyens de première classe dans le monde des mots de passe forts, au lieu d'être des vecteurs d'attaque à moitié abandonnés et à moitié ouverts.

Donc, oui, tous mes œufs sont dans le même panier. Un panier bien protégé, complexe et surveillé, par opposition à être dispersé dans plusieurs de ces cartons en papier de l'épicerie qui ne ferment pas vraiment et ne peuvent certainement pas survivre à un _choc plutôt doux_ lorsque vous entrez par la porte, Victoria, combien de fois dois-je vous rappeler d'être prudente.

## Authy

D'accord - c'est plutôt un panier et demi. 😅

[Authy](https://authy.com/), des gens de [Twilio](https://www.twilio.com), fournit une solution 2FA plus sécurisée que les SMS (je trouve cela une intersection intéressante, venant de Twilio, et je l'applaudis.) [Contrairement à Google Authenticator](https://authy.com/blog/authy-vs-google-authenticator/), vous pouvez choisir de sauvegarder vos codes 2FA au cas où vous perdriez ou changeriez votre téléphone. (1Password offre également une fonctionnalité 2FA - mais, vous savez, redondances.)

Avec Authy, votre sauvegarde est chiffrée avec votre mot de passe, de manière similaire à 1Password. Cela en fait le deuxième mot de passe que vous ne pouvez pas oublier, si vous ne voulez pas perdre l'accès à vos codes. Si vous réinitialisez votre compte, ils disparaissent tous. Je peux gérer le fait de me souvenir de deux mots de passe ; je ferai ce compromis.

J'ai essayé d'autres méthodes de MFA, y compris des clés matérielles, qui peuvent rendre l'accès aux comptes sur votre téléphone plus compliqué que je ne suis prêt à supporter. Je trouve que la combinaison de 1Password et Authy est la combinaison la plus pratique de commodité et de sécurité qui existe encore à ma connaissance.

## Privacy.com

Enfin, il y a une dernière ligne de défense que vous pouvez mettre en place dans le cas malheureux où l'un de vos comptes est encore compromis. Tous les mots de passe forts et MFA du monde ne vous aideront pas si vous ouvrez vous-même les portes, et les escroqueries et le phishing existent.

Puisqu'il est plutôt impratique d'utiliser une carte de crédit réelle différente à chaque endroit où vous faites des achats, les cartes virtuelles sont une excellente idée. Il n'y a aucune bonne raison de passer un après-midi (ou plus) à réinitialiser vos informations de paiement sur chaque compte juste pour contrer un commerçant malveillant ou réparer une violation de données de ce magasin en ligne de mignons distributeurs de sel où vous avez fait un achat l'année dernière (juste moi ?).

En configurant une carte virtuelle séparée pour chaque commerçant, dans le cas où l'un de ces commerçants est compromis, je peux simplement suspendre ou supprimer cette carte. Aucun de mes autres comptes ou détails bancaires réels ne sont impliqués dans le processus. Les cartes peuvent avoir des limites temporelles ou être des numéros jetables, ce qui les rend idéales pour configurer des abonnements.

C'est le genre de fonctionnalité de base que j'espère, un jour, devenir plus répandue de la part des banques et des cartes de crédit. En attendant, je continuerai à utiliser [Privacy.com](https://privacy.com/join/Q6V3V). C'est mon lien de parrainage ; si vous souhaitez me remercier en l'utilisant, nous recevrons tous les deux cinq dollars en bonus.

## Externaliser une meilleure sécurité

Ensemble, la mise en œuvre de ces changements prendra probablement un après-midi, selon le nombre de comptes que vous avez. Cela en vaut la peine pour le temps que vous passeriez sinon à réinitialiser les mots de passe, à configurer de nouveaux appareils ou (touchez du bois) à vous remettre de détails bancaires compromis.

Le meilleur de tout, vous aurez une protection continue qui fonctionne en arrière-plan - un renforcement sans effort de votre [posture de cybersécurité personnelle](https://victoria.dev/blog/personal-cybersecurity-posture-for-when-youre-just-this-guy-you-know/).

Nous avons la technologie. Libérez quelques cycles cérébraux pour vous concentrer sur d'autres choses - ou simplement éliminez du stress inutile de votre vie en externalisant les détails fastidieux.