---
title: Comment créer un compte AWS Free Tier – Un guide étape par étape
subtitle: ''
author: Victoria Nduka
co_authors: []
series: null
date: '2025-07-15T17:06:54.633Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-aws-free-tier-account
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1752599184286/ff14fece-f865-4d8f-87e7-4cfed11a6946.png
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: AWS
  slug: aws
- name: AWS Free Tier
  slug: aws-free-tier
- name: Cloud Computing Services
  slug: cloud-computing-services
seo_title: Comment créer un compte AWS Free Tier – Un guide étape par étape
seo_desc: I recently started learning cloud engineering through a bootcamp. One of
  our first tasks was to create an AWS account. For those of us who didn’t already
  have one, it seemed like a simple enough assignment. But as I went through the signup
  process, I...
---

J'ai récemment commencé à apprendre l'ingénierie cloud grâce à un bootcamp. L'une de nos premières tâches était de créer un compte AWS. Pour ceux d'entre nous qui n'en avaient pas déjà un, cela semblait être une mission assez simple. Mais en suivant le processus d'inscription, j'ai rencontré quelques problèmes inattendus, notamment avec la vérification de ma méthode de paiement.

Lorsque j'en ai parlé dans notre chat de groupe, j'ai réalisé que je n'étais pas le seul. D'autres étaient également bloqués. Certains ne pouvaient pas vérifier leur numéro de téléphone, d'autres voyaient leur carte rejetée, et quelques-uns ne savaient même pas quel type de carte fonctionnerait.

C'est ce qui a inspiré ce guide.

Cet article vous guide à travers les étapes exactes pour créer un compte AWS, avec des conseils pratiques pour résoudre les problèmes courants (surtout pour les utilisateurs au Nigeria), basés sur des solutions qui ont fonctionné pour moi et pour d'autres.

## Table des matières

