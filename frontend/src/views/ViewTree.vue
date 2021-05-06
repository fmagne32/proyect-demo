<template>
  <v-container>
    <v-container class="grey lighten-5">
      <v-container>
        <v-container>
          <v-row>
            <v-col cols="12" sm="6">
              <v-text-field
                v-model="formone.world"
                label="Value String"
                filled
              ></v-text-field>
            </v-col>

            <v-col cols="12" sm="6">
              <div>
                <pre><code>pre code {
  background-color: #eee;
  border: 1px solid #999;
  display: block;
  padding: 20px;
}
</code></pre>
              </div>

              <div>
                <v-text-field
                  v-model="result"
                  label="Resultado"
                  filled
                ></v-text-field>
              </div>
            </v-col>
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
              <v-btn rounded @click="submitproblemtree" color="success" dark
                >Submit
              </v-btn>
            </v-container>
          </v-row>
        </v-container>
      </v-container>
    </v-container>
  </v-container>
</template>

<script>
export default {
  name: "ProblemTree",
  data() {
    return {
      formone: {
        word: "",
      },
      result: 0,
    };
  },

  created() {},
  methods: {
    async submitproblemtree() {
      const data = JSON.parse(JSON.stringify(this.formone));
      await this.axios({
        method: "post",
        url: "laboratory/problemtree",
        data: data,
      })
        .then((res) => {
          if (res.status == 200) {
            const ResponseObtenido = res.data;
            if (ResponseObtenido.codigo == 0) {
              let mijson = ResponseObtenido.data;
              console.log(mijson);
              this.result = mijson;
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
