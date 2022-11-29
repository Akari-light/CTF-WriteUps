from selenium import webdriver
from twilio.rest import Client
from time import strftime, ctime

def notification(msg):
    account_sid = 'ACa2a5730cf28b4e09f8a674cecc9230dd'
    auth_token = '1d241ed747033eef7cb915a16404c84b'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=msg,
                        from_='+17175395560',
                        to='+6581611479'
                    )

def chrome_instance():
    url = 'https://fypj.sit.nyp.edu.sg/'
    check_in = ['08:25','08:26','08:27','08:28','08:29', '08:30']
    check_out = ['18:00', '18:01', '18:02', '18:03', '18:04', '18:05']
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)

    # Login to the portal
    driver.find_element('xpath','/html/body/div/div/div/div/div[2]/form/fieldset/div[2]/input').send_keys("201805Q")
    driver.find_element('xpath','/html/body/div/div/div/div/div[2]/form/fieldset/div[3]/input').send_keys("P@ssw0rd!123")
    driver.find_element('xpath','/html/body/div/div/div/div/div[2]/form/fieldset/div[6]/input[2]').click()

    driver.implicitly_wait(10)
    # Click "Student" Dropdown
    driver.find_element('xpath', '/html/body/form/div[3]/nav/div/div[2]/ul[1]/li[1]/a').click()
    # Click Sign In/Out page
    driver.find_element('xpath', '/html/body/form/div[3]/nav/div/div[2]/ul[1]/li[1]/ul/li[1]/a').click()

    # Sign In/Out
    driver.find_element('xpath', '/html/body/form/div[3]/div[2]/div[5]/div/div/div[4]/div[3]/input')

    if strftime('%H:%M') in check_in:
        notification("You have successfully checked into the FYPJ System at " + ctime())
    elif strftime('%H:%M') in check_out:
        notification("You have successfully checked out of the FYPJ System at " + ctime())

    return driver

if __name__ == '__main__':
    # driver = chrome_instance()
    notification("Testing Noti")

