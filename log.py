from settings import Settings
def log(status, string, level=1):
    if Settings["Logs"] == "true" and level <= int(Settings["LoggingLevel"]):
        print("# ({0}): {1}".format(status, string))