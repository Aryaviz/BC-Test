# BC-Test
BC platform assignment





 












March 2023 – QA Specialist
By
Arya Vishnu Ram Thamarakkulam




















 

Introduction	

BC Platforms is a global leader in building data networks for the life sciences industry and provides versatile technology platforms for personalized medicine, accelerating the translation of innovations into clinical practice.

As part of QA specialists job application assignment, I am presenting this documentation.

In the objective of given assignment, existing workflow of one application is given along with information of three tickets which is planned for delivery in the respective sprint.

Assessment scenario

The company is developing a new release of a web application, which connects to a backend SQL database, and uses various GUI frameworks of different ages in different application modules. Users of the web application are authenticated at login. The web application provides tools for following kinds of tasks:

•	Browse SQL data tables and their metadata
•	Import more data to SQL, using a GUI wizard designed for CSV/TSV file imports
•	Browse file import logs in Import History GUI that shows the previous file uploads
•	Control permissions to SQL data for other users

Ticket 1:

Type: Bug
Description: User is allowed to upload data to ABCD dataset using upload wizard but it fails.
To reproduce:
Transfer the data afflist.txt (attached) to server for importing using File Transfer Tool
Create ABCD dataset using the sql structure attached in Dataset Tool
Upload the data directly from the server and select Upload Wizard.
Wizard GUI fails to show the fields in the file.
Status: In progress
Attachments: afflist.txt, dataset_ABCD.sql


Ticket 2:

Type: New Feature
Description: We need BLOB support
Status: Done
Attachments: --


Ticket 3:

Type: New Feature
Description: In Import History view, flag old imported files for reupload and provide a reupload button. In the Import History view the old uploaded files may need to be re-uploaded, if the SQL structure has been changed after original upload.

1) Flag all Historical files, where the file structure is different to the current table SQL structure. The Senior Developer has created an API method to compare if there is a difference. The aim is to compare the original files to the current SQL structure, and if there are differences, the HISTORY row should have a flag (icon, words?) that shows that files are out-of-date.
2) Provide a 'Re-import' button that opens the original files into a new Import session. The file import should follow the same path as any other conventional file import.
File sql_structure.sql gives a table structure that has changed from original, and import_file.csv is the original file used, and matches the original structure. Mock-up of how the GUI should display the flagging to the user is also provided.
Status: In progress
Attachments: screenshot_of gui_mock_up.png, sql_structure.sql, import_file.csv 


Tasks
● Read through the Scenario, and the JIRA issue descriptions. You should be able to proceed with
the assessment even though some concepts in the tickets may require understanding of the web
application in question. This is understood and taken into account in the evaluation of the tasks.

Existing functional flow/ user story

Given web application, which connects to a backend SQL database, and uses various GUI frameworks of different ages in different application modules.
Users of the web application are authenticated at login.
The web application provides tools for following kinds of tasks:

•	Browse SQL data tables and their metadata
•	Import more data to SQL, using a GUI wizard designed for CSV/TSV file imports
•	Browse file import logs in Import History GUI that shows the previous file uploads
•	Control permissions to SQL data for other users

Ticket 1: Is a bug on an existing functionality.
Ticket 2: Is a new feature which has only description and the status is done.
Ticket 3: Is a new feature and status is in progress and UI and API test need to be done.
 
● Rank the descriptions by quality in terms of being suitable for building test cases based on them

Ticket 1	5/ 14
Ticket 2	3/ 14
Ticket 3	5/14



○ Provide reasoning for ranking, how could the ticket be improved to increase its usefulness
for building a test case

Whenever a bug ticket or feature ticket is created, as a best practice if we collect below information’s in planning and refinement meeting, QA can independently build test cases with maximum test coverage and test in right place to save time and effort. 

Ticket 1 :  5/ 14

SL NO	Bug ticket info	Available info
1	Type	Yes
2	Description	Yes
3	Summary	No
4	Source URL	No
5	Environments and build	No
6	assignee	No
7	Steps to reproduce	Yes
8	Console logs	No
9	Expected vs. actual results	No
10	Test evidence attachments	Yes
11	Priority	No
12	Label	No
13	Reporter	No
14	status	Yes


