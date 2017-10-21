
import sys
sys.path.append("../")


from library.Rules import BaseRule2
from library.Rules.Operations import Or
from library.Rules.Filters import FilenameFilter

class ConfRule_(BaseRule2.Rule):
    def __init__(self):
        ff1 = FilenameFilter.FilenameFilter("Settings.py", "")
        a = Or.Or(ff1, None)
        super(ConfRule_, self).__init__(a,["A", "M"])

    def get_skill_string(self):
        return "Other/DjangoConfiguration"


