let todoList = [];
let express = require("express")
let projectRouter = express.Router();
let path = require("path")
let bodyParser = require("body-parser");
let query_firestore = require('./get_data.js')

projectRouter.use(bodyParser.urlencoded({ extended: true }));


projectRouter.post('/get_data', function (req, res) {
    console.log("Testing");
    console.log(req.body);
    //query_firestore(res)
    //res.sendFile(path.join(__dirname,'/pages/','index.html'));
});

projectRouter.get('/',function(req,res){
    console.log("Testing get home")
    res.sendFile(path.join(__dirname,'/pages/','index.html'));
});

projectRouter.post('/create',function(req,res){    
    let graph_options = (req.body);
    query_firestore(graph_options,res)
    console.log(graph_options);
    //res.sendFile(path.join(__dirname,'/pages','create.html'));
});

projectRouter.get('/delete',function(req,res){
    res.sendFile(path.join(__dirname,'/pages','delete.html'));
});

projectRouter.get('/edit',function(req,res){
    res.sendFile(path.join(__dirname,'/pages','edit.html'));
});

module.exports = projectRouter;