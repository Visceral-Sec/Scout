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
<You are here>  (This is used for all the differnet configurations)

        Scout Project Diagram
    ??????????????????????????????????????????????????????????????????????????????????????????
???????????????????????????????????????   ??????????????????????????????????????????????????????     ???????????????????????????????????????
??? scoutMain ??????????????? scoutValidation?????????????????????scoutConfig???
???????????????????????????????????????   ??????????????????????????????????????????????????????     ???????????????????????????????????????
      ???
      ???         ????????????????????????????????????????????????
      ?????????????????????   ??? Scout Handler???
                ????????????????????????????????????????????????
                    ???       ???
                    ???       ???
                    ???       ???
                    ???       ???
                    ???       ???
                    ???       ???
             ?????????????????????????????????  ??????????????????????????????????????????
             ???         ???  ???            ???
             ???ScoutNmap???  ??? ScoutBuster???
             ???         ???  ???            ???
             ?????????????????????????????????  ??????????????????????????????????????????
                        ???
                        ???
                        ???
                        ???                 ??????????????????????????????????????????
                        ??????????????????????????????????????????????????? ???ScoutWriter ???
                                          ??????????????????????????????????????????
"""
class scoutNmapUserInputClass:
    def __init__(self, targets, range, option) -> None:
        self.target = [targets]
        self.range = range
        self.option = option
        self.args = ""

class scoutGobusterInputClass:
    def __init__(self) -> None:
        self.target = ""
