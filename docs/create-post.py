__author__ = 'TomShine'

import os
import re
import subprocess
from datetime import datetime

# replace to vim or others if your like
# EDITOR = ['MarkdownPad2.exe']
EDITOR = ['emacsclient']

def default_content():
    return '''
#+HUGO_BASE_DIR: ~/blog
#+HUGO_SECTION: ./post
#+TITLE: {post_name}
#+DATE: {date_format}
#+options: author:nil
#+HUGO_AUTO_SET_LASTMOD: t
#+HUGO_TAGS:
#+HUGO_CATEGORIES:
#+HUGO_DRAFT: false

* Footnotes
* COMMENT Local Variables                          :ARCHIVE:
# Local Variables:
# org-hugo-auto-export-on-save: t
# End:
    '''.format(
        post_name=post_name,
        date_format=datetime.now().strftime('%Y-%m-%d'),
    )

if __name__ == '__main__':
    post_name = raw_input("Post'title: ")

    post_path = 'content-org/{post_name}.org'.format(post_name=post_name)
    subprocess.call(['touch', post_path])

    with open(post_path, 'w') as f:
        f.write(default_content())

    subprocess.Popen(EDITOR + [post_path])
