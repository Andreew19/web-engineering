<template>
  <v-app>
    <v-card
        
      >
          <div class="hader-wrap">
            <v-app-bar
              class="d-flex justify-space-around mb-6"
              height="98px"
              color="#fff"
              elevation="0"
              prominent
            >


              <h3 class="logo-title">logo</h3>
              <nav class="nav-bar">
                <router-link to="/">Проекты</router-link> 
                <router-link class="about" to="/about">Настройки</router-link>
              </nav>
              <router-view/>


             <div class="block-accaunt">
              <v-avatar
              class="avatat"
              color="primary"
              size="30"
              ></v-avatar>
              <h4>designer@arenda.mm</h4>
            </div> 

            </v-app-bar>
        </div>

      </v-card>
    <v-main>
      <div class="info-nav-project">
        <div class="nav-info">
          <p class="nav-pn">Название проекта</p> 
          <p class="vector">/</p>
          <p class="nav-ppn">Название страницы</p>
        </div>
        
      </div>
      <div class="wrapper">
        <h1 class="main-title">Добавить блок</h1>
        <div class="components-bar">
          <v-card
    class="mx-auto"
    max-width="344"
  >
    <v-img
      src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
      height="200px"
    ></v-img>

    <v-card-title>
      Top western road trips
    </v-card-title>

    <v-card-subtitle>
      1,000 miles of wonder
    </v-card-subtitle>

    <v-card-actions>
      <v-btn
        color="orange lighten-2"
        text
      >
        Explore
      </v-btn>

      <v-spacer></v-spacer>

      <v-btn
        icon
        @click="show = !show"
      >
        <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
          I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
        </div>
      </div>
      
    </v-main>
  </v-app>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #000;
    text-decoration: none;
    &.router-link-exact-active {
      border-bottom: 1px solid #000;
      
    }
  }
  .about{
    margin-left: 20px;
  }
}

main{
  margin-top: 50px;
}

.hader-wrap{
  .logo-title{
    margin-left: 30px;
  }
  .nav-bar{
     margin-left: 490px;
  }
  .block-accaunt{
    display: flex;
    margin-left: 1100px;
    
    position: fixed;
  }
  .avatat{
    margin-right: 12px;
  }

}
.info-nav-project{
  
  margin-top: 30px;
  height: 68px;
  background: #F9F9F9;
  .nav-info{
    margin-left: 26px;
    padding-top: 24px;
    display: flex;
    justify-content: space-between;
    width: 350px;
  }
}
.main-title{
  margin-top: 126px;
}

</style>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'App',

  data () {
    return {
      //
    }
  },
})
</script>
