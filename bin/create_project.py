#!/usr/bin/env python

import os
import shutil
import pathlib

print("=== Creating Ansible Project ===")

print("# Project name: ")
project_name = input()

print("# Parent directory: ")
parent_dir_path = os.path.expanduser(input())

print("# Type of template: ")
template_type = input()

print("Creating the parent directory...")
print(parent_dir_path)
os.makedirs(parent_dir_path, exist_ok=True)

print("Copying template to the directory...")
root_path = pathlib.Path(__file__).parent.parent.resolve()
templates_dir_name = "templates"
templates_path = root_path.joinpath(root_path, templates_dir_name)
src_path = os.path.join(templates_path, template_type)
dest_path = pathlib.Path(os.path.join(parent_dir_path, project_name)).resolve()
print("Copy from {} to {}".format(src_path, dest_path))
shutil.copytree(src_path, dest_path)