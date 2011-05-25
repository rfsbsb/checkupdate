#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author Rafael Ferreira Silva - http://rafaelsilva.net
# See LICENSE.txt for details.

import os

class Updater:

  def __init__(self, path = "./"):
    self.path = path
    self.paths = []
    if (os.path.exists(path)):
      for file_dir in os.listdir(path):
        full_path =  path + "/" + file_dir
        if os.path.isdir(full_path) and file_dir[0] != ".":
          self.paths.append(full_path)

  def check(self):
    for path in self.paths:
      if os.path.isfile(path + "/cron.php"):
        print "\033[1;33mDrupal site: "+ path+"\033[0m"
        os.system("drush up -r "+path)
        os.system("sleep 5")
        os.system("clear")
    

#main
if __name__ == "__main__":
  #change this path to the one your sites live
  up = Updater('/var/www')
  up.check()

