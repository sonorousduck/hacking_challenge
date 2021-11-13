const app = Vue.createApp({
    delimiters: ['[%', '%]' ],


    data() {
        return {
            time: null,
            date: null,
            notLoaded: true,
            unreadEmails: 1,
            clockInPopupInvisible: true,
            emailPopupInvisible: true,
            composePopupInvisible: true,
        }


    },

    created() {
        setInterval(this.getTime, 1000);

    },

    methods: {
        getTime: function() {
            const today = new Date();
            const date = (today.getMonth() + 1) + '/' + (today.getDate()) + '/' + (today.getFullYear());
            let time = ''



            if (today.getMinutes() < 10) {
                minutes = "0" + today.getMinutes();
            } else {
                minutes = today.getMinutes();
            }
            if (today.getSeconds() < 10) {
                seconds = "0" + today.getSeconds()
                time = today.getHours() + ":" + minutes + ":" + seconds;
            } else {
                time = today.getHours() + ":" + minutes + ":" + today.getSeconds();
            }
            this.time = time;
            this.date = date;

            if (this.notLoaded === true) {
                this.notLoaded = false;
            }
        },

        clockIn: function() {
            console.log("Weird. You aren't in our employee database. This seems to be a mistake")
            this.clockInPopupInvisible = !this.clockInPopupInvisible;

        },

        email: function() {
            console.log("Email! Email!")
            
            if (this.clockInPopupInvisible && this.composePopupInvisible) {
                this.emailPopupInvisible = !this.emailPopupInvisible;
                this.unreadEmails = 0;
            }
        },

        composeEmail: function() {
            console.log("Compose! Compose!");
            if (this.emailPopupInvisible === false) {
                this.emailPopupInvisible = !this.emailPopupInvisible;
            }
        
            this.composePopupInvisible = !this.composePopupInvisible;
            


        },
        
    },

});

const vm = app.mount("#mainContent")
