from settings import Settings
def log(status, string, level=1):
    if Settings["Logs"] == "true" and level <= int(Settings["LoggingLevel"]):
        print("# ({0}): {1}".format(status, string))
def error(status, string):
    print("! ({0}): {1}".format(status, string))
def message(string):
    print("$ (message): {1}".format(string))