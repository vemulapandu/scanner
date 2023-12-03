# class Weather:
#     pass

from libsast import Scanner
import os

options = {
    # 'match_rules': r"/home/iot-lab/Desktop/Mallik/mobsfscan/mobsfscan/rules/patterns/android",
    # 'sgrep_rules': r"/home/iot-lab/Desktop/Mallik/mobsfscan/mobsfscan/rules/semgrep",
    'match_rules': os.path.join(os.path.dirname(__file__), "../vulunerabilities/patterns"),
    # 'sgrep_rules': os.path.join(os.path.dirname(__file__), "../vulunerabilities/sgrep"),
    # 'sgrep_extensions': {".java"},
    'match_extensions': {".java"},
    'ignore_filenames': {".DS_Store"},
    'ignore_extensions': {".apk", ".zip", ".ipa"},
    "ignore_paths": {"__MACOSX", "fixtures", "spec", ".git", ".svn"}
}

paths = [r"/home/iot-lab/Desktop/Mallik/test"]
# paths = [r"/home/iot-lab/Desktop/Mallik/com.imangi.templerun_v1.23.5-66_Android-4.4"]

scanner = Scanner(options, paths)

results = scanner.scan()

print(results)