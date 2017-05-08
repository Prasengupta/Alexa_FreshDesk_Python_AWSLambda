             Sample Python AWS Lambda function for Alexa
A sample AWS lambda function which helps for writing skills for Amazon Alexa Echo

Concepts	
This simple sample has an external dependencies or session management, and shows the most basic example of how to create a Lambda function for handling Alexa Skill requests.
Setup
You need to install below libraries to test in the local machine, I have already included them in the repository 
Libraries Needed
1.	Requests
2.	Json 
AWS Lambda Setup
1.	Go to the AWS Console and click on the Lambda link. Note: ensure you are in us-east or you won't be able to use Alexa with Lambda.
2.	Click on the Create a Lambda Function or Get Started Now button.
3.	Search for alexa-python kit
4.	Name the Lambda Function “FreshDesk_Alexa".
5.	Select the runtime as Python 2.7
6.	Go to the src directory, select all files and then create a zip file, make sure the zip file does not contain the src directory itself, otherwise Lambda function will not work.
7.	Select Code entry type as "Upload a .ZIP file" and then upload the .zip file to the Lambda
8.	Keep the Handler as Freshdesk_alexa.lambda_handler (this refers to the main python file in the zip).
9.	Create a basic execution role and click create.
10.	Leave the Advanced settings as the defaults.
11.	Click "Next" and review the settings then click "Create Function"
12.	Click the "Event Sources" tab and select "Add event source"
13.	Set the Event Source type as Alexa Skills kit and Enable it now. Click Submit.
14.	Copy the ARN from the top right to be used later in the Alexa Skill Setup.

Alexa Skill Setup
1.	Go to the Alexa Console and click Add a New Skill.
2.	Set "Fresh Desk tickets" as the skill name and " how many tickets in my fresh desk" as the invocation name, this is what is used to activate your skill. For example you would say: "Alexa,how many tickets in my fresh desk."
3.	Select the Lambda ARN for the skill Endpoint and paste the ARN copied from above. Click Next.
4.	Copy the Intent Schema from blog
5.	Copy the Sample Utterances from blog Click Next.
6.	[optional] go back to the skill Information tab and copy the appId. Paste the appId into the main.py file for the variable APP_ID, then update the lambda source zip file with this change and upload to lambda again, this step makes sure the lambda function only serves request from authorized source.
7.	You are now able to start testing your sample skill! You should be able to go to the Echo webpage and see your skill enabled.
8.	In order to test it, try to say some of the Sample Utterances from the Examples section below.
9.	Your skill is now saved and once you are finished testing you can continue to publish your skill.