Ticket 2 : 3/ 14

SL NO	Feature ticket info	Available info
1	Type	Yes
2	status	Yes
3	Description	Yes
4	Summary (User Story Statement)	No
5	Acceptance criteria (give : when :then)	No
6	Design /wireframe attachments	No
7	build	No
8	Epic	No
9	Priority	No
10	Effort points for QA and Dev	No
11	Functional Requirements
 and Developer Notes	No
12	QA Notes	No
13	Links and References	No
14	Dependency information 
with other systems and
 CC respective persons
 "to be informed"	NO


Ticket 3 :  5/14

SL NO	Feature ticket info	Available info
1	Type	Yes
2	status	Yes
3	Description	Yes
4	Summary (User Story Statement)	Yes
5	Acceptance criteria (give : when :then)	No
6	Design /wireframe/ attachments	Yes
7	build	No
8	Epic	No
9	Priority	No
10	Effort points for QA and Dev	No
11	Functional Requirements
 and Developer Notes	No
12	QA Notes	No
13	Links and References	No
14	Dependency information 
with other systems and
 CC respective persons
 "to be informed"	No





● Write a skeleton test-case or test-scenario for each ticket
○ Describe, what would you, as a QA Engineer, need to do in order to finish writing the test
cases, if there is not yet enough data to do that

As a QA Engineer if I get any ticket for one sprint below actions need to be done. 
•	First check type of the ticket
•	If it is bug, check the status
•	If it is in progress check if the ticket is having the following minimum information 
1)	Build in which bug is available
2)	Steps to reproduce the bug
3)	Attachment evidence
4)	Environment
5)	Test data used
6)	Expected and actual result 
7)	Bug reporter 
8)	Assignees
9)	priority

   If above details are not available, connect with bug reporter for the missing details 

•	If the status is done check the below information is updated by developer
1)	Build in which fix is available
2)	Environment where the bug is to be tested

    If above details are not available, connect with the developer for the details
•	If it is a feature ticket check below information is available 
		1) User stories and Acceptance criteria 
		2) QA notes
		3) Prerequisite
		4) Dependencies 
		5) Attachments 
If any information is missing connect with Solution Owner (has ownership of solution features and user stories)

Once ticket is assigned need to start planning and update test case with respect to acceptance criteria and need to get approval from Solution Owner.

Once ticket status is done from developer side, need to start execution with approved test plan. 
If any approved test case failed, Fail the ticket and by linking newly created functional bug.


Ticket 1:

This is a bug ticket of an existing feature. 

Once the fix is available for retesting, we should have information from developer like

Description: 

User is allowed to upload data to ABCD dataset using upload wizard but it fails.

To reproduce:

Transfer the data afflist.txt (attached) to server for importing using File Transfer Tool
Create ABCD dataset using the sql structure attached in Dataset Tool
Upload the data directly from the server and select Upload Wizard.
Wizard GUI fails to show the fields in the file.
Status: In progress

Attachments: afflist.txt, dataset_ABCD.sql


Note: In the given case, status is “In progress”. Hence need to connect with bug reporter for more information. Bug functionality is already implemented and related testcases are available in feature ticket or related ticket listed in epic. In general, there is no need to write new testcases for bug tickets. We need to validate status of bug when the fix is available. However as requested in the given assessment, adding the test scenarios below.

Test scenario

TS No	Test scenarios 	Expected Result
1	Verify whether user is allowed to upload data to ABCD dataset using upload wizard	User should be able to successfully upload dataset
2	Verify whether user can browse file import logs in Import History GUI	User should be able to see import history
3	Verify whether user can browse SQL data tables and their metadata	User should be able to browse SQL data tables and their metadata
4	Verify Control permissions to SQL data for other users	User should be able to access the data with respect to the control permission
5 	Verify user not able to add new file with wrong format.	User not able to add new file with wrong format.


Ticket 2:

Type: New Feature
Description: We need BLOB support
Status: Done
Attachments: --

