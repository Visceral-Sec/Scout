# Require for Script Functionality

# SYS For File Commands
# Getops For Commands line arguments (Will be extended)
# Logging for logging purposes
# Time for thread manipulation
# Threading
import sys, getopt, logging, threading, time, requests as reqs, json, subprocess, nmap

# Require for Report Generation
from geopy.geocoders import Nominatim
from datetime import datetime
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
# Log File, (Logs completetion and issues of certain classes)
open('Scout.log', 'w').close()
logging.basicConfig(filename='Scout.log',encoding='utf-8', level=logging.DEBUG)           


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
#                                                              #@@# 
"""
Scout Diagram

               SCOUT_FILE
SCOUT.SH    ------------->       SCOUT.py


                                    ┃
                                    ┃
                                    ┃
                                    ┃
                                    ↓
                                scout_Lauch  ---> file_opener ---> file_Reader ----> Module Handler -------> WEB SCRAPPER MODULES 
                                                                                              ┃                         ┃
                                                                                              ┃                         ┃
                                                                                              ┃                         ┃
                                                                                              ┃                         ┃
                                                                                              ┃                         ┃
                                                                                              ┃                         ┃
                                                                                              ↓                         ↓
                                                                                        WEB SRAPPER MODULES     ---------------------------------------> Report Writer --------> Scout_Report.pdf
                                                                                            
"""
#
#Globals
#

#Used for keeping track how far through the file, very important variable for ensuring all data lands into the correct dictionary
lines_Read = 0
#Boolean for when the report is finalised, the quick "report_Completed = 1 " should only be selected once all MODULES have been called.
report_Completed=0

#
#Functions
#

# Launchs the Script (Landing Point), Takes command line argument (File Location)
def scout_launch(argv):
    scoutFile = ''
    try:
      option, arg = getopt.getopt(argv,":f:",["file="])
    except getopt.GetoptError:
      logging.error('Invalid Call')
      sys.exit(2)
    for option, arg in option:
        if option == '-f':
            logging.info('File Given at:' + arg)
            scoutFile = arg
    file_Opener(scoutFile)


# Error Function, Called when scout encounters a terminal error 
def scout_Terminate():
    logging.error('An Error occured. Check previous step')
    logging.error('SCOUT TERMINATED')
    sys.exit(2)

# Exit Function, Called when scout encourters a normal error 
def scout_Exit():
    logging.info('Successfully Completed')
    logging.info('SCOUT TERMINATED')
    sys.exit(0)

#Function for Opening the scout file (Inputs)
def file_Opener(file_Location):
    try:
        f = open(file_Location, "r")
    except:
        logging.info('Scout file could not be found')
        scout_Terminate()
    else:
        f.close()
        logging.info('File Successfully opened %s', file_Location)
        file_Reader(file_Location)
"""
#Function for splitting input 
def text_Splitter(file,parameter):
    f = open(file, "r")
    global lines_Read
    line_Reader= f.readlines()
    text = line_Reader[lines_Read]
    logging.info("%s", text)
    # COMMAND FOR CHECKING IF COMMENT, Recursion used if a comment is found, (Restarts the function with the lines read increased (neat trick))
    if text.startswith("#"):
        logging.info("Commented found in scoutfile.txt")
        lines_Read = lines_Read+1
        text_Splitter(file,parameter)
    else:
        if (':' in text):
            split=text.split(':')
            f.close()
            lines_Read = lines_Read+1
            logging.info('File Successfully parsed')
            if split[0] == parameter:
                return split[1]
            else:
                lines_Read = lines_Read+1
                text_Splitter(file,parameter)
        else:
            logging.error('File Syntax invalid')
            f.close()
            scout_Exit()
"""
def text_Splitter(file):
    f = open(file, "r")
    global lines_Read
    line_Reader= f.readlines()
    text = line_Reader[lines_Read]
    logging.info("%s", text)
    # COMMAND FOR CHECKING IF COMMENT, Recursion used if a comment is found, (Restarts the function with the lines read increased (neat trick))
    if text.startswith("#"):
        logging.info("Commented found in scoutfile.txt")
        lines_Read = lines_Read+1
        text_Splitter(file)
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
            scout_Exit()

