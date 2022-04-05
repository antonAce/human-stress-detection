"""Main file to perform XGBoost model prediction."""

import json
import functions_framework

from flask import make_response, jsonify
from predictor import Predictor


required_argument_list = [
    "sr", "rr", "t", "lm", "bo", "rem", "sh", "hr"
]

required_argument_transcription = {
    "sr": "Snoring range of the user",
    "rr": "Respiration rate",
    "t": "Body temperature",
    "lm": "Limb movement rate",
    "bo": "Blood oxygen levels",
    "rem": "Eye movement",
    "sh": "Number of hours of sleep",
    "hr": "Heart rate"
}

stress_level_transcription = {
    "4": "High", "3": "Medium high", "2": "Medium",
    "1": "Medium low", "0": "Low or normal"
}

lists_contain_same_elements = lambda l_list, r_list: len(list(set(l_list) & set(r_list))) == len(l_list)
get_missing_elements = lambda expected_list, actual_list: list(set(actual_list) - set(expected_list))


@functions_framework.http
def calculate_stress_level(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
    Returns:
        The response text, or any set of values that can be turned into a Response object using `make_response`.
    """

    if request.method != 'POST':
        return make_response(jsonify(message="HTTP method is not allowed."), 405)
    else:
        request_json = request.get_json(silent=True)
        request_json_keys = list(request_json.keys())

        if not lists_contain_same_elements(required_argument_list, request_json_keys):
            missing_args = get_missing_elements(request_json_keys, required_argument_list)
            transcripted_missing_args = [f"'{arg}': '{required_argument_transcription[arg]}'" for arg in missing_args]
            return make_response(jsonify(message=f"Body is missing following arguments: [{', '.join(transcripted_missing_args)}]."), 400)

        predictor = Predictor.from_path('./')
        prediction = predictor.predict([request_json])

        return json.dumps({
            "stress_level": prediction[0]["predicted_sl"],
            "stress_level_transcription": stress_level_transcription[prediction[0]["predicted_sl"]],
            "stress_level_probabilities": {
                stress_level_transcription[val]:prob for val, prob in zip(prediction[0]["sl_values"], prediction[0]["sl_probs"])
            }
        })
