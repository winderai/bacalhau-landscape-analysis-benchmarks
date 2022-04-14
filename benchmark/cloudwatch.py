from email.policy import default
import os
import datetime
from datetime import date, timedelta, datetime
import pprint
import argparse
import pytz

import boto3
import pandas as pd


def main(args):
   print(args)
   host_ip = args.host_ip
   # Create CloudWatch client
   cloudwatch = boto3.client('cloudwatch', region_name=args.aws_region)
   start_time = datetime.fromtimestamp(int(float(args.start_time)), pytz.timezone("UTC"))
   end_time = datetime.fromtimestamp(int(float(args.end_time)), pytz.timezone("UTC"))
   output_dir = args.output_dir
   print("start_time: {}".format(start_time))
   print("end_time: {}".format(end_time))

   paginator = cloudwatch.get_paginator('list_metrics')
   metrics = []
   for response in paginator.paginate(Dimensions=[{"Name": "host", "Value": host_ip}],
                   Namespace='CWAgent'):
      for metric in response['Metrics']:
         if ("cpu" in metric['MetricName']) or ("mem" in metric['MetricName']) or ("diskio" in metric['MetricName']):
         # if ("cpu" in metric['MetricName']):
            metrics.append(metric)
   
   metric_data_queries = []
   for metric in metrics:
      try:
         id = metric["MetricName"] + "_" + metric['Dimensions'][1]['Value']
      except:
         id = metric["MetricName"] + "_" + metric['Dimensions'][0]['Value']
      id = id.replace("-", "_")
      metric_data_queries.append(
         {
               'Id': id,
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
   # pprint.pprint(response)
   data = response['MetricDataResults']

   all_metrics_data = []
   for metric in data:
      print(metric)
      metric_data = {
         'metric_name': metric['Id'], 
         'timestamp': metric['Timestamps'], 
         'metric_value': metric['Values'],
         'label': metric['Label'],
         'host': host_ip,
      }
      df_metric = pd.DataFrame.from_dict(metric_data)
      all_metrics_data.append(df_metric)
   df = pd.concat(all_metrics_data)

   print(df['metric_name'].unique())
   print(df)
   if output_dir:
      df.to_csv(output_dir + "/" + "{}_{}_{}".format(host_ip, args.start_time, args.end_time) + ".csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host_ip",
        type=str,
        required=True,
        help="EC2 instance's private IP name e.g. 'ip-172-31-12-99'"
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