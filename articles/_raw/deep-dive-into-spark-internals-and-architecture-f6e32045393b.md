---
title: Deep-dive into Spark internals and architecture
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-14T20:18:53.000Z'
originalURL: https://freecodecamp.org/news/deep-dive-into-spark-internals-and-architecture-f6e32045393b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EzZs4uEuO30lV51KV07_RA.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: spark
  slug: spark
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Jayvardhan Reddy

  Apache Spark is an open-source distributed general-purpose cluster-computing framework.
  A spark application is a JVM process that’s running a user code using the spark
  as a 3rd party library.

  As part of this blog, I will be showin...'
---

By Jayvardhan Reddy

**_Apache Spark_** is an open-source distributed general-purpose cluster-computing framework. A spark application is a JVM process that’s running a user code using the spark as a 3rd party library.

As part of this blog, I will be showing the way Spark works on Yarn architecture with an example and the various underlying background processes that are involved such as:

* Spark Context
* Yarn Resource Manager, Application Master & launching of executors (containers).
* Setting up environment variables, job resources.
* CoarseGrainedExecutorBackend & Netty-based RPC.
* SparkListeners.
* Execution of a job (Logical plan, Physical plan).
* Spark-WebUI.

#### **Spark Context**

Spark context is the first level of entry point and the heart of any spark application. **_Spark-shell_** is nothing but a Scala-based REPL with spark binaries which will create an object sc called spark context.

We can launch the spark shell as shown below:

```
spark-shell --master yarn \ --conf spark.ui.port=12345 \ --num-executors 3 \ --executor-cores 2 \ --executor-memory 500M
```

As part of the spark-shell, we have mentioned the num executors. They indicate the number of worker nodes to be used and the number of cores for each of these worker nodes to execute tasks in parallel.

Or you can launch spark shell using the default configuration.

```
spark-shell --master yarn
```

The configurations are present as part of **spark-env.sh**

