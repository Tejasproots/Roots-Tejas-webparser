from fileinput import filename
import os
import re
import cv2
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

df =pd.read_csv(r"C:\Users\TejasP\local_code_repo\DigitialVisionWebparser\shopify.csv")
login_like_pages= []
login_like_pages= df['url'].tolist()
len(login_like_pages)


#PATH =(r"C:\Users\TejasP\OneDrive - Roots Automation, Inc\Documents\chromedriver.exe")
PATH =(r"C:\Users\TejasP\local_code_repo\DigitialVisionWebparser\chromedriver.exe")
driver = webdriver.Chrome(PATH)
#login_like_pages = ["https://houseofcharizma.myshopify.com"]

filename =[]
mappingno =[]
fileno = 0 
if __name__ == "__main__":

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    # optional; reduces amount of info logged to console
    #chrome_options.add_argument("--log-level=3")
    if os.path.isdir('digitalvisionwebparser/')== True:
        print("Directory Exist")
    else:
        os.makedirs('digitalvisionwebparser/')
    #driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    for k in range(len(login_like_pages)):
        driver.get(login_like_pages[k])
        driver.maximize_window()
        fileno = fileno+1
        filename.append(k)
        mappingno.append(fileno)
        img_str = driver.get_screenshot_as_png()

        img_str_arr = np.frombuffer(img_str, np.uint8)
        img = cv2.imdecode(img_str_arr, cv2.IMREAD_COLOR)

        # elements = driver.find_elements(by=By.CLASS_NAME, value="lnXdpd")

        values = ["input", "img", "select", "button","svg","a","span"]
        # radiobutton (<input type="radio">), checkbox (<input type="checkbox">), dateinput (<input type="date">)
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),(128, 255, 0),(0, 128, 0),(0, 0, 128)]
        mapping = {}
        boundingboxes = []
        mapping["input"]="Input"
        mapping["img"]="Image"
        mapping["select"]="Dropdown"
        mapping["button"]="Button"
        mapping["svg"]="Image"
        mapping["a"]="Text"
        mapping["span"]="Text"
        
        for j in range(len(values)):

            elements = driver.find_elements(by=By.TAG_NAME, value=values[j])

            for i in range(len(elements)):
                x1 = int(elements[i].rect['x'])
                y1 = int(elements[i].rect['y'])
                x2 = int(x1 + elements[i].rect['width'])
                y2 = int(y1 + elements[i].rect['height'])
                if x1==y1==x2==y2==0:
                    ...
                else:
                    boundingboxes.append({'x1': x1, 'x2': x2,'y1': y1, 'y2': y2}) 
                    cv2.rectangle(img, (x1, y1), (x2, y2), colors[j], 1)
                    cv2.putText(img,mapping[values[j]], (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36, 255, 12), 1)

        cv2.imwrite("digitalvisionwebparser/"+str(fileno)+'.png'.format(k), img)
        np.save("digitalvisionwebparser/"+str(fileno)+'.npy', boundingboxes)
driver.quit()

mapping= pd.DataFrame({'screenshotno':mappingno,
                  'numpyfileno':mappingno,
                  'urlname': filename
                  })
df.drop_duplicates()
#df.to_pickle((appname)+'.csv')
