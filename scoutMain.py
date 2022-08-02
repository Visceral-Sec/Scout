#                                 .&@@@@@@@@@@@@@@@@(.                                                                                                                               
#                            .@@@@@@%(.. ..#%@@@@@@@&#@@                                                                                                                            
#                           (@@@@#                 @@   @                                                                                                                            
#                          @@@@@                     @@@@                                                                                                                            
#                         @@@@@,                      @@@                                                                                                                            
#                        @@@@@@,                       @@                                                                                                                            
#                        @@@@@@@                                            (@@@@@@@@@@@@@,                  .(%                                                                     
#                        @@@@@@@&                                        %@@%             @@@.               #@@                                                                     
#                         @@@@@@@@@*                        (&    ,&@  *@@,                 /@@    ,     .*&@@@@@@@@@@                                                               
#                          @@ /@@@@@@@@@#*                (@        , (@@                     @@. (@     @%  @@@                                                                     
#                            #/    /@@@@@@@@@@@@&*        @@          @@.                     *@& (@     @%  @@@                                                                     
#                                         .#@@@@@@@@@@(   @@          @@                      .@@ (@.    @%  @@@                                                                     
#                                                (@@@@@@@/#@/         %@                      &@(  %@%(%,@@&.@@@                                                                     
#                                                    ,@@@@@ (@@#*,(&/  @@%                   @@#             @@@                                                                     
#                                                       @@@@            ,@@&               @@@               #@@@&,./&                                                               
#                                                        @@@(              @@@@&,     ,@@@@*                                                                                         
#                                                        @@@(              *@@. *#%%%#,                                                                                              
#                                                       /@@@              #@@                                                                                                        
#                                                      &@@@,            .@@@(                                                                                                        
#                                                    &@@@(             *@@@*                                                                                                         
#                                                 #@@@@%              %@@@,                                                                                                          
#                                             *@@@@@.                @@@@                                                                                                            
#                                           @@@@,                   @@@@                                                                                                             
#                                         ,@(                     *@@@@                                                                                                              
#                                                                %@@@@                                                                                                               
#                                                               @@@@&                                                                                                                
#                                                              @@@@@                                                                                                                 open('Scout.log', 'w').close()
"""
        Scout Project Diagram
    ──────────────────────────────
<You are here>
┌───────────┐   ┌────────────────┐     ┌───────────┐
│ scoutMain │◄──┤ scoutValidation│◄────┤scoutConfig│
└─────┬─────┘   └────────────────┘     └───────────┘
      │
      │         ┌──────────────┐
      └─────►   │ Scout Handler│
                └───┬───────┬──┘
                    │       │
                    │       │
                    │       │
                    │       │
                    │       │
                    │       │
             ┌──────┴──┐  ┌─┴──────────┐
             │         │  │            │
             │ScoutNmap│  │ ScoutBuster│
             │         │  │            │
             └─────────┘  └────────────┘
                        │
                        │
                        │
                        │                 ┌────────────┐
                        └───────────────► │ScoutWriter │
                                          └────────────┘
"""
import logging
import sys
import getopt
from scoutClasses import scoutNmapUserInputClass

from scoutHandler import scoutHandler
open('Scout.log', 'w').close()
logging.basicConfig(filename='Scout.log', level=logging.DEBUG)

#Default debugging log setup. Details the operations completed before the programming, useful for identifiying potentially issues.
lines_Read = 0    
#This function splits Input from the config File
def scout_Splitter(file):
    f = open(file, "r")
    global lines_Read
    line_Reader= f.readlines()
    text = line_Reader[lines_Read]
    logging.info("%s", text)
    # COMMAND FOR CHECKING IF COMMENT, Recursion used if a comment is found, (Buggy)
    if text.startswith("#"):
        logging.info("Commented found in scoutfile.txt")
        lines_Read = lines_Read+1
        scout_Splitter(file)
    else:
        if (':' in text):
            split=text.split(':')
            f.close()
            lines_Read = lines_Read+1
            logging.info('File Successfully parsed')
            return split[1]
        else:
            logging.error('File Syntax invalid')
            f.close()
            scout_Terminate()

#Opens the File
def scout_Opener(scoutConfig):
    try:
        f = open(scoutConfig, "r")
    except:
        logging.info('Scout file could not be found')
        scout_Terminate()
    else:
        f.close()
        logging.info('File Successfully opened %s', scoutConfig)
        scout_Loader(scoutConfig)
        
#Terminates The Scout
def scout_Terminate():
    logging.error('An Error occured. Check previous step')
    logging.error('SCOUT TERMINATED')
    print("Scout Terminated, Please Check Error log to identify the issue.")
    sys.exit(2)

#Scout Launch
def scout_launch(argv):
    scoutConfig = ''
    try:
        option, arg = getopt.getopt(argv,":f:",["file="])
    except getopt.GetoptError:
        logging.error('Invalid Call')
        sys.exit(2)
    for option, arg in option:
        if option == '-f':
            logging.info('File Given at:' + arg)
            scoutConfig = arg
    scout_Loader(scoutConfig)


def scout_Loader(file_Location):
    logging.info('Extracting Config Info')
    # Easier way to do this
    scout_Dictionary ={ "Target_Network": {'Domain':scout_Splitter(file_Location),'IP':scout_Splitter(file_Location), 'nmapRange':scout_Splitter(file_Location), 'nmapIntensity':scout_Splitter(file_Location)}
                    }   
    logging.info('Information Got:')
    for key in scout_Dictionary:
        logging.info(key + ':' + str(scout_Dictionary[key]))
    # Loading classes
    scoutNmapUserInput = scoutNmapUserInputClass(scout_Dictionary['Target_Network']['IP'],scout_Dictionary['Target_Network']['nmapRange'],scout_Dictionary['Target_Network']['nmapIntensity'])
    
    logging.info("Calling Module Handler")
    scoutHandler()
    

scout_launch(sys.argv[1:])
