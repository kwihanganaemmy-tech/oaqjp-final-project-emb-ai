import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test1(self):
        case1 = emotion_detector("I am glad this happened")
        dominant_emotion = max(
            {k: v for k, v in case1.items() if k != 'dominant_emotion'},
            key=case1.get
            )
        self.assertEqual(dominant_emotion, "joy")
        case2 = emotion_detector("I am really mad about this")
        dominant_emotion2 = max(
            {k: v for k, v in case2.items() if k != 'dominant_emotion'},
            key=case2.get
            )
        self.assertEqual(dominant_emotion2, "anger")

        case3 = emotion_detector("I feel disgusted just hearing about this")
        dominant_emotion3 = max(
            {k: v for k, v in case3.items() if k != 'dominant_emotion'},
            key=case3.get
            )
        self.assertEqual(dominant_emotion3, "disgust")

        case4 = emotion_detector("I am so sad about this")
        dominant_emotion4 = max(
            {k: v for k, v in case4.items() if k != 'dominant_emotion'},
            key=case4.get
            )
        self.assertEqual(dominant_emotion4, "sadness")
        
        case5 = emotion_detector("I am really afraid that this will happen")
        dominant_emotion5 = max(
            {k: v for k, v in case5.items() if k != 'dominant_emotion'},
            key=case5.get
            )
        self.assertEqual(dominant_emotion5, "fear")

unittest.main()