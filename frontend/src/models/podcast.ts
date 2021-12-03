/* eslint-disable camelcase */

import { Episodes, Image } from './episodes'

/**
 * Interface representing podcast object in spotify.
 */
export interface PodcastInterface {
    available_markets: string[];

    name: string;

    copyrights: string[];

    description: string;

    episodes: Episodes;

    explicit: boolean;

    external_urls: { [key: string]: string };

    href: string;

    id: string;

    images: Image[];

    is_externally_hosted: boolean;

    languages: string[];

    media_type: string;

    publisher: string;

    type: string;

    uri: string;
}
export class Podcast implements PodcastInterface {
    readonly available_markets: string[];
    readonly name: string;
    readonly copyrights: string[];
    readonly description: string;
    readonly episodes: Episodes;
    readonly explicit: boolean;
    readonly external_urls: { [key: string]: string; };
    readonly href: string;
    readonly id: string;
    readonly images: Image[];
    readonly is_externally_hosted: boolean;
    readonly languages: string[];
    readonly media_type: string;
    readonly publisher: string;
    readonly type: string;
    readonly uri: string;

    constructor (available_markets: string[],
      name: string,
      copyrights: string[],
      description: string,
      episodes: Episodes,
      explicit: boolean,
      external_urls: { [key: string]: string; },
      href: string,
      id: string,
      images: Image[],
      is_externally_hosted: boolean,
      languages: string[],
      media_type: string,
      publisher: string,
      type: string,
      uri: string) {
      this.available_markets = available_markets
      this.name = name
      this.copyrights = copyrights
      this.description = description
      this.episodes = episodes
      this.explicit = explicit
      this.external_urls = external_urls
      this.href = href
      this.id = id
      this.images = images
      this.is_externally_hosted = is_externally_hosted
      this.languages = languages
      this.media_type = media_type
      this.publisher = publisher
      this.type = type
      this.uri = uri
    }
}
