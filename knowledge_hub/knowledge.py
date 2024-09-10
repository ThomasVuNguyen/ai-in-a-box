import chromadb
import random
client = chromadb.HttpClient()
collection = client.get_or_create_collection("hobby")
# Add docs to the collection. Can also update and delete. Row-based API coming soon!

def add():
    collection.add(
        documents=[
            "Thomas is a robotics enthusiast who builds and programs small robots in his spare time.",
            "Emily is an avid painter specializing in watercolor landscapes.",
            "Michael is passionate about urban gardening and grows vegetables on his apartment balcony.",
            "Sarah is a dedicated rock climber who spends weekends scaling challenging routes.",
            "David is an amateur astronomer who enjoys stargazing and astrophotography."
        ],
        metadatas=[
            {"source": "personal-profile", "category": "technology"},
            {"source": "hobby-blog", "category": "art"},
            {"source": "community-forum", "category": "gardening"},
            {"source": "outdoor-club", "category": "sports"},
            {"source": "science-newsletter", "category": "astronomy"}
        ],
        ids=["person1", "person2", "person3", "person4", "person5"]
    )


def add_random():
    # Lists of names, hobbies, sources, and categories
    names = ["Thomas", "Emily", "Michael", "Sarah", "David", "Lisa", "Alex", "Olivia", "Daniel", "Sophia"]
    hobbies = ["robotics", "painting", "gardening", "rock climbing", "astronomy", "cooking", "photography", "writing", "dancing", "woodworking"]
    sources = ["personal-profile", "hobby-blog", "community-forum", "social-media", "local-club"]
    categories = ["technology", "art", "outdoors", "science", "crafts", "sports", "literature", "music", "culinary", "fitness"]

    # Generate 100 people
    documents = []
    metadatas = []
    ids = []

    for i in range(1, 1000):
        name = random.choice(names)
        hobby = random.choice(hobbies)
        source = random.choice(sources)
        category = random.choice(categories)
        
        documents.append(f"{name} is passionate about {hobby} and dedicates time to this hobby regularly.")
        metadatas.append({"source": source, "category": category})
        ids.append(f"person{i}")

    # Add to collection
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )
def query():
    results = collection.query(
        query_texts=["Who loves robotics?"],
        n_results=5,
        # where={"metadata_field": "is_equal_to_this"}, # optional filter
        # where_document={"$contains":"search_string"}  # optional filter
    )

    print(results['documents'][0])
    return results['documents'][0]

#query()

#add_random()

