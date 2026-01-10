---
title: Comment transformer une application Angular avec les Signals
subtitle: ''
author: Anujkumarsinh Donvir
co_authors: []
series: null
date: '2024-09-10T11:49:37.864Z'
originalURL: https://freecodecamp.org/news/how-to-transform-an-angular-appl-with-signals
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1725482117668/26d8fde9-0ff5-4496-9de2-c9e0deb8a02c.jpeg
tags:
- name: Angular
  slug: angularjs
seo_title: Comment transformer une application Angular avec les Signals
seo_desc: 'Angular is a famous framework for building robust and complex enterprise
  applications. It is widely used by large companies. Therefore, having the skills
  to build a performant application using Angular is one of the top skills for a developer..

  Angul...'
---

Angular est un framework célèbre pour la création d'applications d'entreprise robustes et complexes. Il est largement utilisé par les grandes entreprises. Par conséquent, posséder les compétences nécessaires pour construire une application performante avec Angular est l'une des compétences les plus recherchées pour un développeur.

L'ascension d'Angular peut être attribuée à une fonctionnalité spéciale appelée réactivité. La réactivité est la capacité du framework à modifier l'interface utilisateur (UI) lorsque les données sous-jacentes ou l'état de l'application changent.

Ce changement peut être dû à des événements asynchrones comme la réception d'une réponse d'un appel API, ou à une action de l'utilisateur telle que le clic sur un bouton. Pour atteindre cette réactivité, Angular déploie un mécanisme appelé détection de changements. La réactivité est cependant un outil à double tranchant et peut souvent entraîner des problèmes de performance en raison de mises à jour indésirables de l'UI.

Angular a récemment publié une nouvelle fonctionnalité appelée Signals, qui permet aux développeurs d'améliorer la performance des applications existantes construites avec Angular, ainsi que de créer de nouvelles applications offrant des gains de performance significatifs par rapport aux applications Angular traditionnelles.

Les Signals vous donnent le contrôle sur la détection de changements et empêchent les mises à jour indésirables de l'UI. Il peut être très délicat de transformer des applications existantes pour utiliser les Signals, et ce tutoriel vise à vous guider pour commencer. Dans ce tutoriel, une application Angular existante, construite de manière traditionnelle, sera transformée étape par étape pour utiliser les Signals.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Comment exécuter une application existante](#heading-comment-executer-une-application-existante)
    