![Image](https://cdn-media-1.freecodecamp.org/images/-6BLEYtF8novhDmJFdm5jOcRIcU2BnIeIMSY)

Our Driver program is executed on the Gateway node which is nothing but a spark-shell. It will create a spark context and launch an application.

![Image](https://cdn-media-1.freecodecamp.org/images/AfCWOl6WV-LTqqOBZhu1vmZgAdxTuEUO0NXm)

The spark context object can be accessed using **sc.**

![Image](https://cdn-media-1.freecodecamp.org/images/XddrUMFGYv0CZtW0KVYll8t6gH0B-vsdJrZJ)

After the Spark context is created it waits for the resources. Once the resources are available, Spark context sets up internal services and establishes a connection to a Spark execution environment.

#### **Yarn Resource Manager, Application Master & launching of executors (containers).**

Once the Spark context is created it will check with the **_Cluster Manager_** and launch the **_Application Master_** i.e, launches a container and registers signal handlers**_._**

![Image](https://cdn-media-1.freecodecamp.org/images/cjo3Db6Bu6YAfbynbMqAnUeZwq7b2gyDktzI)

![Image](https://cdn-media-1.freecodecamp.org/images/oPN9axnzYJYOD4uVrgnAFHavgelG7PU6qcxC)

Once the Application Master is started it establishes a connection with the Driver.

![Image](https://cdn-media-1.freecodecamp.org/images/HNXgewZ5xbv1rnAtlAkrVX8cIpM57MEAPUUF)

Next, the ApplicationMasterEndPoint triggers a proxy application to connect to the resource manager.

![Image](https://cdn-media-1.freecodecamp.org/images/qYP4KcyLx47l13m2rK7DmHz1v3HjjvOvfCfc)

Now, the Yarn Container will perform the below operations as shown in the diagram.

![Image](https://cdn-media-1.freecodecamp.org/images/Nn-uzm4KF38fk3GEP46x6nHaRY4qEiF0OKZv)
_Image Credits: [jaceklaskowski.gitbooks.io](https://jaceklaskowski.gitbooks.io/mastering-apache-spark/yarn/spark-yarn-applicationmaster.html" rel="noopener" target="_blank" title=")_

ii) YarnRMClient will register with the Application Master.

![Image](https://cdn-media-1.freecodecamp.org/images/L-1dKAks3zKzEG-3LQjUb59y87o32NwCm0CH)

iii) YarnAllocator: Will request 3 executor containers, each with 2 cores and 884 MB memory including 384 MB overhead

![Image](https://cdn-media-1.freecodecamp.org/images/k8JzuqdtEIr30S2i9FDqjLfuCU0fdx1V7hJ9)

iv) AM starts the Reporter Thread

![Image](https://cdn-media-1.freecodecamp.org/images/0ivLtRFO8U-sXl9auRRFgjaIiCRl7ggf5gEU)

Now the Yarn Allocator receives tokens from Driver to launch the Executor nodes and start the containers.

![Image](https://cdn-media-1.freecodecamp.org/images/ISQkVVySYyDsBWkE5i3OEi-JI602MXyd1SpG)

#### **Setting up environment variables, job resources & launching containers.**

Every time a container is launched it does the following 3 things in each of these.

* Setting up env variables

Spark Runtime Environment (SparkEnv) is the runtime environment with Spark’s services that are used to interact with each other in order to establish a distributed computing platform for a Spark application.

![Image](https://cdn-media-1.freecodecamp.org/images/IuLu5w5LZBGd3LNj5HMD7hUA8M0f9KpdQO4T)

![Image](https://cdn-media-1.freecodecamp.org/images/WvPtwOF6swG4mdHfNdA7SNiaoW1WSAu5b16C)

* Setting up job resources

![Image](https://cdn-media-1.freecodecamp.org/images/-4Kq6oTpBIzxXxJslrnyja9NvEYOVK0fN8Eo)

* Launching container

![Image](https://cdn-media-1.freecodecamp.org/images/eovWnCKboFLKrabJTkQeheqlSEL1pjvYzyIQ)

YARN executor launch context assigns each executor with an executor id to identify the corresponding executor (via Spark WebUI) and starts a CoarseGrainedExecutorBackend.

![Image](https://cdn-media-1.freecodecamp.org/images/HwkvxgUxXrbP-sSlod7ww2ON730xBNoCD5OL)

#### **CoarseGrainedExecutorBackend & Netty-based RPC.**

After obtaining resources from Resource Manager, we will see the executor starting up

![Image](https://cdn-media-1.freecodecamp.org/images/JV2n4sSeorLmRQeqYV5qnX0VipHO7UDpOTDs)

**_CoarseGrainedExecutorBackend_** is an ExecutorBackend that controls the lifecycle of a single executor. It sends the executor’s status to the driver.

When ExecutorRunnable is started, CoarseGrainedExecutorBackend registers the Executor RPC endpoint and signal handlers to communicate with the driver (i.e. with CoarseGrainedScheduler RPC endpoint) and to inform that it is ready to launch tasks.

![Image](https://cdn-media-1.freecodecamp.org/images/eCIDgTM7qIHET63gN0hT3bURjLreHK0clFvD)

**_Netty-based RPC -_** It is used to communicate between worker nodes, spark context, executors.

![Image](https://cdn-media-1.freecodecamp.org/images/enybOZ6oQRaFwrbnQIbxdcEYf4taktLy8-vO)

NettyRPCEndPoint is used to track the result status of the worker node.

RpcEndpointAddress is the logical address for an endpoint registered to an RPC Environment, with RpcAddress and name.

It is in the format as shown below:

![Image](https://cdn-media-1.freecodecamp.org/images/kLkRsIqy4YhYzRXyUuDroQHeNgxu7Vozk1Gp)

This is the first moment when CoarseGrainedExecutorBackend initiates communication with the driver available at driverUrl through RpcEnv.

![Image](https://cdn-media-1.freecodecamp.org/images/de85dQifuBDHqUZdqmXrl14e3LYMJuHvQZKP)

#### **SparkListeners**

![Image](https://cdn-media-1.freecodecamp.org/images/AIHRmLNMZpTUpgYFqylC0FeveeYLmLjbnZbo)
_Image Credits:[ jaceklaskowski.gitbooks.io](https://jaceklaskowski.gitbooks.io/mastering-apache-spark/spark-scheduler-LiveListenerBus.html" rel="noopener" target="_blank" title=")_

SparkListener (Scheduler listener) is a class that listens to execution events from Spark’s DAGScheduler and logs all the event information of an application such as the executor, driver allocation details along with jobs, stages, and tasks and other environment properties changes.

SparkContext starts the LiveListenerBus that resides inside the driver. It registers JobProgressListener with LiveListenerBus which collects all the data to show the statistics in spark UI.

By default, only the listener for WebUI would be enabled but if we want to add any other listeners then we can use **spark.extraListeners.**

Spark comes with two listeners that showcase most of the activities

i) StatsReportListener

ii) EventLoggingListener

**_EventLoggingListener:_** If you want to analyze further the performance of your applications beyond what is available as part of the Spark history server then you can process the event log data. Spark Event Log records info on processed jobs/stages/tasks. It can be enabled as shown below...

![Image](https://cdn-media-1.freecodecamp.org/images/haTAg5LO0bzKsjjXZbpE26AkR2Is2nLBbOzF)

The event log file can be read as shown below

* The Spark driver logs into job workload/perf metrics in the spark.evenLog.dir directory as JSON files.
* There is one file per application, the file names contain the application id (therefore including a timestamp) application_1540458187951_38909.

![Image](https://cdn-media-1.freecodecamp.org/images/ecY6tTy-i4s3mmYZoAhraM2KENWWtVgJD8wY)

It shows the type of events and the number of entries for each.

![Image](https://cdn-media-1.freecodecamp.org/images/ANujSUpy0IQexpkoae-HfMFckmOPwCLV1-ve)

Now, let’s add **_StatsReportListener_** to the spark.extraListeners and check the status of the job.

Enable INFO logging level for org.apache.spark.scheduler.StatsReportListener logger to see Spark events.

![Image](https://cdn-media-1.freecodecamp.org/images/B7HGuBTSYxAa6Ep8B47LncJicPMXZiT6bkPP)

To enable the listener, you register it to SparkContext. It can be done in two ways.

i) Using SparkContext.addSparkListener(listener: SparkListener) method inside your Spark application.

Click on the link to implement custom listeners - [**CustomListener**](https://stackoverflow.com/questions/24463055/how-to-implement-custom-job-listener-tracker-in-spark)

ii) Using the conf command-line option

![Image](https://cdn-media-1.freecodecamp.org/images/eOkpNJ380lOHphroPJjCYtKcBTrnwCMncM7G)

Let’s read a sample file and perform a count operation to see the StatsReportListener.

![Image](https://cdn-media-1.freecodecamp.org/images/C5Aro1tHenM1CulhoUqtcvbg487-4TfhrNfR)

#### **Execution of a job (Logical plan, Physical plan).**

In Spark, RDD (_resilient distributed dataset_) is the first level of the abstraction layer. It is a collection of elements partitioned across the nodes of the cluster that can be operated on in parallel. RDDs can be created in 2 ways.

**i) P_arallelizing_ an existing collection in your driver program**

![Image](https://cdn-media-1.freecodecamp.org/images/URNJDr-DZdPfXLVbiWQrEe2-PEX0-p67g1mw)

**ii) Referencing a dataset in an external storage system**

![Image](https://cdn-media-1.freecodecamp.org/images/mFYIkS67sITmSz7SV1MOfFDaMVh-jWQB4ARv)

RDDs are created either by using a file in the Hadoop file system, or an existing Scala collection in the driver program, and transforming it.

Let’s take a sample snippet as shown below

![Image](https://cdn-media-1.freecodecamp.org/images/H4qJqN74iIRbDBWx6qhi9Uuqr7EFNTKYT2Df)

The execution of the above snippet takes place in 2 phases.

**_6.1 Logical Plan:_** In this phase, an RDD is created using a set of transformations, It keeps track of those transformations in the driver program by building a computing chain (a series of RDD)as a Graph of transformations to produce one RDD called a **_Lineage Graph_**.

Transformations can further be divided into 2 types

* **Narrow transformation:** A pipeline of operations that can be executed as one stage and does not require the data to be shuffled across the partitions — for example, Map, filter, etc..

![Image](https://cdn-media-1.freecodecamp.org/images/y0iv0YErJYvRwvm8BEEqw9KhIVM5IM54FLJZ)

Now the data will be read into the driver using the broadcast variable.

![Image](https://cdn-media-1.freecodecamp.org/images/LpuhSTa3XXdggW9J4e52QXTSNGKIbBzwOYdY)

* **Wide transformation:** Here each operation requires the data to be shuffled, henceforth for each wide transformation a new stage will be created — for example, reduceByKey, etc..

![Image](https://cdn-media-1.freecodecamp.org/images/8Wzx99ex1SXX0WUPWTVPjzUTLbjS1j0QawFG)

We can view the lineage graph by using **_toDebugString_**

![Image](https://cdn-media-1.freecodecamp.org/images/Tiz7zB4BUl8KhLcyE9LFZMKzwt3RWt1Symj9)

**_6.2 Physical Plan:_** In this phase, once we trigger an action on the RDD, The **_DAG Scheduler_** looks at RDD lineage and comes up with the best execution plan with stages and tasks together with TaskSchedulerImpl and execute the job into a set of tasks parallelly.

![Image](https://cdn-media-1.freecodecamp.org/images/YYUBKfaYaYQiE7zrsdUOCNwSkcs8fll7FhyF)

Once we perform an action operation, the SparkContext triggers a job and registers the RDD until the first stage (i.e, before any wide transformations) as part of the DAGScheduler.

![Image](https://cdn-media-1.freecodecamp.org/images/5zSZlLhIownDYA1xRAuMjyG4waHL4M654lNn)

Now before moving onto the next stage (Wide transformations), it will check if there are any partition data that is to be shuffled and if it has any missing parent operation results on which it depends, if any such stage is missing then it re-executes that part of the operation by making use of the DAG( Directed Acyclic Graph) which makes it Fault tolerant.

![Image](https://cdn-media-1.freecodecamp.org/images/RbSQEIy9nbRolwQPc0lygIxhCa9odYAgaaP0)

In the case of missing tasks, it assigns tasks to executors.

![Image](https://cdn-media-1.freecodecamp.org/images/q2UCiTrCdl1D4Jr7uM47IbdStmXvOSW2LrNc)

Each task is assigned to CoarseGrainedExecutorBackend of the executor.

![Image](https://cdn-media-1.freecodecamp.org/images/QcoWEHGMvmiF5lBbmAN4oT1y5cOUt6kEZ0OB)

It gets the block info from the Namenode.

![Image](https://cdn-media-1.freecodecamp.org/images/smtnxaTQw1B5rzIQ0aoDgfcpZh4PL5GPhcrH)

now, it performs the computation and returns the result.

![Image](https://cdn-media-1.freecodecamp.org/images/pSG-NIrRKOV-LxRxXGLgbi2pizwgx2wiCZtB)

Next, the DAGScheduler looks for the newly runnable stages and triggers the next stage (reduceByKey) operation.

![Image](https://cdn-media-1.freecodecamp.org/images/o5SPhS1d8o1fG5klmiupU--BEc52ZvmaWbbA)

The ShuffleBlockFetcherIterator gets the blocks to be shuffled.

![Image](https://cdn-media-1.freecodecamp.org/images/aUU1-Z-0bbW8vZRS43DhJrwffkR6V0pHos2z)

Now the reduce operation is divided into 2 tasks and executed.

![Image](https://cdn-media-1.freecodecamp.org/images/U4WfZPLsoa76XL9bTz2xadadQD5cpZAVrTpq)

On completion of each task, the executor returns the result back to the driver.

![Image](https://cdn-media-1.freecodecamp.org/images/-8Pwz7cMv3GLJwRJSCZ42Bm-NeD98E91Zf1r)

Once the Job is finished the result is displayed.

![Image](https://cdn-media-1.freecodecamp.org/images/m3KpbqF4utduxP0wHb634aOREZf2LXehYoyu)

#### **Spark-WebUI**

Spark-UI helps in understanding the code execution flow and the time taken to complete a particular job. The visualization helps in finding out any underlying problems that take place during the execution and optimizing the spark application further.

We will see the Spark-UI visualization as part of the previous **step 6.**

Once the job is completed you can see the job details such as the number of stages, the number of tasks that were scheduled during the job execution of a Job.

![Image](https://cdn-media-1.freecodecamp.org/images/oMGL38wBVkMpbyBwDz8oUjn4J8HgUa6FkQcy)

On clicking the completed jobs we can view the DAG visualization i.e, the different wide and narrow transformations as part of it.

![Image](https://cdn-media-1.freecodecamp.org/images/QbHRUFsfBCmjW5Wjx-iwl1RKFG181TPvsso2)

You can see the execution time taken by each stage.

![Image](https://cdn-media-1.freecodecamp.org/images/EnqEsKsm7oOpyCmYjJUVJ78V6dP0tZwDYfr6)

On clicking on a Particular stage as part of the job, it will show the complete details as to where the data blocks are residing, data size, the executor used, memory utilized and the time taken to complete a particular task. It also shows the number of shuffles that take place.

![Image](https://cdn-media-1.freecodecamp.org/images/XABdREC97TPKB3l1tDHuvBT9fUo9oGnjFLm4)

Further, we can click on the Executors tab to view the Executor and driver used.

![Image](https://cdn-media-1.freecodecamp.org/images/VAWPvAI4Jst5MN4Z60ed29qgrhAgs2fy5Yd0)

Now that we have seen how Spark works internally, you can determine the flow of execution by making use of Spark UI, logs and tweaking the Spark EventListeners to determine optimal solution on the submission of a Spark job.

**Note_:_** The commands that were executed related to this post are added as part of my [GIT](https://github.com/Jayvardhan-Reddy/BigData-Ecosystem-Architecture) account.

Similarly, you can also read more here:

* [Sqoop Architecture in Depth](https://medium.freecodecamp.org/an-in-depth-introduction-to-sqoop-architecture-ad4ae0532583) with **code.**
* [HDFS Architecture in Depth](https://medium.com/plumbersofdatascience/hdfs-architecture-in-depth-1edb822b95fa) with **code**.
* [Hive Architecture in Depth](https://medium.com/plumbersofdatascience/hive-architecture-in-depth-ba44e8946cbc) with **code**.

If you would like too, you can connect with me on LinkedIn — [Jayvardhan Reddy](https://www.linkedin.com/in/jayvardhan-reddy-vanchireddy).

If you enjoyed reading it, you can click the clap and let others know about it. If you would like me to add anything else, please feel free to leave a response ?

