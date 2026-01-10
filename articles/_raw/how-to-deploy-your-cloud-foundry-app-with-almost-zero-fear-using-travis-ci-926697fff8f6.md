---
title: How to deploy your Cloud Foundry app with (almost) zero fear using Travis CI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-15T17:19:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-your-cloud-foundry-app-with-almost-zero-fear-using-travis-ci-926697fff8f6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PXXH-HGbEP2x3LWooWGLlA.jpeg
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: Devops
  slug: devops
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Robin Bobbitt

  Application deployments to the cloud should be painless. We should be able to deploy
  new code continuously, as often as we want, without fear. The blue-green deployment
  model enables us to do this.

  I recently joined a new team at wor...'
---

By Robin Bobbitt

Application deployments to the cloud should be painless. We should be able to deploy new code continuously, as often as we want, without fear. The [blue-green deployment](https://docs.cloudfoundry.org/devguide/deploy-apps/blue-green.html) model enables us to do this.

I recently joined a new team at work that was deploying node.js Cloud Foundry applications to the IBM Cloud using Travis with the [Bluemix CloudFoundry deployment provider](https://docs.travis-ci.com/user/deployment/bluemixcloudfoundry/). This works great for quickly and easily setting up your deployment with just a few parameters.

Unfortunately, every deployment means an outage of your application as the existing version stops and the new version starts up. Also, there is no verification that the new code is good before the old code is blown away.

With the blue-green deployment technique, your current application (Blue) continues to run and take network traffic. While your new application code (Green) is deployed on a temporary route. The new Green application can be validated on the temporary route. If there are any problems, the deployment stops. The Blue application continues to serve traffic uninterrupted. Once the Green application is vetted, the router is updated to point at the Green application. The Blue can be stopped.

In this manner, there is always a version of the application available to take traffic. Any problems in the deployment or runtime of the new code will not impact the availability of your application.

I immediately started looking around for a way to blue-green deploy our applications. In the interest of writing as little custom code as possible, I decided to leverage the [cf-blue-green-deploy plugin](https://github.com/bluemixgaragelondon/cf-blue-green-deploy) for the Cloud Foundry command-line interface (CLI). I will share how I did this here.

I’m going to assume if you landed here you are probably past the point of simply [“getting started” with Travis](https://docs.travis-ci.com/user/getting-started/). I won’t be covering those details here.

If you’re not interested in following along and just want to get straight to the goods, you can clone my working sample from [GitHub](https://github.com/robinbobbitt/blue-green-cf-travis).

### **Installing the CF CLI and blue-green plugin**

Since we’re not using the Cloud Foundry [deployment provider](https://github.com/travis-ci/dpl), we have to install the Cloud Foundry CLI ourselves, as well as the blue-green deploy plugin. We can do this in the `before_deploy` phase of the [Travis build lifecycle](https://docs.travis-ci.com/user/customizing-the-build/).

Note that the `before_deploy` phase runs before each deployment provider. If you are doing additional things in your deploy phase, you may want to move these steps into the `after_success` phase (which runs just once after a successful build) to avoid unnecessary extra installs. You could also move these steps into the deploy script itself, which we will be writing next.

Regardless of where you put it, here is the script:

```
- echo "Installing cf cli"- test x$TRAVIS_OS_NAME = "xlinux" && rel="linux64-binary" || rel="macosx64"; wget "https://cli.run.pivotal.io/stable?release=${rel}&source=github" -qO cf.tgz && tar -zxvf cf.tgz && rm cf.tgz- export PATH="$PATH:."- cf --version
```

```
- echo "Installing cf blue-green deploy plugin"- cf add-plugin-repo CF-Community https://plugins.cloudfoundry.org- cf install-plugin blue-green-deploy -r CF-Community -f
```

The command to install the CLI comes directly from the CloudFoundry DPL [source](https://github.com/travis-ci/dpl/blob/master/lib/dpl/provider/cloud_foundry.rb). The commands to install the blue-green deploy plugin come from the plugin’s [README](https://github.com/bluemixgaragelondon/cf-blue-green-deploy).

### **Invoking the blue-green deploy**

To invoke the blue-green deploy, we will use the [script deployment provider](https://github.com/travis-ci/dpl#script), which executes a provided command and checks for zero status as indication of success.

```
deploy:# on update to master branch we deploy to Cloud Foundry- provider: script  skip_cleanup: true  script:  ./scripts/cf-blue-green-deploy.sh blue-green-cf-travis manifest.yml prod  on:    branch: master
```

Note that `skip_cleanup` is set to `true`. Without this, the cf CLI and blue-green deploy plugin you just installed would be removed prior to the deploy running.

The [cf-blue-green-deploy.sh script](https://github.com/robinbobbitt/blue-green-cf-travis/blob/master/scripts/cf-blue-green-deploy.sh) logs in to the Cloud Foundry API and invokes the blue-green deploy plugin. In addition to specifying an application name and manifest file, you can also pass a smoke test script to the blue-green deploy plugin. The plugin will call the smoke test script after the new application code has been deployed, but before the application route is switched to the new application. This allows you to run any number of tests against the new code before any real traffic accesses it.

The smoke test script is passed a single argument. The argument is the temporary URL of the newly deployed application. If the smoke test script exits with success, the blue-green deploy will complete by switching the route to the new application. If the smoke test script exits with a failure, traffic continues to flow to the old version of the application. The new version remains available for troubleshooting.

In my example project, the smoke test script invokes a /version API and verifies that it returns with a 200 status code.

In our real projects at work, we run a Postman collection against the newly deployed app. You want your smoke test suite to be sufficiently big enough that you feel confident in your new code, but not so big that it takes a long time to complete a deployment or flaky tests block you from completing a successful deploy.

You could optionally run a more comprehensive suite of regression tests as an `after_deploy` step, after your new code is live.

### **Side effects of a blue-green deploy in IBM Cloud**

There are a few nuances of this approach to be aware of if you are deploying to IBM Cloud. Because you are creating a new CF application instance each time you blue-green deploy, your application guid will change. If you use the Availability Monitoring service, your configured tests will be lost when your guid changes.

To work around this, stand up a permanent dummy application. Write your tests for your blue-green deployed app in this dummy application’s configuration. You can specify any URL when you write your Availability Monitoring tests.

Similarly, if you use the Log Analysis service, you’ll see that when you click the “View in Kibana” link on your application dashboard’s Logs tab, you will be launched into a Kibana search on the application guid string. Any application logs from before your most recent deployment will not show up. To work around this, you can simply filter on the application name rather than the application guid.

Another service that has the same issue is Auto-Scaling. Each time a new application is stood up as part of the blue-green deploy, it needs its Auto-Scaling policy reconfigured. There is a command line interface available that you presumably could use to script this, but I have not yet had a need to try this.

If any of these issues are non-starters for you, you always have the option of writing a custom blue-green deploy script that leverages two permanent CF applications, a blue, and a green. These two apps would take turns being live and being idle. You could configure both applications with an auto-scaling policy, for example.

Of course, this approach means you can’t take advantage of the blue-green deploy plugin described in this post, and you need to maintain your own custom script.

### **Wrapping up**

In this post, we’ve examined how we can accomplish a low risk, zero-downtime deployment using Travis and the cf blue-green deploy plugin.

In a real project, we would have even greater assurances, as we would have a suite of unit tests in place, and errors there would fail the Travis build before the deployment had a chance to run. We would also potentially have dev and staging branches configured to deploy to their own respective spaces in our Cloud Foundry organization, allowing us to validate and stabilize the application as necessary before promoting changes to production.

Thanks for reading! This is my first Medium story, and I hope you found it useful.

