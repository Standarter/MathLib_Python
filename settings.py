import os.path
import os
from pprint import pprint
class ProgramSettings:
    settingsFile = "data/settings.txt"
    settings = {}
    def __init__(self, mode = "default"):
        if os.path.exists(self.settingsFile):
            settingsFile = open(self.settingsFile, "r")
            settings = settingsFile.readlines()
            for setting in settings:
                if setting[0] != "#":
                    key = setting.replace(" ", "").replace("\n", "").split("=")[0]
                    value = setting.replace(" ", "").replace("\n", "").split("=")[1]
                    self.settings[key] = value
            settingsFile.close()
        else:
            settingsFile = open(self.settingsFile, "w")
            settingsFile.write("# Types: (Float, Decimal)" + "\n")
            settingsFile.write("NumberType = Decimal" + "\n")
            settingsFile.write("# Trigonometry method's" + "\n")
            settingsFile.write("# 1) math" + "\n")
            settingsFile.write("# 2) numpy" + "\n")
            settingsFile.write("# 3) taylor" + "\n")
            settingsFile.write("TrigMethod = math" + "\n")
            settingsFile.write("# Functions round to N numbers after dot" + "\n")
            settingsFile.write("FunctionsRoundTo = 5" + "\n")
            settingsFile.write("# Factorial method's" + "\n")
            settingsFile.write("# 1) standart" + "\n")
            settingsFile.write("# 2) math" + "\n")
            settingsFile.write("# 3) stirling" + "\n")
            settingsFile.write("FactorialMethod = standart" + "\n")
            settingsFile.write("# Log method's" + "\n")
            settingsFile.write("# 1) standart" + "\n")
            settingsFile.write("LogMethod = standart" + "\n")
            settingsFile.write("# Do logs?" + "\n")
            settingsFile.write("Logs = false" + "\n")
            settingsFile.write("LoggingLevel = 1" + "\n")
            settingsFile.close()
            self.__init__()
Settings = ProgramSettings()
Settings = Settings.settings
RoundTo = int(Settings["FunctionsRoundTo"])
