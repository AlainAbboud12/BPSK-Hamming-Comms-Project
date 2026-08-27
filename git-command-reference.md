# Git Command Reference

## Setup (one-time per project)

```bash
git init
# Turns the current folder into a Git repo. Only run once, when starting fresh.

git clone <url>
# Downloads an existing repo (with full history) onto your machine.

git remote add origin <url>
# Connects your local repo to a GitHub repo. Only needed once per project.

git remote -v
# Shows which remote URL(s) your local repo is connected to. Useful for checking you're pointed at the right repo.

git remote set-url origin <url>
# Changes the remote URL if you connected to the wrong repo.

git config --global user.name "Your Name"
git config --global user.email "you@example.com"
# Tells Git who you are, so commits are attributed to you. Only needed once per machine.
```

## The everyday cycle

```bash
git status
# Shows what's changed, staged, or untracked. Your go-to "what's going on" command — run this often.

git add <file>
git add .
# Stages changes, marking them ready to be committed. "." stages everything changed.

git commit -m "message"
# Saves a local snapshot of your staged changes, with a description. This does NOT touch GitHub.

git push
# Uploads your local commits to GitHub. This is the only command that actually changes what's on GitHub.

git push -u origin main
# Same as above, but also tells Git "remember that local main should push to origin/main." Only needed on your very first push of a branch.

git pull
# Downloads and merges any new commits from GitHub into your local copy. Run this before starting new work, especially when collaborating.
```

## Branches (isolating work)

```bash
git branch
# Lists all branches, shows which one you're currently on.

git checkout -b branch-name
# Creates a new branch and switches to it immediately. Good for experimenting without touching main.

git checkout main
# Switches back to the main branch.

git branch -M main
# Renames the current branch to "main" (used once during initial setup).
```

## Inspecting / undoing

```bash
git log
# Shows commit history — who committed what, and when.

git diff
# Shows exact line-by-line changes that aren't staged yet.

git checkout -- <file>
# Discards uncommitted changes to a file, reverting it to the last commit.

git reset --soft HEAD~1
# Undoes the last commit but keeps the changes staged (so you can re-commit differently).
```

## File operations

```bash
git mv old-name new-name
# Renames a file and stages the rename in one step (better than renaming manually then git add-ing separately).

git rm <file>
# Removes a file from both your folder and Git tracking.
```

## Quick reference: what you'll actually type 95% of the time

```bash
git pull
git add .
git commit -m "..."
git push
```

Everything else above is situational — good to know exists, but this four-line loop is the daily driver.
