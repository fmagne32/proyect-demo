<template>
  <v-container>
    <v-container class="grey lighten-5">
      <v-row>
        <v-container>
          <v-subheader class="text-h6">Chess</v-subheader>
          <v-row>
            <v-col cols="12" sm="6">
              <v-text-field label="N" v-model="request.n" filled></v-text-field>
            </v-col>

            <v-col cols="12" sm="6">
              <v-text-field label="K" v-model="request.k" filled></v-text-field>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="12" sm="6">
              <v-text-field
                label="RQ"
                v-model="request.rq"
                filled
              ></v-text-field>
            </v-col>

            <v-col cols="12" sm="6">
              <v-text-field
                label="CQ"
                v-model="request.cq"
                filled
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-container>
              <v-card class="mx-auto" max-width="800" tile>
                <v-list dense>
                  <v-subheader>obstacle</v-subheader>
                  <div>
                    <v-container>
                      <v-row>
                        <v-col cols="12" sm="4">
                          <v-text-field
                            v-model="subform.row"
                            label="FO"
                            filled
                          ></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="4">
                          <v-text-field
                            v-model="subform.column"
                            label="CO"
                            filled
                          ></v-text-field>
                        </v-col>

                        <v-col cols="12" sm="4">
                          <v-btn
                            rounded
                            color="primary"
                            dark
                            @click="loadobstacle"
                            >Add</v-btn
                          >
                        </v-col>
                      </v-row>
                    </v-container>
                  </div>
                  <v-container>
                    <v-list-item-group color="primary">
                      <v-list-item v-for="(item, i) in obstacle" :key="i">
                        <v-list-item-content>
                          <v-list-item-title
                            v-text="`Row ${item.row} - Column ${item.column}`"
                          ></v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list-item-group>
                  </v-container>
                </v-list>
              </v-card>
            </v-container>
          </v-row>

          <div>
            <v-btn @click="ShowChess" rounded color="success" dark
              >Submit</v-btn
            >
          </div>

          <br />
          <br />
          <v-row>
            <v-container>
              <div v-if="chess.length">
                <h4>Queen's attack number is {{ attack }}</h4>
                <table style="width: 40%; height: 40%" class="chess-board">
                  <tbody>
                    <tr v-for="(item, index) in chess" :key="`chess-${index}`">
                      <td
                        class="light"
                        v-for="(itemx, indej) in item"
                        :key="`chessv2-${indej}`"
                        v-bind:style="{ 'background-color': itemx.color }"
                      >
                        <div>
                          <div v-if="itemx.detail.figure == 'Queen'">
                            <img
                              width="40"
                              height="40"
                              :src="itemx.detail.imageurl"
                            />
                          </div>
                          <div v-else-if="itemx.detail.figure === 'Available'">
                            <img
                              width="40"
                              height="40"
                              :src="itemx.detail.imageurl"
                            />
                          </div>
                          <div v-else-if="itemx.detail.figure === 'Obstacle'">
                            <img
                              width="40"
                              height="40"
                              :src="itemx.detail.imageurl"
                            />
                          </div>
                          <div v-else>
                            <span></span>
                          </div>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </v-container>
          </v-row>
        </v-container>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
export default {
  name: "ProblemTwo",
  data() {
    return {
      chess: [],
      attack: 0,
      subform: {
        row: 0,
        column: 0,
      },
      obstacle: [],
      request: {
        n: 0,
        k: 0,
        rq: 0,
        cq: 0,
        obstacle: [],
      },
    };
  },

  created() {},
  methods: {
    loadobstacle() {
      const item = {
        row: parseInt(this.subform.row),
        column: parseInt(this.subform.column),
      };
      this.obstacle.push(item);
      this.subform.row = 0;
      this.subform.column = 0;
    },
    async ShowChess() {
      this.request.obstacle = this.obstacle;
      const data = JSON.parse(JSON.stringify(this.request));
      await this.axios({
        method: "post",
        url: "laboratory/problemtwo",
        data: data,
      })
        .then((res) => {
          if (res.status == 200) {
            const Response = res.data;
            if (Response.code == 0) {
              let json = Response.data;
              this.chess = json.chess;
              this.attack = json.attack;
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
};
</script>

<style>
.chess-board {
  border-spacing: 0;
  border-collapse: collapse;
}
.chess-board th {
  padding: 0.5em;
}
.chess-board th + th {
  border-bottom: 1px solid #000;
}
.chess-board th:first-child,
.chess-board td:last-child {
  border-right: 3px solid #000;
}
.chess-board tr:last-child td {
  border-bottom: 3px solid;
}
.chess-board th:empty {
  border: none;
}
.chess-board td {
  width: 1.5em;
  height: 1.5em;
  text-align: center;
  font-size: 32px;
  line-height: 0;
  border: 3px solid #000;
}
</style>
