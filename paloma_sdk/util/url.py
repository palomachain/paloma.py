# from furl import furl  # type: ignore


def urljoin(base: str, url: str) -> str:
    return base.rstrip("/") + url