#File Reader (Not multi-threaded in case of issues with parrallaism
def file_Reader(file_Location):
    # Unfished prototype for more effective and less buggy file reader
    """
    scout_Dictionary ={ "Target_Identity": {'Target_Username':text_Splitter(file_Location,"Target_Username"),'Target_Full_Name':text_Splitter(file_Location,"Target_Full_Name"),'Dating_User_Name':text_Splitter(file_Location,'Dating_User_Name'),'Target_Telephone_Number':text_Splitter(file_Location,"Target_Telephone_Number"),'Vehcile_Identification_Number':text_Splitter(file_Location,"Vehcile_Identification_Number"),'Coordinates':text_Splitter(file_Location,"Coordinates")},
                        "Target_Social_Media":{'Facebook':text_Splitter(file_Location,'Facebook'),'Twitter':text_Splitter(file_Location,'Facebook'),"Reddit":text_Splitter(file_Location,'Reddit'),"LinkedIn":text_Splitter(file_Location,'LinkedIn'),"Other_social_Media":text_Splitter(file_Location,'Other_Social_Media'),"Skype":text_Splitter(file_Location,'Skype'),"Snapchat":text_Splitter(file_Location,'Snapchat'),"Kik":text_Splitter(file_Location,'Kik')},
                        "Target_Network": {'Domain':text_Splitter(file_Location,'Domain'),'IP':text_Splitter(file_Location,'IP')},
                        "Target_Misc":{'Images':text_Splitter(file_Location,'Images'),'Videos':text_Splitter(file_Location,'Videos'),'Webcams':text_Splitter(file_Location,"Webcams"),'Documents':text_Splitter(file_Location,'Documents')}
                        }
    """
    scout_Dictionary ={ "Target_Identity": {'Target_Username':text_Splitter(file_Location,),'Target_Full_Name':text_Splitter(file_Location),'Dating_User_Name':text_Splitter(file_Location),'Target_Telephone_Number':text_Splitter(file_Location),'Vehcile_Identification_Number':text_Splitter(file_Location),'Coordinates':text_Splitter(file_Location)},
                        "Target_Social_Media":{'Facebook':text_Splitter(file_Location),'Twitter':text_Splitter(file_Location),'Reddit':text_Splitter(file_Location),'LinkedIn':text_Splitter(file_Location),'Other_social_Media':text_Splitter(file_Location),'Skype':text_Splitter(file_Location),'Snapchat':text_Splitter(file_Location),'Kik':text_Splitter(file_Location)},
                        "Target_Network": {'Domain':text_Splitter(file_Location),'IP':text_Splitter(file_Location)},
                        "Target_Misc":{'Images':text_Splitter(file_Location),'Videos':text_Splitter(file_Location),'Webcams':text_Splitter(file_Location),'Documents':text_Splitter(file_Location)},
                        "Target_Command":{"nmap":text_Splitter(file_Location)}
                        }
                        
    logging.info('Calling Module_Handler')
    Module_handler(scout_Dictionary)


