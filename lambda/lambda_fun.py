import json
def lamda_handler(event, context):
    return {
        "statuscode" : 200,
        "body" : json.dumps("Hellow Lambda from vscode for my-lambda_test")
    }
    
    