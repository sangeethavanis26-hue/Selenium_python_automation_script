# # Licensed to the Software Freedom Conservancy (SFC) under one
# # or more contributor license agreements.  See the NOTICE file
# # distributed with this work for additional information
# # regarding copyright ownership.  The SFC licenses this file
# # to you under the Apache License, Version 2.0 (the
# # "License"); you may not use this file except in compliance
# # with the License.  You may obtain a copy of the License at
# #
# #   http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing,
# # software distributed under the License is distributed on an
# # "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# # KIND, either express or implied.  See the License for the
# # specific language governing permissions and limitations
# # under the License.
#
# from selenium.webdriver.chromium.webdriver import ChromiumDriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import webDriverWait
# # from .options import Options
# # from .service import Service
#
#
# class WebDriver(ChromiumDriver):
#     """Controls the ChromeDriver and allows you to drive the browser."""
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.initial_window = self.driver.windows_handles
#         self.wait = webdriverWait(self.driver, 30)
#         self.driver.maximize_window()
#         # options: Options = None,
#         # service: Service = None,
#         # keep_alive: bool = True,
#
#         # -> None:
#         """Creates a new instance of the chrome driver. Starts the service and
#         then creates new instance of chrome driver.
#
#         :Args:
#          - options - this takes an instance of ChromeOptions
#          - service - Service object for handling the browser driver if you need to pass extra details
#          - keep_alive - Whether to configure ChromeRemoteConnection to use HTTP keep-alive.
#         """
#         # service = service if service else Service()
#         # options = options if options else Options()
#
#         super().__init__(
#             browser_name=DesiredCapabilities.CHROME["browserName"],
#             vendor_prefix="goog",
#             # options=options,
#             # service=service,
#             # keep_alive=keep_alive,
#         )
#
#     def wait_until_element_present(self, identifier_type, element_identifier):
#         if identifier_type.upper() == 'XPATH':
#             self.wait_until(ec.visibility_of_element_locators((By.XPATH, element_identifier)))
#         elif identifier_type.upper() == 'ID':
#             self.wait_until(ec.visibility_of_element_locators((By.XPATH, element_identifier)))
#         elif identifier_type.upper() == 'NAME':
#             self.wait_until(ec.visibility_of_element_locators((By.XPATH, element_identifier)))
#         elif identifier_type.upper() == 'LINK':
#             self.wait_until(ec.visibility_of_element_locators((By.XPATH, element_identifier)))
