from typing import Any, Dict, List, Union

class Image(dict):
    """
    Represents the image object sent by spotify.
    """
    
    def __init__(self, height: int, url: str, width: int) -> None:
        self.height: int = height 
        self.url: str = url
        self.width: int = width

    @property
    def serialize(self) -> Dict[str, str]:
        return {
            "height": self.height,
            "url": self.url,
            "width": self.width,
        }

    @staticmethod
    def load_from_json(values: Dict[str, Union[str, int]]) -> None:
        return Image(values["height"], values["url"], values["width"])

    def __str__(self) -> str:
        return str(self.__dict__)

class Item(dict):
    """Individual episode."""

    def __init__(self,audio_preview_url: str,
        description: str,
        duration_ms: int,
        external_urls: Dict[str, str],
        href: str,
        id: str,
        images: List[Image],
        is_externally_hosted: bool,
        language: str,
        name: str,
        release_date: str,
        release_date_precision: str,
        type: str,
        uri: str) -> None:
        """Constructor"""

        self.audio_preview_url: str = audio_preview_url
        self.description: str = description
        self.duration_ms: int = duration_ms
        self.external_urls: Dict[str, str] = external_urls
        self.href: str = href
        self.id: str = id
        self.images: List[Image] = images
        self.is_externally_hosted: bool = is_externally_hosted
        self.language: str = language
        self.name: str = name
        self.release_date: str = release_date
        self.release_date_precision: str = release_date_precision
        self.type: str = type
        self.uri: str = uri

    @property
    def serialize(self) -> Dict[str, Any]:
        return {
            "description": self.description,
            "duration_ms": self.duration_ms,
            "external_urls": self.external_urls,
            "href": self.href,
            "id": self.id,
            "images": [ str(image) for image in self.images],
            "is_externally_hosted": self.is_externally_hosted,
            "language": self.language,
            "name": self.name,
            "release_date": self.release_date,
            "release_date_precision": self.release_date_precision,
            "type": self.type,
            "uri": self.uri
        }

    def __str__(self):
        return str({
            "description": self.description,
            "duration_ms": self.duration_ms,
            "external_urls": self.external_urls,
            "href": self.href,
            "id": self.id,
            "images": [ str(image) for image in self.images],
            "is_externally_hosted": self.is_externally_hosted,
            "language": self.language,
            "name": self.name,
            "release_date": self.release_date,
            "release_date_precision": self.release_date_precision,
            "type": self.type,
            "uri": self.uri
        })
    
    @staticmethod
    def load(values: Dict[str, Any]) -> 'Item':
        return Item(values["audio_preview_url"],
            values["description"],
            values["duration_ms"],
            values["external_urls"],
            values["href"],
            values["id"],
            values["images"],
            values["is_externally_hosted"],values["language"],
            name = values["name"],
            release_date = values["release_date"],
            release_date_precision = values["release_date_precision"],
            type = values["type"],
            uri = values["uri"])

class Episodes(dict):
    """Episodes from spotify"""

    def __init__(self, href: str, items: List[Item], limit: int,
        next: str, offset: int, previous: Union[str, None], 
        total: int) -> None:
        """Constructor"""
        self.href: str = href
        self.items_sp: List[Item] = items
        self.limit: int = limit
        self.next: str = next
        self.offset: int = offset
        self.previous: Union[str, None] = previous
        self.total: int = total

    @property
    def serialize(self) -> Dict[str, Any]:
        return {
             "href": self.href,
            "items": [x for x in self.items_sp],
            "limit": self.limit,
            "next": self.next,
            "offset":  self.offset,
            "previous": self.previous,
            "total": self.total
        }

    def __str__(self) -> str:
        print(self.items_sp)
        return str({
             "href": self.href,
            "items": [ str(x) for x in self.items_sp],
            "limit": self.limit,
            "next": self.next,
            "offset":  self.offset,
            "previous": self.previous,
            "total": self.total
        })

    @staticmethod
    def load_from_json(values: Dict[str, Any]) -> 'Episodes':
        return Episodes( href= values["href"],
        items = [ Item.load(item) for item in values["items"]],
        limit = values["limit"],
        next = values["next"],
        offset = values["offset"],
        previous = values["previous"],
        total = values["total"])


class Podcast(dict):

    def __init__(self, available_markets: str, name: str, copyrights: str, description: str,
        episodes: Dict[str, Any], explicit: bool, external_urls: Dict[str, str],
        href: str, id: str, images: Dict[str, Any], is_externally_hosted: bool,
        languages: List[str], media_type: str, publisher: str,
        type: str, uri: str) -> None:
        """Constructor"""
        self.available_markets: str = available_markets
        self.name: str = name
        self.copyrights: str = copyrights
        self.description: str = description
        self.episodes: Dict[str, Any] = episodes
        self.explicit: bool = explicit
        self.external_urls: Dict[str, str] = external_urls
        self.href: str = href
        self.id: str = id
        self.images = images
        self.is_externally_hosted: bool = is_externally_hosted
        self.languages: List[str] = languages
        self.media_type: str = media_type
        self.publisher: str = publisher
        self.type: str = type
        self.uri: str = uri

    @property
    def serialize(self):
        return {
            "available_markets": self.available_markets,
            "name": self.name,
            "copyrights": self.copyrights,
            "description": self.description,
            "episodes": self.episodes,
            "explicit": self.explicit,
            "external_urls": self.external_urls,
            "href": self.href,
            "id": self.id,
            "images": self.images,
            "is_externally_hosted": self.is_externally_hosted,
            "languages": self.languages,
            "media_type": self.media_type,
            "publisher": self.publisher,
            "type": self.type,
            "uri": self.uri,
        }

    def __str__(self) -> str:
        return str({
            "available_markets": self.available_markets,
            "name": self.name,
            "copyrights": self.copyrights,
            "description": self.description,
            "episodes": self.episodes,
            "explicit": self.explicit,
            "external_urls": self.external_urls,
            "href": self.href,
            "id": self.id,
            "images": self.images,
            "is_externally_hosted": self.is_externally_hosted,
            "languages": self.languages,
            "media_type": self.media_type,
            "publisher": self.publisher,
            "type": self.type,
            "uri": self.uri,
        })

    def merge_episodes(self, episode_dict: Dict[str, Any]) -> None:
        self.episodes["next"] = episode_dict["next"]
        self.episodes["href"] = episode_dict["href"]
        self.episodes["offset"] = episode_dict["offset"]
        id_list: List[str] = [ item["id"] for item in self.episodes["items"]]
        for item in episode_dict["items"]:
            if not (str(item["id"]) in id_list):
                self.episodes["items"].append(item)

    @staticmethod
    def load_from_json(json_dict: Dict[str, Any]) -> 'Podcast':
        return Podcast(json_dict["available_markets"], json_dict["name"], json_dict["copyrights"], json_dict["description"],
            json_dict["episodes"], json_dict["explicit"], json_dict["external_urls"],
            json_dict["href"], json_dict["id"],json_dict["images"], json_dict["is_externally_hosted"],
            json_dict["languages"], json_dict["media_type"], json_dict["publisher"],
            json_dict["type"], json_dict["uri"])