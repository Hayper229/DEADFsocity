#!/bin/python3
import requests
import os
import sys
from colorama import Fore, Style, Back
def option():
    print(''' Usage: ./DorkingScriptArg.py   URL 
Type targets protocols:  http://example.com/  or  https://example.com/ ''')
    
    


img_display=print(Fore.RED + '''
                                                                               mmmm      m
   mmmm                         "                   mmmm                  "    #" "#   mm#mm
   #   "m  mmm    m mm   mmm   mmm    m mm    mmmm  #"   "  mmm    m mm  mmm   #    #    #
   #    # #" "#   #"  " #"  "    #    #"  #  #" "#  "#mmm  #"  "   #"  "   #   ##m#"     #
   #    # #   #   #     #        #    #   #  #   #      "# #       #       #   #         "mm
   #mmm"  "#m#"   #     "#mm"  mm#mm  #   #  "#m"#  "mmm#" "#mm"   #     mm#mm "
                                              m  #                             

+===================================================================+
|           [Developer: https://github.com/Hayper229]               |
+-------------------------------------------------------------------+
|                                                                   |                              
|                        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                   | 
|                        ⣿⣿⣿⣿⣿⣿⣿⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⣿⣿⣿⣿⣿⣿⣿                   | 
|                        ⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿                   | 
|                        ⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿                   | 
|                        ⣿⣿⡿⠛⠉⣁⣀⣠⣴⣿⣿⣿⣿⣿⣿⣦⣄⣀⣈⡉⠙⠻⣿⣿                   | 
|                        ⣿⠏⢠⣾⣿⣿⣿⣿⣿⠟⠋⠉⠉⠉⠛⢿⣿⣿⣿⣿⣷⣆⠘⣿                   | 
|                        ⣿⠄⢸⣿⣿⣿⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⣿⣿⣿⠄⣿                   | 
|                        ⣿⠄⢸⣿⣿⣿⣿⠁⠄⠄⡀⠄⠄⢀⡀⠄⠄⢹⣿⣿⣿⣿⠄⣿                   | 
|                        ⣿⠄⢸⣿⣿⣿⣿⡀⠄⢾⣿⠆⠄⣿⡿⠄⠄⣸⣿⣿⣿⣿⠄⣿                   | 
|                        ⣿⠄⢸⣿⣿⣿⣿⣿⣦⡀⠄⢠⡆⠄⠄⣠⣾⣿⣿⣿⣿⣿⠄⣿                   | 
|                        ⣿⠄⢸⣿⣿⣿⣿⣿⣿⣷⣀⣚⣛⣀⣰⣿⣿⣿⣿⣿⣿⣿⠄⣿                   |
|                        ⣿⠄⢸⣿⣿⣿⣿⣿⣿⠏⠛⠛⠛⠛⠛⢿⣿⣿⣿⣿⣿⣿⠄⣿                   |
|                        ⣿⠄⢸⣿⡇⠄⠉⠛⠿⢿⣶⣶⣶⣶⣾⠿⠛⠋⠁⠈⣿⣿⠄⣿                   |
|                        ⣿⠄⢸⣿⣷⣶⣶⣶⣤⣤⣀⡈⠉⠛⠛⠿⠿⢷⣶⣶⣿⣿⠄⣿                   |
|                        ⣿⠄⢸⣿⡇⠄⠄⣠⣭⣿⣿⣿⣿⣷⣶⣤⣄⡀⠄⢀⣿⣿⠄⣿                   |
|                        ⣿⡄⠸⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⡟⢀⣿                   |
|                        ⣿⣿⣄⡈⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⢉⣠⣾⣿                   |
|                        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                   |
+-------------------------------------------------------------------+
|===================================================================|
|                 DorkingScript-Version > FullConsole               |
+-------------------------------------------------------------------+


''')







print(img_display)
print('please enter url | URL examples <http://example.com/ | https://example.com/')
url=input('@DSARG >  ') 
if url=='show options':
   print(option())
   exit
#
#n = input("Введите целое число: ")
#try:
#    n = int(n)
#    print("Удачно")
#except:
#    print("Что-то пошло не так")
#
print('[![Search for directories and files]!]')
a=url+'admin '
print('[+]',a)
rem=requests.get(url, 'admin ')
print(rem)

a=url+'accessibility  '
print('[+]',a)
rem=requests.get(url, 'accessibility ')
print(rem)


