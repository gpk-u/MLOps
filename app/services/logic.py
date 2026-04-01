import pickle
import re
from app.services.rules import rule_engine

# load model + vectorizer
with open("model.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)


def clean_text(text: str):

    # split camelCase & PascalCase
    text = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

    text = text.lower()

    # normalize common words
    text = text.replace("utilization", "usage")

    # remove numbers
    text = re.sub(r"\b\d+\b", " ", text)

    # remove special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    # normalize spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def predict_ticket(text: str):

    cleaned = clean_text(text)

    # ML FIRST (always runs)
    X = vectorizer.transform([cleaned])
    probs = model.predict_proba(X)[0]
    labels = model.classes_

    max_index = probs.argmax()
    ml_prediction = labels[max_index]
    ml_confidence = probs[max_index]

    # RULES (assist, not override blindly)
    rule_result = rule_engine(cleaned)

    # COMBINE LOGIC
    if rule_result and ml_confidence < 0.7:
        prediction = rule_result
        confidence = 0.85
        source = "rule+ml"
    else:
        prediction = ml_prediction
        confidence = ml_confidence
        source = "ml"

    # DECISION LAYER
    if confidence > 0.8:
        action = "auto"
    elif confidence > 0.4:
        action = "suggest"
    else:
        action = "review"

    return {
        "issue_bucket": prediction,
        "confidence": round(float(confidence), 2),
        "source": source,
        "action": action
    }