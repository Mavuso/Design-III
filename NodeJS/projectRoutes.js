let todoList = [];
let express = require("express")
let projectRouter = express.Router();
let path = require("path")

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