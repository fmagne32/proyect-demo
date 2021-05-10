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
                          v-model.trim="category"
                          label="Category"
                          filled
                          :counter="16"
                          :error-messages="nameCategoryErrors"
                          @input="$v.category.$touch()"
                          @blur="$v.category.$touch()"
                        ></v-text-field>
                      </v-col>
                    </v-container>
                  </v-row>
                  <v-container>
                    <v-row>
                      <v-col cols="12" sm="3">
                        <v-text-field
                          v-model.trim="subform.local.name"
                          label="Local Team"
                          filled
                          :counter="16"
                          :error-messages="namelocalErrors"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="2">
                        <v-text-field
                          v-model.number="subform.local.sets"
                          label="Sets"
                          filled
                          type="number"
                          :error-messages="setlocalErrors"
                          @input="$v.subform.local.sets.$touch()"
                          @blur="$v.subform.local.sets.$touch()"
                        ></v-text-field>
                      </v-col>

                      <v-col cols="12" sm="3">
                        <v-text-field
                          label="Visiting Team"
                          v-model.trim="subform.visitant.name"
                          filled
                          :counter="16"
                          :error-messages="namevisitantErrors"
                          @input="$v.subform.visitant.name.$touch()"
                          @blur="$v.subform.visitant.name.$touch()"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="2">
                        <v-text-field
                          v-model.number="subform.visitant.sets"
                          label="Sets"
                          filled
                          type="number"
                          :error-messages="setvisitantErrors"
                          @input="$v.subform.visitant.sets.$touch()"
                          @blur="$v.subform.visitant.sets.$touch()"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="2">
                        <br />

                        <v-btn
                          @click="addteam"
                          :disabled="$v.validationGroup.$invalid"
                        >
                          Add
                        </v-btn>
                      </v-col>
                    </v-row>
                  </v-container>
                </div>
                <v-container>
                  <v-card class="mx-auto" max-width="600">
                    <v-toolbar flat color="deep-purple accent-4" dark>
                      <v-btn icon>
                        <v-icon>mdi-close</v-icon>
                      </v-btn>
                      <v-toolbar-title
                        >Team Category {{ category }}</v-toolbar-title
                      >
                    </v-toolbar>
                    <v-alert v-if="team_required" type="error">
                      <span>{{ msg_team }}</span>
                    </v-alert>
                    <v-card-text>
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
                    </v-card-text>
                  </v-card>
                </v-container>
                <v-container>
                  <v-row>
                    <v-container>
                      <v-btn
                        :disabled="existeam"
                        @click="addprelist"
                        rounded
                        color="primary"
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
                          <v-alert v-if="pre_teams_required" type="error">
                            <span>{{ msg_pre_teams }}</span>
                          </v-alert>
                          <div>
                            <v-card-text
                              v-for="(item, i) in pre_teams"
                              :key="i"
                            >
                              <div>
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
                              </div>
                            </v-card-text>
                          </div>
                        </v-container>
                      </v-card>
                    </v-container>
                  </v-row>

                  <v-row v-if="detail.length">
                    <v-container>
                      <v-card class="mx-auto" max-width="900">
                        <v-toolbar flat color="blue accent-4" dark>
                          <v-btn icon>
                            <v-icon>mdi-close</v-icon>
                          </v-btn>
                          <v-toolbar-title>Response</v-toolbar-title>
                        </v-toolbar>
                        <v-container>
                          <div>
                            <v-card-text v-for="(item, i) in detail" :key="i">
                              <h3 class="title mb-2">
                                {{ item.category }}
                              </h3>
                              <v-divider :key="i"></v-divider>

                              <v-list-item>
                                <v-list-item-content>
                                  <v-list-item-title
                                    ><h2>Team {{ item.team }}</h2>
                                  </v-list-item-title>
                                </v-list-item-content>
                              </v-list-item>
                              <v-list-item>
                                <v-list-item-content>
                                  <v-list-item-title>
                                    <div v-if="item.tie"><h3>Tie</h3></div>
                                    <div v-else><h3>Tie 0</h3></div>
                                  </v-list-item-title>
                                </v-list-item-content>
                              </v-list-item>

                              <div>
                                <h3>Stadistic</h3>
                                <pre data-enlighter-language="json">
                                {{ item.stadistic }}
                                </pre>
                              </div>
                              <h5>{{ item.message }}</h5>
                            </v-card-text>
                          </div>
                        </v-container>
                      </v-card>
                    </v-container>
                  </v-row>

                  <v-row>
                    <v-container>
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
import {
  required,
  numeric,
  maxLength,
  between,
} from "vuelidate/lib/validators";

