#!/usr/bin/env python3
import os
import pyspark
from pyspark import SparkContext, SparkConf
from collections import defaultdict
from pyspark.sql.types import Row


def sortchars(w):
    return ("".join(sorted(w)), [w])

def to_list(a):
    return [a]
def append(a, b):
    a.append(b)
    return a

def extend(a, b):
    a.extend(b)
    return a

sc = pyspark.SparkContext()
print("Job Running..")
rddData = sc.textFile("gs://dataproc-37bf26ad-209a-48cf-9193-c82e1c017f8c-us-central1/dummyData/*")

splittedData = rddData.flatMap(lambda x: x.split(" "))
loweredData = splittedData.map(lambda x: x.lower())
alpha_numData = loweredData.map(lambda x: ''.join(e for e in x if e.isalnum()))
cleanedData = alpha_numData.filter(lambda x: len(x)>1)
wordskv = cleanedData.map(sortchars)

groupedRDD = wordskv.combineByKey(to_list, append, extend)

result = sorted(groupedRDD.collect())
reduced_result =[]
for i in range(len(result)):
    l = result[i][1]
    flatten = [item for sublist in l for item in sublist]
    values = list(set(flatten))
    # print(values)
    if len(values)>1:
        reduced_result.append((result[i][0], values))
reduced_result.sort(key = lambda x: x[1])
rdd = sc.parallelize(reduced_result)
rdd.saveAsTextFile("gs://dataproc-37bf26ad-209a-48cf-9193-c82e1c017f8c-us-central1/dummy_output_spark_anagram")
