# json debug scripts from StackOverFlow - see full reference link in README
# https://stackoverflow.com/questions/67467874/an-error-has-occurred-the-server-encountered-an-error-processing-the-lambda-res


import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def dispatch(event):
    # TODO implement
    slots= event["slots"];
    drink,qty,unit= slots["Drink"], slots["Quantity"], slots["Unit"]
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
    """
    Called when the user specifies an intent for this bot.
    """
    
    slots= intent_request['slots'];
    first_name, age, investment_amount, risk_level = slots['firstName'], slots['age'], slots['investmentAmount'], slots['riskLevel']

    intent_name = intent_request['currentIntent']['name']

    # Dispatch to bot's intent handlers
    if intent_name == 'recommendPortfolio':
        return recommend_portfolio(intent_request)

    raise Exception('Intent with name ' + intent_name + ' not supported')

    

def lambda_handler(intent_request, context):
    logger.debug('event={}'.format(event))
    response = dispatch(intent_request)
    logger.debug(response)
    return response

    
    
    
    
    
    
____________________________________

    
    
    
import json
import logging

### Intents Dispatcher ###
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """
    
    slots= intent_request['slots'];
    first_name, age, investment_amount, risk_level = slots['firstName'], slots['age'], slots['investmentAmount'], slots['riskLevel']

    intent_name = intent_request['currentIntent']['name']

    # Dispatch to bot's intent handlers
    if intent_name == 'recommendPortfolio':
        return recommend_portfolio(intent_request)

    raise Exception('Intent with name ' + intent_name + ' not supported')

    

def lambda_handler(intent_request, context):
    logger.debug('event={}'.format(event))
    response = dispatch(intent_request)
    logger.debug(response)
    return response
    
    


    
