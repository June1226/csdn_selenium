from BeautifulReport import BeautifulReport
import unittest

if __name__ == '__main__':
    suite = unittest.TestLoader().discover("./testCases/", pattern="test_*.py")
    result = BeautifulReport(suite)
    result.verbosity = 2
    result.report(filename="report.html", description="拒绝内卷的小测试_测试报告", report_dir="./reports")