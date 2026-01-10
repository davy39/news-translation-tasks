---
title: Détecter les ANR dans votre application
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2022-05-11T15:48:14.000Z'
originalURL: https://freecodecamp.org/news/detect-application-not-responding-errors-in-your-application
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/mediamodifier-yx17UuZw1Ck-unsplash.jpg
tags:
- name: android app development
  slug: android-app-development
- name: error handling
  slug: error-handling
seo_title: Détecter les ANR dans votre application
seo_desc: "If there was a way to make my applications \"Application not responding\"\
  \ error proof, I would do it. \nANRs always seem to sneak up on you when you're\
  \ not expecting them. And the problem is that there's nothing you can do about them.\
  \ \nYou might see the..."
---

Si je pouvais rendre mes applications à l'épreuve des erreurs "Application non répondante", je le ferais.

Les ANR semblent toujours nous surprendre quand on ne s'y attend pas. Et le problème, c'est qu'il n'y a rien que l'on puisse faire à leur sujet.

Vous pourriez les voir apparaître lors de l'examen de votre application dans la Google Play Console. Mais il n'y aura pas beaucoup d'informations pour comprendre comment l'ANR s'est produit et ce que vous auriez pu faire pour corriger la situation.

Et au-delà de cela, si un utilisateur rencontre un ANR, vous devez compter sur sa bonne volonté pour investir du temps et des efforts afin de vous en informer. Nous avons tous été de l'autre côté. Si vous utilisez une application qui se bloque, la première chose que vous faites est de la désinstaller immédiatement.

Alors, comment pouvons-nous, en tant que développeurs, faire tout notre possible pour protéger les utilisateurs de nos applications contre les ANR ?

Découvrons-le.

## Comment prévenir les erreurs "Application non répondante" sur Android

### Soyez proactif

Avant de nous pencher sur les solutions qui peuvent nous aider à détecter les ANR, comprenons ce que nous pouvons faire pour éviter d'en avoir en premier lieu (ou minimiser les chances qu'ils se produisent).

Ces points peuvent sembler évidents, mais dans une application suffisamment grande, il peut être facile de négliger certaines choses :

Premièrement, vérifiez si vous avez des endroits dans votre code qui effectuent un travail intensif sur le thread UI. Le travail effectué sur le thread UI doit être court et lié à quelque chose concernant l'interface utilisateur de votre application.

Si vous effectuez une autre logique ou même un travail asynchrone, déléguez-le à un thread d'arrière-plan ou à un service.

Deuxièmement, si par hasard vous avez des threads qui détiennent des verrous ou certains blocs de code qui doivent être synchronisés, assurez-vous de ne pas créer de blocage ou un certain état de votre application qui pourrait y parvenir.

Et troisièmement, si votre application traite avec des récepteurs de diffusion, vous devez vérifier que l'exécution de la méthode **onReceive** est courte et se termine en temps opportun. Si un travail peut prendre du temps, déléguez-le à un thread d'arrière-plan.

Une autre façon de détecter les endroits qui pourraient causer des ANR est d'utiliser [**StrictMode**](https://developer.android.com/reference/android/os/StrictMode). Vous pouvez l'utiliser pendant le développement de votre application car il détecte les utilisations accidentelles du disque ou du réseau sur le thread principal.

### Soyez intelligent

Vous avez passé en revue votre application et vous pensez qu'elle n'est pas à risque pour des ANR. Vous la publiez donc pour une utilisation publique.

Et voilà, quelques mois passent et vous commencez à voir des rapports d'ANR. Qu'auriez-vous pu faire différemment ? Comme nous l'avons discuté précédemment, ces rapports de plantage fournissent à peine des informations concernant l'ANR.

Pour aider votre application à vous fournir le niveau de détail le plus élevé possible lorsqu'un ANR se produit, je vais détailler deux options :

1. Exécuter un thread qui interroge le thread UI pour voir s'il est bloqué
2. Sur le niveau d'API ≥ 30, vous pouvez utiliser [**getHistoricalProcessExitReasons**](https://developer.android.com/reference/kotlin/android/app/ActivityManager#gethistoricalprocessexitreasons)

Examinons chacune d'elles en détail maintenant :

#### Exécuter un thread qui interroge le thread UI

