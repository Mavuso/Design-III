let todoList = [];
let express = require("express")
let projectRouter = express.Router();
let path = require("path")
let bodyParser = require("body-parser");
let query_firestore = require('./get_data.js')


//dataRouter.use(bodyParser.urlencoded({ extended: true }));

projectRouter.get('/get_data', function (req, res) {
    console.log("BODY");
    query_firestore(res)
    //res.sendFile(path.join(__dirname,'/pages/','index.html'));
});

projectRouter.get('/',function(req,res){
    console.log("Testing get home")
    res.sendFile(path.join(__dirname,'/pages/','index.html'));
});


projectRouter.get('/create',function(req,res){
    res.sendFile(path.join(__dirname,'/pages','create.html'));
});

projectRouter.get('/delete',function(req,res){
    res.sendFile(path.join(__dirname,'/pages','delete.html'));
});

projectRouter.get('/edit',function(req,res){
    res.sendFile(path.join(__dirname,'/pages','edit.html'));
});

module.exports = projectRouter;