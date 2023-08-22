import logging
from playwright.sync_api import sync_playwright

from talenta_clockin import config

class SesssionIDNotFound(Exception):
    pass

def get_sessionid(username:str, password:str):
    with sync_playwright() as pwr:
        logging.info('Launching browser')
        browser = pwr.chromium.launch()

        logging.info('Creating new page')
        page = browser.new_page()

        logging.info(f'Navigating to login page : {config.TALENTA_LOGIN_URL}')
        page.goto(config.TALENTA_LOGIN_URL)

        logging.info('Filling login form')
        #find user_email input by id
        page.fill('#user_email', username)

        #find user_password input by id
        page.fill('#user_password', password)

        logging.info('Clicking sign in button')
        #click sign in button find by id new-signin-button
        page.click('#new-signin-button')

        logging.info('Waiting for page to load')
        #wait for page to load
        page.wait_for_load_state('domcontentloaded')

        logging.info('Getting PHPSESSID')
        cookies = page.context.cookies()
        #Filter out dict in cookies list that has name: PHPSESSID

        while len([cookie for cookie in cookies if cookie['name'] == 'PHPSESSID']) == 0:
            logging.info('PHPSESSID not found, waiting')
            page.wait_for_load_state('domcontentloaded')
            cookies = page.context.cookies()

        cookies = [cookie for cookie in cookies if cookie['name'] == 'PHPSESSID']

        if len(cookies) == 0:
            raise SesssionIDNotFound('Failed to get PHPSESSID')
        
        browser.close()

        return cookies[0]['value']