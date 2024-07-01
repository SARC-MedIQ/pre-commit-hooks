from __future__ import annotations

import os.path
import subprocess

TESTING_DIR = os.path.abspath(os.path.dirname(__file__))


def git_commit(*args, **kwargs):
    cmd = ("git", "commit", "--no-gpg-sign", "--no-verify", "--no-edit", *args)
    subprocess.check_call(cmd, **kwargs)
