import json
from typing import Any, Dict, List, Union


class Episode:
    def __init__(self, audio_preview_url: str=None, description: str = None, duration_ms: int = None,
        external_urls: Dict[str, str] = None, href: str = None, id: str = None, images: List[Any] = None,
        is_externally_hosted: bool = None, language: str = None, name: str = None, release_date: str = None,
        release_date_precision: str = None, type: str = None, uri: str = None) -> None:
        """Constructor.
        
        Arguments:
            audio_preview_url:      Audio preview url.
            description:            Description of the episode.
            duration_ms:            Duration in miliseconds.
            external_urls:          External urls for the episode.
            href:                   The link to the episode.
            id:                     Id of the episode.
            images:                 Images for the episode.
            is_externally_hosted:   Is the episode externally hosted, boolean.
            language:               Language of the episode.
            name:                   Name of the episode.
            release_date:           Release date.
            release_date_precision: Release date precision.
            type:                   Type, should be episode.
            uri:                    Uri of the episode.
        """
        self.audio_preview_url: str = audio_preview_url
        self.description: str = description
        self.duration_ms: int = duration_ms,
        self.external_urls: Dict[str, str] = external_urls
        self.href: str = href
        self.id: str = id
        self.images: List[Any] = images,
        self.is_externally_hosted: bool = is_externally_hosted
        self.language: str = language
        self.name: str = name
        self.release_date: str = release_date
        self.release_date_precision: str = release_date_precision
        self.type: str = type
        self.uri: str = uri

    def __str__(self) -> str:
        return str(self.__dict__)


def load_episode_from_json(json_str: Union[str, Dict[str, Any]]) -> Union[Episode, None]:
    try:
        if type(json_str) == "str":
            complex_dict: Dict[str, Any] = json.loads(json_str)
        else:
            complex_dict = json_str
        return Episode(audio_preview_url=complex_dict["audio_preview_url"],
            description=complex_dict["description"],
            duration_ms=complex_dict["duration_ms"],
            external_urls=complex_dict["external_urls"],
            href=complex_dict["href"],
            id=complex_dict["id"],
            images=complex_dict["images"],
            is_externally_hosted=complex_dict["is_externally_hosted"],
            language=complex_dict["language"],
            name=complex_dict["name"],
            release_date=complex_dict["release_date"],
            release_date_precision=complex_dict["release_date_precision"],
            type=complex_dict["type"],
            uri=complex_dict["uri"])
    except Exception as e:
        print(f"Encountered error {e}")
        return None
