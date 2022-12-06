# json debug scripts from StackOverFlow - see full reference link in README
# https://stackoverflow.com/questions/67467874/an-error-has-occurred-the-server-encountered-an-error-processing-the-lambda-res


import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def dispatch(event):
    # TODO implement
    slots= event['slots'];
    drink,qty,unit= slots['Drink'], slots['Quantity'], slots['Unit']
    retStr= "your order of "+qty+" "+unit+ " of "+drink+ " is coming right up!";
    return {"dialogAction": {
        "type": "Close",
        "fulfillmentState": "Fulfilled",
        "message": {
            "contentType": "PlainText",
            "content": retStr
        },
    }}

def lambda_handler(event, context):
    logger.debug('event={}'.format(event))
    response = dispatch(event)
    logger.debug(response)
    return response


    
    
    ### Intents Dispatcher ###
def dispatch(intent_request):
    slots= intent_request['slots'];
    """
    Called when the user specifies an intent for this bot.
    """

    intent_name = intent_request["currentIntent"]["name"]

    # Dispatch to bot's intent handlers
    if intent_name == 'recommendPortfolio':
        return recommend_portfolio(intent_request)

    raise Exception('Intent with name ' + intent_name + ' not supported')
