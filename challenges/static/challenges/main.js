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


    },


    methods: {

        goToChallenge(event) {
            console.log(event.currentTarget.id);
            fetch(this.navigation, {challenge: 'event.currentTarget.id'})



        },


    },


});


const vm = app.mount('#challenges');
