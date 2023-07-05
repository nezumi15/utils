###############################################################################
"""

Cookie Cutter BitBucket Client for the util

"""
###############################################################################

import os
import git
import shutil

from ..constants.common_constants import (
  COOKIE_CUTTER_GIT,
  COOKIE_CUTTER_REPLAY_FILE_PATH,
  COOKIE_CUTTER_LOC,
  GIT_BRANCH,
  COOKIE_CUTTER_REPLAY,
)

class RepoClient:
  def __init__(self):
    pass

  # Clone cookiecutter repo
  def clone_repo():
    git.Repo.clone_from(
      COOKIE_CUTTER_GIT,
      COOKIE_CUTTER_REPLAY_FILE_PATH + "/" + COOKIE_CUTTER_LOC,
      branch=GIT_BRANCH,
    )

  # List Tags for the cookiecutter repo
  def list_repo():
    tag_list = sorted(
      git.Repo(COOKIE_CUTTER_REPLAY_FILE_PATH + "/" + COOKIE_CUTTER_LOC.tags,
      key=lambda t: t.commit.committed_datetime,
      reverse=True,
    )
    return tag_list

    def checkout_repo_tag(tag_name):
      cookie_cutter_repo = git.Repo(
        COOKIE_CUTTER_REPLAY_FILE_PATH + "/" + COOKIE_CUTTER_LOC
      )
      cookie_cutter_repo.init()
      cookie_cutter_repo.git.checkout(tag_name)

  # Provision cookiecutter IRLCC
  def start_provisioning(replay_answers):
    os.system(
      "cookiecutter "
      + COOKIE_CUTTER_LOC
      + " --replayfile "
      + COOKIE_CUTTER_REPLAY
    )

  Cleanup the cookiecutter cloned repo
  def clean_cookiecutter():
    shutil.remtree(
      COOKIE_CUTTER_REPLAY_FILE_PATH + "/" + COOKIE_CUTTER_LOC, ignore_errors=True
    )
      
