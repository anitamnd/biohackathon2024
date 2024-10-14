import requests

def search_europe_pmc(query):
    """Search Europe PMC and return the JSON response."""
    api_endpoint = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
    params = {
        'query': query,
        'format': 'json',
        'resultType': 'core'
    }
    response = requests.get(api_endpoint, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None
    