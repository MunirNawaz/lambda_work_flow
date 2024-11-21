import json
def lamda_handler(event, context):
    return {
        "statuscode" : 200,
        "body" : json.dumps("Hellow Lambda from vscode-1 for my-lambda_test")
    }
    
    