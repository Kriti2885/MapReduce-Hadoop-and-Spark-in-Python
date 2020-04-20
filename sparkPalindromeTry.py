#!/usr/bin/env python3
import os
import pyspark
from pyspark import SparkContext, SparkConf
from collections import defaultdict
from pyspark.sql.types import Row


def findPalindrome(x):
    if((x == x[::-1]) & (len(x)>1)):    # Checking for reverse of string and length
        return x


sc = pyspark.SparkContext()
print("Job Running..")
rddData = sc.textFile("gs://dataproc-37bf26ad-209a-48cf-9193-c82e1c017f8c-us-central1/dummyData/*")

splittedData = rddData.flatMap(lambda x: x.split(" "))
loweredData = splittedData.map(lambda x: x.lower())
alpha_numData = loweredData.map(lambda x: ''.join(e for e in x if e.isalnum()))
cleanedData = alpha_numData.filter(lambda x: len(x)>1)
palindrome = cleanedData.map(findPalindrome)
palindrome_filtered = palindrome.filter(lambda x: x!=None)  #Palindromes
result = sorted(palindrome_filtered.collect())
sorted(list(set(result)))   # Checking for duplicates
reduced_result =[]
for i in range(len(result)):
   if result[i] not in reduced_result:
        reduced_result.append(result[i])
reduced = sorted(reduced_result)

print(reduced)
rdd = sc.parallelize(reduced)
rdd.saveAsTextFile("gs://dataproc-37bf26ad-209a-48cf-9193-c82e1c017f8c-us-central1/dummy_output_spark_palindrome")
