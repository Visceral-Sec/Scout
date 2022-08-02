# Validation Check
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
#                                                              @@@@@   
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
from scoutMain import scout_Terminate
from scoutClasses import scoutNmapUserInputClass
#Global Variable, is changed by validationTermiante
from scoutMain import scout_Terminate
logging.basicConfig(filename='Scout.log', level=logging.DEBUG)
#     Plan for Input Validation
#     Pass in userScout Input classes. (Nmap/Gobuster at time of writing)
#     Scan each class artibute. 
#     if error is found it is displayed in the scout log. Any issues will prevent the application from running (could potentially be changed)
#    
# Not fully implemented yet 
def ValidationTerminate(errorMessage: str ,errorType: str) -> bool:
    logging.info("Error in scoutConfig, consider changing configuration")
    if errorType == "E":
        logging.error(errorMessage)
    if errorType == "I":
        logging.info(errorMessage)
    verfication = True
    # code that handles exiting


def scoutIPChecker(ip: str):
    # Returns true if larger than 255 or smaller than 1 
    numCheck = lambda a : a > 255 or a < 1
    # First check --> split apart the octets, if doesn't split return error
    ip = ip.split(".",3)
    if len(ip) != 4:
        ValidationTerminate("IP Octect Issues, check config", "E")
    # Second Check --> if all the octects are between 255 or 1
    for octect in ip:
        if numCheck(octect) == True:
            ValidationTerminate("IP Octect is not between 255 and 1, please check configuration", "E")
    # second check --> subnet mask/cidr stuff not yet implemented
    #
    #
    # Finally Return True
    return True

def scoutPortChecker(range: list):
    portCheck = lambda a: a > 65535 or a < 1
    for port in range:
        if portCheck(port) == True:
            ValidationTerminate("Port is out of bounds", "E")
def scoutOptionChecker(option: str) -> bool:
    optionCheck = lambda a: a > 4 or a < 1
    if optionCheck == True:
        ValidationTerminate("Option Error", 'E')

def scoutMacChecker(mac: str):
    # Check One, splitting mac address
    mac = mac.split(".",5)
    if len(mac) != 5:
        ValidationTerminate("Mac address should contain 6 octects","E")
    #Check two
    for octect in mac:
        try:
            int(octect,16)
        except ValueError:
            ValidationTerminate("Mac Address Error, value is not hexademical",'E')
        except:
            ValidationTerminate("Mac Address Error" ,'E')

def scoutInputValidation(scoutNmapUserInput):
    verfication = False
    # Checking the IP Checker
    scoutIPChecker(scoutNmapUserInput.target)
    scoutOptionChecker(scoutNmapUserInput.option)
    scoutPortChecker(scoutNmapUserInput.range)
    if verfication == True:
        scout_Terminate()
