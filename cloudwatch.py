import datetime
from datetime import date, timedelta, datetime
import pprint

import boto3
import pandas as pd

# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch', region_name='eu-central-1')



# paginator = cloudwatch.get_paginator('list_metrics')
# for response in paginator.paginate(Dimensions=[{"Name": "host", "Value": "ip-172-31-43-56"}],
#                 Namespace='CWAgent'):
#     pprint.pprint(response)



host_ip = "ip-172-31-43-56"

metrics = [{
    "Dimensions":[
       {
          "Name":"host",
          "Value":host_ip
       },
       {
          "Name":"cpu",
          "Value":"cpu0"
       }
    ],
    "MetricName":"cpu_usage_user",
    "Namespace":"CWAgent"
 },
 {
    "Dimensions":[
       {
          "Name":"host",
          "Value":host_ip
       },
       {
          "Name":"cpu",
          "Value":"cpu0"
       }
    ],
    "MetricName":"cpu_usage_system",
    "Namespace":"CWAgent"
 },
 {
    "Dimensions":[
       {
          "Name":"host",
          "Value":host_ip
       },
       {
          "Name":"cpu",
          "Value":"cpu0"
       }
    ],
    "MetricName":"cpu_usage_idle",
    "Namespace":"CWAgent"
 },
 {
    "Dimensions":[
       {
          "Name":"host",
          "Value":host_ip
       },
       {
          "Name":"cpu",
          "Value":"cpu0"
       }
    ],
    "MetricName":"cpu_usage_iowait",
    "Namespace":"CWAgent"
 },
 {
    "Dimensions":[
       {
          "Name":"host",
          "Value":host_ip
       }
    ],
    "MetricName":"mem_used_percent",
    "Namespace":"CWAgent"
 },
 {
    "Dimensions":[
       {
          "Name":"host",
          "Value":host_ip
       },
       {
          "Name":"name",
          "Value":"xvda1"
       }
    ],
    "MetricName":"diskio_io_time",
    "Namespace":"CWAgent"
 },
 {
    "Dimensions":[
       {
          "Name":"host",
          "Value":host_ip
       },
       {
          "Name":"name",
          "Value":"xvda"
       }
    ],
    "MetricName":"diskio_writes",
    "Namespace":"CWAgent"
 },
 {
    "Dimensions":[
       {
          "Name":"host",
          "Value":host_ip
       },
       {
          "Name":"name",
          "Value":"xvda"
       }
    ],
    "MetricName":"diskio_reads",
    "Namespace":"CWAgent"
 }
]


metric_data_queries = []
for metric in metrics:
    metric_data_queries.append(
        {
            'Id': metric["MetricName"],
            'MetricStat': {
                'Metric': metric,
                'Period': 60,
                'Stat': 'Average',
            },
            'ReturnData': True,
        }
    )

# pprint.pprint(metric_data_queries)


yesterday=date.today() - timedelta(days=1)
tomorrow=date.today() + timedelta(days=1)

print(datetime(yesterday.year, yesterday.month, yesterday.day))
print(datetime(tomorrow.year, tomorrow.month, tomorrow.day))

response = cloudwatch.get_metric_data(
    MetricDataQueries=metric_data_queries,
        StartTime=datetime(yesterday.year, yesterday.month, yesterday.day), 
        EndTime=datetime(tomorrow.year, tomorrow.month, tomorrow.day),
)

#pprint.pprint(response)
data = response['MetricDataResults']

all_metrics_data = []
for metric in data:
    metric_data = {
        'metric_name': metric['Id'], 
        'timestamp': metric['Timestamps'], 
        'metric_value': metric['Values'],
        'host': host_ip,
    }
    df_metric = pd.DataFrame.from_dict(metric_data)
    all_metrics_data.append(df_metric)

df = pd.concat(all_metrics_data)

#print(df)


df.to_csv("./" + host_ip + ".csv")