a=url+'accounts   '
print('[+]',a)
rem=requests.get(url, 'accounts  ')
print(rem)



a=url+'action   '
print('[+]',a)
rem=requests.get(url, 'action  ')
print(rem)

a=url+'ads  '
print('[+]',a)
rem=requests.get(url, 'ads ')
print(rem)

a=url+'favicon.ico  '
print('[+]',a)
rem=requests.get(url, 'favicon.ico ')
print(rem)

a=url+'friends  '
print('[+]',a)
rem=requests.get(url, 'friends ')
print(rem)

a=url+'home   '
print('[+]',a)
rem=requests.get(url, 'home ')
print(rem)

a=url+'home   '
print('[+]',a)
rem=requests.get(url, 'home  ')
print(rem)

a=url+'homepage  '
print('[+]',a)
rem=requests.get(url, 'homepage ')
print(rem)

a=url+'hosted  '
print('[+]',a)
rem=requests.get(url, 'hosted ')
print(rem)

a=url+'log  '
print('[+]',a)
rem=requests.get(url, 'log ')
print(rem)

a=url+'local  '
print('[+]',a)
rem=requests.get(url, 'local ')
print(rem)

a=url+'logos  '
print('[+]',a)
rem=requests.get(url, 'logos ')
print(rem)

a=url+'mail  '
print('[+]',a)
rem=requests.get(url, 'mail ')
print(rem)

a=url+'manifest  '
print('[+]',a)
rem=requests.get(url, 'manifest ')
print(rem)

a=url+'phone   '
print('[+]',a)
rem=requests.get(url, 'phone  ')
print(rem)

a=url+'ping  '
print('[+]',a)
rem=requests.get(url, 'ping ')
print(rem)

a=url+'pixel  '
print('[+]',a)
rem=requests.get(url, 'pixel ')
print(rem)

a=url+'passwords   '
print('[+]',a)
rem=requests.get(url, 'passwords  ')
print(rem)

a=url+'partners  '
print('[+]',a)
rem=requests.get(url, 'partners ')
print(rem)

a=url+'print*  '
print('[+]',a)
rem=requests.get(url, 'print* ')
print(rem)

a=url+'cgi-bin  '
print('[+]',a)
rem=requests.get(url, 'cgi-bin ')
print(rem)

a=url+'super_admin  '
print('[+]',a)
rem=requests.get(url, 'super_admin ')
print(rem)

a=url+'CHANGELOG.txt'
print('[+]',a)
rem=requests.get(url, 'CHANGELOG.txt')
print(rem)

a=url+' cron.php  '
print('[+]',a)
rem=requests.get(url, ' cron.php ')
print(rem)

a=url+'INSTALL.mysql.txt  '
print('[+]',a)
rem=requests.get(url, 'INSTALL.mysql.txt ')
print(rem)

a=url+'INSTALL.pgsql.txt  '
print('[+]',a)
rem=requests.get(url, 'INSTALL.pgsql.txt ')
print(rem)

a=url+'INSTALL.sqlite.txt  '
print('[+]',a)
rem=requests.get(url, 'INSTALL.sqlite.txt ')
print(rem)

a=url+'INSTALL.txt  '
print('[+]',a)
rem=requests.get(url, 'INSTALL.txt ')
print(rem)

a=url+'LICENSE.txt  '
print('[+]',a)
rem=requests.get(url, 'LICENSE.txt ')
print(rem)

a=url+'MAINTAINERS.txt  '
print('[+]',a)
rem=requests.get(url, 'MAINTAINERS.txt ')
print(rem)


a=url+'update.php  '
print('[+]',a)
rem=requests.get(url, 'update.php ')
print(rem)

a=url+'UPGRADE.txt  '
print('[+]',a)
rem=requests.get(url, 'UPGRADE.txt ')
print(rem)

a=url+'includes  '
print('[+]',a)
rem=requests.get(url, 'includes ')
print(rem)






#
##

a=url+'misc  '
print('[+]',a)
rem=requests.get(url, 'misc ')
print(rem)

a=url+'modules  '
print('[+]',a)
rem=requests.get(url, 'modules ')
print(rem)

a=url+'profiles  '
print('[+]',a)
rem=requests.get(url, 'profiles ')
print(rem)

a=url+'scripts  '
print('[+]',a)
rem=requests.get(url, 'scripts ')
print(rem)

