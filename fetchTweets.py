import requests

def run(term):
    query = """
    {{
      sentiment(term:"{term}") {{
        averageWeighedPolarity
        negativeTweetsCount
        neutralTweetsCount
        positiveTweetsCount
      }}
    }}
    """
    queryFormatted = query.format(term=term)
    request = requests.post("https://doxa-api.herokuapp.com/graphql", json={"query":queryFormatted})
    return request.json()

