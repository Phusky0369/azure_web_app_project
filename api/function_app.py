import azure.functions as func
import json
import math
import logging

app = func.FunctionApp()

@app.route(route="CalculateMath", auth_level=func.AuthLevel.ANONYMOUS)
def CalculateMath(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing math calculation request.')

    try:
        # 1. Get the JSON body from the frontend request
        req_body = req.get_json()
        number = int(req_body.get('number'))
        
        # 2. Perform Math Logic
        # Square Root
        sqrt_val = math.sqrt(number)
        
        # Finding Divisors
        divisors = [i for i in range(1, number + 1) if number % i == 0]
        
        # 3. Create response object
        result = {
            "sqrt": sqrt_val,
            "divisors": divisors
        }
        
        # 4. Return as JSON
        return func.HttpResponse(
            json.dumps(result),
            mimetype="application/json",
            status_code=200
        )
        
    except (ValueError, TypeError):
        return func.HttpResponse(
            "Please provide a valid integer in the 'number' field.",
            status_code=400
        )
