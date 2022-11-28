<script>
export default {
  //
};
</script>

<template>
  <v-app class="screen">
    <v-app-bar app shrink-on-scroll>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <router-link to="/"
        ><v-toolbar-title>Coffee Hunter</v-toolbar-title></router-link
      >
      <router-link to="/register"><v-btn>Register</v-btn></router-link>
      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main class="inner">
      <slot></slot>
    </v-main>
  </v-app>
</template>


<style scoped>
.screen {
  width: 100vw;
  min-height: 100vh;
  margin: 0;
  padding: 0;
}

.inner {
  width: 80%;
  max-width: 1600px;
  margin: 0 auto;
}
</style>