a=url+'themes  '
print('[+]',a)
rem=requests.get(url, 'themes ')
print(rem)

a=url+'xmlrpc.php '
print('[+]',a)
rem=requests.get(url, 'xmlrpc.php ')
print(rem)

a=url+'comment/reply '
print('[+]',a)
rem=requests.get(url, 'comment/reply ')
print(rem)







a=url+'filter/tips '
print('[+]',a)
rem=requests.get(url, 'filter/tips  ')
print(rem)

a=url+'node/add  '
print('[+]',a)
rem=requests.get(url, 'node/add ')
print(rem)

a=url+'?q=admin  '
print('[+]',a)
rem=requests.get(url, '?q=admin ')
print(rem)

a=url+'?q=filter/tips  '
print('[+]',a)
rem=requests.get(url, '?q=filter/tips ')
print(rem)



a=url+'?q=comment/reply  '
print('[+]',a)
rem=requests.get(url, '?q=comment/reply ')
print(rem)

a=url+'?q=node/add  '
print('[+]',a)
rem=requests.get(url, '?q=node/add ')
print(rem)

a=url+'user/password  '
print('[+]',a)
rem=requests.get(url, 'user/password ')
print(rem)

a=url+'misc/*.css?  '
print('[+]',a)
rem=requests.get(url, 'misc/*.css? ')
print(rem)

a=url+'misc/*.js$  '
print('[+]',a)
rem=requests.get(url, 'misc/*.js$ ')
print(rem)

a=url+'misc/*.gif  '
print('[+]',a)
rem=requests.get(url, 'misc/*.gif ')
print(rem)

a=url+'misc/*.jpg  '
print('[+]',a)
rem=requests.get(url, 'misc/*.jpg ')
print(rem)

a=url+'misc/*.jpeg  '
print('[+]',a)
rem=requests.get(url, 'misc/*.jpeg ')
print(rem)

a=url+'misc/*.png  '
print('[+]',a)
rem=requests.get(url, 'misc/*.png ')
print(rem)

a=url+'misc/*.css$  '
print('[+]',a)
rem=requests.get(url, 'misc/*.css$  ')
print(rem)

a=url+'dotfiles/file  '
print('[+]',a)
rem=requests.get(url, 'dotfiles/file ')
print(rem)

a=url+'dotfiles/commit  '
print('[+]',a)
rem=requests.get(url, 'dotfiles/commit ')
print(rem)

a=url+'wa/file  '
print('[+]',a)
rem=requests.get(url, 'wa/file ')
print(rem)

a=url+'wa/commit  '
print('[+]',a)
rem=requests.get(url, 'wa/commit ')
print(rem)

a=url+'stream-tty/file  '
print('[+]',a)
rem=requests.get(url, 'stream-tty/file ')
print(rem)

a=url+'stream-tty/commit  '
print('[+]',a)
rem=requests.get(url, 'stream-tty/commit ')
print(rem)

a=url+'null  '
print('[+]',a)
rem=requests.get(url, 'null ')
print(rem)

a=url+'offers  '
print('[+]',a)
rem=requests.get(url, 'offers ')
print(rem)

a=url+'partners  '
print('[+]',a)
rem=requests.get(url, 'partners ')
print(rem)

a=url+'passwords   '
print('[+]',a)
rem=requests.get(url, 'passwords  ')
print(rem)

a=url+'patents  '
print('[+]',a)
rem=requests.get(url, 'patents ')
print(rem)

a=url+'preferences  '
print('[+]',a)
rem=requests.get(url, 'preferences ')
print(rem)

a=url+'press  '
print('[+]',a)
rem=requests.get(url, 'press ')
print(rem)

a=url+'products  '
print('[+]',a)
rem=requests.get(url, 'products  ')
print(rem)

a=url+'publications  '
print('[+]',a)
rem=requests.get(url, 'publications ')
print(rem)

a=url+'publisher  '
print('[+]',a)
rem=requests.get(url, 'publisher ')
print(rem)

a=url+'related     '
print('[+]',a)
rem=requests.get(url, 'related    ')
print(rem)

a=url+'research  '
print('[+]',a)
rem=requests.get(url, 'research ')
print(rem)

a=url+'index.html  '
print('[+]',a)
rem=requests.get(url, 'index.html ')
print(rem)

a=url+'ads/print   '
print('[+]',a)
rem=requests.get(url, 'ads/print ')
print(rem)

