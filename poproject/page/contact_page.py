from page.base_func import BaseFunc


class ContactPage(BaseFunc):
    adddepart1 = '.member_colLeft_top_addBtnWrap.js_create_dropdown'
    adddepart2 = '.js_create_party'
    departtext = '.qui_inputText.ww_inputText[name="name"]'
    choicecon = '.qui_btn.ww_btn.ww_btn_Dropdown.js_toggle_party_list'
    contactid = '.qui_dialog_body.ww_dialog_body [id="1688850949858056_anchor"]'
    confire = '.qui_dialog_foot.ww_dialog_foot>a:nth-child(1)'

    def goto_add_member(self):
        pass
    def goto_add_contact(self):
        pass
    def add_depart(self):
        self.find(self.adddepart1).click()
        self.find(self.adddepart2).click()
        self.find(self.departtext).send_keys('牛哥的UI设计部')
        self.find(self.choicecon).click()
        self.find(self.contactid).click()
        self.find(self.confire).click()
        return ContactPage(self.driver)
    def get_list_member(self,name):
        ele_list_member = self.driver.find_elements_by_css_selector('.member_colRight_memberTable_td:nth-child(2)')
        list_member = [i.text for i in ele_list_member]
        # for i in ele_list_member:
        #     list_member.append(i.text)
        print(list_member)
        return list_member
    def get_list_depart(self):
        self.driver.find_element_by_css_selector('.jstree-node.js_editable.jstree-last.jstree-open').click()
        ele_list_depart = self.driver.find_elements_by_css_selector(".jstree-anchor")
        list_member = [i.text for i in ele_list_depart]
        print(list_member)
        return list_member