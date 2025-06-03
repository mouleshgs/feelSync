from transformers import pipeline

def get_emotion_classifier():
    return pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=False)

def classify_emotion(classifier, text):
    result = classifier(text)[0]
    return result['label'].lower()
