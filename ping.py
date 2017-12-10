import os
import sys
import getopt

def usage():
       
       print("Uso: Ping")
       print("")
       print("-d Direccion")
       print("-h info de ayuda")

def main():
       'Main function'
       global Action, x, y, z

       try:
              opts, args = getopt.getopt(sys.argv[1:], "d:h")

       except getopt.GetoptError as err:
              print("Error: "+str(err)+", Intente -h para ayuda\n\n")
              usage()
              sys.exit(2)

       for o, a in opts:
                if o in ("-h"):
                        usage()
                        sys.exit()
                if o in ("-d"):
                        try:
                            response = os.system("ping -c 1 " + hostname)
                            if response == 0:
                                pingstatus = "Ususario Activo"
                            else:
                                pingstatus = "Usuario no Activo"
                            print(pingstatus)

                        except:
                            sys.exit(2)
if __name__ == "__main__":
main()
