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
# 
# 
"""
        Scout Project Diagram
    ──────────────────────────────

┌───────────┐   ┌────────────────┐     ┌───────────┐
│ scoutMain │◄──┤ scoutValidation│◄────┤scoutConfig│
└─────┬─────┘   └────────────────┘     └───────────┘
      │          <You are here>
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







import scoutClasses
import logging, threading, time 
import time
import scoutBuster
import scoutNmap

class scoutThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

   # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    #    executor.map(thread_function, range(3))


def scoutHandler(scoutNmapUserInput, scoutGobusterInput):
    nmapThread = threading.Thread(target=scoutNmap.scoutNmap(scoutNmapUserInput), name="NmapThread")
    goThread = threading.Thread(target=scoutBuster.scoutBuster(scoutGobusterInput), name="goBusterThread")

    #Smart Threading stuff goes here. I Will return when more confident on how to thread in python
    nmapThread.start()
    goThread.start()
    time.sleep(5)
    nmapThread.join()
    goThread.join()
