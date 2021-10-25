import os.path
import os
from pprint import pprint
class ProgramSettings:
    settingsFile = "data/settings.txt"
    settings = {}
    def SettingsInit(self, mode = "default"):
        if os.path.exists(self.settingsFile):
            settingsFile = open(self.settingsFile, "r")
            settings = settingsFile.readlines()
            for setting in settings:
                if setting[0] != "#":
                    key = setting.replace(" ", "").replace("\n", "").split("=")[0]
                    value = setting.replace(" ", "").replace("\n", "").split("=")[1]
                    self.settings[key] = value
            settingsFile.close()
        elif mode == "reset":
            settingsFile = open(self.settingsFile, "w")
            settingsFile.write("# Types: (Float, Decimal)" + "\n")
            settingsFile.write("NumberType = Decimal" + "\n")
            settingsFile.write("# Trigonometry method's" + "\n")
            settingsFile.write("# 1) math" + "\n")
            settingsFile.write("# 2) numpy" + "\n")
            settingsFile.write("# 3) taylor sum's" + "\n")
            settingsFile.write("TrigMethod = math" + "\n")
            settingsFile.write("FunctionsRoundTo = 5" + "\n")
            settingsFile.close()
            self.SettingsInit()
        else:
            settingsFile = open(self.settingsFile, "w")
            settingsFile.write("# Types: (Float, Decimal)" + "\n")
            settingsFile.write("NumberType = Decimal" + "\n")
            settingsFile.write("# Trigonometry method's" + "\n")
            settingsFile.write("# 1) math" + "\n")
            settingsFile.write("# 2) numpy" + "\n")
            settingsFile.write("# 3) taylor sum's" + "\n")
            settingsFile.write("TrigMethod = math" + "\n")
            settingsFile.write("FunctionsRoundTo = 5" + "\n")
            settingsFile.close()
            self.SettingsInit()
Settings = ProgramSettings()
Settings.SettingsInit()
Settings = Settings.settings
pprint(Settings, width=1)
