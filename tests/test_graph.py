def test_graph_creation():
    from graph.create_graph import create_graph_from_text
    try:
        create_graph_from_text("Albert Einstein developed relativity.")
    except Exception as e:
        assert False, f"Graph creation failed: {e}"