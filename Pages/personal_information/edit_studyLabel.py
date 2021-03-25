#�������������༭ѧϰ��ǩҳ������������#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Study_label(BaseAction):
    # ���˰�ť
    backBtn = By.ID,'com.huiian.timing:id/activity_banner_back_ll'
    # ��ɰ�ť
    finshBtn = By.ID,'com.huiian.timing:id/tv_enter_timing'
    # ɾ��ѧϰ��ǩ��ť
    deleteStudyLabel = By.ID,'com.huiian.timing:id/iv_close'
    # �п���ǩ
    zhongKaoLabel = By.XPATH,'//*[@text="�п�"]'
    # ���ఴť
    moreBtn = By.ID,'com.huiian.timing:id/tv_want_exam_more'
    #�Զ���ѧϰ��ǩ
    editLabelBtn = By.ID,'com.huiian.timing:id/tv_go_custom'
    #�Զ����ǩ�༭��
    editLabelBox = By.ID,'com.huiian.timing:id/et'
    #�Զ����ǩѡ��
    selectLabel = By.ID,'com.huiian.timing:id/recyclerview'

    def click_backBtn(self):
        self.click(self.backBtn)
    def click_finshBtn(self):
        self.click(self.finshBtn)
    def click_deleteStudyLabel(self):
        self.click(self.deleteStudyLabel)
    def click_zhongKaoLabel(self):
        self.click(self.zhongKaoLabel)
    def click_moreBtn(self):
        self.click(self.moreBtn)
    def click_editLabelBtn(self):
        self.click(self.editLabelBtn)
    def click_selectLabel(self):
        self.click(self.selectLabel)
    def tapScreen(self,x,y):
        self.tapOperat(x,y)
    def input_editLabelBox(self,context):
        self.input(self.editLabelBox,context)