export default {
  name: "ProblemOne",
  data() {
    return {
      team_required: false,
      pre_teams_required: false,
      msg_team: "team required",
      msg_pre_teams: "list detail team required",
      message: "",
      teams: [],
      pre_teams: [],
      category: "",
      detail: [],
      notshow: false,
      subvalidate: {
        local: false,
        setl: false,
        visitant: false,
        setv: false,
      },
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
  validations: {
    subform: {
      local: {
        name: {
          required,
          maxLength: maxLength(16),
        },
        sets: {
          numeric,
          required,
          between: between(0, 30),
        },
      },
      visitant: {
        name: {
          required,
          maxLength: maxLength(16),
        },
        sets: {
          numeric,
          required,
          between: between(0, 30),
        },
      },
    },
    category: {
      required,
      maxLength: maxLength(16),
    },
    pre_teams: {
      required,
    },
    validationGroup: ["category", "subform"],
  },
  computed: {
    nameCategoryErrors() {
      const errors = [];
      if (!this.$v.category.$dirty) return errors;
      !this.$v.category.maxLength &&
        errors.push("Name category must be at most 16 characters long");
      !this.$v.category.required && errors.push("Name category is required.");
      return errors;
    },
    namelocalErrors() {
      const errors = [];
      if (!this.$v.subform.local.name.$dirty) return errors;
      !this.$v.subform.local.name.maxLength &&
        errors.push("Name local must be at most 16 characters long");
      !this.$v.subform.local.name.required &&
        errors.push("Name local is required.");
      return errors;
    },
    setlocalErrors() {
      const errors = [];
      if (!this.$v.subform.local.sets.$dirty) return errors;
      if (!this.$v.subform.local.sets.between) {
        errors.push(
          `Must be between  ${this.$v.subform.local.sets.$params.between.min} and ${this.$v.subform.local.sets.$params.between.max}`
        );
      }
      if (!this.$v.subform.local.sets.required) {
        errors.push("sets local is required.");
      }

      return errors;
    },

    namevisitantErrors() {
      const errors = [];
      if (!this.$v.subform.visitant.name.$dirty) return errors;
      !this.$v.subform.visitant.name.maxLength &&
        errors.push("Name visitant must be at most 16 characters long");
      !this.$v.subform.visitant.name.required &&
        errors.push("Name visitant is required.");

      return errors;
    },
    setvisitantErrors() {
      const errors = [];
      if (!this.$v.subform.visitant.sets.$dirty) return errors;
      if (!this.$v.subform.visitant.sets.between) {
        errors.push(
          `Must be between  ${this.$v.subform.visitant.sets.$params.between.min} and ${this.$v.subform.visitant.sets.$params.between.max}`
        );
      }
      if (!this.$v.subform.visitant.sets.required) {
        errors.push("sets visitant is required.");
      }
      return errors;
    },

    preListTeamErrors() {
      const errors = [];
      if (!this.$v.pre_teams.required) {
        errors.push("sets visitant is required.");
      }
      return errors;
    },

    existeam() {
      return this.teams.length === 0;
    },
    existe_preteam() {
      return this.pre_teams.length === 0;
    },
  },
  methods: {
    clear() {
      this.subform.local.name = "";
      this.subform.local.sets = 0;
      this.subform.visitant.name = "";
      this.subform.visitant.sets = 0;
      this.$v.subform.$reset();
    },
    clearpreteams() {
      this.category = "";
      this.teams = [];
      this.$v.category.$reset();
    },
    addprelist() {
      const item = {
        name: this.category,
        teams: this.teams,
      };
      this.pre_teams.push(item);
      this.clearpreteams();
    },
    addprelistv2() {
      this.$v.pre_teams.$touch();
    },
    addteam() {
      if (
        parseInt(this.subform.local.sets) ===
        parseInt(this.subform.visitant.sets)
      ) {
        this.$swal(
          "An error has occurred",
          "tie match is not allowed",
          "warning"
        );
        this.$v.$reset;
        return;
      }
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

    prevalidate() {
      var count = 0;

      if (this.pre_teams.length == 0) {
        if (this.$v.category.$invalid && this.teams.length == 0) {
          this.$v.category.$touch();
          count++;
        }

        if (this.$v.subform.$invalid && this.teams.length == 0) {
          this.$v.subform.$touch();
          count++;
        }
        if (this.teams.length == 0) {
          this.team_required = true;
          count++;
        }
        if (this.pre_teams.length == 0) {
          this.pre_teams_required = true;
          count++;
        }
        if (this.team_required) {
          count++;
        }
        if (this.pre_teams_required) {
          count++;
        }
      } else {
        this.$v.category.$reset();
        this.$v.subform.$reset();
        this.pre_teams_required = false;
      }

      return count;
    },
    async submitproblemone() {
      const info = this.prevalidate();
      if (info > 0) {
        return;
      }
      const data = JSON.parse(JSON.stringify(this.pre_teams));

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
              this.detail = json;
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
          this.$swal("An error has occurred Js", "", "error");
        });
    },
  },

  watch: {
    pre_teams: {
      deep: true,
      handler(value) {
        if (value.length == 0) {
          this.pre_teams_required = true;
        } else if (value.length > 0) {
          this.team_required = false;
          this.pre_teams_required = false;
        }
      },
    },

    teams: {
      deep: true,
      handler(value) {
        if (value.length == 0) {
          if (this.pre_teams.length > 0) {
            this.team_required = false;
          } else {
            this.team_required = true;
          }
        } else if (value.length > 0) {
          this.team_required = false;
        }
      },
    },
  },
};
</script>
