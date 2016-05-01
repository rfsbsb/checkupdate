#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author Rafael Ferreira Silva - http://rafaelsilva.net
# See LICENSE.txt for details.
import os, fnmatch, subprocess

class Updater:

  def __init__(self, path = "./"):
    self.path = path
    self.paths = []
    if (os.path.exists(path)):
      for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, 'settings.php'):
          droot, fname = os.path.split(root)
          if fname == "default":
            droot, fname = os.path.split(droot)
            self.paths.append([droot, None])
          else:
            droot, fname = os.path.split(droot)
            self.paths.append([droot, fname])

  def check(self):
    for path in self.paths:
      #if Drupal 8, use drush cache-rebuild instead of cache clear
      version = subprocess.Popen("drush -r "+path[0]+" php-eval 'echo VERSION'", shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[0]
      if (version == "VERSION")
        cache_clear_command = "/root/tools/drush/drush cr"
      else
        cache_clear_command = "/root/tools/drush/drush cc all"
      print "\033[1;33mDrupal site: "+ path[0]+"\033[0m"
      if path[1]:
        subprocess.call(cache_clear_command+" -r "+path[0]+" -l "+path[1], shell=True)
        subprocess.call("/root/tools/drush/drush vset update_last_check 0 -r "+path[0]+" -l "+path[1], shell=True)
        subprocess.call("/root/tools/drush/drush cron -y -r "+path[0]+" -l "+path[1], shell=True)
        subprocess.call("/root/tools/drush/drush up -y -r "+path[0]+" -l "+path[1], shell=True)
      else:
        subprocess.call(cache_clear_command+" -r "+path[0], shell=True)
        subprocess.call("/root/tools/drush/drush vset update_last_check 0 -r "+path[0] , shell=True)
        subprocess.call("/root/tools/drush/drush cron -y -r "+path[0], shell=True)
        subprocess.call("/root/tools/drush/drush up -y -r "+path[0], shell=True)


#main
if __name__ == "__main__":
  #change this path to the one your sites live
  up = Updater('/home')
  up.check()
