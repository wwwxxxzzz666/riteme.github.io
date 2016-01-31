# navigater.py处理以下信息
# mathjax, favicon, strapdown, home

import os
import os.path

home_folder = os.path.abspath(".")
handle_map = {}

MATHJAX = """<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
      tex2jax: {inlineMath: [['$','$']]}
    });
    </script>
    <script type="text/javascript" async
      src="path-to-mathjax/MathJax.js?config=TeX-AMS_CHTML"></script>
    <script type="text/javascript" async
      src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
    </script>
    """


def handle(key, path):
    global handle_map
    assert isinstance(path, str), "Path must be a string!"

    handle_map[key] = path


def get_in(folder):
    global handle_map

    for key in handle_map.keys():
        handle_map[key] = os.path.join(handle_map[key], folder)


def go_up():
    global handle_map

    for key in handle_map.keys():
        handle_map[key] = os.path.basename(handle_map[key])


def get_path(key):
    global home_folder
    global handle_map

    return os.path.relpath(handle_map[key], start=home_folder)


def get_mathjax():
    return MATHJAX
