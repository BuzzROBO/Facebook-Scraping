from waitress import serve
import falcon
from falcon_cors import CORS
import os
from time import sleep
from selenium import webdriver
import csv
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.service import Service
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import csv
import sys, os
import traceback
import datetime
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
import time
from fetch_info import scrap





cors = CORS(allow_all_origins=True, allow_all_headers=True, allow_credentials_all_origins=True, allow_all_methods=True)



class startscrap:
    _required_params = ["id","pass","key","type","scrl","num","msg"]
    _dot_string = '-----'
    dir = os.path.dirname(__file__)

    def _handleQuery(self, provided_params):
        _required_params = self._required_params
        # Checking whether we are getting all the required parameters. Incomplete parameters will result in an error
        all_params_provided = all([False if param not in provided_params else True for param in _required_params])
        # If we are not getting all the parameters, we gracefully exit with an error statement
        if not all_params_provided:
            return {'Error': 'Missing Parameter. Make Sure all parameters are present. Valid parameters are '
                             '{0}'.format(', '.join(_required_params))}
        idd = provided_params['id'] if provided_params['id'] else None
        pas = provided_params['pass'] if provided_params['pass'] else None
        keyy = provided_params['key'] if provided_params['key'] else None
        typee = provided_params['type'] if provided_params['type'] else None
        scrll = provided_params['scrl'] if provided_params['scrl'] else None
        num = provided_params['num'] if provided_params['num'] else 10
        msgg = provided_params['msg'] if provided_params['msg'] else None

        print(idd,pas,keyy,typee,scrll,num,msgg)
        scrap(idd,pas,keyy,typee,scrll,num,msgg)
        return "Finished"
        

    def on_get(self, req, resp):
        params = req.params
        resp.media = self._handleQuery(params)

    def on_post(self, req, resp):
        params = req.media
        resp.media = self._handleQuery(params)


if __name__ == '__main__':
    api = falcon.API(middleware=[cors.middleware])
    api.add_route('/start', startscrap())
    serve(api, host='localhost', port=8050)
