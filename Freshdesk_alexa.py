import json
from Get_Fresh_Desk_opentickets import GetFreshDeskCount
def lambda_handler(event, context):
    # if (event["session"]["application"]["applicationId"] !=
    #         "amzn1.echo-sdk-ams.app.bd304b90-xxxx-xxxx-xxxx-xxxxd4772bab"):
    #     raise ValueError("Invalid Application ID")
    
    # if event["session"]["new"]:
    #     on_session_started({"requestId": event["request"]["requestId"]}, event["session"])
    #event = json.loads(event)
    if event["request"]["type"] == "LaunchRequest":
        return on_launch(event["request"], event["session"])
    elif event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return on_session_ended(event["request"], event["session"])

def on_session_started(session_started_request, session):
    print "Starting new session."

def on_launch(launch_request, session):
    return GetFreshDeskCount_alexa()

def on_intent(intent_request, session):
    intent = intent_request["intent"]
    intent_name = intent_request["intent"]["name"]

    if intent_name == "GetFreshDeskCount":
        return GetFreshDeskCount_alexa()
    elif intent_name == "GetHai":
        return get_hai()
    elif intent_name == "GetPythonLibraries":
        return get_python_libraries(intent)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    print "Ending session."
    # Cleanup goes here...

def handle_session_end_request():
    card_title = "Thanks"
    speech_output = "Thank you for using Fresh Desk Support"
    should_end_session = True

    return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))

def GetFreshDeskCount_alexa():
    session_attributes = {}
    card_title = ""
    reprompt_text = ""
    should_end_session = True
    a = GetFreshDeskCount()
    print a
    speech_output =  "Your have %s open tickets in fresh desk"%a
    #speech_output = "Your have %d"

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        "outputSpeech": {
            "type": "PlainText",
            "text": output
        },
        "card": {
            "type": "Simple",
            "title": title,
            "content": output
        },
        "reprompt": {
            "outputSpeech": {
                "type": "PlainText",
                "text": reprompt_text
            }
        },
        "shouldEndSession": str(should_end_session)
    }

def build_response(session_attributes, speechlet_response):
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response
    }
# event = '''
# {
#   "session": {
#     "sessionId": "SessionId.219ee2b6-2054-4739-860b-5755772fef37",
#     "application": {
#       "applicationId": "amzn1.ask.skill.4f07d409-e907-4dac-b420-e695c7496cfe"
#     },
#     "attributes": {},
#     "user": {
#       "userId": "amzn1.ask.account.AGSJQB2DUXPPWJDIEOJRKEC2E4V76RMV2YEA3VLURKYWD5V5NJF6OVKDAWPRB5K2WWSDLVWYBHZBUQQ7T37XO4HDFSBPVX43GVTLN7NV4YEOU4JPG2ECJGNL6MLLZRZCQNGWMIMLRK4XR45PYJQCFS6JOH7AILDPVBIPO4XCNSP7VBN5VMCK7U3FCP4PQJH4LCVTTOOK5R7Z3EQ"
#     },
#     "new": true
#   },
#   "request": {
#     "type": "LaunchRequest",
#     "requestId": "EdwRequestId.db3eacdc-643e-41c8-b1e7-9cb996bb83b1",
#     "locale": "en-US",
#     "timestamp": "2017-04-30T22:45:00Z"
#   },
#   "version": "1.0"
# }'''
# import json
# print type(event)
# #d = json.loads(event)
# a = lambda_handler(event)
# print type(a)
# r = json.dumps(a)
# #loaded_r = json.loads(r)
# print r