---
title: Comment connecter un nom de domaine à un site web hébergé sur AWS EC2
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-02-19T23:51:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-connect-a-domain-to-a-website-hosted-on-aws-ec2
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/my-hashnode-technical-blog-images.jpg
tags:
- name: AWS
  slug: aws
- name: ec2
  slug: ec2
seo_title: Comment connecter un nom de domaine à un site web hébergé sur AWS EC2
seo_desc: 'By Obed Ehoneah

  You may want to host your website on a virtual private server or a virtual machine
  like AWS EC2. But it can be a challenge to connect a domain name that you purchased
  from providers like Namecheap or Godaddy.

  But if you know the steps...'
---

Par Obed Ehoneah

Vous souhaitez peut-être héberger votre site web sur un serveur privé virtuel ou une machine virtuelle comme AWS EC2. Mais il peut être difficile de connecter un nom de domaine que vous avez acheté auprès de fournisseurs comme Namecheap ou GoDaddy.

Mais si vous connaissez les étapes à suivre, cela ne doit pas être difficile.

Dans cet article, je vais décomposer tout le processus de connexion d'un nom de domaine à un site web hébergé sur EC2. Je vais vous montrer comment le faire pratiquement avec des captures d'écran vous guidant à chaque étape. J'utiliserai un domaine Namecheap dans cet exemple.

Il y a 4 étapes majeures que vous devrez suivre, et cela ne devrait pas être trop compliqué si vous suivez la discussion dans ce tutoriel. Les voici :

