#�������������ҳ�桪����������#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Activity(BaseAction):
    # �ҳ��Ԫ��------------------------------------------------------------------------
    # ���˰�ť
    backBtn = By.ID, 'com.huiian.timing:id/activity_banner_back_arrow_iv'
    # Live�رհ�ť
    closeLive = By.ID, 'com.huiian.timing:id/iv_close'
    def click_back(self):
        self.click(self.backBtn)
    def click_closeLive(self):
        self.click(self.closeLive)
    def check_backBtn(self):
        return self.is_feature_exist(self.backBtn)
    def tapScreen(self,x,y):
        self.tapOperat(x,y)