const app = Vue.createApp({
    delimiters: ['[%', '%]' ],


    data() {
        return {
            time: null,
            date: null,
            notLoaded: true,

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
            if (today.getSeconds() < 10) {
                seconds = "0" + today.getSeconds()
                time = today.getHours() + ":" + today.getMinutes() + ":" + seconds;
            } else {
                time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
            }
            this.time = time;
            this.date = date;

            if (this.notLoaded === true) {
                this.notLoaded = false;
            }
        }
    },

});

const vm = app.mount("#mainContent")