* [Comprendre le code de l'application existante](#heading-comprendre-le-code-de-lapplication-existante)
    
* [Comment transformer l'application pour utiliser les Signals Angular](#heading-comment-transformer-lapplication-pour-utiliser-les-signals-angular)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Pour suivre ce tutoriel, vous devez remplir les prérequis suivants :

* Avoir une compréhension de JavaScript, TypeScript et du framework Angular.
    
* Node.js et NPM installés sur votre machine. Vous pouvez vérifier cela à l'aide de ces commandes : `node -v` et `npm --version`.
    
* Git installé sur votre machine. Vous pouvez vérifier cela à l'aide de `git --version`.
    
    ![version de node, npm et git dans le terminal](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeA5rN06IP7YBlURVo8cJ24QdPVik3dxCci04fP3Yp9otnbB5A13q49K5OrmOKon9EUDRgEpxWXKV08dmkcSJtDkT0u4Ceq3mD_ER2aqJSCyshULZIcQBWz9MP-JC3faqWqE79fHIfsrfRvLw63JAQs0pQ?key=SIi3jhbWSizs2BNTxpZ_RQ align="center")
    
* Un éditeur de code installé sur votre machine. Ce tutoriel a été développé en utilisant Visual Studio Code, mais n'importe quel éditeur de code devrait fonctionner.
    

## Comment exécuter une application existante

Nous allons transformer une application existante en utilisant les Signals Angular. L'application est un gestionnaire de feuilles de temps dans lequel un chef d'équipe ou un gestionnaire de quarts peut voir le nombre d'heures travaillées par chaque employé chaque semaine, ainsi que le total des heures de l'équipe.

Le chef d'équipe peut également mettre à jour les heures d'un employé. Suivez les étapes ci-dessous pour cloner et exécuter l'application localement sur votre machine :

* Clonez l'application en utilisant l'URL GitHub - https://github.com/anujkumartech/emp-time-tracker-1.git. Vous pouvez utiliser le terminal ou la cloner directement dans votre éditeur.
    
* Après avoir cloné l'application, ouvrez un nouveau terminal si ce n'est pas déjà fait et allez dans le dossier de l'application en utilisant `cd emp-time-tracker-1`.
    
* Une fois dans le dossier de l'application, installez les dépendances du projet en utilisant `npm install`.
    

Une fois les dépendances installées, lancez l'application avec `npm start`. Une fois l'application démarrée, accédez à http://localhost:4200/ et vous devriez voir la page suivante s'afficher.

![Page d'accueil de l'application existante](https://lh7-rt.googleusercontent.com/docsz/AD_4nXei6amdCIZzGq01anHIe4QYHU-EA8Zy3NyjNoDbU1zAx8na_xOHs6-uSZh2Eorqhu7UrHdFwmV_A5hT0xsOS5xMiHm94Z6wxsmpagiPQqecjQUNkJqiuzgA9q64H05f2N3GGj_VA0YsAJO9xkZa3KNNHcVU?key=SIi3jhbWSizs2BNTxpZ_RQ align="left")

### Comprendre le code de l'application existante

Il est très important de comprendre le code et l'architecture des composants qui affichent l'application. Ouvrez l'application dans votre éditeur de code en naviguant vers **src -> app**. Vous devriez voir une structure comme celle-ci.

![Répertoire du code](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeoOadAD5vMfCyV1ZamtdaYe0cSCEyeySD82_q1jDmvLfi1eGDDa2Gs7m0C5L-8I8yQgdiI9vWXaBuB-W3KgDv8PC0jyKajzHtq16fpVUssb-EgCO_0a5W_5KmwGkoPq9UdDLIqjRjVb0NhU1IQBEj8qL7W?key=SIi3jhbWSizs2BNTxpZ_RQ align="center")

Cette application possède deux composants principaux, le composant parent et le composant enfant. Le composant parent affiche les heures cumulées de l'équipe ainsi qu'une liste des employés rattachés au chef d'équipe, avec les heures totales et les heures supplémentaires de chaque employé. Le composant parent contient le code nécessaire pour afficher la liste et calculer les heures cumulées de l'équipe à partir de cette liste. De plus, le composant parent fournit également les détails de l'employé sélectionné au composant enfant.

Le composant enfant reçoit les détails de l'employé sélectionné en tant qu'entrée et permet de modifier les heures normales ainsi que les heures supplémentaires. Une fois que le chef d'équipe est satisfait, une action de sauvegarde est initiée. L'action de sauvegarde émet un événement du composant enfant vers le composant parent. Le composant parent réagit à cet événement et effectue les mises à jour nécessaires aux heures de l'employé sélectionné. Cette mise à jour déclenche le recalcul des heures cumulées.

![Architecture des composants de l'application existante](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcipNqPsU-ACMQnJ578FL51paiBdzoNtWygqAACkWIdJmhP8SPAxQPg-SInKOoev7dmSNMINdmFFCNDntFly1ZpkKe6HgwbvNGRZZmhIYfFGtwUXgb2TZpMBC67B7sRcoDNmdsIbLSij8YHzp5AfjKuEtg?key=SIi3jhbWSizs2BNTxpZ_RQ align="left")

Veuillez parcourir le code dans l'éditeur également, et portez une attention particulière au code dans les fichiers **parent-component.ts** et **child-component.ts**. Dans la section suivante, vous transformerez ces deux composants pour utiliser la nouvelle fonctionnalité Signals d'Angular.

## Comment transformer l'application pour utiliser les Signals Angular

La transformation du code peut commencer par le code du composant parent. Changez la variable `managerName` pour utiliser les Signals. Cela montre comment une nouvelle variable Signal peut être créée. Un Signal peut être initié avec le mot-clé `signal` et une définition de type optionnelle, ainsi qu'une valeur initiale. Le code ci-dessous montre comment un nouveau Signal nommé `managerName` de type `string` peut être initié avec la valeur initiale `John Doe`.

```typescript
// parent-component.ts
managerName = signal<string>('John Doe');
```

Vous observerez des problèmes d'affichage une fois que vous aurez mis à jour `managerName` dans le fichier du composant pour utiliser le Signal. C'est parce que, pour lire la valeur d'un Signal, il doit être exécuté. Mettez à jour le code HTML du composant comme suit pour lire correctement la valeur du Signal.

```xml
<!-- parent-component.html -->
<h1 class="text-3xl font-bold mb-6">Bonjour {{managerName()}}!</h1>
```

La liste des employés à l'intérieur du composant parent est un simple tableau, transformez-la également en Signal.

```typescript
// parent-component.ts
 employees = signal<Employee[]>([
    {
      id: 1,
      name: 'Jon Snow',
      regularHours: 40,
      overtimeHours: 5
    },
    ...restOfEmployees
    }
  ])
```

Dès que le tableau des employés est transformé en Signal, le composant parent affichera plusieurs erreurs. Pour le moment, commentez le code à l'intérieur des méthodes `getTeamRegularHoursTotal`, `getTeamOvertimeHoursTotal` et `employeeChange` comme indiqué dans l'illustration ci-dessous.

```typescript
  // parent-component.ts
  getTeamRegularHoursTotal() {
    let total = 0;
    // this.employees.forEach(employee => total += employee.regularHours);
    return total;
  }

  getTeamOvertimeHoursTotal() {
    let total = 0;
    // this.employees.forEach(employee => total += employee.overtimeHours);
    return total;
  }

  employeeChange(updatedEmployee: Employee | null) {
    // if (updatedEmployee) {
    //   const index = this.employees.findIndex(emp => emp.id === updatedEmployee.id);
    //   if (index !== -1) {
    //     this.employees[index] = updatedEmployee;
    //   }
    // }
    // this.selectedEmployee = null;
  }
```

Pour afficher à nouveau l'application, mettez à jour le template HTML du composant parent et exécutez le Signal `employees` selon le code ci-dessous.

```xml
<!-- parent-component.html -->
<div class="flex items-center py-4 space-x-4 group border-b cursor-pointer hover:bg-gray-50" *ngFor="let employee of employees()" (click)="selectEmployee(employee)">
```

Il est temps de transformer la logique pour calculer la valeur des heures normales qui s'affichent actuellement à zéro. Cela nous amène à examiner un autre type important de Signal appelé "computed".

Les Signals **computed**, comme leur nom l'indique, dépendent d'autres Signals pour leur valeur. Leur valeur est mise à jour dès que les Signals sous-jacents changent, sans avoir besoin de code supplémentaire pour gérer le changement.

Créez un Signal computed `teamRegularHoursTotal` comme indiqué dans le code ci-dessous, qui dépend directement du Signal `employees`. Ainsi, chaque fois que le Signal `employees` change, la valeur de `teamRegularHoursTotal` est mise à jour automatiquement.

Définissez le Signal computed comme indiqué ci-dessous, et assurez-vous que la dépendance `computed` est importée depuis le package core d'Angular. Supprimez ou commentez également complètement la méthode `getTeamRegularHoursTotal`.

```typescript
// parent-component.ts
 teamRegularHoursTotal = computed(() => {
    let total = 0;
    this.employees().forEach(employee => total += employee.regularHours);
    return total;
  })
```

Mettez à jour le template HTML du composant parent pour refléter ce changement et afficher la valeur des heures totales.

```xml
<!-- parent-component.html -->
<p class="text-lg font-medium text-gray-700">Heures normales : <span class="font-bold">
{{teamRegularHoursTotal() }}</span></p>
```

De même, les heures supplémentaires peuvent également être transformées en un Signal computed. Reportez-vous au code ci-dessous pour mettre à jour à la fois le code du composant et son template HTML. Commentez ou supprimez également la méthode `getTeamOvertimeHoursTotal`.

```typescript
// parent-component.ts
 teamOvertimeHoursTotal = computed(() => {
    let total = 0;
    this.employees().forEach(employee => total += employee.overtimeHours);
    return total;
  })
```

```xml
<!-- parent-component.html -->
<p class="text-lg font-medium text-gray-700">Heures supplémentaires : <span class="font-bold">
{{teamOvertimeHoursTotal() }}</span></p>
```

Il est temps de convertir la variable `selectedEmployee` du composant parent en Signal. Transformez-la en utilisant le code ci-dessous :

```typescript
// parent-component.ts
selectedEmployee = signal<Employee | null>(null);
```

Dès que ce changement est effectué, la méthode `selectEmployee` du composant parent présentera des erreurs. Ces erreurs sont une excellente occasion d'aborder un sujet important : la modification des valeurs d'un Signal. Les Signals Angular peuvent être mis à jour à l'aide des API `set` ou `update`.

Comme son nom l'indique, la méthode `set` assigne une nouvelle valeur à un Signal, et la méthode `update` met à jour la valeur d'un Signal. Utilisez la méthode `set` pour modifier la valeur du Signal `selectedEmployee`. Vous verrez bientôt la méthode `update` en action.

```typescript
// parent-component.ts
selectEmployee(employee: Employee): void {
    this.selectedEmployee.set(employee);
}
```

En parallèle de ce changement, le template du composant parent doit être mis à jour. Modifiez le code contenant le composant enfant comme indiqué ci-dessous.

Après ce changement, vérifiez que l'application s'affiche correctement et que vous pouvez sélectionner un employé et voir ses détails à l'écran. C'est important car nous allons poursuivre ce voyage de transformation vers le composant enfant.

```xml
<!-- parent-component.html -->
<section class="w-full md:w-1/2 bg-white p-6 rounded-lg shadow-lg border border-gray-200 order-1 md:order-2 mb-4 md:mb-0"
      *ngIf="selectedEmployee() !== null">
    <app-child-component [employee]="selectedEmployee()" (employeeChange)="employeeChange($event)"></app-child-component>
</section>
```

Le composant enfant reçoit la valeur de l'employé sélectionné via son entrée, qui est actuellement définie à l'aide du décorateur `@Input`. Cela peut être transformé à l'aide d'un Signal opportunément nommé `input`. Changez la variable `employee` pour qu'elle soit de type `input` comme indiqué ci-dessous. Commentez le code dans les méthodes `saveChanges` et `resetForm` comme indiqué.

```typescript
// child-component.ts
employee  = input<Employee | null>();
saveChanges() {
    // this.employee.regularHours = this.editedRegularHours;
    // this.employee.overtimeHours = this.editedOvertimeHours;
    // this.employeeChange.emit(this.employee);
}

private resetForm() {
    // this.editedRegularHours = this.employee.regularHours;
    // this.editedOvertimeHours = this.employee.overtimeHours;
}
```

Le formulaire à l'intérieur du composant enfant affiche les heures normales et supplémentaires de l'employé sélectionné en utilisant deux variables de modèle : `editedRegularHours` et `editedOvertimeHours`.

Ces variables ne sont plus nécessaires et les entrées du formulaire du composant enfant peuvent être mises à jour pour utiliser directement la valeur du Signal.

```xml
<!-- child-component.html --> 
<input 
     type="number" 
     id="regularHours" 
     [ngModel]="editedRegularHours"
     (ngModelChange)="onRegularHoursChange($event)"
      class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
 />
 <input 
      type="number" 
      id="overtimeHours" 
      [ngModel]="editedOvertimeHours"
      (ngModelChange)="onOvertimeHoursChange($event)"
      class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
  />
```

La logique pour capturer les valeurs mises à jour pour les heures normales et supplémentaires peut également être transformée. Idéalement, la mise à jour du code ci-dessous devrait fonctionner, mais vous obtiendrez une erreur comme illustré ci-dessous.

![Erreur de composant](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf3Zhm_Buy_VvhnYrZcx4YBNFjxoA4jR47L75eLEE2An9xt-aHNWI7iO9uEFp7KlzfoofoUGjaSW6CR-raKXjuVe0_XDhl8SMfMWBTpiQ5eHIfQxoS5qqeFKcu3k3Rb246K8cB7xiIpK4ein7-4xBhkgeA?key=SIi3jhbWSizs2BNTxpZ_RQ align="center")

La raison de cette erreur est que le Signal de type `input` ne peut pas être muté avec les méthodes `set` et `update`. Angular fournit un type différent de Signal appelé `model` pour permettre aux composants d'avoir des entrées mutables au sein du composant lui-même. Changez `employee` en type `model` comme illustré ci-dessous.

```typescript
// child-component.ts
employee = model<Employee | null>();
```

Mettez à jour la méthode de mise à jour des heures supplémentaires comme indiqué ci-dessous. Ainsi, le composant enfant retrouve la capacité de mettre à jour les valeurs des heures normales et supplémentaires de l'employé reçu du composant parent.

```typescript
// child-component.ts
  onOvertimeHoursChange(event: number) {
    this.employee.set({
      ...this.employee(),
      overtimeHours: event
    })
  }
```

Actuellement, le composant enfant communique les changements au composant parent en utilisant le décorateur `@Output`. À l'instar d' `input` et de `model`, Angular dispose d'un Signal de type `output` pour permettre une communication bidirectionnelle entre les composants enfant et parent. Mettez à jour l'événement `employeeChange` vers le type `output` comme illustré ci-dessous.

```typescript
// child-component.ts 
employeeChange = output<Employee | null>();
```

Mettez à jour la méthode `saveChanges` et émettez un objet employé mis à jour.

```typescript
// child-component.ts 
 saveChanges() {
    this.employeeChange.emit(this.employee());
 }
```

Pour la dernière étape de la mise à jour du composant enfant, modifiez les méthodes `resetForm` et `cancelChanges` pour refléter les changements effectués comme indiqué ci-dessous.

```typescript
// child-component.ts   
cancelChanges() {
    this.employeeChange.emit(null);
 }
resetForm() {
    this.employee.set(null);
}
```

De retour au composant parent, il est important d'apporter des modifications au template pour assurer une communication fluide entre les deux composants.

L'entrée `employee` dans le composant enfant est passée à un type `model`. Un modèle dispose d'une liaison de données bidirectionnelle. Mettez à jour le code comme illustré ci-dessous pour utiliser la notation "banane dans la boîte" (syntaxe spéciale `[( )]`, qui est un raccourci pour la liaison de données bidirectionnelle).

```xml
<!-- parent-component.html -->
<section class="w-full md:w-1/2 bg-white p-6 rounded-lg shadow-lg border border-gray-200 order-1 md:order-2 mb-4 md:mb-0"
    *ngIf="selectedEmployee() !== null">
    <app-child-component [(employee)]="selectedEmployee" (employeeChange)="employeeChange($event)"></app-child-component>
</section>
```

Il est temps de mettre à jour la méthode `employeeChange` dans le composant parent afin que les valeurs d'heures mises à jour de l'employé sélectionné puissent être répercutées à l'écran.

Pour y parvenir, une autre méthode clé utilisée pour muter les valeurs peut être exploitée. Il s'agit de la méthode `update`, qui prend une fonction comme argument au lieu d'une valeur complète. La fonction passe la valeur actuelle du Signal comme premier paramètre et renvoie la valeur mise à jour du Signal.

Reportez-vous au code mis à jour pour la méthode `employeeChange` ci-dessous pour mieux comprendre cela.

```typescript
// parent-component.ts  
employeeChange() {
    if (this.selectedEmployee()) {
      this.employees.update(employees => employees.map(employee => {
        if (employee.id === this.selectedEmployee().id) {
          employee.regularHours = this.selectedEmployee().regularHours;
          employee.overtimeHours = this.selectedEmployee().overtimeHours;
        }
        return employee;
      }))
    }
    this.selectedEmployee.set(null);
  }
```

Avec ce changement, la transformation complète de l'application pour utiliser les Signals est terminée. Assurez-vous que tout se charge correctement et que toutes les fonctionnalités opèrent comme prévu.

## Conclusion

Félicitations pour avoir terminé ce tutoriel. Au cours de ce parcours, vous avez créé un Signal classique et mis à jour sa valeur en utilisant les méthodes `set` et `update`.

Vous avez également appris comment les Signals computed sont définis et utilisés. De plus, vous avez activé la communication entre deux composants en utilisant les Signals `input`, `model` et `output`.

Si vous rencontrez des problèmes lors de cette transformation, vous pouvez vérifier le code dans la branche `feature/signals` du même dépôt que vous avez cloné précédemment. Il est recommandé de suivre les étapes plutôt que de simplement copier la solution depuis cette branche.

Une fois que vous vous sentirez à l'aise avec les types de Signals abordés, poursuivez votre apprentissage en explorant l'Interop RxJS de l'équipe Angular pour gérer l'intégration de vos Signals avec les observables RxJS.