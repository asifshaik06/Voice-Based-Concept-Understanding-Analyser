from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_similarity(transcript, reference):
    embedding1 = model.encode(transcript, convert_to_tensor=True)
    embedding2 = model.encode(reference, convert_to_tensor=True)

    similarity = util.cos_sim(embedding1, embedding2).item() * 100

    if similarity >= 85:
        level = "Excellent Understanding"
    elif similarity >= 70:
        level = "Good Understanding"
    elif similarity >= 50:
        level = "Average Understanding"
    else:
        level = "Poor Understanding"

    return round(similarity, 2), level
