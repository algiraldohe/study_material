# Import the necessary libraries
# Since we are using Python, import the SparkSession and related functions
# from the PySpark module

import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("Usage: mnmcount <file>", file=sys.stderr)
        sys.exit(-1)



# Build a SparkSession using the SparkSession APIs.
# If one does not exists, then create an instance. There
# can only be on SparkSession per JVM.

spark = (SparkSession
    .builder
    .appName("PythonMnMCount")
    .getOrCreate())

spark.sparkContext.setLogLevel('WARN')

# Get the M&M dataset filename from the commad-line arguments
mnm_file = sys.argv[1]

# Read the file into a Spark DataFrame using CSV
# format by inferring the schema and specifying that the
# file contains a header, which provides column names from comma-
# separated fields.

mnm_df = (spark.read.format('csv')
    .option('header', 'true')
    .option('inferSchema', 'true')
    .load(mnm_file))

# We use the DataFrame high-level APIs. Note
# that we don't use RDDs at all. Because some of Spark's
# functions return same object, we can chain function cals.
# 1. Select from the DataFrame the fields 'State', 'Color', and 'Count'
# 2. Since we want to group each state and its M&M color count,
#    we use groupBy()
# 3. Aggregate counts of all colors and groupBy() State and Color
# orderBy() in descending order

count_mnm_df = (mnm_df
    .select('State', 'Color', 'Count')
    .groupBy('State', 'Color')
    .agg(count('Count').alias('Total'))
    .orderBy('Total', ascending=True))

# Show the resulting aggregations for all the states and colors;
# a total count of each color per state.
# Note show() is an action, which will trigger the above
# query to be executed.

count_mnm_df.show(n=60, truncate=False)
print('Total Rows = %d' % (count_mnm_df.count()))


# While the above code aggregated and counted for all
# the states, what if we just want to see the data for 
# a single state e.g. 'CA'?
# 1. Select from all rows in the DataFrame
# 2. Filter only CA state
# 3. groupBy() State and color as we did above
# 5. orderBy()
# Find the aggregate count for California by filtering
ca_count_mnm_df = (mnm_df
    .select('State', 'Color', 'Count')
    .where(mnm_df.State == 'CA')
    .groupby('State', 'Color')
    .agg(count('Count').alias('Total'))
    .orderBy('Total', ascending=False))

# Show the resulting aggregation for California.
# As above, show() is an action that will trigger the execution
# of the entire computation.
ca_count_mnm_df.show(n=10, truncate=False)

# Stop the SparkSession
spark.stop()



