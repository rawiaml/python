  import  jpype     
  import  asposecells
  import wget
     
  url = "https://github.com/cdufour/ingesys-unix-script/blob/main/python/tps/tp3/flags/flags.zip"
  wget.download(url, 'C:/Users/A2M TRANSPORT/python/scripts/')
  jpype.startJVM() 
  from asposecells.api import Workbook
  
  # load CSV file
  workbook = Workbook("input.csv");
  
  # save as TXT
  workbook.save("Output.txt");
  
  jpype.shutdownJVM()
