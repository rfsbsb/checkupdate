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
          droot, fname = os.path.split(root)
          # checking if it's a default or a multisite
          if fname == "default":
            droot, fname = os.path.split(droot)
            self.paths.append([droot, None])
          else:
            droot, fname = os.path.split(droot)
            self.paths.append([droot, fname])

  def check(self):
    for path in self.paths:
      print "\033[1;33mDrupal site: "+ path[0]+"\033[0m"
      # multisite update
      if path[1]:
        os.system("drush up -r "+path[0]+" -l "+path[1])
        print "drush up -r "+path[0]+" -l "+path[1]
      # normal update
      else:
        os.system("drush up -r "+path[0])
      os.system("sleep 5")
      os.system("clear")


#main
if __name__ == "__main__":
  #change this path to the one your sites live
  up = Updater('/var/www')
  up.check()
