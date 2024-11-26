@echo off
set REPO_URL=https://github.com/KexVol/prefect-process-worker.git
set BRANCH=main
set COMMIT_MESSAGE=update code v2

REM Ini if not
if not exist ".git" (
    git init
    git remote add origin %REPO_URL%
)

REM added to temp
git add .

REM submit commit
git commit -m "%COMMIT_MESSAGE%"

REM push to
git push -u origin %BRANCH%
