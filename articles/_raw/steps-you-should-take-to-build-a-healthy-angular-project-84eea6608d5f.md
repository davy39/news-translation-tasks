---
title: Steps you should take to build a healthy Angular project
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-16T22:53:15.000Z'
originalURL: https://freecodecamp.org/news/steps-you-should-take-to-build-a-healthy-angular-project-84eea6608d5f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Q_Tuv1uGF5i5opPCuZrh0A.png
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: Jenkins
  slug: jenkins
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ashish Gaikwad

  Create your “Angular Fitbit” with Jenkins + SonarQube


  Just like the recent introduction of wearables to track our health, the software
  industry has long followed the practice of monitoring the health of software projects.
  The most ...'
---

By Ashish Gaikwad

#### Create your “Angular Fitbit” with Jenkins + SonarQube

![Image](https://cdn-media-1.freecodecamp.org/images/wjMyKOsxM2Mcyv9WVWqsjKodQ0tksqkMMpGb)

Just like the recent introduction of wearables to track our health, the software industry has long followed the practice of monitoring the health of software projects. The most common processes applied are unit tests, integration tests, continuous integration, and code coverage.

I recently struggled a bit in trying to setup the above mentioned processes for our project, so I wrote this post to document my experience. Since TypeScript is the default language for Angular 2 projects, existing JS setups do not work.

### Getting started

Here are the steps to setup a Jenkins CI environment for Angular projects with code coverage using SonarQube on a headless Linux server:

* Download [Jenkins](https://jenkins.io/) and set it up on your build server. Make sure you have Java installed on it, as it is required by Jenkins. **Note**: Jenkins’ default configuration runs with `jenkins` user, so you might need to set `JAVA_HOME` for the `jenkins` user.
* Once Jenkins is setup, install or make sure you have the following plugins installed from the manage plugins menu:

![Image](https://cdn-media-1.freecodecamp.org/images/Z1fjqabmgmBITHEsZaWFDf1FOYOpZI-alnLR)
_[**Git plugin**](http://wiki.jenkins-ci.org/display/JENKINS/Git+Plugin" rel="noopener" target="_blank" title=") **for repo configuration**_

![Image](https://cdn-media-1.freecodecamp.org/images/Ynn9vwg7yFFUHeRcH5IzcmcYLjb2lcnse8mY)
_[**NodeJs Plugin**](http://wiki.jenkins-ci.org/display/JENKINS/NodeJS+Plugin" rel="noopener" target="_blank" title=") **for running npm commands and scripts**_

![Image](https://cdn-media-1.freecodecamp.org/images/DqokQi13Q-TFB0a0VLSEKNP4je9sIdhFiu9e)
_[**SonarQube scanner**](http://redirect.sonarsource.com/plugins/jenkins.html" rel="noopener" target="_blank" title=") **for test report analysis and publishing.**_

* Make Git, Node, and SonarQube scanner available to Jenkins. This can be done from the **Global Tool Configuration** menu in the **Manage Jenkins** menu. You can either chose to install automatically or provide the installation path for these tools. For example:

![Image](https://cdn-media-1.freecodecamp.org/images/tE0Qjwua7ul3uwGOM-gYThmyhfJD82ASDDt3)
_Providing the path for local installation._

* Lastly, make Jenkins aware of the SonarQube server installation from the **Configure** menu in **Manage Jenkins**. For example:

![Image](https://cdn-media-1.freecodecamp.org/images/SAtVBrKnLxF4kfg2zHLxnQkjvEB3stLLLoXb)
_SonarQube Server url configuration in Jenkins_

Download [SonarQube](https://www.sonarqube.org/) and set it up on your server. It is usually a simple package extraction on all platforms.

To enable Typescript support in SonarQube, we will use the [**SonarTsPlugin**](https://github.com/Pablissimo/SonarTsPlugin) since SonarQube doesn’t yet have a default plugin for Typescript. Simply download the jar from the [releases page](https://github.com/Pablissimo/SonarTsPlugin/releases) of the plugin and place it in your SonarQube installations `**bin**` folder. Restart Jenkins once. That is all.

In the Angular projects `**karma.conf.js**` file, change/add to the `browsers` section `ChromeHeadless`.

Example: `**browsers:['ChromeHeadless']**` . From version 60 onwards [Google Chrome supports headless](https://developers.google.com/web/updates/2017/04/headless-chrome) mode on Windows as well. So you can continue to use this setting on local machine as well, in case you work on a Windows machine in an enterprise environment (as I do). I personally prefer the headless mode only for the 1–2 seconds that it saves me.

Add the following to the `**scripts**` section in `**package.json**` file.

![Image](https://cdn-media-1.freecodecamp.org/images/RXJqP0brv2WpNbxhjnmxG8522mLee71UonFR)
_NPM command for test followed by build_

The above command makes sure that the build is **only triggered if all the tests are successful**. The `**--cc**` flag is a short code for `**--code-coverage**`. This flag will produce the projects coverage report in a new folder named `**coverage**` within the project directory. The report file is named `**lcov.info**`.

The default configuration uses Istanbul reporter to show the code coverage report. To publish this coverage report to SonarQube server, the Jenkins SonarQube scanner plugin requires a configuration which can be added as a `**sonar-project.properties**` file to the project or within the Jenkins project configuration. Example properties file:

![Image](https://cdn-media-1.freecodecamp.org/images/WlS8OKVSTkUI6CcXgAn-crU-tpNVTWfHbLoS)
_Sample sonar-project.properties file._

### Configuration

With the above steps done, the project configuration in Jenkins is fairly simple.

First create a new configuration using **New Item** menu and then a **Freestyle project**.

Next in the **Source Code Management** section enable **Git** and setup the projects repo URL:

![Image](https://cdn-media-1.freecodecamp.org/images/5gEgzqe6qCIPmd60CTD0XzzvlU7AGf3hisnz)
_Repo setup in Jenkins project configuration._

In the **Build Environment** section, enable the checkbox for providing the node and npm environment to the build configuration.

![Image](https://cdn-media-1.freecodecamp.org/images/m2ioZHC6dtQwyNJq4uS260Xffyxne4oEVlHs)
_Provide node and npm to current build._

Then in the **Build** sectionn add two build steps. First **Execute Shell** and second **Execute SonarQube Scanner**.

The shell step is to run the `**cibuild**` npm script and the latter to trigger the coverage report analysis. As mentioned above, the sonar properties can be set in the build configuration as well. Example build configuration:

![Image](https://cdn-media-1.freecodecamp.org/images/olqC-tt1a7qk6BgZxJjOH9iHiLejWRyE5vuD)
_Build section with npm and sonar analysis_

That is all. Now a build can be triggered using the **Build Now** menu on the projects home page.

> _The build log will show the test results, the build logs, and the publish log to SonarQube server. It is ideal to setup remote triggers or web hooks to trigger the project build. This will ensure the stability of the project whenever there is a change in the repo._

Finally, on visiting the SonarQube server, the project details should be visible with all the metrics captured from code coverage report. Example:

![Image](https://cdn-media-1.freecodecamp.org/images/v3aWz3iidRPk0KIDZRnI2A26a9uEFRaqSm3I)
_Sonar Projects Dashboard._

This is only the first step towards creating a healthier code base. The Jenkins build can be further enhanced to create a pipeline build for better control and granular modifications.

_Originally published at [medium.com](https://medium.com/@ashishgkwd/angular-fitbit-jenkins-sonarqube-829cc6201469) on September 16, 2017._

