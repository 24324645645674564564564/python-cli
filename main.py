import cmd
import os

class Cli(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "> "
        self.intro  = "Welcome\n for the details enter help 'help'"
        self.doc_header ="Availbale commands "

    def do_show_cpu(self, args):
        """show_cpu - cpu usage"""
        os.system("sar 2")

    def do_show_mem(self, args):
        """show_mem -  RAM usage"""
        os.system("free")

    def do_show_disk(self, args):
        """show_disk - free space on hdd"""
        os.system("df -h")

    def do_show_net(self, args):
        """show_net -net swttings"""
        os.system("sudo ifconfig")
        os.system("sudo route -n")


    def default(self, line):
        print ("error")
    def do_syslog(self,arg):
        """syslog-system log """
        os.system("sudo tail -f /var/log/syslog")    
    def do_browser(self,arg):
        """ browser-star browser"""
        os.system("/usr/bin/lynx")
    def do_nload(self,arg):
        """ network usage """
        os.system("nload")
            
    def emptyline(self):
        pass

if __name__ == "__main__":
    cli = Cli()
    try:
        cli.cmdloop()
    except KeyboardInterrupt:
        print ("Goodbye")