# Main Function (Runs Mosts things) (I think I can just make this function run threaded and it just works?)
def Module_handler(scout_Dictionary):
    logging.info("%s", scout_Dictionary)
    # Initlizating the values that will be in the classes to store the data (Can't do this during class definiton because issues to do with python thinking that they tuplas? couldn't find a fix, this is a work around)
    target_Identity_User_Name = scout_Dictionary["Target_Identity"]["Target_Username"]
    target_Identity_Full_Name = scout_Dictionary["Target_Identity"]["Target_Full_Name"]
    target_identity_Telephone_Number = scout_Dictionary["Target_Identity"]["Target_Telephone_Number"]
    target_identity_VIN = scout_Dictionary["Target_Identity"]["Vehcile_Identification_Number"]
    target_identity_Coordinate = scout_Dictionary["Target_Identity"]["Coordinates"]
    target_Dating_User_Name = scout_Dictionary["Target_Identity"]["Dating_User_Name"]
    # Inilizating the target_identity class
    logging.info("Inilisating the target identity class")
    target_identity = class_target_Identity(target_Identity_User_Name,target_Identity_Full_Name,target_identity_Telephone_Number,target_identity_VIN,target_identity_Coordinate,target_Dating_User_Name)
    

    # Creating the network values
    target_Network_Domain = scout_Dictionary["Target_Network"]["Domain"]
    target_Network_IP = scout_Dictionary["Target_Network"]["IP"]

    # Inilizating the target_network class
    logging.info("Inilisating the target identity class")
    target_Network = class_target_Network(target_Network_Domain,target_Network_IP)
    
    #Creating the social media values
    target_Social_Media_Facebook = scout_Dictionary["Target_Social_Media"]["Facebook"]
    target_Social_Media_Twitter = scout_Dictionary["Target_Social_Media"]["Twitter"]
    target_Social_Media_Reddit = scout_Dictionary["Target_Social_Media"]["Facebook"]
    target_Social_Media_Linkedin = scout_Dictionary["Target_Social_Media"]["LinkedIn"]
    target_Social_Media_other_social_media = scout_Dictionary["Target_Social_Media"]["Other_social_Media"]
    target_Social_Media_Skype = scout_Dictionary["Target_Social_Media"]["Skype"]
    target_Social_Media_snapchat = scout_Dictionary["Target_Social_Media"]["Snapchat"]
    target_Social_Media_kik = scout_Dictionary["Target_Social_Media"]["Kik"]

    # Inilizating the identity class
    logging.info("Inilisating the target identity class")
    target_Social_Accounts = class_target_Social_Accounts(target_Social_Media_Facebook,target_Social_Media_Twitter, target_Social_Media_Reddit, target_Social_Media_Linkedin, target_Social_Media_other_social_media,target_Social_Media_Skype,target_Social_Media_snapchat,target_Social_Media_kik)
    
    #Creating the misc values 
    target_misc_images=scout_Dictionary["Target_Misc"]["Images"]
    target_misc_videos=scout_Dictionary["Target_Misc"]["Videos"]
    target_misc_webcams=scout_Dictionary["Target_Misc"]["Webcams"]
    target_misc_documents=scout_Dictionary["Target_Misc"]["Documents"]

    # Inilizating the target_misc class
    logging.info("Inilisating the target misc class")
    target_Misc = class_target_Misc(target_misc_images,target_misc_videos,target_misc_webcams,target_misc_documents)
    

    # Creating the command values
    target_commands_nmap = scout_Dictionary["Target_Command"]["nmap"]
    target_commands = class_target_Commands(target_commands_nmap)

    logging.info('Creating Report Template')
    scout_Report = class_scout_Report()
    # Creating the function classes  
    # Classes don't use __init__ to load in the classes created above because adding new functionality would then mean updated it in two different places
    target_network_functions = class_target_Network_Functions
    target_social_functions = class_target_Social_Functions
    target_identity_functions = class_target_Identity_Functions
    target_misc_functions  = class_target_Misc_Functions
    target_commands_functions = class_target_Commands_Functions

    #Calling the Network Functions
    """
    CURRENTLY COMMENTED TO PREVENT ISSUES
    """
    target_network_functions.whoIS(target_Network, scout_Report)

    # Calling the social functions
    
    target_social_functions.facebookScraper(target_Social_Accounts, scout_Report)
    target_social_functions.twitterScraper(target_Social_Accounts, scout_Report)
    target_social_functions.redditScraper(target_Social_Accounts, scout_Report)
    target_social_functions.linkedInScraper(target_Social_Accounts, scout_Report)
    target_social_functions.other_social_mediaScraper(target_Social_Accounts, scout_Report)
    target_social_functions.skypeScraper(target_Social_Accounts, scout_Report)
    target_social_functions.snapchatScraper(target_Social_Accounts, scout_Report)
    target_social_functions.kikScraper(target_Social_Accounts, scout_Report)


    # Calling the identity functions
    target_identity_functions.full_name_Scraper(target_identity, scout_Report)
    target_identity_functions.dating_user_nameScraper(target_identity, scout_Report)
    target_identity_functions.target_telephone_numberScraper(target_identity, scout_Report)
    target_identity_functions.VINScraper(target_identity, scout_Report)
    target_identity_functions.CoordinatesScraper(target_identity, scout_Report)

    # Calling the Misc Functions
    target_misc_functions.target_image_Function(target_Misc, scout_Report)
    target_misc_functions.target_video_Function(target_Misc, scout_Report)
    target_misc_functions.target_webcams_Funciton(target_Misc, scout_Report)
    target_misc_functions.target_document_Function(target_Misc, scout_Report)

    # Calling the Nmap Functions
    target_commands_functions.target_nmap(target_commands, target_Network, scout_Report)
    scout_Report.report_Complete=1 
    scout_Report.report_Writer()
