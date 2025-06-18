from sklearn.feature_extraction.text import TfidfVectorizer

# 1. Input documents
documents = [
    "k-means clustering is a method to partition data into clusters",
    "centroid calculation uses euclidean distance to measure similarity",
    "a heatmap shows the intensity of data distribution",
    # ... more documents
]

# 2. Keywords to align
keywords = ['advantages disadvantages', 'alright tune', 'axes', 'badness', 'best clustering', 'best overall', 'best question', 'best value', 'better idea', 'black point', 'bloch cluster', 'blue center', 'blue cluster', 'blue point', 'brown point', 'calculations', 'cell types', 'centroid', 'centroids', 'centuries', 'century', 'clustering algorithms', 'clusters', 'colors', 'coordinates', 'crazy high dimension', 'data points', 'data set', 'decent amount', 'dimensions', 'discord server', 'distances', 'distinct data points', 'drawing', 'easier job', 'equals', 'essentially', 'euclidean distance', 'fancier', 'final points', 'green cluster', 'handwritten digits', 'heat map', 'heatmap', 'hey', 'hierarchical clustering', 'image', 'influential parameter', 'initial clusters', 'iteration', 'iterations', 'josh stormer', 'k-means clustering', 'labels', 'learning tutorial', 'like button', 'long time', 'lovely photo', 'machine learning']

# 3. Create TF-IDF vectorizer with 1-2 word phrases and remove stopwords
vectorizer = TfidfVectorizer(ngram_range=(1,2), stop_words='english')
tfidf_matrix = vectorizer.fit_transform(keywords)

# 4. Get terms and their TF-IDF scores (summed across all documents)
terms = vectorizer.get_feature_names_out()
scores = tfidf_matrix.sum(axis=0).A1
tfidf_dict = dict(zip(terms, scores))

# 5. Map keywords to TF-IDF scores (0 if not found)
keyword_weights = {kw: tfidf_dict.get(kw, 0.0) for kw in keywords}

# 6. Sort keywords by weight (optional)
sorted_keyword_weights = dict(sorted(keyword_weights.items(), key=lambda x: x[1], reverse=True))

print(sorted_keyword_weights)
