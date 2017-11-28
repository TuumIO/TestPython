#!/usr/bin/python

import sys,os,getopt,time, select, subprocess

def usage():
       
        print("Hello World")
        print("Usage: Adding Test")
        print("")
        print(" --A (-f) First Number")
        print(" --B (-s) Second Number")
        print(" --help this screen")

def main():
        'Main function'
        global Action, x, y, z

        try:
                opts, args = getopt.getopt(sys.argv[1:], "sl:d:i", ["First=", "Second=", "help"]) # output=

        except getopt.GetoptError as err:
                print("Error: "+str(err)+", Try --help for usage\n\n")
                # usage()
                sys.exit(2)

        for o, a in opts:
                if o in ("-h", "--help"):
                        usage()
                        sys.exit()
                if o in ("-f"):
                        try:
                                x=float(a)
                        except ValueError:
                                print("--from argument is taking only numeric values")
                                sys.exit(2);

                if o in ("-s"):
                        try:
                                y=float(a)
                        except ValueError:
                                print ("--to argument is taking only numeric values")
                                sys.exit(2);
                
        if len(opts) == 0:
            print("Adding Test,  See --help for usage")
            sys.exit()
            
        z = x + y
        print(z)
        print("Thats it")

if __name__ == "__main__":
main()
