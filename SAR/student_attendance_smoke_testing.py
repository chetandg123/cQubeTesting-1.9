import time
import unittest

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Data.parameters import Data
from SAR.Click_on_hyper_link_in_SAR import Hyperlink
from SAR.arg import arg
from SAR.check_cluster_per_block_csv_download import ClusterPerBlockCsvDownload
from SAR.check_districts_csv_download import DistrictCsvDownload
from SAR.check_dots_on_each_district_block import DotsOnDistrictsBlock
from SAR.check_dots_on_each_districts import DotsOnDistricts
from SAR.check_schools_per_cluster_csv_download import SchoolsPerClusterCsvDownload
from SAR.check_with_total_schools_in_SAR import TotalSchools
from SAR.check_with_total_student_in_SAR import TotalStudents
from SAR.click_on_Home_icon import Home
from SAR.click_on_SAR import DahboardSar
from SAR.click_on_SAR_and_logout import Logout
from SAR.click_on_blocks import Blocks
from SAR.click_on_clusters import Clusters
from SAR.click_on_dashboard import Dashboard
from SAR.click_on_schools import Schools
from SAR.cluster_level_comaparing_dots_with_no_of_schools import ClusterDotsWithNoOfSchools
from SAR.download_blockwise_csv import BlockwiseCsv
from SAR.download_clusterwise_csv import ClusterwiseCsv
from SAR.download_districtwise_csv import DistrictwiseCsv
from SAR.download_schoolwise_csv import SchoolwiseCsv
from reuse_func import GetData


