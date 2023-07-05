###################################################################
"""

Cookie Cutter AWS Client values for the util

"""
###################################################################

import boto3
import re
from botocore.exceptions import ClientError, NoRegionError

from ..constants.common_constants import (
  NO_ITEM,
  CONST_EC2,
  CONST_IAM,
  CONST_STS,
  AWS_ERR_MSG,
  PIAB_IMAGES,
)

class AwsClient:
  def __init__(self):
    try:
      self.vpc_client = boto3.client(CONST_EC2)
      self.iam_client = boto3.client(CONST_IAM)
      self.sts_client = boto3.client(CONST_STS)
    except (ClientError, NoRegionError) as err:
      raise Exception(AWS_ERR_MSG) from err

  # Gather VPC Info
  def aws_describe_vpc(self):
    response = self.vpc_client.describe_vpcs()
    response_list []
    for x in response["Vpcs"]:
      temp_dir = {}
      temp_dir["VpcId"] = x["VpcId]
      temp_dir["Name"] = list(
        filter(lambda tag: tag["Key"] == "Name", x["Tags"])
      )[0]["Value"]
      response_list.append(temp_dir)
    return response_list

  # Gather Available AMI info
  def aws_describe_ami(self):
    response = self.vpc_client.describe_images()
    response_list []
    for x in response["Images"]:
      temp_dir = {}
      temp_dir["Name"] = x["Name]
      temp_dir["ImageId"] = x["ImageId"]
      response_list.append(temp_dir)
    return response_list

  # Gather SG info
  def aws_describe_sg(self, aws_vpc_id):
    response = self.vpc_client.describe_security_groups()
    response_list []
    for x in response["SecurityGroups"]:
      temp_dir = {}
      temp_dir["GroupName"] = x["GroupName]
      temp_dir["GroupId"] = x["GroupId"]
      response_list.append(temp_dir)
    response_list.append(NO_ITEM)
    return response_list

  # Get IAM role information
  def aws_get_role(self, aws_role):
    response_list []
    response = self.iam_client.get_role(RoleName=aws_role)
    response_list.append(response["Role"]["RoleId"])
    response_list.append(NO_ITEM)
    return response_list

  # Get IAM role information
  def aws_get_role(self):
    response_list []
    response = self.sts_client.get_caller_identity().get("Account")
    response_list.append(response)
    return response_list

  # Get Security Group specific based on alias
  def aws_sg_group(self, alias, aws_sg_list):
    response_list []
    try:
      for x in aws_sg_list:
        if re.search(alias, x["GroupName"], re.IGNORECASE):
          response_list.append(x)
    except TypeError:
      pass
    response_list.append(NO_ITEM)
    return response_list
