ES_PREDICTIONS_QUERY = """
{
    "query": {
        "terms": {
            "sentence_content": {}
        }
    }
}
"""

ES_PREDICTIONS_PARAMS = {
    'size': 20
}