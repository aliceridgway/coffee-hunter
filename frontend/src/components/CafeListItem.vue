<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
</script>

<template>
  <div class="px-0">
    <v-card class="cafe__thumbnail">
      <v-img
        src="https://images.unsplash.com/photo-1525648199074-cee30ba79a4a?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzMjM4NDZ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NjkyNDQ4MTc&ixlib=rb-4.0.3&q=80&w=400"
      />
    </v-card>
    <v-container class="d-flex justify-space-between">
      <h4 class="cafe__name">Cafe Name</h4>
      <small class="cafe__rating">4.3</small>
    </v-container>
  </div>
</template>

<style scoped>
.cafe .cafe__name {
  text-align: left;
}
.cafe__thumbnail {
  padding: 0;
}
</style>