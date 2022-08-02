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
            <You are here> 
                        │
                        │
                        │
                        │                 ┌────────────┐
                        └───────────────► │ScoutWriter │
                                          └────────────┘
"""
import logging
import nmap
from scoutMain import scout_Terminate
from scoutClasses import scoutNmapUserInputClass
logging.basicConfig(filename='Scout.log', level=logging.DEBUG)

def scoutNmapScanExtreme(scoutNmapUserInput):
    logging.info("Extreme Intensity Nmap Scan Initiated")
    target = scoutNmapUserInput.target
    range = scoutNmapUserInput.range
    map = nmap.PortScanner()
    map.command_line()
def scoutNmapScanHigh(scoutNmapUserInput):
    target = scoutNmapUserInput.target
    range = scoutNmapUserInput.range
    logging.info("High Intensity Nmap scan Initiated")
    map = nmap.Nmap()
def scoutNmapscanMedium(scoutNmapUserInput):
    target = scoutNmapUserInput.target
    range = scoutNmapUserInput.range
    logging.info("Medium Intensity Nmap Scan initiated")
    map = nmap.Nmap()
def scoutNmapscanLow(scoutNmapUserInput):
    target = scoutNmapUserInput.target
    range = scoutNmapUserInput.range<
    logging.info("Low Intensity Nmap scan initiated")
    map = nmap.Nmap()

def scoutNmapLauncher(scoutNmapUserInput: object) -> object:
    

    # Setting Intensity 
    if scoutNmapUserInput.options != 1:
        if scoutNmapUserInput.options !=2: 
            if scoutNmapUserInput.options !=3:
                if scoutNmapUserInput.options !=4:
                    logging.info("Error in config, this shouldn't happen. Contact visceral regarding this issue")
                    scout_Terminate()
                else:
                    scoutNmapScanExtreme(scoutNmapUserInput)
            else:
                scoutNmapScanHigh(scoutNmapUserInput)
        else:
            scoutNmapscanMedium(scoutNmapUserInput)
    else:
        scoutNmapscanLow(scoutNmapUserInput)
    
    #Setting Intensity Redutant, 
    """
    match intensity:
        case "low":
            print("Low Scanning    Enabled")
            scoutNmapUserInput.args = "Low scanning args"
            return scoutNmapUserInput
        case "medium":
            print("Medium Scanning Enabled")
            scoutNmapUserInput.args = "Medium scanning args"
            return scoutNmapUserInput
        case "high":
            scoutNmapUserInput.args = "High scanning args"
            print("High intensity Enabled")
            return scoutNmapUserInput
        case "extreme":
            scoutNmapUserInput.args = "Extreme scanning args"
            print("extreme Intensity Enabled")
            return scoutNmapUserInput
    """

# Called by scout Handler
def scoutNmap(scoutNmapUserInput):
    scoutNmapUserInput = scoutNmapLauncher(scoutNmapUserInput) # Converts Option from 1 --> low intensity
