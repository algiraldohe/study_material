from pyspark.sql import SparkSession
from pyspark.sql.types import *
import sys


# Define the schema for our data programmatically
schema = StructType([StructField('Id', IntegerType(), False), 
                     StructField('First', StringType(), False), 
                     StructField('Last', StringType(), False),
                     StructField('Url', StringType(), False),
                     StructField('Published', StringType(), False),
                     StructField('Hits', IntegerType(), False),
                     StructField('Campaigns', ArrayType(StringType()), False)])

# Main program
if __name__ == '__main__':
    # Create SparkSession
    spark = (SparkSession
            .builder
            .appName('read_json')
            .getOrCreate())

    # Read data from JSON file
    json_file = sys.argv[1]
  
    # Create a DataFrame by reading from the JSON file
    # with a predefined schema
    blogs_df = spark.read.schema(schema).json(json_file)

    # Show DataFrame
    blogs_df.show()

    # Print the schema
    print(blogs_df.printSchema)
    print(blogs_df.schema)
