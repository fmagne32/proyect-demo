<template>
  <v-container>
    <v-container class="grey lighten-5">
      <v-container>
        <v-container>
          <v-row>
            <v-col cols="12" sm="6">
              <v-text-field
                v-model="world"
                label="Value String"
                filled
              ></v-text-field>
            </v-col>

            <v-col cols="12" sm="6">
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
      world: "",
      result: 0,
    };
  },

  created() {},
  methods: {
    async submitproblemtree() {
      await this.axios({
        method: "post",
        url: `laboratory/problemtree/${this.world}`,
      })
        .then((res) => {
          if (res.status == 200) {
            const Response = res.data;
            if (Response.code == 0) {
              let json = Response.data;
              this.result = json;
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
