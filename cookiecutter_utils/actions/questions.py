###########################################################################
"""

Questions - for the User Questions and Answers inputs

"""
###########################################################################

import inquirer
import re
import string
import random
from ..classes import AwsClient
from ..classes import RepoClient
from .utils import CookieCutterUtils
from ..constants.common_constants import *

class Questions:
  def __init__(self):
    pass

  def start_inquiring():
    # Get AWS Client
    aws_client - AwsClient()

    # Clone the Repo
    RepoClient.clone_repo()

    # Determine what set of questions to Ask based on Tag
    questions = [
      inquirer.List(
        "tag_name",
        message=TAG_MSG,
        choices=RepoClient.list_repo(),
        default=COOKIE_CUTTER_DEFAULT_TAG_VRSN,
      ),
    ]

    # Prompt Users for the Question
    answers = inquirer.prompt(
      questions, theme=inquirer.themes.load_theme_from_dict(COOKIE_CUTTER_THEME)
    )

    # Checkout the correct tag based on user selection
    RepoClient.checkout_repo_tag(answers["tag_name"])

    # Determine Account ID & VPC Infor set of questions to Ask based on Tag
    questions_1 = [
      inquirer.List(
        "aws_account_id",
        message=AWS_ACCOUNT_ID_MSG,
        choices=aws_client.aws_get_account_id(),
      ),
      inquirer.List(
        "vpd_id", message=VPC_ID_MSG, choices=aws_client.aws_describe_vpc()
      ),
    ]

    # Prompt Users for the Question
    answers.update(
      inquirer.prompt(
        questions_1,
        theme=inquirer.themes.load_theme_from_dict(COOKIE_CUTTER_THEME),
      )
    )

    # Gather the Security Groups
    answers["vpc_id"] = answers["vpc_id"]["VpcId"]
    aws_sg_list = aws_client.aws_describe_sg(answers["vpc_id"])

    # Get Question Set based on Tag
    cookie_cutter_dict = CookieCutterUtils.cookie_cutter_keys()

    question_2 = []

    for tag_key in cookie_cutter_dict.keys():
      if tag_key == "tenant_name":
        questions_2.append(
          inquirer.Text(
            "tenant_name",
            message=TENANT_MSG,
            validate=lambda _, x: len(x) > 0,
          )
        )
      elif tag_key == "account_level":
        questions_2.append(
          inquirer.List(
            "account_level":,
            message=ACCOUNT_LEVEL_MSG,
            choices=ACCOUNT_LEVEL_STATIC_LIST,
          )
        )
      elif tag_key == "enclave":
        questions_2.append(
          inquirer.List(
            "enclave", message=ENCLAVE_MSG, choices=ENCLAVE_STATIC_LIST
          )
        )
      elif tag_key == "network_level":
        questions_2.append(
          inquirer.List(
            "network_level",
            message=NETWORK_LEVEL_MSG,
            choices=NETWORK_LEVEL_STATIC_LIST,
          )
        )
      elif tag_key == "tenant_division_name":
        questions_2.append(
          inquirer.List(
            "tenant_division_name",
            message=TENANT_DIVISION_NAME_MSG,
            choices=TENANT_DIVISION_NAME_STATIC_LIST,
          )
        )
      elif tag_key == "aws_account_id":
        pass
      elif tag_key == "vpc_id":
        pass
      elif tag_key == "sg_default":
        questions_2.append(
          inquirer.List(
            "sg_default",
            message=SG_DEFAULT_MSG + answers["vpc_id"],
            choices=aws_client.get_sg_group(CONSTANT_DEFAULT, aws_sg_list),
          )
        )
      elif tag_key == "sg_dns":
        questions_2.append(
          inquirer.List(
            "sg_dns",
            message=SG_DNS_MSG + answers["vpc_id"],
            choices=aws_client.get_sg_group(CONSTANT_DNS, aws_sg_list),
          )
        )
      elif tag_key == "sg_ssh":
        questions_2.append(
          inquirer.List(
            "sg_ssh",
            message=SG_SSH_MSG + answers["vpc_id"],
            choices=aws_client.get_sg_group(CONSTANT_SSH, aws_sg_list),
          )
        )
      elif tag_key == "sg_web":
        questions_2.append(
          inquirer.List(
            "sg_web",
            message=SG_WEB_MSG + answers["vpc_id"],
            choices=aws_client.get_sg_group(CONSTANT_WEB, aws_sg_list),
          )
        )
      elif tag_key == "sg_ess":
        questions_2.append(
          inquirer.List(
            "sg_ess",
            message=SG_ESS_MSG + answers["vpc_id"],
            choices=aws_client.get_sg_group(CONSTANT_ESS, aws_sg_list),
          )
        )
      elif tag_key == "appdevel_role_id":
        questions_2.append(
          inquirer.List(
            "appdevel_role_id",
            message=APPDEVEL_ROLE_MSG,
            choices=aws_client.aws_get_role(CONSTANT_APP_ROLE),
          )
        )
      elif tag_key == "projowner_role_id":
        questions_2.append(
          inquirer.List(
            "projowner_role_id",
            message=PROJOWNER_ROLE_MSG,
            choices=aws_client.aws_get_role(CONSTANT_PROJ_ROLE),
          )
        )
      elif tag_key == "base_hardened_ami_id":
        questions_2.append(
          inquirer.List(
            "base_hardened_ami_id",
            message=AMI_MSG,
            choices=aws_client.aws_describe_ami(),
          )
        )
      elif tag_key == "kibana_alerting_email":
        questions_2.append(
          inquirer.Text(
            "kibana_alerting_email,
            message=KIBANA_ALERTING_EMAIL_MSG,
            validate=lambda _, x: len(x) > 0,
          )
        )
      elif tag_key == "jenkins_base_domain":
        questions_2.append(
          inquirer.Text(
            "jenkins_base_domain",
            message=JENKINS_BASE_DOMAIN_MSG,
            validate=lambda _, x: len(x) > 0,
          )
        )
      elif tag_key == "tfstate_backend_bucket_suffix":
        answers["tfstate_backend_bucket_suffix"] = "".join(
          random.SystemRandom().choice(string.ascii_lowercase)
          for _ in range (7)
        )
        elif tag_key == "__env_name":
          answers["__env_name"] = True
        elif tag_key == "__template_dir_name":
          answers["__template_dir_name"] = True
        else:
          questions_2.append(inquirer.Text(tag_key, message=COMMON_MSG + tag_key))

      # Prompt user for second set and update answer dict
      answers.update(
        inquirer.prompt(
          questions_2,
          theme=inquirer.themes.load_theme_from_dict(COOKIE_CUTTER_THEME),
        )
      )
      answers["confirm_provision"] = inquirer.confirm(CONFIRM_PROVISION, default=False)
      return answers
