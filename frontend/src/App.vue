<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-app-bar-nav-icon
        @click.stop="sidebarMenu = !sidebarMenu"
      ></v-app-bar-nav-icon>
      <div>App Proyect Demo</div>
      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/fmagne32/proyect-demo"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release Github</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer
      v-model="sidebarMenu"
      app
      floating
      :permanent="sidebarMenu"
      :mini-variant.sync="mini"
    >
      <v-list dense color="primary" dark>
        <v-list-item>
          <v-list-item-action>
            <v-icon @click.stop="sidebarMenu = !sidebarMenu"
              >mdi-chevron-left</v-icon
            >
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>
              <h3 class="font-weight-thin">Vuetify Dashboard</h3>
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-list-item class="px-2" @click="toggleMini = !toggleMini">
        <v-list-item-avatar>
          <v-icon>mdi-account-outline</v-icon>
        </v-list-item-avatar>
        <v-list-item-content class="text-truncate">
          Fernando Magne
        </v-list-item-content>
        <v-btn icon small>
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
      </v-list-item>
      <v-divider></v-divider>
      <v-list>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
          :to="item.href"
        >
          <v-list-item-icon>
            <v-icon color="primary">{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title class="primary--text">{{
              item.title
            }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <v-container class="px-4 py-0 fill-height" fluid>
        <v-row class="fill-height">
          <v-col>
            <transition name="fade">
              <router-view></router-view>
            </transition>
          </v-col>
        </v-row>
      </v-container>
      <!--  <router-view />-->
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    drawer: false,
    sidebarMenu: true,
    toggleMini: false,
    items: [
      { title: "Home", href: "/", icon: "mdi-home-outline" },
      {
        title: "Problem One",
        href: "/problem-one",
        icon: "mdi-shield-account",
      },
      { title: "Problem Two", href: "/problem-two", icon: "mdi-bus-clock" },
      {
        title: "Problem Tree",
        href: "/problem-tree",
        icon: "mdi-apps-box",
      },
      {
        title: "About",
        href: "/about",
        icon: "mdi-reorder-horizontal",
      },
    ],
  }),
  methods: {
    name() {},
  },
  computed: {
    mini: {
      get() {
        return this.$vuetify.breakpoint.smAndDown || this.toggleMini;
      },
      set(value) {
        this.toggleMini = value;
      },
    },
    /*mini() {
     
     return this.$vuetify.breakpoint.smAndDown || this.toggleMini;
    },*/
  },
};
</script>
