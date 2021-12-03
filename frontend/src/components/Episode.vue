<template>

        <div class="container" >
          <nav class="navbar navbar-default sticky-top">
            <router-link :to="'/show/' + this.$route.query.show_id">Show episode list</router-link>

          </nav>

        <div v-if="ready" >
            <img :src=item.images[1].url />
        <h1>{{ item.name }}</h1>
        <p>{{ item.description }}</p>
        <p><a :href="item.external_urls['spotify']">Listen on spotify</a></p>
    </div>
    </div>
</template>
<script lang = "ts">
import { Item } from '@/models/episodes'
import axios from 'axios'
import Vue from 'vue'

interface EpisodeData {
    ready: boolean;
    item: Item | undefined;
}

interface Props {
    id: string;
}
export default Vue.extend<EpisodeData, unknown, unknown, Props>({
  name: 'Episode',
  data () {
    return {
      item: undefined,
      ready: false
    }
  },
  async mounted () {
    try {
      const resp = await axios.get<Item>('http://127.0.0.1:5000/v1/episode/'.concat(this.$props.id))
      if (resp.status === 200) {
        this.item = resp.data
      }
    } catch (err) {
      console.error('Error message: ' + (err as Error).message)
    } finally {
      this.ready = true
    }
  },
  props: {
    id: String
  }
})
</script>
