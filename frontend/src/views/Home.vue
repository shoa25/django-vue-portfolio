<template>
  <div class="home">
    <Navbar/>
    <hero-section/>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from '@/components/Navbar.vue'
import HeroSection from '@/components/HeroSection.vue'

export default {
  name: 'Home',
  components: {
    Navbar,
    HeroSection
  }
}
</script>

<style scoped>

</style>
