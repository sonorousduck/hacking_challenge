const app = Vue.createApp({
    
    delimiters: [ '[%', '%]' ],


    data() {
        return {
            someText: "This is a test",
            challengesFromDatabase: null,
            databaseChallengesLocation: 'getChallenges',
            isCompleted: false,
            isLocked: false,
            navigation: 'navigateToChallenge',

        }

    },

    created() {
        this.challengesFromDatabase = this.getChallenges();


    },


    methods: {
        getChallenges() {
            fetch(this.databaseChallengesLocation)
                .then(response => response.json())
                .then(json => {
                    this.challengesFromDatabase = json;
                });
        },

        goToChallenge(event) {
            console.log(event.currentTarget.id);
            fetch(this.navigation, {challenge: 'event.currentTarget.id'})



        },


    },


});


const vm = app.mount('#challenges');