Note: In this ticket status is Done. So, no action needed from QA. But need to clarify in the stand-up meeting whether this new feature has any impact on the functionality of the existing system. If there is no testing scope for QA, need to request to team to add label “NO QA” in the ticket. However as requested in the given assessment, adding the test scenarios below.

Test scenarios 

TS No	Test scenarios 	Expected Result
1	Verify whether user is allowed to upload data of BLOB to dataset using upload wizard	User should be successfully able to upload dataset
2	Verify whether user can browse file import logs in Import History GUI of BLOB type data set	User should be successfully able to see import history
3	Verify whether user can browse SQL data tables and their metadata which have BLOB type	User should be able to can browse SQL data tables and their metadata



Ticket 3:

Type: New Feature
Description: In Import History view, flag old imported files for reupload and provide a reupload
button.
In the Import History view the old uploaded files may need to be re-uploaded, if the SQL structure has been changed after original upload.

1) Flag all Historical files, where the file structure is different to the current table SQL structure.
The Senior Developer has created an API method to compare if there is a difference. The aim is
to compare the original files to the current SQL structure, and if there are differences, the
HISTORY row should have a flag (icon, words?) that shows that files are out-of-date.

2) Provide a 'Re-import' button that opens the original files into a new Import session. The file
import should follow the same path as any other conventional file import.
File sql_structure.sql gives a table structure that has changed from original, and import_file.csv is the original file used, and matches the original structure.
Mock-up of how the GUI should display the flagging to the user is also provided.

Status: In progress
Attachments: screenshot_of gui_mock_up.png, sql_structure.sql, import_file.csv 

Note: This ticket needs to plan for the release. But need some clarification done in refinement session or stand up

1)	Acceptance criteria
2)	User stories 
3)	QA note


Test Scenarios

TS No	Test scenarios 	Expected Result
1	Verify whether user can browse file import logs in Import History GUI	User should be successfully able to see import history
2	Verify whether user can see the rows hilted with a flag (icon, words?) of Historical files, where the file structure is different to the current table SQL structure	user should be able to see the rows hilted with a flag (icon, words?) of Historical files
3	Verify whether user can see 'Re-import' button that opens the original files into a new Import session.	User should be able to see the ‘Re-import' button
4	Verify user able re import successfully using the button.	User should be able re import successfully using the button.
5	Verify user can see not hilted with a flag (icon, words?) for the successfully re imported data.	User should not be able to see hilted with a flag (icon, words?) for the successfully re imported data.
6	Verify user can see not hilted with a flag (icon, words?) for the new file added with right format.	User should not be able to see hilted with a flag (icon, words?) for the new file added with right format.

● Which tool/set of tools you think is best to write automated testcases for the above scenarios
and explain why?

•	Jira/ pivotal: For user stories and acceptances criteria
•	Testrail/Test link:  Test documentation and execution.
•	Selenium/BDD/POM/Robot framework:  Automation scripting 
[ open source and keyword-driven automation framework for acceptance test-driven development ATDD. Independent of the software automation framework to be used, proper BDD allows more efficient acceptance criteria for proper ATDD. ]
•	Git for version control
•	Jenkin for running independently.

● Write a pseudo / segment of automated script against the test scenario selected above
(preferably in robot framework or your choice of scripting, framework, tool) and explain why it’s
designed that way?
For automating given scenario we can use Robot framework beacause as a bestpractice we need to resuse and reduse code.

We can use page object model (POM) to keep all actions/functions and variables in a file for better visibility and clarity.

In Robot framework we have inbuilt libraries which is easily understandable and cover most of the commen actions it.

Kind of Girkin language scripting (BDD) will make easy to read for non tectical team members.


A generic structure of Setup and file organization is given below. 

Setup and file organization

Step 1 Create a project folder “ BC test”
Step 2 Create below files
 
a)	BC_Testcases.robot
b)	BC_Testcases_keywords.robot
c)	BC_Testcases.py
d)	__init__.robot

Step 3 Create a virtual environment 

python -m virtualenv virtual

Step 4 activate virtual environment

source virtual/Scripts/activate

Step 5 Install robot framework and selenium library 

pip install robotframework
pip install --upgrade robotframework-seleniumlibrary

