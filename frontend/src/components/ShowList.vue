
<template>
<div>
<nav class="navbar navbar-expand-lg navbar-light bg-light sticky-top justify-content-center">
  <a class="navbar-brand" href="/">Home</a>
      <input class="form-control wd-50" type="search" placeholder="Search for episode" aria-label="Search" v-model="search" style="width: 50%">
  <div v-if="ready">
  <button v-if="podcastVal.episodes.items.length < podcastVal.episodes.total" v-on:click="updateEpisodeListAsync" class="btn btn-primary">Load more</button>
   </div>
  <div v-if="ready">
   <p>Loaded {{ podcastVal.episodes.items.length }} out of {{ podcastVal.episodes.total }} <br>
      Dispaying {{ filtered.episodes.items.length }} out of {{ podcastVal.episodes.items.length }} </p>
  </div>
</nav>
  <div class="container" v-if="ready">

    <h1 class="mt-2">{{ podcastVal.name }}</h1>
    <p>{{ podcastVal.description }}</p>
      <template v-for="(item, i) in filtered.episodes.items">
        <div class="container-fluid border border-secondary mt-2" :key="item.id + i">
          <h3 :key=item.id>
              <img :src="item.images.at(-1).url"/> <a :href="'\/episode\/' + item.id + '?' + 'show_id=' +  podcastVal.id"> {{ item.name }}</a>
          </h3>
          <h4> {{ displayDateString(item.release_date) }} </h4>
          <p class="w-50" style="word-wrap:break-word">{{ item.description }}</p>
        </div>
      </template>
      <!-- Only show 'load more' button if there are more episodes to be loaded -->
      <button v-if="podcastVal.episodes.items.length !== podcastVal.episodes.total" v-on:click="updateEpisodeListAsync" class="btn btn-primary">Load more</button>
  </div>
</div>
</template>

<script lang = "ts">
import Vue from 'vue'
import axios from 'axios'
import { Podcast } from '@/models/podcast'
import { loadMoreEpisodesAsync, mergeEpisodes } from '@/helpers/episodeHelper'
import { Episodes } from '@/models/episodes'
import { displayDateString } from '../helpers/dateHelper'

interface Props {
  id: string;
}

interface ShowListData {
  ready: boolean;
  podcastVal: Podcast | undefined;
  search: string;
}

export default Vue.extend<ShowListData, unknown, unknown, Props>({
  data () {
    return {
      ready: false,
      podcastVal: undefined,
      search: ''
    }
  },
  name: 'ShowList',
  async created () {
    try {
      const resp = await axios.get<Podcast>('http://127.0.0.1:5000/v1/show/'.concat(this.$props.id))
      if (resp.status === 200) {
        this.podcastVal = resp.data
      }
    } catch (err) {
      console.error('Error message: ' + (err as Error).message)
    } finally {
      this.ready = true
    }
  },
  props: {
    id: String
  },
  methods: {
    updateEpisodeListAsync: async function (): Promise<void> {
      try {
        // Check if podcast has been loaded
        if (this.podcastVal) {
          const episodes: Episodes = await loadMoreEpisodesAsync('http://127.0.0.1:5000/next', this.podcastVal)
          this.podcastVal = mergeEpisodes(this.podcastVal, episodes)
        } else {
          console.debug('No podcast loaded')
        }
      } catch (error) {
        console.error(error)
      }
    },
    displayDateString: displayDateString
  },
  computed: {
    filtered: function (): Podcast | undefined {
      if (this.search.length === 0) {
        return this.podcastVal
      } else if (this.search.length !== 0 && this.podcastVal) {
        const podcastfiltered = JSON.parse(JSON.stringify(this.podcastVal)) as Podcast
        // Filter the episodes based on the search string
        podcastfiltered.episodes.items = podcastfiltered.episodes.items.filter(x => {
          return x.name.toLocaleLowerCase().includes(this.search.toLocaleLowerCase()) || x.description.toLocaleLowerCase().includes(this.search.toLocaleLowerCase())
        })
        return podcastfiltered
      } else {
        return undefined
      }
    }
  },
  watch: {
    /**
    search: function (val: string): void {
      if (val.length === 0) {
        this.filtered = this.podcastVal
      } else if (val.length !== 0 && this.podcastVal) {
        this.filtered = JSON.parse(JSON.stringify(this.podcastVal)) as Podcast

        // Filter the episodes based on the search string
        this.filtered.episodes.items = this.filtered.episodes.items.filter(x => {
          return x.name.toLocaleLowerCase().includes(val.toLocaleLowerCase()) || x.description.toLocaleLowerCase().includes(val.toLocaleLowerCase())
        })
      }
      this.search = val
    },
    podcastVal: function (val: Podcast): void {
      this.podcastVal = val

      if (this.search.length === 0) {
        this.filtered = this.podcastVal
      } else if (this.search.length !== 0 && this.podcastVal) {
        this.filtered = JSON.parse(JSON.stringify(this.podcastVal)) as Podcast

        // Filter the episodes based on the search string
        this.filtered.episodes.items = this.filtered.episodes.items.filter(x => {
          return x.name.toLocaleLowerCase().includes(this.search.toLocaleLowerCase()) || x.description.toLocaleLowerCase().includes(this.search.toLocaleLowerCase())
        })
      }
    }
    **/
  }
})
</script>

<style>

</style>
