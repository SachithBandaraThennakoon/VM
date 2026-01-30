from app.memory.knowledge_store import add_document

def load_knowledge():
    documents = [
        "Balance comes from a relaxed and stable center.",
        "Tension reduces awareness and control.",
        "Move with awareness, not speed.",
        "Discipline begins with calm breathing.",
        "Stability is maintained through posture and grounding."
    ]

    for doc in documents:
        add_document(doc)

    print(f"[KnowledgeLoader] Loaded {len(documents)} documents.")
