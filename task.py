from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

        #TASK12
        #1. Launch browser
        #2. Navigate to url 'http://automationexercise.com'
        #3. Verify that home page is visible successfully
        #4. Click 'Products' button
        #5. Hover over first product and click 'Add to cart'
        #6. Click 'Continue Shopping' button
        #7. Hover over second product and click 'Add to cart'
        #8. Click 'View Cart' button
        #9. Verify both products are added to Cart
        #10. Verify their prices, quantity and total price

        #1. Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

        # WebDriverWait objesini tanımlayalım
wait = WebDriverWait(driver, 10)

        #2. Navigate to url 'http://automationexercise.com'
url="http://automationexercise.com"
driver.get(url)


        #3. Verify that home page is visible successfully
link = driver.current_url
print("Current URL : ", link)
baslik=driver.title
print("Page Title : ", baslik)
if "Automation Exercise" in baslik:
        print('Home Page is opened Successfully')

        #4. click "products" button 
driver.find_element(By.XPATH,"//a[@href='/products']").click();
driver.back()
driver.forward()

        #5. Hover over first product and click 'Add to cart'
        #6. Click 'Continue Shopping' button
        #7. Hover over second product and click 'Add to cart'

    #MOUSE otomasyonu için Action  kullanılmalıdır.
actions = ActionChains(driver)
actions.send_keys(Keys.PAGE_DOWN).perform() 
time.sleep(1)  

        # 1.Ürünü sepete ekle
product1_add_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-product-id='1']")))
actions.move_to_element(product1_add_button).perform()
product1_add_button.click()

        # 'Continue Shopping' butonuna tıkla className ile 
continue_shopping_button1 = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btn-block")))
continue_shopping_button1.click()

        # Bir sonraki ürünü sepete ekle
product2_add_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-product-id='2']")))
actions.move_to_element(product2_add_button).perform()
product2_add_button.click()

        # 'Continue Shopping' butonuna tıkla =text ile 
continue_shopping_button2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Continue Shopping']")))
continue_shopping_button2.click()

        # 8. Click 'View Cart' button =css selector ile 
cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/view_cart']")))
cart_button.click()

        #9. Verify both products are added to Cart
        #10. Verify their prices, quantity and total price
        
        # Ürünlerin ve diğer öğelerin XPath'lerini tanımlandım OOP bir framework kullanılıyorsa kolayca convert edilebilir.
product1_xpath = "//a[@href='/product_details/1']"
product2_xpath = "//a[@href='/product_details/2']"
price1_xpath = "(//td[@class='cart_price'])[1]"
price2_xpath = "(//td[@class='cart_price'])[2]"
quantity1_xpath = "(//td[@class='cart_quantity'])[1]"
quantity2_xpath = "(//td[@class='cart_quantity'])[2]"
total1_xpath = "(//td[@class='cart_total'])[1]"
total2_xpath = "(//td[@class='cart_total'])[2]"

        #her element locate'ine explicit wait eklenerek stable çalışması sağlanmaya çalışıldı
        # Ürünlerin varlığını doğrula
product1 = wait.until(EC.visibility_of_element_located((By.XPATH, product1_xpath)))
product2 = wait.until(EC.visibility_of_element_located((By.XPATH, product2_xpath)))
assert product1.is_displayed() and product2.is_displayed()

        # Fiyatların varlığını doğrula
price1 = wait.until(EC.visibility_of_element_located((By.XPATH, price1_xpath)))
price2 = wait.until(EC.visibility_of_element_located((By.XPATH, price2_xpath)))
assert price1.is_displayed() and price2.is_displayed()

        # Miktarların varlığını doğrula
quantity1 = wait.until(EC.visibility_of_element_located((By.XPATH, quantity1_xpath)))
quantity2 = wait.until(EC.visibility_of_element_located((By.XPATH, quantity2_xpath)))
assert quantity1.is_displayed() and quantity2.is_displayed()

        # Toplam tutarların varlığını doğrula
total1 = wait.until(EC.visibility_of_element_located((By.XPATH, total1_xpath)))
total2 = wait.until(EC.visibility_of_element_located((By.XPATH, total2_xpath)))
assert total1.is_displayed() and total2.is_displayed()

        #Toplam fiyat kontrolü
print(f"birinci ürün fiyatı {price1.text.split()[1]}")
print(f"ikinci ürün fiyatı {price2.text.split()[1]}")

fiyat1=int(price1.text.split()[1])
fiyat2=int(price2.text.split()[1])

toplam1=int(total1.text.split()[1])
toplam2=int(total2.text.split()[1])

miktar1=int(quantity1.text)
miktar2=int(quantity2.text)

#Lambda ile toplam fiyat kontrolü
check_operation = lambda toplam1, fiyat1, miktar1: "Başarılı" if fiyat1 * miktar1 == toplam1 else "Başarısız"
print(check_operation(toplam1, fiyat1, miktar1))

check_operation = lambda toplam2, fiyat2, miktar2: "Başarılı" if fiyat2 * miktar2 == toplam2 else "Başarısız"
print(check_operation(toplam2, fiyat2, miktar2))

print(f"birici ürün fiyatı:{fiyat1}, miktarı: {miktar1}, toplam olması gereken :{fiyat1*miktar1}, ekranda görülen :{toplam1}")
assert toplam1==(fiyat1*miktar1)
print(f"ikinci ürün fiyatı:{fiyat2}, miktarı: {miktar2}, toplam olması gereken :{fiyat2*miktar2}, ekranda görülen :{toplam2}")
assert toplam2==(fiyat2*miktar2)

print("Test başarıyla sonuçlandı.")

# WebDriver'ı kapat
#driver.quit()





