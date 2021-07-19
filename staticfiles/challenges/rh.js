let app = Vue.createApp({
    delimiters: [ '[%', '%]' ],
    
    data() {
        return {
            flag: "",
            nothingJustForWarning: "",



        };
    },

    mounted() {
        const headers = new Headers();
        headers.append("Allowed", "True");
        fetch(`../anotherRequest/`, { headers }) 
            .then(response => response.json())
            .then(json => {
                this.flag = json[0]['flag'];
                headers.append("SuperSecretAndSecurePassword", `${this.flag}`);
                fetch(`../passwordSecurity`, { headers })
                    .then(response => response.json())
                    .then(json => {
                });

            });
        




    },


    methods: {




    },







});

const vm1 = app.mount("#challenge");






//function sendHeader(flag) {
//    let xhr = new XMLHttpRequest();
//    
//
//
//    xhr.open("GET", '../passwordSecurity');
//    xhr.setRequestHeader("SuperSecureAndSecretPassword", flag);
//    xhr.send();
//}
