const app = Vue.createApp({
    
    delimiters: [ '[%', '%]' ],


    data() {
        return {
            someText: "This is a test",
            objectFromDatabase: null,
            dataLoading: true,
            databaseDataURL: `data/`,


        }

    },

    created() {
        this.objectsFromDatabase = this.getData();       



    },


    methods: {
        
        getData()  {
            fetch(this.databaseDataURL)
                .then(response => response.json())
                .then(json => {
                    this.objectFromDatabase = json;
                    this.dataLoading = false;
                    console.log(this.objectFromDatabase)
                });
        },


    },


});


const vm = app.mount('#challenges');
