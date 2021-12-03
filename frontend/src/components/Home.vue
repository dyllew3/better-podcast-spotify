<template>
<div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light sticky-top justify-content-center">
  <a class="navbar-brand" href="/">Home</a>
</nav>

    <form class="container">
    <div class="form-group">
        <label for="searchShows">Search for a show</label>
        <input type="search" class="form-control" id="searchShows" aria-describedby="searchShow" placeholder="Enter show name" v-model="search">
    </div>
    </form>

  <div class="container" v-if="searchResult !== null">
      <template v-for="item in searchResult.shows.items">
        <div class="container-fluid border border-secondary mt-2" :key=item.id>
          <h3 :key=item.id>
             <img :src="item.images.at(-1).url"/> <a :href="'\/show\/' + item.id"> {{ item.name }}</a>
          </h3>
          <p class="w-50" style="word-wrap:break-word">{{ item.description }}</p>
        </div>
      </template>
      <!-- Only show 'load more' button if there are more episodes to be loaded -->
  </div>
</div>
</template>

<script lang="ts">
import { SearchResults } from '@/models/search'
import axios from 'axios'
import Vue from 'vue'

interface HomeData {
    search: string;
    searchResult: SearchResults | null;
}

export default Vue.extend<HomeData, unknown, unknown, unknown>({
  data (): HomeData {
    return {
      search: '',
      searchResult: null
    }
  },
  methods: {
  },
  name: 'Home',
  watch: {
    search: async function (val: string): Promise<void> {
      this.search = val
      if (this.search.length !== 0) {
        const response = await axios.get<SearchResults>('http://127.0.0.1:5000/search?name='.concat(val))
        if (response.status === 200) {
          this.searchResult = response.data
          console.log(this.searchResult.shows.items.length)
        }
      }
    }
  }
})
</script>

<style>

</style>
