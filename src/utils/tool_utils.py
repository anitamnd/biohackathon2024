def get_publication_from_match(match):
    """Update the original publication information with data from the match if available.
    Exclude fields that do not have a value."""
    return {
        key: value
        for key, value in (('doi', match.get('doi')), 
                           ('pmid', match.get('pmid')), 
                           ('pmcid', match.get('pmcid')))
        if value is not None
    }