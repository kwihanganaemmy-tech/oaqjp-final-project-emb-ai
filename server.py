from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app =Flask("emotionDetector")
@app.route("/emotionDetector")
def emotionDetector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    if response is None or response.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    dominant_emotion = max(
            {k: v for k, v in response.items() if k != 'dominant_emotion'},
            key=response.get
            )
    emotion_parts = [f"'{k}': {v}" for k, v in response.items()]
    
    if len(emotion_parts) > 1:
        emotion_text = ", ".join(emotion_parts[:-1]) + " and " + emotion_parts[-1]
    else:
        emotion_text = emotion_parts[0]
    dominant = response.get("dominant_emotion", "unknown")
    
    return f"For the given statement, the system response is {emotion_text}. The dominant emotion is {dominant_emotion}."
@app.route("/") 
def render_index_page(): 
    return render_template('index.html')

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000)