Step 6 Install browsers needed for testing 

pip install webdrivermanager
webdrivermanager chrome --linkpath chromedriver


Project Structure 

Contents avilable in below files 

a)	BC_Testcases.robot

All test case information which needs to be run will be available in this file.

*** Settings ***
Library          BC_Testcases.py   Firefox    #Chrome
Suite Setup     Open
Suite Teardown  Close

*** Test Cases ***
Here we need to write all test case
All locators and action need to be done is available in BC_Testcases.py 
Respective keywords and arguments are available in BC_Testcases_keywords.robot.

To be automated test scenarios 

Verify whether user is allowed to upload data to ABCD dataset using upload wizard
Verify whether user can browse file import logs in Import History GUI
Verify whether user can browse SQL data tables and their metadata
Verify Control permissions to SQL data for other users
Verify user not able to add new file with wrong format.


New functionality to be automated after manual testing

Verify whether user is allowed to upload data of BLOB to dataset using upload wizard
Verify whether user can browse file import logs in Import History GUI of BLOB type data set
Verify whether user can browse SQL data tables and their metadata which have BLOB type



New functionality to be automated after manual testing

Verify whether user can browse file import logs in Import History GUI
Verify whether user can see the rows hilted with a flag (icon, words?) of Historical files, where the file structure is different to the current table SQL structure
Verify whether user can see 'Re-import' button that opens the original files into a new Import session.
Verify user able re import successfully using the button.
Verify user can see not hilted with a flag (icon, words?) for the successfully re imported data.
Verify user can see not hilted with a flag (icon, words?) for the new file added with right format.



b)	BC_Testcases_keywords.robot

Key words need to be given in this file like 

*** Settings ***
Library       	BC_Testcases.py    Firefox    #Chrome


*** Keywords ***
Open search page
    Open

Close pages
    Close




c)	BC_Testcases.py

All action needs to be script in this file

class BC_Testcases (object):

    __url = " "

    def open(self):
        self._web.open(self.__url)

    def __init__(self, browser):
        self._web = Web(browser)

    def close(self):
        self._web.close_all()


d)	__init__.robot

The __init__ function is called every time an object is created from a class. The __init__ method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes.

*** Settings ***
Suite Setup     Open Home Page
Suite Teardown   Close Browsers
Resource        BC_Testcases_keywords.robot


Pseudo code existing functionality 

Test case 1 : User login

Open browser with given url

__url = "”
    def open(self):
        self._web.open(self.__url)

    def __init__(self, browser):
        self._web = Web(browser)

Navigate to login page

    def login (self):
        self._web.get_web_element_by_xpath(" ").click()

Give login credentials and Validate application is navigating to home page.

def login_submit(self):
        self._web.get_web_element_by_xpath("//input[@type='submit']").click()

Give invalidate credentials and validate error message


Test case 2: The user can Browse SQL data tables and their metadata

Navigate to “SQL data Search” page and perform click action on search button.

def search_for_SQL (self):
        self._web.get_web_element_by_xpath("//input[@type='search']").click()


Test case 3: Import more data to SQL, using a GUI wizard designed for CSV/TSV file imports

Navigate to import GUI wizard 

Browse file from the location

Click on the import button

def import (self):
        self._web.get_web_element_by_xpath("//input[@type='import']").click()

Test case 4: Browse file import logs in Import History GUI that shows the previous file uploads

Navigate to Import history GUI

Browse the recent file from Import history GUI


Test case 5: Control permissions to SQL data for other users

Validate data visibility of different types of users based on permission set.


Pseudo code for Ticket 1

We can reuse script which created upto Test case 4

Pseudo code for Ticket 2

We can reuse script which created upto Test case 4 with test data containing BLOB


Pseudo code for Ticket 4

We can reuse script which created upto Test case 4 with additional one test case 6


Test case 6: Browse file import logs in Import History GUI that shows the previous file uploads as highlighted having re import button option.




Concluding Remarks 

Every company has their own process to do manual and automation testing.
For the given scenario based on my hands on or previous project experience things are narrated based on the available information. 
















