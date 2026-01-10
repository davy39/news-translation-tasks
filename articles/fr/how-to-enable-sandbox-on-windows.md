---
title: Tutoriel Windows Sandbox – Comment activer le bac à sable sur Windows
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-04-11T20:13:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-enable-sandbox-on-windows
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/close-up-image-programer-working-his-desk-office.jpg
tags:
- name: virtualization
  slug: virtualization
- name: Windows
  slug: windows
seo_title: Tutoriel Windows Sandbox – Comment activer le bac à sable sur Windows
seo_desc: "Windows Sandbox is a temporary lightweight desktop environment that you\
  \ can use to safely run Windows applications in an isolated space. \nThe software\
  \ or applications that you install inside the Windows sandbox environment remain\
  \ \"sandboxed\", and the..."
---

Windows Sandbox est un environnement de bureau léger temporaire que vous pouvez utiliser pour exécuter en toute sécurité des applications Windows dans un espace isolé. 

Les logiciels ou applications que vous installez à l'intérieur de l'environnement Windows Sandbox restent « sandboxés », et ils s'exécutent tous séparément de la machine hôte. Ainsi, tout ce qui se passe dans le bac à sable y reste, et votre machine hôte reste 100 % sécurisée.

Comme le bac à sable est une instance temporaire de votre machine hôte, lorsque vous le fermez, tous les logiciels, données, fichiers et l'état sont également supprimés instantanément. Vous devez donc copier toutes les données/logiciels nécessaires dont vous aurez besoin plus tard du bac à sable vers la machine hôte avant de le fermer. 

Chaque fois que vous ouvrez le bac à sable, vous obtenez une instance complètement neuve. Cela signifie également que vous obtiendrez une instance complètement nouvelle de votre machine hôte qui agit comme un laboratoire d'expérimentation temporaire. Là, vous pouvez expérimenter avec n'importe quelle application/donnée Windows que vous souhaitez, sans risquer d'endommager votre machine hôte d'origine.

Selon la [documentation Microsoft](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-sandbox/windows-sandbox-overview),

> Windows Sandbox possède les propriétés suivantes :
> **Fait partie de Windows :** Tout ce qui est nécessaire pour cette fonctionnalité est inclus dans Windows 10 Pro et Enterprise. Il n'est pas nécessaire de télécharger un VHD.
> **Immaculé :** Chaque fois que Windows Sandbox s'exécute, il est aussi propre qu'une nouvelle installation de Windows.
> **Jetable :** Rien ne persiste sur l'appareil. Tout est supprimé lorsque l'utilisateur ferme l'application.
> **Sécurisé :** Utilise la virtualisation basée sur le matériel pour l'isolation du noyau. Il s'appuie sur l'hyperviseur Microsoft pour exécuter un noyau séparé qui isole Windows Sandbox de l'hôte.
> **Efficace :** Utilise le planificateur de noyau intégré, la gestion intelligente de la mémoire et le GPU virtuel.

💡(Windows Sandbox active la connexion réseau par défaut. Elle peut être désactivée en utilisant le [fichier de configuration Windows Sandbox](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-sandbox/windows-sandbox-configure-using-wsb-file#networking)). 

Dans cet article, j'utilise Windows 11 Pro. Le bac à sable Windows est également disponible pour Windows 10 comme le dit la documentation, et les processus sont presque identiques.

## Virtualisation avec Windows Sandbox

Ceci est une partie importante du bac à sable. Comme il s'exécute dans un espace élevé, il doit nécessiter la fonctionnalité de virtualisation. Vous devez vous assurer que vous avez déjà activé la virtualisation. 

Si vous vous demandez comment savoir si vous avez activé la virtualisation ou non, ne vous inquiétez pas – je vais vous le montrer !

Ouvrez le gestionnaire des tâches. Vous pouvez faire un clic droit sur le logo Windows et cliquer sur Gestionnaire des tâches, ou vous pouvez utiliser le raccourci **`Ctrl`  + `Maj` + `Échap`** pour cela.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-09-181256.png)

Après avoir ouvert le gestionnaire des tâches, allez dans l'onglet **Performances**. Ensuite, cliquez sur **UC** et vérifiez le statut de la **virtualisation** comme ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-09-181405.png)

Si le statut de la virtualisation indique qu'elle a déjà été activée comme c'est le cas sur la mienne, alors vous êtes prêt à passer aux étapes suivantes. 

Si elle indique qu'elle a été désactivée, alors vous devez l'activer depuis le BIOS. Je vais vous montrer comment activer la virtualisation ci-dessous.

## Comment activer la virtualisation sur votre ordinateur 

Tout d'abord, allez dans le BIOS. Selon le fabricant de votre BIOS, cela peut être l'une de ces touches pour entrer dans le BIOS pendant le démarrage : Suppr, Échap, F1, F2 ou F4. 

Lorsque votre écran devient noir pendant le processus de redémarrage, vous devez appuyer rapidement sur la touche BIOS (mentionnée ci-dessus) jusqu'à ce que le menu BIOS apparaisse. Si la touche que vous utilisez ne fonctionne pas pour vous, essayez de redémarrer votre ordinateur et faites le même processus en utilisant les autres touches mentionnées ci-dessus jusqu'à ce que vous trouviez la touche qui fonctionne pour vous.

Après être entré dans le BIOS, vous devez trouver la section pour la configuration de votre CPU. Vous pouvez la trouver sous l'onglet CPU, Processeur, Northbridge ou Chipset. Vous pouvez trouver la section de configuration en tant que section Avancé ou Mode avancé dans votre cas.

Après être entré dans la section de configuration du CPU, vous devez trouver l'option qui vous permet d'activer la virtualisation matérielle. Selon votre système, vous pouvez trouver des noms comme Hyper-V, Vanderpool, SVM (généralement les cartes mères de Gigabyte utilisent ceci), AMD-V, Intel Virtualization Technology ou simplement VT-X.

Activez cette option qui apparaît dans votre cas. Si vous voyez AMD IOMMU ou Intel VT-d, activez-les également. 

Ensuite, vous devez enregistrer les modifications. Vous pouvez utiliser les touches de raccourci pour cela également, qui devraient être affichées sur votre BIOS. La plupart des fabricants utilisent F10 pour enregistrer la configuration du BIOS. 

Ensuite, vous devez quitter le BIOS. Votre ordinateur redémarrera une fois de plus. Ensuite, si vous vérifiez le statut de la virtualisation depuis votre gestionnaire des tâches, vous verrez qu'elle a été activée !

Maintenant, je peux supposer en toute sécurité que la virtualisation a été activée sur votre ordinateur.

## Comment activer Windows Sandbox

Cliquez sur le bouton démarrer ou le bouton de recherche et recherchez les fonctionnalités Windows.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--1-.png)

