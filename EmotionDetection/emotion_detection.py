import requests, json

def emotion_detector (text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = input_json, headers=header)

    formatted_response = json.loads(response.text)
    formatted_response = formatted_response['emotionPredictions'][0]['emotion']
    
    max_value = 0
    dominant_emotion = ""
    for key, value in formatted_response.items():
        if value > max_value:
            max_value = value
            dominant_emotion = key
    
    formatted_response['dominant_emotion'] = dominant_emotion

    return formatted_response