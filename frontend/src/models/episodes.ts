/* eslint-disable camelcase */

/**
 * Represents the image object sent by spotify.
 */
export interface Image {
    height: number;
    url: string;
    width: number;
}

/**
 * Individual episode.
 */
export interface Item {
    /**
     * Audio preview url.
     */
    audio_preview_url: string;
    description: string;
    duration_ms: number;
    external_urls: { [key: string]: string };
    href: string;
    id: string;
    images: Image[];
    is_externally_hosted: boolean;
    language: string;
    name: string;
    release_date: string;
    release_date_precision: string;
    type: string;
    uri: string;
}

/**
 * Represents the list of episodes for a given
 * podcast in spotify.
 */
export interface Episodes {
    href: string;
    items: Item[];
    limit: number;
    next: string;
    offset: number;
    previous?: string;
    total: number;
}
