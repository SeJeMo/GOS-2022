from configparser import ConfigParser()


def readConf(conf: str, sections: str) -> dict:
    parseObj = ConfigParser()
    parseObj.read(conf)
    databaseOpts = {}
    if parseObj.has_section(sections):
        confData = parseObj.items(sections)
        for d in confData:
            databaseOpts[d[0]] = d[1]
        return databaseOpts





