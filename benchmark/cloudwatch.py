from email.policy import default
import os
import datetime
from datetime import date, timedelta, datetime
import pprint
import argparse

import boto3
import pandas as pd


def main(args):
   print(args)
   host_ip = args.host_ip
   # Create CloudWatch client
   cloudwatch = boto3.client('cloudwatch', region_name=args.aws_region)
   start_time = datetime.fromtimestamp(int(float(args.start_time)))
   end_time = datetime.fromtimestamp(int(float(args.end_time)))
   output_dir = args.output_dir

   # paginator = cloudwatch.get_paginator('list_metrics')
   # for response in paginator.paginate(Dimensions=[{"Name": "host", "Value": "ip-172-31-43-56"}],
   #                 Namespace='CWAgent'):
   #     pprint.pprint(response)

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


   response = cloudwatch.get_metric_data(
      MetricDataQueries=metric_data_queries,
         StartTime=start_time, 
         EndTime=end_time,
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

   print(df)
   if output_dir:
      df.to_csv(output_dir + "/" + "{}_{}_{}".format(host_ip, args.start_time, args.end_time) + ".csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host_ip",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--aws_region",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--start_time",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--end_time",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        required=False,
        default=None
    )
    args = parser.parse_args()
    main(args)