#
#Classes
#
#Personal Info
# Combine the writing functions with these and then polymorphism 

class class_target:
    def __init__(self):
        pass

class class_target_Identity(class_target):
    def __init__(self, Target_Username, Target_Full_Name, Target_Telephone_Number, Vehcile_Identification_Number, Coordinates, Dating_User_Name):
        self.Target_Username = Target_Username
        self.Target_Full_Name = Target_Full_Name
        self.Target_Telephone_Number = Target_Telephone_Number
        self.Dating_User_Name = Dating_User_Name
        self.VIN = Vehcile_Identification_Number
        self.Coordinates = Coordinates
        self.Dating_User_Name = Dating_User_Name
        logging.info("Target_Identity class is initialised")

#Website Info
class class_target_Network(class_target):
    def __init__(self, Domain, IP):
        self.Domain = Domain
        self.IP = IP
        logging.info("Class_target_network is initialised")

class class_target_Social_Accounts(class_target):
    def __init__(self, Facebook, Twitter, Reddit, LinkedIn, Other_social_Media, Skype, Snapchat, Kik):
        self.Facebook = Facebook
        self.Twitter = Twitter
        self.Reddit = Reddit
        self.LinkedIn = LinkedIn
        self.Other_social_Media = Other_social_Media
        self.Skype = Skype
        self.Snapchat = Snapchat
        self.Kik = Kik
        logging.info("Class social accounts is initialised")

class class_target_Misc(class_target):
    def __init__(self, Images, Videos, Webcams, Documents):
        self.Image =Images
        self.Videos = Videos
        self.Webcams = Webcams
        self.Documents = Documents
        logging.info("Class target misc is initialised")

class class_target_Commands(class_target):
    def __init__(self, nmap):
        self.nmap=nmap
        logging.info("Class target commands is initialised")


# Stores output information from Scrapper Modules (Used by scout_Report_Build er to build the report)
class class_scout_Report:
    def __init__(self): # Takes the classes generated by the modules 
        self.report_global = globals
        self.report_Complete = self.report_global
        self.scout_Story=[]
        self.report = SimpleDocTemplate("Scout_Report.pdf",pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)
        # Report formatting
        logo = "Scout_Logo.png"
        formatted_time=datetime.today().strftime('%Y-%m-%d')
        im=Image(logo)
        self.scout_Story.append(im)
        self.styles=getSampleStyleSheet()
        self.styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
        ptext = '%s' % formatted_time
        self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
        self.scout_Story.append(Spacer(1, 12))
        ptext='Scout Generated OSINT Report'
        self.scout_Story.append(Paragraph(ptext, self.styles["Title"]))
        self.scout_Story.append(Spacer(1,1))

