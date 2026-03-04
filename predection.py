def predict_routes(routes):

    predictions=[]

    for r in routes:

        success=r["active_flights"]*10

        if success>100:
            success=100

        predictions.append({
            "destination":r["destination"],
            "chance_of_flying":success,
            "chance_of_cancel":100-success
        })

    return predictions
