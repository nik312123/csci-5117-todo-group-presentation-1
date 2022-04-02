from urllib.parse import urlparse, urljoin


def valid_url(url: str) -> bool:
    """
    Returns true if a URL is valid. Based on https://stackoverflow.com/a/50352868.
    :param url: The URL to validate
    :return: True if a URL is valid
    """
    try:
        final_url = urlparse(urljoin(url, "/"))
        return all([final_url.scheme, final_url.netloc, final_url.path]) and len(final_url.netloc.split(".")) > 1
    except:
        return False
