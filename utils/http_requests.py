from urllib.request import Request, urlopen
from urllib.parse import urlencode


def get_url(url: str, headers: dict = None, params: dict = None) -> str:
    """
    Helper function to get url content using standard library
    """
    if params:
        params = urlencode(params)
        url = f"{url}?{params}"

    req = Request(url)

    if headers:
        {req.add_header(k, v) for k, v in headers.items()}

    resp = urlopen(req)
    text = resp.read().decode("utf-8").strip()
    return text


if __name__ == "__main__":
    params = {"test1": "response1", "test2": "response2"}
    print(get_url("https://httpbin.org/get", params=params))
