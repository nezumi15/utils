###############################################################################
"""

Utils - for the helper functions

"""
###############################################################################

import os
import json
import re

from ..constants.common_constants import (
  NO_ITEM,
  COOKIE_CUTTER_LOC,
  COOKIE_CUTTER_REPLAY_FILE_PATH,
  COOKIE_CUTTER_GIT,
  COOKIE_CUTTER_REPLAY,
  COOKIE_CUTTER_JSON_FILE,
)

class CookieCutterUtils:
  def __init__(self):
    pass

  def cookie_cutter_keys():
    with open(
      COOKIE_CUTTER_REPLAY_FILE_PATH
      + "/"
      + COOKIE_CUTTER_LOC
      + COOKIE_CUTTER_JSON_FILE
    ) as json_file:
      cookie_cutter_json = json_file.read()
    return json.loads(cookie_cutter_json)

  # Format the dictionary for the replay json
  def replay_dict(answers):
    replay_answers = {}
    if answers.get("sg_default") and answers.get("sg_default") != NO_ITEM:
      answers["sg_default"] = answers["sg_default"]["GroupId"]
    if answers.get("sg_dns") and answers.get("sg_dns") != NO_ITEM:
      answers["sg_dns"] = answers["sg_dns"]["GroupId"]
    if answers.get("sg_ssh") and answers.get("sg_ssh") != NO_ITEM:
      answers["sg_ssh"] = answers["sg_ssh"]["GroupId"]
    if answers.get("sg_web") and answers.get("sg_web") != NO_ITEM:
      answers["sg_web"] = answers["sg_web"]["GroupId"]
    if answers.get("sg_ess") and answers.get("sg_ess") != NO_ITEM:
      answers["sg_ess"] = answers["sg_ess"]["GroupId"]
    if answers.get("base_hardened_ami_id"):
      answers["base_hardened_ami_id"] = answers["base_hardened_ami_id"]["ImageId"]
    if answers.get("__env_name"):
      answers["__env_name"] = (
        answers['tenant_name']
        + "-"
        + answers['enclave']
        + "-"
        + answers['network_level']
      )
      if answers.get("__template_dir_name"):
        answers["__tempalte_dir_name"] = (
          answers['tenant_name']
          + "-"
          + answers['enclave']
          + "-"
          + answers['network_level']
        )    
      del answers["confirm_provision"]
      del answers["tag_name"]
      replay_answers["cookiecutter"] = answers
      return replay_answers
    
    
