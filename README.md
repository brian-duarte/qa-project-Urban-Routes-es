# 🚕 Automatización Web - Urban Routes

## 📋 Project Overview
  
This project focuses on automated user interface (UI) testing for the Urban Routes platform. The main objective was to validate the critical flow of requesting a taxi, ensuring that each step of the process, from route selection to driver assignment, works smoothly and without errors for the end user.

---

## 🎯 Project Impact
**Key Result:** A robust test suite was implemented using Selenium WebDriver and the Page Object Model (POM) design pattern. This approach enabled comprehensive coverage of the user flow, identifying areas for improvement in interface interaction and ensuring the stability of ride-hailing services.

---

## 🎥 Project Demonstration

https://github.com/user-attachments/assets/1242773d-60ae-43e3-9ab4-56cfa4e6d6be


---

## ✅ Key Activities

* **Page Object Model (POM) Implementation:** Project structuring by separating locators from test logic, which facilitates code maintenance and scalability.
  
*  **Full Flow Automation:** Step-by-step simulation of the user experience:

      **Entering origin and destination addresses.**
  
      **Selecting taxi categories (Comfort).**
  
      **Registering and validating phone numbers via SMS.**
  
      **Managing payment methods and comments for the driver.**
  
* **Advanced Selenium Techniques:** Application of WebDriverWait and expected_conditions to handle web page asynchrony, and JavaScript execution for complex interactions.
* **Efficient Resource Management:** Implementation of teardown methods to ensure proper browser closure and optimize system performance.

---

## 🛠️ Test Coverage


| Category | Tools / Techniques |
| --- | --- |
| Language | Python |
| Automation | Selenium WebDriver |
| Test Framework | pytest |
| Design Pattern | Page Object Model (POM) |
| Interactions | JavaScript Executor |
| Waits | WebDriverWait / EC |

---

## 📊 Test Results

| Status | Quantity | Percentage |
| --- | --- | --- |
| **Passed** | 5 | 55.6% |
| **Failed** | 4 | 44.4% |
| **Total** | **9** | **100%** |


### Findings Analysis

The execution identified that 55.6% of critical functionalities operate correctly under normal conditions. The detected failures serve as a roadmap for the development team, allowing them to prioritize fixes in specific UI elements and server response times.


