const app = Vue.createApp({

  delimiters: [ '[%', '%]' ],


  data() {
      return {
          placeholder: "Text",
          isAdmin: false,
          isAdminText: "Admin: ",
          isNotLoaded: true,
          completedChallenges: null,
          completedRequiredChallenges: null,
          numChallenges: null,
          numRequiredChallenges: null,
          percentComplete: null,
      }
      


  },

  mounted() {
      if (this.$refs.admin.firstChild.data.toLowerCase() === 'false') {
          this.isAdmin = false;
          this.isAdminText = "User";
      } else {
          this.isAdmin = true;
          this.isAdminText = "Admin";
      }
      this.isNotLoaded = false;
      this.completedRequiredChallenges = this.$refs.completedRequiredChallenges.firstChild.data;
      this.completedChallenges = this.$refs.completedChallenges.firstChild.data;
      this.numChallenges = this.$refs.numChallenges.firstChild.data;
      this.numRequiredChallenges = this.$refs.numRequiredChallenges.firstChild.data;
      percentage = ((this.completedRequiredChallenges / this.numRequiredChallenges) * 100).toFixed(2)
      if (percentage > 100) {
          percentage = 100;
      }
      this.percentComplete = '' + percentage + '%';

  },


});


const vm = app.mount('#homepage');