# Called at the end, creates the final report
    def report_Writer(self):
        if self.report_Complete == 1:
            logging.info('Report built')
            self.report.build(self.scout_Story)

            

    def network_Writer(self,target_info,target_result,target_type): 
        #target_info = the targets given info by the user 
        #target_result = json object given by the get requests
        #target_type = the type of network data given (aka is it a domain or an operating system etc?)
        if target_type == 'whoIS':  #This checks the type of wr
            ptext='Domain Selected is ' + target_info.Domain
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 5))
            ptext='WHOS IS report:'
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 3))
            ptext='created_date: ' + target_result["WhoisRecord"]["createdDate"]
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            ptext='updated_date: ' + target_result["WhoisRecord"]["updatedDate"]
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            ptext='expires_date: ' + target_result["WhoisRecord"]["expiresDate"]
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            ptext='Registrant: '
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            try:
                ptext='Organisation - ' + target_result["WhoisRecord"]["registrant"]["organization"]
            except:
                ptext='No Organisation Found'
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            try:
                ptext='State - ' + target_result["WhoisRecord"]["registrant"]["state"]
            except:
                ptext='No State Found'
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            try:
                ptext='Country - ' + target_result["WhoisRecord"]["registrant"]["country"]
            except:
                ptext='No Country Found'
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            try:
                ptext='Country Code - ' + target_result["WhoisRecord"]["registrant"]["countryCode"]
            except:
                ptext='No Country Code found'
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            ptext='Admin Contact'
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            try:
                ptext='Organisation - ' + target_result["WhoisRecord"]["administrativeContact"]["organization"]
            except:
                ptext='Organisation Not found'
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            try:
                ptext='State - ' + target_result["WhoisRecord"]["administrativeContact"]["state"]
            except:
                ptext='No State given'
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            try:
                ptext='Country - ' + target_result["WhoisRecord"]["administrativeContact"]["country"]
            except:
                ptext='No State Given'
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            try:
                ptext='Country Code - ' + target_result["WhoisRecord"]["administrativeContact"]["countryCode"]
            except:
                ptext='No country Code given'
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            ptext='Technical Contact'
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            try:
                ptext='Organisation - ' + target_result["WhoisRecord"]["technicalContact"]["organization"]
            except:
                ptext='Organisation Not found'
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            try:
                ptext='State - ' + target_result["WhoisRecord"]["technicalContact"]["state"]
            except:
                ptext='No State given'
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            try:
                ptext='Country - ' + target_result["WhoisRecord"]["technicalContact"]["country"]
            except:
                ptext='No State Given'
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            try:
                ptext='Country Code - ' + target_result["WhoisRecord"]["technicalContact"]["countryCode"]
            except:
                ptext='No country Code given'
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            ptext='Name Servers:'
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            try:
                ptext=target_result["WhoisRecord"]["nameServers"]["rawText"]
            except:
                ptext='No Name Servers found'
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            try:
                ptext="Statuses: " + target_result["WhoisRecord"]["nameServers"]["status"]
            except:
                ptext='No Status found'
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))

    def command_Writer(self,target_info,target_result,target_type):
        if target_type == "nmap":
            #Converting nmap results into pdf friendly strings
            nmap_result = str(target_result)
            nmap_result = nmap_result.replace("{"," ")
            nmap_result = nmap_result.replace("}"," ")
            nmap_result = nmap_result.replace("'","  ")

            nmap_result = nmap_result.split(", ",-1)
            nmap_Address=nmap_result[0]
            nmap_Hosts=nmap_result[2]
            self.scout_Story.append(Spacer(1, 5))
            ptext='NMAP Results:'
            self.scout_Story.append(Paragraph(ptext, self.styles["Title"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext=nmap_Address
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            ptext=nmap_Hosts
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
            for x in range(23):
                try:
                    nmap_port=nmap_Hosts=nmap_result[(x+3)]
                except:
                    logging.info("Nmap results finished")
                    break
                else:
                    nmap_port=nmap_Hosts=nmap_result[(x+3)]
                    ptext=nmap_port
                    if 'state' in ptext:
                        self.scout_Story.append(Paragraph(ptext, self.styles["Heading3"]))
                        self.scout_Story.append(Spacer(1, 1))
                    else:
                        self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
                        self.scout_Story.append(Spacer(1, 1))
            
    def identity_Writer(self,target_info,target_result,target_type):
        #Coordinate Writer
        if target_type == "cords":
            self.scout_Story.append(Spacer(1, 5))
            ptext='Coordinates:'
            self.scout_Story.append(Paragraph(ptext, self.styles["Heading2"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext='Given Cords: ' + target_info.Coordinates
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext='Reversed Cords:'
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext=str(target_result["location"])
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext="URL For map location"
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext=target_result["URL"]
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 2))
        #Name Scrapper Writer 
        if target_type == "name":
            self.scout_Story.append(Spacer(1, 5))
            ptext='Name:'
            self.scout_Story.append(Paragraph(ptext, self.styles["Heading2"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext='Given Name:' + target_info.Target_Full_Name
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext='URL for people searchers (Most people searchers forbid automated tools)'
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 3))
            ptext=target_result["anywhoURL"]
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 1))
        #Telephone writer
        if target_type == "telephone":
            self.scout_Story.append(Spacer(1, 5))
            ptext='Telephone results:'
            self.scout_Story.append(Paragraph(ptext, self.styles["Heading2"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext=target_result
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 2))
        if target_type == "VIN":
            self.scout_Story.append(Spacer(1, 5))
            ptext='VIN results:'
            self.scout_Story.append(Paragraph(ptext, self.styles["Heading2"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext=target_result
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 2))
        if target_type == "dating":
            self.scout_Story.append(Spacer(1, 5))
            ptext='Dating username results:'
            self.scout_Story.append(Paragraph(ptext, self.styles["Heading2"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext=target_result
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 2))
        else:
            pass
    
    def misc_Writer(self,target_info,target_result,target_type):
        if target_type == "image":
            self.scout_Story.append(Spacer(1, 5))
            ptext='Image results:'
            self.scout_Story.append(Paragraph(ptext, self.styles["Heading2"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext=target_result
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 2))
        if target_type == "video":
            self.scout_Story.append(Spacer(1, 5))
            ptext='Video results:'
            self.scout_Story.append(Paragraph(ptext, self.styles["Heading2"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext=target_result
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 2))
        if target_type == "Webcam":
            self.scout_Story.append(Spacer(1, 5))
            ptext='Webcam results:'
            self.scout_Story.append(Paragraph(ptext, self.styles["Heading2"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext=target_result
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 2))
        if target_type == "Document":
            self.scout_Story.append(Spacer(1, 5))
            ptext='Document results:'
            self.scout_Story.append(Paragraph(ptext, self.styles["Heading2"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext=target_result
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 2))

    def social_Writer(self,target_info,target_result,target_type):
        if target_type == "Facebook":
            self.scout_Story.append(Spacer(1, 5))
            ptext='Facebook results:'
            self.scout_Story.append(Paragraph(ptext, self.styles["Heading2"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext=target_result
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 2))
        if target_type == "Twitter":
            self.scout_Story.append(Spacer(1, 5))
            ptext='Twitter results:'
            self.scout_Story.append(Paragraph(ptext, self.styles["Heading2"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext=target_result
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 2))
        if target_type == "Reddit":
            self.scout_Story.append(Spacer(1, 5))
            ptext='Reddit results:'
            self.scout_Story.append(Paragraph(ptext, self.styles["Heading2"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext=target_result
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 2))
        if target_type == "Other":
            self.scout_Story.append(Spacer(1, 5))
            ptext='Other social Media results:'
            self.scout_Story.append(Paragraph(ptext, self.styles["Heading2"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext=target_result
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 2))
        if target_type == "Snapchat":
            self.scout_Story.append(Spacer(1, 5))
            ptext='Snapchat results:'
            self.scout_Story.append(Paragraph(ptext, self.styles["Heading2"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext=target_result
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 2))
        if target_type == "LinkedIn":
            self.scout_Story.append(Spacer(1, 5))
            ptext='LinkedIn results:'
            self.scout_Story.append(Paragraph(ptext, self.styles["Heading2"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext=target_result
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 2))
        if target_type == "Kik":
            self.scout_Story.append(Spacer(1, 5))
            ptext='Kik results:'
            self.scout_Story.append(Paragraph(ptext, self.styles["Heading2"]))
            self.scout_Story.append(Spacer(1, 2))
            ptext=target_result
            self.scout_Story.append(Paragraph(ptext, self.styles["Normal"]))
            self.scout_Story.append(Spacer(1, 2))

##################### OSINT CLASSES  ##############################
class class_target_Functions():
    def __init__(self):
        logging.info("Function classes initlizated")

class class_target_Network_Functions(class_target_Functions):
    #Uses the whoisXML Api Data request https://main.whoisxmlapi.com/
    def whoIS(target_Network, scout_Report):
    # ZMiMtxcy6k769DiN03DDyUO4SfQR API key example
        # Uses the whoisXML Api Data request https://main.whoisxmlapi.com/
        #Logging info
        logging.info('Domain: %s', target_Network)
        logging.info('IP: %s', target_Network.IP)
        #Checks to see if Domain is given
        if (target_Network.Domain) == '':
            logging.info('No Domain Given')
            return 
        #If a Domain is given
        else:
            # Ensures that the domain doesn't include any escape characters that could potentially interfere with the web-requests
            target_Network.Domain = target_Network.Domain.strip(" '\n")
            # Performs a WHOIS web-requests
            whoIS_response = reqs.get('https://www.whoisxmlapi.com/whoisserver/WhoisService?&domainName='+target_Network.Domain+'&apiKey=at_ZMiMtxcy6k769DiN03DDyUO4SfQRo' + '&outputFormat=JSON')  
            # Loads the response into a json object
            website_errored="false"
            for x in range(51):  # Checks all ERROR status codes, potentially turn this into a function
                if whoIS_response.status_code == ("4" + str(x)):
                    website_errored="true"
                else:
                    pass
            if website_errored == "false":
                logging.info("whoIS successful")
                try:
                    target_Network_whoIS = json.loads(whoIS_response.content)
                    jsontest=target_Network_whoIS["WhoisRecord"]["createdDate"]
                except:
                    logging.info("Website gave no valid response, No WHOIS report given")
                    return
                else:
                    target_Network_whoIS = json.loads(whoIS_response.content)
                    scout_Report.network_Writer(target_Network,target_Network_whoIS,'whoIS')
            else:
                logging.info("Website gave error status code, No WHOIS report given")
                return

class class_target_Social_Functions(class_target_Functions):
    def facebookScraper(target_Social, scout_Report):
        logging.info("Facebook scrapper not implemented")
        if (target_Social.Facebook != 'none'):
            target_results = "Not Implemented"
            scout_Report.social_Writer(target_Social, target_results,"Facebook")
        else:
            pass
    def twitterScraper(target_Social, scout_Report):
        logging.info("Twitter scrapper not implemented")
        if (target_Social.Twitter != 'none'):
            target_results = "Not Implemented"
            scout_Report.social_Writer(target_Social, target_results,"Twitter")
        else:
            pass
    
    def redditScraper(target_Social, scout_Report):
        logging.info("reddit scrapper not implemented")
        if (target_Social.Reddit != 'none'):
            target_results = "Not Implemented"
            scout_Report.social_Writer(target_Social, target_results,"Reddit")
        else:
            pass
    
    def linkedInScraper(target_Social, scout_Report):
        logging.info("linkedIn scrapper not implemented")
        if (target_Social.LinkedIn != 'none'):
            target_results = "Not Implemented"
            scout_Report.social_Writer(target_Social, target_results,"LinkedIn")
        else:
            pass
    def other_social_mediaScraper(target_Social, scout_Report):
        logging.info("Other social Media scrapper not implemented")
        if (target_Social.Other_social_Media != 'none'):
            target_results = "Not Implemented"
            scout_Report.social_Writer(target_Social, target_results,"Other")
        else:
            pass

    def skypeScraper(target_Social, scout_Report):
        logging.info("linkedIn scrapper not implemented")
        if (target_Social.Skype != 'none'):
            target_results = "Not Implemented"
            scout_Report.social_Writer(target_Social, target_results,"Skype")
        else:
            pass
    
    def snapchatScraper(target_Social, scout_Report):
        logging.info("Snap chat scrapper scrapper not implemented")
        if (target_Social.Snapchat != 'none'):
            target_results = "Not Implemented"
            scout_Report.social_Writer(target_Social, target_results,"Snapchat")
        else:
            pass

    def kikScraper(target_Social, scout_Report):
        logging.info("Kik scrapper not implemented")
        if (target_Social.Kik != 'none'):
            target_results = "Not Implemented"
            scout_Report.social_Writer(target_Social, target_results,"Kik")
        else:
            pass

class class_target_Identity_Functions(class_target_Functions):
    def full_name_Scraper(target_identity, scout_Report):
        if (target_identity.Target_Full_Name != 'none'):
            #Finding full name from anywho people
            logging.info("Full Name Checker")
            name = str(target_identity.Target_Full_Name).split(",")
            first_name = name[0]
            last_name = name[1]
            first_name = first_name.strip(" ")
            last_name = last_name.strip(" ")
            anywhoURL = "https://www.anywho/people/"+first_name+"+"+last_name+"/"
            target_result={"anywhoURL":anywhoURL}
            scout_Report.identity_Writer(target_identity, target_result, "name")
            #Open Search People (running into issues currently)
            #scout_Report.identity_Writer(target_identity,target_result, "name")
            #logging.info("Running name through openpeoplesearch")
            #openpeoplesearchurl= 'curl -X POST "https://api.openpeoplesearch.com/api/v1/User/authenticate" -H  "accept: */*" -H  "Content-Type: application/json" -d "{\"username\":visceralsec@gmail.com\",\"password\":\"N99n7dB3Ajki22P\"}"'
            #openpeoplesearchurl = openpeoplesearchurl.strip()
            #print(type(openpeoplesearchurl))
            #open_Return_unsplit = subprocess.run([openpeoplesearchurl], shell=True, capture_output=True)
            #ope_Return=nmap_Return_unsplit.stderr.splitlines()
            # API is not supported          
            #findmypast_response = reqs.get('http://api.findmypast.com/search/category/count?$filter=LastName eq' + last_name +' and FirstName eq' + first_name)
            # Loads the response into a json object

        else:
            pass

    def dating_user_nameScraper(target_Identity, scout_Report):
        logging.info("dating user name api not currently implemented, posting URLs")
        if (target_Identity.Dating_User_Name != 'none'):
            target_results = "Not Implemented"
            scout_Report.identity_Writer(target_Identity, target_results,"dating")
        else:
            pass
    
    def target_telephone_numberScraper(target_Identity, scout_Report):
        logging.info("telephone scrapper api not currently implemented, posting URLs")
        if (target_Identity.Target_Telephone_Number != 'none'):
            target_results = "Not Implemented"
            scout_Report.identity_Writer(target_Identity, target_results,"telephone")
        else:
            pass
    def VINScraper(target_Identity, scout_Report):
        logging.info("VIN scrapper api not currently implemented, posting URLs")
        if (target_Identity.VIN != 'none'):
            target_results = "Not Implemented"
            scout_Report.identity_Writer(target_Identity, target_results,"VIN")
        else:
            pass
    
    def CoordinatesScraper(target_Identity, scout_Report):
        if (target_Identity.Coordinates != 'none'):
            logging.info("Starting cordinate scrapper")
            xy = str(target_Identity.Coordinates).split(",")
            x = xy[0]
            y = xy[1]
            strcords = str(x) + ',' + str(y)
            geolocator = Nominatim(user_agent="Scout")
            target_location = geolocator.reverse(strcords)
            target_URI = ("https://maps.google.com/?q=" +x+","+y)
            target_results = {"location": target_location, "URL": target_URI}
            scout_Report.identity_Writer(target_Identity,target_results,"cords")
        else:
            pass

class class_target_Misc_Functions(class_target_Functions):
    def target_image_Function(target_Misc, scout_Report):
        logging.info("Image function not implemented")
        if (target_Misc.Image != 'none'):
            logging.info("Target Image Function Called ")
            target_results = "Not Implemented"
            scout_Report.misc_Writer(target_Misc, target_results,"image")
        else:
            pass
    def target_video_Function(target_Misc, scout_Report):
        logging.info("Video function not implemented")
        if (target_Misc.Videos != 'none'):
            logging.info("Target video Function Called ")
            target_results = "Not Implemented"
            scout_Report.misc_Writer(target_Misc, target_results,"video")
        else:
            pass
    def target_webcams_Funciton(target_Misc, scout_Report):
        logging.info("Webcam function not implemented")
        if (target_Misc.Webcams != 'none'):
            logging.info("Target webcam Function Called ")
            target_results = "Not Implemented"
            scout_Report.misc_Writer(target_Misc, target_results,"webcam")
        else:
            pass
    def target_document_Function(target_Misc, scout_Report):
        logging.info("Document functons not implemented")
        if (target_Misc.Documents != 'none'):
            logging.info("Target Document Function Called ")
            target_results = "Not Implemented"
            scout_Report.misc_Writer(target_Misc, target_results,"Document")
        else:
            pass


class class_target_Commands_Functions(class_target_Functions):
    def target_nmap(target_commands,target_network, scout_Report):
        if (target_commands.nmap == 'true'):
            logging.info("Nmap module called")
            #nmap using commandline rather than a library
            #print(target_network.IP)
            #nmap_Return_unsplit = (subprocess.run(["nmap","127.0.0.1"], capture_output=True))
            #nmap_Return= nmap_Return_unsplit.stderr.splitlines()
            #print(nmap_Return)
            scout_nmap = nmap.PortScanner()
            scout_range = scout_nmap.scan(hosts=target_network.IP)
            target_result=scout_range['scan']
            scout_Report.command_Writer(target_network,target_result,'nmap')
        else:
            pass


#
# MAIN

#

#if __name__ == "__scout_launch__":

scout_launch(sys.argv[1:])


