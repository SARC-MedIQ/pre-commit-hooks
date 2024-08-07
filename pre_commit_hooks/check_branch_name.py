from __future__ import annotations

import argparse
import os
import re
from typing import AbstractSet, Sequence

from pre_commit_hooks.util import CalledProcessError, cmd_output

DEFAULT_PATTERN = r"[a-z]{2,5}-\d+-[a-z0-9-]+"


def branch_matches(patterns: AbstractSet[str] | None = None) -> bool:
    if not patterns:
        patterns = frozenset((DEFAULT_PATTERN,))
    # check if it's GHA
    github_ref = os.getenv("GITHUB_REF")
    if github_ref:
        branch_name = github_ref.replace("refs/heads/", "")
    else:
        try:
            ref_name = cmd_output("git", "symbolic-ref", "HEAD")
        except CalledProcessError:
            return True
        chunks = ref_name.strip().split("/")
        branch_name = "/".join(chunks[2:])
    result = any(re.match(p, branch_name) for p in patterns)
    if not result:
        print(
            f"Branch {branch_name} does not match "
            f'the allowed patterns: {" | ".join(patterns)}',
        )
    return result


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--pattern",
        action="append",
        help=(
            "regex pattern for branch name to match, " "may be specified multiple times"
        ),
    )
    args, _ = parser.parse_known_args(argv)
    patterns = frozenset(args.pattern or ())

    return int(not branch_matches(patterns))


if __name__ == "__main__":
    raise SystemExit(main())
