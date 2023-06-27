########################################################################
"""

Cookie Cutter Utils - Dynamically provisions information for the Template

"""
########################################################################


import os
import json
from .actions import Questions
from .actions import CookieCutterUtils
from .classes import RepoClient

from .constants.common_constants import COOKIE_CUTTER_REPLAY

# Change to current Working Dir
os.chdir(os.getcwd())


def main():
  # Start with Questions, prompts users for questions and records answers
  answers = Questions.start_inquiring()
  is_provision_confirmed = answers["confirm_provision"]

  # Format the dict, remove extra elements
  replay_answers = CookieCutterUtils.replay_dict(answers)

  # Write Json File
  with open(COOKIE_CUTTER_REPLAY, "w") as f:
    json.dump(replay_answers, f)

  # If User likes to provision the Project
  if is_provision_confirmed:
    # Start Provisioning
    RepoClient.start_provisioning(replay_answers)
    RepoClient.clean_cookiecutter()

if __main__ == "__main__":
  main()
