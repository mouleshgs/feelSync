from transformers import pipeline

def get_emotion_classifier():
    return pipeline("text-classification", model="SamLowe/roberta-base-go_emotions", top_k=1)

def classify_emotion(classifier, text):
    result = classifier(text)[0]
    return result[0]['label'].lower()

