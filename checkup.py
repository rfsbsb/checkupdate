#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author Rafael Ferreira Silva - http://rafaelsilva.net
# See LICENSE.txt for details.
import os, fnmatch

class Updater:

  def __init__(self, path = "./"):
    self.path = path
    self.paths = []
    if (os.path.exists(path)):
      for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, 'settings.php'):
          droot, fname = os.path.split(os.path.split(root)[0])
          self.paths.append(os.path.join(droot))

  def check(self):
    for path in self.paths:
      print "\033[1;33mDrupal site: "+ path+"\033[0m"
      os.system("drush up -y -r "+path)
      os.system("sleep 5")
      os.system("clear")


#main
if __name__ == "__main__":
  #change this path to the one your sites live
  up = Updater('/var/www')
  up.check()