class cQube_Student_Attendance(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        year = Select(self.driver.find_element_by_id(Data.sar_year))
        month = Select(self.driver.find_element_by_id(Data.sar_month))
        self.year = year.first_selected_option.text
        self.month = month.first_selected_option.text

    def test_click_on_student_attendence_report(self):
        sar = DahboardSar(self.driver)
        result = sar.click_on_sar()
        if "Student Attendance Report" in result:
            print("Student Attendance Report is Working")
        else:
            raise self.failureException("Student Attendance Report Is Not Working")

    def test_click_on_blocks(self):
        state = GetData()
        state.click_on_state(self.driver)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, Data.SAR_Blocks_btn))
        )
        try:
            element.click()
            time.sleep(5)
            print("Blocks Button is working")
        except WebDriverException:
            raise self.failureException("Blocks Button is not clickable")

    def test_click_on_clusters(self):
        state = GetData()
        state.click_on_state(self.driver)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, Data.SAR_Clusters_btn))
        )
        try:
            element.click()
            time.sleep(15)
            print("Cluster Button is working")
        except WebDriverException:
            raise self.failureException("Cluster Button is not working")

    def test_click_on_schools(self):
        state = GetData()
        state.click_on_state(self.driver)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, Data.SAR_Schools_btn))
        )
        try:
            element.click()
            time.sleep(30)
            print("Schools Button is working")
        except WebDriverException:
            raise self.failureException("Schools Button is not working")

    def test_logout(self):
        state = GetData()
        state.click_on_state(self.driver)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, Data.Logout))
        )
        try:
            element.click()
            print("Logout Button is working")
            self.data.login_cqube(self.driver)
            time.sleep(5)
        except WebDriverException:
            raise self.failureException("Logout Button is not working")

    def test_check_hyperlinks(self):
        hyperlinks = Hyperlink(self.driver)
        result1, result2, choose_dist = hyperlinks.click_on_hyperlinks()
        if result1 == False and result2 == False and choose_dist == "Choose a District ":
            print("hyperlinks are working")
        else:
            raise self.failureException("hyperlinks are not working")

    def test_select_year(self):
        state = GetData()
        state.click_on_state(self.driver)
        year = Select(self.driver.find_element_by_id(Data.sar_year))
        try:
            for x in range(1, len(year.options)):
                year.select_by_index(x)
                time.sleep(5)
            print("Select year is working")
        except WebDriverException:
            raise self.failureException("Select Year is not working")

    def test_select_month(self):
        state = GetData()
        state.click_on_state(self.driver)
        month = Select(self.driver.find_element_by_id(Data.sar_month))
        try:
            for x in range(1, len(month.options)):
                month.select_by_index(x)
                time.sleep(5)
            print("Select month is working")
        except WebDriverException:
            raise self.failureException("Select month is not working")

    def test_choose_district(self):
        state = GetData()
        state.click_on_state(self.driver)
        choose_district = Select(self.driver.find_element_by_id(Data.sar_district))
        try:
            for x in range(1, len(choose_district.options)):
                choose_district.select_by_index(x)
                time.sleep(2)
            print("Choose District is working")
        except WebDriverException:
            raise self.failureException("Choose District is not working")

    def test_choose_block(self):
        state = GetData()
        state.click_on_state(self.driver)
        choose_district = Select(self.driver.find_element_by_id(Data.sar_district))
        choose_block = Select(self.driver.find_element_by_id(Data.sar_block))

        try:
            for x in range(len(choose_district.options) - 1, len(choose_district.options)):
                choose_district.select_by_index(x)
                time.sleep(2)
                for y in range(len(choose_block.options) - 1, len(choose_block.options)):
                    choose_block.select_by_index(y)
                    time.sleep(2)
            print("Choose District and Block is working")
        except WebDriverException:
            raise self.failureException("Choose District and Block is not working")

    def test_choose_cluster(self):
        state = GetData()
        state.click_on_state(self.driver)
        choose_district = Select(self.driver.find_element_by_id(Data.sar_district))
        choose_block = Select(self.driver.find_element_by_id(Data.sar_block))
        choose_cluster = Select(self.driver.find_element_by_id(Data.sar_cluster))

        try:
            for x in range(len(choose_district.options) - 1, len(choose_district.options)):
                choose_district.select_by_index(x)
                time.sleep(2)
                for y in range(len(choose_block.options) - 1, len(choose_block.options)):
                    choose_block.select_by_index(y)
                    time.sleep(2)
                    for z in range(1, len(choose_cluster.options)):
                        choose_cluster.select_by_index(z)
                        time.sleep(2)
            print("Choose District,Block and Cluster is working")
        except WebDriverException:
            raise self.failureException("Choose District,Block and Cluster is not working")

    def test_home_icon(self):
        home = Home(self.driver)
        home.click_on_blocks_click_on_home_icon()
        result = home.click_HomeButton()
        if "Student Attendance Report" in result:
            print("Home Icon is Working")
        else:
            raise self.failureException('Home Icon is not working')

    def test_download(self):
        state = GetData()
        state.click_on_state(self.driver)
        element = self.driver.find_element_by_id(Data.sar_download)
        try:
            element.click()
            time.sleep(2)
            print("Download Button is working")
            time.sleep(5)
        except WebDriverException:
            raise self.failureException("Download Button is not working")

    def test_markers_on_map(self):
        state = GetData()
        state.click_on_state(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        if int(len(dots)-1) != 0:
            print('Markers are present on the map')
        else:
            raise self.failureException("Markers are not present on the map")

    def test_no_of_schools_is_equals_at_districts_blocks_clusters_schools(self):
        tc = TotalSchools(self.driver)
        schools, Bschools = tc.block_no_of_schools()
        self.assertEqual(int(schools), int(Bschools), msg="Block level no of schools are not equal to no of schools ")
        schools, Cschools = tc.cluster_no_of_schools()
        self.assertEqual(int(schools), int(Cschools), msg="Cluster level no of schools are not equal to no of schools ")
        schools, Sschools = tc.schools_no_of_schools()
        self.assertEqual(int(schools), int(Sschools), msg="Cluster level no of schools are not equal to no of schools ")

    def test_total_no_of_students_is_equals_at_districts_blocks_clusters_schools(self):
        tc = TotalStudents(self.driver)
        student_count, Bstudents = tc.block_total_no_of_students()
        self.assertEqual(int(student_count), int(Bstudents), msg="Block level no of students are not equal")
        student_count, Cstudents = tc.cluster_total_no_of_students()
        self.assertEqual(int(student_count), int(Cstudents), msg="Cluster level no of students are not equal")
        student_count, Sstudents = tc.schools_total_no_of_students()
        self.assertEqual(int(student_count), int(Sstudents), msg="Cluster level no of students are not equal")


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()