Il existe déjà une bibliothèque appelée [ANR-Watchdog](https://github.com/SalomonBrys/ANR-WatchDog) qui se charge de détecter les ANR et vous fournit tous les détails. Au cas où vous ne souhaiteriez pas l'utiliser ou auriez besoin de quelque chose de personnalisé, voici un aperçu de ce qu'elle fait :

* Créer un thread qui s'exécute sur le thread principal (il n'a pas besoin d'effectuer de travail réel)
* Voir si l'exécution du thread se termine après quelques secondes
* Si c'est le cas, aucun ANR ne s'est produit et vous exécutez à nouveau le thread
* Si ce n'est pas le cas, un autre thread bloque le thread principal et cause un ANR

Voici un aperçu d'une telle classe :

```kotlin
package com.tomerpacific.anrdetection

import android.os.Handler
import android.os.Looper
import java.lang.Exception

class ANRHandler: Thread() {

    val TIMEOUT: Long = 5000L
    private val handler: Handler = Handler(Looper.getMainLooper())
    private val worker : Runnable = Runnable {  }

    override fun run() {
        while (!isInterrupted) {
            handler.postAtFrontOfQueue(worker)

            try {
                sleep(TIMEOUT)
            } catch (exception: Exception) {
                exception.printStackTrace()
            }

            if (handler.hasMessages(0)) {
                //worker n'a pas terminé son exécution, donc le thread UI est bloqué
                val stackTrace: Array<StackTraceElement> = currentThread().stackTrace
                var output: String = ""
                for (element in stackTrace) {
                    output += element.className + " " + element.methodName + " " + element.lineNumber
                }

                print(output)
            }
        }
    }
}
```

⚠️ L'exécution du runnable est toujours sur le thread principal, mais comme il ne fait aucun travail, il ne devrait pas impacter les performances de votre application. Vous pourriez également décider de l'exécuter à intervalles de temps souhaités.

#### Utiliser [getHistoricalProcessExitReasons](https://developer.android.com/reference/kotlin/android/app/ActivityManager#gethistoricalprocessexitreasons)

L'option #2 peut simplifier votre vie, car son API vous fournit beaucoup d'informations.

Introduit dans Android 11 (niveau d'API 30), getHistoricalProcessExitReasons fait exactement ce que vous pensez. Il retourne une liste d'objets enregistrés qui rendent compte des terminaisons d'applications les plus récentes.

Cette méthode est appelée sur le ActivityManager et accepte trois arguments :

1. Le nom du package – de type String (peut être null)
2. L'ID du processus appartenant au package – de type int
3. Le nombre maximum de raisons que vous souhaitez obtenir – de type int

Il est important de noter que tous ces arguments peuvent être substitués par des valeurs par défaut. C'est-à-dire que vous pouvez passer null comme nom de package et obtenir toutes les raisons de sortie pour l'UID de l'appelant.

Alors, que contiennent ces objets enregistrés ? Eh bien, ces objets sont de type [**ApplicationExitInfo**](https://developer.android.com/reference/kotlin/android/app/ApplicationExitInfo) et ils peuvent vous fournir beaucoup d'informations utiles.

Pour commencer, vous pourriez appeler la méthode **getReason** pour découvrir pourquoi le processus s'est terminé. Cette méthode retourne un entier marquant le code de la raison de la sortie. Si la valeur retournée est **6**, cela signifie que l'application a été terminée parce qu'elle était sans réponse en raison du fait qu'un [ANR](https://developer.android.com/reference/kotlin/android/app/ApplicationExitInfo#reason_anr) s'est produit.

<iframe src="https://giphy.com/embed/917Ve5cLpoB3Nhd1xh" width="480" height="400" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/theoffice-nbc-the-office-tv-917Ve5cLpoB3Nhd1xh">via GIPHY</a></p>

C'est bien, mais comment pouvons-nous voir où l'ANR s'est produit ? Pour cela, nous pouvons utiliser [**getTraceInputStream**](https://developer.android.com/reference/kotlin/android/app/ApplicationExitInfo#gettraceinputstream). Comme le nom l'indique, la valeur retournée est un InputStream d'octets qui doit être lu comme tout autre InputStream.

Un exemple de sortie ressemble à ce qui suit :

```log
I/System.out: ----- pid 2738 à 2022-04-26 17:48:12 -----
    Ligne de commande : com.tomerpacific.anrdetection
    Empreinte de construction : 'Android/sdk_phone_x86/generic_x86:11/RSR1.210210.001.A1/7193139:userdebug/dev-keys'
    ABI : 'x86'
    Type de construction : optimisé
I/System.out: Classes chargées par Zygote=15746 classes post zygote=728
    Vidage des chargeurs de classe enregistrés
    #0 dalvik.system.PathClassLoader: [], parent #1
    #1 java.lang.BootClassLoader: [], pas de parent
I/System.out: #2 dalvik.system.PathClassLoader: [/data/app/~~C_0mqw-g_9cjPjIR_kpRIg==/com.tomerpacific.anrdetection-3-t-I6JR9Q3QA6UY7L8iPA==/base.apk], parent #1
    Fin du vidage des chargeurs de classe
    Classes initialisées : 302 en 19.361ms
    Table d'internement : 31490 forts ; 543 faibles
    JNI : CheckJNI est activé ; globals=637 (plus 31 faibles)
I/System.out: Bibliothèques : libandroid.so libaudioeffect_jni.so libcompiler_rt.so libicu_jni.so libjavacore.so libjavacrypto.so libjnigraphics.so libmedia_jni.so libopenjdk.so librs_jni.so libsfplugin_ccodec.so libsoundpool.so libstats_jni.so libwebviewchromium_loader.so (14)
    Tas : 91% libre, 2330KB/26MB ; 67022 objets
    Vidage des temps cumulés de GC
I/System.out: Ratio moyen de récupération des octets de GC majeur inf sur 0 cycles de GC
    Ratio moyen de copie des octets vivants de GC majeur 0.738176 sur 4 GC majeurs
    Octets cumulés déplacés 11482280
    Objets cumulés déplacés 217937
    Régions de pointe allouées 28 (7168KB) / 768 (192MB)
I/System.out: Début du vidage des histogrammes pour 1 itération pour la copie concurrente jeune
    ProcessMarkStack:	Somme : 26.311ms 99% C.I. 26.311ms-26.311ms Moy : 26.311ms Max : 26.311ms
    ScanImmuneSpaces:	Somme : 5.625ms 99% C.I. 5.625ms-5.625ms Moy : 5.625ms Max : 5.625ms
    VisitConcurrentRoots:	Somme : 1.121ms 99% C.I. 1.121ms-1.121ms Moy : 1.121ms Max : 1.121ms
I/System.out: (Paused)ClearCards:	Somme : 375us 99% C.I. 7us-235us Moy : 28.846us Max : 235us
    GrayAllDirtyImmuneObjects:	Somme : 329us 99% C.I. 329us-329us Moy : 329us Max : 329us
    VisitNonThreadRoots:	Somme : 327us 99% C.I. 327us-327us Moy : 327us Max : 327us
I/System.out: InitializePhase:	Somme : 306us 99% C.I. 306us-306us Moy : 306us Max : 306us
    (Paused)GrayAllNewlyDirtyImmuneObjects:	Somme : 164us 99% C.I. 164us-164us Moy : 164us Max : 164us
    (Paused)FlipCallback:	Somme : 144us 99% C.I. 144us-144us Moy : 144us Max : 144us
    SweepSystemWeaks:	Somme : 142us 99% C.I. 142us-142us Moy : 142us Max : 142us
I/System.out: ScanCardsForSpace:	Somme : 125us 99% C.I. 125us-125us Moy : 125us Max : 125us
    ThreadListFlip:	Somme : 96us 99% C.I. 96us-96us Moy : 96us Max : 96us
    ClearFromSpace:	Somme : 78us 99% C.I. 78us-78us Moy : 78us Max : 78us
    CopyingPhase:	Somme : 76us 99% C.I. 76us-76us Moy : 76us Max : 76us
I/System.out: FlipOtherThreads:	Somme : 58us 99% C.I. 58us-58us Moy : 58us Max : 58us
    ProcessReferences:	Somme : 54us 99% C.I. 19us-35us Moy : 27us Max : 35us
    SweepArray:	Somme : 53us 99% C.I. 53us-53us Moy : 53us Max : 53us
I/System.out: EnqueueFinalizerReferences:	Somme : 38us 99% C.I. 38us-38us Moy : 38us Max : 38us
    RecordFree:	Somme : 37us 99% C.I. 14us-23us Moy : 18.500us Max : 23us
    ForwardSoftReferences:	Somme : 25us 99% C.I. 25us-25us Moy : 25us Max : 25us
    FlipThreadRoots:	Somme : 21us 99% C.I. 21us-21us Moy : 21us Max : 21us
I/System.out: (Paused)SetFromSpace:	Somme : 19us 99% C.I. 19us-19us Moy : 19us Max : 19us
    ResumeRunnableThreads:	Somme : 12us 99% C.I. 12us-12us Moy : 12us Max : 12us
    EmptyRBMarkBitStack:	Somme : 8us 99% C.I. 8us-8us Moy : 8us Max : 8us
    SwapBitmaps:	Somme : 7us 99% C.I. 7us-7us Moy : 7us Max : 7us
    Fin du vidage des histogrammes
    jeune copie concurrente en pause :	Somme : 750us 99% C.I. 750us-750us Moy : 750us Max : 750us
I/System.out: jeune copie concurrente octets libérés : Moy : 1052KB Max : 1052KB Min : 1052KB
    Histogramme des octets libérés : 960:1
    temps total de la jeune copie concurrente : 35.641ms temps moyen : 35.641ms
    jeune copie concurrente libérée : 8956 objets avec une taille totale de 1052KB
I/System.out: débit de la jeune copie concurrente : 255886/s / 29MB/s par temps CPU : 179578666/s / 171MB/s
    Ratio moyen de récupération des octets de GC mineur 0.742269 sur 1 cycle de GC
    Ratio moyen de copie des octets vivants de GC mineur 0.276211 sur 2 GC mineurs
    Octets cumulés déplacés 1410368
    Objets cumulés déplacés 26626
I/System.out: Régions de pointe allouées 28 (7168KB) / 768 (192MB)
    Temps total passé en GC : 35.641ms
    Débit moyen de la taille du GC : 28MB/s par temps CPU : 169MB/s
    Débit moyen des objets du GC : 251284 objets/s
    Nombre total d'allocations 75978
    Octets totaux alloués 3382KB
    Octets totaux libérés 1052KB
I/System.out: Mémoire libre 23MB
    Mémoire libre jusqu'au GC 23MB
    Mémoire libre jusqu'à OOME 189MB
    Mémoire totale 26MB
    Mémoire max 192MB
    Taille de l'espace Zygote 3040KB
    Temps total de pause du mutateur : 750us
I/System.out: Temps total d'attente pour la fin du GC : 80.600us
    Nombre total de GC : 1
    Temps total de GC : 35.641ms
    Nombre total de GC bloquants : 0
    Temps total de GC bloquants : 0
    Histogramme du nombre de GC par 10000 ms : 0:1
    Histogramme du nombre de GC bloquants par 10000 ms : 0:1
    Octets natifs totaux : 15621964 enregistrés : 98204
I/System.out: Octets natifs totaux au dernier GC : 15537168
    /system/framework/oat/x86/android.hidl.manager-V1.0-java.odex : quicken
    /system/framework/oat/x86/android.test.base.odex : quicken
    /system/framework/oat/x86/android.hidl.base-V1.0-java.odex : quicken
I/System.out: Taille actuelle du cache de code JIT (utilisé / résident) : 0KB / 32KB
    Taille actuelle du cache de données JIT (utilisé / résident) : 4KB / 32KB
    Taille du cache de code JIT de Zygote (au point de fork) : 45KB / 48KB
    Taille du cache de données JIT de Zygote (au point de fork) : 33KB / 36KB
    Taille actuelle des mini-infos de débogage JIT : 26KB
I/System.out: Capacité actuelle du JIT : 64KB
    Nombre actuel d'entrées de stub JNI JIT : 0
    Nombre actuel d'entrées de cache de code JIT : 48
    Nombre total de compilations JIT : 6
    Nombre total de compilations JIT pour le remplacement de pile : 1
I/System.out: Nombre total de collections de cache de code JIT : 0
    Mémoire utilisée pour les cartes de pile : Moy : 35B Max : 52B Min : 28B
    Mémoire utilisée pour le code compilé : Moy : 125B Max : 257B Min : 69B
    Mémoire utilisée pour les infos de profilage : Moy : 70B Max : 188B Min : 20B
    Début du vidage des histogrammes pour 48 itérations pour les temps JIT
    Compilation :	Somme : 385.780ms 99% C.I. 0.556ms-25.610ms Moy : 8.037ms Max : 25.610ms
I/System.out: TrimMaps :	Somme : 44.431ms 99% C.I. 2.400us-5148us Moy : 925.645us Max : 5643us
    Fin du vidage des histogrammes
    Mémoire utilisée pour la compilation : Moy : 83KB Max : 322KB Min : 8560B
    ProfileSaver total_bytes_written=0
    ProfileSaver total_number_of_writes=0
    ProfileSaver total_number_of_code_cache_queries=0
I/System.out: ProfileSaver total_number_of_skipped_writes=0
    ProfileSaver total_number_of_failed_writes=0
    ProfileSaver total_ms_of_sleep=5000
    ProfileSaver total_ms_of_work=0
I/System.out: ProfileSaver total_number_of_hot_spikes=5
    ProfileSaver total_number_of_wake_ups=0
I/System.out: histogramme de suspension de tous :	Somme : 11.468ms 99% C.I. 0.018ms-10.658ms Moy : 1.042ms Max : 11.094ms
    THREADS DALVIK (15) :
    "main" prio=5 tid=1 Runnable
      | group="main" sCount=0 dsCount=0 flags=0 obj=0x72107008 self=0xe7d05410
      | sysTid=2738 nice=-10 cgrp=top-app sched=0/0 handle=0xf6267478
I/System.out:   | state=R schedstat=( 5812106631 1041760011 2536 ) utm=535 stm=45 core=0 HZ=100
      | stack=0xff7cb000-0xff7cd000 stackSize=8192KB
      | mutex détenus= "mutator lock"(partagé détenu)
        à com.tomerpacific.anrdetection.MainActivity$onCreate$1$1.onClick(MainActivity.kt:18)
        à android.view.View.performClick(View.java:7448)
        à android.view.View.performClickInternal(View.java:7425)
I/System.out:     à android.view.View.access$3600(View.java:810)
        à android.view.View$PerformClick.run(View.java:28305)
I/System.out:     à android.os.Handler.handleCallback(Handler.java:938)
        à android.os.Handler.dispatchMessage(Handler.java:99)
        à android.os.Looper.loop(Looper.java:223)
        à android.app.ActivityThread.main(ActivityThread.java:7656)
I/System.out:     à java.lang.reflect.Method.invoke(Native method)
        à com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:592)
        à com.android.internal.os.ZygoteInit.main(ZygoteInit.java:947)
```

Ce n'est qu'un extrait partiel de toute la sortie, mais vous pouvez voir qu'il fournit une tonne d'informations, y compris :

* Mémoire libre/Mémoire totale/Mémoire max
* Diagnostic du tas (pourcentage libre, taille et quantité d'objets alloués)
* La stacktrace du thread principal

D'autres méthodes utiles incluent :

* getTimestamp – l'horodatage de la terminaison du processus
* getDescription – une description système de la raison de la terminaison du processus

### Soyez ingénieux

Si votre application souffre d'ANR, les résoudre peut être assez délicat. Cela peut être dû au fait que vous n'obtenez pas une stacktrace complète (ou n'en avez pas du tout), que vous ne pouvez pas la reproduire, ou qu'elle se produit sur un appareil ésotérique. Alors, que pouvez-vous faire ?

Dans Android Studio version ≥ 3.2, vous avez un utilitaire appelé [CPU Profiler](https://developer.android.com/studio/profile/cpu-profiler). Cet outil vous permet d'inspecter l'activité de vos threads pendant l'exécution de votre application. Avec lui, vous pourriez découvrir quels threads sont en cours d'exécution, pendant combien de temps et où ils s'exécutent.

Pour l'utiliser, dans Android Studio, allez dans View → Tool Window → Profiler :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/1_RklpDywn-s_a7seW8_wcaw.jpeg)

Une fenêtre s'ouvrira en bas de l'écran. Une fois que vous avez attaché un processus, vous verrez trois chronologies :

1. Chronologie des événements
2. Chronologie du CPU
3. Chronologie des threads

![Image](https://www.freecodecamp.org/news/content/images/2022/05/1__aG-Tlaaa7ZWpLbuQnLlqQ.jpeg)

Vous voulez vous concentrer sur la chronologie des threads pour voir si quelque chose est hors de l'ordinaire. L'activité de chaque thread peut être identifiée par trois couleurs :

* Vert – indique que le thread est en cours d'exécution ou dans un état exécutable
* Jaune – indique que le thread attend l'exécution d'une opération d'E/S
* Gris – indique que le thread est en sommeil

## Conclusion

Espérons que vous avez gagné en confiance pour rendre vos applications aussi résistantes aux ANR que possible. L'utilisation des outils et techniques listés ci-dessus peut aider à prévenir le prochain ANR de votre application.

Vous êtes les bienvenus pour consulter certains de mes autres articles sur GitHub :

%[https://github.com/TomerPacific/MediumArticles]