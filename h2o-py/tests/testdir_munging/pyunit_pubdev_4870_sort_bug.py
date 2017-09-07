from __future__ import print_function
import sys
sys.path.insert(1,"../../")
import h2o
from tests import pyunit_utils

def sort():
    df = h2o.import_file(pyunit_utils.locate("bigdata/laptop/jira/NEW_ORIGINAL.csv.zip"))
    df1 = df.sort([0, 5])
    print("wow")
    h2o.remove_all()

if __name__ == "__main__":
    pyunit_utils.standalone_test(sort)
else:
    sort()

