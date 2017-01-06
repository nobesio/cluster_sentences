import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AffinityPropagation

punctuation_map = dict((ord(char), None) for char in string.punctuation)
stemmer = nltk.stem.snowball.SpanishStemmer()

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize)

def get_clusters(sentences):
    tf_idf_matrix = vectorizer.fit_transform(sentences)
    similarity_matrix = (tf_idf_matrix * tf_idf_matrix.T).A
    affinity_propagation = AffinityPropagation(affinity="precomputed", damping=0.5)
    affinity_propagation.fit(similarity_matrix)

    labels = affinity_propagation.labels_
    cluster_centers = affinity_propagation.cluster_centers_indices_

    tagged_sentences = zip(sentences, labels)
    clusters = {}

    for sentence, cluster_id in tagged_sentences:
        clusters.setdefault(sentences[cluster_centers[cluster_id]], []).append(sentence)

    return clusters


sentences = [
    'Messi es el mejor jugador de Football.',
    'Neymar juega al football con Messi en el Barcelona.',
    'Los Pumas son la seleccion nacional de Rugby.',
    'Los Pumas ganaron contra Japon.',
    'Las Leonas ganaron una medalla de Oro en las olimpiadas.',
    'Carla Rebecchi es la capitana de las Leonas.'
]

clusters = get_clusters(sentences)
print()
for cluster in clusters:
    print(cluster, ':')
    for element in clusters[cluster]:
        print('  - ', element)