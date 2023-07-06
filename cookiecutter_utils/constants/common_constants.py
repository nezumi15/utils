#########################################################################
"""

Cookie Cutter Common Constants values for the util

"""
########################################################################

import os

# No Item Found
NO_ITEM = "NONE"
AWS_ERR_MSG = "Please Update Access Portal Credentials"

# Custom Theme for the cookie cutter
COOKIE_CUTTER_THEME = {
  "Question": {
    "mark_color": "yellow",
    "bracket_color": "normal",
    "default_color": "white",
  },
  "List": {
    "selection_color": "bold_red",
    "selection_cursor": "=>",
    "unselected_color": "bold_blue",
  },
}

# Cookie Cutter Git
COOKIE_CUTTER_GIT = "ssh://git@bitbucket.example.proj.com:7999/cookie-cutter-tenant-infrastructure-live-template.git"
GIT_BRANCH = "master"
COOKIE_CUTTER_DEFAULT_TAG_VRSN = "v2.0"

# Cookie Cutter Replay File Name
COOKIE_CUTTER_REPLAY = "cookie-cutter-tenant-infrastructure-live-template/"

# Cookie Cutter Location
COOKIE_CUTTER_LOC = "cookie-cutter-tenant-infrastructure-live-template/"
COOKIE_CUTTER_JSON_FILE = "cookiecutter.json"

# Static Lists
ACCOUNT_LEVEL_STATIC_LIST = ["TEST", "PROD"]
ENCLAVE_STATIC_LIST = ["test", "ops", "dev"]
NETWORK_LEVEL_STATIC_LIST = ["unclass", "class"]
TENANT_DIVISION_NAME_STATIC_LIST = ["EX1", "EX2"]

# AWS BOTO3 Constants
CONST_EC2 = "ec2"
CONST_IAM = "iam"
CONST_STS = "sts"

# Questions for the Cookie Cutter
CONSTANT_DEFAULT = "default"
CONSTANT_DNS = "DNS"
CONSTANT_SSH = "SSH"
CONSTANT_WEB = "WEB"
CONSTANT_ESS = "ESS"
CONSTANT_APP_ROLE = "APPDEVEL"
CONSTANT_PROJ_ROLE = "PROJOWNER"

# AMI Images
PIAB_IMAGES = "*Image*Hardened*"

# Questions Constants
CONFIRM_PROVISION = "Would you like to start provisioning the project with cookie cutter in current directory?"

TAG_MSG = "Please select cookie-cutter-tenant-infrastructure-live-template Tag version"
TENANT_MSG = "Please Enter Tenant Name"
ACCOUNT_LEVEL_MSG = "Select Account Level "
ENCLAVE_MSG = "Select Enclave "
NETWORK_LEVEL_MSG = "Select Network Level "
TENANT_DIVISION_NAME_MSG = "Select Division Name"
AWS_ACCOUNT_ID_MSG = "Please Enter Tenant AWS Account Number "
VPC_ID_MSG = "Select VPC for the AWS account "
KIBANA_ALERTING_EMAIL_MSG = "Please enter Kibana Alerting Email [example.yahoo.com]"
JENKINS_BASE_DOMAIN_MSG = (
  "Please enter Base Jenkins Domain [https://jenkins.project.com]"
)
COMMON_MSG = "Please Enter Value for "

SG_DEFAULT_MSG = "Select Default SG for the "
SG_DNS_MSG = "Select DNS SG for the "
SG_SSH_MSG = "Select SSH SG for the "
SG_WEB_MSG = "Select WEB SG for the "
SG_ESS_MSG = "Select ESS SG for the "
APPDEVEL_ROLE_MSG = "Please Select APPDEVEL Role id "
PROJOWNER_ROLE_ID = "Please Select PROJOWNER Role id "
AMI_MSG = "Please Select Base hardened AMI ID "