* [Qu'est-ce qu'AWS ?](#heading-qu-est-ce-que-aws)
  
* [Étapes pour créer un compte](#heading-etapes-pour-creer-un-compte)
  
* [Problèmes courants d'installation et comment les résoudre](#heading-problemes-courants-d-installation-et-comment-les-resoudre)
  
* [Conclusion](#heading-conclusion)
  

## Qu'est-ce qu'AWS ?

Imaginez que vous voulez un endroit où vivre. Normalement, vous devriez acheter un terrain, construire la maison à partir de zéro, gérer le câblage et la plomberie, et peut-être même superviser la construction. Après tout cela, vous devriez toujours meubler la maison – acheter des meubles, peindre les murs, peut-être faire appel à un décorateur d'intérieur. Ensuite, vous devriez contacter la compagnie d'électricité pour connecter votre maison au réseau… et ainsi de suite.

Comparez cela à la location d'une maison. Avec la location, une grande partie de ce travail est déjà faite. Vous emménagez dans un espace déjà construit. Si vous voulez repeindre ou obtenir des meubles différents, vous pouvez. Si l'électricité n'est pas déjà incluse, vous appelez quelqu'un pour vous aider. Mais vous traitez toujours avec plusieurs fournisseurs : le propriétaire, le décorateur d'intérieur, l'électricien, et ainsi de suite.

Imaginez maintenant qu'il existe un seul fournisseur qui vous donne accès à tout en un seul endroit : un espace prêt à l'emploi, de l'électricité, des meubles, de la décoration intérieure et même de la maintenance, le tout à la demande – comme un appartement pré-meublé. Tout ce que vous avez à faire est de vous connecter à votre compte, de sélectionner les services dont vous avez besoin et de payer uniquement ce que vous utilisez. Si vous êtes absent pendant un certain temps (par exemple, en vacances prolongées), vous pouvez suspendre vos services publics pendant votre absence. C'est essentiellement ce qu'AWS fait, mais pour la puissance de calcul et l'infrastructure numérique.

Amazon Web Services (AWS) est une plateforme qui vous donne accès à des outils informatiques tels que des serveurs (EC2), du stockage (S3), des bases de données, et bien plus encore, sans avoir besoin de "construire la maison" vous-même. Vous ne payez que pour ce que vous utilisez. La plupart des gens (surtout les étudiants ou les apprenants) commencent par le niveau gratuit, qui vous offre suffisamment de ressources pour apprendre et construire des projets de base sans être facturé. Et c'est ce que vous apprendrez à configurer ici.

## **Étapes pour créer un compte**

Il y a 5 étapes impliquées dans la création réussie d'un compte AWS Free Tier. Nous les passerons en revue une par une.

### Étape 1 : Configurer et vérifier votre adresse e-mail

Allez sur [aws.amazon.com](https://aws.amazon.com) et cliquez sur **"Créer un compte"** en haut à droite de l'écran.

![La page d'accueil d'AWS avec le bouton "créer un compte" mis en évidence](https://cdn.hashnode.com/res/hashnode/image/upload/v1751572272275/7a9cdf0a-8afd-4b26-b5ca-4dffb2d82cd6.png align="center")

Vous devriez être redirigé vers la page d'inscription. Mais vous pourriez être redirigé vers la page de connexion à la place. Si cela se produit, faites défiler un peu vers le bas jusqu'à ce que vous voyiez le bouton **"Nouveau sur AWS ? Inscrivez-vous"**. Cliquez dessus pour accéder à la page d'inscription.

![La page de connexion AWS montrant le type d'utilisateur (utilisateur root ou IAM) et le champ d'adresse e-mail. Le bouton "s'inscrire" est mis en évidence.](https://cdn.hashnode.com/res/hashnode/image/upload/v1751574858697/13ec0c92-93bb-4b3c-a12c-d280a754a70f.png align="center")

Sur la page d'inscription, vous serez invité à :

* entrer une adresse e-mail d'utilisateur root
  
* choisir un nom pour votre compte AWS (vous pouvez changer ce nom dans les paramètres de votre compte après votre inscription)
  

**Conseil :** Utilisez un e-mail que vous consultez régulièrement. AWS envoie des alertes importantes de vérification et de facturation que vous ne voulez pas manquer.

![La page d'inscription AWS montrant les champs d'adresse e-mail de l'utilisateur root et de nom de compte.](https://cdn.hashnode.com/res/hashnode/image/upload/v1751575004070/8c07161a-42d9-46dc-86b8-c8133f586e67.png align="center")

Ensuite, cliquez sur **"Vérifier l'adresse e-mail"**. Un CAPTCHA basé sur du texte apparaîtra pour vérifier votre identité. Dans le champ fourni, tapez les caractères affichés et soumettez.

**Conseil :** L'icône de rafraîchissement vous permet de charger une nouvelle image si celle actuelle est difficile à lire. Vous pouvez également cliquer sur l'icône du haut-parleur pour obtenir un CAPTCHA audio si vous avez des déficiences visuelles.

![La page de vérification de sécurité avec CAPTCHA. Les boutons du haut-parleur et de rafraîchissement sont à droite du CAPTCHA.](https://cdn.hashnode.com/res/hashnode/image/upload/v1751579148594/9a1668ca-b09a-455b-a29f-43e62e30a702.png align="center")

Vous recevrez un code de vérification à 6 chiffres dans votre e-mail. Entrez le code dans la fenêtre contextuelle de confirmation d'e-mail, puis cliquez sur **"Vérifier"** pour vérifier votre adresse e-mail.

**Conseil :** Si vous ne trouvez pas le code dans votre boîte de réception, vérifiez votre dossier de spam pour un e-mail d'Amazon Web Services. S'il n'y est pas, attendez jusqu'à 5 minutes, puis vérifiez à nouveau. Si vous ne le recevez toujours pas, cliquez sur le bouton "Renvoyer le code" pour que le code soit renvoyé à votre e-mail.

![Page de vérification d'e-mail avec un champ pour entrer le code de vérification reçu dans votre e-mail](https://cdn.hashnode.com/res/hashnode/image/upload/v1751579441960/ec052bc8-ec71-4b56-8210-0cb65e221760.png align="center")

Une fois votre e-mail vérifié, vous recevrez une notification de succès et, sur la même page, vous serez invité à entrer votre mot de passe. Votre mot de passe doit comporter au moins 8 caractères et doit contenir au moins 3 des éléments suivants :

* des chiffres
  
* des lettres majuscules
  
* des lettres minuscules
  
* des caractères non alphanumériques (tels que !, @, #, etc.)
  

Entrez à nouveau le mot de passe dans le champ "Confirmer le mot de passe de l'utilisateur root" et cliquez sur **"Continuer"**.

![Écran d'inscription au compte AWS montrant l'étape 'Créer votre mot de passe' pour la vérification de l'utilisateur root, avec des champs pour la saisie du mot de passe et un bouton 'Continuer'.](https://cdn.hashnode.com/res/hashnode/image/upload/v1751642655084/c7deb8c3-23f5-4821-961a-c66f984acf9e.png align="center")

### **Étape 2 : Entrez vos informations de contact**

Vous devrez choisir entre un compte **Personnel** ou **Professionnel**. Si vous vous inscrivez pour apprendre ou pour des projets personnels, l'option Personnel est suffisante.

Ensuite, vous devrez remplir vos informations de contact. Cela inclut :

* Votre nom complet
  
* Votre numéro de téléphone (avec l'indicatif du pays)
  
* Votre adresse
  
* Votre code postal
  

Ensuite, cochez la case qui dit "*J'ai lu et j'accepte les termes du Contrat Client AWS.*"

![Écran de création de compte AWS montrant le formulaire d'informations de contact avec le champ de nom et les options de sélection de type d'utilisation (Professionnel ou Personnel).](https://cdn.hashnode.com/res/hashnode/image/upload/v1751816749502/c7ab3be6-f2a5-476f-bbaa-cf6f1ee02651.png align="center")

### **Étape 3 : Ajoutez vos informations de facturation**

L'étape suivante consiste à entrer vos informations de facturation. Ici, vous devrez entrer :

* Votre pays de facturation
  
* Les détails de votre carte de crédit ou de débit
  
* Votre adresse de facturation (peut être votre adresse de contact ou une adresse différente)
  

![Écran de vérification de compte AWS montrant le formulaire d'informations de facturation, y compris la sélection du pays et les détails de la carte de crédit pour la validation d'identité. Le texte explique la retenue temporaire de 1 $ pour la vérification.](https://cdn.hashnode.com/res/hashnode/image/upload/v1751825939816/81343027-1231-4458-92de-7a1a57353c5c.png align="left")

Cliquez sur "Vérifier et continuer" pour passer à l'étape suivante.

**Note :** AWS peut temporairement bloquer jusqu'à 1 $ (ou un montant équivalent en monnaie locale) en tant que transaction en attente pendant 3 à 5 jours pour vérifier votre identité.

### **Étape 4 : Vérifiez votre identité**

Une fois que vous avez rempli vos informations de facturation, AWS vous demandera de vérifier votre identité en entrant un code qu'ils vous enverront. Vous pouvez choisir de recevoir le code par message texte (SMS) ou par appel vocal.

Entrez votre indicatif de pays et votre numéro de mobile et cliquez sur **"Envoyer SMS"** (si vous avez choisi l'option de message texte) pour continuer.

![Écran de vérification de compte AWS montrant l'étape d'authentification par numéro de téléphone, avec des options pour la vérification par SMS ou par appel vocal. Inclut le menu déroulant de l'indicatif de pays (Nigeria +234 sélectionné) et le champ de saisie du numéro de téléphone.](https://cdn.hashnode.com/res/hashnode/image/upload/v1751826368753/e77d6961-d949-430e-843a-9d9193687d98.png align="center")

Vous devrez compléter un autre CAPTCHA. Entrez les caractères de l'image affichée pour confirmer votre identité.

Entrez le code que vous avez reçu dans le champ et cliquez sur **"Vérifier et continuer"**.

Vous pourriez voir un message d'erreur indiquant : **"Il y a eu un problème avec vos informations de paiement."** Cela signifie qu'AWS n'a pas pu vérifier votre méthode de paiement. Lorsque cela se produit, c'est généralement dû à l'une des raisons suivantes :

* La carte que vous avez utilisée n'est pas acceptée par AWS
  
* Vous avez entré des détails de carte incorrects
  
* Le nom et l'adresse de facturation que vous avez fournis ne correspondent pas à ceux de votre émetteur de carte
  
* Votre carte n'a pas au moins 1 $ disponible pour la retenue temporaire
  

![Écran de message d'erreur AWS montrant l'échec de la vérification du paiement, avec des instructions pour mettre à jour les détails de paiement ou contacter le support.](https://cdn.hashnode.com/res/hashnode/image/upload/v1752326420973/33a9f33b-55aa-4539-9a2f-1d04ad701c32.png align="center")

Si vous obtenez cette erreur, AWS vous demandera de vous connecter et de mettre à jour votre méthode de paiement. Voici comment faire :

1. [Connectez-vous](https://signin.aws.amazon.com/) à votre compte AWS. Vous pourriez être automatiquement redirigé vers le tableau de bord de gestion des coûts et de la facturation. Sinon, utilisez la barre de recherche en haut de la page pour rechercher "Facturation", puis cliquez sur le service de gestion des coûts et de la facturation.
  
2. Dans le menu de gauche, faites défiler vers le bas et cliquez sur "Préférences de paiement".
  
3. Cliquez sur **"Modifier"** à côté des détails de votre carte existante pour corriger le nom et l'adresse de facturation, ou cliquez sur **"Ajouter une méthode de paiement"** pour entrer une nouvelle méthode de paiement.
  
  ![Tableau de bord des préférences de paiement AWS montrant une alerte de carte Mastercard non vérifiée avec des instructions pour résoudre les problèmes de vérification de paiement.](https://cdn.hashnode.com/res/hashnode/image/upload/v1752329795101/a4106217-e747-4a20-a099-7d1a8bcb5e04.png align="center")
  

### **Étape 5 : Choisissez un plan de support**

Ensuite, AWS vous demande de choisir un plan de support. Sélectionnez le plan **Support de base (Gratuit)**. C'est le plan recommandé pour les nouveaux utilisateurs qui commencent avec AWS.

![Écran de sélection du plan de support AWS montrant trois options hiérarchisées : Support de base gratuit pour les débutants, plan Développeur à 29 $/mois avec assistance aux heures de bureau, et plan Entreprise à 100 $/mois avec support de production 24/7.](https://cdn.hashnode.com/res/hashnode/image/upload/v1751827793660/0e4b9aec-62fc-42cf-a11b-822251377ff6.png align="center")

Vous aurez toujours accès au niveau gratuit AWS, qui inclut :

* 750 heures de calcul EC2
  
* 5 Go de stockage S3
  
* et bien d'autres services que vous pouvez essayer gratuitement (jusqu'à 12 mois)
  

**Note :** Vous pouvez mettre à niveau votre plan plus tard si nécessaire. Pas besoin de payer maintenant.

### **Étape 6 : Connectez-vous et explorez la console**

Une fois tout vérifié, vous pourrez vous connecter à la [Console de gestion AWS](https://console.aws.amazon.com/). C'est votre tableau de bord pour gérer tous les services AWS, de la configuration de serveurs virtuels (EC2) à l'expérimentation avec le stockage (S3) ou les bases de données (RDS).

**Note :** Parfois, il faut quelques heures pour que votre compte devienne pleinement actif. Si cela prend plus de 24 heures, contactez le support AWS par chat ou e-mail.

![Écran final de création de compte AWS montrant le message de succès d'activation avec notification de progression. Inclut deux boutons d'action : 'Aller à la Console de gestion AWS' et 'S'inscrire pour un autre compte'.](https://cdn.hashnode.com/res/hashnode/image/upload/v1752332214646/570608e0-6e7d-46a0-83c2-41d60604792e.png align="center")

## **Problèmes courants d'installation et comment les résoudre**

J'ai résumé les problèmes les plus courants que j'ai rencontrés ou entendus avec des solutions rapides ici :

| **Problème** | **Cause** | **Solution** |
| --- | --- | --- |
| Échec de la vérification du paiement | 1. Carte naira locale rejetée | 1. Utilisez une carte virtuelle en dollars (par exemple, Geegpay, Grey, etc.) |
|  | 2. Les informations de la carte ne correspondent pas aux informations de facturation | 2. Faites correspondre le nom, l'adresse et le code postal exactement |
|  | 3. Informations de facturation incorrectes | 3. Modifiez la méthode de paiement avec les informations de facturation correctes (nom complet, adresse de facturation et détails de la carte) |
|  | 4. Solde insuffisant sur la carte | 4. Ayez au moins 1 $ sur votre carte pour la retenue temporaire |
| Code de vérification non reçu | Échec du réseau ou du SMS | Essayez un autre réseau mobile ou utilisez l'option d'appel vocal |
| Bloqué après l'inscription | AWS traite toujours votre compte | Attendez quelques heures, puis contactez le support si nécessaire |

## **Conclusion**

La configuration de votre compte AWS est une étape importante dans votre parcours cloud. Une fois que vous êtes inscrit, vous pourrez explorer des outils puissants, construire des projets et acquérir une expérience pratique, le tout dans le cadre du niveau gratuit.

Si vous lisez ceci parce que vous commencez comme moi, bravo. Vous avez déjà franchi l'une des étapes les plus importantes. Continuez à apprendre, continuez à construire et n'ayez pas peur de demander de l'aide lorsque vous en avez besoin.