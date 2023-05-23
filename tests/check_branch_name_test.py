from __future__ import annotations

from pre_commit_hooks.check_branch_name import branch_matches
from pre_commit_hooks.check_branch_name import main
from pre_commit_hooks.util import cmd_output
from testing.util import git_commit


def test_valid_default_branch(temp_git_dir):
    with temp_git_dir.as_cwd():
        cmd_output('git', 'checkout', '-b', 'aaa-101-test-branch')
        assert branch_matches() is True


def test_invalid_default_branch(temp_git_dir):
    with temp_git_dir.as_cwd():
        cmd_output('git', 'checkout', '-b', 'test-branch')
        assert branch_matches({r'^good-.*$'}) is False


def test_multi_pattern_pass(temp_git_dir):
    with temp_git_dir.as_cwd():
        cmd_output('git', 'checkout', '-b', 'test-branch')
        assert branch_matches({r'^good-.*$', '^test-.*$'}) is True


def test_multi_pattern_fail(temp_git_dir):
    with temp_git_dir.as_cwd():
        cmd_output('git', 'checkout', '-b', 'another-branch')
        assert branch_matches({r'^good-.*$', '^test-.*"'}) is False


def test_not_on_a_branch(temp_git_dir):
    with temp_git_dir.as_cwd():
        git_commit('--allow-empty', '-m1')
        head = cmd_output('git', 'rev-parse', 'HEAD').strip()
        cmd_output('git', 'checkout', head)
        # we're not on a branch!
        assert main() == 0
