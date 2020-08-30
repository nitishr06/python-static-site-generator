import Path from pathlib
import os

class Site:

    def __init__(self,source,dest):
        self.source = source.Path()
        self.dest = dest.Path()

    def create_dir(self, path):
        directory = self.dest/relative_to(self.source)
        mkdir(directory,parents = True, exist_ok = True)

    def build():
        mkdir(self.dest,parents = True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.isdir():
                self.create_dir(path)