Cliquez sur **Activer ou désactiver des fonctionnalités Windows**.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--2-.png)

Cela ouvrira la fenêtre **Fonctionnalités Windows** comme sur l'image ci-dessus.

Faites défiler vers le bas jusqu'à ce que vous trouviez **Windows Sandbox** :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--3-.png)

Assurez-vous d'avoir coché la case comme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--4-.png)

Ensuite, cliquez sur **OK**.

Il commencera à rechercher les fichiers requis.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--5-.png)

Ensuite, il appliquera les modifications tout seul.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--6-.png)

Après avoir terminé les modifications demandées, il vous demandera de redémarrer votre système. 

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--7-.png)

Cliquez sur **Redémarrer maintenant**.

Après avoir redémarré votre ordinateur, votre ordinateur est complètement prêt à utiliser le bac à sable Windows.

## Comment tester Windows Sandbox

Cliquez sur le menu démarrer ou la barre de recherche et recherchez **Windows Sandbox**.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--9-.png)

Windows Sandbox s'ouvrira après cela. Ne craignez pas si vous obtenez un écran noir comme ci-dessous, car c'est normal lorsque vous démarrez le bac à sable pour la première fois.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--10-.png)

Après un moment, vous verrez qu'une nouvelle instance de votre machine hôte est apparue devant vos yeux.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--11-.png)

Vous pouvez maximiser la fenêtre du bac à sable si vous le souhaitez.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--12-.png)

Maintenant, vous pouvez expérimenter dans votre bac à sable. Cela donnera l'impression que vous utilisez votre machine hôte principale, mais ce n'est pas le cas. Vous utilisez une machine virtuelle temporaire avec des privilèges élevés dans un environnement isolé – et quoi que vous fassiez dans ce bac à sable, votre machine hôte restera intacte !

N'est-ce pas génial, non ! 😍

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--13-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--14-.png)

Si vous souhaitez ajouter des données/logiciels à l'intérieur de votre bac à sable, vous devez les copier-coller comme vous le faites normalement sur votre ordinateur. Copiez simplement le fichier/logiciel que vous souhaitez utiliser à l'intérieur du bac à sable, et dans la fenêtre du bac à sable, collez-les simplement.

## Comment fermer le bac à sable

Faites attention ici ! Tout ce que vous faites et gardez dans votre bac à sable se passe dans une instance temporaire. Rappelez-vous qu'il n'est pas enregistré ailleurs dans votre machine hôte pour une utilisation ultérieure. 

Une fois que vous fermez le bac à sable, toutes les données/applications que vous gardez dans ce bac à sable seront supprimées instantanément.

Avant de fermer le bac à sable, vous devez vous assurer que vous n'avez pas gardé quelque chose d'important dans le bac à sable dont vous pourriez avoir besoin par la suite, même après avoir fermé le bac à sable.

Lorsque vous souhaitez fermer le bac à sable, fermez simplement la fenêtre du bac à sable. Une invite apparaîtra vous informant que, une fois la fenêtre fermée, tous les fichiers/applications que vous avez dans le bac à sable seront perdus à jamais.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--15-.png)

Si tout est correct, cliquez simplement sur OK. Cela fermera le bac à sable. 

Si vous devez ouvrir à nouveau le bac à sable, ouvrez-le simplement comme précédemment et effectuez vos tâches. Tous les processus sont exactement les mêmes.

## Conclusion

Merci d'avoir lu l'article entier. Si cela vous aide, vous pouvez également consulter mes autres articles sur [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

Si vous souhaitez me contacter, vous pouvez le faire via [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/) et [GitHub](https://github.com/FahimFBA). 

Vous pouvez également [VOUS ABONNER à ma chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) si vous souhaitez apprendre divers types de langages de programmation avec de nombreux exemples pratiques régulièrement.

Si vous souhaitez consulter mes moments forts, vous pouvez le faire sur ma [chronologie Polywork](https://www.polywork.com/fahimbinamin).

Vous pouvez également [visiter mon site web](https://fahimbinamin.com/) pour en savoir plus sur moi et sur ce que je fais.

Merci beaucoup !