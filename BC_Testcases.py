class BC_Testcases (object):

    __url = " "

    def open(self):
        self._web.open(self.__url)

    def __init__(self, browser):
        self._web = Web(browser)

    def close(self):
        self._web.close_all()
