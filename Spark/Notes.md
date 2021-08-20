# Apache Spark [Python]

### Spark Performance: Scala or Python?
In general, most developers seems to agree that Scala wins in terms of Performance and concurrency: It's definitely faster than Python when you are working with Spark, and when you are talking about concurrency, it's sure that Scala and the Play Framework make it easy to write clean and performant async code.

**Concurrency:** Means multiple computations are happening at the same time, or being executed out-of-order, wuthout affecting final outcome.

**Play Framework**
Play Framework is an open-source web application framework which follows the model–view–controller architectural pattern. It is written in Scala and usable from other programming languages that are compiled to JVM bytecode, e.g. Java.

Asynchronous code allows for non-blocking I/O (Input & Output processing that permits other processing to continue before the transmission has finished). If your programming language does not support asynchronous programming, you'll need to make threads to execute lines of code in parallel.

When working with the *DataFrame API*, you do need to be wary of User Defined Functions (UDFs). Favor built-in expressions when working with Python. Also make sure not to pass your data between DataFrame and RDD unnecessarily, as the serialization and deserialization of the data transfer is particularly expensive.

**Serialization** is a process of converting an object into a sequence of bytes which can be persisted to a disk or database or can be sent through streams. the reverse process, creating an object from sequence of bytes, is called **Deserialization**

### RDD Actions versus Transformations
RDDs support two types of operations: transformations which create a new dataset from an existing one, and actions, which return a value to the driver program after running a computation on the dataset.

Nothing in a query plan is executed until an action is invoked.

### Using the Local Machine
Every computation expressed in high-level Strcutured APIs is decomposed into low-level optimized and generated RDD operations and then converted into Scala bytecode for the executors' JVMs. This generated RDD operation code is not accessible to users, nor is it the same as the user-facing RDD APIs

### Understanding Spark Application Concepts
**SparkSession** An object that provides a point of entry to interact with underlying Spark functionality. In an interactive Spark sheel, the Spark driver instantiates a SparkSession for you, while in a Spark application, you create a SparkSession object yourself.

**Job** A parallel computation consisting of multiple tasks that gets spawned in response to a Spark action.

**Stage** Each job gets divided into smaller sets of tasks that depends on each other.

**Task** A single unit of work or execution that will be sent to Spark executor

### Spark Optimization
A huge advantage of the lazy evaluation scheme is that Spark can inspect your computational query and ascertain how it can optimize it. This optimization can be done by either joinning or pipelinning some operations and assigning them to a stage, or breaking them into stages by determining *which operations require a shuffle or exchange of data across clusters.*

Transformations can be classified as having:
**Narrow Dependencies** where a single output partition can be computed from a single input partition, without any exchange of data.

**Wide Dependencies** where data from other partitions is read in, combined, and written to disk

## Apache Spark's Structured APIs

### RDDs
In Spark, RDD stands for Resilient Distributed Dataset. RDD is a core abstraction and logical data structures of Spark. RDD is a collection of elements divided into partitions and distributed to multiple nodes of the cluster to store and process data in parallel.

Here are three vital characteristics associated with an RDD:
* Dependencies
* Partitions
* Compute function: Partition => Iterator[T]

First, a list of *dependencies* that instructsSpark how an RDD is constructed with 
its inputs is required. When necessary to reproduce results, Spark can recreate an 
RDD from these dependencies and replicate operations on it. This characteristic 
gives RDDs *resiliency*.

Second, *partitions* provide Spark the ability to split the work to parallelize computation
on partitions across executors.

And finally, an RDD has a *compute function* that produces an Iterator[T] for the
data that will be stored in the RDD.

**DSL:** Domain Specific Language
**DDL:** Data definition Language



