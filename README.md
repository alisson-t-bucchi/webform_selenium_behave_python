# Selenium Behave WebForm Test

This project implements automation tests for the [Selenium Web Form](https://www.selenium.dev/selenium/web/web-form.html) page using **Behave** (a BDD testing framework for Python), **Selenium WebDriver** and **Allure Reports** to create detailed performance reports.

## 📝 Objective

The goal of this project is to demonstrate how to use **Behave** and **Selenium WebDriver** to create and execute automated tests based on scenarios described in the Gherkin language.

## 🚀 Technologies Used

- [Python](https://www.python.org/) - Programming language
- [Behave](https://behave.readthedocs.io/) - Framework for Behavior-Driven Development (BDD)
- [Selenium WebDriver](https://www.selenium.dev/documentation/) - Browser automation
- [Gherkin](https://cucumber.io/docs/gherkin/) - Language for describing test scenarios

## 📂 Project Structure

The main code resides in the Behave step definition file, which connects the scenarios described in Gherkin files to Python code.

## 📝 Step File Organization
Here's the information organized in a **table format**:  

| **Feature File**                   | **Description of Scenarios**                          | **Step File**                 | **Step Definitions Purpose**                                                       |  
|------------------------------------|-------------------------------------------------------|-------------------------------|------------------------------------------------------------------------------------|  
| **webform_actions_part_1.feature** | Scenarios for text, password, and textarea inputs.    | **webform_actions_part_1.py** | Contains step definitions for handling input scenarios.                            |  
| **webform_actions_part_2.feature** | Scenarios for dropdown boxes.                         | **webform_actions_part_2.py** | Contains step definitions for handling dropdown scenarios.                         |  
| **webform_actions_part_3.feature** | Scenarios for file input, checkbox and radio buttons. | **webform_actions_part_3.py** | Contains step definitions for handling file input and buttons scenarios.           |  
| **webform_actions_part_4.feature** | Scenarios for color, date picker and range bar.       | **webform_actions_part_4.py** | Contains step definitions for handling color, date picker and range bar scenarios. |


It includes three main steps:

1. **Given:** Opens the web form page.
2. **When:** Enters text into the input field.
3. **Then:** Clicks the submit button.

```python
@given(u'the browser open Webform page')
@when(u'insert a information in the text input field')
@then(u'the submit button will be clicked')
```

## Example Gherkin Scenario
An example of how a scenario can be described in Gherkin in the features/form_test.feature file:

```gherkin
Feature: Test the Selenium Web Form

  Scenario: Fill and submit the form
    Given the browser open Webform page
    When insert a information in the text input field
    Then the submit button will be clicked
```

## Files project structure

```
webform_selenium_behave_python/
├── allure-reports/             # Directory for Allure reports
├── features/                   # Tests and automation logic
│   ├── pages/                  # Page Objects (Page Object Pattern)
│   ├── steps/                  # Step definitions (separated by part)
│   ├── *.feature               # Gherkin test scenarios
├── behave.ini                  # Behave configuration
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
```

## ⚙️ Installation and Setup
Follow these steps to set up and run the project:

1. Clone this repository:
```bash
git clone https://github.com/your-username/selenium-behave-webform.git
cd selenium-behave-webform
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```
Make sure the requirements.txt file includes the following dependencies:
```
behave
selenium
```

4. Install the WebDriver for your browser (e.g., ChromeDriver for Google Chrome). Ensure the driver is added to your system PATH.

## ▶️ Running the Tests
To run the tests, use the following command:
```bash
behave
```
This will execute all scenarios described in the .feature files within the features directory.

## 🗒️ Generating Allure Reports 
1. Install AlLure:
Allure can be installed in various ways. Choose the method that best fits your environment:

## Option 1: Use the Allure Commandline
Via Homebrew (macOS/Linux):
```bash
brew install allure
```

Via Chocolatey (Windows): 
First, install Chocolatey. Then:
```bash
choco install allure
```

Via Binary (manual):
Download the zip file from Allure Releases.
Extract the contents and add the binary directory to your PATH.

2. Install Allure plugin for Python:
Install the allure-behave package, which integrates Allure with Behave.
```bash
pip install allure-behave
```

3. Set up project for Allure
Make sure Behave test results are generated in a format compatible with Allure:
- Run Behave with the Allure Plugin: When running your Behave tests, include the -f allure_behave.formatter:AllureFormatter option to use the Allure format and -o allure-results to specify the output directory for the results.

Example:
```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results
```
-f: Specifies the report format.  

-o: Specifies the output directory. 

- Final Structure: After running the tests, Allure results will be saved in a directory called allure-results.

4. Generate HTML Report
Once the results are generated, use the Allure Commandline to create the report:

- Run the command to generate and view the report:

```bash
allure serve allure-results
``` 
This will open the report in your default browser. The report is served from a temporary local server.

- To create a static report:
```bash
allure generate allure-results -o allure-report
```
- allure-results: Directory containing the raw test results.
- allure-report: Directory where the HTML report will be saved.

- To view the static report:
```bash
allure open allure-report
```

## 📚 Resources and References
- Selenium Documentation
- Behave Documentation
- Guide to Writing Gherkin Scenarios

## 🤝 Contributing
Contributions are welcome! Follow these steps to contribute:
1. Fork this repository.
2. Create a branch for your changes (git checkout -b feature/new-feature). 
3. Commit your changes (git commit -m 'Add new feature'). 
4. Push to your branch (git push origin feature/new-feature). 
5. Open a Pull Request.

Made with ❤️ by Alisson (https://github.com/alisson-t-bucchi)
Let me know if you need any additional modifications! 🚀