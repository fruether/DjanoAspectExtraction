import sys
sys.path.append("../../../../")
from library.Rules import BaseRule

class Test2_(BaseRule.Rule):
    def check_directory(self, type, filepath, diff, content):
        return None

    def check_filename(self, type, filepath, diff, content):
       # if Filename.match_filename("Admin.py", filepath):
       #     return len(Diff.get_modified_lines(diff))
        return 15

    def check_content(self, type, filepath, diff, content):
        return None

    def check_parse_tree(self, type, filepath, diff, content):
        #return ParseTree.match_baseclass("admin.ModelAdmin", content, diff)
        return 33

    def get_skill_string(self):
        return "Model/Data"

    def __init__(self):
        super(Test2_, self).__init__(["filename", "parse_tree"], False,["A", "E"])


def test():
    return Test2_()