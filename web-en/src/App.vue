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
        <div class="component-bar d-flex justify-space-around mb-6 ">
            <v-card
          class="card-tool"
          color="#F5F5F5"
          max-width="344"
          outlined
          >
    <v-list-item three-line>
      <v-list-item-content>
        <div class="text-overline mb-4">
          <v-avatar
              class="avatar-tool"
              color="primary"
              size="50"
          >
            
          </v-avatar>
        </div>
        <v-list-item-title class="text-h5 mb-1">
          Изображение
        </v-list-item-title>
        
      </v-list-item-content>

      
    </v-list-item>

    
  </v-card>

  <v-card
          class="card-tool"
          color="#F5F5F5"
          max-width="344"
          outlined
          >
    <v-list-item three-line>
      <v-list-item-content>
        <div class="text-overline mb-4">
          <v-avatar
              class="avatar-tool"
              color="primary"
              size="50"
          >
            
          </v-avatar>
        </div>
        <v-list-item-title class="text-h5 mb-1">
          Текст
        </v-list-item-title>
        
      </v-list-item-content>

      
    </v-list-item>

    
  </v-card>

  <v-card
          class="card-tool"
          color="#F5F5F5"
          max-width="344"
          outlined
          >
    <v-list-item three-line>
      <v-list-item-content>
        <div class="text-overline mb-4">
          <v-avatar
              class="avatar-tool"
              color="primary"
              size="50"
          >
            
          </v-avatar>
        </div>
        <v-list-item-title class="text-h5 mb-1">
          Шаблоны
        </v-list-item-title>
        
      </v-list-item-content>

      

  

  
  
    </v-list-item>

    
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

.card-tool{
  width: 250px;
  height: 125px;
  border-radius: 30px;
}

.component-bar{
  margin-top: 52px;
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