a=url+'ads/global  '
print('[+]',a)
rem=requests.get(url, 'ads/global ')
print(rem)

a=url+'ads/preferences   '
print('[+]',a)
rem=requests.get(url, 'ads/preferences ( ')
print(rem)

a=url+'ads/sitemap.xml   '
print('[+]',a)
rem=requests.get(url, 'ads/sitemap.xml ')
print(rem)

a=url+'ADMIN  '
print('[+]',a)
rem=requests.get(url, 'ADMIN ')
print(rem)

a=url+'Admin  '
print('[+]',a)
rem=requests.get(url, 'Admin ')
print(rem)

a=url+'Administration  '
print('[+]',a)
rem=requests.get(url, 'Administration ')
print(rem)

a=url+'administration  '
print('[+]',a)
rem=requests.get(url, 'administration ')
print(rem)

a=url+'ushell/shells/abap  '
print('[+]',a)
rem=requests.get(url, 'ushell/shells/abap ')
print(rem)

a=url+'coders.php  '
print('[+]',a)
rem=requests.get(url, 'coders.php ')
print(rem)

a=url+'arra.php  '
print('[+]',a)
rem=requests.get(url, 'arra.php ')
print(rem)

a=url+'ara.php  '
print('[+]',a)
rem=requests.get(url, 'ara.php ')
print(rem)

a=url+'wp.php  '
print('[+]',a)
rem=requests.get(url, 'wp.php ')
print(rem)

a=url+'admin.php  '
print('[+]',a)
rem=requests.get(url, 'admin.php ')
print(rem)

a=url+'Admin.php  '
print('[+]',a)
rem=requests.get(url, 'Admin.php ')
print(rem)

a=url+'ADMIN.php  '
print('[+]',a)
rem=requests.get(url, 'ADMIN.php ')
print(rem)

a=url+'ShellBackDoor.php  '
print('[+]',a)
rem=requests.get(url, 'ShellBackDoor.php ')
print(rem)

a=url+'ShellBackdoor.php  '
print('[+]',a)
rem=requests.get(url, 'ShellBackdoor.php ')
print(rem)

a=url+'lost.php  '
print('[+]',a)
rem=requests.get(url, 'lost.php ')
print(rem)

a=url+'losting.php  '
print('[+]',a)
rem=requests.get(url, 'losting.php ')
print(rem)

a=url+'Sh3llBackd00r.php  '
print('[+]',a)
rem=requests.get(url, 'Sh3llBackd00r.php ')
print(rem)

a=url+'kntl.php  '
print('[+]',a)
rem=requests.get(url, 'kntl.php ')
print(rem)

a=url+'ok.php  '
print('[+]',a)
rem=requests.get(url, 'ok.php ')
print(rem)

a=url+'0.php  '
print('[+]',a)
rem=requests.get(url, '0.php ')
print(rem)

a=url+'1.php  '
print('[+]',a)
rem=requests.get(url, '1.php ')
print(rem)

a=url+'2.php  '
print('[+]',a)
rem=requests.get(url, '2.php ')
print(rem)

a=url+'3.php  '
print('[+]',a)
rem=requests.get(url, '3.php ')
print(rem)

a=url+'4.php  '
print('[+]',a)
rem=requests.get(url, '4.php ')
print(rem)

a=url+'5.php  '
print('[+]',a)
rem=requests.get(url, '5.php ')
print(rem)

a=url+'6.php  '
print('[+]',a)
rem=requests.get(url, '6.php ')
print(rem)

a=url+'7.php  '
print('[+]',a)
rem=requests.get(url, '7.php ')
print(rem)

a=url+'8.php  '
print('[+]',a)
rem=requests.get(url, '8.php ')
print(rem)

a=url+'9.php  '
print('[+]',a)
rem=requests.get(url, '9.php ')
print(rem)

a=url+'10.php  '
print('[+]',a)
rem=requests.get(url, '10.php ')
print(rem)

a=url+'minishell.php  '
print('[+]',a)
rem=requests.get(url, 'minishell.php ')
print(rem)

a=url+'backdoor.php  '
print('[+]',a)
rem=requests.get(url, 'backdoor.php ')
print(rem)

a=url+'b4ckd00r.php  '
print('[+]',a)
rem=requests.get(url, 'b4ckd00r.php ')
print(rem)

