import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    myobj = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, json=myobj, headers=headers)

        # Handle HTTP errors
        if response.status_code == 400:
            return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        elif response.status_code != 200:
            return {"error": f"Request failed with status code {response.status_code}"}

        formatted_response = response.json()

        # Extract emotions safely
        emotions = formatted_response.get('emotionPredictions', [{}])
        emotion_scores = emotions[0].get('emotion', {}) if emotions else {}

        anger = emotion_scores.get('anger', 0)
        disgust = emotion_scores.get('disgust', 0)
        fear = emotion_scores.get('fear', 0)
        joy = emotion_scores.get('joy', 0)
        sadness = emotion_scores.get('sadness', 0)

        dominant_emotion = formatted_response.get('producerId', {}).get('name', 'unknown')

        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }

    except requests.exceptions.RequestException as e:
        return {"error": f"Network error occurred: {str(e)}"}
    except json.JSONDecodeError:
        return {"error": "Failed to parse response JSON."}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}