#!/usr/bin/python

''' Sets up the perfect development environment

Configures Vim and Bash just the way I like it. More functionality will be
added as I need it. Here are some of the features.

==============================================================================
                               Vim Features
==============================================================================
    * Zenburn colorscheme
    * Easier window switching with <C-[h,j,k,l]>
    * Disables arrow keys to enforce strong Vim-Fu
    * C-language syntax highlighting
    * Remap <Esc> key to `kj` to make exiting insert mode easier
    * Uses spaces instead of tabs for indentation

==============================================================================
                               Bash Features
==============================================================================
    * Color prompt with directory structure above current line so lone directory
      names don't crowd the input space
    * Different color prompt for root user 
    * Various custom aliases including a special keyword that reruns the previous
      command with sudo when you forget to.
'''
import argparse
import os
import pwd
import shutil

__author__ = "Noel Niles"
__email__ = "noelniles@gmail.com"

''' directory where this script lives '''
script_dir = os.getcwd()

home_dir = os.path.expanduser('~')

''' old vim and bash files '''
old_vim = os.path.join(home_dir, '.vimrc')
old_vim_plugins = os.path.join(home_dir, '.vim')
old_bash = os.path.join(home_dir, '.bashrc')

''' playing it safe '''
vim_backup = os.path.join(home_dir, 'bak.vimrc')
vim_plugin_backup = os.path.join(home_dir, 'bak.vim')
bash_backup = os.path.join(home_dir, 'bak.bashrc')

''' shiny new vim and bash configs with all the bells and whistles '''
new_vim = os.path.join(script_dir, 'vim/.vimrc')
new_vim_plugins = os.path.join(script_dir, 'vim/.vim')
new_bash = os.path.join(script_dir, 'bash/.bashrc')

''' rsync commands to update the configs '''
vim_cmd = 'rsync -hrzi %(new_vim)s %(old_vim)s && rsync -vrz %(new_vim_plugins)s %(old_vim_plugins)s' % locals()
bash_cmd = 'rsync -hrzi %(new_bash)s %(old_bash)s' % locals()

''' command line arguments '''
def parger():
    parg = argparse.ArgumentParser()
    parg.add_argument('-u', '--update', help='update the config files without backing up',
                      action="store_true")
    return parg.parse_args()

''' backs up the vim and bash config and plugin files '''
def backup_configs():
    try:
        shutil.copyfile(old_vim, vim_backup)
        shutil.copyfile(old_vim_plugins, vim_plugins_backup)
        shutil.copyfile(old_bash, bash_backup)
        print('config files backed up to:\n vimrc: %s\n vim plugins: %s\n'
              'bashrc: %s\n'%(vim_backup, vim_plugin_backup, bash_backup))
        return true
    except OSerror:
        print('There was an error copying %s to %s.\n' 
              % (OSerror.filename, OSerror.filename2))
        sys.exit('Config backup failed. Check your file permissions.\n')

''' runs the rsync commands '''
def update_configs():
    try:
        os.system(vim_cmd)
        print('vim updated\n')
        os.system(bash_cmd)
        print('bash updated\n')
    except Exception:
        print('There was a problem updating syncing the config files.\n')

def init():
    args = parger()

    if args.update:
        update_configs()
        print('Configs updated. Happy haxing!')
    else: 
        print ('This script will help set up Vim and Bash\n')
        print ('it will overwrite your current .vimrc and .bashrc\n')
        print ('the old files will be backed up in bak.vimrc and bak.bashrc\n')

        resp = input('Do you want to continue? [y,N]: ')
        if resp.lower() == 'y':
            backup_configs()
            update_configs()
        else:
            print('Quitting')

if __name__ == '__main__':
    init()

