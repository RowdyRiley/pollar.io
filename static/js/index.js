// This will be the object that will contain the Vue attributes
// and be used to initialize it.
let app = {};


// Given an empty app object, initializes it filling its attributes,
// creates a Vue instance, and then initializes the Vue instance.
let init = (app) => {

    // This is the Vue data.
    app.data = {
        // Complete as you see fit.
        //Contains all the database questions
        qa: [],
        //This should hold only a single question so it can be displayed to the user.
        single_qa: [],
    };

    app.enumerate = (a) => {
        // This adds an _idx field to each element of the array.
        let k = 0;
        a.map((e) => {e._idx = k++;});
        return a;
    };

    //This will go to the controller and gets the question database and sets it up in vue as well.
    app.get_qa = function () {
        axios.get(get_qa_url,).then(function (response) {
            app.enumerate(response.data.qa);
            app.vue.qa = response.data.qa;
        });
    };

    app.get_next_question = function () {
        console.log("GETTING NEXT QUESTION");
        axios.get(get_next_question_url,).then(function (response) {
            
            app.get_qa();
        });
    };
    
    // This contains all the methods.
    app.methods = {
        // Complete as you see fit.
        get_qa: app.get_qa,
        get_next_question: app.get_next_question,
        submitAnswer(qa_id, answer_id) {
            axios.post(submit_answer, {
                qa_id: qa_id,
                answer_id: answer_id,
            })
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
            });
        },
        
    };

    // This creates the Vue instance.
    app.vue = new Vue({
        el: "#vue-target",
        data: app.data,
        methods: app.methods
    });

    // And this initializes it.
    app.init = () => {
        // Put here any initialization code.
        // Typically this is a server GET call to load the data.
        app.get_qa();
        // app.get_next_question();
    };

    // Call to the initializer.
    app.init();
};

// This takes the (empty) app object, and initializes it,
// putting all the code i
init(app);

