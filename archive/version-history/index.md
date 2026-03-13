# Version History Archive

## Purpose

This directory maintains a changelog and version history for the Deep Research
Squad's tools, configurations, and processes. Each entry documents what changed
between versions, providing a clear record for auditing, debugging, and
onboarding.

## Directory Structure

```
version-history/
  index.md                    # This file
  vN.N.N.md                   # One file per version release
  CHANGELOG.md                # Consolidated changelog (optional)
```

## File Naming Convention

Use semantic versioning in the format `vN.N.N.md` (e.g., `v1.2.0.md`). Each
file should cover a single release or version bump. For non-release milestones,
use `YYYY-MM-DD-milestone-slug.md` instead.

Each file should include: version number, release date, summary of changes,
breaking changes (if any), and migration steps.

## Example Entries

```
# (No versions recorded yet)
#
# Future entries will appear as:
#   v1.0.0.md
#   v1.1.0.md
#   v2.0.0.md
```
