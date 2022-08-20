<template>
  <v-app>
    <v-main>
      <v-card
        
      >
          <div class="hader-wrap">
            <v-app-bar
              class="d-flex justify-space-around mb-6"
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
