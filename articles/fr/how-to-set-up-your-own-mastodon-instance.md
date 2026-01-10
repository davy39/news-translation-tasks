---
title: Comment installer votre propre instance Mastodon
subtitle: ''
author: Naomi Carrigan
co_authors: []
series: null
date: '2022-11-11T16:29:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-your-own-mastodon-instance
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-14-at-4.49.55-PM.png
tags:
- name: freeCodeCamp.org
  slug: freecodecamp
- name: mastadon
  slug: mastadon
- name: social media
  slug: social-media
seo_title: Comment installer votre propre instance Mastodon
seo_desc: "Mastodon is a decentralized, federated social media platform based on the\
  \ ActivityPub protocol. It allows you to follow and interact with friends across\
  \ multiple instances. \nIn this article, you will learn how freeCodeCamp set up\
  \ our own Mastodon ins..."
---

Mastodon est une plateforme de médias sociaux décentralisée et fédérée basée sur le protocole [ActivityPub](https://www.w3.org/TR/activitypub/). Elle vous permet de suivre et d'interagir avec des amis sur plusieurs instances. 

Dans cet article, vous apprendrez comment freeCodeCamp a mis en place notre propre instance Mastodon - et comment vous pouvez faire de même.

## Qu'est-ce que Mastodon ?

Imaginez s'il existait plusieurs sites web différents pour Twitter. Sur chacun de ces sites, vous pourriez créer un compte (en créer un sur tous, si vous vous sentiez ambitieux). 

Vous pourriez alors utiliser votre compte pour suivre vos amis sur n'importe quel autre site. Vous pourriez republier leur contenu sur votre compte et voir l'activité de tous vos comptes suivis sur une seule timeline.

Bien que Mastodon soit de loin la plateforme la plus populaire à utiliser, il existe également d'autres options telles que [Misskey](https://github.com/misskey-dev/misskey), [Pleroma](https://git.pleroma.social/pleroma/pleroma), et leurs diverses variantes. 

Certaines de ces plateformes pourront se fédérer les unes avec les autres, avec des capacités interplateformes, tandis que d'autres ne le pourront pas.

## Commencer avec Mastodon

Il y a quelques choses dont vous aurez besoin pour commencer le processus que nous avons suivi pour freeCodeCamp :

* Un compte [DigitalOcean](https://digitalocean.com)
* Un fournisseur DNS (nous utilisons [Cloudflare](https://cloudflare.com)).

Commencez par vous connecter à DigitalOcean et créez une nouvelle droplet. Dans les options d'image, sélectionnez l'onglet marketplace. Ensuite, recherchez l'image Mastodon - cela gérera une bonne partie de la configuration pour vous.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-48.png)

Configurez le reste des paramètres de la droplet selon vos besoins - pour la taille, nous avons commencé avec l'option à 12 $ avec l'intention de monter en puissance si nécessaire.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-49.png)

Une fois que la droplet a fini d'être provisionnée, copiez l'adresse IP. Configurez un enregistrement A pour votre domaine ou sous-domaine pour pointer vers votre droplet - **faites cela AVANT de vous connecter en SSH à la droplet**.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-50.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-52.png)

Une fois que votre DNS est prêt, connectez-vous en SSH à la droplet en tant qu'utilisateur `root`.

## Comment configurer votre instance Mastodon

Lorsque vous vous connectez pour la première fois au serveur, l'outil de configuration automatique s'exécutera.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-54.png)

Suivez les invites :

* Pour `Nom de domaine`, entrez le nouveau domaine/sous-domaine que vous venez de configurer.
* L'outil vous demandera si vous souhaitez stocker les fichiers téléchargés par les utilisateurs sur le cloud. Si c'est le cas, vous devrez fournir des identifiants pour un fournisseur de stockage tel qu'Amazon S3.
* Mastodon nécessite un serveur SMTP pour les notifications par email et le flux d'inscription. Vous pouvez soit configurer le vôtre, soit fournir des identifiants pour un service comme [SendGrid](https://sendgrid.com).
* Le flux SMTP vous invitera à envoyer un email de test. Cela est _fortement recommandé_, car cela confirmera que vos paramètres SMTP sont corrects. Si ce n'est pas le cas, l'assistant de configuration vous invitera à les ressaisir.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-55.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-67.png)

Vous allez ensuite créer un compte Mastodon pour servir d'administrateur. Cela peut être votre compte personnel, ou cela peut être un compte partagé parmi votre équipe.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-68.png)

Enfin, vous serez invité à entrer votre email pour les notifications de renouvellement de certificat LetsEncrypt.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-57.png)

Après quelques minutes, votre instance devrait être opérationnelle.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-61.png)

## Comment configurer votre instance Mastodon

La visite de votre nouveau domaine/sous-domaine devrait afficher la page d'accueil de Mastodon.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-58.png)

Connectez-vous en utilisant les identifiants d'administrateur que vous avez générés précédemment. Ensuite, sélectionnez `Préférences` dans la barre latérale de droite, puis `Administration` -> `Paramètres du site` à gauche.

Ici, vous pouvez configurer les informations de base liées à votre instance et télécharger vos actifs de marque.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-59.png)

Celles-ci seront affichées sur la page `/about` de votre instance, présentée aux utilisateurs lorsqu'ils s'inscrivent/se connectent (et disponible dans le pied de page).

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-66.png)

Lorsque vous êtes prêt à commencer à accepter les inscriptions des utilisateurs, changez le paramètre `Mode d'inscription` en `Tout le monde peut s'inscrire` ou `Approbation requise pour l'inscription`.

## Comment gérer les utilisateurs

Sous l'onglet `Modération` -> `Comptes` dans les paramètres, vous pouvez voir les utilisateurs inscrits et en attente.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-63.png)

Si vous cliquez sur un nom d'utilisateur, vous serez redirigé vers la vue de gestion de l'utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-65.png)

À partir de cet écran, vous pouvez gérer leur niveau de permission (c'est-à-dire, accorder un statut de modération ou d'administrateur), vérifier les informations IP et bloquer les domaines d'email. 

Votre équipe de modération peut également laisser des notes privées (visibles uniquement par l'équipe) sur un compte utilisateur, pour aider à garder un historique des préoccupations de modération.

## Conclusion

Maintenant que votre instance est opérationnelle, n'hésitez pas à explorer les paramètres et les options d'interaction. Pour plus d'informations sur les différentes options, consultez la [documentation officielle](https://docs.joinmastodon.org/).

Vous pouvez trouver l'équipe principale de freeCodeCamp et les modérateurs bénévoles sur [notre instance privée](https://social.freecodecamp.org), où vous pouvez nous suivre depuis l'instance que vous venez de créer.

Profitez de votre nouvelle plateforme, et bon codage !

_Image de couverture provenant de la [page de mise à jour de la marque de Mastodon](https://blog.joinmastodon.org/2022/06/mastodon-branding-updates/)._