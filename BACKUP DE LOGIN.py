import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
from des_cap import get_des_cap
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Inicializa el driver con las Desired Capabilities
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", get_des_cap())
        cls.driver.implicitly_wait(10)  # Tiempo de espera implícito

    def test_login_with_microsoft(self):
        # 1. Presionar el botón "Iniciar sesión con Microsoft"
        try:
            login_button = self.driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='Iniciar sesión con Microsoft']")
            login_button.click()
            print("Botón de inicio de sesión presionado con éxito.")
        except Exception as e:
            self.fail(f"Error localizando o presionando el botón de inicio de sesión: {e}")

        # 2. Esperar a que el campo de correo esté presente y tenga foco
        try:
            email_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@class='android.widget.EditText' and @index='0']"))
            )
            email_field.click()  # Asegúrate de que el campo esté enfocado
            email_field.clear()  # Limpia el campo antes de enviar el texto
            email_field.send_keys('jhorivera@upt.pe')  # Reemplaza con tu correo de prueba
            print("Correo electrónico ingresado con éxito.")
        except Exception as e:
            self.fail(f"Error localizando o ingresando el correo electrónico: {e}")

        # 3. Presionar el botón "Next"
        try:
            next_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@text='Next']"))
            )
            next_button.click()
            print("Botón 'Next' presionado con éxito.")
        except Exception as e:
            self.fail(f"Error localizando o presionando el botón 'Next': {e}")

        # 4. Esperar a que el campo de contraseña esté presente y tenga foco
        try:
            password_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@index='0']"))
            )
            password_field.click()
            password_field.send_keys('dfhgdvh123456jN')  # Reemplaza con tu contraseña
            print("Contraseña ingresada con éxito.")





        except Exception as e:
            self.fail(f"Error localizando o ingresando la contraseña: {e}")

        # 5. Presionar el botón "Sign in"
        try:
            sign_in_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@text='Sign in']"))
            )
            sign_in_button.click()
            print("Botón 'Sign in' presionado con éxito.")
        except Exception as e:
            self.fail(f"Error localizando o presionando el botón 'Sign in': {e}")

        # 6. Esperar a que se complete el proceso de inicio de sesión
        time.sleep(5)

        """ # Verificar que se haya redirigido a la vista de bienvenida o al menú
        try:
            welcome_text = self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Bienvenido')]")
            self.assertTrue(welcome_text.is_displayed(), "No se encontró el texto de bienvenida después de iniciar sesión.")
            print("Inicio de sesión completado y redirigido con éxito.")
        except Exception as e:
            self.fail(f"Error verificando la vista de bienvenida después de iniciar sesión: {e}") """

    @classmethod
    def tearDownClass(cls):
        # Finaliza la sesión
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
