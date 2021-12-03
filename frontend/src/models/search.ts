import { PodcastInterface } from './podcast'
/**
 *
 */
export interface ShowsResultsInterface {
    href: string;
    items: PodcastInterface[];
    limit: number;
    next: string;
    offset: number;
    previous: string | null;
    total: number
}

/**
 * Search results from spotify API.
 */
export interface SearchResultsInterface {
    shows: ShowsResultsInterface;
}

/**
 * Search Result class used in component implements SearchResultsInterface
 */
export class SearchResults implements SearchResultsInterface {
    readonly shows: ShowsResultsInterface;
    constructor (shows: ShowsResultsInterface) {
      this.shows = shows
    }
}
