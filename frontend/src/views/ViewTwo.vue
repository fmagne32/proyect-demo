<template>
  <v-container>
    <v-container class="grey lighten-5">
      <v-row>
        <v-btn rounded color="primary" dark>Prueba</v-btn>

        <v-container>
          <v-row>
            <v-col cols="12" sm="6">
              <v-text-field
                label="N"
                v-model="formulario.n"
                filled
              ></v-text-field>
            </v-col>

            <v-col cols="12" sm="6">
              <v-text-field
                label="K"
                v-model="formulario.k"
                filled
              ></v-text-field>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="12" sm="6">
              <v-text-field
                label="RQ"
                v-model="formulario.rq"
                filled
              ></v-text-field>
            </v-col>

            <v-col cols="12" sm="6">
              <v-text-field
                label="CQ"
                v-model="formulario.cq"
                filled
              ></v-text-field>
            </v-col>
          </v-row>
        </v-container>
        <v-btn @click="MostrarAjedrez" rounded color="primary" dark>Show</v-btn>

        <div>
          listado

          <table class="chess-board">
            <tbody>
              <tr v-for="(item, index) in listado" :key="`chess-${index}`">
                <td
                  class="light"
                  v-for="(itemx, indej) in item"
                  :key="`chessv2-${indej}`"
                  v-bind:style="{ 'background-color': itemx.color }"
                >
                  <div>
                    <div v-if="itemx.detalle.figura == 'Reina'">
                      <img
                        width="40"
                        height="40"
                        :src="itemx.detalle.imageurl"
                      />
                    </div>
                    <div v-else-if="itemx.detalle.figura === 'Disponible'">
                      <img
                        width="30"
                        height="30"
                        :src="itemx.detalle.imageurl"
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
        <div>
        
        </div>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
export default {
  name: "ProblemTwo",
  data() {
    return {
      listado: [],
      formulario: {
        n: 0,
        k: 0,
        rq: 0,
        cq: 0,
        obstaculo: [
          {
            fila: 0,
            columna: 0,
          },
        ],
      },
    };
  },

  created() {},
  methods: {
    async MostrarAjedrez() {
      const data = JSON.parse(JSON.stringify(this.formulario));
      console.log("data enviado");
      console.log(data);
      await this.axios({
        method: "post",
        url: "laboratory/problemtwo",
        data: data,
      })
        .then((res) => {
          if (res.status == 200) {
            const ResponseObtenido = res.data;
            if (ResponseObtenido.codigo == 0) {
              let mijson = ResponseObtenido.data;
              console.log(mijson);
              this.listado = mijson;
              this.$swal("Good job!", "d", "success");
            } else if (ResponseObtenido.codigo == 1) {
              this.$swal(
                "Ha Ocurrido Error",
                ResponseObtenido.mensaje,
                "error"
              );
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
  border-right: 1px solid #000;
}
.chess-board tr:last-child td {
  border-bottom: 1px solid;
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
}
.chess-board .light {
  background: #eee;
}
.chess-board .dark {
  background: #aaa;
}
</style>
