import os
import yaml
import re

class Checks:
    def isValid(self, path):
        dirs = os.listdir(path)
        if dirs == ['resources', 'sources']:
            return True
        else:
            return False
        
    # def scan(self, path):
    #     i = 0
    #     with open(os.path.join(os.path.dirname(__file__), "../weaknesses/warning.yml"), 'r') as file:
    #         info = yaml.safe_load(file)
    #     print(info)
    #     patterns = []
    #     for ii in info:
    #         print(ii)
    #         patterns.append(re.compile(ii['pattern']))
    #     # print(patterns)
    #     for root, dirs, files in os.walk(path):
    #         for file in files:
    #             if(file == "zzant.java"):
    #                 print(file)
    #             fileextenstion = os.path.splitext(file)[1]
    #             if fileextenstion == ".java":
    #                 self.scanfile(info, patterns, root + '/' + file)
    #                 # print(root,file)
    #                 i = i+1
    #     print(i)

    # def scanfile(self, info, patterns, file):
    #     for i, line in enumerate(open(file, encoding="utf8")):
    #         if("zzant.java" in file and i == 22):
    #             print(line)
    #             for k in re.finditer(r"new ObjectInputStream(...)", line):
    #                 print("Hello",k.group())
    #         for j in range (len(patterns)):
    #             for match in re.finditer(patterns[j], line):
    #                 print('Found on line %s: %s' % (i+1, match.group()))

    def scan(self, path):
        with open(os.path.join(os.path.dirname(__file__), "../weaknesses/warning.yml"), 'r') as file:
            warnings = yaml.safe_load(file)
        with open(os.path.join(os.path.dirname(__file__), "../weaknesses/info.yml"), 'r') as file:
            infos = yaml.safe_load(file)
        with open(os.path.join(os.path.dirname(__file__), "../weaknesses/error.yml"), 'r') as file:
            errors = yaml.safe_load(file)
        for warning in warnings:
            warning["pattern"] = re.compile(warning["pattern"])
        for error in errors:
            error["pattern"] = re.compile(error["pattern"])
        for info in infos:
            info["pattern"] = re.compile(info["pattern"])
        
        for root, dirs, files in os.walk(path):
            for file in files:
                fileextenstion = os.path.splitext(file)[1]
                if fileextenstion == ".java":
                    self.scanfile(warnings, infos, errors, root + '/' + file)
    
    def scanfile(self, warnings, infos, errors, file):
        for i, line in enumerate(open(file, encoding="utf8")):
            for warning in warnings:
                for match in re.finditer(warning["pattern"], line):
                    obj = {
                        "id":warning["id"],
                        "description": warning["message"],
                        "match_line": "Found on line " + str(i+1) + " , " + str(match.group()),
                        "severity": warning["severity"],
                        "cwe": warning["cwe"]
                    }
                    print(obj)
            
            for error in errors:
                # if("SafeDKWebAppInterface.java" in file and i == 147):
                #     print(line, error["pattern"])
                for match in re.finditer(error["pattern"], line):
                    obj = {
                        "id":error["id"],
                        "description": error["message"],
                        "match_line": "Found on line " + str(i+1) + " , " + str(match.group()),
                        "severity": error["severity"],
                        "cwe": error["cwe"]
                    }
                    print(obj)
            
            for info in infos:
                for match in re.finditer(info["pattern"], line):
                    obj = {
                        "id":info["id"],
                        "description": info["message"],
                        "match_line": "Found on line " + str(i+1) + " , " + str(match.group()),
                        "severity": info["severity"],
                        "cwe": info["cwe"]
                    }
                    print(obj)