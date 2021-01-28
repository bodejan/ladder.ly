<template>
  <v-app>
    <v-main>
      <v-container>
        <router-link to="/">Upload new files</router-link> |
        <router-link to="/about">About</router-link> | 
        <router-link to="/data">Data</router-link> | 
        <router-link to="/hvm">HVM</router-link>
        <router-view/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
</script>