* Étape 1 : [Installer votre site web sur EC2](#heading-installation)
* Étape 2 : [Configurer Route 53 pour la gestion DNS](#heading-etape-2-configurer-route-53-pour-la-gestion-dns)
* Étape 3 : [Mettre à jour les serveurs de noms avec votre fournisseur de domaine](#heading-etape-3-mettre-a-jour-les-serveurs-de-noms-avec-votre-fournisseur-de-domaine)
* Étape 4 : [Attendre la propagation](#heading-attendre-la-propagation)

Commençons.

## Étape 1 : Comment installer votre site web sur EC2

Tout d'abord, visitez [https://aws.amazon.com/console/](https://aws.amazon.com/console/). Cliquez sur le bouton de connexion en haut à droite ou sur le bouton "Se reconnecter" au milieu.

![Image](https://lh7-us.googleusercontent.com/1P8t02v71WBoFie3Noxs-9-32Ckege-I36ZM4vpfsXqBiSrJTeOgvOA2F9FCTPBTFo4fkWUhwxCDIXAiB2ZTyPgRXqJpyYOGIv7EhV2AS01LnsMilBBCgvgYwKxVauR70bKfIQ3FVFD7JrrPwW_9A94)
_Console de gestion AWS_


Créez un compte si vous n'en avez pas déjà un. Sinon, connectez-vous avec vos identifiants.

![Image](https://lh7-us.googleusercontent.com/_4dJQGRVfyRepII17I6GGUmpHiEJ_YShtzztq9SBMPS8GIqk79HdS_678Cue6g7Ws06LlV28ity_Nqjwk8QJkF3SZOUgSdImmdTbOhfvpUWXZ4foziwGLkwtL1NJdTfiHnje9k9GwugtjxGRP2b14fU)
_Page de connexion utilisateur_

Après vous être connecté, vous serez redirigé vers le tableau de bord principal.

![Image](https://lh7-us.googleusercontent.com/1ten0edaOEW9fyi94wZJDYLAO4iwjMOxpR9iVX9Q-52fnDO8_W2zq85Jm9y70K0Nm32twNDmEFmFjQ1FYUvkW7iqcfHpaeBCRSZqYWSIYouvkmgvScm4p15zeH6r6El_6S23mW_GBTCd-OQ3DC-FUs4)
_Tableau de bord utilisateur_


Dans la barre de recherche tout en haut, vous pouvez rechercher EC2 et cliquer sur la première option sous Services.

![Image](https://lh7-us.googleusercontent.com/wVnUvVADZoMmKBmWMTGjA79mBeSni4Ie7U6IuvatJNeglH1ss4-JPapyqWUNHuCTEmxHm4_Wl12jhL4Y7DbSmhO_HqFhLCRxxqfT9N_2K3o_0Sp5t_5xoAagztYd5ZXIoTX_qCZTTh07VA99E1pQRsE)
_Recherche de EC2_

Cela ouvrira alors le tableau de bord EC2 qui vous donne un résumé de toutes les ressources EC2 que vous utilisez. Si vous n'en utilisez aucune, alors il est probable que la valeur pour chacune soit zéro.

![Image](https://lh7-us.googleusercontent.com/G7PsvT8tE97xb4pp75H1Kmta3Jdv_A8xIWtAROQXz7vNNYQ2O6g8VliULPxLQmcGwOxf_BXcwE_QBrKtLVqdlM-8j5BSkJUzfGiI6NDBtCaAsyMRwxC7Oj_HEDkNt0_CcgEL-yOqgfPws1ZMs4PAutQ)
_Tableau de bord EC2_

### Lancement d'une instance EC2

Cliquez sur le bouton Lancer une instance.

Sur la page "Lancer une instance", vous sélectionnerez les spécifications pour la machine virtuelle destinée à héberger votre site web ou votre application web. Initialement, attribuez un nom à votre machine pour une identification facile.

Pour cet exemple, j'ai utilisé le nom "FC Web Server".

![Image](https://lh7-us.googleusercontent.com/PGh6o3yysjEl5xkqof7IvhE7Dg0eU6SWO9fmRaRY0sEUJoWLPiXcunxQQ4MI1Z_k1oaGbymInJLxTJv9l02pcmrfxi_YPjRZdPnW72PojjOTwqtihrtFVUwK5FZw-y_d1UyrdcjOafbr_KlIlKQkN_4)
_Nommer votre instance EC2_

Choisissez l'Amazon Machine Image (AMI) qui représente le système d'exploitation spécifique et les applications que vous souhaitez avoir par défaut sur votre machine virtuelle lorsque vous la démarrez.

Pour cet exemple, j'ai sélectionné Ubuntu, et j'utilise l'Ubuntu Server 22.04 LTS éligible pour le niveau gratuit comme AMI. J'ai laissé l'architecture en 64-bit (x86).

![Image](https://lh7-us.googleusercontent.com/T2FD0Pwnrkni6FWDuK1P_NFgPVmoV63I9QRFFLPt6HijKo4MuBGZr8Kua4ELs8p9ThtDYOF4juugnrZOYi3G9Pq4u1GkF-V8ZJjUq3rj9zg1pCyAwJj-0L3-vi-CFs8G718iZlVFPgSzGsjOPY7G61Y)
_Choix d'une Amazon Machine Image_

Pour le type d'instance, vous pouvez également rester avec le t2.micro éligible pour le niveau gratuit - mais si votre application ou site web nécessite plus de ressources, alors vous devrez choisir l'instance la plus appropriée en fonction du nombre de vCPU et de mémoire requis.

![Image](https://lh7-us.googleusercontent.com/L-syY4yUQNlpzBn_3EchnBFOPzCcVs_6yOgtdjljp05Gn6cTr0XLONAiDY_nNuILJq4tV2y5yug6IJdEagCu599FanEYkrV9QrKwbwpxqAD0EOGpZJcDQob1A99y3E977vV7BaY1m9oBxLyfA79YJ5A)
_Choix du type d'instance_

Pour vous connecter de manière sécurisée à votre machine virtuelle, vous aurez besoin d'une paire de clés SSH. Allez-y et cliquez sur le lien Créer une nouvelle paire de clés sous la section Paire de clés si vous n'avez pas déjà une paire de clés existante que vous pouvez utiliser.

![Image](https://lh7-us.googleusercontent.com/35slbh7seL4zxMwSnR4ZrZPddFJ0yAOxvJIPatukKXAb0wIbuJ9wfOWRdbGHSFJRaMUsSiCV0-d-NiZqMe0gQVppGCU4WbMyN33XcrOvnwmXtf1ZEeMYJhyAAugpcawQ7jz2zuwiX6Yiyy7_xwOLOH0)
_Création d'une paire de clés_

Donnez un nom à votre paire de clés que vous pouvez facilement identifier. Définissez le type de paire de clés sur RSA et le format de fichier de clé privée sur .pem. Vous pouvez également utiliser .ppk si vous êtes dans un environnement Windows et savez comment utiliser PuTTY.

Cliquez sur le bouton Créer une paire de clés. Après avoir cliqué dessus, le fichier sera automatiquement téléchargé. Assurez-vous de garder ce fichier dans un endroit sécurisé.

Passez aux paramètres réseau. Vous devez configurer un pare-feu qui contrôle les différents protocoles par lesquels votre site web ou votre application web peut être accessible. Pour cet exemple, vous pouvez choisir Créer un groupe de sécurité et autoriser SSH, HTTPS et HTTP.

Vous pouvez laisser l'adresse IP sur N'importe où 0.0.0.0/0.

![Image](https://lh7-us.googleusercontent.com/pmqY3ZoEQF7G0EcQPi49Ik6LjrwM3AkK3k2pgXbC4YpEn61ISeXjZID3l2cIK2cyNMrRKSTksLtRNeOZQ4zRyTAyKHZcxattdNOgY5bLunSvKzMJI8gaDovxxYKz6yKc-LXPPwVrG3xtc_SxjhLXMoY)
_Paramètres réseau pour votre instance_

Enfin, vous devez configurer les options de stockage. Vous pouvez également opter pour le gp2 par défaut de 8 GiB. Vous pouvez ignorer les détails supplémentaires et cliquer sur le bouton Lancer l'instance.

![Image](https://lh7-us.googleusercontent.com/og9GB9frMs-IFbrDxUhwS5FXefMLDISspiJCMhskzN0nX9JVabNKbo-VWw-HQ1q9Tq7_ONdQRGAzbttG_nbEuWihA2mjVX-BZNFOL32pEyzz0JNUR6ESr3-M8TWwckI7IfslpirqkXKULWg06Ag7ssI)
_Configuration du stockage pour votre instance_

Après que l'instance a été lancée avec succès, vous recevrez un message de succès.

![Image](https://lh7-us.googleusercontent.com/qNgmnZI1S2YUOoSc6Pv92rlo40HDxFquPmXOP_1Qdqx103KxBfsSZyzw1Q6xDpy2J7q_3cIdXHpsGsa8B3NEeTYAaImUk31nf4M5DmgXeQouwYQKwDzo9YYWD9akS0tfv7xPHhbFeANXAfR4AXe041I)
_Message de succès après le lancement de l'instance_

### Connexion à une instance EC2

Vous avez maintenant créé votre machine virtuelle - vous devez donc vous y connecter et la démarrer. Vous pouvez le faire en cliquant sur Se connecter à l'instance. Vous pouvez également cliquer sur Voir toutes les instances pour voir l'instance que vous avez créée.

Si vous cliquez sur voir toutes les instances, cela vous amènera à cette page où vous voyez votre instance (voir ci-dessous). Si vous n'en avez qu'une, alors vous verrez quelque chose comme ce qui est montré ci-dessous. Mais si vous avez d'autres instances, alors vous verrez toutes les instances créées dans cette même région AWS.

![Image](https://lh7-us.googleusercontent.com/kKXsADE-G5yS_Z0EKK6KQx7QviZnJrrhAyorzGJC6DPPH53aXcVWmxW_AjvpfwrAtYNzIS6JF3uKySS2R3ehgQGxKmCFL-lGAqtCSsA9sB95HIr15XP3gVCb9hNcU9ca8nZX_ocgmNGpWhCSt_a5LfE)
_Liste des instances EC2 lancées_

Sélectionnez l'instance spécifique que vous venez de créer et cliquez sur le menu déroulant Actions en haut à droite. Vous pouvez ensuite cliquer sur Se connecter dans le menu déroulant.

![Image](https://lh7-us.googleusercontent.com/HlYh7FNpoUi-BvMCg_J9hANAg9w0HWoISqCquGaJ5agnv5a6fpkG29qqpPsh8D47ntjd35TZY5e6FyQF2SxzQ4VmsBoY2uFigDIXsl-zy7xWAP6d-g92s-uDyqk1NITQ3c6hnax5hWx87dOS-IZ6FUQ)
_Connexion à l'instance sélectionnée_

La troisième façon dont vous auriez pu atteindre la page de connexion à l'instance est de cliquer sur l'ID de l'instance dans la liste des instances. Cela vous amène à la page de l'instance avec des détails sur votre instance sélectionnée. Vous trouverez ensuite un bouton Se connecter en haut à droite.

![Image](https://lh7-us.googleusercontent.com/TjXw51BB3V9HLxnXsKszZUyIRNzAwa_GvobWLHxPzYf0QnrzCLofCa8TGVspGR5NpfDniXSiiYkEtxpmsAkHHlz8XXVdqZhd_Xn5H3gaVkECfHCFAWmbA23Ni8-GUTrYzwk0tGKfgW28xJt9SFckaOM)
_Détails sur l'instance sélectionnée_

Sur la page **Se connecter à l'instance**, plusieurs options s'offrent à vous pour vous connecter à votre instance. Pour cet exemple, vous pouvez utiliser EC2 Instance Connect. Cette option vous permettra de vous connecter à votre machine virtuelle via le navigateur. Vous pouvez conserver les valeurs par défaut et cliquer sur le bouton Se connecter.

![Image](https://lh7-us.googleusercontent.com/SjIELpNqBcMXahNHK_dJx3Jhky8CdXxr0kbdhOpWqQZ-nM3BLEQ9A8uGv4Uh-alBNA5aYWDuXOGEw_MS48VM3InAQQJquHHvq2yl7FYlk98GDy0QDd0a9LFaGENVUMM9Sucz7Rc1ti6LjeZuKPTsLGw)
_Options pour se connecter à l'instance_

Cela ouvre un terminal dans le navigateur. C'est votre machine virtuelle. N'oubliez pas que vous avez installé Ubuntu, vous avez donc maintenant accès à une machine Ubuntu avec toutes les spécifications que vous avez sélectionnées.

![Image](https://lh7-us.googleusercontent.com/KdV49cJVMg2EEVOdVkhZNWbG9qtA2u0H3OahaZDCnkoTcgjnZBuI4ZWY_GQKG1o_fbUkocBljYl8RB2LbVG969eq6az-R8csZEXAIxo74mv-1frHdrE_pAwwwHsa4CCHz1eM2rHynGX6NeFAtgineEg)
_Terminal Ubuntu ouvert dans le navigateur_

Il est maintenant temps pour vous d'installer NGINX. Suivez les étapes ci-dessous pour installer NGINX sur votre instance.

### Mettre à jour votre liste de paquets

Utilisez cette commande pour mettre à jour vos listes de paquets :

`sudo apt update`

![Image](https://lh7-us.googleusercontent.com/cnk6SxfwNaz-dsEUd1C3AcaM1Ueh-GGTRCRTEoRNDYKIs_Gp2bU1JwsBwLzd05mwGLrDjVscZuWq2mu-6CU0Ch5Tx7TQ0rraMc3_BVUIGtBH8jjsQcH7FlkYR5vRBQ33jvUVc6bIIQ5RHAkY24bHyQg)
_Mise à jour de la liste de paquets_

### Installer NGINX

Utilisez cette commande pour installer NGINX :

`sudo apt install nginx -y`

![Image](https://lh7-us.googleusercontent.com/5xyqlguhGA2pCjltDJXeLFKNsm-HaKTlDab6QjmlucpBWRLGdEbjoFg5_5FJ3xV73s047_ycOX59A7Yphq4xyKBZmcv1NfWySx3G6nqi6a8e2XgQutrJBWazwR4UlYi9CA49c-8TL2-7E7PVRml6h38)
_Installation de NGINX_

Une fois l'installation terminée, vous pouvez accéder à la page par défaut de NGINX en entrant l'adresse IP publique de votre instance dans la barre d'adresse de votre navigateur.

Pour trouver l'adresse IP publique, vous pouvez vérifier le bas de votre terminal ou aller à la page de l'instance et chercher l'adresse IPv4 publique.

![Image](https://lh7-us.googleusercontent.com/hYkF9Fvl2yc-W6kR5XWQWGTnEINJbEdj3k9_SQZUGcdb_MQ3MgQ6fKOh791HgxEdDXC28g2Mazk04n-JsM1xwT2TttF5u_vZQqp5aUD963ZzKelbImsPqW_1ePkI0FNFH-mPT0QC3CWhzgYxQZxLmos)
_Adresse IP publique de l'instance depuis le bas du terminal_

![Image](https://lh7-us.googleusercontent.com/86hZhXn99AFBdk-gZ6fqa-yLLzJqqAASd43rL0zM-kD0ZflQJ_65yP4s4bSKcxYFvaPiLThaX948B8Q12iQrmeQw8rwkbCwrhP-RdWdU2ZOhUz1OVTTHr7BbEYFxDtX_Obpfj7rqHhzAjgqntzW0s4g)
_Adresse IP publique de l'instance depuis la page des détails_

Vous devriez obtenir la page par défaut ouverte dans votre navigateur comme montré ci-dessous :

![Image](https://lh7-us.googleusercontent.com/JZPEFIWMHIUAWSURn80p-AEYsWukl-W5Um2YZ9ce5d4Ox9H8UQozMnYCltaLTBfbzl_tvmZ3Fn6tJEO_VOv-_1ne7F8ElYIUexdg9I7JgySqSmI2yo0b2fmT0zJYxHArDYxY39LTsmDrRbmG6M5ZKsQ)
_Page par défaut pour le serveur web NGINX_

NB : Vous devrez peut-être actualiser la page pour que cela fonctionne.

Pour les prochaines étapes de configuration de votre site web ou de votre application web, cela dépendra du langage de programmation ou du framework que vous avez utilisé. Mais comme ce tutoriel est axé sur la connexion d'un nom de domaine à votre EC2, vous pouvez passer aux étapes suivantes pour connecter le domaine.

![Image](https://lh7-us.googleusercontent.com/m9xoyqffR1ExdcIcXO7Ir5owVxyZgVP3z1iPaG_ISKUyIn6nwlCP_sJH-Yn6y64ZytEQkS0hLMXTirDdwHzAHnUrr0j8H4vj8v-2i1KATd7cDf7r8d47siBIEET12RKg68Q183mrw3XmXFnQG0l4gxE)
_Page par défaut de NGINX_

En partant de cette image, connectons maintenant notre nom de domaine à ce site web. Comme vous pouvez le voir dans l'image ci-dessus, j'y accède avec l'adresse IP publique de l'instance EC2.

Connecter le site web avec un nom de domaine signifie simplement remplacer son adresse IP par un nom plus mémorable. Dans notre cas, je vais le remplacer par le nom de domaine `krachy.com`.

## Étape 2 : Comment configurer Route 53 pour la gestion DNS

AWS fournit un service appelé Route 53 que vous pouvez utiliser pour la gestion DNS (Domain Name Service). Maintenant, nous devons configurer ce service pour gérer le domaine que vous avez acheté.

J'ai mon domaine avec Namecheap, mais le processus sera similaire pour presque toutes les autres entreprises de vente de domaines.

Tout d'abord, vous devrez créer une [zone hébergée](https://aws.amazon.com/route53/faqs/#:~:text=A%20hosted%20zone%20is%20an,domain%20name%20as%20a%20suffix.) dans Route 53.

![Image](https://lh7-us.googleusercontent.com/XVis1IAhzZ3CdJiDBOu9NXc66ER63DSDgfuWLL-zqiJStnsjEa0COfK-EtuKYnpjBr6gOouLcAYDQlhcrRX1YNIFbNk4qyzYIuLHqJ2Y3f1zo4Rz7OI0lv-MI2Z6g_AMvgoCcjY-5zNYernNhhCoUv0)
_Amazon Route 53_

### Création d'une zone hébergée dans Route 53

Pour cela, cliquez sur le bouton orange `Commencer`. Cela vous amène à la page suivante, comme montré ci-dessous.

![Image](https://lh7-us.googleusercontent.com/2ZJ658N8zV3L9UjxrRDqmAUSF-6se1J6yc0qBRO_tsATMijkY3k7cWc5D2TFIiC_PHLOEvukyQnVo5vJi7mQQq19y1bNJCeeYsvBQ_Of5RrfL7tjRfWYOfaPzRtjKiEKnENyU48ZxQeXr63R4IY9mU4)
_Options de démarrage pour Route 53_

Choisissez `Créer des zones hébergées` et cliquez sur le bouton `Commencer`. Allez-y et remplissez les détails sur la page suivante.

![Image](https://lh7-us.googleusercontent.com/ibfwFdt41BH4rgMKJ44-4qmcF-xUTePMD6WL7Q341AzcBM6KWUtrwvGAavwuZmEWNeImMVuPLQfRsfkaMKjiDSpfA1r5IRQEXo1crcbZL33vpNCH8hrbYetMUCuFYsTOXZrU18fe-H3NR_BCNdpdE3g)
_Configuration de la zone hébergée_

![Image](https://lh7-us.googleusercontent.com/-UmPq2sd9RuiNkRxwC545W0iXzSnofRok4d3XVJ4yMoxP4j7jM_WQp2FzUeptBEmlFknPgeB4DY3EjDUtlu-dGgwfLK-bCyCtHv4DyUxYHXWOYKv9V1M3Z-oyPrcJDKXULWPxFi7WTmkjWUsXi8oTwY)
_Fournir les détails pour la zone hébergée_

Fournissez le nom de domaine que vous souhaitez connecter à l'instance EC2, puis donnez-lui une description qui vous permettra de distinguer cette zone hébergée des autres que vous pourriez avoir. Choisissez `Zone hébergée publique` puisque vous souhaitez que votre site web soit accessible au public.

Cliquez sur le bouton orange `Créer une zone hébergée`.

![Image](https://lh7-us.googleusercontent.com/A4_iFzOVyOTal9QBXCCVAaI56OaNs-Z9yQfZKqDWzSbMj1sE953_z3kUi9v_L8hq25FBjgt-MolYw0pANYVsawS4oek9KkJpJikW6XWmDsaxEr2-XaPi_Um2Zl58MdNrsuw5CFKvFolNSxieIlduwnE)
_Message de succès pour la zone hébergée_

Vous recevrez un message de succès vert indiquant que vous avez créé avec succès la zone hébergée.

### Ajout d'enregistrements à la zone hébergée créée

D'après la capture d'écran ci-dessus, vous pouvez voir que Route 53 a automatiquement créé deux enregistrements pour nous : l'enregistrement NS (Name Server) et l'enregistrement SOA (Start of Authority). L'enregistrement NS est ce dont vous aurez besoin pour pointer votre domaine vers ce service. Mais avant de les récupérer, vous avez quelques choses à faire ici.

Parce que notre site web est hébergé sur une instance EC2 qui peut être accessible via son adresse IP publique, vous devez créer un **enregistrement A** pour celui-ci. De plus, pour vous assurer que les personnes qui tentent d'accéder à votre site web avec le sous-domaine `www` peuvent toujours y accéder, vous devrez également ajouter un autre enregistrement avec un **alias** pour celui-ci.

Pour cela, commencez par cliquer sur le bouton orange `Créer un enregistrement`, comme vous pouvez le voir dans la capture d'écran ci-dessous :

![Image](https://lh7-us.googleusercontent.com/0Sb2ip2tg_IvOAaumH1KB4V8d6XPFtBk9s1lBJ1lyTXHnia3kCe5VicjCqd-D1VX14fpGSoJp0GlskDDxtgOb8ztgFrGXJP_cHQgomH114x85tXrxQEC177Yn8pUsz3XghjBPc_OTRoUiBcuDA-500I)
_Ajout d'un enregistrement A_

Pour l'**enregistrement A**, ne mettez rien dans la zone de texte `sous-domaine`. Sous Type d'enregistrement, assurez-vous que `A - Achemine le trafic vers une adresse IPv4 et certaines ressources AWS` est sélectionné. Ensuite, collez ou tapez l'IP publique de votre instance EC2 dans la zone de texte pour Valeur.

Vous pouvez tout laisser par défaut (NB : Vérifiez pour vous assurer que la Politique de routage est Simple).

Pour obtenir l'adresse IP, visitez l'instance que vous utilisez et cherchez l'adresse IPv4 publique et copiez celle-ci.

![Image](https://lh7-us.googleusercontent.com/m1uIxp03So9xxaiE-YvmS9Px93lq48sMG0V6ZA84MmNsjHHn6eQZW6SyWN1nvacKelmqboYRG-RSJzViGtmJ1M9YOI8iX8dnmEKPiioPZhfE5sf65WhGHCfukTVY8OjfUvlNYpEgm-EF53AWwBigGXw)
_Adresse IP depuis la page des détails de l'instance_

Cela devrait maintenant ressembler à ce qui est montré ci-dessous (où 18.232.109.18 est l'IP publique de mon instance). Ensuite, cliquez sur le bouton orange `Créer des enregistrements` dans le coin inférieur droit.

![Image](https://lh7-us.googleusercontent.com/5oj2JsQt_YRKWqDSbINcSWbnK5ON3T1u49MI9TyYqhuSMkcaJ3SU__aYJjh7cc7730OVsIDVRC9WMiWzEshiDkYl1NIJ8cb6sdYmHQuvW9Y7kcYarxdBk-BcZ91zPHKyZkFIpWBJCZ4aI_ouyPWx374)
_Finalisation de la création de l'enregistrement A_

Vous devriez voir un message de succès. De plus, l'enregistrement sera maintenant ajouté au tableau des enregistrements que vous avez vu précédemment, comme montré ci-dessous :

![Image](https://lh7-us.googleusercontent.com/DlR8djeTU_JtBEWHJIbwxfhxHzI_ubQl5Bfx2X6f3qlpnDwr3R_xs1YuZN_2donh4sH8KTG1PRWicd7wjzLLcjjoRcdTOHENhKGpvcNDEecudxvYC3JAhCvvEh6rmgBOVKDAkF_rZWZrbyP61dV0SkI)
_Message de succès après la création de l'enregistrement_

Vous devez encore ajouter l'enregistrement pour prendre en compte l'utilisation possible de `www` lors de l'accès à votre site web. Cliquez sur le bouton `Créer un enregistrement` pour ajouter cet enregistrement. Cette fois-ci, vous mettrez `www` dans la zone de texte du sous-domaine.

![Image](https://lh7-us.googleusercontent.com/4JBcC8FFtVm9GLd3hl0wm3PptwXgpaySUlxdw2g1vWnu0g3jote---0v5MxLVTz6Ypj3yjAEngPx4XfUDgJ2-uShQiY5z8sKTI0yLiCJLH4saASR5xdwxLXSKyxzySYGBrgWa_E3LsdVBruMJ9dSIr8)
_Ajout d'un enregistrement A pour gérer l'utilisation de www_

De plus, vous devrez activer `Alias` qui se trouve sous le Nom de l'enregistrement. Après l'avoir activé, un nouvel ensemble d'options (Acheminer le trafic vers) sera disponible.

![Image](https://lh7-us.googleusercontent.com/xd5aFDvaDaCl6i4ZV-8ZHhmRTBcE8UDLjTe9N1p6ffOhRYFZuAt2ElEAGyXV4piLPk8pJD3e_uS-3MXBZDU5nN1n4XWHd9k49HYkrGeiZMtQl4935dhvhjzgC2wgS2tIpNSs4HARQ5Dl5hVZvZ6h1SY)
_Activation de l'Alias pour l'enregistrement_

Pour le menu déroulant `Choisir un point de terminaison`, sélectionnez `Alias vers un autre enregistrement dans cette zone hébergée` et la Région sera automatiquement remplie pour vous. Mais cela fait également apparaître un autre champ intitulé `Choisir un enregistrement`.

![Image](https://lh7-us.googleusercontent.com/tzVQSFj6MyEhnT-7p_310X_DgbuucKT3BqKmbgIUqihIAfdiFvJw83HTlpG8mGVdhOFjyCOn0lFSkFFlgdk2sQH9aE6fINs29BoyPZs35uZwbP-p76mGU9cFGBnqFmHNVVaRWJd-G2MxTGRBldM4TMA)
_Sélectionner une option pour "Acheminer le trafic vers"_

Allez-y et cliquez dans le champ `Choisir un enregistrement` et il vous suggérera votre nom de domaine. Allez-y et sélectionnez-le.

![Image](https://lh7-us.googleusercontent.com/cCGijn9B6_j8BtxIs-zncIDZyRoRsb66JdeLPJv4-RgSNlbT8aZr6CELWboC7zYfuspwoRE3bhlOKvCeZ4RFESKzmA47SoYTX5N9119kdA9QxC6gw2e2895IK3Vlo5tWwyOs62zYESw22keeTWs3nU4)
_Associer le domaine avec l'enregistrement_

Vous êtes maintenant prêt à ajouter cet enregistrement aussi, alors procédez en cliquant sur le bouton `Créer des enregistrements`. Vous recevrez un message de succès et verrez que le nouvel enregistrement a été ajouté au tableau des enregistrements.

![Image](https://lh7-us.googleusercontent.com/2SmlaORdC9UHuNL_FDJxTKNUBTqfRloS3jK1TtB4N_mzfVIWwXI-N33kd2qizIGlUGvuGm1lvBUdMj3T99BnG6t-AcOiZd2mQk-dnBY-i2rLr7OWVwwO8VaEauOLsIpk2r7pqQFujv5OWw_dIzjC0DY)
_Message de succès après l'ajout du nouvel enregistrement_

Une fois que vous avez terminé la configuration des enregistrements, vous pouvez maintenant procéder à la mise à jour de vos serveurs de noms avec notre entreprise de vente de domaines (NameCheap dans mon cas).

## Étape 3 : Mettre à jour les serveurs de noms avec votre fournisseur de domaine

Si vous avez déjà un compte avec un fournisseur de domaine, connectez-vous à votre compte. Sinon, vous devrez vous inscrire auprès d'un fournisseur pour acheter un nouveau domaine.

Personnellement, j'utilise Namecheap pour la plupart de mes domaines. Je vais donc montrer comment faire cela avec Namecheap (mais encore une fois, cela sera similaire pour divers fournisseurs de domaines).

Notez que j'ai déjà un nom de domaine, et pour tout domaine que vous achetez, vous aurez certains serveurs de noms par défaut. Votre objectif ici est de changer les serveurs de noms par défaut ou ceux que vous avez actuellement par ceux que Route 53 vous fournit.

### Changer les serveurs de noms dans Namecheap

![Image](https://lh7-us.googleusercontent.com/Lkdxzcd7dt-85SamUv4R2c1OI0UY9W3zAqqlXljpI6x4ywSlFUxbPJ-y1F3CGHlxW6Laz55IaS542jSeZuo3uc_gQqsMEL4ysQEK4pR3i6Ig81GXXNjCB0uuqlWyrufEEGjYbMYvqIbT-4lbkeu72Qs)
_Tableau de bord utilisateur Namecheap_

Cliquez sur `Liste des domaines` pour voir une liste de tous les domaines que vous avez dans ce compte. Cherchez le domaine spécifique que vous avez.

![Image](https://lh7-us.googleusercontent.com/4eSm_L1erf8ma66aZNKJCQtFCjIgJgQ0i7mx013PJ6ZRZU-zp2gHOltqYrZFaworF9-sUGE5iW07joLUw4rlUnPx7aUiCdyxDCljZtFv7l5C5HViYdZh-my2aOXji55OaIwG2m7_anaUs1XPS-aR3fg)
_Liste des domaines_

À côté de chaque nom de domaine, vous trouverez le bouton `Gérer`. Cliquez sur celui correspondant au domaine que vous utilisez (krachy.com dans mon cas).

![Image](https://lh7-us.googleusercontent.com/sTT4r41ZnwwtG9FURnWSo4SDEvhhuiXXfhDrJDgSxg26Jk2VmWhLMkL-SWhQJ9b84l88LsPf-ywDaxnWpbI7VD44tl3Kprau26EoTzRRfo2cdcRPSxvqAnFCyGqnmQrMgrJ-zgXl-o6r_QBMxPRHgVc)
_Page de détails pour le domaine sélectionné_

Sous Serveurs de noms, assurez-vous d'avoir sélectionné `DNS personnalisé`. Ensuite, retournez à Route 53 et copiez les serveurs de noms qui vous ont été fournis. Ensuite, supprimez ce que vous avez actuellement et ajoutez ce que vous obtenez de Route 53.

Dans mon cas, Route 53 m'a donné quatre serveurs de noms différents. Je dois donc les copier un après l'autre et les ajouter à Namecheap (n'oubliez pas de supprimer les anciens qui étaient dans le compte du fournisseur de domaine).

![Image](https://lh7-us.googleusercontent.com/vq9KwsyF13Tmt00vHzDIkIMU47h_5EzB4CaXFUhrvjpIJqpWCI8qOcmXEkdqJS92d6up3nvVYq78gSE-4SHMATFxJWSNQJvdhZZW-SUh4tAOi4llNRIJwy4_Kj5qRhhuHHth1mDpQS08gTu_R-OcjGg)
_Serveurs de noms pour le nom de domaine_

Dans Namecheap, ils fournissent deux espaces pour les serveurs de noms - mais il y a un bouton juste en dessous qui vous permet d'en ajouter plus de 2. Dans mon cas, j'ai ajouté les quatre comme vous pouvez le voir ci-dessous :

![Image](https://lh7-us.googleusercontent.com/Bunq4l59Hm7HzrnOzqDwU1YesduGAhxdlpuOYVp8290Mc30rY3z3iwSg0D6LCra4t2JJ2ysGEWqdIdDA18YfGIEvdpWNMFuGkKF7k9RAJ-v-A1Z678QfdVJqv4GZUsDP9cjZnt6eNmlOoGFk4XpaPKg)
_Mise à jour des serveurs de noms_

De plus, après les avoir ajoutés, vous devez accepter les changements et les enregistrer. Dans la capture d'écran ci-dessus, vous pouvez voir qu'à l'extrême droite de `DNS personnalisé` se trouve une coche et une croix. Cliquez sur la coche pour enregistrer les changements.

Après avoir enregistré, vous remarquerez que ces boutons ne sont plus disponibles.

![Image](https://lh7-us.googleusercontent.com/7xuh7yPSzecl12m5BCblDIWBcXo27f5dqPK6huZpGLvZ-R2gH3wTYHaWCl02X3xTZLBAKWbNvGyyIPn4pkaMMQv6xO9nORX-BDZw21k_0hwVx4L8rSXYq0UuzTPTnhuSIFNLhbgWpl63BxXubJf5yDk)
_Serveurs de noms mis à jour sur Namecheap_

## Étape 4 : Propagation DNS

Félicitations, vous avez maintenant terminé la configuration. Maintenant, vous devez simplement attendre que la propagation DNS soit terminée.

Cette étape ne vous demande pas de prendre d'action, mais simplement d'attendre quelques minutes. La propagation peut prendre de quelques minutes à plus de 24 heures.

Mais après un court moment, entrez simplement votre nom de domaine dans la barre d'adresse de votre navigateur et voyez s'il affiche le site web que vous avez hébergé sur l'instance EC2.

Une fois la propagation DNS effectuée, votre site web sera en ligne sur le nom de domaine que vous avez utilisé. Félicitations une fois de plus !

![Image](https://lh7-us.googleusercontent.com/UOIjgyUqN4-DGBvTfLscjsnulDkapBsOvEfga7m-NkEkp8CriJfXEL-w1a6ZdlqIOc_ebkK1NLQm7H-tZDIOEMhcj3_cWfEUPLXjyob7aq4bU19qyN3lWHlL60G1pCH_AdrydjUE1KiZPC4gHCwwvQw)
_Site web lié au domaine après la propagation DNS_

Comme vous pouvez le voir, c'est la même interface avec laquelle j'ai commencé - mais la bonne nouvelle est que maintenant, j'y accède avec le nom de domaine que j'ai acheté et non avec l'adresse IP de l'instance.

## Conclusion

Même si vous avez terminé, vous utilisez actuellement un protocole de transfert non sécurisé (http) pour votre site web. Cela est dû au fait que vous n'avez pas encore installé de certificat SSL sur votre site web.

Restez à l'affût de mon prochain tutoriel où je vous guide à travers l'installation de SSL sur votre domaine pour le sécuriser (https).