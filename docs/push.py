import os


if __name__ == "__main__":
    os.system("git add -A")
    os.system("git commit")
    os.system("git fetch origin")
    os.system("git rebase origin/main")
    os.system("git push origin main")
