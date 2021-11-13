import json
from typing import Any, Dict, List, Union

class Episodes(dict):
    def __init__(self, href: str = None, items: List[Dict[str, Any]] = None,
    limit: int = None,
    next: str = None,
    offset: int = None,
    previous: str = None,
    total: int = None) -> None:
        """"""
        self.href = href
        self.items = items
        self.limit = limit
        self.next = next
        self.offset = offset
        self.previous = previous
        self.total = total

class PodcastInfo(dict):
    """Class for representing information about a podcast."""
    def __init__(self, name: str = None, id: str = None,
        available_markets: List[str] = None,
        copyrights: List[str] = None,
        description: str = None,
        episodes: Dict[str, Any] = None,
        explicit: bool = None,
        external_urls: Dict[str, str] = None,
        href: str = None,
        images: List[Dict[str, Any]] = None,
        is_externally_hosted: bool = None,
        languages: List[str] = None,
        media_type: str = None,
        publisher: str = None,
        type: str = None,
        uri: str = None) -> None:
        """Constructor.

        Arguments:
            name:                   Name of show.
            id:                     The show's id.
            available_markets:      List of markets its available.
            copyrights:             Copyrights.
            description:            Description of the show.
            episodes:               List of episodes (will be of length 50)
            explicit:               Whether or not its explicit content.
            external_urls:          External urls list.
            href:                   Link to show.
            images:                 List of images for the show.
            is_externally_hosted:   Is the show externally hosted.
            languages:              Languages of the broadcast.
            media_type:             Type of media, i.e. "audio".
            publisher:              Name of the podcast's publisher.
            type:                   Type, should always be "show". 
            uri:                    Uri for the podcast example "spotify:show:38bS44xjbVVZ3No3ByF1dJ".
        """
        self.name = name
        self.id = id
        self.available_markets = available_markets
        self.copyrights: List[str] = copyrights
        self.description: str = description
        self.explicit: bool = explicit
        self.external_urls: Dict[str, str] = external_urls
        self.href: str = href
        self.images = images
        self.is_externally_hosted: bool = is_externally_hosted
        self.languages: List[str] = languages
        self.media_type: str = media_type
        self.publisher: str = publisher
        self.type = type
        self.uri = uri
        #self.episodes = episodes
        # set episode
        self.episodes = Episodes(episodes["href"],
            items=episodes["items"], limit=episodes["limit"], next=episodes["next"],
            offset=episodes["offset"], previous=episodes["previous"], total=episodes["total"])

    def load_episodes(self, amount: int = 50) -> None:
        """"""
        if amount <= 0:
            return None
        return None

    def filter_episodes(self) -> None:
        return None

    def __str__(self) -> str:
        return str(self.__dict__)

def load_podcast_from_json(json_str: Union[str, Dict[str, Any]]) -> Union[PodcastInfo, None]:
    try:
        if type(json_str) == "str":
            complex_dict: Dict[str, Any] = json.loads(json_str)
        else:
            complex_dict = json_str
        return PodcastInfo(name=complex_dict["name"],
            id=complex_dict["id"],
            available_markets=complex_dict["available_markets"],
            copyrights=complex_dict["copyrights"],
            description=complex_dict["description"],
            episodes=complex_dict["episodes"],
            explicit=complex_dict["explicit"],
            external_urls=complex_dict["external_urls"],
            href=complex_dict["href"],
            images=complex_dict["images"],
            is_externally_hosted=complex_dict["is_externally_hosted"],
            languages=complex_dict["languages"],
            media_type=complex_dict["media_type"],
            publisher=complex_dict["publisher"],
            type=complex_dict["type"],
            uri=complex_dict["uri"])
    except Exception as e:
        print(f"Encountered error {e}")
        return None