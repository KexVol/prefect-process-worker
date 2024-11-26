@echo off
REM 变量定义
set REPO_URL=https://github.com/KexVol/prefect-process-worker.git  REM 替换为你的远程仓库URL
set BRANCH=main  REM 替换为你的目标分支
set COMMIT_MESSAGE=更新代码  REM 提交信息

REM 初始化 Git 仓库（如果尚未初始化）
if not exist ".git" (
    git init
    git remote add origin %REPO_URL%
)

REM 添加所有更改到暂存区
git add .

REM 提交更改
git commit -m "%COMMIT_MESSAGE%"

REM 推送更改到远程仓库
git push -u origin %BRANCH%
