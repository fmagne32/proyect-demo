<template>
  <v-container>
    <v-container class="grey lighten-5">
      <v-container>
        <v-row>
          <v-container>
            <v-card class="mx-auto" tile>
              <v-list dense>
                <v-subheader class="text-h6">Padel</v-subheader>
                <div>
                  <v-row>
                    <v-container>
                      <v-col cols="12" sm="12">
                        <v-text-field
                          v-model="category"
                          label="Category"
                          filled
                          maxlength="16"
                        ></v-text-field>
                      </v-col>
                    </v-container>
                  </v-row>
                  <v-container>
                    <v-row>
                      <v-col cols="12" sm="3">
                        <v-text-field
                          v-model="subform.local.name"
                          label="Local Team"
                          filled
                          maxlength="16"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="2">
                        <v-text-field
                          v-model="subform.local.sets"
                          label="Sets"
                          filled
                          type="number"
                        ></v-text-field>
                      </v-col>

                      <v-col cols="12" sm="3">
                        <v-text-field
                          label="Visiting Team"
                          v-model="subform.visitant.name"
                          filled
                          maxlength="16"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="2">
                        <v-text-field
                          v-model="subform.visitant.sets"
                          label="Sets"
                          filled
                          type="number"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="2">
                        <br />
                        <v-btn rounded color="primary" dark @click="addteam"
                          >Add</v-btn
                        >
                      </v-col>
                    </v-row>
                  </v-container>
                </div>
                <v-container>
                  <v-list-item-group color="primary">
                    <v-list-item v-for="(item, i) in teams" :key="i">
                      <v-list-item-content>
                        <v-list-item-title
                          class="d-flex justify-center text-h6"
                          v-text="
                            `Local ${item.local.name} - Sets ${item.local.sets}, visitant ${item.visitant.name} - Sets ${item.visitant.sets} `
                          "
                        ></v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list-item-group>
                </v-container>
                <v-container>
                  <v-row>
                    <v-container>
                      <v-btn @click="addprelist" rounded color="primary" dark
                        >Add List</v-btn
                      >
                    </v-container>
                  </v-row>

                  <v-row>
                    <v-container>
                      <v-card class="mx-auto" max-width="600">
                        <v-toolbar flat color="deep-purple accent-4" dark>
                          <v-btn icon>
                            <v-icon>mdi-close</v-icon>
                          </v-btn>
                          <v-toolbar-title>Pre Teams</v-toolbar-title>
                        </v-toolbar>
                        <v-container>
                          <div>
                            <v-card-text
                              v-for="(item, i) in pre_teams"
                              :key="i"
                            >
                              <h2 class="title mb-2">
                                {{ item.name }}
                              </h2>
                              <v-divider :key="i"></v-divider>
                              <v-list-item-group color="primary">
                                <v-list-item
                                  v-for="(team, j) in item.teams"
                                  :key="j"
                                >
                                  <v-list-item-content>
                                    <v-list-item-title
                                      class="d-flex justify-center text-h6"
                                      v-text="
                                        `Local ${team.local.name} - Sets ${team.local.sets}, visitant ${team.visitant.name} - Sets ${team.visitant.sets} `
                                      "
                                    ></v-list-item-title>
                                  </v-list-item-content>
                                </v-list-item>
                              </v-list-item-group>
                            </v-card-text>
                          </div>
                        </v-container>
                      </v-card>
                    </v-container>
                  </v-row>

                  <v-row>
                    <h5>{{ message }}</h5>
                  </v-row>
                  <v-row>
                    <v-container>
                      <v-btn
                        rounded
                        @click="
                          $router.push({
                            name: 'Home',
                          })
                        "
                        color="primary"
                        dark
                        >Home</v-btn
                      >
                      <v-btn
                        @click="submitproblemone"
                        rounded
                        color="success"
                        dark
                        >Submit
                      </v-btn>
                    </v-container>
                  </v-row>
                </v-container>
              </v-list>
            </v-card>
          </v-container>
        </v-row>
      </v-container>
    </v-container>
  </v-container>
</template>

<script>
export default {
  name: "ProblemOne",
  data() {
    return {
      message: "",
      teams: [],
      pre_teams: [],
      category: "",
      subform: {
        local: {
          name: "",
          sets: 0,
        },
        visitant: {
          name: "",
          sets: 0,
        },
      },
    };
  },

  methods: {
    clear() {
      this.subform.local.name = "";
      this.subform.local.sets = 0;
      this.subform.visitant.name = "";
      this.subform.visitant.sets = 0;
    },
    clearpreteams() {
      this.category = "";
      this.teams = [];
    },
    addprelist() {
      console.log("click pre");
      const item = {
        name: this.category,
        teams: this.teams,
      };
      const myJSON = JSON.stringify(this.teams);
      console.log(myJSON);

      this.pre_teams.push(item);
      this.clearpreteams();
    },
    addteam() {
      const item = {
        local: {
          name: this.subform.local.name,
          sets: parseInt(this.subform.local.sets),
        },
        visitant: {
          name: this.subform.visitant.name,
          sets: parseInt(this.subform.visitant.sets),
        },
      };
      this.teams.push(item);
      this.clear();
    },
    async submitproblemone() {
      const data = JSON.parse(JSON.stringify(this.pre_teams));
      console.log("data enviado");
      const myJSON = JSON.stringify(data);
      console.log(myJSON);

      await this.axios({
        method: "post",
        url: "laboratory/problemone",
        data: data,
      })
        .then((res) => {
          if (res.status == 200) {
            const Response = res.data;
            if (Response.code == 0) {
              let json = Response.data;
              console.log(json);
              this.listado = json;
              this.message = JSON.stringify(json);
              this.$swal("Good job!", "", "success");
            } else {
              const icon = Response.code == 2 ? "warning" : "error";
              this.$swal("An error has occurred", Response.message, icon);
            }
          }
        })
        .catch((err) => {
          console.log("ERROR");
          console.log(err.response);
        });
    },
  },
};
</script>
