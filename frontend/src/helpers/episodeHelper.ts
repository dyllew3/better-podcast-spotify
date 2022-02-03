import axios from 'axios'
import { Episodes } from '../models/episodes'
import { Podcast } from '../models/podcast'

/**
 * loadMoreEpisodesAsync
 * @param {string} url url to send load the next list of episodes.
 * @param {Podcast} podcast podcast to request more episodes of.
 * @returns {Promises<Episodes>} The next episode interface.
 * @throws Throws an exception when the data can't be parsed
 */
export async function loadMoreEpisodesAsync (url: string, podcast: Podcast): Promise<Podcast> {
  const response = await axios.post<Podcast>(url, podcast)
  if (response.status === 200) {
    // Check if data is valid
    if (!response.data) {
      throw new Error('Unknown data given: '.concat(JSON.stringify(response.data as unknown)))
    }
    return response.data
  } else {
    throw new Error('unable to get data from '.concat(url))
  }
}

/**
 * mergeEpisodes
 * @param podcast Podcast to add episode to.
 * @param moreEps More episodes to add.
 * @returns
 */
export function mergeEpisodes (podcast: Podcast, moreEps: Episodes): Podcast {
  podcast.episodes.next = moreEps.next
  podcast.episodes.href = moreEps.href
  podcast.episodes.offset = moreEps.offset
  podcast.episodes.items = podcast.episodes.items.concat(moreEps.items)
  return podcast
}
