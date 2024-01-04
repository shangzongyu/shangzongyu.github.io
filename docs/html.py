import os

HTML_DIR = "../blog-html"

print("generate public dir")
os.system("hugo")
print("generate public dir END")

print("Copy files to blog-html")
cp = "cp -r public/* ../blog-html"
os.system(cp)
print("Copy files to blog-html END")

os.system("rm -fr public")