a=url+'b4ckd0or.php  '
print('[+]',a)
rem=requests.get(url, 'b4ckd0or.php ')
print(rem)

a=url+'b4ckdo0r.php  '
print('[+]',a)
rem=requests.get(url, 'b4ckdo0r.php ')
print(rem)

a=url+'00.php  '
print('[+]',a)
rem=requests.get(url, '00.php ')
print(rem)

a=url+'herp.php  '
print('[+]',a)
rem=requests.get(url, 'herp.php ')
print(rem)

a=url+'sh3ll.php  '
print('[+]',a)
rem=requests.get(url, 'sh3ll.php ')
print(rem)

a=url+'shelling.php  '
print('[+]',a)
rem=requests.get(url, 'shelling.php ')
print(rem)

a=url+'sh33ll.php  '
print('[+]',a)
rem=requests.get(url, 'sh33ll.php ')
print(rem)

a=url+'sh3lll.php  '
print('[+]',a)
rem=requests.get(url, 'sh3lll.php ')
print(rem)

a=url+'sh331l.php  '
print('[+]',a)
rem=requests.get(url, 'sh331l.php ')
print(rem)

a=url+'sh33l1.php  '
print('[+]',a)
rem=requests.get(url, 'sh33l1.php ')
print(rem)

a=url+'upload/TnX.php  '
print('[+]',a)
rem=requests.get(url, 'upload/TnX.php ')
print(rem)

a=url+'upload/shell.php  '
print('[+]',a)
rem=requests.get(url, 'upload/shell.php ')
print(rem)

a=url+'upload/Shell.php  '
print('[+]',a)
rem=requests.get(url, 'upload/Shell.php ')
print(rem)

a=url+'upload/she1l.php  '
print('[+]',a)
rem=requests.get(url, 'upload/she1l.php ')
print(rem)

a=url+'G.php  '
print('[+]',a)
rem=requests.get(url, 'G.php ')
print(rem)

a=url+'wso.php  '
print('[+]',a)
rem=requests.get(url, 'wso.php ')
print(rem)

a=url+'lux.php  '
print('[+]',a)
rem=requests.get(url, 'lux.php ')
print(rem)

a=url+'mego.php  '
print('[+]',a)
rem=requests.get(url, 'mego.php ')
print(rem)

a=url+'raw.php  '
print('[+]',a)
rem=requests.get(url, ' raw.php ')
print(rem)

a=url+'H3IIO.php  '
print('[+]',a)
rem=requests.get(url, 'H3IIO.php ')
print(rem)

a=url+'H3IIX.php  '
print('[+]',a)
rem=requests.get(url, 'H3IIX.php ')
print(rem)

a=url+'shell.php  '
print('[+]',a)
rem=requests.get(url, 'shell.php ')
print(rem)

a=url+'cgi.php  '
print('[+]',a)
rem=requests.get(url, 'cgi.php ')
print(rem)

a=url+'DrugO.php  '
print('[+]',a)
rem=requests.get(url, 'DrugO.php ')
print(rem)

a=url+'xleet.php  '
print('[+]',a)
rem=requests.get(url, 'xleet.php ')
print(rem)

a=url+'php/mysql  '
print('[+]',a)
rem=requests.get(url, 'php/mysql ')
print(rem)

a=url+'security.txt  '
print('[+]',a)
rem=requests.get(url, 'security.txt ')
print(rem)

a=url+'filedown.php?file=  '
print('[+]',a)
rem=requests.get(url, 'filedown.php?file= ')
print(rem)

a=url+'admin/index.php  '
print('[+]',a)
rem=requests.get(url, 'admin/index.php ')
print(rem)

a=url+'scopia/entry/index.jsp  '
print('[+]',a)
rem=requests.get(url, 'scopia/entry/index.jsp ')
print(rem)

a=url+'portal/apis/fileExplorer  '
print('[+]',a)
rem=requests.get(url, 'portal/apis/fileExplorer ')
print(rem)

a=url+'aws.s3  '
print('[+]',a)
rem=requests.get(url, 'aws.s3 ')
print(rem)

a=url+'_cpanel/forgotpwd  '
print('[+]',a)
rem=requests.get(url, '_cpanel/forgotpwd ')
print(rem)

a=url+'backup  '
print('[+]',a)
rem=requests.get(url, 'backup ')
print(rem)

