import json
def lamda_handler(event, context):
    return {
        "statuscode" : 200,
        "body" : json.dumps("Hellow from CICD Lambda from vscode1")
    }
    
    