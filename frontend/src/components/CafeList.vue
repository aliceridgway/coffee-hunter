<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import CafeListItem from "./CafeListItem.vue";
</script>

<template>
  <v-container>
    <v-row>
      <v-col v-for="n in 24" :key="n" cols="4">
        <cafe-list-item />
      </v-col>
    </v-row>
  </v-container>
</template>