a=url+'database.sql.zi  '
print('[+]',a)
rem=requests.get(url, 'database.sql.zi ')
print(rem)

a=url+'etc/shadow  '
print('[+]',a)
rem=requests.get(url, 'etc/shadow ')
print(rem)

a=url+'htpasswd  '
print('[+]',a)
rem=requests.get(url, 'htpasswd ')
print(rem)

a=url+'mysql.conf  '
print('[+]',a)
rem=requests.get(url, 'mysql.conf ')
print(rem)

a=url+'passwd  '
print('[+]',a)
rem=requests.get(url, 'passwd ')
print(rem)

a=url+'people.lst  '
print('[+]',a)
rem=requests.get(url, 'people.lst ')
print(rem)

a=url+'pwd.db  '
print('[+]',a)
rem=requests.get(url, 'pwd.db ')
print(rem)

a=url+'wp-admin  '
print('[+]',a)
rem=requests.get(url, 'wp-admin ')
print(rem)

a=url+'ForgotPassword  '
print('[+]',a)
rem=requests.get(url, 'ForgotPassword ')
print(rem)

a=url+'wp-login  '
print('[+]',a)
rem=requests.get(url, 'wp-login ')
print(rem)

a=url+'userportal  '
print('[+]',a)
rem=requests.get(url, 'userportal ')
print(rem)

a=url+'loginpanel  '
print('[+]',a)
rem=requests.get(url, 'loginpanel ')
print(rem)

a=url+'memberlogin  '
print('[+]',a)
rem=requests.get(url, 'memberlogin ')
print(rem)

a=url+'remote  '
print('[+]',a)
rem=requests.get(url, 'remote ')
print(rem)

a=url+'dashboard  '
print('[+]',a)
rem=requests.get(url, 'dashboard ')
print(rem)

a=url+'auth  '
print('[+]',a)
rem=requests.get(url, 'auth ')
print(rem)

a=url+'portal  '
print('[+]',a)
rem=requests.get(url, 'portal ')
print(rem)

a=url+'security  '
print('[+]',a)
rem=requests.get(url, 'security ')
print(rem)

a=url+'security "reward"  '
print('[+]',a)
rem=requests.get(url, 'security "reward" ')
print(rem)

a=url+'bug bounty  '
print('[+]',a)
rem=requests.get(url, 'bug bounty ')
print(rem)

a=url+'index.html  '
print('[+]',a)
rem=requests.get(url, 'index.html ')
print(rem)

a=url+'fckeditor  '
print('[+]',a)
rem=requests.get(url, 'fckeditor ')
print(rem)

a=url+'security.txt  '
print('[+]',a)
rem=requests.get(url, 'security.txt ')
print(rem)

a=url+'ls.txt  '
print('[+]',a)
rem=requests.get(url, 'ls.txt ')
print(rem)

a=url+'ls.conf  '
print('[+]',a)
rem=requests.get(url, 'ls.conf ')
print(rem)

a=url+'ls.cfg  '
print('[+]',a)
rem=requests.get(url, 'ls.cfg ')
print(rem)

a=url+'sitemap.xml  '
print('[+]',a)
rem=requests.get(url, 'sitemap.xml ')
print(rem)

a=url+'guestimage.html  '
print('[+]',a)
rem=requests.get(url, 'guestimage.html ')
print(rem)

a=url+'home.asp  '
print('[+]',a)
rem=requests.get(url, 'home.asp ')
print(rem)

a=url+'index of  '
print('[+]',a)
rem=requests.get(url, 'index of ')
print(rem)
print('[![SQLi]!]')
a=url+'php?id=  '
print('[+]',a)
rem=requests.get(url, 'php?id= ')
print(rem)

a=url+'asp?id=" –   '
print('[+]',a)
rem=requests.get(url, 'asp?id=” –  ')
print(rem)

a=url+'changelog.txt  '
print('[+]',a)
rem=requests.get(url, 'changelog.txt ')
print(rem)

a=url+'php.txt  '
print('[+]',a)
rem=requests.get(url, 'php.txt ')
print(rem)

a=url+'code.txt  '
print('[+]',a)
rem=requests.get(url, 'code.txt ')
print(rem)

a=url+'filemanage  '
print('[+]',a)
rem=requests.get(url, 'filemanage ')
print(rem)

a=url+'accessibility/  '
print('[+]',a)
rem=requests.get(url, 'accessibility/ ')
print(rem)













