module.exports = app => {
  // const tutorials = require("../controllers/stats.controller.js");

  const stats = require("../controllers/stats.controller.js");


  var router = require("express").Router();

  // Retrieve all Stats with condition
  router.get("/aircraft", stats.getAircraft);


  // Get post to run python script
  router.get("/python", stats.runPython);

  // Create and save form post 
  // router.post("/", stats.formPost);

  // // Retrieve all Tutorials
  // router.get("/", tutorials.findCondition);

  // // Retrieve all published Tutorials
  // router.get("/published", tutorials.findAllPublished);

  // // Retrieve a single Tutorial with id
  // router.get("/:id", tutorials.findOne);


  // // Update a Tutorial with id
  // router.put("/:id", tutorials.update);

  // // Delete a Tutorial with id
  // router.delete("/:id", tutorials.delete);

  // // Delete all Tutorials
  // router.delete("/", tutorials.deleteAll);

  app.use('/api/', router);
};
